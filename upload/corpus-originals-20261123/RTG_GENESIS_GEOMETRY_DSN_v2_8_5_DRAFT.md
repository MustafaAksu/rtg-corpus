# RTG_GENESIS_GEOMETRY_DSN_v2.8.5_DRAFT

**Title:** RTG Genesis Geometry Study — Canonical Scientific Ledger  
**Date:** 5 October 2026  
**Scope:** Primitive dyadic/triadic/tetrahedral Genesis algebra, quaternionic metric lift, UV completion, foam network structure, and Regge bridge. Imports settled continuous-branch results from Dyadic and Triadic with inherited scope; routes TDR-G dependencies through explicit bridge requirements only.  
**Draft base / supersedes on adoption:** `RTG_GENESIS_GEOMETRY_DSN_v2.8.4` · `RTG_GENESIS_GEOMETRY_DSN_v2.8.3` · `RTG_GENESIS_GEOMETRY_DSN_v2.8.2` · `RTG_GENESIS_GEOMETRY_DSN_v2.8.1` · `RTG_GENESIS_GEOMETRY_DSN_v2.8.0` · `RTG_GENESIS_GEOMETRY_DSN_v2.7.7` · `RTG_GENESIS_GEOMETRY_DSN_v2.7.6` · `RTG_GENESIS_GEOMETRY_DSN_v2.7.5` · `RTG_GENESIS_GEOMETRY_DSN_v2.7.4` · `RTG_GENESIS_GEOMETRY_DSN_v2.7.3` · `RTG_GENESIS_GEOMETRY_DSN_v2.7.2` · `RTG_GENESIS_GEOMETRY_DSN_v2.7.1` · `RTG_GENESIS_GEOMETRY_DSN_v2.7` · `RTG_GENESIS_GEOMETRY_DSN_v2.6` · `RTG_GENESIS_GEOMETRY_DSN_v2.5` · `RTG_GENESIS_GEOMETRY_DSN_v2.4` · `RTG_GENESIS_GEOMETRY_DSN_v2.3` · `RTG_GENESIS_GEOMETRY_DSN_v2.2` · `RTG_GENESIS_GEOMETRY_DSN_v2.1` · `RTG_GENESIS_GEOMETRY_DSN_v2.0` · `DSN_RTG_Genesis_Study_v1.1` · `DSN_GENESIS_II_UV_PATCH_v0.1` (absorbed)  
**Companion documents:** `RTG_PROGRAMME_OVERVIEW_v1.2` · `RTG_ONTOLOGICAL_FOUNDATIONS_v0.8` · `DSN_METHODOLOGY_v1.3` · `RTG_DYADIC_OSCILLATOR_DSN_v6.4.10` · `RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6` · `RTG_DISCRETE_GENESIS_DSN_v2.12.13`  
**DSN Methodology:** DSN_METHODOLOGY_v1.3  
**Programme tier:** Tier 3/4 — Integrating document; imports scoped continuous-branch results from Dyadic and Triadic; routes Discrete/TDR-G dependencies through explicit bridge requirements only.  
**Status summary.** *(v2.8.5 draft; correction/reconciliation-first. Version history remains in Appendix A.)* Primitive Genesis algebra through the certified tetrahedral quartic polynomials is retained. This draft applies the frozen GCL-01–11 corrections and reconciles adopted Triadic v1.6 consumer notices without importing the optional v0.20 cubic/quartic extensions. The principal owner-state changes are: (i) the birth residual is object-typed — the raw six-step residual contains a nonzero quartic term, while the odd/normal-form residuals support the fifth-order remainder; the physical residual choice remains OPEN; (ii) the physical child W-ratio is \(i\kappa Q_s\) at leading order, not the unit-quarter-turn identity \(i\), and the full face-phase remainder is conditional on the child remainder order; (iii) §6.8/9B-tau contains a sign-branch inconsistency — the printed \(+2a\tau\) numerator reconstructs exactly with \(K=\tau I-\Delta M_f\), while the physical operator sign remains OPEN; (iv) 9B closes the covector type but does not uniquely force \(B\) as the physical lowering map, so the PSD residue is retained conditional on \(S_f=Bc_f\); (v) the 9C family is retained as the exact solution of an additional raw-array \(B\)-self-adjointness premise, not a requirement implied by 9B; (vi) the former apex–UV slot identity is retracted while the Jacobi \(d\)-mode and primitive seed diagnostics remain; (vii) Triadic v1.6 withdraws current use of the historical \(x_*\), 5.5° wedge, no-safe-basin and phase-steering route-obstruction chain, while preserving the exact reference quarter-turn and narrowed T-6s/t/u successor results; (viii) OPEN 1A candidate #2 is archival-chart evidence only, not a proved gauge-class invariance theorem; (ix) the ×2 SU(2) amplitude verdict is conditional on both the \(h\leftrightarrow\|H\|_B\) bridge and an explicit energy-to-amplitude square-root constitutive relation; and (x) the reduced-model saturation ceiling \(Q_d^*\approx1.13\times10^{-2}\) is distinguished from the window-dependent control-loss values. Internal typing/model questions therefore remain OPEN alongside OPEN M and OPEN 0-Regge. Candidates A–C and V20-O1–O5 are not admitted in this draft.

## Local Tag Aliases

| Local alias | Expands to | Used for |
|---|---|---|
| `[ALG structure]` | `[ALG]` `[scope: structural / open coefficients]` | structural algebraic result with open coefficients, normalization, or completion |
| `[ALG-conditional]` | `[ALG]` `[scope: conditional on named hypothesis]` | exact result conditional on a named unproven hypothesis |
| `[INTERP]` | `[HEUR]` `[scope: ontological interpretation]` | motivational interpretation layer |
| `[CONVENTION]` | `[DEF]` `[scope: gauge / normalization choice]` | fixed by chosen convention, not derivation |

`[DEF]` New cross-document imports and exports must use canonical forms from `DSN_METHODOLOGY_v1.3`. Local aliases above are permitted inside this document for readability.  
`[DEF]` `[COR]` is a canonical DSN workflow tag; it does not require local aliasing.

---

## §1. Current Canonical State {#sec-1-canonical-state}

`[DEF]` `[RID: GEN-DEF-PRIMITIVE-MAP]` **Primitive generator.**
$$T(\rho,\eta)=\bigl(\rho-\sin\eta,\;\eta+e^\rho-1-\sin\eta\bigr).$$

`[THM]` `[RID: GEN-THM-LIN-ORDER6]` $\lambda = e^{\pm i\pi/3}$; $A^3 = -I$; $A^6 = I$. Order-6 elliptic resonance at the origin.

`[THM]` **Pure chiral protection.** All quadratic terms cancel in the pure chiral antisymmetric channel. With longitudinal background $s \neq 0$, mixed quadratic terms survive.

`[THM]` **\(\Phi_{2\to3}\) leading one-dimensional transverse birth.** The certified cubic birth direction is
\[
c_0^{[3]}=\kappa Q_sJ_Qs_*.
\]
If the selected child functional is built from a residual with fifth-order absolute remainder (as for the odd/normal-form residual objects), then \(c_0=\kappa Q_sJ_Qs_*+O(|s_*|^5)\) and \(Q_c=\kappa^2Q_s^3+O(Q_s^4)\). The raw six-step residual carries a nonzero quartic term, so the same fifth-order remainder is **not** asserted for a raw-residual birth; the physical residual/child functional remains OPEN (GCL-06).

`[THM]` **Tetrahedral chronological protection.** All one-step quadratic forcing cancels over one 6-step tetrahedral block: $G_2(Z) = 0$.

`[THM]` **Primitive $Q_d$-quartic drift closed.** The full primitive $Q_d$-quartic drift polynomial $\mathcal{P}_4(s,c,d)$ is closed; see §6.5.

`[THM]` **Triad chiral admissibility surface closed (OPEN 1C).** Standalone triad and K4-shadow chiral drift are both nonnegative-definite:
$$\Delta Q_c^{(4)}\big|_{\rm standalone} = \tfrac{1}{3}Q_c^2 + \tfrac{1}{4}(I_{sc}+\omega_{sc})^2 + \tfrac{5}{16}\omega_{sc}^2 \geq 0,$$
$$\Delta Q_c^{(4)}\big|_{\rm K4\,shadow} = \tfrac{1}{3}Q_c^2 + \tfrac{1}{4}(I_{sc}+\tfrac{19}{24}\omega_{sc})^2 + \tfrac{359}{2304}\omega_{sc}^2 \geq 0.$$
The standalone triad is a **universal chiral pump**: no quartic safe surface exists except $c=0$. Certified by `genesis_k4_route_census.py` (all PASS) and independent two-route re-derivation. See §6.5.

`[FAIL]` **No $Q_s^3$ safe surface.** $Q_{c,\rm safe}(s^+) = C_{\rm triad}Q_s^3 + O(Q_s^4)$ is not supplied by primitive quartic triad dynamics; consequently constant perturbative $\kappa_{\rm phys}$ from capacity matching is `[FAIL]`. Physical $\kappa$ selection moves to the NF frame, higher order, or network/UV policy.

`[THM]` **NF/primitive sign split (typed comparison).** NF chiral healing gives $-Q_c(Q_s+Q_c)$ while primitive incidence gives $+\tfrac{1}{3}Q_c^2$ at pure $c^3$ — opposite signs in their declared constructions. NF-frame healing is a normal-form coordinate statement, not a primitive-amplitude statement. **No claim is made here that a passive representation change alone explains the sign difference; matched model/mode/observable/clock transport remains unresolved (Candidate B deferred).**

`[ALG]` **Uniform independent phase average.** $\langle\mathcal{P}_4\rangle_{\rm ind.phase} = -Q_d^2 - \frac{1}{12}Q_dQ_s - \frac{1}{9}Q_dQ_c \leq 0$. Always a sink; cannot produce $4\to5$ cascade.

`[THM]` **Universal no-go.** $T_{\mathbb{H}} = T \oplus T \Rightarrow w=0$. Block-diagonal quaternionic extension cannot generate a smooth 3D metric branch.

`[THM]` **Smooth single-face metric criterion.**
$$Q_s>0,\quad \beta\neq0,\quad \Delta_3>0,\quad \sigma_f\neq0,\quad w\neq0 \;\Rightarrow\; \det\Gamma_{\mathbb{H}} = \beta^2\Delta_3 Q_s^3 > 0.$$

`[THM]` **Local sourced-junction theorem.** If $w=0$ and $\sigma_f\neq0$: vacuum gluing fails ($S_f = 0$ is impossible), but the constrained birth $(\Delta M_f + \tau I)d_\perp + S_f = 0$ has a valid minimizer. The foam branch is sourced-birth, not no-birth.

`[ALG]` **Apex-correlated foam.** All active faces sharing apex $D$ must satisfy $d_{\perp,f}^* = d_\perp^{(D)}$; the $\Pi_\perp$ displacement belongs to the apex, not individual faces.

`[RESULT]` **Programme dependency:** $\text{OPEN M}_{\rm smooth} \prec \text{OPEN 0}_{\rm smooth}$.

`[OPEN]` **UV data.** $\alpha_f$ and $w = \mu_1 + i\mu_2$ remain distinct UV data until OPEN M is resolved.

`[RESULT]` **Genesis II archival recovery (promoted in v2.2).** The May 22 Genesis II audit items are now certified following attachment of `genesis_k4_route_census.py` (all PASS) and `genesis_birth_race_model.py`: OPEN 1C closed `[THM]`; vector apex seeding $G_{3,d}(s,c,0)$, $Q_{d,1}^{[s^3]}=\tfrac{7}{1024}Q_s^3$, and $\Delta Q_s^{(4)}$ shadow all `[ALG verified]`; corrected $J_Q$, birth-symmetry sign, and phase-drift law promoted to `[ALG]`; rejected mechanisms (HYP-A, HYP-C, incoherent seeding, smooth-$\chi$) promoted to established `[FAIL]`. The cascade threshold $|\alpha_f|\ge 0.012$ remains `[HYP]` (model-dependent). See OPEN-GEN-II-7B and §6.5–§6.6.

`[ALG]` `[scope: scalar-M ansatz M=gI]` **Scalar-M resolvent** (Genesis II UV patch). Under the scalar-M ansatz:
$$((\tau-g)I - \Delta M_f)^{-1} = \frac{(\tau-g)I + \Delta M_f}{(\tau-g)^2 - \kappa^2}.$$
Algebraic poles occur at $\tau-g=\pm\kappa$. The physically relevant soft branch must be specified by the constrained-lift sign convention; branch selection is part of OPEN-GEN-II-9. `[RID: GEN-ALG-SCALARM-RESOLVENT]`

`[DEF]` **Immediate frontier.** With OPEN 1C and the scalar-M 9-series closed, the cascade question routes entirely through OPEN M. The highest-value next computations are (i) **OPEN M proper** — deriving the two UV scalars $\|H\|_B$ and $g$ from the UV completion and running them through the certified cascade test $(\|H\|_B/g)|w|\gtrsim0.024$ (the reduced-wrapper threshold recorded as hypothesis-grade under OPEN-GEN-II-7B; the earlier $|\alpha_f|\gtrsim0.012$ framing as the next target is superseded by this $B$-native form); (ii) **OPEN 0-Regge** — the minimal holonomy-consistent curvature cluster, which blocks continuum gravity independently of OPEN M; and (iii) **OPEN 1** follow-up — the physical phase-moment distribution $\mathcal{M}_{\rm phase}$ (reduced to a finite moment problem in OPEN 1A).

---

## §2. Active Frontier / OPEN Registry {#sec-2-open-registry}

### Priority ordering

**Immediate Genesis frontier:**
1. **OPEN 1 — Physical phase-moment distribution.** Determine $\mathcal{M}_{\rm phase}$ for the cascade condition $\langle\mathcal{P}_4\rangle > 0$. **Reduced to a finite moment problem in v2.7.4 (OPEN 1A):** $\langle\mathcal{P}_4\rangle$ is linear in 13 phase moments; leading criterion $\langle\cos\phi_{ds}\rangle+\tfrac{\sqrt3}{2}\langle\sin\phi_{ds}\rangle<0$. Candidate #1 (plateau) leading-favorable but threshold-insufficient. Remaining: candidates #2–#4.
1b. **OPEN 1T — Triadic v1.6 phase/interface import protocol.** Reconciled in this draft: the historical $x_*$, $[0^\circ,5.5^\circ]$ safety wedge, no-safe-basin and phase-steering route-obstruction chain are withdrawn from current Genesis use under CN-05. Retained imports are limited to currently adopted, explicitly scoped Triadic v1.6 statements; no replacement global phase/basin theorem is imported.
2. **OPEN-GEN-II-7B — Cascade-to-OPEN-M bridge.** Derive $\alpha_f$ from the OPEN M UV jet and test the reported cascade threshold $|\alpha_f|\ge 0.012$. The isolated-$K_4$ saturation ceiling makes a non-$\mathcal{P}_4$ pure-seeding source (OPEN M $\sigma_f$ form) the only viable cascade mechanism; cascade and OPEN M are now the same computation.
3. **OPEN-GEN-II-9 — Exact constrained resolvent** (UV patch). Sub-steps 1–4 closed under scalar-M (OPEN-GEN-II-9A); next is general eigendecomposition once OPEN M supplies $M_{\rm spin2}$.
3b. **OPEN-GEN-II-9C — $M_{\rm spin2}$ anisotropy.** Verify whether the physical $M_{\rm spin2}(x)$ carries the diagonal splitting $(M_{\rm spin2})_{11}-(M_{\rm spin2})_{22}=-2m\,\Im w$ required for $B$-self-adjointness of the secular operator. Operator-side target for OPEN M. **v2.7.6:** the complete admissible solution space is certified as the two-parameter family $M_{\rm spin2}(g,D)$, collapsing $K$ into the $B$-commutant $\mathrm{span}\{I,P\}$; any $B$-self-adjoint OPEN M construction must land in this family.
3c. **OPEN-GEN-II-HINDEX — source-block index trace.** CLOSED (v2.7.7): $H$ is covector-valued; $\|H\|_B^2=\lambda_{\max}(B^{-1}H^\top B^{-1}H)$; checksum $H=\sigma B\Rightarrow$ double root $\sigma^2$; norm convention unified with $\|M\|_B$. Guard lifted.
4. **OPEN M — Quaternionic metric lift.** Derive UV blocks $H(x)$, $M_{\rm spin2}(x)$.

**Recently closed:**
- **OPEN 1C — Triad chiral admissibility surface.** `[THM CLOSED]` in v2.2. $\Delta Q_c^{(4)} \geq 0$ (universal chiral pump); no $Q_s^3$ safe surface. See §6.5.
- **OPEN-GEN-II-9A — Scalar-$M$ soft-pole residue.** Sub-steps 1–4 closed under scalar-M ansatz in v2.3. Soft pole generically excited; residue PSD under either Euclidean or lowered-covector source convention. See §6.9.
- **OPEN-GEN-II-9B — Source index type / lowering bridge.** PARTIAL after GCL-03: covector type is closed, but \(B\) is not uniquely forced as the physical vector→covector lowering map. Conditional on \(S_f=Bc_f\), the residue is PSD. 9B-tau reconstructs the printed secular equation exactly for \(K=	au I-\Delta M_f\); physical \(\pm\Delta M_f\) sign/energy selection is OPEN under GCL-02. See §6.9.

**Secondary / blocked frontier:**
5. **OPEN 5/2B — face-phase / gap typing.** PARTIAL: the unit \(J_Q\) quarter-turn identity is distinct from the physical leading child ratio \(i\kappa Q_s\); the leading face phase is fixed only after the sign of \(\kappa\), while the full-phase remainder depends on GCL-06 residual typing. OPEN 5/2B-a retains the certified in-plane polynomial gap \(\frac13Q_c^2+\frac34Q_sQ_c\). The T-6u primitive seed ratio is retained only as a seed diagnostic; the former apex–UV slot localization is retracted (GCL-05/CN-01).
6. **OPEN K — Physical birth coefficient.** OPEN 1C remains resolved: capacity matching does **not** select $\kappa_{\rm phys}$ (universal pump, no $Q_s^3$ safe surface). The former safety-window route is withdrawn from current use by Triadic v1.6 CN-05; $\kappa$ selection remains OPEN and routes to higher-order, network/event, or UV policy without a wedge premise.
7. **OPEN M-foam — Network phase compatibility.** Downstream of local sourced-junction structure.
8. **OPEN 0-Regge → OPEN 0.** Blocked by OPEN M and the smooth metric branch; $\kappa_{\rm RTG}$ cannot be defined before both are closed.

**Handoff queue** — for upstream documents:
- Triadic: adopted v1.6 retains the exact reference quarter-turn but withdraws the historical wedge/no-basin/phase-steering obstruction chain. Any new orientation-flow input to Genesis requires the corrected Triadic model/domain obligations (T-6r/T-6q), not reuse of the old T-6m/T-6p route-closure narrative.
- Discrete (TDR-G): TDR-24D/A/B, OPEN TDR-19, native TDR-T phase/orientation statistics, and a named discrete-continuous bridge theorem are required before TDR-G–induced phase moments can be imported.

---

**OPEN 1 — Phase distribution / cascade criterion** [RID: GEN-OPEN-PHASE-DIST]

Status: ACTIVE  
Question: What is the physically relevant phase moment set $\mathcal{M}_{\rm phase}$?

Active sub-items:
- Plateau attractor phase moments: `[OPEN]`
- Dyadic Lie-gauge projected moments: `[OPEN]`
- Network-gluing induced moments: `[OPEN]` — constrained by the v2.2 saturation result: identical-cell network aggregation $m\mathcal{P}_4$ cannot break the $\mathcal{P}_4=0$ ceiling ($Q_d^* \approx 1.13\times10^{-2}$, ≈23% of threshold). Plateau-neighbor (HYP-A) gives zero injection; heterochronous uniform-phase spread (HYP-C) is net negative. Net cascade requires a non-$\mathcal{P}_4$ source (routed to OPEN-GEN-II-7B).
- TDR-G policy-induced moments: `[OPEN]` — requires OPEN TDR-19, TDR-24D/A/B, native TDR-T discrete triadic dynamics, and an explicit discrete-continuous bridge theorem. The historical Triadic wedge/phase-steering chain is not a current premise; the retained T-6m reference quarter-turn does not by itself authorize TDR-G import.

Closed sub-item:
- Uniform independent phase average: `[ALG]` ✓ — always a sink, $\langle\mathcal{P}_4\rangle_{\rm ind.phase} \leq 0$.
- $\mathcal{P}_4$-only cascade within the reduced birth-race model: `[RESULT]` `[scope: reduced birth-race model]` ✓ — **impossible**. Checksum-certified (`checksum_v272.py`): the full-$\mathcal{P}_4$ scalar race saturates at $Q_d^* \approx 1.13\times10^{-2}$ (shear $1.133\times10^{-2}$, recoil $1.166\times10^{-2}$), with control-loss value $Q_d(n_{\rm ctrl}) \approx 5.6\times10^{-3}$ across the lower window $Q_{s,0}\in[10^{-3},10^{-2}]$ (declining to $2.3\times10^{-3}$ at $Q_{s,0}=5\times10^{-2}$), and $\max_{\rm scanned}Q_d = 5.67\times10^{-3} < Q_{d,\rm thresh}=0.05$ over both $\kappa$ policies. This is scoped to the reduced model, **not** a theorem over arbitrary $\mathcal{M}_{\rm phase}$: the question of the physically selected distribution remains open (sub-items above). Cascade requires a non-$\mathcal{P}_4$ source (OPEN-GEN-II-7B).

---

**OPEN 1A — Phase-moment reduction** [RID: GEN-OPEN-PHASE-MOMENT]

Status: ACTIVE (reduces OPEN 1 to a finite moment problem) | v2.7.4  
Result: averaging the certified primitive $\mathcal{P}_4$ over any phase distribution $\mathcal{M}_{\rm phase}$ on $(\phi_{ds},\phi_{dc},\phi_{sc})$ yields $\langle\mathcal{P}_4\rangle$ as a **linear form in exactly 13 trigonometric phase moments**: $\{1, c_{dc}, c_{dc}c_{sc}, c_{dc}s_{dc}, c_{dc}s_{sc}, c_{ds}, c_{ds}c_{sc}, c_{ds}s_{ds}, c_{ds}s_{sc}, s_{dc}, s_{dc}^2, s_{ds}, s_{ds}^2\}$. No higher moments enter. The cascade condition $\langle\mathcal{P}_4\rangle>0$ is therefore a **finite linear inequality**, not a functional over arbitrary measures.

