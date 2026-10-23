# RECOG — source recovery list

**Date:** 23 October 2026. **Prepared by:** Claude (atlas owner). **Status:** working record at a fixed path; updated when files arrive. **PI decision (23 Oct 2026):** record what is still missing as missing and continue.
**Scope:** every SHA-256 cited in `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` v0.3.22 (`0dcce9e4…bcd9`, tag `recog-v0.3.22`), full or short (`xxxxxxxx…yyyy`), checked against the repository tree, the members of every ZIP in it, every `dsn/` file at every tag, and the hand-over bundle kept in history.
**Tool and data:** `evidence/recog/inventory/build_recog_recovery_list.py` (run `python -I` from the repository root); output `evidence/recog/inventory/recog_recovery_inventory_v0_3_22.json`, one row per cited hash with its DSN lines and every place it was found.

**Goal.** Anyone can test a RECOG claim from the repository alone. A missing file does not mean the work was not done or the result is wrong. It means the evidence cannot be inspected from the repository.

## 1. Result

137 distinct hashes are cited (78 full, 59 short).

| State | Count | Meaning |
|---|---|---|
| in the tree | 92 | found under `records/recog/` or `evidence/recog/` (loose or as a ZIP member) |
| earlier RECOG editions, in history | 19 | found in `editions/` of the hand-over bundle; not placed in the tree (§3) |
| other owners' current files | 2 | OFN v0.10 and Genesis v2.8.9 in `dsn/` |
| not found | 24 | §2 (RECOG items) and §4 (other owners' earlier editions) |

The E2C stage-1 production run is complete. `e2c_production_certificate_v2.json` (`1d58749b…7c15`, PASS) lists 29 chunk files with full hashes, and all 29 match files in `evidence/recog/packages/e2c_prod.zip`. Two of them are in that ZIP's `failures/` folder: those chunks had tiles certified later by refinement (`e2c_refine_m2.jsonl`). The chunk hashes are not cited in the DSN itself, so they are not in the 137.

## 2. Missing RECOG records and evidence

| Cited item | Hash | DSN line | Note |
|---|---|---|---|
| `recog_cell_f2b_token_bridge.py` rev. 1 | `9c0b065523a6c90375a1ec51acdfeb1064e1617a052740d3e47bce0c3009e46a` | 1235 | superseded; rev. 2 (`a78de837…`) is present and is the one the certificate uses |
| `recog_cell_d_lattice_memory_cert.py` rev. 3 | `b92b9936…59cd` | 1229 | superseded; rev. 4 (`242b13e3…8b7f`) present |
| CELL-D comparator check rev. 2 | `5c678051…d3ad` | 1229 | superseded |
| v0.3.21 independent receiving review | `9a7ae8aa…31c45` | 52, 1331 | name unknown |
| NUMGEN C4 reply | `8a887ef3…bc4d` | 730, 1260 | name unknown; NUMGEN-side record |
| receiving review of the NUMGEN C4 reply | `e5a5fcec…fec1` | 1260 | name unknown |
| A1a cell draft v0.1 review | `02762139…f0e8b` | 1260 | name unknown; the drafts themselves are present (`records/recog/a1a/`) |
| A1a cell draft v0.2 review | `1b1c664e…7068a0` | 1260 | name unknown |
| A1a cell draft v0.3 review | `d9b20aea…7a5` | 1260 | name unknown |
| A1a session v0.3 review | `5ccf9098…f994` | 1260 | name unknown |
| Dyadic v6.4.17 release-verification report | `c0ef4446…1e39` | 1199 | Dyadic-side record; full hash in `records/dyad/DYAD_REPLY_TO_RECOG_G3_v0_1_2.md` |

No certificate on which a current RECOG theorem rests is in this list. The A1a draft reviews r1–r3 and the v0.4 release-readiness review are present (`records/recog/a1a/reviews/`).

## 3. Earlier RECOG editions

All earlier editions v0.1 … v0.3.21 and the v0.3.21/v0.3.22 drafts were handed over in `editions/` of `RECOG_HANDOVER_RECORDS_AND_EVIDENCE_20261023.zip` (`c20e1aa5…bd79`). Under the live-file rule older editions come from tags, not from copies in the tree, so they were not placed. Retrieve with
`git show f177eee:upload/recog-record-recovery/RECOG_HANDOVER_RECORDS_AND_EVIDENCE_20261023.zip > bundle.zip`.
Whether to tag them is the PI's decision.

One mismatch: the DSN cites v0.3.5 as `3ba74002…abd6`; the bundle's `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_5.md` is `9dd73601…6ab1`. It is a different version, not the cited one.

## 4. Other owners' earlier editions (pins, not RECOG evidence)

Cited as source pins; the governing copies belong to their owners' archives. Only Dyadic v6.4.19+ and NUMGEN v1.20.8 are tagged.

| Edition | Hash |
|---|---|
| Dyadic v6.4.10 | `7455811928606076b3bc3075…` (full in DSN line 1230) |
| Dyadic v6.4.16 | `33c14c5c…59e0` |
| Dyadic v6.4.17 | `e07cf2b9…4bfc` |
| Dyadic v6.4.18 | `f70308f19f5955c0597c03a2…` (full, line 742) |
| NUMGEN v1.20.7 | `c4637e7a5cfaf8eaf001746f…` (full, lines 917, 1140, 1160) |
| OFN v0.8 | `56bc991d28c4a6f3e841eec5…` (full, line 1160) |
| RRF v0.6 | `7a31357729e1561c600673cf…` (full, line 1123) |
| RRF v0.8.3 | `b393657e…a187` |
| Genesis v2.8.4 | `c145f5d2…cebd` |

## 5. Placement (commit on `claude/recog-records`)

| From the upload | To |
|---|---|
| bundle `records/` (release records, freeze provenance, G2 audits, memos, study plans, E3A-4 preregistration, outbound notices, post-release maintenance note, co-owner state review), `records/a1a/`, `records/g3/` | `records/recog/`, same subfolders |
| bundle `MANIFEST.md`, `SHA256SUMS.txt` | `records/recog/handover_20261023/` (paths there refer to the bundle layout) |
| bundle `evidence/scripts/`, `outputs/`, `packages/` | `evidence/recog/scripts/`, `outputs/`, `packages/` |
| loose uploads: three contributor scripts | `evidence/recog/scripts/` |
| loose uploads: `f2b_results_rev2.json`, `e3a1r31_summary.json`, `e3a1r31_late_cells.jsonl` | `evidence/recog/outputs/` |
| `e2c_prod.zip` (`4f171da6…b22d`, PI production run, as received) | `evidence/recog/packages/` |
| first co-owner self-review, received from the PI as `attachment.txt` | `records/recog/RECOG_OWNER_SELF_REVIEW_20261023.md` (`33a491d0…c845`, bytes unchanged) |

Dropped as exact duplicates: the loose copies of the two release records, the freeze provenance, the A1a-G1 disposition record and the state review (identical to the bundle copies); `RECOG_v0_3_22_RELEASE_RECORD (1).md`; `RECOG_ATLAS_INDEPENDENT_REVIEW.md` (identical to `records/recog/ATLAS_ADVISORY_RECOG_INDEPENDENT_REVIEW.md`). The bundle ZIP itself is kept in history only (§3). Bundle integrity before placement: `SHA256SUMS.txt` 174/174 OK.
