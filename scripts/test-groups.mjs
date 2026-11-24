// Smoke tests for unified per-faction RXP leveling packs.
// Run: node scripts/test-groups.mjs
import assert from "node:assert/strict";

globalThis.self={postMessage(){}};
const {buildGroups,guideText}=await import("../compile-worker.mjs");

function guide(slug,faction,route="main",next=""){
  const label=faction?"faction "+faction+"\n":"";
  const link=next?"next "+next+"\n":"";
  return {slug,route,text:"guide rxp-test/"+slug+"\n"+label+"levels 10-20\n"+link+"category Leveling\n\nstep Start\n  note Test\n"};
}
const input=[
  guide("horde-01","Horde","main","rxp-test/horde-02"),
  guide("horde-02","Horde"),
  guide("alliance-01","Alliance","main","rxp-test/alliance-02"),
  guide("alliance-02","Alliance"),
  guide("common-01",null,"main","rxp-test/horde-02, rxp-test/alliance-02"),
  guide("dungeon-horde","Horde","dungeon"),
  guide("dungeon-alliance","Alliance","dungeon")
];
const groups=buildGroups(input);
const speedruns=groups.filter(g=>g.unified);
assert.equal(speedruns.length,2,"exactly one unified pack per faction");
const h=speedruns.find(g=>g.faction==="horde");
const a=speedruns.find(g=>g.faction==="alliance");
assert.deepEqual(h.guides.map(g=>g.slug),["horde-01","horde-02","common-01"]);
assert.deepEqual(a.guides.map(g=>g.slug),["alliance-01","alliance-02","common-01"]);
assert.equal(groups.filter(g=>!g.unified).length,2,"optional dungeon groups separate");
const selected=buildGroups(input,["horde"]);
assert.equal(selected.filter(g=>g.unified).length,1);
assert.equal(selected.find(g=>g.unified).faction,"horde");
assert.ok(selected.every(g=>g.key==="horde-main"||g.key==="horde-dungeon"),"skip unselected faction");

const hId="rxp-completo-160-horde";
const stats={interpack:0};
const hText=guideText(h.guides[0],"rxp-test",hId,new Set(h.guides.map(g=>g.slug)),stats);
assert.ok(hText.startsWith("guide "+hId+"/horde-01\n"));
assert.ok(hText.includes("next "+hId+"/horde-02\n"),"Horde 1-60 links intact");
const aId="rxp-completo-160-alliance";
const aText=guideText(a.guides[0],"rxp-test",aId,new Set(a.guides.map(g=>g.slug)),stats);
assert.ok(aText.includes("next "+aId+"/alliance-02\n"),"Alliance 1-60 links intact");
const hCommon=guideText(h.guides.find(g=>g.slug==="common-01"),"rxp-test",hId,new Set(h.guides.map(g=>g.slug)),stats);
assert.ok(hCommon.includes("next "+hId+"/horde-02\n"));
assert.ok(!hCommon.includes("alliance-02"),"shared guide must not cross factions");
assert.equal(stats.interpack,1);
console.log("PASS: 1 Horde pack + 1 Alliance pack; shared guides and same-faction next links preserved.");
