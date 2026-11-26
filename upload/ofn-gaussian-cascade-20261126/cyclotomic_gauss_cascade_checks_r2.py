#!/usr/bin/env python3
"""SESSION r2: cubic cascade and Gaussian quotient, independent exact checks.
Sources: dyad-v6.4.24 §§6.9, 6.11; dzt-v0.19 §6.3; Binary Recognition
wrap-up §2, merge 1da597feb194837f56ad5d632c3ddd36c9f80abc.
Not a replay of the owner extractor or a physics certificate.
Requires Python 3 and SymPy 1.14. See written proof for all-p claims.
"""
import sympy as sp
from sympy import QQ

SAMPLES = (8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 72)
NEGATIVE = (8, 12, 20, 28, 40)


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def symbolic_paths():
    L, a, b, g, W, V = sp.symbols('L a b g W V')
    K = 2-L-1/L
    rho = (W+L*V)/(1+L)
    eta = (L-1)*(V-W)/(1+L)
    require(sp.cancel(rho-eta+(L-1)/K*(eta+K*(rho-eta))-L*W)==0, 'linear frame')
    A = a*(L-1)/(L*(1+L)**2)
    B, C = 2*L*A, L**2*A
    require(sp.cancel(a*(L-1)/L*rho**2-(A*W**2+B*W*V+C*V**2))==0, 'quadratic jet')
    h3 = (-g*eta**3+(L-1)*(b*rho**3-g*eta**3))/L
    direct = sp.cancel(h3.subs({W:0,V:1}))
    require(direct.has(b) and direct.has(g), 'independent direct cubic coefficients')
    Abar = A.subs(L,1/L)
    require(sp.cancel(2*C*Abar+L**2*B*C)==0, 'two path ratio')
    # Written proof: (1-L**u) S(u,v)=G(v)-G(u+v),
    # (1-L**k) G(k)=1-I**k, I=L**s=i. Derive rather than input the weights.
    def G(k):
        return (1-sp.I**k)/(1-L**k)
    def S(u,v):
        return sp.cancel((G(v)-G(u+v))/(1-L**u))
    require(sp.cancel(G(-4))==0, 'direct cubic cancellation')
    D = (1-1/L)*(1-1/L**3)
    S31, S13 = S(-3,-1), S(-1,-3)
    require(sp.cancel(D*S31-(1+sp.I))==0, 'ordered sum -3,-1')
    require(sp.cancel(D*S13-(1-sp.I))==0, 'ordered sum -1,-3')
    path = B*C*S31 + 2*C*Abar*S13
    target = 2*a**2*L**5*(sp.I*L**2+sp.I-L**2+1)/((L+1)**4*(L**2+L+1))
    require(sp.cancel(path-target)==0, 'all-p symbolic path identity')
    require(sp.expand((1+sp.I)*(1+sp.I*L**2)-(sp.I*L**2+sp.I-L**2+1))==0,
            'common Gaussian factor')
    print('SYMBOLIC_PATH_IDENTITY_PASS (derived weights; common Gaussian factor)')


def field_setup(p):
    K=QQ.cyclotomic_field(p); L=K.unit; s=p//4; I=L**s
    require(I**2==-K.one, 'quarter-turn')
    kap=2-L-L**(p-1)
    inv_plus=(1+L)**(-1)
    wcoef=(L-1)/kap
    return K,L,s,I,kap,inv_plus,wcoef


def raw_cubic(data,a,b,g,steps):
    """Direct real-coordinate jet iteration at W=0, Wbar=t. No normalizer.
    Explicit homogeneous recurrences are exact through degree 3.
    """
    K,L,s,I,kap,inv_plus,wcoef=data
    r1=L*inv_plus; e1=(L-1)*inv_plus
    r2=e2=r3=e3=K.zero
    for _ in range(steps):
        G2=a*r1*r1
        G3=2*a*r1*r2+b*r1*r1*r1
        S3=g*e1*e1*e1
        r1,e1,r2,e2,r3,e3=(r1-e1, e1+kap*(r1-e1),
                            r2-e2, e2+kap*(r2-e2+G2),
                            r3-e3-S3, e3+kap*(r3-e3+G3-S3))
    return L**((-steps)%(4*s))*(r3+wcoef*e3)


