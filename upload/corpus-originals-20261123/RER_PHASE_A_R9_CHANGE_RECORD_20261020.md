# RER Phase A r9: change record

**Date:** 20 Oct 2026.
**From:** Claude, RER co-owner (preparer). The preparer does not accept his own work.
**Status:** NONCANONICAL Phase A candidate, revision 9. Nothing is adopted, frozen or published.
**Answers:** the receiver's decision of 20 Oct 2026, taken after its independent run of the v6.4.16/v6.4.17 section check. The decision authorized r9 with four conditions:
- add the verified v6.4.17 bytes;
- raise the Dyadic evidence level;
- make A23 require the real file and the expected hash;
- keep pins, records, grades and OPEN statuses unchanged, and keep r8 as history.

## 1. Base

- **RER draft:** the same r4.6 bytes (`2fa878ff…4772`); no Markdown change.
- **Base package:** Phase A r8 (`37092f28…6b02`, accepted), extracted fresh from its zip.
- **Patch:** `patch_r9.py`, included at the package root. It makes exact-once text edits and edits catalog JSON by key.

## 2. Added files

| Path | SHA-256 | Note |
|---|---|---|
| `sources_available/DYAD617__RTG_DYADIC_OSCILLATOR_DSN_v6_4_17.md` | `e07cf2b9…4bfc` | PI upload, 20 Oct 2026; equals the release-record hash; the receiver confirmed the same hash independently |
| `inputs/source_custody_r9.json` | (in `PINS.json`) | Custody entry, key `DYAD617`. The container chain is preparer-declared. Records both section-check packages: `56e772ad…8ca9` (receiver-run) and `6e512651…29a1` (preparer; not uploaded to the receiver) |
| `inputs/dyad_v6_4_17_section_check/` | (in `PINS.json`) | The checker `381e6160…4057` and its three outputs: compare (PASS, 5/5 IDENTICAL), negative control, single-file run |

The v6.4.16 file is not added. Its hash identity was already receiver-verified (Phase A r3), and the compare output records it as MATCH.

## 3. Catalog changes

| Field | r8 | r9 |
|---|---|---|
| `owner_current.Dyadic.evidence` | OWNER_REPORTED | **BYTE_VERIFIED** |
| `owner_current.Dyadic.history.phaseA_r8` | — | the r8 evidence and note, verbatim |
| `owner_current.Dyadic` version / sha256 / superseded | 6.4.17 / `e07cf2b9…` / v6.4.16 `33c14c5c…` | unchanged |
| Frozen catalog check date and Dyadic source authority | r8 | r9 (byte-verified here; receiver-confirmed hash) |
| `DYAD6413` rule / cited version / cited hash | UNCHANGED_OWNER_REPORTED / 6.4.13 / `5958f7fe…8542` | unchanged |
| `DYAD6413` reason | r8 text | r8 text plus one sentence on the section check (5/5 IDENTICAL) |
| Watch items | r8 lines | kept; one r9 line added |

**Matrix effect.** Exactly one row changes: RER-DYAD-FORMAL-INVOLUTION / DYAD6413. The changed fields are:
- `current_owner_evidence`: OWNER_REPORTED → BYTE_VERIFIED;
- `verified_current_hash`: none → `e07cf2b9…`;
- `currency_reason`.

Status stays OWNER_REPORTED, because the cited v6.4.13 bytes are not held here and the rule label is kept. The registry JSON and the blocked register change only in `schema` (/8 → /9).

**Counts:** unchanged — VERIFIED 30, OWNER_REPORTED 4, HISTORICAL 49, BLOCKED 6; BYTE_VERIFIED_HERE 58, RECEIVER_BYTE_VERIFIED 6, HASH_PRINTED_UNVERIFIED 24, UNAUTHENTICATED_NO_HASH 1.

## 4. Gates: 23/23 PASS; negative controls 32/32 fail as required

**A23 now requires all of the following:**
- evidence is BYTE_VERIFIED;
- a file with hash `e07cf2b9…` is present in `sources_available`;
- the custody entry for that file matches (key `DYAD617`, hash);
- the section-check output shows both file hashes as MATCH, "RESULT: PASS", 5 IDENTICAL and no DIFFERENT;
- the r8 OWNER_REPORTED state is kept under `history`;
- the superseded v6.4.16 entry is present;
- every Dyadic row carries the v6.4.17 hash as its verified current hash;
- DYAD6413 stays at v6.4.13, `5958f7fe…8542`, RECEIVER_BYTE_VERIFIED.

**Controls.** Four r8 A23 controls tested promotions that are now the correct state, so they are replaced. The remaining 26 earlier controls are carried. Five output controls are new:

| Control | Must fail |
|---|---|
| evidence back to OWNER_REPORTED | A23 |
| evidence relabelled BYTE_VERIFIED_HERE | A23 |
| BYTE_VERIFIED with a hash no held file has | A23 |
| Dyadic row's verified hash removed | A23 |
| r8 history dropped | A23 |

**File-level control (new).** The checker is re-run with the v6.4.17 file withheld from `sources_available`, and A23 must fail.

**Regression.** The r8 outputs fail three gates under the r9 checker: A2, A19 (check date) and A23.

**Clean extraction.** The package was re-extracted into an empty directory and run with `python -I`: 23/23 gates PASS and 32/32 controls fail as required, with output byte-identical to the stored `check_phaseA_output.txt`.

## 5. Not changed

- RER r4.6 stays DRAFT: no scientific record, grade, OPEN status or pin changes.
- The Phase A r8 package stays the accepted r8 record.
- The six B-05 record-text items are handled separately in RER r4.7 DRAFT.
- ER-2B stays blocked; G2 §5b stays `CARRIER_IDENTIFICATION_PENDING`; the 13 gap references keep `PENDING_PER_REFERENCE_AUDIT`.
