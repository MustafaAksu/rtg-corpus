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
W2a (further down): first-order jets in d, the order-zero series, Cauchy constants and tails, evaluation on discs.
W2b (last part): second-order jets, the remainder in d (d_remainder_constants), the step on a tube piece (tube_step),
and the local inverse lemma (inverse_conditions, inverse_step).
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


def _up(v):
    """Upper bound of |v| (v acb or arb), as an arb."""
    return arb(abs(v).upper())


def _tm_step_bound(qb, Br, Be, rho):
    """Remainder bounds of one step of T for the Taylor model in d of order two.
    Input: rho = r0 + r1 d + r2 d^2 + (remainder of modulus <= Br), eta likewise with Be, valid for |d| <= rho and x on
    the ball; qb are the enclosures of the six jets on the ball.  With delta = e1 d + e2 d^2 + remainder,
        sin(e0 + delta) = sin e0 + cos e0 delta - sin e0 delta^2 / 2 + R,   |R| <= cosh(|Im e0| + |delta|) |delta|^3 / 6,
        exp(r0 + delta) = exp(r0) (1 + delta + delta^2 / 2 + R),            |R| <= exp(|delta|) |delta|^3 / 6,
    and delta^2 - e1^2 d^2 is bounded term by term.  Returns the bounds for the image (rho - sin eta,
    eta + exp(rho) - 1 - sin eta)."""
    r0, e0, r1, e1, r2, e2 = (t.v for t in qb)

    def parts(c1, c2, B):
        a1, a2 = _up(c1), _up(c2)
        lin = a1 * rho + a2 * rho ** 2
        return lin + B, 2 * a1 * a2 * rho ** 3 + a2 ** 2 * rho ** 4 + 2 * lin * B + B ** 2
    De, qe = parts(e1, e2, Be)
    Bs = _up(e0.cos()) * Be + _up(e0.sin()) * qe / 2 + (_up(e0.imag) + De).cosh() * De ** 3 / 6
    Dr, qr = parts(r1, r2, Br)
    BE = _up(r0.exp()) * (Br + qr / 2 + Dr.exp() * Dr ** 3 / 6)
    return arb((Br + Bs).upper()), arb((Be + BE + Bs).upper())


def raw_jet_arc(K, a, xc, rad, rho=None):
    """Enclosures of Z0, W0, Z1, W1, Z2, W2 (the jets in d up to second order) on the ball |x - xc| <= rad (xc a point).
    The six steps are carried with the first and second x-derivative, at the centre and on the ball.  After every step
    the enclosures on the ball are replaced by their mean-value forms,  f'(x) in f'(xc) + f''(ball) h  and
    f(x) in f(xc) + f'(ball) h,  |h| <= rad, which stops the growth of the balls through the steps.  Used for sup
    bounds on circles.
    With rho (an arb), two more entries are returned: bounds BZ, BW with
        |Z(x, d) - Z0 - Z1 d - Z2 d^2| <= BZ,   |W(x, d) - W0 - W1 d - W2 d^2| <= BW   for x on the ball and |d| <= rho
    (a Taylor model in d of order two; _tm_step_bound)."""
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
        return [r0, e0, r1, e1, D2(0), D2(0)]

    def step(q):
        r0, e0, r1, e1, r2, e2 = q
        s, c, E = e0.sin(), e0.cos(), r0.exp()
        s1 = c * e1; x1 = E * r1
        s2 = c * e2 - s * (e1 * e1) * acb(0.5); x2 = E * (r2 + (r1 * r1) * acb(0.5))
        return [r0 - s, e0 + E - 1 - s, r1 - s1, e1 + x1 - s1, r2 - s2, e2 + x2 - s2]

    def tight(qb, qc):
        for b, c in zip(qb, qc):
            b.d = c.d + b.e * h
            b.v = c.v + b.d * h
        return qb
    qc = start(xc); qb = tight(start(xc + h), qc)
    Br = Be = arb(0)
    for _ in range(6):
        if rho is not None:
            Br, Be = _tm_step_bound(qb, Br, Be, rho)
        qc = step(qc); qb = tight(step(qb), qc)
    out = []
    for r, e in ((qb[0], qb[1]), (qb[2], qb[3]), (qb[4], qb[5])):
        out += [(r + e * K.OM).v, (r + e * K.OMB).v]
    out.append(xc + h)
    if rho is not None:
        out += [Br + _up(K.OM) * Be, Br + _up(K.OMB) * Be]
    return out


def _arcs(X, narc):
    """Centres and the common radius of narc balls covering the circle |x| = X: the centre of ball i is (a point close
    to) the midpoint of arc i, and the radius 1.0001 X pi / narc exceeds the half-length of the arc."""
    half = arb.pi() / narc
    rad_arc = float((arb(X) * half * 1.0001).upper())
    for i in range(narc):
        c = acb(X) * (acb(0, 1) * (2 * i + 1) * half).exp()
        yield acb(c.real.mid(), c.imag.mid()), rad_arc


def _phi_at(a, Z0, order):
    """phi_N and its derivatives up to `order` (at most 2) on the ball Z0, by Horner."""
    N = len(a) - 1
    p = acb(0); dp = acb(0); ddp = acb(0)
    for k in range(N, 1, -1):
        ddp = ddp * Z0 + a[k] * (k * (k - 1)); dp = dp * Z0 + a[k] * k; p = p * Z0 + a[k]
    return (p * Z0 * Z0, dp * Z0, ddp)[:order + 1]


