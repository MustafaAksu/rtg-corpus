# RTG Number Genesis v1.4 Import Audit v1

**Date:** 2026-08-28
**Auditor:** Claude (RTG mathematical auditor / DSN editor)
**Object:** `RTG_NUMBER_GENESIS_DSN_v1_4.md` (external-reviewer candidate canonical, incorporating an unseen v1.3)
**Baseline:** `RTG_NUMBER_GENESIS_DSN_v1_2.md` + `RTG_NG_PROGRAMME_REVIEW_AUDIT_v1.md` (D1–D13)
**Deliverables:** this report; `NG_NG8AB_INDEPENDENT_RECERT_v1.md` + script + log; patched candidate `RTG_NUMBER_GENESIS_DSN_v1_4_1.md`

---

## §1. Verdict

**ACCEPT v1.4 as scientifically sound; RECOMMEND ADOPTING the v1.4.1 audit-hygiene patch as the canonical file.** Every check of substance passes: no certified content was lost or mutated, guards SG-NG-1–18 are byte-identical, the v1.3 synchronization layer implements the programme-review checklist faithfully, the v1.4 conceptual layer (C_NG, NG-0R, SG-NG-22, classification-first N-5/N-6, functorial NG-8) matches the agreed corrections without overclaim, and the NG-8A/NG-8B closures are mathematically valid. Six findings — all certificate-hygiene or bookkeeping grade, none touching scientific state — are fixed in the v1.4.1 patch. Adoption of v1.4.1 over raw v1.4 is decision **D14**.

## §2. Integrity verification (v1.2 → v1.4)

| Check | Result |
|---|---|
| All 43 v1.2 `[RESULT]` lines preserved | PASS — 41 verbatim-anchored; 2 apparent misses are rewordings with content intact (N-3 layer summary now includes N-3C+; N-2 infinite-cyclic block present verbatim at v1.4 line 949) |
| Guards SG-NG-1 … SG-NG-18 unchanged | PASS — byte-identical |
| Key certified anchors (`N-1B-MIN`, `N-1A2`, wrapped-S¹ `[FAIL]`, `q_*` witness digits, `37/40`, `47/54`, `β` boundary cases, `χ_p(a,b)=a−b−1`, Bessel-residue guard, `Q_d*≈1.13e-2`) | PASS — all present |
| v1.3 checklist execution (numbering glitch; stale §8 item 5 CLOSED-by-import from `DYAD-THM-Q403-PHASELAW`; pointer refresh to OFN v0.7 / Dyadic v6.4.9 §6.1 / Discrete v2.12.13 / Genesis v2.8.4 §6.6 / Programme Overview v1.1; SG-PROG-2/OPEN-P0 ceiling; N-2-ORD, N-5A, SG-NG-19/20, NG-7A/7B split, NG-8A/B registration; N-1B-GROWTH re-route; DZT-not-substituted provenance note) | PASS — item-for-item, including the honest `[PROVENANCE]` handling of the absent DZT v0.17 owner file |
| Reviewer's earlier ℤ→ℚ roadmap overclaim imported? | NO — no checkmark graphic present |
| Governance discipline (three-programme split not silently registered) | PASS — explicit "Routing-label guard": Arithmetic-Dynamics is a routing label only; Programme Overview registration correctly left to PI (D1 remains open) |
| NG-0R content vs agreed corrections | PASS — quotient/difference declared a non-test; `U(1)→(ℝ,+)` obstruction recorded; three additive mechanisms separated; typed identity/inverse; arrow-before-label; non-blocking guard |
| Overclaim scan of v1.4 layer | PASS — "no universal ratio-priority claim" stated three times; N-5A and SG-NG-19/20 retained under the classification-first reframe |

## §3. Mathematical audit of the two new closures

**NG-8A valid.** Injectivity of `k ↦ T^k x` from certified N-1 non-collision; surjectivity by construction; `|S_m^+| = m` including `m = 0`. The off-by-one guard is a genuine and correct catch: the position-set convention counts `m` positions but `m−1` transitions, and equals `S_{m−1}^+ ∪ {x}` exactly.
**NG-8B valid.** `⟨T^m⟩` freeness via the length homomorphism plus integer cancellation; `(T^m)^k = T^{mk}` holds as literal identity of the ordered history under regrouping, verified at the word level; single-alphabet checks confirm the SG-NG-20 guard that no second generator appears, including for mixed pairs `(T^m, T^n)`.
**Independent re-certification executed:** 15 assertion families, all PASS, exit 0 (see companion certificate). Both closures stand.

