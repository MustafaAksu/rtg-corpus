# RTG Dyadic v6.4.23 — release record

**Status:** ADOPTED — PI, 30 October 2026. Final SHA-256 `9f874ccc1cd684482f26a27fca13b37102977cba2a80a75e762ecd7b300425cb` (after the status-lines-only publication transform of the reviewed r2 candidate). Tag `dyad-v6.4.23` to be created by the PI after the merge.

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

## 4. Reviews and decision

| Step | Record | Verdict |
|---|---|---|
| Co-owner change-focused review of r1 (`4d2ae89`, `3de022a7…dd2b`) | PR #132 review `5712270269` | scientific scope ACCEPT (D1–D7); editorial corrections E1–E3 required |
| D7 co-owner disposition | PR #130 comment `6522906761` | ACCEPT |
| r2 (`5894fae`, `5e55602f…d7fb`): E1–E3 applied | this record §3 | — |
| Co-owner delta-only read-back of r2 | PR #132 review `5712364282` | ACCEPT — E1–E3 closed |
| Atlas row check of r2 against `atlas-v0.8` | PR #134, `records/atlas/ATLAS_DYAD_v6_4_23_R2_ROW_CHECK_CHATGPT.md`; PR #132 comment `6523451445` | PASS SCOPED — no Atlas-row blocker; follow-ups for Atlas and RECOG (below) |
| **PI decision** | relayed in the owner session, 30 October 2026, 16:18 (UTC+3): "ben de bu sonuçları benimsiyorum." | **ADOPTED** |

The reviews checked file hashes, the RID inventory and arithmetic independently. The builder, checker, controls and certificate runs are OWNER-RUN; no reviewer reran them.

**Follow-ups noted by the Atlas check (not blockers for this edition):**
- RECOG.R-A1 stays open. RECOG v0.3.26 uses $c'_Q=0.36915$ in conditional computations, and it may drop `[assuming:]` only after its own re-check with $0.36916$.
- The Atlas diagnosis `NUMGEN.N-Q*` (possible identity of the two $q_*$) is to be removed or reclassified at the next Atlas refresh: the two roots differ.

## 5. Publication

**Transform.** `evidence/dyad/scripts/release_dyad_v6_4_23.py` (SHA-256 `3b92d4c3aab5299056b9cea76300d8f35a432986a3b93ca973381a3ea0f28dc6`):
- it asserts the reviewed candidate hash `5e55602f…d7fb`;
- it changes exactly three lines: the header status, the Appendix A heading and the footer;
- the output is deterministic over two runs.

| | SHA-256 |
|---|---|
| Reviewed candidate (r2) | `5e55602fd858c81cdd7400f1d244be1c712e770745c55decd60c28d33b45d7fb` |
| **Adopted v6.4.23** | **`9f874ccc1cd684482f26a27fca13b37102977cba2a80a75e762ecd7b300425cb`** (268 947 bytes) |
| Predecessor v6.4.22 | `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29` (`dyad-v6.4.22`) |

`BASELINE.md`: the DYAD row names v6.4.23 with the final hash.

**Order of the remaining steps (PI), as in CONVENTIONS §4:**
1. Merge the evidence and record PRs that this edition cites (merge commits, not squash):
   - PR #125: uploads, Atlas advisory and reruns;
   - PR #127: co-owner disposition;
   - PR #130: owner disposition, owner checks, reconciliation;
   - PR #134: Atlas row check.
2. Merge PR #132.
3. Create the annotated tag `dyad-v6.4.23` on the merge commit, with the final hash in the tag message.
4. Owner read-back of the tag (hash at the tag equals the value above).
5. After the tag:
   - close the seven `pipes/DYAD/` items and regenerate `INDEX.md`;
   - prepare notices to RECOG (the two RIDs, $c'_Q=0.36916$, the chain correction, the re-check request), NUMGEN (the "no", $q_{3/4}$, the successor RID) and OFN (receipt of v0.11 and v0.12). Notices are routed through the PI.
