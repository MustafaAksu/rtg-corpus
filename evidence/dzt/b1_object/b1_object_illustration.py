#!/usr/bin/env python3
"""DZT B1 object record (triage row 6): coefficient arithmetic and a [NUM] orbit illustration.

    python3 -I evidence/dzt/b1_object/b1_object_illustration.py [M_MAX]      (default 1000000 blocks)

Written for the record from the Dyadic definitions at dyad-v6.4.24; no recovered DZT script is run.
Part 1 (exact): from the six-step chart jet of DYAD-ALG-NF6, mu = -1/2 - (2/sqrt3) i and Re a32 = -97/432:
  the chart isotropic coefficient |mu|^2 + 2 Re a32 = 245/216 (RECOG-ALG-CHART-LAWS) and the reciprocal-drift
  coefficient 1 - 245/216 = -29/216 (RECOG-ALG-A1C-RECIPROCAL-DRIFT), against the raw angular-mean coefficient
  47/54 (DYAD-ALG-RAW-ANGULAR-MEAN) and the recovered B1 value 1 - 47/54 = 7/54.
Part 2 ([NUM], illustration only, double precision): orbits of the primitive map T (DYAD-DEF-PRIMITIVE-MAP)
  from three starts in U = {0 < Q <= 1/625}; at block times m (six steps) it prints
    D_prim(m) = 1/Q_m - 1/Q_0 - m          primitive observable Q = |W|^2, W = rho - eta/2 + i (sqrt3/2) eta
    D_chart(m) = 1/q_m - 1/q_0 - m         chart amplitude to first order, q = |W - h2(W)|^2 (h2 of DYAD-ALG-NF6)
  with the chart prediction -(29/216) H_m(b), H_m(b) = sum_{j<m} 1/(b+j), b = 1/q_0, the recovered B1 prediction
  +(7/54) H_m(b), and sqrt(m). The first-order chart (h2 only) leaves an O(1) error in 1/q; the full degree-6 chart
  h is not used here. Not a proof input.
"""
import math, sys
from fractions import Fraction as Fr

M_MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000
mu2 = Fr(1, 4) + Fr(4, 3)
re_a32 = Fr(-97, 432)
a_chart = mu2 + 2 * re_a32
print("Part 1 (exact): |mu|^2 = %s, 2 Re a32 = %s, |mu|^2 + 2 Re a32 = %s; 1 - that = %s" % (mu2, 2 * re_a32, a_chart, 1 - a_chart))
print("                raw angular mean 47/54 = %s; recovered B1 drift 1 - 47/54 = %s; 245/216 - 47/54 = %s"
      % (Fr(47, 54), 1 - Fr(47, 54), a_chart - Fr(47, 54)))
assert a_chart == Fr(245, 216) and 1 - a_chart == Fr(-29, 216) and a_chart != Fr(47, 54)

s3 = math.sqrt(3)
c20, c11, c02 = complex(-1 / 12, -s3 / 12), -1 / 3, complex(1 / 24, -s3 / 24)   # h2 of DYAD-ALG-NF6


def h2(z):
    return c20 * z * z + c11 * z * z.conjugate() + c02 * z.conjugate() ** 2


def T(r, e):
    return r - math.sin(e), e + math.expm1(r) - math.sin(e)


def Wof(r, e):
    return complex(r - e / 2, s3 / 2 * e)


marks = sorted({10 ** k for k in range(1, 7)} | {3 * 10 ** k for k in range(1, 6)})
marks = [m for m in marks if m <= M_MAX]
print("Part 2 ([NUM] illustration): D_prim = 1/Q_m-1/Q_0-m; D_chart = 1/q_m-1/q_0-m (first-order chart);")
print("        chart = -(29/216) H_m(b); recovered = +(7/54) H_m(b); b = 1/q_0")
for (r, e) in [(0.03, 0.0), (0.0, 0.03), (0.02, -0.02)]:
    W = Wof(r, e)
    Q0 = abs(W) ** 2
    q0 = abs(W - h2(W)) ** 2
    b = 1 / q0
    print("start (rho, eta) = (%g, %g): Q_0 = %.6f, q_0 = %.6f" % (r, e, Q0, q0))
    m, H, k = 0, 0.0, 0
    while m < marks[-1]:
        for _ in range(6):
            r, e = T(r, e)
        H += 1 / (b + m)
        m += 1
        if m == marks[k]:
            W = Wof(r, e)
            Q, q = abs(W) ** 2, abs(W - h2(W)) ** 2
            print("  m=%8d  D_prim=%10.3f  D_chart=%8.3f  chart=%8.3f  recovered=%8.3f  sqrt(m)=%7.1f"
                  % (m, 1 / Q - 1 / Q0 - m, 1 / q - 1 / q0 - m, -29 / 216 * H, 7 / 54 * H, math.sqrt(m)))
            k += 1
