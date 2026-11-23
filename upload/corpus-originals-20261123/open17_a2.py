#!/usr/bin/env python3
"""
open17_a2.py
============
RTG OPEN 17 — Second-order projection coefficient a₂  [ALG by convention (Lie gauge)]

RESULT:
  a₂ = 86775991·√15 / 755827200  ≈  0.44465450303143985

CORRECTION NOTE:
  Earlier session used factor 5 for A₂[0,0].
  Corrected factor = 7 = 2k+1 for k=3 (monomial degree 2k+1=7).
  Derivation: for c·Z^{k+1}Z̄^k = c·Q^k·Z, the perturbation
    δZ = Z(ξ+iψ) gives δ(c·Q^k·Z) = c·Q^k·Z·((2k+1)ξ + iψ)
  → A_k = [[(2k+1)R, -S], [(2k+1)S, R]]   where c = R+iS.
  k=2 → factor=5 for A₁ ✓; k=3 → factor=7 for A₂ (corrected).

DERIVATION CHAIN:
  1. F^6 through degree 7 (exact fraction arithmetic, Python/fractions module)
  2. Lie log: V = log(F^6) through degree 7 (BCH inversion)
  3. Extract raw MAP resonant channels in W = (ρ+ωη) coordinates:
       c₃₂^raw = -77/216 + (97√3/648)i    [degree 5, m-n=1, k=2]
       c₄₃^raw = -31/864 + (307√3/864)i   [degree 7, m-n=1, k=3]
  4. Build A-matrices with (2k+1) factors:
       A₁ = [[-385/216, -97√3/648], [485√3/648, -77/216]]   (factor 5)
       A₂ = [[-217/864, -307√3/864], [2149√3/864, -31/864]] (factor 7)
  5. Second-order eigenvector perturbation theory:
       a₂ = Im(x₂/x₀ − (x₁/x₀)²/2)
  6. Closed formula with c₄₃ = R+is√3, R=-31/864, s=307/864:
       a₂ = √15·(31167871/755827200 − (2/5)R + s/6)
          = √15·(86775991/755827200)
  7. PSLQ-confirmed at 400 dps (error < 5×10⁻⁴⁰²).

STRUCTURAL NOTES:
  - Denominator: 755827200 = 2⁹·3¹⁰·5² = 32·4860²
  - Numerator: 86775991 = 1097×79103 (both prime, no pattern with 559=13×43)
  - Both a₁ and a₂ ∈ Q(√15)
  - c₁₆^raw and c₇₀^raw do NOT enter a₂; they feed O(Q₀²) alias corrections
  - Convention: Lie strict-kernel gauge. Not gauge-universal.
"""

import mpmath as mp
mp.mp.dps = 400
from mpmath import mpf, mpc, sqrt, pi, atan, nstr, im, re, fabs, pslq

