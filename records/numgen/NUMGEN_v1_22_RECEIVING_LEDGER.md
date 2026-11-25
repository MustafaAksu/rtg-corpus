# NUMGEN v1.22 — receiving ledger (S2)

**Date:** 24 November 2026.
**Session:** Claude, Number Genesis co-owner.
**Status:** owner receiving decisions for the v1.22 pass.
- The eleven items are set to `dispositioned` on the v1.22 branch, with a pointer to this ledger.
- They are closed after `numgen-v1.22` is tagged.
- The DSN changes they lead to are the S3 edits listed in the v1.22 release record (DRAFT).

**Basis:**
- `records/numgen/ATLAS_ADVISORY_NUMGEN_SYNC_20261123.md` (rev. 2) and `records/numgen/NUMGEN_OWNER_DISPOSITION_SYNC_20261123_CLAUDE_20261124.md` (PR #374);
- the ChatGPT co-owner GO for S2–S3 (24 Nov 2026; S1 review comment `7128043448` on PR #375);
- `records/numgen/NUMGEN_v1_22_S1_P2_REANNOTATION.md`.

**Three separate states** (`pipes/README.md`):
- `state` is the queue;
- *statement accepted* is a verdict on the producer's statement;
- *adopted use* exists only where a NUMGEN Import Ledger row or this release cites the statement by RID at the producer edition.

A receipt never creates adopted use. The proposed-use column records the candidate's intended use; no new adopted use is asserted before PI adoption and publication.

| Key | Item (`pipes/NUMGEN/`) | Verdict | Statement accepted | Proposed use if v1.22 is adopted | DSN edit (S3) |
|---|---|---|---|---|---|
| P01 | `20261028-TDRG-v2-12-14-adopted.md` | accept with change | TDRG-DEF-ORIENT; the eight producer RIDs | §1.1 state-space and recurrence imports repinned to `tdrg-v2.13` with `TDRG-DEF-ZN-STATE`, `TDRG-DEF-PHYSICAL-STATE`, `TDRG-THM-RECURRENCE` (statements byte-identical to v2.12.13 apart from the RID tag; checked). The SG-10 firewall stays a guard citation without RID at `tdrg-v2.12.13` (unchanged at v2.13). TDRG-DEF-ORIENT is an implementation input only for the bounded consumer re-annotation (S1), not a new general theorem import. Frozen DISC evidence keeps `[conv: pinned TDR-G v18 …]`. | §1.1 lines 69, 71, 75; §2 item 1; §6.6 P2 lines; §9.1 TDR-G rows |
| P02 | `20261029-RECOG-v0-3-26-adopted.md` | accept | historical receipt; superseded by P07 | none | — |
| P03 | `20261030-DYAD-v6-4-23-adopted.md` | accept | `q_{3/4}` is not NUMGEN's `q_*` (`DYAD-THM-OPEN18-STEP-MONOTONE`); N15 receipt confirmed | none (row-A import unchanged; 403/250 unchanged) | §6.2 disambiguation at the `q_*` witness (closes NC-17) |
| P04 | `20261030-OFN-v0-11-adopted.md` | accept | REQ-O09-03 fulfilled | none | §9.1 REQ-O09-03 row |
| P05 | `20261030-OFN-v0-12-adopted.md` | accept | OFN uses the N-1A2 definitions as vocabulary only; the closure is not imported | none | §9.1 consumer row (OFN) |
| P06 | `20261104-PROG-v1-4-adopted.md` | accept | IF12, IF13, IF14, IF24, IF27, IF37 and IF38 checked against §9.1; SG-PROG-1 and SG-PROG-2 byte-identical at v1.4 (SG-PROG-1 checked) | none. The pin used stays v1.3, because the statement is unchanged; v1.4 becomes the current companion | §9.1 Programme and Genesis rows (IF37, IF38) |
| P07 | `20261104-RECOG-v0-3-27-adopted.md` | accept with change | GAP-LOCK Lemma 3 consumption at two grades; A1c without (D5) | none (A1c is comparison only, not imported). The eight-row matrix of v1.21 stays the baseline at v0.3.24 | §9.1 RECOG export and received rows |
| P08 | `20261111-DYAD-v6-4-24-adopted.md` | no action | imported statements unchanged; `DYAD-THM-OPEN21-SHARP-ROWS` noted (conditional on RECOG; not an L-PHASE input) | none | §9.1 current companion `dyad-v6.4.24` only |
| P09 | `20261112-TDRG-v2-12-15-adopted.md` | accept | star / multistar domain statement | none | none: no affected NUMGEN claim relies on the earlier K1,3-only restriction; RF-06 uses fixed-centre token inversion in its token-shift guard. The DISC panels are three-node and birth-free. |
| P10 | `20261119-DZT-v0-18-adopted.md` | accept | v0.17 files present as unadopted received history; governing DZT edition | none (NUMGEN imports nothing from DZT) | §8 `[PROVENANCE]` paragraph |
| P11 | `20261120-DZT-v0-19-adopted.md` | accept | `DZT-THM-CASCADE-NORM-LAW` as a scoped locator for the audit-reported statements | none (reference only, no import) | §8 `[PROVENANCE]` paragraph |

## Not received or changed here

- No new import from RECOG, OFN, DZT or Programme.
- No repin of the Dyadic imports.
- No change to the C7C algebra, Census-1, M4 HOLD, DISC-3 DEFER or the φ* comparison (OPEN).
- The four outbound items of 26 Oct 2026 are closed by their receivers. Nothing new is filed.

*END OF RECORD.*
