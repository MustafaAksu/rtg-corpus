# Number Genesis v1.20.8 — independent Atlas advisory (ChatGPT, pass 2)

**Date:** 26 October 2026. **Status:** [SESSION] / INDEPENDENT ADVISORY; not an owner disposition, scientific adoption or NUMGEN edit.  
**Review separation:** Claude's pass-1 record `records/numgen/ATLAS_ADVISORY_NUMGEN_v1_20_8.md` (PR #62) **was not opened or read**. This record is independently authored against the tagged owner sources and the accepted Atlas v0.5. PI determines final dispositions; NUMGEN owner sessions prepare any successor.

## 0. Source manifest and review extent

| Source | Governing tag, identity | Coverage in this pass |
|---|---|---|
| NUMGEN | `numgen-v1.20.8`, SHA-256 `835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e` | Owner text retrieved as a whole (3,412 physical lines; split produces 3,413 slots); targeted §§0–3, 6.2, 6.6 and C7C subblocks, 6.8–6.9, 7–9, Appendix A. Not a complete proof audit of 3,412 lines. |
| Atlas | `atlas-v0.5`, SHA-256 `cf250c9140e6ee26c65b2497a2a61dc1e326a69574d590132f0cea9646a2b0e5` | Whole text retrieved; targeted H4/H5/H8, D2.L5 NUMGEN.N-*, D5 DISC/TDRG, D2 and D3 interfaces. |
| RECOG | `recog-v0.3.24`, SHA-256 `8c64bea231b3691b737f4143f6f4105030ee183fcc90d7f604ec83a4c869e7c1` | Targeted §6.13b (A1a/A1b), §6.16e (A1c), §7 imports; v0.3.23 predecessor provenance read through v0.3.24 release/interface statements, **not** a separate full v0.3.23 byte-level comparison. |
| DYAD | `dyad-v6.4.22`, SHA-256 `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29` | Targeted §6.14 row-A/PRIM-CTR and cited boundary results, no new DYAD proof replay. |
| Programme | `programme-v1.3` | §7.2 IF12/13/14/24/27 and adjacent interface rows, scoped contextual reading. |
| Methodology | `methodology-v1.4` | Relevant §§1.1, 3.4, 4.4, 12 and 13.6–13.9; `CONVENTIONS.md` also retrieved before branch writing. |

Source identity: tag names and full NUMGEN/Atlas/RECOG/DYAD hashes are checked against the repo's governing manifest and/or recorded releases. GitHub file retrieval confirms text at each tag; **file SHA-256 values were not independently recomputed locally**, no owner certificates or substantial computational campaign rerun. Source quotes and file line positions are from the tagged files, not mutable main. Older consumer pins remain deliberately older until each owner accepts new inputs.

## 1. Decision

**[SESSION] ADVISE CORRECTIONS AND TYPED HANDOFFS, NOT SCIENTIFIC REOPENING OF THE N-5 PROOFS.** The highest leverage is a bounded synchronized owner pass covering (i) explicit-domain A1a/A1b comparison, (ii) GAP-LOCK/INF-1 custody and RIDs, (iii) DYAD row-A intake, (iv) C7C-M's blocking TDR-G P2 policy, followed by (v) a Methodology v1.4 current-only migration. No certificate rerun is justified by stale pointers alone.

### N208-I01 — RED FLAG: A1b's stronger slip theorem exists, but NUMGEN's physical/clock import is not performed [P0 interface]

**[OWNER: NUMGEN v1.20.8 §§6.6, 9.1, lines 1630–1636, 2086–2316, 2727–2753; RECOG v0.3.24 §6.13b lines 730–740; Atlas v0.5 H5 line 48, NUMGEN.N-B/N-E lines 583–584].** RECOG `RECOG-THM-A1B-SLIP-SCHEDULE-U` supplies on explicit `U={0<Q_0≤1/625}`: lift-crossing identification (A), six-step deficit (C′), 6/7 alphabet and infinitely many sevens (B), and the digamma slip schedule with its **a-priori** error (S). NUMGEN GAP-LOCK Lemmas 1–3 and physical 7-gap rate remain NUMGEN owner's accepted local proofs; the new theorem is a distinct explicit-domain comparison, **not proof that all NUMGEN existential-tube predicates inherit the RECOG domain**.

**Action:** owner makes an acceptance matrix for RECOG A1a/A1b versus NUMGEN GAP-LOCK 1/2/3 and INF-1, with one row per statement specifying event predicate (section sign and anchor convention), primitive lift, base vs full tube, clock/block index, domain of the estimate, and evidence grade. Explicitly distinguish independent agreement, consumed theorem and not adopted. **Criterion:** a precise domain-and-clock map for every imported result, with any nonidentical event definition retained as open. Do not claim GAP-LOCK/INF-1 ownership transfer or widen DYAD `U_T`.

