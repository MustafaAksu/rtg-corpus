# RRF S0 — source custody and readiness

**Date:** 26 November 2026.
**Status:** [SESSION] / NONCANONICAL; proposed placement and orientation for independent review. ChatGPT prepares; Claude independently reviews; PI decides scope, source status, adoption and publication. S0 is not accepted until review of the exact PR head; S1 and BR-Q2 remain held.
**Source checkpoint:** `43dabc5818b2dccba31030116e4ecd80570e7e35`. Atlas advisory PR #395 at `73dd0cf88d3e89063f1eff1de911255c26313489`; independent RRF reviewer PR #396 at `fcaaeac133ab2b663972999756feff5b8487724b` (record §3 F1–F7, §4 A1–A8). Review #396 is an unmerged SESSION input, not a new RRF acceptance. This PR does not merge either advisory/review branch.
**Governance:** CONVENTIONS §§1–9; Methodology v1.4; Programme v1.5. No canonical DSN, BASELINE, tag, upload file, existing pipe state, or science changed. No LIT dependency.

## 1. Governing identity (A1)

The only RRF tag is the annotated `rrf-v0.8.4`, object `cb8f7caf6ac4c3772fe3d4390b667e8d1bbed474` → commit `d7d661c0b89c6f3d9ceea2e205bf75fccfcfbf8d`, blob `6882fd517e548e5d6a9aecad9c958af74fe447dc`, 108,615 bytes, SHA-256 `2fb0a0fe9d998be91618cb731e2dee7301952ffdbe374f4889dd5e61c5cbafce`. The tag and release record agree with BASELINE; tagged file and upload copy share that blob and digest. The adopted scope remains **working representation standard only**. RRF declares Methodology v1.3; migration is S2, not this PR. Methodology v1.4 and Programme v1.5 annotated identities and SHA-256 are independently checked and in the manifest.

## 2. Placement and provenance (A2–A4, A8)

Exact source/destination paths, full SHA-256, byte counts, blob identities and custody type: `evidence/rrf/s0/custody_manifest.json`. Fifteen originals (13 loose including the cited historical parent and the misnamed candidate, two extracted ZIP members) and two regenerated diffs; no historical text edited, no upload removed. Other sources remain in existing upload custody and are referenced rather than duplicated. The v0.8.2 record and G2 v0.3 final are extracted from the *adopted* package, not the review candidate package. Their SHA-256 and sizes independently checked by the preparer using base64-decoded GitHub bytes and ZIP member extraction. G2 v0.2.1/v0.4 are exact recovered interface notes, not scientific owner adoption.

The six original adoption records are read in full; their authorization wording is preserved in the originals. Exact authorization excerpts (formatting only omitted below):
- v0.7 §1: "The current user message supplies the reviewer's adoption-ready assessment, explicitly accepts the existing scientific scope, and recommends finalizing v0.7 after three small editorial notes with a separate adoption record." Also: "The review recommendation is recorded as a review recommendation, not as an invented separate PI signature or an independent owner vote."
- v0.8 header: "User's October 14 adopted-base candidate review: adoption-ready; three non-blocking editorial corrections recommended". §1: "This record does **not** claim a separate PI signature, upstream owner adoption of conditional studies, successful scientific certificate reproduction or downstream consumer synchronization."
- v0.8.1 header: "User's 16 October 2026 adopted-v0.8 diff and provenance review: revised v0.8.1 candidate **fit for adoption**, subject to release-header correction; optional §8 G1 disclaimer accepted as non-substantive". Record type explicitly not Programme/PI adoption.
- v0.8.2 header: "Reviewer confirms v0.8.2 and G2 v0.3 are fit for scoped acceptance subject to four provenance/internal-consistency corrections."
- v0.8.3 header: "Reviewer examined exact source identities/diffs and approved v0.8.3 subject to one §2.4c clarification; accepted G2 v0.4 without scientific-content changes."
- v0.8.4 Approval and scope: "The reviewer explicitly authorized adoption as-is; two optional suggestions do not block adoption." Decision line: "ADOPTED, 20 October 2026, only as the RRF working representation standard."
No additional historical PI signature, new consent or scientific grade is inferred. The v0.8.4 record retains its original name. BASELINE provenance update is deliberately left to PI decision.

**37/37 digest links:** intake `evidence/atlas/intake/corpus_originals_20261123/rrf_adoption_record_digests.csv` reports 35/37; PR #396's independent native archive scan (13,013 objects incl. 9,234 archive members, zero read errors) and difflib regeneration report 37/37. This is a digest-to-object link count, not 37 approval authentications. The preparer did not repeat the 9,234-member scan. Instead the two missing diffs are independently regenerated using a JavaScript implementation of the sequence matcher/unified-diff algorithm on the exact base, candidate and adopted UTF-8 bytes; SHA-256 self-test passed; control output matches the archived Review diff A digest, 36,647 bytes `e4b666fadd181551428b1407c6df2edd45f583887c8ae2d8be378a83ef433385`; both target sizes and digests match the adoption record. Perturbing the first v0.8.4 string changes the second target digest to `aa4887acbb5fefa7315dc517f2303bdccb6258d595b5128b880e2234944fe4aa`. These two objects are explicitly **regenerated, digest-verified**, not recovered original custody. The reviewer script `evidence/rrf/scripts/rrf_s0_regenerate_v084_diffs.py` at #396 head is the independent Python route, not imported into this PR. The new read-only verifier checks the archived control and both regenerated targets against the manifest.

