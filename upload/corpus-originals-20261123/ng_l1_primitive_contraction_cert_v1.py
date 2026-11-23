#!/usr/bin/env python3
"""Exact symbolic certificate for Number Genesis L1.

Target:
  For the exact primitive dyad map
      T(rho,eta) = (rho-sin eta, eta + exp(rho)-1-sin eta),
  with F=T^6 and Q_true=rho^2-rho*eta+eta^2,
  certify the primitive-frame expansion
      Q_true(Fx)-Q_true(x)
        = -Q_true(x)^2 + Q_true(x)*C3(rho,eta)/24 + O(||x||^6)
        = -Q_true^2 + O(Q_true^(5/2)),
  uniformly in phase near the elliptic fixed point.

The script uses exact SymPy rational/sqrt(3) algebra for every polynomial identity.
It does not use a normal-form identification Q=|W_nf|^2, so it is immune to
that frame-conflation error.
"""

import sympy as sp

rho, eta = sp.symbols("rho eta")
U, V, phi = sp.symbols("U V phi", real=True)


def trunc(expr, deg):
    """Total-degree truncation in (rho,eta)."""
    expr = sp.expand(expr)
    poly = sp.Poly(expr, rho, eta, domain="EX")
    out = 0
    for mon, coeff in poly.terms():
        if sum(mon) <= deg:
            out += coeff * rho**mon[0] * eta**mon[1]
    return sp.expand(out)


def homogeneous(expr, deg):
    expr = sp.expand(expr)
    poly = sp.Poly(expr, rho, eta, domain="EX")
    out = 0
    for mon, coeff in poly.terms():
        if sum(mon) == deg:
            out += coeff * rho**mon[0] * eta**mon[1]
    return sp.expand(out)


def T_trunc(R, E, deg=4):
    # Degree 4 is sufficient because Q_true is quadratic and
    # Delta Q through total degree 5 depends on Delta(rho,eta) through degree 4.
    sinE = trunc(E - E**3 / sp.Integer(6), deg)
    expm1R = trunc(
        R + R**2 / sp.Integer(2) + R**3 / sp.Integer(6) + R**4 / sp.Integer(24),
        deg,
    )
    return trunc(R - sinE, deg), trunc(E + expm1R - sinE, deg)


def Q(R, E):
    return sp.expand(R**2 - R*E + E**2)


# Exact total-degree-4 Taylor jet of F=T^6.
R, E = rho, eta
for _ in range(6):
    R, E = T_trunc(R, E, 4)

drho = trunc(R - rho, 4)
deta = trunc(E - eta, 4)

# Certified cubic jet already present in the dyadic ledger.
drho3_expected = (
    sp.Rational(4, 3) * eta**3
    - sp.Rational(5, 2) * rho * eta**2
    + sp.Rational(5, 2) * rho**2 * eta
    - sp.Rational(7, 6) * rho**3
)
deta3_expected = (
    sp.Rational(1, 6) * eta**3
    - sp.Rational(3, 2) * rho * eta**2
    + sp.Rational(3, 2) * rho**2 * eta
    - sp.Rational(4, 3) * rho**3
)
assert sp.expand(homogeneous(drho, 3) - drho3_expected) == 0
assert sp.expand(homogeneous(deta, 3) - deta3_expected) == 0

# New primitive-frame quartic coordinate jet.
drho4 = sp.factor(homogeneous(drho, 4))
deta4 = sp.factor(homogeneous(deta, 4))

# Radial change through total degree 5.
dQ = trunc(Q(R, E) - Q(rho, eta), 5)
dQ4 = sp.factor(homogeneous(dQ, 4))
dQ5 = sp.factor(homogeneous(dQ, 5))
Q0 = Q(rho, eta)

assert sp.expand(dQ4 + Q0**2) == 0

C3 = sp.expand(5*eta**3 - 43*eta**2*rho + 4*eta*rho**2 - 5*rho**3)
assert sp.expand(dQ5 - Q0*C3/sp.Integer(24)) == 0

# Independent exact cross-check using a one-parameter radial scaling
# rho=t*a, eta=t*b and series in t.  This checks the same radial
# coefficients without using the total-degree monomial filter above.
a, b, t = sp.symbols("a b t")
def trunc_t(expr, order):
    return sp.series(expr, t, 0, order).removeO().expand()
