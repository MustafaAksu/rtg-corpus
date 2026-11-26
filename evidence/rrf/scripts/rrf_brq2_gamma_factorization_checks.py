#!/usr/bin/env python3
"""BR-Q2: finite exact checks of the register Gamma factorization theorem.
Requires SymPy for cyclotomic polynomials. Integer coefficient arithmetic only.
Positive small-n cases exhaust ordered pairs; negative cases stop at a witness.
Unbounded statements are proved in the SESSION record, not by this script.
"""
from itertools import product
import sympy as sp

t = sp.symbols("t")


def model(n):
    poly = sp.Poly(sp.cyclotomic_poly(2*n, t), t)
    m = poly.degree()
    mod = [int(poly.nth(i)) for i in range(m)]

    def reduce(v):
        v = list(v) + [0]*max(0, m-len(v))
        for k in range(len(v)-1, m-1, -1):
            a = v[k]
            if a:
                for j, b in enumerate(mod):
                    if b:
                        v[k-m+j] -= a*b
        return tuple(v[:m])

    powers = [reduce([0]*j+[1]) for j in range(2*n)]
    one = powers[0]
    zero = (0,)*m

    def mul(a, b):
        v = [0]*(2*m-1)
        for i, u in enumerate(a):
            if u:
                for j, w in enumerate(b):
                    if w:
                        v[i+j] += u*w
        return reduce(v)

    def conj(a):
        return tuple(sum(a[j]*powers[(-j)%(2*n)][i] for j in range(m)) for i in range(m))

    def z(x):
        return tuple(one[i] + sum(x[j]*(powers[(j+1)%(2*n)][i]-powers[j][i]) for j in range(n))
                     for i in range(m))

    def power(a, k):
        v = one
        for _ in range(k):
            v = mul(v, a)
        return v

    return zero, one, mul, conj, z, power


def r(x):
    return (-1)**sum(x)


def F(x):
    return (1-x[-1],)+x[:-1]


def bits(n, indices):
    return tuple(int(j in indices) for j in range(n))


def is_dyadic(n):
    return n & (n-1) == 0


def check_small():
    print("n nonzero_states checked_pairs result")
    for n in range(1, 10):
        zero, one, mul, cj, z, power = model(n)
        nz = [(x, z(x), r(x)) for x in product((0,1), repeat=n) if z(x) != zero]
        seen = {}
        witness = None
        checked = 0
        for x, a, s in nz:
            for y, b, u in nz:
                G = mul(cj(a), b)
                P = s*u
                checked += 1
                if G in seen and seen[G][0] != P:
                    witness = (seen[G], (P,x,y), G)
                    break
                seen.setdefault(G, (P,x,y))
            if witness:
                break
        expected = is_dyadic(n) or n == 3
        assert (witness is None) == expected
        if expected:
            assert checked == len(nz)**2
        print(n, len(nz), checked, "FACTOR" if expected else "COLLISION", witness or "")
    print("PASS exact pair tests n=1..9")


def check_constructive():
    for n in range(1,33):
        zero, one, mul, cj, z, power = model(n)
        X0 = (0,)*n
        if is_dyadic(n):
            # Sample exact dual-number decoder tests; proof covers the full cube.
            states = [X0, (1,)*n, tuple(j%2 for j in range(n))]
            states += [bits(n, {j}) for j in range(n)]
            states += [bits(n, {0,j}) for j in range(1,n)]
            for x in states:
                assert z(x) != zero
                for y in states:
                    G = mul(cj(z(x)),z(y))
                    if n == 1:
                        assert G == (r(x)*r(y),)
                    else:
                        assert sum(G)%2 == 1
                        assert (-1)**(sum(j*v for j,v in enumerate(G))%2) == r(x)*r(y)
        else:
            p = next(j for j in range(3,n+1,2) if n%j == 0)
            d = n//p
            # Zero fibre contains opposite recognition signs.
            x = tuple(int((j//d)%2==0) for j in range(n))
            assert z(x) == z(F(x)) == zero and r(F(x)) == -r(x)
            if d > 1:
                # Equal, nonzero Z values but opposite signs.
                x = bits(n, {j*d for j in range(0,p,2)})
                y = bits(n, {j*d for j in range(1,p,2)})
                assert z(x) == z(y) != zero and r(x) == -r(y)
            elif n >= 5:
                # Prime case: subset-product collision.
                ell = (n+1)//2
                def subset(S):
                    return tuple(int(((ell*j)%n in S) == (j%2==0)) for j in range(n))
                x,y = subset({0,n-1}),subset({0,2})
                u,v = subset({0}),subset({0,1,2,3})
                assert all(z(w) != zero for w in (x,y,u,v))
                assert mul(cj(z(x)),z(y)) == mul(cj(z(u)),z(v))
                assert r(x)*r(y) == -r(u)*r(v)
        if n <= 4:
            for x in product((0,1),repeat=n):
                a = z(x)
                if a == zero:
                    continue
                norm = mul(cj(a),a)
                if n%2 == 1:
                    assert norm == one
                    rhs = one
                else:
                    rhs = power(norm,n//2)
                assert power(a,n) == tuple(r(x)*v for v in rhs)
        elif n >= 6:
            a = power(z(bits(n,{2})),n)
            assert a != cj(a)  # exact failure of the simple phase-power identity
    print("PASS constructive witnesses / sampled exact decoder / phase controls n=1..32")
    print("n=5 phase counterexample sign uses the analytic proof in the record")
    x = (1,0,0,0)
    assert r(F(x)) != r(x)
    assert (-r(F(x))) == r(x)  # injected wrong successor label violates alternation
    print("PASS perturbed-sign negative control")


if __name__ == "__main__":
    print("SymPy", sp.__version__)
    check_small()
    check_constructive()