def circle_sup(K, a, X, narc, second=False):
    """Rigorous Cauchy constants M for the order-zero series, from sup bounds on the circle |x| = X.
    Each series is (P1 - P2 - ...) / x^p with entire pieces, so its k-th coefficient is bounded by
    (sum of the sup bounds of the pieces) / X^(k + p).  The pieces are bounded separately (no cancellation between
    them is needed):
        G0   = (Z0 - x) / x^4                                  M = (sup|Z0| + X) / X^4
        Q4   = Z1 / x^4                                        M = sup|Z1| / X^4
        M3   = (W1 - phi'(Z0) Z1 - x^2) / x^5                  M = (sup|W1| + sup|phi'(Z0) Z1| + X^2) / X^5
        ET44 = (W0 - phi(Z0)) / x^44                           M = (sup|W0| + sup|phi(Z0)|) / X^44
    and, with second=True, for the two series of second order in d:
        P4   = Z2 / x^4                                        M = sup|Z2| / X^4
        S2   = (W2 - phi'(Z0) Z2 - phi''(Z0) Z1^2 / 2) / x^5   M = (sup|W2| + sup|phi'(Z0) Z2| + sup|phi''(Z0) Z1^2| / 2) / X^5
    The circle is covered by narc balls (_arcs, raw_jet_arc).  By the maximum principle the bounds hold on the disc.
    Upper bounds are converted to floats and multiplied by 1 + 1e-12, which covers the rounding of the conversion.
    Returns the constants and the sup bounds."""
    names = ('Z0', 'W0', 'Z1', 'W1', 'phiZ', 'dphiZ_Z1') + (('Z2', 'W2', 'dphiZ_Z2', 'ddphiZ_Z1sq') if second else ())
    sup = dict.fromkeys(names, 0.0)
    for xc, rad_arc in _arcs(X, narc):
        Z0, W0, Z1, W1, Z2, W2, x = raw_jet_arc(K, a, xc, rad_arc)
        p, dp, ddp = _phi_at(a, Z0, 2)
        vals = dict(Z0=Z0, W0=W0, Z1=Z1, W1=W1, phiZ=p, dphiZ_Z1=dp * Z1)
        if second:
            vals.update(Z2=Z2, W2=W2, dphiZ_Z2=dp * Z2, ddphiZ_Z1sq=ddp * Z1 * Z1)
        for k, v in vals.items():
            u = float(abs(v).upper())
            if not u == u or u == float('inf'):
                raise ArithmeticError('circle_sup: enclosure not finite; use more arcs')
            sup[k] = max(sup[k], u)
    up = 1 + 1e-12
    sup = {k: v * up for k, v in sup.items()}
    M = dict(G0=(sup['Z0'] + X) / X ** 4 * up, Q4=sup['Z1'] / X ** 4 * up,
             M3=(sup['W1'] + sup['dphiZ_Z1'] + X ** 2) / X ** 5 * up, ET44=(sup['W0'] + sup['phiZ']) / X ** 44 * up)
    if second:
        M.update(P4=sup['Z2'] / X ** 4 * up, S2=(sup['W2'] + sup['dphiZ_Z2'] + sup['ddphiZ_Z1sq'] / 2) / X ** 5 * up)
    return M, sup


class Series:
    """An entire function given by D + 1 ball coefficients, with the Cauchy bound |c_k| <= M / X^k for k > D
    (M an upper bound of the function on |x| = X)."""
    def __init__(self, coeffs, X, M):
        self.poly = acb_poly(coeffs); self.D = len(coeffs) - 1; self.X = float(X); self.M = float(M)
        self.dpoly = self.poly.derivative()

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

    def enclose_derivative(self, xc, r):
        """A ball containing the derivative on the disc |x - xc| <= r.  The tail of the derivative is bounded by
        sum_{k > D} k M t^(k-1) / X = (M / X) ((D + 1) t^D (1 - t) + t^(D+1)) / (1 - t)^2,  t = (|xc| + r) / X."""
        sh = self.poly(acb_poly([xc, 1]))
        co = sh.coeffs()
        rr = arb(r); acc = arb(0); pw = arb(1)
        for j in range(2, len(co)):
            pw = pw * rr
            acc += j * arb(abs(co[j]).upper()) * pw
        t = arb((abs(xc) + rr).upper()) / arb(self.X)
        assert t < 1
        tl = arb(self.M) / arb(self.X) * ((self.D + 1) * t ** self.D * (1 - t) + t ** (self.D + 1)) / (1 - t) ** 2
        e = arb(0, arb((acc + tl).upper()))
        return (co[1] if len(co) > 1 else acb(0)) + acb(e, e)

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


# ----------------------------------------------------------------------------------------------------------------------
# Work package W2b: second-order jets in d, the remainder in d, the one-step quantities on the tube, and the local
# inverse.  (The formal inverse along the curve is kept only to reproduce a recorded finding: its coefficients grow, so
# it is not used; plan record 2.5.)
#
# Second-order series (entire, by S5):  P4 = Z2 / x^4,  S2 = (W2 - phi_N'(Z0) Z2 - phi_N''(Z0) Z1^2 / 2) / x^5, with
# Z2, W2 the d^2 coefficients of Z, W.
# Structural fact S5 (exact; proof in the proof record, W7).  With weights (1, 2) for (z, w):  F_z - z has only
# monomials z^p w^q with p + 2q >= 4 (this is S1), and F_w - w only monomials with p + 2q >= 5.  Consequences at the
# input (x, phi_N(x) + x^2 d):  (Z - x)/x^4 and (W - phi_N(x) - x^2 d)/x^5 are entire functions of (x, d);  where
# Z/x != 0 the lifted deviation Phi = (W - phi_N(Z))/Z^2 satisfies Phi - d = x^3 (analytic in (x, d)).  S2, S3 and the
# regularity of P4 and of the series S2 are the instances of S5 at orders 1 and 2 in d.
#
# A "jet" is a triple of coefficient lists (s0, s1, s2): the series s0(x) + d s1(x) + d^2 s2(x), truncated at d^3.
def _jmul(a, b, n):
    return (S2.mul(a[0], b[0], n),
            [p + q for p, q in zip(S2.mul(a[0], b[1], n), S2.mul(a[1], b[0], n))],
            [p + q + r for p, q, r in zip(S2.mul(a[0], b[2], n), S2.mul(a[1], b[1], n), S2.mul(a[2], b[0], n))])


