# RER Phase A r7: change record

**Date:** 19 Oct 2026.
**From:** Claude, RER co-owner (preparer). The preparer does not accept his own work.
**Status:** NONCANONICAL Phase A candidate, revision 7. Nothing is adopted, frozen or published.
**Answers:** the Phase A r6 receiving review of 19 Oct 2026:
- finding **A6-G8-01**;
- the container-provenance boundary.

## 1. Base

- **RER draft:** the same r4.6 bytes (`2fa878ff…4772`); no Markdown change.
- **Base package:** Phase A r6 (`909a4beb…ff0c`).

## 2. A6-G8-01: G8/0 is HISTORICAL, not BLOCKED

**The problem.** In r6 the key-level rule `ER01 = BLOCKED` also applied to the G8 gap reference (n = 0). That reference cites ER-2B v0.1 §5 C15 as historical, noncanonical context. Its bytes are verified, and it does not need the missing v0.2 primary package.

**The fix.** `catalog_sources.json` gains a `gap_reference_overrides` map. Only gap-reference rows use it, and its only entry is ER01. The builder applies it before the key-level rule.

| Row | r6 | r7 |
|---|---|---|
| RER-G8 / gap reference 0 / ER01 | BLOCKED, currency BLOCKED | **HISTORICAL**, currency `SNAPSHOT_RECHECK_IN_PHASE_B`, `BYTE_VERIFIED_HERE`, `gap_reference_review = PENDING_PER_REFERENCE_AUDIT` |
| The 3 ER01 record-import rows (RER-ER2B-T6D, RER-ER2B-CARRIER) | BLOCKED | BLOCKED (unchanged) |
| RER-ER2B-T6D, RER-ER2B-CARRIER records | BLOCKED_SOURCE_UNVERIFIED | unchanged |

**What else changes.** Exactly one matrix row changes, in its `currency`, `currency_reason` and `status`. The registry JSON and the blocked register change only in `schema` (/6 → /7). The blocked register is built from records, so it is unchanged.

**Counts:**

| Measure | r7 | Change from r6 |
|---|---|---|
| VERIFIED | 30 | — |
| OWNER_REPORTED | 4 | — |
| HISTORICAL | **49** | +1 |
| BLOCKED | **6** | −1 |

Authentication counts are unchanged: BYTE_VERIFIED_HERE 58, RECEIVER_BYTE_VERIFIED 6, HASH_PRINTED_UNVERIFIED 24, UNAUTHENTICATED_NO_HASH 1.

## 3. Container provenance

`inputs/source_custody_r6.json` gains `container_chain_status = PREPARER_DECLARED`. It states that:
- the receiver verified the content hashes of the 14 files;
- the container names, container SHA-256 values and member paths are the preparer's declaration;
- these were not re-verified on the receiving side.

## 4. Gates: 22/22 PASS; negative controls 23/23 fail as required

**A22 is narrowed.** It now requires:
- the three ER01 record-import rows to be BLOCKED, with bytes matched;
- exactly one ER01 gap row, RER-G8 n = 0, which must be HISTORICAL, have `SNAPSHOT_RECHECK_IN_PHASE_B` currency, carry `BYTE_VERIFIED_HERE` and have a pending per-reference audit;
- the custody file to declare its container chain as preparer-declared.

**Controls.** The 21 earlier controls are carried. The A22 control now targets a record-import row explicitly: unblocking an ER01 record row fails A22. One control is new: putting G8/0 back to BLOCKED also fails A22.

**Regression.** Run under the r7 checker, the r6 outputs fail three gates:
- A2 (rebuild);
- A19 (catalog check date);
- A22.

## 5. Not changed

- Both ER-2B records stay blocked.
- No scientific record changes, and no grade or OPEN status changes.
- The 13 gap references keep `PENDING_PER_REFERENCE_AUDIT`.
- G2 §5b stays `CARRIER_IDENTIFICATION_PENDING`.
