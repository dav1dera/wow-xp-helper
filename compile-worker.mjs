/* WoW XP Helper segmented compiler: one conversion, small WebAssembly compiles. */
const BASE = new URL("./converter/", import.meta.url).href;
const tell=(type,props={})=>self.postMessage({type,...props});
const LIMIT=32;
const ORDER=["horde-main","alliance-main","both-main","horde-dungeon","alliance-dungeon","both-dungeon","horde-survival","alliance-survival","both-survival"];
function segments(guides){
  const map=new Map();
  for(const g of guides){
    const faction=(/^faction (Horde|Alliance)\s*$/mi.exec(g.text)||[])[1]?.toLowerCase()||"both";
    const route=["main","dungeon","survival"].includes(g.route)?g.route:"main";
    const key=faction+"-"+route;
    if(!map.has(key))map.set(key,[]);
    map.get(key).push(g);
  }
  const groups=[];
  for(const key of [...map.keys()].sort((a,b)=>ORDER.indexOf(a)-ORDER.indexOf(b))){
    const list=map.get(key),count=Math.ceil(list.length/LIMIT);
    for(let i=0;i<count;i++)groups.push({key,index:i+1,count,guides:list.slice(i*LIMIT,(i+1)*LIMIT),code:ORDER.indexOf(key)+1});
  }
  return groups;
}
function groupName(group){
  const [faction,route]=group.key.split("-");
  const side={horde:"Horde",alliance:"Alliance",both:"Entrambe"}[faction];
  const type={main:"Speedrun",dungeon:"Dungeon",survival:"Survival"}[route];
  return side+" - "+type+(group.count>1?" "+group.index+"/"+group.count:"");
}
function guideText(g,sourceId,packId,members,stats){
  const old="guide "+sourceId+"/"+g.slug+"\n";
  if(!g.text.startsWith(old))throw Error("Guida RXP senza intestazione attesa: "+g.slug);
  return g.text.replace(old,"guide "+packId+"/"+g.slug+"\n").replace(/^next ([^\r\n]+)\r?$/gm,(_line,raw)=>{
    const keep=[];
    for(const full of raw.split(/,\s*/)){
      const slug=full.startsWith(sourceId+"/")?full.slice(sourceId.length+1):"";
      if(slug&&members.has(slug))keep.push(packId+"/"+slug);
      else stats.interpack++;
    }
    return keep.length?"next "+keep.join(", "):"";
  });
}
async function compile({files,options,includeEntries}){
  tell("phase",{text:"Caricamento convertitore e dati Polestar…",progress:67});
  const [dm,nm,cm,bm,pm,am,zm,wasm]=await Promise.all([
    import(BASE+"src/data.mjs"),import(BASE+"src/journey/names.mjs"),
    import(BASE+"src/core.mjs"),import(BASE+"src/build.mjs"),
    import(BASE+"src/pack.mjs"),import(BASE+"src/addon.mjs"),
    import(BASE+"src/zip.mjs"),import(BASE+"forge/polestar_convert_wasm.js")
  ]);
  await wasm.default({module_or_path:BASE+"forge/polestar_convert_wasm_bg.wasm"});
  const virt=new Map(files);
  const root=BASE+"polestar-data/";
  const manifestResponse=await fetch(root+"manifest.json");
  if(!manifestResponse.ok)throw Error("Dati Polestar non disponibili (HTTP "+manifestResponse.status+")");
  const manifest=await manifestResponse.json();
  const paths=new Set(manifest.files||[]);
  const cache=new Map();
  const readData=async p=>{
    if(!paths.has(p))return null;
    if(!cache.has(p))cache.set(p,fetch(root+p).then(async r=>{
      if(!r.ok)throw Error("Dato mancante: "+p+" HTTP "+r.status);
      return r.text();
    }));
    return cache.get(p);
  };
  tell("phase",{text:"Conversione guide RestedXP…",progress:69});
  const data=await dm.loadData(readData);
  const names=await nm.loadNames(readData,data,manifest.levelXp);
  const runs=await cm.convertAddons(p=>Promise.resolve(virt.get(p.toLowerCase())??null),data,names,{
    packId:options.id,sources:["rxp"],routes:options.routes,
    progress:src=>tell("log",{text:"Conversione "+src})
  });
  const run=runs.rxp;
  if(!run?.guides?.length)throw Error("Nessuna guida convertibile dalla cache RestedXP.");
  const parts=segments(run.guides);
  tell("log",{text:"Guide riconosciute: "+run.guides.length+". Compilazione in "+parts.length+" pacchetti più piccoli (massimo "+LIMIT+" guide)."});
  const coreTexts={};
  for(const n of dm.COMPILER_NAMES){
    const t=await readData("data/forever/"+n+".json");
    if(t!=null)coreTexts[n]=t;
  }
  const library=JSON.stringify(coreTexts);
  const [instances,areas,spells]=await Promise.all([
    readData("tables/instances.json"),readData("tables/areas.json"),readData("tables/spell-names.json")
  ]);
  const version=cm.packVersion({rxp:run.version});
  const all={}; const reports=[];
  const stats={compiled:0,dropped:0,interpack:0};
  for(let i=0;i<parts.length;i++){
    const part=parts[i],label=groupName(part);
    const suffix="-"+part.code+"-"+part.index;
    const id=options.id.slice(0,32-suffix.length).replace(/-+$/,"")+suffix;
    const title=(label+" - "+options.title).slice(0,64);
    const local=new Set(part.guides.map(g=>g.slug));
    const input=part.guides.map(g=>["guides/"+g.slug+".guide",guideText(g,options.id,id,local,stats)]);
    tell("phase",{text:"Compilazione "+(i+1)+"/"+parts.length+": "+label+" ("+input.length+" guide)",progress:72+Math.floor(20*i/parts.length)});
    tell("log",{text:"Compilazione "+(i+1)+"/"+parts.length+": "+label});
    let compiler;
    try{
      compiler=new wasm.Compiler(library,instances??"",areas??"");
      compiler.setSpellNames(spells??"[]");
      const diagnostics=JSON.parse(compiler.setPack(pm.packJson({id,title,author:"WoW XP Helper",version}),null,manifest.iface));
      const errors=diagnostics.filter(d=>d.severity==="error");
      if(errors.length)throw Error("Pacchetto "+label+": "+errors.map(x=>x.message).join("; "));
      const result=bm.compileKeeping(compiler,input);
      if(result.errors.length){
        for(const e of result.errors.slice(0,12))tell("log",{text:(e.file||"")+" "+(e.message||JSON.stringify(e))});
        throw Error("Compilatore Polestar: errore nel gruppo "+label);
      }
      const kept=result.kept.length;
      stats.dropped+=result.dropped.length;
      if(!kept){tell("log",{text:"Nessuna guida valida in "+label});continue;}
      const packed=JSON.parse(compiler.packFiles("{}"));
      const entries=am.addonEntries(compiler.folder(),packed.files);
      for(const [path,value] of Object.entries(entries)){
        if(Object.hasOwn(all,path))throw Error("Nome addon duplicato: "+path);
        all[path]=value;
      }
      stats.compiled+=kept;
      reports.push(label+": "+kept+" guide, "+result.dropped.length+" scartate");
      tell("log",{text:"Completato "+(i+1)+"/"+parts.length+": "+kept+" guide, "+result.dropped.length+" scartate"});
    }finally{compiler?.free?.();}
    await new Promise(resolve=>setTimeout(resolve,0));
  }
  if(!stats.compiled)throw Error("Nessuna guida compilata.");
  const guideMessage=[
    "WoW XP Helper - Pacchetti RestedXP per Polestar",
    "Chiudi WoW ed estrai TUTTE le cartelle PolestarPack_* in:",
    "World of Warcraft\\_forever_\\Interface\\AddOns",
    "Riavvia WoW. Apri Polestar > Community guides.",
    "",
    "Guide compilate: "+stats.compiled,
    "Guide scartate: "+stats.dropped,
    "Pacchetti: "+reports.length,
    ...reports,"",
    "Per evitare blocchi le guide sono divise in pacchetti.",
    "Al confine tra pacchetti potrebbe servire scegliere la guida successiva a mano.",
    "Collegamenti tra pacchetti separati: "+stats.interpack
  ].join("\r\n");
  all["LEGGIMI_INSTALLAZIONE.txt"]=guideMessage;
  tell("phase",{text:"Preparazione dello ZIP finale…",progress:95});
  const archive=zm.zip(all);
  const entries=includeEntries?Object.fromEntries(Object.entries(all).filter(([k])=>k!=="LEGGIMI_INSTALLAZIONE.txt")):null;
  self.postMessage({
    type:"done",filename:"PolestarPack_"+options.id+"_completo.zip",
    buffer:archive.buffer,guideCount:stats.compiled,droppedCount:stats.dropped,
    packCount:reports.length,detachedLinks:stats.interpack,warnings:stats.interpack,
    entries
  },[archive.buffer]);
}
self.onmessage=async({data})=>{
 if(data?.type!=="compile")return;
 try{await compile(data);}
 catch(e){tell("error",{text:e instanceof Error?e.message:String(e),stack:e instanceof Error?e.stack:""});}
};