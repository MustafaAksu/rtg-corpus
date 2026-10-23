#!/usr/bin/env python3
"""RTG State Atlas checker (report-only).

Implements the checks of atlas/RTG_STATE_ATLAS_METHOD.md §7:
  sources      source table == frozen manifest == BASELINE.md; manifest hashes/commits == tagged bytes
  coverage     typed source-item -> home map for re-extracted sources (DYAD RIDs, RER local keys)
               and METH section keys; a dependency mention, an index/L0 mention, an L5 mention
               or a cert field is never a home
  qualifiers   NARROW: DYAD declarations carrying [assuming: X] keep an explicit conditional marker
               and the named prerequisite X on their atlas node; 'unconditional' never qualifies
  links        cited RIDs resolve to an ACTIVE owner declaration; owner-denied names, historical
               labels and classified consumer strings are typed DOCUMENTED-UNRESOLVED (never PASS);
               unrecognized declaration syntax stays UNVERIFIED
  artifacts    cited artifact RIDs exist in the owner file; cert script names are named in the
               owner file (naming only: availability and execution are not checked)
  keys         no retired L5 diagnostic key is referenced in the atlas
  process      advisory keys / process-status phrases (FAIL); other history-like words (WARN)

PASS, FAIL and UNVERIFIED are kept separate; unparsed or unchecked items are never PASS.
Exit code: 0 no FAIL, 1 at least one FAIL, 2 usage/input error.

Usage:
  python3 tools/atlas_check.py [--atlas PATH] [--manifest PATH] [--report PATH] [--json PATH]
  python3 tools/atlas_check.py --self-test     # negative controls (incl. receiving-review fixtures RV-*)
"""
import argparse, hashlib, json, os, re, subprocess, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EV = os.path.join(ROOT, 'evidence', 'atlas')
DEF_ATLAS = os.path.join(ROOT, 'atlas', 'RTG_STATE_ATLAS.md')
DEF_MANIFEST = os.path.join(EV, 'source_manifest_v0_2.json')
DEF_COVMAP = os.path.join(EV, 'coverage_map_v0_2.json')
DEF_IDMAP = os.path.join(EV, 'owner_identifier_map_v0_2.json')
DEF_RETIRED = os.path.join(EV, 'retired_l5_keys_v0_2.json')
BASELINE = os.path.join(ROOT, 'BASELINE.md')

# RID namespace -> source key (METH v1.4 §4.2). Longest prefix first.
NAMESPACES = [('RTG-OFN-', 'OFN'), ('DYAD-', 'DYAD'), ('TRIAD-', 'TRIAD'), ('GEN-', 'GEN'),
              ('TDRG-', 'TDRG'), ('RECOG-', 'RECOG'), ('DZT-', 'DZT'), ('AZ-', 'AZ'),
              ('UVM-', 'UVM'), ('NUMGEN-', 'NUMGEN'), ('RRF-', 'RRF'), ('PL-', 'PREL'),
              ('L0L1-', 'LEGACY'), ('L2-', 'LEGACY'), ('RTG-', 'PROG')]
TAG_CONVENTION = {'DYAD'}  # owners whose active declarations are exactly their [RID: ...] tags
TYPEWORDS = r'(?:THM|ALG|DEF|NUM|OBS|HYP|CAND|RESULT|OPEN|ART|ENG|FAIL|CONV|EXPORT|NOGO|INTERP|HEUR|RES|CF)'
RID_RE = re.compile(r'(?<![A-Za-z0-9_-])(?:RTG-OFN|DYAD|TRIAD|GEN|TDRG|RECOG|DZT|AZ|UVM|NUMGEN|RRF|PL|L0L1|L2|RTG)-'
                    + TYPEWORDS + r'(?:-[A-Z0-9]+)+(?![A-Za-z0-9_])')
