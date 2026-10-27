#!/usr/bin/env python3
"""Hash-check of upload/numgen-records (PR #69) against the identities cited by numgen-v1.20.8.
Run from the repository root with the upload branch fetched: python3 -I evidence/numgen/inventory/build_numgen_upload_check.py
Writes evidence/numgen/inventory/numgen_upload_inventory_20261026.json. Reads only; places nothing."""
import hashlib, io, json, re, subprocess, zipfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]; UP = 'origin/upload/numgen-records'; DIR = 'upload/numgen-records/'
TAG = 'numgen-v1.20.8'; TAG_SHA = '835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e'
def git(*a): return subprocess.check_output(['git', '-C', str(ROOT), *a])
def h(b): return hashlib.sha256(b).hexdigest()
names = [l for l in git('ls-tree', '-r', '--name-only', UP, DIR).decode().split('\n') if l]
blobs = {n[len(DIR):]: git('show', f'{UP}:{n}') for n in names}
sums = {l.split(maxsplit=1)[1].lstrip('*').strip(): l.split()[0] for l in blobs['SHA256SUMS.txt'].decode().splitlines() if l.strip()}
listed_ok = {f: h(blobs[f]) == s for f, s in sums.items() if f in blobs}
missing_listed = [f for f in sums if f not in blobs]
unlisted = [f for f in blobs if f not in sums and f not in ('SHA256SUMS.txt', 'README_UPLOAD.md')]
ident = {f: h(b) for f, b in blobs.items()}
for f, b in blobs.items():
    if f.endswith('.zip'):
        with zipfile.ZipFile(io.BytesIO(b)) as z:
            for n in z.namelist():
                if not n.endswith('/'): ident[f + '::' + n] = h(z.read(n))
# banner-stripped payloads: every .md whose first line is a '> **[SUPERSEDED' banner (README_UPLOAD: payload = everything after the first blank line)
bannered = []
for f, b in blobs.items():
    if f.endswith('.md') and b.startswith(b'> **[SUPERSEDED'):
        i = b.find(b'\n\n')
        if i >= 0: ident[f + '::payload'] = h(b[i + 2:]); bannered.append(f)
ng = git('show', f'{TAG}:dsn/RTG_NUMBER_GENESIS_DSN.md'); assert h(ng) == TAG_SHA
txt = ng.decode()
cited = {(a, b[-4:]) for a, b in re.findall(r'([0-9a-f]{8})…([0-9a-f]{4,5})', txt)} | {(m[:8], m[-4:]) for m in re.findall(r'\b[0-9a-f]{64}\b', txt)}
# one abbreviated citation (cefb7180…b165b, §9.2) carries a 5-character suffix; it is matched on its last four characters
present = {}
for f, v in ident.items():
    k = (v[:8], v[-4:])
    if k in cited: present.setdefault(v, []).append(f)
def ctx(p):
    m = re.search(r'.{0,90}' + p + r'.{0,30}', txt); return m.group(0).replace('\n', ' ') if m else ''
not_present = [{'prefix': a + '…' + b, 'context': ctx(a)} for a, b in sorted(cited) if not any(v.startswith(a) for v in present)]
out = dict(upload_branch=UP, upload_commit=git('rev-parse', UP).decode().strip(), source_tag=TAG, source_sha256=TAG_SHA,
           files=len(blobs), sha256sums_entries=len(sums), sha256sums_all_ok=all(listed_ok.values()) and not missing_listed,
           listed_mismatch=[f for f, ok in listed_ok.items() if not ok], listed_but_absent=missing_listed, unlisted_files=unlisted,
           zip_members=sum(1 for k in ident if '::' in k and not k.endswith('::payload')), bannered_files=sorted(bannered),
           cited_identities_in_numgen=len(cited), cited_and_present=[{'sha256': v, 'where': w} for v, w in sorted(present.items())],
           cited_not_in_upload=not_present, file_hashes={f: h(b) for f, b in sorted(blobs.items())})
Path(ROOT / 'evidence/numgen/inventory/numgen_upload_inventory_20261026.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(json.dumps({k: out[k] for k in ('upload_commit', 'files', 'sha256sums_entries', 'sha256sums_all_ok', 'listed_mismatch', 'listed_but_absent', 'unlisted_files', 'zip_members', 'cited_identities_in_numgen')} | {'bannered_files': len(out['bannered_files'])}, indent=1))
print('cited & present:', len(out['cited_and_present']), ' cited, not in upload:', len(not_present))
for r in out['cited_and_present']: print(' +', r['sha256'][:8] + '…' + r['sha256'][-4:], '|', '; '.join(r['where'])[:120])
for r in not_present: print(' -', r['prefix'], '|', r['context'][:130])
