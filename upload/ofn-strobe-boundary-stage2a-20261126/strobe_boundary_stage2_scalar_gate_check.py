#!/usr/bin/env python3
"""SESSION: parity-gated quadratic shear, fixed raw DYAD frame and quarter strobe.
Exact regressions for the written scalar-gate classification and norm blindness.
Independent of the ordered-sum evaluation, the raw jet recurrence is adapted
from the frozen #398 r2 real-coordinate checker to an alternating source.
No owner extractor replay; no physical selection. Python 3 / SymPy 1.14.0.
"""
from math import gcd
import sympy as sp
from sympy import QQ


def need(ok, label):
    if not ok:
        raise AssertionError(label)


def formulas(x, I, eps):
    A = (1+I)*(x*x+I)/(x*x*(x-1)**2*(x*x+x+1))
    B = ((1+eps*I)*(x*x+eps*I))/(x*x*(x+1)**2*(x*x-x+1))
    Cnum = -2*(x+I)**2*(x*x-I*x-1) if eps == -1 else -2*(1+I)*(x*x+1)*(x*x+I)
    C = Cnum/(x*x*(x-1)*(x+1)*(x*x-x+1)*(x*x+x+1))
    return A, B, C


def symbolic():
    x, I = sp.Symbol('x'), sp.I
    for eps in (-1, 1):
        def S(u, v, a, b):
            X, Y = a*x**u, b*x**v
            Xs = (eps if a == -1 else 1)*(-I)**u
            Ys = (eps if b == -1 else 1)*(-I)**v
            return ((1-Ys)/(1-Y)-(1-Xs*Ys)/(1-X*Y))/(1-X)
        def T(a,b):
            return S(3,1,a,b)-x**(-2)*S(1,3,a,b)
        A,B,C = formulas(x,I,eps)
        for value,target in ((T(1,1),A),(T(-1,-1),B),(T(-1,1)+T(1,-1),C)):
            need(sp.cancel(value-target)==0, f'geometric collapse eps={eps}')
        # The automorphism x -> -x, i -> eps*i interchanges A and B.
        Ap,Bp,_ = formulas(-x,eps*I,eps)
        need(sp.cancel(Ap-B)==0 and sp.cancel(Bp-A)==0, 'Galois exchange')
    print('SYMBOLIC_GEOMETRIC_AND_GALOIS_PASS (both strobe parities)')


def automorphism(K,value,k):
    z=K.zero; w=K.unit**k
    for c in value.to_list():
        z=z*w+K.convert(c)
    return z


def raw(K,L,p,ac,ad,sigma,b,g,steps):
    # Extract pure V^3 by exact truncated real-coordinate iteration W=0,V=t.
    kap=2-L-L**(p-1); ip=(1+L)**(-1); wc=(L-1)/kap
    r1=L*ip; e1=(L-1)*ip
    r2=e2=r3=e3=K.zero
    for j in range(steps):
        a=ac+sigma*((-1)**j)*ad
        G2=a*r1*r1; G3=2*a*r1*r2+b*r1*r1*r1; S3=g*e1*e1*e1
        r1,e1,r2,e2,r3,e3=(r1-e1,e1+kap*(r1-e1),
                           r2-e2,e2+kap*(r2-e2+G2),
                           r3-e3-S3,e3+kap*(r3-e3+G3-S3))
    return L**((-steps)%p)*(r3+wc*e3)


def exact():
    samples=(12,16,20,24,28,32,36,40,44,60,72)
    gates=((0,0),(sp.Rational(1,2),0),(-sp.Rational(1,2),0),
           (0,sp.Rational(1,2)),(sp.Rational(1,4),sp.Rational(1,4)),
           (sp.Rational(3,5),-sp.Rational(2,7)))
    cubics=((sp.Rational(1,6),-sp.Rational(1,6)),(sp.Rational(7,5),-sp.Rational(3,7)))
    paths=cases=norms=contrast=0
    for p in samples:
        s=p//4; eps=(-1)**s; K=QQ.cyclotomic_field(p); L=K.unit; x=L**(p-1); I=L**s
        A,B,C=formulas(x,I,eps); ratio=B/A; mix=C/A
        need(A!=K.zero and B!=K.zero and C!=K.zero,'nonzero coefficients')
        # Direct finite ordered sums, independent of the geometric expression.
        def S(u,v,a,b):
            X=a*x**u;Y=b*x**v; Xj=Yj=K.one; pref=val=K.zero
            for _ in range(s):
                val+=pref*Yj;pref+=Xj;Xj*=X;Yj*=Y
            return val
        def T(a,b):return S(3,1,a,b)-L**2*S(1,3,a,b)
        for val,target in ((T(1,1),A),(T(-1,-1),B),(T(1,-1)+T(-1,1),C)):
            need(val==target,f'path p={p}');paths+=1
        q0=L**5*(I*L**2+I-L**2+1)/(2*(L+1)**4*(L**2+L+1))
        A1=(L-1)/(L*(1+L)**2); B1=2*L*A1; C1=L*L*A1
        need(B1*C1*A==4*q0 and q0!=K.zero,'baseline')
        need(automorphism(K,ratio,p-1)==ratio,'ratio real')
        need(automorphism(K,ratio,1+p//2)*ratio==K.one,'inverse conjugate')
        # Product of the embeddings of K^+; all calculations in the full field.
        norm=K.one
        for k in range(1,p//2):
            if gcd(k,p)==1:norm*=automorphism(K,ratio,k)
        need(norm==K.one,f'real-subfield norm p={p}');norms+=1
        need((ratio==K.one)==(p==12),'exception p=12 only')
        for ac,ad in gates:
            aa,dd=map(K.convert,(ac,ad))
            for b,g in cubics:
                bb,gg=map(K.convert,(b,g))
                for sigma in (1,-1):
                    expected=4*q0*(aa*aa+ratio*dd*dd+sigma*mix*aa*dd)
                    need(raw(K,L,p,aa,dd,sigma,bb,gg,s)==expected,
                         f'raw p={p} mean={ac} contrast={ad} sign={sigma}')
                    cases+=1
        # Positive/negative control: a gate which switches off every other step
        # must be distinguishable by initial parity, unlike the pure sign gate.
        a=K.convert(sp.Rational(1,4)); z=K.zero
        plus=raw(K,L,p,a,a,1,z,z,s);minus=raw(K,L,p,a,a,-1,z,z,s)
        need(plus-minus==8*q0*mix*a*a and plus!=minus,'asymmetric gate contrast');contrast+=1
        print(f'P={p} RAW_PASS 24/24; PATH_PASS 3/3; NORM_PASS; CONTRAST_PASS')
    print(f'RAW_JET_PASS {cases}/{cases}; DIRECT_SUM_PASS {paths}/{paths}')
    print(f'REAL_NORM_ONE_PASS {norms}/{norms}; NONCONSTANT_AMPLITUDE_CONTRAST_PASS {contrast}/{contrast}')


if __name__=='__main__':
    print('SymPy',sp.__version__,flush=True)
    symbolic()
    exact()
    print('ALL_STAGE2_SCALAR_GATE_CHECKS_PASS')
