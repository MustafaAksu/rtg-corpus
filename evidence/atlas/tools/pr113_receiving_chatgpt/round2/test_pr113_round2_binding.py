#!/usr/bin/env python3
"""Bounded round-2 receiving controls for PR #113 (SESSION; no owner science).

Requires the unchanged round-2 producer fixture module and the checker under review.
Every candidate is derived exactly from its movement map. The two negative cases
exercise the already-requested source-operation and history-target binding for
relocate_hashes. Exit 1 means a safety-expectation mismatch, not a runtime error.
"""
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def cases(f):
    # P: an actual live deletion declares the hash, which enters the history region.
    yield ('P_DECLARED', 'PASS', 'Declared live deletion to actual history',
           f.base_text(), f.ops('', f.new_appendix(), [f.DRAFTP]))
    # N: the live deletion is undeclared; the same hash already occurs in history.
    base = f.base_text().replace(
        'Many words of history.',
        f'Many words of history. Previous draft `{f.DRAFT}`.')
    ops = f.ops('', f.new_appendix(), [f.DRAFTP], relocate=False)
    ops[-1]['relocate_hashes'] = [f.DRAFT]
    yield ('N_WRONG_OPERATION', 'FAIL',
           'Declaration on history rewrite that retains the hash; live deletion has none',
           base, ops)
    # N: a valid live deletion declares the hash but its only target is the footer.
    new = f.new_appendix().replace(f'; draft `{f.DRAFT}`', '').replace(
        '*END OF DOCUMENT — RTG_TEST_DSN_v0.2*',
        f'*END OF DOCUMENT — RTG_TEST_DSN_v0.2 — draft `{f.DRAFT}`*')
    yield ('N_FOOTER_TARGET', 'FAIL', 'Hash occurs only in footer, not history region',
           f.base_text(), f.ops('', new, [f.DRAFTP]))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--fixtures', type=Path, required=True)
    p.add_argument('--checker', type=Path, required=True)
    p.add_argument('--report', type=Path, required=True)
    args = p.parse_args()
    spec = importlib.util.spec_from_file_location('producer_fixtures', args.fixtures.resolve())
    f = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(f)
    report = {'review_date': '2026-10-30', 'python': sys.version.split()[0],
              'checker_sha256': digest(args.checker.read_bytes()),
              'fixture_sha256': digest(args.fixtures.read_bytes()), 'cases': []}
    print('CHECKER', report['checker_sha256'])
    print('FIXTURES', report['fixture_sha256'])
    mismatches = 0
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        for cid, expected, description, base, operations in cases(f):
            operations = copy.deepcopy(operations)
            candidate = f.derive(base, operations)
            bp, cp, mp, rp = [root / x for x in ('base.md', 'candidate.md', 'map.json', 'result.json')]
            bp.write_bytes(base.encode('utf-8'))
            cp.write_bytes(candidate.encode('utf-8'))
            mapping = {'base_sha256': digest(bp.read_bytes()),
                       'candidate_sha256': digest(cp.read_bytes()),
                       'archives': [{'name': 'base', 'path': str(bp), 'sha256': digest(bp.read_bytes())}],
                       'profile': {'history_appendix': 'C', 'history_words': ['v0.9']},
                       'operations': operations}
            mp.write_text(json.dumps(mapping, ensure_ascii=False, indent=2), encoding='utf-8')
            rp.unlink(missing_ok=True)
            run = subprocess.run([sys.executable, '-I', str(args.checker.resolve()),
                                  str(bp), str(cp), str(mp), '--report', str(rp)],
                                 capture_output=True, text=True, timeout=30)
            result = json.loads(rp.read_text(encoding='utf-8')) if rp.exists() else {}
            observed = result.get('result', 'ERROR')
            matched = observed == expected and run.returncode == {'PASS': 0, 'FAIL': 1}[expected]
            mismatches += not matched
            row = {'id': cid, 'description': description, 'expected': expected,
                   'observed': observed, 'exit_code': run.returncode, 'matched': matched,
                   'base_sha256': digest(bp.read_bytes()), 'candidate_sha256': digest(cp.read_bytes()),
                   'checks': result.get('checks', []), 'stderr': run.stderr}
            report['cases'].append(row)
            print(cid, 'expected', expected, 'observed', observed, 'MATCH' if matched else 'MISMATCH')
            for check in row['checks']:
                if check['check'] in ('history appendix region', 'source hashes preserved in live text'):
                    print(' ', check['result'], check['check'], '—', check['detail'])
    report['mismatches'] = mismatches
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('MISMATCHES', mismatches)
    return int(mismatches != 0)


if __name__ == '__main__':
    sys.exit(main())