### N208-I02 — A1a's `C_D^{ext}` is not NUMGEN's phase constant `φ^*` [P0/P1 interface]

**[OWNER: RECOG v0.3.24 §§6.13b, 6.16e lines 720–740, 1000; NUMGEN v1.20.8 §§6.6, 9.1 lines 2086–2316, 2742–2753; Atlas NUMGEN.N-D/N-L4 lines 582,593, H5 line 48].** A1a gives existence of an explicit-U phase constant without importing R9/INF-1. Its `C_D^{ext}` and infinite-record `Ψ_∞` may be compared to `φ^*` only after a NUMGEN-specific observable/gauge/initial-condition proof. A1c yields record `L` without knowing `a`; it **does not** recover `a` or imply an `R_ind` memory-carrier downgrade.

**Action/criterion:** enter A1a/A1c as **available comparisons** (not imported identities), specify whether `φ^*` uses the same chart, lift, readout, clock, starting state and overlap set. Keep identification OPEN until equality or counterexample is established with these conventions. Do not call `C_D^{ext}` a generic physical phase observable.

### N208-I03 — L-BACKBONE 15/2 bound is not a complete explicit error budget [P1]

**[OWNER: RECOG v0.3.24 §6.13b lines 720–739; NUMGEN v1.20.8 §6.6 and §9.1 lines 2745–2753; Atlas NUMGEN.N-B line 583].** The `(15/2)√Q_m` ceiling bounds the reciprocal-amplitude **increment error** on a certified explicit sector. It is not the missing complete NUMGEN L-BACKBONE error constant or its integrated error budget. RECOG's digamma `ε_k` ceiling uses the largest primitive amplitude *within the kth slip block* and infinite series tails; it is not computable from `(a,k,M_k)` alone.

**Action/criterion:** type the three distinct errors (increment, summed-tail/backbone, slip schedule), their domains and `Q/q` representation. Either derive a valid complete NUMGEN error bound or keep the explicit-constant import pending; never substitute 15/2 for the latter.

### N208-I04 — DYAD row-A is received, not adopted into NUMGEN [P1]

**[OWNER: NUMGEN v1.20.8 header lines 10–13, §9.1 lines 2734–2736, 2748–2750; DYAD v6.4.22 §6.14 `DYAD-THM-LPHASE-ROWA-REMAINDER` (owner uses same 403/250 constant); Atlas NUMGEN.N-A line 581].** NUMGEN's I1–I5 interface confirmation and receipt replay do **not** constitute theorem consumption. NUMGEN explicitly defers an import of the Dyadic v6.4.19 row-A theorem. The v6.4.22 owner keeps the theorem; `403/250≥1.61112` is a compatible remainder ceiling, not proof of all NUMGEN hypotheses. DYAD's stated row-A base-point `U` does not automatically cover `U_T\setminus U`.

**Action/criterion:** one explicit receiving-decision row, exact producer tag/RID, mapping `W↔\mathcal L`, `Q_m↔q_m`, primitive lift and lag sign, with start/base-point restrictions. Mark **prepared/received/accepted/adopted-use** separately. Retain NOMINAL `[RESULT][from: ALG]` for un-imported NUMGEN clauses. Do not bulk-repin older DYAD imports (v6.4.18).

### N208-I05 — GAP-LOCK Lemmas 1–3 need dedicated owner RIDs and consumer-grade reconciliation [P1]

**[OWNER: NUMGEN v1.20.8 §§6.6–6.7 lines 2086–2316, §9.2 lines 2793–2796, 2824–2825; RECOG v0.3.24 §7 lines 1109–1118, §6.13b lines 737–740; Atlas H4 line 47, NUMGEN.N-R1/N-G1 lines 597–608].** NUMGEN's `NUMGEN-DEF-N5AS1-DEFECT`, `NUMGEN-RESULT-N5AS1-INF1`, `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` are distinct from unnumbered GAP-LOCK 1/2/3. Historical NUMGEN §9.2 (line 2824) still says RECOG consumes GAP-LOCK 3 at HEUR based on an old v0.3.5 reference, while the current RECOG claim use includes ALG-grade event alignment and explicit A1b proof. A RECOG import is not itself a promotion of a NUMGEN lemma grade.

**Action/criterion:** assign owner-chosen, collision-checked RIDs to each load-bearing lemma; distinguish original proof/cert custody from RECOG's independent explicit-U route and from informed recipient status. Correct the current RECOG consumer-grade description without asserting an unverified higher grade; check precise importing RID and hypothesis.

### N208-I06 — P2 endpoint-antipode orientation is an external scientific blocker for C7C-M4 [P0 cross-owner]

