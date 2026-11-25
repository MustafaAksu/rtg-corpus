#!/usr/bin/env python3
"""Bounded PR #202 rev.2 readback: unchanged suites plus two paired route checks.

Usage: python3 -I check_compound_routes.py TOOL.py PRIOR_HARNESS.py NEW_OUTPUT_DIR
Synthetic TEST identifiers are not owner RIDs. Inputs are read-only. Only the
prior harness's two identity constants are reassigned in memory. Exit 1 means
an unmet receiving expectation, not a runtime failure or scientific disproof.
"""
from __future__ import annotations
import contextlib
from datetime import datetime, timezone
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys

TOOL_SHA256 = 'c6e6660b4d57c39a81bda9ad5c476db684ee74c962794a58cae2e1a9d5fed0e1'
TOOL_BLOB = 'dda7d60000267442708e3030911f45223be03c6a'
PRIOR_SHA256 = '39b1441121c74f184428fcb302b04beeb87a2a0c4adb7321bd455258681554ea'
PRIOR_BLOB = '66881e777f2d7ca9e2021d81c720c070c778da4a'


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def checked_module(path: Path, digest: str, blob: str, name: str):
    data = path.read_bytes()
    actual_blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    if sha(data) != digest or actual_blob != blob:
        raise ValueError(f'{name}: source identity mismatch')
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, len(data)


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(__doc__)
    tool_path, prior_path, out = map(Path, sys.argv[1:])
    tool, size = checked_module(tool_path, TOOL_SHA256, TOOL_BLOB, 'reviewed_tool')
    prior, _ = checked_module(prior_path, PRIOR_SHA256, PRIOR_BLOB, 'unchanged_prior_harness')
    out.mkdir(parents=True, exist_ok=False)
    started = datetime.now(timezone.utc).isoformat()
    print('[SESSION] PR202 rev2 receiving execution', started)
    print('PYTHON', sys.version.split()[0])
    print('TOOL', TOOL_SHA256, 'BLOB', TOOL_BLOB, 'BYTES', size)
    print('PRIOR_HARNESS', PRIOR_SHA256, 'BLOB', PRIOR_BLOB)
    producer = subprocess.run([sys.executable, '-I', str(tool_path), 'selftest'],
                              capture_output=True, text=True, timeout=30)
    print('\n=== PRODUCER SELFTEST (UNCHANGED) ===')
    print(producer.stdout, end='')
    if producer.stderr:
        print(producer.stderr, end='')
    print('SELFTEST_EXIT', producer.returncode)
    (out / 'producer_stdout.txt').write_text(producer.stdout + producer.stderr, encoding='utf-8')

    prior.EXPECTED_SHA256 = TOOL_SHA256
    prior.EXPECTED_BLOB = TOOL_BLOB
    argv = sys.argv[:]
    capture = io.StringIO()
    try:
        sys.argv = [str(prior_path), str(tool_path), str(out / 'prior_results.json')]
        with contextlib.redirect_stdout(capture):
            prior_exit = prior.main()
    finally:
        sys.argv = argv
    print('\n=== PRIOR 11 CONTROLS + OBSERVATION (CASES UNCHANGED) ===')
    print(capture.getvalue(), end='')
    print('PRIOR_EXIT', prior_exit)
    (out / 'prior_stdout.txt').write_text(capture.getvalue(), encoding='utf-8')

    cases = []
    def check(cid, base, candidate, mapping, expected, predicate):
        b, c = base.encode(), candidate.encode()
        mapping = dict(mapping, base_sha256=sha(b), candidate_sha256=sha(c))
        result = tool.compare(b, c, mapping)
        matched = bool(predicate(result, b, c))
        cases.append(dict(id=cid, expected=expected, matched=matched,
                          base=base, candidate=candidate, movement_map=mapping, report=result))
        print(cid, 'MATCH' if matched else 'MISMATCH', result['result'], result['counts'],
              'context_reviews', len(result['obligations']['context_reviews']))

    print('\n=== PAIRED CONTEXT / FIELD-CONSUMPTION ROUTES ===')
    base = '# Domain\n## Only for q>0\nTEST-THM-X THM | P(q) holds | @TEST§1\n## All real q\n'
    moved = '# Domain\n## Only for q>0\n## All real q\nTEST-THM-X THM | P(q) holds | @TEST§1\n'
    mapping = {'records': [{'base': 'TEST-THM-X#1', 'cand': 'TEST-THM-X#1',
                            'reason': 'regroup; no scientific edit'}]}
    def has_context_obligation(r, b, c):
        before = next(x for x in tool.extract(b)['regions'] if x.get('id') == 'TEST-THM-X')
        after = next(x for x in tool.extract(c)['regions'] if x.get('id') == 'TEST-THM-X')
        return any(x.get('item') == 'TEST-THM-X#1'
                   and x.get('base_context') == before['context']
                   and x.get('candidate_context') == after['context']
                   for x in r['obligations']['context_reviews'])
    check('P_EXACT_CONTEXT_QUEUE', base, moved, mapping,
          'MAPPED_EXACT plus the correct old/new context obligation',
          lambda r, b, c: r['result'] == 'MECHANICAL PASS'
          and r['counts'].get('MAPPED_EXACT') == 1 and has_context_obligation(r, b, c))
    check('N_WHITESPACE_CONTEXT_BYPASS', base,
          moved.replace('TEST-THM-X THM |', 'TEST-THM-X THM  |'), mapping,
          'FAIL or the same context obligation; whitespace cannot erase inherited-scope review',
          lambda r, b, c: r['result'] == 'FAIL' or has_context_obligation(r, b, c))

    base = '# D\nTEST-ALG-X ALG | local | sc: q>0 | sc: q<0 | @T§1\n'
    mapping = {'records': [{'base': 'TEST-ALG-X#1', 'cand': 'TEST-ALG-X#1', 'fields': [
        {'base_sha256': sha(b'sc: q>0'), 'cand_sha256': sha(b'sc: q<0'),
         'reason': 'edit the first scope only; no deletion or deduplication declared'}]}]}
    check('P_DISTINCT_REPLACEMENT_OCCURRENCES', base, base.replace('sc: q>0', 'sc: q<0'), mapping,
          'pending edit and separate unchanged scope both have distinct target occurrences',
          lambda r, b, c: r['result'] == 'MECHANICAL PASS'
          and r['counts'].get('DECLARED_PENDING_REVIEW') == 1)
    check('N_REPLACEMENT_TARGET_DOUBLE_USE', base, base.replace(' | sc: q>0', ''), mapping,
          'FAIL: one target occurrence cannot satisfy both an edit and an unchanged source field',
          lambda r, b, c: r['result'] == 'FAIL')
    matched = sum(x['matched'] for x in cases)
    prior_report = json.loads((out / 'prior_results.json').read_text(encoding='utf-8'))
    report = dict(status='SESSION bounded tool review; not Atlas compaction or owner-science acceptance',
                  started_utc=started, python=sys.version.split()[0], tool_sha256=TOOL_SHA256,
                  tool_blob=TOOL_BLOB, tool_bytes=size, prior_harness_sha256=PRIOR_SHA256,
                  producer_exit=producer.returncode, prior_exit=prior_exit,
                  prior_matched=prior_report['matched'], prior_total=prior_report['total'],
                  prior_observations=prior_report['observation_count'],
                  compound_matched=matched, compound_total=len(cases), cases=cases)
    (out / 'compound_results.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print('COMPOUND_MATCHED', matched, '/', len(cases))
    code = int(producer.returncode != 0 or prior_exit != 0 or matched != len(cases))
    print('RECEIVING_EXIT', code)
    return code


if __name__ == '__main__':
    sys.exit(main())
