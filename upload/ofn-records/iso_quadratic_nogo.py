# Standard C (PI decision 18 Oct: cubic order) -- raw carrier no-go, exact check of the key identity.
# Any F_kappa-invariant C^2 surface M through 0 with interaction I=O(|r|^3) on M is a graph w_e=G_e(w), G_e commuting
# with T to order 2, linear parts c_e in C with c_1=1, sum c_e=0 (tangent in the closure plane).
# Claim: the z*zbar coefficient of sum_e G_e(w) at degree 2 equals c11 * sum_e |c_e|^2, c11=-1/3  (never 0).
import sympy as sp, sys
s3=sp.sqrt(3); lam=sp.Rational(1,2)+sp.I*s3/2; lamb=sp.conjugate(lam)
z,zb=sp.symbols('z zb'); x,y=sp.symbols('x y',real=True)
eta=(z-zb)/(sp.I*s3); rho=(z+zb)/2+eta/2
f2=sp.expand(-(rho**2/2)/2+sp.I*s3/2*(rho**2/2))     # W-quadratic part of one step of T
def g2(c,cb):
    a=sp.symbols('a0:3'); g=a[0]*z**2+a[1]*z*zb+a[2]*zb**2
    eq=sp.expand(c*f2+g.subs({z:lam*z,zb:lamb*zb},simultaneous=True)-lam*g-f2.subs({z:c*z,zb:cb*zb},simultaneous=True))
    sol=sp.solve(sp.Poly(eq,z,zb).coeffs(),a,dict=True)[0]; return sp.expand(g.subs(sol))
c2=x+sp.I*y; c3=-1-c2
tot=sp.expand(g2(1,1)+g2(c2,sp.conjugate(c2))+g2(c3,sp.conjugate(c3)))
zzb=sp.Poly(tot,z,zb).coeff_monomial(z*zb)
target=-sp.Rational(1,3)*(1+x**2+y**2+(1+x)**2+y**2)
ok=sp.simplify(zzb-target)==0
print("zzbar coeff:",sp.factor(zzb)," == -1/3*sum|c_e|^2 :",ok)
sys.exit(0 if ok else 1)
