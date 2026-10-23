#!/usr/bin/env python3
r"""
recog_cell_e3a3b_p9_stable_local.py — RECOG OPEN R7 / CELL-E3A-3b: certified local stable graph and signed separator of the period-9 saddle.
Target RID: RECOG-THM-TWIN-P9-STABLE-LOCAL   [ALG via IA]   (scope: diagnostic twin, SG-R4; depends on RECOG-THM-TWIN-P9-SADDLE)

Input: e3a3a_p9_saddle.json (rev. 1.1; its sha256 is recorded). Fixed EXACT frame: c = exact midpoint of the certified root box,
v_s0, v_u0 = exact dyadic midpoints of the certified eigendirections, P0 = [v_s0 v_u0]; det P0 != 0 certified; P0^{-1} exact rational.
Return map F(x) = T_s^9(x) - (0, 8 pi) on the lift; chart G(xi) = P0^{-1}(F(c + P0 xi) - c), xi = (s, u).  Rectangle R = [-r, r] x [-r, r].
Interval data on R: B_0 = c + P0 R (box), B_{i+1} = T_s(B_i) (box evaluation), J = prod DT_s(B_i) ⊇ all DT_s^9 on c + P0 R,
DG(R) = P0^{-1} J P0 = [[a, b], [cc, d]] (interval), G(R) ⊆ G(0) + DG(R) R (mean value).
Gates (all certified in Arb):
 (G1) s-mapping:   sup |G_s(R)| < r                                       (R maps into the strip |s| < r)
 (G2) u-edges outward: inf G_u(s, +r) > r and sup G_u(s, -r) < -r for |s| <= r
 (G3) unstable cone C_u = {|ds| <= gam |du|}: mu := inf|d| - gam sup|cc| > 1 and gam sup|a| + sup|b| <= gam mu
 (G4) primitive positivity: inf D_s(B_i) > 0 for i = 0..8 (every primitive step from any point of c + P0 R)
Theorem (standard h-set / cone argument): W = {xi in R : G^n(xi) in R for all n >= 0} is the graph u = h(s), |s| <= r, of a function with
Lipschitz constant <= 1/gam:  (uniqueness) two points of W on one vertical differ by a C_u vector, whose u-separation grows by mu > 1 per
iterate (G3, mean value on convex R), contradiction with staying in R; (existence) each vertical segment {s} x [-r, r] is mapped across R
in u with ends outside (G2) and inside the s-strip (G1), and the nested preimages give a point staying forever; (Lipschitz) two graph points
cannot differ by a C_u vector, so |du| < |ds|/gam. The saddle point xi* (enclosed from the 3a root box) lies on W, so
   h_-(s) := u*_lo - (|s| + |s*|_hi)/gam  <=  h(s)  <=  h_+(s) := u*_hi + (|s| + |s*|_hi)/gam.
Every point of W stays in R under G, hence every primitive iterate lies in some B_i and has D_s > 0 (G4): points of W are survivors.
Separator interface for E3A-4:  u < h_-(s) => negative side;  u > h_+(s) => positive side (strict, for points of R).
r is chosen automatically: start at 1e-3 and shrink by 10 until G1-G4 all pass; gam is the largest of {1e6, ..., 1} passing G3.
Rev. 1.1: uses ONLY the 3a rev. 1.2 safe root box (centre + exact radius 1e-35); fails closed unless the 3a record has the expected
sha256; exports all gate margins (G1 strip, both G2 edges, mu, cone inequality) and a conservative RATIONAL separator.
Usage: python recog_cell_e3a3b_p9_stable_local.py [prec_bits]   (default 512)
"""
import sys, json, hashlib
from fractions import Fraction as Fr
import flint

