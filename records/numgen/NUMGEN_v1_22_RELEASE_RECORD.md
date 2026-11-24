# Number Genesis v1.22 — Release Record

**Status:** DRAFT. Not adopted. `numgen-v1.21` governs until the PI adopts v1.22 and tags it.
**Date:** 24 November 2026.
**Prepared by:** Claude, Number Genesis co-owner session. Branch `claude/numgen-v1.22`, stacked on PR #375, which is stacked on PR #374.
**Edition:** v1.22, one content stage: receiving and synchronization. No layout change, so no stage 2 (Methodology v1.4 §13.6).
**Predecessor:** `RTG_NUMBER_GENESIS_DSN_v1.21`, tag `numgen-v1.21`, SHA-256 `4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701`.

Fields marked *(to be filled)* depend on steps that have not happened yet. This record invents no hash, approval or review identifier.

## 1. Authorization and reviews

| Item | Source | State |
|---|---|---|
| Atlas sync advisory, rev. 2 | `records/numgen/ATLAS_ADVISORY_NUMGEN_SYNC_20261123.md` (PR #372, merged); atlas-owner readback ACCEPT, comment `7113435416` | merged |
| Owner disposition (Claude) | `records/numgen/NUMGEN_OWNER_DISPOSITION_SYNC_20261123_CLAUDE_20261124.md` (PR #374): ACCEPT SCOPED; v1.22 one content stage | filed; not merged |
| Co-owner review and GO for S1 | ChatGPT co-owner, 24 Nov 2026, as given to this session by the PI: v1.22 ACCEPT SCOPED; S1 GO with acceptance criteria 1–7 | given |
| S1 evidence | `records/numgen/NUMGEN_v1_22_S1_P2_REANNOTATION.md` (PR #375) | filed; not merged |
| Co-owner review of S1 and GO for S2–S3 | ChatGPT co-owner on PR #375, comment `7128043448` (commit `7bb2f63`): ACCEPT SCOPED. Independent recheck: 10/10 manifest hashes and 158 annotation records. Three abbreviation errors, fixed as errata in commit `062ec86` | given |
| Co-owner review of the v1.22 build | *(to be filled)* | pending |
| Atlas row check | *(to be filled)* | pending |
| PI adoption | *(to be filled)* | pending |

## 2. Identities

| Object | SHA-256 |
|---|---|
| Base: `numgen-v1.21` (274,246 bytes) | `4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701` |
| **Candidate** `dsn/RTG_NUMBER_GENESIS_DSN.md` (280,405 bytes, 2,990 lines) | **`8ccc8e38f0ad054d68f59bf5d95c9364afa093f02cb3e418295625db3763148a`** |
| Published file (after the publication transform) | *(to be filled)* |
| Tag `numgen-v1.22` | *(to be filled by the PI)* |

| Build or check file | SHA-256 |
|---|---|
| `evidence/numgen/scripts/build_numgen_v1_22.py` | `7bce47b21a770bb8e4363c003cd0cf52acfcc1dd19a453da0326959ee0c4ebd9` |
| `evidence/numgen/scripts/check_numgen_v1_22.py` | `4212e61c6fb9ce3a1b5ff238c766cc8d0daab33119edcb0f1e4d0ca4358cf9f7` |
| `evidence/numgen/v1.22/edit_log.json` (35 edits) | `f1f31c63ffed15b8ddd6e99f42c6ba6861c94c93e463b29feff5b88859265462` |
| `evidence/numgen/v1.22/check_output.txt` (C0–C9 PASS) | `9745d4aea7445dd492fd8948840e31c77cadcaed094f351799dc3c565a2afadc` |
| `evidence/numgen/v1.22/negative_controls_output.txt` (NC1–NC11 caught) | `b8b038d550c87cd8177a609cbda6dfb0339acb48a933b1a0bc01cf9a10af84cd` |
| `evidence/numgen/v1.22/dsn_lint.txt` (informational) | `dde570e2cfcbb01e6a5cbbb0b30f0130d78ab4e434831ae7be848c5ba5bd9138` |
| `records/numgen/NUMGEN_v1_22_RECEIVING_LEDGER.md` | `1f1cc2c621fc608404490a66bede629de9c7fe79737d773d7687a7013cc9a08a` |
| S1: script / annotation / manifest | `4c5c2f17…8ae9` / `1819015a…3524` / `3981cfe6…67dc` |

**Reproduce:**
1. `git show numgen-v1.21:dsn/RTG_NUMBER_GENESIS_DSN.md > v.md`
2. `python3 -I evidence/numgen/scripts/build_numgen_v1_22.py v.md OUT LOG` gives `8ccc8e38…148a`.
3. `python3 -I evidence/numgen/scripts/check_numgen_v1_22.py v.md OUT LOG --root .`, and again with `--controls`.

## 3. Edits by group

The edit log has 35 entries. Each replaces one exact substring that occurs exactly once, in order, and each is reversible (gate C2).

| Group | Keys | Change |
|---|---|---|
| Header | H1–H5 | title v1.22; Date 24 November 2026; Document status DRAFT; Supersedes v1.21 with its hash and tag; Release record |
| P01: TDR-G RIDs | I1–I3, L2, C3 | §1.1 state-space and recurrence imports repinned to `tdrg-v2.13` with `TDRG-DEF-ZN-STATE`, `TDRG-DEF-PHYSICAL-STATE` and `TDRG-THM-RECURRENCE` (statements byte-identical to v2.12.13 apart from the RID tag; checked). The firewall stays a guard citation without RID (SG-10 and SG-PROG-1 checked identical at `tdrg-v2.13` and `programme-v1.4`). §9.1 rows. |
| F1: C7C-M4 hold | Q1, Q2, P5, R1 | §2 item 1 and §6.6: the P2 policy is answered (`TDRG-DEF-ORIENT`), and the consumer re-annotation is recorded. **M-4 stays HOLD.** The reason is the missing composable chain: the Census-1 universe is all `(SWAP, P3)`. Next comes a non-degenerate composable-chain construction; Census-2 needs its own preregistration. |
| F1/F2: P2 audit, S1 | P1–P4 | §6.6 DISC-2 summary, DISC-1 evidence, DISC-2 evidence, the P2 guard, and the new `[NUM]` block "P2 re-annotation under TDRG-DEF-ORIENT (v1.22 S1)". "DISC-1 requires the same audit" (two sites) is replaced by the scoped result. |
| F3: q* | Z1 | §6.2: `q_*` is not Dyadic's `q_{3/4}` (`DYAD-THM-OPEN18-STEP-MONOTONE`, `dyad-v6.4.24` §6.8). This closes NC-17. Scan-resolution qualifications are kept. |
| F5: DZT | D1 | §8 `[PROVENANCE]`: the v0.17 files are received history and not lineage; the governing edition is `dzt-v0.19`; `DZT-THM-CASCADE-NORM-LAW` is cited as a locator only. NUMGEN still imports nothing from DZT. |
| Pins and consumers | L1, L3, L4, C1, C2, C4–C9 | §9.1: dispositions table (six v1.22 rows); current companions Dyadic v6.4.24, TDR-G v2.13, OFN v0.12, Programme v1.4, Genesis v2.10, RECOG v0.3.27; pins used unchanged where the statement is unchanged; RECOG export row with the two-grade GAP-LOCK 3 use; OFN export row (REQ-O09-03; N-1A2 vocabulary only); **new export row Genesis** (`NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE`, IF38); Genesis import row IF37 |
| S1 evidence | R2 | §9.2 artifact row for the S1 record and evidence |
| Hash form | X1 | §9.2 RECOG v0.3.24 hash written `8c64bea2…e7c1` (was a six-character suffix; v1.21 release record §14, atlas note on E42) |
| History | A1, F1 | Appendix A v1.22 entry; footer |

The tag census (gate C3) changes exactly by `[NUM] +2`, `[scope: …] +1` and `[conv: …] +1`:
- the S1 `[NUM]` block with its scope and convention tags;
- the `[NUM]` status label of the new §9.2 artifact row.

No other grade tag changes. No edit lowers OPEN, CLOSED or INCONCLUSIVE (C4). No NUMGEN RID is added or removed. The seven newly cited external RIDs are each declared at the tag the text names (C5).

## 4. Checks

| Check | Evidence key | Result |
|---|---|---|
| `check_numgen_v1_22.py` C0–C9 (base, build, reverse, tags, status, RIDs, header, tags exist, paths, hash abbreviations) | EV-RUN | PASS |
| Negative controls NC1–NC11, each caught by a substantive gate besides C1 | EV-RUN | all caught |
| `tools/dsn_lint.py` | EV-RUN | informational; history phrases as at v1.21 |
| `tools/pipes_index.py --check` | EV-RUN | OK |
| S1 re-annotation (G1–G7) | EV-RUN | PASS, with independent co-owner recheck (comment `7128043448`) |
| N-5, C7A, DISC and Census-1 campaigns | EV-NOT-RERUN | not rerun |

## 5. Pipe items

- Inbound: the eleven notices are dispositioned on this branch (`records/numgen/NUMGEN_v1_22_RECEIVING_LEDGER.md`). They are closed after the tag.
- Outbound: none filed. The four items of 26 Oct 2026 are closed by their receivers.

## 6. Affected consumers (notices after the tag)

| Consumer | What changes for them |
|---|---|
| TDR-G | §1.1 imports cite their RIDs at `tdrg-v2.13`; consumer re-annotation under TDRG-DEF-ORIENT (20/136; DISC-1 0/22); M4 still HOLD, for a NUMGEN-side reason |
| Genesis | export row IF38 recorded (`NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE`) |
| RECOG | consumer row with the two-grade GAP-LOCK 3 use; A1c comparison only |
| Dyadic | `q_*` / `q_{3/4}` disambiguation; NC-17 closed |
| OFN | consumer row (REQ-O09-03; vocabulary only) |
| DZT | §8 provenance updated; no import |
| Programme | companion v1.4; pins used unchanged |

## 7. Live-file exceptions kept on purpose

These are unchanged from v1.21 §6 and are not part of this scope:
- the LOGSLIP block (NA-06);
- the dated `[v1.20.x]` markers in untouched rows;
- the §1 profile exception.

The §9.1 TDR-G import ledger row still says the per-cycle enumerator is "pending in accessible corpus". The enumerators are now in `upload/numgen-records/`, but that row is not in the reconciled v1.22 scope. It is left for the next edition.

## 8. Not done

- No new import.
- No grade or OPEN change.
- No reopening of Census-1.
- No M4.
- No DISC-3.
- No compaction.
- No merge and no tag by this session.

## 9. Remaining steps

1. Co-owner review of the v1.22 build.
2. Atlas row check.
3. PI adoption.
4. Publication transform (status lines only).
5. PI merge (#374 → #375 → v1.22 PR) and tag `numgen-v1.22`.
6. Notices (§6) and closure of the eleven inbox items.

*END OF RECORD.*
