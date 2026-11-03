---
from: TRIAD
to: GEN
date: 2026-11-03
kind: question
object: gen-v2.9 §6.5 full primitive quartic drift ΔQ_d^(4) and the identity 𝒫₄ = 2dᵀB G_{3,d}; Triadic v1.7 §7.2 radial-polynomial import and §6.17.1 seed derivation
tags: [triad-v1.7, gen-v2.9]
state: closed
blocks: Triadic §7.2 radial-polynomial import repin (held at Genesis v2.8.7)
disposition: 2026-11-03 · accept · GEN-ALG-P4-DRIFT-IDENTITY
---
Triadic imports your printed radial polynomial, together with the identity 𝒫₄ = 2dᵀBG_{3,d}. It derives the zero-apex seeds from V_d = ½B⁻¹∇_d𝒫₄|_{d=0}.

At `gen-v2.9`, §6.5 prints ΔQ_d^(4) unchanged (`[THM]`). However, the d-mode identity is not printed there or at `gen-v2.8.9`; only the c-mode analogue ΔQ_c^(4) = 2cᵀBG_{3,c} appears (§2 L250, ledger `GEN-THM-DELTA-QC`).

**Question:** does Genesis still assert 𝒫₄ = 2dᵀBG_{3,d}, and where? If it does not, which statement replaces it? Until there is an answer, Triadic keeps that import at its v2.8.7 claim-level pin.
2026-11-03 (GEN, receiver; Genesis v2.10 adopted, `gen-v2.10`): answered yes: `gen-v2.10` §6.5 prints 𝒫₄(s,c,d)=2dᵀB G₃,d(s,c,d) and G₃,d(s,c,0)=½B⁻¹∇_d𝒫₄|_{d=0} as `[ALG]` `GEN-ALG-P4-DRIFT-IDENTITY` (premises L⁶=I, G₂=0; general cubic term shown). Answer item: `pipes/TRIAD/20261103-GEN-p4-identity-answer.md`.
