#!/usr/bin/env python3
r"""
recog_cell_r8_hetero_enclosure.py — RECOG OPEN R8 / CELL-B2: heteroclinic entry certificate.
RTG_RELATIONAL_RECOGNITION_DSN (v0.3.2 frozen; result for v0.3.3).

(rep:) primitive-lift (rho, eta), lifted local phase, no wrapping seam (as in DYAD-THM-PRIM-CTR).
(transport:) T(rho,eta) = (rho - sin eta, eta + e^rho - 1 - sin eta);  P2 = (0, pi), P1 = (0, 0);
             Q_prim = rho^2 - rho*eta + eta^2 (invariant form of DT(P1)).

Claim (RECOG-THM-P2-HET):  W^u_-(P2)\{P2} ⊂ B(P1), i.e. every point of the negative unstable branch of P2 tends to P1.
Proof structure:
 Stage 1 [ALG, exact rationals]: local unstable-shell lemma at P2 (cusp R = {|w| <= kappa s^2}, eigen-coordinates
   (s,w) along v_u=(1,phi), v_s=(1,-1/phi)) [ALG: exact symbolic constants + rational transcendental remainder bounds:
   sqrt5 enclosed by rationals verified by squaring; e^x <= 1+x+x^2/(2(1-x/3)); |sin v - v| <= |v|^3/6]; every point of W^u_-(P2)\{P2} has an iterate in the fundamental shell
   Sigma = {s in [-delta, -delta/lam_+], |w| <= kappa s^2}, and its forward orbit passes through Sigma or starts after it.
   Logic: W^u_-(P2) ∩ U_loc ⊂ {|w| <= kappa s^2} (cusp invariance + complement contraction), plus outward monotonicity of |s|.
   Certifying EVERY point of the 2-D shell Sigma implies the result for the manifold a fortiori (no P_u(t) evaluation).
 Stage 2/3 [ALG via IA]: Sigma is covered by parallelepipeds X = c + A*E (point centre, point frame, ball box) and each is
   transported by the rigorous mean-value (Lohner) step  T(X) ⊂ T([c]) + (DT(hull(X ∪ c)) R_k) E  with moving frame R_k,
   re-framed with a Q-orthonormal frame R_{k+1} (the P1 linear map L satisfies L^T B L = B, so B-orthonormal frames suppress
   shear accumulation); R_{k+1} is chosen from midpoints (any choice is admissible) but is an exact point matrix whose inverse
   is enclosed in Arb. Pieces are split when a box component exceeds WSPLIT.
   At every pre-entry step inf det DT(hull) > 0 is certified; transport stops when sup Q_prim(hull) <= 1/625.
 Tail [import]: DYAD-THM-PRIM-CTR — every trajectory in U = {0 < Q_prim <= 1/625} tends to P1 (six-phase invariant tube).
Backend: Arb (python-flint, outward-rounded balls) is the trust anchor; mpmath.iv is available as a prototype backend
 (--backend mpmath) and is NOT used for the certificate. The engine touches arithmetic only through class Backend.
"""
import sys, time, os, json
from fractions import Fraction as F

