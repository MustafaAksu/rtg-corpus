// OFN v0.13 independent validation and synthetic negative controls.
// Connector execution used these functions with self-tested JS SHA-256; Node CLI uses native SHA-256.
const H={"base":"55ff8ba85d4bb48b52266bdd9a44aa84efcd2cc19903d059266fa406a6bb76aa","map":"b46574cb6daaf437a384ec3622b0edb2f3109d41d1ee55eeb6ad3335424feb21","candidate":"7f026a9d3da6c2572281972e7c35c7635fb74888307d9cfe28088087b14613d7","source":"02e90f12f6b785757d2d384f22d1972e08ca0692eaf3d919c3f099ce2f5ee0be"};
function req(ok,g,msg){if(!ok)throw Error(g+": "+msg);}

function eq(a,b){return JSON.stringify(a)===JSON.stringify(b);}

function span(s,a,b,g){const i=s.indexOf(a),j=s.indexOf(b,i+a.length);req(i>=0&&j>i,g,"missing section "+a);return s.slice(i,j);}

function basegate(b,hash){req(hash(b)===H.base,"C0","base identity");}

function mapgate(b,m,hash){
 req(hash(m)===H.map,"C1","frozen map identity");
 const p=JSON.parse(m),l=b.split("\n"),ids=new Set();let last=0;
 req(p.schema==="ofn-stage1-line-addressed-v1"&&p.base_sha256===H.base&&p.edits.length===145,"C1","schema/count");
 for(const e of p.edits){req(e.line>last&&Number.isInteger(e.line)&&e.line<=l.length&&!ids.has(e.id),"C1","unique address");req(l[e.line-1]===e.old&&e.old!==e.new&&!e.old.includes("\n"),"C1","exact anchor "+e.id);last=e.line;ids.add(e.id);}
 return p;
}

function replaygate(b,p,log,c,hash){
 const l=b.split("\n"),lookup=new Map(p.edits.map(e=>[e.line,e]));
 req(l.flatMap((s,i)=>lookup.has(i+1)?lookup.get(i+1).new.split("\n"):[s]).join("\n")===c,"C2","independent linear rebuild");
 req(hash(c)===H.candidate&&log.candidate_sha256===H.candidate&&log.base_sha256===H.base&&log.edits.length===p.edits.length,"C2","candidate/log identity");
 const work=l.slice(),undo=[];let d=0,prev=hash(b);
 for(let i=0;i<p.edits.length;i++){const e=p.edits[i],r=log.edits[i],j=e.line-1+d,n=e.new.split("\n");req(work[j]===e.old,"C2","anchor "+e.id);work.splice(j,1,...n);d+=n.length-1;undo.push({j,e,n});const after=hash(work.join("\n"));req(r.id===e.id&&r.line===e.line&&r.group===e.group&&r.reason===e.reason&&r.old_sha256===hash(e.old)&&r.new_sha256===hash(e.new)&&r.doc_sha256_before===prev&&r.doc_sha256_after===after,"C2","hash chain "+e.id);prev=after;}
 req(work.join("\n")===c,"C2","chain reconstruction");
 for(const {j,e,n} of undo.reverse()){req(eq(work.slice(j,j+n.length),n),"C2","reverse payload");work.splice(j,n.length,e.old);}
 req(work.join("\n")===b,"C2","exact reverse recovery");
}

function ridgate(b,c){
 const d=s=>[...s.matchAll(/\[RID: (RTG-OFN-[A-Z0-9-]+)\]/g)].map(x=>x[1]).sort(),a=d(b),z=d(c);
 req(eq(a,z)&&z.length===44&&new Set(z).size===44,"C3","OFN RID declarations");
 for(const [k,n] of Object.entries({DEF:17,ALG:5,HYP:1,OPEN:21}))req(z.filter(x=>x.startsWith("RTG-OFN-"+k+"-")).length===n,"C3","RID type "+k);
 const refs=s=>[...new Set(s.match(/\bRTG-OFN-[A-Z0-9]+(?:-[A-Z0-9]+)*/g)||[])].sort();req(eq(refs(b),refs(c)),"C3","identity references");
}

