#!/usr/bin/env python3
"""Validate pipe items and rebuild pipes/<STREAM>/INDEX.md.

usage: pipes_index.py [--check] [--selftest] [--root REPO]
  --check     validate only (exit 1 on any error); without it, validate and write the indexes
  --selftest  run the negative controls (bad items must be rejected) and exit
Front matter rules: see pipes/README.md. INDEX.md files are derived views and are rewritten on every run.
"""
import argparse, json, os, re, subprocess, sys, tempfile

STREAMS = ['METH', 'PROG', 'OFN', 'RRF', 'LEGACY', 'PREL', 'NUMGEN', 'DYAD', 'TRIAD', 'GEN', 'UVM', 'RECOG', 'DZT', 'TDRG', 'AZ', 'RER', 'FMS', 'ER2B', 'ATLAS']
KINDS = ['request', 'offer', 'finding', 'question', 'notice']
STATES = ['open', 'acknowledged', 'dispositioned', 'closed']
REQUIRED = ['from', 'to', 'date', 'kind', 'object', 'tags', 'state']
OPTIONAL = ['blocks', 'disposition', 'filed_by']
VERDICTS = ['accept', 'accept with change', 'reject', 'defer', 'no action']
DISP_RE = re.compile(r'^(\d{4}-\d{2}-\d{2}) · (accept with change|accept|reject|defer|no action) · (.+)$')
NAME_RE = re.compile(r'^\d{8}-([A-Z0-9]+)-[a-z0-9][a-z0-9-]*\.md$')

def parse(text):
    if not text.startswith('---\n'): raise ValueError('no front matter')
    end = text.find('\n---\n', 4)
    if end < 0: raise ValueError('front matter not closed')
    fm, body = text[4:end], text[end + 5:]
    data = {}
    for line in fm.split('\n'):
        if not line.strip(): continue
        if ':' not in line: raise ValueError(f'bad front-matter line: {line!r}')
        k, v = line.split(':', 1); k = k.strip(); v = v.split('   #')[0].strip() if '   #' in v else v.strip()
        if k in data: raise ValueError(f'duplicate field {k}')
        data[k] = v
    return data, body

def git_tags(root):
    """Repository tags; raises if the list cannot be read or is empty (validation must not pass by accident)."""
    out = subprocess.check_output(['git', '-C', root, 'tag', '-l']).decode().split()
    if not out: raise RuntimeError('repository tag list is empty — cannot validate tags')
    return set(out)

