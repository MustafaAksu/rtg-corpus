#!/usr/bin/env python3
"""A1c part 1 -- a finite-prefix error envelope for the known-a decoder, computable from declared data only.

Setting (RECOG-THM-A1B-SLIP-SCHEDULE-U, recog-v0.3.24 §6.13b): for x0 in U, a = 1/Q0, the k-th 7-gap at block M_k,
    tau psi(a + M_k) - (k-1) pi/3 = L + eps_k,
    |eps_k| <= Delta_{j_k} + 5 arcsin(0.705 sqrt(Q*) + 0.257 Q*) + tau |S^tail_{M_k}| + |R^tail_{M_k}|,
with Q* the largest primitive amplitude among the points of the slip block, Delta <= tau Q + 1.82 Q^{3/2} (Lemma C'),
S^tail_M = sum_{m>=M} (Q_m - 1/(a+m)),  R^tail_M = sum_{m>=M} r_m,  |r_m| <= (403/250) Q_m^{3/2}.
The theorem's envelope names orbit quantities (Q*, the tails). Here they are majorised by functions of (a, M) alone,
from four adopted inputs:
  (I1) DYAD-THM-PRIM-CTR:                  Q_m <= 1/(a + m/2)
  (I2) RECOG-THM-A1A-RECIPROCAL-AMPLITUDE: |Q_{m+1}^{-1} - Q_m^{-1} - 1| < (15/2) sqrt(Q_m)
  (I3) one-step pointwise bound on U_T (A1b cell §2): |W(Tx)/(lambda W(x)) - 1| <= 0.705 sqrt(Q) + 0.257 Q
  (I4) DYAD-THM-LPHASE-ROWA-REMAINDER:      |r_m| <= (403/250) Q_m^{3/2}
Derived majorants (all elementary; proofs in the record):
  qbar_M   = 1/(a + M/2)                                                    [I1]
  Q*(a,M)  = f^5(qbar_M),  f(Q) = Q (1 + 0.705 sqrt Q + 0.257 Q)^2         [I3; at most five in-block steps]
  ebar_m   = (15/2) [ a^{-1/2} + 4 ( sqrt(a + (m-1)/2) - sqrt a ) ]  (m>=1), ebar_0 = 0     [I2 + I1 + integral comparison]
  Q_m in [ 1/(a+m+ebar_m),  min(1/(a+m/2), 1/(a+m-ebar_m)) ]  ->  |Q_m - 1/(a+m)| <= D_m
  Sbar(a,M) = sum_{m=M}^{m_c-1} D_m + 75 [ (a+m_c)^{-3/2} + 2 (a+m_c)^{-1/2} ],  m_c = max(M, 5625 - a)
              (for a+m >= 5625: ebar_m <= 37.5 sqrt(a+m) <= (a+m)/2, so D_m <= 2 ebar_m/(a+m)^2 <= 75 (a+m)^{-3/2})
  Rbar(a,M) = (403/250) [ (a+M/2)^{-3/2} + 4 (a+M/2)^{-1/2} ]                [I4 + I1]
  E(a,M)    = tau Q* + 1.82 Q*^{3/2} + 5 arcsin(0.705 sqrt Q* + 0.257 Q*) + tau Sbar + Rbar
Known-a decoder window after k slips:  L in [ c_k - E(a,M_k), c_k + E(a,M_k) ],  c_k = tau psi(a+M_k) - (k-1) pi/3;
the intersection over k <= K is also reported.
[NUM] check (not a proof input): 12 orbits in U (Q0 in {1/625, 1/1000, 1/2500}, four phases), 2e6 primitive steps;
slips detected with the F2(b) predicate; eps_k measured against Psi_inf estimated at the end of the run (tail O(sqrt Q_end));
reports |eps_k| / E(a, M_k) (must be <= 1 up to the Psi_inf estimation error) and the ratio E / (0.75 sqrt Q_{M_k}).
usage: python -I recog_a1c_known_a_envelope.py [OUT_JSON] [N_STEPS]
"""
import json, math, sys
import numpy as np
import mpmath as mp

