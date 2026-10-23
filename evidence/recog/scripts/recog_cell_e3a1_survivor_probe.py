#!/usr/bin/env python3
r"""
recog_cell_e3a1_survivor_probe.py — RECOG OPEN R7 / CELL-E3A-1: Stage-2 survivor probe by adaptive escape-time refinement.   [NUM]
(binary64 with mpmath spot checks; nothing here is a certificate)

(rep:) primitive lift (rho, eta); raw P1 eigenframe W = rho + omega*eta (omega = e^{2 pi i/3}), Q = |W|^2, W = sqrt(Q) e^{i theta}.
(transport:) twin T_s(rho, eta) = (rho - sin eta, eta + sinh rho - sin eta);  D_s = det DT_s = 1 + (cosh rho - 1) cos eta.
Domain: the E2B annulus A = {7/200 <= Q < 58107/1600000}, half-annulus theta in [0, pi): exact oddness T_s(-x) = -T_s(x) and D_s(-x) = D_s(x)
        make the other half redundant. Cells are dyadic in (Q, theta): at depth d, cell (iq, it) has exact edges
        Q in [q1 + (q2-q1) iq / (NQ 2^d), q1 + (q2-q1)(iq+1)/(NQ 2^d)],  theta in [pi it / (NT 2^d), pi (it+1) / (NT 2^d)].
Escape time (STRICT, as in Stage 2):  tau_-(x) = inf{ n >= 0 : D_s(T_s^n x) < 0 };  |D_s| < 1e-12 events are logged separately.
Question (preregistered): does adaptive refinement produce a NESTED locus whose escape time keeps diverging with refinement?
Outcomes:  PLATEAU          tau_max stops increasing over several depths and no nested growing chain   -> supports attempting the universal IA proof
                            (does NOT prove absence of an exceptional orbit)
           COHERENT-GROWTH  a nested chain C_0 > C_1 > ... with tau increasing; if its slope per level approaches
                            log 2 / log|lambda_1| = 0.74919 (|lambda_1| = sqrt(cosh arsinh 2pi) = 2.52235) -> p_1-preimage candidate,
                            otherwise generic survivor candidate.  Seeds E3A-2 (local Newton for T_s^n x = (rho_k, 2 pi l) on the right lift).
           UNRESOLVED       intermittent growth, maximisers jumping among unrelated regions, or the float64 precision floor reached
                            before plateau/growth can be distinguished.
The automatic label printed at the end is ADVISORY; the classification is made by review of the per-depth table and chains.
Usage:  python recog_cell_e3a1_survivor_probe.py [NQ] [NT] [max_depth] [out_prefix]     (defaults 64 4096 40 e3a1)
"""
import sys, json, math, time, hashlib
import numpy as np
from fractions import Fraction as Fr

NQ = int(sys.argv[1]) if len(sys.argv) > 1 else 64
NT = int(sys.argv[2]) if len(sys.argv) > 2 else 4096
DMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 40
OUT = sys.argv[4] if len(sys.argv) > 4 else "e3a1"
NMAX, DTAU, KEEP, CAP, NEARZERO, PERT = 1000, 3, 512, 16384, 1e-12, 1e-11
Q1, Q2 = Fr(7, 200), Fr(58107, 1600000)
q1, q2 = float(Q1), float(Q2)
S3 = math.sqrt(3)
LAM1 = math.sqrt(math.cosh(math.asinh(2*math.pi)))
SLOPE_P1 = math.log(2)/math.log(LAM1)
SRC = [(s*math.asinh(2*math.pi*k), k, s) for k in (1, 2, 3) for s in (1, -1)]   # winding sources p_{+-k} on the cylinder (eta = 0)

def lift_from_QT(Q, th):
    W = np.sqrt(Q)*np.exp(1j*th); eta = W.imag/(S3/2); rho = W.real + eta/2
    return rho, eta
def escape(rho, eta, track=True):
    """vectorised: returns tau (NMAX+1 = no escape), nearzero flag, per-source min cylinder distance and step before escape"""
    n_pts = rho.size; tau = np.full(n_pts, NMAX + 1); nz = np.zeros(n_pts, bool)
    dmin = np.full((len(SRC), n_pts), np.inf); nnear = np.zeros((len(SRC), n_pts), int)
    act = np.ones(n_pts, bool); r, e = rho.copy(), eta.copy()
    for n in range(NMAX + 1):
        idx = np.nonzero(act)[0]
        if idx.size == 0: break
        rr, ee = r[idx], e[idx]
        D = 1 + (np.cosh(rr) - 1)*np.cos(ee)
        nz[idx] |= np.abs(D) < NEARZERO
        hit = D < 0
        tau[idx[hit]] = n; act[idx[hit]] = False
        if track:
            keep = idx[~hit]; ew = (e[keep] + np.pi) % (2*np.pi) - np.pi
            for si, (rk, k, s) in enumerate(SRC):
                dd = np.hypot(r[keep] - rk, ew)
                better = dd < dmin[si, keep]; dmin[si, keep[better]] = dd[better]; nnear[si, keep[better]] = n
        idx = idx[~hit]
        if n == NMAX or idx.size == 0: break
        s_ = np.sin(e[idx]); r[idx], e[idx] = r[idx] - s_, e[idx] + np.sinh(r[idx]) - s_
    return tau, nz, dmin, nnear
