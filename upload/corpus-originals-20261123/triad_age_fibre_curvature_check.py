#!/usr/bin/env python3
"""
Age-fibre curvature at degree 13: symbolic all-direction derivation from the pinned G3/G4 jet,
cross-checked against untruncated full-map ray series.

Setting (Genesis->RER conditional analytic modal model, birth contract A, matched current parent s):
   c_n(s) = C(s) + n D5 + n D6 + n D7 + binom(n,2) B7 + binom(n,2) B8 + ... ,  kappa = sqrt3*kt.
Chords d_j(s) = c_j(s) - c_0(s).  Collinearity of the three age states (0,1,2) in the child plane is
measured by  w(s) = det[d_1(s), d_2(s)].  Since d_2 - 2 d_1 = B7 + B8 + ..., and B7 || D5,

   w(s) = D5 ^ B8 + D6 ^ B7 + O(||s||^14)          (degree 13, all directions)

with, from the one-step propagation of a current-parent child perturbation (degree 8 only needs G3,G4):
   D5 = [G3_c(s,C)]_5 - DC g3 ,            D6 = [G4_c(s,C)]_6 - DC g4
   B7 = A3 D5 - DD5 g3 ,                   B8 = A3 D6 + A4 D5 - DD6 g3 - DD5 g4
   A_k = D_c G_{k,c}(s,0),  g_k = G_{k,s}(s,0).

The symbolic part needs SymPy and the pinned jet (SHA-256 15a7d056...2824).  The ray cross-check uses the
contributor's standard-library full-map series code (rev2, SHA-256 67b2e0e7...799b) placed in ../source/.
Usage:  python triad_age_fibre_curvature_check.py [--negative]
"""
import sys, json, hashlib
from pathlib import Path
from fractions import Fraction as Fr
import sympy as S

HERE = Path(__file__).resolve().parent
JET = HERE.parent / 'source' / 'jet_coefficients.json'
SERIES = HERE.parent / 'source' / 'c09_independent_series_check_rev2.py'
assert hashlib.sha256(JET.read_bytes()).hexdigest() == '15a7d0569a1e8ceefe04260ce83e204acb2eeed20b2639eebd810e14ee992824'
assert hashlib.sha256(SERIES.read_bytes()).hexdigest() == '67b2e0e785dd30a1bd637c79db2a7210d93516b79f5a00d5fb8233da04f6799b'
NEG = '--negative' in sys.argv

r, e, cr, ce, kt = S.symbols('r e cr ce kt', real=True)
V4 = [r, e, cr, ce]
def poly(d):
    out = 0
    for ex, co in d.items():
        term = S.Rational(co)
        for x, j in zip(V4, map(int, ex.split(','))):
            term *= x**j
        out += term
    return S.expand(out)
src = json.loads(JET.read_text())
G3 = S.Matrix([poly(d) for d in src['G3']]); G4 = S.Matrix([poly(d) for d in src['G4']])
Q = r*r - r*e + e*e
sv = S.Matrix([r, e]); cv = S.Matrix([cr, ce])
C = kt * Q * S.Matrix([[1, -2], [2, -1]]) * sv
at0 = {cr: 0, ce: 0}
def hom(expr, deg):   # homogeneous part of given total degree in (r,e)
    return S.Matrix([sum(t for t in S.Add.make_args(S.expand(x)) if S.Poly(t, r, e).total_degree() == deg) for x in expr])
g3 = G3[0:2, :].subs(at0); g4 = G4[0:2, :].subs(at0)
A3 = G3[2:4, :].jacobian([cr, ce]).subs(at0); A4 = G4[2:4, :].jacobian([cr, ce]).subs(at0)
subC = {cr: C[0], ce: C[1]}
D5 = hom(G3[2:4, :].subs(subC) - C.jacobian([r, e]) * g3, 5)
D6 = hom(G4[2:4, :].subs(subC) - C.jacobian([r, e]) * g4, 6)
B7 = S.expand(A3 * D5 - D5.jacobian([r, e]) * g3)
B8 = S.expand(A3 * D6 + A4 * D5 - D6.jacobian([r, e]) * g3 - D5.jacobian([r, e]) * g4)
if NEG: B8 = B8 * S.Rational(9, 10)   # negative control: a wrong B8 must be caught by the ray cross-check
wedge = lambda a, b: S.expand(a[0]*b[1] - a[1]*b[0])
W13 = wedge(D5, B8) + wedge(D6, B7)