TAU = 2*math.sqrt(3)/3
OMEGA = complex(-0.5, math.sqrt(3)/2)
LAM = complex(0.5, math.sqrt(3)/2)
C1, C2, K32, R15, RA = 0.705, 0.257, 1.82, 7.5, 403/250

def f_step(Q): return Q*(1 + C1*math.sqrt(Q) + C2*Q)**2
def Qstar(a, M):
    Q = 1/(a + M/2)
    for _ in range(5): Q = f_step(Q)
    return Q
def ebar(a, m):
    if m == 0: return 0.0
    return R15*(a**-0.5 + 4*(math.sqrt(a + (m - 1)/2) - math.sqrt(a)))
def D_m(a, m):
    e = ebar(a, m); c = 1/(a + m)
    lo = 1/(a + m + e)
    up = 1/(a + m/2)
    if a + m > e: up = min(up, 1/(a + m - e))
    return max(c - lo, up - c)
def Sbar(a, M):
    mc = max(M, int(math.ceil(5625 - a)))
    s = sum(D_m(a, m) for m in range(M, mc))
    return s + 75*((a + mc)**-1.5 + 2*(a + mc)**-0.5)
def Rbar(a, M): return RA*((a + M/2)**-1.5 + 4*(a + M/2)**-0.5)
def envelope(a, M):
    Qs = Qstar(a, M)
    parts = {"tauQ*": TAU*Qs, "K32": K32*Qs**1.5, "arcsin": 5*math.asin(C1*math.sqrt(Qs) + C2*Qs), "tau_Sbar": TAU*Sbar(a, M), "Rbar": Rbar(a, M)}
    return sum(parts.values()), parts

def run_orbits(N):
    Q0s = [1/625]*4 + [1/1000]*4 + [1/2500]*4
    ths = [0.3, 1.7, 3.9, 5.1]*3
    n = len(Q0s)
    rho = np.array([math.sqrt(Q0s[i])*math.cos(ths[i]) for i in range(n)])      # W = rho + omega eta = sqrt(Q0) e^{i th}
    eta = np.array([math.sqrt(Q0s[i])*math.sin(ths[i]) for i in range(n)])/OMEGA.imag
    rho = rho - OMEGA.real*eta                                                   # Re W = rho + Re(omega) eta
    W = rho + OMEGA*eta
    phihat = np.angle(W).copy()
    # record: anchors and gaps; block phases Theta_W(M) at block base points
    anchors = [[] for _ in range(n)]
    prev_eta = eta.copy(); prev_rho = rho.copy()
    Theta_blocks = [[] for _ in range(n)]; Q_blocks = [[] for _ in range(n)]
    for step in range(1, N + 1):
        rho_n = rho - np.sin(eta); eta_n = eta + np.exp(rho) - 1 - np.sin(eta)
        Wn = rho_n + OMEGA*eta_n
        phihat += np.angle(Wn/W)
        bev = (eta < 0) & (eta_n >= 0) & (rho > 0) & (rho_n > 0)
        for i in np.nonzero(bev)[0]: anchors[i].append((step, phihat[i]))
        rho, eta, W = rho_n, eta_n, Wn
        if step % 6 == 0:
            M = step//6
            for i in range(n):
                Theta_blocks[i].append(phihat[i] - 2*math.pi*M); Q_blocks[i].append(abs(W[i])**2)
    out = []
    for i in range(n):
        a = 1/Q0s[i]
        Qend = Q_blocks[i][-1]; Psi_inf = Theta_blocks[i][-1] - TAU*math.log(Qend)
        an = anchors[i]
        n0, phi0 = an[0]; ell0 = math.floor(phi0/(2*math.pi))
        L = math.pi/3*n0 - 2*math.pi*ell0 + Psi_inf
        slips = []
        k = 0
        for j in range(1, len(an)):
            gap = an[j][0] - an[j-1][0]
            if gap == 7:
                k += 1; nk = an[j-1][0]; Mk = nk//6
                ck = TAU*float(mp.digamma(a + Mk)) - (k - 1)*math.pi/3
                eps = ck - L
                E, parts = envelope(a, Mk)
                QM = Q_blocks[i][Mk - 1] if Mk >= 1 else Q0s[i]
                slips.append({"k": int(k), "M_k": int(Mk), "eps_k": eps, "E": E, "ratio_eps_over_E": abs(eps)/E, "E_over_0.75sqrtQ": E/(0.75*math.sqrt(QM)), "parts": parts, "window": [ck - E, ck + E]})
            elif gap != 6:
                slips.append({"bad_gap": gap, "at": an[j][0]})
        # intersection of windows
        lo = max(s["window"][0] for s in slips if "window" in s); hi = min(s["window"][1] for s in slips if "window" in s)
        out.append({"Q0": Q0s[i], "a": a, "theta0": ths[i], "n0": int(n0), "ell0": int(ell0), "L_est": L, "Psi_inf_tail_scale_sqrtQend": math.sqrt(Qend),
                    "n_anchors": len(an), "slips": slips, "window_intersection": [lo, hi], "L_in_intersection": lo <= L <= hi, "width_last": 2*slips[-1]["E"] if slips else None})
    return out

