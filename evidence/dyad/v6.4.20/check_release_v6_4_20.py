#!/usr/bin/env python3
"""check_release_v6_4_20.py -- release gates for RTG_DYADIC_OSCILLATOR_DSN_v6_4_20.md (adopted) against the reviewed DRAFT r2.

R0  identities: r2 = f2030f85...; final = fresh release transform of r2
R1  determinism: two transforms in clean directories are byte-identical (file and log)
R2  confinement: outside the new adoption record the final file has r2's line count; every changed line is quoted verbatim in
    the record; the number of changed lines equals the log; header changes only on the Edition/Status/Supersedes/record
    lines, the status-summary text before its last two sentences is unchanged; in every other changed line the removed
    words lie in a fixed label vocabulary (proposed/adopted/draft/...), so no scientific word is removed
R3  RID census: tagged identifier set equal to r2 (148) and equal to v6.4.19's set plus the 13 new RIDs; the sequence of
    RID tags outside Appendix A is identical to r2
R4  mathematics: the multiset of $...$ spans in the whole file equals r2's (adoption record excluded)
R5  grades: the sequence of grade tags `[ALG]`, `[THM]`, ... outside the adoption record equals r2's
R6  no live label residue: "registered only at adoption", "— proposed, not adopted |", "not adopted, not released",
    "Supersedes (on adoption only)", "canonical until a v6.4.20 adoption decision", "| proposed RID" absent outside Appendix A
R7  header: title; Edition adopted; Status ADOPTED with the PI decision label, the r2 review label and the r2 hash;
    Supersedes v6.4.19 with its hash
R8  exactly one footer (adopted form) and one AI_CONTEXT_CORE_END marker
R9  OPEN state: the OPEN 20 status sentence and every "Status:" line of section 2 are byte-identical to r2
R10 adoption record: placed before the DRAFT r2 record; names the decision, the 13 RIDs, the three evidence levels with the
    combined G14-G15 item NOT COMPLETED, and N16-N20 only after external hash verification
R11 Appendix E: 58 E.1 and 58 E.2 rows; the 11 rows of new identifiers read "— new in v6.4.20"; no "proposed" in E.1/E.2 cells
Exit 0 all pass / 1 any fail / 3 crash.
Usage: python -B check_release_v6_4_20.py --final F --r2 R2 --base V6419 [--norebuild] [--out J]
"""
import sys, os, re, json, hashlib, argparse, subprocess, tempfile, shutil, collections
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
R2_HASH = 'f2030f853b94a7caa1d1d7c4afd8bdf9b6059582d331100bb0033226fd68465e'
V619 = '40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9'
NEW13 = {'DYAD-ALG-KP-FRAME-SCALE', 'DYAD-THM-SMOOTH-EQUIVARIANT-CHART', 'DYAD-ALG-B5-ALLP-NONVANISHING', 'DYAD-ALG-RAW-ANGULAR-MEAN',
         'DYAD-ALG-ONE-BLOCK-BURST', 'DYAD-ALG-P5-RADIAL', 'DYAD-ALG-SIXSTEP-CUBIC-JET', 'DYAD-ALG-Q3-DEG2-CANCEL', 'DYAD-DEF-CRITICAL-CURVE',
         'DYAD-ALG-QC-CRITICAL-AMPLITUDE', 'DYAD-ALG-ISP-MAPS', 'DYAD-ART-ATLAS-P1', 'DYAD-ART-ATLAS-P2'}
LABEL_WORDS = {'.', 'DRAFT', 'a', 'adopted', 'adoption', 'after', 'and', 'canonical', 'decision', 'draft', 'draft.', 'for', 'issued',
               'not', 'only', 'proposed', 'r2', 'this', 'until'}
GRADE_RE = re.compile(r'`\[(?:THM-ALG via IA|ALG|THM|DEF|CAND|ENG|NUM|HYP|OBS|OPEN|COR|FAIL)\]`')


def sha(b): return hashlib.sha256(b).hexdigest()
def tok(s): return re.findall(r'[A-Za-z0-9.\-]+', s)
def census(s):
    out = set()
    for m in re.finditer(r'\[RID:\s*([^\]]+)\]', s):
        for r in m.group(1).split(','): out.add(r.strip())
    return out