Leading-order dominant lever (birth gauge $I_{sc}=0$, $\phi_{dc}=0$; $Q_c=\kappa^2Q_s^3$, $Q_d=bQ_s^3$): the first $d$-$s$ phase moments enter at $Q_s^3$, one order below the constant drift and all other moments ($Q_s^4$):
$$\langle\mathcal{P}_4\rangle \sim -Q_s^3\sqrt{b}\left[\tfrac18\langle\cos\phi_{ds}\rangle + \tfrac{\sqrt3}{16}\langle\sin\phi_{ds}\rangle\right] + O(Q_s^4).$$
Cascade-necessary (leading order):
$$\boxed{\langle\cos\phi_{ds}\rangle + \tfrac{\sqrt3}{2}\langle\sin\phi_{ds}\rangle < 0}\quad\text{i.e. }\langle\cos(\phi_{ds}-\delta)\rangle<0,\ \tan\delta=\tfrac{\sqrt3}{2}\ (\delta\approx40.9°).$$

| Claim | Status |
|---|---|
| $\langle\mathcal{P}_4\rangle$ linear in 13 phase moments | `[ALG]` |
| Cascade condition is a finite linear moment inequality | `[RESULT]` |
| Leading lever is the $d$-$s$ first moment (at $Q_s^3$) | `[ALG]` |
| Criterion $\langle\cos\phi_{ds}\rangle+\tfrac{\sqrt3}{2}\langle\sin\phi_{ds}\rangle<0$ | `[RESULT]` `[scope: primitive $\mathcal{P}_4$, birth gauge, leading order]` |

Cross-checks (artifact `open1_moment_reduction.py`): uniform independent phases give lever $0$ → sink (consistent with the certified $\langle\mathcal{P}_4\rangle_{\rm ind.phase}\leq0$); deterministic birth-drift gives lever $<0$ (leading-favorable) but saturates (consistent with the v2.7.2 reduced-model ceiling).

**Candidate #1 — plateau attractor** (artifact `open1_plateau_candidate.py`): the plateau distribution generated by the certified phase-drift law from the birth phase $\phi_{ds}^{(1)}=\pi+\arctan(\sqrt3/2)=220.9°$ gives race-averaged lever $L\approx-1.30<0$ across all tested seeds (e.g. $Q_{s,0}=10^{-2}$: $\langle\cos\phi_{ds}\rangle=-0.6605$, $\langle\sin\phi_{ds}\rangle=-0.7437$, $L=-1.3045$). The phase drifts $\sim0.81$ rad over the race but stays entirely inside the favorable $L<0$ half-plane ($130.9°$–$310.9°$). Verdict: leading-favorable `[RESULT]` `[scope: reduced birth-race phase dynamics]`, but threshold-insufficient in the reduced model `[FAIL]` `[scope: reduced model]` — the favorable margin is $O(Q_s^3\sqrt{b})$, capped by the $Q_d^*\approx1.13\times10^{-2}$ ceiling (v2.7.2). This explains the saturation at the phase-moment level: the distribution is on the correct side, the magnitude is too small.

**Candidate #2 — dyadic chart comparison** (artifact history `open1_liegauge_candidate.py`, corrected by GCL-07): the statement $h_3=0$ belongs to the **archival** coordinate change, not the adopted polynomial conjugacy. The previously quoted $O(Q^{3/2})$ phase-shift bound is therefore retained only at archival-chart scope; the general claim that the lever is gauge-class invariant is withdrawn. Supporting only: the isolated-dyad conjugacy has a leading $h_2$ shift small compared with the previously tested tolerance, but this is not the coupled-network normalizer and does not close the full-map/observable comparison. **Verdict: full map + observable retest OPEN; candidate #2 is not a closed gauge-invariance result.**

**OPEN 1A candidate table (v2.8.1):**

| # | Candidate | Verdict |
|---|---|---|
| 1 | plateau attractor | leading-favorable ($L\approx-1.30$), threshold-insufficient |
| 2 | dyadic chart comparison | archival $h_3=0$ scope only; full map/observable retest OPEN |
| 3 | network-gluing | constrained no-gain (cannot beat the saturation ceiling) |
| 4 | TDR-G policy | blocked behind OPEN TDR-19 / T-6m |

**OPEN 1 remains ACTIVE.** Candidate #2 is reopened at the full-map/observable level by GCL-07, and the historical Triadic phase-steering obstruction is withdrawn by adopted v1.6 CN-05. The reduced $\mathcal P_4$ saturation result remains valid at its declared wrapper scope, but this draft does **not** claim that all phase routes are exhausted or that phase selection is globally settled. OPEN M remains the required source branch for the reduced-model cascade mechanism; broader route closure is not inferred.

---

**OPEN 5/2B — Face W-phase / gap functional** [RID: GEN-OPEN-WPHASE]

Status: ACTIVE (algebraically corrected; interpretation/UV use remains OPEN) | v2.8.5 draft

`[ALG, exact]` **Unit quarter-turn identity.**
\[
\frac{W(J_Qs)}{W(s)}=i\qquad(s\ne0).
\]
This is an identity for the unit \(J_Q\) direction; it is **not** the physical child/parent amplitude ratio.

`[ALG, exact]` **Leading physical child ratio.**
\[
c_0^{[3]}=\kappa Q_sJ_Qs_*,
\qquad
\frac{W(c_0^{[3]})}{W(s_*)}=i\kappa Q_s.
\]
Both retained reference policies have \(\kappa<0\), so the leading child/parent phase is \(-\pi/2\). Define the face-phase diagnostic separately from the six-step return map:
\[
F_{\rm face}^{(0)}
=-\frac{\pi}{2}+\arg\mu_6
=-3.550230508687\ldots
\equiv2.732954798492\ldots\pmod{2\pi}.
\]
The leading phase is shared by policies with the same sign of \(\kappa\); the magnitude \(|\kappa|Q_s\) is policy-dependent.

**Remainder-order guard (GCL-06).** If
\[
c(s)=\kappa Q_sJ_Qs+r(s),\qquad r(s)=O(\|s\|^p),\quad p>3,
\]
then on a continuous local phase branch the phase perturbation is bounded by
\[
\delta\theta=O(\|s\|^{p-3})=O\!\left(Q_s^{(p-3)/2}\right),
\]
provided the leading child is nonzero. Thus \(p=5\) permits \(O(Q_s)\), while a raw-residual quartic transmitted into the child (\(p=4\)) permits \(O(Q_s^{1/2})\). This is an upper-order bound, not a claim of nonzero phase motion. The physical residual/child functional remains OPEN.

`[ALG diagnostic]` `[RID: GEN-OPEN-WPHASE-GSPLIT]` **OPEN 5/2B-a — gap-functional mode-split audit.** At the exact \(I_{sc}=0\) birth diagnostic,
\[
\Delta\mathcal{E}_c^{\rm birth}
=\frac13Q_c^2+\frac34Q_sQ_c.
\]
Triadic v1.6 CN-03 independently checks the same sign-even specialization; the proof dependency remains Genesis \(\to\) Triadic, not the reverse. The certified in-plane birth gap is therefore not a scalar function of \(F_{\rm face}\) alone. This statement does not supply UV energy sufficiency, an apex embedding, or a physical source norm.

The historical free \(F_W(\eta_*)\) parametrization and old unit-ratio physical reading are retained only in version history/artifact provenance. Live text uses \(F_{\rm face}\) for this diagnostic to avoid collision with the Dyadic/RECOG/RRF six-step return \(F_W\).

---

**RESULT-P0-DYADIC — SU(2) representation lift of the $p=6$ resonance** [RID: GEN-IMPORT-P0-DYADIC]

Status: `[CAND/conditional]` (repinned to Dyadic DSN v6.4.10; scientific import scope corrected in v2.8.5 draft) | historical integration v2.8.1  
Import (under SG-15 / no-unaudited-import guard — recorded, not certified by Genesis): the dyadic $p=6$ NF identifies $\lambda=e^{iF_f/2}$, $F_f=2\pi/3$ `[ALG, exact]`, with an SU(2) half/full energy ratio $E_{\rm full}/E_{\rm half}=4$. The proposal that this supplies a legal $\times4$ cascade rescue is `[CAND]` with one exact leg ($\lambda=e^{iF_f/2}$) and one open leg (the $h$-source bridge). **Genesis does not certify the $\times4$ rescue**; SG-15 forbids importing the dyadic factor as a certified gate factor.

`[RESULT]` `[scope: conditional calibration]` **×2 cross-stream amplitude verdict (AUDIT-1-DIMENSIONAL, corrected GCL-08).** The Genesis cascade test is linear in the admitted source amplitude \(\|H\|_B\). If **both** of the following are supplied: (1) the assembler/source bridge identifying the representation-theory source variable with the certified \(\|H\|_B\) pipeline, and (2) a constitutive relation in which the SU(2) energy ratio maps to source amplitude by a square root (\(E\propto\) amplitude²), then \(E_{\rm full}/E_{\rm half}=4\) corresponds to an amplitude factor \(2\), not \(4\). Norm homogeneity alone does not establish premise (2). Therefore the numerical “OPEN-M is \(\sim2\times\) short” reading remains **conditional on both bridges**; the \(\times4\) energy factor is not directly admissible in an amplitude-linear inequality.

`[RESULT]` `[from: ALG]` **Object-typed norm refinement.** For the symmetric covariant block \(M=gI:V\to V^*\), the \(B\)-generalized norm is \(2|g|\). Raising correctly gives \(A=B^{-1}M=gB^{-1}\) with the same induced \(B\)-norm \(2|g|\). An endomorphism whose numerical array is \(gI\) is a different object (corresponding covariant block \(gB\)) and has induced norm \(|g|\). The same array may not be reused across index placement without changing the object. The final OPEN-M calibration remains conditional on GCL-04's 9C premise where that family is invoked.

Cross-reference: OPEN 5/2B-a and the adopted-scope T-6s/T-6t candidate notes constrain the same interface without selecting a physical source. T-6s supplies a conditional coherent-family norm identity; T-6t supplies mode-label/sign information only. Neither establishes apex source independence or supplies the missing energy→amplitude constitutive bridge.

`[CAND]` `[source: TRIAD-ALG-T6S-COHERENT-CONJUGATE-FAMILY]` **In-plane coherent-source identity (Triadic v1.6 scope).** For the declared coherent source family with real \(g_2\),
\[
H_{\rm total}=(1-g_2)BJ_Q,\qquad
\|H_{\rm total}\|_B=|1-g_2|,
\]
and
\[
\|H_{\rm total}\|_B\le1\iff0\le g_2\le2.
\]
The older unconditional “any coherent source cannot raise the norm” reading is withdrawn. Neither physical selection of \(0\le g_2\le2\) nor a source-lowering identification follows from the identity. This remains a candidate interface statement, not an OPEN-M source realization.

`[CAND]` `[source: TRIAD-ALG-T6T-JACOBI-MODE-SIGNS]` **Mode-sign count, not physical source-direction independence.** Adopted Triadic v1.6 retains independently signable Jacobi mode labels within the stated node-mediated incidence reduction. It does **not** establish that the \(d\)-mode is a separate physical transverse/out-of-plane source carrier. Any physical apex-source realization requires an explicit enlarged carrier, embedding, metric and source map (CN-01 / GCL-05).

---

**OPEN 1C — Triad chiral admissibility surface** [RID: GEN-OPEN-CHIRAL-ADMISS]

Status: **CLOSED `[THM]` (v2.2)**  
Question (resolved): Compute $\Delta Q_c^{(4)} = 2c^\top B G_{3,c}(s,c,0)$ for channels $c^3$, $cs^2$, $sc^2$.  
Result:
$$\Delta Q_c^{(4)}\big|_{\rm standalone} = \tfrac{1}{3}Q_c^2 + \tfrac{1}{4}(I_{sc}+\omega_{sc})^2 + \tfrac{5}{16}\omega_{sc}^2 \geq 0.$$
Channel ledger: $[c^3]=+\tfrac{1}{3}Q_c^2$; $[c,s^2]=+\tfrac{1}{4}Q_sQ_c+\tfrac{1}{2}I_{sc}\omega_{sc}+\tfrac{3}{8}\omega_{sc}^2$; $[s,c^2]=0$; $[s^3]=0$.  
Verdict: **No quartic safe surface** — $Q_{c,\rm safe}(s^+) = C_{\rm triad}Q_s^3$ is `[FAIL]`. The "if yes" branch (constant perturbative $\kappa_{\rm phys}$ from capacity matching) did **not** occur; OPEN K does not collapse this way. Certification: `genesis_k4_route_census.py` (PASS) + independent two-route SymPy re-derivation. Definition retained: $s^+$ is the post-fracture/post-birth longitudinal state after the chosen $\Phi_{2\to3}$ policy.

---

**OPEN 1T — Triadic v1.6 phase/interface import protocol** [RID: GEN-OPEN-TRIAD-PHASE-IMPORT]

Status: **CLOSED / current import protocol (v2.8.5 draft reconciliation)** | Source: adopted `RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6`

Genesis may import only adopted, currently scoped Triadic claims. The historical \(x_*\), \(0^\circ\)–\(5.5^\circ\) safety wedge, \(K=1\) no-safe-basin classifications, phase-steering synthesis, T-6m wedge comparison, and T-6p route-obstruction exports are **withdrawn from current Genesis use** under CN-05; they are not rescaled or replaced by a new global torsion verdict.

Retained at their own scopes: the exact T-6m reference quarter-turn / producer-frame algebra; T-6s coherent-source identity with its required \(0\le g_2\le2\) coefficient interval; T-6t mode-label/sign result (not a physical transverse embedding); T-6u primitive seed diagnostics; and CN-03's positive GSPLIT consistency at exactly \(I_{sc}=0\). Corrected finite-\(u/r\) orientation flow, basin structure and global phase steering remain Triadic OPEN work (T-6r/T-6q) and are not imported here.

---

**OPEN 2 — Primitive tetrahedral $Q_d$ drift: interpretive tasks** [RID: GEN-OPEN-TETH-INTERP]

Status: ACTIVE | Polynomial $\mathcal{P}_4$ is `[THM]`; projection tasks remain  
Active sub-items:
- Choose invariant gauge modulo Plücker identities: `[OPEN]`
- Derive physical phase-moment distribution: `[OPEN]` (overlaps OPEN 1)
- Test whether old scalar law is a nonuniform/projection closure: `[OPEN]`
- Compute $\Delta Q_s^{(4)}$, $\Delta Q_c^{(4)}$ as needed: `[ALG verified]` / `[THM]` — done v2.2 (OPEN 1C closed; $\Delta Q_s^{(4)}$ shadow certified, §6.5)

---

**OPEN 5 / 2B — face-phase / healing-core insertion** [RID: GEN-OPEN-WPHASE]

Status: ACTIVE — corrected live formulation is the OPEN 5/2B block above.  
Question: determine the physical UV interpretation of the typed face-phase/amplitude data after GCL-01/GCL-06; the historical free \(F_W(\eta_*)\) parametrization is not a live target.

---

**OPEN 9 — General $p$-resonance theory** [RID: GEN-OPEN-P-RESONANCE]

Status: PARTIAL — see `RTG_DYADIC_OSCILLATOR_DSN_v6.4.10` for the primary ledger  

Closed sub-items (imported from Dyadic):
- $p=5,6,7$ finite one-step ledgers: `[ALG]` ✓ `[RID: DYAD-ALG-P567-LEDGER]`
- $p=5$ primary lattice harmonic $(0,4)$ cancellation: `[ALG]` ✓ `[RID: DYAD-ALG-GLATTICE5]`
- Exact $G_{04}(10)=0$ reinterpretation: `[ALG]` ✓
- Cascade boundary $p=12, q=4,(0,3)$: $-13+15\sqrt{3}/2 \neq 0$: `[ALG]` ✓

Active sub-items:
- Universal $\nu_5^{(p)}$ generator: `[OPEN]`
- Universal tangent-to-identity gauge / retained-channel classification: `[OPEN]`
- Higher lattice harmonics $(0,2p-1)$ and beyond: `[OPEN]`
- Cancellation rules $Z_{p,d}(D)$: `[OPEN]`

---

**OPEN K — $\Phi_{2\to3}$ physical birth coefficient** [RID: GEN-OPEN-KAPPA-PHYS]

Status: ACTIVE  
Question: What is the physical $\kappa$ selecting a unique birth?

Reference policies: $\kappa_{\rm shear} = -2\sqrt{3}/3$ `[from: RTG_TRIADIC_BIRTH_LIFT_DSN_v1.3]`; $\kappa_{\rm recoil} = -1/2$.  
Current state: perturbative bridge gives the one-dimensional birth direction `[THM]`; physical $\kappa$ requires post-birth admissibility rule.  
Connection (resolved v2.2): OPEN 1C is closed — the universal chiral pump means there is **no $Q_s^3$ safe surface**, so capacity matching does **not** select $\kappa_{\rm phys}$. Selection is routed to the NF frame (NF/primitive sign split), higher order, or network/UV policy. Still depends on OPEN 1T for the legal safety-window import.

---

**OPEN M — Quaternionic metric lift** [RID: GEN-OPEN-UV-LIFT]

Status: ACTIVE | **BLOCKS** OPEN 0  
Question: Derive UV blocks $H(x)$ and $M_{\rm spin2}(x)$ from a minimal non-block-diagonal quaternionic UV generator.

Active sub-items:
- Derive $H(x)$: zeroth-order source block $\Pi_\parallel \to \Pi_\perp$: `[OPEN]`
- Derive $M_{\rm spin2}(x)$: first-order spin-2 restoring block: `[OPEN]`
- Single-jet construction: `[HYP]` — if proved, $\alpha_f = c_0|w|$; until then, $\alpha_f$ and $w$ are distinct UV data.
- **HYP-B (cascade mechanism).** The v2.2 audit (artifact-certified) establishes that, after HYP-A (plateau neighbor, zero injection) and HYP-C (heterochronous uniform-phase spread, net negative) are ruled out `[FAIL]`, an OPEN M source term $\sigma_f$ of pure-seeding form is the sole viable cascade mechanism. The threshold $|\alpha_f| \geq 0.012$ is `[HYP]` (model-dependent on the reduced birth-race wrapper); deriving $\alpha_f$ from the UV jet and confirming the bound is OPEN-GEN-II-7B.

---

**OPEN-GEN-II-7B — UV-jet amplitude and cascade threshold** [RID: GEN-OPEN-UVJET-ALPHAF]

Status: ACTIVE | Depends on OPEN M and OPEN-GEN-II-9  
Question: Derive $\alpha_f$ from the minimal non-block-diagonal UV jet and determine whether the cascade threshold $|\alpha_f| \ge 0.012$ is necessary, sufficient, or model/convention scoped.

Current state (v2.8.5 correction): the artifact-certified reduced model has a fixed-point ceiling $Q_d^*\approx1.13\times10^{-2}$ (≈23% of threshold). The control-loss value is about $5.6\times10^{-3}$ over the lower initial-state window and declines to $2.3\times10^{-3}$ at $Q_{s,0}=5\times10^{-2}$; it is not universal over the full wider window. A pure-seeding source of the form $\varepsilon = \sigma\sqrt{Q_dQ_s}$ with $\sigma_{\rm min} \approx 0.048$ closes the reduced-model gap. Translating to the OPEN M convention $\sigma_f = |\alpha_f|(\Delta\mathcal{E}_c^{(f)})^p\sqrt{Q_c^{(f)}}$ gives the estimate $|\alpha_f| \gtrsim 0.012$. This is `[HYP]` `[scope: reduced wrapper estimate]`: the birth-race wrapper is a reduced numerical model, not full symbolic UV dynamics. Deriving $\alpha_f$ from UV jet data and verifying/correcting/rejecting the bound against full UV dynamics (with the scalar-M / 9C normalization) remains open.

Active sub-items:
- Derive $\alpha_f$ from UV jet data rather than assigning it as an independent phenomenological source: `[OPEN]`
- Verify, correct, or reject the threshold $|\alpha_f|\ge0.012$ against full UV dynamics: `[OPEN]`
- State the normalization, source-amplitude convention, and relation to $\sigma_f = |\alpha_f|(\Delta\mathcal{E}_c^{(f)})^p\sqrt{Q_c^{(f)}}$: `[OPEN]`

**Constraint scoping (corrected scope).** `[RESULT]` `[scope: certified scalar-M frame + **9C raw-array modelling HYP** + single-jet HYP]` (artifact `open_m_constraint_scope.py`): **if** the physical $M_{\rm spin2}$ is required to satisfy the 9C raw-array $B$-self-adjointness premise, the certified frame reduces that branch of the OPEN M blocker to two UV scalars, $\|H\|$ and $g$. With $\alpha_f = c_0|w|$, $c_0=\|H\|/\|M\|_{\rm op}$:
- $M_{\rm spin2}$ trace-free diagonal part is fixed to $-2m\,\Im w$ (9C);
- $M_{\rm spin2}$ off-diagonal is fixed by the documented spin-2 sector (§6.7) *once that sector is instantiated with an explicit expression* (§6.7 currently names the sector but gives no closed off-diagonal formula);
- the soft-mode physics (9A/9B/9B-tau) is $g$-covariant — the isotropic spin-2 mass $g=\tfrac12\mathrm{tr}\,M_{\rm spin2}$ only shifts the soft-pole location $\tau_{\rm soft}=g+\kappa$;
- $\|M\|_{\rm op}$ is then pinned up to $g$; $B$-eigenvalues $\lambda_\pm=\tfrac{2D+4g}{3}\pm\tfrac23\sqrt{4D^2+4Dg+g^2+3m^2\Im w^2}$, and $\|M\|_{\rm op}\to2g$ in the large-$g$ regime.

