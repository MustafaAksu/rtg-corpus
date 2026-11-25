# RER Phase A r6: change record

**Date:** 19 Oct 2026.
**From:** Claude, RER co-owner (preparer). The preparer does not accept his own work.
**Status:** NONCANONICAL Phase A candidate, revision 6. Nothing is adopted, frozen or published.
**Trigger:** a preparer self-correction found while preparing Phase B source reviews. No receiver finding asked for it.

## 1. What was wrong in r1–r5

The blocked-source register's `byte_availability_gap` note said the printed-hash sources were "not in the preparer workspace". **That was incomplete.**

A hash scan of the session uploads that the PI had supplied found 14 of the 27 cited keys whose bytes had not been verified. Each file's SHA-256 equals the hash cited in RER r4.6. Neither the cited hashes nor the RER text was at fault; the error was only in what the preparer said was available.

## 2. Change

- **Files added.** The 14 files are added to `sources_available/` under their cited names, taken from their containers without modification.
- **Custody record.** `inputs/source_custody_r6.json` records each file's key, SHA-256, container, container SHA-256, member path and supplier (PI, session upload).

| Key | Container |
|---|---|
| GENMODEL, RANK, F3, REACH, AGE, JET | `RER_TRIAD_CONTRIBUTOR_HANDOFF_20261009.zip` (`a10a9bc9…1277`) |
| ANGLE, **ER01** | `RTG_ER2B_CONSOLIDATED_v0_1.zip` (`46c1dad7…a24f`) |
| N7REVIEW | `TRIAD_N7N8_RECEIVING_REVIEW_20261010.zip` (`ece707ad…5423`) |
| RECOG | `RTG_RELATIONAL_EMERGENCE_REGISTRY_v0_1_20261008.zip` (`033d6742…105c1c`) |
| FORMAL, AGEGEO, TMREVIEW, S2FOLLOWUP | loose upload files |

- **RECOG owner evidence:** `PRINTED_ONLY` becomes `BYTE_VERIFIED`. The header still reads freeze candidate; no adoption or freeze is asserted.
- **ER01:** the reason now says that the cited v0.1 study bytes are byte-verified. **The blocking reason is unchanged**: the v0.2 primary package is missing, and certificate custody is open.
  - Both ER-2B records stay `BLOCKED_SOURCE_UNVERIFIED`.
  - The four ER01 rows stay `BLOCKED`.
  - The G8/0 gap reference to ER-2B v0.1 C15 now has verified bytes. Whether that changes its blocked reading is the receiver's decision.
- **Still without bytes (14 keys):** ANGLE_DATA, DYAD6413, ERADD, ERREPLY, G2NOTE04, GEN287, HARM, K36S, K3REC, OFN9, R3_REQUEST, RANKDATA, RRF082 and RRF08_ADOPTED.
  - The receiver separately byte-verified DYAD6413, GEN287, OFN9 and RRF082, and those rows carry `RECEIVER_BYTE_VERIFIED`.

## 3. Effect (89 rows; 35 rows change)

| Measure | r5 | r6 |
|---|---|---|
| Authentication | BYTE_VERIFIED_HERE 23, RECEIVER_BYTE_VERIFIED 6, HASH_PRINTED_UNVERIFIED 59, UNAUTHENTICATED_NO_HASH 1 | **BYTE_VERIFIED_HERE 58**, RECEIVER_BYTE_VERIFIED 6, HASH_PRINTED_UNVERIFIED **24**, UNAUTHENTICATED_NO_HASH 1 |
| Status | VERIFIED 23, OWNER_REPORTED 6, HISTORICAL 53, BLOCKED 7 | **VERIFIED 30**, OWNER_REPORTED **4**, HISTORICAL **48**, BLOCKED 7 |

**Status changes.** Seven rows change status:
- **N7REVIEW (3 rows), TMREVIEW (1), S2FOLLOWUP (1):** HISTORICAL → VERIFIED. They are artifact-pinned evidence files, now byte-matched.
- **RECOG (2 rows, gap references G9/0 and G9/1):** OWNER_REPORTED → VERIFIED.

**Snapshot rows** (GENMODEL, ANGLE, RANK, F3, REACH, AGE, JET, FORMAL, AGEGEO) gain `BYTE_VERIFIED_HERE` but keep `SNAPSHOT_RECHECK_IN_PHASE_B`, and therefore stay HISTORICAL. The currency of each underlying owner result is still a per-record Phase B check.

**Other outputs.** The registry JSON and the blocked register change only in `schema` (/5 → /6) and the corrected gap note. No record, grade, contract table or OPEN status changes, and the r4.6 Markdown is unchanged.

## 4. Gates: 22/22 PASS; negative controls 22/22 fail as required

- **New gate A22.**
  - All 14 custody entries must be present. Each file hash must equal its entry, and the entry must equal the cited hash for its key.
  - The ER01 rows must stay BLOCKED while their bytes are present.
- **New control:** an ER01 row relabelled HISTORICAL fails A22.
- **Unchanged:** the 21 r5 controls are carried. A19 and A21 still hold; OFN stays `OWNER_REPORTED` here.

## 5. Meaning and limits

`BYTE_VERIFIED_HERE` means only that the bytes are identical to PI-supplied copies. It is not:
- a certificate rerun;
- scientific acceptance;
- an owner adoption;
- an unblocking.

The files are noncanonical study, review and handoff records, except RECOG, which is an owner freeze-candidate file.
