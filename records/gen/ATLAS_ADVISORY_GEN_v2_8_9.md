# Atlas advisory — Genesis Geometry v2.8.9 → next edition (pass 1 of 2)

**Date:** 24 October 2026. **From:** Claude (atlas owner). **To:** the PI and the Genesis owner session(s). **Status:** advisory; the Genesis owner and the PI decide every row. Nothing here changes a document. A second, independent pass (ChatGPT) follows; the two are reconciled before any edit.
**Object:** `dsn/RTG_GENESIS_GEOMETRY_DSN.md` v2.8.9, tag `gen-v2.8.9`, SHA-256 `d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc` (= file at `main` `a1c267a`), adopted 19 Oct 2026 under Methodology v1.3; 1,649 lines. Line numbers below are at that hash.
**Basis:** atlas v0.4 (`atlas-v0.4`) H6, D4b GEN.D1–D7, D14 and the D4a rows F9, F10, F14–F17, F19, F20 that carry GEN.D9–D16; atlas audit item A04-06 (deferred to this advisory); `records/gen/GENESIS_V2_8_9_NOTICE_ERRATUM_OFN_Q6_v0_1.md`; DYAD v6.4.22, OFN v0.10, RRF v0.8.4, Programme v1.3 at their tags; Methodology v1.4 §§1.1, 13.6–13.9. Every finding below was re-read in the owner text at `gen-v2.8.9`; nothing is carried from the atlas unverified. No proof or certificate was rerun.

## 0. Why now

Genesis is the integrating continuous study (Programme v1.3 §6.3) and the producer for OPEN M (IF08), RECOG (IF15), Triadic (IF06), RRF (IF30) and OFN's class-C contract (§6.3b–c via IF31/IF32). Its last adopted edition, v2.8.9, is a scientific release (D-4: §6.3c) built on the v2.8.5 reconciliation base; it declares Methodology v1.3 and pins Dyadic v6.4.13 and Triadic v1.6. Since then Dyadic adopted v6.4.22 (incl. `DYAD-THM-SMOOTH-EMBEDDING`, `DYAD-THM-SMOOTH-EQUIVARIANT-CHART`, which bear directly on §6.3c (C2)/G-20), OFN v0.10 adopted the class-C contract that cites §6.3b–c, Methodology moved to v1.4 (live-file rule), and Programme v1.3 records Genesis's maintenance pass as "executed" at v2.8.9. The atlas has carried eight Genesis-internal diagnostics since v0.2 that no Genesis edition has dispositioned. This advisory puts them, and the new interface items, in front of the owner in one list.

## 1. Proposed outcome and release contract

One Genesis edition (v2.8.10 if the owner treats it as maintenance + scoped corrections; v2.9 if the owner migrates to Methodology v1.4 in the same edition — owner's call, §4 Q1), built the way RECOG v0.3.23 and Programme v1.3 were: stage 1 (exact-once corrections, assertion-gated script, checker with negative controls), stage 2 (layout-only compaction checked by `tools/check_compaction.py`), publication transform (status lines only), release record, PI adoption, merge commit, annotated tag. Two independent advisories (this one and ChatGPT's), reconciled in `records/gen/`, define the stage-1 scope; the owner dispositions every row (§3).

Labels: **I** inconsistency inside the live text · **S** stale against an adopted source · **Y** RID/identifier · **E** editorial/clarity · **G** governance/methodology.

## 2. Findings register

### 2.1 Tier A — live-text inconsistencies (owner must choose one statement)

**GA-01 | I | Sign convention of the sourced-junction theorem (atlas GEN.D1; A04-06).** §1 line 68 and §6.9 line 1049 state the `[THM]` "Local sourced-junction theorem" with the constrained birth written as `(ΔM_f + τI)d⊥ + S_f = 0` (= K₊). §6.8 GCL-02 (lines 1012–1020) and §6.9 9B-tau (lines 1076–1085) establish that the documented secular equation belongs to **K₋ = τI − ΔM_f**, that K₊ flips the 2aτ sign, and that "the physical ±ΔM_f sign, energy branch and minimizer selection" are `[OPEN]` (line 1038). The theorem statement was not re-typed when GCL-02 was applied. Owner options: (a) restate the theorem for K∓ ("a valid minimizer exists for either algebraic branch; which branch is physical is OPEN (GCL-02)"), if the minimizer argument is sign-independent; (b) restate it for K₋ and say so; (c) demote the "valid minimizer" clause to the GCL-02 `[OPEN]`. Load-bearing: the theorem is in the export list (§7 line 1185) and OPEN M imports it (atlas OPENM.U3).