def _jlin(c1, a, c2, b):
    return tuple([c1 * p + c2 * q for p, q in zip(a[i], b[i])] for i in range(3))


def jet_T_step(r, e, n):
    """One step of T on jets r = rho, e = eta (triples of lists; the order-zero parts have no constant term)."""
    sn, cs = _exp_pm(e[0], n); ex = S2.exp_series(r[0], n)
    e1sq = S2.mul(e[1], e[1], n); r1sq = S2.mul(r[1], r[1], n)
    s = (sn, S2.mul(cs, e[1], n), [p - q / 2 for p, q in zip(S2.mul(cs, e[2], n), S2.mul(sn, e1sq, n))])
    x = ([ex[k] - (1 if k == 0 else 0) for k in range(n)], S2.mul(ex, r[1], n),
         S2.mul(ex, [p + q / 2 for p, q in zip(r[2], r1sq)], n))
    return (tuple([p - q for p, q in zip(r[i], s[i])] for i in range(3)),
            tuple([p + q - t for p, q, t in zip(e[i], x[i], s[i])] for i in range(3)))


def jet_image(K, zj, wj, n):
    """Jets of (Z, W) = F(z, w) for input jets zj, wj (triples of lists of length n)."""
    e = tuple([(p - q) / K.DEN for p, q in zip(zj[i], wj[i])] for i in range(3))
    r = tuple([p - K.OM * q for p, q in zip(zj[i], e[i])] for i in range(3))
    for _ in range(6):
        r, e = jet_T_step(r, e, n)
    return (tuple([p + K.OM * q for p, q in zip(r[i], e[i])] for i in range(3)),
            tuple([p + K.OMB * q for p, q in zip(r[i], e[i])] for i in range(3)))


def ser_inv(s, n):
    """1/s for a series with s[0] != 0 (Newton iteration y <- y (2 - s y); exact modulo x^n after log2(n) steps)."""
    y = [1 / s[0]] + [acb(0)] * (n - 1)
    m = 1
    while m < n:
        m *= 2
        t = S2.mul(s, y, n)
        t = [(2 if k == 0 else 0) - t[k] for k in range(n)]
        y = S2.mul(y, t, n)
    return y


def inverse_curve(K, phi, n):
    """Order-zero series (z0, w0) of the formal inverse along the curve: F(z0(x), w0(x)) = (x, phi(x)).  Each of the six
    inverse steps of T solves  eta + expm1(rho' + sin eta) - sin eta = eta'  for the series eta by Newton iteration,
    starting from the inverse of the linear part; the k-th iterate is exact modulo x^(2^k), so after the loop the
    coefficients below x^n are those of the formal inverse (in ball arithmetic: enclosures of them)."""
    z = [acb(0), acb(1)] + [acb(0)] * (n - 2); w = list(phi[:n]) + [acb(0)] * (n - len(phi))
    eta1 = [(p - q) / K.DEN for p, q in zip(z, w)]; rho1 = [p - K.OM * q for p, q in zip(z, eta1)]
    for _ in range(6):
        eta = [p - q for p, q in zip(eta1, rho1)]
        m = 2
        while m < 2 * n:
            sn, cs = _exp_pm(eta, n)
            arg = [p + q for p, q in zip(rho1, sn)]
            ex = S2.exp_series(arg, n)
            gval = [eta[k] + ex[k] - (1 if k == 0 else 0) - sn[k] - eta1[k] for k in range(n)]
            excs = S2.mul(ex, cs, n)
            gder = [(1 if k == 0 else 0) + excs[k] - cs[k] for k in range(n)]
            corr = S2.mul(gval, ser_inv(gder, n), n)
            eta = [p - q for p, q in zip(eta, corr)]
            m *= 2
        sn, _ = _exp_pm(eta, n)
        rho = [p + q for p, q in zip(rho1, sn)]
        rho1, eta1 = rho, eta
    return [p + K.OM * q for p, q in zip(rho1, eta1)], [p + K.OMB * q for p, q in zip(rho1, eta1)]


def forward_jets(K, phi, n):
    """Jets (Z, W) of F at the input (x, phi(x) + x^2 d)."""
    O = [acb(0)] * n
    z = ([acb(0), acb(1)] + [acb(0)] * (n - 2), O, O)
    w = (list(phi[:n]) + [acb(0)] * (n - len(phi)), [acb(0), acb(0), acb(1)] + [acb(0)] * (n - 3), O)
    return jet_image(K, z, w, n)


