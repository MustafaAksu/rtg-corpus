#!/usr/bin/env python3
r"""
recog_cell_e3a4_crossing.py — RECOG OPEN R7 / CELL-E3A-4: certified crossing of the period-9 local stable graph from the annulus A.
Target RID: RECOG-THM-TWIN-STAGE2-NONUNIVERSAL  [THM]  (scope: diagnostic twin T_s, SG-R4). Preregistration: RECOG_E3A4_PREREGISTRATION.md.

Claim: there is x* in A = {7/200 <= Q < 58107/1600000} with D_s(T_s^n x*) > 0 for all n >= 0, so the universal R7 Stage-2 statement
"for all x in A there is n with D_s(T_s^n x) < 0" is FALSE. Corollary: that survivor never meets C0^(s). No genericity / measure claim.

(rep:) primitive LIFT (rho, eta).  (transport:) T_s(rho, eta) = (rho - sin eta, eta + sinh rho - sin eta); D_s = 1 + (cosh rho - 1) cos eta.
Upstream (fail-closed): e3a3a_p9_saddle.json (rev. 1.2) and e3a3b_p9_stable_local.json (rev. 1.1): exact frame c, P0, rectangle r = 1e-6,
gamma, rational separator  h_-(s) = U_LO - (|s| + S_HI)/gamma,  h_+(s) = U_HI + (|s| + S_HI)/gamma  (3b: u < h_- => negative side,
u > h_+ => positive side, for points of c + P0 R).
MODES
 --shoot LATE_CELLS.jsonl   [ENG/NUM, mpmath; NOT part of the proof]: from E3A-1 late seeds, find an approach to the period-9 orbit, append
     (9 - j) mod 9 steps so the terminal test is in the phase-0 chart, Newton along the gradient of the terminal unstable coordinate to a
     crossing point, choose N (extra near-saddle periods until |s| < r/4) and a half-vector w so that u(x_c +- w) ~ +-r/10; freeze the
     candidate (x_c, w, N, L) as exact rationals in e3a4_candidate.json.
 --cert [CANDIDATE]          [ALG via IA, Arb]: reads ONLY the frozen candidate and certifies
     (C1) I = {x_c + t w : -1 <= t <= 1} lies in A  (Q = rho^2 - rho eta + eta^2 on the lift);
     (C2) every piece of I, transported from step 0 by the in-source Lohner kernel, has inf D_s > 0 at steps 0..N-1;
     (C3) every piece's terminal enclosure, minus (0, 2 pi L), lies in c + P0 R  (|s|, |u| < r in the exact 3b frame);
     (C4) coverage: the certified pieces tile [-1, 1] with exact rational endpoints, ordered, no gaps;
     (C5) the endpoints t = -1, +1 (transported as exact points) lie on opposite certified sides: one has u < h_-(s), the other u > h_+(s).
     Then f(t) = u(t) - h(s(t)) is continuous on [-1, 1] (h Lipschitz by 3b) with opposite endpoint signs; IVT gives t* with
     T_s^N(x(t*)) - (0, 2 pi L) on the local stable graph; C2 gives D_s > 0 for n < N and 3b (G4) for every n >= N.
     Failure policy: a failing piece is re-transported from step 0 as two exact t-halves (geometric cause); if the piece is already narrower
     than MIN_DT, precision is doubled up to 4096 bits (arithmetic cause); otherwise fail closed.
"""
import sys, os, json, hashlib, time, math
from fractions import Fraction as Fr

