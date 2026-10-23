#!/usr/bin/env python3
r"""
recog_cell_e3b_c0_access.py — RECOG OPEN R7 / CELL-E3B: exact accessibility of the twin rank locus C0^(s).
Target RID: RECOG-THM-TWIN-C0-ACCESS  [THM]  (scope: diagnostic twin T_s, SG-R4)

Claim: there exist x* in A = {7/200 <= Q < 58107/1600000} and N with D_s(T_s^N x*) = 0, i.e. T_s^N x* in C0^(s).
Corollary (exact oddness T_s(-x) = -T_s(x), D_s(-x) = D_s(x)): -x* is a second witness at the same N (antipodal pair).
Preregistered logic:  a sign change of D_s IN TIME along one orbit does NOT imply a hit of C0^(s);  but
   D_s(T_s^N x_-) > 0,  D_s(T_s^N x_+) < 0  (SAME N),  [x_-, x_+] subset of A   ==>   exists x* in [x_-, x_+] with D_s(T_s^N x*) = 0,
because t -> D_s(T_s^N(I(t))) is continuous (T_s analytic, D_s continuous) — IVT. No first-hit, uniqueness, transversality or
pre-hit positivity is claimed or needed.
(rep:) primitive lift (rho, eta); Q = rho^2 - rho eta + eta^2.  (transport:) T_s(rho, eta) = (rho - sin eta, eta + sinh rho - sin eta).
MODES
 --shoot [N]   [ENG/NUM, mpmath]: sample a mid-band arc of A (0.1 rad), find two sample points (adjacency not required — IVT
               needs only opposite signs at the same N) whose D_s at step N have opposite signs with |D_s| >= 0.05; freeze exact rationals x_-, x_+, N in e3b_candidate.json. Not part of the proof.
 --cert        [ALG / ALG via IA]: (G1) Q(I(t)) for the affine segment is an exact rational quadratic in t; its min and max on [-1, 1]
               are computed exactly and certified in [q1, q2);  (G2) D_s(T_s^N x_-) > 0 and D_s(T_s^N x_+) < 0 certified in Arb
               (PREC bits, two exact point orbits; fail closed if a ball straddles 0);  (G3) IVT assembly.
"""
import sys, json, hashlib
from fractions import Fraction as Fr
Q1, Q2 = Fr(7, 200), Fr(58107, 1600000)
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()

def shoot(N=200, dps=120, n_pts=400):
    import mpmath as mp
    mp.mp.dps = dps
    qm = (Q1 + Q2)/2; Q = mp.mpf(qm.numerator)/qm.denominator
    def lift(Qv, th):
        W = mp.sqrt(Qv)*mp.e**(1j*th); e = mp.im(W)/(mp.sqrt(3)/2); return (mp.re(W) + e/2, e)
    def DN(x):
        for _ in range(N): s = mp.sin(x[1]); x = (x[0] - s, x[1] + mp.sinh(x[0]) - s)
        return 1 + (mp.cosh(x[0]) - 1)*mp.cos(x[1])
    th0, dth = mp.mpf('0.7'), mp.mpf('0.1')                   # chord over 0.1 rad at mid-band Q: Q dips ~ Q dth^2/4 ~ 9e-5 << band half-width 6.6e-4 (G1 certifies exactly)
    pts = [lift(Q, th0 + k*dth/n_pts) for k in range(n_pts + 1)]
    vals = [DN(p) for p in pts]
    pos = [k for k in range(n_pts + 1) if vals[k] > mp.mpf('0.05')]; neg = [k for k in range(n_pts + 1) if vals[k] < mp.mpf('-0.05')]
    if pos and neg:
        kp, kn = min(((a, b) for a in pos for b in neg), key=lambda ab: abs(ab[0] - ab[1]))   # closest opposite-sign pair
        xm, xp = pts[kp], pts[kn]
    else:
        print("[shoot] no bracket with |D_s| >= 0.05 on this chord; try another N"); sys.exit(1)
    def rat(v, D=dps - 10): return Fr(int(mp.nint(v*mp.mpf(10)**D)), 10**D)
    cand = dict(mode="shoot [ENG/NUM]", N=N, x_minus=[str(rat(xm[0])), str(rat(xm[1]))], x_plus=[str(rat(xp[0])), str(rat(xp[1]))],
                shoot=dict(Q=str(qm), theta0=str(th0), dtheta=str(dth), n_pts=n_pts, D_minus=float(DN(xm)), D_plus=float(DN(xp))))
    json.dump(cand, open("e3b_candidate.json", "w"), indent=1)
    print(f"[shoot] N = {N}: D_s(T^N x_-) = {float(DN(xm)):+.4f}, D_s(T^N x_+) = {float(DN(xp)):+.4f} -> e3b_candidate.json")

