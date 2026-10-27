#!/usr/bin/env python3
"""Hash-check of upload/tdrg-records (branch missing-files, commit 9df0319 "TDRG files") against the PI's held-file manifest
SHA256SUMS_tdrg_held.txt and the artifact registry of tdrg-v2.12.13 §8.
Run from the repository root with the branch fetched: python3 -I evidence/tdrg/inventory/build_tdrg_upload_check.py
Writes evidence/tdrg/inventory/tdrg_upload_inventory_20261027.json. Reads only; places nothing."""
import hashlib, io, json, re, subprocess, zipfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]; UP = 'origin/missing-files'; DIR = 'upload/tdrg-records/'
def git(*a): return subprocess.check_output(['git', '-C', str(ROOT), *a])
def h(b): return hashlib.sha256(b).hexdigest()
names = [l for l in git('ls-tree', '-r', '--name-only', UP, DIR).decode().split('\n') if l]
blobs = {n[len(DIR):]: git('show', f'{UP}:{n}') for n in names}
held = {}
for l in blobs['SHA256SUMS_tdrg_held.txt'].decode('utf-8-sig').splitlines():
    if l.strip():
        hh, fn = l.split(None, 1); held[fn.strip()] = hh.lower()
uploaded = {f: h(b) for f, b in blobs.items() if f != 'SHA256SUMS_tdrg_held.txt'}
zips = {}
for f, b in blobs.items():
    if f.endswith('.zip'):
        with zipfile.ZipFile(io.BytesIO(b)) as z:
            zips[f] = {n: h(z.read(n)) for n in z.namelist() if not n.endswith('/')}
match = {f: (held.get(f) == v) for f, v in uploaded.items() if f in held}
mismatch = [f for f, ok in match.items() if not ok]
not_in_manifest = sorted(f for f in uploaded if f not in held)
present_as_zip_member = {}
for zf, members in zips.items():
    for m, v in members.items():
        if m in held: present_as_zip_member[m] = dict(zip=zf, member_hash_matches=(held[m] == v))
held_not_uploaded = sorted(f for f in held if f not in uploaded and f not in present_as_zip_member)
# TDRG v2.12.13 §8 artifact registry names
tdrg = git('show', 'tdrg-v2.12.13:dsn/RTG_DISCRETE_GENESIS_DSN.md').decode()
assert h(tdrg.encode()) == 'aa232643f6f631694b0eda1532be213e5a517ef109cd66794f8e638e24fc053f'
sec8 = tdrg.split('## §8.')[1].split('## §9.')[0]
registry = {m.group(1): m.group(2) for m in re.finditer(r'\[RID: (TDRG-ART-[A-Z0-9-]+)\] :: `?([^:`]+)`? ::', sec8)}
out = dict(upload_branch=UP, upload_commit=git('rev-parse', UP).decode().strip(), files=len(blobs), manifest_entries=len(held), uploaded_files=len(uploaded),
           manifest_match_all=not mismatch, mismatch=mismatch, not_in_manifest=not_in_manifest, zip_members=zips, present_as_zip_member=present_as_zip_member,
           held_not_uploaded=held_not_uploaded, tdrg_sec8_registry=registry, file_hashes=dict(sorted(uploaded.items())))
Path(ROOT / 'evidence/tdrg/inventory/tdrg_upload_inventory_20261027.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(json.dumps({k: out[k] for k in ('upload_commit', 'files', 'manifest_entries', 'uploaded_files', 'manifest_match_all', 'mismatch', 'not_in_manifest')}, indent=1))
print('zip members:'); [print(' ', zf, '->', m, 'matches manifest:', present_as_zip_member.get(m, {}).get('member_hash_matches')) for zf, ms in zips.items() for m in ms]
print('held, not uploaded (%d):' % len(held_not_uploaded)); [print(' ', f, held[f][:8]) for f in held_not_uploaded]
print('§8 registry:'); [print(' ', k, '::', v) for k, v in registry.items()]
