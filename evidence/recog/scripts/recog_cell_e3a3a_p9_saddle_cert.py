#!/usr/bin/env python3
r"""
recog_cell_e3a3a_p9_saddle_cert.py — RECOG OPEN R7 / CELL-E3A-3a: certified period-9, winding-4, positive-D_s hyperbolic saddle of T_s.
Target RID: RECOG-THM-TWIN-P9-SADDLE   [ALG via IA]   (scope: diagnostic twin, SG-R4)

(rep:) primitive LIFT (rho, eta) — no reduction mod 2 pi;  (transport:) T_s(rho, eta) = (rho - sin eta, eta + sinh rho - sin eta),
D_s = det DT_s = 1 + (cosh rho - 1) cos eta,  DT_s = [[1, -cos eta], [cosh rho, 1 - cos eta]].
T_s(rho, eta + 2 pi) = T_s(rho, eta) + (0, 2 pi), so a winding-k period-p orbit on the cylinder is a root of
   G_{p,k}(x) = T_s^p(x) - x - (0, 2 pi k).        Here p = 9, k = 4.
Certified items (Arb, PREC bits):
 1. Krawczyk:  K(X0) = xh - Y G(xh) + (I - Y DG(X0)) (X0 - xh)  strictly inside X0  =>  unique root x9 in X0 of G_{9,4}.
    Minimal period 9 on the cylinder follows arithmetically: if d | 9, d < 9 had T^d x = x + (0, 2 pi k_d), then 4 = k_d * 9/d with 9/d in {3, 9}.
 2. Orbit enclosures X_i  (i = 0..8, X_i = T_s^i(X0) by ball arithmetic) with inf D_s(X_i) > 0 — all nine lower bounds reported.
 3. Monodromy enclosure M ⊇ DT_s^9(x9) (product of DT_s over the X_i); tr M, det M, Delta = tr^2 - 4 det > 0; real multipliers
    lambda_{s,u} = (tr -+ sqrt Delta)/2 with 0 < |lambda_s| < 1 < |lambda_u|.
 4. Eigendirections: interval vectors v = (M12, lambda - M11) (normalised), reported for E^s and E^u.
 5. Positive primitive neighbourhood: boxes B_i = X_i inflated by RB in each coordinate with inf D_s(B_i) >= delta_D > 0 (all nine).
Candidate seed (40-digit Newton from E3A-1 recurrence, [NUM]): x ~ (1.210718, -1.396099).
Rev. 1.1: adds the simple-root / nonsingular-preconditioner check 1h (certificate hardening).
Rev. 1.2: exports a SAFE root box — a 60-digit decimal centre and an exact radius 10^-35 — and certifies in Arb that the Krawczyk
enclosure lies inside it (rev. 1.1 printed a 40-digit centre with the 1e-97 Krawczyk radius, which is not a certified enclosure).
Usage: python recog_cell_e3a3a_p9_saddle_cert.py [prec_bits] [RB]     (defaults 512, 1/100)
"""
import sys, json, hashlib
from fractions import Fraction as Fr
import flint
import mpmath as mp

PREC = int(sys.argv[1]) if len(sys.argv) > 1 else 512
RB = Fr(sys.argv[2]) if len(sys.argv) > 2 else Fr(1, 100)
P, KW = 9, 4
flint.ctx.prec = PREC; arb = flint.arb
mp.mp.dps = int(PREC*0.30)
ok = True
def check(name, cond, info=""):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name} {info}", flush=True); ok = ok and bool(cond)

# ---------- high-precision Newton for the candidate (non-rigorous; only supplies the centre) ----------
def T_mp(x): s = mp.sin(x[1]); return (x[0] - s, x[1] + mp.sinh(x[0]) - s)
def DT_mp(x): c = mp.cos(x[1]); return mp.matrix([[1, -c], [mp.cosh(x[0]), 1 - c]])
def G_and_DG_mp(x):
    y = x; M = mp.eye(2)
    for _ in range(P): M = DT_mp(y)*M; y = T_mp(y)
    return mp.matrix([y[0] - x[0], y[1] - x[1] - 2*KW*mp.pi]), M - mp.eye(2)
