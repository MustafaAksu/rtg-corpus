# RER Phase A r8: change record

**Date:** 20 Oct 2026.
**From:** Claude, RER co-owner (preparer). The preparer does not accept his own work.
**Status:** NONCANONICAL Phase A candidate, revision 8. Nothing is adopted, frozen or published.
**Answers:** the receiving decision on Phase B-05 (20 Oct 2026). The receiver authorized a narrow r8 with these conditions:
- show Dyadic v6.4.17 with the reported hash at `OWNER_REPORTED` level;
- add a negative control that rejects a `BYTE_VERIFIED` promotion without bytes;
- do not change the RER v6.4.13 scientific pins.

## 1. Base

- **RER draft:** the same r4.6 bytes (`2fa878ff…4772`); no Markdown change.
- **Base package:** Phase A r7 (`2a13e279…a4d3`).
- **Patch:** `patch_r8.py`, included at the package root. It makes exact-once text edits and edits catalog JSON by key. It was applied to a fresh copy of r7.

## 2. Dyadic currency

| Field | r7 | r8 |
|---|---|---|
| `owner_current.Dyadic.version` | 6.4.16 | **6.4.17** |
| `sha256` | `33c14c5c…59e0` | `e07cf2b9…4bfc` (stated in `claude/RTG_DYADIC_v6_4_17_RELEASE_RECORD.md`; not computed here) |
| `evidence` | HASH_VERIFIED_BY_RECEIVER | **OWNER_REPORTED** |
| `superseded` | — | v6.4.16 `33c14c5c…59e0`, HASH_VERIFIED_BY_RECEIVER (Phase A r3 review) |
| Frozen catalog `Dyadic` | 6.4.16 | 6.4.17; check date 2026-10-20 (Phase A r8); source authority = the v6.4.17 release record, with release verification by the reviewer pending |
| Watch item | v6.4.16 line | kept; a v6.4.17 line is added |

**The DYAD6413 pin is unchanged.** It keeps v6.4.13, `5958f7fe…8542`, `RECEIVER_BYTE_VERIFIED`, rule `UNCHANGED_OWNER_REPORTED` and status OWNER_REPORTED.

Its `currency_reason` gains one sentence. Byte equality of the cited §§6.15–6.17 between v6.4.16 and v6.4.17 is **not** checked here. It is to be checked once the v6.4.17 file is available.

**Matrix effect.** Exactly one row changes: RER-DYAD-FORMAL-INVOLUTION / DYAD6413. The changed fields are:
- `current_owner_version`: 6.4.16 → 6.4.17;
- `current_owner_sha256`;
- `current_owner_evidence`: HASH_VERIFIED_BY_RECEIVER → OWNER_REPORTED;
- `verified_current_hash`: `33c14c5c…` → none;
- `currency_reason`.

The registry JSON and the blocked register change only in `schema` (/7 → /8).

**Counts** are unchanged from r7:

| Measure | Count |
|---|---|
| VERIFIED | 30 |
| OWNER_REPORTED | 4 |
| HISTORICAL | 49 |
| BLOCKED | 6 |
| BYTE_VERIFIED_HERE | 58 |
| RECEIVER_BYTE_VERIFIED | 6 |
| HASH_PRINTED_UNVERIFIED | 24 |
| UNAUTHENTICATED_NO_HASH | 1 |

## 3. Gates: 23/23 PASS; negative controls 30/30 fail as required

**A19** now also rejects Dyadic v6.4.16 as current.

**A23 (new)** requires all of the following:
- Dyadic current is v6.4.17 with the release-record hash, evidence `OWNER_REPORTED`;
- no file with that hash is in `sources_available`;
- the superseded v6.4.16 entry is present with its receiver hash;
- every Dyadic row has no verified current hash, owner evidence `OWNER_REPORTED` and a non-CURRENT currency;
- DYAD6413 stays at v6.4.13, `5958f7fe…8542`, `RECEIVER_BYTE_VERIFIED`.

**Controls.** The 23 earlier controls are carried. Seven are new:

| Control | Must fail |
|---|---|
| Dyadic v6.4.16 claimed current | A19 |
| v6.4.17 promoted to `BYTE_VERIFIED` without bytes | A23 |
| v6.4.17 promoted to `BYTE_VERIFIED_HERE` | A23 |
| v6.4.17 promoted to `HASH_VERIFIED_BY_RECEIVER` | A23 |
| a Dyadic row given a verified current hash | A23 |
| DYAD6413 silently repinned to v6.4.17 | A23 |
| the superseded v6.4.16 record dropped | A23 |

**Regression.** The r7 outputs fail three gates under the r8 checker: A2 (rebuild), A19 and A23.

**Clean extraction.** The package was re-extracted into an empty directory and run with `python -I`: 23/23 gates PASS and 30/30 controls fail as required, with output byte-identical to the stored `check_phaseA_output.txt`.

## 4. Not changed

- RER r4.6 stays DRAFT. No scientific record, grade or OPEN status changes, and no pin moves.
- The six DYAD-FORMAL-INVOLUTION follow-up items from B-05 (O1–O5 and the RRF v0.8.3 carrier pin) are **not** applied. They are record-text corrections and belong to a separately authorized RER text revision.
- ER-2B stays blocked; G2 §5b stays `CARRIER_IDENTIFICATION_PENDING`; the 13 gap references keep `PENDING_PER_REFERENCE_AUDIT`.
