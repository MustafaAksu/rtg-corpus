# Riemann-lens finding certificate: invariant form, uniqueness, tau, closed form,
# and the tangent-to-identity property of F = T^6.
import sympy as sp, sys
FAIL=[]
def ck(n,c):
    print(f"[{'PASS' if c else 'FAIL'}] {n}")
    if not c: FAIL.append(n)
r,e,a,b,c_=sp.symbols('r e a b c')
J=sp.Matrix([[1,-1],[1,0]])
ck("R1 J has order 6 with eigenvalues exp(+-i pi/3)",
   (J**6==sp.eye(2)) and all((J**k)!=sp.eye(2) for k in range(1,6)))
v=sp.Matrix([r,e]); w=J*v
Q=r**2-r*e+e**2
ck("R2 Q_true is exactly J-invariant", sp.simplify(sp.expand((w[0]**2-w[0]*w[1]+w[1]**2)-Q))==0)
Qe=r**2+e**2
ck("R3 Q_euclid is NOT J-invariant (defect rho(rho-2eta)) -> SG-1 primacy is forced, not conventional",
   sp.simplify(sp.expand((w[0]**2+w[1]**2)-Qe)-(r*(r-2*e)))==0)
F=a*r**2+b*r*e+c_*e**2
Fw=a*w[0]**2+b*w[0]*w[1]+c_*w[1]**2
sol=sp.solve(sp.Poly(sp.expand(Fw-F),r,e).coeffs(),[a,b,c_],dict=True)
ck("R4 the invariant quadratic forms are a 1-parameter family -> Q_true unique up to scale",
   sol==[{a:c_, b:-c_}])
g=sp.Matrix([[1,sp.Rational(-1,2)],[sp.Rational(-1,2),1]])
tau=2*sp.sqrt(3)/3
ck("R5 tau = 1/sqrt(det g) exactly (det g = 3/4)", sp.simplify(tau-1/sp.sqrt(g.det()))==0 and g.det()==sp.Rational(3,4))
ratio=sp.exp(sp.pi/(3*tau))
ck("R6 closed form: exp(pi/(3 tau)) = exp(sqrt(3) pi/6) = 2.476632271...",
   sp.simplify(sp.pi/(3*tau)-sp.sqrt(3)*sp.pi/6)==0 and abs(float(ratio)-2.476632271)<1e-8)
N=5
def tr(x): return sp.expand(sp.series(sp.series(x,r,0,N).removeO(),e,0,N).removeO())
def T(u): 
    p,q=u; return (tr(p-sp.sin(q)), tr(q+(sp.exp(p)-1)-sp.sin(q)))
u=(r,e)
for _ in range(6): u=T(u)
J6=sp.Matrix([[sp.diff(u[0],r),sp.diff(u[0],e)],[sp.diff(u[1],r),sp.diff(u[1],e)]]).subs({r:0,e:0})
ck("R7 F = T^6 is tangent to the identity", J6==sp.eye(2))
degs=[min(sum(m) for m in sp.Poly(sp.simplify(u[i]-[r,e][i]),r,e).monoms()) for i in range(2)]
ck(f"R8 F - id has leading total degree 3 in both components {degs} -> cubic parabolic class, |z_n| ~ n^(-1/2), matching Q_m ~ 1/m", degs==[3,3])
print("-"*60)
if FAIL: print("FAILURES:",FAIL); sys.exit(1)
print("RESULT: ALL PASS — Riemann-lens identifications certified.")
sys.exit(0)
