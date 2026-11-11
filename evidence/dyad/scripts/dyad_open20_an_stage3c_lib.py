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
