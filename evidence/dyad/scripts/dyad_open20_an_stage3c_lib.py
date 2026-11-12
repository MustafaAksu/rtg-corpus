#!/usr/bin/env python3
"""dyad_open20_an_stage3c_lib.py -- OPEN 20 analytic branch, stage 3c-a: ball-arithmetic engine for the tube certificate.

Stage 3c-a (authorized by the PI on 11 November 2026): proof record and certificate script, WITHOUT a certification
claim.  This module is the engine only.  Nothing computed with it is a certificate until stage 3c-b is authorized, run
with fixed commands and reviewed.  Design: records/dyad/DYAD_OPEN20_AN_STAGE3B_DESIGN.md r2; plan and progress:
records/dyad/DYAD_OPEN20_AN_STAGE3C_A_PLAN.md.

All arithmetic is python-flint ball arithmetic (arb/acb): a ball is a rigorous enclosure of the exact value.

Architecture (plan record section 2).  Every one-step quantity of the tube lemma is needed on the tube around the
truncated series, i.e. at points (z, w) = (x, phi_N(x) + x^2 d) with small d.  Along the curve d = 0 these are
functions of ONE complex variable x, and F = T^6 is entire.  So they are represented by their power series in x at
x = 0, with ball coefficients, a truncation degree D and a rigorous tail bound; the dependence on d is carried as a
jet in d.  The cancellation in F - id is then exact: the low coefficients vanish identically.

Provided in this first part (work package W1):
  Consts        exact constants of the pilot branch (stage 1) as balls
  coefficients  the balls a_2..a_N of the formal curve, by the exact recursion of stage 2
  curve_image   the series of Z = F_z(x, phi_N(x)) and W = F_w(x, phi_N(x)) to degree D
  residual      the series of the raw truncation defect  W - phi_N(Z)
The jets in d, the tail bounds, the box evaluation and the inverse map follow in W2.
"""
import os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from flint import acb, arb
import dyad_open20_an_stage2_scout as S2


class Consts:
    """Exact constants of the pilot branch (stage 1), as balls at the current precision."""
    def __init__(self):
        s3 = arb(3).sqrt()

        def Q(p, q):
            return acb(arb(p.numerator) / p.denominator, (arb(q.numerator) / q.denominator) * s3)
        self.MU = Q(Fr(-1, 2), Fr(-2, 3)); self.C40 = Q(Fr(-1, 16), Fr(7, 144))
        self.D31 = Q(Fr(1, 3), Fr(-1, 9)); self.CC = Q(Fr(-61, 2160), Fr(43, 6480))
        self.A = self.MU.conjugate() - 2 * self.MU; self.B = self.D31 - 2 * self.C40
        self.KSTAR = Q(Fr(-64, 19), Fr(-16, 19)); self.ALPHA = Q(Fr(-102, 19), Fr(-16, 19))
        self.OM = Q(Fr(-1, 2), Fr(1, 2)); self.OMB = self.OM.conjugate(); self.DEN = self.OM - self.OMB
        disc = self.B * self.B - 4 * self.A * self.CC
        self.a = (-self.B - disc.sqrt()) / (2 * self.A)            # pilot root, Im a > 0 (stage-1 gate S1)
        assert self.a.imag > 0
        self.ell = self.C40 + self.MU * self.a
        self.c = (-self.ell) ** (acb(1) / 3)                       # principal cube root; xi = c x
        assert self.c.real > 0 and self.c.imag > 0


def curve_image(K, phi, nn):
    """Coefficient lists (length nn) of Z(x) = F_z(x, phi(x)) and W(x) = F_w(x, phi(x)) for the curve w = phi(z) given
    by its coefficient list.  The six steps of T act on the series (stage-2 routines); the full map is used."""
    zser = [acb(0), acb(1)] + [acb(0)] * (nn - 2); wser = list(phi[:nn]) + [acb(0)] * (nn - len(phi))
    eta = [(zser[k] - wser[k]) / K.DEN for k in range(nn)]; rho = [zser[k] - K.OM * eta[k] for k in range(nn)]
    for _ in range(6):
        rho, eta = S2.T_step(rho, eta, nn)
    return [rho[k] + K.OM * eta[k] for k in range(nn)], [rho[k] + K.OMB * eta[k] for k in range(nn)]


