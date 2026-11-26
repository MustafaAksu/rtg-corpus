#!/usr/bin/env python3
"""SESSION Stage 1: signed history algebra, affine-clock and parity obstructions.
Exact finite regressions for the accompanying written proofs; not a DYAD replay.
Python 3 / SymPy 1.14.0. No physical-mechanism inference.
"""
import sympy as sp


def need(ok, label):
    if not ok:
        raise AssertionError(label)


def shift(x, n, k=1):
    k %= n
    return ((x << k) | (x >> (n-k))) & ((1 << n)-1)


def fold(x, n, r):
    mask = (1 << r)-1
    y = 0
    for j in range(0, n, r):
        y ^= (x >> j) & mask
    return y


def xor_span_basis(xs):
    pivots = {}
    for x in xs:
        while x:
            k = x.bit_length()-1
            if k in pivots:
                x ^= pivots[k]
            else:
                pivots[k] = x
                break
    return pivots


def finite_registers():
    total = 0
    for s in range(1, 8):
        n = 2*s
        nmask, smask = (1 << n)-1, (1 << s)-1
        boundary, defects, centered = set(), set(), set()
        for x in range(1 << n):
            y = shift(x,n)^1
            # Exact signed integral lift tP+1 has binary coefficients.
            coeff = [1-((x>>(n-1))&1)]+[(x>>j)&1 for j in range(n-1)]
            need(sum(v<<j for j,v in enumerate(coeff))==y, 'integral lift')
            bx = fold(x,n,s)
            ys = shift(x,n,s)^smask
            need(fold(y,n,s)==(shift(bx,s)^1), 'fold equivariance')
            need(fold(ys,n,s)==(bx^smask), 'affine clock does not descend to identity')
            need((shift(ys,n,s)^smask)==(x^nmask), 'half turn complement')
            z = 1 ^ bx ^ shift(bx,s)
            by = fold(y,n,s)
            need((1^by^shift(by,s))==shift(z,s), 'centered covariance')
            need((1^fold(ys,n,s)^shift(fold(ys,n,s),s))==z, 'centered strobe invariance')
            boundary.add(x^shift(x,n,s))
            defects.add(x^ys)
            centered.add(z)
            need((x.bit_count()&1)==(bx.bit_count()&1), 'fold parity')
            total += 1
        need(boundary=={x|(x<<s) for x in range(1<<s)}, 'boundary image')
        need(len(xor_span_basis(defects))==s+1, 'affine defect span')
        need(all((d.bit_count()&1)==(s%2) for d in defects), 'defect parity')
        need(len(centered)==1<<(s-1), 'centered image size')
    print(f'FULL_REGISTER_PASS s=1..7; {total} states; affine/linear quotient separation')


def monomial(n,k):
    k %= 2*n
    a = [0]*n
    a[k%n] = 1 if k<n else -1
    return a


def add(a,b):
    return [x+y for x,y in zip(a,b)]


def sub(a,b):
    return [x-y for x,y in zip(a,b)]


def mul(a,b):
    n=len(a); z=[0]*n
    for j,x in enumerate(a):
        if x:
            for k,y in enumerate(b):
                if y:
                    i=j+k
                    z[i%n] += x*y*(1 if i<n else -1)
    return z


def G(n,s,k):
    z=[0]*n
    for j in range(s):
        z=add(z,monomial(n,k*j))
    return z


def S(n,s,u,v):
    prefix=[0]*n; z=[0]*n
    for j in range(s):
        z=add(z,mul(prefix,monomial(n,v*j)))
        prefix=add(prefix,monomial(n,u*j))
    return z


