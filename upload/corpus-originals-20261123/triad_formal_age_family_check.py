#!/usr/bin/env python3
"""
Formal F-invariant age family with trivial clock  (Genesis->RER conditional analytic modal model, birth contract A).

Claim [ALG, formal]: at matched current parent s, the s-degree-d coefficient of the age-n child graph c_n(s)
is a polynomial in n of degree <= d-4.  Hence the sheets admit a unique interpolation C(s,tau) that is
polynomial in tau at each s-degree, and because F(s,c_n(s)) = (s+, c_{n+1}(s+)) for every integer n >= 0,
the identity theorem for polynomials gives, order by order in s,

        F( s, C(s,tau) ) = ( s+, C(s+, tau+1) )        for every real tau.

This script tests both statements on the untruncated full map (standard-library exact series, rev2 code):
  * degree bound: age-8 coefficients through t^11 are predicted by Lagrange interpolation of ages 0..7;
  * invariance at non-integer tau (1/2, -1/3, 5/2): zero child residual through t^NT on sampled rays.
Negative control (--negative): uses tau+ = tau + 1 + 1/10 ; must fail and exit 1.

Scope: formal only. Polynomial degree in tau grows with s-degree, so this is a formal family, not a convergent
or smooth 3-fold; all sheets still meet at the origin (C^1 obstruction theorem unchanged); no uniform-in-age
control, physical clock, memory variable or observable-preserving 2D factor is claimed.

Place the contributor's rev2 series file in ../source/ (SHA-256 67b2e0e7...799b).
"""
import sys, hashlib
from pathlib import Path
from fractions import Fraction as Fr
SERIES = Path(__file__).resolve().parent.parent / 'source' / 'c09_independent_series_check_rev2.py'
assert hashlib.sha256(SERIES.read_bytes()).hexdigest() == '67b2e0e785dd30a1bd637c79db2a7210d93516b79f5a00d5fb8233da04f6799b'
NEG = '--negative' in sys.argv
scope = {'__name__': '__probe__'}
exec(SERIES.read_text().split('# ---------------------------------------------------------------- checks')[0], scope)
NT = 12
scope['NT'] = NT
g = scope
ray, Fn, F, birth, initial_for_current_parent, sub, order = g['ray'], g['Fn'], g['F'], g['birth'], g['initial_for_current_parent'], g['sub'], g['order']

def lagrange_eval(xs, ys, x):
    tot = Fr(0)
    for i, (xi, yi) in enumerate(zip(xs, ys)):
        L = Fr(1)
        for j, xj in enumerate(xs):
            if j != i: L *= Fr(x - xj, xi - xj)
        tot += yi * L
    return tot

NAGES = 9   # tau-degree <= d-4 <= 8 at NT=12
def sheets(parent, kt):
    return [Fn(birth(initial_for_current_parent(parent, n, kt), kt), n)[1] for n in range(NAGES)]
def interp(cs, tau):
    ns = list(range(NAGES))
    return tuple([lagrange_eval(ns, [cs[n][i][k] for n in ns], tau) for k in range(NT + 1)] for i in range(2))

checks = []
def chk(name, ok):
    checks.append(ok); print(('PASS ' if ok else 'FAIL '), name)

SHIFT = Fr(1) + (Fr(1, 10) if NEG else 0)
for kt, u in [(Fr(1), (1, 0)), (Fr(1), (1, 1)), (Fr(-2, 3), (2, -1))]:
    tgt = ray(u); cs = sheets(tgt, kt)
    ok = True
    for k in range(5, NT):
        for i in range(2):
            ok &= lagrange_eval(list(range(8)), [cs[n][i][k] for n in range(8)], 8) == cs[8][i][k]
    chk(f'kt={kt} u={u}: age dependence polynomial of degree <= d-4 (age 8 predicted by ages 0..7 through t^{NT-1})', ok)
    for tau in [Fr(1, 2), Fr(-1, 3), Fr(5, 2)]:
        X = (tgt, interp(cs, tau)); Y = F(X)
        c_pred = interp(sheets(Y[0], kt), tau + SHIFT)
        res = [sub(Y[1][i], c_pred[i]) for i in range(2)]
        chk(f'kt={kt} u={u} tau={tau}: F(s,C(s,tau)) = (s+, C(s+, tau+{SHIFT})) through t^{NT}', order(res[0]) is None and order(res[1]) is None)
print(f'\n{sum(checks)} PASS, {len(checks) - sum(checks)} FAIL')
sys.exit(0 if all(checks) else 1)
