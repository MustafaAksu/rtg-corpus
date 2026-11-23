#!/usr/bin/env python3
"""Intake check of upload/corpus-originals-20261123/ (PI archive search of 23 Nov 2026). Version 2, after review 6021632408.
Reads files as bytes only; nothing from the upload folder is imported or executed.
Run from the repository root:  python3 -I evidence/atlas/intake/corpus_originals_20261123/intake_check.py
                               python3 -I evidence/atlas/intake/corpus_originals_20261123/intake_check.py --controls

What it establishes, and what it does not:
 A. TRANSFER INTEGRITY: every source file has the SHA-256 stated in SHA256SUMS.txt and MANIFEST.csv (written on the PI's machine).
 B. A CENSUS AGAINST THE EXTRACTED WANTED LIST (_WANTED_LIST.txt). Every object is indexed under ITS OWN name: a loose file under
    the OriginalName of MANIFEST.csv (all rows, pattern rows included; never under the stored name), a zip member under its
    member name. For each wanted name the check reports, separately: objects of that name (loose / in zips, all of them),
    whether one of them has the recorded digest, on which basis (full 64-hex digest, or the short prefix~suffix form a source
    prints), and whether bytes with the recorded digest exist under another name.
 C. ARCHIVE COVERAGE: every archive opened, skipped or unreadable is logged with its reason. "Not found" always means
    "not found in the inspected scope".
 It does NOT establish that a recorded digest belongs to the name the wanted list pairs it with: that pairing was extracted
 automatically and is known to be wrong in places. No full digest is derived from a short one."""
import csv, io, hashlib, os, re, zipfile, json, collections, sys, tempfile, shutil
MAX_DEPTH = 8                 # nesting depth of archives that is opened (top-level zip = depth 1)
MAX_MEMBER = 300_000_000      # a zip member larger than this is not read
REPORTS = {'MANIFEST.csv', 'SHA256SUMS.txt', 'NOT_FOUND.txt', 'TOO_LARGE.txt', 'VARIANTS_OVER_CAP.txt', '_WANTED_LIST.txt'}
sha = lambda b: hashlib.sha256(b).hexdigest()
def norm(n):
    b, e = os.path.splitext(os.path.basename(n))
    b = re.sub(r'\s*\(\d+\)$', '', b); b = re.sub(r'\s*-\s*(Copy|Kopya)(\s*\(\d+\))?$', '', b)
    return (b + e).lower()
def ref_kind(rec): return 'full' if re.fullmatch(r'[0-9a-f]{64}', rec) else ('short' if re.fullmatch(r'[0-9a-f]+~[0-9a-f]+', rec) else 'none')
def agrees(h, rec):
    k = ref_kind(rec)
    if k == 'full': return h == rec
    if k == 'short':
        a, b = rec.split('~'); return h.startswith(a) and h.endswith(b)
    return False

