"""Run focused review fixtures; do not claim full PR/checker replay.
The negative fixtures are not edits to the repository or to the Atlas candidate.
"""
import json
from pathlib import Path
import argparse, importlib.util
ap=argparse.ArgumentParser()
ap.add_argument('--checker', default='tools/atlas_check.py')
ap.add_argument('--output', default='receiver_component_results.json')
a=ap.parse_args()
spec=importlib.util.spec_from_file_location('atlas_checker_under_review', a.checker)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
Atlas,Report=m.Atlas,m.Report
check_coverage,check_links,check_qualifiers=m.check_coverage,m.check_links,m.check_qualifiers
OUT=Path(__file__).parent
rows=[]
def record(key, expected, rep, explanation):
    rows.append(dict(id=key, expected=expected, observed=rep.rows, explanation=explanation))
# Source is the exact current-source table row fetched from DYAD v6.4.22 lines 15–50.
phantom='DYAD-CAND-PHISTAR-ENTRY-PHASE'
source=f'| `{phantom}` | never a Dyadic identifier (former NUMGEN pin; removed by NUMGEN v1.20.8, notice N3) | §7 notices |'
rep=Report(); check_links(rep,Atlas(f'### D2.L5 DIAGNOSTICS\nNUMGEN.N-D D-RID | {phantom}: not an owner identifier.'),{'DYAD':source})
record('RV-N1-explicitly-denied-identifier','DOCUMENTED-UNRESOLVED, never PASS',rep,'A table cell explicitly denying RID ownership is accepted as a declaration.')
# Same false identifier placed in a result node must not become a real scientific source.
rep=Report(); check_links(rep,Atlas(f'### D2.L2 CLAIMS\n{phantom} CAND | fabricated fixture; not in submitted Atlas'),{'DYAD':source})
record('RV-N1b-denied-identifier-as-node','FAIL or explicitly unresolved, never PASS',rep,'No source claim exists, but generic first-table-cell recognition passes it.')
# Coverage fixture: scientific conclusion omitted but a dependency mention survives.
rid='DYAD-ALG-RAW-ANGULAR-MEAN'
src={'DYAD':f'`[ALG]` [RID: {rid}] Fixed-radius raw-frame mean has coefficient 47/54.', 'RER':'','METH':''}
positive=f'### D2.L2 CLAIMS\n{rid} ALG | fixed-radius raw-frame mean coefficient 47/54 | @DYAD§6.5'
rep=Report();check_coverage(rep,Atlas(positive),src,{})
record('RV-P1-explicit-claim-present','PASS',rep,'Positive control for the same source declaration.')
negative=f'### D2.L2 CLAIMS\n*FIXTURE:consumer OPEN | unidentified application | <{rid}'
rep=Report();check_coverage(rep,Atlas(negative),src,{})
record('RV-N2-missing-claim-dependency-left','FAIL/UNVERIFIED unless an explicit reviewed shared-home mapping resolves the claim',rep,'Only a bare dependency remains; there is no claim statement or a shared claim home.')
negative2=f'## L0 KEY\nIdentifiers considered: {rid}'
rep=Report();check_coverage(rep,Atlas(negative2),src,{})
record('RV-N2b-missing-claim-l0-left','FAIL (L0 identifier mention is not result coverage)',rep,'Atlas.kind treats L0 as node content and grants coverage.')
# Scope-marker limitation: supplemental, not an assertion of a new Atlas scientific error.
rid2='DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER'
src2={'DYAD':f'`[THM]` [assuming: RECOG-THM-R9-MEMORY] [RID: {rid2}] Remainder bound.'}
rep=Report();check_qualifiers(rep,Atlas(f'### D2.L2 CLAIMS\n{rid2} THM | unconditional bound'),src2)
record('RV-N3-marker-substring','FAIL for this fixture, or limit gate label strictly to a lexical marker test',rep,'The marker conditional is a substring of unconditional. This is a supplemental implementation limitation.')
Path(a.output).write_text(json.dumps({'scope':'Focused component fixtures; original repository not changed; no full-suite replay','results':rows},ensure_ascii=False,indent=2)+'\n')
for row in rows:
    print(row['id'], 'expected:',row['expected'], '\n ',row['observed'])