x = (mp.mpf('1.210718'), mp.mpf('-1.396099'))
for _ in range(200):
    Gv, J = G_and_DG_mp(x); dx = mp.lu_solve(J, -Gv); x = (x[0] + dx[0], x[1] + dx[1])
    if mp.norm(dx) < mp.mpf(10)**(-(mp.mp.dps - 10)): break
Gv, J = G_and_DG_mp(x)
print(f"Newton centre: rho = {mp.nstr(x[0], 30)}, eta = {mp.nstr(x[1], 30)}, |G| = {mp.nstr(mp.norm(Gv), 5)}")

# ---------- Arb objects ----------
def A(v): return arb(mp.nstr(v, mp.mp.dps)).mid()          # exact point (dyadic) near v
xh = [A(x[0]), A(x[1])]
r0 = arb(2)**(-(PREC//3))                                    # Krawczyk box radius
X0 = [arb(xh[0], r0), arb(xh[1], r0)]
two_pi_k = 2*KW*arb.pi()
def T(v): s = v[1].sin(); return [v[0] - s, v[1] + v[0].sinh() - s]
def DT(v): c = v[1].cos(); return [[arb(1), -c], [v[0].cosh(), 1 - c]]
def mm(Ma, Mb): return [[Ma[i][0]*Mb[0][j] + Ma[i][1]*Mb[1][j] for j in range(2)] for i in range(2)]
def orbit_and_jac(v0):
    v = v0; M = [[arb(1), arb(0)], [arb(0), arb(1)]]; orb = [v0]
    for _ in range(P):
        M = mm(DT(v), M); v = T(v); orb.append(v)
    return orb, M
def Dsf(v): return 1 + (v[0].cosh() - 1)*v[1].cos()

# 1. Krawczyk
orb_pt, _ = orbit_and_jac(xh)
Gh = [orb_pt[-1][0] - xh[0], orb_pt[-1][1] - xh[1] - two_pi_k]
orbX, MX = orbit_and_jac(X0)
DGX = [[MX[0][0] - 1, MX[0][1]], [MX[1][0], MX[1][1] - 1]]
Jm = mp.matrix([[J[0, 0], J[0, 1]], [J[1, 0], J[1, 1]]]); Ym = mp.inverse(Jm)
Y = [[A(Ym[i, j]) for j in range(2)] for i in range(2)]
YG = [Y[i][0]*Gh[0] + Y[i][1]*Gh[1] for i in range(2)]
YD = mm(Y, DGX); C = [[(1 if i == j else 0) - YD[i][j] for j in range(2)] for i in range(2)]
dX = [X0[0] - xh[0], X0[1] - xh[1]]
K = [xh[i] - YG[i] + (C[i][0]*dX[0] + C[i][1]*dX[1]) for i in range(2)]
inside = all(K[i].lower() > X0[i].lower() and K[i].upper() < X0[i].upper() for i in range(2))
check("1. Krawczyk K(X0) strictly inside X0 => unique root x9 of G_{9,4} in X0", inside,
      f"(box radius 2^-{PREC//3}; K radius {float(max(K[0].rad(), K[1].rad())):.2e})")
detDG = DGX[0][0]*DGX[1][1] - DGX[0][1]*DGX[1][0]; detY = Y[0][0]*Y[1][1] - Y[0][1]*Y[1][0]
check("1h. hardening: 0 notin det DG(X0) (simple root) and 0 notin det Y (nonsingular preconditioner)", (detDG < 0 or detDG > 0) and (detY < 0 or detY > 0),
      f"det DG(X0) = {detDG.str(10)}")
check("1'. minimal period 9 on the cylinder (gcd(9,4) = 1 argument; winding fixed by G_{9,4})", True)

# 2. orbit enclosures with positive D_s (use the certified root box K, which contains x9)
Xr = [K[0], K[1]]; orbK, MK = orbit_and_jac(Xr)
Dlow = [float(Dsf(orbK[i]).lower()) for i in range(P)]
check("2. inf D_s(X_i) > 0 for i = 0..8", all(Dsf(orbK[i]) > 0 for i in range(P)), f"lower bounds {[round(d, 4) for d in Dlow]}")
print("   orbit (lift):", [(round(float(v[0].mid()), 5), round(float(v[1].mid()), 5)) for v in orbK[:P]])

# 3. monodromy and multipliers
M = MK; tr = M[0][0] + M[1][1]; det = M[0][0]*M[1][1] - M[0][1]*M[1][0]; disc = tr*tr - 4*det
check("3. Delta = tr^2 - 4 det > 0 (real multipliers)", disc > 0, f"tr = {float(tr.mid()):.6f}, det = {float(det.mid()):.6f}, Delta = {float(disc.mid()):.4f}")
sq = disc.sqrt(); lam = [(tr - sq)/2, (tr + sq)/2]
ls, lu = (lam[0], lam[1]) if abs(lam[0]).upper() < abs(lam[1]).lower() else (lam[1], lam[0])
check("3'. 0 < |lambda_s| < 1 < |lambda_u|", abs(ls) > 0 and abs(ls) < 1 and abs(lu) > 1,
      f"lambda_s = {ls.str(12)}, lambda_u = {lu.str(12)}")
# determinant cross-check: det M = prod D_s(orbit)
prodD = arb(1)
for i in range(P): prodD = prodD*Dsf(orbK[i])
check("3''. det M = prod_i D_s(x_i) (consistency)", abs(det - prodD).upper() < 1e-20)

# 4. eigendirections
def evec(l):
    v = [M[0][1], l - M[0][0]]; n = (v[0]*v[0] + v[1]*v[1]).sqrt(); return [v[0]/n, v[1]/n]
vs, vu = evec(ls), evec(lu)
indep = abs(vs[0]*vu[1] - vs[1]*vu[0]) > 0
check("4. eigendirections E^s, E^u enclosed and independent", indep,
      f"E^s = ({vs[0].str(10)}, {vs[1].str(10)}), E^u = ({vu[0].str(10)}, {vu[1].str(10)})")

# 5. positive primitive neighbourhood
rb = arb(RB.numerator)/RB.denominator
B = [[arb(orbK[i][0].mid(), rb + orbK[i][0].rad()), arb(orbK[i][1].mid(), rb + orbK[i][1].rad())] for i in range(P)]
DB = [Dsf(B[i]) for i in range(P)]
deltaD = min(float(d.lower()) for d in DB)
check(f"5. inf D_s(B_i) > 0 on boxes inflated by {RB} (all nine)", all(d > 0 for d in DB), f"delta_D = {deltaD:.4f}; lower bounds {[round(float(d.lower()), 4) for d in DB]}")

SAFE_RAD = Fr(1, 10**35)
safe_c = [K[i].mid().str(60, radius=False) for i in range(2)]
safe_ok = all((K[i] - arb(safe_c[i])).__abs__().upper() < arb(1)/10**35 for i in range(2))
check("1s. safe root box: Krawczyk enclosure K lies inside (decimal centre, exact radius 1e-35)", safe_ok)
rec = dict(rid="RECOG-THM-TWIN-P9-SADDLE", script_sha256=hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
           flint=flint.__version__, prec_bits=PREC, period=P, winding=KW, krawczyk_box_radius_log2=-(PREC//3),
           root_box=[[K[i].mid().str(40, radius=False), float(K[i].rad())] for i in range(2)], root_box_note='internal Krawczyk ball (40-digit print); NOT for downstream use',
           safe_root_box=dict(centre=safe_c, radius=str(SAFE_RAD), certified='Krawczyk enclosure inside safe box (Arb)'),
           D_s_lower_on_orbit=Dlow, monodromy=[[M[i][j].str(20) for j in range(2)] for i in range(2)],
           det_DG_X0=detDG.str(20), trace=tr.str(20), det=det.str(20), discriminant=disc.str(20), lambda_s=ls.str(20), lambda_u=lu.str(20),
           E_s=[vs[0].str(15), vs[1].str(15)], E_u=[vu[0].str(15), vu[1].str(15)],
           neighbourhood_radius=str(RB), D_s_lower_on_neighbourhood=[float(d.lower()) for d in DB], delta_D=deltaD,
           orbit_centres=[[orbK[i][0].mid().str(25, radius=False), orbK[i][1].mid().str(25, radius=False)] for i in range(P)],
           all_checks_pass=ok)
json.dump(rec, open("e3a3a_p9_saddle.json", "w"), indent=1)
print("E3A-3a CERTIFICATE PASS" if ok else "E3A-3a CERTIFICATE FAIL"); sys.exit(0 if ok else 1)
