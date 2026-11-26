#!/usr/bin/env python3
"""RRF BR-Q2 reviewer checks (Claude, independent derivation; SESSION).

Model (records/ofn/NODE_BINARY_RECOGNITION_WRAPUP.md §2): X_n={0,1}^n,
F_n(x0..x_{n-1})=(1-x_{n-1},x0..x_{n-2}), C_n X=1-X, pi_n=XOR, r_n=(-1)^pi_n,
lambda=e^{i pi/n}, Z_n(X)=1-(1-lambda)P_X(lambda).  Exact arithmetic: Z_n is handled as an integer
vector in Z[t]/Phi_{2n}(t) (stdlib only) for equality tests; floating values only for phases with an
explicit tolerance check.

Checks (exit 0 iff all pass):
 T1  r(FX)=-r(X), r(CX)=(-1)^n r(X); at odd n r(CX)!=r(X)^{-1} (not C_- typed).
 T2  transport kernel: for (a,b) in Z_{2n}^2, r(F^aX)r(F^bY)=r(X)r(Y) for all X,Y  <=>  a=b mod 2.
 T3  orbit label: on X^x={Z!=0}, c(X)=r(X)/u(X)^n (u=Z/|Z|) is constant on <F_n>-orbits, |c|=1.
 T4  bridge identity: r(X)r(Y) = conj(c(X)) c(Y) (Gamma/|Gamma|)^n, Gamma=conj(Z_X)Z_Y, all X,Y in X^x;
     same orbit: r(X)r(Y) = (Gamma/|Gamma|)^n.
 T5  no label-free bridge: count pairs (X,Y),(X',Y') in X^x with Gamma equal (exact, in Z[lambda])
     but r-products different; also report whether c is real-valued.
 T6  zero fibre: if Zero(n) nonempty, Gamma=0 carries both product values (no extension).
 T7  label constancy: c takes a single value (=1) on X^x, i.e. r(X)r(Y)=(Gamma/|Gamma|)^n globally;
     reported for n<=12 (finite census, not a general claim).
 T8  n=3 linear hexagon (wrap-up §3B map B): (-1)^pi_3=-W^3 and r(X)r(Y)=(conj(W_X)W_Y)^3 on the 6-cycle.
Negative control: a perturbed sign (r flipped on one state) must fail T1 or T4.
"""
import cmath, itertools, sys
# ---- exact integer polynomial arithmetic (coefficient lists, low degree first) ----
def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i + j] += x * y
    return out
def pdivmod(a, b):  # b monic
    a = a[:]; q = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        k = len(a) - len(b); c = a[-1]; q[k] = c
        for i, y in enumerate(b): a[i + k] -= c * y
        while a and a[-1] == 0: a.pop()
    return q, a
_cyc = {}
def cyclo(m):
    if m in _cyc: return _cyc[m]
    num = [-1] + [0] * (m - 1) + [1]
    for d in range(1, m):
        if m % d == 0:
            num, rr = pdivmod(num, cyclo(d)); assert not any(rr)
    while num and num[-1] == 0: num.pop()
    _cyc[m] = num; return num
def prem(a, phi):
    _, rr = pdivmod(a, phi); rr = rr + [0] * (len(phi) - 1 - len(rr)); return tuple(rr)
TOL = 1e-9
def F(x):  return (1 - x[-1],) + x[:-1]
def C(x):  return tuple(1 - v for v in x)
def r(x):  return -1 if sum(x) % 2 else 1
def Zc(x, lam): return 1 - (1 - lam) * sum(v * lam**j for j, v in enumerate(x))
def exact_key(x, n, phi):
    # Z_n(X) = 1-(1-t)P_X(t) mod Phi_{2n}; exact integer coefficient tuple (low degree first)
    P = list(x) if x else [0]
    a = [1] + [0] * len(P)
    for i, v in enumerate(pmul([1, -1], P)): a[i] -= v
    return prem(a, phi)
fails = []
def check(name, ok, info=""):
    print(("PASS " if ok else "FAIL ") + name + (" " + info if info else ""))
    if not ok: fails.append(name)