function protectedgate(b,c){
 const live=s=>s.split("## Appendix A —")[0].split("\n");
 const d=s=>live(s).filter(x=>x.startsWith("`[DEF]`")&&!x.includes("[import:")),g=s=>live(s).filter(x=>/^\*\*\[SG-|^Violation:/.test(x)),q=s=>live(s).filter(x=>/^\| \*\*Q[1-6]/.test(x));
 req(eq(d(b),d(c)),"C4","local definitions");req(eq(g(b),g(c)),"C4","guards");req(eq(q(b),q(c))&&q(c).length===7,"C4","Q rows");
 const core=s=>span(s,"### 5.5 Genuine Relational-Triad Model-Selection Contract","\n## 6.","C4").split("\n").filter(x=>!x.startsWith("| κ values |")).join("\n");
 req(core(b)===core(c),"C4","class C / Standard C / narrow Q6 outside attribution");
 req(span(b,"### 2.4 The Relational Build Sequence","\n## 3.","C4")===span(c,"### 2.4 The Relational Build Sequence","\n## 3.","C4"),"C4","REF-CLOSURE");
 const fa=s=>live(s).find(x=>x.includes("**Finding A — common-token shifts.**"));
 req(fa(b).replace("custody transfer deferred","custody transfer open (separate joint decision)")===fa(c),"C4","Finding A declaration");
 const grades=s=>live(s).filter(x=>/^`?\[(?:DEF|THM|ALG|RESULT|HYP|OPEN|HEUR|NUM|INTERP|COR)\]/.test(x)).map(x=>x.match(/^`?\[([A-Z]+)\]/)[1]);
 req(eq(grades(b),grades(c)),"C4","ordered live claim-opening grades");
}

function opengate(b,c,p){
 const ss=s=>[...s.matchAll(/^Status: (?:ACTIVE|PARTIAL|CLOSED|HOLD|INCONCLUSIVE)\b.*$/gm)].map(x=>x[0]),x=ss(b),y=ss(c);
 req(eq(x,y)&&y.length===21&&y.filter(l=>l.startsWith("Status: ACTIVE")).length===20&&y.filter(l=>l.startsWith("Status: PARTIAL")).length===1,"C5","OPEN status lines");
 const region=s=>span(s,"## 9. Foundational OPEN Problems","\n## 10.","C5");let expected=region(b);
 for(const id of ["E0709","E0883"]){const e=p.edits.find(x=>x.id===id);req(!!e&&expected.split(e.old).length===2,"C5","unique registry anchor "+id);expected=expected.replace(e.old,e.new);}
 req(expected===region(c),"C5","registry outside two authorized edits");
}

function histgate(b,c){
 const a=s=>[...s.matchAll(/<a id="([^"]+)"|\{#([^}]+)\}/g)].map(m=>m[1]||m[2]);req(eq(a(b),a(c))&&a(c).length===101,"C6","anchors");
 const ab=s=>span(s,"## Appendix A —","## Appendix C —","C6");req(ab(b)===ab(c),"C6","Appendices A/B");
 const h=s=>span(s,"### v0.12 — 30 October 2026 — ADOPTED","*END OF DOCUMENT —","C6");req(h(b)===h(c),"C6","inherited Appendix C");
}

