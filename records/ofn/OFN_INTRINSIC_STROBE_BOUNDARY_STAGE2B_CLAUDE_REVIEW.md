# Review — Intrinsic strobe-boundary structure, Stage 2B (PR #413)

**Date:** 26 November 2026.
**Reviewer:** Claude (SESSION, independent review requested in the record's §7).
**Object:** PR #413 at head `37e4f006b22b98582394903cd9183b3f02c3b70b`. Record: `records/ofn/OFN_INTRINSIC_STROBE_BOUNDARY_STAGE2B.md`. The PR also updates the ChatGPT lane of `OFN_COOWNER_ENTRY_NOTE.md`.
**Status:** SESSION / NONCANONICAL. A review is not adoption.

## 1. Evidence

- **Hashes.** The PR head was fetched read-only. The script (`a64602fc…`) and the output (`b2bf2247…`) match the record's table, `SHA256SUMS.txt` and the `upload/` copies.
- **Script inspection.** The script imports only `math` and SymPy. It makes no file, process or network calls.
- **Native replay.** Run on Linux with Python 3 and SymPy 1.14.0. Exit code 0. The output is byte-identical to the stored run.
- **Independent check.** Written in mpmath at 50 digits, without importing the PR script. It iterates the raw map G_σ = e^ρ − 1 + εσρ^q, S = sin η, with full Taylor jets to degree q, for p = 12, 16, 20 and 24. The last value is outside the PR's high-jet range. Results:
  - The pure V^k coefficients for 2 ≤ k < q agree exactly for σ = ± and for ε = 0.
  - The ε = 0 cubic equals the owner closed form.
  - The degree-q contrast equals 2sεκ_{p,q} to within 10⁻⁵².

## 2. Proof checks (by hand)

**§2: correct.** Φ̄_p(1) = 1 when p is not a power of 2. Since φ(p) < p/2 = n, the polynomials 0 and Φ̄_p give the required witness pair.

**§3: correct.**
- The one-step cubic is (L−1)bρ³/L − γη³. At W = 0, and using K_p = −(L−1)²/L, the alternating part gives χ = (L−1)L²(1+L)⁻³(β + δK_p/L).
- J_s = Σ L^{(2s−4)j} = (1 − (−1)^s)/(1 + L⁻⁴).
- K_p/L = (2 − 2cos θ)·L⁻¹ is nonreal, so (β, δ) ↦ χ is bijective onto ℂ.
- The conic parametrization satisfies a² + r_p d² = 1/4.
- The compensator formulas solve J_s χ = −4Q₀c_p ad with real β and δ.

**§4: correct.**
- The alternating homological multiplier is L^{u−v} + L. It vanishes iff u − v − 1 ≡ 2s (mod 4s).
- The minimal degree is reached at u = 0, v = 2s − 1.
- At even degree the charge is odd while p/2 is even, so even degrees are never resonant.

**§5: correct, including both linear branches.**
- Drift: (−1)^j L^{−(q+1)j} = (−1)^j L^{−2sj} = 1, so the alternating source accumulates in phase. κ_{p,q} is verified.
- Linear typing: R² is a nonreal rotation, so S ∈ {±R} and A₋ = ±Id.
- Case S = R: by induction, the odd chart parts below degree q vanish, and the resonant V^q multiplier forces a contradiction.
- Case S = −R: the recharting w′ = σw produces a reflection-symmetric target pair. Its alternating terms occur only in even degree and can be eliminated at every even degree by reflection-preserving charts. Odd degrees stay common under this symmetry. This reduces the case to S = R.

This answers the concern that the linear σ-twist used in Stage 2A §6 might defeat the obstruction: it does not.

## 3. Remarks (no change to the results)

- **N1 (framing).** The threshold is the standard resonance condition for a period-two nonautonomous (Floquet-type) map. The alternating sign acts as the order-two character L^{p/2}. A single sentence saying so would place the result in known theory, consistent with the record's no-novelty statement.
- **N2 (joint reading with #411).** The new coupling lives at degree q ≥ 5, so it is invisible by construction to the owner cubic and to the DZT norm. With #411 §§5–6 this shows that the DZT cubic norm cannot certify recognition coupling in either direction. The decouplable sign gate changes the coefficient but not the norm. The irreducible degree-q coupling changes neither.
- **N3 (dependency).** The record cites #411 at a pinned commit, and #411 is unmerged. Merge #411 first or together. The ChatGPT-lane note edit is confined to its own lane.

## 4. Verdict

The mathematics is correct, including both branches of the product-conjugacy obstruction, and was replicated independently beyond the PR's high-jet range. The record honestly states that the term σρ^{2s−1} is chosen, not derived, and that the chart class is limited to parity-only charts. **Approve.** N1 and N2 are optional additions.