Under the stated 9C modelling premise, $\|H\|$ and $g$ are the remaining inputs in this reduced constraint-scoping branch; without that premise the physical $M_{\rm spin2}$ family is not reduced this way. In the large-$g$ regime the cascade test collapses to a single dimensionless inequality
$$\left(\frac{\|H\|}{g}\right)|w| \gtrsim 0.024 \qquad \text{`[large-$g$ asymptotic]` `[inherits reduced-wrapper HYP]`,}$$
which uses $\|M\|_{\rm op}\to2g$ and the reduced-wrapper estimate $|\alpha_f|\gtrsim0.012$. The constant $0.024$ is **not** a first-principles OPEN M threshold — it is a clean target inequality for what OPEN M must eventually check. Deriving $\|H\|$ and $g$ requires the RTG UV completion (the jet structure) and is the irreducible OPEN M content, not attempted here.

**CHECK-GEN-II-7B-NORM — RESOLVED → `[DEF/CONVENTION]` (v2.7.6).** The $\|M\|_{\rm op}$ in this constraint scoping is the **B-native operator norm**:
$$\|M\|_B=\max|\lambda|,\qquad \det(M_{\rm spin2}-\lambda B)=0,$$
identically the spectrum of the raised endomorphism $B^{-1}M_{\rm spin2}$ — index-consistent with the 9B $(0,2)$-Hessian calculus. For the 9C admissible family the exact $B$-spectrum is
$$\lambda_\pm=\frac{2D+4g}{3}\pm\frac{2}{3}\sqrt{4D^2+4Dg+g^2+3m^2\Im(w)^2},$$
with large-$g$ limit $\{2g/3,\,2g\}$, hence $\|M\|_B\to2g$. Sanity anchor: even scalar $gI$ has $\|gI\|_B=2g$, since $B$'s eigenvalues are $\{3/2,1/2\}$. The local Euclidean block norm $\|M\|_E=g+\sqrt{D^2+m^2\Im(w)^2}\to g$ is a *different, correctly computed object* and must not share the symbol. **Naming guard:** $\|\cdot\|_B$ = B-native generalized-eigenvalue norm; $\|\cdot\|_E$ = local Euclidean block norm. The cascade inequality uses $\|\cdot\|_B$; the target $(\|H\|_B/g)|w|\gtrsim0.024$ stands, and the transient local-Euclidean alternative ($0.012$) is withdrawn as a live reading — it was an artifact of evaluating a B-native inequality with a Euclidean norm. The large-$g$ value is asymptotic; finite-$g$ evaluations must use the exact $\lambda_\pm$ above (note the $4Dg$ cross-term). `[RID: GEN-DEF-NORM-BNATIVE]`

---

**[CAND/diagnostic import from Triadic T-6u]** [RID: GEN-CAND-APEX-T6U] [source: TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC]

The primitive census contains distinct apex channels that must not be conflated. For the parent-seeding channel
\[
V_s:=G_{3,d}^{[s^3]}(s,0,0),\qquad Q(V_s)=\frac7{1024}Q_s^3,
\]
so relative to the reference in-plane seed \(Q_c^{\rm seed}=\frac43Q_s^3\),
\[
R_{\rm apex}^{\rm cert}
=\sqrt{\frac{Q(V_s)}{Q_c^{\rm seed}}}
=\frac{\sqrt{21}}{64}\approx0.0716.
\]
This is a **primitive seeded-state amplitude diagnostic**, not an HINDEX/OPEN-M source-norm ratio and not a bound on an independent UV source. Triadic v1.6 separately types
\[
D_{\rm birth}^{[s^3]}=\frac7{512}Q_s^3=2Q(V_s)
\]
as a seeded-vector **increment-channel diagnostic**, not an alternative value of the initial seed norm or a demonstrated complete next-block increment. The pure-apex self-channel \([d^3]\), parent-seed channel \([s^3]\), and any OPEN-M/UV apex source are distinct objects.

`[RETRACTED]` `[RID preserved: GEN-OPEN-APEX-SLOT]` **Former apex–UV slot identity.** The v2.8.4 `[RESULT]` identifying the Jacobi \(d\)-mode with a physical transverse/out-of-plane UV slot is withdrawn. In Genesis, \(s,c,d\) are each vectors in the same two-dimensional \(B\)-carrier; orthogonality of Jacobi coefficient rows is in node-label space and does not establish an additional physical state-carrier direction. The distinct \(d\)-mode label and its primitive seed calculations remain valid. A physical transverse/UV embedding requires an explicit enlarged carrier, metric, embedding and source map and remains `[OPEN]`.

The 9C off-diagonal \(D\) remains a differently typed operator coefficient; no geometric “in-plane versus apex” theorem is inferred from that type distinction. OPEN M remains unresolved, and no primitive seed ratio localizes the missing UV source to a proved physical slot.
---

**OPEN-GEN-II-HINDEX — Source-block index placement for $H$** [RID: GEN-OPEN-HINDEX]

Status: **CLOSED for index type (v2.7.7); physical lowering bridge conditional** | by 9B-style index-placement trace  
Resolution: under the §6.8 scalar-M face-gauge source equation, the zeroth-order source block $H$ is **covector-valued**: $S=Hx\in\Pi_\perp^*$. The further identification $S_f=Bc_f$ is an admitted lowering choice whose physical uniqueness is not supplied by tensor type/covariance alone (GCL-03). The physical output amplitude therefore contracts with the **inverse** metric, $|S|^2_{B^{-1}}=S^\top B^{-1}S$, giving $|Hx|^2_{B^{-1}}=x^\top H^\top B^{-1}Hx$. Relative to the input amplitude $|x|^2_B=x^\top Bx$, the generalized eigenproblem is $H^\top B^{-1}H\,v=\lambda Bv$, so the $B$-native source-block norm entering $c_0$ is
$$\|H\|_B^2=\lambda_{\max}\!\left(B^{-1}H^\top B^{-1}H\right).$$
Checksum: $H=\sigma B$ (pure metric lowering) gives $B^{-1}(\sigma B)B^{-1}(\sigma B)=\sigma^2 I$ — a **double** eigenvalue $\sigma^2$, confirming norm $|\sigma|$ with no hidden normalization fork.

| Claim | Status |
|---|---|
| $H$ is covector-valued under the §6.8 / 9B index calculus | `[THM]` `[scope: scalar-M / face-gauge source equation]` |
| Numerator norm is $\lambda_{\max}(B^{-1}H^\top B^{-1}H)^{1/2}$ | `[DEF/ALG]` |
| $H=\sigma B\Rightarrow\|H\|_B=\lvert\sigma\rvert$ (double root $\sigma^2$) | `[CERT checksum]` |
| Euclidean $\|H\|$ | `[diagnostic only]` |
| Vector-valued norm $B^{-1}H^\top BH$ | `[FAIL as HINDEX norm]` unless OPEN M changes the source index — at $H=\sigma B$ it gives eigenvalues $\{\tfrac94\sigma^2,\tfrac14\sigma^2\}$, exhibiting the concrete hidden fork (spurious $3/2$, $1/2$ factors) |

`[CERT]` **Norm-convention unification (v2.7.7 cross-check).** On the 9C admissible family $M_{\rm spin2}(g,D)$, the HINDEX singular-value spectrum equals the squared $B$-native eigenvalue spectrum: $\mathrm{spec}(B^{-1}M^\top B^{-1}M)=\{\lambda^2:\lambda\in\mathrm{spec}(B^{-1}M)\}$ (verified symbolically; $gI$ sub-case: both give $\{2g,\tfrac{2g}{3}\}$). So $\|H\|_B$ (HINDEX) and $\|M\|_B$ (CHECK-GEN-II-7B-NORM) are **one** $B$-native convention — $c_0=\|H\|_B/\|M\|_B$ is matched-raising by construction, satisfying the convention-invariance requirement that motivated this item.

Provenance: trace and checksum executed by PI (`independent_hindex_trace.py`); independently re-verified including the `[FAIL]`-alternative eigenvalues and the norm-unification cross-check (`hindex_verification.py`). The norm-convention guard is lifted for objects explicitly defined with the stated lowering; numerical $\|H\|_B$ values may enter the $0.024$ target **provided** the source object uses this norm and the physical vector→covector bridge is separately declared. The remaining OPEN M deliverable is exactly the v2.7.5/v2.7.6 statement: derive the actual UV values of $\|H\|_B$ and $g$.

---

**OPEN-GEN-II-ARCHIVE — Genesis II correction/rejection recovery** [RID: GEN-OPEN-GENII-ARCHIVE]

Status: **RESOLVED (v2.2)** | Archival/provenance patch complete  
Resolution: The May 22 Genesis II results are now artifact-attached (`genesis_k4_route_census.py` all PASS; `genesis_birth_race_model.py`) and migrated into the live ledger:
- OPEN 1C closed `[THM]` (§1, §2, §6.5).
- Vector apex seeding $G_{3,d}(s,c,0)$, $Q_{d,1}^{[s^3]}=\tfrac{7}{1024}Q_s^3$, $\Delta Q_s^{(4)}$ shadow: `[ALG verified]` (§6.5).
- Corrected $J_Q$, birth-symmetry sign, phase-drift law: `[ALG]` (§6.6).
- HYP-A, HYP-C, incoherent seeding, smooth-$\chi$: established `[FAIL]` (Appendix B).
- Saturation ceiling $Q_d^*\approx1.13\times10^{-2}$ and control value $Q_d(n_{\rm ctrl})\approx5.6\times10^{-3}$: `[RESULT]` `[scope: reduced birth-race model]` (§6.6).
- Cascade threshold $|\alpha_f|\ge0.012$: routed to OPEN-GEN-II-7B as `[HYP]`.

Residual recovery item: none. SG-14 no longer gates these items; the model-dependent saturation numerics and $\alpha_f$ threshold retain explicit scope tags pending full UV-dynamics confirmation.

---

**OPEN-GEN-II-9 — Exact constrained resolvent and soft-mode susceptibility** [RID: GEN-OPEN-RESOLVENT-SOFTMODE]

Status: ACTIVE | Absorbed from `DSN_GENESIS_II_UV_PATCH_v0.1`  
Question: Does the soft mode structurally dominate the susceptibility of the constrained lift system at the saddle-node transition?

`[COR]` Prior premature `[THM]` claims downgraded (see Appendix B):
- Soft-mode resolvent singularity governs critical lift: `[THM]` → `[ALG structure]`
- Resonance-assisted saddle-node is exact: `[THM]` → `[HYP]` → `[THM]` target
- Projection nontriviality resolved: `[RESULT]` → `[OPEN]`

Closed sub-item:
- Exact resolvent under scalar-M ansatz $M=gI$: `[ALG]` ✓ `[scope: scalar-M ansatz]`  
  $((\tau-g)I - \Delta M_f)^{-1} = ((\tau-g)I + \Delta M_f)/((\tau-g)^2 - \kappa^2)$

Closed under scalar-M (OPEN-GEN-II-9A, v2.3 — see §6.9, artifacts `resolvent_soft_mode.py`, `chi_susceptibility.py`):
1. Scalar-M eigendecomposition $\lambda_\pm=(\tau-g)\mp\kappa$, $\kappa=m|w|$: `[THM]` `[scope: scalar-M ansatz]` ✓
2. Soft-mode identification (branch $\tau-g-\kappa\to0$, eigenvector $v_+=(\mu_1,\mu_2-|w|)$): `[ALG]` ✓
3. Projection nontriviality — $R_{\rm soft}\neq0$ generically at $H_0=J_Qs_*$, both pairings: `[ALG]` ✓ (residue sign convention-dependent — Euclidean PSD, $B$ indefinite)
4. Scalar susceptibility $\chi_E,\chi_B$ closed-form with soft-pole numerators: `[ALG]` ✓ `[convention-dependent numerator]`

Active sub-items (in order):
1b. General eigendecomposition of $L_{\mathbb{C}} = \tau I - \Delta M_f - M_{\rm spin2}$ once OPEN M supplies $M_{\rm spin2}$: `[OPEN]`
5. Saddle-node nucleation condition on $(w, \alpha_f, \tau, \sigma_f)$: `[ALG structure]` — soft residue is PSD **conditional on the declared $B$-lowering $S_f=Bc_f$**; covector type is closed but the physical lowering bridge remains OPEN (9B PARTIAL). Exact value still depends on OPEN M $M_{\rm spin2}$; not yet `[THM]`.

Dependencies:
- $\Delta M_f(w)$ — available `[ALG]` from §6.8
- $M_{\rm spin2}$ — `[OPEN]` under OPEN M
- Source pairing — PARTIAL after GCL-03: covector type is closed; $S_f=Bc_f$ is a declared lowering bridge, not uniquely forced by tensor type/covariance. Conditional on that lowering, the residue is PSD. $\tau$-coupling algebra is exact for the branch $K=\tau I-\Delta M_f$, while physical sign/energy-branch selection is reopened by GCL-02
- $M_{\rm spin2}$ anisotropy — `[OPEN-GEN-II-9C]`; diagonal splitting $-2m\,\Im w$ gives $B$-self-adjointness (generalization beyond scalar-M)

---

**OPEN-GEN-II-9B — Source index type and lowering bridge** [RID: GEN-OPEN-SOURCE-PAIRING]

Status: **PARTIAL** — covector index type closed; physical vector→covector lowering map remains OPEN after GCL-03.

`[ALG]` The §6.8 stationarity equation is a covector equation: the Hessian/secular block maps the state vector to a covector and therefore \(S_f\) is covector-valued. This index-type conclusion is retained.

`[COR]` The stronger v2.6 statement that covariance **forces** the specific lowering \(S_f=Bc_f\) is withdrawn. Tensor type/covariance alone do not uniquely select \(B\); choosing \(B\) as the physical lowering form requires an additional geometric/constitutive/event bridge.

`[RESULT]` `[from: ALG]` **Conditional residue statement.** Given the declared lowering \(S_f=Bc_f\), the soft residue
\[
c_f^\top B\Pi_+Bc_f=|\Pi_+Bc_f|^2\ge0
\]
is PSD and generically nonzero. This remains an exact conditional algebraic result; it is not a uniqueness theorem for the lowering map.

**9B-tau sign reconciliation (GCL-02).** The v2.8.4 §6.8 display used \((\Delta M_f+\tau I)d_\perp+S_f=0\), while the documented numerator \(+2a\tau\) reconstructs exactly from
\[
K_-=\tau I-\Delta M_f.
\]
For \(K_+=\tau I+\Delta M_f\), the corresponding cross term has the opposite sign. The determinant factor alone cannot select the sign because \(\det(\tau I+\Delta)=\det(\tau I-\Delta)\). Therefore:

- `[ALG]` retained: the full printed secular numerator/denominator reconstructs exactly **for** \(K_-\);
- `[OPEN]`: the physical operator sign, energy branch and minimum selection must be re-derived from one typed energy/constraint equation;
- the earlier sentence that the documented factor “fixes the physical soft branch” is withdrawn.

The \(\tau I\) versus \(\tau B\) multiplier-type distinction remains separate from the \(\pm\Delta M_f\) sign question.
---

**OPEN-GEN-II-9C — conditional raw-array $B$-self-adjoint family** [RID: GEN-OPEN-MSPIN2-ANISO]

Status: ACTIVE | exact solution family to a declared raw-array modelling premise; physical-block selection remains OPEN M

`[ALG]` `[CERT ×2]` **Conditional criterion (re-certified v2.7.6).** If one imposes the additional raw-array modelling premise $K^\top B=BK$, then for symmetric $M_{\rm spin2}$ it holds **iff** $(M_{\rm spin2})_{11}-(M_{\rm spin2})_{22}=-2m\,\Im w$. 9B's $(0,2)$ Hessian typing does **not** imply this premise; for any symmetric covariant Hessian $K$, the raised endomorphism $B^{-1}K$ is already $B$-self-adjoint in the correctly typed sense. Scalar $M_{\rm spin2}=gI$ fails the additional raw-array condition when $\Im w\neq0$. Independently reconstructed a second time from documented §6.8 inputs only (artifact `mspin2_admissible_family.py`); the $\tau B$-exclusion determinant cross-check independently confirms $\mu_1=\Re w$ and the $B$ identification.

`[ALG]` **Admissible family (v2.7.6).** The complete solution space is the two-parameter family
$$M_{\rm spin2}(g,D) = gI - m\,\Im(w)\,\sigma_3 + D\,\sigma_1,$$
i.e. forced diagonal $(g-m\,\Im w,\ g+m\,\Im w)$, free off-diagonal $D$. Euclidean eigenvalues $g\pm\sqrt{D^2+m^2\Im(w)^2}$; $B$-spectrum per CHECK-GEN-II-7B-NORM. The resulting secular operator collapses to
$$K = gI + (D - m\,\Re w)\,P,\qquad P=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix},$$
with eigenvectors $(1,1)$, $(1,-1)$ shared with $B$, and soft mode at $g\to|D-m\,\Re w|$. If the physical block is admissible, the OPEN-GEN-II-9 general eigendecomposition (item 1b) is closed-form immediate.

`[INTERP]` **Eigenframe reading.** $B$-self-adjointness is exactly the condition that the spin-2 anisotropy cancels the $\sigma_3$ ($\Im w$) component of the face-lift obstruction $\Delta M_f$, locking $K$ into the commutant algebra $\mathrm{span}\{I,P\}$ of $B$. The $\Re w$ component is not cancellable by the diagonal; it merges additively with $D$ in the off-diagonal.

`[RESULT]` `[from: ALG]` `[scope: conditional raw-array premise]` **OPEN M target statement.** Any OPEN M construction that **chooses to impose the raw-array condition** $K^\top B=BK$ must produce diagonal split $-2m\,\Im w$ exactly; its residual content is the two scalars $(g,D)$, with $D$ supplied by the instantiated §6.7 spin-2 sector and $g$ entering the OPEN-GEN-II-7B cascade inequality. If the construction yields a different split, $B$-self-adjointness fails; this is a consistent outcome (the 9B physical residue is PSD-certified without it) but forfeits the structural simplification. Neither branch is presupposed.

Significance (corrected scope): under the additional raw-array premise, $\Pi_\pm$ become $B$-orthogonal and the one-$B$ form $c_f^\top B\Pi_+c_f$ coincides with a clean $B$-quadratic residue — removing the diagnostic/physical distinction of 9B. This is a structural simplification, not a prerequisite for a definite-sign saddle-node. The off-diagonal $(M_{\rm spin2})_{12}=D$ is fixed by the documented spin-2 sector (§6.7) once that sector is instantiated with an explicit expression. `[HYP]` pending OPEN M derivation of $M_{\rm spin2}(x)$. **No claim is made that the physical block lies in the admissible family.**

---

**OPEN M-foam — Network phase compatibility** [RID: GEN-OPEN-FOAM-NETWORK]

Status: ACTIVE  
Question: Do apex-correlated sourced-junction networks admit coherent global phase locking, chirality-neutral averaging, nontrivial boundary charges, or a foam curvature/torsion invariant?

---

**OPEN 0 — Emergent coupling constant** [RID: GEN-OPEN-KAPPA-RTG]

Status: ACTIVE | **BLOCKS** continuum gravity definition; **BLOCKED BY** OPEN M  
Question: Define $\kappa_{\rm RTG} = \mathcal{G}_e / J_e$ from the first nondegenerate hinge-star cluster after smooth metric branch and RTG-to-Regge map are constructed.

---

**OPEN 0-Regge — Minimal curvature cluster** [RID: GEN-OPEN-REGGE]

Status: ACTIVE | **BLOCKS** OPEN 0  
Question: Construct the minimal holonomy-consistent hinge-star cluster $\mathcal{C}_{\rm ref}$ with closed fan, face-adapted gluing, nonzero deficit angle, and explicit RTG-to-edge-length map.

---

## §3. Scope Guards {#sec-3-scope-guards}

**[SG-1]** Full triad quadratic cancellation: `[FAIL]`. Only pure chiral quadratic cancellation is proved. With longitudinal background $s \neq 0$, mixed quadratic terms survive.  
Violation: Asserting quadratic cancellation in the full triadic system.

**[SG-2]** The pure-$d$ six-step leading sink coefficient is $-1$ (from $-Q_d^2$), not $-\frac{1}{2}$. The $-\frac{1}{2}Q_d^2$ value is a one-step / unintegrated artifact.  
Violation: Using $-\frac{1}{2}$ as the primitive six-step pure-$d$ coefficient.

**[SG-3]** Uniform independent phase averaging cannot produce cascade ($\langle\mathcal{P}_4\rangle_{\rm ind.phase} \leq 0$ always). Cascade requires nonuniform, birth-correlated, plateau-attractor, or network-gluing phase moments.  
Violation: Claiming cascade from the uniform independent phase average.

**[SG-4]** Raw one-step antisymmetric cubic coefficients ($\nu_{3,\rm raw}^{\rm anti}$) are distinct from Birkhoff normal-form coefficients ($\nu_{3;6}^{\rm NF}$). The difference arises from the near-identity Birkhoff coordinate change.  
Violation: Equating raw and normalized cubic coefficients.

**[SG-5]** The dyad alone does not fix the Genesis birth coefficient $\kappa$, UV source $\alpha_f$, or stiffness $w$. These are distinct objects requiring separate derivations.  
Violation: Deriving $\kappa_{\rm phys}$, $\alpha_f$, or $w$ from dyadic coefficients alone.

**[SG-6]** $\alpha_f = c_0|w|$ holds only if the single-jet construction is explicitly derived (OPEN M). Until then, $\alpha_f$ and $w$ are independent UV data.  
Violation: Using $\alpha_f = c_0|w|$ without citing the single-jet proof.

**[SG-7]** $T_{\mathbb{H}} = T \oplus T$ does not generate a smooth 3D metric branch ($w = 0$ theorem-grade). A non-block-diagonal UV generator is required.  
Violation: Claiming metric emergence from block-diagonal quaternionic extension.

**[SG-8]** Foam chirality neutrality is at most `[HEUR]`; pending network holonomy / compatibility analysis. Force-balance / $120°$ patterns in node-coordinate space are `[FAIL]`.  
Violation: Claiming chirality neutrality as a theorem.

**[SG-9]** Observable phase/projection data depend on normalization and gauge choices. No Genesis claim may identify an observable phase directly with an internal mode phase without a projection bridge.  
Violation: Equating observable and internal mode phases without a named projection bridge.

