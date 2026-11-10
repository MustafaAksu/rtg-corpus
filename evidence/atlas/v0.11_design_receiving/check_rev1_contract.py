#!/usr/bin/env python3
"""Bounded receiving controls for PR #202 implementation revision 1.

Usage: python3 -I check_rev1_contract.py TOOL.py OUTPUT.json
No production file is changed. Synthetic TEST identifiers are not owner RIDs.
Exit 1 denotes an unmet preservation-safety expectation, not a runtime error.
A changed context may be rejected or explicitly queued for review; byte equality
alone is not evidence that inherited scientific scope survived.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

EXPECTED_SHA256 = 'c78be1f29bae55642704bbeaaeef86c06b17983423a2c819ac8c2fe574a8b75a'
EXPECTED_BLOB = '67a16432b19e771d40e8d27f7b16130952929f54'

def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def pending(r: dict) -> int:
    return r['counts'].get('DECLARED_PENDING_REVIEW', 0)

def fail(r: dict) -> bool:
    return r['result'] == 'FAIL'

def clean(r: dict) -> bool:
    return r['result'] == 'MECHANICAL PASS' and pending(r) == 0

def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    tool, output = map(Path, sys.argv[1:])
    b = tool.read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
    if sha(b) != EXPECTED_SHA256 or blob != EXPECTED_BLOB:
        raise SystemExit('Tool identity mismatch; review the successor before changing pins.')
    spec = importlib.util.spec_from_file_location('upstream_atlas_preservation', tool)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    observations = []
    def run(cid, base, cand, mapping, expectation, predicate, observation=False):
        base, cand = base.encode(), cand.encode()
        mapping = {'base_sha256': sha(base), 'candidate_sha256': sha(cand), **mapping}
        r = mod.compare(base, cand, mapping)
        ok = bool(predicate(r))
        observations.append(dict(id=cid, kind="observation" if observation else "control", expected=expectation, matched=ok,
                                 base=base.decode(), candidate=cand.decode(), movement_map=mapping, report=r))
        print(cid, 'MATCH' if ok else 'MISMATCH', r['result'], r['counts'])

    simple = '# D\n## L2\nTEST-ALG-X ALG | x=1 | sc: q>0 | @TEST§1\n'
    run('P_IDENTITY', simple, simple, {}, 'MECHANICAL PASS; no pending items', clean)
    change = simple.replace('x=1', 'x=2')
    fmap = {'records': [{'base': 'TEST-ALG-X#1', 'cand': 'TEST-ALG-X#1', 'fields': [
        {'base_sha256': sha(b'x=1'), 'cand_sha256': sha(b'x=2'), 'reason': 'review required'}]}]}
    run('P_DECLARED_EDIT_PENDING', simple, change, fmap, 'one pending field, never exact preservation',
        lambda r: r['result'] == 'MECHANICAL PASS' and pending(r) == 1)
    run('P_IDENTITY_HASH_MISMATCH_REJECTED', simple, simple, {'base_sha256': '0'*64}, 'FAIL', fail)
    edge = '# D\nTEST-ALG-X ALG | imports | >GEN-ALG-A [gen-v1.0]; GEN-ALG-B [gen-v2.0]\n'
    swapped = edge.replace('gen-v1.0','TEMP').replace('gen-v2.0','gen-v1.0').replace('TEMP','gen-v2.0')
    run('P_INLINE_PIN_SWAP_REJECTED', edge, swapped,
        {'records': [{'base':'TEST-ALG-X#1','cand':'TEST-ALG-X#1'}]}, 'FAIL', fail)
    # Typed scope and opaque statements must remain associated, not just a multiset.
    scopes = '# D\n## L2\nTEST-ALG-X ALG | Local family | sc: q>0 | P(q) holds | sc: q<0 | R(q) holds | @TEST§1\n'
    moved = scopes.replace('sc: q>0 | P(q) holds | sc: q<0 | R(q) holds',
                           'sc: q<0 | P(q) holds | sc: q>0 | R(q) holds')
    run('N_FIELD_ORDER_BINDING', scopes, moved,
        {'records':[{'base':'TEST-ALG-X#1','cand':'TEST-ALG-X#1','reason':'match record, no field reorder declared'}]},
        'FAIL or explicit pending relation/order review, never all EXACT', lambda r: fail(r) or pending(r)>0)
    # A raw continuation is no safer than a typed premise. Same heading is insufficient.
    raw = '# D\nTEST-ALG-X ALG | P\nThe preceding claim requires q>0.\nTEST-ALG-Y ALG | R\n'
    moved = '# D\nTEST-ALG-X ALG | P\nTEST-ALG-Y ALG | R\nThe preceding claim requires q>0.\n'
    run('N_RAW_OWNER_BINDING', raw, moved, {},
        'FAIL: undeclared raw continuation moved to another claim', fail)
    context = '# Domain\n## Only for q>0\nTEST-THM-X THM | P(q) holds | @TEST§1\n## All real q\n'
    moved = '# Domain\n## Only for q>0\n## All real q\nTEST-THM-X THM | P(q) holds | @TEST§1\n'
    run('O_CONTEXT_CHANGE_IS_ONLY_A_BYTE_MOVE', context, moved,
        {'records':[{'base':'TEST-THM-X#1','cand':'TEST-THM-X#1','reason':'regroup'}]},
        'Documented behavior: MAPPED_EXACT with no pending item; separate context review remains necessary',
        lambda r: clean(r) and r['counts'].get('MAPPED_EXACT')==1, observation=True)
    # Same protected identity cannot evade an unconditional invariant by routing through delete+insert.
    node = '# D\nTEST-ALG-X ALG | Local result | @TEST§1\n'
    route = {'records':[{'base':'TEST-ALG-X#1','cand':None,'reason':'remove row'}],
             'inserts':[{'cand':'TEST-ALG-X#1','reason':'insert row'}]}
    run('N_GRADE_DELETE_INSERT_ROUTE', node, node.replace('ALG |','THM |'), route,
        'FAIL under the documented hard grade invariant', fail)
    diag = '# D\nF1 D-PROOF | evidence unavailable\n'
    route = {'records':[{'base':'F1#1','cand':None,'reason':'remove row'}],
             'inserts':[{'cand':'F1#1','reason':'insert row'}]}
    run('N_DIAGNOSTIC_DELETE_INSERT_ROUTE', diag, diag.replace('D-PROOF','D-LINK'), route,
        'FAIL under the documented hard diagnostic-class invariant', fail)
    # A declared permutation under the SAME complete context remains useful and permitted.
    order = '# D\n## L2\nTEST-ALG-X ALG | P\nTEST-ALG-Y ALG | R\n'
    moved = '# D\n## L2\nTEST-ALG-Y ALG | R\nTEST-ALG-X ALG | P\n'
    run('P_SAME_CONTEXT_MAPPED_MOVE', order, moved,
        {'records':[{'base':'TEST-ALG-X#1','cand':'TEST-ALG-X#1','reason':'same context regroup'}]},
        'MECHANICAL PASS; no pending; one MAPPED_EXACT',
        lambda r: clean(r) and r['counts'].get('MAPPED_EXACT')==1)
    raw = '# D\nTEST-ALG-X ALG | α=1 | sc: q>0\n'.encode().replace(b'\n',b'\r\n')
    ex = mod.extract(raw)
    slices=[raw[r['span'][0]:r['span'][1]] for r in ex['regions']]
    ok = ex['source_sha256']==sha(raw) and b'\n'.join(slices)==raw
    ok = ok and all(sha(raw[f['span'][0]:f['span'][1]])==f['sha256'] for r in ex['regions'] for f in r.get('fields',[]))
    observations.append(dict(id='P_UTF8_CRLF_BINDING', expected='raw identity and all byte slices; implicit LF reconstruction', matched=ok))
    print('P_UTF8_CRLF_BINDING','MATCH' if ok else 'MISMATCH')
    headings = '# D\n### Branch A\nTEST-ALG-X ALG | P\n### Branch B\nTEST-ALG-Y ALG | Q\n'.encode()
    ex=mod.extract(headings)
    y=next(r for r in ex['regions'] if r.get('id')=='TEST-ALG-Y')
    expected=[sha(b'# D')[:16],sha(b'### Branch B')[:16]]
    ok=y['context']==expected
    observations.append(dict(id='N_SKIPPED_LEVEL_SIBLING_CONTEXT', expected=expected,
                             observed=y['context'], matched=ok,
                             reason='Branch A and Branch B are level-3 siblings, not nested.'))
    print('N_SKIPPED_LEVEL_SIBLING_CONTEXT','MATCH' if ok else 'MISMATCH',y['context'])
    controls=[x for x in observations if x.get('kind','control')=='control']
    count=sum(x['matched'] for x in controls)
    report=dict(status='SESSION bounded receiving test, no owner-science or Atlas-release validation',
                date='2026-11-10', python=sys.version.split()[0], tool_sha256=sha(b), tool_blob=blob,
                tool_bytes=len(b), cases=observations, matched=count, total=len(controls), observation_count=len(observations)-len(controls))
    with output.open('x',encoding='utf-8') as f:
        json.dump(report,f,ensure_ascii=False,indent=2);f.write('\n')
    print('CONTROLS MATCHED',count,'/',len(controls),'OBSERVATIONS',len(observations)-len(controls))
    return int(count!=len(controls))

if __name__=='__main__':
    sys.exit(main())
