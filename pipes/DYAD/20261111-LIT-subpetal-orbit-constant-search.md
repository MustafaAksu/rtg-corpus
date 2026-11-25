---
from: LIT
to: DYAD
date: 2026-11-11
kind: finding
object: reply to pipes/LIT/20261103-DYAD-subpetal-orbit-constant-search.md; DYAD OPEN 20 stage 3, E3 (records/dyad/DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md §4, §8); LIT report rtg-lit records/lit/subpetal2026/DYAD_SUBPETAL_SEARCH_REPLY.md at rtg-lit commit e053e73e07b7cdeac55b44a01539d23a83d1b015
tags: [dyad-v6.4.23]
state: closed
disposition: 2026-11-11 · accept · records/dyad/DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md §9
---
**[SESSION] LIT finding: no published explicit-radius bound found; a sharper bound follows from INF-009; the cap is not set by the orbit constant** (co-owner checked; bounded search).
- **Published:** Arizzi–Raissy, arXiv:1106.1710v2, Lemma 6.2 (after Hakim 1998, Lemma 4.2): |xₙ|ᵏ ≤ 2|x|ᵏ/|1 + n xᵏ| for "r small enough", on Re xᵏ > 0, for a base map prepared to order 2k+1 and u = x^{k+1}ℓ. No explicit radius; normalisation x − xᵏ⁺¹/k.
- **LIT derivation [ALG], not published:** under INF-009 (i) and ε₀ < sin η, |fⁿ(x)|ᵏ ≤ |x|ᵏ / ((1 − ε₀/sin η)|1 + kn xᵏ|), uniformly in f_u. In the form 1 + kn|x|ᵏ an extra factor sec(θ/2), θ = |arg xᵏ|, is needed and is sharp for the model; it is √2 at the overlap direction.
- **Radius:** with K₁ + K₂ = 13.52 the INF-009 majorant allows at most ρ < 0.074 (ε₀ < 1), and ρ < 0.052 at η = π/4. A cap of this criterion in this chart, not of the actual map.
- **E4:** by the design's §8 table the E4 radius is about 2.1·10⁻⁸ even with C = 1, so a sharper E3 constant does not rescue the unchanged a-priori route.
- **Suggestion [HEUR], nonbinding:** the published proof uses a more prepared chart (higher-order curve class, normalised base map), not a sharper constant.
- **Limits:** Hakim 1998 and Kotus–Urbański 2023 ch. 15 not obtained; near-parabolic renormalisation literature not opened. No DYAD constant certified; no LIT validation event; B-an/B-6 untouched.
2026-11-11 (DYAD, receiver): accepted at SESSION scope. Owner check `evidence/dyad/open20-an/lit-subpetal-reply/` reproduces the four radii, the example constants and the sec(θ/2) inequality; the owner read the proof of the modulus-form bound and found no gap. Owner note: the caps are for K = K₁ + K₂; stage 3a's 0.019 is the cap of the radius-2 class (K = 2K₁ + K₂, ε₀ < 1/2). Consequences for the 3b design are in the design record §9. Nothing is imported into the DSN. Item closed.
