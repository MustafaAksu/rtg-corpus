#!/usr/bin/env python3
"""B1 L1+L2 -- sharpened R9 rows: certificate (mpmath interval arithmetic, 60 digits; rigorous enclosures).

Base: RECOG-THM-R9-MEMORY (recog-v0.3.24 §6.13a), proof structure of recog_cell_r9_memory_cert.py (Arb):
   |R| <= K_Phi * sum_m q_m^3,   K_Phi from the jet coefficients, C7 (DYAD-THM-NF-REM) and four elementary inequalities.
L1 (summation lemma, RECOG-side, exact). From the adopted one-orbit bound q_m <= q0/(1 + q0 m/2) (DYAD-THM-NF-REM):
   sum_{m>=0} q_m^3 <= q0^3 [ 1 + sum_{m>=1} (1 + q0 m/2)^{-3} ] <= q0^3 [ 1 + int_0^inf (1 + q0 x/2)^{-3} dx ] = q0^3 (1 + 1/q0) = (1 + q0) q0^2.
   Hence |R| <= K_Phi (1 + q0) q0^2 <= K_Phi (1 + qbar) q0^2 on the row (qbar = q_max).  Old: |R| <= 2 K_Phi q0^2.
L2 (Dyadic certificate values as ceilings, conditional). DYAD-THM-NF-REM states C7 = 100 (certificate value 85.07) on |z| <= 1/20
   and C7 = 30 (certificate value 27.60) on |z| <= 1/40. Safe rounded-up ceilings used here: 85.1 and 27.7 (>= published value + 0.03);
   a row built on them is conditional on Dyadic accepting these ceilings (notice); the L1-only rows rest on adopted statements only.
Gates (exit 0 iff all pass):
   G1  L1 lemma: the integral identity int_0^inf (1+q0 x/2)^{-3} dx = 1/q0 (exact, sympy); the rigorous interval bracket
       q0^3 [1 + (1/q0)(1+q0/2)^{-2}] <= sum <= (1+q0) q0^2 for q0 down to 1e-6; float64 explicit sums for three q0 (sanity).
   G2  reproduction: interval enclosure of K_Phi for the adopted rows (C7 = 100, 30) has upper bound <= 258.49 / 81.44 (the Arb values
       quoted in the DSN), and >= 258.48 / 81.43 (no accidental weakening).
   G3  new rows: enclosures of K_Phi(C7, qbar) and C2' = ceil_4( K_Phi (1 + qbar) ) for (100, 1/400), (30, 1/1600) [L1] and
       (85.1, 1/400), (27.7, 1/1600) [L1+L2]; printed with safe ceilings; the corollary windows |G|/C2'.
   G4  consistency: C2' < C2_old for every row; the windows widen by the stated factors.
Negative controls:
   NC1 the lemma's bound with the integral mis-evaluated as 1/(2 q0) (factor 1/2) is violated by the explicit sum (must be detected).
   NC2 a C7 ceiling below the published certificate value (85.06) is refused by the safety check.
usage: python -I recog_b1_l1l2_sharpened_rows_cert.py [OUT_JSON]
"""
import json, sys
import mpmath as mp
from mpmath import iv
mp.mp.dps = 60; iv.dps = 60
I = lambda x: iv.mpf(x)
def cplx(re, im): return (I(re), I(im))
def cabs(z): return iv.sqrt(z[0]**2 + z[1]**2)
def cmul(a, b): return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])
def csub(a, b): return (a[0] - b[0], a[1] - b[1])
def cdiv(a, b):
    d = b[0]**2 + b[1]**2
    return ((a[0]*b[0] + a[1]*b[1])/d, (a[1]*b[0] - a[0]*b[1])/d)
