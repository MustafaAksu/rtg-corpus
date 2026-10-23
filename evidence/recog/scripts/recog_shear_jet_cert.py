#!/usr/bin/env python3
"""
recog_shear_jet_cert.py — RECOG CELL-0 certificate (RTG_RELATIONAL_RECOGNITION_DSN_v0.2.1, §8)

Verifies, by exact symbolic six-step cubic composition in the canonical p=6
eigenframe W = rho + omega*eta (omega = exp(2*pi*i/3)):

  (1) original dyad T        : mu_6 = -1/2 - i*2*sqrt(3)/3   (must reproduce DYAD-THM-C21)
  (2) swap-projection twin T_s: mu_6 = +1/2 - i*sqrt(3)/6
  (3) log twin T_log         : mu_6 = -i*sqrt(3)/3
  (4) shear-jet law          : mu_6(a,b) = 3b - 4a^2 - i*sqrt(3)*(1/3 + 2a^2 - b)
      for g(rho) = rho + a*rho^2 + b*rho^3, radial row rho' = rho - sin(eta)
  (5) tanh twin (a=0,b=-1/3) : mu_6 = -1 - i*2*sqrt(3)/3
  (6) six-step quadratic part vanishes identically for all (a,b)
  (7) cubic six-step residual lies in the (2,1) channel only, for all (a,b)
  (8) cubic-return rigidity: |mu_6(a,b)|^2 = 12(b - 3a^2/2 - 1/12)^2 + (2a^2+1)^2/4 >= 1/4
  (9) direct primitive-T composition reproduces DYAD-THM-C21 (control, non-parametrised)
 (10) comparator orientation: conj(W_a) W_b = a^T B b - i a^T B J_Q b (Genesis J_Q, + convention)
 (11) invariant-form uniqueness: A^T H A = H, H symmetric  =>  H = c B
 (12) radial-fate boundary corollary: b = 4a^2/3  =>  mu_6 = -i (sqrt3/3)(1+2a^2), purely angular
 (13) rigidity minimiser: mu_6(0,1/12) = (1/2) exp(-i pi/3)

Exit 0 and "CERTIFICATE PASS" iff all checks hold.
"""
import sympy as sp, sys

r, e = sp.symbols('rho eta', real=True)
a, b = sp.symbols('a b', real=True)
om = (-1 + sp.I*sp.sqrt(3))/2   # exact primitive cube root of unity

def trunc(expr, deg):
    P = sp.Poly(sp.expand(expr), r, e)
    return sum(c*r**i*e**j for (i, j), c in P.terms() if i + j <= deg)

def jet(F, deg=3):
    out = []
    for fi in F:
        s = sp.expand(sp.series(fi, r, 0, deg+1).removeO())
        s = sp.expand(sp.series(s, e, 0, deg+1).removeO())
        out.append(trunc(s, deg))
    return out

def compose(F, G, deg=3):
    return [trunc(sp.expand(fi.subs({r: G[0], e: G[1]}, simultaneous=True)), deg) for fi in F]

def sixstep(J):
    G = J
    for _ in range(5):
        G = compose(J, G)
    return G

def channels(G):
    w, wb = sp.symbols('w wb')
    omb = sp.conjugate(om)
    eta_ = (w - wb)/(om - omb)
    rho_ = w - om*eta_
    DW = sp.expand((G[0] - r + om*(G[1] - e)).subs({r: rho_, e: eta_}, simultaneous=True))
    P = sp.Poly(DW, w, wb)
    return {k: sp.nsimplify(sp.expand(sp.expand_complex(v))) for k, v in P.terms()}

ok = True
def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and bool(cond)

# generic shear family
Tab = [r - sp.sin(e), e + r + a*r**2 + b*r**3 - sp.sin(e)]
G = sixstep(jet(Tab))
quad = [trunc(sp.expand(G[0] - r), 2), trunc(sp.expand(G[1] - e), 2)]
check("six-step quadratic part vanishes for all (a,b)", quad == [0, 0])
ch = channels(G)
check("cubic residual confined to (2,1) channel", all(sp.simplify(v) == 0 for k, v in ch.items() if k != (2, 1)))
mu_ab = ch[(2, 1)]
law = 3*b - 4*a**2 - sp.I*sp.sqrt(3)*(sp.Rational(1, 3) + 2*a**2 - b)
check("shear-jet law mu_6(a,b)", sp.simplify(mu_ab - law) == 0)

