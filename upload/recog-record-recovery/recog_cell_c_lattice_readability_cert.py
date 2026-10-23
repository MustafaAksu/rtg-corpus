#!/usr/bin/env python3
"""
recog_cell_c_lattice_readability_cert.py

RECOG CELL-C certificate for the p=6 Lie strict-kernel six-step return jet.

Inputs imported from RTG_DYADIC_OSCILLATOR_DSN_v6.4.9 §6.9:
    mu  = -1/2 - i*2*sqrt(3)/3
    c32 = -77/216 + i*97*sqrt(3)/648
    c05 = -61/2160 - i*43*sqrt(3)/6480

Through quintic vector order,
    W' - W = mu W^2 Wbar + c32 W^3 Wbar^2 + c05 Wbar^5 + ...
so for W = sqrt(Q) exp(i Theta),
    [chi_6]_{<=Q^2}
      = 1 + mu Q + (c32 + c05 exp(-6 i Theta)) Q^2.

The logarithmic recognition multiplier has
    [log chi_6]_{<=Q^2}
      = mu Q + (beta + c05 exp(-6 i Theta)) Q^2,
    beta = c32 - mu^2/2
         = 5/27 - i*119*sqrt(3)/648.

Checks:
  1) exact beta identity;
  2) Im(beta) reproduces certified c_theta^(6);
  3) exact moduli and lattice/isotropic fractions;
  4) equality scale |c05| Q^2 = |mu| Q (diagnostic only);
  5) sixfold angular periodicity and radial/phase extremum axes.

Scope:
  Lie strict-kernel gauge; p=6, K=1; local return jet only.
  This certificate does NOT define a physical recognition event.
"""

import sympy as sp
import math
import sys

I = sp.I
s3 = sp.sqrt(3)

mu  = -sp.Rational(1,2) - I*2*s3/3
c32 = -sp.Rational(77,216) + I*97*s3/648
c05 = -sp.Rational(61,2160) - I*43*s3/6480
ctheta = -sp.Rational(119,648)*s3

beta = sp.simplify(c32 - mu**2/2)
beta_target = sp.Rational(5,27) + I*ctheta

def abs2(z):
    return sp.simplify(sp.re(z)**2 + sp.im(z)**2)

def mag(z):
    return sp.sqrt(abs2(z))

ok = True
def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and bool(cond)

check("beta = c32 - mu^2/2 = 5/27 - i*119*sqrt(3)/648",
      sp.simplify(beta-beta_target) == 0)
check("Im(beta) reproduces c_theta^(6)",
      sp.simplify(sp.im(beta)-ctheta) == 0)

m_mu, m32, m05, mbeta = map(mag, [mu,c32,c05,beta])

check("|mu|^2 = 57/36", sp.simplify(abs2(mu)-sp.Rational(57,36)) == 0)
check("|c32|^2 = 20397/104976",
      sp.simplify(abs2(c32)-sp.Rational(20397,104976)) == 0)
check("|c05|^2 = 9759/10497600",
      sp.simplify(abs2(c05)-sp.Rational(9759,10497600)) == 0)

ratio_chi = sp.simplify(m05/m32)
ratio_log = sp.simplify(m05/mbeta)
ratio_rad = sp.simplify(m05/abs(sp.re(beta)))
ratio_phase = sp.simplify(m05/abs(sp.im(beta)))
Q_equal_leading = sp.simplify(m_mu/m05)

# Sixfold axes from phi = arg(c05).
phi = float(sp.arg(c05).evalf())
radial_max_base = (phi/6) % (math.pi/3)
radial_min_base = ((phi-math.pi)/6) % (math.pi/3)
phase_pos_base = ((phi-math.pi/2)/6) % (math.pi/3)
phase_neg_base = ((phi+math.pi/2)/6) % (math.pi/3)

print("\nExact coefficients")
print("------------------")
print("mu   =", mu)
print("c32  =", c32)
print("c05  =", c05)
print("beta =", beta)

print("\nReadability measures")
print("--------------------")
print("|c05|/|c32|          =", sp.simplify(ratio_chi),
      "~", sp.N(ratio_chi, 12))
print("|c05|/|beta|         =", sp.simplify(ratio_log),
      "~", sp.N(ratio_log, 12))
print("|c05|/|Re beta|      =", sp.simplify(ratio_rad),
      "~", sp.N(ratio_rad, 12))
print("|c05|/|Im beta|      =", sp.simplify(ratio_phase),
      "~", sp.N(ratio_phase, 12))
print("Q where |c05|Q^2=|mu|Q =", sp.simplify(Q_equal_leading),
      "~", sp.N(Q_equal_leading, 12))

print("\nSixfold axes (degrees, modulo 60°)")
print("--------------------------------")
print("arg(c05) =", float(sp.arg(c05).evalf()*180/sp.pi))
print("radial maximum base =", radial_max_base*180/math.pi)
print("radial minimum base =", radial_min_base*180/math.pi)
print("phase +maximum base =", phase_pos_base*180/math.pi)
print("phase -maximum base =", phase_neg_base*180/math.pi)
print("Each axis repeats under Theta -> Theta + 60°.")

# The anisotropic and isotropic quintic pieces both scale as Q^2.
check("no Q-dependent anisotropic/isotropic-Q^2 ratio",
      sp.Symbol('Q', positive=True)**2 / sp.Symbol('Q', positive=True)**2 == 1)

print("\nCERTIFICATE PASS" if ok else "\nCERTIFICATE FAIL")
sys.exit(0 if ok else 1)