def residual(K, phi, nn):
    """Coefficient list of the raw invariance defect W(x) - phi(Z(x)) (P1-c convention), length nn."""
    Z, W = curve_image(K, phi, nn)
    comp = S2.compose_phi(list(phi) + [acb(0)] * (nn - len(phi)), Z, nn)
    return [W[k] - comp[k] for k in range(nn)]


def coefficients(K, N):
    """Balls a_0..a_N of the formal curve w = sum a_k z^k (a_0 = a_1 = 0, a_2 = a_pil): the exact recursion of stage 2,
    a_k = -R_k / (ell (k* - k)), with R_k the order-(k+3) coefficient of the defect computed with a_k = 0 (P1-c)."""
    phi = [acb(0), acb(0), K.a] + [acb(0)] * (N + 1)
    for k in range(3, N + 1):
        phi[k] = -residual(K, phi, k + 4)[k + 3] / (K.ell * (K.KSTAR - k))
    return phi[:N + 1]


# ----------------------------------------------------------------------------------------------------------------------
# Work package W2 (first half): jets in d, order-zero series, tail bounds, evaluation on discs.
#
# Input point of the map: (z, w) = (x, phi_N(x) + x^2 d).  Z(x, d), W(x, d) are its images under F = T^6.
#   Z0, W0 = Z, W at d = 0;   Z1, W1 = dZ/dd, dW/dd at d = 0   (all entire functions of x).
# Order-zero series (entire; the divisions are exact by the structural facts S1-S4 below):
#   G0   = (Z0 - x) / x^4                                   g = x^3 G0 = x'/x - 1
#   Q4   = Z1 / x^4                                          d x'/dd at d = 0, divided by x^4
#   M3   = ((W1 - phi_N'(Z0) Z1) / x^2 - 1) / x^3            numerator of the normal multiplier, see step quantities
#   ET44 = (W0 - phi_N(Z0)) / x^44                           raw truncation defect, divided by x^44
# Structural facts (exact; their proofs are in the proof record, W7):
#   S1  F_z(z, w) - z has only monomials z^p w^q with p + 2q >= 4 (stage 1; gate H4 of the INF-014/015 check), and
#       phi_N = O(x^2): so Z0 - x = O(x^4).
#   S2  dF_z/dw has only monomials with p + 2q >= 2: so Z1 = x^2 dF_z/dw = O(x^4).
#   S3  dF_w/dw - 1 has only monomials with p + 2q >= 3, and phi_N'(Z0) Z1 = O(x^5): so the bracket of M3 is O(x^3).
#   S4  a_2..a_N are the exact formal coefficients: the order-(k+3) coefficient of the defect is affine in a_k with slope
#       ell (k* - k) and does not depend on a_j, j > k (P1-c); orders 0..4 vanish by S1 and its analogue for F_w.  So
#       the raw defect is O(x^(N+4)) = O(x^44).
# In ball arithmetic the vanishing coefficients come out as small balls around 0.  A ball that contains 0 does not
# prove that a coefficient is 0; S1-S4 do.  The code sets these coefficients to 0 on the strength of S1-S4 and reports,
# as a consistency check only, whether the balls contained 0.
from flint import acb_poly, ctx


def _exp_pm(s, n):
    I = acb(0, 1)
    ep = S2.exp_series([t * I for t in s], n); em = S2.exp_series([-(t * I) for t in s], n)
    return [(ep[k] - em[k]) / (2 * I) for k in range(n)], [(ep[k] + em[k]) / 2 for k in range(n)]


