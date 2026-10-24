# Independent Atlas advisory — Genesis Geometry v2.8.9 (ChatGPT pass 2, blind)

**Date:** 24 October 2026. **Status:** SESSION / NONCANONICAL advisory. **Recipient:** Genesis scientific owner and PI. **Scientific adoption:** none. **Blindness:** PR #37's `records/gen/ATLAS_ADVISORY_GEN_v2_8_9.md` and the Claude first-pass findings were **not opened or read** before fixing this report. This is a separate independent pass, not an owner disposition and not a proposed Genesis patch.

## 0. Sources, identity and reading extent

| Source | Governing edition / identity | Extent in this pass |
|---|---|---|
| Genesis scientific owner | `gen-v2.8.9`; `dsn/RTG_GENESIS_GEOMETRY_DSN.md`; SHA-256 **`d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc`** (`BASELINE.md`) | Full 1,650-line file retrieved from this tag; header, §§1–2, 6.2, 6.5–6.9, §7, §8 and named OPENs inspected closely; targeted keyword/section review elsewhere. Owner line numbers below refer to this fixed tag, not `main` or historic project copies. |
| Accepted Atlas | `atlas-v0.4`; `atlas/RTG_STATE_ATLAS.md`, accepted SHA-256 `b63eaf8b85dbb1f4a8fbee61cb82f2af089276797c387e6a8a0b13922805c35b` | H6; D4b GEN.D1–D7/D14; D4a F9/F10/F14–F17/F19/F20; A04-06 and supporting D4a/D4b records read. |
| Method / repository | `methodology-v1.4`; root `CONVENTIONS.md` | Governance, source/proof grades, live document vs historical record and two-stage successor rules; no new scientific authority inferred. |
| Relevant interfaces | DYAD `dyad-v6.4.22`; OFN `ofn-v0.10`; RRF `rrf-v0.8.4`; Programme `programme-v1.3` | Governing editions checked in `BASELINE.md` and relevant source/import rules, but **not all owner proofs/certificates** re-audited. GEN's own historical import pins are treated as consumer states, not automatic defects. |

**Evidence classification:** [OWNER] means the cited text was inspected in tagged owner file; [SESSION] is interpretation/review finding; [UNVERIFIED] flags a dependency not reproduced. `[THM]` in owner text is reported as an owner grade, not independently re-proved. No campaign was rerun.

## 1. Findings: scientific wording / interface correctness (highest priority)

### G29-I01 — [P0, D-CONV / D-GRADE] sourced-junction sign and minimizer scope (Atlas GEN.D1; H6)

[OWNER: GEN v2.8.9 lines 74–76, 1012–1039, 1048, 1076–1085; §2 lines 468–478] Genesis §1 and §6.9 state an unqualified `[THM]` that constrained birth has a valid **minimizer** for `(ΔM_f+τI)d_⊥+S_f=0` (the plus operator). §6.8 GCL-02 explicitly derives the displayed `+2aτ` secular numerator from **`K_-=τI−ΔM_f`**, says `K_+` reverses the cross term, and explicitly leaves physical sign, energy and minimizer selection OPEN.

[SESSION] The algebraic minus-branch reconstruction is **not** itself a refutation of the existence of a plus-branch stationary solution; the actual conflict is the theorem's unconditional **minimizer/physical sourced-birth** wording versus the admitted lack of a typed energy / Hessian / sign-selection argument. The two `K_±` are not equivalent under a fixed source and fixed phase. Algebraic stationary solvability need not imply positive second variation.

**Owner action:** produce a single canonical variational functional and second-variation criterion (or explicitly scope the plus-branch theorem to a specified algebraic conditional). Reconcile the two theorem occurrences in §1 and §6.9, the source equation §6.8, and export limits §7. No physical branch claim from determinant `(τ²−κ²)²` alone.

**Acceptance:** branch, source covariance/metric pairing, sign of `ΔM_f`, energy Hessian, minimizer conditions and any `w=0`, `σ_f≠0` specializations are consistent at every occurrence; the conditional `[THM]` survives only for a proved implication.