**[SG-10]** $\kappa_{\rm RTG}$ cannot be defined before the smooth metric branch (OPEN M) and RTG-to-Regge map (OPEN 0-Regge) are established.  
Violation: Asserting a value for $\kappa_{\rm RTG}$ before OPEN M and OPEN 0-Regge are closed.

**[SG-11]** All dyadic and triadic imports carry `[scope: conditional on postulated continuous generator T]` until OPEN-P0 (generator selection) is resolved. Programme-level SG-PROG-1 applies.  
Violation: Treating imported dyadic or triadic coefficients as unconditional.

**[SG-12]** **Triadic v1.6 current-use guard.** The historical $x_*$ threshold, $0^\circ$–$5.5^\circ$ safety wedge, no-safe-basin classifications, phase-steering synthesis and T-6m/T-6p route-obstruction exports are withdrawn from current Genesis use. No rescaled wedge or replacement global torsion verdict is imported.  
Violation: Using any withdrawn phase-chain element as a live premise.

**[SG-12b]** **Reference-quarter-turn / remainder guard.** The homogeneous birth graph with fixed $\kappa<0$ has leading child/parent phase $-\pi/2$. Any full-phase correction depends on the child remainder order and directional preservation (GCL-06); the quarter-turn does not supply a global Triadic flow/basin theorem.  
Violation: Turning the local reference angle into a current safety threshold, basin verdict, or remainder-independent exact full phase.

**[SG-13]** Soft-mode resolvent singularity governs critical lift is `[ALG structure]`, not `[THM]`. Resonance-assisted saddle-node is `[HYP]`, not `[THM]`. Projection nontriviality is `[OPEN]`, not resolved. (Genesis II UV patch corrections.)  
Violation: Restoring the pre-patch `[THM]` or `[RESULT]` status to these UV lift claims.

**[SG-14]** Genesis II conversation-recovered thresholds, saturation numerics, and correction labels became certification claims in v2.2 upon attachment of the computational artifacts (`genesis_k4_route_census.py`, all PASS; `genesis_birth_race_model.py`). Items now carry explicit scope tags: artifact-symbolic results are `[THM]`/`[ALG verified]`; reduced birth-race numerics (saturation ceiling, $|\alpha_f|$ threshold) remain `[RESULT]`/`[HYP]` `[scope: reduced birth-race model]` pending full UV-dynamics confirmation. SG-14 no longer gates the attached items; it continues to gate any future conversation-recovered claim lacking an artifact.
Violation: Using reported $|\alpha_f|\ge0.012$, $Q_d^*\approx1.133\times10^{-2}$, corrected $J_Q$ form, or corrected phase-drift law as certified claims before provenance attachment.

---

## §4. Layer Routing {#sec-4-layer-routing}

$$\text{Primitive} \;\to\; \text{Dyadic module} \;\to\; \text{Triad birth} \;\to\; \text{Tetrahedral drift} \;\to\; \text{UV lift} \;\to\; \text{Regge bridge}$$

| Layer | Object | Canonical tool |
|---|---|---|
| Primitive | $T(\rho,\eta)$, $A$, $B$, $Q$, $W$ | Genesis §6.1–§6.3; Dyadic §6.1 |
| Dyadic module | $\mu_6$, $\tau$, $v_\perp$, antisymmetric channel | Dyadic DSN `[RID: DYAD-THM-C21]` |
| Triad birth | $\kappa$, $Q_c \sim Q_s^3$, chiral protection | Triadic DSN §6.1 |
| Tetrahedral drift | $\mathcal{P}_4(s,c,d)$, phase moments | Genesis §6.5–§6.6 |
| UV lift | $\alpha_f$, $w$, $\Delta M_f$, $\Gamma_{\mathbb{H}}$ | Genesis §6.7–§6.9 |
| Regge bridge | $\mathcal{C}_{\rm ref}$, $\kappa_{\rm RTG}$ | Genesis §6.10; OPEN 0-Regge |

Routing rules:
- No Regge-layer claim without OPEN M + OPEN 0-Regge closure (SG-10).
- No raw ↔ Birkhoff coefficient identification without a named bridge (SG-4).
- Foam chirality neutrality is not a layer result; it is `[HEUR]` (SG-8).
- All dyadic/triadic imports carry generator-T conditionality (SG-11).
- Historical Triadic wedge/phase-steering premises are withdrawn from current use (SG-12); the retained quarter-turn is local and remainder-typed (SG-12b).
- Physical branch selection for the scalar-M resolvent poles is part of OPEN-GEN-II-9 (SG-13).
- Conversation-recovered Genesis II items route first through OPEN-GEN-II-ARCHIVE before entering §6 or Appendix B (SG-14).

<!-- AI_CONTEXT_CORE_END -->

---

## §5. High-Risk Claims Ledger {#sec-5-high-risk}

| Claim | Valid form | Forbidden overclaim | Section |
|---|---|---|---|
| Pure triad quadratic cancellation | `[THM]` — pure chiral only | Full triadic quadratic cancellation | §6.2, SG-1 |
| Pure-$d$ six-step leading coefficient | $-Q_d^2$ (`[THM]`) | $-\frac{1}{2}Q_d^2$ (one-step artifact) | §6.5, SG-2 |
| Uniform phase average | Always sink `[ALG]` | Can produce cascade | §6.6, SG-3 |
| Raw vs. Birkhoff cubic | Distinct objects `[COR]` | Equated without bridge | §6.3, SG-4 |
| Birth residual remainder | $O(|s|^5)$ applies to declared odd/NF residual objects; raw return carries nonzero quartic | Raw $F_6-id$ written as cubic $+O(|s|^5)$ | §6.2–§6.3, GCL-06 |
| Source lowering | Covector source type closed; $S_f=Bc_f$ is a conditional physical lowering bridge | “$B$ lowering uniquely forced by tensor type” | §2/§6.9 OPEN-GEN-II-9B |
| 9C raw-array family | Exact family under additional $K^TB=BK$ modelling premise | Premise implied by 9B typing / universally required | §2/§6.9 OPEN-GEN-II-9C |
| $\kappa_{\rm phys}$, $\alpha_f$, $w$ | Distinct; require separate derivation | Fixed by dyad alone | SG-5/SG-6 |
| Block-diagonal metric | `[THM]` no-go ($w=0$) | $T \oplus T$ generates smooth metric | §6.7, SG-7 |
| Foam chirality neutrality | `[HEUR]` | Theorem-grade | §6.9, SG-8 |
| Soft-mode resolvent mechanism | `[ALG structure]` (Genesis II patch) | `[THM]` | §2, SG-13 |
| Scalar-M resolvent (ansatz) | `[ALG]` `[scope: scalar-M ansatz]` | General $M_{\rm spin2}$ result | §6.9, SG-13 |
| Triadic phase-chain | Historical wedge/$x_*$/no-basin/phase-steering exports withdrawn from current use by adopted v1.6 | Any live Genesis premise or rescaled replacement based on that chain | §2 OPEN 1T, §7, SG-12/SG-12b |
| $\kappa_{\rm RTG}$ | `[OPEN]` — not definable before OPEN M + Regge | Free parameter | §6.10, SG-10 |
| $\alpha_f = c_0|w|$ | `[ALG-conditional]` — requires single-jet proof | Closed result | §6.9, SG-6 |
| $|\alpha_f|\ge0.012$ cascade threshold | `[HYP]` `[scope: reduced birth-race model]`; estimate from $\sigma_{\rm min}\approx0.048$ via $\sigma_f$ convention | Certified lower bound from full UV dynamics | OPEN-GEN-II-7B |
| Isolated-$K_4$ saturation ceiling | `[RESULT]` `[scope: reduced birth-race model]`: $Q_d^*\approx1.13\times10^{-2}$, $Q_d(n_{\rm ctrl})\approx5.6\times10^{-3}$ | Universal saturation theorem (full UV) | §6.6, GEN-ART-SATURATION |
| Genesis II HYP-B mechanism | `[HYP]`: sole viable cascade route after HYP-A/HYP-C `[FAIL]`; requires OPEN M source | Sole viable cascade mechanism globally | OPEN M, OPEN-GEN-II-7B |

---

## §6. Main Scientific Ledger {#sec-6-ledger}

### §6.1 Primitive State and Generator `[THM / mixed]` {#sec-6-1-primitive}

`[DEF]` **Zero-origin condition.** $\mathcal{O}_0 = 0$.

`[DEF]` **First dyad.** $0 \to (A,B)$, $A + B = 0$.

`[INTERP]` Genesis begins with the first internal distinction in a zero-sum relational state.

`[DEF]` **RTG dyad generator.**
$$\boxed{T(\rho,\eta)=\bigl(\rho-\sin\eta,\;\eta+e^\rho-1-\sin\eta\bigr).}$$

`[ALG]` Linearization: $DT(0,0) = A = \begin{pmatrix}1&-1\\1&0\end{pmatrix}$.

`[THM]` $\lambda = e^{\pm i\pi/3}$; $A^3 = -I$; $A^6 = I$.

`[DEF]` `[RID: GEN-DEF-PRIMITIVE-METRIC]` **Quadratic form:** $B = \begin{pmatrix}1&-\frac{1}{2}\\-\frac{1}{2}&1\end{pmatrix}$; $Q(r) = r^\top Br = \rho^2 - \rho\eta + \eta^2$.

`[THM]` `[RID: GEN-THM-PRIMITIVE-METRIC-INVARIANCE]` $A^\top BA = B$.

### §6.2 Dyadic Certified Module `[THM / mixed]` {#sec-6-2-dyadic}

> **[SG-11 applies]** All results in this section are `[scope: conditional on postulated continuous generator T]`.

`[ALG]` **Canonical $p=6$ eigenframe.** Complex coordinate $W = \rho + \omega\eta$, $\omega = e^{2\pi i/3}$; with $W = s + ic$:
$$s = \rho - \tfrac{1}{2}\eta, \quad c = \tfrac{\sqrt{3}}{2}\eta, \quad v_\perp = \bigl(\tfrac{1}{\sqrt{3}},\tfrac{2}{\sqrt{3}}\bigr).$$

`[THM]` **Antisymmetric channel.** $\Delta_c T := T(x+cv) - T(x-cv)$ contains only odd powers of $c$. Quadratic fatigue cancels identically in the local antisymmetric channel.

`[ALG]` **Six-step cubic coefficient from one-step normalized form** ($p=6$): $\mu_6 = 6\bar\lambda\nu_{3;6}^{\rm NF} = -\frac{1}{2} - i\frac{2\sqrt{3}}{3}$. `[from: DYAD-THM-C21]`

`[COR]` Raw antisymmetric extraction gives $\nu_{3,\rm raw}^{\rm anti} = \frac{1}{4} - i\frac{7\sqrt{3}}{108}$; normalized $\nu_{3;6}^{\rm NF} = \frac{1}{8} - i\frac{7\sqrt{3}}{72}$. These are distinct; the Birkhoff coordinate change renormalizes the resonant cubic. Raw channels certify local cancellation; Birkhoff coefficients certify six-step slow healing.

`[ALG]` **Six-step leading healing law, representation-typed (GCL-06).** The odd/normal-form six-step residual has
\[
W_{m+1}=W_m+\mu_6|W_m|^2W_m+O(|W|^5),
\]
while the **raw** six-step return contains an additional nonzero even quartic jet \(F_4\). The leading radial sink \(-Q_m^2\) is shared at quartic amplitude order; higher scalar closure is representation/direction dependent and is not used here as an exact autonomous-state theorem. Any \(\kappa_3\) or higher scalar recurrence coefficient must be imported together with its frame/observable definition.

`[THM]` **Master resonance parity lemma.** For any even scalar $f$: $\sum_{j=0}^5 A^{5-j}e_\eta f(A^jx) = 0$. Exact consequence of $A^3 = -I$.

`[ALG structure]` **OPEN 9 imports.** Low-horizon normalization results (all `[scope: conditional on postulated generator T]`; primary ledger in `RTG_DYADIC_OSCILLATOR_DSN_v6.4.10`):
- $p=6$: $c_\theta^{(6)} = -119\sqrt{3}/648$ `[conv: Lie strict-kernel gauge]`
- $p=5$: $\nu_5^{(5)} = \frac{355-159\sqrt{5}}{48} + i\frac{(1106\sqrt{5}-2473)\sqrt{10+2\sqrt{5}}}{48}$
- $p=7$: $c_{06}^{(7)}$ exact over $\mathbb{Q}(\zeta_7)$ (see Dyadic DSN §6.11)

`[DEF]` **Projection warning.** Each imported dyadic quantity must be tagged as: primitive / normalized / convention-fixed / cycle-averaged / observable-projected. No observable phase may be identified with an internal mode phase without a named projection bridge.

### §6.3 Triad Birth — $\Phi_{2\to3}$ Bridge `[THM / mixed]` {#sec-6-3-triad}

> **[SG-11 applies]**

`[THM]` **Pure chiral protection.** $\frac{1}{2}(T(c) - T(-c)) = Ac + O(c^3)$. All quadratic terms cancel in the pure chiral sector.

`[FAIL]` Full triad quadratic cancellation with longitudinal background.

`[ALG]` **Dyadic residuals at fracture (GCL-06).** At fracture state \(s_*\) with \(Q_s=s_*^\top Bs_*\), distinguish
\[
E_{\rm raw}=F_6(s_*)-s_*,
\qquad
E_{\rm odd},
\qquad
E_{\rm NF}.
\]
All share the cubic jet
\[
E^{[3]}=\mu_6Q_ss_*
=E_{\parallel,*}^{[3]}+E_{\perp,*}^{[3]},
\quad
E_{\parallel,*}^{[3]}=-\tfrac12Q_ss_*,
\quad
E_{\perp,*}^{[3]}=-\tau Q_sJ_Qs_*.
\]
The longitudinal/transverse labels above are **cubic truncations**. \(E_{\rm odd}\) and \(E_{\rm NF}\) support a fifth-order remainder after the cubic term at their declared scopes; \(E_{\rm raw}\) instead carries a nonzero quartic \(F_4\) (real-ray witness \(F_4(t)=-(5+25i\sqrt3)t^4/48\ne0\)). The physical residual realized by the birth event remains OPEN.

`[THM]` **\(\Phi_{2\to3}\) leading one-dimensional birth.**
\[
c_0^{[3]}=\kappa Q_sJ_Qs_*.
\]
If the selected child functional inherits a fifth-order absolute remainder, then \(c_0=c_0^{[3]}+O(|s_*|^5)\) and \(Q_c=\kappa^2Q_s^3+O(Q_s^4)\). If a raw-residual quartic is retained by the child functional, an \(O(|s_*|^4)\) child remainder and \(O(Q_s^{7/2})\) amplitude correction are not excluded. No physical residual/child functional is selected here.

`[ALG structure]` **Shear policy:** $\kappa_{\rm shear} = -2\sqrt{3}/3$; $Q_c^{\rm shear} = \frac{4}{3}Q_s^3$.  
`[ALG structure]` **Recoil policy:** $\kappa_{\rm recoil} = -\frac{1}{2}$; $Q_c^{\rm recoil} = \frac{1}{4}Q_s^3$.  
`[RESULT]` $Q_c^{\rm shear}/Q_c^{\rm recoil} = 16/3 = (\tau/(1/2))^2$.

`[COR]` Physical $\kappa$ requires post-birth admissibility or defect-conservation rule; dyad conventions do not uniquely select it.

`[FAIL]` Constant-$\kappa$ capacity matching to a fixed absolute chiral ceiling $Q_{\rm cubic}$.

`[FAIL]` **(Resolved v2.2)** Constant perturbative $\kappa$ via $Q_{c,\rm safe}(s^+) = C_{\rm triad}Q_s^3 + O(Q_s^4)$. OPEN 1C is closed: $\Delta Q_c^{(4)} \geq 0$ is a universal chiral pump with no quartic safe surface (§6.5), so this branch does not exist. Physical $\kappa$ selection routes to the NF frame (NF/primitive sign split), higher order, or network/UV policy.

`[OPEN]` $\lambda_\parallel$ (longitudinal retention) depends on whether the birth map retains, subtracts, or redistributes the longitudinal residual.

### §6.4 Tetrahedral Jacobi Modes and Chronological Protection `[THM / mixed]` {#sec-6-4-tetrahedral}

`[DEF]` **Jacobi coordinates.** $(s,c,d) \in (\mathbb{R}^2)^3$ with edge-incidence matrix $E$ giving $E^\top E = \operatorname{diag}(2, 8/3, 3)$.

`[THM]` **Rank obstruction.** For the primitive tetrahedral lift built from one orthogonal mode $d$: $\det\Gamma = 0$. A genuine 3D metric does not appear at the primitive tetrahedral stage.

`[HYP]` Cycle-averaging over the 6-step block may generate $\det\bar\Gamma > 0$, but this belongs to the quaternionic lift branch, not primitive tetrahedral. It is not a closed primitive-tetrahedral theorem.

`[THM]` **Tetrahedral chronological protection.** Let $L = \operatorname{diag}(A,A,A)$; $G_2(Z) = \sum_{j=0}^5 L^{5-j}F_2(L^j Z) = 0$. All one-step quadratic forcing cancels over one 6-step block.

`[THM]` Amplitude drift begins at quartic order: $\Delta Q_u = O(\|Z\|^4)$, $u \in \{s,c,d\}$.

`[ALG]` Six-step cubic vector drift $G_3(Z)$ survives the parity filter (odd composition channel). Its magnitude requires explicit hexagonal-orbit evaluation.

### §6.5 Primitive $Q_d$-Quartic Drift `[THM / mixed]` {#sec-6-5-quartic}

> **[SG-2 applies]**

`[FAIL]` Old scalar quartic secular drift law (contains $-\frac{1}{2}Q_d^2$ and scalar capacity terms). Reasons: wrong pure-$d$ coefficient; scalar laws require a phase projection layer.

`[THM]` **Pure-$d$ checksum.** $\Delta Q_d^{(4)}[d^3] = -Q_d^2$.

`[FAIL]` $-\frac{1}{2}Q_d^2$ as one-step / unintegrated artifact.

`[THM]` **Full primitive $Q_d$-quartic drift.**
$$\boxed{
\begin{aligned}
\Delta Q_d^{(4)} ={}& -Q_d^2 \\
&-\tfrac{1}{8}Q_sI_{ds} - \tfrac{3}{32}Q_s\omega_{ds} \\
&-\tfrac{1}{27}Q_cI_{dc} + \tfrac{7}{108}Q_c\omega_{dc} \\
&-\tfrac{5}{12}\omega_{ds}I_{ds} - \tfrac{1}{8}\omega_{ds}^2 \\
&-\tfrac{5}{9}\omega_{dc}I_{dc} - \tfrac{1}{6}\omega_{dc}^2 \\
&+\tfrac{1}{36}Q_sI_{dc} - \tfrac{7}{48}Q_s\omega_{dc} + \tfrac{1}{18}I_{ds}I_{sc} + \tfrac{7}{72}I_{ds}\omega_{sc} \\
&+\tfrac{1}{6}Q_cI_{ds} + \tfrac{3}{8}Q_c\omega_{ds} + \tfrac{1}{3}I_{dc}I_{sc} + \tfrac{1}{4}I_{dc}\omega_{sc}.
\end{aligned}}$$

`[THM]` Vanishing channels: $d^2s$, $d^2c$, $scd$ — by direct incidence cancellation and quadratic route sparsity.

`[ALG]` Torque-channel consistency: $\frac{5/12}{1/8} = \frac{5/9}{1/6} = \frac{10}{3}$; incidence ratio: $\frac{1/6}{1/8} = \frac{4}{3}$.

`[RESULT]` Primitive tetrahedral Genesis is a chiral-torque engine, not a scalar-capacity engine.

`[THM]` **Triad chiral admissibility surface $\Delta Q_c^{(4)}$ (OPEN 1C, closed v2.2).** Standalone triad:
$$\Delta Q_c^{(4)}\big|_{\rm standalone} = \tfrac{1}{3}Q_c^2 + \tfrac{1}{4}(I_{sc}+\omega_{sc})^2 + \tfrac{5}{16}\omega_{sc}^2 \geq 0.$$
K4 shadow at $d=0$:
$$\Delta Q_c^{(4)}\big|_{\rm K4\,shadow} = \tfrac{1}{3}Q_c^2 + \tfrac{1}{4}(I_{sc}+\tfrac{19}{24}\omega_{sc})^2 + \tfrac{359}{2304}\omega_{sc}^2 \geq 0.$$
Channel ledger (standalone): $[c^3]=+\tfrac{1}{3}Q_c^2$; $[c,s^2]=+\tfrac{1}{4}Q_sQ_c+\tfrac{1}{2}I_{sc}\omega_{sc}+\tfrac{3}{8}\omega_{sc}^2$; $[s,c^2]=0$; $[s^3]=0$. Certified by `genesis_k4_route_census.py` (PASS) and independent two-route SymPy re-derivation. `[RID: GEN-THM-DELTA-QC]`

`[RESULT]` **Universal chiral pump.** $\Delta Q_c^{(4)} \geq 0$ everywhere; no quartic safe surface except $c=0$. Consequently $Q_{c,\rm safe}(s^+)=C_{\rm triad}Q_s^3$ is `[FAIL]` and constant-$\kappa_{\rm phys}$ capacity matching is `[FAIL]`.

`[THM]` **NF/primitive sign split.** At pure $c^3$: NF chiral healing gives $-Q_c(Q_s+Q_c)$; primitive incidence gives $+\tfrac{1}{3}Q_c^2$. Opposite signs — NF healing is a coordinate statement, not a primitive-amplitude statement.

`[ALG]` **Vector apex seeding $G_{3,d}(s,c,0)$ (K4 shadow).** All four channels ($s^3$, $s^2c$, $sc^2$, $c^3$) closed-form; certified by `genesis_k4_route_census.py`. Leading apex seed: $Q_{d,1}^{[s^3]} = \tfrac{7}{1024}Q_s^3$. Subdominant: $Q_{d,1}^{[c^3]} = \tfrac{61}{34992}Q_c^3$, suppressed by $\sim Q_s^6$ at canonical birth gauge $Q_c=\kappa^2 Q_s^3$.