EXP_3A = "01ba69c3b5a36afc6ff5baf46eaf14de86876533546f7e6f93c4b187bb642cef"
EXP_3B = "545ecf628d6bdc40fe16530624935380868ae7252d6da23ad10f88421fc4531a"
Q1, Q2 = Fr(7, 200), Fr(58107, 1600000)
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def load_upstream():
    for p, h in (("e3a3a_p9_saddle.json", EXP_3A), ("e3a3b_p9_stable_local.json", EXP_3B)):
        if sha(p) != h: print(f"[FAIL] {p} hash mismatch"); sys.exit(1)
    a, b = json.load(open("e3a3a_p9_saddle.json")), json.load(open("e3a3b_p9_stable_local.json"))
    assert a["all_checks_pass"] and b["all_checks_pass"]
    fr = b["frame"]; sep = b["separator"]
    return dict(c=[Fr(fr["c"][0]), Fr(fr["c"][1])], vs=[Fr(fr["v_s0"][0]), Fr(fr["v_s0"][1])], vu=[Fr(fr["v_u0"][0]), Fr(fr["v_u0"][1])],
                r=Fr(1, 10**int(b["rectangle_r"].split("e-")[1])), gamma=int(sep["gamma"]),
                U_LO=Fr(sep["U_LO"]), U_HI=Fr(sep["U_HI"]), S_HI=Fr(sep["S_HI"]),
                orbit=[(Fr(o[0]), Fr(o[1])) for o in a["orbit_centres"]])
def Pinv_of(U):
    vs, vu = U["vs"], U["vu"]; det = vs[0]*vu[1] - vu[0]*vs[1]
    return [[vu[1]/det, -vu[0]/det], [-vs[1]/det, vs[0]/det]]