def exact_tests():
    a_vals=(0,sp.Rational(1,4),sp.Rational(1,2),1,sp.Rational(-3,2))
    cubics=((sp.Rational(1,6),sp.Rational(-1,6)),(0,0),
            (sp.Rational(7,5),sp.Rational(-3,7)),(-2,5))
    count=ordered=neg=0
    for p in SAMPLES:
        data=field_setup(p); K,L,s,I,kap,inv_plus,wcoef=data
        q0=L**5*(I*L**2+I-L**2+1)/(2*(L+1)**4*(L**2+L+1))
        require(q0==K.zero if p==8 else q0!=K.zero,'zero degeneracy')
        powers=[L**((-j)%p) for j in range(s)]
        require(sum((x**4 for x in powers),K.zero)==K.zero,f'G(-4) p={p}')
        den=(1-L**(p-1))*(1-L**(p-3))
        for u,v,expected in ((3,1,1+I),(1,3,1-I)):
            prefix=actual=K.zero
            for x in powers:
                actual+=prefix*x**v
                prefix+=x**u
            require(den*actual==expected,f'ordered sum p={p} u={u} v={v}')
            ordered+=1
        for a in a_vals:
            for b,g in cubics:
                aa,bb,gg=map(K.convert,(a,b,g))
                require(raw_cubic(data,aa,bb,gg,s)==4*aa**2*q0,
                        f'raw p={p} a={a} b={b} g={g}')
                count+=1
        if p in NEGATIVE:
            for b,g in ((K.one,K.zero),(K.zero,K.one)):
                require(raw_cubic(data,K.zero,b,g,s+1)!=K.zero,
                        f'changed clock negative control p={p}')
                neg+=1
        print(f'RAW_JET_PASS p={p} (20 exact cases); ORDERED_SUM_PASS (2 cases)')
    print(f'RAW_CUBIC_INDEPENDENCE_PASS {count}/{count}')
    print(f'EXACT_ORDERED_SUM_PASS {ordered}/{ordered}')
    print(f'CHANGED_CLOCK_NEGATIVE_CONTROLS_PASS {neg}/{neg} (steps=s+1)')


def gaussian_quotient_tests():
    t=sp.Symbol('t'); count=0
    for p in range(4,257,4):
        s=p//4
        P=sp.Poly(sp.cyclotomic_poly(p,t),t,modulus=2)
        H=sp.Poly(sp.cyclotomic_poly(p//2,t),t,modulus=2)
        S=sp.Poly(t**s+1,t,modulus=2)
        require(P==H**2,f'Phi reduction p={p}')
        require(sp.gcd(P,S)==H,f'Gaussian quotient p={p}')
        require(H.degree()==P.degree()//2,f'half rank p={p}')
        require((sp.Poly(t**s,t,modulus=2)-1).rem(H).is_zero,f'folding p={p}')
        require(S.rem(H).is_zero and sp.gcd(S.exquo(H),H).degree()==0,
                f'Gaussian layer generator p={p}')
        # Natural inclusion induces t -> t**2 (Frobenius), not t -> t.
        require((sp.gcd(H,H.diff()).degree()==0)==(p%8!=0),
                f'Frobenius bijectivity p={p}')
        count+=1
    print(f'GAUSSIAN_QUOTIENT_POLYNOMIAL_PASS {count}/{count} (4<=p<=256, 4|p)')


if __name__=='__main__':
    print('SymPy', sp.__version__)
    symbolic_paths()
    exact_tests()
    gaussian_quotient_tests()
    print('ALL_CHECKS_PASS')
