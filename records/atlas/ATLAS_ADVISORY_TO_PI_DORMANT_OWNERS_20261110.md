# Atlas advisory to the PI — findings whose owner streams are not in the maintenance sequence

**Date:** 10 November 2026. **By:** Claude, Atlas owner. **Status:** [SESSION] advisory. The Atlas owner advises and does not decide; no DSN is edited by the Atlas; nothing here is adopted.
**Basis:** `atlas-v0.11` (`8d7a43f0…f358`), HEADLINE items H2, H3, H11 and their L5 keys. Each row was spot-checked today against the owner file at its tag (`az-v0.6`, `dzt-v0.8`, `uvm-v0.7.1`; each equal to `main`); `legacy-v0.7` and `prelegacy-v0.8` were **not** reread for this note (rows 4 and 5 rest on the Atlas diagnostics: UNVERIFIED today).
**Why to the PI:** Method §7 sends advisories to stream owners. Programme v1.4 §9.2 records the maintenance sequence as not executed for Pre-Legacy, DZT and AZ (PROG.G6); Legacy is a historical source. For these rows there is no active owner session to answer, so the disposition is the PI's.

## 1. Rows

| # | Atlas key | Owner, place | Observation | Smallest fix | Kind |
|---|---|---|---|---|---|
| 1 | H2, AZ.A1 (D-WRONG) | AZ v0.6 §6 "To OPEN M" (DSN line 440) | States "the legal correction is ×2, not ×4; applying ×4 is a certified dimensional type error under AUDIT-1-DIMENSIONAL in the OPEN-M ledger". OPEN-M v0.7.1 says "no certified deficit factor" (DSN line 104) and withdrew the 2× verdict (R16). A canonical DSN therefore still asserts, as certified, a verdict its source withdrew. | AZ: replace the sentence by a pointer to OPEN-M v0.7.1 R15/R16 ("no certified deficit factor; the 2× branch is superseded"). | scientific (a claim is withdrawn) |
| 2 | H3, DZT.Q1 | DZT v0.8 §7 and body (DSN lines 53, 82, 247, 260, 301, 304, 313, 319) | Cites strings that are not Dyadic owner RIDs: DYAD-THM-Q403-PHASE-ALLP, DYAD-ALG-PHASELAW, DYAD-CF-Q403, DYAD-ART-CASCADE-Q4-03, and others listed in DZT.Q1. Dyadic Appendix F classifies each and creates no alias. | DZT: repin to DYAD-THM-Q403-PHASELAW and DYAD-ART-Q403-EXTRACT as Appendix F states; the p=12 value has no RID and stays a named value. | editorial (identifiers) |
| 3 | H3, AZ.A7 | AZ v0.6 (three occurrences of the two strings) | Cites DYAD-ALG-Q3-CANCEL (owner: DYAD-ALG-Q3-DEG2-CANCEL) and TDRG-ZN-STATE (owner: TDRG-DEF-ZN-STATE); AZ-side labels BIND3-*, TDR-24/26 are AZ's to repin. | AZ: repin. | editorial (identifiers) |
| 4 | H11, OPENM.U9 ≡ LEGACY.Y2 | OPEN-M v0.7.1 R12 (DSN line 271) | "the Legacy cooled-vacuum 0.403": per the Atlas reading the value is Pre-Legacy's (grown N=175, η_irr). Attribution only; the number is not disputed. | OPEN-M: cite Pre-Legacy v0.8. | editorial (attribution); PREL side UNVERIFIED today |
| 5 | H11, LEGACY.Y3, PREL.P4 | Legacy v0.7, Pre-Legacy v0.8 | (a) Legacy's "Hodge ≈75.2 % curvature variance" coincides with Pre-Legacy's N=14 seed-floor η_irr; identity not shown. (b) "Δ=0.5" is the signed δ_P; Legacy's δ_L=1−t gives 0 for the same holonomy. | (a) a producer check, or the labels stay as two readings; (b) every downstream "0.5" names its convention. | (a) scientific, open; (b) convention |

Open pipe notices that already sit in these inboxes and concern the same repins: `pipes/AZ/` (TDR-G v2.12.14; Dyadic notices n16–n21), `pipes/DZT/` (Dyadic n16–n21), `pipes/UVM/` (four items). They are unanswered because no owner session runs.

## 2. What deferring costs

- **Row 1** is the only row where a canonical DSN asserts something its source has withdrawn. The Atlas blocks it (D-WRONG, not a node), and Programme does not adopt the "2× short" headline, so no adopted result depends on it. The cost of deferring is that a reader of AZ alone is misled.
- **Rows 2–3**: no science is wrong. The cost is 11 documented-unresolved links in every Atlas check and consumer strings that cannot be resolved mechanically.
- **Row 4**: an attribution error between two historical sources.
- **Row 5**: (a) stays an open identification, guarded in the Atlas by `~`; (b) is a live trap for anyone reusing "0.5".

"Accept the recorded state" for any row means: the debt is known and stays, the Atlas diagnostic remains its guard. It does not resolve the row.

## 3. Advice

The PI has said the remaining streams (AZ and others) will be reworked. Under that plan:

1. **Row 1 first.** When AZ is opened, make this the first correction, or, if AZ's rework is not near, a one-sentence corrections edition `az-v0.7` now. It is small and it is the only scientific row.
2. **Rows 2–4 ride with each stream's rework** (DZT, AZ, OPEN-M), as part of answering the open pipe notices. Not worth separate editions.
3. **Row 5 stays recorded** until Pre-Legacy is opened; (b) could be one line in a Legacy/Pre-Legacy source-maintenance pass.

## 4. Disposition asked of the PI, per row

For each row one of: **fix now** (own small edition of the owner DSN, through that stream's release cycle), **with the stream's rework**, or **accept the recorded state** (deferred debt). The Atlas is refreshed from the adopted result; it changes nothing before that.

| # | Disposition | Date |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