# ------------------------------------------------------------------ Stage 1 (exact rationals)
def stage1(delta, kappa):
    out = {}; ok = True
    s5_lo, s5_hi = F(22360679, 10**7), F(22360680, 10**7)
    ok &= s5_lo**2 < 5 < s5_hi**2
    ph_lo, ph_hi = (1+s5_lo)/2, (1+s5_hi)/2
    lam_u_lo, lam_u_hi, lam_s_hi = ph_lo+1, ph_hi+1, 2-ph_lo
    x = 2*delta; ok &= x < 3
    E_hi = 1 + x + x**2/2/(1 - x/3)                     # e^x upper bound, 0 <= x < 3
    cube = ph_hi**3/6
    c_u = cube*2*delta; c_v = E_hi/2 + cube*2*delta     # |N_u| <= c_u (a+b)^2, |N_v| <= c_v (a+b)^2
    k_w = 1 - 1/(ph_hi*s5_hi); ok &= k_w > 0
    C_w = k_w*c_u + c_v/s5_lo; C_s = (c_v + c_u/ph_lo)/s5_lo
    f = (1 + kappa*delta)**2
    lam_m, lam_p = lam_u_lo - C_s*f*delta, lam_u_hi + C_s*f*delta
    A_ok = lam_s_hi*kappa + C_w*f <= kappa*lam_m**2
    theta = lam_s_hi + C_w*(2/kappa + 2*delta)
    out.update(A=A_ok, B=theta < 1, C=lam_m > 1, D=kappa*delta**2 <= delta, theta=float(theta), lam_m=float(lam_m), lam_p=lam_p)
    return ok and A_ok and theta < 1 and lam_m > 1 and kappa*delta**2 <= delta, out

# ------------------------------------------------------------------ backends
class ArbBackend:
    name = "arb (python-flint)"
    def __init__(self, prec=120):
        import flint; flint.ctx.prec = prec; self.f = flint; self.arb = flint.arb
    def q(self, fr):        return self.arb(fr.numerator)/self.arb(fr.denominator)       # ball containing a rational
    def pt(self, x):        return self.arb(x.mid())                                       # exact point (radius 0)
    def one(self):          return self.arb(1)
    def pi(self):           return self.arb.pi()
    def sqrt(self, x):      return x.sqrt()
    def sin(self, x):       return x.sin()
    def cos(self, x):       return x.cos()
    def exp(self, x):       return x.exp()
    def union(self, a, b):  return a.union(b)
    def lo(self, x):        return float(x.lower())
    def hi(self, x):        return float(x.upper())
    def width(self, x):     return 2*float(x.rad())
    def box(self):          return self.arb(0, 1)                                          # [-1,1]
    def split(self, x):     # halves covering x: [lower, mid] and [mid, upper] via unions of exact points
        lo, hi, m = self.arb(x.lower()), self.arb(x.upper()), self.arb(x.mid())
        return lo.union(m), m.union(hi)
    def positive(self, x):  return x > 0
    def le(self, x, fr):    return x <= self.q(fr)
    def mid_float(self, x): return float(x.mid())
class MpmathBackend:
    name = "mpmath.iv (prototype, not a trust anchor)"
    def __init__(self, dps=30):
        from mpmath import iv, mp; iv.dps = dps; mp.dps = dps; self.iv, self.mp = iv, mp
    def q(self, fr):        return self.iv.mpf(fr.numerator)/fr.denominator
    def pt(self, x):        return self.iv.mpf(self.mp.mpf(x.mid))
    def one(self):          return self.iv.mpf(1)
    def pi(self):           return self.iv.pi
    def sqrt(self, x):      return self.iv.sqrt(x)
    def sin(self, x):       return self.iv.sin(x)
    def cos(self, x):       return self.iv.cos(x)
    def exp(self, x):       return self.iv.exp(x)
    def union(self, a, b):  return self.iv.mpf([min(a.a, b.a), max(a.b, b.b)])
    def lo(self, x):        return float(x.a)
    def hi(self, x):        return float(x.b)
    def width(self, x):     return float(x.delta)
    def box(self):          return self.iv.mpf([-1, 1])
    def split(self, x):     m = x.mid; return self.iv.mpf([x.a, m]), self.iv.mpf([m, x.b])
    def positive(self, x):  return x.a > 0
    def le(self, x, fr):    return x.b <= self.q(fr).a
    def mid_float(self, x): return float(x.mid)