**[OWNER: NUMGEN v1.20.8 §2 line 163, §6.6 lines 1901–1945, 2028–2035; Atlas D5.X1 line 1402, H9 line 52].** Under TDR-G `signed_centered∈(-N/2,N/2]`, `S=0`, `|E|=N/2` makes endpoint reversal return the same positive centered antipode. NUMGEN's observed v18 node-ID tie-break gives a deterministic implementation but **not relabelling covariance**; owner reports 40/136 DISC-2 witnesses exposed (216 events). It is not repaired by rerunning the same frozen experiment.

**Action/criterion:** request TDR-G owner's **scientific orientation-policy disposition** and specify which admitted DISC witnesses depend on it. Keep `C7C-M4` realization HOLD until a covariant or explicitly scoped policy and affected-witness reassessment; continue abstract WD-DOM design in parallel. Never silently discard the ten-label established spectrum on an untested blanket inference, or declare unaffected statuses without a sensitivity audit.

### N208-I07 — C7C algebra and physical composition must not be conflated [P0/P1]

**[OWNER: NUMGEN v1.20.8 §2 lines 147, 161–164; §§6.6/8 lines 2004–2059, 2699–2705; Atlas D2 NUMGEN dependency line 563, D5 DISC lines 1292–1384].** `M-1A` exact chain identity and `M2-1` algebraic transported chain are conditional mathematical results; `C7C-0` reciprocal closure is a total unary operation on certified `R_bd`, not multiplication. `Census-1` INCONCLUSIVE/INCONCLUSIVE means no admitted nondegenerate composable source chain was found in the bounded instrument; **not** proof that none exists. Label-only `WD-DOM` fails; full-interface admissibility descent, identities, inverse and associativity remain OPEN.

**Action/criterion:** retain a precise typed `Φ_{τ1,τ2}^{τ3}` signature and domain-congruence/value-congruence proof obligations ahead of any new M4 campaign, then require an actual composable three-stream witness. No theorem that all positive rationals or ℚ arithmetic have emerged.

### N208-I08 — NUMGEN existential tube, DYAD `U/U_T` and RECOG `U` are different domains [P1]

**[OWNER: NUMGEN v1.20.8 §6.2 lines 1045–1065 and §6.6, DYAD v6.4.22 §6.14, RECOG v0.3.24 §6.13b line 730; Atlas NUMGEN.N-S1/N-SC1 lines 580,596 and H8 line 51].** NUMGEN writes `U` for a continuity-chosen radius `δ` and `U_T=⋃_{j=0}^5T^jU`; the explicit DYAD-certified base `U={0<Q≤1/625}` and its full `U_T` have an additional published contraction contract. RECOG A1b takes starts on explicit base `U`, with some estimates on explicit `U_T`. Evidence of one-chart shrinking for NUMGEN theorems does not identify these three representations or ranges.

**Action/criterion:** a compact domain alias table and at point of theorem use `U_{NG}`, `U_{D,base}`, `U_{D,tube}`, `U_{R,base}` or another unambiguous scheme. No mathematical repinning or global renaming is needed where old proofs intentionally use their original domain. Check any new explicit-domain corollary separately.

### N208-I09 — Source-header currency and historical consumer pins [P1 documentation]

**[OWNER: NUMGEN v1.20.8 header lines 5–13, §9.1 lines 2727–2753, §9.2 lines 2824–2827; Programme v1.3 IF12–14, IF24, IF27 lines 428–443; Atlas NUMGEN.N-F/N-G1/N-L5 lines 605,608,594].** NUMGEN header says `Programme v1.2`, `GEN v2.8.9`, DYAD v6.4.18 and calls Dyadic v6.4.19 “current”; Programme now v1.3, Genesis v2.9, DYAD v6.4.22, RECOG v0.3.24 and Methodology v1.4. Some are intentionally earlier **claim-specific pins**; the obsolete “current” labels are not. Programme IF12 still records the historical NUMGEN Dyadic intake as v6.4.18; IF13 TDRG v2.12.13; IF14 NUMGEN→RECOG v1.20.8; IF24 holonomy to OFN with its declared OFN pin; IF27 NUMGEN as receiver of RECOG consumer information at v0.3.22. None authorizes an automatic RECOG A1b import.

**Action/criterion:** §7 Imports/Exports/Consumers/Pins or equivalent scoped matrix; one unambiguous current context, historical proof pins retained in a separate column, and explicit **offered/received/accepted/adopted-use** states. Programme interface changes by its owner, no automatic re-pinning of consumers.

### N208-I10 — Methodology v1.4 live-ledger migration should be separately staged [P1/P2]

