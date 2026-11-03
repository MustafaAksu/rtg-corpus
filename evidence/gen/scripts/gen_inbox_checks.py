#!/usr/bin/env python
"""gen_inbox_checks.py — Genesis co-owner (Claude) checks behind the owner disposition of the Genesis inbox round
(records/gen/ATLAS_ADVISORY_GEN_INBOX_20261103.md, items G1, G7, G8).

Status: SESSION evidence, an independent contribution (Methodology v1.4 §12.3). It is not a rerun of any archived
Genesis script: genesis_k4_route_census.py and the G2-CHRONO source are not in the repository ([custody-A]).
Inputs are read from the adopted Genesis file at tag gen-v2.9 (SHA-256 9178ca2c…00ac); the printed 𝒫₄ coefficients
are transcribed below and the transcription is asserted against the tag text (gate T0).

Gates (all exact, sympy):
  T0  the transcribed §6.5 ΔQ_d^(4) display, the §6.6 J_Q display and the §6.5 seed lines occur verbatim in gen-v2.9.
  G1  (G1, chronological protection) with A = DT(0) = [[1,-1],[1,0]] (A^6 = I, A^3 = -I) and L = diag(A,A,A), the
      six-step quadratic term G_2(Z) = Σ_{j=0}^{5} L^{5-j} F_2(L^j Z) vanishes for a *generic* quadratic F_2: R^6 -> R^6
      (126 free coefficients). This is the diag(A,A,A) application of the NUMGEN cyclic-average route.
  G7a (G7, abstract identity) for a six-step map Z -> L^6 Z + G_2 + G_3 + G_4 with L^6 = I and Q_d = d^T B d, the
      degree-4 part of Q_d(d') - Q_d(d) equals 2 d^T B G_{3,d} + Q(G_{2,d}); the degree-3 part equals 2 d^T B G_{2,d}.
      With G_2 = 0: the quartic drift is 2 d^T B G_{3,d}. (Generic symbolic G_k components.)
  G7b (G7, consistency with printed data) from the printed ΔQ_d^(4) = 𝒫₄(s,c,d) and the identity,
      V_d := G_{3,d}(s,c,0) = ½ B^{-1} ∇_d 𝒫₄ |_{d=0}; on the s^3 channel Q(V) = 7/1024 Q_s^3 and on the c^3 channel
      Q(V) = 61/34992 Q_c^3 — both equal to the values Genesis prints independently (§6.5 "Vector apex seeding").
  G8  (G8, birth symmetry) with V = V_d^{[s^3]}: I_ds^(1) = V^T B s = -Q_s^2/16, ω_ds^(1) = -Q_s^2/16 (ω_ab = a2 b1 - a1 b2,
      a^T B J_Q b = (√3/2) ω_ab), and D_birth^{[s^3]} = 2 Q(V) = 7/512 Q_s^3 — the §6.6 values.
  CONV B is fixed by J_Q^T B J_Q = B with unit diagonal; J_Q^2 = -I; a^T B J_Q b = (√3/2) ω_ab holds identically.
Usage: python -I gen_inbox_checks.py GEN_V2_9_FILE     (exit 0 iff all gates PASS)
       python -I gen_inbox_checks.py GEN_V2_9_FILE --control NAME   (a negative control; must exit 1)
"""
import sys
import sympy as sp

R = {}
def gate(k, ok, note=""):
    R[k] = bool(ok); print(f"[{'PASS' if ok else 'FAIL'}] {k} {note}")

CONTROL = sys.argv[sys.argv.index("--control") + 1] if "--control" in sys.argv else None
text = open(sys.argv[1], encoding="utf-8").read()

