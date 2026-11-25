// OFN v0.13 publication: approved lifecycle metadata only. No science change.
// Usage: node publish_ofn_v0_13.js CANDIDATE PLAN OUT [--check] [--controls]
const CAND="8659d0bc046a204aae2dc0a7a9d3de3c302771e4b66fbde607730933cdbb283e", PUB="4a2d266bf89cd2130e901b7543bacbaf7fa3e844c60e355a2e3c23ef4f075a49";
function need(ok,msg){if(!ok)throw Error(msg);}
function apply(s,p,reverse=false){
 const a=s.split("\n");
 for(const e of p.edits){const [x,y]=reverse?[e.new,e.old]:[e.old,e.new];need(a[e.line-1]===x&&a.filter(t=>t===x).length===1,"exact anchor "+e.line);a[e.line-1]=y;}
 return a.join("\n");
}
function verify(c,p,o,hash){
 need(hash(c)===CAND&&p.candidate_sha256===CAND,"P1 candidate");
 need(p.schema==="ofn-publication-v1"&&p.published_sha256===PUB&&p.edits.map(e=>e.line).join(",")==="4,7,8,13,15,1563,1567,1613","P2 plan");
 need(apply(c,p)===o&&hash(o)===PUB,"P3 publication bytes");
 const a=c.split("\n"),b=o.split("\n"),diff=a.flatMap((s,i)=>s===b[i]?[]:[i+1]);need(a.length===b.length&&diff.join(",")===p.edits.map(e=>e.line).join(","),"P4 exact metadata delta");
 need(apply(o,p,true)===c,"P5 reverse");
 const rid=s=>s.match(/\[RID: RTG-OFN-[A-Z0-9-]+\]/g)||[],status=s=>s.split("\n").filter(t=>/^Status: (ACTIVE|PARTIAL)\b/.test(t)),anchors=s=>s.match(/<a id="[^"]+"|\{#[^}]+\}/g)||[];
 need(JSON.stringify(rid(c))===JSON.stringify(rid(o))&&rid(o).length===44&&JSON.stringify(status(c))===JSON.stringify(status(o))&&status(o).length===21&&JSON.stringify(anchors(c))===JSON.stringify(anchors(o))&&anchors(o).length===101,"P6 preserved registry");
 return ["P1 PASS exact adopted candidate digest","P2 PASS fixed eight-line metadata plan","P3 PASS exact publication and digest","P4 PASS eight changed lines, every other byte identical","P5 PASS reverse recovers candidate","P6 PASS 44 RIDs, 21 OPEN status lines, 101 anchors"];
}
function controls(c,p,o,hash){
 const cases=[["X1 altered candidate",c+"x",p,o],["X2 extra scientific edit",c,p,o.replace("no physical generator, carrier or primitive object is selected","a physical generator is selected")],["X3 footer left draft",c,p,o.replace("*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.13*","*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.13 — DRAFT*")],["X4 missing metadata edit",c,{...p,edits:p.edits.slice(1)},o],["X5 status modified",c,p,o.replace("Status: ACTIVE","Status: CLOSED")],["X6 RID modified",c,p,o.replace("[RID: RTG-OFN-DEF-FEEDBACK]","[RID: RTG-OFN-DEF-FAKE]")]];
 return cases.map(([n,x,y,z])=>{need(x!==c||y!==p||z!==o,"control invalid "+n);let caught=false;try{verify(x,y,z,hash);}catch(e){caught=true;}need(caught,n+" missed");return n+" caught";});
}
module.exports={apply,verify,controls};
if(require.main===module){const fs=require("node:fs"),crypto=require("node:crypto"),hash=s=>crypto.createHash("sha256").update(s,"utf8").digest("hex"),a=process.argv.slice(2);if(a.length<3)throw Error("usage: CANDIDATE PLAN OUT [--check] [--controls]");const c=fs.readFileSync(a[0],"utf8"),p=JSON.parse(fs.readFileSync(a[1],"utf8")),o=a.includes("--check")?fs.readFileSync(a[2],"utf8"):apply(c,p);console.log(verify(c,p,o,hash).join("\n"));if(a.includes("--controls"))console.log(controls(c,p,o,hash).join("\n"));if(!a.includes("--check"))fs.writeFileSync(a[2],o);console.log("RESULT: PASS",hash(o));}
