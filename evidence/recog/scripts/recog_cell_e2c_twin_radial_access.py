#!/usr/bin/env python3
r"""
recog_cell_e2c_twin_radial_access.py — RECOG OPEN R7 / CELL-E2C stage 1: radial access of the symmetric twin.
(rep:) primitive-lift (rho, eta); raw P1 eigenframe W = rho + omega eta, Q = |W|^2.   (transport:) T_s(rho,eta) = (rho - sin eta, eta + sinh rho - sin eta).
Target (RECOG-THM-TWIN-RADIAL-ACCESS):  for all x in A = {7/200 <= Q < 58107/1600000} there is 0 <= n <= NMAX with |rho(T_s^n x)| >= arccosh 2;
with E2A/E2B (recog_cell_e2a_twin_expansion.py) this extends to every orbit with 0 < Q0 < 7/200. No first-hit / root claim; nothing about C0^(s).
Tiling: half-annulus theta in [0, pi) (exact oddness T_s(-x) = -T_s(x) and antipodal invariance of the target supply [pi, 2 pi));
radial rings in Q with exact rational edges q_i = q1 + (q2 - q1) i / NR; angular sectors theta_k = k pi / NTH. Each annular sector
{r e^{i theta}} lies in the exact W-rectangle (rotated to the mid-angle) u in [r_a cos(D/2), r_b], |v| <= r_b sin(D/2), mapped linearly to (rho, eta)
and re-expressed in a Q-orthonormal frame. Transport: R8 engine mathematics (hash-gated import) with T_s substituted; LOCAL repair: after
any split the subtile is re-centred inside frame coordinates (c' = pt(c + R mid(E)), E' = E - mid(E) + R^{-1}(rounding residual)); no (rho,eta)-box round trip — the frozen R8 split path keeps
the old centre, which is sound but defeats refinement (R8/B3 certificates used zero splits and are unaffected).
Stopping: a (sub)tile stops when its whole hull has rho >= arccosh 2 or rho <= -arccosh 2 (Arb, certain). Straddling enclosures continue.
Splits only on enclosure width > WSPLIT; leaf budget per tile; failure on NMAX, budget, or non-finite values.
Modes:  --calibrate   (sampled tiles at NTH in {1024, 2048, 4096}, NR = 256, inner/middle/outer strips)
        --run NTH NR k0 k1   (production chunk over flattened tile index range [k0, k1), writes JSONL)
"""
import sys, os, json, time, hashlib, importlib.util, math
from fractions import Fraction as F
here = os.path.dirname(os.path.abspath(__file__))
R8_SHA256 = "1f8876a8a3fc31428d5ffb4873e62eb0780c08763b80281e1edeb8c1ab1223fd"
p = os.path.join(here, "recog_cell_r8_hetero_enclosure.py")
if hashlib.sha256(open(p, 'rb').read()).hexdigest() != R8_SHA256: print("[FAIL] R8 engine hash mismatch"); sys.exit(1)
spec = importlib.util.spec_from_file_location("r8", p); r8 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r8)
K = r8.ArbBackend(); arb = K.arb
class TwinEngine(r8.Engine):
    def T(self, x):
        r, e = x; s = K.sin(e); return [r - s, e + r.sinh() - s]
    def DT(self, x):
        r, e = x; c = K.cos(e); return [[K.one(), -c], [r.cosh(), K.one() - c]]
    def det(self, x):
        r, e = x; return K.one() + (r.cosh() - K.one())*K.cos(e)
    def recenter(self, c, A, E):
        # frame unchanged: shift inside frame coordinates; only the rounding residual of the new centre passes through A^{-1}
        # (no (rho, eta)-box round trip, hence no wrapping inflation)
        m = [K.pt(E[0]), K.pt(E[1])]
        c_b = [c[i] + (A[i][0]*m[0] + A[i][1]*m[1]) for i in range(2)]
        c2 = [K.pt(c_b[0]), K.pt(c_b[1])]
        res = self.mv(self.inv(A), [c_b[0] - c2[0], c_b[1] - c2[1]])
        return c2, A, [E[0] - m[0] + res[0], E[1] - m[1] + res[1]]