SCRIPT_RE = re.compile(r'[A-Za-z0-9_]+\.(?:py|cpp|ipynb)\b')
DENIAL_RE = re.compile(r'never an? [A-Za-z ]{0,20}identifier|is not an? [A-Za-z ]{0,30}(?:identifier|RID)|does not exist|'
                       r'historical note label|no alias (?:is )?created|unmatched', re.I)
ATLAS_UNRESOLVED_MARK = re.compile(r'phantom|historical note label|not an? (?:owner |DYAD )?RIDs?\b|not owner RIDs|'
                                   r'never a\b|does not exist|is a DYAD RID|unmatched|consumer string|App F', re.I)
COND_RE = re.compile(r'·c(?![A-Za-z])|\bif:|\bif\b|\bassuming\b|(?<![A-Za-z])conditional\b')
UNCOND_RE = re.compile(r"(?<!¬ )\bunconditional\b", re.I)
PROCESS_FAIL = [r'\bFC-[A-Z]+-\d+\b', r'\bTier-[A-C]\b', r'\bAdvisory\b', r'\bpass (?:one|two) (?:done|pending)\b',
                r'\bnot started\b', r'\bgovernance only\b', r'\b(?:notices?|receipts?) (?:pending|unsent)\b']
WORDING = [r'\bnow\b', r'\bpreviously\b', r'\bformerly\b', r'\bno longer\b', r'\bresolved\b', r'\bpending\b',
           r'\bwas\b', r'\bthis refresh\b']