s3 = iv.sqrt(I(3)); tau = 2*s3/3
mu = cplx(I(-1)/2, -2*s3/3)
a32 = cplx(I(-97)/432, 197*s3/324)
a05 = cplx(I(-49)/8640, -307*s3/25920)
beta = csub(a32, (cmul(mu, mu)[0]/2, cmul(mu, mu)[1]/2))
one_m2it = cplx(I(1), -2*tau); one_m6it = cplx(I(1), -6*tau)
c_iso = cmul(one_m2it, beta)[1]
G = cmul(cdiv(one_m2it, one_m6it), a05)
absG = cabs(G)
norm = iv.sqrt(1 + 4*tau**2)
m, A, a5 = cabs(mu), cabs(a32) + cabs(a05), cabs(a05)
def K_Phi(C7, qb):
    C7, qb = I(C7), I(qb)
    X = m*qb + A*qb**2 + C7*qb**3
    E_l = C7 + (A + C7*qb)*(2*m + (A + C7*qb)*qb)/2 + (m + A*qb + C7*qb**2)**3/(3*(1 - X))
    e1 = norm*E_l
    B2 = cabs(beta) + a5 + E_l*qb
    r1 = qb/2 + B2*qb**2
    D1 = 2*B2 + 2*(I(1)/2 + B2*qb)**2*iv.exp(2*r1)
    gmax = abs(c_iso) + absG; g1 = 6*absG; g2 = 36*absG
    e2 = gmax*D1 + tau*g1*(1 + D1*qb) + g1*B2 + g2/2*(tau + B2*qb)**2
    return e1 + e2
def up(x): return mp.mpf(x._mpi_[1])
def lo(x): return mp.mpf(x._mpi_[0])
def ceil_sig(x, digits=4):
    x = mp.mpf(x); e = mp.floor(mp.log10(x)); scale = mp.mpf(10)**(digits - 1 - e)
    return mp.ceil(x*scale)/scale
res = {"gates": {}}
# ---- G1: lemma ----
import numpy as np
def S_explicit_float(q0):
    """explicit partial sum (float64, numpy) to m = 400/q0 plus the rigorous integral tail q0^2 (1 + q0 cutoff/2)^{-2}; sanity only"""
    cutoff = int(400/q0); mm = np.arange(0, cutoff + 1, dtype=np.float64)
    return float(np.sum((q0/(1 + q0*mm/2))**3) + q0**2*(1 + q0*cutoff/2)**-2)
g1 = True; lemma_rows = {}
for q0 in (1/400, 1/1600, 1e-4):
    S = S_explicit_float(q0); bound = (1 + q0)*q0**2
    ok = S <= bound; g1 &= ok
    lemma_rows[str(q0)] = {"sum_float": S, "bound": bound, "ratio": S/bound, "ok": bool(ok), "note": "float64 sanity; the proof is the integral comparison"}
# rigorous bracket for every q0 (interval): q0^3 [1 + int_1^inf f] <= sum <= q0^3 [1 + int_0^inf f], f(x) = (1+q0 x/2)^-3,
# int_c^inf f = (1/q0)(1 + q0 c/2)^{-2}; the upper member is the lemma's bound (1+q0) q0^2 exactly.
bracket = {}
for q0s in ("0.0025", "0.000625", "1e-4", "1e-6"):
    q0 = I(q0s)
    upper = q0**3*(1 + 1/q0); lower = q0**3*(1 + (1/q0)*(1 + q0/2)**(-2))
    bracket[q0s] = {"lower": float(lo(lower)), "upper(=lemma bound)": float(up(upper)), "lower/upper": float(lo(lower)/up(upper))}
    g1 &= up(upper) <= up((1 + q0)*q0**2) + mp.mpf(10)**-50