PREC = int(sys.argv[1]) if len(sys.argv) > 1 else 512
flint.ctx.prec = PREC; arb = flint.arb
EXPECTED_3A = "01ba69c3b5a36afc6ff5baf46eaf14de86876533546f7e6f93c4b187bb642cef"
src = "e3a3a_p9_saddle.json"; rec3a = json.load(open(src)); h3a = hashlib.sha256(open(src, 'rb').read()).hexdigest()
if h3a != EXPECTED_3A: print('[FAIL] e3a3a_p9_saddle.json hash mismatch'); sys.exit(1)
assert rec3a["all_checks_pass"] and rec3a["period"] == 9 and rec3a["winding"] == 4
ok = True
def check(name, cond, info=""):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name} {info}", flush=True); ok = ok and bool(cond)
def A(fr): return arb(fr.numerator)/fr.denominator
# exact frame
c = [Fr(rec3a["safe_root_box"]["centre"][i]) for i in range(2)]
root_rad = [Fr(rec3a["safe_root_box"]["radius"])]*2
def mid_of(s): return Fr(arb(s).mid().str(30, radius=False))
vs0 = [mid_of(rec3a["E_s"][0]), mid_of(rec3a["E_s"][1])]; vu0 = [mid_of(rec3a["E_u"][0]), mid_of(rec3a["E_u"][1])]
detP = vs0[0]*vu0[1] - vu0[0]*vs0[1]
check("frame: det P0 != 0 (exact rational)", detP != 0, f"det P0 = {float(detP):.6f}")
Pinv = [[vu0[1]/detP, -vu0[0]/detP], [-vs0[1]/detP, vs0[0]/detP]]           # exact
P0a = [[A(vs0[0]), A(vu0[0])], [A(vs0[1]), A(vu0[1])]]; Pia = [[A(Pinv[i][j]) for j in range(2)] for i in range(2)]
ca = [A(c[0]), A(c[1])]; shift = 8*arb.pi()
def T(v): s = v[1].sin(); return [v[0] - s, v[1] + v[0].sinh() - s]
def DT(v): cs = v[1].cos(); return [[arb(1), -cs], [v[0].cosh(), 1 - cs]]
def mm(X, Y): return [[X[i][0]*Y[0][j] + X[i][1]*Y[1][j] for j in range(2)] for i in range(2)]
def mv(X, v): return [X[0][0]*v[0] + X[0][1]*v[1], X[1][0]*v[0] + X[1][1]*v[1]]
def Ds(v): return 1 + (v[0].cosh() - 1)*v[1].cos()
def F(v):
    for _ in range(9): v = T(v)
    return [v[0], v[1] - shift]
# saddle point in the chart: xi* = P0^{-1}(x9 - c), x9 in root box
x9 = [arb(ca[i], A(root_rad[i])) for i in range(2)]
xis = mv(Pia, [x9[0] - ca[0], x9[1] - ca[1]])
G0 = mv(Pia, [F(ca)[0] - ca[0], F(ca)[1] - ca[1]])

def attempt(r):
    R = [arb(0, r), arb(0, r)]
    B = [[ca[i] + P0a[i][0]*R[0] + P0a[i][1]*R[1] for i in range(2)]]
    J = [[arb(1), arb(0)], [arb(0), arb(1)]]
    for _ in range(9):
        J = mm(DT(B[-1]), J); B.append(T(B[-1]))
    DG = mm(Pia, mm(J, P0a)); a, b, cc, d = DG[0][0], DG[0][1], DG[1][0], DG[1][1]
    GR = [G0[i] + DG[i][0]*R[0] + DG[i][1]*R[1] for i in range(2)]
    g1 = abs(GR[0]) < r
    up = G0[1] + cc*R[0] + d*arb(r); dn = G0[1] + cc*R[0] - d*arb(r)
    g2 = (up > r and dn < -r) or (up < -r and dn > r)                       # outward (either orientation of d)
    g4 = all(Ds(B[i]) > 0 for i in range(9))
    gam_ok = None
    for gam in (10**6, 10**5, 10**4, 10**3, 10**2, 10, 1):
        g = arb(gam); mu = abs(d).lower() - g*abs(cc).upper()
        if mu > 1 and g*abs(a).upper() + abs(b).upper() <= g*mu: gam_ok = gam; break
    margins = None
    if gam_ok is not None:
        g = arb(gam_ok); mu = abs(d).lower() - g*abs(cc).upper()
        margins = dict(G1_strip=float((arb(r) - abs(GR[0])).lower()), G2_upper_edge=float((abs(up) - r).lower()), G2_lower_edge=float((abs(dn) - r).lower()),
                       mu=float(mu), cone_ineq=float((g*mu - (g*abs(a).upper() + abs(b).upper()))))
    return dict(margins=margins, g1=bool(g1), g2=bool(g2), g3=gam_ok is not None, g4=bool(g4), gam=gam_ok, DG=DG, B=B,
                Dlow=[float(Ds(B[i]).lower()) for i in range(9)], up=up, dn=dn, GRs=GR[0])