def run(UP, max_depth=MAX_DEPTH):
    W = {}
    for l in io.open(f'{UP}/_WANTED_LIST.txt', encoding='ascii').read().split('\n'):
        l = l.strip()
        if l:
            n, h, s = l.split('|'); W[n] = (h, s)
    # ---- A. transfer integrity ----
    sums = [l.split('  ', 1) for l in io.open(f'{UP}/SHA256SUMS.txt', encoding='ascii').read().strip().split('\n') if l.strip()]
    rows = list(csv.DictReader(io.open(f'{UP}/MANIFEST.csv', encoding='utf-8-sig')))
    bad = sorted({n for h, n in sums if sha(open(f'{UP}/{n}', 'rb').read()) != h} | {r['StoredAs'] for r in rows if sha(open(f"{UP}/{r['StoredAs']}", 'rb').read()) != r['Sha']})
    unlisted = sorted(set(os.listdir(UP)) - {n for _, n in sums} - REPORTS)
    # ---- index every object under its own name ----
    objs = []       # dict(kind, own, where, sha, stored_as)
    for r in rows:
        objs.append(dict(kind='loose', own=r['OriginalName'], where=r['StoredAs'], sha=r['Sha'], stored_as=r['StoredAs'], listed_for=r['WantedName']))
    archives = []   # dict(path, depth, status, members, reason)
    def walk(zf, label, depth):
        n = 0
        for i in zf.infolist():
            if i.is_dir(): continue
            n += 1; path = label + '!' + i.filename
            if i.file_size > MAX_MEMBER:
                archives.append(dict(path=path, depth=depth, status='MEMBER NOT READ (SIZE)', members='', reason=f'{i.file_size} bytes > {MAX_MEMBER}')); continue
            try: data = zf.read(i)
            except Exception as e:
                archives.append(dict(path=path, depth=depth, status='MEMBER UNREADABLE', members='', reason=type(e).__name__ + ': ' + str(e)[:80])); continue
            objs.append(dict(kind='zip', own=os.path.basename(i.filename), where=path, sha=sha(data), stored_as='', listed_for=''))
            if i.filename.lower().endswith('.zip'):
                if depth + 1 > max_depth:
                    archives.append(dict(path=path, depth=depth + 1, status='SKIPPED (DEPTH)', members='', reason=f'depth {depth + 1} > {max_depth}')); continue
                try: inner = zipfile.ZipFile(io.BytesIO(data))
                except Exception as e:
                    archives.append(dict(path=path, depth=depth + 1, status='UNREADABLE', members='', reason=type(e).__name__ + ': ' + str(e)[:80])); continue
                m = walk(inner, path, depth + 1); archives.append(dict(path=path, depth=depth + 1, status='READ', members=m, reason=''))
        return n
    for z in sorted(f for f in os.listdir(UP) if f.lower().endswith('.zip')):
        try: zf = zipfile.ZipFile(f'{UP}/{z}')
        except Exception as e:
            archives.append(dict(path=z, depth=1, status='UNREADABLE', members='', reason=type(e).__name__ + ': ' + str(e)[:80])); continue
        m = walk(zf, z, 1); archives.append(dict(path=z, depth=1, status='READ', members=m, reason=''))
    by_name = collections.defaultdict(list); by_sha = collections.defaultdict(list)
    for o in objs: by_name[norm(o['own'])].append(o); by_sha[o['sha']].append(o)
    all_shas = list(by_sha)
    # ---- B. census ----
    result, cands = {}, {}
    for n, (rec, cited) in W.items():
        kind = ref_kind(rec)
        named = by_name.get(n.lower(), [])
        if kind == 'full': hashed = by_sha.get(rec, [])
        elif kind == 'short': hashed = [o for h in all_shas if agrees(h, rec) for o in by_sha[h]]
        else: hashed = []
        both = [o for o in named if agrees(o['sha'], rec)] if kind != 'none' else []
        other = [o for o in hashed if norm(o['own']) != n.lower()]
        if both: res = 'NAME AND FULL DIGEST' if kind == 'full' else 'NAME AND SHORT DIGEST'
        elif named and kind == 'none': res = 'NAME ONLY (NO RECORDED DIGEST)'
        elif named: res = 'NAME, DIGEST DIFFERS'
        elif hashed: res = 'DIGEST UNDER ANOTHER NAME ONLY'
        else: res = 'NOT FOUND IN INSPECTED SCOPE'
        loose = [o for o in named if o['kind'] == 'loose']; inzip = [o for o in named if o['kind'] == 'zip']
        avail = 'loose and zip' if loose and inzip else ('loose only' if loose else ('zip only' if inzip else ''))
        rep = (both or named or hashed or [None])[0]
        result[n] = dict(wanted_name=n, cited_by=cited, recorded_reference=rec, reference_kind=kind, result=res, name_available=avail,
                         loose_objects_of_name=len(loose), zip_objects_of_name=len(inzip), distinct_contents_under_name=len({o['sha'] for o in named}),
                         representative_location=(rep['where'] if rep else ''), representative_own_name=(rep['own'] if rep else ''),
                         representative_sha256=(rep['sha'] if rep else ''),
                         recorded_digest_under_other_names=' ; '.join(sorted({o['own'] for o in other}))[:300],
                         pairing_of_name_and_digest='extracted automatically; not validated against the citing sentence' if kind != 'none' else '')
        cands[n] = dict(named=[dict(kind=o['kind'], own=o['own'], where=o['where'], sha256=o['sha']) for o in named],
                        recorded_digest_elsewhere=[dict(kind=o['kind'], own=o['own'], where=o['where'], sha256=o['sha']) for o in other])
    wrong_store = [dict(stored_as=r['StoredAs'], own_name=r['OriginalName'], sha256=r['Sha'], listed_for=r['WantedName'])
                   for r in rows if r['WantedName'] and norm(r['OriginalName']) != r['WantedName'].lower() and '__' not in r['StoredAs']]
    incomplete = [a for a in archives if a['status'] != 'READ']
    tot = collections.Counter(v['result'] for v in result.values())
    per = collections.defaultdict(collections.Counter)
    for v in result.values():
        for st in v['cited_by'].split('+'): per[st][v['result']] += 1
    summary = dict(upload=UP, source_files=len(sums), manifest_rows=len(rows), stated_hash_mismatches=bad, files_not_listed=unlisted,
                   objects_indexed=dict(loose=len(rows), zip_members=sum(1 for o in objs if o['kind'] == 'zip')),
                   archives=dict(collections.Counter(a['status'] for a in archives)), archive_search_limits=dict(max_depth=max_depth, max_member_bytes=MAX_MEMBER),
                   archive_coverage_complete=not incomplete, archives_not_fully_read=incomplete,
                   wanted_names=len(W), reference_kinds=dict(collections.Counter(ref_kind(h) for h, _ in W.values())),
                   census_against_the_extracted_list=dict(tot),
                   name_available=dict(collections.Counter(v['name_available'] or 'no object of that name' for v in result.values())),
                   names_with_several_distinct_contents=sum(1 for v in result.values() if v['distinct_contents_under_name'] > 1),
                   per_stream={k: dict(v) for k, v in sorted(per.items())}, loose_files_stored_under_a_name_not_their_own=wrong_store,
                   manifest_status=dict(collections.Counter(r['Status'] for r in rows)), variant_named_files=sum(1 for r in rows if '__' in r['StoredAs']))
    return dict(summary=summary, result=result, candidates=cands, archives=archives, objects=objs)

