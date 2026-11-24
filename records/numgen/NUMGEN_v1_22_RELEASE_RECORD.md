# Number Genesis v1.22 — Release Record

**Status:** DRAFT. Not adopted. `numgen-v1.21` governs until the PI adopts v1.22 and tags it.
**Date:** 24 November 2026.
**Prepared by:** Claude, Number Genesis co-owner session; round-2 repairs applied by ChatGPT, at the PI's request. Branch `claude/numgen-v1.22`, stacked on PR #375, which is stacked on PR #374.
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
| Co-owner review of the v1.22 build, round 1 | ChatGPT review `6041922508` on PR #377, head `fabb6c0122c6b8abd0daf84ba9be6b4466882bb2`: ACCEPT WITH CHANGES (R1–R4) | repairs applied in round 2; readback pending |
| Round-2 readback and native rerun | Claude co-owner on PR #377, comment `7136733537` (outputs in commit `99bae54`): ACCEPT; R1–R4 checked against the sources; C0–C10 PASS; NC1–NC15 caught | done |
| Atlas row check | *(to be filled)* | pending |
| PI adoption | *(to be filled)* | pending |

## 2. Identities

| Object | SHA-256 |
|---|---|
| Base: `numgen-v1.21` (274,246 bytes) | `4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701` |
| Candidate round 1 (reviewed, superseded; Git commit `fabb6c0122c6b8abd0daf84ba9be6b4466882bb2`) | `8ccc8e38f0ad054d68f59bf5d95c9364afa093f02cb3e418295625db3763148a` |
| **Candidate round 2** `dsn/RTG_NUMBER_GENESIS_DSN.md` (282,107 bytes, 2990 lines) | **`fa28c0abe8bca5e9e7bb307e27ecb8f13c75399a7d804487a7a48b7a8b5c78b9`** |
| Published file (after the publication transform) | *(to be filled)* |
| Tag `numgen-v1.22` | *(to be filled by the PI)* |

| Build or check file | SHA-256 |
|---|---|
| `evidence/numgen/scripts/build_numgen_v1_22.py` | `2c3356c2a4080c221125c1925ea6cd4bb75c2c796431692ce1823f5771c6a0b9` |
| `evidence/numgen/scripts/check_numgen_v1_22.py` | `2d3b06fc1c0a56a8c20ef0df03e373f2a45227ba3127f1801f8b57e875d60ad0` |
| `evidence/numgen/v1.22/edit_log.json` (39 edits; round 2) | `243ce7c62969a28e1e477e787d09ea5caef094cde8372f2fc97d75ae00765a60` |
| `evidence/numgen/v1.22/check_output.txt` (round 1: C0–C9 PASS; not round 2) | `9745d4aea7445dd492fd8948840e31c77cadcaed094f351799dc3c565a2afadc` |
| `evidence/numgen/v1.22/negative_controls_output.txt` (round 1: NC1–NC11 caught; not round 2) | `b8b038d550c87cd8177a609cbda6dfb0339acb48a933b1a0bc01cf9a10af84cd` |
| `evidence/numgen/v1.22/dsn_lint.txt` (round 1, informational) | `dde570e2cfcbb01e6a5cbbb0b30f0130d78ab4e434831ae7be848c5ba5bd9138` |
| `records/numgen/NUMGEN_v1_22_RECEIVING_LEDGER.md` | `17341c762e6535742607af6831f409141ed78a535cb0e906efb8f9c6499aac1e` |
| `evidence/numgen/v1.22/round2_readback.json` (round-2 connector-side rebuild and controls) | `f61900932a5103645b627ad6ba0999d1b30860be11a52c5e0b32e086877bb020` |
| `evidence/numgen/v1.22/round2_check_output.txt` (round 2, native: C0–C10 PASS) | `28fcccdd382f7cb58690693f820126b5adb5656c31e82cdef6d69c04e2785460` |
| `evidence/numgen/v1.22/round2_negative_controls_output.txt` (round 2, native: NC1–NC15 caught) | `ccc5b707b3356cd3d81161e42c67e9be206d7b827b5aaa54d4a246331e5f3a93` |
| `evidence/numgen/v1.22/round2_dsn_lint.txt` (round 2, informational) | `7e28828950c5839c0216d4a0c08082e3c50859bdf21b2acf90354b65da57b177` |
| `evidence/numgen/v1.22/round2_pipes_check.txt` (round 2: OK, 149 items in 20 inboxes) | `6a8820015bf7afa2fa4adf458baedb7d4cd0657a0bbb340f19cf5f8d2a5822da` |
| S1: script / annotation / manifest | `4c5c2f17…8ae9` / `1819015a…3524` / `3981cfe6…67dc` |

