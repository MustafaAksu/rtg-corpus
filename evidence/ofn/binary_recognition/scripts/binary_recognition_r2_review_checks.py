#!/usr/bin/env python3
"""Binary-recognition wrap-up r2 review checks (Claude, 25 Nov 2026; SESSION). One check group per item of the ChatGPT
OFN co-owner review 6054839244 of PR #183 (R-B1a, R-B1b, R-B5, R-BRQ3, R-B6, R-B2, R-B3). Exact arithmetic in Z[t]/Phi_N;
SymPy only generates Phi_N. usage: python3 -I binary_recognition_r2_review_checks.py   (exit 0 iff all pass)
"""
import itertools, sys
from math import gcd
from sympy import cyclotomic_poly, Poly, symbols
t = symbols("t")
_phi = {}
def phi(N):
    if N not in _phi: _phi[N] = [int(c) for c in reversed(Poly(cyclotomic_poly(N, t), t).all_coeffs())]
    return _phi[N]
def red(c, N):                       # reduce integer coefficient list modulo Phi_N (monic)
    c = list(c); p = phi(N); d = len(p) - 1
    for i in range(len(c) - 1, d - 1, -1):
        a = c[i]
        if a:
            for j in range(d + 1): c[i - d + j] -= a * p[j]
    c = c[:d] + [0] * max(0, d - len(c)); return tuple(c[:d])
def F(X): return (1 - X[-1],) + tuple(X[:-1])
def C(X): return tuple(1 - x for x in X)
def par(X): return sum(X) % 2
def zkey(X):                         # Z_n(X) = 1 - (1-lam) P_X(lam), lam = primitive 2n-th root; exact element of Z[lam]
    n = len(X); P = list(X) + [0]; q = [0] * (n + 2)
    for j, x in enumerate(X): q[j] -= x; q[j + 1] += x          # -(1-t)P = -P + tP
    q[0] += 1; return red(q, 2 * n)
def zero(X): return all(v == 0 for v in zkey(X))
def period(X):
    Y, k = F(X), 1
    while Y != X: Y, k = F(Y), k + 1
    return k
res = []
def ok(name, cond): res.append((name, bool(cond))); print(("PASS " if cond else "FAIL ") + name)

# B1a  Z_n is C-odd for every n (so it is never an instantaneous C-invariant); parity C-type is n mod 2
for n in range(1, 11):
    good = all(red([-a for a in zkey(X)], 2 * n) == zkey(C(X)) for X in itertools.product((0, 1), repeat=n))
    ok(f"B1a Z_{n}(CX) = -Z_{n}(X) on all 2^{n} states", good)
ok("B1a parity is C-invariant iff n even (n=1..10)", all((par(C(X)) == par(X)) == (n % 2 == 0)
   for n in range(1, 11) for X in itertools.product((0, 1), repeat=n)))
ok("B1a n=1 (=2^0): Z_1 injective, but parity is C-odd (not gauge-invariant)", par(C((0,))) != par((0,)))

# B1b  vanishing-subset equivalence of §3D needs odd m > 1
def S_of(X):
    m = len(X); l = (m + 1) // 2; y = [2 * x - 1 for x in X]
    return {(l * j) % m for j in range(m) if (-1) ** j * y[j] == 1}
def vanishing(S, m):                 # sum_{u in S} zeta_m^u == 0 in Q(zeta_m)
    c = [0] * m
    for u in S: c[u] += 1
    return all(v == 0 for v in red(c, m)) if m > 1 else len(S) == 0
X0 = (0,)
ok("B1b m=1: X=(0) has empty S (vanishing empty sum) but Z_1=1 != 0 -> equivalence fails", vanishing(S_of(X0), 1) and not zero(X0))
for m in (3, 5, 7, 9, 15):
    ok(f"B1b m={m}: Z_m(X)=0 iff sum_(u in S_X) zeta_m^u = 0 (all 2^{m} states)",
       all(zero(X) == vanishing(S_of(X), m) for X in itertools.product((0, 1), repeat=m)))

# B5  retention alone does not force the four-cycle
def cyc(f):
    G = lambda s: (f(*s), s[0]); return sorted((period_of(G, s) or 0) for s in itertools.product((0, 1), repeat=2))  # 0 = not on a cycle
def period_of(G, s):
    y, k = G(s), 1
    while y != s and k < 9: y, k = G(y), k + 1
    return k if y == s else None