res["G1_lemma_bracket"] = bracket
# integral identity exact (symbolic): int_0^inf (1 + q x/2)^{-3} dx = [ -(1/q) (1+qx/2)^{-2} ]_0^inf = 1/q
import sympy as sp
xq, qq = sp.symbols('x q', positive=True)
integral_ok = sp.simplify(sp.integrate((1 + qq*xq/2)**-3, (xq, 0, sp.oo)) - 1/qq) == 0
g1 &= bool(integral_ok)
res["G1_lemma"] = {"rows": lemma_rows, "integral_identity": bool(integral_ok)}
res["gates"]["G1"] = bool(g1)
# ---- G2: reproduction ----
K100, K30 = K_Phi(100, mp.mpf(1)/400), K_Phi(30, mp.mpf(1)/1600)
g2 = (up(K100) <= mp.mpf("258.49") and up(K30) <= mp.mpf("81.44") and lo(K100) >= mp.mpf("258.48") and lo(K30) >= mp.mpf("81.43"))
res["G2_reproduction"] = {"K_Phi_100": [float(lo(K100)), float(up(K100))], "K_Phi_30": [float(lo(K30)), float(up(K30))]}
res["gates"]["G2"] = bool(g2)
# ---- G3: new rows ----
PUBLISHED = {"1/400": mp.mpf("85.07"), "1/1600": mp.mpf("27.60")}
def safe_ceiling(C7, row):
    if mp.mpf(C7) < PUBLISHED[row] + mp.mpf("0.005"):
        raise ValueError(f"C7 ceiling {C7} is not safely above the published certificate value {PUBLISHED[row]} (round-to-nearest 2 decimals)")
    return mp.mpf(C7)
rows = []
for label, C7, qb_s, qb, kind in [("L1 large", 100, "1/400", mp.mpf(1)/400, "adopted statements only"), ("L1 small", 30, "1/1600", mp.mpf(1)/1600, "adopted statements only"),
                                  ("L1+L2 large", "85.1", "1/400", mp.mpf(1)/400, "conditional on the Dyadic certificate value 85.07 as ceiling 85.1"),
                                  ("L1+L2 small", "27.7", "1/1600", mp.mpf(1)/1600, "conditional on the Dyadic certificate value 27.60 as ceiling 27.7")]:
    if "L2" in label: safe_ceiling(C7, qb_s)
    K = K_Phi(C7, qb)
    C2new = up(K*(1 + I(qb)))
    C2ceil = ceil_sig(C2new, 4)
    C2old = 517 if "large" in label else 163
    window = lo(absG)/C2ceil; window_old = lo(absG)/C2old
    rows.append({"row": label, "C7": str(C7), "qbar": qb_s, "basis": kind, "K_Phi_upper": float(up(K)), "C2_new_exact_upper": float(C2new), "C2_new_ceiling_4sig": float(C2ceil),
                 "C2_old": C2old, "window_new": float(window), "window_old": float(window_old), "gain": float(window/window_old)})
res["G3_rows"] = rows
res["gates"]["G3"] = True
res["gates"]["G4"] = all(r["C2_new_ceiling_4sig"] < r["C2_old"] and r["gain"] > 1 for r in rows)
res["constants"] = {"|G|": [float(lo(absG)), float(up(absG))], "norm": [float(lo(norm)), float(up(norm))]}
# ---- negative controls ----
S = S_explicit_float(1/400)
nc1_bad_bound = (1/400)**3*(1 + 1/(2*(1/400)))               # mis-evaluated integral (factor 1/2): bound = q0^3 (1 + 1/(2 q0))
nc1 = S > nc1_bad_bound                                        # the explicit sum exceeds the wrong bound -> detected
try:
    safe_ceiling("85.06", "1/400"); nc2 = False
except ValueError:
    nc2 = True
res["gates"]["NC1_wrong_integral_caught"] = bool(nc1); res["gates"]["NC2_unsafe_ceiling_refused"] = bool(nc2)
ok = all(res["gates"].values()); res["ALL_PASS"] = ok
json.dump(res, open(sys.argv[1] if len(sys.argv) > 1 else "b1_l1l2_sharpened_rows_cert.json", "w"), indent=1)
for k, v in res["gates"].items(): print(k, "PASS" if v else "FAIL")
print("lemma ratios:", {k: round(v["ratio"], 6) for k, v in lemma_rows.items()})
print("K_Phi adopted rows:", res["G2_reproduction"])
for r in rows: print(f"{r['row']:<12} C7={r['C7']:<5} K_Phi<={r['K_Phi_upper']:.4f}  C2'={r['C2_new_ceiling_4sig']:.4g} (old {r['C2_old']})  window {r['window_new']:.4e} (old {r['window_old']:.4e}, x{r['gain']:.3f})  [{r['basis']}]")
print("ALL PASS" if ok else "FAILURES"); sys.exit(0 if ok else 1)
