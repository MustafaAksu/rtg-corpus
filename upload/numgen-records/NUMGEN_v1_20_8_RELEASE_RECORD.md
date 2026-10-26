# NUMGEN v1.20.8 — release record

**Date:** 21 October 2026 · **Owner:** Number Genesis (PI Mustafa; Claude, DSN editor/auditor; ChatGPT, co-owner)
**Status:** `[SESSION]` release record. It records the adoption, the release pass and its verification. The owner side ran the release verification. An independent verification of the adopted file is a separate step and is not claimed here.

## 1. Identities

| Object | SHA-256 | Note |
|---|---|---|
| Predecessor: v1.20.7 | `c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28` | unchanged; remains the prior adopted edition (frozen 2026-10-01) |
| Reviewed source: DRAFT r3 | `9d59cfa1edf15c4e263494c9fbc615dc915ed3b84e556df8ade61fd1fa7de7b3` | co-owner delta review: scientific review accepted, artifact verification passed |
| r3 review package `NUMGEN_v1_20_8_DRAFT_r3_REVIEW.zip` | `a7fc9ed63113e7f6f48296b9593b92467b94314d71f5117e106cf9dcdbe1ee84` | builder, checker (G1–G13, N1–N10), diffs, replay inputs |
| **Adopted v1.20.8** `RTG_NUMBER_GENESIS_DSN_v1_20_8.md` | **`835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e`** | 3,412 lines, 339,003 bytes |
| Release transform `release_v1_20_8.py` | `5f219ee949776db1741ccf8e6bc9ec0c15ee06d785adc5d46d65b25209c738f3` | refuses any input other than r3 |
| Release edit list `release_v1_20_8_edits.json` | `c9148e8dbcba76222c07daed7f7677478ca590e89e5e158dcba971f3b2da9414` | 5 exact-once edits |
| Release checker `check_release_v1_20_8.py` | `1f97081e330e2c3d18eaa3aac6366727527fbbac71185911ded9dbfd96fa092d` | gates P0–P9 |
| Checker output `check_release_v1_20_8_output.txt` | `1d04c1aed566da409982d11c784abd28a254398b76b86c20263f5ee895ca4c38` | 10/10 PASS; 6/6 negative controls caught |
| r3 → adopted diff `v1_20_8_r3_to_release.diff` | `2e24ad5846c744a1e83b02d9bb551fdbb2a6b2a0f8b1d301c9bfe7c9f12b741f` | 6 lines removed, 8 added |
| v1.20.7 → adopted diff `RTG_NUMBER_GENESIS_v1_20_7_to_v1_20_8.diff` | `65c548549c4a309465cb61faf24c0feecfe4fbff8a985b17cb39a5cae27eb468` | full edition delta |
| Tools: `ng_state_fingerprint_v2_3.py`, `ng_inv_live_v1_1.py` | `1fbeb19d…3ff6`, `3354621b…f7a145` | unchanged |

## 2. Adoption authorization

- **Decision:** PI, 21 Oct 2026, 09:26 local time: "v1.20.8 DRAFT r3 (`9d59cfa1…e7b3`) adoption için uygundur. benimsiyorum."
- **Basis:** the co-owner delta review of r3 gave three findings:
  - SCIENTIFIC REVIEW ACCEPTED;
  - ARTIFACT VERIFICATION PASSED;
  - PI OWNER ADOPTION READY, with no r4 needed.

  The co-owner independently reproduced the ZIP and file hashes, G1–G13 (13/13), N1–N10 (all caught), INV-LIVE (0 hits) and the Dyadic replay JSON (`8697c697…a4fa`).
- **Earlier review chain:**
  - r1: scientific scope accepted, two repairs;
  - r2 (`423cd719…7b78`): review accepted, PI adoption pending;
  - r3: narrow fact synchronization (Dyadic v6.4.19, RECOG v0.3.22, RRF v0.8.4, N15).
