# OPEN 19 Lemma K reproduction (exit-gated; finite k only, not the all-k proof). Independent check: real kernel of ad_{X3} on homogeneous real vector fields of degree k on R^2,
# X3 = complex component mu*|W|^2 W, computed with sympy real Jacobians (no complex shortcut).
import sympy as sp
x,y=sp.symbols('x y',real=True)
s3=sp.sqrt(3); mu=sp.Rational(-1,2)-sp.I*2*s3/3
W=x+sp.I*y
V3=sp.expand(mu*(x**2+y**2)*W)
X3=sp.Matrix([sp.re(V3),sp.im(V3)]).applyfunc(sp.expand)
def bracket(A,B):
    JA=A.jacobian([x,y]); JB=B.jacobian([x,y])
    return (JB*A-JA*B).applyfunc(sp.expand)
FAIL=[]
for k in range(2,14):
    mons=[x**i*y**(k-i) for i in range(k+1)]
    cs=sp.symbols(f'c0:{2*(k+1)}')
    Y=sp.Matrix([sum(cs[i]*mons[i] for i in range(k+1)), sum(cs[k+1+i]*mons[i] for i in range(k+1))])
    Bk=bracket(X3,Y)
    eqs=[]
    for comp in Bk:
        P=sp.Poly(comp,x,y)
        eqs+=P.coeffs()
    M=sp.Matrix([[sp.diff(e,c) for c in cs] for e in eqs])
    M=M.applyfunc(sp.nsimplify)
    dim=len(cs)-M.rank(simplify=True)
    print(k,'kernel dim',dim)
    expect=1 if k==3 else 0
    if dim!=expect: FAIL.append(k)
    if k==3:
        ns=M.nullspace(simplify=True)
        v=ns[0]; Yk=sp.Matrix([sum(v[i]*mons[i] for i in range(k+1)), sum(v[k+1+i]*mons[i] for i in range(k+1))])
        # check proportional to X3
        r=sp.simplify(Yk[0]*X3[1]-Yk[1]*X3[0]); print('  parallel to X3:',r==0)
        if r!=0: FAIL.append('k3-parallel')
import sys
print('PASS' if not FAIL else ('FAIL',FAIL)); sys.exit(1 if FAIL else 0)