**Reproduce:**
1. `git show numgen-v1.21:dsn/RTG_NUMBER_GENESIS_DSN.md > v.md`
2. `python3 -I evidence/numgen/scripts/build_numgen_v1_22.py v.md OUT LOG` gives `fa28c0ab…78b9` (round 2; native rerun 24 Nov 2026 reproduced the candidate and the edit log byte-identically).
3. `python3 -I evidence/numgen/scripts/check_numgen_v1_22.py v.md OUT LOG --root .`, and again with `--controls`.

## 3. Edits by group

The edit log has 39 entries: the original 35 with seven edited replacement entries refined, plus four exact-once review edits (RV1A, RV1B, RV4A, RV4B). Round 1 is preserved at the reviewed commit and SHA above. Each replaces one exact substring that occurs exactly once, in order, and each is reversible (gate C2).

| Group | Keys | Change |
|---|---|---|
| Header | H1–H5 | title v1.22; Date 24 November 2026; Document status DRAFT; Supersedes v1.21 with its hash and tag; Release record |
| P01: TDR-G RIDs | I1–I3, L2, C3 | §1.1 state-space and recurrence imports repinned to `tdrg-v2.13` with `TDRG-DEF-ZN-STATE`, `TDRG-DEF-PHYSICAL-STATE` and `TDRG-THM-RECURRENCE` (statements byte-identical to v2.12.13 apart from the RID tag; checked). The firewall stays a guard citation without RID (SG-10 and SG-PROG-1 checked identical at `tdrg-v2.13` and `programme-v1.4`). §9.1 rows. |
| F1: C7C-M4 hold | Q1, Q2, P5, R1 | §2 item 1 and §6.6: the P2 policy is answered (`TDRG-DEF-ORIENT`), and the consumer re-annotation is recorded. **M-4 stays HOLD.** The remaining launch gate is an approved design/preregistration for the missing non-degenerate chain, with middle-interface witnesses, outer-pair admissibility and WD-DOM explicit. All 158 TDR-G records in Census-1 are `(SWAP, P3)`; the two dyad records are separate. The witness is the research target, not a prerequisite to the search. Census-2 needs its own preregistration. |
| F1/F2: P2 audit, S1 | P1–P4 | §6.6 DISC-2 summary, DISC-1 evidence, DISC-2 evidence, the P2 guard, and the new `[NUM]` block "P2 re-annotation under TDRG-DEF-ORIENT (v1.22 S1)". "DISC-1 requires the same audit" (two sites) is replaced by the scoped result. |
| F3: q* | Z1 | §6.2: `q_*` is not Dyadic's `q_{3/4}` (`DYAD-THM-OPEN18-STEP-MONOTONE`, `dyad-v6.4.24` §6.8). This closes NC-17. Scan-resolution qualifications are kept. |
| F5: DZT | D1 | §8 `[PROVENANCE]`: the v0.17 files are received history and not lineage; the governing edition is `dzt-v0.19`; `DZT-THM-CASCADE-NORM-LAW` is cited as a locator only. NUMGEN still imports nothing from DZT. |
| Pins and consumers | L1, L3, L4, C1, C2, C4–C9 | §9.1: dispositions table (six v1.22 rows); current companions Dyadic v6.4.24, TDR-G v2.13, OFN v0.12, Programme v1.4, Genesis v2.10, RECOG v0.3.27; pins used unchanged where the statement is unchanged; RECOG export row with the two-grade GAP-LOCK 3 use; OFN export row (REQ-O09-03; N-1A2 vocabulary only); **new export row Genesis** (`NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE`, IF38); Genesis import row IF37 |
| S1 evidence | R2 | §9.2 artifact row for the S1 record and evidence |
| Hash form | X1 | §9.2 RECOG v0.3.24 hash written `8c64bea2…e7c1` (was a six-character suffix; v1.21 release record §14, atlas note on E42) |
| History | A1, F1 | Appendix A v1.22 entry; footer |
| Round-2 review repairs | RV1A, RV1B, RV4A, RV4B; refined Q2, P4, P5, L2, L4, C3, A1 | Both stale M4 summaries synchronized; S1 comparison and G2 scoped; actual firewall pin, star-domain and OFN vocabulary limits clarified; original BIND3 owner export distinguished from accessible NUMGEN inputs; receiving/entry records updated. Review `6041922508`. |