# ---- T0: transcription anchors (verbatim from gen-v2.9) ----
ANCHORS = [
    r"&-\tfrac{1}{8}Q_sI_{ds} - \tfrac{3}{32}Q_s\omega_{ds} \\",
    r"&-\tfrac{1}{27}Q_cI_{dc} + \tfrac{7}{108}Q_c\omega_{dc} \\",
    r"J_Q = \tfrac{1}{\sqrt{3}}\begin{pmatrix}1 & -2 \\ 2 & -1\end{pmatrix}, \qquad a^\top B J_Q b = \tfrac{\sqrt{3}}{2}\omega_{ab}, \qquad J_Q^2 = -I.",
    r"Leading apex seed: $Q_{d,1}^{[s^3]} = \tfrac{7}{1024}Q_s^3$. Subdominant: $Q_{d,1}^{[c^3]} = \tfrac{61}{34992}Q_c^3$",
    r"$I_{ds}^{(1)} = \omega_{ds}^{(1)} = -Q_s^2/16$",
    r"$D_{\rm birth}^{[s^3]}=\tfrac{7}{512}Q_s^3=2Q(V_s)$",
    r"\(\omega_{ab}=a_2b_1-a_1b_2\)",
]
gate("T0", all(text.count(a) >= 1 for a in ANCHORS), "transcription anchors present in the given Genesis file")

# ---- conventions ----
b = sp.Symbol("b", real=True)
JQ = sp.Matrix([[1, -2], [2, -1]]) / sp.sqrt(3)
Bg = sp.Matrix([[1, b], [b, 1]])
sol = sp.solve(list(JQ.T * Bg * JQ - Bg), b, dict=True)
B = Bg.subs(sol[0]) if len(sol) == 1 else None
a1, a2, b1, b2 = sp.symbols("a1 a2 b1 b2", real=True)
av, bv = sp.Matrix([a1, a2]), sp.Matrix([b1, b2])
om = lambda x, y: x[1]*y[0] - x[0]*y[1]
conv_ok = (B is not None and sp.simplify(JQ*JQ + sp.eye(2)) == sp.zeros(2)
           and sp.simplify((av.T*B*JQ*bv)[0] - sp.sqrt(3)/2*om(av, bv)) == 0)
gate("CONV", conv_ok, f"B offdiag={sol[0][b] if sol else None}; J_Q^2=-I; a^T B J_Q b = (√3/2)ω_ab")

# ---- G1: six-step quadratic cancellation for generic F2 on R^6 ----
A = sp.Matrix([[1, -1], [1, 0]])
L = sp.diag(A, A, A)
if CONTROL == "G1-wrong-L":           # A with eigenvalues e^{±iπ/2}: six-step quadratic need not cancel
    A2 = sp.Matrix([[0, -1], [1, 0]]); L = sp.diag(A2, A2, A2)
z = sp.symbols("z0:6", real=True)
Z = sp.Matrix(z)
mons = [z[i]*z[j] for i in range(6) for j in range(i, 6)]
coef = sp.symbols(f"k0:{6*len(mons)}")
F2 = lambda X: sp.Matrix([sum(coef[r*len(mons)+m] * mons[m].subs(dict(zip(z, X)), simultaneous=True)
                              for m in range(len(mons))) for r in range(6)])
Lp = [L**j for j in range(7)]
G2 = sp.zeros(6, 1)
for j in range(6):
    G2 += Lp[5-j] * F2(list(Lp[j] * Z))
G2 = G2.applyfunc(sp.expand)
gate("G1", (L**6 == sp.eye(6) or CONTROL == "G1-wrong-L") and G2 == sp.zeros(6, 1),
     f"Σ_j L^(5-j) F2(L^j Z) = 0 for generic quadratic F2 ({len(coef)} coefficients); A^6=I: {A**6 == sp.eye(2)}")