def privacy_scan(UP):
    """Bounded scan for four generic classes of personal data. Counts only; no matched text is written.
    Two further literal strings specific to the PI's machine were searched by hand on 23 Nov 2026 and are deliberately not written here."""
    classes = {'e-mail address': rb'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}(?![A-Za-z0-9_(.])', 'Windows user path': rb'[A-Za-z]:\\Users\\[A-Za-z0-9._-]+',
               'private key header': rb'BEGIN (?:RSA|OPENSSH|EC) PRIVATE KEY', 'token-like assignment': rb'(?i)(?:password|api[_-]?key|secret)\s*[:=]\s*["\']?[A-Za-z0-9_\-]{12,}'}
    TEXT = ('.md', '.py', '.json', '.jsonl', '.txt', '.csv', '.diff', '.log', '.yaml', '.yml', '.c', '.cpp')
    cnt = collections.Counter(); scanned = dict(loose=0, zip_members=0, zip_members_not_scanned=0)
    def scan(data):
        for k, p in classes.items():
            if re.search(p, data): cnt[k] += 1
    def walk(zf, depth):
        for i in zf.infolist():
            if i.is_dir(): continue
            low = i.filename.lower()
            if low.endswith('.zip') and depth < MAX_DEPTH:
                try: walk(zipfile.ZipFile(io.BytesIO(zf.read(i))), depth + 1)
                except Exception: scanned['zip_members_not_scanned'] += 1
            elif low.endswith(TEXT) and i.file_size <= 20_000_000:
                try: scan(zf.read(i)); scanned['zip_members'] += 1
                except Exception: scanned['zip_members_not_scanned'] += 1
            else: scanned['zip_members_not_scanned'] += 1
    for f in sorted(os.listdir(UP)):
        if f in REPORTS: continue
        if f.lower().endswith(TEXT): scan(open(f'{UP}/{f}', 'rb').read()); scanned['loose'] += 1
        elif f.lower().endswith('.zip'):
            try: walk(zipfile.ZipFile(f'{UP}/{f}'), 1)
            except Exception: scanned['zip_members_not_scanned'] += 1
    return dict(classes=list(classes), files_with_a_match=dict(cnt), scanned=scanned,
                not_scanned='binary and image members (png, npz, pyc, pdf), members over 20 MB, unreadable members')

def rrf_record_digests(UP, objs):
    """The six RRF adoption records: every 64-hex digest each record prints, and the object (if any) that has it.
    The digests are read from the records themselves, not from the wanted list. What role a record gives a digest is not parsed."""
    by_sha = collections.defaultdict(list)
    for o in objs: by_sha[o['sha']].append(o)
    tracked = {}
    for d in ('dsn', 'noncanonical'):
        for f in sorted(os.listdir(d)):
            if os.path.isfile(f'{d}/{f}'): tracked[sha(open(f'{d}/{f}', 'rb').read())] = f'{d}/{f}'
    out = []
    for ed in ('v0_7', 'v0_8', 'v0_8_1', 'v0_8_2', 'v0_8_3', 'v0_8_4'):
        name = f'RTG_RRF_REPRESENTATION_REGISTRY_{ed}_ADOPTION_RECORD.md'
        c = [o for o in objs if o['own'] == name]
        if not c: out.append(dict(record=name, record_location='', record_sha256='', digest='', object_with_digest='', same_as_tracked_file='')); continue
        o = sorted(c, key=lambda x: x['kind'])[0]
        if o['kind'] == 'loose': data = open(f"{UP}/{o['where']}", 'rb').read()
        else:
            parts = o['where'].split('!'); zf = zipfile.ZipFile(f'{UP}/{parts[0]}')
            for q in parts[1:-1]: zf = zipfile.ZipFile(io.BytesIO(zf.read(q)))
            data = zf.read(parts[-1])
        assert sha(data) == o['sha']
        for h in dict.fromkeys(re.findall(rb'(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])', data)):
            h = h.decode(); hit = by_sha.get(h, [])
            out.append(dict(record=name, record_location=o['where'], record_sha256=o['sha'], digest=h,
                            object_with_digest=(sorted(hit, key=lambda x: x['kind'])[0]['own'] if hit else ''), same_as_tracked_file=tracked.get(h, '')))
    return out