def centres(d, iq, it):
    nq, nt = NQ*2**d, NT*2**d
    Q = q1 + (q2 - q1)*(iq + 0.5)/nq; th = math.pi*(it + 0.5)/nt
    return Q, th
def tau_mp(Q, th, dps=40):
    import mpmath as mp
    mp.mp.dps = dps
    W = mp.sqrt(mp.mpf(Q))*mp.e**(1j*mp.mpf(th)); e = mp.im(W)/(mp.sqrt(3)/2); r = mp.re(W) + e/2
    for n in range(NMAX + 1):
        if 1 + (mp.cosh(r) - 1)*mp.cos(e) < 0: return n
        s = mp.sin(e); r, e = r - s, e + mp.sinh(r) - s
    return NMAX + 1

t0 = time.time()
meta = dict(script_sha256=hashlib.sha256(open(__file__, 'rb').read()).hexdigest(), numpy=np.__version__, python=sys.version.split()[0],
            NQ=NQ, NT=NT, DMAX=DMAX, NMAX=NMAX, DTAU=DTAU, KEEP=KEEP, CAP=CAP, NEARZERO=NEARZERO, PERT=PERT, q1=str(Q1), q2=str(Q2),
            half_annulus="theta in [0, pi)", lambda1=LAM1, slope_p1_per_level=SLOPE_P1, grade="[NUM]")
# ---------------- depth 0: uniform pass ----------------
iq0, it0 = np.meshgrid(np.arange(NQ), np.arange(NT), indexing='ij'); iq0, it0 = iq0.ravel(), it0.ravel()
Qc, Tc = centres(0, iq0, it0); rho, eta = lift_from_QT(Qc, Tc)
tau, nz, dmin, nnear = escape(rho, eta)
cells = dict(d=np.zeros(iq0.size, int), iq=iq0, it=it0, tau=tau, nz=nz, dmin=dmin, nnear=nnear, parent=np.full(iq0.size, -1))
print(f"[d=0] {iq0.size} cells, tau range [{tau.min()}, {tau.max()}], no-escape {int((tau > NMAX).sum())}, near-zero-D {int(nz.sum())}  [{time.time()-t0:.0f}s]", flush=True)
rows, late_records, chains_prev = [], [], {}
cur = cells; uid_base = 0
def cluster_count(d, iq, it):
    S = set(zip(iq.tolist(), it.tolist())); seen = set(); c = 0; ntot = NT*2**d
    for p in S:
        if p in seen: continue
        c += 1; stack = [p]; seen.add(p)
        while stack:
            a, b = stack.pop()
            for da in (-1, 0, 1):
                for db in (-1, 0, 1):
                    nb = (a + da, (b + db) % ntot)
                    if nb in S and nb not in seen: seen.add(nb); stack.append(nb)
    return c