def jet_curve_image(K, phi, nn):
    """Coefficient lists (length nn) of Z0, W0, Z1, W1 for the input (x, phi(x) + x^2 d)."""
    z0 = [acb(0), acb(1)] + [acb(0)] * (nn - 2); w0 = list(phi[:nn]) + [acb(0)] * (nn - len(phi))
    z1 = [acb(0)] * nn; w1 = [acb(0), acb(0), acb(1)] + [acb(0)] * (nn - 3)
    e0 = [(z0[k] - w0[k]) / K.DEN for k in range(nn)]; r0 = [z0[k] - K.OM * e0[k] for k in range(nn)]
    e1 = [(z1[k] - w1[k]) / K.DEN for k in range(nn)]; r1 = [z1[k] - K.OM * e1[k] for k in range(nn)]
    for _ in range(6):
        sn, cs = _exp_pm(e0, nn)
        ex = S2.exp_series(r0, nn)                       # r0 has no constant term
        s1 = S2.mul(cs, e1, nn); x1 = S2.mul(ex, r1, nn)
        r0, e0, r1, e1 = ([r0[k] - sn[k] for k in range(nn)], [e0[k] + ex[k] - (1 if k == 0 else 0) - sn[k] for k in range(nn)],
                          [r1[k] - s1[k] for k in range(nn)], [e1[k] + x1[k] - s1[k] for k in range(nn)])
    Z0 = [r0[k] + K.OM * e0[k] for k in range(nn)]; W0 = [r0[k] + K.OMB * e0[k] for k in range(nn)]
    Z1 = [r1[k] + K.OM * e1[k] for k in range(nn)]; W1 = [r1[k] + K.OMB * e1[k] for k in range(nn)]
    return Z0, W0, Z1, W1


def order_zero_series(K, a, D):
    """The four order-zero series as coefficient lists of length D + 1, and the consistency report."""
    N = len(a) - 1
    nn = D + N + 5
    Z0, W0, Z1, W1 = jet_curve_image(K, a, nn)
    phi = list(a) + [acb(0)] * (nn - len(a))
    dphi = [a[k + 1] * (k + 1) for k in range(N)] + [acb(0)] * (nn - N)
    comp = S2.compose_phi(phi, Z0, nn); dcomp = S2.compose_phi(dphi, Z0, nn)
    et = [W0[k] - comp[k] for k in range(nn)]
    prod = S2.mul(dcomp, Z1, nn)
    br = [W1[k] - prod[k] for k in range(nn)]             # W1 - phi'(Z0) Z1 = x^2 (1 + x^3 M3)
    zero = lambda v: bool(v.contains(acb(0)))
    report = dict(
        S1_Z0_minus_x=all(zero(Z0[k]) for k in (0, 2, 3)) and zero(Z0[1] - 1),
        S2_Z1=all(zero(Z1[k]) for k in range(4)),
        S3_bracket=zero(br[0]) and zero(br[1]) and zero(br[2] - 1) and zero(br[3]) and zero(br[4]),
        S4_defect=all(zero(et[k]) for k in range(N + 4)),
        max_radius_of_vanishing_coefficients=max([float(Z0[k].rad()) for k in (0, 2, 3)] + [float(Z1[k].rad()) for k in range(4)]
                                                 + [float(et[k].rad()) for k in range(N + 4)]))
    ser = dict(G0=Z0[4:4 + D + 1], Q4=Z1[4:4 + D + 1], M3=br[5:5 + D + 1], ET44=et[N + 4:N + 4 + D + 1])
    return ser, report


class D2:
    """Value, first and second x-derivative of a holomorphic function of x (entries acb: points or balls)."""
    __slots__ = ('v', 'd', 'e')

    def __init__(self, v, d=0, e=0):
        self.v, self.d, self.e = acb(v), acb(d), acb(e)

    def __add__(s, o):
        return D2(s.v + o.v, s.d + o.d, s.e + o.e) if isinstance(o, D2) else D2(s.v + o, s.d, s.e)
    __radd__ = __add__

    def __sub__(s, o):
        return D2(s.v - o.v, s.d - o.d, s.e - o.e) if isinstance(o, D2) else D2(s.v - o, s.d, s.e)

    def __mul__(s, o):
        if not isinstance(o, D2):
            return D2(s.v * o, s.d * o, s.e * o)
        return D2(s.v * o.v, s.d * o.v + s.v * o.d, s.e * o.v + 2 * s.d * o.d + s.v * o.e)
    __rmul__ = __mul__

    def comp(s, g0, g1, g2):
        return D2(g0, g1 * s.d, g2 * s.d * s.d + g1 * s.e)

    def sin(s):
        sn, cs = s.v.sin(), s.v.cos()
        return s.comp(sn, cs, -sn)

    def cos(s):
        sn, cs = s.v.sin(), s.v.cos()
        return s.comp(cs, -sn, -cs)

    def exp(s):
        e = s.v.exp()
        return s.comp(e, e, e)


