# RER Phase A r5: change record

**Date:** 19 Oct 2026.
**From:** Claude, RER co-owner (preparer). The preparer does not accept his own work.
**Status:** NONCANONICAL Phase A candidate, revision 5. Nothing is adopted, frozen or published.
**Answers:** the receiving decision of 19 Oct 2026, which asked for "Phase A r5 first, then Phase B §6.3c": an OFN currency correction, limited to metadata and source currency.

## 1. Base

- **RER draft:** the same r4.6 bytes (`2fa878ff…4772`). No Markdown change and no record change.
- **Changed:** only the following:
  - the OFN entries in the source catalog;
  - the frozen-catalog input;
  - the two OFN rows of the currency matrix;
  - the watch items;
  - gates A19 and A21.

## 2. OFN currency

| Item | r4 | r5 |
|---|---|---|
| Current OFN | v0.9 `5ae8fdab…9795` | **v0.10** `acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa`, `OWNER_REPORTED` |
| Superseded | — | v0.9 `5ae8fdab…9795` (RECEIVER_BYTE_VERIFIED) |
| Hash authority | — | The hash is the one stated in the OFN v0.10 release record. It was not computed here, and the v0.10 bytes are not in this package. |
| RER pins | OFN9 (§8 lines 541–557, §12.4 lines 1186–1205), rule CURRENT | **Pins unchanged on v0.9; no repin.** The rule is now `RECHECK_IN_PHASE_B`, with a reason. |

The v0.10 version history says every v0.9 line outside the header block is preserved. Lines may still have been inserted, and the v0.10 bytes were not inspected. So r5 does not claim that §8 or §12.4 is unchanged; checking that belongs to Phase B.

**Effect on the matrix.** Only the two OFN9 rows (both RER-RRF-CND01) change: status goes from OWNER_REPORTED to HISTORICAL, and currency from CURRENT to RECHECK_IN_PHASE_B.

| Count | r4 | r5 |
|---|---|---|
| VERIFIED | 23 | 23 |
| OWNER_REPORTED | 8 | **6** |
| HISTORICAL | 51 | **53** |
| BLOCKED | 7 | 7 |

The authentication counts are unchanged. The two rows stay RECEIVER_BYTE_VERIFIED for the cited v0.9 bytes.

**Watch item added.** OFN v0.10 §11.4 imports IMP-O10-01 and IMP-O10-02 consume Genesis v2.8.9 §6.3c. Their status is `CONSUMER_CHECK_PENDING` (Phase B-01). It needs a direct reading of OFN v0.10.

**Second watch item.** RECOG v0.3.20 is recorded as the latest known version. Its own header reads freeze candidate, so the catalog does not record it as adopted or frozen.

## 3. Frozen catalog

`inputs/owner_versions_known.json` now records three things:

- `_catalog_checked: 2026-10-19 (Phase A r5, preparer)`;
- `_scope`: a frozen known-versions ledger. It is not live release discovery and not owner-adoption certification;
- `_source_authority`: the source of each owner's version (release record, receiver hash, owner header and so on).

The matrix mirrors these as `owner_catalog`, and the Markdown matrix prints them above the owner table.

## 4. Gates: 21/21 PASS

- **A19, extended.**
  - OFN must be current at v0.10.
  - The catalog date, scope and source authority must be present and must equal the input.
  - The scope must say "not live release discovery".
  - Every owner must have an authority entry.
- **A21, new.**
  - Owner-current evidence must use the catalog vocabulary.
  - `BYTE_VERIFIED` is allowed only when the bytes are in `sources_available` with the same hash.
  - OFN must be `OWNER_REPORTED` with the release-record hash, and v0.9 must be recorded as superseded.
  - No OFN row may carry a verified current hash or currency CURRENT.

## 5. Negative controls: 21/21 fail as required

The 16 controls from r4 are carried. Five are new:

| Gate | Control |
|---|---|
| A19 | OFN v0.9 claimed current |
| A19 | Catalog scope presented as live discovery |
| A21 | OFN v0.10's reported hash promoted to `BYTE_VERIFIED_HERE` |
| A21 | OFN v0.10 promoted to `BYTE_VERIFIED` without bytes |
| A21 | An OFN row given a verified current hash |

**Regression check.** The r4 outputs run through the r5 checker fail A2, A19 and A21.

## 6. Output differences from r4

- **Registry JSON and blocked register:** only the top-level `schema` changes (PHASEA/4 → /5).
- **Currency matrix:** `owner_current.OFN`, the new `owner_catalog`, the two OFN9 rows and the watch items.

## 7. Not in r5

- No reading of OFN v0.10 §8 or §12.4, and no section-equality claim.
- No check of IMP-O10-01/02. Both belong to Phase B-01.
- No Phase B disposition. ER-2B stays blocked. G6 stays OPEN.