The tag census (gate C3) changes exactly by `[NUM] +2`, `[scope: …] +1` and `[conv: …] +1`:
- the S1 `[NUM]` block with its scope and convention tags;
- the `[NUM]` status label of the new §9.2 artifact row.

No other grade tag changes. No edit lowers OPEN, CLOSED or INCONCLUSIVE (C4). No NUMGEN RID is added or removed. The eight newly cited external RIDs include `TDRG-ART-BIND3-N24K1` (owner v2.13 §8, missing-artifact locator only). No new NUMGEN RID or truth-status change. Round-2 native C5 rerun: PASS (no NUMGEN RID changed; all eight external RIDs declared at the named tags).

## 4. Checks

Round-1 native output files are retained unchanged and refer to the superseded candidate. Round 2 was rebuilt and reversed against the exact tagged base by a connector-side independent readback, including edit hashes, tag/status/RID checks and the four targeted negative controls. The Python builder, checker with full controls, lint and pipes validator were then rerun natively on round 2 by the Claude co-owner session (24 Nov 2026, Python 3.13): candidate and edit log reproduced byte-identically; C0–C10 PASS; NC1–NC15 each caught by a substantive gate; pipes OK. Outputs: `evidence/numgen/v1.22/round2_*.txt`. The atlas row check may rerun them independently.

| Check | Evidence key | Result |
|---|---|---|
| Round-1 `check_numgen_v1_22.py` C0–C9 | EV-RUN | PASS on round 1 only |
| Round-2 independent connector readback (`round2_readback.json`) | EV-HASH, EV-BYTES | 39/39 exact-once, 78/78 edit hashes, forward/reverse reconstruction, review guards and 4/4 targeted negative controls PASS |
| Round-2 Python C0–C10 and NC1–NC15 | EV-RUN (Claude, 24 Nov 2026) | C0–C10 PASS; NC1–NC15 all caught |
| Round-1 negative controls NC1–NC11 | EV-RUN | all caught on round 1 |
| `tools/dsn_lint.py` | EV-RUN (round 2) | informational; one more `historical` phrase than v1.21 (the R4 governance row), otherwise as at v1.21 |
| `tools/pipes_index.py --check` | EV-RUN (round 2) | OK; pipe files and index unchanged by round 2 |
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

Round 2 clarifies the §9.1 availability row: NUMGEN enumerators and S1 inputs are accessible, but the exact original owner-side `TDRG-ART-BIND3-N24K1` enumeration/export remains reported missing in `tdrg-v2.13` §8 (EV-SRC-REPORTED). No original is reconstructed and no new recovery campaign is needed.

## 8. Not done

- No new import.
- No grade or OPEN change.
- No reopening of Census-1.
- No M4.
- No DISC-3.
- No compaction.
- No merge and no tag by this session.

## 9. Remaining steps

1. Round-2 change-focused readback of R1–R4: done by the Claude co-owner session (24 Nov 2026; PR #377 comment).
2. Atlas row check (native round-2 outputs are on the branch; independent rerun optional).
3. PI adoption.
4. Publication transform (status lines only).
5. PI merge (#374 → #375 → v1.22 PR) and tag `numgen-v1.22`.
6. Notices (§6) and closure of the eleven inbox items.

*END OF RECORD.*