chain = {}                       # (d, iq, it) -> chain length of consecutive late ancestors
tau_of = {}; cum_max = 0; chain_tau = []
floor_hit = None
for d in range(0, DMAX + 1):
    tau_c = cur['tau']; tmax = int(tau_c.max()); t999 = float(np.quantile(tau_c, 0.999))
    band = np.nonzero(tau_c >= tmax - DTAU)[0]; topk = np.argsort(-tau_c)[:KEEP]      # Delta_tau band PLUS top-KEEP cells
    late = np.union1d(band, topk)
    if late.size > CAP: late = late[np.argsort(-tau_c[late])[:CAP]]
    cum_max = max(cum_max, tmax)
    # precision check: re-evaluate late centres with a tiny theta offset
    Ql, Tl = centres(d, cur['iq'][late], cur['it'][late])
    rp, ep = lift_from_QT(Ql, Tl*(1 + PERT)); taup, _, _, _ = escape(rp, ep, track=False)
    noisy = float(np.mean(np.abs(taup - tau_c[late]) > 1))
    # chains
    for k in late:
        key = (d, int(cur['iq'][k]), int(cur['it'][k])); pk = (d - 1, int(cur['iq'][k])//2, int(cur['it'][k])//2)
        chain[key] = chain.get(pk, 0) + 1; tau_of[key] = int(cur['tau'][k])
    clen = max(chain[(d, int(cur['iq'][k]), int(cur['it'][k]))] for k in late)
    # tau sequence along the deepest chain ending at the latest cell of the longest chains
    best = max(late, key=lambda k: (chain[(d, int(cur['iq'][k]), int(cur['it'][k]))], int(cur['tau'][k])))
    key = (d, int(cur['iq'][best]), int(cur['it'][best])); seq = []
    while key in tau_of: seq.append(tau_of[key]); key = (key[0] - 1, key[1]//2, key[2]//2)
    chain_tau = seq[::-1]
    si1 = 0; j = late[np.argmin(cur['dmin'][si1, late])]
    ncl = cluster_count(d, cur['iq'][late], cur['it'][late])
    # mpmath spot check of the 4 latest cells
    top = late[np.argsort(-tau_c[late])[:4]]; mp_ok = []
    for k in top:
        Qk, Tk = centres(d, cur['iq'][k], cur['it'][k]); mp_ok.append(int(tau_mp(Qk, Tk)) == int(tau_c[k]))
    epsQ, epsT = (q2 - q1)/(NQ*2**d), math.pi/(NT*2**d)
    row = dict(d=d, N_active=int(tau_c.size), epsQ=epsQ, epsTheta=epsT, tau_max=tmax, tau_max_cumulative=cum_max, tau_999=t999, chain_tau_tail=chain_tau[-8:], n_late=int(late.size),
               clusters=ncl, longest_chain=clen, d_p1_min=float(cur['dmin'][si1, j]), n_near_p1=int(cur['nnear'][si1, j]),
               no_escape=int((tau_c > NMAX).sum()), near_zero_D=int(cur['nz'].sum()), noisy_frac=noisy, mp_agree=f"{sum(mp_ok)}/{len(mp_ok)}")
    rows.append(row)
    print(f"[d={d:2d}] active {row['N_active']:6d}  eps=({epsQ:.2e},{epsT:.2e})  tau_max {tmax}  tau_99.9 {t999:.1f}  late {row['n_late']}  "
          f"clusters {ncl}  chain {clen} tail {chain_tau[-6:]}  d_p1 {row['d_p1_min']:.3f}@{row['n_near_p1']}  noisy {noisy:.2f}  mp {row['mp_agree']}  [{time.time()-t0:.0f}s]", flush=True)
    for k in late:
        nq_, nt_ = NQ*2**d, NT*2**d; iqk, itk = int(cur['iq'][k]), int(cur['it'][k])
        late_records.append(dict(d=d, iq=iqk, it=itk,
            Q_bounds=[str(Q1 + (Q2 - Q1)*Fr(iqk, nq_)), str(Q1 + (Q2 - Q1)*Fr(iqk + 1, nq_))],
            theta_bounds_over_pi=[str(Fr(itk, nt_)), str(Fr(itk + 1, nt_))],
            parent=[d - 1, iqk//2, itk//2] if d > 0 else None, tau_centre=int(cur['tau'][k]),
            terminal=("no-escape" if cur['tau'][k] > NMAX else ("near-zero-D" if cur['nz'][k] else "escaped")),
            closest=[dict(k=SRC[si][1], sign=SRC[si][2], dmin=float(cur['dmin'][si, k]), n_near=int(cur['nnear'][si, k])) for si in range(len(SRC))]))
    if noisy > 0.5:
        floor_hit = d; print(f"   precision floor reached at depth {d} (more than half of late cells change tau under a {PERT:g} relative offset)"); break
    if d == DMAX: break
    # refine: four children of every late cell
    ciq = np.concatenate([2*cur['iq'][late] + a for a in (0, 1) for b in (0, 1)])
    cit = np.concatenate([2*cur['it'][late] + b for a in (0, 1) for b in (0, 1)])
    Qc, Tc = centres(d + 1, ciq, cit); rho, eta = lift_from_QT(Qc, Tc)
    tau, nz, dmin, nnear = escape(rho, eta)
    cur = dict(iq=ciq, it=cit, tau=tau, nz=nz, dmin=dmin, nnear=nnear)

# ---------------- advisory classification ----------------
K = 5
ct = chain_tau                                   # tau along the deepest nested chain (final depth)
slope = None; growth = plateau = False
if len(ct) > K:
    y = np.array(ct[-K-1:], float); slope = float(np.polyfit(np.arange(len(y)), y, 1)[0])
    nondecr = bool(np.all(np.diff(y) >= -1))
    growth = nondecr and slope >= 0.3
    plateau = abs(slope) < 0.15
cm = [r['tau_max_cumulative'] for r in rows]
plateau = plateau or (len(cm) > K and cm[-1] - cm[-1-K] < 1 and not growth)
if floor_hit is not None and not growth: label = "UNRESOLVED (precision floor before a decisive trend)"
elif growth and rows[-1]['longest_chain'] >= K:
    label = "COHERENT-GROWTH (" + ("p_1-preimage candidate" if slope is not None and abs(slope - SLOPE_P1) < 0.15 else "generic survivor candidate") + ")"
elif plateau and rows[-1]['longest_chain'] < K: label = "PLATEAU"
else: label = "UNRESOLVED"
print(f"\nadvisory label: {label}   (last-{K}-depth slope {slope}, p_1 fingerprint {SLOPE_P1:.5f} per level)")
json.dump(dict(meta=meta, per_depth=rows, advisory_label=label, slope_last=slope, deepest_chain_tau=ct, precision_floor_depth=floor_hit,
               seconds=round(time.time() - t0, 1)), open(f"{OUT}_summary.json", "w"), indent=1)
with open(f"{OUT}_late_cells.jsonl", "w") as f:
    for r in late_records: f.write(json.dumps(r) + "\n")
print(f"written {OUT}_summary.json, {OUT}_late_cells.jsonl  [{time.time()-t0:.0f}s]")