`[ALG]` **Shadow longitudinal drift.** $\Delta Q_s^{(4)}\big|_{\rm shadow} = \tfrac{1}{4}Q_s^2 + \tfrac{5}{9}Q_sQ_c - \tfrac{2}{9}I_{sc}^2 - \tfrac{19}{36}I_{sc}\omega_{sc}$; at birth gauge $I_{sc}=0$ this reduces to $\tfrac{1}{4}Q_s^2 + \tfrac{5}{9}Q_sQ_c$. The $Q_s$-freeze heuristic is `[FAIL]` as a theorem; it holds only as a local leading approximation.

### §6.6 Phase Bridge and Cascade Condition `[ALG / mixed]` {#sec-6-6-phase}

`[DEF]` **Phase variables.** $I_{ab} = \sqrt{Q_aQ_b}\cos\theta_{ab}$; $\frac{\sqrt{3}}{2}\omega_{ab} = \sqrt{Q_aQ_b}\sin\theta_{ab}$. Phase convention, not a dynamical theorem.

`[ALG]` **Uniform independent phase average.** $\langle\mathcal{P}_4\rangle_{\rm ind.phase} = -Q_d^2 - \frac{1}{12}Q_dQ_s - \frac{1}{9}Q_dQ_c \leq 0$. Always a sink.

`[RESULT]` Cascade requires nonuniform, birth-correlated, plateau-attractor, or network-gluing phase moments.

`[ALG structure]` **Phase-moment closure.** Macroscopic scalar closure requires specifying:
$$\mathcal{M}_{\rm phase} = \{m^C, m^S, m^{CS}, m^{S2}, m^{CC}_{\rm transfer}, m^{CS}_{\rm transfer}\}.$$
Cascade condition: $\langle\mathcal{P}_4\rangle > 0$.

`[ALG structure]` **Plateau shear bridge.** Six-step coefficient $\mu_6$ supports leading plateau interpolation $\dot Q_k = -Q_k^2$, giving $Q_k(t) = q_k/(1+q_kt)$ and phase memory:
$$\Phi_{ab}(\infty) = \Phi_{ab}(0) - \tfrac{2\sqrt{3}}{3}\log\frac{q_a}{q_b}.$$
Plateau does not randomize phases; maps birth phases to amplitude-ratio memory.

`[OPEN]` Physical plateau phase moments and whether the trajectory crosses $\mathcal{P}_4^{\rm shear}(t) > 0$.

`[ALG]` **Symplectic phase-drift operator (corrected v2.2).** The B-metric quarter-turn is
$$J_Q = \tfrac{1}{\sqrt{3}}\begin{pmatrix}1 & -2 \\ 2 & -1\end{pmatrix}, \qquad a^\top B J_Q b = \tfrac{\sqrt{3}}{2}\omega_{ab}, \qquad J_Q^2 = -I.$$
This $J_Q$ is the birth-direction/phase-drift rotation operator. The Euclidean form $\tfrac{\sqrt{3}}{2}\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}$ is `[FAIL]` for the B-metric (see Appendix B). Phase drift: $\Delta\theta_u = (J_Q u)^\top B G_{3,u}/Q_u$ (note: $u^\top B J_Q G_{3,u}$ has the wrong sign).

`[CONVENTION]` (v2.7.3) The identity $a^\top B J_Q b = \tfrac{\sqrt{3}}{2}\omega_{ab}$ uses the index order $\omega_{ab}=a_2b_1-a_1b_2$ for the stated $J_Q$. The independent re-derivation (GEN-ART-REDERIV) confirmed that $\{J_Q^\top B J_Q=B,\ J_Q^2=-I\}$ has exactly two solutions $\pm J_Q$; the documented $+\tfrac{\sqrt{3}}{2}$ sign fixes the branch/index-order pairing. No downstream result depends on this sign: the load-bearing properties ($J_Q^\top B J_Q=B$, $J_Q^2=-I$) are branch-independent, and $J_Q$ enters the 9-series only through $c_f=\beta J_Qs_*$, whose B-amplitude $Q_c=c_f^\top Bc_f$ is branch-invariant.

`[THM]` **Birth-symmetry (corrected v2.2).** For the certified $s^3$-seeded apex at $d_0=0$: $I_{ds}^{(1)} = \omega_{ds}^{(1)} = -Q_s^2/16$, hence $\omega_{ds}^{(1)} = +I_{ds}^{(1)} < 0$ and $\phi_{ds}^{(1)} = \pi + \arctan(\sqrt{3}/2) \approx 3.8553$ rad (3rd quadrant). The selected seeded-vector radial channel evaluates to $D_{\rm birth}^{[s^3]}=\tfrac{7}{512}Q_s^3=2Q(V_s)$. This is distinct from the seeded-state squared amplitude $Q(V_s)=Q_{d,1}^{[s^3]}=\tfrac{7}{1024}Q_s^3$ and is not by itself a demonstrated complete next-block increment. The prior $\omega_{ds}^{(1)}=-I_{ds}^{(1)}$ and second-quadrant branch are `[FAIL]` (Appendix B).

`[ALG]` **Phase-drift law (corrected v2.2).** At birth gauge, to leading order in $Q_s$:
$$\Delta\theta_s = -\tfrac{19\sqrt{3}}{2592}Q_s(16Q_s^2+27), \quad \Delta\theta_d = -\tfrac{\sqrt{3}}{4536}Q_s(848Q_s^2+783),$$
$$\Delta\phi_{ds} = -\tfrac{\sqrt{3}}{18144}Q_s(1264Q_s^2-459).$$
Sign flip at $Q_s^* = \sqrt{459/1264}\approx0.603$. The entire primitive window $Q_s \in (0, 0.1]$ is cascade-favorable ($\Delta\phi_{ds}>0$); total drift over a race window is $\approx 23°$. **Phase coherence is not the cascade bottleneck.** The prior $\Delta\phi_{ds}$ law (evaluated at $Q_s=1$; 175× scale error, wrong sign) is `[FAIL]` (Appendix B).

`[RESULT]` `[scope: reduced birth-race model]` **Isolated-$K_4$ saturation ceiling.** The full $\mathcal{P}_4$ flow has a fixed point $Q_d^* \approx 1.13\times10^{-2}$ (≈23% of the $Q_{d,\rm thresh}=0.05$ reference), with control-loss value $Q_d(n_{\rm ctrl})\approx5.6\times10^{-3}$ over the lower initial-state window $Q_{s,0}\in[10^{-3},10^{-2}]$, declining to $2.3\times10^{-3}$ at $Q_{s,0}=5\times10^{-2}$, across the recorded policies. Identical-cell network aggregation $m\mathcal{P}_4$ does not move the $\mathcal{P}_4=0$ zero, so cascade is impossible from $\mathcal{P}_4$-coupled neighbors for any $m$. Cascade requires a non-$\mathcal{P}_4$ pure-seeding source (OPEN-GEN-II-7B). These numerics are model-dependent (reduced birth-race wrapper `genesis_birth_race_model.py`), pending full UV-dynamics confirmation.

### §6.7 Quaternionic No-Go and UV Structure `[THM / mixed]` {#sec-6-7-nogo}

`[THM]` **Universal no-go.** $T_{\mathbb{H}} = T \oplus T \Rightarrow w = 0$. No smooth local metric branch from block-diagonal extension.

`[DEF]` **Minimal UV completion.** $P_\perp T_{\mathbb{H}}^{\rm UV}(x+y) = H(x) + M_{\rm spin2}(x)y + O(|y|^2)$.

`[COR]` The two UV blocks are not co-equal in derivation:
- $H(x)$: zeroth-order source block $\Pi_\parallel \to \Pi_\perp$ — requires separate source mechanism.
- $M_{\rm spin2}(x)y$: first-order restoring block from face-mismatch / spin-2 projection sector.

`[COR]` $H(x) \neq 0$ specifically means a nonzero zeroth-order $\Pi_\parallel \to \Pi_\perp$ source component, not general non-block-diagonality.

### §6.8 Canonical Face Lift `[ALG / mixed]` {#sec-6-8-facelift}

`[ALG]` **Canonical face lift matrix** (canonical face gauge):
$$\Delta M_f(w) = m\begin{pmatrix}\Im w & -\Re w \\ -\Re w & -\Im w\end{pmatrix}, \quad m = 2Q_s B_*, \quad (\Delta M_f)^2 = \kappa^2 I, \quad \kappa = |m||w|.$$

`[ALG]` $a(\phi) = r_\phi^\top \Delta M_f r_\phi = m(\Im w\cos 2\phi - \Re w\sin 2\phi)$; $|a(\phi)| \leq \kappa$.

`[DEF]` Source amplitude: $\sigma_f = |\alpha_f|(\Delta\mathcal{E}_c^{(f)})^p\sqrt{Q_c^{(f)}}$.  
`[HYP]` `[scope: reduced birth-race model]` **UV-jet amplitude threshold.** The cascade estimate $|\alpha_f|\gtrsim0.012$ derives from the reduced-model source coefficient $\sigma_{\rm min}\approx0.048$ (for $\varepsilon=\sigma\sqrt{Q_dQ_s}$) translated through this convention. Confirming it against full UV dynamics and the $\Delta\mathcal{E}_c^{(f)}$ normalization is OPEN-GEN-II-7B.
`[CONVENTION]` Primitive fracture smoothness: $p=1$.

`[COR]` **Constrained-lift sign reconciliation (GCL-02).** The v2.8.4 display
\[
(\Delta M_f+\tau I)d_\perp+S_f=0
\]
was printed beside a secular numerator with \(+2a\tau\). Exact reconstruction shows that the printed numerator belongs to
\[
K_-=\tau I-\Delta M_f,\qquad K_-d_\perp+S_f=0,
\]
whereas \(K_+=\tau I+\Delta M_f\) gives the opposite cross-term sign. The determinant factor \((\tau^2-\kappa^2)^2\) is common to both signs and cannot select the physical branch.

`[ALG]` **Conditional secular reconstruction.** For \(K_-\),
\[
\Delta_3(\tau^2-\kappa^2)^2
=\sigma_f^2(\tau^2+2a(\phi)\tau+\kappa^2)
\]
is reconstructed exactly at the declared scalar-M / canonical-face-gauge scope.

`[OPEN]` The physical \(\pm\Delta M_f\) sign, energy branch and minimizer selection must be re-derived from one typed energy/constraint equation. The prior reduced-energy and weak-stiffness “stable branch” formulas are retained only as historical/conditional calculations until that sign derivation is supplied; they are not used in this draft to select the physical branch.

### §6.9 UV Lift Theorems and Genesis II Corrections `[THM / mixed]` {#sec-6-9-uvlift}

> **[SG-13 applies]** Genesis II UV patch corrections are active here.

`[THM]` **Smooth single-face metric criterion.** If $Q_s>0$, $\beta\neq0$, $\Delta_3>0$, $\sigma_f\neq0$, $w\neq0$:
$$\det\Gamma_{\mathbb{H}} = \beta^2\Delta_3 Q_s^3 > 0.$$

`[THM]` **Local sourced-junction theorem.** If $w=0$, $\sigma_f\neq0$: vacuum gluing fails; constrained birth $(\Delta M_f + \tau I)d_\perp + S_f = 0$ has a valid minimizer.

`[COR]` (Genesis II UV patch) **Soft-mode resolvent mechanism.** Prior `[THM]` downgraded to `[ALG structure]`: critical lift is governed by a soft-mode resolvent singularity tied to $\omega - g \to 0$, structurally identified and physically motivated, but algebraic exactness not yet certified.

`[HYP]` (Genesis II UV patch) **Resonance-assisted saddle-node.** Prior `[THM]` downgraded to `[HYP]`: the resonance-assisted saddle-node bifurcation is the physical mechanism of dimensional lift, conditional upon exact resolvent derivation and projection nontriviality verification.

`[OPEN]` (Genesis II UV patch) **Projection nontriviality.** Prior `[RESULT]` downgraded to `[OPEN]`: soft-mode dominance requires that the residue of the pole at $\omega = g$ in $\chi(\omega) = H_0^\top L_{\mathbb{C}}^{-1}(\omega)H_0$ does not vanish. Not guaranteed by spectral softening alone. See OPEN-GEN-II-9.

`[ALG]` `[scope: scalar-M ansatz M=gI]` **Scalar-M resolvent** (Genesis II UV patch):
$$((\tau-g)I - \Delta M_f)^{-1} = \frac{(\tau-g)I + \Delta M_f}{(\tau-g)^2 - \kappa^2}.$$ `[RID: GEN-ALG-SCALARM-RESOLVENT]`  
Algebraic poles at $\tau-g=\pm\kappa$; selecting the physical soft branch is part of OPEN-GEN-II-9.

`[THM]` `[scope: scalar-M ansatz]` **(OPEN-GEN-II-9A) Scalar-M eigendecomposition.** With $L_{\rm sc}(\tau)=(\tau-g)I-\Delta M_f$, eigenvalues are $\lambda_\pm=(\tau-g)\mp\kappa$, $\kappa=m|w|$, and
$$L_{\rm sc}^{-1} = \frac{\Pi_+}{\tau-g-\kappa} + \frac{\Pi_-}{\tau-g+\kappa}, \qquad \Pi_\pm=\tfrac{1}{2}\!\left(I\pm\frac{\Delta M_f}{\kappa}\right).$$
Reconstruction $L_{\rm sc}^{-1}L_{\rm sc}=I$ verified symbolically. The soft branch is $\tau-g-\kappa\to0$ with soft eigenvector $v_+=(\mu_1,\ \mu_2-|w|)$. Artifacts: `resolvent_soft_mode.py`, `chi_susceptibility.py`. `[RID: GEN-THM-SCALARM-EIGEN]`

`[ALG]` **(OPEN-GEN-II-9A) Eigenbasis metric status.** $v_+\cdot v_-=0$ (Euclidean-orthogonal) but $v_+^\top B\,v_-=-\mu_1\mu_2\neq0$ ($B$-non-orthogonal). The scalar-M eigenbasis is not $B$-orthogonal.

`[ALG]` **(OPEN-GEN-II-9A) Soft-pole residue, both pairings.**
$$R^{(E)}_+ = H_0^\top\Pi_+H_0 = \frac{(v_+\cdot H_0)^2}{|v_+|^2}\geq0, \qquad R^{(B)}_+ = H_0^\top B\,\Pi_+H_0.$$
$R^{(E)}_+$ is positive-semidefinite (one vanishing line in $s_*$-space, discriminant $0$). $R^{(B)}_+$ is **sign-indefinite**: $\mathrm{sym}(B\Pi_+)$ has eigenvalues of opposite sign (discriminant $+\tfrac{1}{20}>0$ generically), so its zero set is two real lines and its sign varies with $s_*$. The Euclidean/$B$ vanishing lines are non-coincident (cross-term $3\mu_2(\mu_2-|w|)\neq0$).

`[RESULT]` **(OPEN-GEN-II-9A) Soft-pole excitation.** At the physical Bridge-Theorem source $H_0=J_Qs_*$ (corrected $J_Q$), both residues are generically nonzero: the soft pole is generically **excited** under the scalar-M ansatz. The residue numerator and its sign are convention-dependent (Euclidean PSD vs $B$ indefinite). Soft-mode excitation is certified; **saddle-node sign/dominance remains source-pairing dependent** (OPEN-GEN-II-9B). This supersedes the prior scoped residue-vanishing note.

`[ALG]` `[scope: scalar-M ansatz, §6.8 source equation]` **(OPEN-GEN-II-9B corrected scope) Covector source type; lowering bridge OPEN.** The Hessian/secular source equation is covector-valued, so \(S_f\in V^*\). The former uniqueness claim \(S_f=Bc_f\) does not follow from tensor type/covariance alone. **Conditional on** the declared \(B\)-lowering \(S_f=Bc_f\), the susceptibility \(c_f^\top BL^{-1}Bc_f\) has soft residue \(c_f^\top B\Pi_+Bc_f=|\Pi_+Bc_f|^2\ge0\), PSD and generically nonzero. Selection of \(B\) as the physical lowering map remains `[OPEN]`.

