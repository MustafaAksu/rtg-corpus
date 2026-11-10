#!/usr/bin/env python3
"""SESSION receiving controls for CCP113-R2: metadata cannot authorize live deletion.

Run against PR #113 round 3, with its unchanged producer fixture module.
Only temporary files are written. Exit 1 indicates an expectation mismatch.
The paired positives retain the same metadata edits but put relocate_hashes on
its actual live-removal operation. No owner-science certificate is executed.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile

CHECKER_SHA256 = 'd2977b3e24fd54a1d85fe53ea88f65dd51a9e26890b56b17ab5855716b57d87c'
FIXTURE_SHA256 = '45c3cbb5d28d550f2ddae00620b4c759c6aefa51384588c87b6977f951f78ec7'

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def derive(text: str, operations: list[dict]) -> str:
    for op in operations:
        if op['op'] == 'replace-header':
            text = op['new'] + text[text.index('\n## '):]
        elif op['op'] == 'replace-footer':
            start = text.index('*END OF DOCUMENT')
            assert start == 0 or text[start - 1] == '\n'
            text = text[:start] + op['new']
        elif op['op'] == 'edit':
            assert text.count(op['old']) == 1
            text = text.replace(op['old'], op['new'])
        elif op['op'] == 'replace-section':
            assert text.count(op['start']) == 1
            start = text.index(op['start'])
            end = text.index(op['end'], start + len(op['start'])) if op.get('end') else len(text)
            text = text[:start] + op['new'] + text[end:]
        else:
            raise ValueError(op['op'])
    return text

def cases(f):
    metadata = f'**Historical draft:** `{f.DRAFT}`\n'
    base = f.base_text().replace('**Status summary:**', metadata + '**Status summary:**')
    old_header = base[:base.index('\n## ')]
    for valid in (True, False):
        header = {'id': 'HEADER', 'op': 'replace-header', 'archive': ['base'],
                  'new': old_header.replace(metadata, '')}
        ops = [header, *f.ops('', f.new_appendix(), [f.DRAFTP], relocate=valid)]
        if not valid:
            header['relocate_hashes'] = [f.DRAFT]
        yield ('P_HEADER_LIVE_DECL' if valid else 'N_HEADER_AUTHORIZATION',
               'PASS' if valid else 'FAIL', base, ops)
    ordinary_footer = '*END OF DOCUMENT — RTG_TEST_DSN_v0.2*\n'
    metadata_footer = f'*END OF DOCUMENT — RTG_TEST_DSN_v0.2 — draft `{f.DRAFT}`*\n'
    base = f.base_text().replace(ordinary_footer, metadata_footer)
    history = f.new_appendix().replace(ordinary_footer, metadata_footer)
    for valid in (True, False):
        footer = {'id': 'FOOTER', 'op': 'replace-footer', 'archive': ['base'], 'new': ordinary_footer}
        ops = [*f.ops('', history, [f.DRAFTP], relocate=valid), footer]
        if not valid:
            footer['relocate_hashes'] = [f.DRAFT]
        yield ('P_FOOTER_LIVE_DECL' if valid else 'N_FOOTER_AUTHORIZATION',
               'PASS' if valid else 'FAIL', base, ops)

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--checker', type=Path, required=True)
    p.add_argument('--fixtures', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    for path, expected in [(a.checker, CHECKER_SHA256), (a.fixtures, FIXTURE_SHA256)]:
        if sha(path.read_bytes()) != expected:
            raise SystemExit(f'Input identity mismatch: {path}')
    spec = importlib.util.spec_from_file_location('producer_fixtures', a.fixtures.resolve())
    f = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(f)
    a.out.mkdir(parents=True, exist_ok=False)
    report = {'date': '2026-11-09', 'python': sys.version.split()[0],
              'checker_sha256': CHECKER_SHA256, 'fixture_sha256': FIXTURE_SHA256, 'cases': []}
    with tempfile.TemporaryDirectory() as td:
        for cid, expected, base, original_ops in cases(f):
            ops = copy.deepcopy(original_ops)
            candidate = derive(base, ops)
            tmp = Path(td)
            bp, cp, mp, rp = [tmp / n for n in ('base.md', 'candidate.md', 'map.json', 'result.json')]
            bp.write_bytes(base.encode('utf-8')); cp.write_bytes(candidate.encode('utf-8'))
            mapping = {'base_sha256': sha(bp.read_bytes()), 'candidate_sha256': sha(cp.read_bytes()),
                       'archives': [{'name': 'base', 'path': str(bp), 'sha256': sha(bp.read_bytes())}],
                       'profile': {'history_appendix': 'C', 'history_words': ['v0.9']}, 'operations': ops}
            mp.write_text(json.dumps(mapping, ensure_ascii=False, indent=2), encoding='utf-8')
            rp.unlink(missing_ok=True)
            r = subprocess.run([sys.executable, '-I', str(a.checker.resolve()), str(bp), str(cp), str(mp), '--report', str(rp)],
                               capture_output=True, text=True, timeout=30)
            checked = json.loads(rp.read_text(encoding='utf-8')) if rp.exists() else {}
            observed = checked.get('result', 'ERROR')
            ok = observed == expected and r.returncode == {'PASS': 0, 'FAIL': 1}[expected]
            row = {'id': cid, 'expected': expected, 'observed': observed, 'exit_code': r.returncode,
                   'matched': ok, 'checks': checked.get('checks', []), 'stderr': r.stderr}
            report['cases'].append(row)
            print(f'{cid}: expected {expected}, observed {observed}, exit {r.returncode}, {"MATCH" if ok else "MISMATCH"}')
            for item in row['checks']:
                if item['check'] == 'source hashes preserved in live text':
                    print(' ', item['result'], item['detail'])
            (a.out / f'{cid}.stdout.txt').write_text(r.stdout, encoding='utf-8')
    bad = sum(not row['matched'] for row in report['cases'])
    report['mismatches'] = bad
    (a.out / 'results.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('MISMATCHES', bad)
    return int(bad != 0)

if __name__ == '__main__':
    sys.exit(main())
