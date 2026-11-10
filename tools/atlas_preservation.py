#!/usr/bin/env python3
"""atlas_preservation.py — preservation manifest and comparator for an Atlas compaction (Atlas-specific; not a DSN tool).

extract  ATLAS OUT.json            every byte of the file is accounted for: one region per line (headings, records,
                                   tables, raw lines), each with its byte span in the file and the SHA-256 of exactly
                                   those bytes; record lines also carry typed fields with byte spans and hashes.
compare  BASE CAND MAP.json [--report R.json]
                                   mechanical statuses only:
                                     EXACT                    same bytes, same occurrence owner, same heading context
                                     MAPPED_EXACT             same bytes, declared move (context or position changed)
                                     DECLARED_PENDING_REVIEW  declared edit/delete/insert; NOT preserved until reviewed
                                     FAIL                     lost, moved to another owner, or unexplained new text
selftest                            negative and positive controls on synthetic fixtures.

What it does not claim. Equal RID/pin/marker/number lists do not prove that changed text is equivalent, so the
comparator never upgrades a changed field: any byte difference is DECLARED_PENDING_REVIEW or FAIL. A grade or qualifier
change, a changed record identifier and a changed diagnostic class are never a compaction: they FAIL here and need a
separately reviewed stage-1 delta. `explicit_condition_marker: false` means no recognised marker was found, not that
the claim is unconditional. Untyped segments are compared only inside their own record occurrence (owner binding).
Reads and hashes bytes; spans are byte offsets; CRLF is preserved. Writes only the files named on the command line.
"""
from __future__ import annotations
import hashlib, json, re, sys
from collections import Counter

GRADES = 'THM ALG DEF CAND HYP RES NUM HEUR INTERP OPEN FAIL RET CONV'.split()
RID = re.compile(r'\b(?:[A-Z][A-Z0-9]*-)+(?:THM|ALG|DEF|CAND|HYP|RES|RESULT|NUM|HEUR|INTERP|OPEN|FAIL|RET|CONV|ART|EXPORT|COR|LEM)-[A-Z0-9][A-Z0-9-]*\b')
PIN = re.compile(r'\b(?:dyad|triad|gen|tdrg|recog|numgen|ofn|programme|methodology|uvm|rrf|legacy|prelegacy|dzt|az|rer|er2b|fms|atlas)-v\d+(?:\.\d+)*\b|\b(?:DYAD|TRIAD|GEN|TDRG|TDR-G|RECOG|NUMGEN|OFN|PROG|UVM|RRF|LEGACY|PREL|DZT|AZ|RER) v\d+(?:\.\d+)*\b')
MARK = re.compile(r'\[custody-[A-Z]\]|\[indep-[A-Z]+\]|\bEV-[A-Z]+(?:-[A-Z]+)*\b|\[assuming:|\bFORMAL_ONLY\b|\bNONCANONICAL\b|\bSESSION\b|\bnot a recovery\b|\bnot rerun\b|\bsource-reported\b')
HEAD = re.compile(r'^(?P<id>\*[A-Z0-9-]+:\S+|(?:[A-Z][A-Z0-9]*-)+[A-Z0-9][A-Za-z0-9-]*)\s+(?P<grade>(?:' + '|'.join(GRADES) + r')(?:\[[A-Z]+\])?(?:·(?:c|s|dx))*(?:\s+nc)?)(?=\s|$)')
L5 = re.compile(r'^(?P<id>(?:[A-Z0-9]+\.[A-Z]+-?[A-Z]?\d+[a-z]?|NUMGEN\.N-[A-Z*]+\d*|RECOG\.R-[A-Z]+\d+[a-z]?|F\d+|H\d+))(?: \+ [A-Z0-9.]+)?\s+(?P<cls>~?\s*D-[A-Z]+(?:/D-[A-Z]+)*)')
FIELD = [('scope', r'sc:'), ('premise', r'if:|\[assuming:|import:'), ('dep', r'<'), ('consumer', r'>'), ('negative', r'¬'), ('cert', r'cert\b|art\b'),
         ('locator', r'@'), ('alias', r'≡'), ('derived', r'~'), ('tension', r'!'), ('collision', r'⊥'), ('evidence', r'atlas-checked|EV-|\[indep-')]