`[RETRACTED]` `[scope: scalar-M ansatz]` **(prior v2.4) Saddle-node `[FAIL]` / birth-direction-selective.** The v2.4 claim used the one-$B$ oblique form $c_f^\top B\Pi_+c_f$ (sign-indefinite) as the physical residue. That form is a diagnostic, not the variational susceptibility (which carries two $B$'s under the lowered-covector convention, or none under the vector convention). Under the declared $B$-lowering, the corrected two-$B$ residue is PSD, so the saddle-node sign is **not** disproven at scalar-M; physical selection of that lowering remains OPEN. See Appendix B and OPEN-GEN-II-9B.

`[ALG]` `[scope: scalar-M ansatz, §6.8 secular algebra]` **(OPEN-GEN-II-9B-tau corrected scope) Exact branch reconstruction; physical sign OPEN.** The \(\tau I\) multiplier type is retained. For
\[
K_-=\tau I-\Delta M_f,
\]
stationarity plus the Euclidean constraint reconstructs the documented secular equation exactly:
\[
\Delta_3(\tau^2-\kappa^2)^2
=\sigma_f^2(\tau^2+2a\tau+\kappa^2).
\]
Using \(K_+=\tau I+\Delta M_f\) flips the \(2a\tau\) sign, while the determinant factor is unchanged. Therefore the reconstruction is exact for the minus branch, but this document no longer claims that the secular factor or numerator by itself selects the **physical** sign. Physical sign/energy/minimum selection is OPEN (GCL-02).

`[ALG]` **(OPEN-GEN-II-9C) Conditional raw-array $B$-self-adjointness criterion.** If the additional modelling premise $K^\top B=BK$ is imposed, then $K=\Delta M_f+M_{\rm spin2}$ satisfies it iff $(M_{\rm spin2})_{11}-(M_{\rm spin2})_{22}=-2m\,\Im w$. Scalar $M_{\rm spin2}=gI$ cannot satisfy this ($\Im w\neq0$). Operator-side result about generalizing beyond scalar-M; with it, $\Pi_\pm$ become $B$-orthogonal and the one-$B$ diagnostic coincides with the physical residue. A simplification, not a prerequisite for soft-mode excitation (already PSD-certified). `[RID: GEN-OPEN-MSPIN2-ANISO]`

`[ALG]` **(v2.7.6) 9C conditional family + commutant collapse.** The complete solution space **under that raw-array premise** is $M_{\rm spin2}(g,D)=gI-m\,\Im(w)\,\sigma_3+D\,\sigma_1$ (forced diagonal split, free off-diagonal). The secular operator collapses to $K=gI+(D-m\,\Re w)P\in\mathrm{span}\{I,P\}$ — the $B$-commutant — sharing the $B$ eigenframe $(1,1),(1,-1)$, with closed-form soft mode at $g=|D-m\,\Re w|$. `[INTERP]`: admissibility cancels the $\sigma_3$ ($\Im w$) component of $\Delta M_f$; the $\Re w$ component merges into the off-diagonal. Second independent reconstruction from documented §6.8 inputs only; $\mu_1=\Re w$ cross-confirmed via the $\tau B$-exclusion determinant. Artifact: `mspin2_admissible_family.py` (all checks PASS).

> ⚠ **[CHECK-GEN-II-7B-NORM applies — resolved v2.7.6.]** The admissible family's *Euclidean* block norm is $\|M\|_E=g+\sqrt{D^2+m^2\Im(w)^2}\to g$ (large $g$), while the OPEN-GEN-II-7B constraint scoping uses the **B-native** norm $\|M\|_B$ (spectrum of $B^{-1}M_{\rm spin2}$) with $\|M\|_B\to2g$. These are different, individually correct objects; the cascade inequality uses $\|\cdot\|_B$, and the target $(\|H\|_B/g)|w|\gtrsim0.024$ stands. See the naming guard and exact $B$-spectrum in the OPEN-GEN-II-7B entry (§2). The 9C family certificate remains valid as algebra for the imposed raw-array condition; that condition is not promoted to a physical requirement.

`[ALG-conditional]` If single-jet construction is proved: $\alpha_f = c_0|w|$, $c_0 = \|H\|/\|M\|_{\rm op}$.

`[RESULT]` `[scope: reduced birth-race model]` **Hard-saturation (resolved v2.2).** The saturation ceiling $Q_d^*\approx1.13\times10^{-2}$ and control value $Q_d(n_{\rm ctrl})\approx5.6\times10^{-3}$ are now artifact-certified (`genesis_birth_race_model.py`) and recorded in §6.6. These are reduced-model (full-$\mathcal{P}_4$ scalar race) results, not scalar-M or constrained-resolvent claims; full-UV confirmation remains open. `[RID: GEN-ART-SATURATION]`

`[RESULT]` **$J_Q$ and smooth-$\chi$ corrections (resolved v2.2).** Corrected $J_Q=\tfrac{1}{\sqrt{3}}\begin{psmallmatrix}1&-2\\2&-1\end{psmallmatrix}$ is live in §6.6; old form and the smooth-$\chi$ parametrization are established `[FAIL]` in Appendix B (notation guard: this $\chi$ is not the susceptibility $\chi(\omega)$).

### §6.10 Foam Network Structure `[ALG / mixed]` {#sec-6-10-foam}

`[ALG]` **Apex-correlated foam.** In node-coordinate space, all active faces sharing apex $D$ must satisfy $d_{\perp,f}^* = d_\perp^{(D)}$.

`[FAIL]` Force-balance / $120°$ pattern as a generic local consequence in node-coordinate space.

`[HEUR]` Global chirality neutrality of the foam branch. Network holonomy / compatibility may select coherent patterns; remains open.

**Foam branch classification table:**

| Scope | Branch | Conditions | Result |
|---|---|---|---|
| single face | no overcritical birth | $\Delta_3 = 0$ | no lift |
| single face | smooth metric branch | $Q_s>0, \beta\neq0, \Delta_3>0, \sigma_f\neq0, w\neq0$ | nondegenerate local metric |
| single face | local sourced junction | $\Delta_3>0, \sigma_f\neq0, w=0$ | constrained birth; vacuum gluing fails |
| network | apex-correlated foam | $w=0$ network-wide, generic $\sigma_f\neq0$ | each apex carries one local $\Pi_\perp$ direction up to sign |
| network | coherent foam | same + global compatibility locking | global phase pattern `[OPEN]` |
| network | incoherent foam | effectively decoupled apices | `[HEUR]` |
| network | foam curvature | sourced network + torsion/foam invariant | `[OPEN]` `[scope: if invariant exists]` |

### §6.11 Regge Bridge `[OPEN / mixed]` {#sec-6-11-regge}

`[OPEN]` **Minimal curvature cluster.** Construct $\mathcal{C}_{\rm ref}$: closed fan around a hinge, face-adapted gluing, nonzero deficit angle, explicit RTG-to-edge-length map.

`[OPEN]` **Emergent coupling.** After $\mathcal{C}_{\rm ref}$ and smooth metric branch: $\kappa_{\rm RTG} = \mathcal{G}_e/J_e$.

`[FAIL]` $\kappa_{\rm RTG}$ as a free parameter.

`[RESULT]` $\text{OPEN M}_{\rm smooth} \prec \text{OPEN 0}_{\rm smooth}$.

---

## §7. Import Ledger {#sec-7-imports}

### From `RTG_DYADIC_OSCILLATOR_DSN_v6.4.10`

All imports carry `[scope: conditional on postulated continuous generator T]` and `[scope: local p=6, K=1 dyadic module]`.

- [RID: DYAD-THM-C21] :: $\mu_6 = -\frac{1}{2}-i\tau$, $\tau=2\sqrt{3}/3$; $\lambda=e^{i\pi/3}$; $A^3=-I$ :: §6.2 six-step healing module
- [RID: DYAD-ALG-LIEGAUGE-NORM] :: Birkhoff frame, $v_\perp$, antisymmetric channel, protection matrix :: §6.2 canonical $p=6$ eigenframe; `[conv: Lie strict-kernel gauge]`
- [RID: DYAD-ALG-P567-LEDGER] :: $p=5,6,7$ finite one-step ledger exact coefficients :: §6.2 OPEN 9 imports
- [RID: DYAD-ALG-GLATTICE5] :: $G_{\rm lattice}(5)=0$ — unique non-trivial degree-4 lattice bridge cancellation :: §6.2 OPEN 9
- [RID: DYAD-ALG-ALIAS-PHASE] :: Alias phase $G_-(\pi/\tau)=1/(1-i\tau)$, $\arg G_-=\arctan(2\sqrt{3}/3)$ :: §6.2 projection warning
- [RID: DYAD-ALG-A1A2-LIEGAUGE] :: $a_1=559\sqrt{15}/4860$, $a_2=86775991\sqrt{15}/755827200$ `[conv: Lie gauge]` :: §2 OPEN 17 (programme continuity only)

### From `RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6`

All imports carry `[scope: conditional on postulated continuous generator T]`. Consumer reconciliation against adopted v1.6 is applied in this draft.

- [RID: TRIAD-ALG-T6S-COHERENT-CONJUGATE-FAMILY] :: coherent in-plane source identity \(\|H_{\rm total}\|_B=|1-g_2|\); no-gain inequality only for real \(0\le g_2\le2\) in the declared coherent family. No physical selection of that interval or source-lowering bridge is imported.
- [RID: TRIAD-ALG-T6T-JACOBI-MODE-SIGNS] :: independently signable Jacobi mode labels in the stated node-mediated incidence reduction; **not** a theorem of physical transverse source independence or added carrier dimension.
- [RID: TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC] :: primitive apex seed diagnostics. \(Q(V_s)=7Q_s^3/1024\) is the seeded-state squared amplitude; \(D_{\rm birth}^{[s^3]}=7Q_s^3/512=2Q(V_s)\) is a differently typed increment-channel diagnostic.
- CN-01 :: review/withdraw unsupported apex–UV slot identification while retaining the \(d\)-mode and seed.
- CN-02 :: correct WPHASE child ratio/sign/symbol and dependent OPEN-M uses, subject to GCL-06 remainder typing.
- CN-03 :: positive GSPLIT consistency at exactly \(I_{sc}=0\); no reverse proof dependency.
- CN-05 :: historical \(x_*\), \(0^\circ\)–\(5.5^\circ\) safety wedge, no-safe-basin, phase-steering and route-obstruction exports are withdrawn from current use. No rescaled replacement is imported.

Inherited scope:
- current Triadic orientation-flow/basin completion remains OPEN (T-6r/T-6q);
- the exact T-6m reference quarter-turn survives at its local fixed-direction scope;
- no Triadic result supplies a physical residual, \(\kappa_{\rm phys}\), UV source, apex embedding, or global cascade verdict.


### From `RTG_DISCRETE_GENESIS_DSN_v2.12.13`

Under cross-branch firewall SG-PROG-1. No discrete results may be directly imported without a named bridge theorem.

- [scope: TDR-G policy-induced phase moments] :: Connection to OPEN 1 (phase-moment distribution) — requires OPEN TDR-19 and T-6m before any import is possible :: §2 OPEN 1 active sub-item

### Programme-context references (not scientific imports)

- `RTG_PROGRAMME_OVERVIEW_v1.2` — current programme inventory/guards; not a re-certification of Genesis claims.
- `RTG_ONTOLOGICAL_FOUNDATIONS_v0.8` — current foundational context; not proof of Genesis birth laws or UV embeddings.

### Programme continuity references

- **OPEN 16 — Dyadic alias phase decomposition:** closed in `RTG_DYADIC_OSCILLATOR_DSN_v6.4.10` `[RID: DYAD-ALG-ALIAS-PHASE]`; not a local Genesis dependency.
- **OPEN 17 — Dyadic $a_2$ computation:** closed under its declared convention in `RTG_DYADIC_OSCILLATOR_DSN_v6.4.10` `[RID: DYAD-ALG-A1A2-LIEGAUGE]`; representation/observable transport remains separately scoped; not a direct Genesis dependency.

### Export protocol

`[DEF]` Genesis may export theorem-grade primitive algebra through tetrahedral quartic drift, the block-diagonal quaternionic no-go, the smooth single-face metric criterion, and the local sourced-junction theorem with their stated scopes.

`[DEF]` Genesis may not export a physical $\kappa_{\rm phys}$, a sufficient triadic escape basin, a completed smooth metric branch, $\kappa_{\rm RTG}$, or a Regge coupling until the relevant OPENs close.

`[DEF]` Any exported claim involving Dyadic or Triadic inputs must carry `[scope: conditional on postulated continuous generator T]` until programme-level OPEN-P0 is resolved.

`[DEF]` Any exported claim involving TDR-G must cite a named discrete-continuous bridge theorem. No such bridge is currently registered.

---

## §8. Artifact Registry {#sec-8-artifacts}

- [RID: GEN-ALG-SCALARM-RESOLVENT] :: scalar-M ansatz resolvent computation (Genesis II UV patch) :: `[ALG]` `[scope: scalar-M ansatz M=gI]` — closed algebraic result; algebraic poles at $\tau-g=\pm\kappa$
- [RID: GEN-THM-DELTA-QC] :: $\Delta Q_c^{(4)} = 2c^\top B G_{3,c}(s,c,0)$ (OPEN 1C) :: `[THM]` **CLOSED v2.2** — standalone + K4-shadow pump forms; certified `genesis_k4_route_census.py` (PASS) + two-route re-derivation
- [RID: GEN-ART-G3D-SEED] :: vector apex seeding $G_{3,d}(s,c,0)$ four-channel closed form; $Q_{d,1}^{[s^3]}=\tfrac{7}{1024}Q_s^3$ :: `[ALG verified]` — `genesis_k4_route_census.py`
- [RID: GEN-ART-DELTA-QS-SHADOW] :: shadow longitudinal drift $\Delta Q_s^{(4)}$ :: `[ALG verified]` — `genesis_k4_route_census.py`
- [RID: GEN-ART-JQ-PHASEDRIFT] :: corrected $J_Q$, birth-symmetry, and phase-drift law $\Delta\phi_{ds}$ :: `[ALG]` — symbolic; sign flip at $Q_s^*\approx0.603$
- [RID: GEN-ART-SATURATION] :: isolated-$K_4$ fixed-point ceiling $Q_d^*\approx1.13\times10^{-2}$ :: `[RESULT]` `[scope: reduced birth-race model]` — `genesis_birth_race_model.py`, checksum `checksum_v272.py`; recorded control-loss values are window-dependent (≈5.6×10⁻³ over the lower window, 2.3×10⁻³ at $Q_{s,0}=5×10^{-2}$). Source location resolved; campaign validation is not re-performed by v2.8.5.
- [RID: GEN-THM-SCALARM-EIGEN] :: scalar-M eigendecomposition + soft-pole residues $R^{(E)}_+,R^{(B)}_+$ + susceptibilities $\chi_E,\chi_B$ (OPEN-GEN-II-9A) :: `[THM]`/`[ALG]` `[scope: scalar-M ansatz]` — `resolvent_soft_mode.py`, `chi_susceptibility.py` (verified)
- [RID: GEN-OPEN-UVJET-SCOPE] :: OPEN M constraint scoping — reduction to two UV scalars \(\{\|H\|,g\}\) is conditional on the additional 9C raw-array \(B\)-self-adjointness modelling premise plus the single-jet hypothesis; norm convention remains \(B\)-native and the 0.024 target retains reduced-wrapper scope :: `[RESULT conditional]` — `open_m_constraint_scope.py` (historical verification retained)
- [RID: GEN-OPEN-PHASE-MOMENT] :: OPEN 1A phase-moment reduction — $\langle\mathcal{P}_4\rangle$ linear in 13 phase moments; leading criterion $\langle\cos\phi_{ds}\rangle+\tfrac{\sqrt3}{2}\langle\sin\phi_{ds}\rangle<0$; plateau candidate #1 leading-favorable ($L\approx-1.30$) but threshold-insufficient :: `[ALG]`/`[RESULT]` `[scope: primitive $\mathcal{P}_4$, birth gauge, leading order]` — `open1_moment_reduction.py`, `open1_plateau_candidate.py` (verified)
- [RID: GEN-OPEN-PHASE-MOMENT-C2] :: OPEN 1A candidate #2 — archival-chart $h_3=0$ phase bound retained only at that chart scope; general lever gauge-class invariance withdrawn; full map + observable retest OPEN :: `[NUM/supporting]`/`[OPEN]` — historical artifacts preserved
- [RID: GEN-OPEN-WPHASE] :: corrected typing — unit identity $W(J_Qs)/W(s)=i$ retained; physical leading child ratio $W(c_0^{[3]})/W(s)=i\kappa Q_s$; leading face phase $F_{\rm face}^{(0)}=-\pi/2+\arg\mu_6$ for retained negative policies; full-phase remainder conditional on GCL-06 :: `[ALG, exact]` + `[OPEN remainder/interpretation]`; historical certificates preserved
- [RID: GEN-OPEN-WPHASE-GSPLIT] :: OPEN 5/2B-a gap-functional mode-split audit — $\Delta\mathcal{E}_c^{\rm birth}=\frac13Q_c^2+\frac34Q_sQ_c$, not scalar $G(F_W)$ :: `[ALG diagnostic]` `[scope: certified in-plane birth gap; not UV energy sufficiency]`
- [RID: GEN-CAND-APEX-T6U] :: adopted Triadic T-6u primitive seed diagnostic — $Q(V_s)=7Q_s^3/1024$ and reference seed ratio $R_{\rm apex}=\sqrt{21}/64$; **not** an HINDEX/UV source-norm ratio. Distinguish the $7/512$ seeded-vector increment-channel diagnostic :: `[CAND/diagnostic]` `[scope: primitive seed comparison]` — source `TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC`
- [RID: GEN-OPEN-APEX-SLOT] :: **RETRACTED as `[RESULT]`** — former apex–UV slot identity conflated node-label Jacobi orthogonality with state-carrier geometry. Retain \(d\)-mode label/seed; physical transverse/UV embedding remains `[OPEN]` and requires explicit enlarged carrier/metric/source map. Historical `apex_uv_frame_map.py` retained as provenance.
- [RID: GEN-IMPORT-P0-DYADIC] :: RESULT-P0-DYADIC import + conditional ×2 amplitude verdict — requires both the source/HINDEX bridge and an explicit \(E\propto\) amplitude² constitutive relation; the numerical “~2× short” conclusion is not unconditional :: `[CAND/conditional]`/`[RESULT conditional]` — imported from Dyadic DSN v6.4.10
- [RID: GEN-ART-REDERIV] :: independent clean-room **reproducibility certificate for the 9-series claims as stated** — rebuilt objects reproduce the declared formulas; this was **not** a typing audit or an audit of the §6.8 sign display and did not detect GCL-02–04 :: `[CERT scoped]` — `independent_rederivation.py`, `INDEPENDENT_REDERIVATION_REPORT.md`
- [RID: GEN-OPEN-SOURCE-PAIRING] :: covector source **type** closed; physical \(B\)-lowering bridge OPEN. Conditional on \(S_f=Bc_f\), residue PSD. 9B-tau secular formula reconstructs exactly for \(K=\tau I-\Delta M_f\); physical sign/energy branch OPEN :: `[ALG conditional]`/`[OPEN]` — source artifacts preserved
- [RID: GEN-OPEN-MSPIN2-ANISO] :: exact solution family for the **additional raw-array premise** \(K^TB=BK\): $(M_{\rm spin2})_{11}-(M_{\rm spin2})_{22}=-2m\Im w$ and \(M_{\rm spin2}(g,D)=gI-m\Im(w)\sigma_3+D\sigma_1\). 9B typing does not require this premise; physical adoption remains OPEN :: `[ALG]` `[CERT ×2]` `[scope: conditional modelling premise]`
- [RID: GEN-DEF-NORM-BNATIVE] :: OPEN-GEN-II-7B norm convention pinned — $\|M\|_B=\max|\lambda|$, $\det(M_{\rm spin2}-\lambda B)=0$ ($=$ spectrum of $B^{-1}M_{\rm spin2}$); exact $\lambda_\pm$ recorded; large-$g$ limit $2g$; scalar anchor $\|gI\|_B=2g$; naming guard $\|\cdot\|_B$ vs $\|\cdot\|_E$; CHECK-GEN-II-7B-NORM resolved, $0.012$ alternative withdrawn :: `[DEF/CONVENTION]` — `open_m_constraint_scope.py` (norm identification), verification in `mspin2_admissible_family.py`
- [RID: GEN-OPEN-HINDEX] :: source-block index trace for $H:\Pi_\parallel\to\Pi_\perp$ — CLOSED (v2.7.7): covector-valued; $\|H\|_B^2=\lambda_{\max}(B^{-1}H^\top B^{-1}H)$; $H=\sigma B$ checksum double root $\sigma^2$; vector-reading `[FAIL]` ($\{9/4,1/4\}\sigma^2$ fork); norm unified with $\|M\|_B$ on admissible family :: `[THM]`/`[DEF/ALG]`/`[CERT]` `[scope: scalar-M / face-gauge source equation]` — `independent_hindex_trace.py` (PI), `hindex_verification.py` (independent re-verification, all PASS)
- [RID: GEN-ART-PURE-CHIRAL] :: pure chiral protection and mixed-longitudinal survival audit :: `[THM]` — proof-source reference required
- [RID: GEN-ART-PHI-2TO3] :: $\Phi_{2\to3}$ one-dimensional transverse birth theorem and $Q_c \sim Q_s^3$ derivation :: `[THM]` — proof-source reference required
- [RID: GEN-ART-G2-CHRONO] :: tetrahedral chronological protection $G_2(Z)=0$ over six-step block :: `[THM]` — proof-source reference required
- [RID: GEN-ART-P4-PRIMITIVE] :: primitive tetrahedral $\mathcal{P}_4(s,c,d)$ derivation / certificate :: `[THM]` — proof-source reference required
- [RID: GEN-ART-PHASE-AVG] :: uniform independent phase-average reduction of $\mathcal{P}_4$ :: `[ALG]` — proof-source reference required
- [RID: GEN-ART-PHASE-CLOSURE] :: phase-moment closure and plateau shear bridge derivation :: `[ALG structure]` — proof-source reference required
- [RID: GEN-ART-QH-NOGO] :: block-diagonal quaternionic no-go proof ($T_{\mathbb{H}}=T\oplus T \Rightarrow w=0$) :: `[THM]` — proof-source reference required
- [RID: GEN-ART-FACE-LIFT] :: canonical face lift matrix $\Delta M_f(w)$ and constrained lift secular equation :: `[ALG]` — proof-source reference required
- [RID: GEN-ART-SOURCED-JUNCTION] :: local sourced-junction theorem proof :: `[THM]` — proof-source reference required
- [RID: GEN-ART-WPHASE] :: historical free \(F_W(\eta_*)\) target — **withdrawn as a live parametrization** for the certified \(J_Q\) birth. Current diagnostic uses \(F_{\rm face}\) with GCL-01/GCL-06 scope; artifact history retained.
- [RID: GEN-ART-REGGE-BRIDGE] :: minimal curvature cluster / RTG-to-Regge map scaffold :: `[OPEN]`

---

## §9. Collaboration and Provenance {#sec-9-provenance}

**Principal investigator:** Mustafa  
**AI / collaborator roles:** Claude · ChatGPT · Gemini · Grok  
**Archive:** Zenodo DOI 10.5281/zenodo.17568897  
**Repository:** `rtg-resonance-2025`

---

## Appendix A — Version History {#appendix-a}

### v2.8.5 DRAFT — 5 October 2026 — correction/reconciliation owner pass

**Draft state:** proposed successor; not adopted by this file-generation step. Baseline `RTG_GENESIS_GEOMETRY_DSN_v2.8.4` remains historical owner until explicit owner adoption.

- **Frozen GCL disposition:** applies GCL-01–11 to live owner text without editing the frozen correction ledger.
- **Triadic v1.6 reconciliation:** consumes CN-01/02/03/05 for Genesis and records CN-04 as a downstream OPEN-M notification; historical wedge/no-basin/phase-steering exports withdrawn from live Genesis use.
- **Import scope repairs:** T-6s no-gain requires \(0\le g_2\le2\) in its declared coherent family; T-6t is mode-label scope, not physical source-direction independence.
- **Typing repairs:** raw/odd/NF residuals separated; face-phase child ratio/sign corrected; 9B covector type separated from physical \(B\)-lowering; §6.8/9B-tau sign contradiction made explicit; 9C family made conditional on its additional raw-array premise.
- **Apex typing:** primitive \([s^3]\) seed, \([d^3]\) self-channel and hypothetical UV source separated; former apex–UV slot `[RESULT]` retracted.
- **Calibration:** ×2 verdict carries both source/HINDEX and energy→amplitude constitutive premises.
- **Saturation provenance:** \(Q_d^*\) ceiling separated from window-dependent control-loss values; the historical \(2.3\times10^{-3}\) source location is answered in owner text without modifying GCL-11.
- **Mechanical:** companion/import pointers moved to Methodology v1.3, Dyadic v6.4.10, Triadic v1.6, TDR-G v2.12.13; §6.1 owner RIDs assigned.
- **Owner-pass disposition companion:** `GENESIS_V2_8_5_OCCURRENCE_DISPOSITION_v0_1.md` records all GCL-01–11 and Triadic CN-01–CN-05 live-occurrence dispositions, deferred items and remaining gates.
- **Excluded by default:** proposed Candidates A–C and V20-O1–O5 are not scientifically integrated in this correction-first draft.

### v2.8.4 — June 2026

**Content-integration release.** Imports the Triadic T-6u apex-source result and adds the Genesis-side apex–UV slot-identity frame map. Additions-only; no prior claim corrected or retracted (the canonical-Gram $\sqrt{3/2}$ apex estimate was a Genesis-side working value, not a registered claim — explicitly superseded here).

- **§2 OPEN-GEN-II-7B [NEW]:** `[CAND]` seam note GEN-CAND-APEX-T6U importing Triadic T-6u. Certified primitive $K_4$ apex/in-plane seed ratio $R_{\rm apex}=\sqrt{21}/64\approx0.0716$ (~20x below $\sqrt2$); the $B_3$-isometric apex-lift model (~1.488) rejected as a physical source; the certified apex is a weakly seeded, self-damped torque channel. Strengthens the non-$\mathcal{P}_4$ $\sigma_f$ conclusion; consistent with the isolated-$K_4$ saturation ceiling.
- **§2 [NEW] `[RESULT]` GEN-OPEN-APEX-SLOT:** apex–UV slot-identity frame map. $d_{\mathcal{P}_4}$ and the hypothetical UV apex source $H_{\rm UV}^{(d)}$ share the transverse out-of-plane slot (the SG-7 no-go slot) at different dynamical order; the 9C off-diagonal $D$ is distinct (in-plane). Localizes the missing OPEN-M factor to one transverse slot. Numerical completion `[OPEN]` pending the UV $3\times3$ $B$-extension.
- **§1 OPEN 5/2B frontier [COR]:** annotated that T-6u closes the apex $\mathcal{P}_4$ route and the frame map localizes the residual to the transverse UV-source slot.
- **§8 [NEW]:** artifact RIDs GEN-CAND-APEX-T6U, GEN-OPEN-APEX-SLOT.
- **Supersession recorded:** canonical-Gram apex ratio $\sqrt{3/2}\approx1.22$ → certified dynamical $\sqrt{21}/64\approx0.0716$ (T-6u uses the actual certified drive coefficients, not mode Gram weights).
- **Consistency:** GSPLIT in-plane birth gap ($\tfrac13Q_c^2+\tfrac34Q_sQ_c$, v2.8.3) and the T-6u apex seed are the two channels the frame map separates (in-plane vs transverse); verified mutually consistent, no conflict.

### v2.8.3 — June 2026
- **Status summary / §2 OPEN 5/2B [COR]:** OPEN 5/2B-a added as `[ALG diagnostic]`: certified in-plane birth gap is $\frac13Q_c^2+\frac34Q_sQ_c$, not scalar $G(F_W)$; phase-chord/angular-gap/squared-gap candidates superseded as complete descriptions of the certified in-plane birth gap.
- **§2 OPEN 1T [CLOSED]:** Triadic v1.4 import status updated: Genesis may import obstruction diagnostics only; no sufficient escape basin or apex sufficiency.
- **OPEN-M candidate notes [NEW]:** T-6s in-plane no-rescue and T-6t apex well-posedness recorded as candidate seam notes, scoped to no realization/sufficiency claim.

### v2.8.2 — June 2026

**Provenance pointer refresh only; no claim-status changes.** Maintenance release. Every cited value was verified unchanged in the current source DSN before its pointer was updated; document claim-tag counts are identical to v2.8.1 ([THM] 81, [FAIL] 57, [RESULT] 51, [CERT] 8, [ALG] 64, [HYP] 25, [CAND] 5, [RETRACTED] 13, [DEF] 20).

- **Companion documents [COR]:** Dyadic v6.0→v6.4.8.1; Triadic v1.0→v1.3; Discrete Genesis v2.0→v2.12; Ontological Foundations v0.3→v0.7.
- **§7 import headers [COR]:** Dyadic/Triadic/Discrete-Genesis import-source pointers refreshed to current versions.
- **§6.1 κ provenance [COR]:** $\kappa_{\rm shear}=-2\sqrt3/3$ `[from: Triadic v1.0]`→`[from: Triadic v1.3]` (value verified unchanged: Triadic v1.3 §6, line 277).
- **OPEN 9 / OPEN 16 / OPEN 17 ledger pointers [COR]:** dyadic primary-ledger references refreshed to v6.4.8.1 (cited closures verified present with matching RIDs: DYAD-ALG-ALIAS-PHASE, DYAD-ALG-A1A2-LIEGAUGE, DYAD-ALG-P567-LEDGER).
- **Verification record:** $\kappa_{\rm shear}=-2\sqrt3/3$, $\mu_6=-\tfrac12-i\tau$ with $\tau=2\sqrt3/3$, $h_3=0$ structural, and the $p=5,6,7$ finite ledger all confirmed unchanged in the current sources. The cited imports are scientifically identical to the v6.0/v1.0/v2.0 originals; only the pointers moved.
- **Held (not in this release):** the dyadic $b=5$ all-$p$ theorem as a scoped `[CAND/conditional]` second-amplitude-factor bridge for OPEN-M — deferred pending dyadic-team export consent (would land as v2.8.3 or with the next result cluster).

### v2.8.1 — June 2026

**Content-integration release (Pass B).** Integrates the result-cluster held out of v2.8.0. This pass *does* change claims (adds `[CAND]`, `[RESULT]`, and an import); the additions and their tags are enumerated below for audit against the v2.8.0 baseline.

- **Header/footer [COR]:** Title v2.8.1; supersedes v2.8.0.
- **§2 OPEN 5/2B [NEW]:** registry entry with the direction-independence certificate ($W_{\rm child}/W_{\rm parent}=i$ exact, shared factor $=Q(s_*)$), $F_W=\tfrac{\pi}{2}+\arg\mu_6$ fixed and policy-independent `[ALG]`/`[RESULT]`, reframing to the gap functional $G$ with candidate table, prior $F_W(\eta_*)$ parametrization `[RETRACTED]` for the $J_Q$ policy. Frontier line 5 updated to match.
- **§2 OPEN 1A [NEW]:** candidate #2 (dyadic Lie-gauge) gauge-invariance result `[RESULT]` and the candidate table; computable phase candidates marked exhausted; OPEN 1 remains ACTIVE.
- **§2 RESULT-P0-DYADIC [NEW import]:** `[CAND/conditional]` import from Dyadic DSN v6.4.8.1 under the SG-15 guard (Genesis does not certify the $\times4$ rescue), plus the AUDIT-1-DIMENSIONAL ×2 cross-stream verdict `[RESULT]` (cascade amplitude-linear ⇒ $\times2$; conditional on the $h\leftrightarrow\|H\|_B$ / CAND-M-BCH bridge).
- **§8 [NEW]:** artifact RIDs GEN-OPEN-PHASE-MOMENT-C2, GEN-OPEN-WPHASE, GEN-IMPORT-P0-DYADIC.
- **No prior claim corrected or retracted** beyond the scoped $F_W(\eta_*)$ parametrization retraction (which was our own prior-turn candidate, not a document claim). Scalar-M 9-series theorem statuses unchanged.

### v2.8.0 — June 2026

**Structural-repair release (no claim changes).** Pass A of the v2.8 consolidation: readability and internal-consistency only; no result added, corrected, or retracted. Verified: every claim-tag count in the document body is identical to v2.7.7 ([THM] 79, [FAIL] 56, [RESULT] 38, [CERT] 6, [ALG] 61, [HYP] 20, [RETRACTED] 10), and every claim from the prior status summary is preserved elsewhere in the document.

- **Header [COR]:** Title v2.8.0; supersedes field updated to include v2.7.7.
- **Status summary [REWRITE]:** the ~9,000-character single-paragraph version-by-version narrative (whose version mentions were chronologically scrambled) is replaced by a ~2,800-character stable present-state summary. No claim is dropped; the version-by-version narrative remains in this Appendix A, where it is correctly ordered.
- **§1 frontier [COR]:** the stale frontier line — which still framed "derive $\alpha_f$ / $|\alpha_f|\gtrsim0.012$" as the next target — is corrected to the certified $(\|H\|_B/g)|w|\gtrsim0.024$ $B$-native OPEN M deliverable, with OPEN 0-Regge and OPEN 1 follow-up. The $0.012$ reduced-wrapper estimate retains its `[HYP]` status everywhere it legitimately appears (OPEN-GEN-II-7B, §6.6, the audit/scope rows); only the *frontier framing* of it as the next target was stale.
- **Deferred to v2.8.1 (Pass B):** OPEN 5/2B W-phase certificate, OPEN 1A candidate #2 (dyadic Lie-gauge), the ×2 cross-stream amplitude-linear verdict, and the RESULT-P0-DYADIC `[CAND]` import are NOT in this release — they are the content batch, integrated separately so the structural diff stays auditable.

### v2.7.7 — June 2026

OPEN-GEN-II-HINDEX closed (no scalar-M theorem-status changes). Artifacts `independent_hindex_trace.py` (PI), `hindex_verification.py` (independent re-verification).

- **Header [COR]:** Title v2.7.7; supersedes field updated to include v2.7.6.
- **Status summary [NEW]:** HINDEX closure recorded; guard on numerical $\|H\|$ lifted.
- **§1/§2 [COR]:** frontier item (iii) and item 3c updated to closed.
- **§2 OPEN-GEN-II-HINDEX [COR]:** entry rewritten as CLOSED with the full tag table — covector-valued $H$ `[THM]`, norm definition `[DEF/ALG]`, $\sigma B$ checksum `[CERT]`, Euclidean norm `[diagnostic only]`, vector-valued norm `[FAIL]` with the explicit $\{9/4,1/4\}\sigma^2$ fork.
- **§2 [NEW] norm unification `[CERT]`:** on the 9C admissible family, the HINDEX singular spectrum equals the squared $B$-native eigenvalue spectrum, so $\|H\|_B$ and $\|M\|_B$ are one convention and $c_0$ is matched-raising by construction.
- **§8 [COR]:** GEN-OPEN-HINDEX updated to CLOSED with both artifacts.
- **Scope discipline:** the theorem rests on the index trace; the $H=\sigma B$ case is the implementation checksum, not the theorem. The OPEN M deliverable is unchanged ($\|H\|_B$, $g$).

### v2.7.6 — June 2026

9C admissible-family certificate + B-native norm closure (no theorem-status changes; no retractions). Artifacts `mspin2_admissible_family.py`, `open_m_constraint_scope.py` (norm identification).

- **Header [COR]:** Title v2.7.6; supersedes field updated to include v2.7.5.
- **Status summary [COR]:** v2.7.6 paragraph added (admissible family; commutant collapse; norm closure; HINDEX prerequisite).
- **§1 [COR]:** frontier item 3b extended with the admissible-family landing zone; new item 3c (OPEN-GEN-II-HINDEX).
- **§2 OPEN-GEN-II-9C [NEW]:** entry rebuilt — criterion re-certified `[CERT ×2]`; complete admissible family $M_{\rm spin2}(g,D)=gI-m\Im(w)\sigma_3+D\sigma_1$ `[ALG]`; commutant collapse $K=gI+(D-m\Re w)P$ with shared $B$ eigenframe and closed-form soft mode at $g=|D-m\Re w|$; `[INTERP]` eigenframe reading; OPEN M target statement tagged `[RESULT][from: ALG][scope: operator-side admissibility]`; explicit guard that the physical block is not claimed admissible.
- **§2 CHECK-GEN-II-7B-NORM [NEW→RESOLVED]:** the factor-2 normalization fork (local Euclidean $\|M\|_E\to g$ vs wrapper $\to2g$), flagged during the 9C certificate audit, is resolved as `[DEF/CONVENTION]`: the wrapper norm is the $B$-native generalized-eigenvalue norm $\|M\|_B$ (spectrum of $B^{-1}M_{\rm spin2}$), index-consistent with the 9B $(0,2)$-Hessian calculus; exact $\lambda_\pm$ recorded; scalar anchor $\|gI\|_B=2g$; naming guard $\|\cdot\|_B$ vs $\|\cdot\|_E$ installed; cascade target $0.024$ stands; the convention-bracketed $0.012$ alternative is withdrawn.
- **§2 OPEN-GEN-II-HINDEX [NEW]:** prerequisite registered — 9B-style index-placement trace for the source block $H$ required before any numerical $\|H\|$ enters the cascade test ($c_0=\|H\|_B/\|M\|_B$ is convention-invariant only with matched raising).
- **§6.9 [NEW]:** admissible-family `[ALG]` entry + norm caution box appended to the 9C ledger.
- **§8 [COR/NEW]:** GEN-OPEN-MSPIN2-ANISO updated; new RIDs GEN-DEF-NORM-BNATIVE, GEN-OPEN-HINDEX; GEN-OPEN-UVJET-SCOPE annotated with the pinned norm convention.
- **Method note:** the norm fork was caught by cross-checking the new admissible-family Euclidean spectrum against the v2.7.5 wrapper asymptotic — a naming collision between two correct objects, not an error in either; resolved by reading the convention off the producing artifact rather than adjudicating from prose. Same failure class as the smooth-$\chi$/susceptibility-$\chi$ collision; same fix (naming guard).

### v2.7.5 — June 2026

OPEN-GEN-II-7B frontier-sharpening entry (no theorem-status changes). Artifact `open_m_constraint_scope.py` (verified).

- **Header [COR]:** Title v2.7.5; supersedes field updated to include v2.7.4.
- **Status summary [NEW]:** OPEN M constraint scoping recorded — blocker reduced to two UV scalars $\{\|H\|, g\}$; cascade test $(\|H\|/g)|w|\gtrsim0.024$ in the large-$g$ asymptotic, inheriting the reduced-wrapper `[HYP]`.
- **§2 OPEN-GEN-II-7B [NEW]:** constraint-scoping `[RESULT]` block added — $M_{\rm spin2}$ diagonal split fixed (9C), off-diagonal by the spin-2 sector once instantiated, soft-mode $g$-covariant, $\|M\|_{\rm op}\to2g$, single-inequality target.
- **§2 OPEN-GEN-II-9C [COR]:** off-diagonal wording softened to "fixed by the documented spin-2 sector once that sector is instantiated with an explicit expression" (§6.7 names the sector but gives no closed off-diagonal formula).
- **§8 [NEW]:** artifact RID GEN-OPEN-UVJET-SCOPE.
- **Scope discipline:** this is a boundary/scoping result, NOT a UV derivation. The $0.024$ constant is a target inequality (large-$g$ asymptotic + reduced-wrapper `[HYP]`), not a first-principles threshold. $\|H\|$ and $g$ remain the irreducible OPEN M inputs requiring the UV completion. No scalar-M theorem statuses changed.

### v2.7.4 — June 2026

OPEN 1A phase-moment reduction added (no OPEN M status changes). Artifacts `open1_moment_reduction.py`, `open1_plateau_candidate.py` (verified).

- **Header [COR]:** Title v2.7.4; supersedes field updated to include v2.7.3.
- **Status summary [NEW]:** OPEN 1A reduction and plateau candidate #1 verdict recorded.
- **§2 [NEW]:** frontier item 1 annotated with the 1A reduction; new OPEN 1A registry entry inserted before OPEN 1C, with the 13-moment linearity, leading criterion, and candidate #1 (plateau) result.
- **§8 [NEW]:** artifact RID GEN-OPEN-PHASE-MOMENT.
- **Scope discipline:** OPEN 1 is *reduced* to a finite moment problem, **not** closed — no global bound over all phase distributions is claimed. The plateau candidate is leading-favorable but threshold-insufficient in the reduced model. Scalar-M 9-series theorem statuses unchanged.
- **Method note:** the leading criterion explains the v2.7.2 saturation at the phase-moment level (favorable side, insufficient magnitude); the decisive cascade source remains the non-$\mathcal{P}_4$ OPEN M $\sigma_f$ term (OPEN-GEN-II-7B), independent of phase selection.

### v2.7.3 — June 2026

Certification / housekeeping patch (no theorem-status changes). Added the independent clean-room re-derivation of the scalar-M 9-series, closing the due-diligence gate flagged after the 9-series correction/retraction cycle (v2.4 retract, v2.7 overpromote-correct, three sign/branch subtleties).

- **Header [COR]:** Title v2.7.3; supersedes field updated to include v2.7.2.
- **Status summary [NEW]:** `[CERT]` independent-verification layer recorded; scalar-M 9-series declared load-bearing.
- **§6.6 [NEW]:** `[CONVENTION]` note at the $J_Q$ definition — the $a^\top BJ_Q b=+\tfrac{\sqrt3}{2}\omega_{ab}$ sign fixes the $\omega$ index-order / $\pm J_Q$ branch; downstream results depend only on $J_Q^\top BJ_Q=B$ and $J_Q^2=-I$, both branch-independent.
- **§8 [NEW]:** artifact RID GEN-ART-REDERIV (`independent_rederivation.py`, `INDEPENDENT_REDERIVATION_REPORT.md`).
- **Scope:** clean-room SymPy rebuilt $B$ (120° Gram), $J_Q$ (solved from $\{J^\top BJ=B,J^2=-I\}$), $\Delta M_f$ (traceless Euclidean-symmetric, square $=\kappa^2I$), the secular reconstruction, the lowered-source PSD residue, and the 9C criterion — all reproduced without reusing `source_pairing.py` / `index_placement_trace.py` / `tau_coupling_trace.py` / `secular_numerator_trace.py`. Only discrepancy: a cosmetic $\omega$ index-order convention (no downstream effect). No claim corrected or retracted; the $[\mathrm{CERT}]$ layer is additive.

### v2.7.2 — June 2026

Checksum-certification release. The reduced-model $\mathcal{P}_4$-only cascade-impossibility result is verified and recorded as a scoped `[RESULT]`, registered as a closed sub-item of OPEN 1 (which itself remains ACTIVE — the physical $\mathcal{M}_{\rm phase}$ is still open). Artifact `checksum_v272.py` (verified, all PASS).

- **Header [COR]:** Title v2.7.2; supersedes field updated to include v2.7.1.
- **Status summary [NEW]:** checksum-certified `[RESULT]` `[scope: reduced birth-race model]` for $\mathcal{P}_4$-only cascade impossibility; explicitly not a theorem over arbitrary $\mathcal{M}_{\rm phase}$; $|\alpha_f|\gtrsim0.012$ kept `[HYP]` `[scope: reduced wrapper estimate]`.
- **§2 OPEN 1 [NEW]:** added closed sub-item "$\mathcal{P}_4$-only cascade within the reduced birth-race model: impossible" with the three checksum numbers ($Q_d^*$, $Q_d(n_{\rm ctrl})$, $\max_{\rm scanned}<0.05$). OPEN 1 remains ACTIVE; the physically selected distribution is not claimed closed.
- **§2 OPEN-GEN-II-7B [COR]:** current-state updated to v2.7.2 with checksum cross-reference; $|\alpha_f|$ estimate explicitly tagged `[scope: reduced wrapper estimate]`; "verify, correct, or reject" sub-item retained.
- **§8 [COR]:** GEN-ART-SATURATION artifact entry updated with checksum results and `checksum_v272.py`.
- **Scope discipline:** the closure is of the reduced-model sub-question only. OPEN 1 (physical phase-moment distribution) and OPEN-GEN-II-7B (UV-derived $\alpha_f$) remain open; no theorem over arbitrary phase measures is claimed.

### v2.7.1 — June 2026

Correction + promotion. External review correctly flagged that v2.7's "full secular equation verified" was overpromoted: `tau_coupling_trace.py` had verified only the denominator factor $(\tau^2-\kappa^2)^2$ via the determinant argument, not the full numerator. v2.7.1 (a) downgrades the denominator-only claim to its correct scope, and (b) supplies the genuine full reconstruction.

- **Header [COR]:** Title v2.7.1; supersedes field updated to include v2.7.
- **Status summary [COR]:** 9B-tau denominator-level result correctly scoped; full secular reconstruction added as the theorem-grade closure.
- **Full reconstruction (new, `secular_numerator_trace.py`):** with Euclidean face-gauge constraint $d^\top d=\Delta_3$, Euclidean unit source $S_f=\sigma_f r_\phi$, and soft-branch operator $K=\tau I-\Delta M_f$, the complete documented secular equation $\Delta_3(\tau^2-\kappa^2)^2=\sigma_f^2(\tau^2+2a\tau+\kappa^2)$ reconstructs with residual identically zero. The $\pm\Delta M_f$ branch sets the sign of $2a\tau$; documented $+2a\tau$ = the $-\Delta M_f$ soft branch (9A label).
- **§6.9 [COR]:** 9B-tau theorem upgraded from denominator-only to full secular reconstruction.
- **§8 [COR]:** artifact entry updated; `secular_numerator_trace.py` added.
- **Honesty note:** the v2.7 "verified" language conflated denominator-match with full-reconstruction. The determinant argument was always sound; the overclaim was in scope, not substance. v2.7.1 separates the two and supplies the missing numerator derivation, so the theorem-grade claim is now backed end-to-end.

### v2.7 — June 2026

OPEN-GEN-II-9B-tau closed: the constrained multiplier is $\tau I$, from the documented §6.8 secular equation. Artifact `tau_coupling_trace.py` (verified). The scalar-M soft-mode frame is now self-contained with no outstanding OPEN M dependency.

- **Header [COR]:** Title v2.7; supersedes field updated to include v2.6.
- **Status summary [COR]:** 9B-tau closure recorded ($\tau I$ via $\det(\Delta M_f+\tau I)^2$ match; $\tau B$ excluded); scalar-M frame fully load-bearing.
- **§2 [COR]:** Source-pairing dependency line updated to 9B-tau CLOSED.
- **§6.9 [NEW]:** 9B closed-line extended with the 9B-tau resolution; new `[THM]` 9B-tau entry (secular-equation determinant argument + canonical-face-gauge orthonormal frame + frame-invariance consistency with 9B).
- **§8 [COR]:** GEN-OPEN-SOURCE-PAIRING artifact entry updated to include 9B-tau and `tau_coupling_trace.py`.
- **Method note:** like 9B, 9B-tau was closed from existing certified structure (the secular equation) with no new OPEN M input. The 9-series scalar-M frame (9A/9B/9B-tau) is now complete; remaining OPEN M items (9C, $H(x)$, $M_{\rm spin2}(x)$) concern generalization beyond scalar-M, not validation of the scalar-M frame.

### v2.6 — June 2026

OPEN-GEN-II-9B closed by index-placement trace (no OPEN M input required). Artifact `index_placement_trace.py` (verified).

- **Header [COR]:** Title v2.6; supersedes field updated to include v2.5.
- **Status summary [COR]:** 9B closure recorded — lowered-covector source forced by the $(0,2)$ Hessian character of the secular operator; single coherent origin for the 9A mixed structure; 9B-tau residual handed to OPEN M.
- **§1 [COR]:** Immediate-frontier item (iii) updated to OPEN M proper (9B no longer pending).
- **§2 [COR]:** OPEN-GEN-II-9B moved from ACTIVE to CLOSED with the five-step trace; removed from active frontier; added to "Recently closed". Sub-step 5 and dependency lines updated.
- **§6.9 [COR]:** 9B PSD `[RESULT]` upgraded to `[THM]` closed-by-trace with the $(0,2)$ Hessian derivation.
- **§8 [COR]:** GEN-OPEN-SOURCE-PAIRING artifact entry updated to CLOSED `[THM]`.
- **Method note:** the closure is structural (index calculus of the §6.8 energy), so it required no new OPEN M data; the one normalization assumption ($\tau I$ vs $\tau B$ coupling) is explicitly flagged as 9B-tau for OPEN M, not silently assumed.

### v2.5 — June 2026

Correction release. The v2.4 OPEN-GEN-II-9B resolution contained an index-placement error; the saddle-node `[FAIL]` verdict is retracted. Artifact `source_pairing.py` re-verified.

- **Header [COR]:** Title v2.5; supersedes field updated to include v2.4.
- **Status summary [COR]:** v2.4 source-pairing resolution and saddle-node `[FAIL]` retracted; corrected to PSD physical residue under both source-index conventions.
- **Core correction:** The variational source is a vector ($S_f=c_f$, residue $c_f^\top\Pi_+c_f$) or a $B$-lowered covector ($S_f=Bc_f$, susceptibility $c_f^\top BL^{-1}Bc_f$, residue $c_f^\top B\Pi_+Bc_f$). Both are Euclidean-orthogonal-projector quadratic forms ⇒ PSD, generically nonzero. The one-$B$ oblique form $c_f^\top B\Pi_+c_f$ (used in v2.4) is sign-indefinite but is a diagnostic, not the variational susceptibility. Verified: $\det\mathrm{sym}(B\Pi_+B)=0$, nonzero eigenvalue $\in[\tfrac14,\tfrac94]>0$.
- **§1 [COR]:** Immediate-frontier item (iii) reworded to OPEN M source index + $M_{\rm spin2}$ structure (not "sign of soft divergence").
- **§2 [COR]:** OPEN-GEN-II-9B reverted from RESOLVED to ACTIVE, rewritten as the source-index question with both PSD residues established and the v2.4 claim explicitly `[RETRACTED]`. 9B removed from "Recently closed". OPEN-GEN-II-9C significance revised (structural simplification, not saddle-node prerequisite). Priority ordering items 3b/3c updated. Sub-step 5 reverted to `[ALG structure]`; dependency lines corrected.
- **§6.9 [COR]:** Saddle-node `[FAIL]` line replaced by PSD `[RESULT]` + explicit `[RETRACTED]` note; 9C criterion reframed as structural simplification.
- **§8 [COR]:** GEN-OPEN-SOURCE-PAIRING artifact entry corrected.
- **Appendix B [NEW]:** v2.4 saddle-node `[FAIL]` retraction entry with reason and verification.
- **Provenance:** correction prompted by external review patch `OPEN_GEN_II_9B_correction_patch.md`, independently re-derived and confirmed.

### v2.4 — June 2026

OPEN-GEN-II-9B resolved by deriving the source pairing from the §6.8 variational structure (not by convention choice); OPEN-GEN-II-9C opened with a sharp $M_{\rm spin2}$ anisotropy prediction. Artifact: `source_pairing.py` (exact SymPy, verified).

- **Header [COR]:** Title v2.4; supersedes field updated to include v2.3.
- **Status summary [COR]:** 9B resolution (oblique $B$-source/Euclidean-operator pairing; sign-indefinite physical residue; saddle-node `[FAIL]` as universal theorem under scalar-M; birth-direction-selective lift) and 9C prediction recorded.
- **§1 [COR]:** Immediate-frontier line updated to the $M_{\rm spin2}$ anisotropy target (9C / OPEN M).
- **§2 [COR]:** Priority item 3b replaced by OPEN-GEN-II-9C; 9B added to "Recently closed". OPEN-GEN-II-9B registry entry rewritten as RESOLVED with the three-fact derivation; new OPEN-GEN-II-9C registry entry added with the $B$-self-adjointness criterion. OPEN-GEN-II-9 sub-step 5 reclassified to `[FAIL]`-universal / 9C-conditional; dependency lines updated.
- **§6.9 [COR/NEW]:** 9A saddle-node `[ALG structure]` line replaced by 9B `[FAIL]`-under-scalar-M result and 9C `[ALG]` restoration criterion.
- **§8 [NEW]:** Artifact RIDs GEN-OPEN-SOURCE-PAIRING and GEN-OPEN-MSPIN2-ANISO added.
- **Scope discipline:** the saddle-node is now an explicit `[FAIL]` as a *universal* theorem under scalar-M (a positive structural result: birth-direction selectivity), not a deferral; a definite-sign version is conditional on the OPEN M $M_{\rm spin2}$ anisotropy.

### v2.3 — June 2026

OPEN-GEN-II-9 sub-steps 1–4 closed under the scalar-M ansatz (new sub-item OPEN-GEN-II-9A), with the source-pairing ambiguity isolated as OPEN-GEN-II-9B. Artifacts: `resolvent_soft_mode.py`, `chi_susceptibility.py` (exact SymPy, executed and verified).

- **Header [COR]:** Title v2.3; supersedes field updated to include v2.2.
- **Status summary [COR]:** OPEN-GEN-II-9A result and 9B deferral recorded; immediate frontier updated.
- **§1 [COR]:** Immediate-frontier line extended with the source-pairing decision (9B).
- **§2 [COR]:** Priority ordering — OPEN-GEN-II-9 annotated (sub-steps 1–4 closed); 9B added as item 3b; 9A added to "Recently closed". OPEN-GEN-II-9 registry entry: sub-steps 1–4 moved to closed-under-scalar-M block with tags `[THM]`/`[ALG]`; sub-step 5 held at `[ALG structure]`; new OPEN-GEN-II-9B entry added.
- **§6.9 [NEW]:** Certified scalar-M eigendecomposition `[THM]`, eigenbasis $B$-non-orthogonality `[ALG]`, soft-pole residues both pairings `[ALG]` (Euclidean PSD / $B$ indefinite), soft-pole excitation `[RESULT]`, saddle-node `[ALG structure]`. Supersedes the prior forward-looking scoped residue-vanishing note.
- **§8 [NEW]:** Artifact RID GEN-THM-SCALARM-EIGEN added.
- **Scope discipline:** "Dominance" claim avoided; only soft-pole *excitation* certified. Residue numerator and sign are convention-dependent; the saddle-node bifurcation type is deferred to 9B, not asserted.

### v2.2 — June 2026

Genesis II archival-recovery items certified and promoted following attachment of computational artifacts (`genesis_k4_route_census.py`, all PASS; `genesis_birth_race_model.py`). OPEN 1C closed. SG-14 lifted for the now-attached items; model-dependent numerics retain explicit scope tags.

- **Header [COR]:** Title v2.2; supersedes field updated to include v2.1.
- **Status summary [COR]:** OPEN 1C closure and capacity-matching `[FAIL]` recorded; archival items marked promoted.
- **§1 [NEW]:** Triad chiral admissibility `[THM]` (standalone + K4-shadow pump forms), no-$Q_s^3$-safe-surface `[FAIL]`, NF/primitive sign split `[THM]`. Immediate-frontier line updated (OPEN 1C removed; OPEN 1 + OPEN-GEN-II-7B promoted). Archival-recovery OPEN converted to `[RESULT]` promotion note.
- **§2 [COR]:** Priority ordering — OPEN 1C moved to "Recently closed"; OPEN-GEN-II-7B promoted to immediate frontier item 2; OPEN-GEN-II-ARCHIVE marked RESOLVED. OPEN 1C registry entry rewritten as CLOSED with full result. OPEN 1 network sub-item annotated with saturation ceiling. OPEN K connection resolved. OPEN M HYP-B sub-item promoted. OPEN-GEN-II-7B current-state updated with artifact certification.
- **§6.3 [COR]:** Capacity-matching conditional converted to resolved `[FAIL]`.
- **§6.5 [NEW]:** $\Delta Q_c^{(4)}$ standalone + shadow `[THM]`; channel ledger; universal chiral pump `[RESULT]`; NF/primitive sign split `[THM]`; $G_{3,d}(s,c,0)$ vector seeding and $\Delta Q_s^{(4)}$ shadow `[ALG verified]`.
- **§6.6 [NEW]:** Corrected $J_Q$, birth-symmetry, and phase-drift law `[ALG]`; saturation ceiling `[RESULT]` `[scope: reduced birth-race model]`. Phase-drift recovery OPEN removed (resolved).
- **§8 [COR]:** $\Delta Q_c$ artifact entry closed `[THM]`; new artifact RIDs added (G3D-SEED, DELTA-QS-SHADOW, JQ-PHASEDRIFT, SATURATION).
- **Appendix B [COR]:** Pending-migration subsection converted to certified Genesis II rejected/corrected claims; added single-neighbor-cascade `[FAIL]`.
- **Scope note:** The $|\alpha_f|\ge0.012$ threshold and saturation numerics remain `[HYP]`/`[RESULT scope: reduced model]` pending full UV-dynamics confirmation; not promoted to `[THM]`.

### v2.1 — June 2026

Genesis II archival-recovery items from May 22 conversation audit incorporated. No existing v2.0 certified claims modified.

- **Header [COR]:** Updated companion documents to `RTG_PROGRAMME_OVERVIEW_v1.1` and `RTG_ONTOLOGICAL_FOUNDATIONS_v0.3`; supersedes field updated to include v2.0.
- **§1 [NEW]:** Genesis II archival-recovery frontier notice added after UV-data OPEN.
- **§2 [NEW]:** Priority items 3b (OPEN-GEN-II-7B) and 3c (OPEN-GEN-II-ARCHIVE) added to immediate frontier ordering.
- **§2 OPEN M [COR]:** HYP-B pending-recovery sub-item added.
- **§2 [NEW]:** Full OPEN-GEN-II-7B entry (UV-jet amplitude and cascade threshold, RID: GEN-OPEN-UVJET-ALPHAF).
- **§2 [NEW]:** Full OPEN-GEN-II-ARCHIVE entry (Genesis II correction/rejection recovery, RID: GEN-OPEN-GENII-ARCHIVE).
- **§3 [NEW]:** SG-14 (conversation-recovered items are not certified claims until artifact attached).
- **§4 [COR]:** Routing rule for SG-14 added.
- **§5 [NEW]:** Three high-risk rows: $|\alpha_f|\ge0.012$ threshold, hard saturation ceiling, HYP-B mechanism.
- **§6.6 [NEW]:** Phase-drift recovery OPEN (RID: GEN-OPEN-PHASEDRIFT-RECOVERY).
- **§6.8 [NEW]:** UV-jet amplitude threshold recovery OPEN (inline, see OPEN-GEN-II-7B).
- **§6.9 [NEW]:** Hard-saturation recovery OPEN (RID: GEN-OPEN-HARDSAT-RECOVERY); $J_Q$ and smooth-$\chi$ correction recovery OPEN (RID: GEN-OPEN-JQ-CHI-RECOVERY).
- **Appendix B [NEW]:** Pending Genesis II archival migration candidates subsection with six `[FAIL]` recovery entries (HYP-A, HYP-C, incoherent seeding, old $J_Q$, smooth-$\chi$ parametrization, old birth-symmetry/phase-drift law).

### v2.0 — June 2026

Full refactor to DSN_METHODOLOGY_v1.2 architecture. Active scientific ledger content preserved or routed; Genesis II UV patch absorbed.

- **Naming [COR]:** Canonical name changed to `RTG_GENESIS_GEOMETRY_DSN` per dual-name convention.
- **Status Tags table [REMOVED]:** Replaced by `DSN_METHODOLOGY_v1.2` pointer + Local Tag Aliases.
- **v1.1 Update Summary [MOVED]:** To this Appendix A subsection below.
- **Part XII §30 Settled Claims [PROMOTED]:** → §1 Current Canonical State with explicit DSN tags.
- **Part XII §31–32 Immediate/Secondary Next Derivation [MOVED]:** → §2 priority ordering.
- **Part X OPEN Ledger [RESTRUCTURED]:** Prose OPEN entries → structured ledger entries with RIDs and sub-items.
- **Part XI Forbidden Overclaims [MOVED]:** → §5 High-Risk Claims Ledger + Appendix B.
- **Import Ledger §7:** Full import ledger with RIDs, inherited scope clauses, and cross-branch firewall notes.
- **Genesis II UV patch [ABSORBED]:** Three `[COR]` downgrades integrated into §2 OPEN-GEN-II-9 and §6.9; scalar-M resolvent registered as `[RID: GEN-ALG-SCALARM-RESOLVENT]`.
- **Prior errata round:** Header scope, `[ARCHIVE-READY]` alias, scalar-M pole ($\pm\kappa$), OPEN 9 $\Phi_p$ wording, OPEN 1T, SG-12b, §4 routing rules, §5 table, §6.2 Birkhoff label, §6.4 cycle-averaging tag, §7 import scope and OPEN K reference, §8 artifact expansion.

Final errata applied before canonical freeze:
- **Programme tier [COR]:** Discrete/TDR-G routed through bridge requirements, not directly imported.
- **Status summary [COR]:** Distinguished closed scalar-M ansatz resolvent `[ALG]` from still-open full constrained soft-mode susceptibility / physical branch selection.
- **§2 [COR]:** OPEN 1T added to priority ordering (item 2b). OPEN 1C: defined $s^+$ as post-fracture/post-birth longitudinal state. OPEN-GEN-II-9: sub-step 1 split into scalar-M first pass (1) and full $M_{\rm spin2}$ generalization (1b).
- **§6.1/§6.2/§6.3/§6.4/§6.5/§6.7/§6.8/§6.9 [COR]:** Marked mixed-status section headings explicitly with `/ mixed`.
- **§6.10 [COR]:** Replaced `[OPEN-if-exists]` with canonical `[OPEN]` `[scope: if invariant exists]`.
- **AI Context Core marker:** Inserted at end of §4.

Final errata applied before freeze:
- **Local Tag Aliases [COR]:** `[ARCHIVE-READY]` row removed (unused).
- **§1 [COR]:** Decorative boxes removed from primitive generator and scalar-M resolvent formulae; $\mathcal{P}_4$ box retained as primary scientific object.
- **§2 OPEN 1 [COR]:** TDR-G policy-induced moments dependency strengthened to require TDR-24D/A/B, TDR-T, and a named bridge theorem — not just TDR-19 and T-6m.
- **§2 handoff queue [COR]:** TDR-G dependency wording strengthened to include TDR-T statistics and named bridge theorem.
- **§2 [NEW]:** Secondary / blocked frontier queue added (OPEN 5/2B, OPEN K, OPEN M-foam, OPEN 0-Regge → OPEN 0).
- **§2 [COR]:** OPEN 16 and OPEN 17 removed from Active Frontier; moved to §7 Programme continuity references.
- **§6.6/§6.10/§6.11 [COR]:** Section headings marked `/ mixed`.
- **§6.9 [COR]:** Projection residue condition branch-scoped to $+\kappa$ soft branch; $-\kappa$ branch sign-reversal noted; branch selection routed to OPEN-GEN-II-9.
- **§7 [NEW]:** Programme continuity references subsection added (OPEN 16, OPEN 17).
- **§7 [NEW]:** Export protocol added (four `[DEF]` entries: exportable content, blocked exports, generator-T scope, TDR-G bridge requirement).
- **§8 [NEW]:** Added proof-source placeholder RIDs for pure chiral protection, $\Phi_{2\to3}$ birth theorem, $G_2=0$ chronological protection, phase-moment closure, and W-phase insertion target.
- **Appendix B [COR]:** Genesis II UV patch `[COR]` demotion entries converted to `[RETRACTED]` with reason format.

### v1.1 Update Summary (from superseded document)

- OPEN 9 / general $p$-resonance imports including $p=5,6,7$ finite ledgers.
- Dyad-to-triad antisymmetric bridge: canonical $W$-frame, $v_\perp$, raw-vs-normalized cubic coefficient distinction.
- Corrected $\Phi_{2\to3}$ policy split: shear, recoil, capacity/defect-conservation branches.
- Closed primitive tetrahedral $Q_d$-quartic drift polynomial $\mathcal{P}_4(s,c,d)$.
- Phase-moment bridge and uniform independent phase-average sink result.
- Next load-bearing computation identified: $\Delta Q_c^{(4)}=2c^\top BG_{3,c}(s,c,0)$.

---

## Appendix B — Retired and Rejected Claims {#appendix-b}

### Genesis II certified rejected/corrected claims (migrated v2.2)

`[DEF]` Entries below were recovered from the May 22 Genesis II audit and certified in v2.2 via `genesis_k4_route_census.py` (all PASS) and `genesis_birth_race_model.py`. Corrected forms are live in §6.5–§6.6. SG-14 no longer gates these.

**[FAIL | RID: GEN-FAIL-HYP-A]** HYP-A cascade mechanism (plateau/relaxed neighbor as sustained injector). Reason: a neighbor at its own $\mathcal{P}_4$ fixed point has $G_{3,d}=0$ as a vector, hence zero projection onto the shared apex; below the fixed point it gives only a decaying transient (≈13% of the gap). Not a sustained mechanism.

**[FAIL | RID: GEN-FAIL-HYP-C]** HYP-C cascade mechanism (heterochronous uniform-phase spread). Reason: source terms average to zero over uniform $\phi_{ds}$; barrier terms average negative. $\langle\mathcal{P}_4\rangle_{\rm uniform}\approx-4.58\times10^{-5}<0$ — phase-spread neighbors are ≈1.7× worse than the isolated cell.

**[FAIL | RID: GEN-FAIL-INCOHERENT-SEEDING]** Incoherent seeding cascade, 2D random-walk scaling $\lambda_{\rm eff}=m\lambda_0^2$. Reason: with $\lambda_0=\lambda_{\min}/m$, $\lambda_{\rm eff}=\lambda_{\min}^2/m\to0$; adding incoherent neighbors never recovers cascade. RTG edge-sharing is fully coherent by zero-sum holonomy, so the incoherent scenario is a counterfactual diagnostic only.

**[FAIL | RID: GEN-FAIL-OLD-JQ]** Prior $J_Q$ operator form $(\sqrt{3}/2)\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}$ for the B-metric. Reason: does not satisfy $a^\top BJ_Q b=\tfrac{\sqrt{3}}{2}\omega_{ab}$. Corrected form $J_Q=\tfrac{1}{\sqrt{3}}\begin{psmallmatrix}1&-2\\2&-1\end{psmallmatrix}$ is live in §6.6. This $J_Q$ is the birth-direction/phase-drift rotation operator, distinct from all other uses of $J$.

