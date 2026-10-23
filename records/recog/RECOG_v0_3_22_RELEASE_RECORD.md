# RECOG v0.3.22 — release record

**Date:** 20 October 2026 · **Owner:** RECOG (PI Mustafa; Claude, co-owner)
**Status:** `[SESSION]` release record. It records the adoption, the release pass and its verification. The release verification below was run by the owner side; independent release verification of the adopted file is a separate step and is not claimed here.

## 1. Identities

| Object | SHA-256 | Note |
|---|---|---|
| Base: adopted v0.3.21 | `a3459522c8f58204f83f5e65e3d1a99912f9651d1c17cc4fb0c090196f670ae3` | unchanged; remains the prior adopted edition |
| Adopted source: DRAFT r3 | `8f496d3c1fd0182e058e5fd814c5530e3952d5469b3ea932d3d3f27718fbd959` | 1,579 lines |
| **Adopted v0.3.22** `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_22.md` | **`0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9`** | 1,581 lines, 329,148 bytes |
| Release transform `release_recog_v0_3_22.py` | `a7134299f406f3cd75113bed0096c787b5fc36d419b1f411cccea5d0e76075e1` | refuses any input other than r3 |
| Release edit list `recog_v0_3_22_release_edits.json` | `679d598dcfdc46abd7b87a3780816f90ae16c106ecaa1e99972a110fe43dfb24` | 12 exact-once edits |
| Release checker `check_recog_v0_3_22_release.py` | `15c35c1fefa0537a71a27875a8309f922339c1d05a081f1c8364059b1be375a3` | gates P0–P12 |
| Checker output `check_recog_v0_3_22_release_output.txt` | `9efae7e6aae415fe165d256a601833d7fe0528e9e1a643ae2df2c70b48f8efe1` | 13/13 PASS; 11/11 negative controls caught |
| r3 → adopted diff `recog_v0_3_22_r3_to_release.diff` | `af71a055d50127183e3535340a5d5808bb7dd47d9329c8c431f05a569c528084` | 12 lines added, 10 removed |
| Outbound notices `RECOG_v0_3_22_OUTBOUND_NOTICES.md` | `0de67ec4f643800719f91d164940a22cafb07d5e828e9b278e08ab9f8da45ed5` | prepared; none sent |
| r3 review package | `b8c4fc60d68b7b0d4f1037121b0294e581812fe62b8b81061fc369c012ea87ba` | builder, checker and evidence for r1–r3 |

## 2. Adoption authorization

- **Decision:** PI, in the RECOG co-owner conversation, 20 Oct 2026, 19:30 local time: "RECOG v0.3.22 DRAFT r3'ü benimsiyorum". Disposition: `ADOPTION APPROVED — PROCEED WITH CONTROLLED RELEASE`.
- **Basis named by the PI:**
  - the independent delta review of r3, `2a65093baa6a07e57faa056ecd755cc8689f94c59d5f071996b31ebb5979fc96` (`REVIEW ACCEPTED — READY FOR SEPARATE PI ADOPTION DECISION`);
  - the A1a-G1 governance disposition;
  - the earlier scientific reviews.
- **Earlier review chain:**
  - cell v0.4 release-readiness review `d195af7a…8445274`;
  - r1 integrated review `c1d49013…8d17`;
  - r2 integrated review `fee7e519…0efe`;
  - A1a-E2 source check `941f42d6…126e`.
- **Conditions set by the PI:**
  1. the release pass is limited to edition markers, adoption information and §8 provenance metadata;
  2. NUMGEN allocations are not canonical before v1.20.8, so `RID unavailable` is kept and the repin is done in a separate revision;
  3. the final NUMGEN reply and its addendum are entered after their hashes are verified;
  4. R6 and every other OPEN status stay unchanged;
  5. the new SHA, the delta and the checker result are recorded separately, which this record does.

## 3. Release delta (r3 → adopted), 12 edits

| Edit | Kind | Change |
|---|---|---|
| P1 | marker | title: "(DRAFT r3)" removed |
| P2 | marker | date line: "not adopted" → "adopted 20 Oct 2026" |
| P3 | marker | "Supersedes (on adoption)" → "Supersedes" |
| P4 | adoption | status summary label; "eight proposed RIDs (registered only on adoption)" → "eight scientific RIDs and four artifact IDs, all registered on adoption" |
| P5 | adoption | status summary release state: "PI adoption pending" → adoption by the PI on r3 after the delta review |
| P6 | marker | freeze status: v0.3.22 adopted; release record named; not frozen |
| P7 | adoption | §6.13b registration sentence |
| P8 | adoption | §7.2 N13 use field: "proposed use … takes effect only on adoption" → "used … in effect from adoption"; receipt and verification fields unchanged |
| P9 | provenance | §8: final NUMGEN reply v0.1.1 (`a2e7bf98…1902`) and addendum (`582d931e…ceae`); both hashes verified in this session |
| P10 | provenance | §8: r3 delta review (`2a65093b…fc96`) |
| P11 | adoption | Appendix A heading and adoption line; the draft history is kept |
| P12 | marker | footer |