def validate_item(path, text, tags):
    errors = []
    name = os.path.basename(path); m = NAME_RE.match(name)
    if not m: errors.append(f'{name}: filename must be YYYYMMDD-<FROM>-<slug>.md')
    try: data, body = parse(text)
    except ValueError as e: return [f'{name}: {e}']
    for k in REQUIRED:
        if k not in data or (k != 'disposition' and not data[k]): errors.append(f'{name}: missing {k}')
    for k in data:
        if k not in REQUIRED + OPTIONAL: errors.append(f'{name}: unknown field {k}')
    if data.get('from') not in STREAMS: errors.append(f"{name}: from={data.get('from')!r} not a stream key")
    if data.get('to') not in STREAMS: errors.append(f"{name}: to={data.get('to')!r} not a stream key")
    if m and data.get('from') and m.group(1) != data['from']: errors.append(f'{name}: filename FROM differs from front matter')
    if m and data.get('date') and name[:8] != data['date'].replace('-', ''): errors.append(f'{name}: filename date differs from date field')
    if data.get('filed_by') and data['filed_by'] not in STREAMS: errors.append(f"{name}: filed_by={data['filed_by']!r} not a stream key")
    stream_dir = os.path.basename(os.path.dirname(path))
    if data.get('to') and stream_dir != data['to']: errors.append(f'{name}: filed under {stream_dir}/ but to={data["to"]}')
    if data.get('kind') not in KINDS: errors.append(f"{name}: kind={data.get('kind')!r}")
    if data.get('state') not in STATES: errors.append(f"{name}: state={data.get('state')!r}")
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', data.get('date', '')): errors.append(f'{name}: date must be YYYY-MM-DD')
    tl = data.get('tags', '')
    if not (tl.startswith('[') and tl.endswith(']')): errors.append(f'{name}: tags must be [a, b]')
    else:
        tag_items = [x.strip() for x in tl[1:-1].split(',') if x.strip()]
        if not tag_items: errors.append(f'{name}: tags must name at least one repository tag')
        for t in tag_items:
            if t not in tags: errors.append(f'{name}: tag {t} does not exist in the repository')
    disp = data.get('disposition', '')
    if data.get('state') in ('dispositioned', 'closed') and not disp: errors.append(f'{name}: state {data["state"]} needs a disposition')
    if disp:
        dm = DISP_RE.match(disp)
        if not dm: errors.append(f'{name}: disposition must read "YYYY-MM-DD · <verdict> · <pointer>" with verdict in {VERDICTS}')
        elif not re.search(r'(records/|dsn/|pipes/|[A-Z]{2,}-[A-Z0-9-]{3,})', dm.group(3)): errors.append(f'{name}: disposition pointer must name a records/dsn path or a RID')
        if data.get('state') in ('open', 'acknowledged'): errors.append(f'{name}: a disposition is present but state is {data["state"]}')
    if not body.strip(): errors.append(f'{name}: empty body')
    if len(body.split('\n')) > 40: errors.append(f'{name}: body longer than 40 lines — science belongs in the DSN/records')
    return errors

def collect(root):
    items = {}
    pdir = os.path.join(root, 'pipes')
    for s in sorted(os.listdir(pdir)):
        d = os.path.join(pdir, s)
        if not os.path.isdir(d): continue
        items[s] = []
        for f in sorted(os.listdir(d)):
            if f.endswith('.md') and f != 'INDEX.md': items[s].append(os.path.join(d, f))
    return items

def render_index(stream, paths):
    rows = ['# Inbox — ' + stream, '', '*Generated by `tools/pipes_index.py`; do not edit. States are changed by the receiver in the item files.*', '',
            '| date | from | kind | state | object | blocks | file |', '|---|---|---|---|---|---|---|']
    for p in paths:
        data, _ = parse(open(p, encoding='utf-8').read())
        rows.append(f"| {data['date']} | {data['from']} | {data['kind']} | {data['state']} | {data['object']} | {data.get('blocks', '') or '—'} | `{os.path.basename(p)}` |")
    if not paths: rows.append('| — | — | — | — | (empty) | — | — |')
    return '\n'.join(rows) + '\n'

def run(root, write):
    tags = git_tags(root); errors = []
    items = collect(root)
    for s in items:
        if s not in STREAMS: errors.append(f'pipes/{s}: not a stream key')
        for p in items[s]:
            errors += validate_item(p, open(p, encoding='utf-8').read(), tags)
    if errors: return errors
    if write:
        for s, paths in items.items():
            open(os.path.join(root, 'pipes', s, 'INDEX.md'), 'w', encoding='utf-8').write(render_index(s, paths))
    return []

GOOD = """---
from: NUMGEN
to: TDRG
date: 2026-10-26
kind: request
object: TDRG-ORIENT (TDRG §6)
tags: [tdrg-v2.12.13]
state: open
---
Body line.
"""