cases = {
    "T (a=1/2,b=1/6) == DYAD-THM-C21": ((sp.Rational(1,2), sp.Rational(1,6)), -sp.Rational(1,2) - sp.I*2*sp.sqrt(3)/3),
    "T_s (a=0,b=1/6)":                  ((0, sp.Rational(1,6)), sp.Rational(1,2) - sp.I*sp.sqrt(3)/6),
    "T_log (a=0,b=0)":                  ((0, 0), -sp.I*sp.sqrt(3)/3),
    "T_tanh (a=0,b=-1/3)":              ((0, -sp.Rational(1,3)), -1 - sp.I*2*sp.sqrt(3)/3),
}
for name, ((av, bv), target) in cases.items():
    check(name, sp.simplify(mu_ab.subs({a: av, b: bv}) - target) == 0)

# direct (non-jet-parametrised) twin check
Ts = [r - sp.sin(e), e + sp.sinh(r) - sp.sin(e)]
check("direct T_s composition", sp.simplify(channels(sixstep(jet(Ts)))[(2,1)] - (sp.Rational(1,2) - sp.I*sp.sqrt(3)/6)) == 0)

# (8) cubic-return rigidity
m2 = sp.expand(mu_ab*sp.conjugate(mu_ab))
cs = 12*(b - sp.Rational(3,2)*a**2 - sp.Rational(1,12))**2 + (2*a**2 + 1)**2/4
check("rigidity: |mu_6|^2 completed-square identity", sp.simplify(m2 - cs) == 0)
check("rigidity: minimum 1/4 attained at (a,b)=(0,1/12)", sp.simplify(cs.subs({a:0,b:sp.Rational(1,12)}) - sp.Rational(1,4)) == 0)

# (9) direct primitive T control
T = [r - sp.sin(e), e + sp.exp(r) - 1 - sp.sin(e)]
check("direct primitive T composition == DYAD-THM-C21",
      sp.simplify(channels(sixstep(jet(T)))[(2,1)] - (-sp.Rational(1,2) - sp.I*2*sp.sqrt(3)/3)) == 0)

# (10) comparator orientation
r1, e1, r2, e2 = sp.symbols('r1 e1 r2 e2', real=True)
B  = sp.Matrix([[1, -sp.Rational(1,2)], [-sp.Rational(1,2), 1]])
JQ = sp.Matrix([[1, -2], [2, -1]])/sp.sqrt(3)
av, bv = sp.Matrix([r1, e1]), sp.Matrix([r2, e2])
C = sp.expand(sp.conjugate(r1 + om*e1)*(r2 + om*e2))
check("comparator: Re conj(W_a)W_b = a^T B b", sp.simplify(sp.re(C) - (av.T*B*bv)[0]) == 0)
check("comparator: Im conj(W_a)W_b = - a^T B J_Q b", sp.simplify(sp.im(C) + (av.T*B*JQ*bv)[0]) == 0)
check("Genesis J_Q: J_Q^T B J_Q = B and J_Q^2 = -I", sp.simplify(JQ.T*B*JQ - B) == sp.zeros(2) and sp.simplify(JQ*JQ + sp.eye(2)) == sp.zeros(2))

# (11) invariant-form uniqueness
h11, h12, h22 = sp.symbols('h11 h12 h22', real=True)
A = sp.Matrix([[1, -1], [1, 0]])
H = sp.Matrix([[h11, h12], [h12, h22]])
sol = sp.solve(list(A.T*H*A - H), [h11, h12, h22], dict=True)
Hs = H.subs(sol[0])
c = sp.symbols('c')
check("invariant symmetric forms of A are exactly c*B", len(sol) == 1 and sp.simplify(Hs - Hs[0,0]*B) == sp.zeros(2))

# (12) radial-fate boundary corollary
mu_bd = sp.simplify(mu_ab.subs(b, sp.Rational(4,3)*a**2))
check("boundary 4a^2=3b: mu_6 = -i sqrt3/3 (1+2a^2)", sp.simplify(mu_bd + sp.I*sp.sqrt(3)/3*(1+2*a**2)) == 0)
check("boundary: Re mu_6 = 0 but |mu_6| >= 1/sqrt3", sp.simplify(sp.re(mu_bd)) == 0 and sp.simplify(sp.Abs(mu_bd).subs(a,0) - 1/sp.sqrt(3)) == 0)

# (13) rigidity minimiser
mu_min = mu_ab.subs({a:0, b:sp.Rational(1,12)})
check("minimiser mu_6(0,1/12) = (1/2) e^{-i pi/3}", sp.simplify(sp.expand_complex(mu_min - sp.Rational(1,2)*sp.exp(-sp.I*sp.pi/3))) == 0)

print("CERTIFICATE PASS" if ok else "CERTIFICATE FAIL")
sys.exit(0 if ok else 1)