**Checker result** (P0–P12, all PASS):
- P3 reverse application gives r3 byte-exactly, so there is no change outside the 12 spans.
- P4 grade-tag sequence identical to r3.
- P5 RID sequence identical to r3.
- P6 OPEN status lines identical.
- P7 vocabulary count identical.
- P8 §6.13b identical apart from the registration sentence; the R9 line is identical.
- P9 N13 receipt and verification fields identical.
- P10 no approved NUMGEN string present, and the `RID unavailable` count is unchanged.
- P11 the three provenance hashes are present.
- P12 the edition markers are in adopted form.

**Negative controls:** all 11 caught. They are fail-closed engineering probes; P1 alone would catch most of them, so they are not independent proofs.

**Reproduction:** run in a clean directory with `python -I`. The adopted file, the edit list and the checker output are byte-identical to the archived copies.

## 4. Registered on adoption

**Scientific RIDs (8), §6.13b:**
- `RECOG-DEF-A1A-PHASE-INTERFACE` `[DEF]`
- `RECOG-THM-A1A-LIFT-ALIGNMENT` `[THM]`
- `RECOG-THM-A1A-RECIPROCAL-AMPLITUDE` `[THM]`
- `RECOG-THM-A1A-PHASE-EXISTENCE-ALT` `[THM] [assuming: H-NG]`
- `RECOG-RESULT-A1A-PHASE-EXISTENCE-NG` `[RESULT] [from: ALG]`
- `RECOG-THM-A1A-CD-IDENTIFICATION` `[THM]`
- `RECOG-RESULT-A1A-CD-AGREEMENT` `[RESULT] [from: ALG]`
- `RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION` `[THM]`

**Artifact RIDs (4), §8:**
- `RECOG-ART-A1A-C1-CHECK`
- `RECOG-ART-A1A-NUM`
- `RECOG-ART-A1A-RECORDS`
- `RECOG-ART-A1A-SOURCE-AND-GOVERNANCE`

The RECOG RID set of v0.3.22 equals that of v0.3.21 plus these 12, with none lost. Every pre-existing RID keeps its statement and grade.

## 5. Evidence classes and limits (carried)

- **(c) and OPEN 21:** source-statement fidelity against Dyadic v6.4.18. The Dyadic P5 certificate and RECOG's R9 Arb certificate were not rerun in this cycle.
- **A1a-G1:** allocation resolved. The evidence is:
  - NUMGEN reply v0.1 and final v0.1.1, whose body is byte-identical to v0.1;
  - the NUMGEN co-owner ruling given by the PI in this conversation, recorded in `RECOG_A1A_G1_DISPOSITION_RECORD_20261020.md` (`0e5f91c0…71a7`). The independent reviewer did not see the ruling's original text; this limit is recorded.
- **Not packaged** but cited by identity: the NUMGEN C4 reply and its receiving review, and the reviews of cell drafts v0.1–v0.3 (PI-held).
- **Gate 6 of the lift-alignment check script** (RECOG-ART-A1A-C1-CHECK) is a `[NUM]` dense check. The two scalar inequalities it samples are proved in the text.

## 6. Carried open after release

- **Repin** of `A1A-NG-D-DEF` and `A1A-NG-INF1` to canonical NUMGEN RIDs, in a separate RECOG revision after NUMGEN v1.20.8 is adopted and inspected.
- **Notices** in `RECOG_v0_3_22_OUTBOUND_NOTICES.md`: N-D (Dyadic), N-NG (NUMGEN) and N-O/N-R/N-E (informational). All are prepared and **unsent**.
- **G3 notices for v0.3.21** to OFN, RRF and RER: still **unsent**. The G3 Dyadic notice was answered (dispatch record r3).
- **Unchanged:** R6 ACTIVE; R1 and R3 PARTIAL; R4 and R5 ACTIVE; R2 and R7–R11 CLOSED. RECOG-THM-R9-MEMORY and its rows are unchanged.
- **Independent release verification** of `0dcce9e4…bcd9` against this record is optional, as for v0.3.21.
