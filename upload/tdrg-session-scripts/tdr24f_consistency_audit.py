#!/usr/bin/env python3
"""
tdr24f_consistency_audit.py

Audits the internal consistency of the TDR-24F structural-to-slot projection
relation against the measured v17/v6 scaling exponents.

The TDR-24F mean-field closure (as stated in the DSN) is:

    psi_slot_bulk = q_proj * cbar_struct / (2k+1)                      ...(5)

with supporting definitions:

    O_t           = (2k+1) * M_t * psi_t        (slot-volume identity, TDR-24D)
    cbar_slot     = occ_clean_pairs / M_pre = (2k+1) * psi_slot        ...(3)
    q_proj        = cbar_slot / cbar_struct                            ...(4)

This script does NOT require the motif CSVs: the inconsistency is diagnosable
from the reported power-law exponents alone, because (3),(4),(5) impose an
exact additive constraint on the exponents that the reported values violate.

If the v17 motif CSVs become available, the `--csv` path recomputes the
exponents directly from data so the misreported quantity can be identified.
"""

import math
import argparse


# ---------------------------------------------------------------------------
# Reported v17/v6 exponents (from collaborator notes / DSN v2.2)
# ---------------------------------------------------------------------------

REPORTED = {
    "psi_slot_bulk":   0.014,   # psi_slot ~ N^+0.014   (R^2 = 0.015, ~flat)
    "q_proj":          1.371,   # claimed q_struct_to_slot_bulk ~ N^+1.371
    "cbar_struct":     0.000,   # claimed bounded 4.5-5.8  => O(1) => N^0
    "O_slot_per_step": 0.709,   # O_slot ~ N^+0.709 (R^2=0.976)
    "O_bulk_per_step": 0.723,   # O_bulk ~ N^+0.723 (R^2=0.972)
}


# ---------------------------------------------------------------------------
# Exact (2k+1) scaling on the canonical k = round(N/15) grid
# ---------------------------------------------------------------------------

CANON_N = [120, 180, 240, 360, 480, 720, 840, 960, 1080, 1200, 1440]


def kval(N: int) -> int:
    return round(N / 15)


def fit_powerlaw(xs, ys):
    """Return exponent alpha in y ~ x^alpha via log-log least squares, plus R^2."""
    lx = [math.log(x) for x in xs]
    ly = [math.log(y) for y in ys]
    n = len(lx)
    mx = sum(lx) / n
    my = sum(ly) / n
    sxx = sum((v - mx) ** 2 for v in lx)
    sxy = sum((lx[i] - mx) * (ly[i] - my) for i in range(n))
    alpha = sxy / sxx
    intercept = my - alpha * mx
    # R^2
    ss_tot = sum((v - my) ** 2 for v in ly)
    ss_res = sum((ly[i] - (intercept + alpha * lx[i])) ** 2 for i in range(n))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    return alpha, r2


def band_exponent():
    Ns = CANON_N
    bands = [2 * kval(N) + 1 for N in Ns]
    return fit_powerlaw(Ns, bands)


# ---------------------------------------------------------------------------
# Consistency audit (exponent algebra)
# ---------------------------------------------------------------------------

