#!/usr/bin/env python3
"""dyad_open20_an_stage1_prep.py -- OPEN 20 analytic branch, sectorial pilot, stage 1: exact preparation.

Design: records/dyad/DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md (D1-D5). Receiving review guards:
records/dyad/DYAD_LH2012_PILOT_RECEIVING_REVIEW.md section 6.

All arithmetic is exact, in the tower  Q(s) [s^2 = -3, s = i sqrt3]  <  E = Q(s)[a]/(P(a)), P = A a^2 + B a + C
<  E(c) = E[c]/(c^3 + ell), ell = c40 + mu a.  Elements are stored in normal form (degree < 2 in a, < 3 in c).
Identities proved in E hold for both roots of P at once; only gate S1 selects the pilot root a_pil (Im a > 0).

  F = T^6 in the complexified raw frame z = rho + omega*eta, w = rho + conj(omega)*eta, jets to total degree 7
      (real-chart Fraction composition from dyad_h4_real_route_check.T6; the frame change is done in Q(s)).
Gates:
  S1  branch isolation: rigorous enclosures (mpmath.iv on real and imaginary parts) of Im a for both roots: one is
      positive (a_pil), the other negative.  Crosswalk: a_pil = a_2^- of P1-c = a_+ of the owner assessment / pilot design.
  S2  graph equation: orders z^2..z^5 vanish identically in E; the order-z^{k+3} coefficient is affine, L_k a_k + R_k,
      with L_k = ell (k* - k) for k = 3, 4 (P1-c); a_3 = b_1 and a_4 = b_2 solved exactly; b_2 != 0, hence m = 2.
  S3  lifted map (z, w) = (x, x^2 (a + y)): the full jets are divisible as required (G = (F_z - x)/x^4, H = (F_w - x^2 u)/x^5
      are series); y' = (a + y + x^3 H)/(1 + x^3 G)^2 - a has no x^0..x^2 terms and its x^3 Y^0 coefficient vanishes (P(a) = 0).
  S4  normalized forward map (xi = c x, Y = y - b_1 x) has the [L12] Definition 4.1 form with k = 3, alpha as recorded, m = 2:
      F_1 = xi - xi^4 + O(xi^4 Y, xi^5);  F_2 = Y - alpha xi^3 Y + O(xi^3 Y^2, xi^4 Y) + xi^5 psi(xi), psi(0) != 0.
  S5  formal inverse of the normalized map (x-order <= 5, Y-degree <= 2): both compositions are the identity to that order;
      after xi~ = rho xi, rho = e^{i pi/3}, the inverse has the same form with the same alpha and m = 2.
Negative controls (exit 1): --control B  b_1 perturbed (S4: a pure xi^4 term appears);  --control R  c^3 = +ell
  (S4: xi^4 coefficient +1);  --control A  alpha altered (S4).
Output JSON is deterministic (exact strings).  Exit 0 PASS / 1 FAIL / 3 crash.
Usage: python -I -B dyad_open20_an_stage1_prep.py [--control B|R|A] [--out stage1_prep.json]
"""
import os, sys, json
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dyad_h4_real_route_check import T6


# ---------------- Q(s), s^2 = -3 ----------------
class Qs:
    __slots__ = ('p', 'q')
    def __init__(self, p=0, q=0): self.p, self.q = Fr(p), Fr(q)
    @staticmethod
    def c(o): return o if isinstance(o, Qs) else Qs(o, 0)
    _ok = (int, Fr)
    def __add__(self, o):
        if not isinstance(o, (Qs,) + Qs._ok): return NotImplemented
        o = Qs.c(o); return Qs(self.p + o.p, self.q + o.q)
    __radd__ = __add__
    def __neg__(self): return Qs(-self.p, -self.q)
    def __sub__(self, o):
        if not isinstance(o, (Qs,) + Qs._ok): return NotImplemented
        return self + (-Qs.c(o))
    def __rsub__(self, o): return Qs.c(o) - self
    def __mul__(self, o):
        if not isinstance(o, (Qs,) + Qs._ok): return NotImplemented
        o = Qs.c(o); return Qs(self.p * o.p - 3 * self.q * o.q, self.p * o.q + self.q * o.p)
    __rmul__ = __mul__
    def conj(self): return Qs(self.p, -self.q)
    def inv(self):
        n = self.p * self.p + 3 * self.q * self.q; assert n != 0; return Qs(self.p / n, -self.q / n)
    def __truediv__(self, o): return self * Qs.c(o).inv()
    def iszero(self): return self.p == 0 and self.q == 0
    def __eq__(self, o): o = Qs.c(o); return self.p == o.p and self.q == o.q
    def __hash__(self): return hash((self.p, self.q))
    def __repr__(self): return str(self.p) if self.q == 0 else '(%s + %s*i*sqrt3)' % (self.p, self.q)
    def complex(self): return complex(float(self.p), float(self.q) * 3 ** 0.5)