def order_zero_from_jets(a, Zj, Wj, D):
    """The six order-zero series of a step (F or its inverse) from the jets of its image, and the consistency report.
        G0 = (Z0 - x)/x^4,  Q4 = Z1/x^4,  P4 = Z2/x^4,
        M3 = ((W1 - phi'(Z0) Z1)/x^2 - 1)/x^3,
        S2 = (W2 - phi'(Z0) Z2 - phi''(Z0) Z1^2 / 2)/x^5,
        ET44 = (W0 - phi(Z0))/x^44.
    The lifted deviation after the step is  d' = (W - phi(Z))/Z^2 = E + mu0 d + c2 d^2 + O(d^3)  with, for g = x^3 G0,
        E = x^42 ET44/(1+g)^2,   mu0 = (1 + x^3 M3)/(1+g)^2 - 2 x^45 ET44 Q4/(1+g)^3,
        c2 = x^3 [ S2/(1+g)^2 - 2 Q4 (1 + x^3 M3)/(1+g)^3 ] + x^48 ET44 (3 Q4^2/(1+g)^4 - 2 P4/(x^3 (1+g)^3))."""
    N = len(a) - 1; n = len(Zj[0])
    assert n >= D + N + 5
    phi = list(a) + [acb(0)] * (n - len(a))
    d1 = [a[k + 1] * (k + 1) for k in range(N)] + [acb(0)] * (n - N)
    d2 = [a[k + 2] * (k + 2) * (k + 1) for k in range(N - 1)] + [acb(0)] * (n - N + 1)
    Z0, Z1, Z2 = Zj; W0, W1, W2 = Wj
    c0, c1, c2 = (S2.compose_phi(p, Z0, n) for p in (phi, d1, d2))
    et = [p - q for p, q in zip(W0, c0)]
    br = [p - q for p, q in zip(W1, S2.mul(c1, Z1, n))]
    s2 = [p - q - r / 2 for p, q, r in zip(W2, S2.mul(c1, Z2, n), S2.mul(c2, S2.mul(Z1, Z1, n), n))]
    zero = lambda v: bool(v.contains(acb(0)))
    vanishing = [Z0[0], Z0[1] - 1, Z0[2], Z0[3]] + Z1[:4] + Z2[:4] + [br[0], br[1], br[2] - 1, br[3], br[4]] + s2[:5] + et[:N + 4]
    report = dict(all_contain_zero=all(zero(v) for v in vanishing), max_radius=max(float(v.rad()) for v in vanishing))
    ser = dict(G0=Z0[4:5 + D], Q4=Z1[4:5 + D], P4=Z2[4:5 + D], M3=br[5:6 + D], S2=s2[5:6 + D], ET44=et[N + 4:N + 5 + D])
    return ser, report


def d_remainder_constants(K, a, X, rho, narc):
    """Constants for the remainder in d beyond second order, on the polydisc |x| <= X, |d| <= rho.

    Structure used (S5, to be proved in the proof record): with weights (1, 2) for (z, w), F_z - z has weighted order
    >= 4 and F_w - w weighted order >= 5.  Hence, at the input (x, phi_N(x) + x^2 d), (Z - x)/x^4 is an entire function
    of (x, d), and where Z/x != 0 the lifted deviation Phi = (W - phi_N(Z))/Z^2 satisfies Phi - d = x^3 (analytic).
    S1-S3 are the instances of S5 at orders 0, 1, 2 in d.

    Method.  On each ball of a cover of the circle |x| = X (raw_jet_arc with rho) a Taylor model in d of order two
    gives bounds BZ, BW of the remainders of Z, W for |d| <= rho.  They are carried through phi_N (third derivative
    bounded on the ball of Z by a Taylor shift), through 1/Z^2 = Z0^-2 (1 - 2q + 3q^2 + ...), q = (Z - Z0)/Z0, and
    through the product, to a bound BPhi of |Phi - Phi0 - Phi1 d - Phi2 d^2| on the torus.

    Conclusions (maximum principle on the polydisc, for functions that S5 makes analytic there):
      theta = sup |Z/x - 1| on the torus must be < 1; then Z/x != 0 on the polydisc;
      |Phi(x, d) - E - mu0 d - c2 d^2|           <= M3  |x|^3 |d|^3,    M3  = sup BPhi / (X^3 rho^3);
      |Z(x, d) - Z0 - x^4 Q4 d - x^4 P4 d^2|     <= MZ3 |x|^4 |d|^3,    MZ3 = sup BZ / (X^4 rho^3),
    for |x| <= X, |d| <= rho.  Returns dict(M3, MZ3, theta, X, rho) with float upper bounds."""
    N = len(a) - 1
    rho_a = arb(rho)
    p3 = acb_poly([a[k] * (k * (k - 1) * (k - 2)) for k in range(3, N + 1)])       # phi_N''' as a polynomial
    worst = dict(BPhi=0.0, BZ=0.0, theta=0.0)
    for xc, rad_arc in _arcs(X, narc):
        Z0, W0, Z1, W1, Z2, W2, x, BZ, BW = raw_jet_arc(K, a, xc, rad_arc, rho_a)
        z1, z2 = _up(Z1), _up(Z2)
        lin = z1 * rho_a + z2 * rho_a ** 2
        DZ = lin + BZ                                                               # |Z - Z0| <= DZ
        quadZ = 2 * z1 * z2 * rho_a ** 3 + z2 ** 2 * rho_a ** 4 + 2 * lin * BZ + BZ ** 2   # |(Z - Z0)^2 - Z1^2 d^2|
        p, dp, ddp = _phi_at(a, Z0, 2)
        m = acb(Z0.real.mid(), Z0.imag.mid()); rz = _up(Z0 - m) + DZ
        s3 = arb(0); pw = arb(1)
        for cf in p3(acb_poly([m, 1])).coeffs():
            s3 += _up(cf) * pw; pw = pw * rz                                        # sup |phi_N'''| on |zeta - m| <= rz
        BP = _up(dp) * BZ + _up(ddp) * quadZ / 2 + s3 * DZ ** 3 / 6
        N0 = W0 - p; N1 = W1 - dp * Z1; N2 = W2 - dp * Z2 - ddp * Z1 * Z1 / 2
        BN = BW + BP
        z0lo = arb(abs(Z0).lower())
        th = DZ / z0lo
        if not (z0lo > 0 and th < 1):
            raise ArithmeticError('d_remainder_constants: Z not bounded away from 0 on the torus')
        BI = (2 * BZ / z0lo + 3 * quadZ / z0lo ** 2 + th ** 3 * (4 - 3 * th) / (1 - th) ** 2) / z0lo ** 2
        I0 = 1 / z0lo ** 2; I1 = 2 * z1 / z0lo ** 3; I2 = 2 * z2 / z0lo ** 3 + 3 * z1 ** 2 / z0lo ** 4
        n0, n1, n2 = _up(N0), _up(N1), _up(N2)
        BPhi = ((n1 * I2 + n2 * I1) * rho_a ** 3 + n2 * I2 * rho_a ** 4 + (n0 + n1 * rho_a + n2 * rho_a ** 2) * BI
                + (I0 + I1 * rho_a + I2 * rho_a ** 2) * BN + BN * BI)
        theta = (_up(Z0 - x) + DZ) / arb(abs(x).lower())
        for k, v in (('BPhi', BPhi), ('BZ', BZ), ('theta', theta)):
            u = float(v.upper())
            if not u == u or u == float('inf'):
                raise ArithmeticError('d_remainder_constants: bound not finite; use more arcs')
            worst[k] = max(worst[k], u)
    up = 1 + 1e-12
    return dict(M3=worst['BPhi'] / (X ** 3 * rho ** 3) * up, MZ3=worst['BZ'] / (X ** 4 * rho ** 3) * up,
                theta=worst['theta'] * up, X=float(X), rho=float(rho))


