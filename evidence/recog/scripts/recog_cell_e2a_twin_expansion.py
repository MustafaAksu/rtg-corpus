#!/usr/bin/env python3
r"""
recog_cell_e2a_twin_expansion.py — RECOG OPEN R7 / CELL-E2A: certified raw-frame six-step expansion of the symmetric twin.
(rep:) raw P1 eigenframe W = rho + omega eta (omega = e^{2 pi i/3}), Q = |W|^2 = rho^2 - rho eta + eta^2 (no normalizer).
(transport:) T_s(rho,eta) = (rho - sin eta, eta + sinh rho - sin eta);  F = T_s^6 written in W.
Claim (RECOG-ALG-TWIN-EXPANSION; corollary E2B = fundamental annulus A = {7/200 <= Q < 58107/1600000}). On 0 < Q <= r^2 (radius row r below):  Q + c_- Q^2 <= Q(F(W)) <= Q + c_+ Q^2,  c_- > 0,
for every phase. Proof:
 (i) exact oddness: T_s(-x) = -T_s(x) => F odd => all even-degree Taylor terms of F vanish identically;
 (ii) leading-return equivariance (RECOG-ALG-LEADING-RETURN-EQUIVARIANCE) confines the cubic term to mu_s |W|^2 W; the Arb jet
      confirms mu_s = 1/2 - i sqrt3/6 and |other cubic channels| < 1e-40 (balls), and degrees 2, 4 vanish (balls, consistency only);
 (iii) F = W + mu_s|W|^2 W + H, |H(W)| <= h(|W|) |W|^5, h(t) = b5 + b7 t^2 + b9 t^4 + K11(r) t^6, with b_d = Arb upper bounds of the
      degree-d coefficient-modulus sums of the exact jet and K11 from the coefficient majorant S6 = Psi_s^{o6},
      Psi_s(t) = t + 2(sinh(a t) - a t), a = 7/6 > 2/sqrt3 (row coefficient sums of rho, eta in (W, Wbar));
 (iv) |F|^2 = Q + 2 Re(mu_s) Q^2 + |mu_s|^2 Q^3 + E,  |E| <= Q^3 [2h + 2|mu_s| r^2 h + r^4 h^2],  2 Re mu_s = 1, |mu_s|^2 = 1/3;
      hence c_- = 1 - max(0, e - 1/3) r^2 and c_+ = 1 + (1/3 + e) r^2 with e = sup of the bracket on the row.
"""
import sys, math, hashlib
from fractions import Fraction as F
import flint
from flint import arb, acb
flint.ctx.prec = 200
ok = True
def check(name, cond, info=""):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name} {info}", flush=True); ok = ok and bool(cond)
N = 9
def mul(A, B):
    C = {}
    for (i, j), a in A.items():
        for (k, l), b in B.items():
            if i+j+k+l <= N: C[(i+k, j+l)] = C.get((i+k, j+l), acb(0)) + a*b
    return C
def add(A, B, s=1):
    C = dict(A)
    for k, v in B.items(): C[k] = C.get(k, acb(0)) + s*v
    return C
def scal(A, s): return {k: v*s for k, v in A.items()}
def powr(A, n):
    R = {(0, 0): acb(1)}
    for _ in range(n): R = mul(R, A)
    return R
def compose(Fs, G):
    P0 = [{(0, 0): acb(1)}]; P1 = [{(0, 0): acb(1)}]
    for _ in range(N): P0.append(mul(P0[-1], G[0])); P1.append(mul(P1[-1], G[1]))
    out = []
    for f in Fs:
        R = {}
        for (i, j), c in f.items(): R = add(R, scal(mul(P0[i], P1[j]), c))
        out.append(R)
    return out
s3 = arb(3).sqrt(); om = acb(arb(-1)/2, s3/2); omb = om.conjugate()
Z = {(1, 0): acb(1)}; Zb = {(0, 1): acb(1)}
eta = scal(add(Z, Zb, -1), 1/(om - omb)); rho = add(Z, scal(eta, -om))
def odd_series(x, sgn):          # sin (sgn=-1) or sinh (sgn=+1) to degree N
    r, k = {}, 0
    while 2*k+1 <= N:
        n = 2*k+1; r = add(r, scal(powr(x, n), acb(arb(sgn**k)/math.factorial(n)))); k += 1
    return r
rho1 = add(rho, odd_series(eta, -1), -1)
eta1 = add(add(eta, odd_series(rho, +1)), odd_series(eta, -1), -1)
f = [add(rho1, scal(eta1, om)), add(rho1, scal(eta1, omb))]
G = f
for _ in range(5): G = compose(f, G)
FW = G[0]
def modsum(d): return sum((abs(v) for k, v in FW.items() if sum(k) == d), arb(0))
tiny = arb('1e-40')
check("linear part is W (six-step)", abs(FW.get((1, 0), acb(0)) - 1) < tiny and abs(FW.get((0, 1), acb(0))) < tiny)
check("degrees 2 and 4 vanish (balls; consistency with exact oddness)", all(abs(v) < tiny for k, v in FW.items() if sum(k) in (2, 4)))
mu = FW.get((2, 1), acb(0)); mu_exact = acb(arb(1)/2, -s3/6)
check("cubic = mu_s |W|^2 W, mu_s = 1/2 - i sqrt3/6; other cubic channels vanish", abs(mu - mu_exact) < tiny and
      all(abs(v) < tiny for k, v in FW.items() if sum(k) == 3 and k != (2, 1)))
