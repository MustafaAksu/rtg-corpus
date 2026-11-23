#!/usr/bin/env python3
"""
open16_alias_phase.py
=====================
OPEN 16 / OPEN 5 — Alias phase G_-(U) exact computation.

Predecessor prescription (DSN v5.4.7):
  Decompose the projection operator as:
    Π(Q₀, U, O) = Π₀ + a₁·Q₀ + Π_alias(U, O) + a₂·Q₀² + O(Q₀³)
  where:
    Π₀    = π − arctan(√15)             [ALG]
    a₁    = 559√15/4860                  [ALG by convention (Lie gauge)]
    Π_alias = arg G_-(U)                 [ALG — this script]
    a₂    = [OPEN — requires degree-7 Lie-gauge normalization]

ALIAS FUNCTION (DSN §9.7):
  G_-(U) = 2·sinh(λU) / (λ·sinh(2U))
  where λ = -2 + 2iτ,  τ = 2√3/3

KEY RESULT [ALG]:
  At the canonical window U = π/τ (one full DSI log-period):
    G_-(π/τ) = 1/(1-iτ) = 3/7 + (2√3/7)·i    [exact over Q(√3)]
    |G_-(π/τ)| = √(3/7) = √21/7               [ALG, already in DSN]
    arg G_-(π/τ) = atan(τ) = atan(2√3/3)       [ALG — NEW]
                 = 0.857071947850131 rad
                 = 49.107°

DERIVATION (exact):
  λU at U=π/τ:
    λU = (-2+2iτ)·(π/τ) = -2π/τ + 2πi
  sinh(λU) = sinh(-2π/τ + 2πi)
           = sinh(-2π/τ)·cos(2π) + i·cosh(-2π/τ)·sin(2π)
           = sinh(-2π/τ)·1 + i·cosh(-2π/τ)·0
           = −sinh(2π/τ)     [purely real]
  sinh(2U) = sinh(2π/τ)      [real]

  G_-(π/τ) = 2·(−sinh(2π/τ)) / [(−2+2iτ)·sinh(2π/τ)]
           = −2 / (−2+2iτ) = 2 / (2−2iτ) = 1/(1−iτ)
           = (1+iτ)/(1+τ²) = (1+iτ)/(7/3) = 3(1+iτ)/7
           = 3/7 + i·(2√3/7)

  → arg G_-(π/τ) = atan(Im/Re) = atan((2√3/7)/(3/7)) = atan(2√3/3) = atan(τ)
"""

import mpmath as mp
mp.mp.dps = 120
from mpmath import (mpc, mpf, sqrt, pi, atan, atan2, sinh, log,
                    re, im, nstr, fabs)

