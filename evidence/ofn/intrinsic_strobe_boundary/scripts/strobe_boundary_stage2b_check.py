#!/usr/bin/env python3
"""SESSION Stage 2B: alternating cubic source and first parity resonance.
Exact finite regressions, not an owner extractor replay or physical certificate.
Raw jets use the real-coordinate shear recurrence; no normal form is used in
coefficient extraction. Python 3 / SymPy 1.14.0.
"""
from math import factorial
import sympy as sp
from sympy import QQ


def need(ok, label):
    if not ok:
        raise AssertionError(label)


def conj(K, x, p):
    z = K.zero
    for c in x.to_list():
        z = z*K.unit**(p-1)+K.convert(c)
    return z


def setup(p):
    K = QQ.cyclotomic_field(p); L = K.unit
    return K, L, p//4, 2-L-L**(p-1), (1+L)**(-1)


def raw3(data, a, d, b, g, beta, delta, sigma, steps):
    K,L,s,kap,ip=data
    r1=L*ip; e1=(L-1)*ip; r2=e2=r3=e3=K.zero
    for j in range(steps):
        sign=sigma*(-1)**j
        aj=a+sign*d; bj=b+sign*beta; gj=g+sign*delta
        G2=aj*r1*r1; G3=2*aj*r1*r2+bj*r1*r1*r1; S3=gj*e1*e1*e1
        r1,e1,r2,e2,r3,e3=(r1-e1,e1+kap*(r1-e1),r2-e2,e2+kap*(r2-e2+G2),
                             r3-e3-S3,e3+kap*(r3-e3+G3-S3))
    return L**((-steps)%(4*s))*(r3+(L-1)/kap*e3)


def cubic_tests():
    samples=(12,16,20,24,28,36,40,60)
    cases=comp=0
    for p in samples:
        data=setup(p); K,L,s,kap,ip=data; I=L**s
        x=L**(p-1); H=sum(((-1)**j*x**(4*j) for j in range(s)),K.zero)
        need(H==K.convert(1-(-1)**s)/(1+x**4),'alternating geometric sum')
        need((H==K.zero)==(s%2==0),'alternating cancellation')
        # Compute the two path weights by direct summation, not closed forms.
        A=B=C=K.zero
        for j in range(s):
            for k in range(j+1,s):
                w=x**(3*j+k)-L**2*x**(j+3*k)
                A+=w; B+=(-1)**(j+k)*w; C+=((-1)**j+(-1)**k)*w
        r,c=B/A,C/A
        need(C!=K.zero and conj(K,r,p)==r,'nonzero mixed weight / real ratio')
        q0=L**5*(I*L**2+I-L**2+1)/(2*(L+1)**4*(L**2+L+1))
        chi_b=(L-1)*L**2*ip**3; kappa=kap/L
        need(kappa!=conj(K,kappa,p),'two real cubic directions')
        b,g=map(K.convert,(sp.Rational(1,6),-sp.Rational(1,6)))
        for a,d in ((sp.Rational(1,2),0),(sp.Rational(1,4),sp.Rational(1,4)),(0,sp.Rational(1,2))):
            aa,dd=map(K.convert,(a,d))
            for beta,delta in ((0,0),(sp.Rational(2,7),-sp.Rational(3,5))):
                bb,gg=map(K.convert,(beta,delta))
                for sign in (1,-1):
                    expected=4*q0*(aa*aa+r*dd*dd+sign*c*aa*dd)+sign*H*chi_b*(bb+kappa*gg)
                    need(raw3(data,aa,dd,b,g,bb,gg,sign,s)==expected,'raw alternating cubic')
                    cases+=1
        if s%2:
            # Rational parametrization of a^2+r*d^2=1/4 over K^+.
            t=K.convert(sp.Rational(1,3)); aa=(1-r*t*t)/(2*(1+r*t*t)); dd=t/(1+r*t*t)
            need(aa*aa+r*dd*dd==K.convert(sp.Rational(1,4)) and aa*dd!=K.zero,'mixed conic')
            target=-4*q0*c*aa*dd/(H*chi_b)
            delta=(target-conj(K,target,p))/(kappa-conj(K,kappa,p)); beta=target-kappa*delta
            need(conj(K,beta,p)==beta and conj(K,delta,p)==delta,'real compensator')
            need(H*chi_b*(beta+kappa*delta)!=K.zero,'nontrivial compensation')
        else:
            aa=K.convert(sp.Rational(1,2));dd=K.zero;beta=K.one;delta=K.one
        for sign in (1,-1):
            need(raw3(data,aa,dd,b,g,beta,delta,sign,s)==q0,'both-parity recovery')
            comp+=1
        print(f'P={p} CUBIC_PASS 12/12; RECOVERY_PASS 2/2',flush=True)
    print(f'RAW_CUBIC_PASS {cases}/{cases}; RECOVERY_PASS {comp}/{comp}')


