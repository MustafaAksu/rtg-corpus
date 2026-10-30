# Triadic Birth-Lift v1.6.1 — blind independent Atlas advisory (ChatGPT)

**Date:** 30 October 2026  
**Review status:** [SESSION], NONCANONICAL advisory, second independent pass. No owner disposition, PI adoption, grade amendment, consumer acceptance, or release is made by this document.  
**Blindness:** The Claude/Atlas Triadic first-pass advisory and its PR were **not opened or read**. The current tagged Triadic owner, tagged scientific dependencies, repository conventions, and the independently inspected original source code were the inputs. Compare advisories only after both are frozen.  
**Review object:** `triad-v1.6.1`, `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md`, SHA-256 `95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f`, 159,762 bytes, 1,202 physical lines. Independently recomputed SHA-256 from the local file, matching `BASELINE.md` and the tagged Git blob `203bc1fb97d79594626808f4a67c051a01ce371c`. Annotated tag object `13ff1e9b83452b997b02b2e26845c8c01075411f` points to `d7d661c0b89c6f3d9ceea2e205bf75fccfcfbf8d`. The tag message refers to the baseline hash; it does not itself include the full file hash.

**Provenance qualification:** [UNVERIFIED] The v1.6.1 DSN header cites `records/OWNER_ADOPTION_v1_6_1.json`, `records/RELEASE_RECORD_v1_6_1.md` and `evidence/accepted_r4_2/`. All three paths returned NOT_FOUND at the tagged tree and/or `main` during this review. Thus the tagged DSN bytes and owner-stated ADOPTED status can be inspected, but the separate adoption/release-record identity and the source-package execution cannot be independently authenticated here. Do not manufacture these records from the header or historic summaries. The provenance gap does not justify substituting another owner edition from memory.

## 0. Source manifest, reading extent and evidence grades

| Source | Version actually inspected | Extent / evidential level |
|---|---|---|
| Triadic scientific owner | `triad-v1.6.1`, SHA above | Complete active scientific §§1–9, scope guards, export/receipt ledger, §8 artifact inventory; Appendix B fully, Appendix A targeted for historical lifecycle; `EV-BYTES / EV-HASH / EV-SRC-READ`. |
| Genesis | `gen-v2.9` | Targeted §1, §2, §§6.3/6.5/6.6/6.8, §7 and owner release history for GCL-05/GCL-06, source polynomial, HINDEX and CN receipts; `EV-SRC-READ`. Its historical scientific campaigns not rerun. |
| Dyadic | `dyad-v6.4.22` | Targeted map/metric/linear-frame statements, §6.14 and §7 interfaces; `EV-SRC-READ`; no return-map campaign. |
| OPEN-M | `uvm-v0.7.1` | Targeted §1, §2, §6 R-CHIRALITY-RECONCILIATION and §7 imports; `EV-SRC-READ`. |
| OFN | `ofn-v0.11` | Targeted §§4–5, §8 and §11 RF-O08-02/03/08, current class-C physical-selection guard; `EV-SRC-READ`. |
| RRF | `rrf-v0.8.4` | Targeted §§3.1 and 6.2; planar convention is reference-only and no native Triadic/physical bridge; `EV-SRC-READ`. |
| Programme / Methodology | `programme-v1.3` §§6–8; `methodology-v1.4` §§0.5, 1.1, 3.4, 3.6, 4.4, 12, 13.6–13.9 | Programme routing and grade/evidence/release rules; `EV-SRC-READ`. `CONVENTIONS.md` read on main before creating this record. |
| T-3a external candidate | `upload/dyad-sources/rtg-engine/triad_t3a_arb_enclosure_v4g.cpp`, user-supplied source placed on Atlas/DYAD evidence intake branch | Actual code examined at lines 91–96, 125–135, 148–155; `EV-CODE`, **not** a scientific certificate or an `EV-RUN` proof of trajectories. No Triadic first-pass advisory read. |
| Independent calculations | `evidence/triad/scripts/triad_blind_algebra_checks_20261030.py` | Exact finite-dimensional SymPy spot checks of displayed B/J, H norm, Jacobi rows, T-6u coefficients, §6.9 torsion, conditional §6.18 first integral and finite-difference expansion. Equivalent local implementation executed and passed; script committed as reproducible session evidence. **Not** a replay of the owner's 47-check or orientation audit. |