def signed_lattice():
    paths=charges=layers=0
    t=sp.Symbol('t')
    for s in range(1,65):
        n=2*s; one=monomial(n,0); d=sub(one,monomial(n,s))
        need(mul(d,d)==[-2*x for x in monomial(n,s)], 'boundary square')
        for k in range(-4,5):
            need(mul(sub(one,monomial(n,k)),G(n,s,k))==sub(one,monomial(n,s*k)),
                 'geometric boundary')
            charges+=1
        g=G(n,s,-4)
        need((not any(g))==(s%2==0), 'full lattice cubic cancellation')
        # Evaluate the signed polynomial at i for odd s (valid ring map then).
        if s%2:
            real = sum(x * (1,0,-1,0)[j%4] for j,x in enumerate(g))
            imag = sum(x * (0,1,0,-1)[j%4] for j,x in enumerate(g))
            need((real,imag)==(s,0), 'Phi4 survivor')
        for u,v in ((-3,-1),(-1,-3)):
            D=mul(sub(one,monomial(n,u)),sub(one,monomial(n,v)))
            left=mul(D,S(n,s,u,v))
            boundary=sub(one,monomial(n,s*v))
            right=sub(boundary,mul(sub(one,monomial(n,v)),g))
            need(left==right, 'ordered boundary identity')
            need((left==boundary)==(s%2==0), 'lower-sector correction')
            # Linear folding of boundary-cleared path sums still vanishes mod 2.
            need(all((left[j]+left[j+s])%2==0 for j in range(s)), 'path in fold ideal')
            # Check the entire multiplication image, not just containment.
            poly=sp.Poly.from_list(list(reversed(left)),gens=t,modulus=2)
            modulus=sp.Poly(t**n+1,t,modulus=2)
            expected=sp.Poly(t**s+1,t,modulus=2)*sp.Poly(t+1 if s%2 else 1,t,modulus=2)
            need(sp.gcd(modulus,poly)==expected,'full-register path image')
            layers+=1
            paths+=1
    print(f'SIGNED_LATTICE_PASS s=1..64; {charges} charge and {paths} ordered-sum checks')
    print(f'FULL_REGISTER_PATH_IMAGE_PASS {layers}/{layers}; odd-s misses doubled odd-weight block')


def spectral_quotients():
    t=sp.Symbol('t'); count=0; powers=0; other=0; odd_s=0
    for s in range(1,65):
        p=4*s
        C=sp.Poly(sp.cyclotomic_poly(p,t),t,modulus=2)
        H=sp.Poly(sp.cyclotomic_poly(p//2,t),t,modulus=2)
        d=sp.Poly(t**s+1,t,modulus=2)
        G1=sp.Poly(sum(t**j for j in range(s)),t,modulus=2)
        need(C==H**2 and sp.gcd(C,d)==H, 'Gaussian quotient')
        is_power=(s&(s-1))==0
        need(G1.rem(H).is_zero==(not is_power), 'affine defect in Gaussian layer')
        need(sp.gcd(C,G1)==(H.exquo(sp.Poly(t+1,t,modulus=2)) if is_power else H),
             'spectral affine coequalizer')
        need((sp.gcd(C,sp.Poly(t+1,t,modulus=2)).degree()>0)==is_power,
             'phase parity')
        # Integer primitive cancellation for p>=8, full polynomial failure for s odd.
        if s>=2:
            P=sp.Poly(sp.cyclotomic_poly(p,t),t,domain=sp.ZZ)
            poly=sp.Poly(sum(t**((-4*j)%p) for j in range(s)),t,domain=sp.ZZ)
            need(poly.rem(P).is_zero,'primitive charge -4 cancellation')
        # Odd-s full mod-2 charge sum has augmentation 1, cannot vanish through parity.
        if s%2:
            need(sum(1 for _ in range(s))%2==1,'odd-s parity obstruction')
            odd_s+=1
        powers+=int(is_power);other+=int(not is_power);count+=1
    print(f'SPECTRAL_AFFINE_QUOTIENT_PASS {count}/{count}; power-of-two={powers}; other={other}; odd-s={odd_s}')


if __name__=='__main__':
    print('SymPy',sp.__version__)
    finite_registers()
    signed_lattice()
    spectral_quotients()
    print('ALL_STAGE1_CHECKS_PASS')