_SIX = ('G0', 'Q4', 'P4', 'M3', 'S2', 'ET44')


def pick_constants(MC, ax, rho):
    """MC: a list of results of d_remainder_constants (several circles).  Returns the one of smallest X whose polydisc
    contains {|x| <= ax} x {|d| <= rho}."""
    for mc in sorted(MC, key=lambda t: t['X']):
        if ax < mc['X'] and rho <= mc['rho'] and mc['theta'] < 1:
            return mc
    raise ArithmeticError('no remainder constants for this disc')


def _tau_bracket(TAU, g, x):
    """tau(x (1 + g)) - tau(x) = (g / x^3) * _tau_bracket  for the four-term Fatou coordinate (|g| <= 1/4)."""
    A3, A2, A1, KA = TAU
    og = 1 + g
    return -A3 * (3 + 3 * g + g * g) / (og * og * og) - A2 * x * (2 + g) / (og * og) - A1 * x * x / og + KA * x * x * x * log1p_over(g)


def tube_step(SER, TAU, MC, xc, r, rho):
    """One step of F on the tube piece {|x - xc| <= r} x {|d| <= rho}.  SER: the six Series of order_zero_from_jets;
    MC: a list of constants of d_remainder_constants (needed if rho > 0; pick_constants).
    Returns enclosures (acb) of
        x, g = x^3 G0, mu0, E, c2          the jets at d = 0 (formulas: order_zero_from_jets)
        dxdd = x^4 Q4, d2xdd2 = x^4 P4
        dtau0 = tau(x'(x, 0)) - tau(x)
        gt   = x'/x - 1 for every |d| <= rho      = g + x^3 B,   B = Q4 d + P4 d^2 + (remainder),
                                                    |B| <= bmax = |Q4| rho + |P4| rho^2 + MZ3 rho^3
        dtau = tau(x') - tau(x) for every |d| <= rho.  The dependence on d is separated:  x'(x, d) = x'(x, 0) (1 + gam)
               with gam = x^3 B/(1 + g), and  tau(x') - tau(x'(x, 0)) = (B/(1 + g)^4) * _tau_bracket(gam, x (1 + g)).
    and the bounds (arb)
        gt_dev   >= |gt - g|       = |x|^3 bmax
        dtau_dev >= |dtau - dtau0| = bmax sup|1/(1 + g)^4| sup|_tau_bracket|
        dev_hi >= |d'| for |d| <= rho      = |E| + |mu0| rho + |c2| rho^2 + M3 |x|^3 rho^3
        dev_lo <= |d'| for |d|  = rho      = inf|mu0| rho - |E| - |c2| rho^2 - M3 |x|^3 rho^3."""
    rr = arb(r); x = xc + acb(arb(0, rr), arb(0, rr))
    G0, Q4, P4, M3, S2e, ET = (SER[k].enclose(xc, r) for k in _SIX)
    rho_a = arb(rho); ax = arb((abs(xc) + rr).upper())
    if rho > 0:
        mc = pick_constants(MC, ax, rho)
        m3, mz3 = arb(mc['M3']), arb(mc['MZ3'])
    else:
        m3 = mz3 = arb(0)
    x2 = x * x; x3 = x2 * x; x4 = x2 * x2
    g = x3 * G0; og = 1 + g; og2 = og * og; og3 = og2 * og
    x45 = x3 ** 15
    mu0 = (1 + x3 * M3) / og2 - 2 * x45 * ET * Q4 / og3
    E = x3 ** 14 * ET / og2
    c2 = x3 * (S2e / og2 - 2 * Q4 * (1 + x3 * M3) / og3) + x45 * (x3 * 3 * Q4 * Q4 / (og2 * og2) - 2 * P4 / og3) * ET
    dtau0 = G0 * _tau_bracket(TAU, g, x)
    bmax = arb((_up(Q4) * rho_a + _up(P4) * rho_a ** 2 + mz3 * rho_a ** 3).upper())
    B = acb(arb(0, bmax), arb(0, bmax))                       # a square that contains the disc |B| <= bmax
    gam = x3 * B / og
    dtau_dev = arb((bmax * _up(1 / (og2 * og2)) * _up(_tau_bracket(TAU, gam, x * og))).upper())
    dtau = dtau0 + acb(arb(0, dtau_dev), arb(0, dtau_dev))
    gt_dev = arb((ax ** 3 * bmax).upper())
    nl = _up(c2) * rho_a ** 2 + m3 * ax ** 3 * rho_a ** 3
    return dict(x=x, g=g, mu0=mu0, E=E, c2=c2, dxdd=x4 * Q4, d2xdd2=x4 * P4, dtau0=dtau0, gt=g + x3 * B, dtau=dtau,
                gt_dev=gt_dev, dtau_dev=dtau_dev,
                dev_hi=_up(E) + _up(mu0) * rho_a + nl, dev_lo=arb(abs(mu0).lower()) * rho_a - _up(E) - nl,
                G0=G0, Q4=Q4, P4=P4, absx=ax, MZ3=mz3, M3c=m3)


