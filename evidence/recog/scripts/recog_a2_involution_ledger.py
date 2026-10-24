#!/usr/bin/env python3
"""A2 -- typed involution ledger: exact formal checks (truncated at total degree N, rational arithmetic).

Lifted primitive chart x = (rho, eta); T(rho, eta) = (rho - sin eta, eta + e^rho - 1 - sin eta); A = DT(0) = [[1,-1],[1,0]],
A^3 = -I. Character family T_k = (rho - sin eta, eta + g_k(e^rho) - sin eta), g_k(r) = (r^k - 1)/k (T_1 = T; T_0 the log
twin); symmetric twin T_s = (rho - sin eta, eta + sinh rho - sin eta) (= T with the even part T_b = (0, cosh rho - 1) removed).
S_o = -I (exact linear state swap). R_0 = T^3 o F^{-1/2}, F = T^6 (Dyadic's formal involution, DYAD-THM-FORMAL-INVOLUTION-UNIQUE),
computed here from scratch: F^{-1} and its unique tangent-to-identity square root degree by degree.

Gates (exit 0 iff all pass):
  G1  A^3 = -I; F = T^6 is tangent to the identity with no degree-2 term; its cubic part in the W-frame is mu |W|^2 W,
      mu = -1/2 - (2 sqrt3/3) i (DYAD-THM-C21) -- checked exactly in Q(sqrt3) with sympy.
  G2  K := F^{-1/2}: K o K o F = id to degree N (unique tangent-to-identity root).
  G3  R_0 := T^3 o K: R_0 o R_0 = id, R_0 o T = T o R_0, DR_0(0) = -I, R_0 != -I (degree-2 part nonzero);
      the degree-2 part r_2 solves r_2(Ax) - A r_2(x) = 2 T_2(x), T_2 = (0, rho^2/2) (even part of T);
      on the real W-ray, [R_0]_2(t,0) = (-t^2, -t^2/2) in (rho, eta), i.e. W' = -t + 2 c t^2 with c = -(3 + i sqrt3)/8
      (2c = -(3 + i sqrt3)/4 = j^2 S_h of RECOG-ALG-SH-SECTION-SHADOW, from Dyadic's h_2: [R_0]_2 = 2 h_2).
  G4  symmetric twin: R_0^{(s)} = -I = S_o exactly to degree N (T_s odd); log twin T_0: R_0^{(0)} = -I as well (T_0 odd).
  G5  orientation: Phi := S_o o R_0^{(1)} is tangent to the identity and Phi o T_1 o Phi^{-1} = T_{-1} to degree N;
      R_0^{(-1)} = S_o o R_0^{(1)} o S_o; S_o o T_1 o S_o = T_{-1} exactly (polynomial identity).
  G6  no selective power: for a perturbed germ T~ = T + (quadratic, cubic rational terms) with DT~(0) = A, the same
      construction gives an involution with linear part -I commuting with T~ (existence needs only A^3 = -I).
  G7  S_o-equivariance defect of T: T o S_o - S_o o T = (0, 2(cosh rho - 1)) (quadratic; T_b); for T_s the defect is 0.
  G8  wrapped inversion: zeta = e^{rho + i eta}, zeta^{-1} = e^{-rho - i eta}: the inversion of the RRF wrapped native ratio
      is S_o on the lift (symbolic identity); action table on observables: rho -> -rho, C_pole -> C_pole^{-1}, Q -> Q,
      C_->(a,b) = conj(W_a) W_b -> itself under S_o on both states (W -> -W).
Negative controls:
  NC1 a germ with A'^3 = +I (A' = rotation by 2 pi/3): the construction returns a tangent-to-identity involution, hence the
      identity -- the "linear part -I" gate must fail.
  NC2 root factor 1/3 instead of 1/2 (R' = T^3 o F^{-1/3}): R' o R' != id must be detected.
  NC3 claiming S_o o T o S_o = T must fail (T is not S_o-symmetric).
usage: python -I recog_a2_involution_ledger.py [OUT_JSON]
"""
import json, math, sys
from fractions import Fraction as Fr

