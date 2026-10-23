#!/usr/bin/env python3
r"""
recog_cell_e1_twin_survey.py — RECOG OPEN R7 / CELL-E1: global fate survey of the expansive symmetric twin.  [NUM]
(rep:) primitive-lift (rho, eta), P1 eigenframe W = rho + omega eta (omega = e^{2 pi i/3}), Q = |W|^2 = rho^2 - rho eta + eta^2.
(transport:) T_s(rho,eta) = (rho - sin eta, eta + sinh rho - sin eta);  control: primitive T (e^rho - 1 in place of sinh rho).
D_s = det DT_s = 1 + (cosh rho - 1) cos eta;  C0^(s) = {|rho| >= arccosh 2, cos eta = -1/(cosh rho - 1)}.
Questions: (1) do small nonzero seeds near P1 leave the NF neighbourhood?  (2) if so, is C0^(s) reached, or is there an
intervening bounded/invariant region?  (3) is there a reproducible first-hit geometry suggesting a certified route?
Does NOT assume Re mu_6^(s) > 0  =>  C0^(s) globally accessible (that implication is R7).
Classes per seed (first event wins): RANK = first n with D <= 0; ESCAPE = |rho| > RHO_ESC with D > 0 so far;
RETURN = left Q > Q_EXIT then later Q < Q0/4; BOUNDED = left Q > Q_EXIT, none of the above by NMAX; LOCAL = never left Q <= Q_EXIT.
Built-in symmetry check: T_s is odd, so x_n(-z0) = -x_n(z0) and D_s histories of antipodal seeds must coincide exactly.
Floating point (binary64); nothing here is a certificate.
"""
import numpy as np, json, sys, hashlib, time
om = np.exp(2j*np.pi/3); s32 = np.sqrt(3)/2
def seeds_to_lift(z):
    eta = z.imag/s32; rho = z.real + eta/2
    return rho, eta
def Ts(r, e): s = np.sin(e); return r - s, e + np.sinh(r) - s
def Tp(r, e): s = np.sin(e); return r - s, e + np.expm1(r) - s
def Ds(r, e): return 1 + (np.cosh(r) - 1)*np.cos(e)
def Dp(r, e): return 1 + np.expm1(r)*np.cos(e)
Q_EXIT, RHO_ESC, NMAX = 1/400, 50.0, 200000
def run(mapf, detf, r0, th, record=False, z0=None):
    z0 = r0*np.exp(1j*th) if z0 is None else z0; rho, eta = seeds_to_lift(z0)
    Q0 = np.abs(z0)**2; n_seed = len(th)
    cls = np.array(["LOCAL"]*n_seed, dtype=object); n_exit = np.full(n_seed, -1); n_hit = np.full(n_seed, -1)
    hit_rho = np.full(n_seed, np.nan); hit_eta = np.full(n_seed, np.nan); exited = np.zeros(n_seed, bool); done = np.zeros(n_seed, bool)
    qmax = Q0.copy(); dhist = [] if record else None
    for n in range(1, NMAX + 1):
        act = ~done
        if not act.any(): break
        rho[act], eta[act] = mapf(rho[act], eta[act])
        d = detf(rho, eta); Q = rho*rho - rho*eta + eta*eta
        if record: dhist.append(d.copy())
        newexit = act & ~exited & (Q > Q_EXIT); n_exit[newexit] = n; exited |= newexit
        qmax = np.where(act, np.maximum(qmax, Q), qmax)
        h = act & (d <= 0); cls[h] = "RANK"; n_hit[h] = n; hit_rho[h] = rho[h]; hit_eta[h] = eta[h]; done |= h
        es = act & ~done & (np.abs(rho) > RHO_ESC); cls[es] = "ESCAPE"; done |= es
        rt = act & ~done & exited & (Q < Q0/4); cls[rt] = "RETURN"; done |= rt
    cls[~done & exited] = "BOUNDED"
    return dict(cls=cls, n_exit=n_exit, n_hit=n_hit, hit_rho=hit_rho, hit_eta=hit_eta, qmax=qmax, dhist=dhist)
t0 = time.time(); out = dict(meta=dict(script_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(), numpy=np.__version__,
     Q_EXIT=Q_EXIT, RHO_ESC=RHO_ESC, NMAX=NMAX, tag="[NUM]"), rows=[])
NTH = 120; th = np.linspace(0, np.pi/3, NTH, endpoint=False)
# symmetry check (twin), r0 = 0.05: antipodal seeds by EXACT negation (re^{i(th+pi)} is not bit-exactly -re^{i th} in binary64)
z0 = 0.05*np.exp(1j*th)
a = run(Ts, Ds, 0.05, th, record=True, z0=z0.copy()); b = run(Ts, Ds, 0.05, th, record=True, z0=-z0)   # exact negation, not th+pi
L = min(len(a['dhist']), len(b['dhist']))
sym = max(np.max(np.abs(np.nan_to_num(a['dhist'][k]) - np.nan_to_num(b['dhist'][k]))) for k in range(L))
same_cls = bool(np.all(a['cls'] == b['cls'])); same_hit = bool(np.all(a['n_hit'] == b['n_hit']))
print(f"[CHECK] odd symmetry: max |D(z0) - D(-z0)| over {L} steps = {sym:.2e}; classes equal: {same_cls}; hit steps equal: {same_hit}")
out['meta']['symmetry'] = dict(max_abs_D_diff=float(sym), classes_equal=same_cls, hit_steps_equal=same_hit)
for label, mapf, detf in [("twin T_s", Ts, Ds), ("control T", Tp, Dp)]:
    for r0 in (0.05, 0.03, 0.02, 0.01):
        res = run(mapf, detf, r0, th.copy())
        c = {k: int(np.sum(res['cls'] == k)) for k in ("RANK", "ESCAPE", "RETURN", "BOUNDED", "LOCAL")}
        hit = res['cls'] == "RANK"; ex = res['n_exit'] >= 0
        row = dict(system=label, r0=r0, Q0=r0*r0, counts=c,
                   n_exit=[int(res['n_exit'][ex].min()), int(res['n_exit'][ex].max())] if ex.any() else None,
                   n_hit=[int(res['n_hit'][hit].min()), int(res['n_hit'][hit].max())] if hit.any() else None,
                   hit_rho=[float(np.nanmin(res['hit_rho'])), float(np.nanmax(res['hit_rho']))] if hit.any() else None,
                   hit_cos_eta=[float(np.nanmin(np.cos(res['hit_eta']))), float(np.nanmax(np.cos(res['hit_eta'])))] if hit.any() else None,
                   hit_rho_sign=[int(np.sum(res['hit_rho'][hit] > 0)), int(np.sum(res['hit_rho'][hit] < 0))] if hit.any() else None,
                   qmax_nonhit=float(np.max(res['qmax'][~hit])) if (~hit).any() else None)
        out['rows'].append(row)
        print(f"{label:9s} r0={r0:<5} counts={c}  exit n∈{row['n_exit']}  hit n∈{row['n_hit']}  hit rho∈{row['hit_rho']}  "
              f"rho>0/<0={row['hit_rho_sign']}  max Q (non-hit)={row['qmax_nonhit']}", flush=True)
out['meta']['seconds'] = round(time.time() - t0, 1)
json.dump(out, open("e1_survey.json", "w"), indent=1, default=str); print("done", out['meta']['seconds'], "s")