def raw_jet_arc(K, a, xc, rad):
    """Enclosures of Z0, W0, Z1, W1 on the ball |x - xc| <= rad (xc a point).  The six steps are carried with the first
    and second x-derivative, at the centre and on the ball.  After every step the enclosures on the ball are replaced
    by their mean-value forms,  f'(x) in f'(xc) + f''(ball) h  and  f(x) in f(xc) + f'(ball) h,  |h| <= rad, which
    stops the growth of the balls through the steps.  Used for sup bounds on circles."""
    N = len(a) - 1
    h = acb(arb(0, rad), arb(0, rad))

    def start(x):
        X = D2(x, 1)
        w0 = D2(0)
        for k in range(N, 1, -1):
            w0 = w0 * X + a[k]
        w0 = w0 * X * X
        z0, z1, w1 = X, D2(0), X * X
        e0 = (z0 - w0) * (1 / K.DEN); r0 = z0 - e0 * K.OM
        e1 = (z1 - w1) * (1 / K.DEN); r1 = z1 - e1 * K.OM
        return [r0, e0, r1, e1]

    def step(q):
        r0, e0, r1, e1 = q
        s, c, E = e0.sin(), e0.cos(), r0.exp()
        s1 = c * e1; x1 = E * r1
        return [r0 - s, e0 + E - 1 - s, r1 - s1, e1 + x1 - s1]

    def tight(qb, qc):
        for b, c in zip(qb, qc):
            b.d = c.d + b.e * h
            b.v = c.v + b.d * h
        return qb
    qc = start(xc); qb = tight(start(xc + h), qc)
    for _ in range(6):
        qc = step(qc); qb = tight(step(qb), qc)
    r0, e0, r1, e1 = qb
    return (r0 + e0 * K.OM).v, (r0 + e0 * K.OMB).v, (r1 + e1 * K.OM).v, (r1 + e1 * K.OMB).v, xc + h


def circle_sup(K, a, X, narc):
    """Rigorous Cauchy constants M for the four order-zero series, from sup bounds on the circle |x| = X.
    Each series is (P1 - P2) / x^p with P1, P2 entire, so its k-th coefficient is bounded by
    (sup|P1| + sup|P2|) / X^(k + p).  The pieces are bounded separately (no cancellation between them is needed):
        G0   = (Z0 - x) / x^4                      M = (sup|Z0| + X) / X^4
        Q4   = Z1 / x^4                            M = sup|Z1| / X^4
        M3   = (W1 - phi'(Z0) Z1 - x^2) / x^5      M = (sup|W1| + sup|phi'(Z0) Z1| + X^2) / X^5
        ET44 = (W0 - phi(Z0)) / x^44               M = (sup|W0| + sup|phi(Z0)|) / X^44
    The circle is covered by narc balls (raw_jet_arc).  Returns the constants and the sup bounds, as floats rounded up."""
    N = len(a) - 1
    half = arb.pi() / narc
    rad_arc = float((arb(X) * half * 1.0001).upper())
    sup = dict(Z0=0.0, W0=0.0, Z1=0.0, W1=0.0, phiZ=0.0, dphiZ_Z1=0.0)
    for i in range(narc):
        c = acb(X) * (acb(0, 1) * (2 * i + 1) * half).exp()
        xc = acb(c.real.mid(), c.imag.mid())
        Z0, W0, Z1, W1, x = raw_jet_arc(K, a, xc, rad_arc)
        p = acb(0); dp = acb(0)
        for k in range(N, 1, -1):
            p = p * Z0 + a[k]; dp = dp * Z0 + a[k] * k
        p = p * Z0 * Z0; dp = dp * Z0
        for k, v in dict(Z0=Z0, W0=W0, Z1=Z1, W1=W1, phiZ=p, dphiZ_Z1=dp * Z1).items():
            u = float(abs(v).upper())
            if not u == u or u == float('inf'):
                raise ArithmeticError('circle_sup: enclosure not finite; use more arcs')
            sup[k] = max(sup[k], u)
    up = 1 + 1e-12
    M = dict(G0=(sup['Z0'] + X) / X ** 4 * up, Q4=sup['Z1'] / X ** 4 * up,
             M3=(sup['W1'] + sup['dphiZ_Z1'] + X ** 2) / X ** 5 * up, ET44=(sup['W0'] + sup['phiZ']) / X ** 44 * up)
    return M, sup


