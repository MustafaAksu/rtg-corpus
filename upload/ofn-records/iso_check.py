# Degree-2 test: can w + G1(w) + G2(w) vanish identically (raw closure) for germs G commuting with T,
# linear parts c in {lambda^2, lambda^4} (cube-root lock) or {-1} (antipodal lock w3=0)?
import sympy as sp
s3=sp.sqrt(3); lam=sp.Rational(1,2)+sp.I*s3/2
z,zb=sp.symbols('z zb')
r,e=sp.symbols('r e')
# W = rho - eta/2 + i sqrt3/2 eta ; inverse
def toRE(w,wb):
    eta=(w-wb)/(sp.I*s3); rho=(w+wb)/2+eta/2; return rho,eta
rho,eta=toRE(z,zb)
T2=(0, rho**2/2)   # quadratic part of T in (rho,eta): rho' has -sin(eta) (no quad); eta' has e^rho-1 -> rho^2/2
f2=sp.expand(T2[0]-T2[1]/2+sp.I*s3/2*T2[1])   # W-component of quadratic part
P=sp.Poly(f2,z,zb); print("f2 =",f2)
def g2_for(c):
    cb=sp.conjugate(c)
    a=sp.symbols('a0:3'); g=a[0]*z**2+a[1]*z*zb+a[2]*zb**2
    lhs=c*f2+g.subs({z:lam*z,zb:sp.conjugate(lam)*zb},simultaneous=True)
    rhs=lam*g+f2.subs({z:c*z,zb:cb*zb},simultaneous=True)
    sol=sp.solve(sp.Poly(sp.expand(lhs-rhs),z,zb).coeffs(),a,dict=True)[0]
    return sp.expand(g.subs(sol))
for name,cs in [("cube-root lock",[lam**2,lam**4]),("conj cube-root",[lam**4,lam**2]),("antipodal",[-1])]:
    tot=sum(g2_for(sp.nsimplify(sp.expand(c))) for c in cs)
    print(name,": degree-2 of w+G1+G2 =",sp.simplify(tot))