N = 8  # truncation degree

# ---------- truncated bivariate polynomials over Q: dict {(i,j): Fr} meaning sum c rho^i eta^j ----------
def padd(P, Q, s=1):
    R = dict(P)
    for k, v in Q.items():
        R[k] = R.get(k, Fr(0)) + s*v
    return {k: v for k, v in R.items() if v != 0}
def pmul(P, Q):
    R = {}
    for (a, b), x in P.items():
        for (c, d), y in Q.items():
            if a + b + c + d <= N:
                R[(a + c, b + d)] = R.get((a + c, b + d), Fr(0)) + x*y
    return {k: v for k, v in R.items() if v != 0}
def pscal(P, r): return {k: v*r for k, v in P.items()} if r else {}
def ppow_table(P):
    T = [{(0, 0): Fr(1)}]
    for _ in range(N): T.append(pmul(T[-1], P))
    return T
def pcompose(P, X, Y):
    """P(x, y) with x := X, y := Y (polynomials)."""
    PX, PY = ppow_table(X), ppow_table(Y)
    R = {}
    for (i, j), c in P.items():
        if i + j <= N:
            R = padd(R, pscal(pmul(PX[i], PY[j]), c))
    return R
def mcompose(P, Q):
    """map composition P o Q for maps = pairs of polynomials."""
    return (pcompose(P[0], Q[0], Q[1]), pcompose(P[1], Q[0], Q[1]))
def madd(P, Q, s=1): return (padd(P[0], Q[0], s), padd(P[1], Q[1], s))
def mscal(P, r): return (pscal(P[0], r), pscal(P[1], r))
def mdeg(P, d): return ({k: v for k, v in P[0].items() if sum(k) == d}, {k: v for k, v in P[1].items() if sum(k) == d})
def mtrunc(P, d): return ({k: v for k, v in P[0].items() if sum(k) <= d}, {k: v for k, v in P[1].items() if sum(k) <= d})
def miszero(P): return not P[0] and not P[1]
def meq(P, Q): return miszero(madd(P, Q, -1))
RHO, ETA = {(1, 0): Fr(1)}, {(0, 1): Fr(1)}
ID = (RHO, ETA)
MINUS_ID = (pscal(RHO, -1), pscal(ETA, -1))
def series(coeffs):  # dict {n: c} of a univariate series in one variable, as polynomial in that variable
    return coeffs
