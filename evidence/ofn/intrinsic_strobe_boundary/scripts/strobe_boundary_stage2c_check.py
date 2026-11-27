#!/usr/bin/env python3
"""Stage 2C SESSION: exact finite controls, not an owner certificate replay."""
from math import factorial, gcd
import sympy as sp
from sympy import QQ


def need(ok, label):
    if not ok:
        raise AssertionError(label)


def registers():
    total = 0
    for n in range(2, 15, 2):
        h = n & -n
        m = n // h
        mask = (1 << n) - 1
        def F(x):
            return ((x << 1) & mask) | (1 ^ (x >> (n-1)))
        seen = set()
        lengths = set()
        for x in range(1 << n):
            y = x
            for _ in range(n):
                y = F(y)
            need(y == x ^ mask, 'complement identity')
            total += 1
            if x in seen:
                continue
            o = [x]
            y = F(x)
            while y != x:
                o.append(y)
                y = F(y)
            d = len(o)
            need(d % (2*h) == 0 and m % (d//(2*h)) == 0, 'period')
            need(o[d//2] == x ^ mask, 'quotient period')
            need(all((o[j].bit_count() ^ o[(j+1)%d].bit_count()) & 1
                     for j in range(d)), 'parity alternation')
            seen.update(o)
            lengths.add(d)
        need(min(lengths) == 2*h, 'shortest orbit')
    print(f'REGISTER_PASS n=2,4,...,14; {total} states; shortest orbit and complement quotient')


def symbolic_cubic():
    L = sp.symbols('L', nonzero=True)
    c = (L+1/L)/2
    f = -(L**5-L**4-L**3-2*L**2+1)/(2*L*(L-1)*(L+1)*(L**2+L+1))
    fc = f.subs(L, 1/L)
    need(sp.cancel(f+fc-(c-1)) == 0, 'real part')
    need(sp.cancel((f-fc)*(L-1/L)+2*(2*c**3+c**2-3*c-1)/(1+2*c)) == 0,
         'imaginary part')
    print('CUBIC_SYMBOLIC_PARTS_PASS (RECOG Z frame; positive W scale)')


def linear_controls():
    count = 0
    for p in range(12, 257, 4):
        n = p//2
        h = n & -n
        m = n//h
        q = n-1
        a = pow(2*h, -1, m) if m > 1 else 0
        b = (1-2*h*a)//m
        need(2*h*a+m*b == 1, 'Bezout')
        j = 2*h*a
        need((2*h*j-2*h)%p == 0 and gcd(j,p) == p//m, 'root multiplier')
        roots = [j for j in range(p) if (h*j-h)%p == 0]
        need(len(roots) == h and all((n*j)%p == n for j in roots), 'complement roots')
        need(all((n*j)%p == n for j in (1,p-1)), 'owner rotations')
        need(all((2*u-(q-2)-1)%p != n for u in range(q-1)), 'lower bracket charge')
        count += 1
    print(f'ROOT_MULTIPLIER_PASS {count}/{count}; complement and owner-linear obstructions')


def mul(K, a, b, q):
    out = [K.zero]*(q+1)
    for i in range(1,q+1):
        if a[i]:
            for j in range(1,q-i+1):
                if b[j]:
                    out[i+j] += a[i]*b[j]
    return out


def analytic_jet(K, x, q, sine):
    result = x.copy()
    power = x.copy()
    for k in range(2,q+1):
        power = mul(K,power,x,q)
        if not sine or k%2:
            c = K.convert(sp.Rational((-1)**((k-1)//2) if sine else 1,factorial(k)))
            for j in range(k,q+1):
                result[j] += c*power[j]
    return result


def trace(K,L,p,q,u,v,eps,sigma,targets):
    kap = 2-L-L**(p-1)
    inv = (1+L)**(-1)
    r = [K.zero,(u+L*v)*inv]+[K.zero]*(q-1)
    e = [K.zero,(L-1)*(v-u)*inv]+[K.zero]*(q-1)
    out = {}
    for step in range(1,max(targets)+1):
        G = analytic_jet(K,r,q,False)
        S = analytic_jet(K,e,q,True)
        G[q] += eps*sigma*(-1)**(step-1)*r[1]**q
        r,e = ([a-b for a,b in zip(r,S)], [a+kap*(b-c) for a,b,c in zip(e,G,S)])
        if step in targets:
            out[step] = [L**((-step)%p)*(a+(L-1)/kap*b) for a,b in zip(r,e)]
    return out


def raw_controls():
    for p in (12,16,20,24):
        K = QQ.cyclotomic_field(p)
        L = K.unit
        n = p//2
        h = n & -n
        q = n-1
        s = p//4
        eps = K.convert(sp.Rational(1,7))
        kappa = (L-1)*L**(q-1)/(1+L)**q
        targets = {2,h,2*h,s,p}
        base = trace(K,L,p,q,K.zero,K.one,K.zero,1,targets)
        for sign in (1,-1):
            gated = trace(K,L,p,q,K.zero,K.one,eps,sign,targets)
            for ell in targets:
                need(gated[ell][:q] == base[ell][:q], 'pure V lower jets')
                need(gated[ell][q]-base[ell][q] == ell*sign*eps*kappa,'pure V drift')
        cubic = trace(K,L,p,3,K.one,K.one,K.zero,1,{p})[p]
        f = -(L**5-L**4-L**3-2*L**2+1)/(2*L*(L-1)*(L+1)*(L**2+L+1))
        mu = p*f*(-(L-1)**2/(L+1)**2)
        need(cubic[2] == K.zero and cubic[3] == mu,'owner cubic in W frame')
        if p == 12:
            for v_int in range(q+1):
                v = K.convert(v_int)
                base_line = trace(K,L,p,q,K.one,v,K.zero,1,{p})[p]
                gate_line = trace(K,L,p,q,K.one,v,eps,1,{p})[p]
                need(gate_line[:q] == base_line[:q], 'full lower jet lines')
                need(gate_line[q]-base_line[q] == p*eps*kappa*v**q, 'full q-jet lines')
        print(f'P={p} Q={q} PURE_V_PASS {2*len(targets)}/{2*len(targets)}; CUBIC_W_PASS',flush=True)
    print('P=12 FULL_HOMOGENEOUS_CONTRAST_PASS 6/6 lines')


if __name__ == '__main__':
    print('SymPy',sp.__version__,flush=True)
    registers()
    symbolic_cubic()
    linear_controls()
    raw_controls()
    print('ALL_STAGE2C_CHECKS_PASS')
