# RECOG owner disposition — inbox round after v0.3.26 (Claude co-owner, independent pass)

**Date:** 3 November 2026. **By:** Claude, RECOG co-owner. **To:** the other RECOG co-owner (ChatGPT), for reconciliation; copy to the PI and the Atlas owner.
**Status:** `[SESSION]` owner disposition, one of two independent passes. It decides nothing alone: the two passes are reconciled into one fixed list, and the PI adopts. It changes no RECOG text, grade, RID, certificate, committed output, pipe state or tag.
**Independence:** written without reading the other co-owner's record (PR #169); that record is read at reconciliation.

**Read:** `records/recog/RECOG_OWNER_ENTRY_NOTE_INBOX_20261103.md` and `records/recog/ATLAS_ADVISORY_RECOG_INBOX_20261103.md` (PR #168, branch `claude/atlas-recog-inbox-advisory`, commit `c05067e`); `evidence/recog/atlas_review/ra1/` (driver, run note, summary); the two open items in `pipes/RECOG/`; `recog-v0.3.26` (`45e307f8…dd34`); `dyad-v6.4.23` §6.14 (`9f874ccc…25cb`), lines 799–804, 823–830, 906–910; for R5 and R6 also `ofn-v0.10`/`ofn-v0.12`, `numgen-v1.21`, `gen-v2.8.9`/`gen-v2.10`.

**Own checks** (noncanonical, `evidence/recog/inbox_20261103_claude/`; details in `RUN_NOTE.md`):
- **C1 — rerun with c′_Q = 0.36916.** Six A1c certificates rerun from scratch copies with the one-literal patch (part 1b, start offset, unknown-a interval, in-block angular, combined tail, drift centring). All gates pass. All six patched JSONs are **byte-equal** to the Atlas's patched JSONs (`rerun_summary.json`). Not rerun here: joint transfer and the drift proof table.
- **C2 — the corrected grid, which the Atlas chain does not contain.** `recog_v0_3_26_corrected_grid.py` (artifact RECOG-ART-A1C-CORRECTED-GRID) imports the stack through the drift-centring script, so c′_Q reaches it.
  - Unpatched: it reproduces the committed `corrected_grid.json` byte for byte.
  - Patched: `all_below` stays true; 606 numeric leaves change, by at most 2.5 × 10⁻⁷ relative (in R̄′); no boolean flips; E‴ is unchanged.
- **C3 — the RECOG-side remainder constants.** `recog_inbox_claude_checks.py c7cj` → `c7cj_check.json`. It is a standalone interval recomputation of the two constants that RECOG-ALG-A1C-COMBINED-TAIL already derives RECOG-side (formulas of `recog_a1c_combined_tail_cert.py` L78–84):
  - c_J^R(q*) = 0.5007984…, below Dyadic's c_J = 0.50220. At q = 1/400 the same formula gives 0.5021980…, which is Dyadic's c_J rounded up: both are the same bound, taken on different disks.
  - c_7^R(q*) = 100.2300…, below Dyadic's c₇ = 157.58.
  - Both formulas are increasing in q (checked on a grid; analytically, every term increases with q).
- **C4 — text checks** behind R3–R6: the claim-audit substrings at `dyad-v6.4.23`, the OFN §6.2a/§7.3 diff, RID resolution and declaration lines (results under each item).

## Summary

| # | Item | Disposition |
|---|---|---|
| R1 | c′_Q re-check | **accept with change** — 0.36916 at the five sites and at part-1b L55; owner rerun of the whole chain **plus the corrected grid**; `[COR]` notes; no Appendix B entry |
| R2 | `[assuming: (D5)]` | **(b), in maintenance form.** The two remaining constants are already supplied RECOG-side by the adopted RECOG-ALG-A1C-COMBINED-TAIL. Name that sub-statement as its own RID, cite it, and drop the qualifier at the five sites. Fallback: (a) |
| R3 | C₇ rows | **accept with change** — import DYAD-THM-NF-REM-C7-SHARP, drop the `[assuming:]`, re-word L662/L663/L771; certificate and its NC2 unchanged |
| R4 | claim-audit strings | **accept with change** — the new audit quotes with delimiters, because the old values also occur as prefixes of the new exact displays |
| R5 | OFN v0.11 notice | **accept** (receipt) |
| R6 | pins | **accept with change** — repin every Dyadic pin to `dyad-v6.4.23` (not only where a use changes); NUMGEN, Genesis and OFN as proposed |

All six fit one maintenance edition (v0.3.27) with one content stage. No grade changes.

## R1 — c′_Q = 0.36916: accept with change

**Agreed.** 0.36915 lies below the certified majorant 0.3691523046…, so it is not a ceiling. Every use of c′_Q in the chain enters an upper bound with a positive coefficient:
- in part 1b: the C term of S̄′, and τ̄c′_Q in c_r2 for R̄′;
- in the start offset: β(a);
- downstream of those two.

Raising the value can therefore only enlarge majorants. C1 confirms that no gate is near its threshold.

**Changes to the Atlas proposal:**
1. **Add the corrected grid** to the owner rerun and to the re-registration (C2). With it, the rows whose quoted output hashes change are:
   - RECOG-ART-A1C-SHARPENED-SCHEDULE: the part-1b script, and the part-1b, in-block and combined-tail outputs;
   - RECOG-ART-A1C-DECODER: the start-offset, unknown-a and joint-transfer outputs;
   - RECOG-ART-A1C-DRIFT-CENTERING: the drift and proof-table outputs (scripts unchanged; the proof-table JSON moves only in its import-hash field);
   - RECOG-ART-A1C-CORRECTED-GRID: the JSON.
2. **Marking.** Use a `[COR]` note at each edited site, citing `dyad-v6.4.23` §6.14 `[COR]`: the earlier copy was a nearest-rounded display below the certified majorant. Make no Appendix B entry. No claim is withdrawn. The value 0.36915 was not shown false (the majorant is not the supremum); it was unsupplied as a ceiling. Every printed conclusion is unchanged at its precision.
3. **Owner rerun.** The run that is adopted is RECOG's own, with the edited script in the repository and part 1b at `argv[2] = 6000000`. C1 and C2 are a dry run of it.
4. **By-reference sites.** L1049 (ADMISSIBLE-REGION) and L1053 (JOINT-CONTRACTOR) need no text edit beyond what R2 does to them.

**L773 wording.** Under R2 (b) the question does not arise, because the qualifier goes away. Under the fallback (a), I would not restrict the L773 qualifier to the start-offset step. ENV's proof cites E⁽⁴⁾ and Δ_a as whole statements. The fact that c′_Q does not reach C(a, r) is a property of the present closed forms, not of the statement.

## R2 — `[assuming: (D5)]`: option (b), in maintenance form

**The Atlas reading is right as far as Dyadic goes.** After `dyad-v6.4.23`, c_J = 0.50220 and c₇ = 157.58 still appear only in the proof sketch of DYAD-THM-LPHASE-ROWA-REMAINDER (L906); everything else in "the remainder decomposition with its constants" has an owner theorem row:
- the exact identity, c_Q and c′_Q → DYAD-THM-LPHASE-ROWA-BRIDGE;
- K_Θ = 123/125 → DYAD-THM-OPEN3-SPIRAL-REM, row |z| ≤ 1/20, which RECOG already cites.

**What the Atlas reading misses: RECOG already supplies the two constants.** RECOG-ALG-A1C-COMBINED-TAIL (adopted at v0.3.25, `[ALG]`, no `[assuming:]`) bounds exactly the same two quantities: |Arg(J/z) + τq| and |Arg(F̂/J)|. It does so RECOG-side, from the adopted rows DYAD-ALG-NF6 (μ, a₃₂, a₀₅) and DYAD-THM-NF-REM (C₇ = 100), on RECOG's domain (block base points of starts in U, q ≤ q* = 256/140625):
- c_J^R = 0.5008;
- c_7^R = 100.23.

The text at L759 calls them "RECOG-derived from the explicit jet and C₇".

The certificate computes them in interval arithmetic (G2 gate; the values are in its JSON `G2_constants`); C3 recomputes them independently and finds them increasing in q. Since they lie below 0.50220 and 157.58, the published values that part 1b uses in c_r2 and c_r3 are **valid ceilings by RECOG's own adopted result** on RECOG's domain. The C3 coincidence (c_J^R(1/400) rounds up to 0.50220) shows these are the same bound, not an analogue.

Option (b) therefore needs no new certified cell and no change of any number.

**Proposal for v0.3.27:**
1. **Name the sub-statement as its own RID**, as v0.3.23 did with RECOG-THM-R9-COMPARATOR-INCOMPLETENESS (statement unchanged, new RID). Suggested name: RECOG-ALG-A1C-JET-REMAINDER-BOUNDS, holding |Arg(J/z) + τq| ≤ c_J^R q² and |Arg(F̂/J)| ≤ c_7^R q³ for 0 < q ≤ q*, c_J^R = 0.5008, c_7^R = 100.23.
   - It depends only on DYAD-ALG-NF6 and DYAD-THM-NF-REM.
   - A separate RID avoids a circular `Depends on:` between TAIL-HARMONICS and COMBINED-TAIL; COMBINED-TAIL already depends on TAIL-HARMONICS.
   - Proof pointer: the combined-tail cell and certificate G2.
2. **At the five sites**, replace the `[assuming: …]` by:
   - `[import: … | DYAD-THM-LPHASE-ROWA-BRIDGE]` and DYAD-THM-OPEN3-SPIRAL-REM;
   - a `Depends on:` RECOG-ALG-A1C-JET-REMAINDER-BOUNDS, for c_J ≤ 0.50220 and c₇ ≤ 157.58 on q ≤ q*;
   - at L1049 and L1053, the matching "as RECOG-THM-A1C-SHARPENED-SCHEDULE" pointer.
3. **Evidence.** Add a stage-1 gate (or a two-line check in the claim-audit script) that up(c_J^R(q*)) ≤ 0.50220 and up(c_7^R(q*)) ≤ 157.58. No certificate is changed. Part 1b keeps its literals, so its numbers do not move; only the justification line changes.
4. **The short-form qualifiers change with it.** These are the §1 sentences (`[assuming: Dyadic row-A bridge proof constants (D5)]`, `[assuming: (D5)]`) and the §7 LPHASE row; the string "(D5)" occurs 11 times in `recog-v0.3.26` (L7 header, L43 §1, L180 R6 decoder line, L1049 and L1053 §6.16e, L1044 "no (D5) constant" in a block that never used it, L1335–L1344 Appendix A). The live qualifier occurrences change; L1044 stays; the header line changes only at publication and the Appendix A history lines stay. The stage-1 checker should account for every occurrence. That includes the decoder line of OPEN R6 ("under the (D5) `[assuming:]` of the envelope"), whose wording is checked by gate C24. The R6 status words do not change.

**Effect.** The (D5) source condition is discharged at all five sites: every constant is either an owner theorem row or a RECOG-adopted bound. Grades are unchanged. The known-a chain still keeps its other stated scope: U, row A, branch (B), ≥ 2 usable slips for the decoder.

**Why (b) rather than (a) or (c):**
- (a) would keep a qualifier that RECOG's own adopted text already discharges.
- (c) would ask Dyadic to register something RECOG does not need from Dyadic. An informational item to Dyadic after the tag is still useful: RECOG has certified c_J ≤ 0.5008 and c₇ ≤ 100.23 on q ≤ q*; and the C₇ = 85.1 row would give c_7^R ≤ 85.30 (C3). That is an offer, not a request.

**Fallback, (a).** If the reconciliation judges that leaning on the combined-tail derivation needs its own review, narrow the qualifier instead to `[assuming: c_J = 0.50220, c₇ = 157.58 as published in the proof of DYAD-THM-LPHASE-ROWA-REMAINDER]`, with the BRIDGE and SPIRAL-REM imports as above. Option (b) can then follow as its own small item.

## R3 — the C₇ rows: accept with change

**Agreed.** DYAD-THM-NF-REM-C7-SHARP (`dyad-v6.4.23` L804) registers C₇ ≤ 85.1 on |z| ≤ 1/20 and C₇ ≤ 27.7 on |z| ≤ 1/40, in the chart and norm of NF-REM, with rows not mixed. Those are exactly RECOG's ceilings.

**Scope check.** `recog_b1_l1l2_sharpened_rows_cert.py` uses C₇ only, through K_Φ(C₇, q̄) with q̄ = 1/400 and 1/1600, that is |z| ≤ 1/20 and 1/40. It does not use C_D, so Dyadic's caveat that the C_D bounds were not re-derived does not reach it.

**Changes:**
- **L662:** `[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.23 §6.14 | DYAD-THM-NF-REM-C7-SHARP]` replaces the `[assuming:]` and its sentence "certificate values 85.07 / 27.60 rounded up; these are not Dyadic theorem statements; registration requested".
- **L663:** "any claim about C₇ beyond Dyadic's published values" becomes "beyond DYAD-THM-NF-REM and DYAD-THM-NF-REM-C7-SHARP".
- **L771 (K_ε, *Not supplied*):** "the registered ceiling C₇ ≤ 85.1 (DYAD-THM-NF-REM-C7-SHARP) would lower it; not applied in this edition". Applying it to γ₂ and K_ε is new science, not maintenance.
- **§7:** add the C7-SHARP row.

**Certificate unchanged; no rerun.** NC2 ("published + 0.005" over 85.07 / 27.60) stays conservative, since 85.075 > 85.0732… and 27.605 > 27.6022…. Repointing it would change a registered script hash for no gain.

One stale sentence for the release record, not an edit: the script's docstring says the ceilings are "≥ published value + 0.03". Against the exact bound, 85.1 − 85.0732 = 0.027, so the docstring is accurate only against the old display 85.07. The proof does not use that margin.

## R4 — claim-audit strings: accept with change

**Agreed** that the past audit scripts stay as they are and that the v0.3.27 audit quotes the new rows.

**Correction to the advisory's explanation (C4).** At `dyad-v6.4.23` the old substrings occur not only in Dyadic's two `[COR]` sentences but also as **prefixes of the new exact displays**:
- "85.07" in "85.0732" (L799, L804);
- "27.60" in "27.6023" (L800);
- "0.36915" in "0.3691523046…" (L910).

The checks "pass for the wrong reason" in more places than the advisory says.

**Change.** The v0.3.27 audit quotes with delimiters, for example `c'_Q=0.36916$`, `$C_7=85.1$ on` and `$C_7=27.7$ on`. It adds one negative control: no RECOG `[assuming:]` or `[import:]` text may contain 0.36915 outside a `[COR]` note. The RECOG checker controls that quote RECOG's own qualifier (NC23 of `check_recog_v0_3_26_stage1.py`, NC22 of v0.3.25) are rewritten together with that text.

## R5 — OFN v0.11 notice: accept (receipt)

**Verified (C4).** Between `ofn-v0.10` and `ofn-v0.12`, §6.2a ("Minimal Constraint List for T") and §7.3 ("Antipodal Band and Width Parameter") have identical headings and line counts. Their only changes are OFN's own import pins and RIDs:
- RECOG v0.3.20 → v0.3.26;
- TDR-G v2.12.13 → v2.12.14, with TDRG-ALG-LEM-RETRIG and TDRG-THM-NARROW-BAND-EXCLUSION filled in;
- one sentence recording OFN08-C12 as fulfilled.

The rows RECOG cites (the radial rows; band k) are unchanged in content. The OFN companion pin moves to `ofn-v0.12` in v0.3.27.

## R6 — pins: accept with change

**Verified (C4):**
- **Dyadic.** All 27 Dyadic RIDs RECOG cites resolve at `dyad-v6.4.23`. (29 matches, less the fragments `DYAD-RADIAL` of NUMGEN-N1C-DYAD-RADIAL and `DYAD-W` of RRF-DYAD-W.) Their `[RID: …]` declaration lines are byte-identical to `dyad-v6.4.22`.
- **NUMGEN.** All 11 cited RIDs resolve at `numgen-v1.21`; the claim-difference audit is in the co-owner review of 29 Oct, §3.
- **Genesis.** The two cited RID lines (GEN-DEF-PRIMITIVE-METRIC, GEN-THM-PRIMITIVE-METRIC-INVARIANCE) are byte-identical between `gen-v2.8.9` and `gen-v2.10`.

**Change against "repin where a use changes":** repin **every** Dyadic pin to `dyad-v6.4.23`. Since every declaration line is unchanged, this costs only the citation. It keeps one Dyadic edition across §6.13a/b, §6.16e and §7, so the next audit compares one pair of tags, not two. Add the two new RIDs (BRIDGE, C7-SHARP) to §7. Everything else as proposed:
- NUMGEN: the citation micro-edit, with GAP-LOCK Lemma 3 by NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO and the two-grade row (inbox finding of 26 Oct);
- Genesis and OFN: companion pins;
- TDR-G: none (reference only).

## The two open inbox items — proposed dispositions (state unchanged now)

| Item | Proposed disposition, set after the tag |
|---|---|
| `pipes/RECOG/20261030-DYAD-v6-4-23-adopted.md` | accept with change · the v0.3.27 release record (R1 with C2, R2 (b), R3) |
| `pipes/RECOG/20261030-OFN-v0-11-adopted.md` | accept · the v0.3.27 release record (R5) |

**Notices after the tag** (entry note §5.4):
- Dyadic: consumer register; the (D5) qualifier dropped; the informational offer of R2;
- NUMGEN, OFN, RRF, RER, Atlas: changed rows and pins.

## Boundaries

- No RECOG text, grade, RID, certificate, committed output, pipe state or tag is changed by this record. The evidence folder `evidence/recog/inbox_20261103_claude/` is noncanonical session evidence.
- R2 (b) as proposed adds one RID that restates an adopted computation. It introduces no new statement and changes no number. Whether that counts as maintenance is for the reconciliation and the PI to confirm.
- Not part of this round: K_ε or c_7^R with C₇ = 85.1; the in-block residual; Q1′; F5/F6.