Notation in the findings: `[OWNER: ...]` is owner source text, `[SESSION]` is a new, non-adopted deduction/check, and `[UNVERIFIED]` is missing necessary provenance or proof input. Grades such as `[THM]` in an owner quotation are never silently reassigned.

## 1. Decision summary

**[SESSION] Verdict: ACTIONABLE INDEPENDENT ADVISORY.** The major v1.6.1 scientific *withdrawals* are internally sound at the inspected level: old sector, wedge, fatal/impact, basin and physical-route obstructions are not valid current corrected-model conclusions. The root-closed and independently oriented models remain distinct. T-6s/t/u limited algebra survives the independent spot checks. Two additional, bounded **mathematical consequences** of the corrected model are identified below and should be owner-checked before designing a new full model; these are not adopted Triadic discoveries.

| Item | Priority | Finding / proposed disposition |
|---|---|---|
| TRI16-I01 | P0 research gate | Corrected §6.18 ODE has a **conditional first integral** `D=\mathcal G/Q_s=Q_c(1-K)`. Independently check original producer extension and decide physical meaning or merely diagnostic artifact. |
| TRI16-I02 | P0 scope gate | The differential Gram identity is **not an exact finite-six-step increment identity** without quadratic cross terms. Explicitly type the ODE/truncated-vector-field versus discrete map. |
| TRI16-I03 | P0/P1 | T-6r requires an actual carrier/embedding and full evolution, not merely the algebraic `K<1` disk. Preserve ACTIVE. |
| TRI16-I04 | P1 new algebra | Corrected leading torsion has an exact **coercive lower bound** from eigenvalues `6(\sqrt3\pm1)`; do not transfer to finite `u,r`/global dynamics. |
| TRI16-I05 | P1 | A bounded sign/action table can already be given for planar mode changes; these actions are not physical node exchange or a branch-switch theorem (T-6q). |
| TRI16-I06 | P1 | T-6s coherent-family norm and precise `g_2` interval pass independent algebra; retain exact physical/source non-implications. |
| TRI16-I07 | P1 | T-6t Jacobi row algebra and 2D span pass; label signability is not independent physical carrier rank. |
| TRI16-I08 | P1 | T-6u four leading ratios pass; distinguish state vector from increment diagnostic, and conditional benchmark from HINDEX. |
| TRI16-I09 | P1/P2 | The 96:1 **coefficient ratio is not invariant under an unproved metric/observable dictionary**. Keep correspondence OPEN. |
| TRI16-I10 | P1 | GCL-06 child-remainder, fixed-sign face-phase, and CN-03 imports must be checked at claim level rather than blanket-repinned. |
| TRI16-I11 | P1 | Consumer acceptance matrix should separate earlier accepted uses, current v1.6.1 receipts and still-pending uses. |
| TRI16-I12 | P1 custody | Release/adoption records and `accepted_r4_2` source package are absent at the verified paths. Intake original bytes unchanged; don't claim independent owner certificate replay. |
| TRI16-I13 | P1 custody/safety | T-3a `v4g` source contains a zero forcing placeholder and dummy `Q_c` evolution while printing “CERTIFIED”; **not** an enclosure certificate. |
| TRI16-I14 | P2 | Methodology v1.4 migration/compaction: stacked header/footer, historical live text and compound grades; not a scientific regrade by itself. |
| TRI16-I15 | P2 | Carry exact negative/historical verdict boundaries without promoting predecessor reasons as current science. |

## 2. Independent scientific findings

### TRI16-I01 — P0: a conditional first integral of the corrected independent-orientation ODE

**[OWNER: Triadic v1.6.1 §6.18 L741–744, §6.4 L374–404, §2 L153–158]** The owner writes for the corrected *five-variable coefficient extension*
$$
\mathcal G:=Q_sQ_c-I_{sc}^2-\Omega^2,\qquad
\dot{\mathcal G}=\frac{\dot Q_s}{Q_s}\mathcal G,\qquad
K=\frac{I_{sc}^2+\Omega^2}{Q_sQ_c}.
$$
The published text draws tangency at `K=1`.