**[OWNER: NUMGEN v1.20.8 header lines 1–13, §2 lines 157–215, §8 lines 2675–2721, Appendix A/Changelog lines 2895–3412; Methodology v1.4 §§1.1, 3.4, 13.6–13.9; CONVENTIONS §§3–4].** Adopted NUMGEN still declares v1.3; live header has supersession/history fragments and dated overlays, live §2 and §8 repeat an evolving priority queue, §9.2 mixes current evidence custody with past consumer summaries, and ~500 lines of historical changelog remain in the live file. These are **presentation/provenance maintenance issues** independent of the C7C scientific frontier. Claim-grade normalization was done in v1.20.7 and should not be undone or re-proved.

**Action/criterion:** follow the two-stage method if upgrading to v1.4: Stage 1 scientific/scope/interface corrections, frozen hash and change-focused review; Stage 2 current-only compaction, movement map, checker and negative fixtures. Preserve every proof, hypothesis, domain, RID, OPEN, grade, negative result, original source location and its historical pin. No blanket retagging from ALG to THM or automatic physical-model claim.

### N208-I11 — NG-7A closed does not close NG-7B or physical curvature [P2]

**[OWNER: NUMGEN v1.20.8 §6.8 lines 2359–2466, §7 lines 2654–2671; Programme IF24 line 440].** Additive cycle nullity/completeness and fundamental-integral-cycle extension over abelian coefficients are owner mathematical results; the source/metric/non-Abelian/physical bridge part remains NG-7B OPEN. The phrase “holonomy rank” must not be allowed to import a non-Abelian invariant or curvature interpretation without a separate construction.

**Action/criterion:** owner handoff of closed operator and precise OPEN source side; list grades and representations; OFN decides its own consumer acceptance.

### N208-I12 — N-1C/N-3C+/representation-vs-dynamics interface remains scoped [P2]

**[OWNER: NUMGEN v1.20.8 §§6.2–6.4 lines 878–890, 1299–1524; Atlas NUMGEN.N-L1/L2/L3 lines 590–592, NUMGEN.N-R1 line 597].** L1 local contraction and history distinction do not imply a topology-changing global counter; root-of-unity projectors and character restriction are representation-kinematic, not imported all-p nonlinearity; the Dyadic all-p Q403 closure stays DYAD-owned. Cross-stream exact identities (ΔQ5/ISP phase) documented by Atlas are candidates for one-line owner context, **not** reasons for a costly new proof campaign.

**Action/criterion:** one bounded navigation pass retaining representation/physical grades, with optional one-line exact coefficient aliases only after checking the producer RIDs.

### N208-I13 — Key counting and grades should be stable under compaction [P2]

**[OWNER: NUMGEN v1.20.8 §2 line 163, §§6.6/9.2 lines 1630–2059, 2727–2828; Atlas H4 line 47, NUMGEN.N-R1/N-R2 lines 597–598].** Many independently load-bearing N5 and DISC subresults are registered only under module `OPEN` RIDs; that is a discoverability issue rather than proof failure or a reason to invent theorem-RID names. A closed algebraic subclaim can still live under an open encompassing module; actual claim grade is the tagged statement, not the RID prefix.

**Action/criterion:** priority RID list for GAP-LOCK, INF-2, C7C-M2, M-1A/M2-1 and DISC-1/2/ten-label bound, with owner-proposed collision-checked identifiers; avoid retagging all inherited labels in a single pass. Preserve negative controls and source evidence matrices.

## 2. Proposed ordering and handoff

1. **Owner decisions first:** handle N208-I01/I02/I03/I04/I05 as **one explicit-U/asymptotic-interface decision** including row-A. Separately request TDR-G disposition on I06 and hold M4.
2. **Scientific corrections (Stage 1):** resolve admitted interface/clock/domain claims and the minimal RIDs. Do not change independently verified N5/C7A, C7C algebra, DISC1/2 evidence absent a concrete scope reason. Every row has acceptance criteria above.
3. **Documentation pass (Stage 2):** v1.4 migration and current-only layout; historical import pins retained rather than overwritten.
4. **Independent receiving review:** changes and affected source dependencies only. Unchanged expensive campaigns stay frozen; new claims require explicit evidence and grades.

## 3. Limitations and specific nonclaims

- The pass did not read the first advisory; the two reports can now be reconciled without compromising independence.
- No REC/DYAD/NUMGEN certificate was independently rerun; cross-owner proofs were read **targetedly**.
- No conclusion is made that RECOG's A1a/A1b settles all NUMGEN GAP-LOCK or INF-1 scope, that `C_D^{ext}=φ^*`, or that a finite slip record uniquely recovers the starting state.
- No conclusion is made that C7C-M is impossible, that P2 policy invalidates the entire ten-label spectrum, or that any physical arithmetic beyond the source's restricted results has been established.
- This report is a **proposal** to the owner and PI. No canonical DSN, scientific adopted tag, consumer acceptance, programme import or notice is changed.
