# OPEN 19 Lemma K, boundary a=0 (exit-gated, finite b<=7): for input c*zbar^b the bracket [X3,Y] has exactly one zbar-free output monomial, z^(b+2), with coefficient -mu*conj(c). Real Jacobians, exact sympy.
import sympy as sp
x,y=sp.symbols('x y',real=True); cr,ci=sp.symbols('cr ci',real=True)
mu=sp.Rational(-1,2)-sp.I*2*sp.sqrt(3)/3; W=x+sp.I*y; Wb=x-sp.I*y; c=cr+sp.I*ci
def vf(V): V=sp.expand(V); return sp.Matrix([sp.re(V),sp.im(V)]).applyfunc(sp.expand)
X3=vf(mu*W**2*Wb)
z,zb=sp.symbols('z zb')
ok=True
for b in range(0,8):
    Y=vf(c*Wb**b)
    Br=(Y.jacobian([x,y])*X3-X3.jacobian([x,y])*Y).applyfunc(sp.expand)
    Bc=sp.expand(Br[0]+sp.I*Br[1])
    Bz=sp.expand(Bc.subs({x:(z+zb)/2,y:(z-zb)/(2*sp.I)}))
    P=sp.Poly(Bz,z,zb)
    got=P.coeff_monomial(z**(b+2)); want=sp.expand(-mu*sp.conjugate(c))
    other=[m for m in P.monoms() if m[1]==0]
    r=sp.simplify(got-want)==0 and other==[(b+2,0)]
    print(b,r); ok&=r
import sys; print("PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
