#!/usr/bin/env python3
"""B1 Stage A -- decomposition of the R9 error budget C_2 = 2 K_Phi of RECOG-THM-R9-MEMORY (recog_cell_r9_memory_cert.py).

Reproduces the certificate's bound structure (mpmath, 60 digits; the certificate itself is Arb) and attributes K_Phi to its
sources, per row (C7, qbar) = (100, 1/400) and (30, 1/1600):
  e1 = sqrt(1+4 tau^2) * E_l,   E_l = C7 + (A + C7 qb)(2m + (A + C7 qb) qb)/2 + (m + A qb + C7 qb^2)^3 / (3 (1 - X))
       -> e1_C7 (the Dyadic remainder ceiling through the norm sqrt(1+4 tau^2) of l -> Im l - 2 tau Re l),
          e1_cross (products of jet moduli), e1_log3 (the cubic term of log(1+x): exact next-order size, not slack)
  e2 = gmax D1 + tau g1 (1 + D1 qb) + g1 B2 + g2/2 (tau + B2 qb)^2   (the Delta(q g(Theta)) part)
  C2 = 2 K_Phi, where the factor 2 is sum_m q_m^3 <= 2 q0^2 (imported one-orbit bound).
Levers evaluated:
  L1  summation lemma: with q_m <= q0/(1 + q0 m/2) (DYAD-THM-NF-REM one-orbit bound) sum q_m^3 <= (1 + q0) q0^2, factor ~2 (RECOG-side, exact)
  L2  Dyadic certificate values C7 = 85.07 / 27.60 instead of the ceilings 100 / 30
  L3  C7 -> 0 (hypothetical perfect degree-7 remainder): the floor of the present first-order budget
  L4  Stage C: exact O(q^2) memory with an O(q^3) remainder (needs the degree-7 NF jet and a C8 row from Dyadic):
      the window becomes q0^2 < |G|/C3; C3 estimated as sqrt(1+4tau^2) C8 + (jet part) for a range of C8.
[NUM] (not a proof input): along orbits of the truncated jet J, the actual per-step |Delta Phi|/q^3 and the actual
|M - q0 g|/q0^2, to gauge how far the jet part of the bound is from the truth (no C7 in the jet model).
usage: python -I recog_b1_stageA_r9_budget.py [OUT_JSON]
"""
import json, sys, math
import mpmath as mp
mp.mp.dps = 60
s3 = mp.sqrt(3); tau = 2*s3/3
mu = mp.mpc(-mp.mpf(1)/2, -2*s3/3)
a32 = mp.mpc(-mp.mpf(97)/432, 197*s3/324)
a05 = mp.mpc(-mp.mpf(49)/8640, -307*s3/25920)
I = mp.mpc(0, 1)
beta = a32 - mu*mu/2
c_iso = ((1 - 2*I*tau)*beta).imag
G = (1 - 2*I*tau)/(1 - 6*I*tau)*a05
absG = abs(G)
norm = mp.sqrt(1 + 4*tau**2)
m, A, a5 = abs(mu), abs(a32) + abs(a05), abs(a05)

def budget(C7, qb):
    C7 = mp.mpf(C7); qb = mp.mpf(qb)
    X = m*qb + A*qb**2 + C7*qb**3
    t_C7 = C7
    t_cross = (A + C7*qb)*(2*m + (A + C7*qb)*qb)/2
    t_log3 = (m + A*qb + C7*qb**2)**3/(3*(1 - X))
    E_l = t_C7 + t_cross + t_log3
    e1 = norm*E_l
    B2 = abs(beta) + a5 + E_l*qb
    r1 = qb/2 + B2*qb**2
    D1 = 2*B2 + 2*(mp.mpf(1)/2 + B2*qb)**2*mp.exp(2*r1)
    gmax = abs(c_iso) + absG; g1 = 6*absG; g2 = 36*absG
    e2a, e2b, e2c, e2d = gmax*D1, tau*g1*(1 + D1*qb), g1*B2, g2/2*(tau + B2*qb)**2
    e2 = e2a + e2b + e2c + e2d
    K = e1 + e2
    return {"C7": float(C7), "qbar": float(qb), "X": float(X), "E_l": float(E_l),
            "e1": float(e1), "e1_C7": float(norm*t_C7), "e1_cross": float(norm*t_cross), "e1_log3": float(norm*t_log3),
            "e2": float(e2), "e2_gmaxD1": float(e2a), "e2_tau_g1": float(e2b), "e2_g1B2": float(e2c), "e2_g2": float(e2d),
            "D1": float(D1), "B2": float(B2), "K_Phi": float(K), "C2": float(2*K), "window_q0": float(absG/(2*K)),
            "share_C7_of_K": float(norm*t_C7/K)}

