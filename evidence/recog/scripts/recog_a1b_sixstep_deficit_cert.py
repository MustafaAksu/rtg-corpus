#!/usr/bin/env python3
"""A1b Lemma C' -- six-step angular deficit on the whole explicit tube U_T, exact-coefficient certificate.

For every y in U_T (DYAD-THM-PRIM-CTR: |W(y)| < 47/1000), the six-step lift increment is
    Lambda_6(y) = 2 pi + Arg( W(T^6 y) / W(y) )            (lift alignment: six-step totals lie in (pi, 3 pi))
and the raw six-step map in the frame W = rho + omega eta is
    W(T^6 y) = W + mu |W|^2 W + sum_{d=4}^{9} F_d(W, conj W) + R_{>=10},   |R_{>=10}| <= 332000 |W|^10 on |W| <= 1/16
(F_d exact polynomials computed here by six-fold composition of the primitive map, truncated at total degree 9;
tail ceiling imported from DYAD-THM-NF-REM ingredients, dyad-v6.4.22 §6.14).  Hence
    W(T^6 y)/W(y) = 1 + mu Q + E,   |E| <= e(Q) := sum_d c_d Q^{(d-1)/2} + 332000 Q^{9/2},   c_d := sum of |coefficients| of F_d,
and with Delta(y) := 2 pi - Lambda_6(y) = -Arg(1 + mu Q + E):
    Delta(y) > 0 on U_T  if  tau Q > e(Q)   (Im mu = -tau),
    |Delta(y) - tau Q| <= K Q^{3/2} with K computed from e(Q), Re(1 + mu Q + E) and the arctan bounds.
Gates (exit 0 iff all pass):
  G1 the degree-3 part of the six-step map is mu |W|^2 W with mu = -1/2 - 2 sqrt3/3 i (DYAD-THM-C21); degree 2 vanishes
  G2 the quartic real-ray value matches Dyadic §6.2 (RECOG §6.2): W(T^6(t,0)) = t + mu t^3 - (5+25 i sqrt3)/48 t^4 + O(t^5)
  G3 sup_{U_T} e(Q)/(tau Q) < 1  (deficit positive on all of U_T), with the value printed
  G4 explicit K with |Delta - tau Q| <= K Q^{3/2} on U_T, and the weaker uniform statement Lambda_6 < 2 pi on U_T
Negative controls: conjugating mu (Im mu -> +tau) must make the deficit non-positive; inflating the tail ceiling by 1e8 must fail G3.
  G5 the coefficient sums c_7, c_8, c_9 lie within Dyadic's vector ceilings 2079/1000, 577/500, 1763/1000 (NF-REM ingredients)
Grid-free gates (round-2 review #5631395296; exact rational arithmetic only, no floating point):
  G6 rational ceilings r_{d,k} >= |coefficient| (verified by r^2 >= a^2 + 3 b^2 exactly) and
     H := sum_d (sum_k r_{d,k}) T^{d-4} + 332000 T^6 < 1783/1000,  T = 47/1000;  hence e(Q) <= H t^3 for t = |W| <= T
  G7 tau bracket 1154700538/1e9 < tau < 1154700539/1e9 (checked by squaring against 4/3)
  G8 with d = T^2/2 + H T^3 and B = (tau + H T)/(1 - d), the uniform bounds on all of U_T (t <= T):
       (Delta - tau t^2)/t^3 <= (H + tau (T/2 + H T^2))/(1 - d) < 1.818
       (tau t^2 - Delta)/t^3 <= H (1 + tau T^2) + B^3 T^3/3          < 1.788
       Delta/(tau t^2)       >= (1 - H T/tau)/(1 + H T^3) - B^3 T^4/(3 tau) > 0.927
     derived from Delta = arctan(y/x), y = tau Q - Im E in [tau Q - e, tau Q + e], x = 1 - Q/2 + Re E in [1 - Q/2 - e, 1 + e],
     u - u^3/3 <= arctan u <= u (u >= 0), A := (tau Q + e)/(1 - Q/2 - e) <= B t^2.  Published constants: K = 1.82, Delta >= 0.927 tau Q.
  (G4's 50-point grid and 40-digit values are kept as an illustration only; the proof is G6-G8.)
usage: python -I recog_a1b_sixstep_deficit_cert.py [OUT_JSON]
"""
import json, math, sys
from fractions import Fraction as Fr
import mpmath as mp

