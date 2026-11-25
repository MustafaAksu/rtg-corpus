#!/usr/bin/env python
"""k3_obstruction_exact_check.py — Genesis-side independent exact check of
K3-CUBIC-FACTOR-OBSTRUCTION. Derives the six-step cubic f_3 of the projected
K3 map F_1 = P_C T^{x3} directly from the primitive (no imported jet), then
checks the ER-2B model, the chiral identity, and the l(f_3)=c l|l|^2 obstruction.
Exact arithmetic in Q(i*sqrt3); no sympy. Run: python k3_obstruction_exact_check.py
"""
import sys
from fractions import Fraction as Fr
from math import factorial
D = 3  # truncation degree

class K:
    __slots__ = ("p", "q")
    def __init__(s, p=0, q=0): s.p, s.q = Fr(p), Fr(q)
    def __add__(a, b): b = k(b); return K(a.p + b.p, a.q + b.q)
    __radd__ = __add__
    def __neg__(a): return K(-a.p, -a.q)
    def __sub__(a, b): return a + (-k(b))
    def __mul__(a, b): b = k(b); return K(a.p*b.p - 3*a.q*b.q, a.p*b.q + a.q*b.p)
    __rmul__ = __mul__
    def conj(a): return K(a.p, -a.q)
    def inv(a): n = a.p*a.p + 3*a.q*a.q; return K(a.p/n, -a.q/n)
    def __truediv__(a, b): return a * k(b).inv()
    def iszero(a): return a.p == 0 and a.q == 0
    def __eq__(a, b): b = k(b); return a.p == b.p and a.q == b.q
    def __repr__(a): return f"{a.p}" if a.q == 0 else f"({a.p}{'+' if a.q>=0 else '-'}{abs(a.q)}i√3)"
def k(x): return x if isinstance(x, K) else K(x)
S3 = K(0, 1); LAM = K(Fr(1, 2), Fr(1, 2))   # i*sqrt3, e^{i pi/3}
# NB: i alone is not in Q(i√3); every coefficient used below is, by construction.

# polynomials in (w1, W1, w2, W2): dict {(a1,b1,a2,b2): K}; W = conj(w)
def clean(P): return {m: c for m, c in P.items() if not c.iszero() and sum(m) <= D}
def add(*Ps):
    R = {}
    for P in Ps:
        for m, c in P.items(): R[m] = R.get(m, K()) + c
    return clean(R)
def scal(c, P): return clean({m: k(c)*v for m, v in P.items()})
def mul(P, Q):
    R = {}
    for m, c in P.items():
        for n, d in Q.items():
            if sum(m) + sum(n) <= D:
                t = tuple(x + y for x, y in zip(m, n)); R[t] = R.get(t, K()) + c*d
    return clean(R)
def conjP(P): return {(b1, a1, b2, a2): c.conj() for (a1, b1, a2, b2), c in P.items()}
def deg(P, d): return {m: c for m, c in P.items() if sum(m) == d}
def eq(P, Q): return not add(P, scal(-1, Q))
one = {(0, 0, 0, 0): K(1)}
w1, W1, w2, W2 = {(1,0,0,0): K(1)}, {(0,1,0,0): K(1)}, {(0,0,1,0): K(1)}, {(0,0,0,1): K(1)}

# primitive edge map in W chart, as a 1-variable polynomial {(a,b): K} in (z, zbar)
def p1add(*Ps):
    R = {}
    for P in Ps:
        for m, c in P.items(): R[m] = R.get(m, K()) + c
    return {m: c for m, c in R.items() if not c.iszero() and sum(m) <= D}
def p1mul(P, Q):
    R = {}
    for (a, b), c in P.items():
        for (e, f), d in Q.items():
            if a+b+e+f <= D: R[(a+e, b+f)] = R.get((a+e, b+f), K()) + c*d
    return {m: c for m, c in R.items() if not c.iszero()}
p1s = lambda c, P: {m: k(c)*v for m, v in P.items() if not (k(c)*v).iszero()}
Z, ZB = {(1, 0): K(1)}, {(0, 1): K(1)}
rho = p1add(p1s(Fr(1, 2), p1add(Z, ZB)), p1s(K(0, Fr(-1, 6)), p1add(Z, p1s(-1, ZB))))
eta = p1s(K(0, Fr(-1, 3)), p1add(Z, p1s(-1, ZB)))
def ser(x, cf):
    R, p = {}, {(0, 0): K(1)}
    for n in range(D + 1):
        if cf(n): R = p1add(R, p1s(cf(n), p))
        p = p1mul(p, x)
    return R
