#!/usr/bin/env python3
"""Bounded PR190 round-2 receiving check; original contracts plus boundary cases.

No live Git/GitHub calls: use the original independently hash-pinned fixture
harness, unchanged except its two target-identity constants set in memory.
All file-output tests are confined to temporary directories. Exit 1 means an
existing R1/R2/R4 contract remains unmet, not a harness failure.
"""
from __future__ import annotations
import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
from types import ModuleType
from unittest.mock import patch

TOOL_SHA = 'dfbcb1da0a7ac4d3ec942cae4a125875caa1030ddebd103821bf5c75b0c5cd0c'  # pin moved to rev. 3
TOOL_BLOB = '6848b4f0c15713f6063be797a396f066f4dafa06'
HARNESS_SHA = 'f585abf7f23ebcbabcd2621795ffebb3dc7625e62ed636e6ad9af8c970762681'


def load_harness(path: Path):
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != HARNESS_SHA:
        raise SystemExit('Unexpected baseline harness; refusing to alter its tests')
    spec = importlib.util.spec_from_file_location('orient_baseline_harness', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.EXPECTED, module.BLOB = TOOL_SHA, TOOL_BLOB
    return module


def public_observation(r):
    report = r.get('report')
    return {
        'status': report.get('status') if report else None,
        'unverified': report.get('unverified') if report else None,
        'release_record': report.get('governing', {}).get('release_record') if report else None,
        'pipes': report.get('pipes') if report else None,
        'stdout': r.get('stdout'),
        'exception': r.get('exception'),
    }


def dangling_output(source: bytes, h):
    module = ModuleType('orient_dangling_output')
    module.__file__ = 'orient.py'
    exec(compile(source, 'orient.py', 'exec'), module.__dict__)
    fixture = h.Fixture()
    stream = io.StringIO()
    error = None
    with tempfile.TemporaryDirectory(prefix='orient-r2-symlink-') as tmp:
        root = Path(tmp)
        source_target = root / 'atlas' / 'RTG_STATE_ATLAS.md'
        source_target.parent.mkdir()
        output = root / 'observation.json'
        output.symlink_to(source_target)
        assert output.is_symlink() and not source_target.exists()
        with patch.object(module.subprocess, 'run', fixture.run), \
             patch.object(sys, 'argv', ['orient.py', 'ATLAS', '--json', str(output)]), \
             contextlib.redirect_stdout(stream):
            try:
                module.main()
            except Exception as exc:
                error = f'{type(exc).__name__}: {exc}'
        created = source_target.exists()
        report = json.loads(source_target.read_text()) if created else None
        return {'report': report, 'stdout': stream.getvalue(), 'exception': error,
                'source_target_created': created, 'output_is_symlink': output.is_symlink()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tool', type=Path, required=True)
    ap.add_argument('--harness', type=Path, default=Path(__file__).with_name('test_orient_receiving.py'))
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    source = args.tool.read_bytes()
    sha = hashlib.sha256(source).hexdigest()
    blob = hashlib.sha1(b'blob ' + str(len(source)).encode() + b'\0' + source).hexdigest()
    if (sha, blob) != (TOOL_SHA, TOOL_BLOB):
        raise SystemExit('Unexpected reporter bytes')
    h = load_harness(args.harness)
    args.out.mkdir(parents=True, exist_ok=True)

    # Run all 21 original tests, with no fixture or predicate changes.
    baseline_stdout = io.StringIO()
    baseline_exit = None
    with patch.object(sys, 'argv', [str(args.harness), '--tool', str(args.tool), '--out', str(args.out / 'baseline')]), \
         contextlib.redirect_stdout(baseline_stdout):
        try:
            h.main()
        except SystemExit as exc:
            baseline_exit = exc.code
    (args.out / 'baseline_stdout.txt').write_text(baseline_stdout.getvalue(), encoding='utf-8')
    base = json.loads((args.out / 'baseline' / 'results.json').read_text())
    print(f'BASELINE: {base["passed"]}/{base["cases"]} PASS; {base["failed"]} FAIL; exit={baseline_exit}')

    extras = []
    def save(key, name, r, ok):
        obs = public_observation(r)
        obs.update({k:r[k] for k in ('source_target_created', 'output_is_symlink') if k in r})
        extras.append({'id': key, 'name': name, 'contract_pass': bool(ok), 'observation': obs})
        print(f'{key}: {"PASS" if ok else "FAIL"} — {name}; status={obs["status"]}; exception={obs["exception"]}')

    record_body = '**Status:** PI ACCEPTED\n' + h.FILE_HASH + '\n'
    patch_record = h.RECORD.replace('v0.10_', 'v0.10.1_')
    r = h.run_one(source, {'records': {patch_record: record_body}})
    save('R2-E1', 'v0.10 must not use the v0.10.1 release record', r,
         h.partial(r) and not r['report']['governing']['release_record'])

    r = h.run_one(source, {'records': {patch_record: record_body, h.RECORD: record_body}})
    save('R2-E2', 'exact v0.10 record with adjacent v0.10.1 is unambiguous', r,
         h.complete(r) and r['report']['governing']['release_record'] == [h.RECORD])

    # Enumerating succeeds; a known file fails to read. Counts must not imply zero.
    old_run = h.Fixture.run
    def read_failure(self, argv, **kw):
        if list(argv) == ['git', 'show', f'origin/main:{h.PIPE}']:
            raise subprocess.CalledProcessError(1, argv, stderr='fixture individual pipe read denied')
        return old_run(self, argv, **kw)
    with patch.object(h.Fixture, 'run', read_failure):
        r = h.run_one(source, {})
    pipes = r['report']['pipes'] if r['report'] else {}
    field_partial = pipes.get('inbox') is None or pipes.get('complete') is False or pipes.get('inbox_complete') is False
    save('R1-E1', 'failed individual pipe read is not an observed empty inbox', r,
         h.partial(r) and field_partial and 'inbox: none' not in r['stdout'])

    r = dangling_output(source, h)
    save('R4-E1', 'default --json must refuse a dangling symlink destination', r,
         not r['source_target_created'])

    # Positive controls: supported underscore filename, and genuine ambiguity.
    underscored = h.RECORD.replace('v0.10_', 'v0_10_')
    r = h.run_one(source, {'records': {underscored: record_body}})
    save('R2-P1', 'exact underscore-format v0_10 record remains supported', r,
         h.complete(r) and r['report']['governing']['release_record'] == [underscored])

    r = h.run_one(source, {'records': {h.RECORD: record_body, underscored: record_body}})
    save('R2-P2', 'two actual representations of the same release flag ambiguity', r,
         h.partial(r) and len(r['report']['governing']['release_record']) == 2)

    result = {
        'python': platform.python_version(), 'mode': 'offline unchanged reporter; deterministic subprocess fixtures',
        'tool_sha256': sha, 'tool_git_blob': blob, 'tool_bytes': len(source),
        'baseline_harness_sha256': HARNESS_SHA,
        'baseline': {'cases':base['cases'], 'passed':base['passed'], 'failed':base['failed'], 'exit':baseline_exit},
        'additional': {'cases':len(extras), 'passed':sum(x['contract_pass'] for x in extras),
                       'failed':sum(not x['contract_pass'] for x in extras)},
        'cases': extras,
    }
    (args.out / 'round2_summary.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(f'ADDITIONAL: {result["additional"]["passed"]}/{len(extras)} PASS; {result["additional"]["failed"]} FAIL')
    raise SystemExit(1 if result['additional']['failed'] or base['failed'] else 0)

if __name__ == '__main__':
    main()
