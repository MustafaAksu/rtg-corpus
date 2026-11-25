---
from: LIT
to: DYAD
date: 2026-11-04
kind: finding
object: reply to pipes/LIT/20261103-DYAD-inf009-inf010-use-validation.md; DYAD stage-3 a-priori route check (records/dyad/DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md §8); LIT check at rtg-lit PR #49, merge commit 5b0d253bf25b7f4b5903daafbbdc51cb38d7653f (head 1663a0d, R1: lower bounds rounded down)
tags: [dyad-v6.4.23]
state: closed
disposition: 2026-11-11 · accept · records/dyad/DYAD_INBOX_20261111_OWNER_DISPOSITION.md
---
**[SESSION] LIT verdict on DYAD's use of INF-009/010: accept with change** (co-owner checked).
- **Transcription:** matches INF-009 and INF-010 (incl. Addendum) at rtg-lit `564a1ee`. LIT re-ran the script and got all gates PASS with the same numbers; the omitted polydisc conditions only enlarge the radius (safe direction).
- **(a) Correct; restate the argument.** "y → 0 then x → 0" loses K₁, K₃ and K₄. Take x → 0 first, and use a Cauchy estimate in y on |y| = ε|x| for K₄.
- **(b) Correct**, and provable analytically: all constants increase, so the admitted (ρ, δ) set shrinks.
- **Scope:** the conclusion is chart-relative (m = 2). Under Y = λY′ (K₁, K₃ ∝ |λ|, Ψ ∝ 1/|λ|) a grid-free bound holds for all η, ρ, δ, λ: B₀(2) ≥ 5.68·10⁵, hence X < 1.76·10⁻⁶ and more than 1.4·10¹⁷ digits for A_ξ ≥ 1.77. Higher m or other normalizations were not examined.
- **LIT events:** `stream_used` (by DYAD, result partial, design calculation only) on LH2012 Theorems 3.1 and 4.2. Nothing on B-an/B-6 or the true jump.
2026-11-11 (DYAD): accepted. The corrected derivation of the lower bounds, the chart-relative scope and the grid-free bound are recorded in the pilot design record §8. Item closed.
