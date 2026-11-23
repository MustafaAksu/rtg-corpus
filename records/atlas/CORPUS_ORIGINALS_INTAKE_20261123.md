# Corpus originals — intake check of `upload/corpus-originals-20261123/`

**Date:** 23 November 2026. **By:** Claude, Atlas owner.
**Status:** [SESSION] intake record, **revision 2** after review `6021632408` (§7). It verifies transfer integrity and reports a census against an extracted list. It adopts nothing, authenticates no old approval, places no file in a stream's folder and changes no DSN, pipe or Atlas byte. What each stream uses is its owner's decision (CONVENTIONS §7).
**Asked by the PI** (project conversation, 23 Nov 2026, 12:30 and 15:03 +03:00): one search script for all files the corpus cites and does not hold, into one upload folder; then a check of what arrived.
**Object:** `upload/corpus-originals-20261123/` on `main` `561bb39b76bff9a28a715f5853a504c22e5e3ca7`: 535 files (529 source files and six report files), 111 MB. The folder is not touched by this record.
**Check:** `python3 -I evidence/atlas/intake/corpus_originals_20261123/intake_check.py`. Outputs next to it: `intake_result.csv` (one row per wanted name), `intake_candidates.json` (every location per name), `intake_archives.csv` (every archive opened), `rrf_adoption_record_digests.csv`, `intake_controls.json`, `intake_summary.json`. Files were read as bytes; nothing from the folder was executed.

## 1. How the files arrived

- **Search:** `Find-RtgCorpusOriginals.ps1` (version 2, copy only), run by the PI on his Windows machine over his archive folder and his Downloads folder. The script and its wanted list were prepared by the Atlas owner. The script was not test-run before it was handed over; its first version stopped at its git step and copied nothing.
- **Wanted list:** 440 file names; 187 carry a full 64-digit SHA-256, 17 a short form (first and last digits, as the source prints it), 236 none. It was extracted automatically from the 18 Atlas sources at `main` `98a4a80`, from the DYAD, RECOG and TRIAD recovery lists and from the RRF inventory of the work list. The copy in the folder (`_WANTED_LIST.txt`) is identical to the list issued. **The pairing of a name with a digest in this list is not validated:** it is known to be wrong in places (§4.1).
- **Route:** the commit `7fa2584` ("missing files") was made on the branch `dyad-cpp-centered-20261116` and merged by PR #367. It did not arrive on a separate `upload/...` branch (CONVENTIONS §6). The merge changes 535 files, all under the folder; nothing else moved.

## 2. What is established

### 2.1 Transfer integrity

All 529 source files have the SHA-256 that `SHA256SUMS.txt` and `MANIFEST.csv` state. Both were written on the PI's machine from the source files, so the copies in the repository equal the files found there. No file in the folder is unlisted. This says nothing about what a file is.

### 2.2 Archive coverage

Every object is indexed under its own name: a loose file under the `OriginalName` of `MANIFEST.csv` (all 529 rows, pattern rows included; never under the name it was stored as), a zip member under its member name. 103 archives were opened and read in full: the 69 loose zip packages and 34 archives nested in them. None was unreadable and none was skipped. Limits: nesting depth 8, member size 300 MB; neither was reached. 8,484 zip members were hashed. "Not found" below therefore means: no object of that name, and no object with the recorded digest, among the 529 loose files and these 8,484 members.

### 2.3 Census against the extracted list

| Result | Names | What it says |
|---|---|---|
| name and full digest | 126 | an object of that name has exactly the 64-digit digest the list pairs with the name |
| name and short digest | 10 | an object of that name agrees with the short form in its first and last digits; the full digest is not known and is not derived |
| name only | 167 | an object of that name exists; the list has no digest for it |
| name, digest differs | 15 | objects of that name exist; none has the paired digest |
| digest under another name only | 5 | no object of that name; bytes with the paired digest exist under another name |
| not found in the inspected scope | 117 | neither |

These are matches against the list. They are not confirmations that the cited historical file is the one found: that needs the citing sentence to be read, name by name, by the stream that cites it.

Where the objects of a name are: 212 names loose only, 60 loose and in zips, **46 only inside zips**, 122 with no object of that name. For 24 names the copies differ in content; `intake_candidates.json` lists all of them.

