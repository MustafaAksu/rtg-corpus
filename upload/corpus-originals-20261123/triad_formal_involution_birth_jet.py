#!/usr/bin/env python3
"""
Formal triadic involution S = N^3 o F^(-1/2) of the conditional modal map, exact jet through degree D=5,
and its interaction with the trial birth graph B_k(s) = (s, kt Q(s) M s)   (kappa = sqrt3*kt, M = [[1,-2],[2,-1]]).

Construction (formal, exact rationals, standard library only):
  F = N^6 = id + g,  g = O(|X|^3);  F^(-1/2) = (F*)^(-1/2) x = sum_k C(-1/2,k) (F* - I)^k x,
  (F* - I) x_i = g_i,  (F* - I)^2 x_i = g_i o F - g_i;  through degree 5 only k <= 2 contribute.
Checks:  S o S = id,  S o N = N o S,  DS(0) = -I,  S o R = R o S  for the slot swap R(s,c) = (s,-c),
         and for the other two slot transpositions (c = +-3s/2 fixed sets) via their linear actions.
Birth graph:
  covariance defect   D(s) = S(B(s)) - B(-s)                      (componentwise; chart-dependent)
  graph defect        G(s) = S_c(B(s)) - C(S_s(B(s)))             (zero iff S maps the graph to itself)
Both are reported as homogeneous components of degree 2..5 in s=(r,e), for kt = 1 and kt = 2 (they are affine in kt
through degree 5, because c enters at most linearly there).
Usage:  python triad_formal_involution_birth_jet.py      (exit 0 iff all identity checks pass)
"""
import sys
from fractions import Fraction as Fr
from math import factorial
D = 5
NV = 4   # X = (s_r, s_e, c_r, c_e)

# --------------------------------------------------------------- sparse truncated polynomials in NV variables
def deg(m): return sum(m)
def padd(a, b, k=1):
    o = dict(a)
    for m, v in b.items():
        o[m] = o.get(m, 0) + k*v
        if o[m] == 0: del o[m]
    return o
def pscale(a, k): return {m: k*v for m, v in a.items() if k*v != 0}
def pmul(a, b):
    o = {}
    for m1, v1 in a.items():
        d1 = deg(m1)
        for m2, v2 in b.items():
            if d1 + deg(m2) > D: continue
            m = tuple(x+y for x, y in zip(m1, m2)); o[m] = o.get(m, 0) + v1*v2
    return {m: v for m, v in o.items() if v != 0}
def pconst(c): return {(0,)*NV: Fr(c)} if c else {}
def pvar(i): m = [0]*NV; m[i] = 1; return {tuple(m): Fr(1)}
def compose(p, Y):
    """p(Y) for polynomial p in NV vars and Y a list of NV polynomials with zero constant term."""
    cache = {}
    def power(i, k):
        if (i, k) not in cache:
            cache[(i, k)] = pconst(1) if k == 0 else pmul(power(i, k-1), Y[i])
        return cache[(i, k)]
    o = {}
    for m, v in p.items():
        t = pconst(v)
        for i, k in enumerate(m):
            if k: t = pmul(t, power(i, k))
            if not t: break
        o = padd(o, t)
    return o
def vcompose(P, Y): return [compose(p, Y) for p in P]
def series_sin(p):
    o = {}; pw = p; k = 0
    while pw:
        o = padd(o, pscale(pw, Fr((-1)**k, factorial(2*k+1)))); pw = pmul(pmul(pw, p), p); k += 1
    return o
def series_expm1(p):
    o = {}; pw = p; k = 1
    while pw:
        o = padd(o, pscale(pw, Fr(1, factorial(k)))); pw = pmul(pw, p); k += 1
    return o
HALF = Fr(1, 2)
def Te(v):
    r, e = v; se = series_sin(e)
    return [padd(r, se, -1), padd(padd(e, series_expm1(r)), se, -1)]
X = [pvar(i) for i in range(NV)]
def N_of(Xv):
    s = Xv[0:2]; c = Xv[2:4]
    a = Te(s)
    b = Te([padd(pscale(s[i], -HALF), c[i]) for i in range(2)])
    d = Te([padd(pscale(s[i], -HALF), c[i], -1) for i in range(2)])
    s2 = [pscale(padd(padd(pscale(a[i], 2), b[i], -1), d[i], -1), Fr(1, 3)) for i in range(2)]
    c2 = [pscale(padd(b[i], d[i], -1), HALF) for i in range(2)]
    return s2 + c2
Nmap = N_of(X)
def iterate(P, n):
    Q = X
    for _ in range(n): Q = vcompose(P, Q)
    return Q
F = iterate(Nmap, 6)
N3 = iterate(Nmap, 3)
g = [padd(F[i], X[i], -1) for i in range(NV)]
gF = vcompose(g, F)
C1, C2 = Fr(-1, 2), Fr(3, 8)
Fm12 = [padd(padd(X[i], pscale(g[i], C1)), pscale(padd(gF[i], g[i], -1), C2)) for i in range(NV)]
S = vcompose(N3, Fm12)

def homog(p, d): return {m: v for m, v in p.items() if deg(m) == d}
def is_zero(P): return all(not p for p in P)
ok_all = True
def check(name, cond):
    global ok_all
    ok_all &= bool(cond); print(('PASS ' if cond else 'FAIL ') + name)
