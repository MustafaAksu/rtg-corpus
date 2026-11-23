#!/usr/bin/env python3
"""OPEN M (UVM) -- OPEN-M-6 stage 1: jet-covariance certificate.

Scope (records/uvm/UVM_OPEN_M6_SCOPE_DRAFT.md, PI authorization of 23 Nov 2026):
  C0   passive-transport control (base chart change + fibre re-trivialization)
  C1   NF-native candidate  s(z) = Lambda*conj(z):   tests A1, A2, A3
  C2   W-native candidate   s(W) = Lambda*conj(W):   test  A1'
Everything is exact arithmetic in Q(i*sqrt(3)) on jets of total degree <= N = 6
in (x, conj x).  Standard library only.  No physical quantity is computed.

Stipulations used (proposals, not adopted science):
  * generator T(rho,eta) = (rho - sin eta, eta + e^rho - 1 - sin eta)   [DYAD SG-14]
  * frame W = rho + omega*eta, omega = (-1 + i sqrt3)/2;  lambda = (1 + i sqrt3)/2
  * constant fibre action: multiplication by conj(lambda) on the complex
    coefficient function s of the source, in the trivialization named in each test
  * quaternion convention for the ordering checks: q = z + j*y, j*a = conj(a)*j,
    Z6 acts by left multiplication by lambda (so the j-component has weight -1)

Exit code 0 iff every check passes.  A check named CONTROL-* passes when the
deliberately wrong variant is DETECTED as wrong.

Usage:  python3 uvm_open_m6_stage1_jet_cert.py [--json OUT.json]
"""
import json
import sys
from fractions import Fraction as Fr

N = 6  # jet order


# ---------------------------------------------------------------- field Q(i sqrt3)
class K:
    __slots__ = ("p", "q")  # p + q * i*sqrt(3)

    def __init__(self, p=0, q=0):
        self.p = Fr(p)
        self.q = Fr(q)

    def __add__(self, o):
        o = kc(o)
        return K(self.p + o.p, self.q + o.q)

    __radd__ = __add__

    def __neg__(self):
        return K(-self.p, -self.q)

    def __sub__(self, o):
        o = kc(o)
        return K(self.p - o.p, self.q - o.q)

    def __rsub__(self, o):
        return kc(o) - self

    def __mul__(self, o):
        o = kc(o)
        return K(self.p * o.p - 3 * self.q * o.q, self.p * o.q + self.q * o.p)

    __rmul__ = __mul__

    def conj(self):
        return K(self.p, -self.q)

    def inv(self):
        d = self.p * self.p + 3 * self.q * self.q
        if d == 0:
            raise ZeroDivisionError
        return K(self.p / d, -self.q / d)

    def __truediv__(self, o):
        return self * kc(o).inv()

    def __eq__(self, o):
        o = kc(o)
        return self.p == o.p and self.q == o.q

    def __hash__(self):
        return hash((self.p, self.q))

    def is_zero(self):
        return self.p == 0 and self.q == 0

    def __repr__(self):
        if self.q == 0:
            return str(self.p)
        if self.p == 0:
            return "(%s)*i*sqrt3" % self.q
        return "%s + (%s)*i*sqrt3" % (self.p, self.q)


def kc(x):
    return x if isinstance(x, K) else K(x)


ZERO, ONE = K(0), K(1)
LAM = K(Fr(1, 2), Fr(1, 2))     # lambda = e^{i pi/3}
LAMB = LAM.conj()
OMEGA = K(Fr(-1, 2), Fr(1, 2))  # omega
INV_ISQRT3 = K(0, Fr(-1, 3))    # 1/(i sqrt3)


# ---------------------------------------------------------------- jets
# a jet is a dict {(a, b): K} meaning sum c_ab x^a conj(x)^b, a + b <= N
def clean(P):
    return {m: c for m, c in P.items() if not c.is_zero()}


