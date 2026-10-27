# TDR-G v2.12.13 advisory — ChatGPT co-owner disposition

**Date:** 2026-10-27  
**Session:** ChatGPT TDR-G co-owner  
**Status:** proposed owner dispositions; NOT PI-fixed, NOT scientific adoption; no DSN edits.  
**Sources read:** adopted tag `tdrg-v2.12.13` as identified by BASELINE (SHA-256 `aa232643f6f631694b0eda1532be213e5a517ef109cd66794f8e638e24fc053f`); current `dsn/RTG_DISCRETE_GENESIS_DSN.md` (targeted §§1–8, especially §6.3); `CONVENTIONS.md`; `pipes/README.md`; governing Methodology v1.4 targeted sections; `records/tdrg/TDRG_COOWNER_ENTRY_NOTE.md`; `records/tdrg/ATLAS_ADVISORY_TDRG_v2_12_13_RECONCILIATION.md` §§1–5; both NUMGEN inbox items; `records/tdrg/TDRG_UPLOAD_HASH_CHECK_20261027.md`; atlas orientation-check script (targeted). Reconciliation §3 has 18 rows; all are dispositioned below. The source hash is the historical adopted source, NOT a hash of this record.

## Decision

**[SESSION — initial independent disposition, superseded by the dated co-owner comparison below] Initially choose option (a): centre-relative G for the degenerate P₃ path, with invariant palindromic-tie behavior for general even-length paths.** Reject retaining node-ID ordering as a physical selector. This is a *proposed convention change* at the owner's decision boundary, not an assertion that old v18 trajectories are unchanged.

The covariance group is the full node-label permutation group `S_M` acting simultaneously on `(theta_i,delta_i)` and all graph labels, with component topology unchanged, plus common global phase translations on `Z_N`. A stronger, independent common-token-shift covariance question belongs in the separate OFN Finding A disposition; this record does not assume it.

For a P₃ with centre c and endpoints v₁,v₃, use the existing signed gradient S if nonzero, then the endpoint advance E if `S=0` and `|E| ≠ N/2`; on `S=0, |E|=N/2` set

`G = sc_N(delta_v1-delta_c)-sc_N(delta_v3-delta_c)`.

Orient in the sign of G, preserving the successor-shift `CONV-P3CYC`. Under endpoint reversal G negates and, on the specified degenerate stratum, G never vanishes (atlas C2, exhaustive N=24; general algebraic argument should accompany the rule). Under global node relabeling the chosen physical orientation must commute with relabeling. For paths of other lengths, do **not** extrapolate nonzero-G; use a separately defined invariant palindromic tie with no oriented update whenever the data do not distinguish direction. The stage-1 checker must include label permutations beyond endpoint reversal and explicit even-length/palindromic controls.

**Definitions:** `sc_N(x) = ((x mod N) - N)` when `x mod N > N/2`, otherwise `x mod N`; codomain `(-N/2,N/2]`. `signed_defect_error(theta_i,theta_j,N)=sc_N(((theta_i-theta_j) mod N)-N/2)`. State the even-N and narrow-band hypotheses explicitly.

**Evidence boundary:** Reported atlas census: 1,152 degenerate (state,k) path cases in the exhaustive N=24 P₃ panel; in the ratified DISC-2 set 136 total witnesses, 40 convention-exposed, and 96 unexposed. Compared to v18, reverse / inert / G changes witness verdict or class in 10 / 20 / 12 cases respectively. The ten-label projection remains unchanged under each tested completion; the 96 unexposed witnesses remain unaffected by a change confined to this stratum. At k=1, 77 of 9,800 eventual cycles (4.9% of states, per census) encounter a v18 listing-dependent event. These are *reported finite-model measurements*, not proofs of preservation of all BIND3 percentages, all future campaigns, or the DISCRETE-1 panel. The change count of 12 versus 20 is not a mathematical optimality proof and is only a secondary tie-breaker; the primary preference is preserving an oriented P₃ interaction where the state data intrinsically determine its direction.

## All 18 reconciled rows — dispositions