### G29-I02 — [P0, D-CONV] `κ` sign and soft-eigenvector assignment (Atlas GEN.D2; H6)

[OWNER: GEN v2.8.9 lines 1003–1006, 1056–1063, §2 lines 433–440] Face lift defines `κ=|m||w|≥0` with `m=2Q_sB_*`; scalar-M 9A uses `κ=m|w|`, projectors `Π_±=(I±ΔM_f/κ)/2`, and `v_+=(μ_1,μ_2−|w|)`. Neither `B_*` nor its sign is specified in §6.8.

[SESSION] For `m<0`, the two algebraic eigenvalues and projectors are merely **relabeled** if one uses signed `κ`; but the assertion “soft branch = `τ-g-κ`” can select the opposite physical projector/eigenvector. This is a convention-typing problem, not an invalidity of the resolvent identity. At `κ=0` the displayed `Π_±` formula also needs a separate degeneracy domain.

**Owner action:** either prove `m≥0` under the stated model or use `κ=|m||w|` consistently and define `s=operatorname{sgn}m` in the projectors and branches; state domain `w≠0, m≠0` when dividing by `κ`. Audit susceptibility/residue formulas for the resulting projector assignment (§6.9 lines 1060–1074).

**Acceptance:** an explicit negative-`m` test swaps labels as predicted, leaves the unordered spectrum invariant, and associates the physically intended residue with a declared eigenprojector.

### G29-I03 — [P1, D-SCOPE] projection nontriviality: scalar-M closure vs general-M OPEN (Atlas GEN.D4)

[OWNER: GEN v2.8.9 §6.9 lines 1052–1054, 1066–1074; §2 lines 430–445] “Projection nontriviality” is labelled generally `[OPEN]` in §6.9, but §2 calls it “closed generically” under scalar-M and (H_0=J_Qs_*). The 9B lowering selection and full `M_{spin2}` are still OPEN.

[SESSION] These statements can coexist **only** when the quantifiers are explicit: scalar-M, `H_0`, and either Euclidean or two-`B` residue, versus arbitrary spin-2 block / physical source pairing. The word “closed” without that model qualifier risks promoting a nonzero algebraic residue to physical pole excitation.

**Owner action:** label §6.9's OPEN as **general-M / physically selected pairing** and §2's completed 9A result as **scalar-M / specified source / generic `s_*`**. Define “generic” by excluded zero set.

**Acceptance:** no statement suggests all source projections nontrivial before OPEN M supplies its full block and physical source map.

### G29-I04 — [P1, D-SCOPE] raw-array 9C premise not inherited from 9B (Atlas GEN.D14)

[OWNER: GEN v2.8.9 §2 lines 97, 481–497, especially 485; §6.9 lines 1087–1091] Full discussion explicitly treats `K^TB=BK` as an **additional raw-array modelling premise**, not implied by the tensor-typed covector Hessian or 9B. Yet §2 dependency summary line **450** says that the split `−2m Im w` “gives B-self-adjointness (generalization beyond scalar-M)” without the qualifier.