**GA-02 | I | κ = |m||w| (§6.8) vs κ = m|w| (§6.9 9A, OPEN-GEN-II-9 item 1) (atlas GEN.D2, H6).** Line 1004: `(ΔM_f)² = κ²I, κ = |m||w|`; lines 437 and 1060: `λ± = (τ−g) ∓ κ, κ = m|w|`. For m < 0 the two differ by sign, so the "soft branch τ−g−κ → 0" and the eigenvector v₊ = (μ₁, μ₂−|w|) swap labels. m = 2Q_sB_* has no stated sign. Owner options: fix a sign convention for m (or for B_*, GA-03) and use one κ; or write κ := |m||w| everywhere and λ± = (τ−g) ∓ sgn(m)κ. Note for the atlas: the atlas labels this face-lift κ as "κ_f"; Genesis writes κ in both places, and the atlas now says so (atlas v0.4, C04-10). No rename is asked of Genesis.

**GA-03 | I/E | B_* undefined (atlas GEN.D6).** `m = 2Q_sB_*` (line 1004) is the only occurrence of B_* in the file; no definition, no RID, no pointer. OPEN M reuses `m = 2Q_sB_*` in its R2. Owner: define B_* (or replace by the quantity meant) at its first use, with its sign (GA-02).

**GA-04 | I | Projection nontriviality: OPEN vs ✓ (atlas GEN.D4).** §6.9 line 1054 `[OPEN]` "Projection nontriviality … See OPEN-GEN-II-9"; SG-13 line 563 "Projection nontriviality is `[OPEN]`, not resolved"; Appendix B line 1637 `[RETRACTED]` "resolved … downgraded to `[OPEN]`; see OPEN-GEN-II-9 sub-step 3". OPEN-GEN-II-9 sub-step 3, line 439: "Projection nontriviality — R_soft ≠ 0 generically at H₀ = J_Qs_*, both pairings: `[ALG]` ✓". These are consistent only if the ✓ is read as "under the scalar-M ansatz" and the `[OPEN]` as "for general M (and physically)", but neither site carries that scope word. Owner: add `[scope: scalar-M ansatz]` at line 439 and "(general M; physical dominance)" at lines 563 and 1054, or re-grade one of them.

**GA-05 | I/E | OPEN-GEN-II-9 dependency line lacks the raw-array qualifier (atlas GEN.D14).** Line 450: "diagonal splitting −2m Im w gives B-self-adjointness (generalization beyond scalar-M)". Everywhere else (§6.9 9C, line 1087; §2 OPEN-GEN-II-9C, lines 485–495) the result is stated **"if the additional modelling premise K^⊤B = BK is imposed"** / "under that raw-array premise". One clause: "(conditional on the raw-array premise K^⊤B = BK; …)".

**GA-06 | Y/I | Two §2 entries headed by the same RID `GEN-OPEN-WPHASE` (atlas GEN.D11, F19).** Line 171 "OPEN 5/2B — Face W-phase / gap functional [RID: GEN-OPEN-WPHASE]" (ACTIVE, corrected live formulation) and line 275 "OPEN 5 / 2B — face-phase / healing-core insertion [RID: GEN-OPEN-WPHASE]" (ACTIVE — "corrected live formulation is the OPEN 5/2B block above"). One RID, one record (Methodology v1.4 §1.1 item 3). Owner: delete the stub at line 275 (its content is history) or fold any residual obligation into the line-171 record.

**GA-07 | I/S | Frontier list and OPEN registry disagree on status (atlas GEN.D12, F20).** (i) OPEN 1T is **CLOSED** at line 256 ("CLOSED / current import protocol (v2.8.5 adopted reconciliation)") and in Appendix A line 1344, but appears in the priority ordering as frontier item 1b (line 94) with no status word. (ii) OPEN 2 (lines 266–271) lists under "Active sub-items" one item marked "`[ALG verified]` / `[THM]` — done v2.2". Under v1.4 §1.1 (current only; one home) a closed item is recorded once (Appendix A / Appendix B) and leaves the active list. Owner: drop 1b from the priority ordering or label it "closed — protocol in force"; move the done sub-item out of "Active sub-items".

**GA-08 | I/E | Two phase-moment sets without a map (atlas GEN.D13, F15).** §6.6 line 965: `ℳ_phase = {m^C, m^S, m^{CS}, m^{S2}, m^{CC}_transfer, m^{CS}_transfer}` (6 named moments). OPEN 1A line 138: `⟨𝒫₄⟩` is "a linear form in exactly 13 trigonometric phase moments" `{1, c_dc, c_dc c_sc, …, s_ds²}`. Both are live; neither says how the 6 relate to the 13 (projection? different closure?). Owner: one sentence at §6.6 or OPEN 1A giving the relation, or retire the 6-moment list if superseded by the v2.7.4 reduction.

