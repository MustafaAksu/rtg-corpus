#!/usr/bin/env python3
r"""
recog_cell_f2b_token_bridge.py — RECOG OPEN R6 / CELL-F2(b): eventwise token test.   [NUM]  (binary64; nothing here is a certificate)

(rep:) primitive lift (rho, eta); raw P1 eigenframe W = rho + omega*eta_wrap, omega = e^{2 pi i/3}  (= Number Genesis section angle
       theta = atan2(sqrt3*eta_wrap, 2 rho - eta_wrap) = arg W);  NF chart z = h^{-1}(W), h = DYAD-ALG-NF6 one-step conjugacy (degree 6).
(transport:) primitive T(rho, eta) = (rho - sin eta, eta + e^rho - 1 - sin eta).

Owner definitions imported literally from RTG_NUMBER_GENESIS_DSN_v1.20.6 (GAP-LOCK Lemmas 1-3) and its GAP-LOCK v2 certificate:
  phi_hat_n       increasing lift of arg W(x_n).  Owner construction: accumulated wrapped differences. IMPLEMENTATION (rev. 2): event-anchored,
                  phi_hat_n = theta_n + 2 pi c_n with theta_n = arg W_n in [0, 2 pi) and c_n = # literal B-events up to n. Mathematically
                  identical to the owner lift; numerically drift-free. (rev. 1 used np.cumsum; over ~4e6 steps its ~1e-9 rounding drift
                  mis-floored one near-section event on one orbit — overshoot ~2 pi instead of ~0. The cumsum lift is kept as a diagnostic.)
  B-event         transition x -> Tx with eta_wrap(x) < 0 <= eta_wrap(Tx) and rho > 0 on both sides; event_step n_j := index of Tx
  gap_next_j      n_{j+1} - n_j  (attached to the START anchor n_j);   s_j = # 7-gaps among the first j returns
  overshoot_j     phi_hat_{n_j} - 2 pi floor(phi_hat_{n_j} / 2 pi)
  Lambda6_j       phi_hat_{n_j + 6} - phi_hat_{n_j};   Delta_j = 2 pi - Lambda6_j
  G_n             (pi/3) n - (phi_hat_n - phi_hat_0);   G_{6M} = D_M
  slip k          start anchor n_{j_k} with gap_next = 7;  slip_start_step = n_{j_k}, slip_end_step = n_{j_k + 1};
                  M_k_phys, r_k from n_{j_k} = 6 M_k_phys + r_k  (start-anchor convention of the GAP-LOCK proof)
F2(b1) owner reproduction checks:   G_{n_j} - (pi/3) s_j + overshoot_j = const;   gap_next_j = 7  <=>  0 <= overshoot_j < Delta_j;
                                     gaps in {6,7};  literal B-event predicate == lifted-phase 2 pi crossings.
F2(b2) chart bridge:   a_n = arg(z_n / W_n);  L^h_n = (pi/3) n - (Theta_hat^h_n - Theta_hat^h_0);  identity L^h_n - G_n = a_0 - a_n;
                       aligned residual  delta~_n = L^h_n - G_n - a_0 = -a_n.
PREREGISTERED predictions (from h_2, [ALG] leading order):
  (P1) at 7-gap START anchors (overshoot < Delta_j = O(Q), phase at the section):  delta~_{n_j} / sqrt(Q_j) -> -sqrt3/8 = -0.216506
  (P1') at generic B-events (overshoot up to ~pi/3):  delta~_{n_j} / sqrt(Q_j) -> -f(arg W_{n_j})   [consistency check]
  (P2) at block states 6m:        a_{6m} / sqrt(Q_{6m}) -> f(theta_{6m}),
                                  f(t) = sin(t + pi/3)/6 - sin(t)/3 + sin(3t + pi/3)/12
  (P3) slip displacement:         level l_k := G_{6 M_k_phys} (block-sampled raw lag at the slip);
                                  m_h(k) := first block m with G_{6m} - a_{6m} >= l_k;   Delta_m_k := m_h(k) - M_k_phys;
                                  Delta_m_k * sqrt(Q_k) -> f(-r_k pi/3) / tau  =  +3/16 for r_k in {0,1,2},  -3/16 for r_k in {3,4,5}
                                  (h-track LATER for r_k in {0,1,2}, EARLIER for r_k in {3,4,5}); tau = 2 sqrt3 / 3.
Usage:  python recog_cell_f2b_token_bridge.py [N_steps] [out.json] [r0 th0]   (default 4,000,000 steps, 12 orbits; optional single orbit)
"""
import sys, json, math, time, hashlib
import numpy as np