MU = Qs(Fr(-1, 2), Fr(-2, 3)); C40 = Qs(Fr(-1, 16), Fr(7, 144)); D31 = Qs(Fr(1, 3), Fr(-1, 9)); CC = Qs(Fr(-61, 2160), Fr(43, 6480))
A_ = MU.conj() - 2 * MU; B_ = D31 - 2 * C40
ALPHA = Qs(Fr(-102, 19), Fr(-16, 19)); KSTAR = Qs(Fr(-64, 19), Fr(-16, 19))
OMEGA = Qs(Fr(-1, 2), Fr(1, 2)); LAMBDA = Qs(Fr(1, 2), Fr(1, 2))   # e^{2 pi i/3}, e^{i pi/3}


# ---------------- E = Q(s)[a]/(P) ----------------
class E_:
    __slots__ = ('e0', 'e1')
    A2_1 = None; A2_0 = None   # a^2 = A2_1 a + A2_0
    def __init__(self, e0=0, e1=0): self.e0, self.e1 = Qs.c(e0), Qs.c(e1)
    @staticmethod
    def c(o): return o if isinstance(o, E_) else E_(o, 0)
    _ok = (int, Fr, Qs)
    def __add__(self, o):
        if not isinstance(o, (E_,) + E_._ok): return NotImplemented
        o = E_.c(o); return E_(self.e0 + o.e0, self.e1 + o.e1)
    __radd__ = __add__
    def __neg__(self): return E_(-self.e0, -self.e1)
    def __sub__(self, o):
        if not isinstance(o, (E_,) + E_._ok): return NotImplemented
        return self + (-E_.c(o))
    def __rsub__(self, o): return E_.c(o) - self
    def __mul__(self, o):
        if not isinstance(o, (E_,) + E_._ok): return NotImplemented
        o = E_.c(o); t2 = self.e1 * o.e1
        return E_(self.e0 * o.e0 + t2 * E_.A2_0, self.e0 * o.e1 + self.e1 * o.e0 + t2 * E_.A2_1)
    __rmul__ = __mul__
    def iszero(self): return self.e0.iszero() and self.e1.iszero()
    def __eq__(self, o): return (self - E_.c(o)).iszero()
    def inv(self):
        m00, m01 = self.e0, self.e1 * E_.A2_0; m10, m11 = self.e1, self.e0 + self.e1 * E_.A2_1
        det = m00 * m11 - m01 * m10; assert not det.iszero()
        res = E_(m11 / det, -m10 / det); assert (self * res) == 1; return res
    def __truediv__(self, o): return self * E_.c(o).inv()
    def __repr__(self): return repr(self.e0) if self.e1.iszero() else '%s + %s*a' % (self.e0, self.e1)
    def complex(self, aval): return self.e0.complex() + self.e1.complex() * aval


E_.A2_1 = -B_ / A_; E_.A2_0 = -CC / A_
A_E = E_(0, 1)
ELL = E_(C40) + MU * A_E


