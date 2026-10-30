# RTG Dyadic v6.4.23 — release record

**Status:** CANDIDATE — awaiting the change-focused co-owner review, the Atlas row check and the PI's decision. Not adopted. This record is completed at adoption; until then it states what the candidate is and how it was built and checked.

## 1. Candidate

| Item | Value |
|---|---|
| File | `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` on branch `claude/dyad-v6.4.23` |
| Candidate SHA-256 | `5e55602fd858c81cdd7400f1d244be1c712e770745c55decd60c28d33b45d7fb` (r2, after the co-owner's editorial corrections E1–E3; r1 was `3de022a7…dd2b`, commit `4d2ae89`) |
| Base | `dyad-v6.4.22`, `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29` |
| Scope | joint reconciliation `records/dyad/DYAD_INBOX_20261030_RECONCILIATION.md` (D1–D6 accepted by the co-owner, PR #130 comment `6522082716`; D7 accepted by the co-owner, PR #130 comment `6522906761`) |
| Kind | single stage, no compaction; 52 assertion-gated edits; three result RIDs and one artifact RID added; no existing RID, grade or OPEN status changed |

## 2. Content

- **D1:** successor `DYAD-THM-OPEN18-STEP-MONOTONE` (§6.8).
  - `DYAD-THM-OPEN18` keeps its text and grade with the scope note agreed in reconciliation §7.
  - The status summary, §1 and §2 cite the successor.
  - §8 DYAD-ART-OPEN18 carries the recovered file hash.
  - Appendix E rows are added for the successor.
- **D2:** `DYAD-THM-NF-REM-C7-SHARP` (§6.14); `[COR]` of the NF-REM table displays.
- **D3:** `DYAD-THM-LPHASE-ROWA-BRIDGE` (§6.14); `[COR]` of the displayed chain in the L-PHASE proof outline; the two "certificate value" displays (§2 table, §7.0a).
- **D4–D7:** the §7.0 rows, the §7 context and consumer lines, the notice-receipt rows N4, N6, N14 (OFN) and N15 (NUMGEN), and the NUMGEN import state at its points of use in §6.14 and §7.0a (E1).
- **Edition lines and Appendix A entry.**

## 3. Build and checks (OWNER-RUN, 30 October 2026)

Builder `evidence/dyad/scripts/build_dyad_v6_4_23.py`, SHA-256 `4d8f8150add23a3707907bcb3597c93f08e961cfe5bde87a2e059514673690a7`. Command:

```
python -I -B evidence/dyad/scripts/build_dyad_v6_4_23.py <v6.4.22 file> <out> <editlog.json>
```

The rebuild is byte-identical to the committed candidate.

Checker `evidence/dyad/scripts/check_dyad_v6_4_23.py`, SHA-256 `83b74df35a31503c2d5f7e15adcefa0967c87bd8c08e52fdffda0ae8f692d859`: C0–C9 ALL PASS. The gates check:
- the identities;
- determinism;
- confinement by reverse application of every edit, which recovers the base byte for byte;
- RID, grade and math-span invariants;
- that the corrected displays are gone outside the `[COR]` lines;
- the D1 wording, and that the stated interval for $q_{3/4}$ contains the O1 enclosure (numerical, not by string);
- the edition lines;
- the §2 Status lines;
- the cited evidence, including a rerun of the chain check and its control;
- the D7 identity (sympy).

Controls `evidence/dyad/scripts/check_dyad_v6_4_23_controls.py`, SHA-256 `892eb4068f42424dfa073787d05754823fede89a113adce7a80ad598e5c6438e`: Q1–Q11 all as expected, each failing its target gate. Q8 now narrows the interval so that it excludes the root (fails C5 numerically); Q10 widens it, which stays outward and is caught as an unlogged alteration (C2); Q11 restores a superseded NUMGEN wording (C4).

Outputs are in `evidence/dyad/v6.4.23/`: the edit log, the check and control JSONs, stdout, and the `dsn_lint` report (informational: +3.8 % bytes, 4 new RIDs).

Evidence cited by the candidate: `evidence/dyad/inbox-20261030/` (owner checks O1–O7, L1–L3, OPEN 18 C++ owner rerun).

## 4. Decisions (to be completed)

- Change-focused co-owner review of r1 (PR #132 review `5712270269`): scientific scope ACCEPT, D7 ACCEPT; editorial corrections E1–E3 required, applied in r2:
  - E1: the NUMGEN import state is now current at §6.14 (iii), the §6.14 boundary list and §7.0a GAP-LOCK;
  - E2: the NF-REM `[COR]` names $27.60$ as well;
  - E3: Q8 is a real non-enclosing interval, and the checker tests the interval numerically.
- Delta-only read-back of r2 by the co-owner: pending.
- Atlas row check: pending.
- PI decision: pending.
- After adoption: a status-lines-only publication commit (header, Appendix A heading, footer) gives the final hash; then merge (merge commit) and the annotated tag `dyad-v6.4.23` by the PI; then the pipe items are closed and the notices to RECOG, NUMGEN and OFN are prepared.
