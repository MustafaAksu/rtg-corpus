#!/usr/bin/env python3
"""Exact finite checks for the Binary Recognition wrap-up (Node Foundations thread).

Standard library only. Integer polynomial arithmetic modulo cyclotomic polynomials;
no floating point decides any predicate. Exit code 0 iff every assertion passes.

Usage:  python binary_recognition_wrapup_checks.py [--out results.json]

Model:  X_n = {0,1}^n,  F_n(x_0..x_{n-1}) = (1-x_{n-1}, x_0, .., x_{n-2}),  C_n X = 1-X,
        Z_n(X) = 1 - (1-lam) P_X(lam),  lam = exp(i pi/n),  P_X(t) = sum x_j t^j.
        Z_n(X) = Z_n(Y)  <=>  Phi_{2n} | (P_X - P_Y);   Z_n(X) = 0  <=>  Phi_{2n} | Y_X,
        Y_X(t) = sum (2x_j - 1) t^j.
"""
import json
import sys
from functools import lru_cache
from itertools import product, combinations

RESULTS = []
FAILED = []
# Negative controls: each deliberately false claim must make the run fail (exit 1).
CONTROL = sys.argv[sys.argv.index("--control") + 1] if "--control" in sys.argv else None


def check(name, cond):
    RESULTS.append({"name": name, "pass": bool(cond)})
    if not cond:
        FAILED.append(name)


# ---------------------------------------------------------------- polynomials (low -> high)
def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    return trim(r)


def pdivmod(a, m):
    """Division by a monic integer polynomial m."""
    a = trim(a)
    m = trim(m)
    assert m[-1] == 1
    q = [0] * max(len(a) - len(m) + 1, 1)
    a = a[:]
    while len(a) >= len(m) and a:
        c = a[-1]
        s = len(a) - len(m)
        q[s] = c
        for i, y in enumerate(m):
            a[s + i] -= c * y
        a = trim(a)
    return trim(q), a


def prem(a, m):
    return tuple(pdivmod(a, m)[1])


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


@lru_cache(maxsize=None)
def cyclo(d):
    num = [-1] + [0] * (d - 1) + [1]  # t^d - 1
    for e in divisors(d):
        if e < d:
            num, r = pdivmod(num, list(cyclo(e)))
            assert not r
    return tuple(num)


def peval(a, x):
    return sum(c * x ** i for i, c in enumerate(a))


def is_pow2(n):
    return n > 0 and n & (n - 1) == 0


def odd_primes(n):
    ps, m, p = [], n, 2
    while m % 2 == 0:
        m //= 2
    p = 3
    while p * p <= m:
        if m % p == 0:
            ps.append(p)
            while m % p == 0:
                m //= p
        p += 2
    if m > 1:
        ps.append(m)
    return ps


def is_odd_prime(n):
    return n > 2 and odd_primes(n) == [n] and n % 2 == 1


# ---------------------------------------------------------------- register
def F(X):
    return (1 - X[-1],) + X[:-1]


def C(X):
    return tuple(1 - x for x in X)


def period(X):
    Y, p = F(X), 1
    while Y != X:
        Y, p = F(Y), p + 1
    return p


def par(X):
    return sum(X) % 2


def PX(X):
    return trim(list(X))


def YX(X):
    return trim([2 * x - 1 for x in X])


def zkey(X, n):
    return prem(PX(X), cyclo(2 * n))


def zero(X, n):
    return prem(YX(X), cyclo(2 * n)) == ()


def two_adic(n):
    h = 1
    while n % (2 * h) == 0:
        h *= 2
    return h, n // h


# ================================================================ C1 two-bit classification
# state (b,p); F(b,p) = (f(b,p), b); d = b xor p
tables = list(product([0, 1], repeat=4))
S2 = list(product([0, 1], repeat=2))
alt = [t for t in tables if all((t[2 * b + p] ^ b) == (1 ^ b ^ p) for b, p in S2)]
check("C1 recognition alternation alone selects f = 1-p", alt == [(1, 0, 1, 0)])
rev_nofix = []
for t in tables:
    Fm = {(b, p): (t[2 * b + p], b) for b, p in S2}
    if len(set(Fm.values())) == 4 and all(Fm[s] != s for s in S2):
        rev_nofix.append(t)
