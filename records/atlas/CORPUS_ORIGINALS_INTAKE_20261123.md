# Corpus originals — intake check of `upload/corpus-originals-20261123/`

**Date:** 23 November 2026. **By:** Claude, Atlas owner.
**Status:** [SESSION] intake record. It verifies bytes and names. It adopts nothing, places no file in a stream's folder and changes no DSN, pipe or Atlas byte. What each stream uses is its owner's decision (CONVENTIONS §7).
**Asked by the PI** (project conversation, 23 Nov 2026, 12:30 and 15:03 +03:00): one search script for all files the corpus cites and does not hold, into one upload folder; then a check of what arrived.
**Object:** `upload/corpus-originals-20261123/` on `main` `561bb39b76bff9a28a715f5853a504c22e5e3ca7`: 535 files (529 source files and six report files), 111 MB.
**Check:** `python3 -I evidence/atlas/intake/corpus_originals_20261123/intake_check.py`; results in `intake_result.csv` (one row per wanted name) and `intake_summary.json`. Files were read as bytes; nothing from the folder was executed.

## 1. How the files arrived

- **Search:** `Find-RtgCorpusOriginals.ps1` (version 2, copy only), run by the PI on his Windows machine over his archive folder and his Downloads folder. The script and its wanted list were prepared by the Atlas owner. The script was not test-run before it was handed over; its first version stopped at its git step and copied nothing.
- **Wanted list:** 440 file names, 187 with a full recorded SHA-256 and 17 with a short one. It was extracted from the 18 Atlas sources at `main` `98a4a80`, from the DYAD, RECOG and TRIAD recovery lists and from the RRF inventory of the work list. The copy in the folder (`_WANTED_LIST.txt`) is identical to the list issued.
- **Route:** the commit `7fa2584` ("missing files") was made on the branch `dyad-cpp-centered-20261116` and merged by PR #367. It did not arrive on a separate `upload/...` branch (CONVENTIONS §6). The merge changes 535 files, all under the folder; nothing else moved.
- **Unchanged bytes:** all 529 source files have the SHA-256 that `SHA256SUMS.txt` and `MANIFEST.csv` state. Both were written on the PI's machine from the source files, so the copies in the repository equal the files found there.
- **The repository is public.** A scan of the loose text files and of the members of the 69 zip packages found no e-mail address, no Windows user path, no employer name and no credential pattern. Wide-pattern hits were read by name: all are RTG documents.

## 2. Result against the wanted list

| Result | Names | Meaning |
|---|---|---|
| hash-verified | 135 | a file of that name is present and its SHA-256 equals the recorded one |
| present, no recorded hash | 165 | a file of that name is present; no source in the repository prints a hash for it, so only the name is matched |
| present, hash differs | 15 | a file of that name is present; none of the copies has the recorded hash |
| not found | 125 | no file of that name, loose or inside an uploaded zip |

46 of the present names were found only inside uploaded zip packages (two levels deep), not as loose files.

| Stream | Hash-verified | Present, no hash | Hash differs | Not found |
|---|---|---|---|---|
| DYAD | 34 | 42 | 3 | 60 |
| RER | 74 | 17 | 8 | 11 |
| Legacy | 1 | 18 | 0 | 21 |
| TRIAD | 8 | 9 | 0 | 12 |
| ER-2B | 13 | 14 | 0 | 1 |
| RRF | 16 | 8 | 0 | 2 |
| NUMGEN | 0 | 19 | 0 | 2 |
| GEN | 6 | 12 | 0 | 2 |
| FMS | 4 | 6 | 4 | 3 |
| AZ | 0 | 11 | 0 | 1 |
| OFN | 2 | 3 | 0 | 5 |
| UVM | 0 | 0 | 0 | 4 |
| PRR Wrap-up | 0 | 3 | 0 | 0 |
| DZT, Pre-Legacy, RECOG, TDR-G, Programme, Methodology | 1 | 6 | 1 | 3 |

A name cited by several streams is counted in each. The four UVM names are those the earlier `upload/uvm-originals/` search had not found either.

Beyond the wanted list, 216 files came in by wide name pattern (for example 106 `RER_*`, 44 `RTG_RRF_*`, 14 Genesis v2.8.x editions, 12 Inheritance Ledger drafts). They are in `MANIFEST.csv` with status `PATTERN` and are not counted above.