# ------------------------------------------------------------------ engine (backend-generic)
class Engine:
    def __init__(self, K): self.K = K
    def T(self, x):
        K = self.K; r, e = x; s = K.sin(e); return [r - s, e + K.exp(r) - K.one() - s]
    def DT(self, x):
        K = self.K; r, e = x; c = K.cos(e); return [[K.one(), -c], [K.exp(r), K.one() - c]]
    def det(self, x):
        K = self.K; r, e = x; return K.one() + (K.exp(r) - K.one())*K.cos(e)
    def Q(self, x):
        r, e = x; return r*r - r*e + e*e
    @staticmethod
    def mv(M, v): return [M[0][0]*v[0] + M[0][1]*v[1], M[1][0]*v[0] + M[1][1]*v[1]]
    @staticmethod
    def mm(M, N): return [[M[i][0]*N[0][j] + M[i][1]*N[1][j] for j in range(2)] for i in range(2)]
    def inv(self, A):
        a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]; D = a*d - b*c
        return [[d/D, -b/D], [-c/D, a/D]]
    def frame(self, M):   # Q-orthonormal frame, longest image column first; returned as exact points
        K = self.K
        qn = lambda v: v[0]*v[0] - v[0]*v[1] + v[1]*v[1]
        cols = [[M[0][j], M[1][j]] for j in range(2)]
        cols.sort(key=lambda v: -K.mid_float(qn(v)))
        n0 = K.sqrt(qn(cols[0])); q0 = [K.pt(cols[0][0]/n0), K.pt(cols[0][1]/n0)]
        Bq = [q0[0] - q0[1]/2, -q0[0]/2 + q0[1]]; q1 = [-Bq[1], Bq[0]]
        n1 = K.sqrt(qn(q1)); q1 = [K.pt(q1[0]/n1), K.pt(q1[1]/n1)]
        return [[q0[0], q1[0]], [q0[1], q1[1]]]
    def hull(self, c, A, E):
        X = [c[i] + (A[i][0]*E[0] + A[i][1]*E[1]) for i in range(2)]
        return [self.K.union(X[i], c[i]) for i in range(2)]
    def step(self, c, A, E):
        K = self.K
        H = self.hull(c, A, E); d = self.det(H)
        Tc = self.T(c); M = self.mm(self.DT(H), A)
        half = [K.width(E[j])/2 for j in range(2)]
        Mmid = [[K.pt(M[i][j]) for j in range(2)] for i in range(2)]
        Ms = [[Mmid[i][j]*half[j] for j in range(2)] for i in range(2)]
        A2 = self.frame(Ms); Ai = self.inv(A2)
        c2 = [K.pt(Tc[0]), K.pt(Tc[1])]
        off = self.mv(Ai, [Tc[0] - c2[0], Tc[1] - c2[1]])
        AM = self.mm(Ai, M)
        E2 = [off[i] + (AM[i][0]*E[0] + AM[i][1]*E[1]) for i in range(2)]
        return c2, A2, E2, d
    def normalize(self, c_b, A_b, E):
        K = self.K
        c = [K.pt(c_b[i]) for i in range(2)]; A = [[K.pt(A_b[i][j]) for j in range(2)] for i in range(2)]
        Ai = self.inv(A)
        X = [(c_b[i] - c[i]) + (A_b[i][0]*E[0] + A_b[i][1]*E[1]) for i in range(2)]
        return c, A, self.mv(Ai, X)