**[FAIL | RID: GEN-FAIL-SMOOTH-CHI-PARAM]** Smooth coherence parametrization $\chi\in[0,1]$ via $\lambda_{\rm eff}=\chi m\lambda_0$. Reason: coherence is a phase transition (coherent $\lambda_{\rm eff}=m\lambda_0$ vs incoherent $m\lambda_0^2$), not a continuously tunable parameter. Notation guard: this $\chi$ is not the susceptibility $\chi(\omega)$ in OPEN-GEN-II-9.

**[FAIL | RID: GEN-FAIL-OLD-BIRTH-SIGN-PHASEDRIFT]** Prior birth-symmetry sign $\omega_{ds}^{(1)}=-I_{ds}^{(1)}$ (second-quadrant $\phi_{ds}^{(1)}\approx2.43$) and old $\Delta\phi_{ds}$ law evaluated at $Q_s=1$ (175× scale error, wrong sign). Reason: corrected to $\omega_{ds}^{(1)}=+I_{ds}^{(1)}<0$, $\phi_{ds}^{(1)}=\pi+\arctan(\sqrt{3}/2)\approx3.8553$, and $\Delta\phi_{ds}=-(\sqrt{3}/18144)Q_s(1264Q_s^2-459)$ with sign flip at $Q_s^*\approx0.603$. Corrected forms live in §6.6.

