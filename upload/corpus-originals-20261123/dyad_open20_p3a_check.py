#!/usr/bin/env python3
"""DYAD OPEN 20 / O20-inf -- P3-a SESSION check script (v0.1).

Deterministic, exact (sympy rationals / Fractions). Light: runs in seconds.

Part J (cubic jet of F = T^6, raw (rho, eta) coordinates):
  J1  linear part of F is the identity
  J2  quadratic part of F vanishes
  J3  cubic part P3 of F is nonzero
  J4  3-jet of F^n equals id + n*P3 for n = 1..8   (=> |D^3 F^n(0)| = n |D^3 F(0)|)
  J5  DQ.P3 = -Q^2 with Q = r^2 - r e + e^2 (= |W|^2), i.e. Q(F w) = Q - Q^2 + O(|w|^5)
Part E (exponent bookkeeping of Lemmas A, B, C; alpha = c1/a, gamma = 2 alpha):
  E1  A_l = (2a+1)(l-1) + a   satisfies A_l >= a + 1 + max_{j>=2 partitions} sum A
  E2  B_l = (7a+1)(l-1) + 2a  satisfies B_l >= gamma + max_{j>=2}(A_j + sum B)
  E3  P_l = (7a+1)(l-1) + (l+2)a satisfies P_l >= max_{j>=1}(B_j + sum A)
  checked for l <= 12 and alpha in a fixed rational grid.
Negative controls (each must FAIL its gate; script exits 1 if a control passes):
  N1  J4 with n-independent cubic part (id + P3)
  N2  A_l with slope 2a      (missing +1)
  N3  B_l with slope 7a      (missing +1)
  N4  P_l with (l+1)a        (one alpha short)
Exit code 0 iff all gates pass and all negative controls fail.
"""
import sys, json, hashlib
from fractions import Fraction as Fr
import sympy as sp

r, e = sp.symbols('r e')
DEG = 3

def trunc(expr):
    p = sp.Poly(sp.expand(expr), r, e)
    return sp.Add(*[c * r**i * e**j for (i, j), c in p.terms() if i + j <= DEG])

def compose(f, g):
    """f∘g for truncated 2-vectors of polynomials."""
    return tuple(trunc(fi.subs({r: g[0], e: g[1]}, simultaneous=True)) for fi in f)

# Taylor jets of T(r,e) = (r - sin e, e + e^r - 1 - sin e) to degree 3
sin_e = e - e**3 / 6
exp_r1 = r + r**2 / 2 + r**3 / 6
T = (trunc(r - sin_e), trunc(e + exp_r1 - sin_e))

F = (r, e)
for _ in range(6):
    F = compose(T, F)

def part(expr, d):
    p = sp.Poly(sp.expand(expr), r, e)
    return sp.Add(*[c * r**i * e**j for (i, j), c in p.terms() if i + j == d])

lin = tuple(part(c, 1) for c in F)
quad = tuple(part(c, 2) for c in F)
P3 = tuple(part(c, 3) for c in F)

res = {}
res['J1'] = sp.simplify(lin[0] - r) == 0 and sp.simplify(lin[1] - e) == 0
res['J2'] = all(sp.expand(q) == 0 for q in quad)
res['J3'] = any(sp.expand(p) != 0 for p in P3)

def jet_power(n):
    G = (r, e)
    for _ in range(n):
        G = compose(F, G)
    return G

ok4, neg1_pass = True, True
for n in range(1, 9):
    Gn = jet_power(n)
    pred = (r + n * P3[0], e + n * P3[1])
    wrong = (r + P3[0], e + P3[1])
    ok4 &= all(sp.expand(Gn[i] - pred[i]) == 0 for i in range(2))
    if n >= 2:
        neg1_pass &= all(sp.expand(Gn[i] - wrong[i]) == 0 for i in range(2))
res['J4'] = ok4
Qr = r**2 - r*e + e**2
res['J5'] = sp.expand(sp.diff(Qr, r) * P3[0] + sp.diff(Qr, e) * P3[1] + Qr**2) == 0

# ---- exponent bookkeeping ----
def partitions(l, jmin):
    """integer partitions of l into >= jmin parts (multisets of block sizes)."""
    out = []
    def rec(rem, maxp, acc):
        if rem == 0:
            if len(acc) >= jmin:
                out.append(tuple(acc))
            return
        for p in range(min(rem, maxp), 0, -1):
            rec(rem - p, p, acc + [p])
    rec(l, l, [])
    return out

L = 12
alphas = [Fr(k, 8) for k in range(0, 33)] + [Fr(1, 1000), Fr(17, 3)]

def gateA(alpha, slope):
    A = lambda l: slope * (l - 1) + alpha
    return all(A(l) >= alpha + 1 + max(sum(A(m) for m in p) for p in partitions(l, 2))
               for l in range(2, L + 1))

def gateB(alpha, slope):
    g = 2 * alpha
    A = lambda l: (2 * alpha + 1) * (l - 1) + alpha
    B = lambda l: slope * (l - 1) + g
    return all(B(l) >= g + max(A(len(p)) + sum(B(m) for m in p) for p in partitions(l, 2))
               for l in range(2, L + 1))

def gateP(alpha, const):
    A = lambda l: (2 * alpha + 1) * (l - 1) + alpha
    B = lambda l: (7 * alpha + 1) * (l - 1) + 2 * alpha
    P = lambda l: (7 * alpha + 1) * (l - 1) + (l + const) * alpha
    return all(P(l) >= max(B(len(p)) + sum(A(m) for m in p) for p in partitions(l, 1))
               for l in range(1, L + 1))

res['E1'] = all(gateA(al, 2 * al + 1) for al in alphas)
res['E2'] = all(gateB(al, 7 * al + 1) for al in alphas)
res['E3'] = all(gateP(al, 2) for al in alphas)

pos = [al for al in alphas if al > 0]
neg = {
    'N1': neg1_pass,
    'N2': all(gateA(al, 2 * al) for al in alphas),
    'N3': all(gateB(al, 7 * al) for al in pos),
    'N4': all(gateP(al, 1) for al in pos),
}

out = {
    'P3_rho': str(sp.factor(P3[0])), 'P3_eta': str(sp.factor(P3[1])),
    'gates': {k: bool(v) for k, v in res.items()},
    'negative_controls_pass_should_be_false': {k: bool(v) for k, v in neg.items()},
}
txt = json.dumps(out, indent=2, sort_keys=True)
print(txt)
with open('p3a_check.json', 'w', encoding='utf-8') as fh:
    fh.write(txt + '\n')
good = all(res.values()) and not any(neg.values())
print('RESULT:', 'PASS' if good else 'FAIL')
sys.exit(0 if good else 1)
