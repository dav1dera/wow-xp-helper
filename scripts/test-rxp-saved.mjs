// Synthetic-only regression check for the upstream RestedXP SavedVariables reader.
// No actual account cache, BattleTag or premium guides are included in the project.
import assert from "node:assert/strict";
import {deflateRawSync} from "node:zlib";
import {savedGuides} from "../_site/converter/src/rxp/saved.mjs";
import {Report} from "../_site/converter/src/ir.mjs";

const guide = [
 "#group Example Speedrun (H)",
 "#name 1-5 Synthetic Test",
 "<< Horde",
 "step",
 ">>Take a fictional errand",
 ".accept 7",
 ""
].join("\n");
const packed=deflateRawSync(Buffer.from("--123456789\n"+guide,"utf8"));
const gameString=[...packed].map(b=>
 b===34?'\\\"':b===92?'\\\\':b>=32&&b<127?String.fromCharCode(b):'\\'+String(b).padStart(3,'0')
).join("");
const fixture=new TextEncoder().encode(
 'RXPData = { ["release"] = "test", }\n'+
 'RXPDB = { ["profiles"] = { ["global"] = { ["guides"] = { '+
 '["Example Speedrun (H)||1-5 Synthetic Test|1"] = { ["groupOrContent"] = "'+
 gameString +'", ["cache"] = true, }, }, }, }, }\n'+
 'RXPSettings = { ["profiles"] = {}, }\n'
);
const report=new Report();
const files=await savedGuides([fixture],report);
assert.equal(files.length,1,"new RXPDB guide profile format should be read");
assert.match(files[0].text,/RegisterGuide\(\[\[--123456789/,"original imported guide content is retained");
assert.match(files[0].text,/#group Example Speedrun \(H\)/);
assert.equal(report.counts.get("imported guide read (SavedVariables)"),1);
console.log("PASS: latest upstream RXP SavedVariables import recognizes synthetic deflated Lua guide.");
