# FMS — Explicit Invariant of the Quintic ψ-Modulus: the Relative-Phase Harmonic v0.1

**Date:** 19 October 2026 · **Status:** `[SESSION]`, noncanonical. Not owner-adopted; no DSN is modified.
**Answers:** FMS v0.6.3 request to write the modulus as an explicit algebraic invariant (ALG target), kept separate from the physical-readout question (OPEN).
**Builds on:**
- `FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py` (`550adcb8…e7eb`);
- `FMS_PSI_QUINTIC_KAPPA_ALL_v0_1.py` (`2849e32f…013e`);
- `FMS_PSI_QUINTIC_MODULUS_SESSION_NOTE_v0_1_1.md`.

## 1. Count `[SESSION — ALG, exact]`

Let V be the space of S₃- and λ-equivariant quintic perturbations of the reduced map. V has real dimension 12.

Its intersection with the image of the full first-order conjugacy operator A has dimension 4. The A columns are Φ₃ (equivariant and non-equivariant) together with Φ₁ in Lie Stab(f₃). So the **S₃ class carries 8 first-order quintic moduli**.

The transported chart line δ₅(a) moves along **one** of these 8 directions. This is consistent with rank 31/32. A single "cokernel functional" is therefore not canonical. What is canonical is a functional that reads the chart direction and vanishes on every gauge direction. §2 gives such a functional explicitly.

## 2. The invariant `[SESSION — ALG, exact checks]`

**Definition.**
- Chiral coordinates: u = w₁ + λw₂ and v = w₁ + λ̄w₂, with intensities A = |u|² and B = |v|².
- Six-step return: F₆ = f⁶.
- c(κ, a) is the coefficient of **u³v̄³** in the degree-6 part of A∘F₆ − A.

**Closed form,** with t = (1 − κ)/κ:

  **c(κ, a) = −1/486 + 7t/648 + i·[ 17√3/2916 + 2√3·t/81 − (2/9)·Im(a μ̄) ]**

**Verified properties.**

| Property | Status |
|---|---|
| (B) Every first-order gauge direction (basis of V ∩ Im A) leaves the u³v̄³ coefficient unchanged. Gauge directions do move the A²B and AB² intensity coefficients. | PASS |
| (C) c is unchanged, exactly, under finite random S₃-symmetric cubic conjugacies at five values of t. | PASS. Exact checks, not a proof |
| (D) The closed form holds exactly at t ∈ {0, 1, −2/3, −1/2, 3/7} and for six values of a, including large finite a (3i, 2 + 5i, 4√3 − 11i). | PASS |
| a ∈ ℝμ ⇒ Im(aμ̄) = 0 ⇒ c unchanged. Consistent with N_a = N. | PASS |

**Consequences.**
- **Re c** does not depend on a. It reads κ only.
- **Im c** reads the modulus Im(aμ̄) and κ together. Its dependence on a is **exactly affine for finite a**, not only at first order.
- Within the scope of (B) and (C), two transported models with different Im(aμ̄) at the same κ therefore have different invariants.
- This partially answers FMS's open finite-a item. It is a proof only for conjugacies covered by (B), i.e. first order. For finite conjugacies it is exact-check evidence, (C), not a theorem.

**Distinguished chart.** At Im(a*μ̄) = 17√3/648 + √3·t/9 we get Im c = 0. This is a mathematical observation. It is **not** a physical selection.

## 3. Readout form `[SESSION — ALG]`; physical status `[OPEN — OFN/RRF]`

Write θ = arg u − arg v for the relative chiral phase. By S₃ symmetry the u³v̄³ coefficient of ΔB is c̄. To sixth order:

- Δ(A + B) ⊃ 4·Re c·(AB)^{3/2}·cos 3θ
- **Δ(A − B) ⊃ −4·Im c·(AB)^{3/2}·sin 3θ**

The ψ-modulus therefore appears as the **sin 3θ harmonic of the chirality-imbalance transfer** in one six-step return. This is the first relative-phase-dependent term in the shape law; the cubic law of Ledger §10A has no phase dependence. The intensity coefficients A²B and AB² at the same order are **not** gauge-invariant, as (B) shows, so FMS's caveat is confirmed for them. The phase harmonic is the gauge-invariant part.

## 4. Limits

- **Conjugacy classes.** The result covers the S₃-equivariant class, first-order generators (all of Im A) and finite S₃ cubic conjugacies (by exact checks). Not covered: finite Φ₅ or non-S₃ finite conjugacies, discrete stabilizer components, and κ ∈ {0, 2}. At κ = 2 the odd category, t = −1/2, is included in (D).
- **Coordinates.** θ, A and B are coordinate expressions. The **coefficient** c is the invariant object. A physical observable must be stated in a declared carrier and encoding, under the RRF contract.
- **Realization.** J and its existence are DYAD OPEN 20. Physical ψ-selection belongs to OFN/RRF.

## 5. Evidence

| File | SHA-256 | Result |
|---|---|---|
| `FMS_PSI_QUINTIC_PHASE_INVARIANT_v0_1.py` | `1c4ab0d0d4e255d474f87b804451f6d92d128471f6268898513d6cd3fe17212f` | 40 checks PASS, ALL PASS, ~45 s. Needs the two scripts above in the same directory |
