# RECOG hand-over bundle — files held in the RECOG co-owner session (Claude)

**Date:** 23 October 2026 · **From:** RECOG co-owner (Claude) · **For:** the PI, to be uploaded unchanged to an `upload/recog-records` branch (CONVENTIONS §6). This session has read-only repository access.
**Integrity:** `SHA256SUMS.txt` lists every file in this bundle. Every file is byte-identical to the copy in the session workspace where it was produced or received. Nothing has been reconstructed or edited for this hand-over.

## Layout (suggested placement; the PI and the placement commit decide)

| Bundle folder | Contents | Suggested destination |
|---|---|---|
| `records/` | release records v0.3.22 and v0.3.21; v0.3.20 freeze provenance; G2 claim audits and source-fidelity runs; memos; study plans; E3A-4 preregistration; v0.3.22 outbound notices; v0.3.22 post-release maintenance note | `records/recog/` |
| `records/g3/` | G3 notices (draft and final) and dispatch records r1–r3 | `records/recog/` |
| `records/a1a/` | A1a session records v0.1–v0.3; cell drafts v0.1–v0.4; C4 questions and receipt; E2 source check; G1 request, NUMGEN replies v0.1 and v0.1.1, receipt, disposition and addendum; reviews received (v0.4 readiness, r1, r2, r3) | `records/recog/` |
| `evidence/scripts/` | certificate and check scripts cited in RECOG §8; build, check and release tooling for v0.3.21 and v0.3.22; G2 diff scripts; G3 finalizer | `evidence/recog/scripts/` |
| `evidence/outputs/` | certificate outputs (JSON/JSONL), checker outputs, edit lists, r1→r2→r3→release diffs, G2 comparison reports | `evidence/recog/<version>/` or `evidence/recog/outputs/` |
| `evidence/packages/` | frozen packages as produced: E2C production bundle, E2C refinement and gate v2, v0.3.22 DRAFT r1/r2/r3 review packages, v0.3.22 release-verification package | `evidence/recog/` (kept as received) |
| `editions/` | earlier RECOG editions v0.1 … v0.3.21, and drafts of v0.3.21 (r1, r2) and v0.3.22 (r1, r2, r3) | PI archive. Not for `dsn/`, since older editions belong to tags. Whether to tag old editions is the PI's decision. |

## Coverage against RECOG v0.3.22

- **Full SHA-256 values cited in the DSN:** 78 in total.
  - 62 match a loose file in this bundle.
  - 4 are members of `evidence/packages/RECOG_E2C_refinement_and_gate_v2.zip`: `e2c_refine_driver.py`, `e2c_production_gate_v2.py`, `e2c_refine_m2.jsonl`, `e2c_production_certificate_v2.json`. They match by hash inside the zip.
  - 5 are owner DSN editions, not RECOG artifacts: OFN v0.8, NUMGEN v1.20.7, Dyadic v6.4.10, Dyadic v6.4.18, RRF v0.6.
- **Short hashes (`xxxxxxxx…yyyy`):** 52 cited, 34 present. The remaining 18 are owner DSNs, owner release reports, or reviews that were never handed into this session.
- **Cited in §8 but not held by this session** (to be supplied by the PI or the contributor, or recorded as missing):
  - contributor scripts:
    - `recog_cell_a_p5_rawcomp_cert.py` (`0a87d59d…4f84383`)
    - `recog_cell_b_p2_manifolds.py` (`7ea5e161…b10216e`)
    - `recog_cell_c_lattice_readability_cert.py` (`73a919e2…1476083`)
  - PI production outputs:
    - `f2b_results_rev2.json` (`07082c4c…`)
    - the F2(b) rev. 1 script (`9c0b0655…`)
    - `e3a1r31_summary.json` (`40b0f170…`)
    - `e3a1r31_late_cells.jsonl` (`0a59d01e…`)
    - the E2C production chunks 32768–131071 run on the PI machine
  - reviews not handed in:
    - v0.3.21 receiving review `9a7ae8aa…31c45`
    - A1a cell v0.1 review `02762139…f0e8b`, v0.2 review `1b1c664e…7068a0`, v0.3 review `d9b20aea…7a5`
    - A1a session v0.3 review `5ccf9098…f994`
    - NUMGEN C4 reply `8a887ef3…bc4d` and its receiving review `e5a5fcec…fec1`
    - Dyadic release-verification reports `c0ef4446…1e39` and `473b6aaa…`
- **Duplicate:** `records/a1a/reviews/` contains the r3 delta review once, under its clean name. The upload copy with a prefix (`93a69179-…`) has the identical hash and is not included.
