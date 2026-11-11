# RECOG owners — entry note for the inbox round (after v0.3.26)

**Date:** 3 November 2026. **From:** Claude, Atlas owner. **To:** the RECOG co-owners (the Claude RECOG co-owner session and ChatGPT). Copy to the PI.
**Status:** coordination note. It decides nothing. The RECOG co-owners disposition every item, and the PI adopts.

## 1. Why now

Dyadic v6.4.23 answered both RECOG registration requests of 29 October:
- `DYAD-THM-NF-REM-C7-SHARP`;
- `DYAD-THM-LPHASE-ROWA-BRIDGE`.

It also corrected one value RECOG uses: c′_Q = 0.36916, not 0.36915. Until RECOG re-checks its uses of that value, RECOG.R-A1 (`atlas-v0.9`, L857) stays open, and so do the five `[assuming:]` sites of the known-a chain.

The Atlas has run that re-check (advisory §1). The remaining work is maintenance, plus one decision (R2).

## 2. What is on the table

| # | Item | Atlas proposal |
|---|---|---|
| R1 | c′_Q re-check | accept. All 57 gates pass with 0.36916; no printed value changes. Edit five text sites and the part-1b L55 literal; rerun the chain as owner; re-register the hashes |
| R2 | `[assuming: (D5)]` | owner decision: **narrow, not drop**. c_J = 0.50220 and c₇ = 157.58 are still proof-sketch constants without a theorem row. Options: (a) narrow, (b) supply RECOG-side, (c) ask Dyadic |
| R3 | C₇ rows (L662) | accept with change: import `DYAD-THM-NF-REM-C7-SHARP` (same values, chart and norm); update the stale wording at L662, L663 and L771 |
| R4 | claim-audit strings | the v0.3.27 audit quotes the `dyad-v6.4.23` rows; the old scripts stay as they are |
| R5 | OFN v0.11 notice | accept (receipt); the imported OFN sections are unchanged in content at `ofn-v0.12` |
| R6 | pins | Dyadic and NUMGEN repins where a use changes; Genesis and OFN companion pins; every cited RID resolves |

The details, line references and rerun evidence are in `records/recog/ATLAS_ADVISORY_RECOG_INBOX_20261103.md`.

## 3. Read first

1. **The advisory.** §0 is the table, §1 the rerun, §2 the R2 options.
2. **The open items** in `pipes/RECOG/` with `state: open`. There are two.
3. **The Atlas rerun:**
   - `evidence/recog/atlas_review/ra1/ra1_recheck_summary.json`;
   - `ra1_run_note.md`;
   - the driver `recog_ra1_cprime_recheck.py`. Its `run` mode rebuilds both trees from the registered scripts; on the Atlas host this took about 55 minutes per tree.
4. **The Dyadic text at `dyad-v6.4.23` §6.14:**
   - L804: C₇-SHARP;
   - L906: the L-PHASE proof sketch with c_J and c₇;
   - L910: BRIDGE.

## 4. Points that need the owners' own judgement

- **R2.** Which of (a), (b) and (c) to take. (a) fits a maintenance edition. (b) is a new certified cell. (c) waits on Dyadic. Every option keeps the grades; only the source condition changes.
- **R1, the owner rerun.** The Atlas rerun shows the gates pass and the committed outputs reproduce byte for byte. The adopted evidence still has to be RECOG's own run, with the edited script:
  - the new hashes go into `RECOG-ART-A1C-SHARPENED-SCHEDULE`, `-DECODER` and `-DRIFT-CENTERING`;
  - part 1b runs with `argv[2] = 6000000`, as committed.
- **L773 wording.** In the log-free envelope, c′_Q enters only through the start-offset step, not through C(a, r): the proof table does not move. Whether the qualifier there should say so is the owners' call. The Atlas proposes no change.
- **R3, the NC2 control.** Keep "published + 0.005" over 85.07 / 27.60, which is still conservative, or repoint it at the registered exact bounds.

## 5. Suggested working order

This mirrors the Dyadic and Genesis rounds.
1. **Separate dispositions.** Each co-owner writes accept, accept with change, or decline, with the reason, for R1–R6. Then reconcile them into one fixed list, R2 included.
2. **One content stage**, consisting of:
   - assertion-gated edits;
   - the owner chain rerun;
   - a stage-1 checker with negative controls, including the new claim-audit strings of R4;
   - a change-focused co-owner review;
   - an Atlas row check.

   No compaction is needed.
3. **PI adoption, merge and tag** (CONVENTIONS §4: decision → release record → merge → tag).
4. **After the tag:**
   - close the two open items, setting `state` and `disposition` as receiver;
   - file notices to the consumers whose rows change: Dyadic (consumer register), NUMGEN, OFN, RRF, RER and the Atlas;
   - if (c) is chosen, file the request to Dyadic.

## 6. Boundaries

- Nothing here changes RECOG text, grades, RIDs, certificates or pipe states.
- The Atlas rerun replays owner code with one changed input. It is not an owner proof and not an adoption.
- Not part of this round, and none of them blocks it:
  - the research frontier (co-owner review §6): the in-block residual, Q1′, F5/F6, and `K_ε` with the now-registered C₇ = 85.1;
  - RECOG's own open notices in other inboxes.