TAU = 2*math.sqrt(3)/3
OM = complex(-0.5, math.sqrt(3)/2)
LAM = complex(0.5, math.sqrt(3)/2)            # e^{i pi/3}: one-step linear part (1 + omega)
DEG = 6

# ---------------- h: one-step normal-form conjugacy (DYAD-ALG-NF6 convention: resonant coefficients of h vanish) ----------------
def pmul(A, B):
    C = {}
    for (i, j), a in A.items():
        for (k, l), b in B.items():
            if i + j + k + l <= DEG: C[(i+k, j+l)] = C.get((i+k, j+l), 0) + a*b
    return C
def padd(A, B, s=1):
    C = dict(A)
    for k, v in B.items(): C[k] = C.get(k, 0) + s*v
    return C
def pscal(A, s): return {k: v*s for k, v in A.items()}
def ppow(A, n):
    R = {(0, 0): 1+0j}
    for _ in range(n): R = pmul(R, A)
    return R
def pconj(A): return {(j, i): v.conjugate() for (i, j), v in A.items()}
def pcomp(F, G):                             # F(G, conj G) for a single component F
    R = {}
    for (i, j), c in F.items(): R = padd(R, pscal(pmul(ppow(G[0], i), ppow(G[1], j)), c))
    return R
Z, Zb = {(1, 0): 1+0j}, {(0, 1): 1+0j}
eta = pscal(padd(Z, Zb, -1), 1/(OM - OM.conjugate())); rho = padd(Z, pscal(eta, -OM))
sin_eta = {}
for k in range(0, DEG):
    n = 2*k + 1
    if n > DEG: break
    sin_eta = padd(sin_eta, pscal(ppow(eta, n), (-1)**k/math.factorial(n)))
expm1_rho = {}
for n in range(1, DEG + 1): expm1_rho = padd(expm1_rho, pscal(ppow(rho, n), 1/math.factorial(n)))
rho1 = padd(rho, sin_eta, -1); eta1 = padd(padd(eta, expm1_rho), sin_eta, -1)
F1 = padd(rho1, pscal(eta1, OM))
h = dict(Z); nmap = {(1, 0): LAM}
for k in range(2, DEG + 1):
    lhs = pcomp(F1, [h, pconj(h)]); rhs = pcomp(h, [nmap, pconj(nmap)])
    K = {kk: v for kk, v in padd(lhs, rhs, -1).items() if sum(kk) == k}
    for (a, b), v in K.items():
        if (a - b - 1) % 6 == 0: nmap[(a, b)] = nmap.get((a, b), 0) + v
        else: h[(a, b)] = h.get((a, b), 0) - v/(LAM - LAM**a * LAM.conjugate()**b)
s3 = math.sqrt(3)
H2_REG = {(2, 0): -(1 + 1j*s3)/12, (1, 1): -1/3 + 0j, (0, 2): (1 - 1j*s3)/24}
h2_err = max(abs(h.get(k, 0) - v) for k, v in H2_REG.items())
assert h2_err < 1e-12, f"h_2 does not match the registered DYAD-ALG-NF6 h_2 (err {h2_err})"
HT = [((a, b), c) for (a, b), c in h.items() if abs(c) > 0 and (a, b) != (1, 0)]
def h_eval(z):
    zc = np.conj(z); out = z.copy()
    for (a, b), c in HT: out += c * z**a * zc**b
    return out
def h_inv(W, iters=40):
    z = W.copy()
    for _ in range(iters): z = W - (h_eval(z) - z)
    return z, float(np.max(np.abs(h_eval(z) - W)))
def f_shadow(t): return np.sin(t + np.pi/3)/6 - np.sin(t)/3 + np.sin(3*t + np.pi/3)/12