FIELD = [(n, re.compile('^(?:' + p + ')')) for n, p in FIELD]
COND = re.compile(r'^if:|\[assuming:|^import:')
ID_KIND = [('artifact', re.compile(r'-ART-')), ('pseudo', re.compile(r'^\*')), ('scientific', re.compile(r'.'))]

def sha(b): return hashlib.sha256(b).hexdigest()

def extract(raw: bytes):
    """Regions cover the file exactly: region i spans [a,b) without its newline; newlines are implied between regions."""
    regions, pos, ctx, occ, stack, anchor = [], 0, [], Counter(), [], None
    lines = raw.split(b'\n')
    for n, lb in enumerate(lines, 1):
        a, b = pos, pos + len(lb); pos = b + 1
        text = lb.decode('utf-8'); core = text.rstrip('\r')
        r = dict(line=n, span=[a, b], sha256=sha(lb))
        hm = re.match(r'^(#+) ', core)
        if hm:
            lvl = len(hm.group(1)); stack = [x for x in stack if x[0] < lvl]   # explicit levels: siblings and skipped levels do not nest
            r.update(kind='heading', level=lvl, context=[h for _, h in stack]); stack.append((lvl, sha(lb)[:16])); ctx = [h for _, h in stack]; anchor = None
        elif not core.strip(): r.update(kind='blank', context=list(ctx))
        else:
            r['context'] = list(ctx); m = HEAD.match(core); d = L5.match(core)
            if m and ' | ' in core:
                key = m.group('id'); occ[key] += 1
                r.update(kind='node', id=key, occurrence=occ[key], id_kind=next(k for k, p in ID_KIND if p.search(key)), grade=m.group('grade'), fields=[])
                off = len(core[:m.end()].encode('utf-8')); body = lb[off:]; cur = 0
                for seg in body.split(b' | '):
                    s0 = cur + (len(seg) - len(seg.lstrip())); s1 = cur + len(seg.rstrip()); cur += len(seg) + 3
                    fb = body[s0:s1]
                    if not fb: continue
                    ft = fb.decode('utf-8'); cls = next((nm for nm, p in FIELD if p.match(ft)), None)
                    if cls is None: cls = 'statement' if not any(f['cls'] == 'statement' for f in r['fields']) else 'UNVERIFIED'
                    f = dict(cls=cls, span=[a + off + s0, a + off + s1], sha256=sha(fb), rids=RID.findall(ft), pins=PIN.findall(ft), markers=MARK.findall(ft))
                    assert sha(raw[f['span'][0]:f['span'][1]]) == f['sha256'], ('span/hash binding', n)
                    r['fields'].append(f)
                r['explicit_condition_marker'] = '·c' in r['grade'] or any(COND.match(raw[f['span'][0]:f['span'][1]].decode('utf-8')) for f in r['fields'])
                anchor = f"{key}#{occ[key]}"
            elif d:
                key = d.group('id'); occ[key] += 1
                r.update(kind='diagnostic', id=key, occurrence=occ[key], id_kind='headline' if key.startswith('H') and key[1:].isdigit() else 'l5-key', cls=d.group('cls').strip(),
                         rids=RID.findall(core), pins=PIN.findall(core), markers=MARK.findall(core)); anchor = f"{key}#{occ[key]}"
            else: r.update(kind='raw', rids=RID.findall(core), anchor=anchor)   # a raw line is bound to the record it follows inside its heading
        assert sha(raw[a:b]) == r['sha256']
        regions.append(r)
    assert pos - 1 == len(raw), 'coverage'
    kinds = Counter(r['kind'] for r in regions)
    nodes = [r for r in regions if r['kind'] == 'node']
    multi = Counter(r['id'] for r in nodes)
    return dict(schema='atlas-preservation-manifest/1', source_sha256=sha(raw), source_bytes=len(raw), span_unit='byte offsets into the source file',
                summary=dict(regions=dict(kinds), node_fields=dict(Counter(f['cls'] for r in nodes for f in r['fields'])),
                             multi_occurrence_ids={k: dict(count=v, id_kind=next(r['id_kind'] for r in nodes if r['id'] == k)) for k, v in sorted(multi.items()) if v > 1},
                             nodes_with_untyped_field=sum(any(f['cls'] == 'UNVERIFIED' for f in r['fields']) for r in nodes)),
                regions=regions)