class Series:
    """An entire function given by D + 1 ball coefficients, with the Cauchy bound |c_k| <= M / X^k for k > D
    (M an upper bound of the function on |x| = X)."""
    def __init__(self, coeffs, X, M):
        self.poly = acb_poly(coeffs); self.D = len(coeffs) - 1; self.X = float(X); self.M = float(M)

    def tail(self, r):
        """Upper bound of |sum_{k > D} c_k x^k| on |x| <= r < X."""
        t = arb(r) / arb(self.X)
        assert t < 1
        return arb(self.M) * t ** (self.D + 1) / (1 - t)

    def enclose(self, xc, r):
        """A ball containing the function on the disc |x - xc| <= r (Taylor shift to xc, then the sum of the moduli)."""
        sh = self.poly(acb_poly([xc, 1]))
        co = sh.coeffs()
        rr = arb(r); acc = arb(0); pw = arb(1)
        for j in range(1, len(co)):
            pw = pw * rr
            acc += arb(abs(co[j]).upper()) * pw
        tot = acc + self.tail((abs(xc) + rr).upper())
        e = arb(0, arb(tot.upper()))
        return co[0] + acb(e, e)

    def point(self, x):
        """Enclosure at a point or small ball x (direct evaluation plus the tail)."""
        t = self.tail(abs(x).upper()); e = arb(0, arb(t.upper()))
        return self.poly(x) + acb(e, e)


def log1p_over(g):
    """Enclosure of log(1 + g) / g for a ball g with |g| <= 1/4 (alternating series, 24 terms and the geometric tail)."""
    ag = arb(abs(g).upper())
    assert ag < 0.25
    acc = acb(0); pw = acb(1)
    for k in range(24):
        acc += pw * (1 if k % 2 == 0 else -1) / (k + 1)
        pw = pw * g
    t = ag ** 24 / (1 - ag); e = arb(0, arb(t.upper()))
    return acc + acb(e, e)


def step_quantities(SER, TAU, xc, r):
    """One step of F at d = 0, on the disc |x - xc| <= r.  SER: dict of Series (G0, Q4, M3, ET44).  TAU = (A3, A2, A1,
    kappa), the fixed coefficients of the four-term Fatou coordinate tau(x) = A3 x^-3 + A2 x^-2 + A1 x^-1 + kappa log x.
    Returns enclosures (acb) of
        g      = x'/x - 1
        dtau   = tau(x') - tau(x)
        mu0    = d d'/dd at d = 0            = (1 + x^3 M3)/(1 + g)^2 - 2 x^45 ET44 Q4/(1 + g)^3
        E      = d'(x, 0), the lifted defect = x^42 ET44/(1 + g)^2
        dxdd   = d x'/dd at d = 0            = x^4 Q4
    and of x itself."""
    rr = arb(r); x = xc + acb(arb(0, rr), arb(0, rr))
    G0, Q4, M3, ET = (SER[k].enclose(xc, r) for k in ('G0', 'Q4', 'M3', 'ET44'))
    x2 = x * x; x3 = x2 * x
    g = x3 * G0
    A3, A2, A1, KA = TAU
    og = 1 + g
    dtau = G0 * (-A3 * (3 + 3 * g + g * g) / (og * og * og) - A2 * x * (2 + g) / (og * og) - A1 * x2 / og + KA * x3 * log1p_over(g))
    x42 = x3 ** 14
    mu0 = (1 + x3 * M3) / (og * og) - 2 * x42 * x3 * ET * Q4 / (og * og * og)
    return dict(x=x, g=g, dtau=dtau, mu0=mu0, E=x42 * ET / (og * og), dxdd=x2 * x2 * Q4, G0=G0)


# The four-term Fatou coordinate of the certificate.  It is a fixed explicit function: its coefficients are these exact
# decimals (the stage-2b values rounded to 15 digits).  Nothing in the tube lemma requires them to solve the Abel
# equation; they only have to make the inequalities (A1), (B) hold.
TAU_DECIMALS = (('-3.32788058725899', '-0.681896765229739'), ('0.536700186091055', '1.61148875597112'),
                ('-0.135079834899795', '0.153567697075599'), ('1.81162096236788', '0.0896653995437725'))


def tau_coefficients():
    return tuple(acb(arb(re), arb(im)) for re, im in TAU_DECIMALS)
