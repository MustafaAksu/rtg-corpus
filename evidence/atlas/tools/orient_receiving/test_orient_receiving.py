#!/usr/bin/env python3
"""Offline receiving checks of PR #190's unmodified orient.py.

The script under review is byte/hash pinned. Only subprocess responses are
replaced with deterministic Git/GitHub fixtures. No live network or repository
writes are performed. A temporary sentinel tests the optional JSON destination.
Run: python3 -I test_orient_receiving.py --tool PATH --out OUTPUT_DIRECTORY
Exit 1 means one or more safety/coverage contracts failed, not a harness crash.
"""
from __future__ import annotations
import argparse
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from types import ModuleType
from unittest.mock import patch
from urllib.parse import parse_qs

EXPECTED = '0a42698cdf50f71173a3ac930ad7e07498b8c204c5f0b9331e78171977f517bb'
BLOB = '1365d748a18383746df00aaa97ee57414e2a79ef'
MAIN = 'a' * 40
TARGET = 'b' * 40
SOURCE = b'# Synthetic Atlas input for a receiving test\n'
FILE_HASH = hashlib.sha256(SOURCE).hexdigest()
RECORD = 'records/atlas/RTG_STATE_ATLAS_v0.10_RELEASE_RECORD.md'
PIPE = 'pipes/ATLAS/20261106-DYAD-fixture.md'
PIPE_TEXT = '---\nfrom: DYAD\nto: ATLAS\ndate: 2026-11-06\nkind: notice\nstate: closed\n---\nSynthetic test.\n'

def pr(n: int, paths: list[dict] | list[str] | None = None, body: str = '') -> dict:
    return {'number': n, 'head': {'ref': f'test/{n}', 'sha': f'{n:040x}'},
            'base': {'ref': 'main'}, 'draft': False,
            'title': f'fixture {n}', 'body': body, '_files': [
                {'filename': f} if isinstance(f, str) else f for f in (paths or [])]}

class Fixture:
    def __init__(self, **options):
        self.options = options
        self.calls: list[list[str]] = []
        self.tags = options.get('tags', ['atlas-v0.10'])
        self.records = options.get('records', {RECORD: '**Status:** PI ACCEPTED\n' + FILE_HASH + '\n'})
        self.prs = options.get('prs', [])
        self.pipe_files = options.get('pipe_files', {PIPE: PIPE_TEXT})

    def run(self, args, **kw):
        a = list(args); self.calls.append(a)
        text = kw.get('text', False)
        def result(data='', rc=0):
            if isinstance(data, bytes):
                stdout = data.decode() if text else data
            else:
                stdout = data if text else data.encode()
            err = 'fixture command failed' if text else b'fixture command failed'
            if rc and kw.get('check'):
                raise subprocess.CalledProcessError(rc, a, output=stdout, stderr=err)
            return subprocess.CompletedProcess(a, rc, stdout, '' if text else b'')
        if a[:3] == ['git', 'rev-parse', 'origin/main']:
            return result(MAIN + '\n')
        if a[:2] == ['git', 'ls-remote']:
            if '--tags' in a:
                return result(''.join(f'{TARGET}\trefs/tags/{t}\n' for t in self.options.get('remote_tags', self.tags)))
            return result('' if self.options.get('empty_remote_main') else self.options.get('remote_main', MAIN) + '\trefs/heads/main\n')
        if a[:3] == ['git', 'tag', '-l']:
            return result('\n'.join(self.tags) + '\n')
        if a[:3] == ['git', 'cat-file', '-t']:
            return result('tag\n')
        if a[:2] == ['git', 'rev-parse'] and a[2].endswith('^{commit}'):
            return result(TARGET + '\n')
        if a[:2] == ['git', 'show']:
            ref, path = a[2].split(':', 1)
            if path == 'atlas/RTG_STATE_ATLAS.md': return result(SOURCE)
            if path in self.records: return result(self.records[path])
            if path in self.pipe_files: return result(self.pipe_files[path])
            return result('', 1)
        if a[:2] == ['git', 'ls-tree']:
            if a[-1] == 'pipes/':
                if self.options.get('pipe_tree_failure'): return result('', 1)
                return result('\n'.join(self.pipe_files) + '\n')
            return result('\n'.join(self.records) + '\n')
        if a[:2] == ['git', 'log']: return result('')
        if a[:2] == ['gh', 'api']:
            path, _, q = a[2].partition('?'); qs = parse_qs(q)
            page = int(qs.get('page', ['1'])[0]); size = int(qs.get('per_page', ['100'])[0])
            if self.options.get('gh_denied'): return result('', 1)
            if self.options.get('malformed_json'): return result('{not JSON')
            if path.endswith('/files'):
                n = int(path.split('/')[-2])
                if n in self.options.get('unreadable_pr_files', []): return result('', 1)
                files = [] if self.options.get('endless_pages') and n == 9000 else next(p['_files'] for p in self.prs if p['number'] == n)
                return result(json.dumps(files[(page-1)*size:page*size]))
            if path.endswith('/pulls'):
                if self.options.get('endless_pages'): return result(json.dumps([pr(9000)] * 100))
                rows = [{k:v for k,v in p.items() if k != '_files'} for p in self.prs]
                return result(json.dumps(rows[(page-1)*size:page*size]))
        raise AssertionError('Unspecified subprocess call: ' + repr(a))