def main():
    args = dict(a.split("=") for a in sys.argv[1:] if "=" in a)
    backend = args.get("--backend", "arb"); delta = F(1, int(args.get("--delta_inv", "100000"))); kappa = F(2)
    npieces = int(args.get("--pieces", "4096")); wsplit = float(args.get("--wsplit", "2e-3"))
    k0, k1 = int(args.get("--from", "0")), int(args.get("--to", str(npieces)))
    maxsteps = int(args.get("--maxsteps", "8000")); out = args.get("--out", "r8_results.jsonl")
    ok1, s1 = stage1(delta, kappa)
    print(f"[{'PASS' if ok1 else 'FAIL'}] Stage 1 local shell lemma: delta={delta}, kappa={kappa}, (A)={s1['A']}, (B) theta={s1['theta']:.6f}, (C) lam in [{s1['lam_m']:.6f},{float(s1['lam_p']):.6f}], (D)={s1['D']}", flush=True)
    if not ok1: sys.exit(1)
    K = ArbBackend() if backend == "arb" else MpmathBackend(); Eng = Engine(K)
    print(f"backend: {K.name}; pieces {k0}..{k1-1} of {npieces}; wsplit={wsplit}", flush=True)
    phi = (K.one() + K.sqrt(K.q(F(5))))/2; P2 = [K.q(F(0)), K.pi()]
    vu = [K.one(), phi]; vs = [K.one(), -K.one()/phi]
    lam_p = s1['lam_p']
    s_lo, s_hi = -delta, -delta/lam_p                    # exact rationals; pieces cover [s_lo, s_hi]
    QIN = F(1, 625)
    import hashlib, flint
    meta = dict(meta=True, script_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(), backend=K.name,
                flint_version=getattr(flint, '__version__', '?'), prec_bits=120, delta=str(delta), kappa=str(kappa),
                lam_plus=str(lam_p), npieces=npieces, wsplit=wsplit, range=[k0, k1], Q_in="1/625")
    dsn = "/mnt/project/RTG_DYADIC_OSCILLATOR_DSN_v6_4_10.md"
    if os.path.exists(dsn): meta['dyad_dsn_v6_4_10_sha256'] = hashlib.sha256(open(dsn,'rb').read()).hexdigest()
    with open(out, "a") as fo:
        fo.write(json.dumps(meta) + "\n"); fo.flush()
        for k in range(k0, k1):
            sa = s_lo + (s_hi - s_lo)*F(k, npieces); sb = s_lo + (s_hi - s_lo)*F(k+1, npieces)
            sm, sr = (sa + sb)/2, (sb - sa)/2; wmax = kappa*max(sa*sa, sb*sb)
            c_b = [P2[i] + K.q(sm)*vu[i] for i in range(2)]
            A_b = [[K.q(sr)*vu[i], K.q(wmax)*vs[i]] for i in range(2)]
            c, A, E = Eng.normalize(c_b, A_b, [K.box(), K.box()])
            stack = [(c, A, E, 0)]; rec = dict(piece=k, sa=str(sa), sb=str(sb), leaves=0, max_steps=0, min_det=9.0, max_width=0.0, q_lo=1.0, q_hi=0.0, ok=True, splits=0)
            t0 = time.time()
            while stack:
                c, A, E, n = stack.pop()
                while True:
                    if n >= maxsteps: rec['ok'] = False; rec['fail'] = f"maxsteps at leaf"; break
                    c, A, E, d = Eng.step(c, A, E); n += 1
                    if not K.positive(d): rec['ok'] = False; rec['fail'] = f"det not certified positive at step {n}"; break
                    rec['min_det'] = min(rec['min_det'], K.lo(d))
                    w = max(K.width(E[0]), K.width(E[1])); rec['max_width'] = max(rec['max_width'], w)
                    H = Eng.hull(c, A, E); qq = Eng.Q(H)
                    if K.le(qq, QIN):
                        if not K.positive(qq): rec['ok'] = False; rec['fail'] = "entry Q not certified > 0"; break
                        rec['leaves'] += 1; rec['max_steps'] = max(rec['max_steps'], n)
                        rec['q_lo'] = min(rec['q_lo'], K.lo(qq)); rec['q_hi'] = max(rec['q_hi'], K.hi(qq)); break
                    if w > wsplit:
                        j = 0 if K.width(E[0]) >= K.width(E[1]) else 1
                        a, b = K.split(E[j]); Ea = list(E); Eb = list(E); Ea[j] = a; Eb[j] = b
                        stack.append((c, A, Eb, n)); E = Ea; rec['splits'] += 1
                if not rec['ok']: break
            rec['secs'] = round(time.time() - t0, 2)
            fo.write(json.dumps(rec) + "\n"); fo.flush()
            if not rec['ok']: print("FAIL", rec, flush=True); sys.exit(1)
    print("range done", flush=True)