def okey(r): return f"{r['id']}#{r['occurrence']}" if r['kind'] in ('node', 'diagnostic') else f"L{r['line']}"

def compare(base: bytes, cand: bytes, mp: dict):
    B, C = extract(base), extract(cand); rows = []
    def add(status, what, detail=''): rows.append(dict(status=status, item=what, detail=detail))
    if mp.get('base_sha256') not in (None, B['source_sha256']): add('FAIL', 'map base identity')
    if mp.get('candidate_sha256') not in (None, C['source_sha256']): add('FAIL', 'map candidate identity')
    bl = [r for r in B['regions'] if r['kind'] != 'blank']; cl = [r for r in C['regions'] if r['kind'] != 'blank']
    decl = {d['base']: d for d in mp.get('records', [])}; ins = {d['cand']: d for d in mp.get('inserts', [])}
    cby = {okey(r): r for r in cl}; used = set()
    # pass 1: exact bytes, same owner occurrence (records) and same heading context
    # invariants of surviving identifiers, checked before any mapping: no route (edit or delete+insert) may change a grade or class
    def grades(regs, kind, key): return {i: Counter(r[key] for r in regs if r['kind'] == kind and r['id'] == i) for i in {r['id'] for r in regs if r['kind'] == kind}}
    for kind, key, what in (('node', 'grade', 'grade/qualifier'), ('diagnostic', 'cls', 'diagnostic class')):
        gb, gc = grades(bl, kind, key), grades(cl, kind, key)
        for i in sorted(set(gb) & set(gc)):
            new = gc[i] - gb[i]
            if new: add('FAIL', i, f"{what} {dict(gb[i])} -> {dict(gc[i])}: not a compaction; needs a reviewed stage-1 delta")
    bind = lambda r: okey(r) if r['kind'] in ('node', 'diagnostic') else (('raw', r.get('anchor')) if r['kind'] == 'raw' else None)
    pool = {}; cidx = {id(r): i for i, r in enumerate(cl)}
    for r in cl: pool.setdefault((r['sha256'], tuple(r['context']), bind(r)), []).append(r)
    pending, last = [], -1
    for r in bl:
        k = (r['sha256'], tuple(r['context']), bind(r))
        if pool.get(k) and okey(r) not in decl:
            t = pool[k].pop(0); used.add(id(t))
            if cidx[id(t)] < last: add('FAIL', okey(r), 'unchanged text, but its order relative to other unchanged regions changed without declaration')
            else: last = cidx[id(t)]; add("EXACT", okey(r))
        else: pending.append(r)
    context_reviews = []
    for r in pending:
        k = okey(r); d = decl.get(k)
        if d is None: add('FAIL', k, 'base region neither found unchanged in place nor declared'); continue
        if d.get('cand') is None: add('DECLARED_PENDING_REVIEW', k, 'declared deletion: ' + d.get('reason', '')); continue
        t = cby.get(d['cand'])
        if t is None or id(t) in used: add('FAIL', k, f"declared target {d['cand']} missing or already matched"); continue
        used.add(id(t))
        if t['sha256'] == r['sha256']:
            if r['kind'] in ('node', 'diagnostic') and (t.get('id'), t.get('occurrence')) != (r['id'], r['occurrence']) and t.get('id') != r['id']: add('FAIL', k, 'identical text under another record identifier')
            else:
                ch = t['context'] != r['context'] or (r['kind'] == 'raw' and t.get('anchor') != r.get('anchor'))
                add('MAPPED_EXACT', k, f"moved to {d['cand']}" + ('; CONTEXT CHANGED — inherited scope must be reviewed' if ch else '; same heading context'))
                if ch: context_reviews.append(dict(item=k, base_context=r['context'], candidate_context=t['context'], base_anchor=r.get('anchor'), candidate_anchor=t.get('anchor')))
            continue
        if r['kind'] != t['kind']: add('FAIL', k, f"kind changes {r['kind']} -> {t['kind']}"); continue
        if r['kind'] == 'node':
            if t['id'] != r['id']: add('FAIL', k, f"record identifier changes to {t['id']} (not a compaction)"); continue
            if t['grade'] != r['grade']: add('FAIL', k, f"grade/qualifier {r['grade']} -> {t['grade']} (needs a reviewed stage-1 delta)"); continue
            fd = {x['base_sha256']: x for x in d.get('fields', [])}
            tpool = Counter((f['cls'], f['sha256']) for f in t['fields'])
            tseq = [(f['cls'], f['sha256']) for f in t['fields']]; tfree = [True] * len(tseq); j = 0
            for f in r['fields']:
                key2 = (f['cls'], f['sha256'])
                ahead = next((i for i in range(j, len(tseq)) if tfree[i] and tseq[i] == key2), None)
                anyw = next((i for i in range(len(tseq)) if tfree[i] and tseq[i] == key2), None)
                if ahead is not None: tfree[ahead] = False; j = ahead + 1; tpool[key2] -= 1; add('EXACT', f"{k}:{f['cls']}:{f['sha256'][:8]}")
                elif anyw is not None:   # same bytes, but its position relative to the other fields changed: the field-to-field relation is not preserved
                    tfree[anyw] = False; tpool[key2] -= 1
                    if d.get('reorder'): add('DECLARED_PENDING_REVIEW', f"{k}:{f['cls']}:{f['sha256'][:8]}", 'field order changed (declared reorder): ' + d.get('reason', ''))
                    else: add('FAIL', f"{k}:{f['cls']}:{f['sha256'][:8]}", 'field order changed without a declared reorder')
                elif f['sha256'] in fd:
                    x = fd[f['sha256']]; cs = x.get('cand_sha256')
                    hit = next((kk for kk in tpool if kk[1] == cs and tpool[kk] > 0), None) if cs else None
                    if cs and hit is None: add('FAIL', f"{k}:{f['cls']}", 'declared replacement text not found in the target record')
                    else:
                        if hit: tpool[hit] -= 1
                        add('DECLARED_PENDING_REVIEW', f"{k}:{f['cls']}:{f['sha256'][:8]}", ('edit' if cs else 'deletion') + ': ' + x.get('reason', ''))
                else: add('FAIL', f"{k}:{f['cls']}:{f['sha256'][:8]}", 'field lost or changed without declaration')
            for (cls, h), n in tpool.items():
                for _ in range(n): add('FAIL', f"{d['cand']}:{cls}:{h[:8]}", 'unexplained new field text in the target record')
        elif r['kind'] == 'diagnostic' and (t['id'] != r['id'] or t['cls'] != r['cls']): add('FAIL', k, 'diagnostic key or class changes (not a compaction)')
        else: add('DECLARED_PENDING_REVIEW', k, f"line edited -> {d['cand']}: " + d.get('reason', ''))
    for r in cl:
        if id(r) in used: continue
        k = okey(r)
        if k in ins: add('DECLARED_PENDING_REVIEW', 'cand ' + k, 'declared insertion: ' + ins[k].get('reason', ''))
        else: add('FAIL', 'cand ' + k, 'candidate text with no base source and no declaration')
    counts = Counter(x['status'] for x in rows)
    return dict(schema='atlas-preservation-compare/2', obligations=dict(pending_review=counts['DECLARED_PENDING_REVIEW'], context_reviews=context_reviews), base_sha256=B['source_sha256'], candidate_sha256=C['source_sha256'], base_bytes=len(base), candidate_bytes=len(cand),
                counts=dict(counts), result='FAIL' if counts['FAIL'] else 'MECHANICAL PASS',
                note='MECHANICAL PASS means no loss or unexplained text; DECLARED_PENDING_REVIEW items are not preserved content until reviewed, and a MAPPED_EXACT move that changes the heading context or anchor certifies bytes only: zero pending items is not proof that inherited scope survived (see obligations.context_reviews).', rows=rows)