def sin_p(X):  # X polynomial
    PX = ppow_table(X); R = {}
    for n in range(1, N + 1, 2): R = padd(R, pscal(PX[n], Fr((-1)**((n - 1)//2), math.factorial(n))))
    return R
def expm1_k(X, k):  # (e^{kX} - 1)/k, k rational nonzero; k = 0 -> X
    PX = ppow_table(X); R = {}
    for n in range(1, N + 1):
        R = padd(R, pscal(PX[n], Fr(1, math.factorial(n)) * (k**(n - 1) if k != 0 else (1 if n == 1 else 0))))
    return R
def sinh_p(X):
    PX = ppow_table(X); R = {}
    for n in range(1, N + 1, 2): R = padd(R, pscal(PX[n], Fr(1, math.factorial(n))))
    return R
def coshm1_p(X):
    PX = ppow_table(X); R = {}
    for n in range(2, N + 1, 2): R = padd(R, pscal(PX[n], Fr(1, math.factorial(n))))
    return R

def T_k(k):
    return (padd(RHO, sin_p(ETA), -1), padd(padd(ETA, expm1_k(RHO, Fr(k))), sin_p(ETA), -1))
T = T_k(1)
T_s = (padd(RHO, sin_p(ETA), -1), padd(padd(ETA, sinh_p(RHO)), sin_p(ETA), -1))

def iterate(P, n):
    R = ID
    for _ in range(n): R = mcompose(P, R)
    return R
def minverse(F):
    """inverse of a map with invertible linear part L: G = L^{-1} o (id + ...) solved degree by degree."""
    L = mdeg(F, 1)
    # linear inverse
    a, b = L[0].get((1, 0), Fr(0)), L[0].get((0, 1), Fr(0)); c, d = L[1].get((1, 0), Fr(0)), L[1].get((0, 1), Fr(0))
    det = a*d - b*c; assert det != 0
    Linv = ({(1, 0): d/det, (0, 1): -b/det}, {(1, 0): -c/det, (0, 1): a/det})
    G = Linv
    for deg in range(2, N + 1):
        E = mtrunc(madd(mcompose(F, G), ID, -1), deg)      # F o G - id, correct below deg
        # correction: G <- G - Linv o E_deg
        corr = mcompose(Linv, mdeg(E, deg))
        G = madd(G, corr, -1)
    assert miszero(mtrunc(madd(mcompose(F, G), ID, -1), N)), "inverse failed"
    return G
def sqrt_tangent(F):
    """unique tangent-to-identity H with H o H = F (F tangent to identity)."""
    assert meq(mdeg(F, 1), ID), "F is not tangent to the identity"
    H = ID
    for deg in range(2, N + 1):
        E = mdeg(madd(mcompose(H, H), F, -1), deg)         # (H o H - F)_deg with h_deg = 0 so far: equals lower-terms - F_deg
        H = madd(H, mscal(E, Fr(-1, 2)))                   # h_deg = (F_deg - lower)/2
    assert miszero(mtrunc(madd(mcompose(H, H), F, -1), N)), "square root failed"
    return H
def R0_of(Tm, root=Fr(1, 2)):
    F = iterate(Tm, 6)
    Finv = minverse(F)
    if root == Fr(1, 2):
        K = sqrt_tangent(Finv)
    else:  # NC2: cube root of F^{-1} (generic degree-by-degree root solver for exponent 3)
        K = ID
        for deg in range(2, N + 1):
            E = mdeg(madd(iterate(K, 3), Finv, -1), deg); K = madd(K, mscal(E, Fr(-1, 3)))
    return mcompose(iterate(Tm, 3), K), F, K

res = {"N": N}
# ---- G1 ----
A = mdeg(T, 1)
A3 = mcompose(A, mcompose(A, A))
F = iterate(T, 6)
g1 = meq(A3, MINUS_ID) and meq(mdeg(F, 1), ID) and miszero(mdeg(F, 2))
# cubic part in the W-frame with sympy (exact Q(sqrt3))
import sympy as sp
r, e = sp.symbols('rho eta', real=True)
def topoly(P): return sum(sp.Rational(v.numerator, v.denominator)*r**i*e**j for (i, j), v in P.items())
F3 = mdeg(F, 3)
w = sp.Rational(-1, 2) + sp.I*sp.sqrt(3)/2
W = r + w*e
mu = sp.Rational(-1, 2) - sp.I*2*sp.sqrt(3)/3
cubic_W = sp.expand(topoly(F3[0]) + w*topoly(F3[1]))
target = sp.expand(mu*W*sp.conjugate(W)*W)
g1 &= sp.simplify(cubic_W - target) == 0
res["G1"] = {"A3_is_minus_I": meq(A3, MINUS_ID), "F_tangent_identity_no_deg2": meq(mdeg(F, 1), ID) and miszero(mdeg(F, 2)), "cubic_part_is_mu_W2W": bool(sp.simplify(cubic_W - target) == 0)}
# ---- G2, G3 ----
R0, F, K = R0_of(T)
g2 = miszero(mtrunc(madd(mcompose(mcompose(K, K), F), ID, -1), N))
r2 = mdeg(R0, 2)
T2 = mdeg(T, 2)
lhs = madd(mcompose(r2, A), mcompose(A, r2), -1)
g3 = (miszero(mtrunc(madd(mcompose(R0, R0), ID, -1), N)) and miszero(mtrunc(madd(mcompose(R0, T), mcompose(T, R0), -1), N))
      and meq(mdeg(R0, 1), MINUS_ID) and not miszero(r2) and meq(mtrunc(lhs, 2), mscal(T2, 2)))
ray = (r2[0].get((2, 0), Fr(0)), r2[1].get((2, 0), Fr(0)))
g3 &= ray == (Fr(-1), Fr(-1, 2))
res["G2_K_is_F_minus_half"] = bool(g2)
res["G3"] = {"R0_involution": miszero(mtrunc(madd(mcompose(R0, R0), ID, -1), N)), "R0_commutes_T": miszero(mtrunc(madd(mcompose(R0, T), mcompose(T, R0), -1), N)),
             "DR0_minus_I": meq(mdeg(R0, 1), MINUS_ID), "R0_not_minus_I": not miszero(r2),
             "r2_homological_equation": meq(mtrunc(lhs, 2), mscal(T2, 2)),
             "r2": {"rho": {f"{i},{j}": str(v) for (i, j), v in r2[0].items()}, "eta": {f"{i},{j}": str(v) for (i, j), v in r2[1].items()}},
             "real_ray_deg2": [str(ray[0]), str(ray[1])], "matches_j2_Sh": ray == (Fr(-1), Fr(-1, 2)), "W_frame_value": "-1 + omega*(-1/2) = -(3 + i sqrt3)/4 = 2c"}
# ---- G4 ----
R0s, _, _ = R0_of(T_s)
R00, _, _ = R0_of(T_k(0))
g4 = meq(mtrunc(R0s, N), MINUS_ID) and meq(mtrunc(R00, N), MINUS_ID)
res["G4"] = {"R0_symmetric_twin_is_minus_I": meq(mtrunc(R0s, N), MINUS_ID), "R0_log_twin_is_minus_I": meq(mtrunc(R00, N), MINUS_ID)}
# ---- G5 ----
Tm1 = T_k(-1)
R0m, _, _ = R0_of(Tm1)
Phi = mcompose(MINUS_ID, R0)
Phi_inv = minverse(Phi)
conj = mcompose(mcompose(Phi, T), Phi_inv)
g5 = (meq(mdeg(Phi, 1), ID) and miszero(mtrunc(madd(conj, Tm1, -1), N))
      and miszero(mtrunc(madd(R0m, mcompose(MINUS_ID, mcompose(R0, MINUS_ID)), -1), N))
      and miszero(mtrunc(madd(mcompose(MINUS_ID, mcompose(T, MINUS_ID)), Tm1, -1), N)))
res["G5"] = {"Phi_tangent_identity": meq(mdeg(Phi, 1), ID), "Phi_T1_Phiinv_eq_Tminus1": miszero(mtrunc(madd(conj, Tm1, -1), N)),
             "R0_minus1_eq_So_R0_So": miszero(mtrunc(madd(R0m, mcompose(MINUS_ID, mcompose(R0, MINUS_ID)), -1), N)),
             "So_T1_So_eq_Tminus1": miszero(mtrunc(madd(mcompose(MINUS_ID, mcompose(T, MINUS_ID)), Tm1, -1), N))}
# ---- G6 ----
pert = ({(2, 0): Fr(1, 7), (1, 1): Fr(-2, 11), (3, 0): Fr(3, 13)}, {(0, 2): Fr(5, 17), (2, 1): Fr(-1, 19), (0, 3): Fr(2, 23)})
Tt = madd(T, pert)
R0t, Ft, _ = R0_of(Tt)
g6 = (meq(mdeg(Tt, 1), A) and miszero(mtrunc(madd(mcompose(R0t, R0t), ID, -1), N)) and miszero(mtrunc(madd(mcompose(R0t, Tt), mcompose(Tt, R0t), -1), N))
      and meq(mdeg(R0t, 1), MINUS_ID))
res["G6_perturbed_germ"] = {"involution": miszero(mtrunc(madd(mcompose(R0t, R0t), ID, -1), N)), "commutes": miszero(mtrunc(madd(mcompose(R0t, Tt), mcompose(Tt, R0t), -1), N)), "linear_part_minus_I": meq(mdeg(R0t, 1), MINUS_ID)}
# ---- G7 ----
defect = madd(mcompose(T, MINUS_ID), mcompose(MINUS_ID, T), -1)
expected = ({}, pscal(coshm1_p(RHO), 2))
defect_s = madd(mcompose(T_s, MINUS_ID), mcompose(MINUS_ID, T_s), -1)
g7 = meq(mtrunc(defect, N), mtrunc(expected, N)) and miszero(mtrunc(defect_s, N))
res["G7"] = {"T_defect_is_2coshm1": meq(mtrunc(defect, N), mtrunc(expected, N)), "Ts_defect_zero": miszero(mtrunc(defect_s, N))}
# ---- G8 ---- symbolic
rho_, eta_ = sp.symbols('rho eta', real=True)
zeta = sp.exp(rho_ + sp.I*eta_)
g8 = sp.simplify(1/zeta - sp.exp(-rho_ - sp.I*eta_)) == 0
Wa, Wb = sp.symbols('W_a W_b')
g8 &= sp.simplify(sp.conjugate(-Wa)*(-Wb) - sp.conjugate(Wa)*Wb) == 0
g8 &= sp.simplify(sp.exp(sp.I*(-eta_)) - 1/sp.exp(sp.I*eta_)) == 0
res["G8"] = {"wrapped_inversion_is_So": bool(g8)}
# ---- negative controls ----
# NC1: linear part rotation by 2pi/3 in a rational model: use A' = [[0,-1],[1,-1]] (A'^3 = I). Germ T' = A' + same nonlinear terms as T.
Ap = ({(0, 1): Fr(-1)}, {(1, 0): Fr(1), (0, 1): Fr(-1)})
Tp = madd(Ap, madd(T, A, -1))
try:
    R0p, Fp, _ = R0_of(Tp)
    nc1_caught = not meq(mdeg(R0p, 1), MINUS_ID)      # construction gives linear part A'^3 = +I: the -I gate fails
except AssertionError:
    nc1_caught = True
res["NC1_A3_plus_I_caught"] = bool(nc1_caught)
# NC2
Rbad, _, _ = R0_of(T, root=Fr(1, 3))
nc2_caught = not miszero(mtrunc(madd(mcompose(Rbad, Rbad), ID, -1), N))
res["NC2_wrong_root_caught"] = bool(nc2_caught)
# NC3
nc3_caught = not miszero(mtrunc(madd(mcompose(MINUS_ID, mcompose(T, MINUS_ID)), T, -1), N))
res["NC3_T_not_So_symmetric_caught"] = bool(nc3_caught)
res["gates"] = {"G1": bool(g1), "G2": bool(g2), "G3": bool(g3), "G4": bool(g4), "G5": bool(g5), "G6": bool(g6), "G7": bool(g7), "G8": bool(g8),
                "NC1": bool(nc1_caught), "NC2": bool(nc2_caught), "NC3": bool(nc3_caught)}
ok = all(res["gates"].values()); res["ALL_PASS"] = ok
json.dump(res, open(sys.argv[1] if len(sys.argv) > 1 else "a2_involution_ledger.json", "w"), indent=1)
for k, v in res["gates"].items(): print(k, "PASS" if v else "FAIL")
print("r2 (degree-2 part of R_0):", res["G3"]["r2"]); print("real-ray degree 2:", res["G3"]["real_ray_deg2"])
print("ALL PASS" if ok else "FAILURES"); sys.exit(0 if ok else 1)
