#!/usr/bin/env python3
"""Intake check of upload/corpus-originals-20261123/ (PI archive search of 23 Nov 2026).
Reads files as bytes only; nothing from the upload folder is imported or executed.
Run from the repository root: python3 -I evidence/atlas/intake/corpus_originals_20261123/intake_check.py
Checks: (1) every file listed in SHA256SUMS.txt and MANIFEST.csv has the stated SHA-256;
(2) for every name of _WANTED_LIST.txt: is a file of that name present (loose, or inside an uploaded zip, two levels deep),
and does its SHA-256 equal the hash recorded for that name (full, or the short prefix~suffix form)?
(3) files whose bytes carry a recorded hash but whose own name is another one are listed separately.
Writes intake_result.csv and intake_summary.json next to this script."""
import csv, io, hashlib, os, re, zipfile, json, collections, sys
UP = 'upload/corpus-originals-20261123'
OUT = os.path.dirname(os.path.abspath(__file__))
sha = lambda b: hashlib.sha256(b).hexdigest()
W = {}
for l in io.open(f'{UP}/_WANTED_LIST.txt', encoding='ascii').read().split('\n'):
    l = l.strip()
    if l:
        n, h, s = l.split('|'); W[n] = (h, s)
def agrees(h, rec):
    if len(rec) == 64: return h == rec
    if '~' in rec:
        a, b = rec.split('~'); return h.startswith(a) and h.endswith(b)
    return None
def norm(n):
    b, e = os.path.splitext(n)
    b = re.sub(r'\s*\(\d+\)$', '', b); b = re.sub(r'\s*-\s*(Copy|Kopya)(\s*\(\d+\))?$', '', b)
    return (b + e).lower()
# (1) stated hashes
sums = [l.split('  ', 1) for l in io.open(f'{UP}/SHA256SUMS.txt', encoding='ascii').read().strip().split('\n')]
bad = [n for h, n in sums if sha(open(f'{UP}/{n}', 'rb').read()) != h]
rows = list(csv.DictReader(io.open(f'{UP}/MANIFEST.csv', encoding='utf-8-sig')))
bad += [r['StoredAs'] for r in rows if sha(open(f"{UP}/{r['StoredAs']}", 'rb').read()) != r['Sha']]
listed = {n for _, n in sums}; reports = {'MANIFEST.csv', 'SHA256SUMS.txt', 'NOT_FOUND.txt', 'TOO_LARGE.txt', 'VARIANTS_OVER_CAP.txt', '_WANTED_LIST.txt'}
unlisted = sorted(set(os.listdir(UP)) - listed - reports)
# (2) loose files
RANK = {'HASH-VERIFIED': 4, 'PRESENT, NO RECORDED HASH': 3, 'PRESENT, HASH DIFFERS': 2}
res = {}; other_name = []
def offer(wn, state, where, h):
    if wn not in res or RANK[state] > RANK[res[wn][0]]: res[wn] = (state, where, h)
for r in rows:
    wn = r['WantedName']
    if not wn: continue
    a = agrees(r['Sha'], W[wn][0]); same = norm(r['OriginalName']) == wn.lower()
    if a and not same:
        other_name.append(dict(stored_as=r['StoredAs'], original_name=r['OriginalName'], sha256=r['Sha'], wanted_name=wn)); continue
    offer(wn, 'HASH-VERIFIED' if a else ('PRESENT, NO RECORDED HASH' if a is None else 'PRESENT, HASH DIFFERS'), r['StoredAs'], r['Sha'])
# (2) inside zips
low = {n.lower(): n for n in W}
def walk(zf, label, depth=0):
    for i in zf.infolist():
        if i.is_dir(): continue
        b = os.path.basename(i.filename)
        if b.lower().endswith('.zip') and depth < 2 and i.file_size < 60_000_000:
            try: walk(zipfile.ZipFile(io.BytesIO(zf.read(i))), label + '!' + i.filename, depth + 1)
            except Exception: pass
        if b.lower() in low:
            wn = low[b.lower()]
            if wn in res and res[wn][0] == 'HASH-VERIFIED' and '!' not in res[wn][1]: continue
            h = sha(zf.read(i)); a = agrees(h, W[wn][0])
            offer(wn, 'HASH-VERIFIED' if a else ('PRESENT, NO RECORDED HASH' if a is None else 'PRESENT, HASH DIFFERS'), label + '!' + i.filename, h)
for z in sorted(f for f in os.listdir(UP) if f.lower().endswith('.zip')):
    walk(zipfile.ZipFile(f'{UP}/{z}'), z)
with open(f'{OUT}/intake_result.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f); w.writerow(['wanted_name', 'cited_by', 'recorded_hash', 'result', 'where', 'sha256'])
    for n in sorted(W, key=str.lower):
        st, where, h = res.get(n, ('NOT FOUND', '', ''))
        w.writerow([n, W[n][1], W[n][0], st, where, h])
tot = collections.Counter(res.get(n, ('NOT FOUND',))[0] for n in W)
per = collections.defaultdict(collections.Counter)
for n, (h, s) in W.items():
    for st in s.split('+'): per[st][res.get(n, ('NOT FOUND',))[0]] += 1
summary = dict(upload=UP, files_in_sha256sums=len(sums), manifest_rows=len(rows), stated_hash_mismatches=bad, files_not_listed=unlisted,
               wanted_names=len(W), totals=dict(tot), in_zip=sum(1 for v in res.values() if '!' in v[1]),
               per_stream={k: dict(v) for k, v in sorted(per.items())}, bytes_with_a_recorded_hash_under_another_name=other_name,
               manifest_status=dict(collections.Counter(r['Status'] for r in rows)), variant_named_files=sum(1 for r in rows if '__' in r['StoredAs']))
json.dump(summary, open(f'{OUT}/intake_summary.json', 'w'), indent=1, ensure_ascii=False)
print(json.dumps({k: v for k, v in summary.items() if k not in ('per_stream', 'bytes_with_a_recorded_hash_under_another_name')}, indent=1))
for k, v in summary['per_stream'].items(): print(f'{k:8}', v)
for o in other_name: print('OTHER NAME:', o['stored_as'], '<-', o['original_name'])
assert not bad and not unlisted
