#!/usr/bin/env python3
r"""
recog_cell_b3_p2_c0_first.py — RECOG OPEN R3 / CELL-B3: first encounter of the positive unstable branch of P2 with C0.

(rep:) primitive-lift (rho, eta);  (transport:) T(rho,eta) = (rho - sin eta, eta + e^rho - 1 - sin eta);  P2 = (0, pi).
C0 = {D = 0},  D(rho,eta) = det DT = 1 + (e^rho - 1) cos eta,  grad D = (e^rho cos eta, -(e^rho - 1) sin eta).

Claim (RECOG-THM-P2-C0-FIRST). Parametrise W^u_+(P2) outward from P2 by (k, s) -> T^k gamma(s), gamma the local unstable
graph over the positive shell. There is a unique FIRST outward parameter value p* at which W^u_+(P2) meets C0; D > 0 at every
earlier branch point, and the first encounter is transverse (d/ds D(T^K gamma(s)) < 0); the encounter point lies in the
theorem-owned exact-rational outer box B* (2.03334 < rho < 2.03342, 8.0048 < eta_lift < 8.0059), checked directly
against the Arb enclosures. No assertion is made about later re-intersections of the branch with C0.
Certificate mode: exactly 4096 pieces (hard-coded); run metadata and certified extrema are written to b3_cert.json.
lambda_- is recomputed here as an exact rational (the frozen R8 stage1() exports it as a float, which is not a lower bound).
Proof structure:
 Stage 1  [ALG, reused from R8]: quadratic-cusp lemma at P2 (delta = 1/100000, kappa = 2); symmetric in the sign of s.
 Stage 1b [ALG via IA]: unstable cone field K_c = {(ds,dw): |dw| <= c|ds|}, c = 1/100, is forward-invariant under DT on
   N = {|s|,|w| <= delta} (Arb); the local unstable manifold is tangent to v_u at P2, so its tangent lies in K_c on N.
 Shell: s in [s0, s1] with s1 = 5/4 s*_design, s0 = s1/lam_+; since s* < s1 < lam_- s*, every branch point before the encounter
   is (i) in the local box near P2 (D >= 1 - (e^{2 delta} - 1) > 0), or (ii) T^k gamma(s), k < K, s in shell, or (iii) T^K gamma(s),
   s < s*. [Images at step K-1 of shell points satisfy sigma(s) <= s1/lam_- < s*, so none lies after the encounter.]
 Transport [ALG via IA]: pieces c + R E (Lohner, Q-orthonormal frames, Arb) with tangent enclosures v_{k+1} in DT(H_k) v_k,
   v_0 = v_u + m v_s, |m| <= c. Checks: D > 0 on every enclosure for k < K; at k = K the pieces split into a prefix with D > 0,
   a contiguous crossing block with grad D . v_K < 0, and a following piece with D < 0. By monotonicity f(s) = D(T^K gamma(s)) has
   exactly one zero, inside the crossing block, and none before it.
"""
import sys, os, json, hashlib, importlib.util
from fractions import Fraction as F
spec = importlib.util.spec_from_file_location("r8", os.path.join(os.path.dirname(os.path.abspath(__file__)), "recog_cell_r8_hetero_enclosure.py"))
R8_SHA256 = "1f8876a8a3fc31428d5ffb4873e62eb0780c08763b80281e1edeb8c1ab1223fd"
if hashlib.sha256(open(spec.origin, 'rb').read()).hexdigest() != R8_SHA256:
    print("[FAIL] R8 transport engine hash mismatch — refusing to run"); sys.exit(1)
r8 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r8)
ok = True
def check(name, cond, info=""):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name} {info}", flush=True); ok = ok and bool(cond)
delta, kappa = F(1, 100000), F(2)
ok1, s1d = r8.stage1(delta, kappa); lam_p = s1d['lam_p']
def exact_lam_minus(delta, kappa):          # identical formulas to r8.stage1, kept exact
    s5_lo, s5_hi = F(22360679, 10**7), F(22360680, 10**7)
    ph_lo, ph_hi = (1+s5_lo)/2, (1+s5_hi)/2
    lam_u_lo = ph_lo + 1; x = 2*delta
    E_hi = 1 + x + x**2/2/(1 - x/3); cube = ph_hi**3/6
    c_u = cube*2*delta; c_v = E_hi/2 + cube*2*delta
    C_s = (c_v + c_u/ph_lo)/s5_lo; f = (1 + kappa*delta)**2
    return lam_u_lo - C_s*f*delta
lam_m = exact_lam_minus(delta, kappa)
check("exact rational lambda_- reconstructed; > 1; float export differs from it by < 1e-15", lam_m > 1 and abs(float(lam_m) - s1d['lam_m']) < 1e-15,
      f"lambda_- = {float(lam_m):.16f} (exact rational, denominator {lam_m.denominator.bit_length()} bits)")
