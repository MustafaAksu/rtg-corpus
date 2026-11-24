# NUMGEN owner disposition — Atlas sync advisory of 23 Nov 2026 (Claude co-owner session)

**Date:** 24 November 2026.
**Session:** Claude, Number Genesis co-owner.
**Status:** [SESSION]. Owner disposition proposal for the PI. It is not a release, it changes no DSN and no pipe state, and it is not PI approval.
**Reads:** `records/numgen/ATLAS_ADVISORY_NUMGEN_SYNC_20261123.md` revision 2 (PR #372, merged; atlas-owner readback ACCEPT, comment `7113435416`), and the ChatGPT co-owner status review of 24 Nov 2026 as given to this session by the PI (not in the repository).
**Checkpoint:** `main` `9ab42f4`.
**Governing NUMGEN:** `numgen-v1.21`, `dsn/RTG_NUMBER_GENESIS_DSN.md` SHA-256 `4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701`.

## 1. Verdict

| Item | This session |
|---|---|
| Advisory (F1–F8, P01–P11, the 17 diagnostic keys) | **ACCEPT SCOPED.** I agree with the ChatGPT co-owner review row by row (§3). §2 adds three corrections and sharpenings. |
| v1.22: one scoped synchronization release | **GO recommended, for PI decision.** One content stage. No stage 2 is needed, because no layout change is proposed (Methodology v1.4 §13.6). |
| Bounded P2 witness re-annotation (F1/F2) | **GO recommended.** Smaller than the review assumes (§2.1). |
| C7C-M: abstract design of a non-degenerate composable chain (WD-DOM) | **GO recommended.** Separate from v1.22. |
| M4 realization campaign | **HOLD** |
| DISC-3, broad campaign reruns | **DEFER** |

## 2. Corrections and sharpenings

### 2.1 F1: NUMGEN already holds the consumer sensitivity run for DISC-2

The held v1.19 audit `upload/numgen-records/disc2_p2_antipodal_exposure_audit_v1.py` (`89a1466f…fe1c`) already computes the case. Its `inert` policy handles S=0, E=N/2 exactly as its own E=0 branch, as an inert tie. TDRG-DEF-ORIENT (`tdrg-v2.13` §6.3) makes S=0, 2E≡0 mod N a balanced tie, which is an inert bound state under `bound_path_tie` and `bound_symmetric`. The audit's log (`51cde879…8c47`) reports **inert-policy changes 20** and **reverse-policy changes 10**. TDR-G's record of the atlas rerun (§6.12, DISC-2 witness effect) reports **20/136** under TDRG-DEF-ORIENT and **reverse 10**.

**Replay (EV-RUN, this session).** The audit was rerun on the held witness report (`ccc84570…aa7d`), and its log reproduced byte-identically (`evidence/numgen/sync_20261124/disc2_p2_audit_replay.log`).

**Session diagnostic.** The diagnostic `evidence/numgen/sync_20261124/p2_witness_identity_check.py` (`2a9a9311…8791`, output `8f99d397…f54d`) uses the audit's own functions:
- The 40 P2-exposed DISC-2 witnesses are **exactly** the 40 Census-1 TDR-G records that fail F6/R6-P2. Census-1 universe = DISC-1 22 + DISC-2 136 = 158 (`NG_C7C_M2_CENSUS_PROTOCOL_v1.md` §U-TDRG).
- The 20 changed records are all exposed records:
  - 8 change rational class within PASS_INT (1:1 → 3:2 ×4, 1:1 → 4:3 ×4);
  - 6 lose PASS status (→ STABLE_NO_CONTINGENCY);
  - 6 lose the base dual (5:2 → NO_BASE_DUAL).
- The ten-label set is unchanged (log, gate P2c).

**Limit.** The identification of `inert` with TDRG-DEF-ORIENT is a code reading (EV-SRC-READ). It is not a run of the pinned engine `genesis_mode_b_mc_v18.py` with the TDR-G reference `orient_path` (`evidence/tdrg/scripts/tdrg_orient_v2_12_14.py` at `tdrg-v2.13`, `ca59e9b9…`).

**So the v1.22 work for F1 is small:**
1. Run the pinned engine with the reference `orient_path` on the 136 DISC-2 witnesses and the 22 DISC-1 witnesses.
2. Check witness by witness that the result equals the audit's `inert` column.
3. Write the witness-level annotation as an `[NUM]` record.

This needs no new seed, panel or policy. Frozen v18 evidence stays untouched.

### 2.2 F2: the 0/22 DISC-1 result is source-reported only

The three sites are confirmed in `numgen-v1.21` §6.6:
- line 1600: "DISC-1 requires the same audit";
- line 1969: "DISC-1 requires the same audit separately";
- line 1912: the v1.20.6 robustness record, "0/22 witnesses exposed; label projection `{2:1, 3:1}` unchanged under the tested reverse and inert alternative policies".

The 0/22 also appears in `NG_V1206_RULING_LEDGER.json` (`b510aa62…a131`, line 106) and `NG_V1206_FREEZE_MANIFEST_v1.md` (line 18). I found **no execution artifact** (script or log) for the DISC-1 P2 audit in `upload/numgen-records/` or elsewhere in the repository. The 0/22 is therefore EV-SRC-REPORTED.

**Proposal.** The 22 DISC-1 witnesses are part of the same run as §2.1. Lines 1600 and 1969 are then replaced by the scoped result. A rerun over all 3,456 seeds is not needed.

### 2.3 Review §2.3 (schema obstacle): already adopted; now confirmed against the records

The obstacle is not a new finding. `numgen-v1.21` §6.6 line 2039 already states it at `[RESULT] [from: ALG]`: "TDR-G contributes no candidate chain at either level, because every admissible record is oriented `(SWAP, P3)`".

What this session adds:
- **All 158** Census-1 TDR-G records, including the 40 quarantined ones, carry the stream pair `(SWAP, P3)` (diagnostic output Q1).
- TDRG-DEF-ORIENT introduces no new event type. A tie becomes inert or ambiguous.

The review's conditional inference therefore holds. Admitting the 40 under the adopted rule can change Census-1's admissible count (118 → up to 158), but it cannot produce a candidate chain. Census-1 stays INCONCLUSIVE / INCONCLUSIVE. The obstacle lies in the record construction of the Census-1 universe (one ordered stream pair per seed), not in P2. A composable chain needs either a different universe, which is Census-2's own preregistration (protocol §U-TDRG), or a third stream. I agree with the review that M4 must not be designed around the P2 fix.

### 2.4 Smaller points

- **GEN v2.10 adopted use.** `NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE` is cited in `gen-v2.10` (lines 919, 1195 and 1280; `GEN-ART-G2-CHRONO` stays custody-A). This is the first adopted cross-stream use of a v1.21 RID. §9.2 Consumers needs a row, which is v1.22 work.
- **RECOG v0.3.27.** It consumes `NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO` at two grades (the exact identity at ALG; the locking statement as a HEUR cross-reference). The §9.2 RECOG row gets both. A1c is comparison only, with no import (review §4). No change to U_NG.
- **Tags.** All tags in the review's table exist. `BASELINE.md`'s RECOG cell still says "(tag to be created by the PI)" although `recog-v0.3.27` exists. This is for BASELINE maintenance, not NUMGEN.
- **Outbound items.** All four are closed (TDRG `2026-10-28 · accept`; RECOG, GEN and DYAD `accept with change`). No new request is needed.

## 3. The eleven inbox items — proposed dispositions

These are proposed for the v1.22 receiving ledger. No `state` is changed here.

| Key | File (`pipes/NUMGEN/`) | Review | This session |
|---|---|---|---|
| P01 | `20261028-TDRG-v2-12-14-adopted.md` | accept with change | **accept with change**: rule and RIDs received; consumer re-annotation per §2.1; eight producer RIDs cited at the §1.1 `RID unavailable` uses after a claim-level match; SG-10 citation kept |
| P02 | `20261029-RECOG-v0-3-26-adopted.md` | accept — historical receipt | **accept**: predecessor receipt; superseded by P07 |
| P03 | `20261030-DYAD-v6-4-23-adopted.md` | accept | **accept**: q* disambiguation at the N-1C witness (F3); closes NC-17 |
| P04 | `20261030-OFN-v0-11-adopted.md` | accept | **accept** |
| P05 | `20261030-OFN-v0-12-adopted.md` | accept scoped | **accept**, scoped: vocabulary use only; no import of the closure |
| P06 | `20261104-PROG-v1-4-adopted.md` | accept | **accept**: IF12–IF14, IF24, IF27, IF37 and IF38 checked against §9.1; repin by statement |
| P07 | `20261104-RECOG-v0-3-27-adopted.md` | accept with change | **accept with change**: two consumption grades in §9.2; A1c comparison only |
| P08 | `20261111-DYAD-v6-4-24-adopted.md` | no action | **no action**: imported statements unchanged |
| P09 | `20261112-TDRG-v2-12-15-adopted.md` | accept scoped | **accept**, scoped: check only the NUMGEN statements that use the star domain |
| P10 | `20261119-DZT-v0-18-adopted.md` | accept | **accept**: §8 provenance (F5) |
| P11 | `20261120-DZT-v0-19-adopted.md` | accept — reference only | **accept**: scoped locator for `DZT-THM-CASCADE-NORM-LAW`; no import |

## 4. Proposed v1.22 scope (for PI decision)

| Step | Content | Exit criterion |
|---|---|---|
| S1 | F1/F2: pinned-engine run with the TDR-G reference `orient_path` on DISC-1 (22) and DISC-2 (136); witness-level `[NUM]` annotation; §2 item 1 and §6.6 lines 1600/1912/1969 | equality with the audit's `inert` column witness by witness, or each difference named |
| S2 | Receiving ledger for P01–P11 (§3) | one record; state, statement acceptance and adopted use kept separate |
| S3 | F3–F8: q* disambiguation, §9.2 consumers (GEN v2.10, RECOG v0.3.27), pins, the eight TDR-G RIDs, DZT provenance, entry-note refresh | exact-once edit log |
| S4 | Build and check script, negative controls, co-owner and atlas review, release record | like v1.21 stage 1 |
| S5 | PI adoption, merge, tag | — |

**Not in v1.22:**
- regrading old claim blocks;
- moving LOGSLIP;
- a new compaction;
- reopening Census-1;
- M4;
- DISC-3.

The C7C-M WD-DOM design is a separate research line after v1.22.

## 5. Not done

- No DSN edit.
- No change to any pipe state or index.
- No change to frozen evidence.
- No campaign run.

The only executions in this session were the replay of the held DISC-2 audit and the read-only diagnostic of §2.1, both on held records.

*END OF RECORD.*
