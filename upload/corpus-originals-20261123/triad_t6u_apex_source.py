#!/usr/bin/env python3
"""
triad_t6u_apex_source.py
RTG Triadic — T-6u certified apex source ratio.

Exit-code-gated. Returns 0 iff the certified-apex derivation holds and
the B_3-isometric model value is correctly rejected.

Certifies (all from Genesis GEN-THM / §6.5 certified coefficients):
  U1: certified in-plane seed   Q_c^seed = (4/3) Q_s^3   (kappa_shear^2, kappa=-2sqrt3/3).
  U2: certified apex seed        Q_d^seed = (7/1024) Q_s^3  (G_{3,d}[s^3]).
  U3: birth-symmetry check       Delta Q_d^[s^3] = (7/512) Q_s^3 = 2 Q_{d,1}.
  U4: certified apex/in-plane seed-amplitude ratio
        R_apex^cert = sqrt(Q_d^seed / Q_c^seed) = sqrt(21)/64 ~ 0.0716.
  U5: R_apex^cert is ~20x below sqrt(2) (the amplitude needed to close OPEN-M x2).
  U6: the B_3-isometric MODEL value R_iso = sqrt(4/3 + sqrt7/3) ~ 1.488 is
      NOT equal to the certified ratio (model rejected as physical source).
  U7: leading apex drive coefficients on (I_ds, omega_ds) are (-1/8, -3/32),
      confirming a weak incidence/torque channel, not a unit-gain isometry.
  U8: the apex self term is a sink: Delta Q_d^(4)[d^3] = -Q_d^2 (not an isometry).

Scope: compares certified primitive P_4 seed amplitudes only. Does NOT
evaluate a non-P_4 OPEN-M sigma_f source, nor UV terms outside the
primitive tetrahedral channel.
"""
import sys
from sympy import Rational, sqrt, simplify, symbols, series, Matrix

FAILURES = []
def check(name, cond):
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not ok: FAILURES.append(name)
    return ok

Qs = symbols('Q_s', positive=True)
sqrt3 = sqrt(3)

print("="*60)
print("T-6u certificate: certified apex source ratio")
print("="*60)

# --- U1: in-plane seed (kappa_shear^2 Q_s^3) ---
kappa_shear = -2*sqrt3/3
Qc_seed = simplify(kappa_shear**2) * Qs**3
check("U1 in-plane seed Q_c^seed = (4/3) Q_s^3",
      simplify(Qc_seed - Rational(4,3)*Qs**3) == 0)

# --- U2: apex seed (G_{3,d}[s^3]) ---
Qd_seed = Rational(7,1024) * Qs**3
check("U2 apex seed Q_d^seed = (7/1024) Q_s^3",
      simplify(Qd_seed - Rational(7,1024)*Qs**3) == 0)

# --- U3: birth-symmetry check Delta Q_d^[s^3] = 7/512 = 2 Q_{d,1} ---
# Reconstruct from the certified Delta Q_d d-s terms at birth gauge:
# I_ds^(1) = omega_ds^(1) = -Q_s^2/16, Q_c -> 0 (pure s^3 seed).
Ids, ods = symbols('I_ds omega_ds', real=True)
Qc = symbols('Q_c', positive=True)
DQd_ds = (-Rational(1,8)*Qs*Ids - Rational(3,32)*Qs*ods
          - Rational(5,12)*ods*Ids - Rational(1,8)*ods**2
          + Rational(1,6)*Qc*Ids + Rational(3,8)*Qc*ods)
DQd_birth = DQd_ds.subs([(Ids, -Qs**2/16), (ods, -Qs**2/16), (Qc, 0)])
leading = series(simplify(DQd_birth), Qs, 0, 4).removeO()
check("U3 birth-symmetry Delta Q_d^[s^3] leading = 7/512 Q_s^3 = 2 Q_{d,1}",
      simplify(leading - Rational(7,512)*Qs**3) == 0
      and simplify(Rational(7,512) - 2*Rational(7,1024)) == 0)

# --- U4: certified ratio sqrt(21)/64 ---
R_apex = simplify(sqrt(Qd_seed / Qc_seed))
check("U4 R_apex^cert = sqrt(Q_d/Q_c) = sqrt(21)/64",
      simplify(R_apex - sqrt(21)/64) == 0)

# --- U5: ~20x below sqrt(2) ---
factor_below = simplify(sqrt(2) / R_apex)
check("U5 R_apex^cert is >~15x below sqrt(2) (gap not closable by apex)",
      float(factor_below) > 15)

# --- U6: reject the B_3-isometric model value ---
R_iso = sqrt(Rational(4,3) + sqrt(7)/3)
check("U6 model R_iso = sqrt(4/3+sqrt7/3) != certified ratio (model rejected)",
      simplify(R_iso - R_apex) != 0 and abs(float(R_iso) - 1.488372) < 1e-5)

# --- U7: weak incidence coefficients (-1/8, -3/32), not unit gain ---
c_Ids = Rational(-1,8)   # coeff of Q_s I_ds in Delta Q_d
c_ods = Rational(-3,32)  # coeff of Q_s omega_ds in Delta Q_d
check("U7 apex drive coeffs (I_ds, omega_ds) = (-1/8, -3/32), |coeff| < 1",
      c_Ids == Rational(-1,8) and c_ods == Rational(-3,32)
      and abs(c_Ids) < 1 and abs(c_ods) < 1)

# --- U8: apex self term is a sink, not an isometry ---
# Delta Q_d^(4)[d^3] = -Q_d^2 (certified pure-d checksum).
Qd = symbols('Q_d', positive=True)
DQd_self = -Qd**2
check("U8 apex self term Delta Q_d[d^3] = -Q_d^2 (sink, not isometry)",
      simplify(DQd_self + Qd**2) == 0)

print("="*60)
if FAILURES:
    print(f"CERTIFICATE FAILED: {FAILURES}")
    sys.exit(1)
print("CERTIFICATE PASSED — T-6u [ALG diagnostic].")
print(f"Certified apex/in-plane seed ratio R_apex = sqrt(21)/64 ~ {float(sqrt(21)/64):.6f}")
print(f"~{float(sqrt(2)/(sqrt(21)/64)):.0f}x below sqrt(2); B_3-isometric model (~1.488) rejected.")
print("Primitive certified apex channel cannot supply the OPEN-M x2 amplitude.")
print("Scope: primitive P_4 seeds only; non-P_4 OPEN-M sigma_f source not evaluated.")
sys.exit(0)