check('F = N^6 has linear part I and no quadratic part', all(homog(F[i], 1) == X[i] and not homog(F[i], 2) for i in range(NV)))
check('DS(0) = -I', all(homog(S[i], 1) == pscale(X[i], -1) for i in range(NV)))
SS = vcompose(S, S); check('S o S = id through degree 5', all(SS[i] == X[i] for i in range(NV)))
SN = vcompose(S, Nmap); NS = vcompose(Nmap, S)
check('S o N = N o S through degree 5', all(SN[i] == NS[i] for i in range(NV)))
# slot actions: R23 (s,c)->(s,-c); R12, R13: linear maps P Pi E (x) I2 computed from E,P
E = [[Fr(1), Fr(0)], [Fr(-1, 2), Fr(1)], [Fr(-1, 2), Fr(-1)]]
Pm = [[Fr(2, 3), Fr(-1, 3), Fr(-1, 3)], [Fr(0), Fr(1, 2), Fr(-1, 2)]]
def slot_action(perm):
    PiE = [E[perm[k]] for k in range(3)]                       # rows of Pi E
    R = [[sum(Pm[a][k]*PiE[k][b] for k in range(3)) for b in range(2)] for a in range(2)]   # 2x2 on (s,c) mode labels
    # acts on X = (s_r,s_e,c_r,c_e) as R (x) I2:  s' = R00 s + R01 c,  c' = R10 s + R11 c
    return [padd(pscale(X[0], R[0][0]), pscale(X[2], R[0][1])), padd(pscale(X[1], R[0][0]), pscale(X[3], R[0][1])),
            padd(pscale(X[0], R[1][0]), pscale(X[2], R[1][1])), padd(pscale(X[1], R[1][0]), pscale(X[3], R[1][1]))]
for name, perm in (('swap 2<->3', (0, 2, 1)), ('swap 1<->2', (1, 0, 2)), ('swap 1<->3', (2, 1, 0)), ('3-cycle', (1, 2, 0))):
    Rv = slot_action(perm)
    NR = vcompose(Nmap, Rv); RN = vcompose(Rv, Nmap)
    SR = vcompose(S, Rv); RS = vcompose(Rv, S)
    check(f'slot action {name}: commutes with N (exact model symmetry) and with S (uniqueness consequence)',
          all(NR[i] == RN[i] for i in range(NV)) and all(SR[i] == RS[i] for i in range(NV)))
check('S is NOT -I (nonzero quadratic jet)', any(homog(S[i], 2) for i in range(NV)))

# --------------------------------------------------------------- birth graph
def birth(kt):
    r, e = X[0], X[1]
    Q = padd(padd(pmul(r, r), pmul(r, e), -1), pmul(e, e))
    c_r = pscale(pmul(Q, padd(r, pscale(e, 2), -1)), kt)
    c_e = pscale(pmul(Q, padd(pscale(r, 2), e, -1)), kt)
    return [r, e, c_r, c_e]
def Cgraph_of(kt, sv):
    r, e = sv
    Q = padd(padd(pmul(r, r), pmul(r, e), -1), pmul(e, e))
    return [pscale(pmul(Q, padd(r, pscale(e, 2), -1)), kt), pscale(pmul(Q, padd(pscale(r, 2), e, -1)), kt)]
def fmt(p):
    if not p: return '0'
    terms = []
    for m, v in sorted(p.items(), key=lambda t: (-t[0][0], t[0])):
        mono = '*'.join(f'{x}^{k}' if k > 1 else x for x, k in zip(('r', 'e', 'cr', 'ce'), m) if k)
        terms.append(f'{v}*{mono}' if mono else str(v))
    return ' + '.join(terms)
results = {}
for kt in (Fr(1), Fr(2)):
    B = birth(kt); Bm = [compose(b, [pscale(X[0], -1), pscale(X[1], -1), X[2], X[3]]) for b in B]   # B(-s)
    SB = vcompose(S, B)
    Dv = [padd(SB[i], Bm[i], -1) for i in range(NV)]
    G = [padd(SB[2+i], Cgraph_of(kt, SB[0:2])[i], -1) for i in range(2)]
    results[kt] = (Dv, G)
    print(f'\n=== kt = {kt} ===')
    for d in range(2, D+1):
        print(f' degree {d}:  D_parent = [{fmt(homog(Dv[0], d))}] , [{fmt(homog(Dv[1], d))}]')
        print(f'            D_child  = [{fmt(homog(Dv[2], d))}] , [{fmt(homog(Dv[3], d))}]')
        print(f'            G (graph defect) = [{fmt(homog(G[0], d))}] , [{fmt(homog(G[1], d))}]')
    lowG = min([deg(m) for p in G for m in p] or [None])
    print(f' first nonzero degree of the graph defect G: {lowG}')
# kt-dependence of G (affine): kappa-free part and kt-linear part
G1, G2 = results[Fr(1)][1], results[Fr(2)][1]
Glin = [padd(G2[i], G1[i], -1) for i in range(2)]; G0 = [padd(G1[i], Glin[i], -1) for i in range(2)]
print('\nG = G0 + kt*Glin:  G0 (kt-free) =', [fmt(p) for p in G0])
print('                   Glin          =', [fmt(p) for p in Glin])
print(f'\nidentity checks: {"ALL PASS" if ok_all else "FAILURES"}')
sys.exit(0 if ok_all else 1)