**[SESSION: exact conditional implication]** On an interval where the differentiable *coefficient ODE* is defined and `Q_s>0`,
$$
\boxed{D:=\frac{\mathcal G}{Q_s}
       =Q_c-\frac{I_{sc}^2+\Omega^2}{Q_s}
       =Q_c(1-K),\qquad \dot D=0.}
$$
Indeed `\dot D=\dot{\mathcal G}/Q_s-\mathcal G\dot Q_s/Q_s^2=0`. With `Q_c>0`, `D>0` implies `K<1` throughout its interval of validity; the surface `K=1` is invariant. In particular a finite crossing to `K=1` from `D>0` cannot occur while `Q_c` stays finite and positive, although convergence as `Q_c\to+\infty` is not ruled out. The related published `\dot K=(1-K)\dot Q_c/Q_c` is precisely the same identity. These implications use **only** the owner's differential identity and are not a reconstruction of `H_j` from unavailable producer bytes.

**Question to the owner:** Is `D` a genuine preserved quantity of the chosen truncated independent-orientation coefficient field, or does the identity cease to hold when the intended physical `K<1` carrier and its extra state variables are installed? Do not call it a conserved physical normal mode without a carrier/observable identification.

**Acceptance criterion:** independently reproduce `\dot{\mathcal G}=(\dot Q_s/Q_s)\mathcal G` from the *complete source expression* at `r^0,r^1,r^2`; if correct, record the explicit `D` implication under the ODE clock (possibly as a new owner RID if exported), its domain `Q_s,Q_c>0` and excluded boundaries. If not, correct the original asserted identity before a sensitivity sweep. No rerun of old mis-scaled trajectories.

### TRI16-I02 — P0: differential vs finite-step Gram law

**[OWNER: Triadic §6.18 L734–742, §6.3 L352–355, SG-18 L251–252].** The source says the Gram relation "forces" the factor `-\sqrt3` via
`2\Omega\Delta\Omega=Q_c\Delta Q_s+Q_s\Delta Q_c-2I_{sc}\Delta I_{sc}` at retained orders. That equality is a **first-variation/differential** identity. An actual finite six-step update also satisfies the exact algebraic expansion
$$
\Delta\mathcal G
=Q_c\Delta Q_s+Q_s\Delta Q_c-2I\Delta I-2\Omega\Delta\Omega
+\underbrace{\Delta Q_s\Delta Q_c-(\Delta I)^2-(\Delta\Omega)^2}_{\text{quadratic increment terms}}.
$$
**[SESSION: exact expansion, EV-RUN algebra]** The quadratic part vanishes only under a separate hypothesis or after a declared truncation. The recorded proof may quite legitimately drop it at its stated homogeneous order; this is **not** a refutation of `TRIAD-ALG-T6E-ORIENTATION-NORMALIZATION`. However the source must not imply an *exact*, all-amplitude discrete Gram conservation or exact discrete `D` conservation from the truncated ODE.

**Acceptance criterion:** owner labels its rate normalization as a coefficient-level differential/first-variation identity, provides the order valuation of the discarded `\Delta^2` terms in the exact six-step map and names the primitive vs six-step clock. Keep the sign/scale correction and all historic-withdrawal conclusions unless an actual order conflict is found.

### TRI16-I03 — P0/P1: T-6r carrier is the main missing physical model

**[OWNER: Triadic §2 L153–158; SG-3 L206–207; §4 L264–272; §6.4 L374–380; §6.8 L456–458; §6.18 L747–751.]** With two actual planar vectors in the declared positive-definite metric, the Gram identity forces `K=1`; the root model `M_root` cannot represent interior `K<1` merely by reparametrization. The five-variable coefficient extension is a *formal diagnostic*, not a verified physical carrier.

**[SESSION]** A minimal illustrative enlargement of a Euclidean planar pair illustrates the extra datum: with `s=(a,0,0)`, `c=(b,d,e)`, `I=ab`, `\Omega=ad`, `Q_s=a^2` and `Q_c=b^2+d^2+e^2`,
`K=(b^2+d^2)/(b^2+d^2+e^2)<1` if `e\neq0`. This does not construct an RTG Triadic law: the embedding, edge readouts, metric, apex coupling, event semantics, and state/action covariance are still missing.