def run_one(source: bytes, options: dict, overwrite=False):
    m = ModuleType('orient_under_review')
    m.__file__ = 'orient.py'
    exec(compile(source, 'orient.py', 'exec'), m.__dict__)
    fixture = Fixture(**options)
    stream = io.StringIO(); error = None; report = None; changed = None
    with tempfile.TemporaryDirectory(prefix='orient-review-') as tmp:
        root = Path(tmp); target = root / 'atlas' / 'RTG_STATE_ATLAS.md'
        target.parent.mkdir(); target.write_bytes(SOURCE)
        destination = target if overwrite else root / 'observation.json'
        argv = ['orient.py', 'ATLAS', '--json', str(destination)]
        with patch.object(m.subprocess, 'run', fixture.run), patch.object(sys, 'argv', argv), contextlib.redirect_stdout(stream):
            try: m.main()
            except Exception as exc: error = f'{type(exc).__name__}: {exc}'
        if destination.exists():
            try: report = json.loads(destination.read_text())
            except (ValueError, UnicodeError): pass
        changed = target.read_bytes() != SOURCE
    return {'report': report, 'stdout': stream.getvalue(), 'exception': error,
            'sentinel_changed': changed, 'calls': fixture.calls}


def partial(r):
    return r['exception'] is None and r['report'] is not None and r['report']['status'].startswith('PARTIAL')
def complete(r):
    return r['exception'] is None and r['report'] is not None and r['report']['status'].startswith('COMPLETE')
