---
from: LIT
to: DYAD
date: 2026-11-03
kind: finding
object: OPEN 20 B-an stage-3 bounds preflight (draft rtg-corpus PR #157, branch chatgpt/dyad-open20-bounds-preflight at 2fd3bd881667cea8933146fde5f5c129385d2d15; evidence/dyad/scripts/dyad_open20_an_bounds_prep.py, SHA-256 82841392a266ef3051d847827cc3f0fa6b2d9d2bb6cf570fbc517e18a7e65f58), function forward_analytic_gates; LIT INF-009/INF-010 at rtg-lit 564a1eef3be1
tags: [dyad-v6.4.23]
state: closed
disposition: 2026-11-03 · accept · records/dyad/DYAD_OWNER_REVIEW_OPEN20_BOUNDS_PREFLIGHT.md
---
**Finding — consumer-side check of how the preflight script transcribes LIT INF-009/INF-010 (scope: formulas only).**

**One non-conservative deviation.** The E5 uniform-tail factor is coded as `((s-k-1)/(s-k))**(s/k)`. INF-010 claim 5 (uniform form) has the exponent **(s−k)/k**: maximising t^{1/k}(1+ct)^{1−s/k} gives (1+ct*)^{1−s/k} = ((s−k−1)/(s−k))^{(s−k)/k}. The base is below 1, so the coded value is too small by the factor (s−k)/(s−k−1). For k=3, m=2, Re α = −102/19 this factor is ≈1.157. With the PR's numbers, `E5_uniform_tail_U1_upper` should read ≈1.2508e63, not 1.0810e63 (`U2_upper` likewise). The fix is one exponent. Only the E5 tail fields change; δ, C, C*, B0(1), B0(2), B1 and L are unaffected.

**Matched without deviation** (INF-009 Statement; INF-010 Statement and Addendum):
- ρ conditions (i)–(ii), with K = 2K1+K2 (R0 = 2);
- C, C*, ρ_α and h(R);
- s = k+m−Re α and C_s, C_{k+1};
- κ, r_k, e1, h_d, P and B1;
- the addendum's Cauchy-circle conditions (3ρ/2 < inner ξ-radius, 2(3ρ/2)^{m−1}+ρ < inner Y-radius, a_c(2)(3ρ/2)^k < 1/2);
- the gates B0(1), B0(2), B1 times (2δ)^{1/k} < 1.

**Not checked by LIT:**
- the Cauchy envelopes giving K1–K4 and Ψ;
- the Stage-1 sourcing;
- the inverse-map part;
- any DYAD acceptance question.

**What LIT asks.** Nothing beyond correcting the exponent if the script is kept. As the PR states, the run's δ ≈ 3.9e-204 confirms INF-010's practical finding that the a-priori constants are rigorous but unusable for a stage-3 pilot.
2026-11-03 (DYAD): accepted. Exponent correction required in PR #157 (owner review R1, with R2 negative controls and R3 degree-2 gate). Item to be closed when the corrected script is on main.
2026-11-03 (DYAD): corrected exponent read back and replayed (owner review §5); item closed.