| Reconciliation §3 row | Disposition | Owner instruction and acceptance condition |
|---|---|---|
| **TA-01 / I01** | **Accept with change** | Select G for degenerate P₃ and invariant palindromic tie otherwise as above; declare covariance group and SG-14, failing v18 permutation and passing G controls. Keep existing v18 conclusions under their actual historical rule with `EV-NOT-RERUN`. |
| **TA-02** | **Accept** | Put `signed_centered` and `signed_defect_error` exact equations and domains at their point of use. Do not conflate the phase defect sign with endpoint advance. |
| **TA-03 / I11** | **Accept with change** | Add SG-14 for node permutations and global phase shifts; add **two distinct** owner decisions: endpoint relabeling under the declared group; OFN common token shift / Finding A separately. No automatic all-token-shift claim. |
| **TA-08 / I02** | **Accept** | Replace the unqualified §6.12 relabeling PASS with the actual ±d mirror test statement; mark old node-permutation selector counterexample and affected certificates `EV-NOT-RERUN`. |
| **TC-14 / I03** | **Accept with change** | Disposition NUMGEN orientation request by chosen G-rule; preserve table 40/136 exposed, 96 unexposed; witness changes 10/20/12 for reverse/inert/G and unchanged ten labels at tested scope. DISC-1 remains unaudited; C7C-M4 held until owner release/consumer replay. |
| **TA-05 / I04** | **Accept** | Retrigger map has period dividing 2; when d=0 the state is fixed (least period 1). Exact least period 2 only when second step differs; exclude the d=N/2 alias from the binding threshold k<N/6 explicitly. |
| **TA-06 / I05** | **Accept** | No-birth magnitude-spectrum conservation implies gcd-class conservation; reverse implication fails (N=24, magnitudes 1 and 5). Replace “equivalently” by “therefore, in particular.” |
| **TA-04 / I06** | **Accept** | Attribute −0.869 to N=120–1440 and approximately −0.730 to N=480–1440, fixed k/N and policy, bulk conditioning; retire χ=0.836 as live consistency evidence. Crystallization remains HEUR extrapolation. |
| **I07** | **Accept** | Align §1/§2/§5: D/F finite identities and numerical mechanism closed at stated grades; analytic constants/residual models open; TDR-24A/B/C open. No gate reversal or rerun. |
| **TA-07** | **Accept** | Mark inherited K₃ 96:1 healing and T-6 wedge/R0 x* references historical/withdrawn for physical downstream use; do not import a corrected Triadic result without owner pin. |
| **TB-09 / I08** | **Accept with change** | Add scoped RIDs for imported definitions first (state, Δ, D_k, E_def, tick, swap, P3 successor, orientation, star, policies), then §6.2 results, four lemmas, BIND3. Propose identifiers during builder stage, check collisions and consumers; **no invented adopted RID now**. Leave all OPEN module RIDs intact. |
| **TB-11 / I08** | **Accept** | Set custody by artifact: placed / held hash-recorded / replayed / missing. Never label a later derivation “recovered”. Pin the verified upload manifest. Historical execution must not be silently promoted to local replay. |
| **TB-10 / I09 / I10** | **Accept with change** | v2.12.14 is corrections-only, under declared Methodology v1.2. Name Methodology v1.4, Programme v1.3, OFN v0.10 as currently governing reference editions without falsely asserting this DSN has migrated; claim-specific historical pins remain. Add §7 Imports/Exports/Consumers/Pins with received/statement accepted/adopted-use separately. Full v1.4 migration and compaction deferred to v2.13. |
| **TB-12** | **Accept** | Split mixed grades into independent exact/numerical/engineering statements and remove dead legacy-alias table from the live edition without deleting archival evidence in tags. |
| **TB-13** | **Accept** | Repair current-only metadata, one predecessor/footer, live TDR-24B presentation, Appendix A ordering and Appendix C gate consistent with D/F current state; avoid layout compaction. |
| **TC-16** | **Accept** | Cross-cite AZ antipodal low-order arithmetic once the TDR-G state/exclusion RIDs exist; replace phantom TDRG-ZN-STATE alias with actual owner RID after issuance. |
| **TC-17** | **Accept** | Restore Programme v1.2 owner-review tasks in TDR-G §2 as current owner obligations: state/gauge, antipodal path tie, counting observables, statistical/rank interpretation. Programme v1.3 dropping prose does not close them. |
| **I12** | **Accept** | Label AZ 4|q Hashimoto signal as substrate-only static graph geometry, not dynamical policy-scaling evidence or a bridge; retain TDR-19 OPEN. |

## OFN questions separated (TA-03/I11)

1. **Node-permutation / endpoint orientation**: **accept with change**; the G-rule is the scoped correction and SG-14 states the group. This addresses the *endpoint-policy* component of REQ-O09-05 at owner-model level only.
2. **Global token shift / OFN Finding A (XFER-O08-01)**: **defer custody adoption**, pending explicit token-shift action, event-level covariance test, and a named claim boundary. The previously source-reported no-birth transformation result remains OFN-owned; TDR-G shall not silently import it into all birth policies. The dispositions must not conflate the two questions.

## Answers to held-file questions

**Q1: which engine produced the v17 corpus?** **Unverified.** Upload inventory authenticates the placed `genesis_mode_b_mc.py` (SHA prefix `4c94d874…a608`; source header “v15.3”) and separately `genesis_mode_b_mc_graph_export.py` (v16.0 header) and v18 engine (`9d787b43…675e`). Version labels and filenames are not producer/run attestations. The present session has no trusted per-run execution manifest mapping those historical v17 CSV hashes to an exact engine hash. Record `engine producer identity unresolved` and the known available candidate files; do not invent that v15.3 generated all v17 files.

**Q2: session-held certificate suites and v6 outputs?** **No originals available to this session.** The four named session-certified suites and per-run v6 CSV/DSN-patch outputs were not in the verified 49-file upload, and have not been located or hash-identified here. Record `missing / not identified` (with earlier session-report provenance where available), not “replayed” or “recovered”. A future independent reconstruction gets an independent artifact identity and claim grade. Large CSVs remain PI-held, hash-recorded, not placed until actual upload.