def numbers(r):
    try: return {p['number'] for p in r['report']['open_prs']['matched']}
    except (KeyError, TypeError): return set()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--tool', type=Path, required=True); ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args(); source = a.tool.read_bytes()
    digest = hashlib.sha256(source).hexdigest()
    blob = hashlib.sha1(b'blob ' + str(len(source)).encode() + b'\0' + source).hexdigest()
    if digest != EXPECTED or blob != BLOB: raise SystemExit('Refusing unpinned target')
    cases = []
    def add(key, name, options, predicate, overwrite=False):
        r = run_one(source, options, overwrite)
        ok = bool(predicate(r)); cases.append({'id':key,'name':name,'contract_pass':ok, **r})
        status = None if r['report'] is None else r['report']['status']
        print(f'{key}: {"PASS" if ok else "FAIL"} — {name}; status={status}; exception={r["exception"]}')
    add('P01','baseline known tag/hash, path matches and reference-only dependency',
        {'prs':[pr(113,['tools/check_compaction.py']),pr(114,['records/atlas/review.md']),pr(188,['records/atlas/entry.md']),pr(189,['dsn/DSN_METHODOLOGY.md'],'References #188'),pr(222,['dsn/unrelated.md'])]},
        lambda r: complete(r) and numbers(r)=={113,114,188,189} and r['report']['governing']['file_sha256_at_tag']==FILE_HASH and not r['sentinel_changed'])
    add('P02','GitHub access denied => partial and null PR collection',{'gh_denied':True},lambda r: partial(r) and r['report']['open_prs'] is None)
    add('P03','stale origin/main => partial',{'remote_main':'c'*40},partial)
    add('P04','unfetched remote tag => partial',{'remote_tags':['atlas-v0.10','atlas-v0.11']},partial)
    add('P05','PR listing pagination reaches page 2',{'prs':[pr(i) for i in range(1,101)]+[pr(201,['atlas/a.md'])]},lambda r: complete(r) and numbers(r)=={201} and r['report']['open_prs']['scanned']==101)
    add('P06','PR files pagination reaches matching file on page 2',{'prs':[pr(201,[f'other/{i}' for i in range(100)]+['atlas/a.md'])]},lambda r: complete(r) and numbers(r)=={201})
    add('P07','pagination limit exposed rather than COMPLETE',{'endless_pages':True},partial)
    add('P08','known missing release record => partial',{'records':{}},partial)
    add('P09','failed PR file list => partial',{'prs':[pr(201,['atlas/a.md'])],'unreadable_pr_files':[201]},partial)
    add('N01','unreadable pipe tree must not render empty/none',{'pipe_tree_failure':True},lambda r: partial(r) and 'inbox: none' not in r['stdout'] and r['report']['pipes']['inbox'] is None)
    add('N02','release record without Status must mark result partial',{'records':{RECORD:FILE_HASH}},partial)
    add('N03','hash-inconsistent release record must flag uncertainty',{'records':{RECORD:'**Status:** PI ACCEPTED\n'+'0'*64}},partial)
    add('N04','release record version matches exactly, not prefix v0.10 vs v0.100',{'records':{'records/atlas/RTG_STATE_ATLAS_v0.100_RELEASE_RECORD.md':'**Status:** PI ACCEPTED\n'+FILE_HASH}},lambda r: partial(r) and not r['report']['governing']['release_record'])
    add('N05','malformed successful GitHub JSON => structured partial, not crash',{'malformed_json':True},partial)
    add('N06','mixed release and -rN candidate tags do not crash',{'tags':['atlas-v0.10-r1','atlas-v0.10.1']},lambda r:r['exception'] is None and r['report'] is not None)
    add('N07','missing remote main ref => partial',{'empty_remote_main':True},partial)
    add('N08','renamed-away Atlas file is a relevant changed path',{'prs':[pr(201,[{'filename':'archive/retired.md','previous_filename':'atlas/old.md','status':'renamed'}])]},lambda r:complete(r) and numbers(r)=={201})
    add('N09','explicit same-repository PR URL dependency is discovered',{'prs':[pr(113,['tools/check_compaction.py']),pr(202,['dsn/other.md'],'https://github.com/MustafaAksu/rtg-corpus/pull/113')]},lambda r:complete(r) and numbers(r)=={113,202})
    add('N10','dependency closure independent of reverse order',{'prs':[pr(201,['dsn/b.md'],'#200'),pr(200,['dsn/a.md'],'#113'),pr(113,['atlas/a.md'])]},lambda r:complete(r) and numbers(r)=={113,200,201})
    add('P10','dependency closure same graph in favorable order',{'prs':[pr(200,['dsn/a.md'],'#113'),pr(201,['dsn/b.md'],'#200'),pr(113,['atlas/a.md'])]},lambda r:complete(r) and numbers(r)=={113,200,201})
    add('N11','JSON output cannot overwrite an existing scientific file',{},lambda r:not r['sentinel_changed'],overwrite=True)
    commands={tuple(c[:2]) for r in cases for c in r['calls']}
    summary={'tool_sha256':digest,'tool_git_blob':blob,'tool_bytes':len(source),
             'mode':'offline unmodified-code execution; only subprocess I/O replaced with fixtures',
             'cases':len(cases),'passed':sum(r['contract_pass'] for r in cases),
             'failed':sum(not r['contract_pass'] for r in cases),
             'subprocess_verbs':[list(x) for x in sorted(commands)],
             'cases_detail':cases}
    a.out.mkdir(parents=True,exist_ok=True)
    (a.out/'results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(f'TOTAL: {summary["passed"]}/{summary["cases"]} contract checks pass; {summary["failed"]} fail')
    raise SystemExit(1 if summary['failed'] else 0)

if __name__=='__main__': main()