# ---------------- E(c) = E[c]/(c^3 - C3) ----------------
class Ec:
    __slots__ = ('v',)
    C3 = None
    def __init__(self, v=None): self.v = [E_.c(t) for t in (v if v is not None else [0, 0, 0])]
    @staticmethod
    def c(o): return o if isinstance(o, Ec) else Ec([E_.c(o), 0, 0])
    _ok = (int, Fr, Qs, E_)
    def __add__(self, o):
        if not isinstance(o, (Ec,) + Ec._ok): return NotImplemented
        o = Ec.c(o); return Ec([self.v[k] + o.v[k] for k in range(3)])
    __radd__ = __add__
    def __neg__(self): return Ec([-t for t in self.v])
    def __sub__(self, o):
        if not isinstance(o, (Ec,) + Ec._ok): return NotImplemented
        return self + (-Ec.c(o))
    def __rsub__(self, o): return Ec.c(o) - self
    def __mul__(self, o):
        if not isinstance(o, (Ec,) + Ec._ok): return NotImplemented
        o = Ec.c(o); r = [E_(0) for _ in range(5)]
        for i in range(3):
            if self.v[i].iszero(): continue
            for j in range(3):
                if not o.v[j].iszero(): r[i + j] = r[i + j] + self.v[i] * o.v[j]
        return Ec([r[0] + r[3] * Ec.C3, r[1] + r[4] * Ec.C3, r[2]])
    __rmul__ = __mul__
    def iszero(self): return all(t.iszero() for t in self.v)
    def __eq__(self, o): return (self - Ec.c(o)).iszero()
    def __repr__(self):
        parts = ['(%s)%s' % (t, ['', '*c', '*c^2'][k]) for k, t in enumerate(self.v) if not t.iszero()]
        return ' + '.join(parts) if parts else '0'


# ---------------- truncated series in (x, y), coefficients in Ec ----------------
class Ser:
    def __init__(self, d=None, nx=5, ny=2):
        self.nx, self.ny = nx, ny
        self.d = {k: v for k, v in (d or {}).items() if k[0] <= nx and k[1] <= ny and not v.iszero()}
    @staticmethod
    def c(o, nx, ny): return o if isinstance(o, Ser) else Ser({(0, 0): Ec.c(o)}, nx, ny)
    def __add__(self, o):
        o = Ser.c(o, self.nx, self.ny); d = dict(self.d)
        for k, v in o.d.items(): d[k] = d.get(k, Ec()) + v
        return Ser(d, self.nx, self.ny)
    __radd__ = __add__
    def __neg__(self): return Ser({k: -v for k, v in self.d.items()}, self.nx, self.ny)
    def __sub__(self, o): return self + (-Ser.c(o, self.nx, self.ny))
    def __rsub__(self, o): return Ser.c(o, self.nx, self.ny) - self
    def __mul__(self, o):
        o = Ser.c(o, self.nx, self.ny); d = {}
        for (i, j), u in self.d.items():
            for (k, l), v in o.d.items():
                if i + k <= self.nx and j + l <= self.ny: d[(i + k, j + l)] = d.get((i + k, j + l), Ec()) + u * v
        return Ser(d, self.nx, self.ny)
    __rmul__ = __mul__
    def trunc(self, nx, ny): return Ser(self.d, nx, ny)
    def coef(self, i, j): return self.d.get((i, j), Ec())
    def iszero(self): return not self.d
    def __eq__(self, o): return (self - Ser.c(o, self.nx, self.ny)).iszero()
    def compose(self, sx, sy):
        nx, ny = sx.nx, sx.ny; out = Ser({}, nx, ny)
        px = {0: Ser.c(1, nx, ny)}; py = {0: Ser.c(1, nx, ny)}
        for i in range(1, self.nx + 1): px[i] = px[i - 1] * sx
        for j in range(1, self.ny + 1): py[j] = py[j - 1] * sy
        for (i, j), v in self.d.items(): out = out + px[i] * py[j] * v
        return out