**Acceptance criterion:** T-6r supplies (C1) an actual state carrier and metric, (C2) encoding/reduction maps and representation, (C3) full `Q_s,Q_c,I,\Omega,r` evolution and the fate of `D`, (C4) primitive/six-step clock and phase convention, (C5) event/contact predicates and field regularity, (C6) covariance under the declared node action. Keep no-basin and physical-route verdict OPEN until all are typed. RRF/OFN input is a contract, not permission to borrow their mathematical class-C realization as the Triadic birth mechanism.

### TRI16-I04 — P1: a uniform lower margin for leading corrected torsion

**[OWNER: Triadic §6.9 L474–480; §6.18 L741–744.]** The corrected leading coefficient is
$$
A_\theta^{\rm corr}=3\sqrt3\,\mu^2+6\mu\nu+9\sqrt3\,\nu^2.
$$
**[SESSION: exact SymPy eigenvalue check]** Its symmetric matrix is
$$
M_\theta=\begin{pmatrix}3\sqrt3&3\\3&9\sqrt3\end{pmatrix},
\qquad \operatorname{spec}M_\theta=\{6\sqrt3-6,\ 6\sqrt3+6\}.
$$
Therefore, for `K=\mu^2+\nu^2`,
$$
\boxed{6(\sqrt3-1)K\le A_\theta^{\rm corr}
           \le6(\sqrt3+1)K.}
$$
On `K=1`, the positive lower margin is `6(\sqrt3-1)` (approximately `4.3923`), stronger than pointwise sign-definiteness.

**Acceptance criterion:** consider registering this as a local algebraic corollary if useful for T-6r perturbation budgets. Any persistence of the sign for finite `u` or nonzero `r` requires a separately proved uniform remainder smaller than this margin; it is **not** a new corrected full-flow theorem.

### TRI16-I05 — P1: an exact *bookkeeping* sign table for T-6q

**[OWNER: Triadic §2 L162–167; §6.17.1 L625–630; §6.18 L730–735; RRF v0.8.4 §3.1.]** For an identified pair of planar source vectors, `Q_s=s^TBs`, `Q_c=c^TBc`, `I=s^TBc`, and `\omega_{\rm raw}=-\Omega/\sqrt3`. Direct algebra yields:

| Coordinate operation only | `Q_s,Q_c` | `I` | `\Omega` | `(\mu,\nu)` |
|---|---|---|---|---|
| `(s,c)\mapsto(c,s)` | exchange | unchanged | negated | `(\mu,-\nu)` |
| `(s,c)\mapsto(-s,c)` | unchanged | negated | negated | `(-\mu,-\nu)` |
| `(s,c)\mapsto(-s,-c)` | unchanged | unchanged | unchanged | unchanged |

`K` is invariant under each operation. **[SESSION]** This is a *kinematical sign-table proposal*, **not** a claim that any operation is a physical node-exchange gauge action, dynamical symmetry, carrier isomorphism or branch continuation.

**Acceptance criterion:** in T-6q label the actions on *complete state including role/incidence, chart, clock and event variables* and test intertwining with the actual selected update. Preserve T-6n's naive-flip failure and its OPEN continuation status; do not generate a mirrored `x_*` or safety wedge from this table.

### TRI16-I06 — P1: T-6s survives exact operator audit, no universal no-gain

**[OWNER: Triadic §6.15 L559–583; Genesis v2.9 HINDEX / owner metric definitions.]** With
`B=\bigl(\begin{smallmatrix}1&-1/2\\-1/2&1\end{smallmatrix}\bigr)`,
`J_Q=\frac1{\sqrt3}\bigl(\begin{smallmatrix}1&-2\\2&-1\end{smallmatrix}\bigr)` and
`H=(1-g_2)BJ_Q`,
**[SESSION: exact symbolic check]**
`J_Q^\top BJ_Q=B` and
`B^{-1}H^\top B^{-1}H=(1-g_2)^2I`.
Hence `\|H\|_B=|1-g_2|`. For real `g_2` the no-gain inequality is equivalent to `0\le g_2\le2`. The signed leading child ratio `i\kappa Q_s` is not the unit quarter-turn `i`; the fifth-order child remainder is **GCL-06-conditional**.

