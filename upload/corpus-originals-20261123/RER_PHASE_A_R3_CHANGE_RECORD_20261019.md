# RER Phase A r3: change record

**Date:** 19 Oct 2026.
**From:** Claude, RER co-owner (preparer). The preparer does not accept his own work.
**Status:** NONCANONICAL Phase A candidate, revision 3. Nothing is adopted, frozen or published.

## 1. Base

- **RER draft:** r4.6 (`2fa878ff…4772`), from package `b2dfc9e2…4477`.
- **Change from r2:** only the base draft and the items below. The record set is the same (20 records, 4 gap entries, 16 legacy entries). The matrix has 89 rows: 76 imports and 13 gap references.

## 2. Changes

1. **Gap-reference paths (receiver data-quality finding).**
   - The receiver's crosswalk has `cited_path: null` in three rows (G8/1, G9/1–2).
   - The Phase A matrix already had all 13 paths. New gate A17 checks that every one is non-null and equals the link target of its reference line. The link target is found by a bracket-aware parse, because some link labels contain nested brackets.
   - Result: 13/13.
   - The crosswalk itself is the receiver's input and is not edited.
2. **Q7 custody in the blocked-source register.**
   - The coincidence response v0.2 and ER-2B v0.2 now carry `rrf_editor_sha256` and `source_custody: RRF_EDITOR_VERIFIED`. The values are parsed from the r4.6 missing-input lines.
   - The coincidence audit ZIP has no hash.
   - Gate A18 also checks that both ER-2B records stay blocked.
3. **Current Genesis.** The current owner version is now v2.8.9 (`d143673e…c6fc`, owner-reported from its release record). RER pins stay on v2.8.7. Whether the new §6.3c matters for GEN-K3-MODAL or G6 is a Phase B item; it is listed as a watch item.
4. **r4.6 package paths** are checked as well (A6, A13).

## 3. Gates

- 18/18 PASS.
- 14/14 negative controls fail as required. New controls: one gap path set to null (A17), and an editor hash given to the ZIP (A18).

## 4. Counts

| Measure | Counts |
|---|---|
| Status | VERIFIED 23, OWNER_REPORTED 8, HISTORICAL 51, BLOCKED 7 |
| Authentication | BYTE_VERIFIED_HERE 23, RECEIVER_BYTE_VERIFIED 6, HASH_PRINTED_UNVERIFIED 59, UNAUTHENTICATED_NO_HASH 1 |

These are the same as in r2.

## 5. Unchanged

- All 20 records are PENDING.
- ER-2B stays blocked.
- No repin.
- The A4 boundary is unchanged: literal and complete, but it does not reconstruct the order across fields and does not check meaning.