Eng = TwinEngine(K)
NMAX, WSPLIT, LEAF_BUDGET = 256, 0.05, 4096
NTH_PROD, NR_PROD = 4096, 32
q1, q2 = F(7, 200), F(58107, 1600000)
A_thr = (2 + arb(3).sqrt()).log(); s3 = arb(3).sqrt()
def W_to_lift(x, y): return [x + y/s3, 2*y/s3]
def tile(kt, kr, NTH, NR):
    qa, qb = q1 + (q2 - q1)*F(kr, NR), q1 + (q2 - q1)*F(kr + 1, NR)
    ra, rb = K.q(qa).sqrt(), K.q(qb).sqrt()
    th = arb.pi()*(2*kt + 1)/(2*NTH); half = arb.pi()/(2*NTH)
    er = [th.cos(), th.sin()]; et = [-th.sin(), th.cos()]
    u_lo, u_hi = ra*half.cos(), rb; hv = rb*half.sin(); um, hu = (u_lo + u_hi)/2, (u_hi - u_lo)/2
    c_b = W_to_lift(um*er[0], um*er[1]); c1 = W_to_lift(hu*er[0], hu*er[1]); c2 = W_to_lift(hv*et[0], hv*et[1])
    c, A, E = Eng.normalize(c_b, [[c1[0], c2[0]], [c1[1], c2[1]]], [K.box(), K.box()])
    A2 = Eng.frame(A); Ai = Eng.inv(A2); AM = Eng.mm(Ai, A)
    return c, A2, [AM[i][0]*E[0] + AM[i][1]*E[1] for i in range(2)]
def finite(x): return math.isfinite(float(x.mid())) and math.isfinite(float(x.rad()))
AH = arb(A_thr.upper())                     # retained closed strip |rho| <= AH (conservative at the boundary)
def clip(c, A, E):
    """Outward enclosure (in frame coordinates) of X ∩ {|rho| <= AH}; None if certainly empty. Sound for the per-point existence claim:
    every not-yet-successful point has its current image in X ∩ {|rho| < arccosh 2} ⊂ X ∩ {|rho| <= AH}."""
    E = list(E)
    for j in (0, 1):
        o = 1 - j; a = A[0][j]; b = A[0][o]
        if not (a > 0 or a < 0): continue
        B1 = (-AH - c[0] - b*E[o])/a; B2 = (AH - c[0] - b*E[o])/a
        lo = max(E[j].lower(), min(B1.lower(), B2.lower())); hi = min(E[j].upper(), max(B1.upper(), B2.upper()))
        if lo > hi: return None
        E[j] = arb(lo).union(arb(hi))
    return E
def run_tile(kt, kr, NTH, NR, budget=LEAF_BUDGET, use_clip=True):
    t = time.time(); c, A, E = tile(kt, kr, NTH, NR); stack = [(c, A, E, 0)]
    rec = dict(kt=kt, kr=kr, NTH=NTH, NR=NR, ok=True, leaves=0, peak=1, splits=0, clips=0, steps=0, n_hit=0, max_wE=0.0, margin=None)
    while stack:
        rec['peak'] = max(rec['peak'], len(stack)); c, A, E, n = stack.pop()
        while True:
            H = Eng.hull(c, A, E); rho = H[0]
            if not (finite(H[0]) and finite(H[1])): rec['ok'] = False; rec['fail'] = f"non-finite at step {n}"; break
            if rho >= A_thr or rho <= -A_thr:
                mg = float((rho - A_thr).lower()) if rho >= A_thr else float((-A_thr - rho).lower())
                rec['leaves'] += 1; rec['n_hit'] = max(rec['n_hit'], n); rec['margin'] = mg if rec['margin'] is None else min(rec['margin'], mg); break
            if use_clip and (rho.upper() > A_thr.lower() or rho.lower() < -A_thr.lower()):
                E2 = clip(c, A, E); rec['clips'] += 1
                if E2 is None: rec['leaves'] += 1; rec['n_hit'] = max(rec['n_hit'], n); break
                c, A, E = Eng.recenter(c, A, E2)
            wE = max(K.width(E[0]), K.width(E[1])); rec['max_wE'] = max(rec['max_wE'], wE)
            if wE > WSPLIT:
                if rec['leaves'] + len(stack) + 1 >= budget: rec['ok'] = False; rec['fail'] = f"budget at step {n}"; break
                j = 0 if K.width(E[0]) >= K.width(E[1]) else 1
                a_, b_ = K.split(E[j]); Ea = list(E); Eb = list(E); Ea[j] = a_; Eb[j] = b_
                stack.append((*Eng.recenter(c, A, Eb), n)); c, A, E = Eng.recenter(c, A, Ea); rec['splits'] += 1; continue
            if n >= NMAX: rec['ok'] = False; rec['fail'] = "NMAX"; break
            c, A, E, _ = Eng.step(c, A, E); n += 1; rec['steps'] += 1
        if not rec['ok']: break
    rec['t'] = round(time.time() - t, 4); return rec
