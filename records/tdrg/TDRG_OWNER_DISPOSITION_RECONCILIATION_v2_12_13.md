# Discrete Genesis (TDR-G) — reconciliation of the two co-owner disposition records (advisory v2.12.13 → v2.12.14)

**Date:** 27 October 2026. **By:** Claude, atlas owner (advises; does not decide). **To:** the PI; the TDR-G co-owner sessions.
**Status:** record. The PI's "start" on the fixed dispositions (§3) releases the v2.12.14 build.
**Inputs.** `records/tdrg/TDRG_OWNER_DISPOSITION_ADVISORY_v2_12_13_chatgpt_20261027.md` (PR #88, merged `ed5f85b`; initial choice (a), post-peer addendum → (b)); `records/tdrg/TDRG_OWNER_DISPOSITION_ADVISORY_v2_12_13_claude01SKePJ_20261027.md` (PR #89, merged `78c2fef`; choice (b); owner checks under `evidence/tdrg/disposition/`); both read in full against `…RECONCILIATION.md` §3 (18 rows) and §5 (PI decisions). Owner text spot-checked at `tdrg-v2.12.13` for the one open difference (§2.2). `tools/pipes_index.py --check` on `main` after both merges: OK (12 items).

## 1. Verdict

**The two records agree on every substantive decision after the ChatGPT addendum; the remaining differences are of form, and one factual question is settled by the owner text.** Both choose **option (b)** (extended balanced tie on S=0 ∧ 2E≡0) for the corrections-only v2.12.14, keep the G-rule (a) recorded as a covariant alternative for the later sensitivity campaign, declare SG-14 with the group Sym(V) × Z_N^phase and the `largest_center` ID tie-break as a recorded exception (owner finding N1), separate the OFN token-shift question from endpoint relabelling, scope the engine identity per file (replayed / schema-consistent / held), record the four certificate suites as missing, keep all v18 results under `EV-NOT-RERUN` with the census bound, and defer layout and the v1.4 migration to v2.13. Nothing requires a PI choice between the co-owners.

## 2. Correspondence

### 2.1 Agreement (verified row by row)

| Row | Both records |
|---|---|
| TA-01 / I01 | accept (with change) — **(b)**: tie on S=0 ∧ 2E≡0 (mod N), i.e. E ∈ {0, N/2}, for all n; `[DEF]` text and `[ALG]` no-go remark as in the Claude record §1; G-rule recorded, not adopted; antipodal fixture (θ_pre=(0,11,12), δ=(0,1,12), k=1) and the exhaustive v18 failure counts (72/72 at k=1, 168/168 at k=3 per S_3 generator; 0 for (a) and (b)) as checker controls; touched results `EV-NOT-RERUN` with the census bound |
| TA-02 | accept — `signed_centered` and `signed_defect_error` as `[DEF]` with the (−N/2, N/2] convention named as the source of the stratum |
| TA-03 / I11 | accept with change — SG-14 (node permutations × global phase shift); token shift and the mirror explicitly outside the group; `largest_center` equal-degree ID tie-break recorded as a non-canonical-branch exception (N1); two separate OFN entries |
| TA-08 / I02 | accept — §6.12 "relabeling-covariance check" reworded as the ±d mirror-inventory identity; the step is not mirror-equivariant at P_3 events (N2); BIND3 numbers unchanged |
| TC-14 / I03 | accept — witness-effect table (40 exposed; 20 records change under (b), 10 / 12 under reverse / G for comparison; ten labels unchanged; 96 unexposed unchanged by construction; DISC-1 and other panels not covered); C7C-M4 HOLD is NUMGEN's to release after the tag |
| TA-05 / I04, TA-06 / I05 | accept — least-period wording (d=0 fixed point; \|d\|_c ≤ 2k < N/3 never reaches N/2, so no aliasing caveat is needed); "therefore, in particular" with the N=24 counterexample (1 and 5 share gcd 1) |
| I07, TA-07, TB-11, TB-12, TC-16, TC-17, I12 | accept — same instructions |
| TB-09 / I08 | accept with change — consumed definitions first; consumer-used names `TDRG-ORIENT` and `TDRG-ZN-STATE` adopted after collision checking; nothing invented before the build |
| TB-10 / I09 / I10 | accept with change — governing editions named, historical pins kept, §7 four-way with received / statement accepted / adopted use; v1.4 migration deferred to v2.13 |
| TB-13 | accept with change — metadata and content items in v2.12.14; footer chain and Appendix A ordering deferred to v2.13 (layout; PI decision) |
| XFER-O08-01 | **statement accepted** (one-line algebra on TDR-G's own DEFs, EV-CODE against v18 `blow_up_star_with_snapshot`: the star map commutes with B_c iff 2c≡0); **custody deferred** to v2.13; REQ-O09-05 answered (endpoint policy = TDRG-ORIENT (b); XFER as above) |
| Held-file Q1 | engine `4c94d874…a608` identified as producer **for the two byte-exact replays** (`motif_TEST_N120_k8_T1200_b3_v17.csv`, canonical-scan `motif_N120_k08_T5000_b20_v17.csv`), schema-consistent for the other placed v17 files, not replayable for the ten held files; v18 = `4c94d874` + logging only (same `orient_path`); §8 records exactly these states |
| Held-file Q2 | the four suites and the v6 per-run outputs: **missing** (custody (a)) unless found; no re-derivation called a recovery |
| Pipe items | request `acknowledged` until the PI fixes the dispositions, then `dispositioned · accept · <release record>`; notice `no action`; both closed after the tag (states on `main` now: request `acknowledged`, notice `dispositioned`; validator OK) |

### 2.2 Differences and fixed resolution

| Point | ChatGPT (#88) | Claude (#89) | Fixed |
|---|---|---|---|
| Orientation | initial (a), addendum **(b)** | (b) | **(b)**; (a) recorded as the unadopted covariant alternative, written as "G on P_3 + tie elsewhere" (the only exact form both tested) |
| TA-04, the restricted exponent ≈ −0.730 on 480–1440 | cite it | "not in the DSN; cite only with an owner source" | **It is in the owner text**: `tdrg-v2.12.13` line 287 (§2, OPEN-POLICY-GEOMETRY entry, Exp-0 = the existing scan on the high-N window: "B/step N^{−0.730}, O/step N^{+0.903}, C_birth N^{−1.633}, χ N^{+0.697}"), beside line 273–275 (window dependence of χ). So the range tag in §1/§5 can cite the owner's own line 287 as `[NUM]` for the 480–1440 window — no atlas-reported figure, no refit, no new headline. (The atlas row TDRG.G1 was built from that line.) |
| XFER-O08-01 statement | not imported now | statement accepted now | **accepted now** (verified algebra), custody deferred — the ChatGPT addendum concurs |
| Q1 engine identity | "unresolved" | per-file scoped with two replays | **per-file scoped** — the addendum concurs |
| TB-13 footer / Appendix A | in v2.12.14 | v2.13 | **v2.13** (PI: no layout work in v2.12.14) — the addendum concurs |
| TC-16 RID name | new RID, then replace the phantom | issue `TDRG-ZN-STATE` itself | **adopt the consumer names** after collision check — both |
| Pipe states | initially `dispositioned` (withdrawn) | `acknowledged` | **`acknowledged`** until the PI's fixation; #88 restored the items, #89's states are on `main` |

### 2.3 Atlas-side observations

1. **N1** (`largest_center` chooses among equal-degree centres by node ID) is a real new finding, outside the advisories; it belongs in v2.12.14 as a scope note on the `largest_center` results (§§6.6–6.7, OPEN-POLICY-GEOMETRY slice) and in SG-14's branch scope, with TDR-19 left OPEN. The atlas D5 gains a row for it at v0.7.
2. **N2** (the mirror (θ,δ) ↦ (−θ,−δ) is not a step symmetry at P_3 events) corrects the reading of §6.12's "±d mirror symmetry": an inventory identity, not equivariance. Consistent with TA-08/I02.
3. The owner equivariance check drives the pinned engine's own `step_universe` (no re-implementation) — stronger than the atlas script, which re-implements the three-node step; the two agree on every count they share (atlas C3/C4 rerun byte-identical in `evidence/tdrg/disposition/`).
4. Under (b) LEM-SPECCONS is untouched by construction (ties act as identity in its proof) — worth one sentence in the release record.
5. The witness-effect figure for (b) is 20 of 136 records (not 12): the release record and the NUMGEN notice must carry the (b) figure, with 10 / 12 only as comparison.

## 3. Fixed dispositions (for the PI's "start")

All 18 rows as in §2.1 with the resolutions of §2.2; orientation (b); SG-14 as drafted by the Claude record with the N1 exception; OFN statement accepted / custody deferred; engine identity per file; suites missing; `EV-NOT-RERUN` with the census bound on every touched result; v2.12.14 corrections-only under Methodology v1.2; v1.4 migration, footer/Appendix A layout and the sensitivity campaign (with (a) vs (b) on the same universes) deferred to v2.13 or later.

## 4. After "start"

The co-owner session `claude01SKePJ` offered to build (it holds the v18 patch history); the ChatGPT session reviews change-focused; the atlas owner reruns the builder/checker and writes `records/tdrg/ATLAS_ROW_CHECK_TDRG_v2_12_14.md`; release record; PI adoption; merge commit; tag `tdrg-v2.12.14`; tag verification; notices to NUMGEN, OFN, AZ; atlas v0.7 (D5 TDRG rows, D5.X1, H4, H9, N1 row, TC-17 fix).
