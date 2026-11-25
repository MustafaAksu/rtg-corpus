# Triadic contributor review of RER v0.2 DRAFT r2 — record-by-record scope check

**14 October 2026 · NONCANONICAL review · no adoption.** Reviewed: `RTG_RELATIONAL_EMERGENCE_REGISTRY_v0_2_DRAFT_r2.md` (SHA-256 `3d346b84d63cc25b8a565bb6407bcd5bd674fb0b811b4165fd41e054f762b163`) and `REGISTRY.json` (`888321b962f03b7dda8a5604e3e5763160f8d4ead6a09363be580d9a3494f0ea`), records that import my results or Triadic-side work. Each statement was compared with the source note it pins, not with memory of it.

## 1. Dispositions

| Record | Disposition | Notes |
|---|---|---|
| RER-GEN-C07 | **ACCEPT SCOPED** | Drift, order, "does not refute event-time initialization" all match C07. |
| RER-GEN-C08 | **ACCEPT SCOPED** | Both witnesses (5t⁵/32; κ²t⁹(−1/18, 1/9)) and the "no exclusion of all 2D reachable factors" boundary are right. |
| RER-GEN-C09 | **ACCEPT SCOPED** | Orders 5/9/10 and the non-uniform-in-age domain are stated correctly. One wording point: "Equal parent states have different future Qs" should read "equal parent states of *unequal fixed ages* …" — as written it could be read as a same-age statement. |
| RER-TRIAD-FORMAL-AGE | **ACCEPT SCOPED** | [THM] + `FORMAL_ONLY`, deg_τ ≤ ⌊(d−3)/2⌋, uniqueness only in the polynomial-coefficient class, typed parameterization i(s,τ) with `F∘i = i∘F_param` as formal series — exactly the agreed scope (§§8–9 of my C09 note). The contract type `FORMAL_PARAMETERIZATION_SEMICONJUGACY_NOT_REDUCTION` is the right name. |
| RER-TRIAD-AGE-CURVATURE | **ACCEPT SCOPED** | w₁₃ polynomial, D₅∧R₈ = w₁₃, "a zero of the leading factor is not exact collinearity" — all correct; the "not invariant under arbitrary nonlinear changes of the complete state" guard is the Triadic caveat I accepted. |
| RER-TRIAD-REGULAR-3FOLD | **ACCEPT SCOPED** | Hypotheses (both sheets graphs over a full parent neighbourhood — which follows from DF(0)=I) and the proof sketch are right. Suggest adding to Constraints: "the argument uses only C07's drift and C¹ continuity of D_cH at 0; the same proof covers any pair n ≠ m". |
| RER-ER2B-T6D | **ACCEPT SCOPED** | Modal ΔQ_T^[4] in producer units and the parity argument are quoted correctly; the "descent from its OWN producer remains open" split is exactly what Triadic and I agreed. Suggest naming the symmetry in Transformation law as "edge-slot swap 2↔3 ⇒ F(s,−c) = (F_s, −F_c) exactly", so a reader sees it is a model identity, not an approximation. |
| RER-F3-N7N8 | **ACCEPT SCOPED, with three corrections on my side** (below) | The record's refusal to accept any global K is right; the Stage-1 v2 table is transcribed correctly; the three-box non-cover statement is right. |

## 2. Corrections and withdrawals on the N7/N8 line (my side)

1. **Pilot finding (v) withdrawn.** I wrote that K_perp/K between 0.98 and 1.19 shows "the defect is not predominantly along D₅". A ratio of two *upper bounds* says nothing about the actual direction of 𝓔; the transverse channel is reported, not interpreted, until a lower bound on the transverse fraction exists. The record's sentence to this effect is correct.
2. **Verifier hardening (record contract).** The delivered `triad_stage2_coverage.py` accepted any PASS record with matching hashes. It now validates every published field against the plan and config: exact rational endpoints equal to the planned square and τ-layer; N ∈ N_LIST; K_deg, dps, κ̃ equal to the config; R_floor equal to the ring's inner radius; R_eff ≥ R_floor (to precision tolerance); R_min < R_max; τ+1 interval exact; six step records with parseable fields and last-step ρ_c, λ consistent with the summary; every published constant upward-rounded to ≤ 4 significant digits with K_up ≥ K_raw; duplicates with differing K_raw rejected. Tamper test: a wrong rounding, a wrong endpoint and a five-step record are each rejected for the named reason while genuine records pass. New SHA `ed19d7139c5a2e96c7a6d526db7692f448398ca1ecfb81fc8f416e3b4b5e1ac5`.
3. **Directed serialisation.** Published decimals were produced by round-to-nearest (`nstr`). Engine v3.1 (`triad_tm_engine_v3_1.py`, SHA `674961ccd19b48653c40f5698668f21d832f1d948a91259eb36d1a639694e17e`; arithmetic unchanged, only the serialisation of step records and τ+1 now exact/directed) and driver v2 (SHA `cb26b2e427e323bbc128f01032c232cfb9c00f3c951379dc01ebc43905a41276`) now convert each interval endpoint exactly (dyadic mpf → Fraction → Decimal) and round upper bounds up and lower bounds down. The config's engine field points to v3.1; the config hash therefore changes and prior records (pilot) do not validate against it, by design.
4. **K = 8 pilot file.** The container was reset between sessions and the background K = 8 run was lost; it is rerunning on engine v3 (its hash is recorded in each line) and the complete `stage2_pilot_K8.jsonl` will be supplied as an informational file, not as records of the governing config.

## 3. Points for the registry editor
- RER-F3-N7N8 "the delivered verifier accepted invalid PASS contracts in the source review" — I have not received `STAGE2_RECEIVING_REVIEW.md` (SHA `c935a4ac…d4e2`) itself; the hardening above addresses the summary in r2. If the review lists further failure modes, send it and I will add them to the tamper test.
- The TM-lemma independent review (product truncation, Lagrange remainders, remainder transport through A⊕A, post-map Lipschitz radius) remains the gate before any `CONTROLLED_APPROXIMATE_CLOSURE` record; nothing here changes that.
- Work-queue item P1 "historical lifted generator → own root diagnostic" is Triadic-internal and I can take it after the pilot; it does not depend on anything in this review.

No owner document, RER record or physical selection is changed by this review.
