# RER Phase A r10: change record (first Phase A pass on RER r4.7)

**Date:** 20 Oct 2026.
**From:** Claude, RER co-owner (preparer). The preparer does not accept his own work.
**Status:** NONCANONICAL Phase A candidate, revision 10. Nothing is adopted, frozen or published.
**Answers:** the receiving decision of 20 Oct 2026 (Phase A r9 and RER r4.7 both ACCEPT SCOPED). The decision asked for a fresh Phase A built from the exact r4.7 bytes, with the new RRF083 reference in the matrix, and not layered over r9.

## 1. Source and base

- **Source Markdown:** RER v0.2 DRAFT r4.7 (`110729e5…cd1d`; package `9ab6393e…c14f`; base r4.6 `2fa878ff…4772`). This replaces r4.6 in the package; the r4.6 file is no longer included.
- **Tooling base:** Phase A r9 (`71ccc7e9…e9ae`), extracted fresh. The builder, checker, parser and catalogs are carried.
- **Patch:** `patch_r10.py`, included at the package root.

## 2. Built from r4.7, not layered over r9

- Every output in `out/` is regenerated from the r4.7 bytes by `build_phaseA.py`.
- The r9 matrix and registry are moved to `inputs/phaseA_r9_outputs/` and pinned in `PINS.json`. They are used only for the A24 regression comparison, never as output.
- The registry output is renamed to `RER_REGISTRY_v0_2_r4_7_PHASEA.json`.
- The r4.7 package manifest is added as `inputs/r4_7_package_SHA256SUMS.txt`. Every row carries `path_in_r4_7_package`, and A6 checks it.
- The r9 blocked register is not carried; it is regenerated. It still lists the same 3 blocked sources; besides its schema and source hash, the only change is that the byte-availability gap list gains `RRF083` (bytes not held by the preparer).

## 3. Catalog

| Change | Detail |
|---|---|
| New key `RRF083` | Cited v0.8.3; family OWNER_DSN; owner RRF; rule CURRENT. Receiver-reported byte verification on the receiving side, as stated in the r4.7 decision. The preparer does not hold the bytes. |
| Record catalog | Classification unchanged; one sentence added to `_about`. |
| Frozen catalog | Check date set to r10. Versions unchanged; Dyadic stays v6.4.17 BYTE_VERIFIED (r9). |

## 4. Result

| Measure | r9 (on r4.6) | r10 (on r4.7) |
|---|---|---|
| Rows | 89 (76 imports + 13 gap references) | **90** (77 imports + 13 gap references) |
| VERIFIED / OWNER_REPORTED / HISTORICAL / BLOCKED | 30 / 4 / 49 / 6 | 30 / **5** / 49 / 6 |
| BYTE_VERIFIED_HERE / RECEIVER_BYTE_VERIFIED / HASH_PRINTED_UNVERIFIED / UNAUTHENTICATED_NO_HASH | 58 / 6 / 24 / 1 | 58 / **7** / 24 / 1 |

**The one added row** is RER-DYAD-FORMAL-INVOLUTION / RECORD_IMPORT / n = 2 / `RRF083`:

| Field | Value |
|---|---|
| Cited version | 0.8.3 |
| Cited hash | `b393657e…a187`, equal to the current owner hash |
| Currency | CURRENT |
| Bytes | PRINTED_ONLY |
| Authentication | RECEIVER_BYTE_VERIFIED |
| Status | OWNER_REPORTED |

All other 89 rows are identical to r9 in identity, cited hash, bytes, authentication, currency, status, owner version and verified hash.

**Registry.** The other 19 records are identical to r9. RER-DYAD-FORMAL-INVOLUTION differs only in its text fields; its exactness, task, adoption and OPEN items are unchanged, and it gains one import.

## 5. Finding R10-F1 (recorded, not repaired)

**What happens.** The pinned parser (`tools/rer_parse.py`) reads the primary grade up to `. **Exactness`. In r4.7 the O3 per-RID owner grades are appended to the same line. The parsed fields therefore change:

| Field | r9 | r10 |
|---|---|---|
| `primary_grade` | `[THM] (owner grade)` | `[THM] (owner grade). Owner grades per imported RID (r4.7): …` |
| `grade_tags` | `['THM']` | `['ALG', 'THM']` |

**How it compares.** This has the same shape as RER-GEN-K3-MODAL ("[THM] (owner import) with an [ALG] transport step", whose `grade_tags` are `['ALG', 'THM']`). It is also close to the reading caution in the receiving decision: the record-level summary should not be read as covering every imported line.

**What I did not do.** I did not change the parser and did not reset the field. A24 records the parsed values exactly, and a control fails if `grade_tags` is silently reset to `['THM']`.

**Options for the receiver:**
- (a) accept the parsed tags as the GEN-K3-MODAL convention;
- (b) a one-edit r4.8 that moves the per-RID grade sentence to its own line below the grade line. That would restore `grade_tags = ['THM']` without any parser change.

## 6. Gates: 24/24 PASS; negative controls 39/39 fail as required

**A24 (new) requires all of the following:**
- the source, package and base hashes are recorded;
- the matrix equals the pinned r9 matrix plus exactly the one RRF083 row described above;
- every row carries `path_in_r4_7_package`;
- the registry equals r9 for the other 19 records;
- for RER-DYAD-FORMAL-INVOLUTION, only the text and import fields change, with the R10-F1 parse recorded exactly.

**Controls.** The 31 r9 output controls and the file-level control are carried. Seven A24 controls are new; each must fail A24:
- r9 matrix rows re-used;
- RRF083 row dropped;
- RRF083 promoted to BYTE_VERIFIED_HERE;
- source recorded as r4.6;
- another record silently changed;
- DYAD primary grade changed;
- `grade_tags` silently reset.

**Clean extraction.** The package was re-extracted into an empty directory and run with `python -I`: output byte-identical to the stored `check_phaseA_output.txt`.

## 7. Not changed

- No RER text change; r4.7 stays a DRAFT accepted for review only.
- No scientific record, grade, OPEN status or pin changes; DYAD6413 stays v6.4.13.
- ER-2B stays blocked; G2 §5b stays `CARRIER_IDENTIFICATION_PENDING`; the 13 gap references keep `PENDING_PER_REFERENCE_AUDIT`.
- The receiving review of the seven author-conflicted Phase B items is open.
