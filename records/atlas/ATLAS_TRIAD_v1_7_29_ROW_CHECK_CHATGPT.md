# Atlas receiving check — Triadic v1.7 fixed candidate, all 29 rows

**Date:** 2 November 2026. **Status:** [SESSION] NONCANONICAL Atlas receiver review; **PASS SCOPED / NO ATLAS-ROW BLOCKER**. This does not adopt science, merge, tag, close pipes or alter the Triadic candidate.

**PI scope decision:** proceed with existing bytes. **F-1** (67 qualifier conversions) **DEFERRED/NONBLOCKING**; **F-2** (six-sentence status-summary shortening) **DEFERRED/NONBLOCKING**; **F-3** (PR description correction) **CLOSED**. No extra scientific or editorial review round is requested.

## Identity and extent

- **Candidate:** PR #140, head `27ddc2fe97e3ba304940fd03792a8e24309d01a6`, `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md`, independently recomputed **SHA-256 `2573961a82ce10a348f76f10feece6fefb3831f3c4dd60de5dcae78acb745c0d`**, 148,596 UTF-8 bytes, Git blob `30b199f0b63d260d135d2532c352917e0d3c5cc7`. Candidate retrieved in full, targeted header, §§1–2, 6.1/6.4/6.9/6.15–6.18, §§7–9, App A/B read.
- **Stage 1:** `evidence/triad/v1.7/stage1_intermediate.md`, independently recomputed SHA-256 `b47d294d9dc82b78f05e02c99e04100177c78480c453438d5d4fca86e14ba66a`, 177,539 bytes; targeted comparison to candidate. **Base:** adopted `triad-v1.6.1`, SHA-256 `95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f`, targeted original owner passages.
- **Decision basis:** `records/triad/ATLAS_ADVISORY_TRIAD_v1_6_1_RECONCILIATION.md` §4 and `records/triad/TRIAD_OWNER_DISPOSITION_RECONCILIATION_v1_6_1.md` §§2–5; both read. Implementation: `records/triad/TRIAD_v1_7_STAGE1_IMPLEMENTATION_MATRIX.md`, all 29 rows inspected. Methodology `methodology-v1.4` and root `CONVENTIONS.md` consulted.
- **Targeted owner cross-checks:** `gen-v2.9` §§1/2/6 (GCL-06, T-6t at consumer [CAND], historical radial polynomial); `programme-v1.3` §§1/6 (pass two); `ofn-v0.12` §§2.4/9 (closure versus reference); `rrf-v0.8.4` §3.1 (CN-05 convention only). Dyadic `dyad-v6.4.23` and TDR-G `tdrg-v2.12.14` claim-pinning checks use producer's per-claim reading notes and prior co-owner read-back, not fresh full owner reads.
- **EV-INDEP/EV-HASH:** both candidate/stage-1 complete UTF-8 SHA-256 recalculated, 46/46 distinct Triadic RID strings, 29/29 unique anchors preserved. The two v1.6.1 custody records under `records/triad/` have identical Git blobs to the unchanged upload originals (`61d240c2…520d52`, `93142fce…9977ca`).
- **EV-SRC-REPORTED / EV-NOT-RERUN:** stage-1 99 assertion-gated edits; K1–K8/S1/S5/S6 PASS, 16 negative controls; stage-2 nine operations, `check_compaction.py` PASS, G0–G9 PASS and 11 study-specific fixtures caught; 256 qualified claim blocks = 241 byte-identical + 15 declared + 0 unexplained. Generic checker harness was only 5/16 caught + 11 not applicable; **not** 16/16. No historical scientific certificate or campaign rerun. Script PASS is not a semantic equivalence proof.

## 29-row receiving matrix