function scopegate(b,c){
 const l=c.split("## Appendix A —")[0];
 for(const rx of [/deferred[^.\n|]{0,60}v2\.13/i,/until TDR-G v2\.13 decides/,/defers the custody transfer XFER-O08-01 to v2\.13/,/registered provisional/,/referred back to TDR-G/,/for this draft/,/under \(D5\)/,/\(D5\) are not removed/,/γ ≡ κ is the declared parameter convention of Genesis/,/DZT v0\.8 charter/,/Triadic v1\.6\.1/])req(!rx.test(l),"C7","stale "+rx.source);
 for(const n of [1149,1155,1185]){const old=b.split("\n")[n-1],start=old.indexOf("Genesis v2.8.5"),suffix="(claim-level pin; not re-read at `gen-v2.9`)",end=old.indexOf(suffix);req(start>=0&&end>start&&l.includes(old.slice(start,end+suffix.length)),"C8","GEN historical reference "+n);}
 const required=["custody transfer XFER-O08-01 is open, a separate decision of both owners","custody component OPEN","the six-constraint list is not recovered","fixed admissible component selection","the sum is invariant under the declared phase gauge and relabelling",'"gauge-like" / "gauge artifact" were withdrawn',"exactly one valid centre","balanced ties are path-rule outcomes, not a component class","The spectrum alone does not determine its birth update","c_{t+1}(y)=c_t(y)+b_t(-y)","b_t(y)=c_{t+1}(-y)-c_t(-y)","It is not shown here that the census determines the selected centres","not an engine reachability test","not a new OFN theorem or selection","D5A fallback not adopted","R9 remains a premise wherever required","at-least-two-usable-slip conditions","known-$a$ schedule","unknown $a$","scope: Programme's reference map, with generator selection open","the Gram relation is a first-variation coefficient identity, not an exact discrete conservation law","truncated coefficient ODE with $Q_s,Q_c>0$","the off-root extension is not unique","not a replacement for the earlier closing result or its rows","The original v6.4.14/15 source blocks, row assumptions, constants and proof/evidence chain were not re-verified","γ ≡ κ is OFN's class-C parameter convention","IF03's Finding A claim pin v0.10 was correct at Programme adoption","DZT v0.17 is recovered, unadopted history","SG-DZT-1 and SG-AZ-7","Bilinearity and full universal-classification proof dependencies remain unverified","NUMGEN v1.22 §6.6 P2 re-annotation","not the earlier Atlas rerun or a retroactive admission/certificate replacement","FMS symbolic P4 source-reported; OFN sampled verification"];
 for(const q of required)req(l.toLowerCase().includes(q.toLowerCase()),"C8","missing scope "+q);
 req(!/(?:I-comp|I-quiet|I-remove|standard \([abc]\))\s+(?:is|was)\s+(?:selected|adopted)\b/i.test(l),"C8","unauthorized standard selection");
 req(!/custody (?:transfer )?XFER-O08-01 (?:is )?(?:completed|transferred|adopted)\b/i.test(l),"C8","unauthorized transfer");
}

function sourcegate(b,c,s,hash){
 req(hash(s)===H.source,"C9","source report identity");const r=JSON.parse(s);
 req(r.pass===true&&r.candidate_sha256===H.candidate&&r.sources.length===11&&r.sources.every(x=>x.sha256===x.expected_sha256),"C9","source hashes");
 const ids=s=>new Set(s.match(/\b(?:DYAD|GEN|TDRG|RECOG|NUMGEN|TRIAD|DZT|AZ)-(?:THM|ALG|DEF|CAND|RESULT|NUM|OPEN|ART|HYP)-[A-Z0-9]+(?:-[A-Z0-9]+)*/g)||[]),a=ids(b),z=ids(c),newIds=[...z].filter(x=>!a.has(x)).sort();
 req([...a].every(x=>z.has(x)),"C9","old external reference removed");
 req(newIds.length===8&&eq(newIds,r.new_external_references.map(x=>x.rid).sort())&&r.new_external_references.every(x=>x.ok&&x.lines.length>0),"C9","new external RID resolution");
 req(r.changed_explicit_imports.length===22&&r.import_rid_checks.length===24&&r.import_anchor_checks.length===21&&r.import_rid_checks.every(x=>x.ok)&&r.import_anchor_checks.every(x=>x.ok),"C9","import locator resolution");
}

function draftgate(c){req(c.startsWith("# RTG_ONTOLOGICAL_FOUNDATIONS_v0.13\n")&&c.includes("**Document status:** DRAFT —")&&c.includes("### v0.13 — 24 November 2026 — DRAFT")&&c.endsWith("*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.13 — DRAFT*\n")&&c.includes("PI adoption pending"),"C10","draft publication boundary");}

function validate(b,m,l,c,s,hash){
 basegate(b,hash);const p=mapgate(b,m,hash);replaygate(b,p,JSON.parse(l),c,hash);ridgate(b,c);protectedgate(b,c);opengate(b,c,p);histgate(b,c);scopegate(b,c);sourcegate(b,c,s,hash);draftgate(c);
 return ["C0 PASS adopted base identity","C1 PASS 145 exact unique line-addressed edits","C2 PASS independent rebuild; 290 payload hashes and all document hash links; exact reverse","C3 PASS 44 OFN RID declarations (17 DEF, 5 ALG results, 1 HYP, 21 OPEN)","C4 PASS local definitions, guards, Q1-Q6, REF-CLOSURE and class-C core, Finding A and claim-opening grades","C5 PASS 20 ACTIVE + 1 PARTIAL; registry exact except two authorized edits","C6 PASS 101 anchors and inherited Appendices A/B/C","C7 PASS live stale wording removed","C8 PASS required scopes, preserved limitations and no selected isolation/independence/custody","C9 PASS source report: 11 source hashes, 8 external RIDs, 24 import RID and 21 anchor checks","C10 PASS DRAFT-only boundary"];
}

