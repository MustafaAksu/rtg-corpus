# RER Phase B-04: author-conflict disclosure and reading note for RER-TRIAD-REGULAR-3FOLD

**Date:** 20 Oct 2026.
**From:** Claude, RER co-owner (preparer). The preparer does not accept his own work.
**Status:** NONCANONICAL Phase B input for independent receiving review. This is not a record disposition.
- No RER record, grade, contract table or OPEN status is changed.
- Nothing is adopted, frozen or published.

## 1. Author-conflict disclosure (correction to the Phase B routing)

Before preparing the next group, I checked who wrote the sources of each remaining record. The working assumption so far was that only two records — RER-TRIAD-FORMAL-INVOLUTION and RER-TRIAD-BIRTH-GRAPH-INVOLUTION — are mine. **That assumption is incomplete.** The source documents below are my own working files (they sit in my output workspace and are written in the first person, with "the co-owner" as the reviewing party):

| Record | My authored source | What is mine |
|---|---|---|
| RER-TRIAD-AGE-CURVATURE | `CURVNOTE` = `RER_C09_INDEPENDENT_VERIFICATION_20261009.md` §7 (`d3553fb4…3321`); `CURVSCRIPT` = `triad_age_fibre_curvature_check.py` (`e56088b0…17f2`) | The w₁₃ wedge formula, R₈, K₃ and its real zero — the record's central result |
| RER-TRIAD-FORMAL-AGE | the same note, §8 (the proposed formal age family); `FORMALSCRIPT` = `triad_formal_age_family_check.py` (`5bc3494d…98e1`); `SERIES2` = `c09_independent_series_check.py` (`67b2e0e7…99b`) | The original claim and checkers. The structural all-orders proof and the floor((d−3)/2) bound in the record come from the co-owner's receiving review (`FORMAL`, `b170dbff…3899`) |
| RER-F3-N7N8 | `TM2NOTE` = `TRIAD_F3_FINITE_JET_CONTROL_STAGE1_20261013.md`; the Stage-2 engine, contract, coverage and regression scripts; the note's §10–11 | The finite-jet defect calculation and the Stage-2 machinery |
| RER-GEN-K3-MODAL | `TRIAD_EC_PY` = `triad_k3_econjugacy_check.py`, `TRIAD_SB_PY` (Triadic R4 package) | The `[ALG]` E-conjugacy transport step. The two `[THM]`s are Genesis owner imports and are not mine |
| RER-RRF-CND01 | RER r3.1 text | The RER-native `[THM]` F σ = σ F ⇒ F(Fix σ) ⊆ Fix σ was written by the RER editor (me). It is elementary standard mathematics, but the receiver may still wish to treat it as an authored record |

**Prior involvement, not authorship:** the same note's §1–§6 is my independent receiving verification of RER-GEN-C09. My B-03 reading of C09 therefore follows an earlier check of mine; the receiver's own acceptance of C09 is unaffected, but the dependence should be visible.

**Consequence.** I should not prepare assessments for TRIAD-AGE-CURVATURE, TRIAD-FORMAL-AGE or F3-N7N8, nor for the E-conjugacy step of GEN-K3-MODAL. Proposed routing, for the receiver's decision:

| Record | Proposed route |
|---|---|
| TRIAD-FORMAL-INVOLUTION, TRIAD-BIRTH-GRAPH-INVOLUTION | receiver (unchanged) |
| TRIAD-AGE-CURVATURE, TRIAD-FORMAL-AGE, F3-N7N8 | **receiver** (new: author conflict) |
| GEN-K3-MODAL | receiver for the E-conjugacy step; the owner-import part was already assessed in Phase B-01 |
| RRF-CND01 | receiver's choice: either receiver review, or a preparer reading note with the conflict recorded |
| TRIAD-REGULAR-3FOLD | **preparer reading note below**: the theorem is from the co-owner's receiving review `AGEGEO` §D, not mine |
| DYAD-FORMAL-INVOLUTION | preparer reading possible (owner import; my part is only the r4.6 carrier-cell wording from RRF editor Q5) |

If useful, I can prepare a **neutral source inventory** for each conflicted record — file identities, byte status, cited line ranges, without any assessment. A reverse conflict may also exist: if the receiver is the author of `AGEGEO`, my note below is the independent review of that theorem.