| Stream | Name + full digest | Name + short digest | Name only | Digest differs | Digest under another name only | Not found |
|---|---|---|---|---|---|---|
| DYAD | 31 | 3 | 43 | 3 | 1 | 58 |
| RER | 72 | 2 | 17 | 8 | 2 | 9 |
| Legacy | 1 | 0 | 18 | 0 | 1 | 20 |
| TRIAD | 8 | 0 | 9 | 0 | 0 | 12 |
| ER-2B | 13 | 0 | 14 | 0 | 0 | 1 |
| RRF | 16 | 0 | 8 | 0 | 1 | 1 |
| NUMGEN | 0 | 0 | 19 | 0 | 0 | 2 |
| GEN | 4 | 3 | 12 | 0 | 0 | 1 |
| FMS | 4 | 1 | 8 | 4 | 0 | 0 |
| AZ | 0 | 0 | 11 | 0 | 0 | 1 |
| OFN | 0 | 2 | 3 | 0 | 0 | 5 |
| UVM | 0 | 0 | 0 | 0 | 0 | 4 |
| PRR Wrap-up | 0 | 0 | 3 | 0 | 0 | 0 |
| DZT, Pre-Legacy, RECOG, TDR-G, Programme, Methodology | 0 | 1 | 6 | 1 | 0 | 3 |

A name cited by several streams is counted in each. Beyond the wanted list, 216 files came in by wide name pattern (106 `RER_*`, 44 `RTG_RRF_*`, 14 Genesis v2.8.x editions, 12 Inheritance Ledger drafts and others). They are indexed like every other object.

### 2.4 The six RRF adoption records, read by their own digests

This check does not use the wanted list. The six records (v0.7, v0.8, v0.8.1, v0.8.3, v0.8.4 loose; v0.8.2 inside `RTG_RRF_v0_8_2_ADOPTED_G2_v0_3_RELEASE_PACKAGE.zip`) print 37 SHA-256 digests between them. For **35** an object with exactly that digest is in the folder; `rrf_adoption_record_digests.csv` gives each digest and the object. They include every registry edition from v0.6 to v0.8.4, the review candidates, the G2 reviews v0.2.1, v0.3 and v0.4, and the pinned owner editions (Dyadic v6.4.10, v6.4.12, v6.4.13; RECOG v0.3.14; NUMGEN v1.20.7; Triadic v1.6; Methodology v1.3). The two without an object are the two publication diffs named in the v0.8.4 record.

**One edition–record link is complete.** The v0.8.4 record (read in full) names the published file as 108,615 bytes with SHA-256 `2fb0a0fe9d998be91618cb731e2dee7301952ffdbe374f4889dd5e61c5cbafce`. That is the tagged `dsn/RTG_RRF_REPRESENTATION_REGISTRY.md` at `rrf-v0.8.4` and the uploaded copy. The reviewer confirmed the same link independently (review `6021632408`).

For the other five records only the digests were extracted. Which role each record gives a digest, and what each record approves, was not read.

### 2.5 Privacy scan (bounded)

The repository is public. The checker scans for four generic classes: e-mail addresses, Windows user paths, private-key headers and token-like assignments. Scanned: 459 loose text files and 7,267 text members of the archives. Not scanned: 1,183 members that are binary or images (png, npz, pyc, pdf) or larger than 20 MB. Files with a match: none. A first run flagged one file; it was a Python matrix product (`X@…`) and the pattern was tightened. Two further literal strings specific to the PI's machine were searched by hand and are not written in a public file. This is a bounded scan, not a guarantee.

## 3. What is now available for the work list (rows A2, A6, A7)

"Available" means an object is in the folder. It does not mean that an old approval is authenticated, that an edition is chosen as governing, or that a dependency is accepted.