## §4. Findings and their v1.4.1 fixes

**F1 (required) — certificates outside the corpus.** `NG_NG8A_ORBIT_CARDINAL_CERT_v1.md` / `NG_NG8B_REBLOCK_MULT_CERT_v1.md` are registered but exist only in the reviewer's sandbox; a CLOSED status may not rest on artifacts we do not hold. *Fix:* registry rows annotated; independent in-corpus re-certification registered; CLOSED now rests on in-corpus artifacts. External files should still be relayed and cross-checked (discrepancies would be ledgered).
**F2 (recommended) — "physically equinumerous" lacked a declared counting predicate.** SG-NG-11 warns counting equivalence may be coarser than strict; NG-8A needs the one-line predicate making set-distinctness = physical distinguishability explicit. *Fix:* `[DEF]` state-counting predicate added (identity of gauge-reduced present state; distinct tube states differ in `Q_true` and/or relational phase).
**F3 (recommended) — guard numbering gap.** v1.4 jumps SG-NG-20 → SG-NG-22 with 21 unassigned while D10 (substrate-arity ≠ derived-cardinal) is pending. *Fix:* SG-NG-21 explicitly reserved for D10.
**F4 (housekeeping) — stale §5 row.** "signed history gives ℤ" still read `[OPEN]` interpretation despite N-2 CLOSED (pre-existing since ≤v1.2). *Fix:* updated to scoped `[RESULT][from: ALG]`.
**F5 (housekeeping) — silent replacement of tagged text.** v1.4 replaced the v1.2 §6.1 two-notion `[DEF]` (count/order vs magnitude/ratio) with the three-notion `[DEF]` without a changelog line. Substantively acceptable — the old protection is subsumed by SG-NG-20/22 + N-5A — but tagged-text replacement must be recorded. *Fix:* provenance line added to the v1.4.1 changelog.
**F6 (recommended) — covariance audit under-pinned.** `HYP-NG-0R-COV` named no specific transformation, leaving post-hoc freedom contrary to falsification-first pre-registration. *Fix:* primary transformation pinned — amplitude scaling `Q → λQ`, with the substantive prediction that naive form-invariance of `ΔQ = −Q² + O(Q^{5/2})` FAILS (intrinsic scale) and the testable covariance is flow-translation in `ln Q`, i.e. `Q₀ → λQ₀` acting only through the `[CAND]` φ* entry-phase shift `τ ln λ`; explicit falsifier; `[CAND]` cap on the φ* leg; secondary transformations only by prior ledger entry.

## §5. Decision items

- **D14 (new):** adopt `RTG_NUMBER_GENESIS_DSN_v1_4_1.md` as canonical (v1.4 science + F1–F6 hygiene). All edits are annotation-grade; none change scientific state.
- **D8 (reiterated):** relay DZT v0.17 into the project corpus — v1.4 §8 `[PROVENANCE]` and the import ledger both correctly flag its absence; and relay the two external NG-8 certificate files for cross-check against the in-corpus re-certification.
- **D1, D9, D10 (unchanged/open):** Programme Overview registration of the three-programme labeling remains PI-gated (v1.4's routing-label guard defers correctly); number-semantics modal layer (D9) and the arity non-identity (D10, now with SG-NG-21 reserved) await ruling.
- **Queue confirmation:** NG-7A → N-2-ORD → N-4+N-5A → N-5 → N-6 → full NG-8, with `HYP-NG-0R-COV` parallel — consistent with D2/D3/D5; NG-7A is the next executable item on my side upon go-ahead.

## §6. Artifacts

| Artifact | Role |
|---|---|
| `RTG_NG_V1_4_IMPORT_AUDIT_v1.md` | this report |
| `NG_NG8AB_INDEPENDENT_RECERT_v1.md` | human-readable independent re-certification (premises, proofs, verdict) |
| `ng8ab_independent_recert_v1.py` / `.log` | exit-code-gated certificate; all assertions pass, exit 0 |
| `RTG_NUMBER_GENESIS_DSN_v1_4_1.md` | patched canonical candidate (8 anchored edits, each verified unique; guards now 1–22 with 21 reserved) |