function controls(b,m,l,c,s,hash){
 const out=[],p=JSON.parse(m);
 function caught(name,g,fn){let msg="";try{fn();}catch(e){msg=String(e.message||e);}req(msg.startsWith(g+":"),"NC",name+" wrong result: "+msg);out.push(name+" caught by "+g);}
 function change(a,z){req(c.includes(a),"NC","missing anchor "+a);return c.replace(a,z);}
 caught("NC1 altered base","C0",()=>basegate(b+"x",hash));
 caught("NC2 altered edit map","C1",()=>mapgate(b,m.replace('"line": 1,','"line": 2,'),hash));
 caught("NC3 undeclared candidate edit","C2",()=>replaygate(b,p,JSON.parse(l),c+"x",hash));
 caught("NC4 local RID changed","C3",()=>ridgate(b,change("[RID: RTG-OFN-DEF-FEEDBACK]","[RID: RTG-OFN-DEF-FAKE]")));
 caught("NC5 Standard C weakened","C4",()=>protectedgate(b,change("requires a positive-dimensional embedded","requires a nonempty embedded")));
 caught("NC6 Q6 weakened","C4",()=>protectedgate(b,change("Required: interaction that cannot be removed","Optional: interaction that cannot be removed")));
 caught("NC7 OPEN status changed","C5",()=>opengate(b,change("Status: ACTIVE |","Status: CLOSED |"),p));
 caught("NC8 anchor removed","C6",()=>histgate(b,change('<a id="ofn-star-token-shift"></a>',"")));
 caught("NC9 historical entry changed","C6",()=>histgate(b,change("### v0.12 — 30 October 2026 — ADOPTED","### v0.12 — 31 October 2026 — ADOPTED")));
 caught("NC10 stale custody target","C7",()=>scopegate(b,change("custody transfer XFER-O08-01 is open, a separate decision of both owners","custody transfer XFER-O08-01 is deferred to v2.13")));
 caught("NC11 stale provisional label","C7",()=>scopegate(b,change("Dyadic custody; scope: Programme's reference map","registered provisional, Dyadic custody")));
 caught("NC12 old D5 assumption","C7",()=>scopegate(b,change("the named former (D5) qualifier is discharged","under (D5)")));
 caught("NC13 R9 removed","C8",()=>scopegate(b,change("R9 remains a premise wherever required","R9 is no longer a premise")));
 caught("NC14 Triadic scope lost","C8",()=>scopegate(b,change("the off-root extension is not unique","the off-root extension is unique")));
 caught("NC15 Genesis historical pin moved","C8",()=>scopegate(b,change("Genesis v2.8.5 §§6.3–6.6","Genesis v2.10 §§6.3–6.6")));
 caught("NC16 physical isolation selected","C8",()=>scopegate(b,change("Isolation frame (recorded; none selected).","Isolation frame (I-quiet is selected).")));
 caught("NC17 FMS universal-P4 overclaim","C8",()=>scopegate(b,change("Bilinearity and full universal-classification proof dependencies remain unverified","Bilinearity and full universal-classification proof dependencies are certified")));
 caught("NC18 source report tampered","C9",()=>sourcegate(b,c,s.replace('"pass": true','"pass": false'),hash));
 caught("NC19 new external RID mistyped","C9",()=>sourcegate(b,change("TDRG-ALG-TOKEN-CENSUS-LAW","TDRG-ALG-FAKE-CENSUS-LAW"),s,hash));
 caught("NC20 premature adoption","C10",()=>draftgate(change("**Document status:** DRAFT —","**Document status:** ADOPTED —")));
 return out;
}
module.exports={validate,controls};
if(require.main===module){const fs=require("node:fs"),crypto=require("node:crypto"),hash=s=>crypto.createHash("sha256").update(s,"utf8").digest("hex");const a=process.argv.slice(2);if(a.length<5)throw Error("usage: node check_ofn_v0_13.js BASE MAP LOG CANDIDATE SOURCE_REPORT [--controls]");const [b,m,l,c,s]=a.slice(0,5).map(p=>fs.readFileSync(p,"utf8"));console.log(validate(b,m,l,c,s,hash).join("\n"));console.log("RESULT: PASS");if(a.includes("--controls")){console.log(controls(b,m,l,c,s,hash).join("\n"));console.log("CONTROLS: PASS");}}