def inverse_conditions(SER, TAU, MC, c, r, rho, xcp, rp, Rp):
    """The two conditions of the local inverse lemma for the disc B = {|x - c| <= r} and the fibre radius rho, with the
    target set  B' x {|d'| <= Rp},  B' = {|x' - xcp| <= rp}.

    Lifted map on B x {|d| <= rho}:   x' = b0(x) + beta(x, d),  d' = E + mu0 d + nu(x, d),  with b0(x) = x + x^4 G0,
        |beta| <= |x|^4 (|Q4| rho + |P4| rho^2 + MZ3 rho^3),    |nu| <= |c2| rho^2 + M3 |x|^3 rho^3.
      (i)  inf|mu0| rho > Rp + sup|E| + sup|nu|                                on B;
      (ii) r (1 - L) > |b0(c) - xcp| + rp + sup|beta|,   L = sup_B |b0' - 1|.
    Lemma.  If (i) and (ii) hold, every (x', d') of the target set has exactly one preimage (x, d) under the lifted map
    with |x - c| < r and |d| < rho.
    Proof.  For x in B, (i) and Rouche in d (against mu0 d) give exactly one d = delta(x) in |d| < rho with d' as
    prescribed; delta is holomorphic on a neighbourhood of B.  The function x -> b0(x) + beta(x, delta(x)) - x' differs
    from x - c by at most  L r + |b0(c) - xcp| + rp + sup|beta| < r  on the circle |x - c| = r (b0 - id has the
    Lipschitz constant L on the convex set B), so by Rouche it has exactly one zero in |x - c| < r.
    Returns (ok, details, q) with q = tube_step on B x {|d| <= rho}."""
    q = tube_step(SER, TAU, MC, c, r, rho)
    rho_a = arb(rho)
    cond1 = bool(q['dev_lo'] > arb(Rp))
    x = q['x']; x3 = x * x * x
    L = _up(4 * x3 * q['G0'] + x3 * x * SER['G0'].enclose_derivative(c, r))
    res = _up(c + c ** 4 * SER['G0'].point(c) - xcp)
    beta = q['absx'] ** 4 * (_up(q['Q4']) * rho_a + _up(q['P4']) * rho_a ** 2 + arb(q['MZ3']) * rho_a ** 3)
    lhs = arb(r) * (1 - L); rhs = res + arb(rp) + beta
    cond2 = bool(L < 1 and lhs > rhs)
    det = dict(L=float(L.upper()), residual=float(res.upper()), beta=float(beta.upper()),
               margin_i=float((q['dev_lo'] - arb(Rp)).lower()), margin_ii=float((lhs - rhs).lower()))
    return cond1 and cond2, det, q


def inverse_step(SER, TAU, MC, xcp, rp, Rp):
    """A disc B = {|x - c| <= r} and a fibre radius rho for which inverse_conditions holds for the target
    B' x {|d'| <= Rp}, found by a (non-rigorous) Newton iteration for the centre and a short search for r and rho; the
    conditions are then checked rigorously.  Returns None if the search fails, else a dict with c, r, rho, the details,
    the forward quantities q on B x {|d| <= rho}, and the quantities of the inverse step on the target set:
        gG    = x/x' - 1          = -gt/(1 + gt)
        dtauG = tau(x) - tau(x')  = -dtau."""
    G = SER['G0']
    c = acb(xcp)
    for _ in range(30):
        f = c + c ** 4 * G.poly(c) - xcp
        df = 1 + 4 * c ** 3 * G.poly(c) + c ** 4 * G.dpoly(c)
        c = c - f / df
        c = acb(c.real.mid(), c.imag.mid())
    r = 1.25 * (rp + float(abs(c + c ** 4 * G.poly(c) - xcp).upper())) + 1e-30
    rho_max = max(mc['rho'] for mc in MC)
    for _ in range(12):
        q0 = tube_step(SER, TAU, None, c, r, 0)
        mlo = arb(abs(q0['mu0']).lower())
        if not mlo > 0:
            return None
        rho = float(((arb(Rp) + _up(q0['E'])) / mlo).upper())
        for _ in range(3):                                   # fixed-point step for (i), with 3% room
            if not 0 < rho <= rho_max:
                return None
            m3 = arb(pick_constants(MC, q0['absx'], rho)['M3'])
            nl = _up(q0['c2']) * arb(rho) ** 2 + m3 * q0['absx'] ** 3 * arb(rho) ** 3
            rho = 1.03 * float(((arb(Rp) + _up(q0['E']) + nl) / mlo).upper())
        if not 0 < rho <= rho_max:
            return None
        ok, det, q = inverse_conditions(SER, TAU, MC, c, r, rho, xcp, rp, Rp)
        if ok:
            gt = q['gt']
            return dict(c=c, r=r, rho=rho, details=det, q=q, gG=-gt / (1 + gt), dtauG=-q['dtau'])
        if det['margin_i'] <= 0 or det['L'] >= 1:
            return None
        r = max(1.3 * r, 1.25 * (det['residual'] + rp + det['beta']) / (1 - det['L']))      # (ii) failed: enlarge the disc
    return None