def selftest(root):
    tags = git_tags(root)
    positive = [('valid open item', 'TDRG/20261026-NUMGEN-x.md', GOOD),
                ('valid closed item with verdict and pointer', 'TDRG/20261026-NUMGEN-x.md', GOOD.replace('state: open', 'state: closed\ndisposition: 2026-11-02 · reject · records/tdrg/TDRG_OWNER_DISPOSITION_20261102.md'))]
    negative = [('unknown stream key', 'TDRG/20261026-NUMGEN-x.md', GOOD.replace('to: TDRG', 'to: FOO')),
                ('invalid state (notice vocabulary)', 'TDRG/20261026-NUMGEN-x.md', GOOD.replace('state: open', 'state: sent')),
                ('dispositioned without disposition', 'TDRG/20261026-NUMGEN-x.md', GOOD.replace('state: open', 'state: dispositioned')),
                ('disposition without verdict/pointer', 'TDRG/20261026-NUMGEN-x.md', GOOD.replace('state: open', 'state: closed\ndisposition: done')),
                ('disposition pointer missing', 'TDRG/20261026-NUMGEN-x.md', GOOD.replace('state: open', 'state: closed\ndisposition: 2026-11-02 · accept · ok')),
                ('disposition present while open', 'TDRG/20261026-NUMGEN-x.md', GOOD.replace('state: open', 'state: open\ndisposition: 2026-11-02 · accept · records/x.md')),
                ('tag not in repository', 'TDRG/20261026-NUMGEN-x.md', GOOD.replace('tdrg-v2.12.13', 'tdrg-v9.9')),
                ('empty tag list', 'TDRG/20261026-NUMGEN-x.md', GOOD.replace('[tdrg-v2.12.13]', '[]')),
                ('filed under wrong inbox', 'DYAD/20261026-NUMGEN-x.md', GOOD),
                ('filename FROM mismatch', 'TDRG/20261026-RECOG-x.md', GOOD),
                ('filename date mismatch', 'TDRG/20261027-NUMGEN-x.md', GOOD),
                ('unknown field (second status axis)', 'TDRG/20261026-NUMGEN-x.md', GOOD.replace('state: open', 'state: open\nnotice_status: sent')),
                ('filed_by not a stream key', 'TDRG/20261026-NUMGEN-x.md', GOOD.replace('to: TDRG', 'filed_by: Claude\nto: TDRG')),
                ('empty body', 'TDRG/20261026-NUMGEN-x.md', GOOD.replace('Body line.\n', ''))]
    ok = True
    for what, rel, text in positive:
        errs = validate_item(os.path.join('/tmp/pipes', rel), text, tags); good = not errs; ok &= good
        print(('ok  ' if good else 'MISS'), 'positive:', what, '—', errs[0] if errs else 'accepted')
    for what, rel, text in negative:
        errs = validate_item(os.path.join('/tmp/pipes', rel), text, tags); good = bool(errs); ok &= good
        print(('ok  ' if good else 'MISS'), 'negative:', what, '—', errs[0] if errs else 'NOT caught')
    # empty tag list must abort validation, not pass it
    try:
        git_tags(tempfile.mkdtemp()); print('MISS negative: empty repository tag list accepted'); ok = False
    except Exception: print('ok   negative: empty repository tag list refused')
    print(f'RESULT: {"PASS" if ok else "FAIL"} ({len(positive)} positive, {len(negative)+1} negative)'); return ok

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--check', action='store_true'); ap.add_argument('--selftest', action='store_true'); ap.add_argument('--root', default=os.getcwd())
    a = ap.parse_args()
    if a.selftest: sys.exit(0 if selftest(a.root) else 1)
    errors = run(a.root, write=not a.check)
    if errors:
        print('\n'.join(errors)); sys.exit(1)
    # after writing, check that indexes equal regeneration (detects hand edits when run with --check)
    items = collect(a.root)
    for s, paths in items.items():
        p = os.path.join(a.root, 'pipes', s, 'INDEX.md')
        if a.check and (not os.path.exists(p) or open(p, encoding='utf-8').read() != render_index(s, paths)):
            print(f'pipes/{s}/INDEX.md is stale or hand-edited; run tools/pipes_index.py'); sys.exit(1)
    print(f"pipes OK: {sum(len(v) for v in items.values())} items in {len(items)} inboxes")

if __name__ == '__main__':
    main()