[SESSION] The shorter sentence is semantically stronger than the separately guarded proof. This is an editorial-scope correction with scientific downstream impact (OPEN M's purported two-scalar input reduction).

**Owner action:** at line 450 refer to “conditional **raw-array** B-self-adjointness under the extra 9C premise”; preserve the physical possibility of blocks outside the family. No new campaign needed.

### G29-I05 — [P1, D-PIN / representation] Lie-gauge coefficient imported at use but owner source excluded in ledger (Atlas F16 / GEN.D9)

[OWNER: GEN v2.8.9 §6.2 lines 681–686 and §7 lines 1133–1146] GEN lists `c_θ^(6)=−119√3/648` as an OPEN 9 import **in the Lie strict-kernel gauge**. The import ledger explicitly says archival `DYAD-ALG-LIEGAUGE-NORM` “is not imported here,” while importing `DYAD-ALG-NF6` for the adopted normalizing chart. The two are different objects; `c_θ` cannot silently be reclassified as a normal-form coefficient.

**Owner action:** either make a *reference-only archival diagnostic* with exact producer edition/RID (if retained merely for contrast) or explicitly import the coefficient with its Lie-gauge convention and limited scientific use. Do **not** change numerical value/gauge by formatting. Compare with DYAD v6.4.22's declaration and producer edition, not merely its latest header.

**Acceptance:** point-of-use source, gauge, representation and §7 import/reference status agree.

### G29-I06 — [P1, D-PROOF / RID] owner certificate custody and missing scientific RIDs (Atlas F14/GEN.D3, F13/GEN.D7)

[OWNER: GEN v2.8.9 §1 lines 34–84, §6.2/§6.4–6.9 and §8 lines 1219–1241] The artifact registry says **“proof-source reference required”** for `GEN-ART-PURE-CHIRAL`, `GEN-ART-PHI-2TO3`, `GEN-ART-G2-CHRONO`, `GEN-ART-P4-PRIMITIVE`, `GEN-ART-PHASE-AVG`, `GEN-ART-PHASE-CLOSURE`, `GEN-ART-QH-NOGO`, `GEN-ART-FACE-LIFT`, `GEN-ART-SOURCED-JUNCTION`. Several corresponding `[THM]` statements have no theorem RID; an `ART` key is not a theorem identity.

[SESSION] The missing artifact locator is an **evidence-access gap**, not a proof that the adopted result is false; no automatic grade reduction is justified. However downstream Triadic, UVM/OPEN M, RRF and OFN cannot reproduce or bind every cited proof to a claim RID.

**Owner action:** classify each as (a) proof missing, (b) available historical evidence not placed/hashed, (c) reviewed but not rerun; assign owner RIDs to the unnumbered core theorems and map artifact keys separately. Prioritize `P4`, `G2-CHRONO`, `FACE-LIFT`, `SOURCED-JUNCTION` for their downstream use.

**Acceptance:** per-claim RID, producer edition, script/path/hash when present, replay status and honest unavailable markers; no invented certificate or retrospective “verified” claim.

## 2. Findings: scope, status, cross-owner interface

### G29-I07 — [P2, D-LINK] two inequivalent phase-moment inventories (Atlas F15 / GEN.D13)

[OWNER: GEN v2.8.9 §2 lines 135–150; §6.6 lines 958–970] OPEN 1A has exactly **13 trigonometric generators** for the stated averaged primitive quartic. §6.6 instead lists a **six-name structural closure vector** `{m^C,m^S,m^{CS},m^{S2},m^{CC}_transfer,m^{CS}_transfer}` without a linear map, normalization or distribution/clock assumptions to the thirteen.

[SESSION] These are not necessarily a contradictory count: a basis for the full quartic observable and a coarse six-coordinate closure ansatz may differ. “Exactly 13” pertains to the declared trigonometric span; it does not establish that any six chosen moments are sufficient to evaluate the quartic under arbitrary measures.

**Owner action:** give an explicit map/rank and domain, or mark the six as a historical/coarse subset that does not close the 13-moment functional. Preserve physical distribution OPEN.

### G29-I08 — [P2, D-LINK] GSPLIT specialization is an algebraic consequence, not a reverse import (Atlas F9)

[OWNER: GEN v2.8.9 §2 lines 206–213; §6.5 lines 931–950; §8 `GEN-THM-DELTA-QC` and `GEN-OPEN-WPHASE-GSPLIT`] The gap polynomial `ΔE_c^{birth}=(1/3)Q_c²+(3/4)Q_sQ_c` is declared at `I_sc=0`; the full standalone pump includes squares in `I_sc+ω_sc`. `TRIAD v1.6` CN-03 is described as independent scope confirmation, not the Genesis proof source.

[SESSION] The equality of the specialized polynomials follows symbolically with `ω_sc²=4Q_sQ_c/3` at `I_sc=0`; but this is an identity in a particular inner-product convention and does not transfer physical UV energy sufficiency.

**Owner action:** add a one-line, source-typed specialization lemma pointing from `GEN-THM-DELTA-QC` to the GSPLIT record. No new scientific campaign.

### G29-I09 — [P2, D-SCOPE] apex seed case is not four-case maximum (Atlas F10)

[OWNER: GEN v2.8.9 §2 `GEN-CAND-APEX-T6U`, §8 line 1215] Genesis quotes `R_apex=√21/64` for the declared primitive seed. That diagnostic is explicitly **not an HINDEX/UV source-norm ratio**. [UNVERIFIED: TRIAD v1.6.1 §6.17 in this pass] Atlas reports a different four-case maximum `√14/16`; its exact table was not independently rerun here.

**Owner action:** label `√21/64` as the *shear/vector case* and cite the Triadic four-case table if the overview compares maxima. Neither is a certified physical UV input or global no-basin theorem.

### G29-I10 — [P2, D-STALE / D-RID] OPEN lifecycle and duplicate header (Atlas F19/F20)

[OWNER: GEN v2.8.9 §2 lines 90–108, 243–275] OPEN 1T is described as reconciled/CLOSED while the “Immediate Genesis frontier” retains it as item 1b; OPEN 2 explicitly includes already verified `ΔQ_s`/`ΔQ_c` tasks under “Active sub-items”; two OPEN 5/2B entries use the same `GEN-OPEN-WPHASE` RID (one corrected description, one stub).

[SESSION] Not a reopened scientific problem, but current-state readers can mistake a closed import protocol for an active scientific blocker. A RID identifying one OPEN scope should resolve to one active authoritative record.

**Owner action:** remove/convert the duplicate OPEN 5/2B stub into a pointer, relocate OPEN 1T from the immediate frontier to completed interface status, split completed OPEN 2 tasks from active. Preserve historical description through Git.

### G29-I11 — [P2, source status] historical pins vs current governing owners (DYAD, OFN, RRF, Programme)

[OWNER: GEN v2.8.9 §7 lines 1133–1181] GEN imports precisely pinned `DYAD v6.4.13`, `TRIAD v1.6`, and names Programme v1.2 and OFN v0.9 as “current context.” Programme `programme-v1.3` is now adopted; OFN `ofn-v0.10`, DYAD `dyad-v6.4.22`, TRIAD `triad-v1.6.1`, RRF `rrf-v0.8.4` also govern their own scope. [OWNER: Programme v1.3 §7.2] *consumer pins are intentional until their consumer adopts a change.*

[SESSION] Therefore **no automatic blanket repin** is justified. But the descriptive words “current programme” and “current foundational context” in GEN §7 are stale when read as programme-wide state, distinct from a valid claim-specific historical import. The lack of a scoped RRF standards interface in the GEN ledger also creates avoidable profile ambiguity for `B`, `W`, `J_Q`, clock and network-vs-dyad transfers.

**Owner action:** divide §7 into (i) current authoritative reference for navigation, (ii) genuine imported scientific statements with their original proof pins, (iii) representation-standard references to RRF (read-only; no owner theorem transfer), and (iv) cross-branch blocked requests. Verify same-content at any proposed newer pin before changing it.

### G29-I12 — [P2, Methodology migration / structural] history and current-state overlays

[OWNER: GEN v2.8.9 header lines 1–11; Appendix A lines 1252–1599; §8 and §9] GEN still names Methodology v1.3 and carries a long multi-edition header supersedes chain and many historical/draft entries in a live DSN. [OWNER: Methodology v1.4 and repository `CONVENTIONS.md`] Current-state sections, compact one-edition history, proof-source / artifact separation, and explicit two-stage compaction are the governing successor rules.

**Owner action:** separate a **stage-1 scientific and interface correction** (P0/P1 findings above) from **stage-2 history relocation**, with movement map and exact intermediate hash. Keep every scope caveat, conditional theorem, RID and evidence limitation. Do not relabel earlier v1.3 statements as currently v1.4-reviewed merely by header edit.

### G29-I13 — [P2, wording / representation] primitive vs normal-form sign “healing” is not a contradiction proof (Atlas F17)

[OWNER: GEN v2.8.9 §1 lines 62–73 and §6.5 line 950] Owner describes NF healing `−Q_c(Q_s+Q_c)` versus primitive incidence `+Q_c²/3` as **different constructed observables**, explicitly withholding passive recharting as a full explanation.

[SESSION] These statements are compatible as scoped claims. It would be incorrect to “correct” one sign to the other without a mathematical transport map for full state, update/clock and observable.

**Owner action:** add “different objects, not a verified passive conjugacy” at the shorter §6.5 occurrence; maintain the negative finding and the OPEN transfer.

## 3. Proposed disposition and acceptance matrix

| ID | Priority | Type | Suggested outcome |
|---|---|---|---|
| G29-I01 | P0 | math/typing | owner sign/minimizer derivation or conditional retyping before exporting sourced junction |
| G29-I02 | P0 | math/convention | owner sign policy and explicit negative-m / κ=0 checks |
| G29-I03 | P1 | owner-scope | separate scalar-M proof from general-M projection OPEN |
| G29-I04 | P1 | interface-scope | 9C additional raw-array hypothesis at §2 point of use |
| G29-I05 | P1 | import/gauge | reclassify cθ archival Lie-gauge diagnostic or explicitly import its producer |
| G29-I06 | P1 | evidence/RID | custody matrix; distinguish ART keys from scientific RIDs |
| G29-I07 | P2 | phase moments | explicit six-to-thirteen map or scoped nonidentity |
| G29-I08 | P2 | algebraic cross-link | one-line GSPLIT specialization pointer |
| G29-I09 | P2 | birth seed | case label; table pointer, no ratio-as-UV promotion |
| G29-I10 | P2 | editorial/lifecycle | remove duplicate OPEN identity; closed tasks out of active frontier |
| G29-I11 | P2 | imports | current references separate from historically valid claim pins |
| G29-I12 | P2 | governance/layout | v1.4 migration via stage 1 + compaction stage 2 |
| G29-I13 | P2 | interpretation | retain two sign objects without claiming conjugacy |

**Avoid a release ping-pong:** batch P0/P1 fixes into one scientific owner decision and one stage-1 build; handle P2 editorial/source additions and all affected dependent occurrences in that same stage. One optional stage-2 layout compaction after the scientific diff is frozen. Do not rerun unchanged GEN K₃ obstruction or DYAD campaigns without a concrete changed dependency.

## 4. Unresolved dependencies and next action

1. A **physical sign/minimizer choice** cannot be settled by the existing determinant reconstruction. If physical energy data do not exist, record the physical branch as OPEN and retain scoped stationary algebra.
2. Independent access/replay of the nine “proof-source reference required” entries was **not performed**; do not convert that fact into mathematical falsification or a claim of full verification.
3. The exact four-case Triadic `R_apex` table and owners' present DYAD/OFN/RRF import content were not re-audited in full; preserve their accepted historical pins unless a content mismatch is demonstrated.
4. `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` (§6.3c) and its hypotheses `(H_spec)`, `μ≠0`, `γ∉{0,2}`, `C³` remain **unchanged** and were not candidates for theorem-level correction here.
5. Release/adoption sequence: blind audits fixed → Atlas owner reconciles independently → PI decides each recommendation → GEN owner prepares scientific successor → independent change-focused review → PI adoption/merge/tag. This record grants **no scientific edit authority**.

**Overall advisory verdict:** **SCIENTIFIC REPAIR REQUIRED at G29-I01/I02 before stronger UV/sourced-junction export; remaining corrections are bounded and mostly editorial or source-interface, not wholesale invalidation of Genesis v2.8.9.**