**Misnamed originals (intake §4.1):**
- `build_r4_7_draft.py` → `RRF_EDITOR_RESPONSE_TO_RER_PHASEA_v0_2_20261019.md`, SHA-256 `413a869b49a295652af1379510fbece2d10619daffd5874c1320e1d686113084`; handoff §1 and original heading confirm. Never executed as Python; preserved as a dated editor response against v0.8.3, not RER acceptance.
- `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4_CANDIDATE.md` → `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4_REVISED_REVIEW_CANDIDATE.md`, SHA-256 `fc53acff20c17e152884bc1835d4de2d4354a406f4d63262cdb04c200e2cab9e`; evidence, not the adopted registry.
- `DYAD_CHECK_degree10_even_term_hatF.md` (intake original browser name `DYAD_CHECK_degree10_even_term_hatF281%29.md`), SHA-256 `dcfd808c0270202768b4422acb474cda08f693a1cf69e8ec368e7faac414f4d4`, 2,827 bytes. Verified by preparer; retained in upload under DYAD custody rather than creating a competing RRF evidence original. VF-1 remains scoped to fixed h6. No new certificate replay.
- SH-R0 note: `87a67a90452ec980254b415c28fdf472402bc6d0ef21b47ff12671bf70f087bf`; reviewer reports co-membership with v0.8.3 adopted release, not a digest citation by its adoption record. Remains SESSION.
- The RER closure proposal is present at exact published digest, nonnormative. The historical coincidence/admissibility/ER2B sources remain in upload custody (intake §3 rows 3.7–3.9, B1 response Q7). Source availability does not establish the RER records' acceptance or reproduce the original ER2B audit.

## 3. PRR and GIIL (A5–A6)

| Object | Source identity and status |
|---|---|
| PRR Wrap-up v0.2 | 49,059 bytes; SHA-256 `88274f70449027d0a27231e950819e7b3d2c3432de4471451486288cffd9e2f2`; historical NONCANONICAL parent preserved as instructed by PI in RRF activation; exact original in records/rrf/. PRR v0.3 Appendix B S00 prints that digest. This is a noncanonical cross-reference, not an adoption. |
| PRR Wrap-up v0.3 | `upload/corpus-originals-20261123/RTG_PRIMORDIAL_RELATIONAL_REPRESENTATION_WRAPUP_v0_3.md`, 101,038 bytes; `68d45d379f7944808db017b0f2ac57951db8190a66c0f5c728845210b6bfa40c`. Noncanonical synchronization draft; no RRF adoption or drop-in parent replacement. GIIL v0.19 cites it; separate future evaluation and PI source-status decision. Left at original upload path. |
| GIIL v0.19 DRAFT | `upload/corpus-originals-20261123/RTG_GENESIS_IDENTIFICATION_INHERITANCE_LEDGER_v0_19_DRAFT.md`, 198,306 bytes, `f6320914190b434332058b69fe0974ce584d1a8167ae40e2650091be5bdbe2f8`. Historical noncanonical working draft, GEN v2.8.4 baseline, PRR v0.3 and RRF v0.6 references. Identity corroborated by Genesis owner-pass queue v0.4 §0 and RER 17 Oct candidate table. Tagged RER v0.2 GIIL019 prints `f6320914…0be8`; reviewer found no matching object. Plausible transcription error, not a concluded correction. No RRF inheritance registration. |

PRR v0.2 locator check (targeted source read, confirmed independently by reviewer #396 F5): §10.2 typed covariance; §11 comparator transport; §14.1 proposed GIIL; §19 chart cycle constraint (explicit h(z_AB)+h(z_BC)+h(z_CA)=0, not a claim that §19 is itself the safety lock); §§20 and 26 profile and next-programme parent pointers. All six locators exist at the intended topics. v0.3 renumbers; retain O1's exact topic. No scientific derivation audited here.

GEN question and RER finding are proposed pipe filings in this PR, not transmission/receipt, acceptance, adoption or an edit to another owner's DSN. GEN decides source/inheritance status; RER decides its short-hash discrepancy. PI retains any broader PRR v0.3 decision.

## 4. Missing or not independently verified (A7)

| Item | Constraint |
|---|---|
| RTG_RRF_v0_8_ADOPTION_QA_MANIFEST.json | Not found in #396 scan; v0.8 record prints no digest. Recovered QA Markdown reports 23/23 but is not the named JSON. No assertion of original manifest identity. |
| PRR_RRF_REVIEW_v1.zip | Not found in #396 scan including nested archives. Third-reviewer artifact identity in RRF §2.4a unavailable. |
| Original v0.8.4 publication diff files | Not located as original objects; regenerated content equals their recorded digests. No original custody inferred. |
| RRF §10 historical scientific rerun gaps (R11/R9/R8/B3/twin/F2/P2-B/degree-ten package, standalone Lemma F; Q7 original ER2B audit) | Not reassessed as proof packages in this S0 placement pass. Some availability has changed in intake; no assertion that all remain missing, no new execution/certificate authentication. Keep owner scope and historical evidence limits; verify only for affected S1/BR-Q2 use. |

Missing or unexamined historical evidence constrains the corresponding assertion only; it does not invalidate an independently established owner theorem or license a missing proof. No historical approval reconstructed.

## 5. S0 check and independent review

`python -I evidence/rrf/scripts/check_s0_custody.py .` independently recomputes every placement's SHA-256, checks exact source bytes or archive member, reconstructs both regenerated diffs, checks control/negative control, verifies tag objects, governing bytes and protected paths. The preparer used connector-side base64 SHA-256 and ZIP extraction and independent diff regeneration; native checkout is unavailable in this session, so no native full script or pipes-index CI run is claimed. Connector index generation for GEN/RER reads their actual 16 and 2 item bodies; the renderer reproduces both existing indexes before adding the new items. The repository checker should verify all pipes on the exact head. PR review must examine readback and A1–A8, including the orientation structure; #396 and #395 remain separate lanes. No S1 science or BR-Q2 work authorized by these checks.
