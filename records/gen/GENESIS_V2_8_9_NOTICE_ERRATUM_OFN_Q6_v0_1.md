# Genesis v2.8.9 — Erratum to the OFN notice (Q6 grade) v0.1

**Date:** 19 October 2026 · **Status:** `[SESSION]` erratum to the release record's outbound OFN notice. The adopted Genesis v2.8.9 (`d143673e…c6fc`) is **unchanged**; only the wording of the notice is corrected.

## 1. Corrected sentence

The release record (`GENESIS_V2_8_9_RELEASE_RECORD.md`, `f6df5d11…4181`), §4 → OFN, reads:

> "The narrow Q6 planar-decoupling forms of OFN v0.7.2 §3.1 are covered at the primitive clock **only at the `[ALG]` grade**, and only if passive transformations are local C³ conjugacies."

This is **too conservative and is withdrawn.** Corrected wording:

> For the narrow Q6 forms (a local C³ conjugacy to G₁ × G₂ × G₃ with planar Gᵢ, or a neutral planar factor), each neutral factor Gᵢ has spec DGᵢ(0) = {λ, λ̄}. Hence spec D(Gᵢ⁶)(0) = {1}, and (H_spec) holds for the induced six-step factor Eᵢ∘F⁶ = Gᵢ⁶∘Eᵢ, because (1−κ)⁶ ≠ 1 for κ ∉ {0, 2}. The six-step `[THM]` `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` (and, for the raw family, `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO`) then excludes these forms. The narrow forms are therefore covered by a **THM-derived argument** at local C³. The `[ALG]` primitive companion is needed only for **general** primitive targets under (H_prim). Those are the targets whose spectrum is not on the unit circle, for which (H_prim) does not imply (H_spec).

The withdrawn sentence wrongly attached the grade of the general primitive statement to the narrow contract.

## 2. Consistency with OFN v0.8 (read 19 Oct)

- **§3.4 narrow-Q6 corollary.** OFN v0.8 already routes the argument through the six-step theorem with (H_spec) for Gᵢ⁶. The step is correct and agrees with §1 above. OFN's own grading of it (OFN SESSION corollary of an owner theorem) is appropriate.
  - **Minor wording:** "(1 − κ)λ is neither real nor on the unit circle for κ ∉ {0, 2}" fails at κ = 1, where (1 − κ)λ = 0.
  - The conclusion still holds at κ = 1: λ and λ̄ must pair in real 2×2 blocks, so two neutral factors remain.
  - κ = 1 also lies outside the class-C formal range.
- **§3.1 (raw family).** The heading `[THM — imported]` is supported, provided the argument is routed through `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` / `GEN-THM-K3-SIXSTEP-FACTOR-NOGO` exactly as in §3.4. The body currently cites "the primitive-clock form of 6S-κ", which in Genesis is the `[ALG]` statement of §6.3b.
  - **Suggestion for OFN v0.10:** cite the six-step route.
  - This is wording only; the conclusion is unchanged.
- **Elsewhere:** the six-step `[THM]` and the primitive `[ALG]` are kept distinct, and the guards G-JET, G-SEL and G-OFN are cited correctly. No other discrepancy was found in OFN v0.8's use of Genesis v2.8.9.

## 3. Unchanged

- The adopted text of §6.3c.
- The other notices (RRF, FMS, Dyadic).
- Q6-REG as an OFN decision. OFN v0.8 now fixes it at local C³ (SESSION, pending v0.10).
- Physical selection of model C, and OPEN 20.