def jadd(P, Q):
    R = dict(P)
    for m, c in Q.items():
        R[m] = R.get(m, ZERO) + c
    return clean(R)


def jscale(c, P):
    c = kc(c)
    return clean({m: c * v for m, v in P.items()})


def jsub(P, Q):
    return jadd(P, jscale(-1, Q))


def jmul(P, Q, n=N):
    R = {}
    for (a, b), c in P.items():
        for (a2, b2), c2 in Q.items():
            if a + b + a2 + b2 <= n:
                m = (a + a2, b + b2)
                R[m] = R.get(m, ZERO) + c * c2
    return clean(R)


def jconj(P):
    """complex conjugate of the function: conj(sum c x^a xb^b) = sum conj(c) x^b xb^a"""
    return {(b, a): c.conj() for (a, b), c in P.items()}


def jtrunc(P, n):
    return {m: c for m, c in P.items() if m[0] + m[1] <= n}


def jpart(P, d):
    return {m: c for m, c in P.items() if m[0] + m[1] == d}


X = {(1, 0): ONE}
CONST1 = {(0, 0): ONE}


def compose(P, Q, n=N):
    """P(Q, conj Q); Q must have zero constant term."""
    assert (0, 0) not in Q
    Qb = jconj(Q)
    amax = max([m[0] for m in P] + [0])
    bmax = max([m[1] for m in P] + [0])
    pa = [CONST1]
    for _ in range(amax):
        pa.append(jmul(pa[-1], Q, n))
    pb = [CONST1]
    for _ in range(bmax):
        pb.append(jmul(pb[-1], Qb, n))
    R = {}
    for (a, b), c in P.items():
        R = jadd(R, jscale(c, jmul(pa[a], pb[b], n)))
    return R


def iterate(P, k, n=N):
    R = X
    for _ in range(k):
        R = compose(P, R, n)
    return R


def inverse_map(P, n=N):
    """inverse of a jet map with linear part l*x (complex-linear)."""
    l = P.get((1, 0), ZERO)
    assert not l.is_zero() and (0, 1) not in P and (0, 0) not in P
    nl = jsub(P, {(1, 0): l})
    G = {(1, 0): l.inv()}
    for _ in range(n + 1):
        G = jscale(l.inv(), jsub(X, compose(nl, G, n)))
    return G


def recip(g, n=N):
    """1/g for a jet with nonzero constant term."""
    g0 = g[(0, 0)]
    u = jsub(CONST1, jscale(g0.inv(), g))  # g = g0 (1 - u)
    R, t = CONST1, CONST1
    for _ in range(n):
        t = jmul(t, u, n)
        R = jadd(R, t)
    return jscale(g0.inv(), R)


def show(P):
    return {"x^%d xb^%d" % m: repr(c) for m, c in sorted(P.items(), key=lambda t: (t[0][0] + t[0][1], -t[0][0]))}


def nonzero_by_degree(P):
    return {d: len(jpart(P, d)) for d in range(0, N + 1) if jpart(P, d)}


# ---------------------------------------------------------------- bookkeeping
RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append({"check": name, "pass": bool(ok), "detail": detail})
    print("%-6s %s%s" % ("PASS" if ok else "FAIL", name, ("  -- " + detail) if detail else ""))
    return bool(ok)