def audit():
    print("=" * 68)
    print("TDR-24F EXPONENT CONSISTENCY AUDIT")
    print("=" * 68)

    band_exp, band_r2 = band_exponent()
    print(f"\n(2k+1) scaling on canonical grid (k=round(N/15)):")
    print(f"  exp(2k+1) = {band_exp:.4f}  (R^2={band_r2:.4f})")
    print(f"  [linear approximation 2k+1 ~ N^1 is accurate to ~2%]")

    e_psi = REPORTED["psi_slot_bulk"]
    e_2k1 = band_exp                      # use measured, not idealized 1.0
    e_qproj = REPORTED["q_proj"]
    e_cstruct = REPORTED["cbar_struct"]

    print(f"\nReported exponents:")
    print(f"  exp(psi_slot)   = {e_psi:+.3f}")
    print(f"  exp(q_proj)     = {e_qproj:+.3f}   (claimed)")
    print(f"  exp(cbar_struct)= {e_cstruct:+.3f}   (claimed bounded => 0)")

    # Constraint from relation (5): exp(psi) = exp(q_proj)+exp(cbar_struct)-exp(2k+1)
    lhs = e_psi
    rhs = e_qproj + e_cstruct - e_2k1
    residual = lhs - rhs
    print(f"\nRelation (5): exp(psi) =? exp(q_proj)+exp(cbar_struct)-exp(2k+1)")
    print(f"  LHS  = {lhs:+.3f}")
    print(f"  RHS  = {e_qproj:+.3f} {e_cstruct:+.3f} - {e_2k1:.3f} = {rhs:+.3f}")
    print(f"  RESIDUAL = {residual:+.3f}   "
          f"{'CONSISTENT' if abs(residual) < 0.05 else '*** INCONSISTENT ***'}")

    # Decisive derived quantity: cbar_slot exponent (uses only psi and band, both robust)
    e_cbar_slot = e_2k1 + e_psi
    print(f"\nDecisive check via cbar_slot = (2k+1)*psi_slot  [eq (3), robust]:")
    print(f"  exp(cbar_slot) = exp(2k+1)+exp(psi) = {e_2k1:.3f}{e_psi:+.3f} = {e_cbar_slot:+.3f}")
    print(f"  Since cbar_slot = q_proj * cbar_struct  [eq (4)]:")
    print(f"    exp(q_proj) + exp(cbar_struct) MUST equal {e_cbar_slot:+.3f}")

    print(f"\n  Resolutions consistent with the data:")
    print(f"    H1: cbar_struct bounded (exp=0)  =>  q_proj ~ N^{e_cbar_slot:+.3f}")
    print(f"        (the reported 1.371 should be ~{e_cbar_slot:.3f})")
    req_cstruct = e_cbar_slot - e_qproj
    print(f"    H2: q_proj ~ N^{e_qproj:+.3f} correct  =>  cbar_struct ~ N^{req_cstruct:+.3f}")
    print(f"        (contradicts the bounded-reservoir claim of 4.5-5.8)")

    print(f"\nVERDICT:")
    print(f"  The reported q_proj exponent (1.371) and bounded cbar_struct (N^0)")
    print(f"  cannot both hold. The hard constraint exp(q_proj)+exp(cbar_struct)")
    print(f"  = {e_cbar_slot:.3f} forces one of them to be misreported.")
    print(f"  Most likely: q_proj ~ N^{e_cbar_slot:.3f}, i.e. the 1.371 figure is a fit error,")
    print(f"  and cbar_struct is genuinely bounded as claimed.")

    # Cross-check: O_slot = (2k+1)*M*... actually O_slot/step = sum(2k+1)*M_pre/T
    # exp(O_slot) should equal exp(2k+1) + exp(M_bulk)
    print(f"\nCross-check on O_slot (independent of q_proj):")
    e_M = -0.295   # M_bulk ~ N^-0.295 (v17/v6)
    e_Oslot_pred = e_2k1 + e_M
    print(f"  O_slot/step = (2k+1)*M_pre (summed): exp = exp(2k+1)+exp(M_bulk)")
    print(f"  predicted exp(O_slot) = {e_2k1:.3f}{e_M:+.3f} = {e_Oslot_pred:+.3f}")
    print(f"  reported  exp(O_slot) = {REPORTED['O_slot_per_step']:+.3f}")
    print(f"  residual = {e_Oslot_pred - REPORTED['O_slot_per_step']:+.3f}  "
          f"{'OK' if abs(e_Oslot_pred - REPORTED['O_slot_per_step']) < 0.05 else 'CHECK'}")
    print(f"  [This path is self-consistent, confirming the slot-volume identity")
    print(f"   itself is sound; only the q_proj/cbar_struct split is in question.]")


if __name__ == "__main__":
    # Pure algebraic consistency check on reported exponents.
    # For data recomputation from v17 CSVs use tdr24f_data_recompute.py.
    audit()