**GA-09 | I/E | Wording of the NF/primitive sign split, §1 line 61 (and its §6.5 home) (atlas GEN.D16, F17).** same block, line 61: "No claim is made here that a passive representation change alone explains the sign difference"; §1 line 61 (the typed-comparison `[THM]`): "NF-frame healing is a normal-form coordinate statement, not a primitive-amplitude statement". Both sentences sit in one `[THM]` block; compatible only as "different objects compared"; a reader can take the second as the explanation the first disclaims. Owner: one sentence tying them ("the comparison is between different objects; whether a matched transport relates them is Candidate B, OPEN").

### 2.2 Tier B — RIDs, proof sources, pins, methodology

**GB-10 | Y | Unnumbered `[THM]`s without RIDs (atlas GEN.D7; OPENM.U3).** §1/§6.7/§6.9 theorems "Pure chiral protection", "Φ₂→₃ leading birth", "Tetrahedral chronological protection", "Primitive Q_d-quartic drift closed", "Universal (quaternionic) no-go", "Smooth single-face metric criterion", "Local sourced-junction theorem", "NF/primitive sign split", and the `[ALG]` "Uniform independent phase average", "Apex-correlated foam" carry no `[RID: GEN-THM-…]`; only artifact RIDs `GEN-ART-*` stand in (§8). Consequences: OPEN M imports four of them as "RID unavailable"; the §7 export list (line 1185) names theorems that cannot be cited by RID; the atlas and RRF use `GEN-ART-*` as surrogates. Owner: register RIDs for the exported theorems first (metric criterion, sourced junction, quaternionic no-go, quartic drift), then the rest; keep the `GEN-ART-*` keys as artifact RIDs (they are not claim RIDs).

**GB-11 | G/Y | Nine §8 artifact entries read "proof-source reference required" (atlas GEN.D3, F14).** `GEN-ART-PURE-CHIRAL, PHI-2TO3, G2-CHRONO, P4-PRIMITIVE, PHASE-AVG, PHASE-CLOSURE, QH-NOGO, FACE-LIFT, SOURCED-JUNCTION`. P4-PRIMITIVE feeds the cascade chain; FACE-LIFT and SOURCED-JUNCTION are exported. Under v1.4 §12 a `[THM]` whose proof source is not available is a `[THM]` with evidence state "proof-source missing", not a defect in the claim — but the state must be declared at the claim, not only in §8. Owner: either attach the proof sources (scripts/notes recovered to `evidence/gen/`), or declare the evidence state at each claim block and in the release record.

**GB-12 | S/Y | c_θ^(6) = −119√3/648 is used (line 682) while §7 says the Lie-gauge normalization RID is not imported (line 1142) (atlas GEN.D9, F16).** The value carries `[conv: Lie strict-kernel gauge]`; §7's v2.8.6 repin note says `DYAD-ALG-LIEGAUGE-NORM` "is now the archival Lie-gauge normalization only and is not imported here". Either the value is imported (add the import row with the pin and RID actually used) or it is not used live (move to history). Related: H6 — the chart coefficient in RECOG CHART-LAWS/R9 is +89√3/324; a phase-moment retest should name which gauge it uses.

**GB-13 | Y/E | GSPLIT ↔ DELTA-QC lemma line (atlas GEN.D10, F9).** `GEN-OPEN-WPHASE-GSPLIT` (line 206) gives ΔE_c^birth = ⅓Q_c² + ¾Q_sQ_c; `GEN-THM-DELTA-QC` (line 1204) is the standalone pump at I_sc = 0, where ¼ω² + 5/16 ω² = 9/16 ω² = ¾Q_sQ_c via ω² = 4/3 Q_sQ_c. TRIAD CN-03 records the identity; Genesis does not. One line at the GSPLIT record: "= `GEN-THM-DELTA-QC` standalone form at I_sc = 0".

**GB-14 | E | `GEN-CAND-APEX-T6U` quotes one case (atlas F10).** Line 1215/1335: R_apex = √21/64 ≈ 0.0716 "~20× below √2". Triadic's T-6u headline is the four-case maximum R = √14/16 (shortfall > 6×). Label the quoted case (shear/vector) or cite the Triadic table.