check("C1 reversible + no fixed state selects the same f", rev_nofix == [(1, 0, 1, 0)])
revs = [t for t in tables if len({(t[2 * b + p], b) for b, p in S2}) == 4]
cov = [t for t in revs if all((t[2 * (1 - b) + (1 - p)], 1 - b) == (1 - t[2 * b + p], 1 - b) for b, p in S2)]
check("C1 four reversible laws, exactly two C-covariant", len(revs) == 4 and len(cov) == 2)

# ================================================================ C2 Gaussian representation
F2 = lambda s: (1 - s[1], s[0])
R2 = lambda s: (s[1], s[0])
C2 = lambda s: (1 - s[0], 1 - s[1])
Zg = lambda s: (1 - s[0] - s[1], s[0] - s[1])  # (re, im)
imul = lambda z: (-z[1], z[0])
check("C2 Z(FX) = i Z(X)", all(Zg(F2(s)) == imul(Zg(s)) for s in S2))
check("C2 |Z| = 1", all(z[0] ** 2 + z[1] ** 2 == 1 for z in map(Zg, S2)))
sq = lambda z: (z[0] ** 2 - z[1] ** 2, 2 * z[0] * z[1])
check("C2 Z^2 = (-1)^d", all(sq(Zg(s)) == ((-1) ** (s[0] ^ s[1]), 0) for s in S2))
check("C2 F^2 = C, F^4 = id", all(F2(F2(s)) == C2(s) and F2(F2(F2(F2(s)))) == s for s in S2))
Finv = {F2(s): s for s in S2}
check("C2 R F R = F^-1 (role reversal)", all(R2(F2(R2(s))) == Finv[s] for s in S2))
check("C2 Z(RX) = conj Z(X)", all(Zg(R2(s)) == (Zg(s)[0], -Zg(s)[1]) for s in S2))

# ================================================================ C3 general register, parity, gauge type
for n in range(1, 11):
    S = list(product([0, 1], repeat=n))
    Fn = lambda X: X
    ok_FnC = True
    for X in S:
        Y = X
        for _ in range(n):
            Y = F(Y)
        ok_FnC &= (Y == C(X))
    check(f"C3 n={n}: F^n = C", ok_FnC)
    check(f"C3 n={n}: parity alternates", all(par(F(X)) == 1 - par(X) for X in S))
    check(f"C3 n={n}: parity(CX) = parity(X) + n mod 2", all(par(C(X)) == (par(X) + n) % 2 for X in S))
    # affine alternating readouts over GF(2)
    aff = []
    for a in product([0, 1], repeat=n):
        for c in (0, 1):
            d = lambda X: (c + sum(ai * xi for ai, xi in zip(a, X))) % 2
            if all(d(F(X)) == 1 - d(X) for X in S):
                aff.append((a, c))
    check(f"C3 n={n}: affine alternating readouts = parity and complement",
          sorted(aff) == sorted([((1,) * n, 0), ((1,) * n, 1)]))
for n in range(1, 5):
    S = list(product([0, 1], repeat=n))
    ok = True
    for tbl in product([0, 1], repeat=2 ** n):
        idx = {X: i for i, X in enumerate(S)}
        d = lambda X: tbl[idx[X]]
        if all(d(F(X)) == 1 - d(X) for X in S):
            ok &= all(d(C(X)) == (d(X) + n) % 2 for X in S)
    check(f"C3 n={n}: every alternating Boolean readout has C-type n mod 2 (exhaustive)", ok)

# ================================================================ C4 three-bit register and DYAD linear bridge
S3 = list(product([0, 1], repeat=3))
seen, orbs = set(), []
for X in S3:
    if X in seen:
        continue
    o, Y = [X], F(X)
    while Y != X:
        o.append(Y)
        Y = F(Y)
    seen |= set(o)
    orbs.append(len(o))
check("C4 n=3 orbits: one 6-cycle and one 2-cycle", sorted(orbs) == [2, 6])
B = lambda s: (s[0] - s[2], s[0] + s[1] - 1)
A = lambda v: (v[0] - v[1], v[0])
check("C4 B F3 = A B on all eight states", all(B(F(s)) == A(B(s)) for s in S3))
Q = lambda v: v[0] ** 2 - v[0] * v[1] + v[1] ** 2
check("C4 six-cycle maps to unit-Q hexagon, two-cycle to origin",
      sorted(Q(B(s)) for s in S3) == [0, 0, 1, 1, 1, 1, 1, 1])