# ------------------------------------------------------------------ controls (synthetic fixtures only)
def _fixture(d, files, wanted, zips=()):
    """files: (stored_as, original_name, bytes, wanted_name); zips: (name, bytes)."""
    os.makedirs(d, exist_ok=True); rows = []
    for stored, orig, data, wn in list(files) + [(n, n, b, '') for n, b in zips]:
        open(f'{d}/{stored}', 'wb').write(data); rows.append(dict(StoredAs=stored, Sha=sha(data), OriginalName=orig, WantedName=wn, Status='X', MatchedBy='x'))
    with open(f'{d}/MANIFEST.csv', 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=['StoredAs', 'Sha', 'OriginalName', 'WantedName', 'Status', 'MatchedBy']); w.writeheader(); w.writerows(rows)
    open(f'{d}/SHA256SUMS.txt', 'w', encoding='ascii').write(''.join(f"{r['Sha']}  {r['StoredAs']}\n" for r in rows))
    open(f'{d}/_WANTED_LIST.txt', 'w', encoding='ascii').write(''.join(f'{n}|{h}|S\n' for n, h in wanted))
def _zip(members):
    b = io.BytesIO()
    with zipfile.ZipFile(b, 'w') as z:
        for n, data in members: z.writestr(n, data)
    return b.getvalue()
def controls():
    out = []; base = tempfile.mkdtemp()
    def case(cid, what, files, wanted, zips=(), check=None, mutate=None, **kw):
        d = f'{base}/{cid}'; _fixture(d, files, wanted, zips)
        if mutate: mutate(d)
        r = run(d, **kw); ok = bool(check(r)); out.append(dict(id=cid, what=what, as_expected=ok))
    A, B = b'alpha\n', b'beta\n'
    case('K1', 'full digest and own name: NAME AND FULL DIGEST', [('a.md', 'a.md', A, 'a.md')], [('a.md', sha(A))], check=lambda r: r['result']['a.md']['result'] == 'NAME AND FULL DIGEST')
    case('K2', 'payload altered after the manifest was written: integrity error', [('a.md', 'a.md', A, 'a.md')], [('a.md', sha(A))],
         mutate=lambda d: open(f'{d}/a.md', 'wb').write(B), check=lambda r: r['summary']['stated_hash_mismatches'] == ['a.md'])
    case('K3', 'short prefix~suffix digest gets its own label, not the full-digest one', [('a.md', 'a.md', A, 'a.md')], [('a.md', sha(A)[:8] + '~' + sha(A)[-4:])],
         check=lambda r: r['result']['a.md']['result'] == 'NAME AND SHORT DIGEST' and r['result']['a.md']['recorded_reference'] == sha(A)[:8] + '~' + sha(A)[-4:])
    case('K4', 'a pattern row (empty WantedName) whose own name is wanted is found', [('a.md', 'a.md', A, '')], [('a.md', sha(A))], check=lambda r: r['result']['a.md']['result'] == 'NAME AND FULL DIGEST')
    case('K5', 'a file stored under a wrong name is found under its own name, and not under the stored one', [('b.md', 'a.md', A, 'b.md')], [('a.md', ''), ('b.md', sha(A))],
         check=lambda r: r['result']['a.md']['result'] == 'NAME ONLY (NO RECORDED DIGEST)' and r['result']['b.md']['result'] == 'DIGEST UNDER ANOTHER NAME ONLY'
         and r['summary']['loose_files_stored_under_a_name_not_their_own'][0]['own_name'] == 'a.md')
    case('K6', 'a corrupt nested zip is logged, coverage is reported incomplete', [], [('a.md', sha(A))], zips=[('p.zip', _zip([('inner.zip', b'not a zip')]))],
         check=lambda r: r['result']['a.md']['result'] == 'NOT FOUND IN INSPECTED SCOPE' and not r['summary']['archive_coverage_complete'] and r['summary']['archives'].get('UNREADABLE') == 1)
    case('K7', 'the same content loose and in a zip: available "loose and zip", not zip-only', [('a.md', 'a.md', A, 'a.md')], [('a.md', sha(A))], zips=[('p.zip', _zip([('x/a.md', A)]))],
         check=lambda r: r['result']['a.md']['name_available'] == 'loose and zip' and 'zip only' not in r['summary']['name_available'])
    case('K8', 'two unequal copies of one name are both counted', [('a.md', 'a.md', A, 'a.md'), ('a__1.md', 'a (1).md', B, 'a.md')], [('a.md', '')],
         check=lambda r: r['result']['a.md']['distinct_contents_under_name'] == 2 and r['summary']['names_with_several_distinct_contents'] == 1)
    case('K9', 'an archive beyond the depth limit is logged as skipped', [], [('a.md', sha(A))], zips=[('p.zip', _zip([('l2.zip', _zip([('a.md', A)]))]))], max_depth=1,
         check=lambda r: r['summary']['archives'].get('SKIPPED (DEPTH)') == 1 and not r['summary']['archive_coverage_complete'] and r['result']['a.md']['result'] == 'NOT FOUND IN INSPECTED SCOPE')
    case('K10', 'the same nested archive within the depth limit is read and the file found, zip-only', [], [('a.md', sha(A))], zips=[('p.zip', _zip([('l2.zip', _zip([('a.md', A)]))]))],
         check=lambda r: r['result']['a.md']['result'] == 'NAME AND FULL DIGEST' and r['result']['a.md']['name_available'] == 'zip only' and r['summary']['archive_coverage_complete'])
    case('K11', 'a name whose only copy has another digest: NAME, DIGEST DIFFERS', [('a.md', 'a.md', B, 'a.md')], [('a.md', sha(A))], check=lambda r: r['result']['a.md']['result'] == 'NAME, DIGEST DIFFERS')
    shutil.rmtree(base); return out