checks = []
def chk(name, ok, detail=''):
    checks.append(ok); print(('PASS ' if ok else 'FAIL '), name, detail)

chk('D5 = -(kt/2) Q^2 s', S.expand(D5 + kt/2*Q**2*sv) == S.zeros(2, 1))
chk('B7 = (kt/4) Q^3 s', S.expand(B7 - kt/4*Q**3*sv) == S.zeros(2, 1))
chk('degrees: D6=6, B8=8, W13=13', all(S.Poly(x, r, e).total_degree() == d for x, d in [(D6[0], 6), (B8[0], 8), (W13, 13)]))
chk('W13 is kt^2 times a kt-free polynomial', S.Poly(W13, kt).degree() == 2 and S.Poly(W13, kt).coeff_monomial(kt) == 0 and S.Poly(W13, kt).coeff_monomial(1) == 0)
P13 = S.factor(S.expand(W13 / kt**2))
print('   W13/kt^2 =', P13)
# parallel/transverse split of the degree-8 residual after the degree-7 tau reparametrisation
R8 = S.expand(B8 + Q/2*D6)               # leftover n^2 term at degree 8 once tau = n - (Q/4) n(n-1) absorbs B7
chk('D5 ^ R8 == W13 (the wedge is exactly the transverse part of the reparametrised degree-8 n^2 term)', S.expand(wedge(D5, R8) - W13) == 0)
# the transverse defect is not a multiple of Q^k: it vanishes on real directions
cubic = S.cancel(S.expand(W13 / kt**2) / (-Q**5 / 1024))
chk('W13 = -(kt^2/1024) Q^5 * K3(r,e) with K3 a cubic form', S.Poly(cubic, r, e).total_degree() == 3 and S.expand(W13 + kt**2*Q**5*cubic/1024) == 0)
print('   K3(r,e) =', S.expand(cubic))
x = S.Symbol('x', real=True)
roots = [float(S.re(z)) for z in S.Poly(S.expand(cubic.subs({r: 1, e: x})), x).nroots() if abs(S.im(z)) < 1e-12]
print('   real zero directions e/r of K3 (hence of W13):', roots)
chk('K3 has exactly one real zero direction, so W13 changes sign across directions', len(roots) == 1)

# ---- cross-check against the untruncated full-map series on rays (standard-library code, no jet) --------
scope = {'__name__': '__probe__'}
exec(SERIES.read_text().split('# ---------------------------------------------------------------- checks')[0], scope)
scope['NT'] = 15
exec('''
def probe(ktv,u):
  tgt=ray(u); c=[]
  for n in (0,1,2):
    s0=initial_for_current_parent(tgt,n,ktv); c.append(Fn(birth(s0,ktv),n)[1])
  d1=[sub(c[1][i],c[0][i]) for i in range(2)]; d2=[sub(c[2][i],c[0][i]) for i in range(2)]
  w=sub(mul(d1[0],d2[1]),mul(d1[1],d2[0]))
  B8=[d2[i][8]-2*d1[i][8] for i in range(2)]; D6=[d1[i][6] for i in range(2)]
  return order(w), w[13], B8, D6
''', scope)
for ktv, u in [(Fr(1), (1, 0)), (Fr(-2, 3), (1, 0)), (Fr(1), (1, 1)), (Fr(1), (0, 1)), (Fr(1), (2, -1)), (Fr(3, 5), (1, 3))]:
    ow, w13, B8ray, D6ray = scope['probe'](ktv, u)
    sub_ = {r: u[0], e: u[1], kt: S.Rational(ktv.numerator, ktv.denominator)}
    okw = ow == 13 and S.Rational(w13.numerator, w13.denominator) == W13.subs(sub_)
    okB = all(S.Rational(x.numerator, x.denominator) == B8.subs(sub_)[i] for i, x in enumerate(B8ray))
    okD = all(S.Rational(x.numerator, x.denominator) == D6.subs(sub_)[i] for i, x in enumerate(D6ray))
    chk(f'ray kt={ktv} u={u}: wedge order 13, W13, B8 and D6 all match full-map series', okw and okB and okD, f'(w13={w13})')

print(f'\n{sum(checks)} PASS, {len(checks)-sum(checks)} FAIL')
sys.exit(0 if all(checks) else 1)
