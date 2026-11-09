#!/usr/bin/env python3
"""orient.py — read-only reporter for the derived (LIVE_STATE) part of a co-owner session orientation.

It prints what can be observed from Git and GitHub for one study: the governing tag and its release record, the
governing file's hash at the tag and at main, commits after the tag on the study's paths, open PRs that touch those
paths (matched by changed file paths, plus PRs that name a matched PR), and the study's pipe states. Nothing here is
an adoption: a tag is reported with its release-record evidence, never as adopted by itself. The tool never writes to
the repository, never checks out, merges, tags or edits pipe items. Every incomplete observation is reported as
UNVERIFIED (missing permission, failed query, truncated page, unreadable tree), never as "no work". The only file the
tool writes is the optional --json report, and it refuses to replace an existing file unless --replace-json is given.
Revisions 2–3 (9 Nov 2026) answer the receiving review of PR #190 (records/atlas/ORIENT_PR190_RECEIVING_REVIEW_CHATGPT.md):
field-level UNVERIFIED, exact version match for release records, safe tag ordering, renamed paths, PR URLs, an
order-independent dependency closure, and the protected JSON destination.

usage (repository root):
  python3 -I tools/orient.py ATLAS                       # built-in study profile
  python3 -I tools/orient.py KEY --tag-prefix P --file F --paths a/ b/ [--record-glob G] [--json out.json [--replace-json]]
Run `git fetch origin --tags` first; the report states the fetch freshness it could observe.
"""
from __future__ import annotations
import argparse, datetime as dt, fnmatch, json, re, subprocess, sys
from collections import Counter

REPO = 'MustafaAksu/rtg-corpus'
PROFILES = {
    'ATLAS': dict(tag_prefix='atlas-v', file='atlas/RTG_STATE_ATLAS.md',
                  paths=['atlas/', 'records/atlas/', 'pipes/ATLAS/', 'evidence/atlas/', 'tools/atlas_check.py', 'tools/check_compaction.py', 'tools/orient.py'],
                  record_glob='records/atlas/RTG_STATE_ATLAS_v*_RELEASE_RECORD.md'),
}
UNV: list[str] = []

