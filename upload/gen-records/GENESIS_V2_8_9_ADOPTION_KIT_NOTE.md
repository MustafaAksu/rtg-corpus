# Genesis v2.8.9 — Adoption Kit (metadata-only release transform)

**Date:** 19 October 2026
**Status:** `[SESSION]` adoption preparation, following the independent receiving review of 19 Oct 2026 ("accepted for adoption preparation; no scientific r2 revision").
- **Nothing is adopted.** Adopted owner remains v2.8.8 (`9abd3616…0f37`).

## 1. Frozen input

| Object | SHA-256 |
|---|---|
| Reviewed DRAFT `RTG_GENESIS_GEOMETRY_DSN_v2_8_9_DRAFT.md` (1645 lines) | `b2cc5c5cb637459b3e2aded30b1c48ad859f2591a93684f463f89fbab503f62a` |
| Reviewed package `GENESIS_V2_8_9_DRAFT_PACKAGE.zip` | `a3ceb92e66d7cd2caf4d96d5e65f6d17607b5b7e50f2f88a6f0582335573e973` |
| Certificate `d4_transported_cubic_cert.py` | `f4c382855b130249ce290d3ca939b283aadd27d6ea9a1af551599f4cd9533f6d` |

`release_v2_8_9.py` refuses any draft with a different hash.

## 2. Transform: 7 metadata edits

| ID | Change |
|---|---|
| R-title | `v2.8.9_DRAFT` → `v2.8.9` |
| R-date | the date and status line become the adopted form: "ADOPTED owner ledger — scientific release (D-4 …)". "(draft)" and "Not adopted" are removed. |
| R-supersedes | "(on adoption)" is removed |
| R-summary | the opening of the status summary names v2.8.9 as an adopted release on the v2.8.8 base |
| R-p11 | "v2.8.9 draft addition" → "v2.8.9 addition" |
| R-appA | the adopted Appendix A heading and **Adoption** paragraph; the DRAFT record is kept below it as history |
| R-foot | the adopted footer |

**Content of the Adoption paragraph**
- the owner decision text and the date;
- the draft and package hashes, the receiving-review results (11/11 `--final --cert`, certificate 6/6, 12/12 SHA256SUMS);
- **the negative-control replay limitation, as the owner required**: the package record shows 8/8; the reviewer's full replay did not complete within the time limit; this is an execution-coverage limitation with no observed failure;
- the in-force RID and its hypotheses;
- that the primitive companion stays an algebraic statement without RID;
- that no v2.8.8 claim changed and the Dyadic pins remain v6.4.13.

## 3. Release checker R1–R8 (`check_release_v2_8_9.py`)

| Gate | Check |
|---|---|
| R1 | reviewed draft hash |
| R2 | output body equals the 7-edit transform of the draft; every anchor is unique |
| R3 | the reverse transform recovers the draft byte-exactly |
| R4 | claim-tag counts are identical |
| R5 | every changed live line is a version, status or metadata line |
| R6 | no draft, not-adopted or on-adoption marker remains in live text |
| R7 | RID set unchanged, including the new RID; **§6.3a–§6.3c byte-identical**; certificate pin intact; the Gröbner line still reads NOT REPLAYED |
| R8 | real decision text and date for a release, or the placeholder inside a preview; the negative-control replay limitation is recorded |

**Results in this workspace**
- The preview (`[PENDING OWNER DECISION]`, date 19 October 2026) gives **8/8 PASS**, exit 0. The release bytes under that placeholder have SHA `d412a153…62c9`. The real release hash will differ, because it depends on the owner's decision text.
- **Controls:**
  - a non-preview run with placeholder text is refused (AssertionError);
  - a preview tampered inside §6.3c (μ/3 → μ/6) gives exit 1, with R2, R3, R5 and R7 failing.

## 4. Supplementary fast negative-control replay

The reviewer's full replay of `negative_controls_v2_8_9.py` hit the execution time limit. The cause was the certificate rerun (about 30 s each) inside every control.

`negative_controls_v2_8_9_fast.py` (`dc882360…7f22`) runs the **same eight controls with the same expected gates**. The only difference: NC1–NC7 run the checker without `--cert`, since M6 is not among their expected gates, and NC8 keeps `--cert --final`.

**Result:** 8/8 caught in under 1 s. The output (`negative_controls_fast_output.txt`) is byte-identical to the recorded output of the original script (`0116d7e8…fc92`). The frozen original script and the draft package are unchanged.

If the reviewer completes this replay before the adoption decision, the owner may replace the limitation sentence in the Adoption paragraph. That needs one kit edit and a rerun of R1–R8.

## 5. Owner commands (after the decision)

```
python release_v2_8_9.py RTG_GENESIS_GEOMETRY_DSN_v2_8_9_DRAFT.md RTG_GENESIS_GEOMETRY_DSN_v2_8_9.md --date "<D Month YYYY>" --decision "<decision text, no trailing period>"
python check_release_v2_8_9.py RTG_GENESIS_GEOMETRY_DSN_v2_8_9_DRAFT.md RTG_GENESIS_GEOMETRY_DSN_v2_8_9.md --date "<same>" --decision "<same>"
```

v2.8.9 counts as adopted only after R1–R8 PASS on the real bytes. Notices then cite the real SHA:
- OFN: informational; the Q6 regularity remains OFN's decision.
- RRF and FMS: informational.

Until then, v2.8.8 stays in force.