def run():
    tau = 2*sqrt(mpf(3))/3
    s3  = sqrt(mpf(3))

    print("="*68)
    print("OPEN 16 — Alias Phase Archival  [ALG]")
    print("="*68)

    # ── Exact components ──────────────────────────────────────────────────
    Re_exact  = mpf(3)/7
    Im_exact  = 2*s3/7
    G_exact   = mpc(Re_exact, Im_exact)

    # ── Numerical verification via formula ────────────────────────────────
    U    = pi/tau
    lam  = mpc(-2, 2*tau)
    G_num = 2*sinh(lam*U) / (lam*sinh(2*U))
    G_formula = mpc(1,0) / mpc(1,-tau)

    err_num     = abs(G_exact - G_num)
    err_formula = abs(G_exact - G_formula)

    print(f"\nτ = 2√3/3 = {nstr(tau,18)}")
    print(f"U = π/τ  = {nstr(U,18)}")
    print(f"\nExact Q(√3) form:  G_-(π/τ) = 3/7 + (2√3/7)·i")
    print(f"  = 1/(1−iτ)                          [exact algebraic simplification]")
    print(f"\nRe(G_-(π/τ)) = 3/7 = {nstr(Re_exact,20)}")
    print(f"Im(G_-(π/τ)) = 2√3/7 = {nstr(Im_exact,20)}")
    print(f"\nVerification errors:")
    print(f"  |G_exact − G_numeric| = {nstr(err_num,5)}")
    print(f"  |G_exact − 1/(1−iτ)| = {nstr(err_formula,5)}")

    # ── Magnitude ─────────────────────────────────────────────────────────
    mag = abs(G_exact)
    mag_theory = sqrt(mpf(3)/7)
    print(f"\n|G_-(π/τ)|  = √(3/7) = √21/7 = {nstr(mag,18)}")
    print(f"             verify: {nstr(mag_theory,18)}  err={nstr(abs(mag-mag_theory),5)}")

    # ── Phase [ALG NEW] ───────────────────────────────────────────────────
    phi_G     = atan(tau)           # exact
    phi_G_num = atan2(im(G_exact), re(G_exact))
    print(f"\narg G_-(π/τ) = atan(τ) = atan(2√3/3)   [ALG]")
    print(f"             = {nstr(phi_G,18)} rad")
    print(f"             = {nstr(phi_G*180/pi,18)}°")
    print(f"  verify atan2: err = {nstr(abs(phi_G-phi_G_num),5)}")

    # ── Derivative dG_-/dU at U=π/τ (for Taylor expansion) ──────────────
    # G_-(U) = 2sinh(λU)/(λ sinh(2U))
    # dG_-/dU = [2λcosh(λU)·λsinh(2U) − 2sinh(λU)·λ·2cosh(2U)] / (λsinh(2U))²
    #         = [2λ²cosh(λU)sinh(2U) − 4λsinh(λU)cosh(2U)] / (λsinh(2U))²
    # Let's compute numerically at U=π/τ
    from mpmath import cosh, diff
    def G_minus_func(U_val):
        return 2*sinh(lam*U_val) / (lam*sinh(2*U_val))

    dG_dU = diff(G_minus_func, U)
    print(f"\ndG_-/dU at U=π/τ = {nstr(dG_dU,18)}")
    print(f"  |dG_-/dU| = {nstr(abs(dG_dU),18)}")
    print(f"  arg(dG_-/dU) = {nstr(atan2(im(dG_dU),re(dG_dU))*180/pi,18)}°")

    # ── OPEN 16 decomposition statement ──────────────────────────────────
    Pi0 = pi - atan(sqrt(mpf(15)))
    a1  = 559*sqrt(mpf(15))/4860

    print(f"\n{'='*68}")
    print(f"OPEN 16 DECOMPOSITION STATEMENT [ALG structure]")
    print(f"{'='*68}")
    print(f"""
  Π(Q₀, U, O) = Π₀ + a₁·Q₀ + Π_alias(U,O) + a₂·Q₀² + O(Q₀³)

  Π₀           = π − arctan(√15) = {nstr(Pi0,15)} rad   [ALG]
  a₁           = 559√15/4860     = {nstr(a1,15)}         [ALG by convention (Lie gauge)]
  Π_alias(π/τ) = arg G_-(π/τ)   = atan(2√3/3)           [ALG — this result]
               = {nstr(phi_G,15)} rad  = {nstr(phi_G*180/pi,12)}°
  a₂           = [OPEN — requires degree-7 Lie-gauge normalization]

  G_-(π/τ) exact:  3/7 + (2√3/7)·i   [Q(√3)]
  |G_-(π/τ)|     = √(3/7) = √21/7
  arg G_-(π/τ)   = atan(τ) = atan(2√3/3)

DISTINCTION (per predecessor):
  Π_alias is the WINDOW-REFERENCE correction from the observable convention.
  It does NOT contribute to a₂ (the intrinsic O(Q₀²) coefficient).
  a₂ requires the degree-7 Lie-gauge log (next normalization layer).

STATUS TAGS:
  G_-(π/τ) = 1/(1−iτ)  exact simplification:  [ALG]
  |G_-| = √(3/7):                              [ALG — confirmed from DSN]
  arg G_- = atan(2√3/3):                       [ALG — NEW this session]
  Π_alias(π/τ) = atan(τ):                      [ALG structure]
  a₂:                                           [OPEN]
""")

    return {
        'G_minus': G_exact,
        'magnitude': mag,
        'phase_rad': phi_G,
        'phase_deg': float(phi_G*180/pi),
        'Re': Re_exact,
        'Im': Im_exact,
    }


if __name__ == "__main__":
    result = run()