#!/usr/bin/env python3
"""OFN v0.10 owner disposition checks (co-owner session claude012ZC8x, 29 Oct 2026).

Reads each owner file at its governing tag with `git show`, recomputes its SHA-256,
and checks that every owner statement this disposition relies on is present at that
tag, quoted by RID and by a load-bearing phrase. Also checks the RECOG v0.3.20 freeze
record hash and two algebraic facts used in rows 1 and 11. Run from the repository root:
    python3 -I evidence/ofn/disposition/ofn_v0_10_owner_disposition_checks.py
Exit 0 iff every check passes. Negative controls at the end must FAIL as required.
"""
import hashlib, subprocess, sys

def show(tag, path):
    return subprocess.run(['git', 'show', f'{tag}:{path}'], capture_output=True, check=True).stdout

FILES = {
    'ofn-v0.10':     ('dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md', 'acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa'),
    'dyad-v6.4.22':  ('dsn/RTG_DYADIC_OSCILLATOR_DSN.md', '2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29'),
    'gen-v2.9':      ('dsn/RTG_GENESIS_GEOMETRY_DSN.md', '9178ca2cd38bea8d55deada78b6adbd8022533c4baad7af101583b1179d300ac'),
    'rrf-v0.8.4':    ('dsn/RTG_RRF_REPRESENTATION_REGISTRY.md', '2fb0a0fe9d998be91618cb731e2dee7301952ffdbe374f4889dd5e61c5cbafce'),
    'tdrg-v2.12.14': ('dsn/RTG_DISCRETE_GENESIS_DSN.md', '3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392'),
    'numgen-v1.21':  ('dsn/RTG_NUMBER_GENESIS_DSN.md', '4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701'),
    'recog-v0.3.26': ('dsn/RTG_RELATIONAL_RECOGNITION_DSN.md', '45e307f8333c81a344158ada07ad34a1a3afab6e1b93b2aa04ee09f84878dd34'),
    'triad-v1.6.1':  ('dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md', '95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f'),
}
# (tag, phrase) pairs: owner statements relied on by the disposition rows
NEEDLES = [
 ('dyad-v6.4.22', '[RID: DYAD-THM-SMOOTH-EMBEDDING]'),
 ('dyad-v6.4.22', '[RID: DYAD-THM-SMOOTH-EQUIVARIANT-CHART]'),
 ('dyad-v6.4.22', 'B-∞ existence **CLOSED (v6.4.18)**'),
 ('dyad-v6.4.22', 'B-an and B-6 ACTIVE'),
 ('dyad-v6.4.22', 'inherits none of the finite-chart bounds of §6.14 (SG-19)'),
 ('dyad-v6.4.22', 'Whether Genesis C2 or OFN class C uses it is their owners\' decision'),
 ('dyad-v6.4.22', '[RID: DYAD-DEF-PRIMITIVE-MAP]'),
 ('dyad-v6.4.22', '| N14 | v6.4.18 | OFN | same | NOT RECORDED |'),
 ('dyad-v6.4.22', 'INFORMATIONAL — no OFN receipt recorded'),
 ('gen-v2.9', '`[RID: GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO]` `[scope: real C^3 germs'),
 ('gen-v2.9', 'so (C2) is non-vacuous at \\(C^\\infty\\)'),
 ('gen-v2.9', '`[RID: GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO]` `[scope:'),
 ('gen-v2.9', '`[RID: GEN-THM-K3-SIXSTEP-FACTOR-NOGO]` `[scope:'),
 ('rrf-v0.8.4', '### 6.2a OFN class-C model contract'),
 ('rrf-v0.8.4', 'OFN/Genesis have **not** separately adopted the resulting class-C family'),
 ('rrf-v0.8.4', 'determines `m` **only up to** the reflection'),
 ('rrf-v0.8.4', 'A $C^\\infty$ carrier may be studied as a **candidate**'),
 ('tdrg-v2.12.14', 'State: **statement accepted**'),
 ('tdrg-v2.12.14', 'Custody transfer XFER-O08-01: **deferred** to v2.13 (the RID stays OFN\'s)'),
 ('tdrg-v2.12.14', 'OFN REQ-O09-05 is answered by TDRG-DEF-ORIENT'),
 ('tdrg-v2.12.14', 'it is a symmetry of the birth-free sector only, not a gauge'),
 ('tdrg-v2.12.14', '[RID: TDRG-DEF-STAR] **Star blow-up**'),
 ('tdrg-v2.12.14', '$\\delta_E = \\delta_A$; center inverts: $\\delta_A \\mapsto -\\delta_A \\bmod N$'),
 ('tdrg-v2.12.14', '**[SG-3]** Total additive momentum $P = \\sum \\delta_i$ is not a physical observable.'),
 ('tdrg-v2.12.14', '[RID: TDRG-DEF-PHYSICAL-STATE] **Physical state** is the quotient by global phase shift'),
 ('tdrg-v2.12.14', 'a 2-cycle for $d\\neq0$, a fixed point for $d=0$ (LEM-RETRIG)'),
] + [('tdrg-v2.12.14', f'[RID: {r}]') for r in (
    'TDRG-DEF-ZN-STATE','TDRG-DEF-REL-ADVANCE','TDRG-DEF-BAND','TDRG-THM-HOLONOMY','TDRG-THM-NARROW-BAND-EXCLUSION',
    'TDRG-THM-RECURRENCE','TDRG-DEF-CONV-TICK','TDRG-DEF-CONV-P3CYC','TDRG-DEF-ORIENT','TDRG-ALG-LEM-REACH',
    'TDRG-ALG-LEM-NOANNIHIL','TDRG-ALG-LEM-RETRIG','TDRG-ALG-LEM-SPECCONS','TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK')] + [
 ('numgen-v1.21', '[RID: NUMGEN-RESULT-N5AS1-L-BACKBONE]'),
 ('numgen-v1.21', 'answers OFN REQ-O09-03'),
] + [('recog-v0.3.26', f'[RID: {r}]') for r in (
    'RECOG-ALG-SHEAR-COCYCLE-CLASSIFICATION','RECOG-ALG-SHEAR-WEIGHT-IDENTIFICATION','RECOG-ALG-SHEAR-ORIENTATION-CONJUGACY',
    'RECOG-DEF-POLE-COMPARATOR','RECOG-DEF-STATE-COMPARATOR','RECOG-ALG-SELECTION-SIN','RECOG-ALG-SWAP-SPLIT',
    'RECOG-THM-R9-MEMORY','RECOG-ALG-CONTINUOUS-CARRIER-NOWRITE','RECOG-RESULT-R9-NO-TOKEN-WRITETHROUGH',
    'RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS','RECOG-THM-R9-SHARPENED-ROWS')] + [
 ('recog-v0.3.26', '| large | $|z|\\le\\tfrac1{20}$, $C_7=100$ | $\\tfrac1{400}$ | $517$ |'),
 ('triad-v1.6.1', 'Programme/OFN pass two'),
 ('ofn-v0.10', '`[DEF]` [RID: RTG-OFN-DEF-STANDARD-C] [scope: as above] **Standard C at cubic order.**'),
 ('ofn-v0.10', 'Standard C holds if there is a nonempty $F$-invariant regime $\\mathcal R$'),
 ('ofn-v0.10', '| Regularity | Real-analytic laws form the admitted continuous FMS test class; this is not a universal requirement. |'),
 ('ofn-v0.10', '| Total additive token sum as a physical conserved quantity |'),
]
ok = True; out = []
texts = {}
for tag, (path, sha) in FILES.items():
    b = show(tag, path); h = hashlib.sha256(b).hexdigest(); texts[tag] = b.decode('utf-8')
    good = h == sha; ok &= good
    out.append(f'HASH {tag:14s} {path} {h} {"PASS" if good else "FAIL"}')
