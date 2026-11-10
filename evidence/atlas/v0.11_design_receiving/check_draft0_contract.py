#!/usr/bin/env python3
"""PR #202 draft-0 design probes; observations, not a nonexistent comparator's verdict.

Run: python3 -I check_draft0_contract.py EXTRACTOR OUTPUT_JSON
The byte-pinned upstream extractor is loaded without modification. Synthetic TEST
identifiers below are fixtures, not scientific owner RIDs. Exit 0 means these
reported draft-0 observations were reproduced, not that preservation is certified.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile

EXTRACTOR_SHA = '5809873f739e144e042b51330ce8511d2eaee7f581090cf3db4f078a27b3b9b2'
EXTRACTOR_BLOB = 'f98ceec30f6c46e6daa9dffc78d461f2f81344a3'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    source, destination = map(Path, sys.argv[1:])
    raw = source.read_bytes()
    assert digest(raw) == EXTRACTOR_SHA
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    assert blob == EXTRACTOR_BLOB
    spec = importlib.util.spec_from_file_location('upstream_draft0', source.resolve())
    draft = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(draft)
    rows = []

    def observe(name, observed, **details):
        assert observed, name
        rows.append(dict(id=name, reproduced=observed, **details))

    def node(text):
        return draft.parse('TEST-ALG-X ALG | ' + text)[0]

    def signature(field):
        # The draft document proposes *multiset* equality for these features.
        return {key: sorted(field.get(key) or [])
                for key in ('rids', 'pins', 'markers', 'numbers')}

    line = 'TEST-ALG-X ALG | α=1 | sc: q>0 | ¬global'
    fields = draft.parse(line)[0]['fields']
    char_checks = [digest(line[a:b].encode()) == f['sha256']
                   for f in fields for a, b in [f['span']]]
    byte_checks = [digest(line.encode()[a:b]) == f['sha256']
                   for f in fields for a, b in [f['span']]]
    observe('BYTE_SPAN_UNITS', all(char_checks) and not any(byte_checks),
            declared='byte spans', actual='Unicode code-point offsets',
            spans=[f['span'] for f in fields], char_checks=char_checks,
            byte_checks=byte_checks)

    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        b = b'# Context\r\nTEST-ALG-X ALG | x=1\r\n'
        inp, out = root / 'source.md', root / 'manifest.json'
        inp.write_bytes(b)
        run = subprocess.run([sys.executable, '-I', str(source.resolve()),
                              str(inp), str(out)], capture_output=True, text=True,
                             timeout=20, check=True)
        declared = json.loads(out.read_text())['summary']['source_sha256']
        observe('RAW_SOURCE_CRLF_IDENTITY',
                declared != digest(b) and declared == digest(b.replace(b'\r\n', b'\n')),
                actual_sha256=digest(b), reported_sha256=declared,
                subprocess_exit=run.returncode)

    for cid, a, b in (
        ('OPERATOR_NOT_CAPTURED', 'q<1', 'q>1'),
        ('NUMBER_ROLE_NOT_CAPTURED', 'x=1,y=2', 'x=2,y=1'),
    ):
        fa, fb = node(a)['fields'][0], node(b)['fields'][0]
        observe(cid, signature(fa) == signature(fb) and fa['sha256'] != fb['sha256'],
                left=a, right=b, identical_signature=signature(fa),
                raw_hashes_differ=True)

    a = '<DYAD-ALG-X [dyad-v1.0]; GEN-ALG-Y [gen-v2.0]'
    b = '<DYAD-ALG-X [gen-v2.0]; GEN-ALG-Y [dyad-v1.0]'
    fa, fb = node('test | ' + a)['fields'][1], node('test | ' + b)['fields'][1]
    observe('EDGE_PIN_ASSOCIATION_NOT_CAPTURED', signature(fa) == signature(fb)
            and fa['sha256'] != fb['sha256'], left=a, right=b,
            identical_signature=signature(fa), raw_hashes_differ=True)

    a, b = '<DYAD-ALG-X DYAD-ALG-X', '<DYAD-ALG-X'
    fa, fb = node('test | ' + a)['fields'][1], node('test | ' + b)['fields'][1]
    observe('RID_MULTIPLICITY_COLLAPSED', fa['rids'] == fb['rids']
            and fa['sha256'] != fb['sha256'], left=a, right=b,
            left_rids=fa['rids'], right_rids=fb['rids'])

    text = '# Global scope: formal only\nTEST-THM-X THM | If H holds, P follows.\n'
    recs = draft.parse(text)
    observe('CONDITION_FLAG_IS_SYNTAX_ONLY', recs[0]['conditional'] is False
            and recs[0]['fields'][0]['cls'] == 'statement',
            conditional=recs[0]['conditional'], statement='If H holds, P follows.',
            interpretation='No syntactic flag is not proof of unconditionality.')
    observe('HEADING_HAS_NO_SOURCE_SPAN', len(recs) == 1 and recs[0]['line'] == 2
            and 'Global scope: formal only' == recs[0]['section'],
            content_lines=[r['line'] for r in recs], section_string=recs[0]['section'],
            interpretation='Heading is context text, not an independently hash-bound source region.')

    # Identical raw text can survive under an unrelated owner. Raw membership is
    # not a sufficient Tier-B preservation rule; no comparator is invoked here.
    base = 'TEST-ALG-X ALG | first | only on q>0\nTEST-ALG-Y ALG | second\n'
    cand = 'TEST-ALG-X ALG | first\nTEST-ALG-Y ALG | second | only on q>0\n'
    rb, rc = draft.parse(base), draft.parse(cand)
    ub = next(f for f in rb[0]['fields'] if f['cls'] == 'UNVERIFIED')
    uc = next(f for f in rc[1]['fields'] if f['cls'] == 'UNVERIFIED')
    observe('TIER_B_REQUIRES_OWNER_BINDING', ub['sha256'] == uc['sha256']
            and rb[0]['id'] != rc[1]['id'], source_owner=rb[0]['id'],
            target_owner=rc[1]['id'], unchanged_untyped_hash=ub['sha256'])

    # Ordered occurrences survive extraction, but set-only compare would miss loss.
    duplicate = draft.parse('TEST-ALG-X ALG | left\nTEST-ALG-X ALG | right\n')
    single = draft.parse('TEST-ALG-X ALG | left\n')
    observe('NODE_SET_DOES_NOT_PRESERVE_OCCURRENCES',
            {r['id'] for r in duplicate} == {r['id'] for r in single}
            and len(duplicate) != len(single), before=len(duplicate), after=len(single),
            identical_id_set=sorted({r['id'] for r in duplicate}))

    report = dict(status='SESSION design observations; no comparator run',
                  date='2026-11-10', python=sys.version.split()[0],
                  extractor_sha256=digest(raw), extractor_blob=blob,
                  extractor_bytes=len(raw), observations=rows,
                  observation_count=len(rows), all_reproduced=True,
                  not_run=['whole Atlas extraction', 'compare stage (not implemented)',
                           'owner scientific certificates'])
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
