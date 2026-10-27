# Number Genesis v1.21 — atlas row check, stage 2 (candidate `05b3315f…4258`) and review of the shared checker extension

**Date:** 26 October 2026. **By:** Claude, atlas owner (advises; does not adopt). **Object:** PR #76 `claude/numgen-v1.21-stage2` (head `19432b9`, stacked on PR #74): candidate `dsn/RTG_NUMBER_GENESIS_DSN.md` SHA-256 `05b3315fe74ec006b5610b1823522f843f55d677c01f1ec39b42144dd4be4258` (2,970 lines, 274,236 bytes) from the stage-1 intermediate `ab25c162…99d2`; movement map `fb93b2a9…bfa9`; `tools/check_compaction.py` extended (`2ba2a409…7306`, from `main` `6ed87798…b603`); DRAFT release record `records/numgen/NUMGEN_v1_21_RELEASE_RECORD.md`.
**Status:** record. **Verdict: ACCEPT FOR ADOPTION (atlas side) — stage 2 is layout-only; the checker extension is accepted for all streams, with two non-blocking notes.** Final acceptance is the PI's.
**Reruns:** `evidence/atlas/rowcheck/numgen_v1_21/` (summary, five regression outputs with both checkers, extra fixtures).

## 1. Independent rerun of stage 2

| Step | Result |
|---|---|
| `build_numgen_v1_21_stage2.py` on the rebuilt stage-1 file | `05b3315f…4258`, **byte-identical** to the branch file; map `fb93b2a9…bfa9` identical |
| `tools/check_compaction.py` (branch version) on the rebuilt triple | PASS; output byte-identical to `evidence/numgen/v1.21/check_compaction_output.txt` (`9e8d2a7b…`): 253/253 claim blocks byte-identical, RID set / source hashes / qualifiers preserved, references resolve, one footer, base history region 79,981 chars relocated and archived |
| `check_numgen_v1_21_stage2.py` G0–G6 | PASS (live body, Appendix B and Working-Thesis body byte-identical to stage 1; header fields; history archived with the tag pointer) |
| `--fixtures` F1–F11 | all caught (F1–F3, F5–F9 by the checker; F4, F10, F11 by guards G2/G3) |
| `tools/pipes_index.py --check` on the tree | OK, 7 items in 19 inboxes |

## 2. Row checks of the compaction

- **Header** (S2-H): current-only; Supersedes names one predecessor with the full hash and tag; `DSN Methodology: v1.4`; status summary = first three sentences of the base summary (checker `summary_from: header`); Document status DRAFT naming the release record. The Methodology note and the Pointer-validation note (history) are gone from the header and present in the stage-1 archive — correct under v1.4 §1.1.
- **Appendix A — Version History** (S2-T): three entries (v1.21 DRAFT, v1.20.8, v1.20.7) with the identities checked: v1.20.8 release record `fb699967…1f97` and r3 `9d59cfa1…e7b3` (both in the upload, hash check 26 Oct), v1.20.7 bytes `c4637e7a…ab28` (upload file hash matches), stage-1 round-1 `702e3917…3880` superseded. Pointer to tag `numgen-v1.20.8` for the full changelog and the three legacy notes. Every identifier named in Appendix A exists in the live text (F5).
- **Appendix B** byte-identical; **Working Thesis** → Appendix C, heading letter only (G3); no live text referred to "Appendix A" as the Working Thesis (checker references).
- **Live body** `## §0.` … first appendix heading byte-identical to stage 1 (G1). No RID, grade, OPEN or hash changed between stage 1 and the candidate.
- **Live-file exceptions kept on purpose** (release record §6): the LOGSLIP `[COR]` block stays in §6.6 marked historical (moving it would move claim blocks — correctly left to a reviewed later edit); ten dated `[v1.20.x]` markers in untouched rows; §1 profile exception declared in the header. Agreed: all three are declared, none is hidden.
- **Removals noted** (release record §7): `RECOG-ALG-LATTICE-CLOCK` (RECOG's RID, dropped from NUMGEN's consumer row by the E42 merge) and `NUMGEN-FAIL-N5AS1-SECTION` (changelog-only) are now at the tag only. Neither was a live NUMGEN statement. The atlas keeps no row on either.
- **Size**: −19.1 % against v1.20.8; stage 1 +15,021 bytes (matrix, alias table, RIDs, evidence keys), stage 2 −79,788.

## 3. Review of the `tools/check_compaction.py` extension (`base_history_from`)