| Work-list inventory item | Available | Basis |
|---|---|---|
| 1.1–1.6 RRF adoption records | all six | by name; five more by the digest chain of §2.4 (each record names its predecessor edition); v0.8.4 by the complete link of §2.4 |
| 1.2 v0.8 QA manifest | candidates by name pattern (`RTG_RRF_v0_8_ADOPTION_QA.md`, `RTG_RRF_v0_8_CANDIDATE_REVIEW_MANIFEST.json`) | not identified |
| 2.1 RRF v0.1–v0.5 | yes (v0.1, v0.2 as drafts) | name pattern only |
| 2.2, 2.4–2.8 RRF v0.6, v0.7, v0.8, v0.8.1, v0.8.2, v0.8.3 | yes | full digest, and the same digests are printed in the adoption records. v0.8 is the edition RER records as not recovered in its search of 21 Oct |
| 2.3 RRF v0.7 DRAFT | yes | by name; its digest is printed in the v0.7 adoption record |
| 2.9 the reviewed v0.8.4 candidate | yes, as `…_v0_8_4_REVISED_REVIEW_CANDIDATE.md` | full digest `fc53acff…ab9e`, named with that file name in the v0.8.4 record |
| 3.1, 3.2 G2 reviews | `RTG_RRF_G2_PRIMITIVE_EXCHANGE_INTERFACE_REVIEW` v0.1, v0.2, v0.2.1, v0.3 (review candidate, and final inside the v0.8.2 package), v0.4, v0.4 (review candidate); `DYAD_RRF_OFN_G2_CONSOLIDATED_NOTE` v0.1–v0.4 | v0.2.1, v0.3 and v0.4 by digests printed in the adoption records; the rest by name. The review and the consolidated note are different documents |
| 3.3 degree-ten review integration | yes | name only |
| 3.4 `PRR_RRF_REVIEW_v1` | **no** | not found in the inspected scope |
| 3.5 the editor response to RER's G9 request | candidates: `RRF_EDITOR_RESPONSE_TO_RER_PHASEA_v0_2_20261019.md`, `RER_RRF_EDITOR_RESPONSE_RECEIVER_HANDOFF_20261019.md`, `RER_TO_RRF_EDITOR_W3_RF1_AND_G9_3_REQUEST_v0_1_20261020.md` | not identified |
| 3.6 the SESSION review of S_h and R₀ | candidate by title: `RTG_RRF_SH_R0_FIRST_DIFFERENCE_SESSION_NOTE_v0_1.md` | not identified |
| 3.7–3.9 closure proposal, OFN-coincidence response, admissibility review | yes | full digest (as reported by the RRF editor in RER); the closure proposal's digest is also printed in the v0.8.1 adoption record |
| 4.1 degree-ten verification record (DYAD) | bytes with DYAD's digest, under a browser-renamed file name | full digest; own name differs (§4.1) |
| 4.2 OPEN19 G2 post-adoption sync review (DYAD) | v0.1–v0.4 | name only |
| 5.1 ER-2B v0.2 (and v0.1) | yes | full digest |
| 5.2 six-step audit zip | yes | name only |
| 6.1 PRR Wrap-up | v0.1, v0.2, v0.3 (40,136 / 49,059 / 101,038 bytes; SHA-256 `7ff7d154…0a9d`, `88274f70…e2f2`, `68d45d37…a40c`) | **name only.** No source prints a digest for any of them. RRF and RECOG cite v0.2; that a v0.3 exists does not make it the cited or the governing one |
| 6.2 Inheritance Ledger | twelve drafts v0.1–v0.19 | name pattern. The v0.19 draft has `f6320914190b…e2f8`; RER prints `f6320914…0be8`. The first eight digits agree, the last four do not. Unresolved; neither source is corrected here |
| 6.3 "Initial Ontological Premises" note | `RTG_INITIAL_ONTOLOGICAL_PREMISES_v0_2.md` | name pattern only |
| 6.4 Legacy sources | `RTG_MASTER_DSN_v1.0.txt`, `L0_MASTER_DSN_v2_2.txt`; the history archive v0.7 | name only; the archive by full digest |
| Genesis v2.8.5 (needed by UVM) | yes | full digest `41ed7660…` |
| DZT's digests for the Dyadic extractor | an object named `q4_03_cascade_extract.py` agrees with the short form `ecdb805f…05eac2` | short digest only |

## 4. Defects of the search, to know before the files are used

**4.1 Twelve loose files are stored under a name that is not their own.** The script stored a file under the wanted-list name whenever its bytes had the digest the list pairs with that name. The bytes are unchanged; `MANIFEST.csv` has the true name in `OriginalName`, and this check indexes each file under that name.

| Stored as | The file's own name | Reading |
|---|---|---|
| `build_r4_1_draft.py` | `RTG_RELATIONAL_EMERGENCE_REGISTRY_v0_2_DRAFT_r3_1.md` | wrong pairing in the list |
| `build_r4_2_draft.py` | `RTG_RELATIONAL_EMERGENCE_REGISTRY_v0_2_DRAFT_r4.md` | wrong pairing |
| `build_r4_7_draft.py` | `RRF_EDITOR_RESPONSE_TO_RER_PHASEA_v0_2_20261019.md` | wrong pairing |
| `cent_output.txt` | `cent.py` | wrong pairing |
| `exact_q_output.txt` | `exact_q.py` | wrong pairing |
| `fit_output.txt` | `cm.py` | wrong pairing |
| `lock5_output.txt` | `lock5.py` | wrong pairing |
| `rtg_betagraded_vanishing.py` | `rtg_betagraded_vanishing_v1_1.py` | renamed copy or wrong pairing; for the owner to say |
| `STAGE2_FOLLOWUP_RECEIVING_RESPONSE_20261014.md` | `RECEIVING_RESPONSE.md` | the same bytes also exist under the wanted name inside a zip |
| `cb732e21-46ad-4a96-a76f-71566f4ed100.zip` | `data.zip` | plausibly a renamed download |
| `DYAD_CHECK_degree10_even_term_hatF.md` | `DYAD_CHECK_degree10_even_term_hatF281%29.md` | a browser-renamed copy |
| `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4_CANDIDATE.md` | `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4_REVISED_REVIEW_CANDIDATE.md` | the stored name is a label the list invented |

