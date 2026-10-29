"""Atlas row check OFN v0.11 — mechanical checks of the candidate against the governing tags.
Usage: python3 -I ofn011_checks.py CANDIDATE STAGE1 (run with cwd = a repository checkout)"""
import re, subprocess, collections, sys
cand = open(sys.argv[1], encoding='utf-8').read(); s1 = open(sys.argv[2], encoding='utf-8').read()
v010 = subprocess.check_output(['git','show','ofn-v0.10:dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md']).decode()
def at(ref, p): return subprocess.check_output(['git','show',f'{ref}:{p}']).decode()
src = {'GEN': at('gen-v2.9','dsn/RTG_GENESIS_GEOMETRY_DSN.md'), 'DYAD': at('dyad-v6.4.22','dsn/RTG_DYADIC_OSCILLATOR_DSN.md'),
       'RECOG': at('recog-v0.3.26','dsn/RTG_RELATIONAL_RECOGNITION_DSN.md'), 'TDRG': at('tdrg-v2.12.14','dsn/RTG_DISCRETE_GENESIS_DSN.md'),
       'NUMGEN': at('numgen-v1.21','dsn/RTG_NUMBER_GENESIS_DSN.md'), 'RRF': at('rrf-v0.8.4','dsn/RTG_RRF_REPRESENTATION_REGISTRY.md'),
       'TRIAD': at('triad-v1.6.1','dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md'), 'UVM': at('uvm-v0.7.1','dsn/RTG_OPEN_M_DSN.md'),
       'RTG': at('programme-v1.3','dsn/RTG_PROGRAMME_OVERVIEW.md')}
def live(t):  # up to the version-history appendix
    i = t.find('\n## Appendix C'); return t[:i] if i > 0 else t
L = live(cand)
print('# 1. owner RIDs cited in the candidate (live text), resolution at the governing tags')
rids = sorted(set(re.findall(r'(?<![A-Za-z0-9-])((?:GEN|DYAD|RECOG|TDRG|NUMGEN|RRF|UVM|TRIAD)-(?:DEF|THM|ALG|RESULT|CAND|OPEN|HYP|ART|NUM|CND|NET|DYAD)-[A-Z0-9-]*[A-Z0-9]|RTG-OPEN-[A-Z0-9-]*[A-Z0-9])', L)))
cnt = collections.Counter()
for r in rids:
    p = 'RTG' if r.startswith('RTG-') else r.split('-')[0]; s = src[p]
    dec = ('RID: ' + r + ']') in s or ('RID: ' + r + ' ') in s or ('`' + r + '`' in s and p == 'RTG')
    st = 'DECLARED' if dec else ('PRESENT' if r in s else 'ABSENT'); cnt[st] += 1
    if st != 'DECLARED': print(f'  {r}: {st} in {p}')
print('  summary:', dict(cnt), 'of', len(rids))
print('\n# 2. OFN RIDs: declared in candidate vs v0.10')
dc = re.findall(r'\[RID: (RTG-OFN-[A-Z0-9-]+)\]', cand); dv = re.findall(r'\[RID: (RTG-OFN-[A-Z0-9-]+)\]', v010)
print('  declared candidate', len(dc), 'distinct', len(set(dc)), '| v0.10', len(dv), len(set(dv)))
print('  new:', sorted(set(dc) - set(dv)), '| dropped:', sorted(set(dv) - set(dc)))
print('  duplicates:', [k for k, v in collections.Counter(dc).items() if v > 1])
ofn_mentioned = set(re.findall(r'RTG-OFN-[A-Z0-9-]*[A-Z0-9]', cand)); print('  mentioned but not declared:', sorted(ofn_mentioned - set(dc) - {'RTG-OFN'}))
print('\n# 3. OPEN status lines')
for t, n in (('v0.10', v010), ('cand', cand)):
    st = re.findall(r'^Status: (ACTIVE|PARTIAL|CLOSED)', n, re.M); print(' ', t, collections.Counter(st))
print('\n# 4. residue in the live text (cand)')
for pat in ['RID unavailable', 'freeze candidate', 'freeze-candidate', 'conditional on DYAD OPEN 20', 'existence is not asserted', 'real only once', 'v2.12.13', 'v0.3.20', 'v6.4.10', 'v1.20.7', 'LEM-REACH', 'CONV-TICK', 'CUST-O09-01', 'Draft 1', 'Until then', 'this draft', 'adoption pending']:
    hits = [i for i, l in enumerate(cand.split('\n'), 1) if pat in l and i <= L.count('\n') + 1]
    print(f'  {pat!r}: {len(hits)} live lines {hits[:10]}')
print('\n# 5. [RESULT] pairing and tag census (candidate)')
print('  [RESULT] without [from: on the same line:', [i for i, l in enumerate(cand.split('\n'), 1) if '`[RESULT]`' in l and '[from:' not in l])
tags = collections.Counter(re.findall(r'`\[([A-Z][A-Za-z -]*(?:—[^\]`]*)?)\]`', cand)); print(' ', dict(tags.most_common(30)))
print('  dash-compound tags:', [k for k in tags if '—' in k])
print('\n# 6. version strings in the candidate live text')
c = collections.Counter(re.findall(r'`[a-z0-9]+-v[0-9][0-9.]*`', L)); print(' ', dict(sorted(c.items())))
c2 = collections.Counter(re.findall(r'(?:Programme|Methodology|Genesis|Dyadic|DYAD|RECOG|Triadic|TRIAD|TDR-G|NUMGEN|RRF|OPEN M|Legacy|Pre-Legacy|DZT|AZ|UVM|ER-2B|FMS)\s+v\d[\d.]*', L)); print(' ', dict(sorted(c2.items())))
print('\n# 7. header')
print('\n'.join(l[:220] for l in cand.split('\n')[:24] if l.startswith('**')))