| Row | Verdict | Point-of-use verification |
|---|---|---|
| 1 — U1 | **PASS SCOPED** | §6.18 L762–766: two root-equivalent off-root extensions. (b): `f_s=dot Q_s, f_c=dot Q_c`, `dot D=0`; (a): `f_s=dot Q_s+rQ_s q_1, f_c=dot Q_c-rQ_c q_1`, `dot D=rq_1D`. Domain `Q_s,Q_c>0`, six-step-block **ODE** clock, special `D≡0`, H1/H2 missing, no physical/discrete or new-RID claim. |
| 2 — U2 | **PASS SCOPED** | §6.18 L753–758: Gram relation is degree-3 first variation, weights `Q_s,Q_c,I,Omega=1; r=1/2`, degree-4 finite-increment corrections explicit; six-step clock, same orientation RID retained. |
| 3 — U3 | **PASS SCOPED** | §6.9 L489–497: `6(sqrt3-1)K ≤ A_theta ≤ 6(sqrt3+1)K` inside existing T-6l ALG; leading order only; no finite-u/r persistence. |
| 4 — A4 | **PASS** | §2 L148–162: T-6r ACTIVE and complete C1–C6 (carrier group/metric, encoding, off-root evolution, clock, events/regularity, covariance), physical selection OPEN. |
| 5 — A9 | **PASS** | §2 L166–181: T-6q ACTIVE, three kinematic transformations with sigma column; not a physical node action, symmetry or T-6n continuation. |
| 6 — A5 | **KEEP/PASS** | §§6.15–17: T-6s coherent `0≤g_2≤2`, T-6t label signs not physical carrier, T-6u four typed leading ratios, not HINDEX. No regrade or source re-certification. |
| 7 — A6 | **PASS** | §1 L34: 96:1 coefficient bookkeeping, common generator/clock/observable bridge OPEN; hypothetical 192 metric example expressly not physical. |
| 8 — A7 | **PASS SCOPED** | §§7.1–7.2: claim-level dyad/gen repins and current Programme/OFN/RRF/TDR-G pointers. **Two held uses** remain pinned: GEN `P4=2d^TBG3d` premise absent at `gen-v2.9`, and changed Programme v1.2 §6.3 wording. GEN birth-symmetry owner wording THM in §6.6 versus ALG in summary/artifact is declared for GEN owner, not quietly resolved. |
| 9 — A8 | **PASS** | §7.4 L844–861: **10-row** CN×receiver matrix with producer claim pin, exact receiver edition, queue, acceptance, adopted use, outstanding gate. GEN T-6t [CAND]; RRF only a convention; OFN reference-only; Programme CN-05 queue not recorded; v1.6 receipt ≠ v1.6.1/v1.7 adoption. |
| 10 — U7 | **PASS** | Programme `programme-v1.3` is pass two; §7.4 says so, without inventing CN-05 receipt. |
| 11 — U8 | **PASS** | §2 obsolete "send CN-01–CN-05" queue removed; current §7.4 matrix replaces it. |
| 12 — U9 | **AFTER TAG** | Future claimant/receiver notices (especially GEN [CAND] and earlier v1.6 pins), no invented sent or accepted status. |
| 13 — U5 | **PASS** | §9 L968: 46 RIDs = 13 ALG + 22 ART + 2 EXPORT + 2 NUM + 7 OPEN; `OPEN-B/E1` corrected. Historic 49 claim acknowledged as unreproducible. |
| 14 — TA03a | **PASS at PI scope** | Mixed grade unpacking; source-quoted GEN [DEF/ALG] not a new Triadic grade. **F-1 explicitly deferred**, not full §3.2 conformity. |
| 15 — TA03d | **PASS** | Release-round labels removed from revised live qualifiers (stage-1 K7/fixtures source-reported). |
| 16 — U6 | **KEEP** | `(rep: [UNREGISTERED-TRIADIC-*])` stays local sentinel, not invented RRF profile. |
| 17 — TA01 | **PASS at PI scope** | v1.4 header fields, one predecessor, true DRAFT and evidence-state locations; **F-2 shortening deferred**. |
| 18 — TA02 | **PASS SCOPED** | Stage-1 tagged history edits and stage-2 S2-M/E01–E03; relocated original archived at `triad-v1.6.1`. Tagged R3/R4.2 evidence notes retained knowingly. |
| 19 — TA03bc | **PASS at PI scope** | Eleven §6 heading grades repaired in stage 1 (G01–G11); anchor set intact. Qualifier F-1 deferred. |
| 20 — TA04 | **PASS / limited** | Stage-2 Appendix A/B relocation/restatement; 9 declared operations and compaction checks PASS; proof/semantic-equivalence limit explicit. |
| 21 — U4 | **PASS** | Appendix B L1097–1113 separates valid negative conclusions from historically withdrawn wedge/torsion rationales; no current fatal-basin claim restored. |
| 22 — footer | **PASS** | Exactly one DRAFT footer; no stacked release metadata. |
| 23 — U11 | **PASS** | Repository locator `rtg-corpus`, not `rtg-resonance-2025`. |
| 24 — custody | **PASS** | Two original v1.6.1 records placed byte-identically under `records/triad/`; no claim of entire original ZIP intake. |
| 25 — U10 | **PASS** | T-6c2 and T-6l producer scripts exist under `evidence/triad/scripts/`; historical hashes cited, T-6l rerun producer-reported; no scientific regrade. |
| 26 — A3 | **PASS** | T-3a v4g is labelled incomplete scaffold, not an Arb scientific certificate; no owner theorem depends on it. |
| 27 — TC04 | **PASS** | `evidence/accepted_r4_2/`, T-6j2 and other missing sources remain held/missing/session-only, not forged or rerun. |
| 28 — recovery | **PASS** | `records/triad/TRIAD_SOURCE_RECOVERY_LIST.md` P/H/K/S/F states and exact source limitations are present. |
| 29 — tool profile | **DEFER** | Optional `history_appendix` profile depends on PR #113 (**open and unmerged** at check time). Not required in v1.7; study-specific fixtures document the boundary. |

## Publication boundary and outstanding obligations

**[SESSION] 29/29 ROWS ACCOUNTED FOR — PASS SCOPED.** Implementation/KEEP/AFTER-TAG/DEFER statuses all correspond to the reconciled 29-row list. No blocking scope, evidence, consumer, RID, source or structural discrepancy was found for exact candidate `2573961a…5c0d`.

**Nonblocking debt:** F-1 = DEFERRED; F-2 = DEFERRED; F-3 = CLOSED; row 29 = DEFER. These do not authorize a new patch, grade upgrade or an additional scientific review; v1.7 does **not** assert full Methodology v1.4 formatting compliance.

**Release dependencies:** PRs #137 and #138 (independent dispositions), #139 (joint reconciliation), and #140 (stacked candidate) were all **open** when checked. Preserve order **#137 and #138 → #139 → #140** and require a PI scientific adoption decision before merging the canonical candidate. The v1.7 release record does not yet exist; its completion follows the PI adoption decision.

**Next permitted sequence:** PI scientific adoption of the exact bytes → release record → metadata-only publication transform → ordered merge commits → annotated `triad-v1.7` tag → post-tag validation and recipient-specific notices/pipe updates. The current governing Triadic source remains `triad-v1.6.1` until publication. Atlas-v0.8 frozen source pins are not changed by this receiving review; a future Atlas edition must refresh its manifest after the Triadic tag.

**No candidate edit, scientific adoption, canonical merge, release tag or pipe closure was performed in this check.**