for tag, needle in NEEDLES:
    n = texts[tag].count(needle); good = n >= 1; ok &= good
    out.append(f'FIND {tag:14s} x{n} {"PASS" if good else "FAIL"} :: {needle[:90]}')
fr = 'records/recog/RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md'
h = hashlib.sha256(open(fr, 'rb').read()).hexdigest()
good = h == '5c00f66dae7d4de6ccd4a04d642a23edfc861bbd6bd55e432513747fbd679b55' and 'Fulfils REQ-O09-02' in open(fr, encoding='utf-8').read()
ok &= good; out.append(f'HASH {fr} {h} + "Fulfils REQ-O09-02" {"PASS" if good else "FAIL"}')

# Row 11 algebra: under TDRG-DEF-STAR the token sum changes by -delta_A (mod N); permutations conserve it.
N = 24; viol = 0
for dA in range(N):
    for rest in range(N):
        before = (dA + rest) % N
        after = ((-dA) % N + dA + rest) % N          # centre inverted, newborn copies delta_A, leaves unchanged
        if (after - before) % N != (-dA) % N: viol += 1
good = viol == 0; ok &= good
out.append(f'ALG  star token-sum change = -delta_A (mod {N}), all delta_A: {"PASS" if good else "FAIL"}')
# Row 1 algebra: a real linear A with A^3=-I, A^6=I (order-6 rotation): any map commuting with A is odd
import math
c, s = math.cos(math.pi/3), math.sin(math.pi/3)
A = [[c, -s], [s, c]]
def mul(X, Y): return [[sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
A3 = mul(mul(A, A), A)
good = all(abs(A3[i][j] - (-1 if i == j else 0)) < 1e-12 for i in range(2) for j in range(2)); ok &= good
out.append(f'ALG  A^3 = -I for the order-6 rotation (so A-commuting maps are odd): {"PASS" if good else "FAIL"}')

# Negative controls: must FAIL
neg = [('dyad-v6.4.22', 'B-∞ existence open'), ('rrf-v0.8.4', 'OFN has adopted the C^\\infty class-C family'),
       ('tdrg-v2.12.14', 'Custody transfer XFER-O08-01: **accepted**'), ('ofn-v0.10', 'positive-dimensional $F$-invariant regime $\\mathcal R$')]
for tag, needle in neg:
    n = texts[tag].count(needle); good = n == 0; ok &= good
    out.append(f'NEG  {tag:14s} absent as required: {"PASS" if good else "FAIL"} :: {needle}')
print('\n'.join(out)); print('ALL PASS' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