def resonance_tests():
    count=0
    for p in range(12,257,4):
        q=p//2-1
        for k in range(2,q):
            need(all((2*u-k-1-p//2)%p!=0 for u in range(k+1)),'no lower odd homological kernel')
        need([u for u in range(q+1) if (2*u-q-1-p//2)%p==0]==[0],'first resonance')
        need(all((2*u-k-1-p//2)%p!=0 for k in range(2,q+1,2) for u in range(k+1)),
             'reflection completion even-degree nonresonance')
        count+=1
    print(f'FIRST_RESONANCE_PASS {count}/{count} (12<=p<=256, 4|p)')
    t=sp.Symbol('t'); count=0
    for p in range(12,257,4):
        s=p//4; M=sp.Poly(t**(2*s)+1,t,modulus=2); P=sp.Poly(sp.cyclotomic_poly(p,t),t,modulus=2)
        if s&(s-1):
            need(P.degree()<M.degree() and P.eval(1)%2==1 and P.rem(P).is_zero,'distinct parity witness')
            count+=1
    print(f'PRIMITIVE_COLLISION_OPPOSITE_PARITY_PASS {count}/{count}')


def mul(K,x,y,q):
    z=[K.zero]*(q+1)
    for j in range(1,q+1):
        if x[j]:
            for k in range(1,q-j+1):
                if y[k]: z[j+k]+=x[j]*y[k]
    return z


def nonlinear(K,x,q,sine):
    z=x.copy(); powx=x.copy()
    for k in range(2,q+1):
        powx=mul(K,powx,x,q)
        if not sine or k%2:
            c=K.convert(sp.Rational((-1)**((k-1)//2) if sine else 1,factorial(k)))
            z=[a+c*b for a,b in zip(z,powx)]
    return z


def raw_high(data,q,eps,sigma,steps):
    K,L,s,kap,ip=data
    r=[K.zero,L*ip]+[K.zero]*(q-1); e=[K.zero,(L-1)*ip]+[K.zero]*(q-1)
    for j in range(steps):
        G=nonlinear(K,r,q,False); S=nonlinear(K,e,q,True)
        G[q]+=eps*sigma*(-1)**j*r[1]**q
        r,e=[a-b for a,b in zip(r,S)],[a+kap*(b-c) for a,b,c in zip(e,G,S)]
    return [L**((-steps)%(4*s))*(a+(L-1)/kap*b) for a,b in zip(r,e)]


def high_tests():
    count=0
    for p in (12,16,20):
        data=setup(p);K,L,s,kap,ip=data;q=p//2-1
        eps=K.convert(sp.Rational(1,7)); kappa=(L-1)*L**(q-1)*ip**q
        for steps in (s,s+1):
            baseline=raw_high(data,q,K.zero,1,steps)
            for sign in (1,-1):
                out=raw_high(data,q,eps,sign,steps)
                need(out[:q]==baseline[:q],'unchanged lower jets')
                need(out[q]-baseline[q]==steps*sign*eps*kappa,'resonant drift')
                count+=1
        print(f'P={p} Q={q} HIGH_JET_PASS 4/4',flush=True)
    print(f'HIGH_JET_PASS {count}/{count}')


if __name__=='__main__':
    print('SymPy',sp.__version__,flush=True)
    cubic_tests();resonance_tests();high_tests()
    print('ALL_STAGE2B_CHECKS_PASS')
