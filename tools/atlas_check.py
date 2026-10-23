#!/usr/bin/env python3
"""RTG State Atlas checker (report-only).

Implements the checks of atlas/RTG_STATE_ATLAS_METHOD.md §7:
  sources        source table == frozen manifest == BASELINE.md; manifest hashes == tagged bytes
  coverage       typed coverage of re-extracted sources (DYAD RIDs, RER local keys, METH section keys)
  qualifiers     conditional DYAD results keep a conditional marker on their atlas node
  links          every cited RID resolves to a declaration in its owner's file at the snapshot tag;
                 documented phantoms (L5) are reported separately, never as resolved
  artifacts      cited artifact RIDs and cert scripts resolve in the owner file
  wording        history/process phrases (warnings only)

PASS, FAIL and UNVERIFIED are kept separate; unparsed or unchecked items are never PASS.
Exit code: 0 no FAIL, 1 at least one FAIL, 2 usage/input error.

Usage:
  python3 tools/atlas_check.py [--atlas PATH] [--manifest PATH] [--report PATH] [--json PATH]
  python3 tools/atlas_check.py --self-test     # negative controls
"""
import argparse, hashlib, json, os, re, subprocess, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEF_ATLAS = os.path.join(ROOT, 'atlas', 'RTG_STATE_ATLAS.md')
DEF_MANIFEST = os.path.join(ROOT, 'evidence', 'atlas', 'source_manifest_v0_2.json')
DEF_DISP = os.path.join(ROOT, 'evidence', 'atlas', 'coverage_dispositions_v0_2.json')
BASELINE = os.path.join(ROOT, 'BASELINE.md')

# RID namespace -> source key (METH v1.4 §4.2). Longest prefix first.
NAMESPACES = [('RTG-OFN-', 'OFN'), ('DYAD-', 'DYAD'), ('TRIAD-', 'TRIAD'), ('GEN-', 'GEN'),
              ('TDRG-', 'TDRG'), ('RECOG-', 'RECOG'), ('DZT-', 'DZT'), ('AZ-', 'AZ'),
              ('UVM-', 'UVM'), ('NUMGEN-', 'NUMGEN'), ('RRF-', 'RRF'), ('PL-', 'PREL'),
              ('L0L1-', 'LEGACY'), ('L2-', 'LEGACY'), ('RTG-', 'PROG')]
TYPEWORDS = r'(?:THM|ALG|DEF|NUM|OBS|HYP|CAND|RESULT|OPEN|ART|ENG|FAIL|CONV|EXPORT|NOGO|INTERP|HEUR|RES)'
RID_RE = re.compile(r'(?<![A-Za-z0-9_-])(?:RTG-OFN|DYAD|TRIAD|GEN|TDRG|RECOG|DZT|AZ|UVM|NUMGEN|RRF|PL|L0L1|L2|RTG)-'
                    + TYPEWORDS + r'(?:-[A-Z0-9]+)+(?![A-Za-z0-9_])')
SCRIPT_RE = re.compile(r'[A-Za-z0-9_]+\.(?:py|cpp|ipynb)\b')
WORDING = [r'\bnow\b', r'\bpreviously\b', r'\bformerly\b', r'\bno longer\b', r'\bresolved\b', r'\badvisor(?:y|ies)\b',
           r'\bpending\b', r'\bmerge-time\b', r'\bat merge\b', r'\bthis refresh\b', r'\bwas\b', r'\bv0\.1\b(?! retained)']