check("C4 B loses parity on the zero fibre",
      B((0, 1, 0)) == B((1, 0, 1)) == (0, 0) and par((0, 1, 0)) != par((1, 0, 1)))

# ================================================================ C5 full-cube parity descent through Z_n
for n in range(1, 13):
    S = list(product([0, 1], repeat=n))
    fib = {}
    for X in S:
        fib.setdefault(zkey(X, n), set()).add(par(X))
    desc = all(len(v) == 1 for v in fib.values())
    inj = len(fib) == len(S)
    check(f"C5 n={n}: parity descends on full cube iff n power of two", desc == is_pow2(n))
    check(f"C5 n={n}: Z_n injective on full cube iff n power of two", inj == is_pow2(n))
for n in range(3, 61):
    for p in odd_primes(n):
        d = n // p
        X = tuple(1 if (j % d == 0 and (j // d) % 2 == 0) else 0 for j in range(n))
        Y = tuple(1 if (j % d == 0 and (j // d) % 2 == 1) else 0 for j in range(n))
        ok = zkey(X, n) == zkey(Y, n) and par(X) != par(Y)
        ok &= (zero(X, n) == (d == 1))  # shared image nonzero iff d > 1
        check(f"C5 K-witness n={n}, p={p}: equal image, opposite parity, nonzero iff d>1", ok)

# ================================================================ C6 zero fibre versus short orbits
def zero_short_class(n):
    if CONTROL == "zero-equals-short-for-all-n":
        return True
    ps = odd_primes(n)
    return len(ps) <= 1 or (n % 2 == 1 and len(ps) == 2 and n == ps[0] * ps[1])


census = {}
for n in range(1, 17):
    S = list(product([0, 1], repeat=n))
    Z0 = {X for X in S if zero(X, n)}
    Sh = {X for X in S if period(X) < 2 * n}
    census[n] = {"zero": len(Z0), "short": len(Sh)}
    check(f"C6 n={n}: Short subset of Zero", Sh <= Z0)
    check(f"C6 n={n}: Zero = Short iff n in classified set", (Z0 == Sh) == zero_short_class(n))
for n, s in [(30, "111111010100101010000101111111"),
             (45, "111101010100010001011101010100110101011101010")]:
    X = tuple(int(c) for c in s)
    check(f"C6 witness n={n}: Z_n = 0 with full period 2n", zero(X, n) and period(X) == 2 * n)
check("C6 n=30 and n=45 are outside the classified set", not zero_short_class(30) and not zero_short_class(45))
check("C6 n=15, 21 inside the classified set", zero_short_class(15) and zero_short_class(21))
# radical stripping: |Zero(n)| = |Zero(M)|^(n/M), M odd radical
for n in range(1, 17):
    M = 1
    for p in odd_primes(n):
        M *= p
    check(f"C6 n={n}: |Zero(n)| = |Zero(M)|^(n/M)", census[n]["zero"] == census[M]["zero"] ** (n // M))

# ================================================================ C7 nonzero-sector injectivity and parity descent
for n in range(1, 15):
    S = list(product([0, 1], repeat=n))
    fib = {}
    for X in S:
        if not zero(X, n):
            fib.setdefault(zkey(X, n), []).append(X)
    inj = all(len(v) == 1 for v in fib.values())
    desc = all(len({par(X) for X in v}) == 1 for v in fib.values())
    expect = is_pow2(n) or is_odd_prime(n)
    if CONTROL == "sector-injective-only-at-powers-of-two":
        expect = is_pow2(n)
    check(f"C7 n={n}: sector injective iff 2^a or odd prime", inj == expect)
    check(f"C7 n={n}: sector parity descent iff 2^a or odd prime", desc == expect)
    check(f"C7 n={n}: every nonzero state has period 2n",
          all(period(X) == 2 * n for v in fib.values() for X in v))

# ================================================================ C8 spectral enrichment and the parity component
for n in range(2, 13):
    h, m = two_adic(n)
    comps = [d for d in divisors(2 * n) if n % d != 0]
    S = list(product([0, 1], repeat=n))
    ok = True
    for r in range(1, len(comps) + 1):
        for D in combinations(comps, r):
            fib = {}
            for X in S:
                key = tuple(prem(PX(X), cyclo(d)) for d in D)
                fib.setdefault(key, set()).add(par(X))
            desc = all(len(v) == 1 for v in fib.values())
            ok &= (desc == ((2 * h) in D)) if CONTROL != "parity-needs-original-component" else (desc == ((2 * n) in D))
    check(f"C8 n={n}: parity descends through retained components D iff 2h in D", ok)
for n in range(1, 65):
    h, m = two_adic(n)
    comps = [d for d in divisors(2 * n) if n % d != 0]
    hits = [d for d in comps if peval(cyclo(d), 1) % 2 == 0]
    check(f"C8 n={n}: Phi_2h is the only component vanishing at t=1 mod 2", hits == [2 * h])

# ================================================================ C9 Boolean folding factor X_n -> X_h
for n in range(1, 15):
    h, m = two_adic(n)
    S = list(product([0, 1], repeat=n))
    phi = lambda X: tuple(sum(X[k * h + r] for k in range(m)) % 2 for r in range(h))
    cf = lambda X: tuple(sum((-1) ** k * X[k * h + r] for k in range(m)) for r in range(h))
    ok = all(phi(F(X)) == F(phi(X)) and phi(C(X)) == C(phi(X)) and par(phi(X)) == par(X) for X in S)
    ok &= len({phi(X) for X in S}) == 2 ** h
    ok &= all(tuple(c % 2 for c in cf(X)) == phi(X) for X in S)
    ok &= all(cf(F(X)) == (1 - cf(X)[-1],) + cf(X)[:-1] for X in S)
    ok &= len({cf(X) for X in S}) == (m + 1) ** h
    check(f"C9 n={n}: folding is F-, C-equivariant, parity-preserving, onto; c-update exact; |c|=(m+1)^h", ok)
    check(f"C9 n={n}: 2h | period(X) | 2n", all(period(X) % (2 * h) == 0 and (2 * n) % period(X) == 0 for X in S))
    full, sec = {}, {}
    for X in S:
        full.setdefault(zkey(X, n), set()).add(phi(X))
        if not zero(X, n):
            sec.setdefault(zkey(X, n), set()).add(phi(X))
    check(f"C9 n={n}: folding descends through Z_n on full cube iff 2^a",
          all(len(v) == 1 for v in full.values()) == is_pow2(n))
    check(f"C9 n={n}: folding descends on nonzero sector iff 2^a or odd prime",
          all(len(v) == 1 for v in sec.values()) == (is_pow2(n) or is_odd_prime(n)))
check("C9 n=6 state (0,1,1,0,0,1) has period 4", period((0, 1, 1, 0, 0, 1)) == 4)

# ================================================================ C10 bit replication (refinement)
def rep(X, k):
    return tuple(x for x in X for _ in range(k))


for n in range(1, 7):
    for k in range(1, 6):
        S = list(product([0, 1], repeat=n))
        ok = True
        for X in S:
            Y = rep(X, k)
            Z = Y
            for _ in range(k):
                Z = F(Z)
            ok &= (Z == rep(F(X), k)) and (C(Y) == rep(C(X), k)) and (par(Y) == (k % 2) * par(X))
            # Z_{kn}(rep X) = Z_n(X): (1-t) P_rep(t) == (1-t^k) P_X(t^k) as polynomials
            lhs = pmul([1, -1], PX(Y))
            Pk = [0] * (k * (n - 1) + 1)
            for j, x in enumerate(X):
                Pk[k * j] = x
            rhs = pmul([1] + [0] * (k - 1) + [-1], trim(Pk))
            ok &= (lhs == rhs)
        check(f"C10 n={n}, k={k}: replication intertwines F, C, Z; parity pulls back as k mod 2", ok)

# ================================================================ output
out = {
    "script": "binary_recognition_wrapup_checks.py",
    "status": "PASS" if not FAILED else "FAIL",
    "count": len(RESULTS),
    "failed": FAILED,
    "zero_short_census_n1_16": census,
    "checks": RESULTS,
}
path = None
if "--out" in sys.argv:
    path = sys.argv[sys.argv.index("--out") + 1]
text = json.dumps(out, indent=1, sort_keys=True)
if path:
    with open(path, "w", newline="\n") as fh:
        fh.write(text + "\n")
print(f"{out['status']}: {len(RESULTS) - len(FAILED)}/{len(RESULTS)} checks")
for f in FAILED:
    print("FAILED:", f)
sys.exit(0 if not FAILED else 1)
