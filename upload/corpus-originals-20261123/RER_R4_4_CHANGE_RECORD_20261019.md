# RER v0.2 DRAFT r4.4: change record (pointer synchronization)

**Date:** 19 Oct 2026. **Preparer:** Claude, RER co-owner.
**Status:** NONCANONICAL. DRAFT, NOT ADOPTED, NOT FROZEN. The preparer does not accept his own draft.

## Identities

| Object | SHA-256 |
|---|---|
| Base r4.3 (receiving review ACCEPTED, 19 Oct) | `0dadf6e888ffc926b9c988dcd94021dc4832a873aec5406f1da0c199b885b159` |
| **DRAFT r4.4** | `5df4738685ecebf979da4f48d432ef2f9af01b6964dfefb62d7ac31887caa9d8` |
| `r4_3_to_r4_4_edits.json` (17 edits) / `make_r4_4_edits.py` | `3dbc9caf…` / `b7ceddce…` |
| `build_r4_4_draft.py` / `check_r4_4_draft.py` | `164988b9…` / `3b391356…` |
| diff (106 lines) / checker output | `9e123d19…` / `8407de12…` |
| New source in package: `sources/current/TRIAD_R4/RTG_TRIADIC_BIRTH_LIFT_DSN_v1_6_1.md` | `95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f` |

## Edits (17)

**Pointers only. No record, grade, contract table, G5/G6 status or earlier revision text changes.**

### Triadic v1.6.1, adopted 19 Oct (edits C1, S1, T1–T5)
- RER now cites v1.6.1 as its single Triadic source object, in the companion line, the RER-TRIAD-BIRTH-GRAPH-INVOLUTION import and the new source-table row `TRIAD161`.
- The v1.6 row and the two draft rows stay as history.
- D3 is CLOSED at the Triadic owner, both in the status summary and in the queue.

### RRF v0.8.3, 19 Oct (edits C1, R1–R4)
- RRF v0.8.3 now governs as the working standard, recorded with a new G10 r4.4 overlay and a new `RRF083` row.
- Its §2.4c correction, B-6 ⇔ B-an ∧ B-3, matches what RER already states.
- The v0.8.2 section citations are kept as exact pins.
- The v0.8.2 hash `f09dbb12…5461` is recorded as reported by the RRF adoption record. It is not byte-verified here.

### Dyadic v6.4.14, 19 Oct (edits C1, D1)
- Recorded as `DYAD6414`, OWNER-REPORTED. It adds OPEN 3 results only, and RER imports none of them.
- RER citations stay on v6.4.13, which the receiving co-owner has now byte-hashed.

### Metadata (edits M1–M3, H1, H2)
- Title, date, status, the §9 r4.4 entry and the release boundary.

## Gates: 21/21 PASS

| Gates | What they check |
|---|---|
| All 17 r4.3 gates (M1–M6, C1–C5, U1–U5, E2) | Carried over. U1 now requires the summary to name the adopted Triadic v1.6.1. |
| **P1** (new) | Triadic v1.6.1 is the cited source in the companion line, the import and the table, and the "Triadic v1.6 (adopted) and …" pair no longer appears. |
| **P2** (new) | RRF v0.8.3 governs. |
| **P3** (new) | Dyadic v6.4.14 is recorded but used in no `[import:]` tag. |
| **P4** (new) | The cited v1.6.1 file is present at the cited path with the cited hash. |

**Negative controls:**
- tampering U1, U2, U3, E2, U5, P1 and P3 each fails its gate;
- the r4.3 bytes fail P1–P3.

## Next

- A receiving review of this delta is requested.
- The way forward to adoption is set out in `RER_ADOPTION_PATH_PLAN_v0_1_20261019.md`. It needs PI decisions D-1 to D-4.