def selftest():
    H = b'# D1\n## L2\n'
    base = H + 'TEST-ALG-X ALG | α=1 on q<1 | sc: q>0 | if: H holds | <DYAD-ALG-A [dyad-v1.0]; GEN-ALG-B [gen-v2.0] | ¬ global claim | cert TEST-ART-C [custody-A] | only on q>0 | @T§1\nTEST-ALG-Y ALG | second | @T§2\nTEST-ALG-X ALG | second home | @T§3\nT.A1 D-LINK (x): note\n## L3\nraw line\n'.encode()
    def run(c, m=None): return compare(base, c, m or {})
    rep = lambda a, b: base.replace(a.encode(), b.encode())
    cases = [
        ('P identity', base, None, 'MECHANICAL PASS', 0),
        ('N dropped premise', rep(' | if: H holds', ''), None, 'FAIL', None),
        ('N operator changed q<1 -> q>1', rep('q<1', 'q>1'), None, 'FAIL', None),
        ('N pins swapped between two edge targets', rep('<DYAD-ALG-A [dyad-v1.0]; GEN-ALG-B [gen-v2.0]', '<DYAD-ALG-A [gen-v2.0]; GEN-ALG-B [dyad-v1.0]'), None, 'FAIL', None),
        ('N custody marker removed', rep(' [custody-A]', ''), None, 'FAIL', None),
        ('N negative constraint merged away', rep(' | ¬ global claim', ''), None, 'FAIL', None),
        ('N untyped condition moved to another record', rep(' | only on q>0', '').replace(b'| second | @T\xc2\xa72', b'| second | only on q>0 | @T\xc2\xa72'), None, 'FAIL', None),
        ('N second occurrence of an identifier deleted', rep('TEST-ALG-X ALG | second home | @T§3\n', ''), None, 'FAIL', None),
        ('N heading removed', rep('## L3\n', ''), None, 'FAIL', None),
        ('N record moved under another heading without declaration', rep('TEST-ALG-Y ALG | second | @T§2\n', '').replace(b'raw line\n', 'TEST-ALG-Y ALG | second | @T§2\nraw line\n'.encode()), None, 'FAIL', None),
        ('N grade changed', rep('TEST-ALG-Y ALG | second', 'TEST-ALG-Y THM | second'), {'records': [{'base': 'TEST-ALG-Y#1', 'cand': 'TEST-ALG-Y#1', 'reason': 'x'}]}, 'FAIL', None),
        ('N unexplained inserted line', base + b'new claim\n', None, 'FAIL', None),
        ('N diagnostic class changed', rep('T.A1 D-LINK', 'T.A1 D-STALE'), {'records': [{'base': 'T.A1#1', 'cand': 'T.A1#1', 'reason': 'x'}]}, 'FAIL', None),
    ]
    mapx = {'records': [{'base': 'TEST-ALG-X#1', 'cand': 'TEST-ALG-X#1', 'reason': 'record mapped, no field declared'}]}
    cases += [('N record mapped but dropped premise not declared', rep(' | if: H holds', ''), mapx, 'FAIL', None),
              ('N record mapped but swapped pins not declared', rep('<DYAD-ALG-A [dyad-v1.0]; GEN-ALG-B [gen-v2.0]', '<DYAD-ALG-A [gen-v2.0]; GEN-ALG-B [dyad-v1.0]'), mapx, 'FAIL', None),
              ('N record mapped but untyped condition dropped', rep(' | only on q>0', ''), mapx, 'FAIL', None)]
    x = extract(base); stmt = next(f for r in x['regions'] if r.get('id') == 'TEST-ALG-Y' for f in r['fields'] if f['cls'] == 'statement')
    c2 = rep('| second | @T§2', '| 2nd | @T§2'); y = extract(c2); new = next(f for r in y['regions'] if r.get('id') == 'TEST-ALG-Y' for f in r['fields'] if f['cls'] == 'statement')
    cases.append(('P declared field edit is pending review, not preserved', c2, {'records': [{'base': 'TEST-ALG-Y#1', 'cand': 'TEST-ALG-Y#1', 'fields': [{'base_sha256': stmt['sha256'], 'cand_sha256': new['sha256'], 'reason': 'wording'}]}]}, 'MECHANICAL PASS', 1))
    c3 = rep('TEST-ALG-Y ALG | second | @T§2\n', '').replace(b'raw line\n', 'raw line\nTEST-ALG-Y ALG | second | @T§2\n'.encode())   # after the raw line, so the raw line keeps its anchor
    cases.append(('P declared move under another heading is MAPPED_EXACT', c3, {'records': [{'base': 'TEST-ALG-Y#1', 'cand': 'TEST-ALG-Y#1', 'reason': 'regroup'}]}, 'MECHANICAL PASS', 0))
    def adhoc(name, b, c, m, want, pred=None):
        r = compare(b.encode(), c.encode(), m); ok = r['result'] == want and (pred is None or pred(r)); extra.append((ok, f"{name}: {r['result']} {r['counts']}"))
    extra = []
    sc = '# D\n## L2\nTEST-ALG-X ALG | Local family | sc: q>0 | P(q) holds | sc: q<0 | R(q) holds | @T§1\n'; sw = sc.replace('sc: q>0 | P(q) holds | sc: q<0', 'sc: q<0 | P(q) holds | sc: q>0')
    mx = {'records': [{'base': 'TEST-ALG-X#1', 'cand': 'TEST-ALG-X#1', 'reason': 'x'}]}
    adhoc('N scopes exchanged between two statements of one record (field order)', sc, sw, mx, 'FAIL')
    adhoc('P the same exchange with a declared reorder stays pending', sc, sw, {'records': [dict(mx['records'][0], reorder=True)]}, 'MECHANICAL PASS', lambda r: r['counts'].get('DECLARED_PENDING_REVIEW', 0) >= 1)
    adhoc('N raw continuation line moved under another record', '# D\nTEST-ALG-X ALG | P\nThe preceding claim requires q>0.\nTEST-ALG-Y ALG | R\n', '# D\nTEST-ALG-X ALG | P\nTEST-ALG-Y ALG | R\nThe preceding claim requires q>0.\n', {}, 'FAIL')
    adhoc('N two unchanged records swapped without declaration', '# D\nTEST-ALG-X ALG | P\nTEST-ALG-Y ALG | R\n', '# D\nTEST-ALG-Y ALG | R\nTEST-ALG-X ALG | P\n', {}, 'FAIL')
    route = lambda k: {'records': [{'base': k, 'cand': None, 'reason': 'remove'}], 'inserts': [{'cand': k, 'reason': 'insert'}]}
    adhoc('N grade changed through delete + insert', '# D\nTEST-ALG-X ALG | r | @T§1\n', '# D\nTEST-ALG-X THM | r | @T§1\n', route('TEST-ALG-X#1'), 'FAIL')
    adhoc('N diagnostic class changed through delete + insert', '# D\nF1 D-PROOF | e\n', '# D\nF1 D-LINK | e\n', route('F1#1'), 'FAIL')
    adhoc('P duplicate occurrence deleted by declaration is pending, not a grade failure', '# D\nTEST-ALG-X ALG | a\nTEST-ALG-X ALG | b\n', '# D\nTEST-ALG-X ALG | a\n', {'records': [{'base': 'TEST-ALG-X#2', 'cand': None, 'reason': 'one home'}]}, 'MECHANICAL PASS', lambda r: r['counts'].get('DECLARED_PENDING_REVIEW') == 1)
    adhoc('P declared move across headings is MAPPED_EXACT with a visible context obligation', '# D\n## Only for q>0\nTEST-THM-X THM | P | @T§1\n## All real q\n', '# D\n## Only for q>0\n## All real q\nTEST-THM-X THM | P | @T§1\n', mx | {'records': [{'base': 'TEST-THM-X#1', 'cand': 'TEST-THM-X#1', 'reason': 'regroup'}]}, 'MECHANICAL PASS', lambda r: len(r['obligations']['context_reviews']) == 1)
    hx = extract(b'# D\n### A\nTEST-ALG-X ALG | P\n### B\nTEST-ALG-Y ALG | Q\n'); yy = next(r for r in hx['regions'] if r.get('id') == 'TEST-ALG-Y')
    extra.append((yy['context'] == [sha(b'# D')[:16], sha(b'### B')[:16]], 'P skipped-level sibling headings: context is D/B, not D/A/B'))
    crlf = b'# C\r\nTEST-ALG-X ALG | x=1\r\n'; e = extract(crlf)
    ok_all = True; out = []
    for name, cand, mp, want, pend in cases:
        r = run(cand, mp); ok = r['result'] == want and (pend is None or r['counts'].get('DECLARED_PENDING_REVIEW', 0) == pend)
        if name.startswith('P declared move'): ok = ok and r['counts'].get('MAPPED_EXACT', 0) == 1
        ok_all &= ok; out.append(f"{'ok ' if ok else 'BAD'} {name}: {r['result']} {r['counts']}")
    ok = e['source_sha256'] == sha(crlf) and all(sha(crlf[r['span'][0]:r['span'][1]]) == r['sha256'] for r in e['regions']); ok_all &= ok
    out.append(f"{'ok ' if ok else 'BAD'} P CRLF source identity and byte spans")
    f = next(f for r in x['regions'] if r.get('id') == 'TEST-ALG-X' and r['occurrence'] == 1 for f in r['fields'] if f['cls'] == 'statement')
    ok = sha(base[f['span'][0]:f['span'][1]]) == f['sha256'] and base[f['span'][0]:f['span'][1]].decode() == 'α=1 on q<1'; ok_all &= ok
    out.append(f"{'ok ' if ok else 'BAD'} P non-ASCII field: byte span binds the hash")
    t = extract(b'TEST-THM-X THM | If H holds, P follows.\n')['regions'][0]; ok = t['explicit_condition_marker'] is False; ok_all &= ok
    out.append(f"{'ok ' if ok else 'BAD'} P explicit_condition_marker is a marker flag only (false here although the text is conditional)")
    for ok, line in extra: ok_all &= ok; out.append(('ok  ' if ok else 'BAD ') + line)
    print('\n'.join(out)); print('SELFTEST', 'PASS' if ok_all else 'FAIL'); return 0 if ok_all else 1

def main():
    a = sys.argv[1:]
    if a[:1] == ['selftest']: return selftest()
    if a[:1] == ['extract']:
        m = extract(open(a[1], 'rb').read()); open(a[2], 'x', encoding='utf-8').write(json.dumps(m, ensure_ascii=False, indent=1) + '\n')
        print(json.dumps(dict(source_sha256=m['source_sha256'], source_bytes=m['source_bytes'], **m['summary']), ensure_ascii=False, indent=1)); return 0
    if a[:1] == ['compare']:
        r = compare(open(a[1], 'rb').read(), open(a[2], 'rb').read(), json.load(open(a[3], encoding='utf-8')))
        if '--report' in a: open(a[a.index('--report') + 1], 'x', encoding='utf-8').write(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
        print(r['result'], r['counts'], 'context reviews:', len(r['obligations']['context_reviews']))
        for x in r['rows']:
            if x['status'] in ('FAIL', 'DECLARED_PENDING_REVIEW'): print(' ', x['status'], x['item'], '—', x['detail'])
        return 1 if r['result'] == 'FAIL' else 0
    print(__doc__); return 2

if __name__ == '__main__':
    sys.exit(main())
