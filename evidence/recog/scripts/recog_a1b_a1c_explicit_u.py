#!/usr/bin/env python3
"""A1b/A1c on the explicit start set U -- sandbox [NUM] illustration (not a proof input).

Tests the explicit-U derivations of records/recog/RECOG_A1B_A1C_SESSION_v0_1.md on float64 primitive orbits:
  T1  B-event predicate (eta_wrap(x)<0<=eta_wrap(Tx), rho>0 both sides)  ==  2pi-crossings of the
      principal-increment lift (Lemma A); event-anchored lift == cumsum lift up to rounding
  T2  one-step angle: max |delta_T - pi/3| over all steps vs the (B) bound arcsin(0.04654) and the
      pointwise bound arcsin(0.705 sqrt(Q) + 0.257 Q)  (Lemma B inputs)
  T3  at every anchor: Lambda_5 < 2pi < Lambda_7 (alphabet {6,7}); Delta_j = 2pi - Lambda_6 > 0 and
      Delta_j / Q(anchor) -> tau (Lemma C)
  T4  exact event identity G_{n_j} = C + (pi/3) s_j - o_j (spread), gap criterion g=7 <=> o_j < Delta_j
  T5  slip schedule: tau psi(a + M_k) - (k-1) pi/3 = L + eps_k, L = (pi/3) n_0 - 2 pi l_0 + Psi_inf, a = 1/Q_0,
      psi the digamma function (the harmonic form of FC-21); eps_k = O(sqrt(Q_{M_k})). The naive form
      tau log M_k - (k-1) pi/3 differs by the known term -tau log(1 + a/M_k). Psi_inf is estimated on the z-track
      by Phi(z_M) = Psi_z(M) + q_M g(Theta_M) (R9 averaging function used as an estimator only).
      Record-only decoder: least-squares fit of (a, L) to the slip data (no state datum used).
  T6  comparator-fiber decode: pairs with the same q_0 and Theta_z difference delta = pi/6; the two token
      records give Delta Psi_inf (mod 2pi); compare with the direct z-track value and with delta + Delta M
      (R9 prediction q[Lambda_1(alpha+delta) - Lambda_1(alpha)]); record-only decode with the fitted (a, L) of each
      orbit; finite-prefix resolution per slip count

usage: python -I recog_a1b_a1c_explicit_u.py [N_steps] [out.json]     (default 2,000,000 steps)
Run from the repository root: it imports h and h^{-1} from recog_cell_f2b_token_bridge.py (DYAD-ALG-NF6).
"""
import json, math, os, sys, time
import numpy as np
from scipy.special import digamma
from scipy.optimize import least_squares

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import recog_cell_f2b_token_bridge as F2B   # h_eval, h_inv, OM, LAM, TAU  (its __main__ is guarded)

TAU, OM, LAM = F2B.TAU, F2B.OM, F2B.LAM
S3 = math.sqrt(3)
C_ISO = -4*S3/27
G_LAT = -(43 + 5611*S3*1j)/1270080
EPS_B = 0.04654                                   # DYAD-THM-LPHASE-ROWA-REMAINDER (B)

def g_avg(theta):      # R9 averaging function g(Theta) = c_iso + Im(G e^{-6 i Theta})
    return C_ISO + np.imag(G_LAT*np.exp(-6j*theta))

def lam1(theta):
    return (43*np.sin(6*theta) - 5611*S3*np.cos(6*theta))/1270080

def wrap(x): return (x + np.pi) % (2*np.pi) - np.pi

def primitive_orbit(rho0, eta0, N):
    rho = np.empty(N + 1); eta = np.empty(N + 1); rho[0], eta[0] = rho0, eta0
    r, e = rho0, eta0; sin, expm1 = math.sin, math.expm1
    for n in range(1, N + 1):
        s = sin(e); r, e = r - s, e + expm1(r) - s
        rho[n] = r; eta[n] = e
    return rho, eta