def git_show(tag, path):
    r = subprocess.run(['git', '-C', ROOT, 'show', f'{tag}:{path}'], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def git_commit(tag):
    r = subprocess.run(['git', '-C', ROOT, 'rev-list', '-n', '1', tag], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def load_json(path, default):
    return json.load(open(path, encoding='utf-8')) if os.path.exists(path) else default


def owner_of(rid):
    for p, k in NAMESPACES:
        if rid.startswith(p):
            return k
    return None


def tokpat(tok):
    return re.compile(r'(?<![A-Za-z0-9_.-])' + re.escape(tok) + r'(?![A-Za-z0-9_-])')


class Report:
    def __init__(self):
        self.rows = []

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
    """Line kinds: source, l0, index, l5, node (domain L1-L4 and domain headers), other, heading."""

    def __init__(self, text):
        self.text = text
        self.lines = text.split('\n')
        self.kind = []
        sec = None
        for l in self.lines:
            if l.startswith('## ') or l.startswith('### '):
                if l.startswith('## SOURCES'):
                    sec = 'source'
                elif l.startswith('## L0') or l.startswith('### L0'):
                    sec = 'l0'
                elif l.startswith('## CROSS'):
                    sec = 'index'
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
                    rows[cells[0]] = {'edition': cells[2], 'tag': cells[3].strip('`')}
        return rows

    @staticmethod
    def segments(line):
        return [s.strip() for s in line.split(' | ')]

    @staticmethod
    def node_id(line):
        s = line.strip()
        if not s:
            return ''
        return s.split(' ')[0].lstrip('*').rstrip(':,;')

    def node_lines(self, item):
        return [i for i, (l, k) in enumerate(zip(self.lines, self.kind)) if k == 'node' and self.node_id(l) == item]

    def occurrences(self, token):
        pat = tokpat(token)
        return [(i + 1, k) for i, (l, k) in enumerate(zip(self.lines, self.kind)) if pat.search(l)]


# ---------------------------------------------------------------- owner identifiers
def tag_declarations(text):
    out = {}
    for l in text.split('\n'):
        for m in re.finditer(r'\[RID:([^\]]*)\]', l):
            for r in RID_RE.findall(m.group(1)):
                out.setdefault(r, l)
    return out


def classify_owner_ids(owner, text, idmap):
    """Return (active set, non-resolved dict rid->type) for one owner text."""
    active, nonres = set(), {}
    tags = tag_declarations(text)
    lines = text.split('\n')
    if owner in TAG_CONVENTION:
        active = set(tags)
    else:
        active = set(tags)
        for l in lines:
            s = l.strip()
            if DENIAL_RE.search(s):
                continue
            if s.startswith('#'):
                active.update(RID_RE.findall(s))
            elif s.startswith('|'):
                cells = s.strip('|').split('|')
                if cells:
                    active.update(RID_RE.findall(cells[0]))
            if re.search(r'\bRID\b\s*[:=]', s):
                active.update(RID_RE.findall(s))
            m = re.match(r'^(?:[-*]\s*)?(?:\*\*)?`?((?:%s)-%s(?:-[A-Z0-9]+)+)`?\s' % (
                '|'.join(p.rstrip('-') for p, _ in NAMESPACES), TYPEWORDS), s)
            if m:
                active.add(m.group(1))
    for l in lines:
        if DENIAL_RE.search(l):
            for r in RID_RE.findall(l):
                if r not in tags:
                    nonres[r] = 'owner-denied or historical (owner text)'
    retired_real = {}
    for typ, d in (idmap.get(owner) or {}).items():
        for r, why in d.items():
            if typ == 'closed_lifecycle_untagged':
                retired_real[r] = why; nonres.pop(r, None); active.discard(r)
            else:
                nonres[r] = f'{typ}: {why}'
                active.discard(r)
    return active, nonres, retired_real


# ---------------------------------------------------------------- checks
def check_sources(rep, atlas, manifest):
    ch = 'sources'
    table = atlas.source_table()
    man = {s['key']: s for s in manifest['sources']}
    for key, row in table.items():
        m = man.get(key)
        if not m:
            rep.add(ch, 'FAIL', key, 'source-table row has no manifest entry'); continue
        ok = row['edition'].split()[0] == m['edition'].split()[0] and row['tag'] == m['tag']
        rep.add(ch, 'PASS' if ok else 'FAIL', key, f"table {row['edition']} `{row['tag']}` vs manifest {m['edition']} `{m['tag']}`")
    for key in man:
        if key not in table:
            rep.add(ch, 'FAIL', key, 'manifest entry missing from atlas source table')
    base = open(BASELINE, encoding='utf-8').read() if os.path.exists(BASELINE) else ''
    for key, m in man.items():
        data = git_show(m['tag'], m['path'])
        if data is None:
            rep.add(ch, 'FAIL', key, f"tag {m['tag']} or path {m['path']} not resolvable"); continue
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


def _home(rep, ch, atlas, item, covmap, src_name):
    nodes = atlas.node_lines(item)
    if nodes:
        rep.add(ch, 'PASS', item, f'home: node line {nodes[0] + 1}'); return
    h = (covmap.get('homes') or {}).get(item)
    if h:
        idx = [i for i, (l, k) in enumerate(zip(atlas.lines, atlas.kind)) if k == 'node' and l.startswith(h['home'])]
        if len(idx) == 1 and tokpat(item).search(atlas.lines[idx[0]]):
            rep.add(ch, 'PASS', item, f"reviewed shared home line {idx[0] + 1} ({h['kind']})")
        else:
            rep.add(ch, 'FAIL', item, f"mapped home '{h['home'][:40]}' not found uniquely or does not name the item")
        return
    ex = (covmap.get('exclusions') or {}).get(item)
    if ex:
        rep.add(ch, 'PASS', item, 'justified exclusion: ' + ex); return
    occ = atlas.occurrences(item)
    where = sorted(set(k for _, k in occ))
    rep.add(ch, 'FAIL', item, (f'{src_name} item has no home; mentioned only in ' + ', '.join(where) + ' (not a home)') if occ else f'{src_name} item not in atlas')


def check_coverage(rep, atlas, src, covmap):
    ch = 'coverage'
    covmap = covmap or {}
    for rid in sorted(tag_declarations(src.get('DYAD') or '')):
        if '-ART-' not in rid:
            _home(rep, ch, atlas, rid, covmap, 'DYAD')
    rer = src.get('RER') or ''
    keys = set(re.findall(r'^### (RER-[A-Z0-9-]+) ', rer, re.M)) | set(re.findall(r'^\| `(RER-[A-Z0-9]+)` \|', rer, re.M))
    for k in sorted(keys):
        _home(rep, ch, atlas, k, covmap, 'RER')
    meth = src.get('METH') or ''
    if meth:
        heads = set()
        for l in meth.split('\n'):
            m = re.match(r'^#{2,4}\s+(?:§\s*)?(\d+(?:\.\d+)*)[.\s]', l)
            if m:
                heads.add(m.group(1))
        cited = set()
        for l in atlas.lines:
            for m in re.finditer(r'(?:METH|DSN_METHODOLOGY)(?: v1\.4)? (§§?[\d.,\s§]+)', l):
                cited.update(n.rstrip('.') for n in re.findall(r'\d+(?:\.\d+)*', m.group(1)))
        for n in sorted(cited, key=lambda x: [int(p) for p in x.split('.')]):
            ok = n in heads or any(h.startswith(n + '.') for h in heads)
            rep.add(ch, 'PASS' if ok else 'FAIL', 'METH §' + n, 'section exists in v1.4' if ok else 'no such section in v1.4')


def check_qualifiers(rep, atlas, src, idmap=None):
    ch = 'qualifiers'
    idmap = load_json(DEF_IDMAP, {}) if idmap is None else idmap
    aliases = idmap.get('prerequisite_aliases', {})
    for rid, line in sorted(tag_declarations(src.get('DYAD') or '').items()):
        m = re.search(r'\[assuming:([^\]]*)\]', line)
        if '-ART-' in rid or not m:
            continue
        prereqs = RID_RE.findall(m.group(1))
        nodes = [atlas.lines[i] for i in atlas.node_lines(rid)]
        if not nodes:
            rep.add(ch, 'UNVERIFIED', rid, 'conditional owner result has no atlas node line to check'); continue
        bad = []
        for n in nodes:
            if UNCOND_RE.search(n):
                bad.append('node says unconditional')
            if not COND_RE.search(n):
                bad.append('no conditional marker')
            for p in prereqs:
                if not any(tokpat(a).search(n) for a in [p] + aliases.get(p, [])):
                    bad.append(f'prerequisite {p} not named')
        rep.add(ch, 'FAIL' if bad else 'PASS', rid, '; '.join(sorted(set(bad))) if bad else f'conditional marker and prerequisite(s) {", ".join(prereqs) or "-"} kept')


def check_links(rep, atlas, src, idmap=None):
    ch = 'links'
    idmap = load_json(DEF_IDMAP, {}) if idmap is None else idmap
    cls = {k: classify_owner_ids(k, v, idmap) for k, v in src.items() if v}
    seen = defaultdict(list)
    for i, (l, k) in enumerate(zip(atlas.lines, atlas.kind)):
        if k in ('source', 'heading'):
            continue
        for rid in RID_RE.findall(l):
            seen[rid].append(i)
    for rid in sorted(seen):
        own = owner_of(rid)
        if own is None or own not in cls:
            rep.add(ch, 'UNVERIFIED', rid, f'owner {own} not in snapshot'); continue
        active, nonres, retired_real = cls[own]
        if rid in active:
            rep.add(ch, 'PASS', rid, f'active declaration in {own}'); continue
        if rid in retired_real:
            rep.add(ch, 'PASS', rid, f'real {own} identifier, closed lifecycle item (untagged): {retired_real[rid]}'); continue
        outside = [i for i in seen[rid] if atlas.kind[i] != 'l5']
        if rid in nonres:
            unmarked = [i for i in outside if not ATLAS_UNRESOLVED_MARK.search(atlas.lines[i])]
            if unmarked:
                rep.add(ch, 'FAIL', rid, f'{own} {nonres[rid]}; used without an unresolved marker at line {unmarked[0] + 1}')
            else:
                rep.add(ch, 'DOCUMENTED-UNRESOLVED', rid, f'{own} {nonres[rid]}; cited only in L5 or marked unresolved')
            continue
        present = tokpat(rid).search(src[own]) is not None
        if present:
            rep.add(ch, 'UNVERIFIED', rid, f'present in {own} but not in a recognized declaration form')
        elif not outside:
            rep.add(ch, 'DOCUMENTED-UNRESOLVED', rid, f'absent from {own}; cited only in L5')
        else:
            rep.add(ch, 'FAIL', rid, f'absent from owner {own} at its tag; cited outside L5 (line {outside[0] + 1})')


def check_artifacts(rep, atlas, src):
    ch = 'artifacts'
    allsrc = '\n'.join(v for v in src.values() if v)
    for i, (l, k) in enumerate(zip(atlas.lines, atlas.kind)):
        if k != 'node':
            continue
        first = Atlas.node_id(l)
        own = owner_of(first)
        if own is None:
            m = re.match(r'\*?([A-Z0-9]+)[:-]', l)
            key = m.group(1) if m else None
            own = {'ER2B': 'ER2B', 'RER': 'RER', 'FMS': 'FMS', 'PL': 'PREL'}.get(key, key if key in src else None)
        for seg in Atlas.segments(l):
            if not seg.lower().startswith(('cert', 'certs', 'evidence')):
                continue
            for art in re.findall(r'(?:DYAD|TRIAD|GEN|RECOG|NUMGEN|UVM|TDRG|DZT|AZ)-ART-[A-Z0-9-]+', seg):
                o = owner_of(art)
                okd = src.get(o) and re.search(re.escape(art) + r'(?![A-Z0-9-])', src[o])
                rep.add(ch, 'PASS' if okd else 'FAIL', art, f'line {i + 1}: ' + ('in owner file' if okd else f'not in owner {o}'))
            for sc in SCRIPT_RE.findall(seg):
                if own and src.get(own) and sc in src[own]:
                    rep.add(ch, 'PASS', sc, f'line {i + 1}: named in {own} (naming only)')
                elif sc in allsrc:
                    rep.add(ch, 'UNVERIFIED', sc, f'line {i + 1}: named in a source other than the line owner ({own})')
                else:
                    rep.add(ch, 'FAIL', sc, f'line {i + 1}: script named in no source file')


def check_keys(rep, atlas, retired):
    ch = 'keys'
    for key in retired:
        pat = tokpat(key)
        hits = [i for i, l in enumerate(atlas.lines) if pat.search(l)]
        if hits:
            rep.add(ch, 'FAIL', key, f'retired L5 key referenced at line {hits[0] + 1}')
        else:
            rep.add(ch, 'PASS', key, 'retired key not referenced')


def check_process(rep, atlas):
    for i, (l, k) in enumerate(zip(atlas.lines, atlas.kind)):
        if k in ('source', 'heading'):
            continue
        for w in PROCESS_FAIL:
            for m in re.finditer(w, l):
                rep.add('process', 'FAIL', f'line {i + 1}', f'"{m.group(0)}": …{l[max(0, m.start() - 40):m.end() + 40]}…')
        for w in WORDING:
            for m in re.finditer(w, l, re.I):
                rep.add('wording', 'WARN', f'line {i + 1}', f'"{m.group(0)}": …{l[max(0, m.start() - 40):m.end() + 40]}…')


CHECKS = ['sources', 'coverage', 'qualifiers', 'links', 'artifacts', 'keys', 'process', 'wording']


def run(atlas_text, manifest, src, covmap, idmap, retired, with_sources=True):
    rep = Report()
    atlas = Atlas(atlas_text)
    if with_sources:
        check_sources(rep, atlas, manifest)
    check_coverage(rep, atlas, src, covmap)
    check_qualifiers(rep, atlas, src, idmap)
    check_links(rep, atlas, src, idmap)
    check_artifacts(rep, atlas, src)
    check_keys(rep, atlas, retired)
    check_process(rep, atlas)
    return rep


def write_report(rep, path, meta):
    out = ['# Atlas check report', '', f"atlas: `{meta['atlas']}` sha256 `{meta['atlas_sha']}`; manifest `{meta['manifest']}`", '',
           '| check | PASS | FAIL | UNVERIFIED | other |', '|---|---|---|---|---|']
    for ch in CHECKS:
        c = rep.count(ch)
        other = {k: v for k, v in c.items() if k not in ('PASS', 'FAIL', 'UNVERIFIED')}
        out.append(f"| {ch} | {c.get('PASS', 0)} | {c.get('FAIL', 0)} | {c.get('UNVERIFIED', 0)} | {', '.join(f'{k} {v}' for k, v in other.items()) or '—'} |")
    out += ['', 'Unparsed or unchecked items are not PASS. Scope notes: the qualifier check covers DYAD declarations carrying `[assuming: …]` only; '
            'script checks establish naming in the owner file, not file availability or execution; content fidelity is a matter for the change-focused review. '
            'Separate limitation (not a checker row): byte equality of 13 sources with the atlas v0.1 extraction input is UNVERIFIED (manifest `v0_1_input_equality`).', '']
    for st in ['FAIL', 'UNVERIFIED', 'DOCUMENTED-UNRESOLVED', 'WARN']:
        rows = [r for r in rep.rows if r[1] == st]
        if rows:
            out += [f'## {st} ({len(rows)})', ''] + [f'- {r[0]} · {r[2]} — {r[3]}' for r in rows] + ['']
    open(path, 'w', encoding='utf-8').write('\n'.join(out))


# ---------------------------------------------------------------- negative controls
def self_test(manifest, src, covmap, idmap, retired, base_text):
    res = []
    base = run(base_text, manifest, src, covmap, idmap, retired, with_sources=False)
    base_fail = {(r[0], r[2]) for r in base.fails()}
    atlas = Atlas(base_text)
    L = base_text.split('\n')

    def new_fails(text):
        r = run(text, manifest, src, covmap, idmap, retired, with_sources=False)
        return [x for x in r.fails() if (x[0], x[2]) not in base_fail]

    dy = tag_declarations(src['DYAD'])
    # NC1 omitted claim, RID kept in an L5 line
    target = next((r for r in sorted(dy) if '-ART-' not in r and len(atlas.node_lines(r)) == 1), None)
    M = L[:]; ln = atlas.node_lines(target)[0]; del M[ln]
    l5i = next(i for i, k in enumerate(Atlas('\n'.join(M)).kind) if k == 'l5' and M[i].strip())
    M[l5i] += f' (see {target})'
    res.append(('NC1 omitted claim, RID kept in L5', target, any(x[0] == 'coverage' and x[2] == target for x in new_fails('\n'.join(M)))))
    # NC1b omitted claim, RID kept as a dependency edge in another node
    M = L[:]; del M[ln]
    other = next(i for i, k in enumerate(Atlas('\n'.join(M)).kind) if k == 'node' and M[i].startswith('DYAD-'))
    M[other] += f' | <{target}'
    res.append(('NC1b omitted claim, RID kept as dependency edge', target, any(x[0] == 'coverage' and x[2] == target for x in new_fails('\n'.join(M)))))
    ni = next(i for i, k in enumerate(atlas.kind) if k == 'node' and L[i].startswith('DYAD-THM-'))
    # NC2 wrong owner
    M = L[:]; M[ni] += ' | <GEN-THM-SMOOTH-EMBEDDING'
    res.append(('NC2 wrong owner', 'GEN-THM-SMOOTH-EMBEDDING', any(x[0] == 'links' and x[2] == 'GEN-THM-SMOOTH-EMBEDDING' for x in new_fails('\n'.join(M)))))
    # NC3 lost qualifier (strip markers) and NC3b 'unconditional'
    cond = [r for r, l in dy.items() if '[assuming' in l and '-ART-' not in r and atlas.node_lines(r)]
    rid = sorted(cond)[0]
    M = L[:]
    for i in atlas.node_lines(rid):
        M[i] = COND_RE.sub('', M[i])
    res.append(('NC3 lost qualifier', rid, any(x[0] == 'qualifiers' and x[2] == rid for x in new_fails('\n'.join(M)))))
    M = L[:]
    for i in atlas.node_lines(rid):
        M[i] = Atlas.node_id(M[i]) + ' THM | unconditional bound'
    res.append(('NC3b "unconditional" does not satisfy "conditional"', rid, any(x[0] == 'qualifiers' and x[2] == rid for x in new_fails('\n'.join(M)))))
    # NC4 invalid artifact target; NC5 script named nowhere
    M = L[:]; M[ni] += ' | cert DYAD-ART-NO-SUCH-CERTIFICATE'
    res.append(('NC4 invalid artifact target', 'DYAD-ART-NO-SUCH-CERTIFICATE', any(x[0] == 'artifacts' and x[2] == 'DYAD-ART-NO-SUCH-CERTIFICATE' for x in new_fails('\n'.join(M)))))
    M = L[:]; M[ni] += ' | cert no_such_owner_script_zz9.py'
    res.append(('NC5 missing artifact link', 'no_such_owner_script_zz9.py', any(x[0] == 'artifacts' and x[2] == 'no_such_owner_script_zz9.py' for x in new_fails('\n'.join(M)))))
    # NC6 fabricated RID: only in L5 -> documented unresolved; in a node -> FAIL
    fake = 'DYAD-THM-FAKE-ONLY-ZZ9'
    M = L[:]; l5i = next(i for i, k in enumerate(atlas.kind) if k == 'l5' and L[i].strip()); M[l5i] += f' {fake}'
    r = run('\n'.join(M), manifest, src, covmap, idmap, retired, with_sources=False)
    res.append(('NC6a fabricated RID only in L5 is not resolved', fake, [x[1] for x in r.rows if x[0] == 'links' and x[2] == fake] == ['DOCUMENTED-UNRESOLVED']))
    M[ni] += f' | <{fake}'
    res.append(('NC6b fabricated RID in a node fails', fake, any(x[0] == 'links' and x[2] == fake for x in new_fails('\n'.join(M)))))
    # NC7 source table mismatch
    M = [l.replace('| v6.4.22 | `dyad-v6.4.22`', '| v6.4.21 | `dyad-v6.4.21`') for l in L]
    r = run('\n'.join(M), manifest, src, covmap, idmap, retired, with_sources=True)
    res.append(('NC7 source table mismatch', 'DYAD', any(x[0] == 'sources' and x[2] == 'DYAD' for x in r.fails())))
    # NC8 retired key referenced; NC9 advisory key in a node
    if retired:
        k = retired[0]; M = L[:]; M[ni] += f' ! {k}'
        res.append(('NC8 retired L5 key referenced', k, any(x[0] == 'keys' and x[2] == k for x in new_fails('\n'.join(M)))))
    M = L[:]; M[ni] += ' | Tier-C target FC-DYAD-99'
    res.append(('NC9 advisory key in a node', 'FC-DYAD-99', any(x[0] == 'process' for x in new_fails('\n'.join(M)))))
    # Receiving-review fixtures (records/atlas/ATLAS_V0_2_RECEIVING_REVIEW.md §3.4), same inputs
    phantom = 'DYAD-CAND-PHISTAR-ENTRY-PHASE'
    srow = f'| `{phantom}` | never a Dyadic identifier (former NUMGEN pin; removed by NUMGEN v1.20.8, notice N3) | §7 notices |'
    rp = Report(); check_links(rp, Atlas(f'### D2.L5 DIAGNOSTICS\nNUMGEN.N-D D-RID | {phantom}: not an owner identifier.'), {'DYAD': srow}, {})
    res.append(('RV-N1 owner-denied id, diagnostic use -> DOCUMENTED-UNRESOLVED', phantom, [x[1] for x in rp.rows] == ['DOCUMENTED-UNRESOLVED']))
    rp = Report(); check_links(rp, Atlas(f'### D2.L2 CLAIMS\n{phantom} CAND | fabricated fixture; not in submitted Atlas'), {'DYAD': srow}, {})
    res.append(('RV-N1b owner-denied id as a node -> not PASS', phantom, bool(rp.rows) and all(x[1] != 'PASS' for x in rp.rows)))
    rr = 'DYAD-ALG-RAW-ANGULAR-MEAN'
    s3 = {'DYAD': f'`[ALG]` [RID: {rr}] Fixed-radius raw-frame mean has coefficient 47/54.', 'RER': '', 'METH': ''}
    rp = Report(); check_coverage(rp, Atlas(f'### D2.L2 CLAIMS\n{rr} ALG | fixed-radius raw-frame mean coefficient 47/54 | @DYAD§6.5'), s3, {})
    res.append(('RV-P1 explicit claim home -> PASS', rr, [x[1] for x in rp.rows] == ['PASS']))
    rp = Report(); check_coverage(rp, Atlas(f'### D2.L2 CLAIMS\n*FIXTURE:consumer OPEN | unidentified application | <{rr}'), s3, {})
    res.append(('RV-N2 bare dependency is not coverage', rr, [x[1] for x in rp.rows] == ['FAIL']))
    rp = Report(); check_coverage(rp, Atlas(f'## L0 KEY\nIdentifiers considered: {rr}'), s3, {})
    res.append(('RV-N2b L0 mention is not coverage', rr, [x[1] for x in rp.rows] == ['FAIL']))
    r2 = 'DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER'
    s4 = {'DYAD': f'`[THM]` [assuming: RECOG-THM-R9-MEMORY] [RID: {r2}] Remainder bound.'}
    rp = Report(); check_qualifiers(rp, Atlas(f'### D2.L2 CLAIMS\n{r2} THM | unconditional bound'), s4, {})
    res.append(('RV-N3 "unconditional" fails the conditional gate', r2, [x[1] for x in rp.rows] == ['FAIL']))
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--atlas', default=DEF_ATLAS)
    ap.add_argument('--manifest', default=DEF_MANIFEST)
    ap.add_argument('--coverage-map', default=DEF_COVMAP)
    ap.add_argument('--id-map', default=DEF_IDMAP)
    ap.add_argument('--retired', default=DEF_RETIRED)
    ap.add_argument('--report')
    ap.add_argument('--json')
    ap.add_argument('--self-test', action='store_true')
    a = ap.parse_args()
    try:
        manifest = json.load(open(a.manifest, encoding='utf-8'))
        text = open(a.atlas, encoding='utf-8').read()
    except OSError as e:
        print(e, file=sys.stderr); return 2
    covmap = load_json(a.coverage_map, {})
    idmap = load_json(a.id_map, {})
    retired = load_json(a.retired, {}).get('retired', [])
    src = load_sources(manifest)
    if a.self_test:
        res = self_test(manifest, src, covmap, idmap, retired, text)
        for name, item, ok in res:
            print(f"{'PASS' if ok else 'FAIL'}  {name}  [{item}]")
        ok = all(r[2] for r in res)
        print(f'negative/positive controls: {sum(r[2] for r in res)}/{len(res)} as expected' + ('' if ok else ' — NOT all'))
        return 0 if ok else 1
    rep = run(text, manifest, src, covmap, idmap, retired)
    meta = {'atlas': os.path.relpath(a.atlas, ROOT), 'atlas_sha': hashlib.sha256(text.encode('utf-8')).hexdigest(),
            'manifest': os.path.relpath(a.manifest, ROOT)}
    for ch in CHECKS:
        print(f'{ch:11s}', rep.count(ch))
    if a.report:
        write_report(rep, a.report, meta)
    if a.json:
        json.dump({'meta': meta, 'rows': rep.rows}, open(a.json, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return 1 if rep.fails() else 0


if __name__ == '__main__':
    sys.exit(main())
