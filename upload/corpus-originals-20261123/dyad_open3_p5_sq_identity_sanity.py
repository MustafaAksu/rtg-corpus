# DYAD OPEN 3 scope note v0.1.1 -- SESSION sanity check (not the P2 gate script).
# Checks exactly over Q(sqrt3):  P5(L^{-1} z) == D(D3)(z)[mu q z] + 2 q D3(z),
# D3 = 2 Re(conj(z) h2(z)), W = rho + omega*eta, omega = e^{2 pi i/3} (DYAD v6.4.13 section 6.14).
# Negative controls (must FAIL): without +2qD3; with -2qD3; omega = e^{-2 pi i/3}.
import sys, sympy as sp
x,y,t=sp.symbols('x y t',real=True); I=sp.I; s3=sp.sqrt(3)
z=x+I*y; zb=x-I*y; q=x**2+y**2
mu=-sp.Rational(1,2)-I*2*s3/3
h2=lambda z,zb: -(1+I*s3)/12*z**2-sp.Rational(1,3)*z*zb+(1-I*s3)/24*zb**2
D3=sp.expand(2*sp.re(sp.expand(zb*h2(z,zb))))
zt=z+t*mu*q*z; zbt=sp.conjugate(zt)
DD=sp.expand(sp.diff(sp.re(sp.expand(2*zbt*h2(zt,zbt))),t).subs(t,0))
def P5(sgn):
    om=sp.Rational(-1,2)+sgn*I*s3/2; eta=y/sp.im(om); rho=x-sp.re(om)*eta
    Qp=sp.expand(rho**2-rho*eta+eta**2); assert sp.simplify(Qp-q)==0
    return sp.expand(Qp/24*(5*eta**3-43*eta**2*rho+4*eta*rho**2-5*rho**3))
zero=lambda e: sp.simplify(sp.expand(e))==0
res={"main":zero(P5(1)-DD-2*q*D3),
     "neg_no_2qD3":zero(P5(1)-DD),
     "neg_minus_2qD3":zero(P5(1)-DD+2*q*D3),
     "neg_other_omega":zero(P5(-1)-DD-2*q*D3)}
print(res)
ok=res["main"] and not any(v for k,v in res.items() if k.startswith("neg"))
print("PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