def cert(cand_path="e3b_candidate.json", PREC=1024):
    import flint
    flint.ctx.prec = PREC; arb = flint.arb
    C = json.load(open(cand_path)); N = int(C["N"])
    xm = [Fr(C["x_minus"][0]), Fr(C["x_minus"][1])]; xp = [Fr(C["x_plus"][0]), Fr(C["x_plus"][1])]
    ok = True; out = {}
    def check(name, cond, info=""):
        nonlocal ok
        print(f"[{'PASS' if cond else 'FAIL'}] {name} {info}", flush=True); ok = ok and bool(cond)
    # G1: exact quadratic Q(I(t)), I(t) = m + t h, m = (x_- + x_+)/2, h = (x_+ - x_-)/2
    m = [(xm[i] + xp[i])/2 for i in range(2)]; h = [(xp[i] - xm[i])/2 for i in range(2)]
    def Qf(r, e): return r*r - r*e + e*e
    a2 = h[0]*h[0] - h[0]*h[1] + h[1]*h[1]; a1 = 2*m[0]*h[0] - (m[0]*h[1] + m[1]*h[0]) + 2*m[1]*h[1]; a0 = Qf(m[0], m[1])
    cands = [Fr(-1), Fr(1)] + ([-a1/(2*a2)] if a2 != 0 and -1 <= -a1/(2*a2) <= 1 else [])
    vals = [a0 + a1*t + a2*t*t for t in cands]; qmin, qmax = min(vals), max(vals)
    check("G1 segment [x_-, x_+] lies in A (exact rational quadratic in t)", qmin >= Q1 and qmax < Q2, f"Q in [{float(qmin):.10f}, {float(qmax):.10f}]")
    # G2: two exact point orbits in Arb
    def DsN(x0):
        r, e = arb(x0[0].numerator)/x0[0].denominator, arb(x0[1].numerator)/x0[1].denominator
        for _ in range(N): s = e.sin(); r, e = r - s, e + r.sinh() - s
        return 1 + (r.cosh() - 1)*e.cos()
    Dm, Dp = DsN(xm), DsN(xp)
    check("G2 D_s(T_s^N x_-) > 0 (Arb)", Dm > 0, f"= {Dm.str(12)}")
    check("G2 D_s(T_s^N x_+) < 0 (Arb)", Dp < 0, f"= {Dp.str(12)}")
    check("G3 IVT: exists x* in [x_-, x_+] subset A with T_s^N x* in C0^(s); -x* is an antipodal witness (exact oddness)", ok)
    rec = dict(rid="RECOG-THM-TWIN-C0-ACCESS", script_sha256=sha(__file__), candidate_sha256=sha(cand_path), flint=flint.__version__,
               prec_bits=PREC, N=N, x_minus=C["x_minus"], x_plus=C["x_plus"], Q_range=[str(qmin), str(qmax)],
               D_minus=Dm.str(20), D_plus=Dp.str(20), all_checks_pass=ok)
    json.dump(rec, open("e3b_cert.json", "w"), indent=1)
    print("E3B CERTIFICATE PASS" if ok else "E3B CERTIFICATE FAIL"); sys.exit(0 if ok else 1)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--shoot": shoot(int(sys.argv[2]) if len(sys.argv) > 2 else 200)
    elif len(sys.argv) > 1 and sys.argv[1] == "--cert": cert(sys.argv[2] if len(sys.argv) > 2 else "e3b_candidate.json")
    else: print(__doc__); sys.exit(2)
