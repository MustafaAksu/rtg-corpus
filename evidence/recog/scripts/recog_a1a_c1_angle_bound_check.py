#!/usr/bin/env python3
"""recog_a1a_c1_angle_bound_check.py -- exact check of Lemma C1 (A1a v0.2 §3.1). Exit 0 = all gates PASS.

Gates
 G1 identity   W(Tx) - lambda W = lambda(eta - sin eta) + omega(e^rho - 1 - rho), exactly (symbolic, omega^2 = -1 - omega)
 G2 frame      Q = (rho - eta/2)^2 + (3/4) eta^2 = (eta - rho/2)^2 + (3/4) rho^2, so |rho|,|eta| <= (2/sqrt3)|W| < 2|W|
 G3 exp bound  2R < ln 2 for R = 47/1000 (via a rational lower bound of ln 2), hence e^{|rho|} < 2 on the tube
 G4 ceiling    with |eta - sin eta| <= |eta|^3/6 <= (4/3)|W|^3 and |e^rho - 1 - rho| <= e^{|rho|} rho^2/2 < 4|W|^2:
               |W(Tx)/(lambda W) - 1| <= 4|W| + (4/3)|W|^2 < 4R + (4/3)R^2 = 143209/750000 < 1/2   (exact rationals)
 G5 angle      |Arg(1+eps)| <= arcsin|eps| < arcsin(1/2) = pi/6 for |eps| < 1/2, hence pi/6 < delta_T < pi/2,
               and six-step totals lie in (pi, 3pi)
 G6 taylor     the two scalar remainder inequalities hold on the needed ranges (exact series argument restated + dense check)
Negative controls (each must FAIL its gate): NC1 R = 1/5; NC2 identity with lambda factor dropped; NC3 1/2 replaced by 1/10.
"""
import sys
from fractions import Fraction as F
import sympy as sp

def gates(R=F(47, 1000), drop_lambda=False, eps_max=F(1, 2)):
    res = {}
    r, e = sp.symbols("rho eta", real=True)
    w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
    lam = 1 + w
    W = lambda a, b: a + w * b
    rT, eT = r - sp.sin(e), e + sp.exp(r) - 1 - sp.sin(e)
    rhs = (1 if drop_lambda else lam) * (e - sp.sin(e)) + w * (sp.exp(r) - 1 - r)
    res["G1"] = sp.simplify(sp.expand(W(rT, eT) - lam * W(r, e) - rhs)) == 0
    Q = r**2 - r*e + e**2
    res["G2"] = (sp.expand((r - e/2)**2 + sp.Rational(3, 4)*e**2 - Q) == 0 and
                 sp.expand((e - r/2)**2 + sp.Rational(3, 4)*r**2 - Q) == 0)
    # ln 2 > 0.6931 (alternating series of ln(1+1) is slow; use ln2 = sum 1/(k 2^k), all terms positive -> partial sum is a lower bound)
    ln2_lo = sum(F(1, k * 2**k) for k in range(1, 30))
    res["G3"] = 2 * R < ln2_lo
    ceil = 4 * R + F(4, 3) * R * R
    res["G4"] = ceil < eps_max and (R != F(47, 1000) or ceil == F(143209, 750000))
    # arcsin(1/2) = pi/6 exactly; the Arg bound needs eps_max <= 1/2
    res["G5"] = eps_max <= F(1, 2) and sp.asin(sp.Rational(1, 2)) == sp.pi / 6 and ceil < eps_max
    # G6: |x - sin x| <= |x|^3/6 (alternating Taylor series) and |e^x-1-x| <= e^|x| x^2/2 (termwise k! >= 2 (k-2)!), dense check
    ok = True
    for k in range(-1000, 1001):
        x = 2 * float(R) * k / 1000
        if abs(x - __import__("math").sin(x)) > abs(x)**3 / 6 + 1e-18: ok = False
        if abs(__import__("math").expm1(x) - x) > __import__("math").exp(abs(x)) * x * x / 2 + 1e-18: ok = False
    res["G6"] = ok
    return res

def main():
    g = gates()
    for k, v in g.items(): print(f"  {k} {'PASS' if v else 'FAIL'}")
    print("  ceiling =", 4*F(47,1000) + F(4,3)*F(47,1000)**2)
    nc = {"NC1 R=1/5 (G4)": not gates(R=F(1, 5))["G4"],
          "NC2 lambda dropped (G1)": not gates(drop_lambda=True)["G1"],
          "NC3 eps bound 1/10 (G4)": not gates(eps_max=F(1, 10))["G4"]}
    for k, v in nc.items(): print(f"  {k:<26} {'caught' if v else 'NOT CAUGHT'}")
    ok = all(g.values()) and all(nc.values())
    print("RESULT:", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)

if __name__ == "__main__": main()