chosen = None
for k in range(3, 40):
    r = arb(10)**(-k); res = attempt(r)
    print(f"  r = 1e-{k}: G1 {res['g1']}  G2 {res['g2']}  G3 {res['g3']} (gam {res['gam']})  G4 {res['g4']}", flush=True)
    if res['g1'] and res['g2'] and res['g3'] and res['g4']: chosen = (k, r, res); break
check("rectangle found with G1-G4 all certified", chosen is not None)
if chosen is None: sys.exit(1)
k, r, res = chosen; gam = res['gam']; DG = res['DG']
check("G1 s-mapping: sup|G_s(R)| < r", res['g1'], f"(r = 1e-{k})")
check("G2 u-edges map outward", res['g2'])
check(f"G3 unstable cone, gam = {gam}", res['g3'], f"DG = [[{DG[0][0].str(6)}, {DG[0][1].str(4)}], [{DG[1][0].str(4)}, {DG[1][1].str(8)}]]")
check("G4 inf D_s(B_i) > 0, i = 0..8", res['g4'], f"lower bounds {[round(x, 4) for x in res['Dlow']]}")
check("saddle point xi* lies in R", all(abs(xis[i]) < r for i in range(2)), f"|xi*| <= {float(max(abs(xis[0]).upper(), abs(xis[1]).upper())):.2e}")
ustar_lo, ustar_hi, sabs = xis[1].lower(), xis[1].upper(), abs(xis[0]).upper()
def rat_down(x): return Fr(int((x*10**40).floor().mid().str(60, radius=False).split('.')[0]), 10**40)
def rat_up(x): return Fr(int((x*10**40).ceil().mid().str(60, radius=False).split('.')[0]), 10**40)
U_LO, U_HI, S_HI = rat_down(arb(ustar_lo)), rat_up(arb(ustar_hi)), rat_up(arb(sabs))
check("separator constants are conservative rationals", A(U_LO) <= arb(ustar_lo) and A(U_HI) >= arb(ustar_hi) and A(S_HI) >= arb(sabs), f"|u*|, |s*| <= {float(max(abs(U_LO), abs(U_HI), S_HI)):.2e}")
rec = dict(rid="RECOG-THM-TWIN-P9-STABLE-LOCAL", script_sha256=hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
           input_e3a3a_sha256=h3a, flint=flint.__version__, prec_bits=PREC,
           frame=dict(c=[str(c[0]), str(c[1])], v_s0=[str(vs0[0]), str(vs0[1])], v_u0=[str(vu0[0]), str(vu0[1])], det_P0=str(detP)),
           rectangle_r=f"1e-{k}", gamma=gam, lipschitz_bound=f"1/{gam}",
           DG_R=[[DG[i][j].str(15) for j in range(2)] for i in range(2)], D_s_lower_primitive=res['Dlow'],
           xi_star=[xis[0].str(15), xis[1].str(15)],
           gate_margins=res['margins'],
           separator=dict(h_minus="U_LO - (|s| + S_HI)/gamma", h_plus="U_HI + (|s| + S_HI)/gamma",
                          U_LO=str(U_LO), U_HI=str(U_HI), S_HI=str(S_HI), gamma=gam,
                          convention="u < h_-(s) => negative side; u > h_+(s) => positive side; points of R only"),
           all_checks_pass=ok)
json.dump(rec, open("e3a3b_p9_stable_local.json", "w"), indent=1)
print("E3A-3b CERTIFICATE PASS" if ok else "E3A-3b CERTIFICATE FAIL"); sys.exit(0 if ok else 1)
