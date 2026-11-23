# RER Phase A r11: change record (Phase A pass on RER r4.8)

**Date:** 20 Oct 2026.
**From:** Claude, RER co-owner (preparer). The preparer does not accept his own work.
**Status:** NONCANONICAL Phase A candidate, revision 11. Nothing is adopted, frozen or published.
**Answers:** the receiving decision on RER r4.8 of 20 Oct 2026 (ACCEPT SCOPED; R10-F1 CLOSED), which authorized a Phase A run on the exact r4.8 bytes.

## 1. Source and base

- **Source Markdown:** RER v0.2 DRAFT r4.8 (`2dfebebf…0e3e`; package `26efafc9…4a9f`; base r4.7 `110729e5…cd1d`). It replaces r4.7 in the package.
- **Tooling base:** Phase A r10 (`bb27548f…270f`), extracted fresh. Builder, checker, parser (unchanged, `7b6b98aa…a7b7`) and catalog contents are carried. Only the `_about` notes and the catalog check date change.
- **Patch:** `patch_r11.py`, included at the package root.

## 2. Built from r4.8; r10 kept as history

- Every output in `out/` is regenerated from the r4.8 bytes.
- The five r10 output files and the r10 checker output are moved, byte-unchanged, to `inputs/phaseA_r10_outputs/` and pinned in `PINS.json` (A1). They are historical evidence; nothing in them is re-used as output.
- The r9 outputs stay under `inputs/phaseA_r9_outputs/`.
- The registry output is now `RER_REGISTRY_v0_2_r4_8_PHASEA.json`.
- The r4.8 package manifest is added; every row carries `path_in_r4_8_package`, and A6 checks it.

## 3. Result

**Matrix.** 90 rows (77 imports + 13 gap references). Every row equals r10 in identity, cited hash, bytes, authentication, currency, status, owner version and verified hash.

| Counts | Value |
|---|---|
| VERIFIED / OWNER_REPORTED / HISTORICAL / BLOCKED | 30 / 5 / 49 / 6 |
| BYTE_VERIFIED_HERE / RECEIVER_BYTE_VERIFIED / HASH_PRINTED_UNVERIFIED / UNAUTHENTICATED_NO_HASH | 58 / 7 / 24 / 1 |

**Registry.** The other 19 records equal r10. RER-DYAD-FORMAL-INVOLUTION differs from r10 in exactly four fields:

| Field | r10 (r4.7, historical) | r11 (r4.8) |
|---|---|---|
| `primary_grade` | `[THM] (owner grade). Owner grades per imported RID (r4.7): …` | `[THM] (owner grade)` (as in r9) |
| `grade_tags` | `['ALG', 'THM']` | `['THM']` (as in r9) |
| `primary_grade_line` | r4.7 line | the r4.6/r4.8 line |
| `unclassified_lines` | — | one added line: the r4.8 source note, carrying `DYAD-ALG-CENT-KERNEL` [ALG] and the other per-RID owner grades |

Exactness, task, adoption, contract, imports and OPEN items are unchanged.

**Blocked register.** Unchanged from r10 apart from its schema and source hash. It lists 3 sources; the byte-availability gap still includes RRF083.

## 4. Gates: 25/25 PASS; negative controls 44/44 fail as required

- **A24 (re-based on r4.8):** checks the r4.8 source, package and base hashes (r4.7 and r4.6); the matrix equals r9 plus the one RRF083 row; the registry equals r9 except the DYAD record's text. The DYAD record's grade must again parse as in r9.
- **A25 (new):** the 90 rows equal r10; the other 19 records equal r10; the DYAD record differs from r10 only in the four R10-F1 fields above. It also requires `grade_tags = ['THM']`, `primary_grade = '[THM] (owner grade)'`, exactly one new source-note line containing `DYAD-ALG-CENT-KERNEL` [ALG], and the r10 parse `['ALG', 'THM']` in the historical outputs.
- **Controls:** the 38 r10 output controls and the file-level control are carried; the r10 control "tags silently reset to [THM]" is replaced by "tags back to the r4.7 parse [ALG, THM]". Five A25 controls are new:
  - r10 registry re-used;
  - source note dropped;
  - CENT-KERNEL relabelled [THM];
  - one matrix row altered;
  - another record altered.
- **Clean extraction:** the package was re-extracted into an empty directory and run with `python -I`; the output is byte-identical to the stored `check_phaseA_output.txt`.

## 5. Not changed

- RER text: r4.8 stays a DRAFT accepted for review only. No grade, OPEN status or pin changes; DYAD6413 stays v6.4.13.
- ER-2B stays blocked; G2 §5b stays `CARRIER_IDENTIFICATION_PENDING`; the 13 gap references keep `PENDING_PER_REFERENCE_AUDIT`.
- The receiving review of the seven author-conflicted Phase B items is open.
