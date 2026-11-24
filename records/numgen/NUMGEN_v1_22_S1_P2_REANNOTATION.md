# NUMGEN v1.22 S1 — witness-level P2 re-annotation under TDRG-DEF-ORIENT

**Date:** 24 November 2026.
**Session:** Claude, Number Genesis co-owner.
**Status:** `[NUM]` evidence record for v1.22 S1. Not adopted; no DSN edit; frozen verdict files untouched.
**Authorization:** the ChatGPT co-owner GO of 24 Nov 2026 for S1, with acceptance criteria 1–7, as given to this session by the PI. It builds on `records/numgen/NUMGEN_OWNER_DISPOSITION_SYNC_20261123_CLAUDE_20261124.md` (PR #374).

## 1. What was run

Script: `evidence/numgen/v1.22/s1/numgen_v1_22_s1_p2_reannotation.py` (`4c5c2f17…8ae9`), run from the repository root.

The universe is the Census-1 TDR-G witness universe: DISC-1 22 + DISC-2 136 = 158 records (`NG_C7C_M2_CENSUS1_UTDRG_UNIVERSE_v1.json`), at k ∈ {0,1,2,3}.

The pinned engine is loaded twice from the same bytes:
- **v18**, unmodified;
- **TDRG-DEF-ORIENT**: the same engine with `orient_path` replaced by the TDR-G reference `make_orient`.

Everything else is unchanged:
- N = 24, three nodes;
- `step_universe(..., multistar_policy="bound_symmetric")`, the policy of the Census-1 lockstep;
- the engine's event semantics;
- the frozen enumerators' `lift` and `canon`, which give the cycle key.

| Input | Path | SHA-256 |
|---|---|---|
| owner engine v18 | `upload/tdrg-records/genesis_mode_b_mc_v18.py` | `9d787b43…675e` |
| TDR-G reference orientation (`tdrg-v2.13`) | `evidence/tdrg/scripts/tdrg_orient_v2_12_14.py` | `ca59e9b9…d59c` |
| Census-1 TDR-G universe | `upload/numgen-records/NG_C7C_M2_CENSUS1_UTDRG_UNIVERSE_v1.json` | `80b0c3b1…13e9` |
| DISC-1 enumerator / result | `upload/numgen-records/bind3_enumerate_k0123_v1.py` / `disc1_result.json` | `41a86011…e929` / `92593b8c…6f70` |
| DISC-2 enumerator / witness report | `upload/numgen-records/disc2_supplementary_enumerator_v3_1.py` / `disc2_witness_report.json` | `b7cee922…35df` / `ccc84570…aa7d` |
| held v1.19 audit (comparison only) | `upload/numgen-records/disc2_p2_antipodal_exposure_audit_v1.py` | `89a1466f…fe1c` |

Outputs, in `evidence/numgen/v1.22/s1/`:
- `numgen_v1_22_s1_witness_annotation.jsonl` (`1819015a…3524`): 158 records. Each has the frozen record, the v18 and TDRG-DEF-ORIENT tuples (k=0..3), verdicts and classes, antipodal hits, the exposed and changed flags, and, for DISC-2, the audit's `inert` column.
- `numgen_v1_22_s1_manifest.json`.
- `numgen_v1_22_s1_output.txt`.

The run was executed twice; the annotation hash was identical both times.

## 2. Gates

| Gate | Criterion | Result |
|---|---|---|
| G1 identity | all 8 inputs match their pins | PASS |
| G2 positive control | unmodified v18 reproduces the frozen record of every witness, with tick-by-tick lockstep against the record's own frozen enumerator: DISC-1 transport tuple k=0..3 and PASS_INT; DISC-2 verdict and base class | PASS, 158/158 |
| G3 single intervention | the two engine copies differ only in `orient_path`; the bytecode of every other function is identical | PASS |
| G4 DISC-2 | the new policy against the held audit's `inert` column, witness by witness (verdict, class, exposure) | PASS, 136/136 equal |
| G5 DISC-1 | 22 witnesses evaluated directly; exposure counted, not assumed | **exposed 0/22, changed 0/22** |
| G6 negative controls | (a) the antipodal fixture (θ_pre=(0,11,12), δ=(0,1,12), k=1): v18 gives δ′=(1,12,0) and is not equivariant under 0↔2, while TDRG-DEF-ORIENT gives a tie (δ unchanged) and is equivariant; (b) an always-reversed orient breaks the v18 reproduction | PASS; (b) 158/158 broken |
| G7 summary | against the co-owner's expected table | no difference |

## 3. Result `[NUM]`

| Measure | Value |
|---|---|
| DISC-2 witnesses | 136 |
| P2-exposed | 40 |
| verdict or class changed | 20 (all exposed) |
| class changed, PASS kept | 8 (1:1 → 4:3 ×4; 1:1 → 3:2 ×4) |
| PASS lost, base dual kept | 6 (1:1 → STABLE_NO_CONTINGENCY ×4; 4:3 → STABLE_NO_CONTINGENCY ×2) |
| base dual lost | 6 (5:2 → NO_BASE_DUAL) |
| PASS witnesses under TDRG-DEF-ORIENT | 124 of 136 |
| admitted labels | 10 under v18; the same 10 under TDRG-DEF-ORIENT |
| DISC-1 | 22 witnesses; 0 exposed; 0 changed; labels {2:1, 3:1} unchanged |

**What this settles:**
1. The held v1.19 `inert` column is the TDRG-DEF-ORIENT result on this panel, now by an engine run and no longer only by reading the code (disposition record §2.1).
2. DISC-1's reported 0/22 now has its own execution artifact (§2.2 of that record).
3. The ten-label set and DISC-1's {2:1, 3:1} hold under the adopted producer rule.

## 4. Guards

- **Census-1 is not reopened.** Its F6/R6-P2 decisions and its INCONCLUSIVE / INCONCLUSIVE verdict stand as frozen. Records evaluated under the new policy are not retroactively admitted to Census-1. Any new admission is Census-2's own preregistration.
- **Frozen evidence stays as it was.** The frozen v18 protocol, verdict files and certificates are unchanged. The annotation is a separate `[NUM]` record; it is not a replacement certificate.
- **Scope.** The finite panel only (N=24, three nodes, k ≤ 3, `bound_symmetric`). This is not a statement about other panels, policies or N.
- **M4 stays HOLD.** S1 is the consumer sensitivity record of F1. It does not release M4. The open target is still a non-degenerate composable chain (WD-DOM).

## 5. Use in v1.22 (S3/S4, proposed)

- §2 item 1: the producer answer (TDRG-DEF-ORIENT) and this consumer annotation are recorded; M4 stays HOLD.
- §6.6 line 1600 and line 1969: "DISC-1 requires the same audit" is replaced by the DISC-1 0/22 result with this record as evidence.
- §6.6 line 1912: the v1.20.6 robustness record now points to this artifact.
- §9.2 artifact row for this record.

## 6. Errata (24 Nov 2026, after co-owner review comment `7128043448`)

- Three abbreviated hashes in this record were wrong in their suffix: S1 script, orientation and annotation. A fourth was not in the four-character form: the witness report. All four are corrected above. The full SHA-256 values in `numgen_v1_22_s1_manifest.json` were correct throughout.
- The docstring of the executed script `numgen_v1_22_s1_p2_reannotation.py` writes the orientation pin as `ca59e9b9…d77c`. The correct abbreviation is `ca59e9b9…d59c`. The script's `PINS` table holds the correct full value `ca59e9b9a1bb260a6600f3f793adea488ba40c416879673219dc30f21f77d59c`, and gate G1 checked that value. The executed bytes (`4c5c2f17…8ae9`) are kept unchanged; this erratum replaces a corrected copy.

*END OF RECORD.*