sn = ser(eta, lambda n: Fr((-1)**((n-1)//2), factorial(n)) if n % 2 else 0)
em = ser(rho, lambda n: Fr(1, factorial(n)) if n else 0)
r1, e1 = p1add(rho, p1s(-1, sn)), p1add(eta, em, p1s(-1, sn))
TW = p1add(r1, p1s(Fr(-1, 2), e1), p1s(S3*Fr(1, 2), e1))

def apply_T(g):  # T_W(g, conj g)
    gb = conjP(g); pw, pwb = [one], [one]
    for _ in range(D): pw.append(mul(pw[-1], g)); pwb.append(mul(pwb[-1], gb))
    R = {}
    for (a, b), c in TW.items(): R = add(R, scal(c, mul(pw[a], pwb[b])))
    return R

def step(e):  # e = [g1, g2, g3] edge polynomials; T each edge, subtract mean
    t = [apply_T(g) for g in e]; m = scal(Fr(1, 3), add(*t))
    return [add(x, scal(-1, m)) for x in t]
edges = [w1, w2, add(scal(-1, w1), scal(-1, w2))]
for _ in range(6): edges = step(edges)

results = []
def check(name, ok): results.append(bool(ok)); print(("PASS  " if ok else "FAIL  ") + name)
check("six-step return is tangent to identity", eq(deg(edges[0], 1), w1) and eq(deg(edges[1], 1), w2))
check("six-step return has no quadratic term (all edges)", all(not deg(e, 2) for e in edges))
f3 = [deg(e, 3) for e in edges]
check("closure: sum_e f3_e = 0", not add(*f3))

# ER-2B model: f_e = nu (w_e|w_e|^2 - mean) + (2i chi/3)(w_{e+1}-w_{e-1}) S, S = Im(w1 conj w2)
# write (2i/3)*S = (1/3)(w1 W2 - W1 w2)  [since 2iS = w1W2 - W1w2] -> chi*(1/3)(...)(w_{e+1}-w_{e-1})
nu, chi = K(Fr(1, 6), Fr(-1, 3)), Fr(1, 3)
if '--negative-control' in sys.argv: chi = Fr(1, 4)   # must FAIL the model check
wl = [w1, w2, add(scal(-1, w1), scal(-1, w2))]; Wl = [conjP(x) for x in wl]
cub = [mul(mul(wl[e], wl[e]), Wl[e]) for e in range(3)]; mean = scal(Fr(1, 3), add(*cub))
twoiS = add(mul(w1, W2), scal(-1, mul(W1, w2)))   # 2i*S
model = [add(scal(nu, add(cub[e], scal(-1, mean))),
             scal(chi*Fr(1, 3), mul(add(wl[(e+1) % 3], scal(-1, wl[(e-1) % 3])), twoiS))) for e in range(3)]
check("f3 from primitive == ER-2B model (nu=1/6-i√3/3, chi=1/3), every edge", all(eq(f3[e], model[e]) for e in range(3)))

# chiral modes u = w1 + lam w2, v = w1 + lamb w2 ; N = sum|w_e|^2 = |u|^2+|v|^2
lamb = LAM.conj()
u = add(w1, scal(LAM, w2)); v = add(w1, scal(lamb, w2)); U, V = conjP(u), conjP(v)
Nn = add(*[mul(wl[e], Wl[e]) for e in range(3)])
check("N = |u|^2 + |v|^2", eq(Nn, add(mul(u, U), mul(v, V))))
c0 = K(Fr(1, 6), Fr(1, 9))          # 1/6 + i√3/9
ib = K(0, Fr(2, 9))                  # i*beta, beta = 2√3/9:  i*(2√3/9) = (2/9)*(i√3)
for name, mode, coef in (("u", u, (K(1), LAM)), ("v", v, (K(1), lamb))):
    lf = add(scal(coef[0], f3[0]), scal(coef[1], f3[1]))
    M = conjP(mode)
    rhs = add(scal(c0, mul(mul(mode, mode), M)), scal(-1, scal(ib, mul(Nn, mode))))
    check(f"chiral identity {name}(f3) = c0 {name}|{name}|^2 - i(2√3/9) N {name}", eq(lf, rhs))

# obstruction: l = alpha u + beta v. LHS = c0(alpha u|u|^2 + beta v|v|^2) - iβ*(|u|^2+|v|^2)(alpha u + beta v)
# RHS = C (alpha u + beta v)^2 conj(alpha u + beta v). Coefficient of u|v|^2 on LHS is -iβ*·alpha;
# on RHS it is 2C alpha|beta|^2; coefficient of u^2 vbar: LHS 0, RHS C alpha^2 conj(beta).
# => C alpha^2 conj(beta)=0 ; C beta^2 conj(alpha)=0.  If C=0: -iβ* alpha = 0 => alpha=0, same for beta.
#    If C!=0: alpha*beta=0; WLOG beta=0, alpha!=0: u|v|^2 coefficient: -iβ* alpha = 0 => contradiction.
check("beta* = 2√3/9 != 0 (phase coupling nonzero)", not ib.iszero())
n = sum(results)
print(f"ALL PASS ({n}/{len(results)})  -> only l = 0; no C^3 rank-2 planar factor" if n == len(results) else f"FAILURES ({n}/{len(results)})")
sys.exit(0 if n == len(results) else 1)