## Inbox dispositions (initial proposals; no inbox edits in this PR after workflow correction)

- `pipes/TDRG/20261026-NUMGEN-orientation-policy-s0-e-half-n.md`: **2026-10-27 · accept with change · records/tdrg/TDRG_OWNER_DISPOSITION_ADVISORY_v2_12_13_chatgpt_20261027.md**; proposed state only, NOT committed. Requested choice G, with finite witness table and delayed consumer re-annotation. No assertion that NUMGEN has adopted the use or lifted C7C-M4 HOLD.
- `pipes/TDRG/20261026-NUMGEN-v1-21-adopted.md`: **2026-10-27 · no action · records/tdrg/TDRG_OWNER_DISPOSITION_ADVISORY_v2_12_13_chatgpt_20261027.md**; proposed state only, NOT committed. Notice acknowledged; scientific adoption remains NUMGEN-owned.

## Release boundary

No BIND3/NKSCAN/N-scaling reruns in v2.12.14 (PI decision). Capture `EV-NOT-RERUN` at each touched result with the exact N=24 reported census bound; a later sensitivity campaign is a distinct task. Do not change the `bound_symmetric` policy fork or SG-10. Await the PI's fixation of the two co-owner disposition records before writing the candidate DSN or asserting release adoption; next step is one stage-1 assertion-gated corrections patch plus negative-control checker and draft release record on a fresh branch.

## 27 October 2026 — post-peer reconciliation addendum (retains initial independent choice)

**New source checked:** Claude co-owner disposition `records/tdrg/TDRG_OWNER_DISPOSITION_ADVISORY_v2_12_13_claude01SKePJ_20261027.md`, PR #89, and associated evidence under `evidence/tdrg/disposition/` (read and compared; NOT rerun in this session). The other owner independently checked the pinned v18 `step_universe` on all 331,776 three-node gauge-reduced states at N=24 for each k=1 and k=3, plus 100,000 four-node random samples and the antipodal permutation fixture. The reported failure counts are 72 and 168 per S₃ generator for v18 and zero for both option (a) and option (b); both restore the tested node-permutation covariance. These tests **do not** establish a general all-N or all-policy symmetry theorem. Its multistar fixture independently finds the `largest_center` equal-degree centre ID tie-break noncovariant (N1), whereas the canonical `bound_symmetric` multistar does not fire; the ±mirror inventory identity is not step-equivariance (N2).

**Revised scientific recommendation for the PI's stipulated *corrections-only* v2.12.14: OPTION (b), extended balanced tie.** The reason is methodological/model selection, not a failed check of option (a): the current rule declares S and E as the orientation inputs, and these carry no reversal-odd sign on `S=0, E=N/2`. Option (b) closes the inconsistency using that existing information contract, whereas option (a) introduces the centre-relative token as a new orientation input. **Neither is dynamics-neutral:** both change the event law from v18 on the affected stratum, and both require historical results to retain the v18 pin/`EV-NOT-RERUN` scope. Record option (a) as a covariant alternative in the later sensitivity campaign; do not retcon its scientific viability away. This addendum **supersedes this record's initial (a) recommendation for the specific v2.12.14 release**, while preserving the independent original disposition for atlas/PI comparison.

**SG-14 refinement:** its `Sym(V) × Z_N^{phase}` step-equivariance requirement must explicitly apply to the *canonical branch and those other policies that pass the stated controls*. The present `largest_center` equal-degree tie-break violates it, so an unqualified universal 'the TDR-G step is covariant under every policy' is false; record that exception and keep TDR-19 open. The common token shift and ±mirror are separate questions, not generators of the declared group.

**Engine Q1 evidence strengthened, but not globalized:** the other owner supplies two SHA-256 byte-exact replays using the uploaded engine `4c94d874…a608` (including canonical-scan `motif_N120_k08_T5000_b20_v17.csv`) and a source-code comparison showing the pinned v18 kernel has the same event rules. This identifies the producer for the **two replayed CSVs** and makes the v17 campaign association strongly supported. It is not a byte-level replay of every uploaded v17 file; preserve this evidence scope in §8. All original certificate suites remain unavailable/missing unless found and hash-identified.

**Workflow correction:** The initial PR #88 changed both `pipes/TDRG/` items to `dispositioned` before the PI fixed the owners' conflicting decisions. That was premature. This branch now restores both items byte-for-byte to `main` and leaves their status to the reconciled checkpoint (PR #89 presently proposes `acknowledged` for the request). The outdated initial proposed metadata above remain as historical proposals only, not actual queue states. No adopted use or C7C-M4 release follows from either PR. After PI fixation, the builder must update the actual pipe states, pointer, generated index and validation.

**Other co-owner deltas to carry into the row reconciliation:** adopt or map consumer-used names `TDRG-ORIENT` and `TDRG-ZN-STATE` after collision checking, keep the Methodology v1.4 migration and layout-only footer/Appendix A cleanup at v2.13 as the PI requires, and distinguish OFN's accepted common-token-shift *statement* from deferred scientific custody. None is silently installed by this note.