if __name__ == '__main__':
    OUT = os.path.dirname(os.path.abspath(__file__))
    ctl = controls(); json.dump(ctl, open(f'{OUT}/intake_controls.json', 'w'), indent=1)
    assert all(c['as_expected'] for c in ctl), [c for c in ctl if not c['as_expected']]
    if '--controls' in sys.argv: print(json.dumps(ctl, indent=1)); sys.exit(0)
    UP = 'upload/corpus-originals-20261123'
    r = run(UP); r['summary']['privacy_scan'] = privacy_scan(UP); r['summary']['controls'] = dict(count=len(ctl), all_as_expected=True)
    cols = ['wanted_name', 'cited_by', 'recorded_reference', 'reference_kind', 'result', 'name_available', 'loose_objects_of_name', 'zip_objects_of_name',
            'distinct_contents_under_name', 'representative_location', 'representative_own_name', 'representative_sha256', 'recorded_digest_under_other_names', 'pairing_of_name_and_digest']
    with open(f'{OUT}/intake_result.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
        for n in sorted(r['result'], key=str.lower): w.writerow(r['result'][n])
    with open(f'{OUT}/intake_archives.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['path', 'depth', 'status', 'members', 'reason']); w.writeheader(); w.writerows(sorted(r['archives'], key=lambda a: a['path']))
    json.dump({n: r['candidates'][n] for n in sorted(r['candidates'], key=str.lower)}, open(f'{OUT}/intake_candidates.json', 'w'), indent=0, ensure_ascii=False)
    rrf = rrf_record_digests(UP, r['objects'])
    with open(f'{OUT}/rrf_adoption_record_digests.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['record', 'record_location', 'record_sha256', 'digest', 'object_with_digest', 'same_as_tracked_file']); w.writeheader(); w.writerows(rrf)
    r['summary']['rrf_adoption_records'] = dict(records_found=len({x['record'] for x in rrf if x['record_sha256']}), digests_printed=sum(1 for x in rrf if x['digest']),
                                                 digests_with_an_object=sum(1 for x in rrf if x['object_with_digest']),
                                                 digests_without_an_object=[x['digest'] for x in rrf if x['digest'] and not x['object_with_digest']])
    json.dump(r['summary'], open(f'{OUT}/intake_summary.json', 'w'), indent=1, ensure_ascii=False)
    s = r['summary']
    print(json.dumps({k: v for k, v in s.items() if k not in ('per_stream', 'loose_files_stored_under_a_name_not_their_own', 'archives_not_fully_read')}, indent=1, ensure_ascii=False))
    for k, v in s['per_stream'].items(): print(f'{k:8}', v)
    assert not s['stated_hash_mismatches'] and not s['files_not_listed']
