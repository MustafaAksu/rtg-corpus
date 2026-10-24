# Note to the Genesis co-owners — current state, the advisory, and what is asked of you

**Date:** 24 October 2026. **From:** the atlas owner (Claude), with the PI. **To:** the Genesis Geometry (GEN) DSN co-owner sessions. **Status:** working note; PI decision of 24 Oct 2026: *the Genesis co-owners prepare the next edition; the atlas owner advises and reviews.*

**Purpose.** Genesis has not changed since v2.8.9 (adopted 19 Oct 2026). Around it, Dyadic moved to v6.4.22, OFN to v0.10, RRF to v0.8.4, Programme to v1.3, Methodology to v1.4, and the corpus moved into a git repository. Two independent advisories (atlas owner; ChatGPT, blind) have now been written against your edition and reconciled. This note brings you to the current state and hands you the reconciled list; the edition is yours to build.

## 1. How we work now

Full rules: `CONVENTIONS.md` (repository root) and Methodology v1.4 (`dsn/DSN_METHODOLOGY.md`). Read `CONVENTIONS.md` before any edit. In short:

- **The repository is the source.** Your DSN is `dsn/RTG_GENESIS_GEOMETRY_DSN.md` in `MustafaAksu/rtg-corpus`; its governing edition is the latest tag `gen-v…` with its release record. No versioned copies, no `_v2_8_x` files; older editions come from tags.
- **Current-only live file** (v1.4 §1.1). Statuses, pins and scopes are edited in place; one compact Appendix A entry per edition; draft rounds, reviews and notices go to the release record and `records/gen/`.
- **Releases**: branch → change-focused review by the other co-owner and the atlas owner → release record → PI adoption → merge commit (never squash) and annotated tag by the PI. A release that also reorganizes layout is built in two stages: stage 1 corrections (assertion-gated script, exact-once edits, checker with negative controls), stage 2 layout-only compaction checked by `tools/check_compaction.py` with a movement map and an intermediate hash. Precedents: Dyadic v6.4.21 (pilot), RECOG v0.3.23 (`records/recog/`, `evidence/recog/`), Programme v1.3 (`records/programme/`, `evidence/programme/scripts/`).
- **Evidence lives with the claims**: `evidence/gen/`, cited in §8 by path and hash.
- **Every session has read and write access.** Push your own `chatgpt/*`, `claude/*` (or agreed stream-named) branches; open a PR; do not hand files to the PI. Outside files arrive unchanged on an `upload/…` branch and are hash-checked.
- **Never invent** hashes, RIDs, approvals or file contents; say when a source is not available.
- **Notices**: none are sent for now (PI decision); a cross-stream notice structure comes later. Record what *would* be notified in the release record.

## 2. Your edition in the repository

| Item | Value |
|---|---|
| File | `dsn/RTG_GENESIS_GEOMETRY_DSN.md` |
| Governing edition | v2.8.9, tag `gen-v2.8.9`, SHA-256 `d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc` (1,649 lines; `BASELINE.md` row GEN) |
| Declared methodology | v1.3 (v1.4 lets a document keep its edition until migrated) |
| Records on `main` | `records/gen/GENESIS_V2_8_9_NOTICE_ERRATUM_OFN_Q6_v0_1.md` |
| Not in the repository | the v2.8.9 release record (`GENESIS_V2_8_9_RELEASE_RECORD.md`, `f6df5d11…4181`, cited by the erratum) and the v2.8.x draft/review records. If your sessions hold them, please place them unchanged on an `upload/gen-records` branch; the atlas owner hash-checks and places them. If not, we record them as missing — nothing is reconstructed. |
| Consumers at their governing editions (Programme v1.3 §7.2) | TRIAD v1.6.1 (IF06, pin v2.8.7), UVM v0.7.1 (IF08, pin v2.8.5), RECOG v0.3.23 (IF15), RRF v0.8.4 (IF30, pin v2.8.9; §6.2a cites §6.3c), OFN v0.10 (IF32; §5.5 and IMP-O10-01 import §6.3a–c), noncanonical RER/FMS/ER-2B (IF33–35) |
| Producers you pin | DYAD v6.4.13 (governing v6.4.22), TRIAD v1.6 (governing v1.6.1), TDRG v2.12.13 (blocked interface IF25) |

## 3. The advisory you are asked to disposition

Three records, all on `main` once PR #37 and PR #38 are merged:

1. `records/gen/ATLAS_ADVISORY_GEN_v2_8_9.md` — pass 1 (atlas owner): GA-01…09 live-text inconsistencies, GB-10…16 RIDs/proof sources/pins/methodology, GC-17…21 interfaces.
2. `records/gen/ATLAS_ADVISORY_GEN_v2_8_9_INDEPENDENT_CHATGPT.md` — pass 2 (ChatGPT, written blind): G29-I01…I13.
3. `records/gen/ATLAS_ADVISORY_GEN_v2_8_9_RECONCILIATION.md` — the merged list (§3) and the PI questions (§4). **This is the list you work from.**

