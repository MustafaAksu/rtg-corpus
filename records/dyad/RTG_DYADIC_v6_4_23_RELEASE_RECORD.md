# RTG Dyadic v6.4.23 — release record

**Status:** CANDIDATE — awaiting the change-focused co-owner review, the Atlas row check and the PI's decision. Not adopted. This record is completed at adoption; until then it states what the candidate is and how it was built and checked.

## 1. Candidate

| Item | Value |
|---|---|
| File | `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` on branch `claude/dyad-v6.4.23` |
| Candidate SHA-256 | `3de022a7fb76d65473776cd759abd90f47b7a0b9a0f1924be0ea56830663dd2b` |
| Base | `dyad-v6.4.22`, `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29` |
| Scope | joint reconciliation `records/dyad/DYAD_INBOX_20261030_RECONCILIATION.md` (D1–D6 accepted by the co-owner, PR #130 comment `6522082716`; the D7 addendum awaits co-owner confirmation) |
| Kind | single stage, no compaction; 49 assertion-gated edits; three result RIDs and one artifact RID added; no existing RID, grade or OPEN status changed |

## 2. Content

- **D1:** successor `DYAD-THM-OPEN18-STEP-MONOTONE` (§6.8).
  - `DYAD-THM-OPEN18` keeps its text and grade with the scope note agreed in reconciliation §7.
  - The status summary, §1 and §2 cite the successor.
  - §8 DYAD-ART-OPEN18 carries the recovered file hash.
  - Appendix E rows are added for the successor.
- **D2:** `DYAD-THM-NF-REM-C7-SHARP` (§6.14); `[COR]` of the NF-REM table displays.
- **D3:** `DYAD-THM-LPHASE-ROWA-BRIDGE` (§6.14); `[COR]` of the displayed chain in the L-PHASE proof outline; the two "certificate value" displays (§2 table, §7.0a).
- **D4–D7:** the §7.0 rows, the §7 context and consumer lines, and the notice-receipt rows N4, N6, N14 (OFN) and N15 (NUMGEN).
- **Edition lines and Appendix A entry.**

## 3. Build and checks (OWNER-RUN, 30 October 2026)

Builder `evidence/dyad/scripts/build_dyad_v6_4_23.py`, SHA-256 `885ea6d109422b403b90110fc63b1cfa3fe8092b1685f24cd231f7f598059777`. Command:

```
python -I -B evidence/dyad/scripts/build_dyad_v6_4_23.py <v6.4.22 file> <out> <editlog.json>
```

The rebuild is byte-identical to the committed candidate.

Checker `evidence/dyad/scripts/check_dyad_v6_4_23.py`, SHA-256 `a0374682df6927f525d10e5f7cafea13cc67e107e295e7734195a39178713f41`: C0–C9 ALL PASS. The gates check:
- the identities;
- determinism;
- confinement by reverse application of every edit, which recovers the base byte for byte;
- RID, grade and math-span invariants;
- that the corrected displays are gone outside the `[COR]` lines;
- the D1 wording;
- the edition lines;
- the §2 Status lines;
- the cited evidence, including a rerun of the chain check and its control;
- the D7 identity (sympy).

Controls `evidence/dyad/scripts/check_dyad_v6_4_23_controls.py`, SHA-256 `84523d9c67e8d58785934bd272c7b40aa74bfcea35679a42db0e8a6607f16758`: Q1–Q9 all as expected, each failing its target gate.

Outputs are in `evidence/dyad/v6.4.23/`: the edit log, the check and control JSONs, stdout, and the `dsn_lint` report (informational: +3.7 % bytes, 4 new RIDs).

Evidence cited by the candidate: `evidence/dyad/inbox-20261030/` (owner checks O1–O7, L1–L3, OPEN 18 C++ owner rerun).

## 4. Decisions (to be completed)

- Change-focused co-owner review: pending. It includes the confirmation of D7.
- Atlas row check: pending.
- PI decision: pending.
- After adoption: a status-lines-only publication commit (header, Appendix A heading, footer) gives the final hash; then merge (merge commit) and the annotated tag `dyad-v6.4.23` by the PI; then the pipe items are closed and the notices to RECOG, NUMGEN and OFN are prepared.