check("Stage 1 quadratic-cusp lemma (delta=1/100000, kappa=2)", ok1, f"theta={s1d['theta']:.6f}, lam in [{s1d['lam_m']:.6f},{float(lam_p):.6f}]")
K = r8.ArbBackend(); Eng = r8.Engine(K); arb = K.arb
phi = (K.one() + K.sqrt(K.q(F(5))))/2; P2 = [K.q(F(0)), K.pi()]
vu = [K.one(), phi]; vs = [K.one(), -K.one()/phi]
# ---- Stage 1b: cone lemma on N
c_cone = F(1, 100); cc = K.q(c_cone); dl = K.q(delta)
box = arb(0, 1)*dl                                                   # [-delta, delta]
X = [P2[i] + box*vu[i] + box*vs[i] for i in range(2)]
J = Eng.DT(X)
Pm = [[vu[0], vs[0]], [vu[1], vs[1]]]; Pi = Eng.inv(Pm)
M = Eng.mm(Pi, Eng.mm(J, Pm))                                          # DT in (s,w) coordinates over N
mm = arb(0, 1)*cc
num = M[1][0] + M[1][1]*mm; den = M[0][0] + M[0][1]*mm
check("Stage 1b cone invariance |dw'| <= c |ds'| on N (c = 1/100)", den > 0 and abs(num) < cc*den,
      f"sup|num| <= {float(abs(num).upper()):.3e}, c*inf den >= {float((cc*den).lower()):.3e}")
check("local box: D > 0 on N", Eng.det(X) > 0, f"inf D >= {float(Eng.det(X).lower()):.6f}")
# ---- shell placement
sstar_design = F(4206858, 10**12)                                      # float design value (not a proof input)
s1 = F(5, 4)*sstar_design; s0 = s1/lam_p
check("shell inside lemma domain and s* < s1 < lam_- s* (design value, exact lam_-)", s1 <= delta and s1/lam_m < sstar_design < s1)
KSTEP = 14; NP = 4096                                     # certificate mode: fixed
recs = []
for j in range(NP):
    sa = s0 + (s1 - s0)*F(j, NP); sb = s0 + (s1 - s0)*F(j+1, NP)
    sm, sr = (sa + sb)/2, (sb - sa)/2; wmax = kappa*max(sa*sa, sb*sb)
    c_b = [P2[i] + K.q(sm)*vu[i] for i in range(2)]
    A_b = [[K.q(sr)*vu[i], K.q(wmax)*vs[i]] for i in range(2)]
    c, A, E = Eng.normalize(c_b, A_b, [K.box(), K.box()])
    v = [vu[i] + arb(0, 1)*cc*vs[i] for i in range(2)]
    mind = None
    for k in range(KSTEP):
        H = Eng.hull(c, A, E); d = Eng.det(H)
        if k > 0:
            if not (d > 0): recs.append(dict(j=j, fail=f"D not > 0 at step {k}")); break
            mind = float(d.lower()) if mind is None else min(mind, float(d.lower()))
        v = Eng.mv(Eng.DT(H), v)
        c, A, E, _ = Eng.step(c, A, E)
    else:
        H = Eng.hull(c, A, E); d = Eng.det(H)
        r_, e_ = H
        grad = [r_.exp()*e_.cos(), -(r_.exp() - 1)*e_.sin()]
        dd = grad[0]*v[0] + grad[1]*v[1]
        cls = "pos" if d > 0 else ("neg" if d < 0 else "cross")
        recs.append(dict(j=j, sa=sa, sb=sb, cls=cls, mind=mind, dlo=float(d.lower()), dhi=float(d.upper()),
                         dd_hi=float(dd.upper()), dd_neg=bool(dd < 0), rho=(float(r_.lower()), float(r_.upper())), eta=(float(e_.lower()), float(e_.upper())),
                         rho_arb=r_, eta_arb=e_))