The two passes agree everywhere. The items that need a *scientific* decision from you, not an editorial one:

- **GA-01 / G29-I01 (P0).** The "Local sourced-junction theorem" (§1, §6.9) is stated with K₊ = ΔM_f + τI and an unconditional "valid minimizer"; GCL-02 (§6.8) established the secular algebra for K₋ and left the physical sign, energy branch and minimizer OPEN. The algebraic K₋ reconstruction does not decide the K₊ question; the missing piece is an energy functional with a second-variation criterion. Either supply it, or scope the theorem to "stationary solution exists for the algebraic branch; physical minimizer OPEN (GCL-02)" — at §1, §6.9 and the §7 export line. OPEN M imports this theorem.
- **GA-02/GA-03 / G29-I02 (P0).** κ = |m||w| (§6.8) vs κ = m|w| (§6.9 9A, OPEN-GEN-II-9); m = 2Q_sB_* with B_* undefined and unsigned; the soft-branch label and v₊ swap for m < 0; Π± divide by κ (κ = 0 domain). One convention, one definition of B_*, and a negative-m check of the residue formulas.
- **GC-17 (P1).** Dyadic v6.4.22 now has `DYAD-THM-SMOOTH-EMBEDDING` and `DYAD-THM-SMOOTH-EQUIVARIANT-CHART`: a C^∞ Φ with ΦTΦ⁻¹ commuting with A exists, so §6.3c (C2) is non-vacuous in C^∞ and G-20's "vacuous if no such Φ exists" is no longer the live situation; the analytic case (Dyadic OPEN 20 / B-6) stays open. One import row and one sentence.

Everything else is bounded: scope words (GA-04/05), one record per RID (GA-06), closed items out of active lists (GA-07), the 6 ↔ 13 phase-moment relation (GA-08), wording (GA-09), RIDs for the unnumbered theorems — exported ones first (GB-10), the nine "proof-source reference required" artifacts classified (a) missing / (b) not placed / (c) not rerun (GB-11), the c_θ⁽⁶⁾ import status (GB-12), the GSPLIT = DELTA-QC line (GB-13), the T-6u case label (GB-14), §7 structure and a Consumers block (GC-18/19).

## 4. What is asked of you, in order

1. **Read** `CONVENTIONS.md`, Methodology v1.4 §§1.1, 3.4, 12, 13.6–13.9, and the three records in §3.
2. **Disposition table.** Fill the "Owner disposition" column of the reconciliation §3 (accept / accept with change / reject with reason / defer) in a record `records/gen/GEN_OWNER_DISPOSITION_ADVISORY_v2_8_9_<session>_<date>.md`, one per co-owner session, on your own branch. Where the two co-owners differ, say so; the atlas owner reconciles and the PI decides.
3. **Answer the PI questions** you can answer as owners (reconciliation §4): Q3 — does an energy-functional / second-variation argument for the constrained birth exist in the Genesis archive? Q4 — can the proof sources of P4-PRIMITIVE, G2-CHRONO, FACE-LIFT, SOURCED-JUNCTION be recovered? Q1 (edition: v2.8.10 corrections-only vs v2.9 with the Methodology v1.4 migration) and Q2 (which co-owner builds) are the PI's; give your recommendation.
4. **Build**, after the PI fixes the dispositions: stage 1 on a branch from `main` (script under `evidence/gen/scripts/`, exact-once edits logged with hashes, checker with negative controls, intermediate hash); stage 2 if the edition migrates (movement map, `tools/check_compaction.py`, negative fixtures); release record `records/gen/RTG_GENESIS_GEOMETRY_v<version>_RELEASE_RECORD.md` (DRAFT) listing the dispositions, hashes, the consumers that would be notified, and the live-file exceptions you keep on purpose.
5. **Review**: the other co-owner reviews stage 1 and stage 2 change-focused; the atlas owner runs its row checks (as `records/recog/ATLAS_ROW_CHECK_RECOG_v0_3_23_STAGE1.md`). Then PI adoption, merge commit, tag; the atlas owner verifies the tag and refreshes the atlas (D4a/D4b, H6).

## 5. What is not asked

No rerun of the K₃ obstruction certificates or the Dyadic campaigns; no change to `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` and its hypotheses; no physical selection of κ, γ or the sourced-junction branch beyond scoping; no notices. The advisory does not grade your claims; where it says a statement is inconsistent it quotes both owner lines and leaves the choice to you.

## 6. Contacts and pointers

Atlas: `atlas/RTG_STATE_ATLAS.md` (`atlas-v0.4`, noncanonical; D4a/D4b carry the Genesis nodes and the diagnostics GEN.D1–D16 behind the advisory). Programme: `dsn/RTG_PROGRAMME_OVERVIEW.md` v1.3 §6.3, §7.2 (IF05–IF08, IF15, IF25, IF30–IF32), §8.2 (κ table). OFN class-C contract: `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md` v0.10 §5.5, §11.4. Questions to the atlas owner go as PR comments or as a record in `records/gen/`.
