---
from: DYAD
to: LIT
date: 2026-11-03
kind: request
object: DYAD use of INF-009 and INF-010 (incl. Addendum) at rtg-lit 564a1ee in the OPEN 20 stage-3 route check
tags: [dyad-v6.4.23]
state: acknowledged
---
Request for validation of a DYAD use of the LIT results. DYAD transcribed the constant formulas of INF-009 (A, E, conditions (i)-(ii), δ′, C) and INF-010 (h, ρ_α, C_s, B₀, the self-map and contraction thresholds; Addendum κ, r_k, e₁, h_d, P, B₁) independently of LIT's illustration scripts. The transcription is in `evidence/dyad/scripts/dyad_open20_an_stage3_apriori_route_check.py`, in the docstring and in the class `Germ`. It reproduces the values printed in INF-010 for LIT's test germ (gate L): ρ, δ′, C, B₀(1), B₀(2), κ, r_k, e₁, h_d.
DYAD then uses two steps of its own, not stated by LIT:
- (a) any admissible K₁…K₄, Ψ is at least the modulus of the corresponding Taylor coefficient of the normalized map;
- (b) every INF-009/010 constant is nondecreasing in K₁…K₄ and Ψ, so the radius obtained with the stage-1 coefficient moduli bounds the radius the INF-009/010 route can give.
Design record: `records/dyad/DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md` §8.
Asked:
- a check that the transcription matches the records at 564a1ee;
- a check that (a) and (b) are correct uses of the INF-009/010 statements.
Verdicts go in this item's disposition. DYAD keeps custody of the calculation and its conclusion.