def git_show(tag, path):
    r = subprocess.run(['git', '-C', ROOT, 'show', f'{tag}:{path}'], capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout


def git_commit(tag):
    r = subprocess.run(['git', '-C', ROOT, 'rev-list', '-n', '1', tag], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def owner_of(rid):
    for p, k in NAMESPACES:
        if rid.startswith(p):
            return k
    return None


class Report:
    def __init__(self):
        self.rows = []  # (check, status, item, detail)

    def add(self, check, status, item, detail=''):
        self.rows.append((check, status, item, detail))

    def count(self, check=None):
        c = defaultdict(int)
        for ch, st, _, _ in self.rows:
            if check is None or ch == check:
                c[st] += 1
        return dict(c)

    def fails(self):
        return [r for r in self.rows if r[1] == 'FAIL']


# ---------------------------------------------------------------- atlas parsing
class Atlas:
    def __init__(self, text):
        self.text = text
        self.lines = text.split('\n')
        self.kind = []  # per line: 'source', 'l5', 'node', 'other'
        sec = None
        for l in self.lines:
            if l.startswith('## ') or l.startswith('### '):
                if l.startswith('## SOURCES'):
                    sec = 'source'
                elif ('L5' in l) or l.startswith('## HEADLINE') or l.startswith('## D-WRONG'):
                    sec = 'l5'
                else:
                    sec = 'node'
                self.kind.append('heading')
                continue
            self.kind.append(sec or 'other')

    def source_table(self):
        rows = {}
        for l, k in zip(self.lines, self.kind):
            if k == 'source' and l.startswith('| ') and not l.startswith('| key') and not l.startswith('|---'):
                cells = [c.strip() for c in l.strip('|').split('|')]
                if len(cells) >= 4:
                    rows[cells[0]] = {'document': cells[1], 'edition': cells[2], 'tag': cells[3].strip('`'), 'class': cells[4] if len(cells) > 4 else ''}
        return rows

    @staticmethod
    def segments(line):
        return [s.strip() for s in line.split(' | ')]

    def occurrences(self, token):
        """Return list of (line_no, kind, in_cert_only_segment, is_node_id)."""
        out = []
        pat = re.compile(r'(?<![A-Za-z0-9_-])' + re.escape(token) + r'(?![A-Za-z0-9_])')
        for i, (l, k) in enumerate(zip(self.lines, self.kind)):
            if not pat.search(l):
                continue
            segs = self.segments(l)
            hit = [s for s in segs if pat.search(s)]
            cert_only = all(s.lower().startswith(('cert', 'certs', 'evidence', 'archive')) for s in hit)
            first = l.split(' ')[0].strip('*')
            out.append((i + 1, k, cert_only, first == token))
        return out


# ---------------------------------------------------------------- checks
def check_sources(rep, atlas, manifest):
    ch = 'sources'
    table = atlas.source_table()
    man = {s['key']: s for s in manifest['sources']}
    for key, row in table.items():
        m = man.get(key)
        if not m:
            rep.add(ch, 'FAIL', key, 'source-table row has no manifest entry')
            continue
        ed_ok = row['edition'].split()[0] == m['edition'].split()[0]
        tag_ok = row['tag'] == m['tag']
        rep.add(ch, 'PASS' if (ed_ok and tag_ok) else 'FAIL', key,
                f"table {row['edition']} `{row['tag']}` vs manifest {m['edition']} `{m['tag']}`")
    for key in man:
        if key not in table:
            rep.add(ch, 'FAIL', key, 'manifest entry missing from atlas source table')
    base = open(BASELINE, encoding='utf-8').read() if os.path.exists(BASELINE) else ''
    for key, m in man.items():
        data = git_show(m['tag'], m['path'])
        if data is None:
            rep.add(ch, 'FAIL', key, f"tag {m['tag']} or path {m['path']} not resolvable")
            continue
        h = hashlib.sha256(data).hexdigest()
        rep.add(ch, 'PASS' if h == m['sha256'] else 'FAIL', key + ' sha256', f'tagged bytes {h[:12]}… vs manifest {m["sha256"][:12]}…')
        c = git_commit(m['tag'])
        rep.add(ch, 'PASS' if c == m.get('commit') else 'FAIL', key + ' commit', f'{(c or "?")[:12]} vs {m.get("commit", "?")[:12]}')
        fname = os.path.basename(m['path'])
        brow = [l for l in base.split('\n') if f'`{fname}`' in l]
        if not brow:
            rep.add(ch, 'UNVERIFIED', key + ' baseline', f'{fname} not listed in BASELINE.md')
        else:
            ok = (m['sha256'] in brow[0]) and (f"`{m['tag']}`" in brow[0])
            rep.add(ch, 'PASS' if ok else 'FAIL', key + ' baseline', 'BASELINE row hash+tag ' + ('match' if ok else 'differ'))


def load_sources(manifest):
    src = {}
    for s in manifest['sources']:
        d = git_show(s['tag'], s['path'])
        src[s['key']] = d.decode('utf-8', 'replace') if d is not None else None
    return src


def declared_rids(text):
    """RIDs in a declaration form: [RID: ...] tag, heading line, first table cell, `RID:` field."""
    dec = set()
    for m in re.finditer(r'\[RID:([^\]]*)\]', text):
        dec.update(RID_RE.findall(m.group(1)))
    for l in text.split('\n'):
        s = l.strip()
        if s.startswith('#'):
            dec.update(RID_RE.findall(s))
        elif s.startswith('|'):
            cells = s.strip('|').split('|')
            if cells:
                dec.update(RID_RE.findall(cells[0]))
        if re.search(r'\bRID\b\s*[:=]', s):
            dec.update(RID_RE.findall(s))
        m = re.match(r'^\s*(?:[-*]\s*)?(?:\*\*)?`?\[?(?:[A-Z]+\]\s*)?`?((?:%s)-%s(?:-[A-Z0-9]+)+)`?' % ('|'.join(p.rstrip('-') for p, _ in NAMESPACES), TYPEWORDS), s)
        if m:
            dec.add(m.group(1))
    return dec


def dyad_declarations(text):
    """DYAD declarations via [RID: X] tags only, with the declaring line."""
    out = {}
    for l in text.split('\n'):
        for m in re.finditer(r'\[RID:([^\]]*)\]', l):
            for r in RID_RE.findall(m.group(1)):
                out.setdefault(r, l)
    return out


def l5_lines_text(atlas):
    return '\n'.join(l for l, k in zip(atlas.lines, atlas.kind) if k == 'l5')


def check_coverage(rep, atlas, src, disp):
    ch = 'coverage'
    # DYAD scientific RIDs
    dy = dyad_declarations(src['DYAD'] or '')
    for rid, line in sorted(dy.items()):
        if '-ART-' in rid:
            continue
        if rid in disp.get('DYAD', {}):
            rep.add(ch, 'PASS', rid, 'out-of-scope disposition: ' + disp['DYAD'][rid])
            continue
        occ = atlas.occurrences(rid)
        good = [o for o in occ if o[1] == 'node' and not o[2]]
        if good:
            rep.add(ch, 'PASS', rid, f'node/edge at line {good[0][0]}')
        elif occ:
            where = sorted(set(o[1] + ('/cert' if o[2] else '') for o in occ))
            rep.add(ch, 'FAIL', rid, 'only in ' + ', '.join(where) + ' (does not cover the claim)')
        else:
            rep.add(ch, 'FAIL', rid, 'not in atlas')
    # RER local keys
    rer = src.get('RER') or ''
    keys = set(re.findall(r'^### (RER-[A-Z0-9-]+) ', rer, re.M))
    keys |= set(re.findall(r'^\| `(RER-[A-Z0-9]+)` \|', rer, re.M))
    for k in sorted(keys):
        if k in disp.get('RER', {}):
            rep.add(ch, 'PASS', k, 'out-of-scope disposition: ' + disp['RER'][k])
            continue
        occ = atlas.occurrences(k)
        good = [o for o in occ if o[1] == 'node' and not o[2]]
        rep.add(ch, 'PASS' if good else 'FAIL', k, f'line {good[0][0]}' if good else ('only in L5/cert' if occ else 'not in atlas'))
    # METH section keys cited by the atlas
    meth = src.get('METH') or ''
    heads = set()
    for l in meth.split('\n'):
        m = re.match(r'^#{2,4}\s+(?:§\s*)?(\d+(?:\.\d+)*)[.\s]', l)
        if m:
            heads.add(m.group(1))
    cited = set()
    for l in atlas.lines:
        for m in re.finditer(r'(?:METH|DSN_METHODOLOGY)(?: v1\.4)? (§§?[\d.,\s§]+)', l):
            for n in re.findall(r'\d+(?:\.\d+)*', m.group(1)):
                cited.add(n.rstrip('.'))
    for n in sorted(cited, key=lambda x: [int(p) for p in x.split('.')]):
        ok = n in heads or any(h.startswith(n + '.') for h in heads)
        rep.add(ch, 'PASS' if ok else 'FAIL', 'METH §' + n, 'section exists in v1.4' if ok else 'no such section in v1.4')


COND_MARKERS = ('·c', 'if:', 'if ', 'assuming', 'conditional', 'cond.', '[assuming')


def check_qualifiers(rep, atlas, src):
    ch = 'qualifiers'
    dy = dyad_declarations(src['DYAD'] or '')
    for rid, line in sorted(dy.items()):
        if '-ART-' in rid or '[assuming' not in line:
            continue
        nodes = [atlas.lines[o[0] - 1] for o in atlas.occurrences(rid) if o[3] and atlas.kind[o[0] - 1] == 'node']
        if not nodes:
            rep.add(ch, 'UNVERIFIED', rid, 'conditional owner result has no atlas node line to check')
            continue
        ok = any(any(mk in n for mk in COND_MARKERS) for n in nodes)
        rep.add(ch, 'PASS' if ok else 'FAIL', rid, 'conditional marker kept' if ok else 'owner result is conditional; atlas node lost the qualifier')


def check_links(rep, atlas, src):
    ch = 'links'
    decl = {k: declared_rids(v) if v else set() for k, v in src.items()}
    l5 = l5_lines_text(atlas)
    seen = {}
    for i, (l, k) in enumerate(zip(atlas.lines, atlas.kind)):
        if k in ('source', 'heading'):
            continue
        for rid in RID_RE.findall(l):
            seen.setdefault(rid, set()).add(k)
    for rid in sorted(seen):
        own = owner_of(rid)
        if own is None or src.get(own) is None:
            rep.add(ch, 'UNVERIFIED', rid, f'owner {own} not in snapshot')
            continue
        if rid in decl[own]:
            rep.add(ch, 'PASS', rid, f'declared in {own}')
            continue
        present = re.search(r'(?<![A-Za-z0-9_-])' + re.escape(rid) + r'(?![A-Za-z0-9_])', src[own]) is not None
        only_l5 = seen[rid] <= {'l5'}
        if present:
            rep.add(ch, 'UNVERIFIED', rid, f'present in {own} but not in a recognized declaration form')
        elif only_l5:
            rep.add(ch, 'DOCUMENTED-UNRESOLVED', rid, f'absent from {own}; cited only in L5 (phantom or consumer string)')
        else:
            rep.add(ch, 'FAIL', rid, f'absent from owner {own} at its tag; cited outside L5')


def check_artifacts(rep, atlas, src):
    ch = 'artifacts'
    allsrc = '\n'.join(v for v in src.values() if v)
    for i, (l, k) in enumerate(zip(atlas.lines, atlas.kind)):
        if k != 'node':
            continue
        first = l.split(' ')[0].strip('*')
        own = owner_of(first)
        if own is None:
            m = re.match(r'\*?([A-Z0-9]+)[:-]', l)
            key = m.group(1) if m else None
            own = {'ER2B': 'ER2B', 'RER': 'RER', 'FMS': 'FMS', 'PL': 'PREL', 'UVM': 'UVM'}.get(key, key if key in src else None)
        for seg in Atlas.segments(l):
            if not seg.lower().startswith(('cert', 'certs', 'evidence')):
                continue
            for art in re.findall(r'(?:DYAD|TRIAD|GEN|RECOG|NUMGEN|UVM|TDRG|DZT|AZ)-ART-[A-Z0-9-]+', seg):
                o = owner_of(art)
                okd = src.get(o) and re.search(re.escape(art) + r'(?![A-Z0-9-])', src[o])
                rep.add(ch, 'PASS' if okd else 'FAIL', art, f'line {i + 1}: ' + ('in owner file' if okd else f'not in owner {o}'))
            for sc in SCRIPT_RE.findall(seg):
                if own and src.get(own) and sc in src[own]:
                    rep.add(ch, 'PASS', sc, f'line {i + 1}: named in {own}')
                elif sc in allsrc:
                    rep.add(ch, 'UNVERIFIED', sc, f'line {i + 1}: named in a source other than the line owner ({own})')
                else:
                    rep.add(ch, 'FAIL', sc, f'line {i + 1}: script named in no source file')


def check_wording(rep, atlas):
    ch = 'wording'
    for i, (l, k) in enumerate(zip(atlas.lines, atlas.kind)):
        if k in ('source', 'heading'):
            continue
        for w in WORDING:
            for m in re.finditer(w, l, re.I):
                ctx = l[max(0, m.start() - 40):m.end() + 40].replace('\n', ' ')
                rep.add(ch, 'WARN', f'line {i + 1}', f'"{m.group(0)}": …{ctx}…')


def run(atlas_text, manifest, src, disp, with_sources=True):
    rep = Report()
    atlas = Atlas(atlas_text)
    if with_sources:
        check_sources(rep, atlas, manifest)
    check_coverage(rep, atlas, src, disp)
    check_qualifiers(rep, atlas, src)
    check_links(rep, atlas, src)
    check_artifacts(rep, atlas, src)
    check_wording(rep, atlas)
    return rep


def write_report(rep, path, meta):
    out = ['# Atlas check report', '', f"atlas: `{meta['atlas']}` sha256 `{meta['atlas_sha']}`; manifest `{meta['manifest']}`", '',
           '| check | PASS | FAIL | UNVERIFIED | other |', '|---|---|---|---|---|']
    for ch in ['sources', 'coverage', 'qualifiers', 'links', 'artifacts', 'wording']:
        c = rep.count(ch)
        other = {k: v for k, v in c.items() if k not in ('PASS', 'FAIL', 'UNVERIFIED')}
        out.append(f"| {ch} | {c.get('PASS', 0)} | {c.get('FAIL', 0)} | {c.get('UNVERIFIED', 0)} | {', '.join(f'{k} {v}' for k, v in other.items()) or '—'} |")
    out += ['', 'Unparsed or unchecked items are not PASS. Content fidelity is a matter for the change-focused review.', '']
    for st in ['FAIL', 'UNVERIFIED', 'DOCUMENTED-UNRESOLVED', 'WARN']:
        rows = [r for r in rep.rows if r[1] == st]
        if rows:
            out += [f'## {st} ({len(rows)})', '']
            out += [f'- {r[0]} · {r[2]} — {r[3]}' for r in rows]
            out.append('')
    open(path, 'w', encoding='utf-8').write('\n'.join(out))


# ---------------------------------------------------------------- negative controls
def self_test(manifest, src, disp, base_text):
    results = []
    base = run(base_text, manifest, src, disp, with_sources=False)
    base_fail = {(r[0], r[2]) for r in base.fails()}
    atlas = Atlas(base_text)

    def new_fails(text):
        r = run(text, manifest, src, disp, with_sources=False)
        return r, [x for x in r.fails() if (x[0], x[2]) not in base_fail]

    L = base_text.split('\n')
    # NC1 omitted claim whose RID survives elsewhere (L5)
    dy = dyad_declarations(src['DYAD'])
    target = None
    for rid in sorted(dy):
        if '-ART-' in rid:
            continue
        occ = [o for o in atlas.occurrences(rid) if o[1] == 'node' and not o[2]]
        if len(occ) == 1 and occ[0][3]:
            target = (rid, occ[0][0]); break
    if target:
        rid, ln = target
        M = L[:]; del M[ln - 1]
        l5i = next(i for i, k in enumerate(Atlas('\n'.join(M)).kind) if k == 'l5' and M[i].strip())
        M[l5i] += f' (see {rid})'
        r, nf = new_fails('\n'.join(M))
        results.append(('NC1 omitted claim, RID kept in L5', rid, any(x[0] == 'coverage' and x[2] == rid for x in nf)))
    else:
        results.append(('NC1 omitted claim, RID kept in L5', 'no single-node RID found', False))
    # NC2 wrong owner
    ni = next(i for i, k in enumerate(atlas.kind) if k == 'node' and L[i].startswith('DYAD-THM-'))
    M = L[:]; M[ni] += ' | <GEN-THM-SMOOTH-EMBEDDING'
    r, nf = new_fails('\n'.join(M))
    results.append(('NC2 wrong owner', 'GEN-THM-SMOOTH-EMBEDDING', any(x[0] == 'links' and x[2] == 'GEN-THM-SMOOTH-EMBEDDING' for x in nf)))
    # NC3 lost qualifier
    cond = [rid for rid, l in dy.items() if '[assuming' in l and '-ART-' not in rid]
    hit = None
    for rid in sorted(cond):
        nodes = [o[0] for o in atlas.occurrences(rid) if o[3] and atlas.kind[o[0] - 1] == 'node']
        if nodes:
            hit = (rid, nodes); break
    if hit:
        rid, nodes = hit
        M = L[:]
        for ln in nodes:
            s = M[ln - 1]
            for mk in COND_MARKERS:
                s = s.replace(mk, '')
            M[ln - 1] = s
        r, nf = new_fails('\n'.join(M))
        results.append(('NC3 lost qualifier', rid, any(x[0] == 'qualifiers' and x[2] == rid for x in nf)))
    else:
        results.append(('NC3 lost qualifier', 'no conditional node found', False))
    # NC4 invalid artifact target
    M = L[:]; M[ni] += ' | cert DYAD-ART-NO-SUCH-CERTIFICATE'
    r, nf = new_fails('\n'.join(M))
    results.append(('NC4 invalid artifact target', 'DYAD-ART-NO-SUCH-CERTIFICATE', any(x[0] == 'artifacts' and x[2] == 'DYAD-ART-NO-SUCH-CERTIFICATE' for x in nf)))
    # NC5 missing artifact link (script named nowhere)
    M = L[:]; M[ni] += ' | cert no_such_owner_script_zz9.py'
    r, nf = new_fails('\n'.join(M))
    results.append(('NC5 missing artifact link', 'no_such_owner_script_zz9.py', any(x[0] == 'artifacts' and x[2] == 'no_such_owner_script_zz9.py' for x in nf)))
    # NC6 unknown RID accepted only via L5: must be DOCUMENTED-UNRESOLVED (never PASS); in a node it must FAIL
    fake = 'DYAD-THM-FAKE-ONLY-ZZ9'
    M = L[:]
    l5i = next(i for i, k in enumerate(atlas.kind) if k == 'l5' and L[i].strip())
    M[l5i] += f' {fake}'
    r = run('\n'.join(M), manifest, src, disp, with_sources=False)
    st = [x[1] for x in r.rows if x[0] == 'links' and x[2] == fake]
    results.append(('NC6a unknown RID only in L5 not resolved', fake, st == ['DOCUMENTED-UNRESOLVED']))
    M[ni] += f' | <{fake}'
    r, nf = new_fails('\n'.join(M))
    results.append(('NC6b unknown RID in a node fails', fake, any(x[0] == 'links' and x[2] == fake for x in nf)))
    # NC7 source-table mismatch
    M = [l.replace('| v6.4.22 | `dyad-v6.4.22`', '| v6.4.21 | `dyad-v6.4.21`') for l in L]
    r = run('\n'.join(M), manifest, src, disp, with_sources=True)
    results.append(('NC7 source table mismatch', 'DYAD', any(x[0] == 'sources' and x[2] == 'DYAD' for x in r.fails())))
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--atlas', default=DEF_ATLAS)
    ap.add_argument('--manifest', default=DEF_MANIFEST)
    ap.add_argument('--dispositions', default=DEF_DISP)
    ap.add_argument('--report')
    ap.add_argument('--json')
    ap.add_argument('--self-test', action='store_true')
    a = ap.parse_args()
    try:
        manifest = json.load(open(a.manifest, encoding='utf-8'))
        text = open(a.atlas, encoding='utf-8').read()
    except OSError as e:
        print(e, file=sys.stderr); return 2
    disp = json.load(open(a.dispositions, encoding='utf-8')) if os.path.exists(a.dispositions) else {}
    src = load_sources(manifest)
    if a.self_test:
        res = self_test(manifest, src, disp, text)
        ok = all(r[2] for r in res)
        for name, item, passed in res:
            print(f"{'PASS' if passed else 'FAIL'}  {name}  [{item}]")
        print('negative controls:', 'all detected' if ok else 'NOT all detected')
        return 0 if ok else 1
    rep = run(text, manifest, src, disp)
    meta = {'atlas': os.path.relpath(a.atlas, ROOT), 'atlas_sha': hashlib.sha256(text.encode('utf-8')).hexdigest(),
            'manifest': os.path.relpath(a.manifest, ROOT)}
    for ch in ['sources', 'coverage', 'qualifiers', 'links', 'artifacts', 'wording']:
        print(f'{ch:11s}', rep.count(ch))
    if a.report:
        write_report(rep, a.report, meta)
    if a.json:
        json.dump({'meta': meta, 'rows': rep.rows}, open(a.json, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return 1 if rep.fails() else 0


if __name__ == '__main__':
    sys.exit(main())