**GB-15 | G | Methodology edition and live-file rule.** Header: "DSN Methodology: DSN_METHODOLOGY_v1.3"; companion list names Programme v1.2, OFN v0.9, Methodology v1.3, DYAD v6.4.13, TRIAD v1.6. Methodology v1.4 §13 lets a document keep its declared edition until migrated, so this is not a violation; it is the single largest maintenance item. Under v1.4 the following would move or shrink: the **Supersedes** line listing 24 editions (v1.4 §1 header: immediately preceding edition + hash only); the "Status summary" paragraph that narrates v2.8.5→v2.8.9 layering; Appendix A (lines 1252–1599, ~350 lines, with DRAFT-record sub-entries → one compact entry per version, draft rounds to the release record, M14-C02); §2 OPEN registry (lines 88–521, ~430 lines, 21 records) where closed items and "resolved vX.Y" narrative sit beside live obligations (GA-07); `[RESULT]` blocks — 47 of 51 carry no `[from: TAG]` pairing (v1.4 §3.4; v1.3 allowed the older pairing form). Programme v1.3 §9.2 lists the Genesis maintenance pass as executed at v2.8.9; the v1.4 migration is a separate, later item and is **not** owed by the Programme record. Owner/PI: decide whether the next edition migrates (then stage 2 is a real compaction and the version is v2.9) or stays on v1.3 with corrections only (v2.8.10).

**GB-16 | E/G | Tier statement.** Header "Programme tier: Tier 3/4 — Integrating document". Programme v1.3 §6.1 places Genesis in Tier 3 and records discrete inputs as blocked interfaces, "Genesis's own header tier statement is the owner's". No conflict is asserted by the Programme; the owner may keep "3/4" or align to "3 (integrating; discrete inputs via blocked interface IF25)". Informational.

### 2.3 Tier C — interfaces with adopted consumers and producers

**GC-17 | S | §6.3c (C2) and G-20 vs Dyadic v6.4.22 (atlas H1, F5, OFN.O1; also OFN/FMS/ER-2B).** Line 887 (C2, conditional): "If Φ is a real C³ diffeomorphism … with N_Φ := ΦTΦ⁻¹ commuting with A"; line 892 G-20: "The theorem neither requires nor supplies existence of an exactly transported realization; (C2) is vacuous if no such Φ exists." Dyadic v6.4.22 now has `DYAD-THM-SMOOTH-EMBEDDING` (C^∞ J_ℤ6 commuting with T; B-∞ existence closed) and `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` (C^∞ chart Φ with ΦTΦ⁻¹ commuting with A). So (C2) is **non-vacuous in C^∞**; only the analytic case (B-an/B-6) is open. G-20 stays true as a statement about the theorem's hypotheses; what is stale is the implicit "if any". Owner: add one import row (DYAD v6.4.22, the two RIDs, scope C^∞ local germs) and one sentence after G-20: "a C^∞ Φ exists (DYAD-THM-SMOOTH-EQUIVARIANT-CHART); the analytic case is Dyadic OPEN 20 (B-6)". This is the Genesis-side half of the H1 correction; OFN, FMS and ER-2B carry the other halves.

