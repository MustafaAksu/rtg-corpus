#!/usr/bin/env python3
"""recog_a1c_jet_remainder_bounds_cert.py -- certificate for RECOG-ALG-A1C-JET-REMAINDER-BOUNDS (RECOG v0.3.27, R2 of the inbox round).

Statement.  In the chart of DYAD-ALG-NF6 / DYAD-THM-NF-REM, for 0 < q = |z|^2 <= q* = 256/140625 (< 1/400, so |z| < 1/20: row A),
    |Arg(J(z)/z) + tau q| <= c_J q^2,   c_J = 0.500819,        |Arg(Fhat(z)/J(z))| <= c_7 q^3,   c_7 = 100.231,
with J the degree-6 jet of DYAD-ALG-NF6 and C_7 = 100 of DYAD-THM-NF-REM (row |z| <= 1/20).  Consequently the two remainder constants
of the DYAD-THM-LPHASE-ROWA-REMAINDER proof sketch used by RECOG's part-1b closed forms, c_J = 0.50220 and c_7 = 157.58, are valid
ceilings on q <= q*.  Dependencies: DYAD-ALG-NF6, DYAD-THM-NF-REM only (no RECOG A1c result; no (D5) constant).

Proof.  J(z)/z = 1 + u, u = mu q + v5, v5 = (a32 + a05 e^{-6 i Theta}) q^2, |v5| <= A5 q^2, A5 = |a32| + |a05|; |u| <= u(q) := |mu| q + A5 q^2 < 1.
 (J) Arg(1+u) = Im u - Im(u^2)/2 + R3, |R3| <= |u|^3/(3(1-|u|)) (log series).  Im mu = -tau, so
     Arg(J/z) + tau q = [Im a32 - Im(mu^2)/2] q^2 + Im(a05 e^{-6i Theta}) q^2 - Im(mu v5) q - Im(v5^2)/2 + R3,
     Im a32 - Im(mu^2)/2 = 197 sqrt3/324 - sqrt3/3 = 89 sqrt3/324, hence |...|/q^2 <= c_J(q) :=
     89 sqrt3/324 + |a05| + |mu| A5 q + A5^2 q^2/2 + u(q)^3/(3(1-u(q)) q^2).
 (7) Fhat = J + R_7, |R_7| <= C_7 |z|^7; |J| >= |z|(1-u(q)); w := C_7 q^3/(1-u(q)) < 1; |Arg(1+x)| <= |x|/(1-|x|) for |x| < 1, so
     |Arg(Fhat/J)|/q^3 <= c_7(q) := C_7/((1-u(q))(1-w)).
 Both majorants are increasing in q (every term is; u(q)^3/q^2 = q(|mu| + A5 q)^3), so their suprema on (0, q*] are the values at q*.
 These are the majorants computed by recog_a1c_combined_tail_cert.py (cJ_R, c7_R; L78-84) for RECOG-ALG-A1C-COMBINED-TAIL; this
 certificate states them as a source-independent lemma with outward displays.
Gates.  G1 exact rationals (Fraction only): sufficient rational enclosures of sqrt3, |mu|, |a32|, |a05| by squared comparisons
        (|mu|^2 = 19/12, |a32|^2 = (97/432)^2 + 3(197/324)^2, |a05|^2 = (49/8640)^2 + 3(307/25920)^2); then c_J(q*) < 0.500819 < 0.50220
        and c_7(q*) < 100.231 < 157.58, with u(q*) < 1, w < 1, q* < 1/400.  (Rational bounds from the co-owner reconciliation script
        evidence/recog/inbox_reconciliation_20261103/recog_r2_rational_bounds.py, PR #172, re-stated here as the owner certificate.)
        G2 interval arithmetic (mpmath iv, 40 digits): the same majorants at q*, with the enclosure inside the rational bounds.
        G3 monotonicity on a q-grid (10^-9 .. q*) for both majorants (illustration of the analytic argument above).
        G4 identity: 89 sqrt3/324 = Im a32 - Im(mu^2)/2 (sympy).
Negative controls.  NC1 the v0.3.25 display 100.23 is refused as a ceiling (the majorant at q* exceeds it); NC2 a wrong sign in
        Im(mu^2)/2 (Im a32 + Im(mu^2)/2) gives a constant above 0.50220 (the identity matters).
usage (repository root): python -I evidence/recog/scripts/recog_a1c_jet_remainder_bounds_cert.py evidence/recog/a1c_jet/a1c_jet_remainder_bounds_cert.json
"""
import json, sys
from fractions import Fraction as F
from mpmath import iv, mp
import sympy as sp

res = {"gates": {}}
q = F(256, 140625)
# ---- G1 exact rationals ----
s3_hi = F(1732051, 1000000)
mu_lo, mu_hi = F(12583, 10000), F(1259, 1000)
a32_lo, a32_hi = F(10768, 10000), F(1077, 1000)
a05_lo, a05_hi = F(2128, 100000), F(213, 10000)
mu2, a32_2, a05_2 = F(19, 12), F(97, 432)**2 + 3*F(197, 324)**2, F(49, 8640)**2 + 3*F(307, 25920)**2
encl = s3_hi**2 > 3 and mu_lo**2 < mu2 < mu_hi**2 and a32_lo**2 < a32_2 < a32_hi**2 and a05_lo**2 < a05_2 < a05_hi**2
A5_lo, A5_hi = a32_lo + a05_lo, a32_hi + a05_hi
def c7_of(u, C7=F(100)):
    w = C7*q**3/(1 - u); return F(C7)/(1 - u)/(1 - w), w
