#!/usr/bin/env python3
"""Hash-check of upload/gen-records (PR #40, commit 2425539) against the identities cited by gen-v2.8.9 and the OFN Q6 erratum.
Run from the repository root with the upload branch fetched: python3 -I evidence/gen/inventory/build_gen_upload_check.py
Writes evidence/gen/inventory/gen_upload_inventory_20261024.json. Reads only; places nothing."""
import hashlib, io, json, re, subprocess, zipfile, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]; UP = 'origin/upload/gen-records'; DIR = 'upload/gen-records/'
def git(*a): return subprocess.check_output(['git', '-C', str(ROOT), *a])
def h(b): return hashlib.sha256(b).hexdigest()
names = [l for l in git('ls-tree', '-r', '--name-only', UP, DIR).decode().split('\n') if l]
blobs = {n[len(DIR):]: git('show', f'{UP}:{n}') for n in names}
sums = {l.split()[1].lstrip('*'): l.split()[0] for l in blobs['SHA256SUMS.txt'].decode().splitlines() if l.strip()}
listed_ok = {f: h(blobs[f]) == s for f, s in sums.items() if f in blobs}
missing_listed = [f for f in sums if f not in blobs]
unlisted = [f for f in blobs if f not in sums and f not in ('SHA256SUMS.txt', 'README_UPLOAD.md')]
ident = {f: h(b) for f, b in blobs.items()}
for f, b in blobs.items():
    if f.endswith('.zip'):
        with zipfile.ZipFile(io.BytesIO(b)) as z:
            for n in z.namelist():
                if not n.endswith('/'): ident[f + '::' + n] = h(z.read(n))
gen = (ROOT / 'dsn/RTG_GENESIS_GEOMETRY_DSN.md').read_bytes(); assert h(gen) == 'd143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc'
txt = gen.decode() + (ROOT / 'records/gen/GENESIS_V2_8_9_NOTICE_ERRATUM_OFN_Q6_v0_1.md').read_text(encoding='utf-8')
cited = set(re.findall(r'([0-9a-f]{8})…([0-9a-f]{4})', txt)) | {(m[:8], m[-4:]) for m in re.findall(r'\b[0-9a-f]{64}\b', txt)}
present = {}
for f, v in ident.items():
    k = (v[:8], v[-4:])
    if k in cited: present.setdefault(v, []).append(f)
def ctx(p):
    m = re.search(r'.{0,80}' + p + r'.{0,20}', txt); return m.group(0).replace('\n', ' ') if m else ''
not_present = [{'prefix': a + '…' + b, 'context': ctx(a)} for a, b in sorted(cited) if not any(v.startswith(a) for v in present)]
out = dict(upload_branch=UP, upload_commit=git('rev-parse', UP).decode().strip(), files=len(blobs), sha256sums_entries=len(sums),
           sha256sums_all_ok=all(listed_ok.values()) and not missing_listed, listed_mismatch=[f for f, ok in listed_ok.items() if not ok],
           listed_but_absent=missing_listed, unlisted_files=unlisted, zip_members=sum(1 for k in ident if '::' in k),
           cited_identities_in_gen_and_erratum=len(cited), cited_and_present=[{'sha256': v, 'where': w} for v, w in sorted(present.items())],
           cited_not_in_upload=not_present, file_hashes={f: h(b) for f, b in sorted(blobs.items())})
Path(ROOT / 'evidence/gen/inventory/gen_upload_inventory_20261024.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(json.dumps({k: out[k] for k in ('upload_commit', 'files', 'sha256sums_all_ok', 'listed_mismatch', 'listed_but_absent', 'unlisted_files', 'zip_members', 'cited_identities_in_gen_and_erratum')}, indent=1))
print('cited & present:', len(out['cited_and_present']), ' cited, not in upload:', len(not_present))
for r in not_present: print(' ', r['prefix'], '|', r['context'][:110])
