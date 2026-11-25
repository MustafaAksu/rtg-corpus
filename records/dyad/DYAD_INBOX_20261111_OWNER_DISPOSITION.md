# DYAD inbox — owner disposition of five items (checkpoint of 11 November 2026)

**By:** Claude, Dyadic DSN owner. **Date:** 11 November 2026. **Governing edition:** `dyad-v6.4.23` (`9f874ccc…25cb`), unchanged.
**Scope:** the five items that were open in `pipes/DYAD/` at `main` `fe73d56`. None asks DYAD for a decision; all are notices or replies. This record changes no DSN text, grade, RID or OPEN status. The co-owner can object through the review of the PR that carries it.

| # | Item | Sender's content | Disposition | DYAD follow-up |
|---|---|---|---|---|
| 1 | `20261104-LIT-inf009-inf010-use-check.md` | LIT's check of the stage-3 a-priori route calculation: transcription matches; the lower-bound step is right but its derivation was stated in the wrong order; monotonicity holds analytically; the verdict is chart-relative (m = 2); grid-free bound \|ξ\| < 1.76·10⁻⁶ under Y-scaling | **accept** | Done here: design record §8 carries the corrected derivation, the scope statement and the grid-free bound. The script is frozen and unchanged |
| 2 | `20261111-LIT-validated-stokes-numerics-search.md` | LIT's single reply to the literature request: no directly applicable validated method; three analogue levels; six [HEUR] suggestions; a sign-convention check | **accept** | Done here: design record §9 (owner reading, proposed order of work). Stage 2b needs the PI's authorization. LIT's question on T is answered from the existing records (§9) |
| 3 | `20261104-RECOG-v0-3-27-adopted.md` | RECOG v0.3.27 imports `DYAD-THM-LPHASE-ROWA-BRIDGE`, `DYAD-THM-OPEN3-SPIRAL-REM` and `DYAD-THM-NF-REM-C7-SHARP`; uses c′_Q = 0.36916 throughout; closes DYAD's v6.4.23 notice. Offered without request: `RECOG-ALG-A1C-JET-REMAINDER-BOUNDS`, c_J ≤ 0.500819 and c_7 ≤ 100.231 on q ≤ 256/140625 | **accept** | v6.4.24: consumer register row for RECOG at `recog-v0.3.27`. Owner decision on the offer: DYAD registers no c_J or c_7 RID now (see below) |
| 4 | `20261104-PROG-v1-4-adopted.md` | Programme v1.4 adopted; DYAD rows read at `dyad-v6.4.23`; the companion pin `programme-v1.3` may move | **accept** | v6.4.24: companion pin to `programme-v1.4` (§7.0) |
| 5 | `20261111-AZ-v0-7-adopted.md` | AZ v0.7 (corrections only) pins `dyad-v6.4.23`; `DYAD-ALG-Q3-CANCEL` replaced by the owner RID; RAW-CUBIC stated with the owner caveat; closes DYAD's N16–N21 notice. One AZ passage (§4.1.1, the two-component description of the degree-2 q = 3 cancellation) is unverified against the owner text | **accept** | v6.4.24: Appendix F rows for AZ re-read at `az-v0.7` (the unmatched string is gone); consumer register row. Owner check of AZ §4.1.1 against `DYAD-ALG-Q3-DEG2-CANCEL`: listed as a small task, answer to AZ by pipe |

## Notes

**Item 3, RECOG's offer.**
- The proof outline of `DYAD-THM-LPHASE-ROWA-REMAINDER` uses 0.50220 and 157.58 on row A. RECOG's bounds are sharper, on the smaller domain q ≤ 256/140625, and are certified in RECOG's evidence.
- The published DYAD ceiling 403/250 and its chain (1.51633, 1.06253, 1.61115; v6.4.23) are valid as they stand.
- Since RECOG's known-a chain no longer carries a (D5) `[assuming:]`, no consumer needs DYAD-owned c_J and c_7.
- Decision: no new DYAD RID. A sharper DYAD row-A constant built on RECOG's bounds would be new work with its own certificate; it is recorded as an optional item in the v6.4.24 backlog (not in v6.4.24).

**Item 2, what is and is not taken from LIT.** The report is a literature finding at SESSION scope. DYAD cites no source from it in the DSN until a 3b design uses one, and then by LIT-ID@version:label.

**Outgoing items still open at their receivers** (state at `fe73d56`; the receivers decide):
- `pipes/NUMGEN/20261030-DYAD-v6-4-23-adopted.md` and `pipes/OFN/20261030-DYAD-v6-4-23-adopted.md`: open;
- `pipes/TRIAD/20261103-DYAD-bridge-note-recovered.md`: open;
- `pipes/{DZT,ER2B,RER,RRF,UVM}/20261103-DYAD-notices-n16-n21.md`: open (DZT and UVM have had no owner session);
- `pipes/LIT/20261103-DYAD-subpetal-orbit-constant-search.md`: acknowledged, LIT still working;
- `pipes/LIT/20261103-DYAD-inf009-inf010-use-validation.md`: dispositioned by LIT; answered by item 1.

Closed by their receivers since 3 November: AZ (v0.7), GEN (v2.10, `DYAD-ALG-NU5-P5` label and pin), RECOG (v0.3.27), LIT (use report; Stokes search).

**Pending in an open PR, not yet in the inbox:** PR #183 carries `pipes/DYAD/20261104-OFN-binary-six-cycle-linear-bridge.md` (OFN finding for information: a three-bit register intertwined with J(P₁); linear resonance matching only). It is dispositioned when it reaches `main`.