**Disposition:** retain owner ALG and the narrowed interval. Do not transfer to incoherent sources, unconstrained weight, physical HINDEX calibration or a selected child/source law.

### TRI16-I07 — P1: T-6t label rank is not physical dimension

**[OWNER: Triadic §6.16 L596–612 and §7.4 CN-01 L843.]** **[SESSION: exact algebra]** The Jacobi rows `(1,-1,0,0)`, `(1/2,1/2,-1,0)` and `(1/3,1/3,1/3,-1)` have Gram
`\operatorname{diag}(2,3/2,4/3)` and the declared diagonal weight transform gives `\operatorname{diag}(2,8/3,3)`. For every nonzero planar `s`, `\det[s,J_Qs]=2Q_s/\sqrt3\ne0`, so these two already span the common 2D carrier. The three signable coefficient labels do not produce three independent physical directions.

**Disposition:** retain ALG within the node-mediated realization. Require an enlarged physical carrier, metric and source map before any claimed apex–UV or transverse-source identification; GEN v2.9 GCL-05 and UVM v0.7.1 already respect that limit.

### TRI16-I08 — P1: T-6u exact algebra passes; numerical shortfall is typed

**[OWNER: Triadic §6.17 L623–721; GEN v2.9 §6.5–6.6.]** **[SESSION: exact independent symbolic check]** Using only the source-displayed `B,J_Q,V_s,V_c`,
$$
Q(V_s)=\frac7{1024}Q_s^3,\quad
Q(V_c)=\frac{61}{34992}Q_c^3,\quad
I_{V_s,s}=\omega_{V_s,s}=-\frac{Q_s^2}{16},
$$
and `D_{\rm birth}^{[s^3]}=7Q_s^3/512=2Q(V_s)`. The four fixed-policy ratios are precisely `\sqrt{21}/64,\sqrt{42}/64,\sqrt7/16,\sqrt{14}/16`, with the exact smallest shortfall `16/\sqrt7>6` against the **stipulated comparator** `\sqrt2`.

**Limit:** this independently validates the **displayed seed/operator algebra**, not the derivation of the microscopic Genesis source polynomial or the original 47-check code. The v1.6.1 `c^3` suppression is relative to the leading seed, and source interference / other channels remain unbounded at finite amplitude. The `D_{\rm birth}` numerator is an increment-channel diagnostic, not a second seeded state or a HINDEX norm.

**Disposition:** accept current scoped ALG; retain four-case typing and negative result against an automatic UV gate/physical deficit inference. No new finite-amplitude calculation until the physical source map is declared.

### TRI16-I09 — P1/P2: 96:1 is neither correspondence nor metric-invariant as written

**[OWNER: Triadic §1 L36; §6.1 L321–329; §6.18 L749–751; RRF v0.8.4 §3.1 L270–284.]** Owner correctly withdraws use of the naked coefficient ratio 96 as a same-system stability theorem. The primitive GEN and producer-Triadic planar metrics have the **same-vector conditional** relation `B_T=2B_G`, so the quadratic observable rescales `Q_T=2Q_G`.

**[SESSION: precise scaling example, not a source comparison]** If one **hypothetically** had the same generator/clock/state and `\Delta Q_G=a_GQ_G^2`, then `\Delta Q_T=2\Delta Q_G=(a_G/2)Q_T^2`. Thus a coefficient `a_G=1/4` would become `a_T=1/8`. A raw arithmetic comparison against a `24` coefficient in T-units would then numerically be `192` instead of `96`. **This is not a new physical ratio**: the two owner calculations are currently not proven to refer to one transported model, and it is not even established that the pump is in the GEN units of this hypothetical example. The exercise shows why ratio-of-coefficients claims require an observable/metric dictionary *before* numerical comparison.

**Acceptance criterion:** provide common generator and primitive/six-step clock, selected state/carrier and metric, actual representation arrow, projection and return extraction, and compared observable; then recompute both coefficients in one normalization. Otherwise retain 96 as arithmetic history only.

## 3. Interface, evidence and structural findings