# ---- G7a: abstract identity ----
d1, d2, t = sp.symbols("d1 d2 t", real=True)
dv = sp.Matrix([d1, d2])
g2 = sp.Matrix(sp.symbols("p1 p2")); g3 = sp.Matrix(sp.symbols("q1 q2")); g4 = sp.Matrix(sp.symbols("r1 r2"))
# grade by a scaling parameter t: d ~ t, G_k ~ t^k
dp = t*dv + t**2*g2 + t**3*g3 + t**4*g4                    # L^6 = I
Bn = B if B is not None else sp.eye(2)
diff = sp.expand((dp.T*Bn*dp)[0] - (t**2)*(dv.T*Bn*dv)[0])
c3 = diff.coeff(t, 3); c4 = diff.coeff(t, 4)
ok7a = (sp.simplify(c3 - 2*(dv.T*Bn*g2)[0]) == 0
        and sp.simplify(c4 - (2*(dv.T*Bn*g3)[0] + (g2.T*Bn*g2)[0])) == 0
        and sp.simplify(c4.subs({g2[0]: 0, g2[1]: 0}) - 2*(dv.T*Bn*g3)[0]) == 0)
gate("G7a", ok7a, "cubic part 2d^T B G2,d; quartic part 2d^T B G3,d + Q(G2,d); with G2=0 quartic = 2d^T B G3,d")

# ---- G7b, G8: printed 𝒫₄ -> seeds and birth symmetry ----
s1, s2, c1, c2 = sp.symbols("s1 s2 c1 c2", real=True)
sv, cv = sp.Matrix([s1, s2]), sp.Matrix([c1, c2])
Q = lambda x: sp.expand((x.T*Bn*x)[0])
I_ = lambda x, y: sp.expand((x.T*Bn*y)[0])
w_ = lambda x, y: sp.expand(om(x, y))
Qs, Qc, Qd = Q(sv), Q(cv), Q(dv)
Ids, Idc, Isc = I_(dv, sv), I_(dv, cv), I_(sv, cv)
wds, wdc, wsc = w_(dv, sv), w_(dv, cv), w_(sv, cv)
F = sp.Rational
k_ds = F(-3, 32) if CONTROL != "G7-wrong-coefficient" else F(-3, 16)
P4 = (-Qd**2
      - F(1, 8)*Qs*Ids + k_ds*Qs*wds
      - F(1, 27)*Qc*Idc + F(7, 108)*Qc*wdc
      - F(5, 12)*wds*Ids - F(1, 8)*wds**2
      - F(5, 9)*wdc*Idc - F(1, 6)*wdc**2
      + F(1, 36)*Qs*Idc - F(7, 48)*Qs*wdc + F(1, 18)*Ids*Isc + F(7, 72)*Ids*wsc
      + F(1, 6)*Qc*Ids + F(3, 8)*Qc*wds + F(1, 3)*Idc*Isc + F(1, 4)*Idc*wsc)
grad = sp.Matrix([sp.diff(P4, d1), sp.diff(P4, d2)]).subs({d1: 0, d2: 0})
V = (Bn.inv() * grad / 2).applyfunc(sp.expand)
Vs = V.subs({c1: 0, c2: 0}); Vc = V.subs({s1: 0, s2: 0})
ok7b = (sp.simplify(Q(Vs) - F(7, 1024)*Qs**3) == 0 and sp.simplify(Q(Vc) - F(61, 34992)*Qc**3) == 0)
gate("G7b", ok7b, "½B⁻¹∇_d𝒫₄|_{d=0}: Q(V^[s³]) = 7/1024 Q_s³, Q(V^[c³]) = 61/34992 Q_c³ (printed seeds)")
I1 = sp.expand((Vs.T*Bn*sv)[0]); w1 = sp.expand(om(Vs, sv))
ok8 = (sp.simplify(I1 + Qs**2/16) == 0 and sp.simplify(w1 + Qs**2/16) == 0
       and sp.simplify(2*Q(Vs) - F(7, 512)*Qs**3) == 0)
gate("G8", ok8, "I_ds^(1) = ω_ds^(1) = -Q_s²/16; D_birth^[s³] = 2Q(V_s) = 7/512 Q_s³")

ok = all(R.values())
print(f"\n{sum(R.values())}/{len(R)} gates PASS" + (f" (control {CONTROL})" if CONTROL else ""))
sys.exit(0 if ok else 1)