def main():
    import argparse, mpmath
    ap = argparse.ArgumentParser(); ap.add_argument('--control', choices=['B', 'R', 'A']); ap.add_argument('--out', default='stage1_prep.json')
    opt = ap.parse_args()
    Ec.C3 = ELL if opt.control == 'R' else -ELL
    G, info = {}, {}
    # ---- F = T^6 to degree 7 in (z, w) ----
    R, Ex = T6(7)
    om, omb = OMEGA, OMEGA.conj(); den = om - omb
    zc, wc = (-omb / den, om / den), (Qs(1) / den, Qs(-1) / den)     # rho = zc0 z + zc1 w ; eta = wc0 z + wc1 w
    def pmul(p, q, D=7):
        r = {}
        for (i, j), u in p.items():
            for (k, l), v in q.items():
                if i + j + k + l <= D: r[(i + k, j + l)] = r.get((i + k, j + l), Qs()) + u * v
        return {k: v for k, v in r.items() if not v.iszero()}
    def padd(p, q):
        r = dict(p)
        for k, v in q.items(): r[k] = r.get(k, Qs()) + v
        return {k: v for k, v in r.items() if not v.iszero()}
    pw_r, pw_e = {0: {(0, 0): Qs(1)}}, {0: {(0, 0): Qs(1)}}
    for n in range(1, 8):
        pw_r[n] = pmul(pw_r[n - 1], {(1, 0): zc[0], (0, 1): zc[1]}); pw_e[n] = pmul(pw_e[n - 1], {(1, 0): wc[0], (0, 1): wc[1]})
    def convert(P):
        out = {}
        for (i, j), v in P.items(): out = padd(out, {k: u * Qs(v) for k, u in pmul(pw_r[i], pw_e[j]).items()})
        return out
    Rz, Ez = convert(R), convert(Ex)
    Fz = padd(Rz, {k: v * om for k, v in Ez.items()}); Fw = padd(Rz, {k: v * omb for k, v in Ez.items()})
    assert Fz[(2, 1)] == MU and Fz[(4, 0)] == C40 and Fw[(3, 1)] == D31 and Fw[(5, 0)] == CC and Fz[(1, 0)] == 1 and Fw[(0, 1)] == 1
    info['raw_coefficients'] = {'F_z_(2,1)=mu': repr(MU), 'F_z_(4,0)=c40': repr(C40), 'F_w_(3,1)=d31': repr(D31), 'F_w_(5,0)=C': repr(CC)}
    # ---- S1 ----
    mpmath.mp.dps = 60; iv = mpmath.iv; iv.dps = 60; r3 = iv.sqrt(3)
    def ivq(u): return (iv.mpf(u.p.numerator) / iv.mpf(u.p.denominator), iv.mpf(u.q.numerator) / iv.mpf(u.q.denominator) * r3)
    def cmul(u, v): return (u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0])
    def cdiv(u, v):
        d = v[0] ** 2 + v[1] ** 2; n = cmul(u, (v[0], -v[1])); return (n[0] / d, n[1] / d)
    disc = B_ * B_ - 4 * A_ * CC
    Ai, Bi, Di = ivq(A_), ivq(B_), ivq(disc); assert Di[1] > 0
    mod = iv.sqrt(Di[0] ** 2 + Di[1] ** 2); sq = (iv.sqrt((mod + Di[0]) / 2), iv.sqrt((mod - Di[0]) / 2))
    rp = cdiv((-Bi[0] + sq[0], -Bi[1] + sq[1]), (2 * Ai[0], 2 * Ai[1])); rm = cdiv((-Bi[0] - sq[0], -Bi[1] - sq[1]), (2 * Ai[0], 2 * Ai[1]))
    G['S1'] = bool((rp[1] > 0 and rm[1] < 0) or (rp[1] < 0 and rm[1] > 0))
    r1, r2, sign = (rp, rm, '+') if rp[1] > 0 else (rm, rp, '-')
    info['S1'] = {'disc': repr(disc), 'a_pil_enclosure_re_im': [str(r1[0]), str(r1[1])], 'a_other_enclosure_re_im': [str(r2[0]), str(r2[1])],
                  'a_pil_formula': '(-B %s sqrt(disc))/(2A), principal square root (Im sqrt(disc) > 0)' % sign,
                  'crosswalk': 'a_pil = root with Im a > 0 = a_2^- of P1-c = a_+ of the LH2012 owner assessment and the pilot design'}
    a_num = complex(float(mpmath.mpf(r1[0].mid)), float(mpmath.mpf(r1[1].mid)))
    # ---- S2: graph equation in E ----
    NZ = 7
    FzS = Ser({k: Ec([E_(v), 0, 0]) for k, v in Fz.items()}, NZ, NZ); FwS = Ser({k: Ec([E_(v), 0, 0]) for k, v in Fw.items()}, NZ, NZ)
    Zs = Ser({(1, 0): Ec.c(1)}, NZ, 0); zero_y = Ser({}, NZ, 0)
    zser = lambda d: Ser({(k, 0): Ec([v, 0, 0]) for k, v in d.items()}, NZ, 0)
    def graph_res(phi):
        Fzp = FzS.compose(Zs, phi).trunc(NZ, 0); Fwp = FwS.compose(Zs, phi).trunc(NZ, 0)
        return Fwp - phi.compose(Fzp, zero_y)   # P1-c sign convention: F_w(z, phi) - phi(F_z(z, phi))
    g2 = {}
    phi2 = zser({2: A_E}); res2 = graph_res(phi2)
    g2['z0..z5_vanish'] = all(res2.coef(k, 0).iszero() for k in range(0, 6))
    def affine(phi_base, k):
        R0 = graph_res(phi_base).coef(k + 3, 0).v[0]
        R1 = graph_res(phi_base + zser({k: E_(1)})).coef(k + 3, 0).v[0]
        R2 = graph_res(phi_base + zser({k: E_(2)})).coef(k + 3, 0).v[0]
        Lk = R1 - R0
        return Lk, R0, (R2 - R0) == 2 * Lk
    L3, R3, lin3 = affine(phi2, 3); g2['L3=ell(k*-3)'] = lin3 and L3 == ELL * (E_(KSTAR) - 3)
    a3 = -R3 / L3; phi3 = phi2 + zser({3: a3}); g2['z6_solved'] = graph_res(phi3).coef(6, 0).iszero()
    L4, R4, lin4 = affine(phi3, 4); g2['L4=ell(k*-4)'] = lin4 and L4 == ELL * (E_(KSTAR) - 4)
    a4 = -R4 / L4; phi4 = phi3 + zser({4: a4}); g2['z7_solved'] = graph_res(phi4).coef(7, 0).iszero()
    g2['b2_nonzero'] = not a4.iszero()
    G['S2'] = all(g2.values())
    info['S2'] = {'gates': {k: bool(v) for k, v in g2.items()}, 'b1=a3': repr(a3), 'b2=a4': repr(a4),
                  'b1_numeric_pil': str(a3.complex(a_num)), 'b2_numeric_pil': str(a4.complex(a_num)), 'm': 2}
    b1 = a3 + (E_(Qs(Fr(1, 1000))) if opt.control == 'B' else E_(0))
    # ---- S3: lifted map ----
    NX, NY = 5, 2
    Xb = Ser({(1, 0): Ec.c(1)}, 7, NY); Ub = Ser({(0, 1): Ec.c(1), (0, 0): Ec([A_E, 0, 0])}, 7, NY)
    W2 = Xb * Xb * Ub
    Fzl = Ser(FzS.d, 7, NY).compose(Xb, W2); Fwl = Ser(FwS.d, 7, NY).compose(Xb, W2)
    def shift(s, n, nx):
        d = {}
        for (i, j), v in s.d.items():
            if i < n: return None
            d[(i - n, j)] = v
        return Ser(d, nx, NY)
    Gq = shift(Fzl - Xb, 4, NX); Hq = shift(Fwl - W2, 5, NX)
    G['S3_div'] = Gq is not None and Hq is not None
    X = Ser({(1, 0): Ec.c(1)}, NX, NY); Yv = Ser({(0, 1): Ec.c(1)}, NX, NY); aE = Ec([A_E, 0, 0])
    X3 = X * X * X
    t = X3 * Gq; inv_sq = Ser.c(1, NX, NY) - 2 * t + 3 * (t * t)       # (1 + t)^-2 exact to x^5 since t = O(x^3)
    xp = X + (X3 * X) * Gq
    yp = (Yv + aE + X3 * Hq) * inv_sq - aE
    dy = yp - Yv
    G['S3_order'] = all(dy.coef(i, j).iszero() for i in range(3) for j in range(NY + 1)) and dy.coef(3, 0).iszero()
    # ---- S4: normalized coordinates ----
    Cc = Ec([0, E_(1), 0]); Cinv = Ec([0, 0, E_(1) / Ec.C3]); assert (Cc * Cinv) == 1
    sx = X * Cinv; sy = Yv + sx * Ec([b1, 0, 0])
    F1 = xp.compose(sx, sy) * Cc; F2 = yp.compose(sx, sy) - xp.compose(sx, sy) * Ec([b1, 0, 0])
    alpha_used = ALPHA + (Qs(Fr(1, 7)) if opt.control == 'A' else Qs(0))
    def def41(P1, P2, alph):
        f1 = (P1.coef(1, 0) == 1 and all(P1.coef(i, 0).iszero() for i in (0, 2, 3)) and P1.coef(4, 0) == -1
              and all(P1.coef(i, j).iszero() for i in range(4) for j in (1, 2)))
        f2 = (P2.coef(0, 1) == 1 and all(P2.coef(i, 1).iszero() for i in (1, 2)) and P2.coef(3, 1) == -Ec.c(E_(alph))
              and all(P2.coef(i, 0).iszero() for i in range(5)) and not P2.coef(5, 0).iszero()
              and all(P2.coef(i, 2).iszero() for i in range(3)))
        return f1 and f2
    G['S4'] = def41(F1, F2, alpha_used)
    info['S4'] = {'F1_xi4Y': repr(F1.coef(4, 1)), 'F1_xi5': repr(F1.coef(5, 0)), 'F2_xi3Y': repr(F2.coef(3, 1)), 'F2_xi3Y2': repr(F2.coef(3, 2)),
                  'F2_xi4Y': repr(F2.coef(4, 1)), 'psi0=F2_xi5': repr(F2.coef(5, 0))}
    # ---- S5: formal inverse ----
    Ix, Iy = X, Yv
    for _ in range(NX + NY + 3):
        Ix_n = X - (F1.compose(Ix, Iy) - Ix); Iy_n = Yv - (F2.compose(Ix, Iy) - Iy)
        if Ix_n == Ix and Iy_n == Iy: break
        Ix, Iy = Ix_n, Iy_n
    G['S5_comp'] = (F1.compose(Ix, Iy) == X and F2.compose(Ix, Iy) == Yv and Ix.compose(F1, F2) == X and Iy.compose(F1, F2) == Yv)
    rinv = Ec.c(E_(Qs(1) / LAMBDA)); rr = Ec.c(E_(LAMBDA))
    J1 = Ix.compose(X * rinv, Yv) * rr; J2 = Iy.compose(X * rinv, Yv)
    G['S5_form'] = def41(J1, J2, ALPHA)
    info['S5'] = {'inverse_xi4': repr(Ix.coef(4, 0)), 'inverse_xi3Y': repr(Iy.coef(3, 1)), 'rotated_inverse_xi4': repr(J1.coef(4, 0)),
                  'rotated_inverse_xi3Y': repr(J2.coef(3, 1)), 'rotated_inverse_psi0': repr(J2.coef(5, 0)), 'rho': 'e^{i pi/3}, rho^3 = -1'}
    ok = all(G.values())
    for k in sorted(G): print(k, 'PASS' if G[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL')
    if opt.control is None:
        with open(opt.out, 'w', encoding='utf-8', newline='\n') as f:
            json.dump({'gates': G, 'info': info, 'all_pass': ok, 'script': 'dyad_open20_an_stage1_prep.py', 'alpha': repr(ALPHA), 'k': 3, 'm': 2,
                       'field': 'Q(i sqrt3)[a]/(A a^2 + B a + C), then [c]/(c^3 + ell); elements printed as p + q*i*sqrt3, (...) + (...)*a, (...)*c^k'},
                      f, indent=1, sort_keys=True, ensure_ascii=False); f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as ex:
        import traceback; traceback.print_exc(); print('CRASH', type(ex).__name__, ex); sys.exit(3)