# ----------------------------------------------------------------------------------------------------------------------
# Work package W3: zone II.  The objects of the design (3b r2, section 3) and the check of one piece.
#
# A piece is a disc |x - xc| <= r in the raw variable x (xi = c x).  The check is wall-independent: a piece that meets
# a wall of D_j is not cut.  Every inequality is verified for all points of the piece that satisfy the two wedge
# conditions; the functionals enter through their enclosures on the piece and through the lower bounds that the
# conditions give (first >= 1, second >= c_j).
class Tube:
    """Design objects for j = 0 (F on D0) or j = 1 (G on D1), as balls.
        tau(x) = A3 x^-3 + A2 x^-2 + A1 x^-1 + kappa log x          (principal log; x = xi / c)
        first(x)  = sgn (Re tau - s_j) + 1,   sgn = +1 (j = 0), -1 (j = 1);   wedge condition: first > 1
        second(x) = Re(rot tau),  rot = e^{i theta0} (j = 0), -e^{-i theta0} (j = 1);   wedge condition: second > c_j
        R(x) = eps |xi^alpha| first^(-q1/3) second^(-q2/3),  eps fixed by R(xi*) = rstar
    with theta0 = pi/2 - pi/8, s_j = Re tau* -+ 0.25, c_j = second(xi*) - 0.15, xi* = 0.40 e^{i pi/6}."""
    def __init__(self, K, TAU, j, rstar='0.002', q=9):
        self.j, self.K, self.TAU, self.q3 = j, K, TAU, q // 3
        assert q % 3 == 0
        th0 = arb.pi() / 2 - arb.pi() / 8
        self.sgn = 1 if j == 0 else -1
        self.rot = (acb(0, 1) * th0).exp() if j == 0 else -((acb(0, -1) * th0).exp())
        xs = acb('0.4') * (acb(0, 1) * arb.pi() / 6).exp() / K.c
        ts = self.tau(xs)
        self.s = ts.real - self.sgn * arb('0.25')
        self.cw = (self.rot * ts).real - arb('0.15')
        self.eps = arb(rstar) / (self.xi_alpha(xs) * arb('1.25') ** (-self.q3) * (self.cw + arb('0.15')) ** (-self.q3))
        # chart sector and guard core (in xi): radius limits and argument limits in units of pi
        self.chart = (arb('0.60'), arb('-0.20'), arb('0.30')) if j == 0 else (arb('0.60'), arb('0.03'), arb('0.50'))
        self.core = (arb('0.47'), arb('-0.08'), arb('0.20')) if j == 0 else (arb('0.42'), arb('0.09'), arb('0.43'))

    def tau(self, x):
        A3, A2, A1, KA = self.TAU
        ix = 1 / x
        return ((A3 * ix + A2) * ix + A1) * ix + KA * x.log()

    def xi_alpha(self, x):
        """|xi^alpha| = exp(Re(alpha log xi)), principal log of xi = c x (an arb)."""
        return ((self.K.ALPHA * (self.K.c * x).log()).real).exp()

    def functionals(self, x):
        t = self.tau(x)
        return self.sgn * (t.real - self.s) + 1, (self.rot * t).real

    def in_core(self, x):
        """True if the ball x lies in the guard core, False if it lies in its complement, None if undecided."""
        xi = self.K.c * x
        rad, lo, hi = self.core
        a = xi.arg() / arb.pi(); m = abs(xi)
        if m <= rad and a >= lo and a <= hi:
            return True
        if m > rad or a < lo or a > hi:
            return False
        return None


def piece_check(SER, MC, TB, xc, r, sigma, kappa='0.15', rho_max=0.02, inverse=False):
    """_piece_check, with every refusal of the engine (a piece outside the range of the series or of the remainder
    constants, a step too large for the logarithm) turned into the status 'fail'."""
    try:
        return _piece_check(SER, MC, TB, xc, r, sigma, kappa, rho_max, inverse)
    except (ArithmeticError, AssertionError) as e:
        return 'fail', dict(why='engine: %s' % (str(e) or type(e).__name__))


