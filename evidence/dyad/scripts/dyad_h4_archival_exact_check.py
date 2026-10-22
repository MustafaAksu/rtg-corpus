"""Exact (sympy) recomputation of the archival h4 of normalize_p6_liegauge_exact.py.
Same frame and map as the script; F^6 truncated at total degree 4; h4 = degree-4 part
of F^6 (all degree-4 channels are non-resonant for p=6, so h4 = V4)."""
import sympy as sp
Z, Zb = sp.symbols('Z Zb'); s3 = sp.sqrt(3); I = sp.I; D = 4
EP2 = -sp.Rational(1,2) + s3/2*I; EM = s3/2 - I/2; EP = s3/2 + I/2
def trunc(e):
    p = sp.Poly(sp.expand(e), Z, Zb)
    return sum(sp.expand(c)*Z**a*Zb**b for (a,b), c in p.terms() if a+b <= D)
def conj(e):  # conjugate coefficients and swap Z <-> Zb
    p = sp.Poly(sp.expand(e), Z, Zb)
    return sum(sp.expand(sp.conjugate(c))*Zb**a*Z**b for (a,b), c in p.terms())
rho = EM/s3*Z + EP/s3*Zb; eta = -I/s3*Z + I/s3*Zb
def sin_(x): return x - x**3/6
def expm1(x): return x + x**2/2 + x**3/6 + x**4/24
EM2 = -sp.Rational(1,2) - s3/2*I
step1 = trunc(Z + EM2*sin_(eta) + EP2*expm1(rho))
F = step1
for _ in range(5):
    Fc = conj(F)
    F = trunc(step1.subs({Z: sp.Symbol('A'), Zb: sp.Symbol('B')}).subs({sp.Symbol('A'): F, sp.Symbol('B'): Fc}, simultaneous=True))
P = sp.Poly(F, Z, Zb)
h4 = {m: sp.nsimplify(sp.radsimp(sp.expand(P.coeff_monomial(Z**m[0]*Zb**m[1])))) for m in [(4,0),(3,1),(2,2),(1,3),(0,4)]}
claimed = {(1,3): sp.Rational(1,3)+s3/9*I, (2,2): -sp.Rational(5,24)-11*s3/24*I,
           (3,1): -sp.Rational(1,6)-2*s3/9*I, (4,0): -sp.Rational(1,16)+7*s3/144*I, (0,4): 0}
ok = True
for m in sorted(h4):
    d = sp.simplify(h4[m] - claimed[m]); ok &= (d == 0)
    print(m, h4[m], 'exact match' if d == 0 else f'DIFF {d}')
print('linear part check:', sp.expand(P.coeff_monomial(Z)), sp.expand(P.coeff_monomial(Zb)))
print('RESULT', 'PASS' if ok else 'FAIL')
raise SystemExit(0 if ok else 1)