if __name__ == "__main__":
    outp = sys.argv[1] if len(sys.argv) > 1 else "a1c_known_a_envelope.json"
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 2_000_000
    table = {}
    for a in (625, 1000, 2500):
        table[str(a)] = {str(M): {"E": envelope(a, M)[0], **{k: v for k, v in envelope(a, M)[1].items()}} for M in (1000, 10000, 100000, 1000000, 10000000)}
    orbits = run_orbits(N)
    res = {"N_steps": N, "constants": {"tau": TAU, "C1": C1, "C2": C2, "K32": K32, "R15": R15, "RA": RA}, "envelope_table": table, "orbits": orbits,
           "summary": {"max_ratio_eps_over_E": max(s["ratio_eps_over_E"] for o in orbits for s in o["slips"] if "ratio_eps_over_E" in s),
                       "all_gaps_6_or_7": all("bad_gap" not in s for o in orbits for s in o["slips"]),
                       "all_L_in_intersection": all(o["L_in_intersection"] for o in orbits),
                       "E_over_0.75sqrtQ_range": [min(s["E_over_0.75sqrtQ"] for o in orbits for s in o["slips"] if "E_over_0.75sqrtQ" in s), max(s["E_over_0.75sqrtQ"] for o in orbits for s in o["slips"] if "E_over_0.75sqrtQ" in s)]}}
    json.dump(res, open(outp, "w"), indent=1, default=lambda o: bool(o) if isinstance(o, np.bool_) else (float(o) if isinstance(o, (np.floating, np.integer)) else str(o)))
    for a, row in table.items():
        print("a=%s: " % a + "  ".join("M=%s E=%.4f (tauS=%.4f R=%.4f blk=%.4f)" % (M, v["E"], v["tau_Sbar"], v["Rbar"], v["tauQ*"] + v["K32"] + v["arcsin"]) for M, v in row.items()))
    for o in orbits:
        print("Q0=%.2e th=%.1f n0=%d slips=%d | " % (o["Q0"], o["theta0"], o["n0"], len(o["slips"])) + " ".join("k%d M=%d eps=%+.2e E=%.3f r=%.3f" % (s["k"], s["M_k"], s["eps_k"], s["E"], s["ratio_eps_over_E"]) for s in o["slips"] if "k" in s) + " | L in cap: %s width_last=%.3f" % (o["L_in_intersection"], o["width_last"]))
    print("summary:", res["summary"])