ok("B5 retention p'=b with f=b: fixed states (0,0),(1,1) -> no four-cycle", 4 not in cyc(lambda b, p: b) and 1 in cyc(lambda b, p: b))
ok("B5 retention with f=1-p: single four-cycle (alternation added)", cyc(lambda b, p: 1 - p) == [4, 4, 4, 4])
ok("B5 retention with f=p: reversible but two-cycles/fixed points", 4 not in cyc(lambda b, p: p))

# BR-Q3 conditional bookkeeping: C_h on X_h, h = 2^a
for h in (1, 2, 4, 8):
    S = list(itertools.product((0, 1), repeat=h)); free = all(C(X) != X for X in S)
    classes = len({min(X, C(X)) for X in S}); desc = all(par(X) == par(C(X)) for X in S)
    ok(f"BR-Q3 h={h}: C_h free, {classes} = 2^(h-1) classes, parity descends to X_h/C: {desc} (expected {h % 2 == 0})",
       free and classes == 2 ** (h - 1) and desc == (h % 2 == 0))

# B6  RRF sign product r(X)r(Y): shared complement invariant for every n; one-sided flips sign iff n odd
r = lambda X: (-1) ** par(X)
for n in range(1, 9):
    S = list(itertools.product((0, 1), repeat=n))
    shared = all(r(C(X)) * r(C(Y)) == r(X) * r(Y) for X in S for Y in S)
    one = all(r(C(X)) * r(Y) == (-1) ** n * r(X) * r(Y) for X in S for Y in S)
    ok(f"B6 n={n}: shared-C invariant; one-sided C multiplies by (-1)^n", shared and one)

# B2  replication: rep_k repeats each bit k times; Z_kn rep_k = Z_n; parity picks up k mod 2
def rep(X, k): return tuple(x for x in X for _ in range(k))
def zval_equal(X, Y):                # Z_n(X) vs Z_kn(Y) compared in Q(lam_kn): lift Z_n through lam_n = lam_kn^k
    n, N = len(X), len(Y); k = N // n; q = [0] * (k * (n + 1) + 1)
    for j, x in enumerate(X): q[k * j] -= x; q[k * (j + 1)] += x
    q[0] += 1; return red(q, 2 * N) == zkey(Y)
ok("B2 rep_k: Z_kn(rep_k X) = Z_n(X) and pi_kn(rep_k X) = (k mod 2) pi_n(X) (n<=5, k<=4)",
   all(zval_equal(X, rep(X, k)) and par(rep(X, k)) == (k % 2) * par(X)
       for n in range(1, 6) for k in range(1, 5) for X in itertools.product((0, 1), repeat=n)))
ok("B2 n=2,k=2,X=(1,0): parity 1 -> 0 under replication", par((1, 0)) == 1 and par(rep((1, 0), 2)) == 0)

# B3  Zero/Short counts (exhaustive where feasible) and the two-prime formulas
def counts(n):
    Z = Sh = 0
    for X in itertools.product((0, 1), repeat=n):
        z = zero(X); s = period(X) < 2 * n; Z += z; Sh += s
    return Z, Sh
for n, exp in ((1, (0, 0)), (3, (2, 2)), (9, (8, 8)), (15, (38, 38))):
    ok(f"B3 n={n}: |Zero| = |Short| = {exp[0]}", counts(n) == exp)
for n, k, p, q in ((30, 2, 3, 5), (45, 3, 3, 5)):
    ok(f"B3 n={n}: (2^p+2^q-2)^k = {(2**p + 2**q - 2)**k}, 2^(kq)+2^(kp)-2^k = {2**(k*q) + 2**(k*p) - 2**k} (stated 1444/1084, 54872/33272)",
       ((2**p + 2**q - 2)**k, 2**(k*q) + 2**(k*p) - 2**k) == {30: (1444, 1084), 45: (54872, 33272)}[n])
for w in ("111111010100101010000101111111", "111101010100010001011101010100110101011101010"):
    X = tuple(int(c) for c in w); ok(f"B3 witness n={len(X)}: Z=0 and period 2n", zero(X) and period(X) == 2 * len(X))

fails = [n for n, c in res if not c]
print(f"\nRESULT: {'PASS' if not fails else 'FAIL'} {len(res) - len(fails)}/{len(res)}")
sys.exit(0 if not fails else 1)
