#!/usr/bin/env python3
# =============================================================================
# N-5A-S1-INF CLOSURE CERTIFICATE v1
# Exact primitive-map Taylor checks supporting L-MONO and L-PHASE.
# L-BACKBONE is an analytic consequence of the already-certified L1 inequality
# and is proved in the companion memo.
# =============================================================================
import sys
import sympy as sp

rho, eta = sp.symbols("rho eta", real=True)
u, v = sp.symbols("u v", real=True)
sqrt3 = sp.sqrt(3)
I = sp.I
FAIL = []

def check(name, cond):
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        FAIL.append(name)

def trunc(expr, deg):
    P = sp.Poly(sp.expand(expr), rho, eta)
    out = 0
    for (a,b), c in P.terms():
        if a+b <= deg:
            out += c*rho**a*eta**b
    return sp.expand(out)

def homogeneous(expr, deg):
    P = sp.Poly(sp.expand(expr), rho, eta)
    return sp.expand(sum(c*rho**a*eta**b for (a,b),c in P.terms() if a+b == deg))

def Tpoly(r,e,deg=4):
    s = e - e**3/sp.Integer(6)  # degree <=4
    exm1 = r + r**2/2 + r**3/6 + r**4/24
    return trunc(r-s,deg), trunc(e+exm1-s,deg)

# Exact Taylor jet of F=T^6 through degree 4.
r,e = rho,eta
for _ in range(6):
    r,e = Tpoly(r,e,4)
dr, de = sp.expand(r-rho), sp.expand(e-eta)

Q = rho**2-rho*eta+eta**2
dr2,de2 = homogeneous(dr,2),homogeneous(de,2)
dr3,de3 = homogeneous(dr,3),homogeneous(de,3)
dr4,de4 = homogeneous(dr,4),homogeneous(de,4)

check("F=T^6 has no quadratic primitive-coordinate term",
      sp.simplify(dr2)==0 and sp.simplify(de2)==0)
check("exact cubic rho jet",
      sp.simplify(dr3 - (8*eta-7*rho)*Q/6)==0)
check("exact cubic eta jet",
      sp.simplify(de3 - (eta-8*rho)*Q/6)==0)

# Primitive analytic W coordinate: W=(rho-eta/2)+i sqrt(3)eta/2.
subs = {rho:u+v/sqrt3, eta:2*v/sqrt3}
du3 = sp.expand((dr3-de3/2).subs(subs))
dv3 = sp.expand((sqrt3*de3/2).subs(subs))
W = u+I*v
Qw = u**2+v**2
tau = 2*sqrt3/3
c = -sp.Rational(1,2)-I*tau
target = sp.expand_complex(c*W*Qw)

check("exact primitive six-step cubic W jet is c21*W*|W|^2",
      sp.simplify(du3-sp.re(target))==0 and
      sp.simplify(dv3-sp.im(target))==0)

# Quartic primitive term produces a genuine Q^(3/2) angular remainder.
du4 = sp.expand((dr4-de4/2).subs(subs))
dv4 = sp.expand((sqrt3*de4/2).subs(subs))
im_rel4 = sp.factor((u*dv4-v*du4)/(u**2+v**2))
ray_coeff = sp.simplify((im_rel4/u**3).subs(v,0))
check("quartic angular relative coefficient on positive-u ray is nonzero",
      sp.simplify(ray_coeff + 25*sqrt3/48)==0)
print("  exact ray coefficient =", ray_coeff)
print("  consequence: after subtracting -tau Q, a uniform O(Q^2) remainder is impossible;")
print("               the exact primitive Taylor scale is O(Q^(3/2)).")

# One-step linear action in W: +pi/3 rotation.
# Linear primitive map is (rho',eta')=(rho-eta,rho).
rho1 = rho-eta
eta1 = rho
u1 = sp.expand((rho1-eta1/2).subs(subs))
v1 = sp.expand((sqrt3*eta1/2).subs(subs))
lamW = sp.expand_complex((sp.Rational(1,2)+I*sqrt3/2)*W)
check("one-step primitive linearization is +pi/3 rotation in W",
      sp.simplify(u1-sp.re(lamW))==0 and
      sp.simplify(v1-sp.im(lamW))==0)

print("-"*72)
if FAIL:
    print("RESULT: FAIL", FAIL)
    sys.exit(1)
print("RESULT: ALL EXACT SYMBOLIC ASSERTIONS PASS.")
print("Analyticity then supplies uniform local Taylor remainders:")
print(" T_W=lambda W+O(|W|^2), F_W=W+c21 W|W|^2+O(|W|^4).")
sys.exit(0)