def analyse(rho, eta, N, with_chart=True):
    ew = wrap(eta); assert np.max(np.abs(eta)) < 1.0 and np.allclose(ew, eta), "eta left the one-chart range"
    W = rho + OM*ew; Q = np.abs(W)**2
    assert Q[0] <= 1/625 + 1e-15, "start not in U"
    assert np.max(np.abs(W)) < 0.047, "left the tube enclosure |W| < 47/1000"
    theta = np.mod(np.angle(W), 2*np.pi)
    # principal one-step increments and the two lifts
    d = wrap(np.diff(np.angle(W)))
    phi_cs = np.concatenate([[theta[0]], theta[0] + np.cumsum(d)])
    ev = np.nonzero((ew[:-1] < 0) & (ew[1:] >= 0) & (rho[:-1] > 0) & (rho[1:] > 0))[0] + 1
    c = np.zeros(N + 1, dtype=np.int64); c[ev] = 1; c = np.cumsum(c)
    phi = theta + 2*np.pi*c
    cross = np.nonzero(np.floor(phi_cs[1:]/(2*np.pi)) > np.floor(phi_cs[:-1]/(2*np.pi)))[0] + 1
    T1 = dict(events=int(len(ev)), predicate_vs_lift_crossing_mismatch=int(len(np.setxor1d(ev, cross))),
              anchored_vs_cumsum_lift_maxdiff=float(np.max(np.abs(phi - phi_cs))),
              lift_increasing=bool(np.all(np.diff(phi) > 0)))
    # T2 one-step angle
    dev = d - np.pi/3
    bound_pt = np.arcsin(np.minimum(0.705*np.sqrt(Q[:-1]) + 0.257*Q[:-1], 0.99))
    T2 = dict(max_abs_dev=float(np.max(np.abs(dev))), B_bound=float(math.asin(EPS_B)),
              max_dev_over_sqrtQ=float(np.max(np.abs(dev)/np.sqrt(Q[:-1]))),
              pointwise_bound_violations=int(np.sum(np.abs(dev) > bound_pt)))
    # T3 anchors
    ev7 = ev[ev + 7 <= N]
    L5 = phi[ev7 + 5] - phi[ev7]; L6 = phi[ev7 + 6] - phi[ev7]; L7 = phi[ev7 + 7] - phi[ev7]
    Dl = 2*np.pi - L6
    T3 = dict(max_Lambda5=float(L5.max()), min_Lambda7=float(L7.min()), two_pi=2*math.pi,
              min_Delta=float(Dl.min()), Delta_over_Q_min=float((Dl/Q[ev7]).min()), Delta_over_Q_max=float((Dl/Q[ev7]).max()),
              tau=TAU, Delta_over_Q_minus_tau_over_sqrtQ_max=float(np.max(np.abs(Dl/Q[ev7] - TAU)/np.sqrt(Q[ev7]))))
    # T4 identity and criterion
    ev6 = ev[ev + 6 <= N]
    gaps = np.diff(ev6); s = np.concatenate([[0], np.cumsum(gaps == 7)])[:len(ev6)]
    over = phi[ev6] - 2*np.pi*np.floor(phi[ev6]/(2*np.pi))
    G = (np.pi/3)*np.arange(N + 1) - (phi - phi[0])
    const = G[ev6] - (np.pi/3)*s + over
    n0, l0 = int(ev6[0]), 1
    C_pred = (np.pi/3)*n0 - 2*np.pi*l0 + phi[0]
    D6 = 2*np.pi - (phi[ev6 + 6] - phi[ev6])
    crit_viol = int(np.sum((gaps == 7) != ((over[:-1] >= 0) & (over[:-1] < D6[:-1]))))
    T4 = dict(gap_alphabet=sorted(set(int(x) for x in gaps)), identity_spread=float(const.max() - const.min()),
              C_from_identity=float(const.mean()), C_predicted=float(C_pred), gap_criterion_violations=crit_viol,
              n0=n0, l0=l0, phi0=float(phi[0]))
    # Psi_inf on the W track (block phase) and on the z track (R9 estimator)
    Mend = N // 6; blk = np.arange(0, 6*Mend + 1, 6)
    ThetaW = phi[blk] - 2*np.pi*np.arange(Mend + 1)
    PsiW = ThetaW - TAU*np.log(Q[blk])
    out = dict(T1=T1, T2=T2, T3=T3, T4=T4, PsiW_end=float(PsiW[-1]), M_end=int(Mend), Q0=float(Q[0]))
    if with_chart:
        z, res = F2B.h_inv(W[blk]); q = np.abs(z)**2
        dz = wrap(np.diff(np.angle(z))); Thz0 = theta[0] + wrap(np.angle(z[0]) - np.angle(W[0]))
        Thz = np.concatenate([[Thz0], Thz0 + np.cumsum(dz)])
        Psiz = Thz - TAU*np.log(q)
        Phi = Psiz + q*g_avg(Thz)
        out.update(h_inv_residual=res, q0=float(q[0]), Theta_z0=float(Thz0), Psi_z0=float(Psiz[0]),
                   Psi_inf=float(Phi[-1]), Psi_inf_drift_last_decade=float(Phi[-1] - Phi[len(Phi)//10*9]),
                   PsiW_minus_Psiz_end=float(PsiW[-1] - Psiz[-1]), M_R9=float(Phi[-1] - Psiz[0]))
        Psi_inf = float(Phi[-1])
    else:
        Psi_inf = float(PsiW[-1])
    # T5 slip schedule
    L_pred = (np.pi/3)*n0 - 2*np.pi*l0 + Psi_inf
    starts = np.nonzero(gaps == 7)[0]
    a_true = 1.0/Q[0]
    sched = []
    for k, idx in enumerate(starts, start=1):
        n = int(ev6[idx]); Mk, rk = divmod(n, 6)
        if Mk == 0: continue
        Lk = TAU*math.log(Mk) - (k - 1)*math.pi/3
        Lk_psi = TAU*float(digamma(a_true + Mk)) - (k - 1)*math.pi/3
        sched.append(dict(k=k, n=n, M_k=Mk, r_k=rk, L_k_naive=Lk, naive_minus_L=Lk - L_pred,
                          harmonic_term=-TAU*math.log(1 + a_true/Mk), L_k_psi=Lk_psi, eps_k=Lk_psi - L_pred,
                          eps_over_sqrtQ=(Lk_psi - L_pred)*math.sqrt(a_true + Mk),
                          overshoot=float(over[idx]), Delta=float(D6[idx])))
    # record-only decoder: fit (a, L) to the slips, no state datum
    ks = np.array([x["k"] for x in sched], float); Ms = np.array([x["M_k"] for x in sched], float)
    def resid(p): return TAU*digamma(p[0] + Ms) - (ks - 1)*math.pi/3 - p[1]
    fit = least_squares(resid, x0=[Ms[0], TAU*math.log(Ms[-1]) - (ks[-1] - 1)*math.pi/3], bounds=([1.0, -np.inf], [np.inf, np.inf]))
    a_hat, L_hat = float(fit.x[0]), float(fit.x[1])
    decoder = dict(a_true=float(a_true), a_hat=a_hat, a_rel_err=(a_hat - a_true)/a_true, L_true=float(L_pred), L_hat=L_hat,
                   L_err=L_hat - L_pred, Psi_inf_hat_mod2pi=float((L_hat - (np.pi/3)*n0 + 2*np.pi*l0) % (2*np.pi)),
                   Psi_inf_true_mod2pi=float(Psi_inf % (2*np.pi)), n_slips_used=int(len(ks)))
    out.update(L_pred=float(L_pred), schedule=sched, decoder=decoder,
               M_ratios=[sched[i + 1]["M_k"]/sched[i]["M_k"] for i in range(len(sched) - 1)], ratio_target=math.exp(math.pi/(3*TAU)),
               record=dict(n0=n0, gap_word_counts={"6": int(np.sum(gaps == 6)), "7": int(np.sum(gaps == 7))}))
    return out

def start_from_W(W0):
    e = W0.imag/(S3/2); r = W0.real + e/2
    return r, e

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
    outp = sys.argv[2] if len(sys.argv) > 2 else "a1b_a1c_explicit_u.json"
    t0 = time.time(); results = {"N": N, "orbits": [], "fibers": []}
    # part 1: orbits in U
    for Q0 in (1/625, 1e-3, 4e-4):
        for th in (0.3, 1.7, 3.9, 5.1):
            W0 = math.sqrt(Q0)*complex(math.cos(th), math.sin(th))
            rho, eta = primitive_orbit(*start_from_W(W0), N)
            o = analyse(rho, eta, N); o.update(start=dict(Q0=Q0, theta0=th)); results["orbits"].append(o)
            s = o["schedule"]
            print(f"Q0={Q0:.2e} th={th}: ev {o['T1']['events']} mismatch {o['T1']['predicate_vs_lift_crossing_mismatch']} "
                  f"| maxdev {o['T2']['max_abs_dev']:.4f} (B {o['T2']['B_bound']:.4f}) dev/sqrtQ {o['T2']['max_dev_over_sqrtQ']:.3f} "
                  f"| L5max {o['T3']['max_Lambda5']:.3f} L7min {o['T3']['min_Lambda7']:.3f} Delta/Q [{o['T3']['Delta_over_Q_min']:.3f},{o['T3']['Delta_over_Q_max']:.3f}] "
                  f"| gaps {o['T4']['gap_alphabet']} spread {o['T4']['identity_spread']:.1e} crit {o['T4']['gap_criterion_violations']} "
                  f"| slips {len(s)} eps/sqrtQ last {s[-1]['eps_over_sqrtQ']:.3f} max {max(abs(x['eps_over_sqrtQ']) for x in s):.3f} "
                  f"| decoder a_hat {o['decoder']['a_hat']:.1f} (true {o['decoder']['a_true']:.1f}) L_err {o['decoder']['L_err']:.2e} drift {o['Psi_inf_drift_last_decade']:.1e}")
    # part 2: comparator fibers (same q0, delta = pi/6)
    q0 = (0.035)**2; delta = math.pi/6
    for alpha in (0.0, 0.5, 1.0, 1.5):
        pair = []
        for th in (alpha, alpha + delta):
            z0 = math.sqrt(q0)*complex(math.cos(th), math.sin(th)); W0 = complex(F2B.h_eval(np.array([z0]))[0])
            rho, eta = primitive_orbit(*start_from_W(W0), N)
            o = analyse(rho, eta, N); o.update(start=dict(q0=q0, theta_z=th)); pair.append(o)
        a, b = pair
        dPsi_true = b["Psi_inf"] - a["Psi_inf"]
        dM_true = float(wrap(dPsi_true - delta))
        dM_pred = q0*(lam1(alpha + delta) - lam1(alpha))
        # decode from the two records at each common slip count
        dec = []
        dn0 = (math.pi/3)*(b["T4"]["n0"] - a["T4"]["n0"])                         # l0 equal (=1)
        for ka, kb in zip(a["schedule"], b["schedule"]):
            k = ka["k"]
            dPsi_naive = float(wrap((kb["L_k_naive"] - ka["L_k_naive"]) - dn0 - dPsi_true)) + dPsi_true
            dPsi_psi = float(wrap((kb["L_k_psi"] - ka["L_k_psi"]) - dn0 - dPsi_true)) + dPsi_true   # true a's (upper bound)
            dec.append(dict(k=k, M_a=ka["M_k"], M_b=kb["M_k"], err_naive=dPsi_naive - dPsi_true, err_true_a=dPsi_psi - dPsi_true,
                            err_true_a_over_dM=(dPsi_psi - dPsi_true)/dM_true))
        dPsi_rec = float(wrap((b["decoder"]["L_hat"] - a["decoder"]["L_hat"]) - dn0 - dPsi_true)) + dPsi_true
        rec_only = dict(err=dPsi_rec - dPsi_true, err_over_dM=(dPsi_rec - dPsi_true)/dM_true,
                        blocks_needed_estimate=(0.5/abs(dM_true))**2 if dM_true != 0 else None)
        fib = dict(alpha=alpha, delta=delta, q0=q0, dPsi_true=dPsi_true, dM_true=dM_true, dM_R9_leading=dM_pred,
                   dM_true_minus_R9=dM_true - dM_pred, R9_bound_2C2q2=2*517*q0**2, decode=dec, record_only_decode=rec_only,
                   record_a=a["record"], record_b=b["record"])
        results["fibers"].append(fib)
        print(f"fiber alpha={alpha}: dPsi_true {dPsi_true:.6f} dM_true {dM_true:.3e} R9 lead {dM_pred:.3e} (diff {dM_true-dM_pred:.1e}, bound {2*517*q0**2:.1e}); "
              f"decode err last slip k={dec[-1]['k']}: naive {dec[-1]['err_naive']:.1e}, true-a {dec[-1]['err_true_a']:.1e} (|/dM| {abs(dec[-1]['err_true_a_over_dM']):.0f}); "
              f"record-only {rec_only['err']:.1e} (|/dM| {abs(rec_only['err_over_dM']):.0f})")
    results["seconds"] = time.time() - t0
    json.dump(results, open(outp, "w"), indent=1)
    print("done", f"{results['seconds']:.0f}s")

if __name__ == "__main__":
    main()