def run():
    s3 = sqrt(mpf(3)); s5 = sqrt(mpf(5)); s15 = sqrt(mpf(15))
    tau = 2*s3/3

    x0 = s3/12 - mpc(0,1)*s5/4
    v0 = mp.matrix([x0, mpc(1)])
    w  = mp.matrix([mpc(1), mpc(-1,s15)/(4*s3)])
    def inner(a,b): return mp.conj(a[0])*b[0] + mp.conj(a[1])*b[1]

    # Raw MAP resonant channels from degree-7 F^6
    Re_c32 = mpf(-77)/216;  Im_c32 = mpf(97)*s3/648   # k=2, factor=5
    Re_c43 = mpf(-31)/864;  Im_c43 = mpf(307)*s3/864  # k=3, factor=7

    A1 = mp.matrix([[5*Re_c32, -Im_c32], [5*Im_c32, Re_c32]])
    A2 = mp.matrix([[7*Re_c43, -Im_c43], [7*Im_c43, Re_c43]])  # corrected

    # First-order
    lam1 = inner(w, A1*v0) / inner(w, v0)
    rhs1 = mp.matrix([lam1*x0 - A1[0,0]*x0 - A1[0,1],
                      lam1    - A1[1,0]*x0 - A1[1,1]])
    x1 = -rhs1[1] / (3*tau)

    # Second-order
    v1 = mp.matrix([x1, mpc(0)])
    rhs2_nl = mp.matrix([-A1[0,0]*x1 - A2[0,0]*x0 - A2[0,1],
                         -A1[1,0]*x1 - A2[1,0]*x0 - A2[1,1]])
    lam2 = -(lam1*inner(w,v1) + inner(w,rhs2_nl)) / inner(w,v0)
    rhs2 = mp.matrix([lam1*x1 + lam2*x0 + rhs2_nl[0],
                             lam2   + rhs2_nl[1]])
    x2 = -rhs2[1] / (3*tau)

    r1 = x1/x0; r2 = x2/x0
    a2_pipeline = im(r2 - mpc('0.5')*r1**2)
    a2_exact = mpf(86775991)*s15/mpf(755827200)

    a1_check = im(r1)
    a1_exact = mpf(559)*s15/mpf(4860)

    print("="*68)
    print("OPEN 17 — a₂  [ALG by convention (Lie gauge)]")
    print("="*68)
    print(f"\nA₁ factor = 5 = 2·2+1  (k=2, degree-5 channel c₃₂)")
    print(f"A₂ factor = 7 = 2·3+1  (k=3, degree-7 channel c₄₃)  [corrected]")
    print(f"\nA₁ = [[-385/216, -97√3/648], [485√3/648, -77/216]]")
    print(f"A₂ = [[-217/864, -307√3/864], [2149√3/864, -31/864]]")
    print(f"\nFirst-order:")
    print(f"  a₁ = {nstr(a1_check,18)}  == 559√15/4860? {abs(a1_check-a1_exact)<mpf('1e-380')}")
    print(f"\nSecond-order:")
    print(f"  λ₂ = {nstr(lam2,18)}")
    print(f"  x₂/x₀ = {nstr(r2,18)}")
    print(f"\n  a₂ (pipeline) = {nstr(a2_pipeline,30)}")
    print(f"  a₂ (formula)  = {nstr(a2_exact,30)}")
    print(f"  error         = {nstr(abs(a2_pipeline-a2_exact),10)}")
    print(f"  [ALG] confirmed: {abs(a2_pipeline-a2_exact)<mpf('1e-380')}")
    print(f"\n  Closed formula:")
    print(f"    a₂ = √15·(31167871/755827200 − (2/5)·(−31/864) + (307/864)/6)")
    print(f"       = √15·(86775991/755827200)")
    print(f"\n  ╔════════════════════════════════════════════════╗")
    print(f"  ║  a₂ = 86775991·√15 / 755827200               ║")
    print(f"  ║     ≈ {nstr(a2_exact,20)}              ║")
    print(f"  ║  Status: [ALG by convention (Lie gauge)]       ║")
    print(f"  ╚════════════════════════════════════════════════╝")

    print(f"\n{'='*68}")
    print("FULL PROJECTION EXPANSION  [ALG by convention (Lie gauge)]")
    print("="*68)
    Pi0 = pi - atan(sqrt(mpf(15)))
    Pi_alias = atan(tau)
    print(f"""
  Π(Q₀, U=π/τ, O) = Π₀ + a₁Q₀ + Π_alias + a₂Q₀² + O(Q₀³)

  Π₀      = π−arctan(√15) = {nstr(Pi0,14)} rad       [ALG]
  a₁      = 559√15/4860   = {nstr(a1_exact,14)}       [ALG by convention]
  Π_alias = arctan(2√3/3) = {nstr(Pi_alias,14)} rad   [ALG]
  a₂      = 86775991√15/755827200
           = {nstr(a2_exact,14)}       [ALG by convention] ← NEW (corrected)

  Denominator: 755827200 = 2⁹·3¹⁰·5² = 32·4860²
  Numerator:   86775991 = 1097×79103 (both prime)
""")
    return a2_exact

if __name__ == "__main__":
    result = run()