### TRI16-I10 — P1: GCL-06 and typed phase/child scope

**[OWNER: Triadic §6.1 L314–317, §6.15 L563–567, §7.2 L811–822, §7.4 CN-02 L845–849; GEN v2.9 §1 L40–43 and §6.3.]** The source's fifth-order remainder is conditional on a selected child functional. For fixed nonzero `\kappa` and remainder `O(\|s\|^p)`, `p>3`, the correct amplitude-ratio correction is `O(Q_s^{(p-1)/2})` and leading face-phase correction `O(Q_s^{(p-3)/2})`. With `p=4` only `O(Q_s^{3/2})` and `O(Q_s^{1/2})` survive; with `p=5` one gains `O(Q_s^2)` and `O(Q_s)`. The conditional error was correctly repaired in v1.6.1 and remains unchanged in GEN v2.9.

**Disposition:** retain the correction, and make the next consumer-sync pass claim-specific: GEN source theorem and actual child functional, UVM phase readouts, and the fixed T-6m reference are not the same proposition. Historical valid v2.8.7 proof pins may remain where checked; a newer tag alone does not invalidate them.

### TRI16-I11 — P1: receiver dispositions and export status need an explicit current matrix

**[OWNER: Triadic §1 L48, §2 L64–67, §7.3–7.4 L826–888; GEN v2.9 §2 OPEN 1T L258–264; UVM v0.7.1 §§1,6,7; OFN v0.11 §11 RF-O08-02/03/08; RRF v0.8.4 §3.1.]** The live Triadic narrative broadly says “consumer acceptance pending,” while §7.4 itself records *prior scoped receipts* from Genesis, OPEN-M and OFN. These statements need not be contradictory: a v1.6 receipt is not automatically acceptance of every v1.6.1 delta, and the source has sometimes distinguished this. They are **too aggregated to use as a current interface-status table**, however.

**Disposition:** list CN-01…CN-05 by recipient, exact producer and receiver tag, claim-level pin, prepared/filed/received/statement accepted/adopted-use status and the remaining scientific gate. GEN v2.9 withdrew old wedge/no-basin conclusions, UVM v0.7.1 already narrowed T-6t and T-6u, OFN v0.11 records its half of pass two, RRF records only metric conventions; none proves a missing physical birth/source model. Historical pins are not automatically replaced by “latest”.

### TRI16-I12 — P1: source, adoption and certificate custody are incomplete in the repository

**[OWNER: Triadic header L12–17; §8 L896–939; §9 L943–953; Methodology v1.4 §§12–13.]** **[UNVERIFIED]** At the tagged and current repository tree, the named v1.6.1 release record (`records/RELEASE_RECORD_v1_6_1.md`), owner adoption JSON (`records/OWNER_ADOPTION_v1_6_1.json`) and `evidence/accepted_r4_2/` return NOT_FOUND. Likewise the direct owner proof sources for many §8 items are described but not independently available. This review does **not** assert those original records never existed or that recorded checks failed. It states that their asserted SHA/checker claims cannot be reproduced from the currently accessible repository.

**Disposition:** accept unchanged original materials under `upload/triad-records`, hash-check and place once, with an explicit placed / held-hash / missing ledger. Do not recreate historical source outputs, treat a new script as an old one, or infer scientific adoption from a checker PASS. The T-6j2 script/log remains separately missing at the source; its excursion is still an author-reported historical NUM, not certified event identity.

### TRI16-I13 — P1: T-3a “Arb enclosure” upload is not a certificate

**[SESSION: EV-CODE]** The PI-supplied `triad_t3a_arb_enclosure_v4g.cpp` under the Dyadic source intake has, at source L91–96, the actual forcing terms elided and `arb_set_d(dz,0.0)` as a placeholder. At L125–130, `Q_c` advances by a dummy `+1`; L135 can print `[CERTIFIED / z(t) >= z0]`, while the reported protocol calls itself interval Picard integration at L154. This does not enclose solutions of the declared physical/diagnostic Triadic ODE. No proposed algorithm using merely pointwise Arb arithmetic automatically certifies global ODE trajectories.