## 3. What this closes in the work list (rows A2, A6, A7)

| Work-list inventory item | Now |
|---|---|
| 1.1–1.6 RRF adoption records | **all six present**: v0.7, v0.8, v0.8.1, v0.8.3, v0.8.4 as loose files; v0.8.2 inside `RTG_RRF_v0_8_2_ADOPTED_G2_v0_3_RELEASE_PACKAGE.zip`. No hash was recorded for any of them. QA files for v0.8, v0.8.1, v0.8.3 and v0.8.4 came in by pattern |
| 2.1 RRF v0.1–v0.5 | present by pattern (v0.1 and v0.2 as drafts) |
| 2.2, 2.4–2.8 RRF v0.6, v0.7, v0.8, v0.8.1, v0.8.2, v0.8.3 | **all hash-verified**. This includes v0.8, which RER records as not recovered in its own search of 21 Oct |
| 2.3 RRF v0.7 DRAFT | present, no recorded hash |
| 2.9 the reviewed v0.8.4 candidate | bytes with the recorded hash `fc53acff…ab9e` are present; the file's own name is `…_v0_8_4_REVISED_REVIEW_CANDIDATE.md` (§4) |
| RRF v0.8.4 itself | the uploaded copy equals the tagged file (`2fb0a0fe…afce`) |
| 3.1, 3.2 G2 reviews | `RTG_RRF_G2_PRIMITIVE_EXCHANGE_INTERFACE_REVIEW` v0.1, v0.2, v0.2.1, v0.3 (review candidate), v0.4 and v0.4 (review candidate) are present. `DYAD_RRF_OFN_G2_CONSOLIDATED_NOTE` v0.1–v0.4 is present as well: the two are different documents, which the work list had left open |
| 3.3 degree-ten review integration | present, no recorded hash |
| 3.4 `PRR_RRF_REVIEW_v1` | **not found** |
| 3.5 the editor response to RER's G9 request | candidates present, not identified by this check: `RRF_EDITOR_RESPONSE_TO_RER_PHASEA_v0_2_20261019.md` (stored under another name, §4), `RER_RRF_EDITOR_RESPONSE_RECEIVER_HANDOFF_20261019.md`, `RER_TO_RRF_EDITOR_W3_RF1_AND_G9_3_REQUEST_v0_1_20261020.md` |
| 3.6 the SESSION review of S_h and R₀ | candidate present by title: `RTG_RRF_SH_R0_FIRST_DIFFERENCE_SESSION_NOTE_v0_1.md` |
| 3.7–3.9 closure proposal, OFN-coincidence response, admissibility review | all three hash-verified |
| 4.1 degree-ten verification record (DYAD) | bytes with the recorded hash present (§4, a browser-renamed copy) |
| 4.2 OPEN19 G2 post-adoption sync review (DYAD) | v0.2 present, no recorded hash; v0.1, v0.3, v0.4 by pattern |
| 5.1 ER-2B v0.2 | hash-verified (v0.1 too) |
| 5.2 six-step audit zip | present, no recorded hash |
| 6.1 **PRR Wrap-up** | **v0.1, v0.2 and v0.3 present** (40,136 / 49,059 / 101,038 bytes; SHA-256 `7ff7d154…0a9d`, `88274f70…e2f2`, `68d45d37…a40c`). No hash was recorded anywhere, so these are identified by name only |
| 6.2 Inheritance Ledger | twelve drafts v0.1–v0.19 present. The v0.19 draft has SHA-256 `f6320914190b…e2f8`. RER prints `f6320914…0be8`: the first eight digits agree, the last four do not. Either the file differs from the one RER names or RER's short form is misprinted; this check cannot tell |
| 6.3 "Initial Ontological Premises" note | present: `RTG_INITIAL_ONTOLOGICAL_PREMISES_v0_2.md` |
| 6.4 Legacy sources | `RTG_MASTER_DSN_v1.0.txt` and `L0_MASTER_DSN_v2_2.txt` present, no recorded hash; the history archive v0.7 hash-verified |
| Genesis v2.8.5 (needed by UVM) | hash-verified (`41ed7660…`); editions v2.8.0–v2.8.9 by pattern |

## 4. Defects of the search, to know before the files are used

**4.1 Twelve files are stored under a name that is not their own.** The script stored a file under the wanted-list name whenever its bytes had a hash recorded for that name. For twelve files the file's own name is another one. The bytes are unchanged; `MANIFEST.csv` has the true name in `OriginalName`.

