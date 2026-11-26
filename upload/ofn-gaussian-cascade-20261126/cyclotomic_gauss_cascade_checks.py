#!/usr/bin/env python3
"""SESSION: exact checks of cubic cascade scaling and the Gaussian register quotient.
Sources: dyad-v6.4.24, §§6.9, 6.11; dzt-v0.19, §6.3;
Binary Recognition wrap-up §2, merge 1da597feb194837f56ad5d632c3ddd36c9f80abc.
Independent implementation, not a replay of the owner extractor or a physics certificate.
Requires Python 3 and SymPy 1.14 (QQ.cyclotomic_field).
"""
import sympy as sp
from sympy import QQ


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def symbolic_paths():
    L, a, b, g = sp.symbols('L a b g')
    W, V = sp.symbols('W V')  # independent formal complex coordinate and conjugate
    K = 2-L-1/L
    rho = (W+L*V)/(1+L)
    eta = (L-1)*(V-W)/(1+L)  # solves W=rho+(L-1)/K*eta
    # Independently derive the linear, quadratic and cubic parts in raw W.
    r1 = rho-eta
    e1 = eta+K*(rho-eta)
    require(sp.cancel(r1+(L-1)/K*e1-L*W)==0, 'linear frame')
    A = a*(L-1)/(L*(1+L)**2)
    B, C = 2*L*A, L**2*A
    h2 = a*(L-1)/L*rho**2
    require(sp.cancel(h2-(A*W**2+B*W*V+C*V**2))==0, 'quadratic jet')
    h3 = (-g*eta**3+(L-1)*(b*rho**3-g*eta**3))/L
    # The direct (0,3) coefficient is arbitrary, and is multiplied by sum L^(-4j)=0.
    direct = sp.cancel(h3.subs({W:0,V:1}))
    require(direct.has(b) and direct.has(g), 'independent direct cubic coefficients')
    Abar = A.subs(L,1/L)
    require(sp.cancel(2*C*Abar+L**2*B*C)==0, 'two path ratio')
    # Ordered sums S(u,v)=(G(v)-G(u+v))/(1-L**u).
    # G(-4)=0, L**s=i at p=4s>=8. Hence the two surviving sums:
    D = (1-1/L)*(1-1/L**3)
    path = B*C*(1+sp.I)/D + 2*C*Abar*(1-sp.I)/D
    target = 2*a**2*L**5*(sp.I*L**2+sp.I-L**2+1)/((L+1)**4*(L**2+L+1))
    require(sp.cancel(path-target)==0, 'all-p symbolic path identity')
    print('SYMBOLIC_PATH_IDENTITY_PASS (direct cubic weight -4, two ordered quadratic paths)')


def mul(x,y,K):
    return [sum((x[j]*y[k-j] for j in range(k+1)), K.zero) for k in range(4)]


def raw_cubic(K,L,a,b,g,steps):
    """Iterate the real coordinate jet after formal W=0, Wbar=t substitution.
    g is the cubic coefficient in sin-like eta+g*eta^3.  Truncation is exact
    for extracting the degree-3 coefficient; no normal-form transformation.
    """
    kap = 2-L-L**(-1)
    r=[K.zero,L/(1+L),K.zero,K.zero]
    e=[K.zero,(L-1)/(L+1),K.zero,K.zero]
    for _ in range(steps):
        r2=mul(r,r,K); r3=mul(r2,r,K); e3=mul(mul(e,e,K),e,K)
        G=[r[j]+a*r2[j]+b*r3[j] for j in range(4)]
        S=[e[j]+g*e3[j] for j in range(4)]
        r,e=[r[j]-S[j] for j in range(4)],[e[j]+kap*(G[j]-S[j]) for j in range(4)]
    return L**(-steps)*(r[3]+(L-1)/kap*e[3])


def exact_raw_tests():
    samples=(8,12,16,24,32,40,72)
    a_vals=(0,sp.Rational(1,4),sp.Rational(1,2),1,sp.Rational(-3,2))
    cubics=((sp.Rational(1,6),sp.Rational(-1,6)),(0,0),
            (sp.Rational(7,5),sp.Rational(-3,7)),(-2,5))
    count=0
    for p in samples:
        K=QQ.cyclotomic_field(p); L=K.unit; s=p//4; I=L**s
        require(I**2==-K.one,'quarter-turn')
        q0=L**5*(I*L**2+I-L**2+1)/(2*(L+1)**4*(L**2+L+1))
        require(q0==K.zero if p==8 else q0!=K.zero,'zero degeneracy')
        for a in a_vals:
            for b,g in cubics:
                aa,bb,gg=map(K.convert,(a,b,g))
                actual=raw_cubic(K,L,aa,bb,gg,s)
                require(actual==4*aa**2*q0, f'raw p={p}, a={a}, b={b}, g={g}')
                count+=1
        print(f'RAW_JET_PASS p={p} ({len(a_vals)*len(cubics)} exact cases)')
    # Negative control: with a changed strobe the direct cubic term need not cancel.
    K=QQ.cyclotomic_field(12); L=K.unit
    require(raw_cubic(K,L,K.zero,K.one,K.zero,4)!=K.zero,'changed clock negative control')
    print(f'RAW_CUBIC_INDEPENDENCE_PASS {count}/{count}; changed-clock negative control PASS')


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
        count+=1
    print(f'GAUSSIAN_QUOTIENT_POLYNOMIAL_PASS {count}/{count} (4<=p<=256, 4|p)')


if __name__=='__main__':
    print('SymPy', sp.__version__)
    symbolic_paths()
    exact_raw_tests()
    gaussian_quotient_tests()
    print('ALL_CHECKS_PASS')