def maths(s):  # per line, so that one stray '$' cannot shift the parity of the whole file
    c = collections.Counter()
    for l in s.split('\n'):
        l = l.replace('$$', '$')
        c.update(l.split('$')[1::2] if l.count('$') % 2 == 0 else [l])
    return c


def transform(tmp, r2):
    shutil.copy(os.path.join(HERE, 'release_v6_4_20.py'), tmp)
    out = os.path.join(tmp, 'final.md')
    r = subprocess.run([sys.executable, '-B', 'release_v6_4_20.py', os.path.abspath(r2), out], cwd=tmp, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return open(out, 'rb').read(), open(os.path.join(tmp, 'release_v6_4_20_log.json'), 'rb').read()


def main():
    ap = argparse.ArgumentParser()
    for k in ('final', 'r2', 'base'): ap.add_argument('--' + k, required=True)
    ap.add_argument('--norebuild', action='store_true'); ap.add_argument('--out', default='check_release_v6_4_20.json')
    a = ap.parse_args()
    FB = open(a.final, 'rb').read(); F = FB.decode('utf-8'); R2B = open(a.r2, 'rb').read(); R2 = R2B.decode('utf-8')
    BASE = open(a.base, encoding='utf-8').read()
    G, info = {}, {}
    G['R0'] = sha(R2B) == R2_HASH and sha(open(a.base, 'rb').read()) == V619
    if a.norebuild: G['R1'] = None
    else:
        t1, t2 = tempfile.mkdtemp(), tempfile.mkdtemp()
        b1, l1 = transform(t1, a.r2); b2, l2 = transform(t2, a.r2)
        G['R1'] = b1 == b2 and l1 == l2; G['R0'] = G['R0'] and b1 == FB
        shutil.rmtree(t1); shutil.rmtree(t2)
    log = json.load(open(os.path.join(os.path.dirname(os.path.abspath(a.final)), 'release_v6_4_20_log.json')))
    FL, RL = F.split('\n'), R2.split('\n')
    s0 = [i for i, l in enumerate(FL) if l.startswith('### v6.4.20 — adopted 21 October 2026')]
    s1 = [i for i, l in enumerate(FL) if l.startswith('### v6.4.20 DRAFT r2 — 21 October 2026')]
    ok_rec = len(s0) == 1 and len(s1) == 1 and s0[0] < s1[0]
    rec = '\n'.join(FL[s0[0]:s1[0]]) if ok_rec else ''
    body = FL[:s0[0]] + FL[s1[0]:] if ok_rec else FL
    why = []
    if ok_rec and len(body) == len(RL):
        changed = [i for i, (x, y) in enumerate(zip(RL, body)) if x != y]
        for i in changed:
            x, y = RL[i], body[i]
            if '> ' + x not in rec: why.append((i + 1, 'not quoted')); continue
            if i < 14:
                if x.startswith(('**Edition:**', '**Status:**', '**Supersedes (on adoption only):**', '**Draft record:**')): continue
                if x.startswith('**Status summary:**') and y.startswith(x[:x.index(' This draft adds')]): continue
                why.append((i + 1, 'header')); continue
            if i >= len(RL) - 3 and x.startswith(('*END OF DOCUMENT', '*DRAFT r2, 21 October 2026')): continue
            removed = collections.Counter(tok(x)) - collections.Counter(tok(y))
            extra = sorted(set(removed) - LABEL_WORDS)
            if 'not' in removed and 'adopted' not in removed: extra.append('not')
            if extra: why.append((i + 1, 'removed words', extra[:5]))
        G['R2'] = not why and len(changed) == log['replaced_lines']
        info['R2'] = {'changed': len(changed), 'log': log['replaced_lines'], 'why': why[:8]}
    else:
        G['R2'] = False; info['R2'] = {'record_ok': ok_rec, 'len_body': len(body), 'len_r2': len(RL)}
    bodyT = '\n'.join(body)
    aF = F.index('## Appendix A'); bF = F.index('## Appendix B'); aR = R2.index('## Appendix A'); bR = R2.index('## Appendix B')
    seqF = re.findall(r'\[RID:\s*[^\]]+\]', F[:aF] + F[bF:]); seqR = re.findall(r'\[RID:\s*[^\]]+\]', R2[:aR] + R2[bR:])
    G['R3'] = census(F) == census(R2) and census(F) == census(BASE) | NEW13 and len(census(F)) == 148 and seqF == seqR
    info['R3'] = {'tagged': len(census(F)), 'v6_4_19': len(census(BASE))}
    G['R4'] = maths(bodyT) == maths(R2)
    G['R5'] = GRADE_RE.findall(bodyT) == GRADE_RE.findall(R2)
    live = F[:aF] + F[bF:]
    residue = ['registered only at adoption', '— proposed, not adopted |', 'not adopted, not released', 'Supersedes (on adoption only)',
               'canonical until a v6.4.20 adoption decision', '| proposed RID', 'DRAFT r2 — not adopted']
    G['R6'] = not any(r in live for r in residue); info['R6'] = [r for r in residue if r in live]
    head = F[:F.index('## Local Tag Aliases')]
    G['R7'] = (F.startswith('# RTG_DYADIC_OSCILLATOR_DSN_v6.4.20\n') and '**Edition:** v6.4.20 — adopted 21 October 2026' in head
               and '**Status:** ADOPTED — owner/PI adoption recorded 21 October 2026 (`DYAD v6.4.20 — OWNER ADOPTION AUTHORIZED`)' in head
               and '`DYAD v6.4.20 DRAFT r2 — REVIEW ACCEPTED`' in head and R2_HASH in head
               and '**Supersedes:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.19` (adopted 20 Oct 2026, `' + V619 + '`' in head)
    G['R8'] = (len(re.findall(r'^\*END OF DOCUMENT', F, re.M)) == 1 and '*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.20*' in F
               and F.count('<!-- AI_CONTEXT_CORE_END -->') == 1 and re.search(r'^\*Adopted 21 October 2026; supersedes RTG_DYADIC_OSCILLATOR_DSN_v6\.4\.19', F, re.M) is not None)
    s2F = F[F.index('## §2.'):F.index('## §3.')]; s2R = R2[R2.index('## §2.'):R2.index('## §3.')]
    stF = [l for l in s2F.split('\n') if 'Status:' in l]; stR = [l for l in s2R.split('\n') if 'Status:' in l]
    o20 = 'OPEN 20 is PARTIAL: B-∞ existence and flat uniqueness are CLOSED; B-an and B-6 are OPEN.'
    G['R9'] = stF == stR and o20 in F[:aF] and o20 in R2[:aR]
    G['R10'] = ok_rec and all(x in rec for x in ['`DYAD v6.4.20 — OWNER ADOPTION AUTHORIZED`', '`REVIEWER-REPLAYED`', '`OWNER-RUN`',
                                                  '`REVIEWER FULL REPLAY NOT COMPLETED` — the combined G14–G15 run carried from v6.4.19',
                                                  'only after external verification of this file\'s SHA-256']) and all('`' + r + '`' in rec for r in NEW13)
    e1 = F[F.index('**E.1 Statement'):F.index('**E.2 Evidence')]; e2 = F[F.index('**E.2 Evidence'):F.index('## Appendix F')]
    r1 = [l for l in e1.split('\n') if l.startswith('| `DYAD-')]; r2 = [l for l in e2.split('\n') if l.startswith('| `DYAD-')]
    newrows = [l for l in r1 if l.split('|')[1].strip().strip('`') in NEW13]
    G['R11'] = (len(r1) == 58 and len(r2) == 58 and len(newrows) == 11 and all('— new in v6.4.20 |' in l for l in newrows)
                and not any('proposed' in l for l in r1 + r2))
    ok = all(v is not False for v in G.values())
    for k in sorted(G, key=lambda x: int(x[1:])): print(k, {True: 'PASS', False: 'FAIL', None: 'SKIP'}[G[k]])
    print('ALL PASS' if ok else 'FAIL')
    with open(a.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': G, 'info': info, 'all_pass': ok, 'final_sha256': sha(FB)}, f, indent=1, sort_keys=True); f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as ex:
        import traceback; traceback.print_exc(); print('CRASH', type(ex).__name__, ex); sys.exit(3)
