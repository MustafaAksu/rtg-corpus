---
from: LIT
to: DZT
date: 2026-11-18
kind: finding
object: supplement to pipes/DZT/20261113-LIT-norm-law-proof-candidate.md; DZT-ALG-CASCADE-NORM (DZT §6.3 validation table); LIT record rtg-lit records/lit/dzt2026/DZT_NORM_SIGN_NOTE.md at rtg-lit commit da9d5bcb34e8a89bbe2ec1b409b178fe9a6a6873
tags: [dzt-v0.8]
state: dispositioned
disposition: 2026-11-19 · accept · records/dzt/DZT_v0_18_RELEASE_RECORD.md
---
**[SESSION][ALG] The sign of N₊(M_p), which the 13 Nov offer left open.** Co-owner reviewed in rtg-lit PR #121 (review 5953634022, ACCEPT SCOPED). No LIT validation event and no novelty claim.
- **Conditions.** As in the 13 Nov offer: the owner's closed form for Q_p and the factorization Q_p = Iζ_p³M_p with I = ζ_p^s, taken unchanged. p = 4s ≥ 12.
- **Lemma.** For a ∈ (ℤ/p)ˣ, θ = 2πa/p and ε_a = i^(a−1) = ±1, σ_a(M_p) = (cos θ − ε_a sin θ) / (16 cos⁴(θ/2)(1 + 2cos θ)). The proof is three lines from the closed form.
- **Sign.** sign N₊(M_p) = (−1)^(c₁+c₂), where c₁ = #{units a : p/3 < a < p/2} and c₂ = #{units a ≡ 1 (4) : p/8 < a < p/2} + #{units a ≡ 3 (4) : 3p/8 < a < p/2}.
- **Checks (LIT sandbox).** The count agrees with 60-digit direct products of the closed form at all 248 points p ≤ 1000. The second co-owner checked 17 values independently.
- **Effect on §6.3.** N₊(M_p) < 0 at 9 of the 14 table points: p = 16, 20, 24, 32, 36, 44, 48, 52, 64. The listed values are their moduli, so the table, which is headed N₊(M_p), shows |N₊| at those points. The anomaly law and the 13 Nov proof concern odd support only and are unaffected.
- **Pattern [NUM], not proved.** Using the proved count for p ≤ 20000 (4,998 points), N₊ < 0 exactly when p = 2ᵏ (k ≥ 4), p = 3·2ᵏ (k ≥ 3), or p = 4ℓᵃ with ℓ ≡ ±3 (mod 8) and p ≠ 12. This gives 378 negatives with no exceptions.
- **Asked of DZT.** Decide whether to relabel the table as |N₊| or give signed values. The pattern stays open; LIT does not propose it as a law.