# =============================== SHOOT (mpmath, heuristic) ===============================
def shoot(late_path, dps=200, top=40):
    import mpmath as mp
    mp.mp.dps = dps
    U = load_upstream(); Pi = Pinv_of(U); r = U["r"]
    P = [[mp.mpf(x.numerator)/x.denominator for x in row] for row in Pi]; c = [mp.mpf(x.numerator)/x.denominator for x in U["c"]]
    orb = [(mp.mpf(o[0].numerator)/o[0].denominator, mp.mpf(o[1].numerator)/o[1].denominator) for o in U["orbit"]]
    def T(x): s = mp.sin(x[1]); return (x[0] - s, x[1] + mp.sinh(x[0]) - s)
    def DT(x): cs = mp.cos(x[1]); return mp.matrix([[1, -cs], [mp.cosh(x[0]), 1 - cs]])
    def Ds(x): return 1 + (mp.cosh(x[0]) - 1)*mp.cos(x[1])
    def wrap(v): return v - 2*mp.pi*mp.nint(v/(2*mp.pi))
    cells = [json.loads(l) for l in open(late_path)]
    dmax = max(cl["d"] for cl in cells); cells = sorted([cl for cl in cells if cl["d"] >= dmax - 2], key=lambda cl: -cl["tau_centre"])
    seen, seeds = set(), []
    for cl in cells:
        qc = (Fr(cl["Q_bounds"][0]) + Fr(cl["Q_bounds"][1]))/2; tc = (Fr(cl["theta_bounds_over_pi"][0]) + Fr(cl["theta_bounds_over_pi"][1]))/2
        if (qc, tc) in seen: continue
        seen.add((qc, tc)); seeds.append((qc, tc, cl["tau_centre"]))
        if len(seeds) >= top: break
    best = None
    for qc, tc, tau in seeds:
        Q = mp.mpf(qc.numerator)/qc.denominator; th = mp.pi*mp.mpf(tc.numerator)/tc.denominator
        W = mp.sqrt(Q)*mp.e**(1j*th); e = mp.im(W)/(mp.sqrt(3)/2); x = (mp.re(W) + e/2, e)
        for n in range(tau):
            for j in range(9):
                d = mp.sqrt((x[0] - orb[j][0])**2 + wrap(x[1] - orb[j][1])**2)
                if best is None or d < best[0]: best = (d, (qc, tc, tau), n, j)
            x = T(x)
    d, (qc, tc, tau), n0, j0 = best
    print(f"[shoot] closest approach to the period-9 orbit: {mp.nstr(d, 5)} at step {n0}, phase {j0} (seed tau {tau})")
    Q = mp.mpf(qc.numerator)/qc.denominator; th = mp.pi*mp.mpf(tc.numerator)/tc.denominator
    W = mp.sqrt(Q)*mp.e**(1j*th); e = mp.im(W)/(mp.sqrt(3)/2); x0 = (mp.re(W) + e/2, e)
    def xi_and_grad(x, N):
        y = x; M = mp.eye(2); dmin = mp.inf
        for _ in range(N):
            dmin = min(dmin, Ds(y)); M = DT(y)*M; y = T(y)
        L = int(mp.nint((y[1] - c[1])/(2*mp.pi)))
        z = (y[0] - c[0], y[1] - 2*mp.pi*L - c[1])
        s = P[0][0]*z[0] + P[0][1]*z[1]; u = P[1][0]*z[0] + P[1][1]*z[1]
        g = mp.matrix([[P[1][0], P[1][1]]])*M
        return s, u, (g[0, 0], g[0, 1]), L, dmin
    N = n0 + (9 - j0) % 9
    x = x0
    for rounds in range(40):
        for it in range(80):
            s, u, g, L, dmin = xi_and_grad(x, N); gn = mp.sqrt(g[0]**2 + g[1]**2)
            step = -u/gn; x = (x[0] + step*g[0]/gn, x[1] + step*g[1]/gn)
            if abs(u) < mp.mpf(10)**(-(dps//2)): break
        s, u, g, L, dmin = xi_and_grad(x, N)
        print(f"[shoot] N = {N}: |s| = {mp.nstr(abs(s), 4)}, |u| = {mp.nstr(abs(u), 4)}, min D_s on prefix = {mp.nstr(dmin, 5)}, L = {L}")
        if abs(s) < mp.mpf(r.numerator)/r.denominator/4 and dmin > 0: break
        N += 9
    gn = mp.sqrt(g[0]**2 + g[1]**2); delta = (mp.mpf(r.numerator)/r.denominator/10)/gn
    w = (delta*g[0]/gn, delta*g[1]/gn)
    def rat(v, D=dps - 20): return Fr(int(mp.nint(v*mp.mpf(10)**D)), 10**D)
    xc = (rat(x[0]), rat(x[1])); wr = (rat(w[0]), rat(w[1]))
    cand = dict(mode="shoot [ENG/NUM]", x_c=[str(xc[0]), str(xc[1])], w=[str(wr[0]), str(wr[1])], N=N, L=L,
                seed=dict(Q=str(qc), theta_over_pi=str(tc), tau=tau), approach=dict(dist=float(d), step=n0, phase=j0),
                upstream=dict(e3a3a=EXP_3A, e3a3b=EXP_3B), shoot_dps=dps)
    json.dump(cand, open("e3a4_candidate.json", "w"), indent=1)
    print(f"[shoot] candidate frozen: N = {N}, L = {L}, |w| ~ {mp.nstr(mp.sqrt(w[0]**2 + w[1]**2), 4)} -> e3a4_candidate.json")

# =============================== CERT (Arb, theorem-grade) ===============================
def cert(cand_path, prec0=1024, prec_max=4096, min_dt=Fr(1, 2**20)):
    import flint
    arb = flint.arb
    U = load_upstream(); Pi = Pinv_of(U); cand = json.load(open(cand_path)); hc = sha(cand_path)
    assert cand["upstream"]["e3a3a"] == EXP_3A and cand["upstream"]["e3a3b"] == EXP_3B
    xc = [Fr(cand["x_c"][0]), Fr(cand["x_c"][1])]; w = [Fr(cand["w"][0]), Fr(cand["w"][1])]; N, L = int(cand["N"]), int(cand["L"])
    ok = True; log = []
    def check(name, cond, info=""):
        nonlocal ok
        print(f"[{'PASS' if cond else 'FAIL'}] {name} {info}", flush=True); ok = ok and bool(cond); log.append(dict(check=name, ok=bool(cond), info=info))
    def setprec(p): flint.ctx.prec = p
    def A(q): return arb(q.numerator)/q.denominator
    # ---- Lohner kernel (in-source) ----
    def T(v): s = v[1].sin(); return [v[0] - s, v[1] + v[0].sinh() - s]
    def DT(v): cs = v[1].cos(); return [[arb(1), -cs], [v[0].cosh(), 1 - cs]]
    def Ds(v): return 1 + (v[0].cosh() - 1)*v[1].cos()
    def mm(X, Y): return [[X[i][0]*Y[0][j] + X[i][1]*Y[1][j] for j in range(2)] for i in range(2)]
    def mv(X, v): return [X[0][0]*v[0] + X[0][1]*v[1], X[1][0]*v[0] + X[1][1]*v[1]]
    def inv(M):
        d = M[0][0]*M[1][1] - M[0][1]*M[1][0]; return [[M[1][1]/d, -M[0][1]/d], [-M[1][0]/d, M[0][0]/d]]
    def pt(x): return arb(x.mid())
    def step(c, Af, E):
        X = [c[i] + Af[i][0]*E[0] + Af[i][1]*E[1] for i in range(2)]
        H = [X[i].union(c[i]) for i in range(2)]
        Tc = T(c); M = mm(DT(H), Af)
        Mm = [[pt(M[i][j]) for j in range(2)] for i in range(2)]
        wts = [float(E[j].rad()) for j in range(2)]
        k = 0 if wts[0] >= wts[1] else 1
        col = [Mm[0][k], Mm[1][k]]; nrm = (col[0]*col[0] + col[1]*col[1]).sqrt()
        if not (nrm > 0): col, nrm = [arb(1), arb(0)], arb(1)
        q0 = [pt(col[0]/nrm), pt(col[1]/nrm)]; q1 = [-q0[1], q0[0]]
        A2 = [[q0[0], q1[0]], [q0[1], q1[1]]] if k == 0 else [[q1[0], q0[0]], [q1[1], q0[1]]]
        Ai = inv(A2); c2 = [pt(Tc[0]), pt(Tc[1])]
        off = mv(Ai, [Tc[0] - c2[0], Tc[1] - c2[1]]); AM = mm(Ai, M)
        E2 = [off[i] + AM[i][0]*E[0] + AM[i][1]*E[1] for i in range(2)]
        return c2, A2, E2, H
    def transport(ta, tb, prec):
        setprec(prec)
        tm, ht = (ta + tb)/2, (tb - ta)/2
        c = [A(xc[i] + tm*w[i]) for i in range(2)]
        wn = A(w[0]*w[0] + w[1]*w[1]).sqrt(); u0 = [pt(A(w[0])/wn), pt(A(w[1])/wn)]
        Af = [[u0[0], -u0[1]], [u0[1], u0[0]]]
        Ainv = inv(Af); e0 = mv(Ainv, [A(ht*w[0]), A(ht*w[1])])     # exact parameterisation of the piece in the frame
        E = [e0[0]*arb(0, 1), e0[1]*arb(0, 1)]
        dlow = []
        for n in range(N):
            c, Af, E, H = step(c, Af, E)
            dH = Ds(H)
            if not (dH > 0): return None, f"D_s not certified > 0 at step {n}", dlow
            dlow.append(float(dH.lower()))
        X = [c[i] + Af[i][0]*E[0] + Af[i][1]*E[1] for i in range(2)]
        z = [X[0] - A(U["c"][0]), X[1] - 2*L*arb.pi() - A(U["c"][1])]
        xi = mv([[A(Pi[0][0]), A(Pi[0][1])], [A(Pi[1][0]), A(Pi[1][1])]], z)
        return xi, None, dlow
    t0 = time.time(); r = A(U["r"]) if False else None
    setprec(prec0); rA = A(U["r"])
    # C1: I inside A
    tball = arb(0, 1)
    xr = [A(xc[i]) + A(w[i])*tball for i in range(2)]
    Qb = xr[0]*xr[0] - xr[0]*xr[1] + xr[1]*xr[1]
    check("C1 segment I lies in A (q1 <= Q < q2 on the lift)", Qb >= A(Q1) and Qb < A(Q2), f"Q in [{float(Qb.lower()):.9f}, {float(Qb.upper()):.9f}]")
    # C2-C4: pieces
    queue = [(Fr(-1), Fr(1), prec0)]; pieces = []; splits = esc = 0; dmin_by_step = None
    while queue:
        ta, tb, prec = queue.pop(0)
        xi, why, dlow = transport(ta, tb, prec)
        good = xi is not None and abs(xi[0]) < A(U["r"]) and abs(xi[1]) < A(U["r"])
        if good:
            pieces.append((ta, tb, prec, [xi[0].str(10), xi[1].str(10)]))
            dmin_by_step = dlow if dmin_by_step is None else [min(a_, b_) for a_, b_ in zip(dmin_by_step, dlow)]
            continue
        if tb - ta > min_dt:
            m = (ta + tb)/2; queue[0:0] = [(ta, m, prec), (m, tb, prec)]; splits += 1
        elif prec < prec_max:
            queue.insert(0, (ta, tb, prec*2)); esc += 1
        else:
            check(f"piece [{ta}, {tb}] certified", False, why or "terminal enclosure not inside R"); break
    pieces.sort(key=lambda p: p[0])
    cover = bool(pieces) and pieces[0][0] == -1 and pieces[-1][1] == 1 and all(pieces[i][1] == pieces[i + 1][0] for i in range(len(pieces) - 1))
    check("C2 inf D_s > 0 at every step 0..N-1 on every piece", ok and dmin_by_step is not None,
          f"min over steps of the certified lower bounds = {min(dmin_by_step):.4f}" if dmin_by_step else "")
    check("C3 every terminal piece lies in c + P0 R", ok and cover, f"{len(pieces)} pieces, {splits} splits, {esc} precision escalations")
    check("C4 coverage: pieces tile [-1, 1] exactly (rational, ordered, no gaps)", cover)
    # C5: endpoint sides (exact points)
    def endpoint(t, prec):
        setprec(prec)
        c = [A(xc[i] + t*w[i]) for i in range(2)]; Af = [[arb(1), arb(0)], [arb(0), arb(1)]]; E = [arb(0), arb(0)]
        for n in range(N): c, Af, E, H = step(c, Af, E)
        X = [c[i] + Af[i][0]*E[0] + Af[i][1]*E[1] for i in range(2)]
        z = [X[0] - A(U["c"][0]), X[1] - 2*L*arb.pi() - A(U["c"][1])]
        return mv([[A(Pi[0][0]), A(Pi[0][1])], [A(Pi[1][0]), A(Pi[1][1])]], z)
    sides = {}
    for t in (Fr(-1), Fr(1)):
        xi = endpoint(t, prec0); g = arb(U["gamma"])
        hm = A(U["U_LO"]) - (abs(xi[0]).upper() + A(U["S_HI"]))/g; hp = A(U["U_HI"]) + (abs(xi[0]).upper() + A(U["S_HI"]))/g
        neg, pos = bool(xi[1] < hm), bool(xi[1] > hp)
        sides[str(t)] = dict(s=xi[0].str(15), u=xi[1].str(15), negative=neg, positive=pos,
                             margin=float((hm - xi[1]).lower()) if neg else (float((xi[1] - hp).lower()) if pos else None))
    opp = (sides["-1"]["negative"] and sides["1"]["positive"]) or (sides["-1"]["positive"] and sides["1"]["negative"])
    check("C5 endpoints on opposite certified sides of the stable graph", opp, json.dumps({k: (v["negative"], v["positive"], v["margin"]) for k, v in sides.items()}))
    rec = dict(rid="RECOG-THM-TWIN-STAGE2-NONUNIVERSAL", script_sha256=sha(__file__), candidate_sha256=hc,
               upstream=dict(e3a3a=EXP_3A, e3a3b=EXP_3B), flint=flint.__version__, prec0=prec0, prec_max=prec_max,
               x_c=cand["x_c"], w=cand["w"], N=N, L=L, Q_range=[Qb.lower().str(20), Qb.upper().str(20)],
               pieces=[dict(t=[str(p[0]), str(p[1])], prec=p[2], xi_terminal=p[3]) for p in pieces],
               splits=splits, escalations=esc, D_s_min_lower_by_step=dmin_by_step, endpoints=sides, checks=log,
               all_checks_pass=ok, seconds=round(time.time() - t0, 1))
    json.dump(rec, open("e3a4_cert.json", "w"), indent=1)
    print("E3A-4 CERTIFICATE PASS" if ok else "E3A-4 CERTIFICATE FAIL"); sys.exit(0 if ok else 1)

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--shoot": shoot(sys.argv[2])
    elif len(sys.argv) > 1 and sys.argv[1] == "--cert": cert(sys.argv[2] if len(sys.argv) > 2 else "e3a4_candidate.json")
    else: print(__doc__); sys.exit(2)