fails = [r for r in recs if 'fail' in r]
check("every piece: D > 0 certified at steps 1..K-1", not fails, f"{len(fails)} failures" if fails else f"min inf D = {min(r['mind'] for r in recs):.6f}")
if fails: print("FAIL", fails[:3]); sys.exit(1)
cls = [r['cls'] for r in recs]
cr = [i for i, x in enumerate(cls) if x == "cross"]
check("crossing block nonempty and contiguous", len(cr) > 0 and cr == list(range(cr[0], cr[-1] + 1)), f"pieces {cr[0]}..{cr[-1]}" if cr else "")
check("all pieces before the block: D > 0 at step K", all(x == "pos" for x in cls[:cr[0]]))
check("piece after the block: D < 0 at step K", cr[-1] + 1 < NP and cls[cr[-1] + 1] == "neg")
check("transversality: grad D . v_K < 0 on every crossing piece", all(recs[i]['dd_neg'] for i in cr), f"sup = {max(recs[i]['dd_hi'] for i in cr):.4e}")
sl, sh = recs[cr[0]]['sa'], recs[cr[-1]]['sb']
check("shell placement re-checked on the CERTIFIED bracket with exact lam_-: s1/lam_- < s*_lo and s*_hi < s1", s1/lam_m < sl and sh < s1,
      f"s1/lam_- = {float(s1/lam_m):.10e} < {float(sl):.10e};  {float(sh):.10e} < s1 = {float(s1):.10e}")
rho_b = (min(recs[i]['rho'][0] for i in cr), max(recs[i]['rho'][1] for i in cr)); eta_b = (min(recs[i]['eta'][0] for i in cr), max(recs[i]['eta'][1] for i in cr))
print(f"    s* in [{float(recs[cr[0]]['sa']):.10e}, {float(recs[cr[-1]]['sb']):.10e}];  K = {KSTEP}")
print(f"    encounter box B*: rho in [{rho_b[0]:.10f}, {rho_b[1]:.10f}],  eta_lift in [{eta_b[0]:.10f}, {eta_b[1]:.10f}]")
import flint
# 4. theorem-owned box: exact rational outer box, compared directly against the Arb enclosures (no float round-trip)
RHO_LO, RHO_HI, ETA_LO, ETA_HI = F(203334, 100000), F(203342, 100000), F(80048, 10000), F(80059, 10000)
EXC_LO, EXC_HI = F(27864, 100), F(27870, 100)
box_ok = all(recs[i]['rho_arb'] > K.q(RHO_LO) and recs[i]['rho_arb'] < K.q(RHO_HI) and
             recs[i]['eta_arb'] > K.q(ETA_LO) and recs[i]['eta_arb'] < K.q(ETA_HI) for i in cr)
check("B* (theorem-owned, exact rationals): 2.03334 < rho < 2.03342, 8.0048 < eta_lift < 8.0059", box_ok)
exc_ok = all(((recs[i]['eta_arb'] - K.pi())*180/K.pi()) > K.q(EXC_LO) and ((recs[i]['eta_arb'] - K.pi())*180/K.pi()) < K.q(EXC_HI) for i in cr)
check("lifted excursion 278.64 deg < eta* - pi < 278.70 deg (Arb vs exact rationals)", exc_ok)
check("eta* > 5 pi/2 (first-hit order -i -> +1 -> +i before the first C0 encounter, by continuity)", all(recs[i]['eta_arb'] > 5*K.pi()/2 for i in cr))
print("    [NUM display from certified enclosure, not theorem-owned] tighter hull as printed above; min inf D and grad bound are displays of Arb endpoints; positivity/negativity were checked in Arb")
here = hashlib.sha256(open(__file__,'rb').read()).hexdigest()
rec = dict(rid="RECOG-THM-P2-C0-FIRST", script_sha256=here, r8_transport_sha256=hashlib.sha256(open(spec.origin,'rb').read()).hexdigest(),
           backend=K.name, flint_version=flint.__version__, prec_bits=120, delta=str(delta), kappa=str(kappa), cone_c=str(c_cone),
           lam_minus_exact=str(lam_m), lam_plus=str(lam_p), s0=str(s0), s1=str(s1), K=KSTEP, pieces=NP,
           crossing_pieces=[cr[0], cr[-1]], s_star=[str(sl), str(sh)],
           sup_gradD_dot_v_on_crossing=max(recs[i]['dd_hi'] for i in cr),
           theorem_box=dict(rho=[str(RHO_LO), str(RHO_HI)], eta_lift=[str(ETA_LO), str(ETA_HI)], excursion_deg=[str(EXC_LO), str(EXC_HI)]),
           num_display=dict(note="displays of Arb endpoints via float; not theorem-owned", box_rho=list(rho_b), box_eta_lift=list(eta_b),
                            min_inf_D_pre=min(r['mind'] for r in recs)),
           all_checks_pass=ok)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "b3_cert.json"), "w").write(json.dumps(rec, indent=1))
print(f"    script sha256 {hashlib.sha256(open(__file__,'rb').read()).hexdigest()}; R8 transport sha256 {hashlib.sha256(open(spec.origin,'rb').read()).hexdigest()}; flint {flint.__version__}; pieces {NP}")
print("B3 CERTIFICATE PASS" if ok else "B3 CERTIFICATE FAIL"); sys.exit(0 if ok else 1)