def run(n, pairs_exhaustive, rfun=r):
    lam = cmath.exp(1j * cmath.pi / n); phi = cyclo(2 * n)
    X = list(itertools.product((0, 1), repeat=n))
    ok1 = all(rfun(F(x)) == -rfun(x) and rfun(C(x)) == (-1) ** n * rfun(x) for x in X)
    notCminus = (n % 2 == 0) or all(rfun(C(x)) != 1 / rfun(x) for x in X)
    # orbits and powers
    def Fp(x, a):
        for _ in range(a % (2 * n)): x = F(x)
        return x
    ok2 = True
    for a in range(2 * n):
        for b in range(2 * n):
            inv = all(rfun(Fp(x, a)) * rfun(Fp(y, b)) == rfun(x) * rfun(y) for x in X[:min(len(X), 16)] for y in X[:min(len(X), 16)])
            if inv != ((a - b) % 2 == 0): ok2 = False
    key = {x: exact_key(x, n, phi) for x in X}
    zero = tuple([0])
    Xx = [x for x in X if any(key[x]) ]
    Z = {x: Zc(x, lam) for x in Xx}
    u = {x: Z[x] / abs(Z[x]) for x in Xx}
    c = {x: rfun(x) / u[x] ** n for x in Xx}
    orbit = {}
    for x in X:
        if x in orbit: continue
        o, y = [], x
        while y not in o: o.append(y); y = F(y)
        for y in o: orbit[y] = min(o)
    ok3 = all(abs(abs(c[x]) - 1) < TOL and abs(c[F(x)] - c[x]) < TOL for x in Xx)
    S = Xx if pairs_exhaustive else Xx[:64]
    ok4 = True; ok4s = True
    for x in S:
        for y in S:
            g = Z[x].conjugate() * Z[y]; gn = (g / abs(g)) ** n
            if abs(rfun(x) * rfun(y) - c[x].conjugate() * c[y] * gn) > 1e-7: ok4 = False
            if orbit[x] == orbit[y] and abs(rfun(x) * rfun(y) - gn) > 1e-7: ok4s = False
    # T5 exact Gamma equality: Gamma = conj(Z_X) Z_Y; conj(lambda)=lambda^{-1}=-lambda^{n-1}; use exact via sympy on keys
    # complex conjugation on Z[lambda]: lambda -> lambda^{-1} = lambda^{2n-1}
    def conj_key(kx):
        a = [0] * (2 * n * max(1, len(kx)))
        for i, cf in enumerate(kx): a[(-i) % (2 * n)] += cf
        return prem(a, phi)
    gam = {}
    clash = 0; real_c = all(abs(c[x].imag) < TOL for x in Xx)
    if pairs_exhaustive:
        ck = {x: list(conj_key(key[x])) for x in Xx}
        for x in Xx:
            for y in Xx:
                gk = prem(pmul(ck[x], list(key[y])), phi)
                pr = rfun(x) * rfun(y)
                if gk in gam and gam[gk] != pr: clash += 1
                gam.setdefault(gk, pr)
    zf = [x for x in X if not any(key[x])]
    zero_both = len(zf) > 0 and len({rfun(x) * rfun(y) for x in zf for y in X}) == 2
    return ok1, notCminus, ok2, ok3, ok4, ok4s, clash, real_c, len(zf), zero_both
for n in range(1, 11):
    ex = n <= 9
    ok1, ncm, ok2, ok3, ok4, ok4s, clash, real_c, nz, zb = run(n, ex)
    check(f"n={n} T1 type law", ok1); check(f"n={n} T1 not C_- typed (odd n)", ncm)
    check(f"n={n} T2 kernel a=b mod 2", ok2); check(f"n={n} T3 orbit label", ok3)
    check(f"n={n} T4 bridge identity ({'exhaustive' if ex else 'first 64 states'})", ok4)
    check(f"n={n} T4 same-orbit identity", ok4s)
    print(f"INFO n={n} T5 Gamma-equal pairs with different product: {clash if ex else 'not run'}; c real-valued: {real_c}; |Zero(n)|={nz}; T6 Gamma=0 carries both products: {zb}")
for n in range(1, 13):
    lam = cmath.exp(1j * cmath.pi / n); phi = cyclo(2 * n)
    Xs = [x for x in itertools.product((0, 1), repeat=n) if any(exact_key(x, n, phi))]
    cs = set()
    for x in Xs:
        z = Zc(x, lam); c = r(x) / (z / abs(z)) ** n
        cs.add((round(c.real, 6) + 0.0, round(c.imag, 6) + 0.0))
    print(f"INFO n={n} T7 distinct orbit labels c: {len(cs)}; global label-free identity: {cs == {(1.0, 0.0)}}")
    if n <= 4: check(f"n={n} T7 c==1 on X^x", cs == {(1.0, 0.0)})
    else: check(f"n={n} T7 c not constant (census)", len(cs) > 1)
w = cmath.exp(2j * cmath.pi / 3); x = (1, 0, 0); orb = []
while x not in orb: orb.append(x); x = F(x)
Wv = {x: (x[0] - x[2]) + w * (x[0] + x[1] - 1) for x in orb}
check("n=3 T8 6-cycle length", len(orb) == 6)
check("n=3 T8 (-1)^pi3=-W^3", all(abs(r(x) + Wv[x] ** 3) < TOL for x in orb))
check("n=3 T8 r_X r_Y=(conj W_X W_Y)^3", all(abs(r(x) * r(y) - (Wv[x].conjugate() * Wv[y]) ** 3) < TOL for x in orb for y in orb))
# negative control
def rbad(x): return -r(x) if x == (1,) + (0,) * 3 else r(x)
res = run(4, True, rbad)
check("negative control: perturbed sign fails T1 or T4", (not res[0]) or (not res[4]))
sys.exit(1 if fails else 0)