def sh(*a, ok=True):
    try: return subprocess.run(a, text=True, capture_output=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        if ok: raise
        UNV.append(f'{" ".join(a[:3])}…: {getattr(e, "stderr", e)}'.strip()[:200]); return None

def gh_pages(path):
    out, page = [], 1
    while True:
        sep = '&' if '?' in path else '?'
        r = sh('gh', 'api', f'{path}{sep}per_page=100&page={page}', ok=False)
        if r is None: return None
        try: batch = json.loads(r)
        except ValueError as e: UNV.append(f'{path}: response is not JSON ({e})'); return None
        if not isinstance(batch, list): UNV.append(f'{path}: unexpected response shape'); return None
        out += batch
        if len(batch) < 100: return out
        page += 1
        if page > 20: UNV.append(f'pagination stopped at 20 pages for {path}'); return out

def sha_at(ref, path):
    data = subprocess.run(['git', 'show', f'{ref}:{path}'], capture_output=True)
    if data.returncode: UNV.append(f'{path} not readable at {ref}'); return None
    import hashlib; return hashlib.sha256(data.stdout).hexdigest()

def version_key(tag, prefix):
    # numeric parts sort before textual ones; mixed release/candidate tags (v0.10.1, v0.10-r1) never raise
    return [(0, int(x)) if x.isdigit() else (1, x) for x in re.split(r'[.\-]', tag[len(prefix):]) if x]

PR_REF = re.compile(r'(?:(?<![\w/])#|github\.com/' + re.escape(REPO) + r'/pull/)(\d+)\b')

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('key'); ap.add_argument('--tag-prefix'); ap.add_argument('--file')
    ap.add_argument('--paths', nargs='*'); ap.add_argument('--record-glob'); ap.add_argument('--json'); ap.add_argument('--replace-json', action='store_true')
    a = ap.parse_args(); p = dict(PROFILES.get(a.key, {}))
    for k in ('tag_prefix', 'file', 'paths', 'record_glob'):
        if getattr(a, k) is not None: p[k] = getattr(a, k)
    missing = [k for k in ('tag_prefix', 'file', 'paths') if not p.get(k)]
    if missing: sys.exit(f'profile incomplete for {a.key}: give --{", --".join(m.replace("_", "-") for m in missing)}')
    rep = dict(study=a.key, query_time_utc=dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'), repo=REPO, unverified=UNV)

    # refs and freshness
    local_main = sh('git', 'rev-parse', 'origin/main', ok=False)
    remote = sh('git', 'ls-remote', f'https://github.com/{REPO}', 'refs/heads/main', ok=False)
    remote_main = remote.split()[0] if remote else None
    rep['refs'] = dict(local_origin_main=local_main, remote_main=remote_main,
                       local_is_current=(local_main == remote_main) if (local_main and remote_main) else None)
    if not remote_main: UNV.append('remote main ref not observed; freshness UNVERIFIED')
    if not local_main: UNV.append('local origin/main not readable')
    if remote_main and local_main and remote_main != local_main: UNV.append('local origin/main is behind the remote; run git fetch origin --tags')

    # governing tag with its release-record evidence
    tags = [t for t in (sh('git', 'tag', '-l', p['tag_prefix'] + '*') or '').split('\n') if t]
    tags.sort(key=lambda t: version_key(t, p['tag_prefix']))
    rtags = sh('git', 'ls-remote', '--tags', f'https://github.com/{REPO}', p['tag_prefix'] + '*', ok=False)
    remote_tags = sorted({l.split('refs/tags/')[1].replace('^{}', '') for l in rtags.split('\n') if 'refs/tags/' in l}) if rtags else None
    if remote_tags is not None and set(remote_tags) - set(tags): UNV.append(f'remote has tags not fetched locally: {sorted(set(remote_tags) - set(tags))}')
    tag = tags[-1] if tags else None
    g = dict(newest_tag=tag, note='newest tag by version; adoption is shown by the release record below, not by the tag')
    if tag:
        g['tag_type'] = sh('git', 'cat-file', '-t', tag, ok=False); g['target'] = sh('git', 'rev-parse', tag + '^{commit}', ok=False)
        g['file_sha256_at_tag'] = sha_at(tag, p['file']); g['file_sha256_at_main'] = sha_at('origin/main', p['file'])
        g['main_equals_tag'] = g['file_sha256_at_tag'] == g['file_sha256_at_main'] if g['file_sha256_at_tag'] else None
        if p.get('record_glob'):
            files = (sh('git', 'ls-tree', '-r', '--name-only', 'origin/main', ok=False) or '').split('\n')
            recs = [f for f in files if fnmatch.fnmatch(f, p['record_glob'])]
            ver = tag[len(p['tag_prefix']):]
            # the whole version token of the file name must equal the tag version: v0.10.1 is not v0.10, v0_10 is
            def tokens(name): return {m.replace('_', '.') for m in re.findall(r'(?<![0-9A-Za-z])v(\d+(?:[._]\d+)*)(?![0-9])', name)}
            hits = [f for f in recs if ver in tokens(f.rsplit('/', 1)[-1])]
            g['release_record'] = hits or None
            if len(hits) > 1: UNV.append(f'{len(hits)} release records match {tag}; identity ambiguous')
            if hits:
                txt = sh('git', 'show', f'origin/main:{hits[0]}', ok=False)
                if txt is None: g['release_record_status_line'] = None; g['release_record_names_tag_hash'] = None
                else:
                    m = re.search(r'\*\*Status:\*\*\s*([^\n]+)', txt); g['release_record_status_line'] = m.group(1)[:160] if m else None
                    if not m: UNV.append(f'{hits[0]}: no Status line; adoption state UNVERIFIED')
                    g['release_record_names_tag_hash'] = bool(g['file_sha256_at_tag'] and g['file_sha256_at_tag'] in txt)
                    if not g['release_record_names_tag_hash']: UNV.append(f'{hits[0]} does not name the file hash at {tag}; identity UNVERIFIED')
            else: UNV.append(f'no release record matching {p["record_glob"]} for {tag}; adoption UNVERIFIED')
        ahead = sh('git', 'log', '--format=%h %s', f'{g["target"]}..origin/main', '--', *p['paths'], ok=False) if g.get('target') else None
        g['commits_after_tag_on_study_paths'] = ahead.split('\n') if ahead else ([] if ahead == '' else None)
    else: UNV.append(f'no local tag with prefix {p["tag_prefix"]}')
    rep['governing'] = g

    # open PRs by changed paths, plus explicit references to matched PRs
    prs = gh_pages(f'repos/{REPO}/pulls?state=open')
    matched = {}
    if prs is None: rep['open_prs'] = None
    else:
        for pr in prs:
            files = gh_pages(f'repos/{REPO}/pulls/{pr["number"]}/files')
            if files is None: UNV.append(f'PR #{pr["number"]} file list unavailable'); continue
            names = {f.get('filename') for f in files} | {f.get('previous_filename') for f in files}   # renamed-away paths count
            hit = sorted(n for n in names if n and any(n.startswith(x) for x in p['paths']))
            if hit: matched[pr['number']] = dict(number=pr['number'], branch=pr['head']['ref'], base=pr['base']['ref'], draft=pr['draft'], head=pr['head']['sha'][:12], title=pr['title'], files=hit[:8], files_total=len(hit), via='changed paths')
        refs = {pr['number']: {int(n) for n in PR_REF.findall((pr['title'] or '') + ' ' + (pr['body'] or ''))} - {pr['number']} for pr in prs}
        changed = True   # transitive closure over explicit references to matched PRs; a fixpoint, so independent of API order
        while changed:
            changed = False
            for pr in prs:
                if pr['number'] in matched: continue
                dep = refs[pr['number']] & set(matched)
                if dep:
                    matched[pr['number']] = dict(number=pr['number'], branch=pr['head']['ref'], base=pr['base']['ref'], draft=pr['draft'], head=pr['head']['sha'][:12], title=pr['title'], via=f'names matched PR(s) {sorted(dep)}'); changed = True
        rep['open_prs'] = dict(scanned=len(prs), matched=[matched[k] for k in sorted(matched)])

    # pipes
    tree = sh('git', 'ls-tree', '-r', '--name-only', 'origin/main', 'pipes/', ok=False)
    files = tree.split('\n') if tree is not None else []
    inbox, outbound, items, unread = Counter(), Counter(), [], []
    if tree is None: UNV.append('pipes/ tree not readable at origin/main; pipe states UNVERIFIED')
    for f in files:
        if not re.match(r'pipes/[A-Z0-9]+/2\d+.*\.md$', f): continue
        t = sh('git', 'show', f'origin/main:{f}', ok=False)
        st = re.search(r'^state:\s*(\S+)', t, re.M) if t is not None else None; frm = re.search(r'^from:\s*(\S+)', t, re.M) if t is not None else None
        if not (st and frm): unread.append(f); UNV.append(f'{f}: not readable or front matter missing; counts below are incomplete'); continue
        if f.startswith(f'pipes/{a.key}/'): inbox[st.group(1)] += 1; (st.group(1) != 'closed') and items.append(f'{f} [{st.group(1)}]')
        if frm.group(1) == a.key and st.group(1) != 'closed': outbound[f'{f.split("/")[1]}:{st.group(1)}'] += 1; items.append(f'{f} [{st.group(1)}, outbound]')
    rep['pipes'] = (dict(inbox=dict(inbox), outbound_not_closed=dict(outbound), not_closed_items=items, unreadable=unread, complete=not unread)
                    if tree is not None else dict(inbox=None, outbound_not_closed=None, not_closed_items=None, unreadable=None, complete=False))
    rep['status'] = 'PARTIAL/UNVERIFIED' if UNV else 'COMPLETE (observations only; no adoption inferred)'

    # report
    print(f"## {a.key} — derived state, {rep['query_time_utc']}  ·  {rep['status']}")
    r = rep['refs']; print(f"- refs: local origin/main {str(r['local_origin_main'])[:12]}, remote main {str(r['remote_main'])[:12]}, local current: {r['local_is_current']}")
    if tag:
        print(f"- newest tag {tag} ({g.get('tag_type')}) -> {str(g.get('target'))[:12]}; {p['file']} sha256 at tag {str(g.get('file_sha256_at_tag'))[:12]}…, main equals tag: {g.get('main_equals_tag')}")
        print(f"- release record: {g.get('release_record')}; status line: {g.get('release_record_status_line', 'n/a')}; names the tag hash: {g.get('release_record_names_tag_hash', 'n/a')}")
        c = g.get('commits_after_tag_on_study_paths'); print(f"- commits after the tag on study paths: {len(c) if c is not None else 'UNVERIFIED'}" + (''.join(f'\n    {x}' for x in c) if c else ''))
    if rep['open_prs'] is None: print('- open PRs: UNVERIFIED (GitHub query failed)')
    else:
        print(f"- open PRs scanned: {rep['open_prs']['scanned']}; matched: {len(rep['open_prs']['matched'])}")
        for m in rep['open_prs']['matched']:
            extra = f" {m['files_total']} files, e.g. {', '.join(m['files'][:3])}" if 'files' in m else ''
            print(f"    #{m['number']} {m['branch']} -> {m['base']} ({'draft' if m['draft'] else 'ready'}, head {m['head']}) via {m['via']}:{extra}")
    if tree is None: print(f'- pipes/{a.key}/: UNVERIFIED (tree not readable)')
    elif unread: print(f"- pipes/{a.key}/: INCOMPLETE — {len(unread)} item(s) unreadable, counts are lower bounds: inbox {dict(inbox)}; outbound not closed {dict(outbound)}" + ''.join(f'\n    {x}' for x in items) + ''.join(f'\n    UNREADABLE {x}' for x in unread))
    else: print(f"- pipes/{a.key}/ inbox: {rep['pipes']['inbox'] or 'none'}; outbound not closed: {rep['pipes']['outbound_not_closed'] or 'none'}" + ''.join(f'\n    {x}' for x in items))
    if UNV: print('- UNVERIFIED:' + ''.join(f'\n    {u}' for u in UNV))
    if a.json:
        import os
        payload = (json.dumps(rep, ensure_ascii=False, indent=1) + '\n').encode('utf-8')
        if os.path.islink(a.json): print(f'- JSON not written: {a.json} is a symbolic link; the reporter writes only a regular file it creates itself')
        else:
            flags = os.O_WRONLY | os.O_CREAT | getattr(os, 'O_NOFOLLOW', 0) | (os.O_TRUNC if a.replace_json else os.O_EXCL)
            try:
                fd = os.open(a.json, flags, 0o644); os.write(fd, payload); os.close(fd)
            except FileExistsError: print(f'- JSON not written: {a.json} exists (pass --replace-json to replace a report file you own)')
            except OSError as e: print(f'- JSON not written: {a.json}: {e.strerror}')

if __name__ == '__main__':
    main()