u_lo, u_hi = mu_lo*q + A5_lo*q*q, mu_hi*q + A5_hi*q*q
c7_lo, w_lo = c7_of(u_lo); c7_hi, w_hi = c7_of(u_hi)
cJ_hi = F(89, 324)*s3_hi + a05_hi + mu_hi*A5_hi*q + A5_hi**2*q**2/2 + u_hi**3/(3*(1 - u_hi)*q*q)
g1 = encl and u_hi < 1 and w_hi < 1 and q < F(1, 400) and cJ_hi < F(500819, 1000000) < F(50220, 100000) and c7_hi < F(100231, 1000) < F(15758, 100)
res["G1_exact_rational"] = {"enclosures_ok": encl, "q_star": "256/140625", "q_star_below_1/400": q < F(1, 400), "u_upper": float(u_hi), "w_upper": float(w_hi),
                            "cJ_upper_rational": str(cJ_hi), "cJ_upper_float": float(cJ_hi), "c7_lower_float": float(c7_lo), "c7_upper_float": float(c7_hi),
                            "cJ < 0.500819": cJ_hi < F(500819, 1000000), "c7 < 100.231": c7_hi < F(100231, 1000),
                            "0.500819 <= 0.50220 (part-1b c_J)": True, "100.231 <= 157.58 (part-1b c_7)": True}
res["gates"]["G1_exact_rational"] = bool(g1)
# ---- G2 interval arithmetic ----
iv.dps = 40; I = iv.mpf
s3 = iv.sqrt(I(3)); tau = 2*s3/3
mu = (I(-1)/2, -2*s3/3); a32 = (I(-97)/432, 197*s3/324); a05 = (I(-49)/8640, -307*s3/25920)
absv = lambda z: iv.sqrt(z[0]**2 + z[1]**2)
abs_mu, abs_a32, abs_a05 = absv(mu), absv(a32), absv(a05); A5 = abs_a32 + abs_a05
def cJ(qq):
    uu = abs_mu*qq + A5*qq**2
    return abs(a32[1] - tau/2) + abs_a05 + abs_mu*A5*qq + A5**2*qq**2/2 + uu**3/(3*(1 - uu))/qq**2
def c7(qq, C7=I(100)):
    uu = abs_mu*qq + A5*qq**2; w = C7*qq**3/(1 - uu); return C7/(1 - uu)/(1 - w)
qs = I(256)/140625
cJ_iv, c7_iv = cJ(qs), c7(qs)
g2 = float(cJ_iv.b) <= float(cJ_hi) and float(c7_lo) <= float(c7_iv.a) and float(c7_iv.b) <= float(c7_hi)
res["G2_interval"] = {"cJ(q*)": [float(cJ_iv.a), float(cJ_iv.b)], "c7(q*)": [float(c7_iv.a), float(c7_iv.b)], "inside_rational_bounds": bool(g2)}
res["gates"]["G2_interval"] = bool(g2)
# ---- G3 monotonicity (illustration of the analytic argument) ----
grid = [I(10)**(-k) for k in range(9, 2, -1)] + [qs]
vJ = [float(cJ(x).b) for x in grid]; v7 = [float(c7(x).b) for x in grid]
g3 = all(vJ[i] <= vJ[i + 1] for i in range(len(vJ) - 1)) and all(v7[i] <= v7[i + 1] for i in range(len(v7) - 1))
res["G3_monotone_grid"] = {"cJ": vJ, "c7": v7}; res["gates"]["G3_monotone"] = bool(g3)
# ---- G4 identity ----
X = sp.sqrt(3); muS = -sp.Rational(1, 2) - sp.I*2*X/3
g4 = sp.simplify(sp.im(sp.expand(muS**2))/2 - X/3) == 0 and sp.simplify(197*X/324 - X/3 - 89*X/324) == 0
res["gates"]["G4_identity_89sqrt3_over_324"] = bool(g4)
# ---- negative controls ----
nc1 = not (c7_lo <= F(10023, 100))                  # 100.23 refused: the majorant's lower end exceeds it
cJ_wrong = F(197 + 108, 324)*s3_hi                   # Im a32 + Im(mu^2)/2 (wrong sign) alone
nc2 = cJ_wrong > F(50220, 100000)
res["NC1_100.23_refused"] = bool(nc1); res["NC2_wrong_sign_exceeds_0.50220"] = bool(nc2)
res["gates"]["NC1"] = bool(nc1); res["gates"]["NC2"] = bool(nc2)
res["ALL_PASS"] = all(res["gates"].values())
if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "a1c_jet_remainder_bounds_cert.json"
    json.dump(res, open(out, "w"), indent=1)
    for k, v in res["gates"].items(): print(k, "PASS" if v else "FAIL")
    print("c_J(q*) <", float(cJ_hi), " c_7(q*) in [", float(c7_lo), ",", float(c7_hi), "]")
    print("ALL PASS" if res["ALL_PASS"] else "FAILURES"); sys.exit(0 if res["ALL_PASS"] else 1)