b5, b7, b9 = modsum(5).upper(), modsum(7).upper(), modsum(9).upper()
print(f"    coefficient-modulus sums: b5 <= {float(b5):.6f}, b7 <= {float(b7):.6f}, b9 <= {float(b9):.6f}")
# majorant
a = F(7, 6); check("a = 7/6 > 2/sqrt3", a*a > F(4, 3))
NM = 10
def series_Psi_compose(S):                               # Psi_s(S(t)) as exact rational series to degree NM
    out = [F(0)]*(NM+1)
    for i, c in enumerate(S): out[i] += c
    Pw = [F(1)] + [F(0)]*NM
    for n in range(1, NM+1):
        Q_ = [F(0)]*(NM+1)
        for i, x in enumerate(Pw):
            if x:
                for j, y in enumerate(S):
                    if y and i+j <= NM: Q_[i+j] += x*y
        Pw = Q_
        if n >= 3 and n % 2 == 1:
            coef = 2*a**n/math.factorial(n)                  # 2 (sinh(a t) - a t)
            for k in range(NM+1): out[k] += coef*Pw[k]
    return out
S = [F(0), F(1)] + [F(0)]*(NM-1)
for _ in range(6): S = series_Psi_compose(S)
def Psi(t): at = arb(a.numerator)/a.denominator*t; return t + 2*(at.sinh() - at)
def S6(r):
    t = r
    for _ in range(6): t = Psi(t)
    return t
def qa(fr): return arb(fr.numerator)/fr.denominator
check("majorant consistency (Arb vs exact rationals): s5 >= b5, s7 >= b7, s9 >= b9", arb(b5) <= qa(S[5]) and arb(b7) <= qa(S[7]) and arb(b9) <= qa(S[9]),
      f"s5,s7,s9 = {float(S[5]):.4f}, {float(S[7]):.4f}, {float(S[9]):.3f}")
mu2 = arb(1)/3; mum = abs(mu_exact).upper()
rows = []
for rn, rd in [(1, 20), (1, 10), (3, 20), (1, 5)]:
    r = arb(rn)/rd
    K11 = ((S6(r) - sum((arb(S[n].numerator)/S[n].denominator*r**n for n in range(NM+1)), arb(0)))/r**11).upper()
    h = arb(b5) + arb(b7)*r**2 + arb(b9)*r**4 + arb(K11)*r**6
    e = (2*h + 2*mum*r**2*h + r**4*h*h).upper()
    cm = 1 - max(arb(0), arb(e) - mu2)*r**2; cp = 1 + (mu2 + arb(e))*r**2
    good = cm > 0
    rows.append((f"{rn}/{rd}", float(K11), float(e), float(cm.lower()), float(cp.upper()), good))
    if (rn, rd) == (1, 5): CM15, CP15 = cm, cp
    check(f"row r = {rn}/{rd} (q_out = {float((r*r).mid()):.4f}): c_- > 0", good,
          f"K11 <= {float(K11):.3e}, e <= {float(e):.4f}, c_- >= {float(cm.lower()):.5f}, c_+ <= {float(cp.upper()):.5f}")
# exact corollaries of the r = 1/5 row (E2B)
check("E2A exact corollary (r = 1/5): c_- > 19/20 and c_+ < 43/40", CM15 > arb(19)/20 and CP15 < arb(43)/40)
q1 = F(7, 200); q2 = q1 + F(43, 40)*q1*q1
check("E2B annulus: q1 = 7/200, q2 = q1 + (43/40) q1^2 = 58107/1600000 < 1/25", q2 == F(58107, 1600000) and q2 < F(1, 25))
print("    E2B (exact one-line corollary): 0 < Q0 < q1 => Q_{m+1} >= Q_m + (19/20) Q_m^2 > Q_m on Q <= 1/25, so the six-step sequence")
print("    crosses q1; at the first crossing Q_{m*} < q1 + (43/40) q1^2 = q2. Hence every orbit with 0 < Q0 < q1 has a six-step iterate in")
print("    A = {7/200 <= Q < 58107/1600000}; orbits with Q0 in A start there.")
print(f"    script sha256 {hashlib.sha256(open(__file__,'rb').read()).hexdigest()}; flint {flint.__version__}")
print("E2A CERTIFICATE PASS" if ok else "E2A CERTIFICATE FAIL (see rows)"); sys.exit(0 if ok else 1)