rows = {"large |z|<=1/20": (100, mp.mpf(1)/400), "small |z|<=1/40": (30, mp.mpf(1)/1600)}
out = {"constants": {"|G|": float(absG), "c_iso": float(c_iso), "norm_sqrt(1+4tau^2)": float(norm), "|mu|": float(m), "A=|a32|+|a05|": float(A)},
       "targets": {"C2_for_whole_small_row": float(absG*1600), "C2_for_whole_large_row": float(absG*400)}, "rows": {}}
for name, (C7, qb) in rows.items():
    b = budget(C7, qb)
    cert = {"large |z|<=1/20": 85.07, "small |z|<=1/40": 27.60}[name]
    L2 = budget(cert, qb)
    L3 = budget(0, qb)
    # L1: sum lemma factor (1+q0) at q0 = qbar (worst), instead of 2
    L1_factor = float(1 + qb)
    b["levers"] = {
        "L1_sum_lemma": {"C2": b["K_Phi"]*L1_factor, "window_q0": float(absG/(b["K_Phi"]*L1_factor)), "gain_factor": 2/L1_factor},
        "L2_cert_values": {"C7": cert, "K_Phi": L2["K_Phi"], "C2": L2["C2"], "window_q0": L2["window_q0"], "gain_factor": b["C2"]/L2["C2"]},
        "L1+L2": {"C2": L2["K_Phi"]*L1_factor, "window_q0": float(absG/(L2["K_Phi"]*L1_factor))},
        "L3_C7_zero_floor": {"K_Phi": L3["K_Phi"], "C2": L3["C2"], "C2_with_L1": L3["K_Phi"]*L1_factor, "window_q0_with_L1": float(absG/(L3["K_Phi"]*L1_factor)),
                              "reaches_target": L3["K_Phi"]*L1_factor <= float(absG*(1600 if 'small' in name else 400))},
    }
    out["rows"][name] = b
# L4: Stage C estimate. With the O(q^2) term computed exactly, the remainder is |R_3| <= C3 q0^3 with
# sum q_m^4 <= (1 + q0 + q0^2/...) q0^3 ~ q0^3 (same lemma at power 4: sum 1/(1+q0 m/2)^4 ~ 2/(3 q0)): C3 ~ (2/3) K3 (1 + O(q0)),
# K3 ~ norm*C8 + jet part (unknown here; taken as 0..20). Incompleteness certified iff 2|G| q0 > 2 C3 q0^3, i.e. q0 < sqrt(|G|/C3).
L4 = []
for C8 in (100, 300, 1000, 3000, 10000):
    for jetpart in (0, 20):
        K3 = norm*C8 + jetpart; C3 = mp.mpf(2)/3*K3
        L4.append({"C8": C8, "jet_part_K3": jetpart, "C3": float(C3), "window_q0": float(mp.sqrt(absG/C3)),
                   "covers_large_row": float(mp.sqrt(absG/C3)) >= 1/400, "covers_small_row": float(mp.sqrt(absG/C3)) >= 1/1600})
out["L4_stageC_estimate"] = L4
# sum lemma check (numerical): sum_{m>=0} (q0/(1+q0 m/2))^3 <= (1+q0) q0^2 for q0 in the rows
chk = {}
for q0 in (1/400, 1/1600, 1e-4):
    S = sum((q0/(1 + q0*mm/2))**3 for mm in range(0, int(50/q0)))
    chk[str(q0)] = {"sum": S, "bound_(1+q0)q0^2": (1 + q0)*q0**2, "ok": S <= (1 + q0)*q0**2, "old_bound_2q0^2": 2*q0**2}