# ---------------------------------------------------------------- dyad side
def build_f():
    """f = L T L^{-1} as a jet in (W, conj W), exact Taylor through degree N."""
    W, Wb = X, {(0, 1): ONE}
    eta = jscale(INV_ISQRT3, jsub(W, Wb))           # eta = (W - Wb)/(i sqrt3)
    rho = jsub(W, jscale(OMEGA, eta))               # rho = W - omega*eta
    def series(arg, coeffs):
        R, p = {}, CONST1
        for k, c in enumerate(coeffs):
            if k > 0:
                p = jmul(p, arg)
            if c != 0:
                R = jadd(R, jscale(c, p))
        return R
    fact = [Fr(1)]
    for k in range(1, N + 1):
        fact.append(fact[-1] * k)
    sin_eta = series(eta, [0 if k % 2 == 0 else Fr((-1) ** ((k - 1) // 2)) / fact[k] for k in range(N + 1)])
    exp_rho_m1 = series(rho, [0] + [1 / fact[k] for k in range(1, N + 1)])
    rho1 = jsub(rho, sin_eta)
    eta1 = jsub(jadd(eta, exp_rho_m1), sin_eta)
    return jadd(rho1, jscale(OMEGA, eta1))


def resonant(a, b):
    return (a - b - 1) % 6 == 0


def normalizer(f, perturb=None):
    """h = id + h_2 + ... + h_N with resonant coefficients zero; n = one-step normal form.
    J_{<=N}(f o h - h o n) = 0.  `perturb` adds an error to one h coefficient (control)."""
    h = dict(X)
    n = {(1, 0): LAM}
    for d in range(2, N + 1):
        E = jpart(jsub(compose(f, h), compose(h, n)), d)
        for a in range(d, -1, -1):
            b = d - a
            e = E.get((a, b), ZERO)
            if resonant(a, b):
                if not e.is_zero():
                    n[(a, b)] = e
            else:
                lam_ab = ONE
                k = (a - b) % 6
                for _ in range(k):
                    lam_ab = lam_ab * LAM
                hab = -e / (LAM - lam_ab)
                if perturb and perturb[0] == (a, b):
                    hab = hab + perturb[1]
                if not hab.is_zero():
                    h[(a, b)] = hab
    return h, n


def sixth_root(F):
    """tangent-to-identity jet Kr with Kr^{o6} = F through degree N."""
    Kr = dict(X)
    for d in range(2, N + 1):
        cur = jpart(iterate(Kr, 6), d)
        diff = jsub(jpart(F, d), cur)
        Kr = jadd(Kr, jscale(Fr(1, 6), diff))
    return Kr


def main():
    out = {"N": N, "checks": RESULTS}
    f = build_f()

    # ---- engine validation against the Dyadic owner values (DYAD-ALG-NF6)
    check("E0  linear part of f is lambda*W", f.get((1, 0)) == LAM and (0, 1) not in f)
    h, n = normalizer(f)
    exp_h2 = {(2, 0): K(Fr(-1, 12), Fr(-1, 12)), (1, 1): K(Fr(-1, 3)), (0, 2): K(Fr(1, 24), Fr(-1, 24))}
    check("E1  h_2 equals the owner h_2", jpart(h, 2) == exp_h2, repr(show(jpart(h, 2))))
    check("E2  h_3 nonzero exactly in channels (3,0),(1,2),(0,3)", set(jpart(h, 3)) == {(3, 0), (1, 2), (0, 3)})
    check("E3  h has 23 nonzero coefficients incl. linear", len(h) == 23, "count=%d" % len(h))
    exp_n = {(1, 0): LAM, (2, 1): K(Fr(1, 8), Fr(-7, 72)), (3, 2): K(Fr(-5, 432), Fr(23, 3888)),
             (0, 5): K(Fr(43, 17280), Fr(-227, 155520))}
    check("E4  one-step normal form n equals the owner n (n_21, n_32, n_05)", n == exp_n, repr(show(n)))
    res = compose(f, h)
    res = jsub(res, compose(h, n))
    check("E5  J_{<=6}(f o h - h o n) = 0", not res)
    Jnf = jtrunc(iterate(n, 6), 5)
    exp_J = {(1, 0): ONE, (2, 1): K(Fr(-1, 2), Fr(-2, 3)), (3, 2): K(Fr(-97, 432), Fr(197, 324)),
             (0, 5): K(Fr(-49, 8640), Fr(-307, 25920))}
    check("E6  six-step jet J_NF = J_{<=5} n^6 equals the owner (mu, a_32, a_05)", Jnf == exp_J, repr(show(Jnf)))
    out["h"] = show(h)
    out["n"] = show(n)

    # ---- intrinsic Z6 generator in the raw frame, from first principles
    F = iterate(f, 6)
    check("G0  F = f^6 is tangent to the identity", F.get((1, 0)) == ONE and not jpart(F, 0) and (0, 1) not in F)
    Kr = sixth_root(F)
    check("G1  K^6 = F through degree 6 (tangent-to-identity sixth root)", not jsub(iterate(Kr, 6), F))
    check("G2  K commutes with f through degree 6", not jsub(compose(Kr, f), compose(f, Kr)))
    JW = compose(f, inverse_map(Kr))
    check("G3  J_W := f o K^{-1} has linear part lambda", JW.get((1, 0)) == LAM and (0, 1) not in JW)
    check("G4  J_W^6 = id through degree 6", iterate(JW, 6) == X)
    check("G5  J_W commutes with f through degree 6", not jsub(compose(JW, f), compose(f, JW)))
    hinv = inverse_map(h)
    check("G6  h^{-1} o h = id through degree 6", compose(hinv, h) == X)
    JNFchart = compose(hinv, compose(JW, h))
    check("P2  J_{<=6}(h^{-1} J_Z6 h) = A  (generator is linear in the NF chart)", JNFchart == {(1, 0): LAM},
          repr(show(JNFchart)))
    exp_d2 = {(2, 0): K(Fr(1, 12), Fr(1, 12)), (1, 1): K(Fr(-1, 6), Fr(1, 6)), (0, 2): K(Fr(-1, 6))}
    check("P4  quadratic part of J_W equals delta_2 = h_2(lam W, lamb Wb) - lam h_2(W, Wb)",
          jpart(JW, 2) == exp_d2, repr(show(jpart(JW, 2))))
    out["J_W"] = show(JW)
    out["J_W_nonzero_by_degree"] = nonzero_by_degree(JW)

    # ---- C1: NF-native candidate, s(z) = conj(z)  (Lambda = 1; the tests are linear in Lambda)
    sC1 = {(0, 1): ONE}
    defect_A1 = jsub(jconj(JNFchart), jscale(LAMB, sC1))        # s(Jz) - lamb*s(z)
    check("A1  C1 is covariant under J_Z6 through degree 6 (constant fibre action lamb)", not defect_A1)

    # A2: weight statement, re-derived by the equivariant projector P s(z) = (1/6) sum_k lam^k s(lam^k z)
    weight_set = []
    for d in range(1, N + 1):
        for a in range(d, -1, -1):
            b = d - a
            acc, lk = ZERO, ONE
            for k in range(6):
                # s(lam^k z) for s = z^a zb^b is lam^{k(a-b)} s ; projector weight lam^k
                e = (k * (a - b)) % 6
                ph = ONE
                for _ in range(e):
                    ph = ph * LAM
                acc = acc + lk * ph
                lk = lk * LAM
            if not (acc / 6).is_zero():
                weight_set.append((a, b))
    exp_ws = [(0, 1), (1, 2), (5, 0), (2, 3)]
    check("A2  covariant source monomials through degree 6 are exactly zb, z zb^2, z^5, z^2 zb^3",
          sorted(weight_set) == sorted(exp_ws), repr(weight_set))
    check("A2b covariant degrees are {1,3,5}; the only degree-1 member is conj(z)",
          sorted({a + b for a, b in weight_set}) == [1, 3, 5] and [m for m in weight_set if sum(m) == 1] == [(0, 1)])
    out["A2_weight_set"] = ["x^%d xb^%d" % m for m in weight_set]

    # A3: centralizer changes psi (tangent to identity, commuting with A) and what they leave invariant
    a3 = []
    for label, psi in (
        ("psi1", {(1, 0): ONE, (2, 1): K(Fr(1, 7), Fr(2, 5))}),
        ("psi2", {(1, 0): ONE, (2, 1): K(Fr(-3, 11), Fr(1, 4)), (3, 2): K(Fr(2, 9), Fr(-1, 13)), (0, 5): K(Fr(5, 17), Fr(3, 8))}),
    ):
        Amap = {(1, 0): LAM}
        ok_comm = not jsub(compose(psi, Amap), compose(Amap, psi))
        s_new = jconj(inverse_map(psi))            # conj(z) written in the coordinate z' = psi(z)
        ok_class = all((m in exp_ws) for m in s_new)
        ok_lin = s_new.get((0, 1)) == ONE
        c21 = psi[(2, 1)]
        ok_cubic = s_new.get((1, 2), ZERO) == -(c21.conj()) and not c21.is_zero()
        a3.append({"psi": label, "transported_source": show(s_new)})
        check("A3  %s: commutes with A; source stays in the weight class; degree-1 coefficient invariant; "
              "cubic member = -conj(c_21) != 0" % label, ok_comm and ok_class and ok_lin and ok_cubic,
              repr(show(s_new)))
    out["A3"] = a3

    # ---- C2: W-native candidate, s(W) = conj(W)
    sC2 = {(0, 1): ONE}
    defect_A1p = jsub(jconj(JW), jscale(LAMB, sC2))             # s(J_W W) - lamb*s(W)
    exp_cd2 = jconj(exp_d2)
    check("A1' C2 is NOT covariant under J_Z6 with a constant fibre action: defect nonzero at degree 2 "
          "and equal to conj(delta_2)", jpart(defect_A1p, 2) == exp_cd2 and bool(jpart(defect_A1p, 2)),
          repr(show(jpart(defect_A1p, 2))))
    out["A1prime_defect"] = show(defect_A1p)
    out["A1prime_defect_nonzero_by_degree"] = nonzero_by_degree(defect_A1p)
    check("A1'b defect of C2 is nonzero at every degree 2..6", all(jpart(defect_A1p, d) for d in range(2, N + 1)),
          repr(nonzero_by_degree(defect_A1p)))

    # P3: C1 written in the raw frame versus C2
    sC1_W = jconj(hinv)                                          # conj(h^{-1}(W))
    diff = jsub(sC1_W, sC2)
    exp_p3 = jscale(-1, jconj(exp_h2))
    check("P3  s_C1^W - s_C2 = -conj(h_2(W, Wb)) at degree 2, nonzero", jpart(diff, 2) == exp_p3 and not jpart(diff, 1),
          repr(show(jpart(diff, 2))))
    out["P3_difference"] = show(diff)

    # C2a at degree 2: which fibre actions can absorb the defect
    D2 = jpart(defect_A1p, 2)
    c1, c2, c3 = D2.get((2, 0), ZERO), D2.get((1, 1), ZERO), D2.get((0, 2), ZERO)
    check("C2a-1 no C^1 complex-scalar fibre action absorbs the degree-2 defect "
          "(coefficient of W^2 in the defect is nonzero, so defect/conj(W) is not C^1 at 0)", not c1.is_zero(), repr(c1))
    alpha = {(0, 0): LAMB, (1, 0): c2, (0, 1): c3}               # acts on s
    beta = {(1, 0): c1}                                          # acts on conj(s)
    lhs = jadd(jmul(alpha, sC2, 2), jmul(beta, jconj(sC2), 2))
    rhs = jtrunc(jconj(JW), 2)
    check("C2a-2 a real-linear state-dependent fibre action alpha*s + beta*conj(s) absorbs it through degree 2",
          lhs == rhs, "alpha=%r beta=%r" % (show(alpha), show(beta)))
    # a real-linear re-trivialization g = (1 + a) s + b conj(s) carrying C1 (in the raw frame) onto C2, degree 2
    e2 = jpart(sC1_W, 2)                                         # = -conj(h_2)
    ga = {(0, 0): ONE, (1, 0): K(Fr(-1, 3)), (0, 1): -e2.get((0, 2), ZERO)}     # 1 + a1 W + a2 Wb
    gb = {(1, 0): -e2.get((2, 0), ZERO)}                                         # b1 W   (b2 = 0)
    s1 = jtrunc(sC1_W, 2)
    carried = jadd(jmul(ga, s1, 2), jmul(gb, jconj(s1), 2))
    check("C2a-3 a real-linear state-dependent re-trivialization carries C1 (raw frame) onto C2 through degree 2: "
          "with unrestricted fibre gauge C2a is C1 in another trivialization", carried == sC2,
          "g: s -> (%r) s + (%r) conj(s)" % (show(ga), show(gb)))

    # ---- quaternionic ordering checks (q = z + j y, j a = conj(a) j, left action by lambda)
    def qmul(u, v):  # (a + j b)(c + j d) = (ac - conj(b) d) + j(conj(a) d + b c)
        (a, b), (c, d) = u, v
        return (a * c - b.conj() * d, a.conj() * d + b * c)

    def qconj(u):    # conj(a + j b) = conj(a) - j b
        return (u[0].conj(), -u[1])

    lamq = (LAM, ZERO)
    jq = (ZERO, ONE)
    z = K(Fr(3, 5), Fr(-2, 7)); y = K(Fr(-4, 9), Fr(1, 6)); Lm = K(Fr(7, 3), Fr(5, 11))
    zq, Lq = (z, ZERO), (Lm, ZERO)
    left = qmul(lamq, (z, y))
    check("Q1  left multiplication by lambda acts as (lambda z, conj(lambda) y): j-component has weight -1",
          left == (LAM * z, LAMB * y))
    src = lambda zz: qmul(jq, qmul(Lq, (zz.conj(), ZERO)))       # j Lambda conj(z)
    check("Q2  H = j Lambda conj(z) on Pi_par satisfies H(lambda z) = lambda H(z); its coefficient function is Lambda conj(z)",
          src(LAM * z) == qmul(lamq, src(z)) and src(z) == (ZERO, Lm * z.conj()))
    word = lambda q: qmul(q, qmul(jq, qmul(Lq, qmul(qconj(q), q))))   # q j Lambda conj(q) q
    q = (z, y)
    check("Q3  the word q j Lambda conj(q) q is left-equivariant for general q and gives j Lambda z conj(z)^2 on Pi_par",
          word(qmul(lamq, q)) == qmul(lamq, word(q)) and word(zq) == (ZERO, Lm * z * z.conj() * z.conj()))
    lin = lambda q: qmul(jq, qmul(Lq, qconj(q)))                  # j Lambda conj(q)
    check("CONTROL-Q4 the full-space linear word j Lambda conj(q) is NOT left-equivariant off Pi_par "
          "(the minimal coupling is a statement on Pi_par only)", lin(qmul(lamq, q)) != qmul(lamq, lin(q)))

    # ---- C0: passive transport control, update form
    # model on (x, y), y complex scalar fibre coordinate:  U(x, y) = (b(x), s(x) + m(x) y)
    def run(bmap, s, m, steps):
        """y after `steps` steps from (x, 0), and the base point, as jets in the initial x."""
        xk, yk = X, {}
        for _ in range(steps):
            yk = jadd(compose(s, xk), jmul(compose(m, xk), yk)) if xk else {}
            xk = compose(bmap, xk)
        return xk, yk

    def transport(bmap, s, m, phi, g, form="update"):
        """push the model forward by Psi(x, y) = (phi(x), g(x) y)."""
        phinv = inverse_map(phi)
        b2 = compose(phi, compose(bmap, phinv))
        g_at = compose(g, bmap) if form == "update" else g        # g at the image point (update form)
        s2 = compose(jmul(g_at, s), phinv)
        m2 = compose(jmul(jmul(g_at, m), recip(g)), phinv)
        return b2, s2, m2

    Lam0 = K(Fr(2, 3), Fr(1, 5))
    mfun = {(0, 0): K(Fr(1, 2)), (1, 0): K(Fr(1, 3), Fr(1, 7)), (0, 1): K(Fr(-2, 5))}
    gfun = {(0, 0): ONE, (1, 0): K(Fr(1, 4), Fr(-1, 9)), (0, 1): K(Fr(3, 8), Fr(2, 3))}
    nhat = compose(hinv, compose(f, h))                           # base map in the NF chart
    check("C0-0 base map in the NF chart equals the normal form n through degree 6", nhat == n)

    def c0(label, bmap, s, m, phi, g, form="update"):
        b2, s2, m2 = transport(bmap, s, m, phi, g, form)
        ok = True
        for steps in (1, 2, 3):
            xk, yk = run(bmap, s, m, steps)
            # transported run started at Psi(x, 0) = (phi(x), 0), expressed in the initial x
            Xk, Yk = phi, {}
            for _ in range(steps):
                Yk = jadd(compose(s2, Xk), jmul(compose(m2, Xk), Yk))
                Xk = compose(b2, Xk)
            # transported observable  O~ = y'/g(phi^{-1}(X'))  against  O = y
            back = jmul(Yk, recip(compose(g, xk)))
            ok = ok and (back == yk) and (Xk == compose(phi, xk))
        return ok

    sNF = jscale(Lam0, {(0, 1): ONE})
    check("C0-1 NF -> W, fixed trivialization (g = 1): transported model reproduces the observable, steps 1..3",
          c0("nf->w g=1", nhat, sNF, mfun, h, CONST1))
    check("C0-2 NF -> W with a fibre re-trivialization g(x): update-form rule s~ = g(b x) s(x) reproduces it",
          c0("nf->w g", nhat, sNF, mfun, h, gfun))
    sW = jscale(Lam0, {(0, 1): ONE})
    check("C0-3 W -> NF, fixed trivialization: transported model reproduces the observable",
          c0("w->nf g=1", f, sW, mfun, hinv, CONST1))
    check("C0-4 W -> NF with a fibre re-trivialization: update-form rule reproduces it",
          c0("w->nf g", f, sW, mfun, hinv, gfun))
    check("CONTROL-C0-5 section-form rule s~ = g(x) s(x) with nonconstant g is detected as wrong",
          not c0("section", nhat, sNF, mfun, h, gfun, form="section"))
    # re-imposed ansatz instead of the transported source
    b2, s2, m2 = transport(nhat, sNF, mfun, h, CONST1)
    check("CONTROL-C0-6 re-imposing Lambda conj(W) in the raw frame differs from the transported source at degree 2",
          jpart(jsub(s2, sW), 2) == jscale(Lam0, exp_p3) and not jpart(jsub(s2, sW), 1))

    # ---- negative control on the engine: a perturbed h_2 breaks P2
    hbad, _ = normalizer(f, perturb=((2, 0), K(Fr(1, 1000))))
    Jbad = compose(inverse_map(hbad), compose(JW, hbad))
    check("CONTROL-P2 a perturbed h_2 coefficient is detected: generator no longer linear in that chart",
          Jbad != {(1, 0): LAM})

    npass = sum(1 for r in RESULTS if r["pass"])
    out["summary"] = {"checks": len(RESULTS), "passed": npass, "failed": len(RESULTS) - npass}
    print("\nSUMMARY: %d checks, %d passed, %d failed" % (len(RESULTS), npass, len(RESULTS) - npass))
    if "--json" in sys.argv:
        with open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8") as fh:
            json.dump(out, fh, indent=1, sort_keys=True, ensure_ascii=True)
            fh.write("\n")
    return 0 if npass == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