def summarize(path, npieces):
    import hashlib
    lines = [json.loads(l) for l in open(path)]
    metas = [m for m in lines if m.get('meta')]; recs = [r for r in lines if not r.get('meta')]
    gates = {}
    ids = [r['piece'] for r in recs]
    gates['1 ids exactly 0..N-1, no omissions/duplicates'] = sorted(ids) == list(range(npieces)) and len(ids) == npieces
    shas = set(m['script_sha256'] for m in metas); here = hashlib.sha256(open(__file__,'rb').read()).hexdigest()
    gates['6a all records from this exact script'] = shas == {here}
    gates['6b single parameter set'] = len(set((m['delta'], m['kappa'], m['lam_plus'], m['npieces']) for m in metas)) == 1
    m0 = metas[0]; delta = F(m0['delta']); lam_p = F(m0['lam_plus'])
    ok1, s1 = stage1(delta, F(m0['kappa']))
    gates['0 stage 1 lemma re-verified with recorded delta, kappa'] = ok1 and s1['lam_p'] == lam_p
    byid = {r['piece']: r for r in recs}
    cover = gates['1 ids exactly 0..N-1, no omissions/duplicates'] and F(byid[0]['sa']) == -delta and F(byid[npieces-1]['sb']) == -delta/lam_p \
            and all(F(byid[k]['sb']) == F(byid[k+1]['sa']) for k in range(npieces-1)) and all(F(byid[k]['sa']) < F(byid[k]['sb']) for k in range(npieces))
    gates['2 initial pieces tile [-delta, -delta/lam_+] exactly (contiguous exact rationals)'] = cover
    gates['3 every leaf certified 0 < Q_entry <= 1/625 (exact rational, Arb comparison)'] = all(r['ok'] and r['leaves'] >= 1 for r in recs) and min(r['q_lo'] for r in recs) > 0
    gates['4 every pre-entry enclosure has certified inf det DT > 0'] = all(r['ok'] for r in recs) and min(r['min_det'] for r in recs) > 0
    gates['5 frames exact points, inverses enclosed in Arb (by construction; backend)'] = all('arb' in m['backend'] for m in metas)
    for g, v in sorted(gates.items()): print(f"[{'PASS' if v else 'FAIL'}] {g}")
    allok = all(gates.values())
    print(f"script sha256: {here}; flint {m0['flint_version']}; prec {m0['prec_bits']} bits; delta={m0['delta']}, kappa={m0['kappa']}, pieces={npieces}")
    if 'dyad_dsn_v6_4_10_sha256' in m0: print(f"Dyadic DSN v6.4.10 sha256: {m0['dyad_dsn_v6_4_10_sha256']}")
    print(f"pieces certified: {len(seen)}/{npieces}; all ok: {allok}")
    print(f"leaves: {sum(r['leaves'] for r in recs)}; splits: {sum(r['splits'] for r in recs)}")
    print(f"max primitive steps to entry: {max(r['max_steps'] for r in recs)}")
    print(f"min certified det DT (pre-entry): {min(r['min_det'] for r in recs):.6f}")
    print(f"max enclosure box width: {max(r['max_width'] for r in recs):.3e}")
    print(f"entry Q_prim interval over all leaves: [{min(r['q_lo'] for r in recs):.8f}, {max(r['q_hi'] for r in recs):.8f}]  (target <= 1/625 = 0.0016)")
    print("R8 CERTIFICATE PASS" if allok else "R8 CERTIFICATE INCOMPLETE/FAIL"); sys.exit(0 if allok else 1)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "summary": summarize(sys.argv[2], int(sys.argv[3]))
    else: main()