**Disposition:** label the unchanged received bytes as **INCOMPLETE SCAFFOLD / NOT A SCIENTIFIC CERTIFICATE**; do not use its printed `CERTIFIED` status as proof of a T-3a, T-6r, basin or safety claim. Recovery of the full right-hand side, validated integrator, initial/domain enclosures and negative-control fixtures is a separate owner/custody job, not grounds to rerun a nonexistent historical campaign.

### TRI16-I14 — P2: migration to Methodology v1.4 is structural, not a back-door regrade

**[OWNER: Triadic header L4–17, Local Tag Aliases L19–28, §§1–9, Appendix A L955–1131, Appendix B L1132–1197, footer L1200–1202; Methodology v1.4 §§1.1,3.4,8,13.6.]** The live header declares v1.3 limited migration and mixes predecessor release narratives into live fields; Appendix A repeats historical drafts; the footer stacks v1.6.1 and v1.6 release endings. Compound forms such as `[ALG/NUM synthesis]`, `[ALG+NUM diagnostic]`, `[DEF/ALG]` survive as literal labels or source-grade summaries; at points of use, the scientific assertion grade must be separated from numerical/engineering corroboration. RIDs, old source scopes, historical proof pins and explicit negative results must survive any migration.

**Disposition:** after the scientific-owner rows are decided, use a correction stage and a **layout-only, claim-preserving** compaction stage with a movement map, negative fixtures and exact predecessor identities, if the successor also migrates. Do not require a full scientific rerun solely because Appendix A is long or a historical pin predates a companion version. Keep one immediate predecessor and one footer, with history retained under immutable tags/records.

### TRI16-I15 — P2: preserve negative results without reviving invalid predecessor reasons

**[OWNER: Triadic §§6.11–6.14 L493–549 and Appendix B L1132–1197.]** Current text correctly withdraws the corrected-model wedge, physical route-closure and “0/120 fatal” claims. Appendix B preserves predecessor rejections and their old reasons, including assertions that torsion “drives fatal sectors” or the 5.5-degree wedge governs (§Appendix B L1187–1196). Their *historical* placement is legitimate; those old reasons must not be read as present explanatory evidence.

**Disposition:** a compact current-state negative ledger should identify the valid failure separately (e.g. `I_{sc}=0` is not invariant in the declared root model; contact alone does not prove annihilation) and the withdrawn historical inference as withdrawn. Leave old text retrievable at the tagged predecessor, not as a competing current-use theory.

## 4. Recommended next action and acceptance gates

1. **Freeze the two independent advisories first**; only then compare finding lists, identify unique scientific results and unresolved disagreements. Owner sessions disposition each row; the PI decides adoption. This review is not a substitute for either.
2. **Priority science before trajectories:** T-6r owner checks `D=\mathcal G/Q_s` using the complete original corrected expressions and defines the physical/nonphysical carrier; T-6q produces the state/action sign table. The coercivity lemma can be accepted at a strictly leading algebraic scope. A full corrected-field simulation is premature until those gates are passed.
3. **One batched successor stage-1 correction set**, if adopted: model/clock typing; first-integral/finite-difference scope as needed; current recipient matrix; exact scoped HINDEX/child/seed imports and missing evidence classification. Do not reopen T-6s/t/u arithmetic without a concrete contradictory test.
4. **Optional stage 2:** Methodology v1.4 compaction separate from scientific changes, with explicit proof/source coverage and negative fixtures. Source files received from outside remain byte-exact.
5. **Consumer notification:** after an owner release, send claim-specific notices to GEN, UVM, OFN and RRF only where statements or interfaces change. Filing a pipe is not a receiver's adoption; no RER/FMS/ER-2B science is automatically modified.

**Limits:** The review does not establish a physical `K<1` carrier, real Triadic dynamical invariant for the *full discrete map*, exact global torsion sign, independent UV source, source-amplitude adequacy, physical birth, annihilation or a continuous/discrete bridge. Historical numerical campaigns and certificates were **not** repeated. Source-reported artifacts remain source-reported; an independently checked formula is not an independent implementation of the complete owner model.

**Final status:** independent blind advisory and session algebra only. Canonical TRIAD, all scientific RIDs/grades, pipe states, owner dispositions, merge and release tags unchanged.