- **Conditions:**
  1. Publication metadata only, with the scientific body preserved.
  2. The final, r3 and v1.20.7 SHAs are recorded separately.
  3. v1.20.7 stays canonical until this release. The governance confirmation of 21 Oct requires this, and this record satisfies it.

## 3. Release delta (r3 → adopted), 5 edits

| Edit | Change |
|---|---|
| R1 | title: "— DRAFT r3" removed |
| R2 | date line: "DRAFT r3" → "adopted" |
| R3 | document status: "DRAFT r3 — not adopted … Supersedes on adoption … until adoption" → ADOPTED owner ledger (PI adoption 21 Oct 2026 on r3; co-owner review); "Supersedes: v1.20.7, retained unchanged as the prior adopted edition"; release record named |
| R4 | §9.1 A1a disposition cell: "canonical on adoption of this edition" → "canonical from the adoption of this edition (21 Oct 2026)" |
| R5 | changelog heading → "v1.20.8 — October 21, 2026 (adopted)", plus an adoption paragraph; the draft record follows unchanged |

## 4. Checker result (P0–P9, all PASS)

| Gate | Check |
|---|---|
| P0 | The input is r3 and the base is v1.20.7 (both hashes). |
| P1 | The release is deterministic. |
| P2 | Reversing the release edits gives r3 byte-exactly, so nothing changed outside the 5 spans. |
| P3 | Each new text occurs exactly once. |
| P4 | The claim-block status-tag multiset is identical to r3. |
| P5 | The explicit and bare RID sets are identical to r3. |
| P6 | The OPEN claim blocks are identical to r3. |
| P7 | No row-A constant appears. |
| P8 | The edition markers are in adopted form. |
| P9 | INV-LIVE reports 0 live hits. |

**Negative controls (all caught):** M1 body edit outside the spans; M2 regrade; M3 RID dropped; M4 constant entered; M5 OPEN sub-item closed; M6 stale title. They are fail-closed engineering probes, not independent proofs.

## 5. Registered on adoption

Six canonical owner RIDs (§6.6):
- `NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT`
- `NUMGEN-DEF-N5AS1-DEFECT`
- `NUMGEN-RESULT-N5AS1-L-BACKBONE`
- `NUMGEN-RESULT-N5AS1-L-MONO`
- `NUMGEN-RESULT-N5AS1-L-PHASE`
- `NUMGEN-RESULT-N5AS1-INF1`

Three OFN definition imports at source grade (§1.1). No result, proof, domain or grade changed.

## 6. Carried open after release

- **L-PHASE explicit constant:** `[OPEN]`. Dyadic `DYAD-THM-LPHASE-ROWA-REMAINDER` is adopted upstream (v6.4.19); the NUMGEN import by RID is reserved for a later edition. An explicit-tube INF-1 also needs an explicit L-BACKBONE constant, which is not started.
- **Unchanged:** C7C-M2 Census-1 INCONCLUSIVE / INCONCLUSIVE; full-interface WD-DOM OPEN; M-4 HOLD (Discrete P2); RF-06 source-side correction with the Discrete owner.
- **Dyadic pins:** stay at v6.4.18 (co-owner ruling); the consumed passages are byte-identical in v6.4.19.
- **Messages prepared, dispatch is the PI's** (none sent by this record):
  - To RECOG: C4 reply v0.1.1 (`23273f86…95b6`) and RID reply v0.1.1 (`a2e7bf98…1902`). RECOG can now repin `A1A-NG-D-DEF` / `A1A-NG-INF1` to canonical RIDs.
  - To FMS: R8 attribution notice.
  - To Dyadic: requests, reply, receiving review, interface confirmation (`7a91c223…f78f`), receipt replay (`71bfc4c5…b66f`), and an N15 receipt line citing this file's hash. Dyadic may now mark N3 ANSWERED.
- **Independent release verification** of `835a56f8…817e` against this record is optional.
