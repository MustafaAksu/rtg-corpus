# DYAD M2c certificate (exit-gated): exact one-step normal form of the K_p family (rho'=rho-sin eta, eta'=eta+K_p(e^rho-1)-K_p sin eta) in the frame W=rho+((lambda-1)/K_p) eta, normalizer with resonant coefficients zero (DYAD-ALG-NF6 convention). p=6 calibrated against DYAD-ALG-NF6; p=5 nu5 = n_32 compared with the Genesis v2.8.7 section 6.2 closed form. Optional argv[1]="neg" perturbs the target (must exit 1).
import sympy as sp, sys
L=sp.symbols('L'); N=5
def make(p):
    Phi=sp.Poly(sp.cyclotomic_poly(p,L),L,domain='QQ')
    def red(e): return sp.Poly(e,L,domain='QQ').rem(Phi).as_expr()
    def inv(e): return sp.invert(sp.Poly(e,L,domain='QQ'),Phi).as_expr()
    lb=red(L**(p-1))
    return Phi,red,inv,lb
def run(p):
    Phi,red,inv,lb=make(p)
    R=lambda e: red(sp.expand(e))
    def mul(A,B):
        C={}
        for (a,b),x in A.items():
            for (c,d),y in B.items():
                if a+b+c+d<=N: C[(a+c,b+d)]=C.get((a+c,b+d),0)+x*y
        return {k:R(v) for k,v in C.items()}
    def add(A,B,s=1):
        C=dict(A)
        for k,v in B.items(): C[k]=R(C.get(k,0)+s*v)
        return C
    scal=lambda A,s:{k:R(v*s) for k,v in A.items()}
    conjE=lambda e: R(sp.expand(e).subs(L,lb))     # complex conjugation sigma_{-1}
    conj=lambda A:{(b,a):conjE(v) for (a,b),v in A.items()}
    def series(X,coef):
        Rr={}; P={(0,0):sp.Integer(1)}
        for k in range(1,N+1):
            P=mul(P,X); c=coef(k)
            if c: Rr=add(Rr,scal(P,c))
        return Rr
    sin_=lambda X: series(X,lambda k: 0 if k%2==0 else sp.Rational((-1)**((k-1)//2),sp.factorial(k)))
    expm1=lambda X: series(X,lambda k: sp.Rational(1,sp.factorial(k)))
    def power(A,e):
        Rr={(0,0):sp.Integer(1)}
        for _ in range(e): Rr=mul(Rr,A)
        return Rr
    def compose(A,H):
        Hb=conj(H); Rr={}
        for (a,b),v in A.items(): Rr=add(Rr,scal(mul(power(H,a),power(Hb,b)),v))
        return Rr
    deg=lambda A,k:{key:v for key,v in A.items() if sum(key)==k and v!=0}
    K=R(2-L-lb); beta=R((L-1)*inv(K)); betab=conjE(beta)
    z={(1,0):sp.Integer(1)}; zb={(0,1):sp.Integer(1)}
    eta=scal(add(z,zb,-1),inv(R(beta-betab)))
    rho=add(z,scal(eta,-beta))
    f=add(add(rho,sin_(eta),-1),scal(add(add(eta,scal(expm1(rho),K)),scal(sin_(eta),-K)),beta))
    assert R(f[(1,0)]-L)==0 and f.get((0,1),0)==0
    h=dict(z); n={(1,0):L}
    for k in range(2,N+1):
        E=deg(add(compose(f,h),compose(h,n),-1),k)
        for (a,b),v in E.items():
            if (a-b-1)%p==0: n[(a,b)]=R(n.get((a,b),0)+v)
            else: h[(a,b)]=R(h.get((a,b),0)-v*inv(R(L-L**a*lb**b)))
    return n,R
ok=True
n6,R6=run(6)   # calibration against DYAD-ALG-NF6 (L=zeta6, sqrt3 i = 2L-1)
s3i=2*L-1
ref={(2,1):sp.Rational(1,8)-sp.Rational(7,72)*s3i,(3,2):-sp.Rational(5,432)+sp.Rational(23,3888)*s3i,(0,5):sp.Rational(43,17280)-sp.Rational(227,155520)*s3i}
for k,v in ref.items():
    d=R6(n6[k]-v); print('p=6',k,'match DYAD-ALG-NF6:',d==0); ok&=(d==0)
n5,R5=run(5)
s5=2*(L+L**4)+1; is10=2*(L-L**4)   # sqrt5, i*sqrt(10+2sqrt5) in Q(zeta5)
NEG=len(sys.argv)>1 and sys.argv[1]=="neg"
g=(355+(1 if NEG else 0)-159*s5)/48+(1106*s5-2473)*is10/48
d=R5(n5[(3,2)]-g); print('p=5 n32 == Genesis closed form:',d==0); ok&=(d==0)
print('p=5 n32 =',n5[(3,2)]); print('p=5 n21 =',n5[(2,1)]); print('p=5 n04 =',n5[(0,4)])
print('PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