Rt, Et = t*a, t*b
for _ in range(6):
    sinEt = trunc_t(sp.sin(Et), 5)
    expRt = trunc_t(sp.exp(Rt)-1, 5)
    Rt, Et = trunc_t(Rt-sinEt, 5), trunc_t(Et+expRt-sinEt, 5)
Qt0 = t**2*(a*a-a*b+b*b)
dQt = sp.series((Rt**2-Rt*Et+Et**2)-Qt0, t, 0, 6).removeO().expand()
assert sp.expand(dQt.coeff(t,4) + (a*a-a*b+b*b)**2) == 0
assert sp.factor(
    dQt.coeff(t,5)
    - (a*a-a*b+b*b)*(5*b**3-43*b**2*a+4*b*a**2-5*a**3)/sp.Integer(24)
) == 0

# Anti-correlation coordinates: Q_true = U^2 + V^2 exactly.
sub_uv = {
    rho: 2*U/sp.sqrt(3),
    eta: V + U/sp.sqrt(3),
}
assert sp.simplify(Q0.subs(sub_uv) - (U**2 + V**2)) == 0
C3_uv = sp.factor(sp.expand(C3.subs(sub_uv)))

# Unit-circle phase harmonic A(phi) defined by dQ5=Q^(5/2) A(phi).
A = sp.trigsimp(
    (C3_uv/sp.Integer(24)).subs({U: sp.cos(phi), V: sp.sin(phi)})
)
A_expected = (
    -sp.Rational(1,3)*sp.sin(phi)
    -sp.Rational(13,24)*sp.sin(3*phi)
    -sp.Rational(11,18)*sp.sqrt(3)*sp.cos(phi)
    +sp.sqrt(3)/sp.Integer(8)*sp.cos(3*phi)
)
assert sp.trigsimp(A - A_expected) == 0

# Explicit phase-uniform triangle bound |A(phi)| <= C5.
C5 = sp.Rational(1,3) + sp.Rational(13,24) + sp.Rational(11,18)*sp.sqrt(3) + sp.sqrt(3)/8
C5 = sp.simplify(C5)
assert sp.simplify(C5 - (sp.Rational(7,8) + sp.Rational(53,72)*sp.sqrt(3))) == 0

print("="*78)
print("RTG Number Genesis L1 symbolic certificate")
print("="*78)
print("Primitive map: T(rho,eta)=(rho-sin eta, eta+exp(rho)-1-sin eta)")
print("F=T^6 ; Q_true=rho^2-rho*eta+eta^2")
print()
print("[PASS] exact primitive six-step cubic jet matches certified ledger jet")
print("[NEW ] primitive six-step quartic coordinate jet:")
print("       Delta rho_4 =", drho4)
print("       Delta eta_4 =", deta4)
print()
print("[PASS] homogeneous degree-4 radial identity:")
print("       Delta Q_4 = -Q_true^2")
print("[PASS] homogeneous degree-5 radial identity:")
print("       Delta Q_5 = Q_true*(5 eta^3 - 43 eta^2 rho + 4 eta rho^2 - 5 rho^3)/24")
print("[PASS] independent one-parameter scaling-series cross-check")
print()
print("[PASS] anti-correlation frame Q_true=U^2+V^2 exactly")
print("       C3(U,V) =", C3_uv)
print("[PASS] phase harmonic A(phi)=DeltaQ_5/Q^(5/2):")
print("       A(phi) =", A_expected)
print("[BOUND] |A(phi)| <= C5 = 7/8 + 53*sqrt(3)/72")
print("        C5 ~=", sp.N(C5, 16))
print()
print("[THEOREM INPUT] Since the exact primitive map is analytic, the omitted Taylor")
print("                terms are uniformly O(||(rho,eta)||^6)=O(Q_true^3) near 0.")
print("[L1] Therefore, phase-uniformly on a sufficiently small punctured sector,")
print("     Delta Q_true = -Q_true^2 + O(Q_true^(5/2)).")
print("     Hence there exists epsilon>0 with 0<Q_true<epsilon =>")
print("     0 < Q_true(Fx) < Q_true(x).")
print("="*78)