# ---------------- one orbit ----------------
def wrap(x): return (x + np.pi) % (2*np.pi) - np.pi
def lift(theta):
    d = wrap(np.diff(theta)); out = np.empty_like(theta); out[0] = theta[0]; out[1:] = theta[0] + np.cumsum(d); return out
def run_orbit(r0, th0, N):
    W0 = r0*complex(math.cos(th0), math.sin(th0)); e = W0.imag/(s3/2); r = W0.real + e/2
    rho_a = np.empty(N + 1); eta_a = np.empty(N + 1); rho_a[0], eta_a[0] = r, e
    sin, expm1 = math.sin, math.expm1
    for n in range(1, N + 1):
        s = sin(e); r, e = r - s, e + expm1(r) - s
        rho_a[n] = r; eta_a[n] = e
    ew = wrap(eta_a); W = rho_a + OM*ew
    assert np.max(np.abs(W)) <= 0.09, "left the NF-INV inverse domain |W| <= 9/100"
    Q = np.abs(W)**2
    # literal B-event predicate (the owner token) and the event-anchored lift
    ev = np.nonzero((ew[:-1] < 0) & (ew[1:] >= 0) & (rho_a[:-1] > 0) & (rho_a[1:] > 0))[0] + 1
    theta = np.mod(np.angle(W), 2*np.pi)
    c = np.zeros(N + 1, dtype=np.int64); c[ev] = 1; c = np.cumsum(c)
    phi = theta + 2*np.pi*c
    assert np.all(np.diff(phi) > 0), "anchored lift not increasing: predicate and principal angle disagree"
    G = (np.pi/3)*np.arange(N + 1) - (phi - phi[0])
    phi_cs = lift(np.angle(W)); phi_cs += phi[0] - phi_cs[0]                  # rev.1 cumsum lift, diagnostic only
    cross = np.nonzero(np.floor(phi_cs[1:]/(2*np.pi)) > np.floor(phi_cs[:-1]/(2*np.pi)))[0] + 1
    pred_mismatch = int(len(np.setxor1d(ev, cross)))                          # diagnostic: predicate vs cumsum-lift crossings
    cumsum_drift = float(np.max(np.abs(phi_cs - phi)))
    ev = ev[ev + 6 <= N]
    gaps = np.diff(ev); s = np.concatenate([[0], np.cumsum(gaps == 7)])[:len(ev)]
    over = phi[ev] - 2*np.pi*np.floor(phi[ev]/(2*np.pi))
    Lam6 = phi[ev + 6] - phi[ev]; Dl = 2*np.pi - Lam6
    const = G[ev] - (np.pi/3)*s + over
    crit = ((gaps == 7) == ((over[:-1] >= 0) & (over[:-1] < Dl[:-1])))
    # chart bridge
    z = np.empty_like(W); res = 0.0
    for c0 in range(0, N + 1, 500000):
        z[c0:c0+500000], rr = h_inv(W[c0:c0+500000]); res = max(res, rr)
    a = np.angle(z/W); Th = lift(np.angle(z)); Lh = (np.pi/3)*np.arange(N + 1) - (Th - Th[0])
    ident = float(np.max(np.abs(Lh - G - (a[0] - a))))
    # P1 at event anchors
    P1 = (-a[ev])/np.sqrt(Q[ev]); P1g = P1 + f_shadow(np.angle(W[ev]))          # generic-event residual (P1')
    # P2 at block states
    blk = np.arange(0, N + 1, 6); P2res = (a[blk]/np.sqrt(Q[blk]) - f_shadow(np.angle(W[blk])))
    # slips and P3
    starts = np.nonzero(gaps == 7)[0]
    Gb = G[blk]; Lt = Gb - a[blk]; slips = []
    for idx in starts:
        n = int(ev[idx]); M, rk = divmod(n, 6); lvl = Gb[M]
        mh = int(np.argmax(Lt >= lvl)) if np.any(Lt >= lvl) else None
        Qk = float(Q[6*M]); pred = float(f_shadow(-rk*np.pi/3)/TAU)
        slips.append(dict(slip_start_step=n, slip_end_step=int(ev[idx + 1]), M_k_phys=M, r_k=rk, Q_k=Qk,
                          overshoot=float(over[idx]), Delta=float(Dl[idx]),
                          delta_tilde_over_sqrtQ=float(P1[idx]),
                          Delta_m=(None if mh is None else mh - M),
                          Delta_m_sqrtQ=(None if mh is None else (mh - M)*math.sqrt(Qk)), pred_Delta_m_sqrtQ=pred))
    Ms = [sl['M_k_phys'] for sl in slips]
    return dict(r0=r0, theta0=th0, N=N, events=int(len(ev)), gaps_set=sorted(set(gaps.tolist())), pred_vs_cumsum_lift_mismatch_diag=pred_mismatch,
                cumsum_lift_drift_diag=cumsum_drift,
                event_identity_spread=float(const.max() - const.min()), gap_criterion_violations=int((~crit).sum()),
                h_inverse_residual=res, Lh_identity_max_err=ident,
                P1_slip_anchor_values=[float(P1[i]) for i in np.nonzero(gaps == 7)[0]], P1_target=-s3/8,
                P1prime_generic_maxabs_late_over_sqrtQ=float(np.max(np.abs(P1g[len(P1g)//2:]) / np.sqrt(Q[ev][len(P1g)//2:]))),
                P2_maxabs_residual_late_over_sqrtQ=float(np.max(np.abs(P2res[len(P2res)//2:]) / np.sqrt(Q[blk][len(P2res)//2:]))),
                slips=slips, M_ratios=[Ms[i+1]/Ms[i] for i in range(len(Ms) - 1)], ratio_target=math.exp(math.pi/(3*TAU)))

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4_000_000
    out = sys.argv[2] if len(sys.argv) > 2 else "f2b_results.json"
    t0 = time.time(); res = []
    grid = [(float(sys.argv[3]), float(sys.argv[4]))] if len(sys.argv) > 4 else [(r, t) for r in (0.05, 0.035, 0.025) for t in (0.3, 1.7, 3.9, 5.1)]
    for r0, th0 in grid:
        if True:
            o = run_orbit(r0, th0, N); res.append(o)
            print(f"r0={r0} th0={th0}: events {o['events']}, gaps {o['gaps_set']}, [diag: cumsum drift {o['cumsum_lift_drift_diag']:.1e}, cumsum-crossing mismatch {o['pred_vs_cumsum_lift_mismatch_diag']}], "
                  f"identity spread {o['event_identity_spread']:.2e}, gap-criterion violations {o['gap_criterion_violations']}, "
                  f"L^h identity err {o['Lh_identity_max_err']:.1e}, P1 at slip anchors {[round(x,4) for x in o['P1_slip_anchor_values']]} (target {-s3/8:+.4f}), "
                  f"slips {len(o['slips'])}  [{time.time()-t0:.0f}s]", flush=True)
    sl = [s for o in res for s in o['slips'] if s['Delta_m'] is not None]
    late = sorted(sl, key=lambda s: s['Q_k'])[:max(1, len(sl)//2)]           # smaller Q = more asymptotic
    by = {}
    for s in late: by.setdefault(s['r_k'], []).append(s['Delta_m_sqrtQ'])
    print("\nP3 (late half of slips, by residue r_k):   predicted +0.1875 for r in {0,1,2}, -0.1875 for r in {3,4,5}")
    for r in sorted(by): print(f"   r_k={r}: n={len(by[r])}, mean Delta_m*sqrt(Q) = {np.mean(by[r]):+.4f}, range [{min(by[r]):+.3f}, {max(by[r]):+.3f}]")
    summary = dict(script_sha256=hashlib.sha256(open(__file__, 'rb').read()).hexdigest(), numpy=np.__version__, python=sys.version.split()[0],
                   owner_source="RTG_NUMBER_GENESIS_DSN_v1.20.6 (record its sha256 alongside this file)", h2_check_err=h2_err,
                   N=N, orbits=res, P3_late_by_residue={str(r): dict(n=len(v), mean=float(np.mean(v))) for r, v in by.items()},
                   seconds=round(time.time() - t0, 1), grade="[NUM]")
    json.dump(summary, open(out, "w"), indent=1); print(f"\nwritten {out}")