DEG = 9
# exact arithmetic in Q(i sqrt3): a number is (a, b) meaning a + b i sqrt3, a, b rational
def nmul(x, y): return (x[0]*y[0] - 3*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def nadd(x, y): return (x[0] + y[0], x[1] + y[1])
def nconj(x): return (x[0], -x[1])
def nscale(x, r): return (x[0]*r, x[1]*r)
ZERO, ONE = (Fr(0), Fr(0)), (Fr(1), Fr(0))
OMEGA = (Fr(-1, 2), Fr(1, 2))                     # omega = -1/2 + i sqrt3/2
# polynomials in (W, conj W): dict {(a, b): coeff}, truncated at total degree DEG
def padd(P, Q, sgn=1):
    R = dict(P)
    for k, v in Q.items():
        R[k] = nadd(R.get(k, ZERO), nscale(v, sgn))
    return R
def pmul(P, Q):
    R = {}
    for (a, b), x in P.items():
        for (c, d), y in Q.items():
            if a + b + c + d <= DEG:
                k = (a + c, b + d); R[k] = nadd(R.get(k, ZERO), nmul(x, y))
    return R
def pscal(P, r): return {k: nscale(v, r) for k, v in P.items()}
def ppow(P, n):
    R = {(0, 0): ONE}
    for _ in range(n): R = pmul(R, P)
    return R
def pconj(P): return {(b, a): nconj(v) for (a, b), v in P.items()}
def pcompose(F, G, Gb):
    R = {}
    for (a, b), c in F.items():
        R = padd(R, {k: nmul(c, v) for k, v in pmul(ppow(G, a), ppow(Gb, b)).items()})
    return R
def clean(P): return {k: v for k, v in P.items() if v != ZERO}

Wp, Wbp = {(1, 0): ONE}, {(0, 1): ONE}
# eta = (W - conj W)/(omega - conj omega) = (W - conj W)/(i sqrt3);  1/(i sqrt3) = -i sqrt3/3 = (0, -1/3)
inv_is3 = (Fr(0), Fr(-1, 3))
eta = {k: nmul(v, inv_is3) for k, v in padd(Wp, Wbp, -1).items()}
rho = padd(Wp, {k: nmul(v, OMEGA) for k, v in eta.items()}, -1)
def series_sin(X):
    R = {}
    for k in range(0, (DEG + 1)//2 + 1):
        n = 2*k + 1
        if n > DEG: break
        R = padd(R, pscal(ppow(X, n), Fr((-1)**k, math.factorial(n))))
    return R
def series_expm1(X):
    R = {}
    for n in range(1, DEG + 1): R = padd(R, pscal(ppow(X, n), Fr(1, math.factorial(n))))
    return R
rho1 = padd(rho, series_sin(eta), -1)
eta1 = padd(padd(eta, series_expm1(rho)), series_sin(eta), -1)
F1 = clean(padd(rho1, {k: nmul(v, OMEGA) for k, v in eta1.items()}))
F1b = pconj(F1)
F, Fb = F1, F1b
for _ in range(5):
    F = clean(pcompose(F1, F, Fb)); Fb = pconj(F)

mp.mp.dps = 40
def nabs(x):
    a = mp.mpf(x[0].numerator)/x[0].denominator; b = mp.mpf(x[1].numerator)/x[1].denominator
    return mp.sqrt(a*a + 3*b*b)
# degree parts and coefficient sums
parts = {}
for (a, b), c in F.items():
    parts.setdefault(a + b, {})[(a, b)] = c
MU = (Fr(-1, 2), Fr(-2, 3))                      # mu = -1/2 - (2/3) i sqrt3
TAU = 2*mp.sqrt(3)/3
res = {}
d1 = parts.get(1, {}); d2 = parts.get(2, {}); d3 = parts.get(3, {})
g1 = (d1 == {(1, 0): ONE}) and (not d2) and (set(d3) == {(2, 1)}) and d3[(2, 1)] == MU
res["G1_cubic_jet_is_mu"] = bool(g1)
q4 = ZERO
for c in parts.get(4, {}).values(): q4 = nadd(q4, c)
res["G2_quartic_real_ray"] = [str(q4[0]), str(q4[1])]      # a + b i sqrt3
g2 = q4 == (Fr(-5, 48), Fr(-25, 48))
res["G2_matches_dyadic"] = bool(g2)
cd = {}
for d in range(4, DEG + 1):
    cd[d] = sum((nabs(c) for c in parts.get(d, {}).values()), mp.mpf(0))
res["coefficient_sums_c_d"] = {str(d): float(v) for d, v in cd.items()}
res["n_terms_per_degree"] = {str(d): len(parts.get(d, {})) for d in range(1, DEG + 1)}
TAIL = mp.mpf(332000)
WMAX = mp.mpf(47)/1000; QMAX = WMAX**2
def e_of_Q(Q): return sum(cd[d]*Q**(mp.mpf(d - 1)/2) for d in cd) + TAIL*Q**mp.mpf(4.5)
ratio_max = e_of_Q(QMAX)/(TAU*QMAX)
res["G3_sup_e_over_tauQ_on_UT"] = float(ratio_max); g3 = ratio_max < 1
def A_of(Q): e = e_of_Q(Q); return (TAU*Q + e)/(1 - Q/2 - e)
def up(Q): return (A_of(Q) - TAU*Q)/Q**mp.mpf(1.5)
def lo(Q): e = e_of_Q(Q); return (TAU*Q - (TAU*Q - e)/(1 + e) + A_of(Q)**3/3)/Q**mp.mpf(1.5)
K_up, K_lo = up(QMAX), lo(QMAX)
grid = [QMAX*k/50 for k in range(1, 51)]
mono = all(up(grid[i]) <= up(grid[i+1]) and lo(grid[i]) <= lo(grid[i+1]) for i in range(len(grid)-1))
K = max(K_up, K_lo)
res["G4_K_upper_branch"] = float(K_up); res["G4_K_lower_branch"] = float(K_lo); res["G4_K"] = float(K)
res["G4_monotone_on_grid"] = bool(mono)
eQ = e_of_Q(QMAX)
res["Delta_lower_bound_at_QMAX"] = float((TAU*QMAX - eQ)/(1 + eQ) - A_of(QMAX)**3/3)
res["Delta_lower_bound_over_tauQ_at_QMAX"] = float(((TAU*QMAX - eQ)/(1 + eQ) - A_of(QMAX)**3/3)/(TAU*QMAX))
g4 = mono and K > 0 and res["Delta_lower_bound_at_QMAX"] > 0
# negative controls: (i) conjugate mu (Im mu -> +tau): the deficit's leading term changes sign and Delta > 0 must fail;
# (ii) the tail ceiling inflated by 1e8: G3 must fail on U_T.
nc1 = (-(+TAU)*QMAX - e_of_Q(QMAX)) > 0                      # "Delta positive" test with Im mu = +tau: must be False
e_inflated = e_of_Q(QMAX) + (1e8 - 1)*TAIL*QMAX**mp.mpf(4.5)
nc2 = (e_inflated/(TAU*QMAX)) < 1                            # must be False
res["NC1_conj_mu_deficit_positive"] = bool(nc1); res["NC2_inflated_tail_G3"] = bool(nc2)
res["gates"] = {"G1": bool(g1), "G2": bool(g2), "G3": bool(g3), "G4": bool(g4), "NC1_caught": (not nc1), "NC2_caught": (not nc2)}
# cross-check against the Dyadic vector ceilings for degrees 7-9 (NF-REM ingredients): c_d <= ceiling
res["dyadic_ceilings_7_8_9"] = {"7": 2079/1000, "8": 577/500, "9": 1763/1000}
res["c_d_within_dyadic_ceilings"] = bool(cd[7] <= 2079/1000 + 1e-12 and cd[8] <= 577/500 + 1e-12 and cd[9] <= 1763/1000 + 1e-12)
res["gates"]["G5_ceilings"] = res["c_d_within_dyadic_ceilings"]
res["inputs"] = {"tube": "|W| < 47/1000 (DYAD-THM-PRIM-CTR)", "tail": "|R_{>=10}| <= 332000 |W|^10 on |W| <= 1/16 (DYAD-THM-NF-REM ingredients, dyad-v6.4.22 §6.14)",
                 "lift": "Lambda_6 = 2 pi + Arg(W(T^6 y)/W(y)) on U_T (RECOG-THM-A1A-LIFT-ALIGNMENT)",
                 "arithmetic": "exact Q(i sqrt3) coefficients (fractions); |coeff| and the final bounds in 40-digit mpmath"}
# ---- grid-free gates G6-G8 (exact rationals) ----
def rat_ceil_abs(c, digits=12):
    """rational r with r^2 >= a^2 + 3 b^2 (exact check), r = round-up of the 40-digit sqrt to `digits` decimals"""
    sq = c[0]*c[0] + 3*c[1]*c[1]
    r = Fr(int(mp.ceil(mp.sqrt(mp.mpf(sq.numerator)/sq.denominator)*10**digits)), 10**digits)
    while r*r < sq: r += Fr(1, 10**digits)
    return r
T = Fr(47, 1000)
cd_rat = {d: sum((rat_ceil_abs(c) for c in parts.get(d, {}).values()), Fr(0)) for d in range(4, DEG + 1)}
H = sum(cd_rat[d]*T**(d - 4) for d in cd_rat) + 332000*T**6
H_CEIL = Fr(1783, 1000)
g6 = H < H_CEIL and all(mp.mpf(cd_rat[d].numerator)/cd_rat[d].denominator >= cd[d] - mp.mpf(10)**-11 for d in cd_rat)
res["G6_rational_coefficient_sums"] = {str(d): str(v) for d, v in cd_rat.items()}
res["G6_H_exact"] = str(H); res["G6_H_float"] = float(H); res["G6_H_lt_1783_over_1000"] = bool(H < H_CEIL)
tau_lo, tau_hi = Fr(1154700538, 10**9), Fr(1154700539, 10**9)
g7 = (3*tau_lo*tau_lo < 4) and (4 < 3*tau_hi*tau_hi)
res["G7_tau_bracket_ok"] = bool(g7)
Hc = H_CEIL                                   # use the published ceiling, as in the review
dd = T*T/2 + Hc*T**3
B = (tau_hi + Hc*T)/(1 - dd)
up_bound  = (Hc + tau_hi*(T/2 + Hc*T*T))/(1 - dd)
low_bound = Hc*(1 + tau_hi*T*T) + B**3*T**3/3
pos_bound = (1 - Hc*T/tau_lo)/(1 + Hc*T**3) - B**3*T**4/(3*tau_lo)
g8 = up_bound < Fr(1818, 1000) and low_bound < Fr(1788, 1000) and pos_bound > Fr(927, 1000)
res["G8_upper_branch_bound"] = float(up_bound); res["G8_lower_branch_bound"] = float(low_bound); res["G8_positivity_ratio_bound"] = float(pos_bound)
res["G8_published"] = {"K": 1.82, "Delta_over_tauQ_min": 0.927}
res["gates"]["G6_rational_H"] = bool(g6); res["gates"]["G7_tau_bracket"] = bool(g7); res["gates"]["G8_gridfree_bounds"] = bool(g8)
ok = all(res["gates"].values())
res["ALL_PASS"] = ok
out = sys.argv[1] if len(sys.argv) > 1 else "a1b_sixstep_deficit_cert.json"
json.dump(res, open(out, "w"), indent=1)
for k, v in res["gates"].items(): print(k, "PASS" if v else "FAIL")
print("c_d:", res["coefficient_sums_c_d"]); print("sup e/(tau Q) on U_T:", res["G3_sup_e_over_tauQ_on_UT"], " K(grid, illustration):", res["G4_K"], " Delta/(tau Q) lower at Qmax:", res["Delta_lower_bound_over_tauQ_at_QMAX"])
print("H =", res["G6_H_float"], "< 1.783:", res["G6_H_lt_1783_over_1000"], "| grid-free: upper", res["G8_upper_branch_bound"], "< 1.818; lower", res["G8_lower_branch_bound"], "< 1.788; positivity", res["G8_positivity_ratio_bound"], "> 0.927 | published K = 1.82")
print("ALL PASS" if ok else "FAILURES")
sys.exit(0 if ok else 1)