**[FAIL | RID: GEN-FAIL-SINGLE-NEIGHBOR-CASCADE]** "Single coherent $K_4$ neighbor suffices for cascade" / "$\lambda_{\min}\Rightarrow\lambda_0=\lambda_{\min}/m$ from gluing identical cells". Reason: object mismatch — the abstract injector $\varepsilon=\lambda Q_d$ is barrier-free, whereas a physical $K_4$ neighbor contributes the full $\mathcal{P}_4$ with its own barriers; the $\mathcal{P}_4=0$ ceiling cannot be broken by identical-cell aggregation. Cascade requires a non-$\mathcal{P}_4$ source (OPEN-GEN-II-7B).

---

### Established rejected and retired claims

- `[FAIL]` Full triad quadratic cancellation — only pure chiral cancellation proved.
- `[FAIL]` Old scalar quartic secular drift law — wrong pure-$d$ coefficient ($-\frac{1}{2}$ instead of $-1$); scalar laws require projection layer.
- `[FAIL]` $-\frac{1}{2}Q_d^2$ as primitive six-step pure-$d$ coefficient — one-step artifact.
- `[FAIL]` Uniform independent phase averaging can produce cascade — always a sink.
- `[FAIL]` Raw antisymmetric cubic $=$ Birkhoff normal-form cubic — near-identity coordinate change separates them.
- `[FAIL]` Dyad alone fixes $\kappa_{\rm phys}$, $\alpha_f$, or $w$.
- `[FAIL]` $T \oplus T$ generates smooth 3D metric branch ($w=0$ theorem-grade no-go).
- `[FAIL]` $\alpha_f = c_0|w|$ without single-jet construction.
- `[FAIL]` Foam chirality neutrality as a theorem.
- `[FAIL]` $\kappa_{\rm RTG}$ as a free parameter.
- `[FAIL]` Force-balance / $120°$ pattern as generic local consequence in node-coordinate space.
- `[RETRACTED]` Soft-mode resolvent singularity governs critical lift as `[THM]`. Reason: exact constrained resolvent and projection nontriviality are not yet certified. Replaced by `[ALG structure]`; see OPEN-GEN-II-9.
- `[RETRACTED]` Resonance-assisted saddle-node is an exact theorem. Reason: conditional on resolvent derivation and projection nontriviality; downgraded to `[HYP]`; target remains `[THM]`.
- `[RETRACTED]` Soft-mode projection nontriviality resolved. Reason: not certified; downgraded from `[RESULT]` to `[OPEN]`; see OPEN-GEN-II-9 sub-step 3.
- `[RETRACTED]` Exact scalar susceptibility derived. Reason: not certified; downgraded from `[CLOSED]` to `[OPEN]`; see OPEN-GEN-II-9 sub-step 4.

- `[RETRACTED]` (v2.4 → v2.5) Scalar-M physical soft residue $=c_f^\top B\Pi_+c_f$ (one-$B$ oblique form), sign-indefinite, ⇒ saddle-node `[FAIL]` as universal theorem / birth-direction-selective lift. Reason: index-placement error. The variational source enters as a vector ($S_f=c_f$) or $B$-lowered covector ($S_f=Bc_f$), giving residues $c_f^\top\Pi_+c_f$ or $c_f^\top B\Pi_+Bc_f$ respectively — both PSD (Euclidean-orthogonal-projector quadratic forms). The one-$B$ form is a diagnostic, not the variational susceptibility. Corrected in OPEN-GEN-II-9B (v2.5); the saddle-node sign is not disproven at scalar-M. Verified: $\det\mathrm{sym}(B\Pi_+B)=0$, nonzero eigenvalue $\tfrac54+\mu_1/|w|\in[\tfrac14,\tfrac94]>0$.

---

*END OF DOCUMENT — RTG_GENESIS_GEOMETRY_DSN_v2.8.5_DRAFT*  
*Draft successor to RTG_GENESIS_GEOMETRY_DSN_v2.8.4. Correction-first scope: GCL-01–11 dispositions, adopted Triadic v1.6 reconciliation, current source/RID repairs, and no default admission of V20-O1–O5 or Candidates A–C. The former apex–UV slot identity and historical Triadic wedge/phase-steering obstruction chain are not live claims. Physical residual, lowering map, constrained-lift sign, 9C modelling premise, \(\kappa_{\rm phys}\), UV source realization and all-order bridges remain OPEN. Conforms to DSN_METHODOLOGY_v1.3.*
