# Note to the RECOG co-owners — current state and the new working method

**Date:** 23 October 2026. **From:** the atlas owner (Claude), with the PI. **To:** the Relational Recognition (RECOG) DSN co-owners. **Status:** working note.

**Purpose.** RECOG has not changed since v0.3.22 (adopted 20 Oct 2026), but the corpus around it has: the documents now live in a git repository, Methodology v1.4 is in force, and four owners that RECOG imports from or exports to have new editions. This note brings you up to date and asks you to review RECOG's current state yourselves. The atlas advisory for RECOG follows as a second step, after your review; it is ready but deliberately not attached here, so that your review is not anchored on it.

## 1. How we work now

The full rules are in `CONVENTIONS.md` and Methodology v1.4 (`dsn/DSN_METHODOLOGY.md`). The short version:

- **The repository is the source.** Your DSN is `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` in `MustafaAksu/rtg-corpus`. The governing edition is the latest tag `recog-v…` together with its release record. The Claude project mirrors the repository; there are no hand-uploaded copies and no `_v0_3_x` files. Older editions come from tags.
- **Keep the file current-only** (v1.4 §1.1). Statuses, pins and scopes are edited in place; each change is recorded once in a compact Appendix A entry; draft rounds, review correspondence, audits and notice history go to the release record and `records/recog/`, not into the DSN.
- **Releases** go through a branch, a change-focused review, a release record, PI adoption, then merge and tag by the PI (`CONVENTIONS.md` §4). A release that also reorganizes layout is built in two stages (corrections, then compaction), and stage 2 is checked with `tools/check_compaction.py`. Dyadic v6.4.21 was the pilot (`records/dyad/RTG_DYADIC_v6_4_21_RELEASE_RECORD.md`).
- **Evidence lives with the claims.** Certificates and their outputs go to `evidence/recog/`, cited in §8 by path and hash. Goal: anyone can test a RECOG claim from the repository alone.
- **Files from your sessions** go unchanged to an `upload/…` branch (or to the PI if you have no repository access); they are hash-checked before placement. Nothing is reconstructed.

## 2. Your edition in the repository

| item | state |
|---|---|
| RECOG v0.3.22 | tag `recog-v0.3.22`; 1,581 lines, 329,148 bytes; SHA-256 `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9` (`BASELINE.md`) |
| earlier editions | not in the repository; they exist only in the PI's archive |
| release and governance records (`RECOG_v0_3_22_RELEASE_RECORD.md`, `RECOG_v0_3_21_RELEASE_RECORD.md`, `RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md`, G2 audits, A1a records) | **not in the repository**, and not found in the files available to the atlas sessions. If you hold the originals, please hand them over unchanged. RER cites the freeze-provenance record with SHA-256 `5c00f66d…9b55`, so that file at least existed with a known hash. |
| scripts and certificates cited in §8 (about 40) | not in the repository |

## 3. What changed around RECOG since v0.3.22

Facts as stated by the owners at their tags. None of this changes a RECOG statement by itself; whether a RECOG text needs updating is your call.

**Methodology v1.4** (`methodology-v1.4`, adopted 22 Oct): git-based workflow; live-file rule (§1.1); compact Appendix A; release records and evidence custody (§13.7); governing edition = tag + release record (§13.9); the `[RESULT]` pairing and conditional-proof rule (§3.4, key M13-C04) unchanged in substance.

**Number Genesis v1.20.8** (`numgen-v1.20.8`, adopted 21 Oct): the RIDs your A1a cell was waiting for are registered — `NUMGEN-DEF-N5AS1-DEFECT` ($D_M$), `NUMGEN-RESULT-N5AS1-INF1`, `NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT`, and `NUMGEN-RESULT-N5AS1-L-BACKBONE`, `-L-MONO`, `-L-PHASE`. NUMGEN records Dyadic's row-A L-PHASE theorem as received and defers its import.

**Dyadic v6.4.19 → v6.4.22** (`dyad-v6.4.22`, adopted 23 Oct):
- `DYAD-THM-LPHASE-ROWA-REMAINDER` (v6.4.19): explicit L-PHASE constant on row A, base points in $U$; not conditional on R9.
- 13 RIDs registered at v6.4.20, among them items RECOG cites without RID: `DYAD-DEF-CRITICAL-CURVE` ($C_0$; it cites your Whitney-fold result), `DYAD-ALG-QC-CRITICAL-AMPLITUDE` ($Q_c$), `DYAD-ALG-ISP-MAPS`, `DYAD-ALG-SIXSTEP-CUBIC-JET`, `DYAD-ALG-RAW-ANGULAR-MEAN` (47/54); also `DYAD-ALG-KP-FRAME-SCALE` (frame scale across $p$: $\nu_3^Z=\cot^2(\pi/p)\nu_3^{W_p}$) and `DYAD-THM-SMOOTH-EQUIVARIANT-CHART`.
- §1 fixed-point table now lists the wrapped-cylinder winding fixed points and states agreement with RECOG §6.3.
- T1/T2, the memory law and OPEN 21 remain `[THM] [assuming: RECOG-THM-R9-MEMORY]`; Dyadic records N11 as RECOG's adopted use in A1a.
- Relation to your $S_h$: $j^6S_h=j^6R_0$; DYAD-THM-SMOOTH-EMBEDDING gives a $C^\infty$ involution commuting exactly with $T$ at germ scope (not a physical exchange).
- v6.4.21 compaction (layout only) and v6.4.22 wording; Dyadic now writes "RECOG R11" for your final-chart ledger.
- Notices N19 and N21 to RECOG are **prepared, not yet sent** (`records/dyad/DYAD_NOTICES_N16_N21.md`).

**RRF v0.8.4** (`rrf-v0.8.4`, adopted 20 Oct): imports W3 verbatim from RECOG v0.3.21 with RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS; inter-space transport is labelled a separate OPEN RRF extension (your RF-1 request is answered).

**RER v0.2** (`rer-v0.2`, adopted 21 Oct, noncanonical): G9 quotes W1/W3 from your §6.16g; RER keeps RECOG v0.3.20 as its frozen pin and records v0.3.21/v0.3.22.

**OFN v0.10** (adopted 19 Oct) predates v0.3.22; no change.

**Atlas v0.2** (`atlas-v0.2`, accepted 23 Oct): `atlas/RTG_STATE_ATLAS.md`, domain D3, holds RECOG's current state as the atlas reads it, with its diagnostics in D3.L5. The atlas is derived and noncanonical; where it disagrees with RECOG, RECOG wins.

## 4. Please review

Before you see the advisory, please give your own reading of RECOG's current state:

1. **Census.** Is the OPEN registry as you understand it today? (As the atlas reads it: R1 PARTIAL, R3 PARTIAL, R4/R5/R6 ACTIVE; R2, R7, R8, R9, R10, R11 closed.) What is the actual next work on R6?
2. **Atlas reading.** Read atlas D3 (L1–L4 and L5) and tell us where it misreads RECOG.
3. **Upstream changes.** Against §3: which RECOG passages now state something no longer true (pins, "RID unavailable", pending repins, notice states), and which owner changes, if any, touch a RECOG claim at statement level?
4. **Unreleased work.** Is there RECOG session work since v0.3.22 (drafts, scripts, certificates) that is not in the DSN? If so, it goes to an `upload/…` branch.
5. **Records.** Where are the original release and governance records (§2)?

## 5. What comes next

After your review, the PI shares the atlas advisory for RECOG v0.3.22 (two independent passes, reconciled into one proposal). It proposes one successor release in two stages — corrections, then compaction — and some optional research items. You decide every row; nothing in it is binding.
