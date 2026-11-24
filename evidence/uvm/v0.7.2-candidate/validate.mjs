#!/usr/bin/env node
// UVM v0.7.2 candidate review verifier. Run at repository root: node evidence/uvm/v0.7.2-candidate/validate.mjs
import { readFileSync, writeFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
const path="dsn/RTG_OPEN_M_DSN.md",dir="evidence/uvm/v0.7.2-candidate/";
const read=(p)=>readFileSync(p,'utf8'),git=(ref)=>execFileSync('git',['show',ref+':'+path],{encoding:'utf8',maxBuffer:32*1024*1024}),digest=s=>createHash('sha256').update(s,'utf8').digest('hex');
function verify(source,one,intermediate,final,p1,p2,map,digest){
 const checks=[];const ck=(name,ok)=>{checks.push({name,ok:!!ok});if(!ok)throw Error(name)};
 const occurrences=(s,x)=>s.split(x).length-1,part=(s,a,b)=>s.slice(s.indexOf(a),s.indexOf(b)),without=(s,a,b)=>s.slice(0,s.indexOf(a))+s.slice(s.indexOf(b));
 ck("01 tagged base identity",digest(source)===p1.source_sha256);
 ck("02 Stage A1 identity",digest(one)===p1.stage_a_sha256);
 ck("03 Stage A1 map non-overlapping",p1.edits.every((x,n,a)=>x.first>=1&&x.last>=x.first&&(n===0||a[n-1].last<x.first)));
 const originalLines=source.split("\n");
 ck("04 all A1 source spans exact",p1.edits.every(x=>originalLines.slice(x.first-1,x.last).join("\n")===x.old));
 let l=originalLines.slice();for(const x of p1.edits.slice().reverse())l.splice(x.first-1,x.last-x.first+1,...x.new.split("\n"));
 ck("05 exact replay A1",l.join("\n")===one);
 ck("06 A2 parent identity",digest(one)===p2.source_sha256);
 let s=one;let valid=true;for(const x of p2.operations){if(occurrences(s,x.old)!==x.count){valid=false;break} s=s.split(x.old).join(x.new)}
 ck("07 all A2 literal guards",valid);ck("08 exact replay A2",s===intermediate);ck("09 corrected intermediate hash",digest(intermediate)===p2.output_sha256&&digest(intermediate)===map.base_sha256);ck("10 candidate hash",digest(final)===map.candidate_sha256);
 ck("11 exactly one structural operation",map.operations.length===1&&map.operations[0].class==="history-appendix"&&map.operations[0].op==="replace-section");
 const op=map.operations[0],a=op.start,b=op.end,archive=map.archives[0];ck("12 unique ordered history bounds",[intermediate,final].every(t=>occurrences(t,a)===1&&occurrences(t,b)===1&&t.indexOf(a)<t.indexOf(b)));
 ck("13 archive identity",archive.sha256===digest(source)&&archive.git===p1.source_tag+":"+p1.source_path);
 ck("14 complete removed history occurs in adopted archive",source.includes(part(intermediate,a,b)));
 ck("15 exact Stage B replay",intermediate.slice(0,intermediate.indexOf(a))+op.new+intermediate.slice(intermediate.indexOf(b))===final);
 ck("16 entire outside-history text byte-identical",without(intermediate,a,b)===without(final,a,b));
 ck("17 Stage B history-only heading",op.new.startsWith(a+"\n")&&(op.new.match(/^## /gm)||[]).length===1);
 const live=final.slice(0,final.indexOf(a));const ids=[...live.matchAll(/\[RID:\s*(UVM-[A-Z0-9-]+)\]/g)].map(m=>m[1]);
 ck("18 unique live local RID declarations",ids.length>0&&new Set(ids).size===ids.length);
 ck("19 OPEN and R14 identities distinct",ids.includes("UVM-OPEN-2F")&&ids.includes("UVM-NUM-2F-TRAJ"));
 ck("20 R14 selected panel scope twice",occurrences(live,"Across nine stage-labelled packs from several run continuations within the recorded `seed_001/rank_2` context (n=9); a common byte-identical bootstrap state has not been established.")===2);
 ck("21 no former single-series assertion",!live.includes("Along a single T80→T120 growth series"));
 ck("22 ultra panel identity",live.includes("T100 ultra (T98_to_T100_2e_ultra)")&&["0.2949","0.5273","nm=2","0.8381","0.7408"].every(x=>live.includes(x)));
 ck("23 gentle panel identity",live.includes("T100 gentle (T80_to_T100_gentle)")&&["0.2521","0.3425","nm=0","1.4884","0.7041"].every(x=>live.includes(x)));
 ck("24 correlations retained",["+0.654","+0.326","+0.488"].every(x=>live.includes(x)));
 ck("25 R14 numerical grade",live.split("\n").some(x=>x.startsWith("`[NUM]`")&&x.includes("[RID: UVM-NUM-2F-TRAJ]")));
 ck("26 independent-correlation/causal limits",live.includes("no test of dependent-correlation difference, independence, causal or universal ranking"));
 ck("27 single jet target contract",live.includes("single-jet hypothesis")&&live.includes("conditional 9C")&&live.includes("large-positive-$g$"));
 ck("28 positive-m branch and signed magnitude",live.includes("$m>0$")&&live.includes("$|m||w|$")&&live.includes("negative-$m$"));
 ck("29 nondegenerate R15 quotient",live.includes("$gC_mh\\ne0$")&&live.includes("$m=C_mh$"));
 ck("30 exact diagnostic conversion retained",live.includes("$\\rho r^4\\ge4/125$")&&live.includes("$\\rho\\ge16/5$"));
 ck("31 prelegacy finite scope",live.includes("Pre-Legacy")&&live.includes("0.403")&&live.includes("N=175"));
 ck("32 proxy not physical identification",live.includes("$h:=z_h^2$")&&live.includes("Identifying it with the physical"));
 ck("33 THM-3G only scoped reported evidence",live.includes("owner-reported branch-native conformal-stiffness result")&&live.includes("two synthetic clusters with six checks PASS")&&live.includes("original output, complete hypotheses/claim/proof registration are missing"));
 ck("34 old audit missing artifact",live.includes("PI-attested audit, 23 Nov 2026")&&live.includes("missing original script and output"));
 ck("35 stage 1 not adopted",live.includes("Stage 1 is not adopted science.")&&live.includes("C3 blocked on Genesis"));
 ck("36 RRF provisional reference",live.includes("RRF v0.8.4")&&live.includes("PI approval pending")&&live.includes("no registered profile or transport arrow"));
 ck("37 owner source receipt not inferred",live.includes("Source-text reference (not a receipt)")&&live.includes("not evidence of receipt of a specific notice"));
 ck("38 all four missing original items named",["uvjet_equivariant_classification.py","esm_harmonic_report.py","t103_defect_carrier_test.py","EDIT_A_wiring_instructions.txt"].every(x=>live.includes(x)));
 ck("39 DRAFT not adopted",live.includes("**Document status:** DRAFT")&&final.endsWith("DRAFT CANDIDATE; NOT ADOPTED*\n"));
 ck("40 one final footer",(final.match(/^\*END OF DOCUMENT/gm)||[]).length===1);
 ck("41 no compound RESULT companion tags",!/\[from:[^\]\n]*(?:\/|,|\+)[^\]\n]*\]/.test(live));
 return checks;
}
function negatives(source,one,intermediate,final,p1,p2,map,digest){
 const changes=[
 ["source corruption",source.replace("OPEN M","OPEN Z"),one,intermediate,final,p1,p2,map],
 ["undeclared A1 change",source,one.replace("OPEN M","OPEN Z"),intermediate,final,p1,p2,map],
 ["undeclared A2 change",source,one,intermediate.replace("0.2949","0.2948"),final,p1,p2,map],
 ["B modifies live result even with matching candidate hash",source,one,intermediate,final.replace("0.2949","0.2948"),p1,p2,{...map,candidate_sha256:digest(final.replace("0.2949","0.2948"))}],
 ["B removes live conditional phrase even with matching hash",source,one,intermediate,final.replace("Stage 1 is not adopted science.","Stage 1 is adopted science."),p1,p2,{...map,candidate_sha256:digest(final.replace("Stage 1 is not adopted science.","Stage 1 is adopted science."))}]
 ];
 return changes.map(([name,...args])=>{let fail="";try{verify(...args,digest)}catch(e){fail=e.message}if(!fail)throw Error("negative control did not reject: "+name);return {name,ok:true,rejectedBy:fail}});
}
const p1=JSON.parse(read(dir+'stage_a_edits.json')),p2=JSON.parse(read(dir+'stage_a_readback_edits.json')),map=JSON.parse(read(dir+'stage_b_map.json'));
const source=git(p1.source_tag),one=git("dfe37264b0bf35a4ccd134ce9fad013366530ad5"),intermediate=git("8b6a46ec8ace905cf7400f2e43f2129b326fb6f5"),final=git("e9efaddc722a5157d1217ac632bf72d9f4403e32");
const checks=verify(source,one,intermediate,final,p1,p2,map,digest),neg=negatives(source,one,intermediate,final,p1,p2,map,digest);
for(const x of checks) console.log('PASS '+x.name);for(const x of neg) console.log('PASS negative: '+x.name+' (rejected by '+x.rejectedBy+')');
console.log('SUMMARY: '+checks.length+'/'+checks.length+' checks PASS; '+neg.length+'/'+neg.length+' negative controls rejected.');

function replay(s,ops){for(const x of ops){if(s.split(x.old).length-1!==x.count)throw Error("literal guard "+x.reason);s=s.split(x.old).join(x.new)}return s}
function verifyRevision(src,A,C,out,M,rev,NM,digest){
 let checks=[];const ck=(n,ok)=>{if(!ok)throw Error(n);checks.push(n)};
 const live=s=>s.split("## Appendix A — Version History")[0],ids=s=>[...live(s).matchAll(/\[RID:\s*([^\]\n]+)\]/g)].flatMap(x=>x[1].match(/\bUVM-[A-Z0-9-]+\b/g)||[]),unique=s=>[...new Set(ids(s))].sort(),eq=(x,y)=>JSON.stringify(x)===JSON.stringify(y),op=M.operations[0],strip=s=>s.slice(0,s.indexOf(op.start))+s.slice(s.indexOf(op.end)),hist=s=>s.slice(s.indexOf(op.start),s.indexOf(op.end));
 ck("R01 original identities",digest(src)===M.archives[0].sha256&&digest(A)===M.base_sha256&&digest(C)===M.candidate_sha256);
 ck("R02 exact original B replay",A.slice(0,A.indexOf(op.start))+op.new+A.slice(A.indexOf(op.end))===C);
 ck("R03 review parents match",rev.source_sha256===digest(C)&&rev.intermediate_source_sha256===digest(A));
 const a=replay(A,rev.operations);
 ck("R04 revised intermediate",digest(a)===rev.intermediate_sha256&&digest(a)===NM.base_sha256);
 ck("R05 exact revision replay and candidate hash",replay(C,rev.operations)===out&&digest(out)===rev.candidate_sha256&&digest(out)===NM.candidate_sha256);
 ck("R06 B01 operation, archive and profile unchanged",eq(M.operations,NM.operations)&&eq(M.archives,NM.archives)&&eq(M.profile,NM.profile));
 ck("R07 revised B exact replay",a.slice(0,a.indexOf(op.start))+op.new+a.slice(a.indexOf(op.end))===out);
 ck("R08 outside Appendix A byte-identical",strip(a)===strip(out));
 ck("R09 history unchanged and archived",hist(a)===hist(A)&&src.includes(hist(a))&&hist(out)===hist(C));
 const before=unique(src),after=unique(out),added=after.filter(x=>!before.includes(x));
 ck("R10 all 50 predecessor RIDs retained",before.length===50&&before.every(x=>after.includes(x)));
 ck("R11 exactly seven approved new RIDs",eq(added,["UVM-ALG-CENTRAL-WEIGHTS","UVM-ALG-HINDEX","UVM-ALG-LOCK-EQUATION","UVM-ALG-SOURCE-TOWER","UVM-ALG-SPIN2-JET","UVM-HEUR-SINGLEJET-NATURALNESS","UVM-HYP-PARAMETER-COUNT"])&&after.length===57);
 ck("R12 no duplicate declarations",ids(out).length===after.length);
 let t=live(out),rows=t.split("\n"),row=id=>rows.find(x=>x.startsWith("- [RID: "+id+"]"))||"";
 ck("R13 carrier NUM provenance",row("UVM-NUM-CARRIER").includes("`[NUM]`")&&row("UVM-NUM-CARRIER").includes("EV-SRC-REPORTED")&&row("UVM-NUM-CARRIER").includes("missing"));
 ck("R14 in-grow ENG and 4dp",["`[ENG]`","4 dp","EV-SRC-REPORTED"].every(x=>row("UVM-ENG-INGROW").includes(x)));
 ck("R15 doclint ENG scope",["`[ENG]`","§6 body","EV-SRC-REPORTED"].every(x=>row("UVM-ENG-DOCLINT").includes(x)));
 ck("R16 artifact grades",["UVM-ART-EQUIV-CLASS","UVM-ART-CONSTRAINT-SCOPE","UVM-ART-PHASE-CLOSE"].every((id,i)=>row(id).includes(i===0?"`[ALG]`":"`[ENG]`")&&row(id).includes("EV-SRC-REPORTED")));
 ck("R17 R9 scoped NUM and separate OPEN",rows.some(x=>x.startsWith("`[NUM]` `[scope: archival chart only; source-reported]` **R9")&&x.includes("[RID: UVM-ALG-H3AUDIT]")&&x.includes("UVM-OPEN-H3AUDIT")&&x.includes("no full-map gauge-class invariance follows")));
 ck("R18 complete R14 scope sentence twice",t.split("The correlations are computed across nine stage-labelled packs from several run continuations within the recorded `seed_001/rank_2` context (n=9); a common byte-identical bootstrap state has not been established.").length===3);
 ck("R19 R14 values and grade retained",["+0.654","+0.326","+0.488"].every(x=>t.includes(x))&&rows.some(x=>x.startsWith("`[NUM]`")&&x.includes("[RID: UVM-NUM-2F-TRAJ]")));
 ck("R20 all 16 SG-M guards retained",[...Array.from({length:15},(_,i)=>"SG-M-"+(i+1)),"SG-M-ESM-CAL"].every(x=>t.includes("**["+x+"]**")));
 ck("R21 RRF reference only",t.includes("PI-approved reference-only scope")&&t.includes("no registered profile or transport arrow")&&t.includes("no factor 2 applied to 0.1")&&!t.includes("PI approval pending"));
 ck("R22 C3 and stage1 status",t.includes("Stage 1 is not adopted science.")&&t.includes("C3 blocked on Genesis"));
 ck("R23 draft status",t.includes("**Document status:** DRAFT")&&out.endsWith("DRAFT CANDIDATE; NOT ADOPTED*\n"));
 ck("R24 target domain and values",["$gC_mh\\ne0$","single-jet hypothesis","$\\rho r^4\\ge4/125$","$\\rho\\ge16/5$","no certified numerical deficit factor"].every(x=>t.includes(x)));
 ck("R25 missing originals remain explicit",["uvjet_equivariant_classification.py","esm_harmonic_report.py","t103_defect_carrier_test.py","EDIT_A_wiring_instructions.txt"].every(x=>t.includes(x)));
 return {checks,intermediate:a};
}
function negRevision(src,A,C,out,M,rev,NM,digest){return [
["lost RID",out.replace("[RID: UVM-NUM-CARRIER]","UVM-NUM-CARRIER")],
["grade promotion",out.replace("`[NUM]` [scope: per-edge harmonic-energy","`[THM]` [scope: per-edge harmonic-energy")],
["RRF broadening",out.replace("PI-approved reference-only scope; no new profile/arrow or UV bundle transport","physical transport approved")],
["n=11",out.replace("context (n=9)","context (n=11)")],
["stage1 adoption",out.replace("Stage 1 is not adopted science.","Stage 1 is adopted science.")],
["history status",out.replace("DRAFT; adoption pending","ADOPTED")]
].map(([name,m])=>{if(m===out)throw Error("absent mutant "+name);let why="";try{verifyRevision(src,A,C,m,M,{...rev,candidate_sha256:digest(m)},{...NM,candidate_sha256:digest(m)},digest)}catch(e){why=e.message}if(!why)throw Error("negative survived "+name);return {name,why}})}
const revision=JSON.parse(read(dir+'review_revision_edits.json')), revisedMap=JSON.parse(read(dir+'stage_b_revision_map.json'));
const revisedCandidate=read(path), result=verifyRevision(source,intermediate,final,revisedCandidate,map,revision,revisedMap,digest), controls=negRevision(source,intermediate,final,revisedCandidate,map,revision,revisedMap,digest);
for(const x of result.checks) console.log('PASS '+x);
for(const x of controls) console.log('PASS negative: '+x.name+' (rejected by '+x.why+')');
console.log('Revision '+result.checks.length+'/'+result.checks.length+' PASS; '+controls.length+'/'+controls.length+' negative controls rejected.');
if(process.argv.length!==2){if(process.argv.length!==4||process.argv[2]!=='--write-intermediate')throw Error('Usage: node validate.mjs [--write-intermediate PATH]');writeFileSync(process.argv[3],result.intermediate,{encoding:'utf8',flag:'wx'});console.log('Revised intermediate SHA-256 '+digest(result.intermediate));}