def _piece_check(SER, MC, TB, xc, r, sigma, kappa, rho_max, inverse):
    """Check of one piece for the tube lemma (design section 4).  Returns (status, info):
        'out'     a wedge condition fails on the whole piece: no point of D_j in it
        'pass'    (A1), (A2), (B) hold for every point of the piece that satisfies the wedge conditions
        'guard'   the piece is not 'out' and is not inside the guard core: (G) is not shown on it
        'fail'    an inequality is not shown (info['why'])
    For j = 0 the step is F on the piece.  For j = 1 (inverse=True) the piece is a target set of the local inverse
    lemma; the step is the inverse step, and the inequalities are checked on the preimage disc B in forward form:
        (A1)  Re dtau > 0 and Re(e^{-i theta0} dtau) >= sigma on B x {|d| <= rho}      (dtau the forward increment)
        (A2)  |x/x' - 1| = |gt/(1 + gt)| <= kappa
        (B)   for x in B and |d| <= R(x):  |d'| < R(x'), in the form
              |mu0| + |E|/R(x) + |c2| R(x) + M3 |x|^3 R(x)^2  <  inf R(x')/R(x).
    For j = 0, (B) is  inf|mu0| - |E|/R - |c2| R - M3 |x|^3 R^2 > sup R(x')/R(x)."""
    rr = arb(r); x = xc + acb(arb(0, rr), arb(0, rr))
    first, second = TB.functionals(x)
    if not (first.is_finite() and second.is_finite()):
        return 'fail', dict(why='functionals not finite')
    if first <= 1 or second <= TB.cw:
        return 'out', {}
    core = TB.in_core(x)
    if core is not True:
        return 'guard', {}
    q3 = TB.q3
    one = arb(1)
    f_lo = one.max(arb(first.lower())); f_hi = arb(first.upper())
    s_lo = arb(TB.cw.upper()).max(arb(second.lower())); s_hi = arb(second.upper())
    xa = TB.xi_alpha(x)
    R_hi = arb((TB.eps * arb(xa.upper()) * f_lo ** (-q3) * s_lo ** (-q3)).upper())
    R_lo = arb((TB.eps * arb(xa.lower()) * f_hi ** (-q3) * s_hi ** (-q3)).lower())
    if not R_hi < rho_max:
        return 'fail', dict(why='tube radius above rho_max')
    info = {}
    if not inverse:
        q = tube_step(SER, TB.TAU, MC, xc, r, float(R_hi.upper()))
    else:
        iv = inverse_step(SER, TB.TAU, MC, xc, r, float(R_hi.upper()))
        if iv is None:
            return 'fail', dict(why='local inverse not found')
        q = iv['q']; info['r_over_rp'] = iv['r'] / r
        if not arb(iv['rho']) < rho_max:
            return 'fail', dict(why='preimage fibre radius above rho_max')
    dre = arb((q['dtau0'].real - q['dtau_dev']).lower())
    rot = TB.rot if not inverse else -TB.rot                     # for j = 1: -rot = e^{-i theta0}
    dh = arb(((rot * q['dtau0']).real - q['dtau_dev']).lower())
    info.update(dre=float(dre), dh=float(dh))
    if not (dre > 0 and dh >= arb(sigma)):
        return 'fail', dict(info, why='A1')
    gt = q['gt']
    a2 = _up(gt) if not inverse else _up(gt / (1 + gt))
    info['a2'] = float(a2)
    if not a2 <= arb(kappa):
        return 'fail', dict(info, why='A2')
    pw = (TB.K.ALPHA * (1 + gt).log()).real.exp()                # |(x'/x)^alpha| on the piece and the fibre
    ax = q['absx']
    if not inverse:
        ratio_hi = arb(pw.upper()) * (1 + dre / f_hi) ** (-q3) * (1 + dh / s_hi) ** (-q3)
        lhs = arb(abs(q['mu0']).lower()) - _up(q['E']) / R_lo - _up(q['c2']) * R_hi - q['M3c'] * ax ** 3 * R_hi ** 2
        margin = arb((lhs - ratio_hi).lower())
    else:
        # source disc B: R(x) for x in B.  With first(x) = first(x') + (Re dtau), second(x) = second(x') + (Re(e^{-i th0} dtau)),
        # and x' in D1:  R(x')/R(x) = |(x'/x)^alpha| (first(x)/first(x'))^q3 (second(x)/second(x'))^q3
        #                           >= inf|(1+gt)^alpha| (1 + dre/f_hi)^q3 (1 + dh/s_hi)^q3.
        ratio_lo = arb(pw.lower()) * (1 + dre / f_hi) ** q3 * (1 + dh / s_hi) ** q3
        # R on B: from R(x') and the ratio:  R(x) <= R_hi(target) / ratio_lo;  R(x) >= R_lo(target) / sup ratio
        dre_hi = arb((q['dtau0'].real + q['dtau_dev']).upper()); dh_hi = arb(((rot * q['dtau0']).real + q['dtau_dev']).upper())
        ratio_hi = arb(pw.upper()) * (1 + dre_hi / f_lo) ** q3 * (1 + dh_hi / s_lo) ** q3
        RS_hi = R_hi / ratio_lo; RS_lo = R_lo / ratio_hi
        if not RS_hi <= arb(iv['rho']):                           # the tube fibre over B must lie in the fibre disc of q
            return 'fail', dict(info, why='source fibre above the fibre radius of the lemma')
        lhs = _up(q['mu0']) + _up(q['E']) / RS_lo + _up(q['c2']) * RS_hi + q['M3c'] * ax ** 3 * RS_hi ** 2
        margin = arb((ratio_lo - lhs).lower())
    info['margin_B'] = float(margin)
    if not margin > 0:
        return 'fail', dict(info, why='B')
    return 'pass', info


def build_engine(N=40, D=360, X=1.10, narc=16000, rem=((0.90, 8000), (1.03, 32000)), rho_d=0.02):
    """The engine of W1-W2 in one call: constants, coefficient balls, the six Series with their Cauchy constants, the
    remainder constants.  Series at 400 digits; on return the working precision is 160 bits.
    Returns K, a, SER, MC, report (structural-zero consistency, tails at |x| = 1.02, theta)."""
    ctx.dps = 400
    K = Consts(); a = coefficients(K, N)
    Zj, Wj = forward_jets(K, a, D + N + 6)
    ser, rep = order_zero_from_jets(a, Zj, Wj, D)
    ctx.prec = 160
    M, _ = circle_sup(K, a, X, narc, second=True)
    SER = {k: Series(ser[k], X, M[k]) for k in ser}
    MC = [d_remainder_constants(K, a, Xr, rho_d, n) for Xr, n in rem]
    report = dict(structural_zeros_consistent=bool(rep['all_contain_zero'] and rep['max_radius'] < 1e-150),
                  max_tail_at_1p02=max(float(SER[k].tail(1.02).upper()) for k in SER),
                  remainder_constants=[dict(X=m['X'], rho=m['rho'], M3=m['M3'], MZ3=m['MZ3'], theta=m['theta']) for m in MC])
    return K, a, SER, MC, report