**GC-18 | S | Pins.** §7 imports from Dyadic v6.4.13 and Triadic v1.6; governing editions are v6.4.22 and v1.6.1 (Programme v1.3 IF05/IF07 record the v6.4.13 / v1.6 pins as the consumer's declared state, not a defect). Owner decides per claim whether to repin; GC-17 needs at least one v6.4.22 row. The RRF export notes (lines 1193–1197) name RRF without an edition; RRF v0.8.4 §6.2a is the consumer that now cites §6.3c — pin it (IF30/IF31).

**GC-19 | E/G | Consumers not recorded.** §7 "Export protocol" lists what may be exported but not to whom. Programme v1.3 §7.2 records GEN → TRIAD (IF06), GEN → UVM (IF08), GEN → RECOG (IF15: B, J_Q, pairings, phase memory), GEN → RRF (IF30), GEN → OFN scoped feedback (IF32), and the noncanonical records RER/FMS/ER-2B (IF33–35). RECOG is not mentioned in Genesis at all (1 incidental hit). Methodology v1.4 asks for consumer fields where a producer's change would obligate notice (§5 OPEN records; §13.7 release records). Owner: a short "Consumers" block in §7 naming the six, with the pins they declare — useful for the notice structure the PI plans.

**GC-20 | E | γ ≡ κ and the class-C model (atlas RRF.F5, CLASS-C; Programme E-P13-1).** Genesis is correct and need not change: SG-16 "γ is a model parameter" and §6.3c "G^N_γ … γ is a model parameter". The record for the owner: OFN v0.10 §11.4/§5.5.4 and RRF v0.8.4 §6.2a write γ ≡ κ as a parameter convention and define class C as the same declared operation as G^N_γ while stating it is a different conditional model from the raw F_γ; the atlas v0.4 now reads it that way, and the Programme's §8.2 sentence calling the convention an atlas reading is recorded as E-P13-1. If Genesis wishes, one sentence in §6.3c acknowledging the OFN/RRF convention (without adopting κ) would close the loop; optional.

**GC-21 | E | OFN notice erratum.** `records/gen/GENESIS_V2_8_9_NOTICE_ERRATUM_OFN_Q6_v0_1.md` corrected the release record's OFN notice wording (narrow-Q6 grade). OFN v0.10 §5.5/§11.4 route through the six-step theorem as the erratum asks. Nothing further for Genesis; the next release record should cite the erratum as applied.

### 2.4 Routed, no Genesis edit

- OPEN M (UVM v0.7.1): imports GEN theorems as "RID unavailable" (atlas OPENM.U3) → resolved by GB-10 on the Genesis side, then an OPEN M repin.
- Triadic v1.6.1: CN-03 (GSPLIT identity) already recorded; GB-13 is the Genesis mirror.
- OFN/FMS/ER-2B: H1/F5 wording ("existence not asserted / real only once J realized") → their own passes; GC-17 is Genesis's part.
- RER: `RER-E-CONJ` identifies RER 𝒩 with GEN F₁ (atlas F2); a noncanonical record, transfers nothing; Genesis need not cite it.
- Atlas: after the next Genesis edition, refresh D4a/D4b and H6; retire GEN.D1/D2/D4/D6/D11/D12/D13/D14/D16 as dispositioned; disambiguate `RECOG-ALG-SHEAR-WEIGHT-IDENTIFICATION` `~` link to the κ-family (atlas v0.4 receiving review §4).

## 3. Owner disposition table (to be filled by the Genesis owner; PI decides)

| Key | Tier | Proposed | Owner disposition | Note |
|---|---|---|---|---|
| GA-01 | A | restate sourced-junction THM for K∓ / K₋, or demote minimizer clause to GCL-02 OPEN | | export-listed |
| GA-02 | A | one κ convention (sign of m) | | atlas label κ_f unaffected |
| GA-03 | A | define B_* | | OPEN M R2 reuses it |
| GA-04 | A | scope words at lines 439 / 563 / 1054 | | |
| GA-05 | A | raw-array qualifier at line 450 | | |
| GA-06 | A | one `GEN-OPEN-WPHASE` record | | delete stub line 275 |
| GA-07 | A | frontier 1b / OPEN 2 "done" out of active lists | | |
| GA-08 | A | relation 6 ↔ 13 phase moments | | |
| GA-09 | A | tie §1 and §6.5 sentences | | |
| GB-10 | B | RIDs for unnumbered THMs (exported first) | | unblocks OPEN M |
| GB-11 | B | proof sources or declared evidence state ×9 | | |
| GB-12 | B | import row for c_θ^(6) or move to history | | |
| GB-13 | B | GSPLIT = DELTA-QC lemma line | | |
| GB-14 | B | label T-6u case | | |
| GB-15 | B | Methodology v1.4 migration (v2.9) or corrections only (v2.8.10) | | PI question Q1 |
| GB-16 | B | tier wording | | optional |
| GC-17 | C | DYAD v6.4.22 import row; sentence after G-20 | | H1 Genesis half |
| GC-18 | C | repins per claim; RRF pin | | |
| GC-19 | C | Consumers block in §7 | | notice structure |
| GC-20 | C | optional sentence on OFN/RRF γ≡κ convention | | |
| GC-21 | C | cite erratum in next release record | | |

## 4. Open questions for the PI

1. **Edition type.** Corrections only on Methodology v1.3 (v2.8.10, smaller stage 2), or migration to v1.4 with full compaction (v2.9; Appendix A, §2 registry, header, `[RESULT]` pairings)? The RECOG and Programme precedents were migrations.
2. **Who builds.** The Genesis owner session builds stage 1 from the reconciled advisory, the atlas owner reviews (as for RECOG); or the atlas owner builds and the owner reviews (as for Programme). Both AIs have write access.
3. **GA-01 option** (a/b/c) is a scientific choice about the minimizer argument; the owner should answer it, not the atlas.
4. **GB-11**: is proof-source recovery feasible from the archive (scripts named in §8), or do we declare the evidence state and move on?

## 5. PI decisions

_(to be filled)_
