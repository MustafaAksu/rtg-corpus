#!/usr/bin/env python3
"""NUMGEN v1.21 stage 1 — exact symbolic check supporting one owner alias (disposition NC-13, verification gate).

Gate A1: the degree-5 radial part of the six-step return of the primitive map
    T(rho, eta) = (rho - sin eta, eta + exp(rho) - 1 - sin eta),   Q = rho^2 - rho*eta + eta^2,
computed here from T by exact Taylor composition, equals
  (a) NUMGEN v1.20.8 §6.2 L1:  Delta Q_5 = Q*(5 eta^3 - 43 eta^2 rho + 4 eta rho^2 - 5 rho^3)/24, and
  (b) DYAD v6.4.22 DYAD-ALG-P5-RADIAL: P_5 = (Q/24)(5 eta^3 - 43 eta^2 rho + 4 eta rho^2 - 5 rho^3);
and the degree-4 part equals -Q^2, degrees 2 and 3 vanish.
Exact rational arithmetic (sympy); no floating point. Exit 0 iff every assertion holds; --neg perturbs the
reference polynomial and must exit 1.
usage: numgen_v1_21_stage1_checks.py [--neg]
"""
import sys
import sympy as sp

r, e, t = sp.symbols("rho eta t")
N = 5  # total degree kept

def trunc(expr):
    """keep total degree <= N in (rho, eta), via the scaling variable t"""
    s = sp.expand(expr.subs({r: t * r, e: t * e}, simultaneous=True))
    s = sp.series(s, t, 0, N + 1).removeO()
    return sp.expand(s.subs(t, 1))

def series_T(R, E):
    sinE = sum((-1) ** k * E ** (2 * k + 1) / sp.factorial(2 * k + 1) for k in range(3))
    expR = sum(R ** k / sp.factorial(k) for k in range(N + 1))
    return trunc(R - sinE), trunc(E + expR - 1 - sinE)

def main(neg=False):
    R, E = r, e
    for _ in range(6):
        R, E = series_T(R, E)
    Q = lambda a, b: a ** 2 - a * b + b ** 2
    dQ = trunc(Q(R, E) - Q(r, e))
    poly = sp.Poly(dQ, r, e)
    parts = {d: sp.expand(sum(c * r ** i * e ** j for (i, j), c in poly.terms() if i + j == d)) for d in range(1, N + 1)}
    q = Q(r, e)
    ref5 = sp.expand(q * (5 * e ** 3 - 43 * e ** 2 * r + 4 * e * r ** 2 - 5 * r ** 3) / 24)
    if neg:
        ref5 = sp.expand(ref5 + q * e ** 3 / 24)
    gates = {
        "deg1-3 vanish": all(parts[d] == 0 for d in (1, 2, 3)),
        "deg4 = -Q^2": sp.expand(parts[4] + q ** 2) == 0,
        "deg5 = NUMGEN Delta Q_5 = DYAD P_5": sp.expand(parts[5] - ref5) == 0,
    }
    for k, v in gates.items():
        print(f"A1 {k}: {'PASS' if v else 'FAIL'}")
    print("degree-5 part:", sp.factor(parts[5]))
    ok = all(gates.values())
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main("--neg" in sys.argv))