| Stored as | The file's own name | Reading |
|---|---|---|
| `build_r4_1_draft.py` | `RTG_RELATIONAL_EMERGENCE_REGISTRY_v0_2_DRAFT_r3_1.md` | wrong pairing in the wanted list |
| `build_r4_2_draft.py` | `RTG_RELATIONAL_EMERGENCE_REGISTRY_v0_2_DRAFT_r4.md` | wrong pairing |
| `build_r4_7_draft.py` | `RRF_EDITOR_RESPONSE_TO_RER_PHASEA_v0_2_20261019.md` | wrong pairing |
| `cent_output.txt` | `cent.py` | wrong pairing |
| `exact_q_output.txt` | `exact_q.py` | wrong pairing |
| `fit_output.txt` | `cm.py` | wrong pairing |
| `lock5_output.txt` | `lock5.py` | wrong pairing |
| `rtg_betagraded_vanishing.py` | `rtg_betagraded_vanishing_v1_1.py` | renamed copy or wrong pairing; for the owner to say |
| `STAGE2_FOLLOWUP_RECEIVING_RESPONSE_20261014.md` | `RECEIVING_RESPONSE.md` | plausibly the same document under its packet name |
| `cb732e21-46ad-4a96-a76f-71566f4ed100.zip` | `data.zip` | plausibly a renamed download |
| `DYAD_CHECK_degree10_even_term_hatF.md` | `DYAD_CHECK_degree10_even_term_hatF281%29.md` | a browser-renamed copy |
| `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4_CANDIDATE.md` | `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4_REVISED_REVIEW_CANDIDATE.md` | the stored name is a label the wanted list invented |

Cause: the wanted list paired each cited name with the first hash printed after it on the same line. Where a source prints a script, its output file and one hash, the hash was attached to the wrong one of the two. The seven "wrong pairing" rows are not counted as hash-verified in §2. The same cause can make a correct file read "hash differs" (§4.2).

**4.2 "Hash differs" (15 names) is not yet a finding about the files.** For each, the recorded hash may belong to a neighbouring name. The owner reads the citing sentence before concluding that a file was altered.

**4.3 Variant names.** 56 files are stored as `name__<8 hex>.ext`, because several copies of one name differed in content. Three further variants of `rtg_dyad_audit.py` were over the cap of eight and were not copied (`VARIANTS_OVER_CAP.txt`).

**4.4 One file was too large:** `motif_N720_k48_T5000_b500_v18.csv` (93.4 MB, TDR-G), listed in `TOO_LARGE.txt` and not copied.

**4.5 Name-only matches.** Generic names (`fit.py`, `cent.py`, `local_results.json` and the like) without a recorded hash are matched by name alone; a file of that name from another context cannot be excluded.

The folder is left as it arrived. When a file is placed in a stream's folder, it takes its own name from `OriginalName`, not the stored one.

## 5. Not found (125 names)

`upload/corpus-originals-20261123/NOT_FOUND.txt` lists the names not found as loose files; `intake_result.csv` gives the state after the zip search. By stream: DYAD 60, Legacy 21, TRIAD 12, RER 11, OFN 5, UVM 4, FMS 3 and one or two each for RRF, GEN, NUMGEN, AZ, DZT, ER-2B, Pre-Legacy and TDR-G. For the two streams this search was first asked for:
- **RRF:** `PRR_RRF_REVIEW_v1.zip` (also absent in its `.md` form).
- **UVM:** `EDIT_A_wiring_instructions.txt`, `esm_harmonic_report.py`, `t103_defect_carrier_test.py`, `uvjet_equivariant_classification.py`.

## 6. What follows (proposals; nothing is done here)

1. Each stream's owners take their files from the folder by their own PR into `records/<study>/` or `evidence/<study>/`, with the file's own name, and say what they use. The Atlas does not place files.
2. The work list rows A2, A6 and A7 are updated from §3 once PR #364 is merged.
3. The RRF source gate set by the PI ("no RRF review before its source files are verified") is now met for the registry's editions v0.6–v0.8.4 and for its six adoption records as files. Whether that opens the RRF review is the PI's decision.
4. The wanted list is repaired before any second search: hashes re-paired by reading the citing sentences, starting with the 15 "hash differs" names.