The tool is shared by every stream (DYAD v6.4.21 pilot, RECOG v0.3.23/v0.3.24, Programme v1.3, GEN v2.9), so the atlas owner reviewed the diff and reran every stream's harness with the extended checker and with the `main` checker.

**What it does (diff read in full, 49 lines).** Optional profile key `base_history_from: "## <heading>"`. When set, the base's live text ends at that heading (`live_text` cuts the base only; the candidate is never cut). A new check "base history region" requires: the heading is a unique `## ` line of the base; no `## §` or `## Appendix` heading follows it; the heading is absent from the candidate; the region is removed by a declared `replace-section`; the region is found byte-identical in a named archive. When absent, `base_history_start` returns −1 and `live_text` is the old function (the added `r["appA"][1] <= len(s)` condition is always true). No check removed or relaxed.

**Regression, both checkers, outputs byte-identical in every case** (`evidence/atlas/rowcheck/numgen_v1_21/*_branch_checker.txt` vs `*_main_checker.txt`):

| Stream triple | Harness | branch | main | identical |
|---|---|---|---|---|
| DYAD v6.4.21 (`6622dcd` → `6f4a667`, reviewed regions) | `tools/test_check_compaction.py` | PASS 16/16 | PASS 16/16 | yes (`0ab7f5f7…`, the hash recorded at RECOG v0.3.23) |
| RECOG v0.3.23 (`97b0425` → `4e7efd9`) | `test_check_compaction_recog.py` | PASS 17/17 | PASS 17/17 | yes |
| RECOG v0.3.24 (round-2 intermediate → `a164704`) | `test_check_compaction_move.py` | PASS 12/12 | PASS 12/12 | yes |
| GEN v2.9 (`5677d706…` → `4438250`) | `check_compaction.py`; `check_gen_v2_9_stage2.py --fixtures` | PASS; all caught | PASS; all caught | yes |
| **Programme v1.3** (`951371d` → `f7ff205`) — not in the co-owner's set | `test_check_compaction_programme.py` | PASS 10/10 | PASS 10/10 | yes |

**Atlas extra fixtures on the new key** (`atlas_extra_fixtures_base_history_from.txt`), through the checker alone: key pointed at `## Appendix B…` → FAIL (heading survives in the candidate); key pointed at a later heading (`## v0.3 Change Note`) → FAIL (changelog RIDs/hashes/qualifiers then count as lost — the key can only tighten when misplaced forward); `## Changelog` surviving as a phrase in the candidate → FAIL; an Appendix B record deleted from the candidate with the map unchanged → FAIL by re-derivation. The "known checker limit" of the release record §5.2 is therefore narrower than stated: the checker accepts a tail change only when the map's `new` text itself carries it; an undeclared deletion is caught by re-derivation. Guards G2/G3 remain the right place for "the declared tail must not alter Appendix B / the Working Thesis".

**Verdict on the tool: ACCEPT** for `main`. Two non-blocking notes for the next tool edition:
1. `base_history_start` recognises the base by object identity (`s is not BASE_TEXT`). It works because `main()` binds the same object; an explicit `is_base` parameter would be sturdier.
2. The declared heading may itself start with `## §` or `## Appendix` (only *following* headings are refused). Refusing such a heading outright would close a path that today fails only because the heading survives in the candidate (fixture X2).

## 4. Release record (DRAFT) — readback

`NUMGEN_v1_21_RELEASE_RECORD.md`: identities match the reruns (§2 table); §3 groups match the 45 logged edits; §5.3 states the extension honestly and asks for this review; §6 exceptions declared; §8 pipe states correct (inbox item dispositioned; four outbound items open; the GEN item will get a dated RID line after the tag); §9 notices after the tag as `kind: notice` items; §12 merge order #69, #70, #72, #73, #74, #76 then the annotated tag. Fields *(to be filled)*: stage-2 review (now given by the ChatGPT co-owner on PR #76, comment `6417476658`: accepted, atlas check pending), this row check, PI adoption, published hash, tag.

## 5. Asked of the PI

Adoption of v1.21 on the bytes `05b3315f…4258` (the publication transform then changes status lines only; the co-owners record the published hash in the release record before the tag). Merge order as the release record §12; annotated tag `numgen-v1.21` naming the published hash; the atlas owner verifies the tag and refreshes the atlas (D2/D5 NUMGEN rows, H4/H5/H8, N-G1; `records/numgen/ATLAS_ROW_CHECK_NUMGEN_v1_21_STAGE1.md` §4).