if __name__ == "__main__":
    import flint
    meta = dict(meta=True, rid="RECOG-THM-TWIN-RADIAL-ACCESS", script_sha256=hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
                r8_sha256=R8_SHA256, backend=K.name, flint=flint.__version__, prec_bits=120, NMAX=NMAX, WSPLIT=WSPLIT, LEAF_BUDGET=LEAF_BUDGET, q1=str(q1), q2=str(q2))
    if sys.argv[1] == "--calibrate":
        import statistics
        NTH, NR = NTH_PROD, NR_PROD; out = open(os.path.join(here, "e2c_calibration_clip.jsonl"), "w")
        out.write(json.dumps(dict(meta, mode="calibrate-clip", NTH=NTH, NR=NR, note="budget is a pure hard stop; splitting heuristics independent of budget")) + "\n")
        sample = [((i*NTH)//50, kr) for kr in (0, NR//2, NR - 1) for i in range(50)]
        t0 = time.time(); base = {}
        for kt, kr in sample: base[(kt, kr)] = run_tile(kt, kr, NTH, NR, budget=1024, use_clip=False)
        WS0 = WSPLIT
        adv = [k for k, r in base.items() if not r['ok']]
        # also the failures of the split-width 0.02 run on this grid
        globals()['WSPLIT'] = 0.02
        adv02 = [k for k in sample if not run_tile(k[0], k[1], NTH, NR, budget=1024, use_clip=False)['ok']]
        globals()['WSPLIT'] = WS0
        advset = sorted(set(adv) | set(adv02))
        recs = {}
        for kt, kr in sample: r = run_tile(kt, kr, NTH, NR); recs[(kt, kr)] = r; out.write(json.dumps(r) + "\n")
        out.close()
        def summ(keys, rs, label):
            L = sorted(rs[k]['leaves'] for k in keys if rs[k]['ok']); ok = sum(rs[k]['ok'] for k in keys)
            pc = lambda p: L[min(len(L) - 1, int(p*len(L)))] if L else None
            print(f"{label}: tiles {len(keys)}, certified {ok}; leaves p50/p90/p99/max = {pc(.5)}/{pc(.9)}/{pc(.99)}/{L[-1] if L else None}; "
                  f"peak live max {max(rs[k]['peak'] for k in keys)}; max wE {max(rs[k]['max_wE'] for k in keys):.3f}; "
                  f"min margin {min((rs[k]['margin'] for k in keys if rs[k]['margin'] is not None), default=float('nan')):.2e}; n_hit max {max(rs[k]['n_hit'] for k in keys)}; "
                  f"mean t {statistics.mean(rs[k]['t'] for k in keys):.4f}s; fails {[rs[k].get('fail') for k in keys if not rs[k]['ok']][:3]}", flush=True)
        summ(sample, base, "UNCLIPPED ws=0.05 budget 1024 (reference)")
        summ(sample, recs, "CLIPPED   ws=0.05 budget 4096           ")
        summ(advset, recs, f"ADVERSARIAL subset ({len(advset)} parents failing unclipped at 1024, ws 0.05 or 0.02), clipped")
        tm = statistics.mean(r['t'] for r in recs.values())
        print(f"estimated production ({NTH}x{NR} = {NTH*NR} tiles): {tm*NTH*NR/3600:.2f} h   [{time.time()-t0:.0f}s calibration]")