out["L1_sum_lemma_numeric_check"] = chk
# [NUM] jet-model floor: per-step |Delta Phi|/q^3 in mpmath (30 digits) over the first steps (float64 noise would dominate at
# late times, where q^3 ~ 1e-17), and sum q_m^3 / q0^2 along the jet orbit
num_mp = {}
mp.mp.dps = 30
for q0 in (mp.mpf(1)/400, mp.mpf(1)/1600):
    worst = mp.mpf(0); sumq3 = mp.mpf(0)
    for th0 in [mp.pi*k/36 for k in range(13)]:
        z = mp.sqrt(q0)*mp.expj(th0); Th = th0
        def gm(t): return c_iso + (G*mp.expj(-6*t)).imag
        Phi = Th - tau*mp.log(q0) + q0*gm(Th); S3 = mp.mpf(0)
        for _ in range(3000):
            q = abs(z)**2; S3 += q**3
            zn = z + mu*z*z*mp.conj(z) + a32*z**3*mp.conj(z)**2 + a05*mp.conj(z)**5
            Th = Th + mp.arg(zn/z); z = zn; qn = abs(z)**2
            Phin = Th - tau*mp.log(qn) + qn*gm(Th)
            worst = max(worst, abs(Phin - Phi)/q**3); Phi = Phin
        sumq3 = max(sumq3, S3)
    num_mp[str(float(q0))] = {"max_per_step_|dPhi|/q^3_jet_model_first3000": float(worst), "sum_q^3/q0^2_first3000": float(sumq3/q0**2)}
out["NUM_jet_model_mp"] = num_mp
mp.mp.dps = 60
import numpy as np
mu_, a32_, a05_ = complex(mu), complex(a32), complex(a05)
G_ = complex(G); c_iso_ = float(c_iso); tau_ = float(tau)
def g(th): return c_iso_ + (G_*np.exp(-6j*th)).imag
num = {}
for q0 in (1/400, 1/1600):
    th0 = np.linspace(0, np.pi/3, 13)
    z = np.sqrt(q0)*np.exp(1j*th0); Th = th0.copy()
    Phi = Th - tau_*np.log(q0) + q0*g(Th)
    maxratio = 0.0; N = 400000
    for _ in range(N):
        q = np.abs(z)**2
        zn = z + mu_*z*z*np.conj(z) + a32_*z**3*np.conj(z)**2 + a05_*np.conj(z)**5
        Th = Th + np.angle(zn/z); z = zn
        qn = np.abs(z)**2
        Phin = Th - tau_*np.log(qn) + qn*g(Th)
        Phi = Phin
    M = Phi - (th0 - tau_*np.log(q0))
    pred = q0*g(th0)
    num[str(q0)] = {"max_|M-q0 g|/q0^2": float(np.max(np.abs(M - pred))/q0**2), "q_end": float(np.abs(z).max()**2), "note": "float64; per-step ratios not reported here (late-time noise)"}
out["NUM_jet_model"] = num
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "b1_stageA_r9_budget.json", "w"), indent=1)
for name, b in out["rows"].items():
    print(f"{name}: K_Phi={b['K_Phi']:.2f} C2={b['C2']:.2f} window={b['window_q0']:.3e} | e1={b['e1']:.2f} [C7 {b['e1_C7']:.2f} ({100*b['share_C7_of_K']:.1f}% of K), cross {b['e1_cross']:.2f}, log3 {b['e1_log3']:.2f}] e2={b['e2']:.2f} [gmaxD1 {b['e2_gmaxD1']:.2f}, tau g1 {b['e2_tau_g1']:.2f}, g1B2 {b['e2_g1B2']:.2f}, g2 {b['e2_g2']:.2f}]")
    for k, v in b["levers"].items(): print("   ", k, {kk: (round(vv, 4) if isinstance(vv, float) else vv) for kk, vv in v.items()})
print("targets:", out["targets"]); print("L4:", [(x["C8"], x["jet_part_K3"], round(x["window_q0"], 5), x["covers_large_row"], x["covers_small_row"]) for x in L4])
print("sum lemma:", {k: (v["ok"], round(v["sum"]/v["bound_(1+q0)q0^2"], 3)) for k, v in chk.items()})
print("NUM jet model (mp, first 3000 steps):", num_mp); print("NUM jet model (float64, full):", num)
