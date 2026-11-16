# Discrete Genesis v2.13 — atlas row check (candidate `c89eb81b…0a14`)

**Date:** 16 November 2026. **By:** Claude, atlas owner (advises; does not adopt).
**Object:** PR #265 `claude/tdrg-v2-13` (draft, head `fba3ea13`): candidate `dsn/RTG_DISCRETE_GENESIS_DSN.md` SHA-256 `c89eb81b8456b3d77e5608d2e288378d581477d36bb0acc80ee1c8b21c3a0a14` (157,343 bytes, 1,199 lines), built in two stages from `tdrg-v2.12.15` (`1e35be54…2e64`) through the stage-1 intermediate `472e26e9…56ff` (commit `fd96f8a`). Release record `records/tdrg/TDRG_v2_13_RELEASE_RECORD.md` at `fba3ea1`. Co-owner reviews: PR #268 (`5906863206`, `5906970313`, round 2 PASS).
**Status:** record. **Verdict: the build is sound and reproduces; one correction is recommended before adoption (§3, F1): the edition pins AZ at v0.8 and restates AZ's v0.8 consumer row, but `az-v0.9` was adopted on 14 Nov, after the cycle started.**
**Reruns:** `evidence/atlas/rowcheck/tdrg_v2_13/`. Owner sources read at their tags (`EV-SRC-READ`). No engine or campaign rerun (`EV-NOT-RERUN`).

## 1. Independent rerun

| Step | Result |
|---|---|
| stage-1 builder from `tdrg-v2.12.15` | intermediate `472e26e9…56ff` and edit log (29 edits) **byte-identical** to the branch files |
| stage-1 checker C0–C10 and controls K1–K10 | outputs byte-identical to `check_output.txt` (11/11) and `controls_output.txt` (10/10 caught) |
| stage-2 builder | candidate `c89eb81b…0a14` and movement map (43 operations) byte-identical |
| `tools/check_compaction.py` | exit 0, output equal to the committed one |
| stage-2 controls P0, N1–N8 | output byte-identical |
| RID declarations | 81 at the predecessor, 81 in the candidate, the same set |
| Atlas-cited TDR-G identifiers | all present in the candidate; the four absent ones are absent at `tdrg-v2.12.15` too (one is AZ's `TDRG-AZ-STATIC-ZN-4Q`, three are atlas pseudo-labels) |
| trial merges onto `main` `54cddd7` | #263, #268, #265 each clean, and clean in the order #263 → #268 → #265 |

## 2. Rows against the plan

The stage-1 rows S1–S8 and the stage-2 operations do what the release record says (§§3–4 there), and the reruns confirm them mechanically. Statement-level spot checks: §1 readouts carry the owner grades of §§2–9 (no grade in §§2–9 changes, checker C4); the §A.sim table moves without its unpaired `[RESULT]` (review R1); the v2.8 failed-relock hypothesis is in Appendix B with its original statement; XFER-O08-01 is stated as open; no compound grade tag remains. The two items reported and not changed (crystallization grade; history phrases in live text) are correctly left to the owners.

## 3. Findings

**F1 — AZ pin and consumer row (recommended before adoption).** The cycle started at `main` `93f1986` (13 Nov), before `az-v0.9` (14 Nov, merge `2676e6f`). The candidate therefore:
- cites `AZ-ALG-ANTIPODAL-LOWORDER` at `az-v0.8` (§6.2). The content is right: the defining line is byte-identical at `az-v0.8` and `az-v0.9`. Only the pin is one edition old.
- restates the AZ consumer row from AZ v0.8 (line 885: "its §8 (IMP-B) cites … at `tdrg-v2.12.14`"). At `az-v0.9` this is no longer true. AZ §8 cites TDR-G at `tdrg-v2.12.15`. It adds two rows: `TDRG-ALG-EVENT-INVENTORY` / `TDRG-ALG-TOKEN-CENSUS-LAW` and `TDRG-ALG-PARENT-CHILD-PHASE`. It also carries one AZ-owned `[NUM diagnostic]`, `AZ-NUM-TOKRES-S1`, computed on TDR-G's pinned engine with `TDRG-DEF-ORIENT`; AZ states it is not a TDR-G result.
- names "AZ v0.8" among the governing editions (line 889) and in the Appendix A entry for v2.13 (line 1007). The release record (S1) says "Pins are current".

Recommendation: one stage-1 change in the existing pattern. Repin to `az-v0.9`, restate the consumer row from AZ v0.9 §8, and move checker C6 and control K1 to `az-v0.9`. Then rebuild stage 2, which gives a new candidate hash, and run a short readback by the co-owner. Whether TDR-G mentions `AZ-NUM-TOKRES-S1` in its consumer row is TDR-G's choice. If it does, the wording should be AZ's: an AZ-owned diagnostic, not a TDR-G result. The alternative is adoption as is, with the staleness recorded in §10. The edition's own claim that pins are current would then be false on the day it is adopted.

**F2 — pipe items.** Release record §7 says `pipes/TDRG/` has no open item, read at `93f1986`. Since 14 Nov it holds `pipes/TDRG/20261114-AZ-v0-9-adopted.md` (open, a notice). It asks nothing, but its subject is the §6.2 citation and AZ §8, which F1 touches. This edition is its natural disposition. The planned notice to `pipes/AZ/` (§7) should then name `az-v0.9`.

**F3 — base of the publication commit.** `BASELINE.md` and the AZ DSN changed on `main` after `93f1986`. The trial merges are clean. The publication commit's BASELINE row should still be written against current `main`, which has the `az-v0.9` row.

**F4 — #263.** `records/tdrg/TDRG_v2_13_EDIT_PLAN.md` is identical on #263 and #265, so closing #263 unmerged loses nothing. The plan's PI-decision commit `666da2b` is an ancestor of #265, so its history arrives with #265 either way.

## 4. For the atlas (impact refresh after `tdrg-v2.13`, Atlas v0.14)

These Atlas lines change when the edition is tagged. They are not changed now; the Atlas v0.13 candidate is pinned at `tdrg-v2.12.15`:
- D5 header: "Methodology v1.2 declared by PI decision, the v1.4 migration is v2.13" → v1.4 declared.
- TDRG.G8 (layout: footer chain, Appendix A order, v1.2 declaration): the candidate has one footer line, Appendix A in edition order, and v1.4 declared. Candidate for retirement.
- XFER-O08-01 "deferred to (TDR-G) v2.13" (OFN admin-queue row, `RTG-OFN-ALG-STAR-TOKEN-SHIFT`, `TDRG-DEF-STAR`): now "open, a separate decision of both owners".
- PROG.G6: "Methodology v1.4 migration planned for v2.13" → executed.
- METH.M1: TDR-G no longer carries compound grade tags. Candidate for leaving the list.
- `TDRG-DEF-ORIENT DEF [COR v2.12.14]`: an atlas edition label; Method §4.1 once D5 is opened.
- If F1 is applied: the TDR-G consumer row toward AZ.

The v0.13 builder asserts that no newer source tag exists. Once `tdrg-v2.13` exists, v0.13 can no longer be rebuilt with that assertion. This does not affect its publication: the PI's merge and tag do not rebuild.

## 5. Asked of the PI

Whether F1 is applied before adoption (recommended) or the edition is adopted as is with the staleness recorded. The merge order (#263 → #268 → #265, or #263 closed unmerged) is the PI's choice. The atlas side has no preference.