## 2. RER-TRIAD-REGULAR-3FOLD — reading note

**Source:** `AGEGEO` §D (lines 59–80), `C09_AGE_GEOMETRY_RECEIVING_REVIEW.md` (`ae3af192…2b2b`, BYTE_VERIFIED_HERE). Also cited: `AGE` §3 (lines 40–53, `fe0da2b3…1392`, BYTE_VERIFIED_HERE). Both read in full. Source coverage: **complete**.

**Statement.** For fixed κ ≠ 0, no C¹ embedded three-dimensional submanifold of ℝ⁴ through the origin contains both age sheets M_{κ,0} and M_{κ,1} near the origin.

**Proof check (read and verified step by step):**

| Step | Content | Reading |
|---|---|---|
| 1 | Locally M = {H = 0} with H a C¹ submersion ℝ⁴ → ℝ | Standard for a C¹ embedded hypersurface |
| 2 | M_{κ,0} ⊂ M gives H(s, C_κ(s)) = 0; differentiating at 0 with DC_κ(0) = 0 (C_κ = O(\|s\|³)) gives D_sH(0) = 0; then a := D_cH(0) ≠ 0 because DH(0) ≠ 0 | Correct; the source says "tangent to the parent s-plane", which is this computation |
| 3 | Both sheets are graphs over a full parent neighbourhood including 0. M_{κ,1} = F(B_κ(U)) is a graph because g_κ = F_s∘B_κ has Dg_κ(0) = I | Correct (REACH, AGE §1) |
| 4 | 0 = H(tu, c₁(tu)) − H(tu, c₀(tu)) = ∫₀¹ D_cH(tu, c₀ + θ(c₁ − c₀)) dθ · (c₁ − c₀) | Mean-value theorem in integral form; needs only D_cH continuous, i.e. H ∈ C¹ |
| 5 | c₁ − c₀ = −(√3κ/6) t⁵ Q(u)² u + O(t⁶), and the integrated D_cH tends to a as t → 0 | The degree-5 difference is exact and was re-derived independently in Phase B-03 (b03c D2, b03d E3/N1). No uniformity in u is needed: u is fixed and t → 0 |
| 6 | Divide by t⁵: Q(u)² a·u = 0 for every u ≠ 0; Q > 0, so a·u = 0 for all u, hence a = 0, contradicting step 2 | Correct. The child difference points along u in every direction, so the drift sweeps all child-plane directions, as the record says |

**Grade `[THM]`, `EXACT_LOCAL`.** Supported. The proof is complete and elementary, given the exact degree-5 sheet difference. Regularity C¹ is all that is used. No radius is claimed or needed.

**Extension to fixed pairs n ≠ m (record's proof-scope clarification).** Correct as stated: replace step 5 by c_n − c_m = −(n−m)(√3κ/6)Q²s + O_{n,m}(6) (AGE §3; numerically confirmed in B-03 N2). Each pair has its own neighbourhood; the record explicitly declines a uniform all-age statement.

**Scope.** The record's boundaries match the source: the obstruction is about a *regular embedded* 3-fold *through the origin*. It says nothing about:
- singular or punctured-domain three-parameter descriptions — the formal age family C(s, τ) of RER-TRIAD-FORMAL-AGE is one, with ∂_τC(0, τ) = 0, so there is no conflict between the two records;
- abstract or non-injective reachable-state factors;
- 2-D factors (the record's contract type is `EMBEDDED_CONTAINMENT_TEST_NOT_FACTOR`).

**One wording observation (B04-O1).** The record's Constraints cell says "candidate is a C1 embedded three-manifold THROUGH the origin" and the closure cell says "near zero". The proof needs the containment only in some neighbourhood of 0. That is what "near zero" means here; no change suggested.

**Suggested disposition (for the receiver):** `SCOPE_CONSISTENT_WITH_AGEGEO; PROOF_CHECKED (preparer, step by step); SOURCE_COVERAGE_COMPLETE`.

## 3. Not in this note

- No assessment of the conflicted records listed in §1.
- No disposition is made.
- G2 §5b carrier identification stays pending; both ER-2B records stay blocked.