Cause: the list paired each cited name with the first digest printed after it on the same line. Where a source prints a script, its output file and one digest, the digest went to the wrong one of the two.

**4.2 "Digest differs" (15 names) is not evidence that a file was altered.** For each, the paired digest may belong to a neighbouring name. Seven of the fifteen are the stored names of §4.1's wrong pairings.

**4.3 Variant names.** 56 files are stored as `name__<8 hex>.ext` because several copies of one name differed. Three further variants of `rtg_dyad_audit.py` were over the script's cap of eight and were not copied (`VARIANTS_OVER_CAP.txt`).

**4.4 One file was too large:** `motif_N720_k48_T5000_b500_v18.csv` (93.4 MB, TDR-G), listed in `TOO_LARGE.txt` and not copied.

**4.5 Name-only matches of generic names** (`fit.py`, `cent.py`, `local_results.json` and the like): a file of that name from another context cannot be excluded.

The folder is left as it arrived. When a file is placed in a stream's folder, it takes its own name, not the stored one.

## 5. Not found in the inspected scope (117 names)

`intake_result.csv` has them. By stream: DYAD 58, Legacy 20, TRIAD 12, RER 9, OFN 5, UVM 4, NUMGEN 2 and one each for RRF, GEN, AZ, ER-2B, Pre-Legacy, DZT and TDR-G. `NOT_FOUND.txt` in the folder is the search script's own list and is longer: it does not look inside zips.
- **RRF:** `PRR_RRF_REVIEW_v1.zip`.
- **UVM:** `EDIT_A_wiring_instructions.txt`, `esm_harmonic_report.py`, `t103_defect_carrier_test.py`, `uvjet_equivariant_classification.py`.

The scope is the PI's archive folder and Downloads folder as searched on 23 Nov. A file kept elsewhere is not excluded.

## 6. What follows (proposals; nothing is done here)

1. Each stream's owners take their files from the folder by their own PR into `records/<study>/` or `evidence/<study>/`, under the file's own name, and say what they use. The Atlas does not place files.
2. The work list rows A2, A6 and A7 are updated from §3 once PR #364 is merged.
3. **For the PI's RRF source condition:** what this intake supplies is the inventory and the byte identity of the registry's editions v0.6–v0.8.4 and of six adoption-record files, with one complete edition–record link (v0.8.4). It does not supply a reading of what the five earlier records approve, a choice among the PRR Wrap-up versions, `PRR_RRF_REVIEW_v1`, or the Inheritance Ledger's provenance. Whether that is enough to open the RRF review, when its turn comes after NUMGEN and OFN, is the PI's decision.
4. Before any second search the wanted list is repaired: each name–digest pairing is read against its citing sentence, starting with the 15 "digest differs" names and the 5 "digest under another name".

## 7. Review and revision

**Review `6021632408`** (ChatGPT, Atlas reviewer, on `474b41c`): changes requested, confined to the checker and the reporting. Three findings, all accepted:
- **R1.** "46 only inside zips" counted the chosen match, not availability, and the loose-file loop skipped pattern rows and never indexed a wrongly stored file under its own name. Now every object is indexed under its own name across the whole manifest and all archives; availability is derived from all objects of a name. The figure "only inside zips" is again 46, now by that definition.
- **R2.** Nested archives that failed to open, or lay beyond the depth and size limits, were passed over silently. Now every archive is logged with its status and reason; the limits are stated; absence is "in the inspected scope". On the real folder no archive was unreadable or skipped.
- **R3.** A full digest and a short one had the same label, and a match against the extracted list read as a verified identity. Now the recorded reference is kept verbatim, the basis is its own column, the pairing is marked as not validated, and §§3 and 6 say "available" with the basis, not "closed".

**Effect on the census.** The first version reported 135 / 165 / 15 / 125 (hash-verified / present without a hash / hash differs / not found). The same 135 are now 125 by full digest and 10 by short digest. Of the 125 "not found", eight leave that class: one is found by name and full digest, two by name, five as bytes under another name. No name entered "not found".

**Controls.** Eleven synthetic fixtures run with the checker (`--controls`, `intake_controls.json`): the reviewer's eight cases, a depth-limited archive, the same archive within the limit, and a differing digest. All behave as intended.

**Not rerun or reread here:** no uploaded script was executed; the 216 pattern files were classified by name, not read; five of the six adoption records were read only for their digests.
