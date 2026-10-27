# RTG_DISCRETE_GENESIS_DSN_v2.12.14

**Title:** RTG Discrete Relational Genesis — Canonical Study Ledger  
**Date:** October 2026 (v2.12.14, corrections only; the scientific content of the v2.12 line is dated June 2026)  
**Scope:** Fully discrete pre-metric relational universe on $\mathbb{Z}_N$. Interaction from relational distinguishability; no continuous coordinates; no imported continuous coefficients.  
**Supersedes:** `RTG_DISCRETE_GENESIS_DSN_v2.12.13` (tag `tdrg-v2.12.13`, SHA-256 `aa232643f6f631694b0eda1532be213e5a517ef109cd66794f8e638e24fc053f`); the earlier lineage is in the footer and Appendix A (compaction is v2.13 work)  
**Companion documents (governing editions, October 2026):** Programme Overview v1.3 (`programme-v1.3`) · Ontological Foundations v0.10 (`ofn-v0.10`) · DSN Methodology v1.4 (`methodology-v1.4`). Claim-specific historical pins (Programme v1.1, OFN v0.6/v0.7) stay where a statement cites them.  
**DSN Methodology:** DSN_METHODOLOGY_v1.2 (declared; kept for this corrections edition by PI decision of 27 Oct 2026 — the v1.4 migration is v2.13)  
**Programme tier:** Tier 4 — Discrete Programme (see Programme Overview §6)  
**Status summary:** TDR-G is a working finite-state relational universe with three certified simulation branches. $k/N$ controls entry into the growth regime; the multistar interaction axiom controls growth character. The canonical clean branch (`bound_symmetric`) shows bulk-conditioned birth rate $B_{\rm bulk}/\text{step} \sim N^{-0.869}$ (v17/v6 canonical scan, full-range fit $N=120$–$1440$; the exponent is window-dependent, §1); thermodynamic crystallization in the $N\to\infty$ limit is a `[HEUR]` extrapolation. TDR-24D and TDR-24F are closed at the mechanism level with their analytic constants OPEN; the gate before discrete triadic dynamics is TDR-24A → TDR-24B → TDR-24C. **v2.12 adds the genesis-layer kinematics and three-node (BIND3) certification arc:** two conventions pinned to script truth (CONV-TICK `[ENG PASS v18]`, CONV-P3CYC successor-shift `[DEF, script-certified]`); four certified lemmas — band-form reachability (LEM-REACH), no-free-annihilation (LEM-NOANNIHIL, replacing the trap axiom upstream in OFN), two-node retrigger/binding threshold (LEM-RETRIG), and conservation of the relational advance spectrum (LEM-SPECCONS, three-node no-birth scope); exact cycle enumeration BIND3-CYCLE-N24K1 (`[ALG]`, finite exact enumeration) establishing that the isolated period-2 bound dyad is not a persistent primitive in the three-node universe (generic exact orbits are multi-pair recurrent scattering cycles with bond transfer); and the NKSCAN falsification suite certifying BIND3-PARITY (survival controlled by advance parity, not binding marginality; BIND3-KNIFE `[FAIL]`/`[REPLACED]`), BIND3-SPECTRAL-GATE (the conserved spectrum is a hard gate on autonomous retrigger), and BIND3-MEMORY-PARITY (binding-history memory is an even-advance sector effect; the odd-sector claim is a composition artifact, `[COR]`). New scope guards SG-11–SG-13; new §6.12. **v2.12.14 (corrections only):** the path orientation rule TDRG-DEF-ORIENT is made node-relabelling covariant by extending the balanced path-tie to $S=0\wedge 2E\equiv0 \pmod N$, with the covariance group named in SG-14; `signed_centered` and `signed_defect_error` are defined; claim RIDs are registered (§7 owner RID map); results computed with the superseded completion keep `[conv: v18 path orientation]` and `EV-NOT-RERUN` (census bound, §6.12).

## Local Tag Aliases

| Local alias | Expands to | Used for |
|---|---|---|
| `[INTERP]` | `[HEUR]` [scope: interpretation] | interpretive reading of a stated result |
| `[REVISED]` | `[COR]`; the revised assertion carries its own tag | in-place revision notes |
| `[REJ]` | `[FAIL]` [scope: the item as stated] | rejected candidate inside an OPEN record |
| `[REPLACED]` | `[SUPERSEDED]` with the replacement pointer | BIND3-KNIFE |
| `[ENG audit: PASS]` | `[ENG]` [scope: the named conformance audit] | CONV-TICK |
| `[NUM exhaustive: …]` | evidence note: exhaustive finite verification over the stated range | lemma certificates |
| `[SCOPE …]`, `[ADMIN …]`, `[METHOD]`, `[BRANCH …]` | prose labels (scope, administrative or tooling, method, exploratory-branch notes); not truth tags | §2 |

Canonical tags follow `DSN_METHODOLOGY` (declared v1.2; the spellings are unchanged in v1.4 §8.1). *(v2.12.14: the legacy rows `[ALG/NUM]`, `[ENG/ALG]`, `[NUM-strong]`, `[HEUR-strong]` are removed and the live compound tags are unpacked; Appendix A history keeps its original spellings.)*

---

## §1. Current Canonical State {#sec-1-canonical-state}

`[DEF]` The TDR-G universe is a finite relational system on $\mathbb{Z}_N$ ($N$ even) with variable-size state
$$X_n \in \bigsqcup_{M\ge2}\mathbb{Z}_N^{2M}, \qquad X_n=(\theta_1,\ldots,\theta_{M_n},\delta_1,\ldots,\delta_{M_n})$$
where $M_n$ increases at each star blow-up, and all physics is in relational phase differences $\Delta_{ij} = (\theta_i - \theta_j) \bmod N$. Absolute phases are gauge.

`[DEF]` The defect band is $\mathcal{D}_k = \{\Delta \in \mathbb{Z}_N : \operatorname{dist}_{\mathbb{Z}_N}(\Delta, N/2) \leq k\}$. Nodes $i,j$ are defect-related when $\Delta_{ij} \in \mathcal{D}_k$.

`[THM]` **Holonomy.** For any three nodes: $\Delta_{AB} + \Delta_{BC} + \Delta_{CA} \equiv 0 \pmod{N}$.

`[THM]` **Narrow-band exclusion.** Under $k < N/6$, no three mutual nodes can all be defect-related: $|E_{\rm def} \cap K_3| \leq 2$.

`[THM]` **Reachability / superselection.** For $k=0$, interaction between two nodes occurs iff $\gcd(d,N) \mid (N/2 - \Delta_0)$. Unreachable pairs are superselection sectors. **(v2.12)** Band-form extension (LEM-REACH): $\mathcal{D}_k$ reachable $\iff \mathcal{D}_k\cap(\Delta_0+g\mathbb{Z}_N)\neq\varnothing$; superselection persists at $k>0$ in the two-node universe. See §6.5.

`[ALG]` **(v2.12) Genesis-layer kinematic lemmas.** No free annihilation: $F^t(\Delta_0,d_0)=(0,0)\iff(\Delta_0,d_0)=(0,0)$ (LEM-NOANNIHIL). Two-node binding threshold: retrigger on every tick — period dividing 2, least period 2 for $d\neq0$, a fixed point at $d=0$ — iff $\varepsilon\in B_k\cap(B_k+d)$, possible iff $|d|_c\le2k$ (LEM-RETRIG). Three-node advance-spectrum conservation: $\{|d_{ij}|_c\}$ is an exact invariant under swap/$P_3$/tie events, no-birth scope (LEM-SPECCONS). See §6.5, §6.12.

`[NUM strong]` `[conv: v18 path orientation]` **(v2.12) BIND3 headline.** In the three-node universe ($N=24$, $k=1$, exact cycle enumeration), the isolated period-2 bound dyad is not a persistent primitive: 96.4% of bound-entry ICs yield multi-pair recurrent scattering cycles with bond transfer in 81.8%; pure-bound survival (3.6%) is confined to even-advance parity sectors (BIND3-PARITY); the conserved spectrum gates autonomous retrigger (BIND3-SPECTRAL-GATE). See §6.12.

`[ALG]` **Birth-rate invariant.** $rN_{\rm err} = 0$ in all valid v16 motif logs. The identity $rN_T = \text{birth\_steps} \cdot b/\text{step}$ holds to machine precision.

`[ALG]` [assuming: the microscopic birth law, `[NUM]`, for the first identity] **TDR-24 factorization.** $C_{\rm birth} = C_{\rm component} / \chi$, and $B/\text{step} = O/\text{step} \cdot C_{\rm birth}$. Numerically corroborated: all identities verified to $<10^{-18}$ in every valid v16 motif log.

`[NUM]` **Microscopic birth law** (under `bound_symmetric`). `births_step` $=$ `clean_star_components` for all steps with nonzero births. Every birth is generated by exactly one clean single-center star component.

`[NUM]` `[scope: full-range composite fit, N=120–1440]` `[conv: v18 path orientation]` **N-scaling** (v17/v6 canonical scan). At fixed $k/N = 1/15$, $T=5000$, bulk-conditioned (excluding tail runs $M>500$):
$$B_{\rm bulk}/\text{step} \sim 1.041 \cdot N^{-0.869}, \quad R^2 = 0.973.$$
The exponent is window-dependent: read on the high-N window $N=480$–$1440$ with run-level bulk filtering, the same scan gives $B/\text{step}\sim N^{-0.730}$ (Experiment-0 readout, §2 OPEN-POLICY-GEOMETRY). $-0.869$ is the full-range convenience value, not a structural constant (the failure class of $\chi$, $C_{\rm component}$ and $q_{\rm proj}$, §2 TDR-24A/B); no refit is made here. (Supersedes the v4 6-point fit $N^{-0.876}$, $N=120$–$1080$.)

`[HEUR]` **Thermodynamic crystallization.** Extrapolating the fitted N-scaling gives $B_{\rm bulk}/\text{step} \to 0$ as $N \to \infty$. No plateau through $N = 1080$. Not yet theorem-grade.

`[NUM strong]` **Three-policy characterization.** `bound_symmetric` → crystallization; `largest_center` → continuous inflation ($rN_T \approx 0.76$–$0.80$ at $k/N \approx 0.0667$); `all_centers` → avalanche inflation ($b/\text{step} \approx 16$–$25$, often cap-limited). Policy choice is physically real, not an implementation detail.

`[ALG]` **Dynamic equivalence.** On state evolution, `trap`, `bound_multistar`, and `bound_path_tie` are dynamically equivalent whenever multistars/path-ties generate no births and no momentum transfer. They may differ in bookkeeping, ambiguity counters, and run-status semantics.

`[HEUR strong]` **Multistar locking mechanism.** In the late-window bulk under `bound_symmetric`, $f_{\rm ms} \approx 1$: large multistar bound states dominate, suppressing clean single-center star births and producing the slow-accretion regime.

**Slot-volume model (verified).** `[ALG]` $O_t = (2k+1) M_t \psi_t$ holds by construction in the v6 extractor. `[NUM strong]` Across the canonical $k/N=1/15$ scan, $\psi_{\rm slot}^{\rm bulk} \approx 0.00204 \cdot N^{+0.014}$ ($R^2 = 0.015$) — effectively intensive (scale-invariant). The positive scaling $O_{\rm bulk}/\text{step} \sim N^{+0.723}$ is therefore explained by slot-volume growth ($O_{\rm slot}^{\rm bulk}/\text{step} \approx 53.69 \cdot N^{+0.709}$, $R^2=0.976$), not by the rejected $M^2$ pair model. The N-independence of $\psi_{\rm slot}^{\rm bulk}$ is explained (TDR-24F resolved `[NUM strong]`): a bounded structural reservoir $\bar{c}_{\rm struct}\approx5$ with projection efficiency $q_{\rm proj}\sim(2k+1)$ exactly offsetting the band, giving $\psi\sim N^0$. (The earlier $q_{\rm proj}\sim N^{1.371}$ was a fit artifact; corrected to $N^{1.06}$.)

`[DEF]` **Immediate frontier gate:** TDR-24D (slot-volume identity: `[ALG]` identity, `[NUM strong]` intensiveness) and TDR-24F (structural-to-slot projection mechanism, `[NUM strong]`) are closed at the mechanism level; their analytic constants ($\bar{c}_{\rm struct}\approx5$, $q_{\rm proj}\sim(2k+1)$) remain OPEN. The remaining gate before discrete triadic dynamics (TDR-T) is TDR-24A → TDR-24B → TDR-24C.

---

## §2. Active Frontier / OPEN Registry {#sec-2-open-registry}

### Priority ordering

**Immediate derivation chain** (blocks TDR-T):
1. ~~**TDR-24D**~~ — slot-volume identity **CLOSED** (`[ALG]` identity; `[NUM strong]` intensiveness); see Settled items and §6.8.
2. ~~**TDR-24F**~~ — structural-to-slot projection **RESOLVED** `[NUM strong]` ($q_{\rm proj}\sim N^{1.06}$, $\bar{c}_{\rm struct}\approx5$ bounded); analytic constants still open.
3. **TDR-24A** — topological filtering / multistar embedding statistics.
4. **TDR-24B** — pair-to-component compression / $\chi$-scaling.
5. **TDR-24C** — combine F/A/B into thermodynamic suppression or identify obstruction.

**Policy-selection frontier:**
5. **TDR-19** — derive or reject `bound_symmetric` as canonical.
6. **TDR-1** — derive defect band and interaction law from relational principles.

**Surveillance frontier:**
7. **TDR-24N / TDR-25 / TDR-26** — finite-size anomalies, tail law, locking-failure topology.

**Genesis-kinematics / BIND3 frontier** *(new in v2.12; does not block TDR-T)*:
8. **OPEN-BIND3-PARITY-GEN** — general $(N,k,d)$ spectator-lattice avoidance theorem.
9. **OPEN-BIND3-MEMORY** — residence-time mechanism for the even-sector occupancy bias.
10. **OPEN-BIND3-REGEN** — $P_3$ lattice-action theorem on the conserved spectrum.
11. **OPEN-BIND3-NKSCAN** — remaining stratified $(N,k)$ scan; three of its pre-registered targets are already executed (see §6.12).
12. **OPEN-SPECCONS-STAR** — advance-spectrum behavior across star blow-up (SG-12).

**Owner-review tasks** *(v2.12.14; recorded for TDR-G by Programme v1.2 §6, not carried by Programme v1.3)*: (1) state/gauge conventions — advanced in v2.12.14 (state and gauge definitions registered as TDRG-DEF-ZN-STATE and TDRG-DEF-PHYSICAL-STATE; covariance group named in SG-14; the common token shift recorded as not a gauge, §7); otherwise open; (2) the antipodal path tie — **discharged** by TDRG-DEF-ORIENT (v2.12.14); (3) counting observables (§6.11) — open; (4) statistical/rank interpretation of the growth fits (§2 TDR-24B rank analysis, §6.8) — open.

---

**OPEN TDR-1 — Interaction onset derivation** [RID: TDRG-OPEN-INTERACTION-ONSET]

Status: ACTIVE | Layer: O2→O4  
Question: Derive the defect band $\mathcal{D}_k$ and the swap/blow-up interaction law from relational distinguishability, closure, or finite-state consistency alone.  
Current state: The bounded distinguishability principle (`[HEUR]`) motivates interaction; no variational or extremal derivation has been produced.  
Connection: OPEN-OFN-2 in `RTG_ONTOLOGICAL_FOUNDATIONS_v0.6`.

---

**OPEN TDR-6 — Birth invariant** [RID: TDRG-OPEN-BIRTH-INVARIANT]

Status: ACTIVE  
Question: Identify a purely relational invariant preserved (or predictably changed) across star blow-up.

Active sub-items:
- Total additive momentum $P$: `[FAIL]` — gauge artifact.
- $\sum \delta_i^2$: `[FAIL]` — increases by $\delta_A^2$.
- Pairwise difference multiset: `[OPEN]`
- Holonomy closure of new triangles: structurally automatic; dynamical invariant status `[OPEN]`

---

**OPEN TDR-19 — Multistar axiom derivation** [RID: TDRG-OPEN-MULTISTAR-AXIOM]

Status: ACTIVE  
Question: What principle selects the canonical multistar resolution policy?

Active sub-items:
- Physical selection principle (minimal information / closure preservation / relational extremum): `[OPEN]`
- Derivation of `bound_symmetric` as canonical: `[OPEN]`

Current state: Three policies are characterized and physically distinct (`[NUM]`). No first-principles derivation selects among them. See §6.3.  
Connection: OPEN-OFN-2 in `RTG_ONTOLOGICAL_FOUNDATIONS_v0.6`.

---

**OPEN TDR-22a — Fixed-N asymptotics** [RID: TDRG-OPEN-FIXED-N-ASYMP]

Status: ACTIVE  
Question: For fixed $N, k$, does slow accretion continue indefinitely or terminate?  
Current state: $N=120, k=8$ shows $rN_{\rm late} \approx 0.02$ through $T=10000$ with $rN_{\rm late}/rN_T \to 0.894$, consistent with approach to steady accretion rather than terminal cooling.

---

**OPEN TDR-22b — Thermodynamic crystallization** [RID: TDRG-OPEN-CRYSTALLIZATION]

Status: ACTIVE  
Question: Does $\lim_{N\to\infty} rN_{\rm late}(N, k/N) = 0$?  
Current state: `[NUM]` full-range fit $B_{\rm bulk}/\text{step} \sim N^{-0.869}$ (v17/v6, $N=120$–$1440$, $R^2=0.973$; window-dependent — $N^{-0.730}$ on $480$–$1440$, §1); the $N\to\infty$ limit is `[HEUR]`. Analytic derivation still open.

---

**OPEN TDR-22c — Steady-state vs. cooling at fixed N** [RID: TDRG-OPEN-STEADY-STATE]

Status: ACTIVE | Diagnostic refinement of TDR-22a  
Question: Does $rN_{\rm late}/rN_T \to 1$ (steady accretion) or $\to 0$ (terminal cooling) at fixed $N$?  
Current state: At $N=120, k=8$: ratio $= 0.473, 0.600, 0.801, 0.894$ at $T = 1000, 2000, 5000, 10000$. Consistent with approach to steady accretion.

---

**OPEN TDR-23 — N-scaling exponent** [RID: TDRG-OPEN-NSCALING]

Status: ACTIVE  
Question: Confirm $B_{\rm bulk}/\text{step} \sim N^{-\alpha}$ for $N > 1440$; identify whether $\alpha \approx 0.869$ is stable or changes regime.  
Current state: `[NUM]` full-range fit ($N=120$–$1440$): $\alpha = 0.869$, $R^2=0.973$; window-dependent ($\alpha\approx0.730$ on $480$–$1440$, §1). Aggregate $\alpha \approx 1$ is tail-inflated and superseded. Stable across the extension from $N=1080$ to $N=1440$.

---

**OPEN TDR-23a — N=480 non-monotonicity** [RID: TDRG-OPEN-N480-NONMONO]

Status: ACTIVE  
Question: Why does $rN_{\rm late}(480) = 0.0054 > rN_{\rm late}(360) = 0.0044$ at $T=5000$?  
Current state: Reproducible at batch=100. $N=720$ gives $rN_{\rm late} = 0.0028$, weakening plateau/floor hypothesis. Possible finite-$N$ resonance or topological fluctuation.

---

**OPEN TDR-24 — Graph-theoretic lower bound on finite-N birth rate** [RID: TDRG-OPEN-BIRTH-LOWER-BOUND]

Status: ACTIVE  
Question: Can one derive $rN_{\rm late}(N) > 0$ for all finite $N$ from defect-graph combinatorics, establishing crystallization as a thermodynamic-limit phenomenon only?

---

### TDR-24 Dependency Chain

$$\boxed{\text{TDR-24D (closed)} \;\to\; \text{TDR-24F (closed)} \;\to\; \text{TDR-24A} \;\to\; \text{TDR-24B} \;\to\; \text{TDR-24C} \;\to\; \text{TDR-T}}$$

TDR-24D and TDR-24F are closed at the mechanism level. TDR-24A current residual: the clean-star supply cap has been decomposed into an N-independent shedding-burst hazard and an N-dependent clean-exposure conditional. The remaining analytic target is to derive $P(\text{clean exposure}\,|\,\text{other-channel burst})\sim N^{-0.6}$ from debris-recapture competition against the multistar absorption zone in the stationary locked measure.

| OPEN | Closure criterion |
|---|---|
| TDR-24D | $\epsilon_{\rm slot}$ machine-small and $\psi_{\rm slot}^{\rm bulk}$ approximately N-independent across the N-scan |
| TDR-24A | Derived or certified scaling law for $C_{\rm component}^{\rm bulk}$ from multistar embedding statistics |
| TDR-24B | Derived or certified scaling law for the clean-star-count collapse $\texttt{clean\_star\_components}/\text{row}\sim N^{-0.73}$ (the $\chi$ denominator; the composite $\chi$ exponent is not a power law — v2.12.1) |
| TDR-24C | Combine A/B/D to show $C_{\rm birth}(N)\to0$ or identify the obstruction |

---

**TDR-24F — Structural-to-slot projection** [RID: TDRG-OPEN-STRUCT-SLOT-PROJECTION]

Status: **RESOLVED (mechanism)** `[NUM strong]` | exponent inconsistency closed  
Question: Why does $\psi_{\rm slot}^{\rm bulk}$ remain intensive (N-independent) across the scan?

Mean-field relation (v6 extractor; $q_{\rm proj} \equiv \bar{c}_{\rm slot}/\bar{c}_{\rm struct}$ by definition):
$$\psi_{\rm slot}^{\rm bulk} = q_{\rm proj} \cdot \frac{\bar{c}_{\rm struct}}{2k+1}, \qquad \bar{c}_{\rm slot} = \frac{\sum_t \texttt{occ\_clean\_pairs}}{\sum_t M_{\rm pre}} = (2k+1)\,\psi_{\rm slot}.$$

**Resolution `[NUM strong]` (two independent methods — v6 per-run output N=120–1080, and pool-level ratio-of-sums on raw v17 logs N=480,840,1200,1440):**

| Quantity | Scaling | Reading |
|---|---|---|
| $\psi_{\rm slot}^{\rm bulk}$ | $\sim N^{+0.01}$ ($R^2\approx0$), value $\in[0.0019,0.0033]$ | **intensive** ✓ |
| $\bar{c}_{\rm struct}$ (unique leaves / component) | $\sim N^{-0.07}$ for $N\ge480$; value $4.5$–$5.0$ | **bounded (N≥480)** ✓ |
| $\bar{c}_{\rm slot}$ | $\sim N^{+1.00}$ ($R^2=0.97$) | $\sim$ band $\sim N$ |
| $q_{\rm proj}$ | $\sim N^{+1.06}$ (both methods: $1.065$, $1.066$) | $\sim N^{1}$ (linear) |

**The reported $q_{\rm proj}\sim N^{+1.371}$ is `[REVISED]` — a convention artifact, not the canonical projection law.** It is reproducible, but only under a *ratio-of-aggregates* convention (dividing pooled $\bar{c}_{\rm slot}$ by the run-mean $\bar{c}_{\rm struct}$) over the full scan including the low-N transient cells. The canonical *run-level* convention (mean of per-run $q$) gives $q_{\rm proj}\sim N^{+1.04}$–$N^{+1.07}$ ($R^2\approx0.99$); the pool-level ratio-of-sums on raw v17 logs gives $N^{+1.066}$. The slot-identity constraint $\exp(q_{\rm proj})+\exp(\bar{c}_{\rm struct})=\exp(\bar{c}_{\rm slot})$ closes with the canonical value: $1.066+(-0.066)=1.000$. **Canonical TDR-24F projection law: $q_{\rm proj}\sim N^{1.0}$.**

**Mechanism (now self-consistent):** the multistar vacuum holds a *bounded* structural leaf reservoir ($\bar{c}_{\rm struct}\approx 4.5$–$5.0$ leaves per component, independent of $N$) while the projection efficiency $q_{\rm proj}\sim(2k+1)\sim N$ scales linearly to exactly offset the widening defect band. The two cancel, leaving $\psi_{\rm slot}^{\rm bulk}=q_{\rm proj}\bar{c}_{\rm struct}/(2k+1)\sim N^{0}$ — the intensive slot density that closes TDR-24D. This is the anatomy of the crystallized vacuum: a fixed-size structural motif tiled at a density that the band-expansion cannot dilute.

**Scope guards (load-bearing):**
- `[NUM]` (finite-N values; boundedness as $N\to\infty$ is `[HEUR]`) $\bar{c}_{\rm struct}$ is bounded **only at high N**: $\approx4.5$–$5.8$ for $N\ge480$. The low-N cells N=120 ($\bar{c}_{\rm struct}\approx12.6$) and N=240 ($\approx7.5$) are finite-size transients and **must not** be used to infer the asymptotic reservoir or to fit projection exponents. Including them is what inflates the ratio-of-aggregates $q_{\rm proj}$ toward 1.3–1.4.
- `[ADMIN]` Raw-motif TDR-24F recomputation must use **run-level** bulk filtering (bulk run $\Leftrightarrow$ final\_M $\le$ tail\_threshold), then aggregate rows. Row-level $M_{\rm pre}\le$ threshold filtering is **not** equivalent: a tail run's early low-$M$ rows leak into the bulk pool. (At clean cells with zero tail runs the two agree; they diverge precisely at N=720-type cells where a locking-failure run exists.)

Remaining `[OPEN]`: an *analytic* derivation of the bound $\bar{c}_{\rm struct}\approx 5$ from $\mathbb{Z}_N$ defect combinatorics (why ~5 and not another constant), and of $q_{\rm proj}\sim(2k+1)$ exactly. The empirical mechanism is settled `[NUM strong]`; the first-principles constants are not.

Audit artifacts: `tdr24f_consistency_audit.py` (exponent algebra), `tdr24f_data_recompute.py` (pool-level recompute from raw v17 logs; run-level bulk filtering).

**OPEN TDR-24A — Topological filtering derivation** [RID: TDRG-OPEN-TOPO-FILTER]

Status: **ACTIVE / mechanism-resolved / analytic residual sharp** | **BLOCKS TDR-T** | Builds on TDR-24D (closed), TDR-24F (closed)  
Question: Derive $C_{\rm component}^{\rm bulk}$ from defect-graph combinatorics and multistar locking.

**`[NUM strong]` Decomposition (v17 bulk, run-level filtered, N=480,840,1200,1440):**
$$C_{\rm component} = \frac{\texttt{occ\_in\_clean\_star}/\text{row}}{\texttt{occ\_clean}/\text{row}} \sim \frac{N^{+0.10}\ (R^2=0.25,\ \text{near-flat})}{N^{+0.945}\ (R^2=0.98)} \sim N^{-0.85}.$$

**Mechanism — geometric dilution:**
- *Denominator* `[ALG candidate]`: the candidate pool is (number of antipodal axes $=N/2$) × (per-axis clean-candidate probability). The per-axis probability is N-independent because window occupancy $\lambda = M(2k+1)/N$ is fixed at fixed $k/N$ with $M$ bounded — verified: per-axis $p \in [0.028, 0.034]$ across $3\times$ in $N$. The pool grows $\sim N$ simply because there are more antipodal axes to scan. This is a clean counting argument.
- *Numerator* `[HEUR strong]`: the supply of birth-producing (genuinely clean, single-center) stars saturates: multistar locking ($f_{\rm ms}\approx1$, ms\_components/row $\sim N^{-0.01}$ flat, cs/(cs+ms) $\approx 0.002$–$0.004$) absorbs hub structure, capping the clean-star count per step at an N-independent level. Mechanism identified; the first-principles N-independence of the cap is **not yet derived** from $\mathbb{Z}_N$ combinatorics.

**`[COR]` The composite exponent is not a true power law.** $C_{\rm component}$ is a ratio of two different N-behaviours, so its apparent exponent drifts with the fitting window: $-0.72$ over $N=120$–$1080$, $-0.85$ over $N=480$–$1440$ ($R^2$ only $0.86$–$0.93$). The canonical "$N^{-0.757}$" is a fitted convenience over a specific range, not a structural constant. Downstream uses (e.g. the dual-suppressor split in §6.8) should treat it as range-tagged.

**`[NUM strong]` Level-1 provenance (clean-star exposure signature; N=480–1440, N-stable):**
- Clean-star rows carry a 7–10× elevated candidate load, almost entirely in the **other** channel (non-star fragments: paths/dyads/irregular, elevated 22–33×), while `multistar_centers_total` is **depleted ~30%** with `multistar_components` unchanged (~1). The locked cluster persists but transiently sheds center mass.
- **Single-step events:** the event-centered ±5-step profile (N=1440) shows the anomaly exists *only at offset 0* (other ×31, centers ×0.71) and vanishes at ±1. Exposure is an instantaneous reorganize-and-snap-back, not an extended episode. (The motif snapshot is pre-birth, so offset 0 is the state that *produced* the star.)
- **Burstiness grows with N:** gap\_mean/(1/rate) falls 0.79→0.41 from N=480 to N=1440 — events increasingly time-clustered.

**`[NUM strong]` Numerator decomposition (closes exactly):**
$$\frac{\texttt{occ\_in\_clean\_star}}{\text{row}} = \underbrace{\text{cs\_rate}}_{\sim N^{-0.669}\ (R^2=0.94)} \times \underbrace{\mathbb{E}[\texttt{occ\_in\_cs}\,|\,\text{event}]}_{\sim N^{+0.766}\ (R^2=0.98)} \sim N^{+0.096}\ \ (\text{measured } {+0.095}\ \checkmark).$$
The "flat numerator" is itself a **compensation**: exposure events become rarer ($\sim N^{-0.67}$) while per-event candidate attachment grows ($\sim N^{+0.77}$, the exposed hub pairing with a band $\sim N$ wide). Structurally analogous to the $q_{\rm proj}\sim(2k+1)$ cancellation in TDR-24F — the locked phase repeatedly exhibits exact band-compensation.

**Mechanism statement `[HEUR strong]`:** clean stars are the fingerprint of single-step partial-unlocking events of the multistar cluster: the cluster sheds ~30% of its center mass into non-star debris for exactly one step, an isolated hub is exposed within the debris, fires (births\_step = 1.000), and the cluster re-locks.

**`[NUM strong]` Rate-law decomposition (TDR-24A-R1/R2):** two conditioning variables tested for cs\_rate $= \Pr(\text{hazard})\times\Pr(\text{cs}\,|\,\text{hazard})$:
- *Center-deficit* $D=\{C_t \le \rho_c\bar{C}_N\}$: **rejected** as the event variable — the exponent split between $P(D)$ and $P(\text{cs}|D)$ is threshold-dependent (slides from $-0.48/-0.19$ at $\rho_c{=}0.70$ to $+0.14/-0.78$ at $0.85$; only the sum $\approx-0.67$ is stable). A decomposition that depends on an arbitrary threshold is not structural.
- *Other-burst* $B=\{O^{\rm other}_t \ge \lambda\bar{O}^{\rm other}_N\}$: **accepted** — threshold-stable across $\lambda\in\{2,5,10\}$:
$$P(B)\sim N^{0}\quad\text{(flat: bursts at }\sim4\text{–}9\%\text{ of steps, all }N,\ \lambda\in\{2,5,10\}\text{)}$$
$$P(B\,|\,\text{clean-star event}) = 0.85\text{–}1.00\quad\text{(coverage, across }\lambda\text{ and }N\text{)}$$
$$P(\text{clean-star event}\,|\,B)\sim N^{-0.58\ldots-0.61}\quad\text{(carries the entire exponent)}$$

**R1 result `[NUM strong]`:** the unlock/shedding hazard is **N-independent**. The locked cluster sheds at a fixed per-step rate at every N. **R2 result `[NUM strong]`:** the N-dependence of clean-star supply lives entirely in the *conditional exposure probability* — whether the shed debris contains a hub that escapes recapture.

**`[NUM]` Successful vs sterile bursts** ($\lambda{=}5$): cs-producing bursts have larger floods ($1.6$–$2.2\times$), stronger center depletion ($0.83\times$), and **3–4× lower multistar candidate absorption** (occ\_in\_multistar ratio $0.26$–$0.31$). The bottleneck is *debris-recapture competition*: a hub is classified clean only if no fragment lands within its defect band.

**R3 `[NUM]`:** per-event attachment $\sim N^{+0.766}$ is **sublinear** vs the band $(2k+1)\sim N$ — *not* the full-band closure of TDR-24F's $q_{\rm proj}\sim N^1$; consistent with partial band exposure during a one-step event. Recorded as a distinct compensation, not assumed identical.

**`[SCOPE — exponent caution]`** $-0.669$ is *near* $-2/3$ (candidate rational, unproven); the conditional's $-0.58\ldots-0.61$ differs from $-2/3$ by more than fit scatter. No rational identification is claimed.

Remaining for full closure `[OPEN]` (final form): derive $P(\text{clean exposure}\,|\,\text{burst})\sim N^{-0.6}$ from the recapture competition between shed debris and the $\sim N$-wide multistar absorption zone in the stationary measure. Level-2 instrumentation (event-local logging) remains optional, needed only for microscopic origin attribution (new-node vs rearrangement), not for the rate law itself.

Artifacts: `tdr24a_decomposition.py`, `tdr24a_provenance.py`, `tdr24a_ratelaw.py`.

---

**OPEN TDR-24B — Pair-to-component compression derivation** [RID: TDRG-OPEN-CHI-SCALING]

Status: ACTIVE | **BLOCKS TDR-T** | Builds on TDR-24D (closed), TDR-24A  
Question (revised v2.12.1): derive the clean-star-count collapse $\texttt{clean\_star\_components}/\text{row}\sim N^{-0.73}$ — *not* the composite $\chi$ exponent, which is not a power law (see below).

**Current status (v2.12.14):** the derivation target is the clean-star-count collapse $\texttt{clean\_star\_components}/\text{row}\sim N^{-0.73}$ ($480$–$1440$ window), which is the per-row form of TDR-24A's clean-star supply cap; $\chi$ is a composite ratio, not an independent scaling field; field count and policy separability are not identifiable on the single-lever corpus and are compute-gated on OPEN-POLICY-GEOMETRY (four new runs). The dated paragraphs below (v2.12.1–v2.12.9) are the supporting record; moving them to Appendix A is v2.13 layout work.

**`[COR]` (v2.12.1) $\chi$ re-fit on v17 corpus (run-level bulk filtering), superseding the v4-era $\chi^{\rm bulk}\sim N^{+0.836}$:**
- $\chi := \texttt{occ\_in\_clean\_star}/\texttt{clean\_star\_components}$ is **not a clean power law** — its apparent exponent is window-dependent: $+0.697$ ($R^2\,0.86$) over $480$–$1440$, $+0.512$ over $720$–$1440$, $+0.866$ over $840$–$1440$. The v4 $+0.836$ is one window's reading of a composite ratio (same failure class as $C_{\rm component}$ and $q_{\rm proj}$).
- **Decomposition `[NUM strong]`:** numerator $\texttt{occ\_in\_clean\_star}/\text{row}\sim N^{-0.03}$ (FLAT, $R^2\,0.00$); denominator $\texttt{clean\_star\_components}/\text{row}\sim N^{-0.73}$ ($R^2\,0.86$). The entire $\chi$ rise comes from the **collapse of the clean-star count per step**, not from per-star occupancy growth (which is flat).
- **Internal consistency — `[ALG]` value-wise identity (given the microscopic birth law) and `[NUM strong]` log-exponent agreement:** the certified factorization $C_{\rm birth}=C_{\rm component}/\chi$ holds **value-wise to machine precision at every $N$** (not as a fit): $C_{\rm component}/\chi = (\texttt{occ\_in\_cs}/\texttt{occ\_clean})\div(\texttt{occ\_in\_cs}/\texttt{clean\_stars}) = \texttt{clean\_stars}/\texttt{occ\_clean}$, which equals $\texttt{births}/\texttt{occ\_clean}=C_{\rm birth}$ exactly because the microscopic birth law $\texttt{births\_step}\!=\!\texttt{clean\_star\_components}$ is certified `[NUM]`. Taking logs, the exponents satisfy $\exp(C_{\rm birth})=\exp(C_{\rm component})-\exp(\chi)=-0.936-(+0.697)=-1.633$, matching the directly-measured $C_{\rm birth}\sim N^{-1.633}$ ($R^2\,0.976$). *(This is a log-space exponent relation of a ratio; it is not a subtraction of the observables themselves.)*
- **Consequence (structural reduction):** $\chi$ is **not an independent scaling field**. With a flat numerator, $\chi$ inherits all scaling from $1/\texttt{clean\_star\_components}$ — it is an amplified inverse of the clean-star-count collapse that TDR-24A already governs. TDR-24B therefore introduces **no new scaling degree of freedom**; its derivation target reduces to the clean-star-count collapse $\texttt{clean\_star\_components}/\text{row}\sim N^{-0.73}$, the per-row form of TDR-24A's clean-star supply cap. The flat numerator is a range-dependent diagnostic, not promoted.

- **`[NUM]` Field-structure test (proposed 3-field basis ρ·σ·κ, tested and rejected):** a review proposed factoring the system into node-availability $\rho\sim N^{-\alpha}$, binding-suppression $\sigma\sim N^{-\beta}$, and geometric fan-out $\kappa\sim N^{+1}$, with the separability test $\chi\cdot\sigma\approx\kappa\sim N^{+1}$. **Tested on v17 bulk: the test fails** — the implied $\kappa=\chi\cdot\sigma$ scales as $N^{-1.03}$, off from $+1$ by two powers. The posited suppression field is also absent: the multistar absorption fraction is **flat** ($N^{-0.02}$), and all three occupancy channels (clean-star, multistar, other) scale identically at $N^{+0.90}$, so the channel split is $N$-independent. **The review's intuition that the clean-star collapse is composite is correct, but the mechanism is the *existing* TDR-24A decomposition, not a new latent:** $\texttt{clean\_star\_components}/\text{row}\equiv$ cs\_rate (clean stars are births, $\le 1$/step), already decomposed in TDR-24A as flat burst-hazard $\times\,P(\text{cs}\,|\,\text{burst})\sim N^{-0.6}$. On this corpus, $\chi$, $C_{\rm component}$, $C_{\rm birth}$ are all quotients of occupancy/row ($\sim N^{+0.90}$) and the clean-star birth rate ($\sim N^{-0.73}$, = TDR-24A residual). Artifact: `tdr24b_field_structure.py`.

- **`[SCOPE — decidability, v2.12.4]` Field count is not resolvable on a $k/N$-fixed family.** Every motif cell in the v17 corpus is at $k/N=1/15$ (single lever $N$). On a one-parameter monotonic family, *every* monotonic observable is trivially a function of one latent ($N$ itself), so "a single latent generator" is unfalsifiable here and carries no physical content; equally, the v2.12.3 phrase "two **independent** inputs" overclaims — occupancy/row and cs\_rate are two *projections* of the single resolvable scaling axis, distinguished only **dynamically** (TDR-24A gives cs\_rate an independent hazard$\times$conditional mechanism), not as separable scaling axes. The reviewer's circular-$\kappa$ diagnosis is confirmed exactly ($\chi\cdot\sigma\equiv(O_{cs}/\text{row})/N$, an identity), and $\sigma$ is flat, so there is **one resolvable scaling axis** on this corpus. **Decisive experiment:** a $k/N$ sweep (e.g. $\{1/30,1/15,1/8\}$). If occupancy/row and cs\_rate share one latent their exponents move together (locked ratio) as $k/N$ varies; if independent they decouple. Not runnable on the current $k/N$-fixed corpus.
- **`[NUM]` Formal rank test (review-directed, executed).** The observable map's resolvable scaling directions $=\min(\text{obs\_rank},\text{control\_rank})$. On the v17 corpus: control manifold **rank 1** (only $\log N$ varies; $\log(k/N)$ constant), so resolvable directions $=1$ **regardless of the true field count** — the design is *rank-deficient*, not merely the inference uncertain (the reviewer's sharper framing, adopted). The centered log-observable matrix itself has apparent rank 3 (singular values $2.18, 0.67, 0.17, \approx0$), but this reflects finite-$N$ scatter and one near-pure-noise channel (occ\_in\_cs/row, residual/total $0.998$), **not** physical structure: with control rank 1 the tool correctly caps resolvable directions at 1 and refuses to read observable scatter as fields. Artifact: `tdr24_observable_rank.py` (returns rank-1 here; ready to report rank $\ge2$ the moment a multi-$k/N$ corpus exists). **Restated frontier:** the meaningful question is not "how many fields" but "does adding the $k/N$ lever raise the observable-Jacobian rank above 1?".
- **`[NUM]` Intrinsic vs apparent dimensionality (review-directed quantification).** Regressing all seven centered log-observables jointly on the single $\log N$ axis explains **88.7%** of total centered variance; the residual $11.3\%$ is finite-$N$ scatter (dominated by $N=840$ and the near-noise occ\_in\_cs/row channel). So the observable cloud is an **overcomplete embedding of a rank-1 ($\log N$) flow**: apparent SVD dimensionality (3) exceeds intrinsic dimensionality (1). This is the precise structural cause of the thread's recurring symptoms — sliding exponents, "composite ratios", and the $\kappa$ sign-flip are all **chart-dependent slopes / non-invariant rescalings of one 1-D trajectory**, not separate fields. **Framing discipline `[SCOPE]`:** these are *identifiability/geometric* statements (one resolvable scaling direction under the current design), **not ontological** ones — "one latent generator" remains unjustified as physics; observable rank $\neq$ latent field count. The $\chi$, $C_{\rm component}$, $C_{\rm birth}$ family is best read as coordinate charts of one flow tangent, i.e. **overparameterized**, not multi-field.
- **`[ADMIN]` Note:** the "thermodynamic crystallization" `[HEUR strong]` claim (§2 TDR-22b, status summary) is a separate, pre-existing $B_{\rm bulk}/\text{step}\to0$ extrapolation and is *not* affected by this rank analysis; the rank-1 finding concerns the scaling-layer observable geometry, not the crystallization limit. The two are independent and neither is upgraded here.
- **`[COR]` (`[NUM]` support from §6.7) k/N is a continuous control, not a phase boundary (review claim tested against §6.7, rejected).** A review proposed that k/N is a *regime-switch / phase-boundary* parameter, making the full design "a foliation of rank-1 manifolds" rather than a smooth rank-2 manifold. The DSN data contradicts this: §6.7 shows $rN_T(k/N)$ is **non-monotone with a smooth peak near $k/N\approx0.05$–$0.0667$**, and the sparse→transition→dense structure is a *continuous* crossover ($p_{\rm frz}\to0$, $p_{\rm strong}\to1$ gradually across the band), not a discontinuity. The genuinely *discrete* selector in TDR-G is the **multistar interaction policy** (`bound_symmetric` / `largest_center` / `all_centers` — crystallization / continuous-inflation / avalanche), which is categorical and which the DSN already separates from k/N: *"k/N selects entry into the growth branch; the multistar interaction axiom selects growth rate and character."* So the correct two-axis picture is **(smooth k/N) × (discrete policy)**, and a k/N sweep at fixed `bound_symmetric` policy *does* probe a smooth rank-2 manifold — exactly the rank-test extension already specified. The review's foliation framing mislocates the discreteness onto the wrong axis; adopted only in the corrected form here.
- **`[SCOPE]` Two-layer reading (adopted, corrected):** Layer A (intra-(N,policy)-slice) — the rank-1 observable geometry of this thread, valid as established. Layer B (across control) — *two* further axes, smooth k/N and discrete policy, neither sampled in the k/N=1/15, `bound_symmetric` corpus. Field-count and regime-classification are Layer-B questions, both blocked on the same unsampled controls.

- **`[DEF]` OPEN-POLICY-GEOMETRY — minimal experimental design specified.** A 10-run matrix separates Layer A (continuous N, k/N) from Layer B (discrete policy): (1) policy-slice at fixed (N=840, k/N=1/15) across `bound_symmetric`/`largest_center`/`all_centers` (amplitude-gap test → DISCRETE-CLEAN vs ENTANGLED); (2) k/N sweep {1/30…1/8} at fixed `bound_symmetric`, repeated at two N (480, 840), giving a 2-D (N,k/N) control so the observable-Jacobian rank becomes meaningful. Pre-registered decision thresholds: Case 1 pure-smooth (k/N-exponents constant ±0.05), Case 2 structural-bending (drift >0.10), Case 3 regime-crossover (piecewise beats power-law). Rank readout: control_rank=2 ⇒ resolvable directions 1 (single latent) or 2 (independent fields) — this is the experiment that finally makes field-count identifiable. Artifacts: `EXPERIMENT_DESIGN.md`, `tdr24_policy_geometry_classify.py` (auto-classifier), reusing `tdr24_observable_rank.py`. **Refinements (review):** (i) goal reframed as a *factorization* test $\mathcal{O}(N,k/N,\pi)\stackrel{?}{=}f(N,k/N)g(\pi)$ under an operator formulation (permits policy↔geometry coupling) rather than a presupposed Layer-A/B independence; Experiment 1 now tests multiplicativity (Case A separable / B partial / C full entanglement), not "independence". (ii) Cross-N normalization anchor (Experiment 0) added — and it is the **existing canonical scan** (N=480–1440 at k/N=1/15, bound\_symmetric), so it adds **zero** new runs; the classifier reports its N-exponents live (C\_birth $N^{-1.633}$, χ $N^{+0.697}$, B/step $N^{-0.730}$, O/step $N^{+0.903}$). **New runs reduced 10→4** (2 policy + 2 k/N-sweep). **Compute-gated** on those 4. Scope guard: no further fitting/basis-reduction/rank-tests on the existing single-slice corpus (information-saturated).

- **`[BRANCH — TDRG-RESPONSE-TENSOR]` Response-tensor formalism (exploratory, firewalled).** Per PI directive, an isolated branch tests whether TDR-G observables are projections of one response tensor whose intrinsic dimension is *read from data*, never imposed. **Governing axiom:** intrinsic dimension = rank of the *unnormalized* response tensor over the full control manifold; normalizations/factorizations/quotients are post-hoc diagnostics only, never the primary rank test (the premature-quotienting guard — a baseline division assumes reducibility and forces rank collapse). **Two-sided discipline:** do not impose dimensions, but do not suppress dimensions the math requires; a rising count is allowed *if* it clears a null-model ceiling (so genuine structure is distinguished from finite-sample noise), and merges are tracked as consolidations, not deletions. **Build status:** module `response_tensor.py` with a null-gated SVD dimension reader, validated on synthetic data. **Calibration (honest limitation):** reliable for dim ≤ 1 at any cell count; dim ≥ 2 is *under-counted* (returns a lower bound) below ~40 control cells; pure noise is not inflated (conservative failure direction). On the current single-lever corpus it reports **intrinsic dimension = 1, HIGH confidence, upper-bounded by control rank** — consistent with the v2.12.5–.7 rank-1 finding (charter consistency criterion (b) met). Resolving dimension > 1, if present, requires the multi-cell (N × k/N × policy) grid. **Firewall:** all outputs `[NUM]` `[scope: branch diagnostic]`; nothing promotes to canonical TDR-G without PI approval against the charter success criteria. Artifacts: `tdrg_response_tensor/BRANCH_CHARTER.md`, `response_tensor.py`.
- **`[NUM]` `[scope: exploratory branch TDRG-RESPONSE-TENSOR; diagnostic]` Dynamical signal layer added (Zeta geometry-saturation response).** Motivated by the Zeta finding that the static angular spectrum is geometry-saturated, `dynamical_extractor.py` adds a SEPARATE trajectory-level layer (autocorrelation times, Fano burstiness, inter-birth-interval CV, birth↔occupancy lagged cross-correlation), kept strictly out of the static exponent pipeline (no recompression). **Key test — does dynamical rank exceed static rank?** On the single-lever corpus: static dim = 1, dynamical dim = 1 — **no extra temporal degree of freedom surfaces.** Caveats keeping this from being a resolution: (i) both control-rank-capped at 1 lever (lower-bound check, not resolution; F3 observable-collapse neither confirmed nor refuted); (ii) the dynamical leading direction is weak and nearly single-feature — dominated by inter-birth-interval CV (slope +0.39, R²0.81), other features flat-to-weak, leading singular value (0.449) barely above null ceiling (0.432). **`[COR]` Inference corrected (review):** the earlier "dynamical summaries also near-saturated / weakly argues against F3" was an inference error and is retracted. On a rank-1 control manifold BOTH layers are forced to rank ≤ 1 *regardless of true dimension*, so static-dim = dynamical-dim = 1 is guaranteed by the geometry and concludes nothing about F3 or about hidden structure. Correct statement: both layers collapse to a rank-1 response under a rank-1 control manifold — an **excitation-insufficiency** result, not a structural one. Second limitation: these features (CV, Fano, autocorr) are compressed many-to-one statistics of path space, not trajectory embeddings, so the layer tests rank(feature_summary), not rank(trajectory_manifold); feature-map injectivity is unverified. The one finding that **does** survive (not a dimension claim): inter-birth-interval CV carries genuine N-dependence (slope +0.39, R²0.81) while autocorrelation times are flat — a statement about which trajectory features respond to N under the applied excitation. CV is the highest-value dynamical observable for the grid.
- **`[NUM]` `[scope: exploratory branch TDRG-RESPONSE-TENSOR; diagnostic]` Feature-map injectivity tested on existing data (review-directed; no grid).** The review held that scalar summaries are compressive and a richer trajectory embedding might extract lost structure — an intra-run question, testable now. Tested three embeddings (N=840): cross-channel increment covariance = rank 1 (all runs); cross-channel level covariance = rank 1 (all runs); single-channel delay embedding gave a spurious "rank 8" on births that was a sparse-series artifact (births rare: median 11 events/4000 steps), **caught by a shuffle null**. Proper null-tested memory on the occupancy channel: real effective rank 7.63 vs shuffled 7.99, gap 0.37 (below 0.5 threshold) — only marginal memory beyond marginals. **Conclusion:** feature non-injectivity is real in principle but hides no extractable structure here; richer embeddings recover no temporal DOF the scalar summaries miss. This removes "improve feature injectivity" from the no-grid lever list — tried, corpus does not reward it. The trajectory process is genuinely low-complexity on this slice (one shared cross-channel mode, near-white residual memory). Artifact: `dynamical_extractor.py`.
- **`[METHOD]` Standing note (adopted from review):** recurring exponent drift (χ, $C_{\rm component}$, $q_{\rm proj}$) arises because most reported exponents are quotients of a few underlying fields; before promoting any exponent, test whether it is a primitive or a ratio of primitives.
- Artifact: `tdr24b_chi_refit.py`. N=840 (7-divisible control) is mildly off-trend but not the source of the window dependence (excluding it: $+0.693$ vs $+0.697$).

---

**OPEN TDR-24C — Thermodynamic suppression via factorization** [RID: TDRG-OPEN-THERMO-SUPPRESS]

Status: ACTIVE | Requires TDR-24F, TDR-24A, TDR-24B  
Question: Does $C_{\rm birth}(N) \to 0$ as $N \to \infty$ at fixed $k/N$, using $C_{\rm birth} = C_{\rm component}/\chi$?  
Extension: Combine with TDR-24D to determine whether $B_{\rm bulk}/\text{step} = O_{\rm bulk}/\text{step} \cdot C_{\rm birth} \to 0$.

---

**OPEN TDR-24N — Finite-size neighborhood anomaly audit** [RID: TDRG-OPEN-FINITESIZE-AUDIT]

Status: ACTIVE  
Question: Systematic audit of $N = 718$–$1440$ neighborhood for arithmetic-driven anomalies. Current arithmetic controls (divisor count, $3$-power, 15-commensurability) are all `[FAIL]` as explanations for the $N=720$ tail.

Required cells:

| $N$ | $k$ | Status | Result |
|---:|---:|---|---|
| 718 | 48 | batch=100 done ✓ | $p_{>500}=0$ |
| 720 | 48 | batch=100 (v17) / batch=200 (legacy) ✓ | $p_{>500}\approx0.005$–$0.01$; locking-failure run |
| 722 | 48 | batch=100 done ✓ | $p_{>500}=0.01$; matching locking-failure run |
| 840 | 56 | batch=100 done ✓ | $p_{>500}=0$; 7-divisible control clean |
| 960 | 64 | batch=100 done ✓ | $p_{>500}=0$ |
| 1200 | 80 | batch=50 done ✓ | $p_{>500}=0$ |
| 1440 | 96 | batch=50 done ✓ | $p_{>500}=0$ |

`[NUM]` **Result:** The required N=718–1440 grid is complete. A matching rare locking-failure tail appears at **both** N=720 and N=722, confirming the tail is a stochastic local-neighborhood phenomenon, not an N=720-only or deterministic-arithmetic effect. The 7-divisible control N=840 is clean, driving the final stake through the deterministic arithmetic-factor hypothesis.

---

**OPEN TDR-25 — Tail probability law** [RID: TDRG-OPEN-TAIL-LAW]

Status: ACTIVE (**bridge to TDR-24A established; burst-quantile model rejected; basin-selection hypothesis posed**)  
Question: Derive or characterize $p_{\rm tail}(N, k)$ — the probability of a runaway high-growth event.  
Current state: Rare locking-failure tails observed at $N=720$ ($1/100$ v17, final_M$\approx$3187, $C_{\rm component}\approx0.782$) **and** $N=722$ ($1/100$, final_M$\approx$2904, $C_{\rm component}\approx0.812$). N=718 and N=840 clean ($0/100$). The tail is a stochastic neighborhood phenomenon, not N=720-singular. Mechanism: topological filtering failure ($C_{\rm component}$ jumps ~100×).

**`[NUM strong]` Burst-quantile bridge, part 1 (clean cells N=480–1440):** tested whether runaways are extreme quantiles of the TDR-24A shedding distribution.
- *One N-stable shedding family:* normalized burst-size survival curves collapse across N (e.g. $P(O^{\rm other}\!\ge\!10\bar{O})=4.3$–$4.5\%$ at every N). The distribution **truncates sharply**: max observed burst $42$–$55\times\bar{O}$, $P(\ge 50\times)\sim6\times10^{-5}$ — no heavy tail in clean cells.
- *Monotone unlock gradient:* with burst size, births/row rises $0\to0.39$–$0.41$, centers fall $53\to29$–$35$, and frac\_cs rises $0\to0.042$–$0.045$ across bands up to $[30,100)\times\bar{O}$. Extreme bursts are genuinely "more unlocked".
- *But the gradient does not reach the runaway:* top-band frac\_cs $\le0.05$ vs runaway $C_{\rm component}\approx0.78$–$0.81$ — a $\sim$16–20× compositional gap. Within-range extrapolation (frac\_cs $\sim$ size$^{1.7}$) would require bursts $\sim300\times\bar{O}$, $\sim6\times$ beyond the observed truncation.

**`[REVISED]` v2.8 failed-relock hypothesis (historical; superseded by part 2 below):** the runaway is *not* an anomalously large single-step burst but an **ordinary-scale burst whose one-step snap-back fails** (cf. TDR-24A provenance: locked-phase anomalies are strictly single-step). Persistent re-lock failure lets clean-star production compound *across* steps instead of resolving within one.

**`[NUM strong]` Bridge part 2 — N=720 onset test (executed; prediction outcome mixed):**
- *Mega-burst falsifier NEGATIVE (as predicted):* r43's maximum burst is $26.95\times\bar{O}$ — **smaller than the bulk's own maximum** ($43.8\times$). Zero r43 rows $\ge30\times$, $\ge50\times$, or $\ge100\times$. The N=720 bulk itself sits exactly in the clean-cell shedding family ($P(\ge10\times)=0.0435$, max $43.8\times$). `[REJ]` single-step burst-size quantile explanation of the runaway: **burst size is not the control variable.**
- *But the v2.8 failed-relock framing was too late-stage* `[REVISED]`: r43 does not behave like a mature locked run suffering one failed snap-back. Window-resolved trajectories show r43 in the clean-star-producing mode **from the first window** (cs-frac $0.72$ at steps 1–100 vs bulk $0.19$) and *never converging*: ms-absorption stays pinned at $\approx0.10$ for all 5000 steps while bulk climbs to $0.734$. Late r43 oscillates (birth rows: centers$=0$, one clean star, one birth; non-birth rows briefly re-form multistars — center count even grows to $\sim113$/row) but multistar absorption never dominates.

**`[HEUR strong]` Revised mechanism — early lock-nonengagement / relock-defective attractor:** the bifurcation is whether a run *enters and maintains* the multistar-locked absorbing basin during early growth, not the magnitude of any later burst. r43 entered the clean-star-producing basin in the pre-lock transient and persisted there.

**`[ADMIN — tooling]`** the unguarded onset detector (frac\_cs$>0.2$) fires on the pre-lock transient (r43: step 9, $M{=}4$). Guards added: `--onset-min-M`, `--onset-min-step`. Guarded onsets: step 122 ($M\ge50$, max nearby burst $13\times$), step 812 ($M\ge500$, max nearby burst $\approx10$–$12\times$) — already in high-clean-star mode at both, no preceding mega-burst.

---

**OPEN TDR-26 — Basin-selection / lock-engagement problem** [RID: TDRG-OPEN-LOCKING-FAIL]

Status: ACTIVE (**reframed by the N=720 part-2 result**)  
Question (revised): Derive or bound the probability that a run **fails to enter the stable multistar-locked absorbing basin during early growth** — i.e. characterize basin selection in the pre-lock transient, replacing the "extreme burst tail" model for r43-type runaways.

`[NUM]` Established constraints: r43 was in the clean-star-producing basin from steps 1–100 (cs-frac 0.72 vs bulk 0.19) and never converged over 5000 steps (ms-absorption pinned at ~0.110 vs bulk 0.734), despite multistar components forming and the center count growing to ~113/row. The defective basin is *persistent and oscillatory*, not centerless: multistars exist but never capture absorption dominance.

**`[NUM strong]` Early-basin discriminator study (sub-question (a), executed on N=720 v17; r43 vs 99 bulk runs):**
- *Timeline of separability:* at $w{\le}50$ r43 is **not** separable (cs\_frac $z{=}1.4$, rank 12/99). At $w{\le}100$ r43 is already an extreme outlier by z-score ($z{\approx}3.1$–$3.2$ on cs\_frac and b/step) but **still not separated — rank-2 in both raw metrics**: r48 exceeds it on cs\_frac ($0.867$ vs $0.715$) and r3 exceeds it on b/step ($0.420$ vs $0.350$). Clean separation appears only at $w{\le}200$. At $w{\le}200$: **clean gap** on b/step (r43 $=0.490$ vs bulk max $0.250$, $1.96\times$ margin), widening to $2.75\times$ at $w{\le}300$.
- *cs\_frac alone is NOT the discriminator* `[COR — important]`: several bulk runs show high early cs\_frac on few candidates (idle pre-lock noise; r48/r90/r92 at $0.70$–$0.87$) and all engage the lock by $w{=}200$ (ms\_abs $\to0.41$–$0.47$). The defective run differs in **sustained production**: its b/step *rises* ($0.35\to0.49\to0.55$) while every contender's collapses.
- *Absolute-step candidate rule* `[FAIL — cross-cell]`: at $w{=}200$ (absolute), b/step $\ge0.30$ ∧ ms\_abs $\le0.25$ gave TP=1/FP=0 on N=720 but **failed on N=722** (TP=0, FN=1): the N=722 tail run r31 was **dormant for 433 steps** ($M{=}4$, zero occupancy — four mutually non-interacting initial nodes), so absolute windows read zeros.

**`[NUM strong]` N=722 cross-cell test — second entry route, same attractor:** r31 woke at step 434 with its *first interaction being a clean-star birth* and entered the **identical defective attractor** (late cs $0.812$, ms-abs $0.090$, b/row $0.652$ vs r43's $0.782/0.110/0.633$) with no locked phase ever forming. Two defective runs sit at *opposite extremes* of first-birth timing (r43: step 9, earlier than 92/99 bulk; r31: step 434, later than 97/99) — `[REJ]` dormancy duration as a discriminator. Also `[REJ]` birth-before-first-multistar (universal: all 198 bulk runs birth first too).

- **Birth-anchored rule (canonical clock):** over $[\mathrm{fb}, \mathrm{fb}{+}200)$ where fb $=$ first-birth step: b/step $\ge0.30$ ∧ ms\_abs $\le0.25$. Tag split: the **dataset fact** is `[NUM cross-cell, n=2]` (both known defective runs satisfy the rule; all 198 known bulk runs fail it); the **classifier claim** (out-of-sample validity) remains `[HEUR]` pending batch-scale validation.
  - N=720: TP=1/FP=0/TN=99 (tail $0.520/0.120$; bulk max b/step $0.265$)
  - N=722: TP=1/FP=0/TN=99 (tail $0.660/0.092$; bulk max b/step $0.240$)
  - **Combined: TP=2, FP=0, FN=0, TN=198** — $\ge2\times$ clean margin at both cells. `[scope: thresholds chosen on n=1, survived n=2; still requires batch-scale validation]`
- *Mechanism refinement:* basin selection is decided within $\sim$200 steps **of first birth**, not of absolute time — dormancy shifts the clock but not the bifurcation. The defective attractor is reachable both from a hyperactive start (r43) and from prolonged dormancy (r31); the common signature is *sustained post-birth production with multistar absorption never establishing*.

`[DEF]` **Next campaign spec (validated-classifier path):** N=720 and 722, batch $\ge500$, motif logging dense up to first-birth$+300$ (normal stride after), expected $\sim5$ defective runs per cell; validate the birth-anchored rule out-of-sample and measure the basin-entry probability directly.

`[OPEN]` Remaining sub-questions: (b) is the basin choice a finite-time decision (suggesting $p_{\rm tail}$ ~ constant per run, consistent with ~1/100 at N=720/722); (c) why the N≈720 neighborhood biases the pre-lock transient without deterministic forcing (all deterministic arithmetic explanations remain `[FAIL]`, §6.9).
---

Settled / routed items (one-line):

- **OPEN TDR-0** :: `[HEUR]` — Interaction interpreted as failed null-return + bounded distinguishability + thresholded debt release. Motivational status only; routed to TDR-1 for derivation. *(v2.12 note: the "failed null-return" component is now theorem-grade — LEM-NOANNIHIL, §6.5.)*
- **Holonomy closed** :: `[THM]` ✓ — $\Delta_{AB}+\Delta_{BC}+\Delta_{CA}\equiv 0$. See §6.1.
- **Narrow-band exclusion closed** :: `[THM]` ✓ — $k<N/6 \Rightarrow |E_{\rm def}\cap K_3|\le2$. See §6.2.
- **Finite-state recurrence closed** :: `[THM]` ✓ — Every orbit of $G_{\rm perm}^{(M)}$ is eventually periodic. See §6.2.
- **Birth-rate invariant closed** :: `[ALG]` ✓ — $rN_{\rm err}=0$ in all clean runs. See §6.3.
- **TDR-24 factorization closed** :: `[ALG]` (given the microscopic birth law; numerically corroborated) ✓ — $C_{\rm birth}=C_{\rm component}/\chi$. See §6.4.
- **Microscopic birth law closed** :: `[NUM]` ✓ — `births_step` $=$ `clean_star_components`. See §6.4.
- **Slot-volume identity closed (TDR-24D)** :: `[ALG]` identity; `[NUM strong]` intensiveness ✓ — $O_t = (2k+1) M_t \psi_t$ verified by v6 extractor; $\psi_{\rm slot}^{\rm bulk} \approx 0.00204 \cdot N^{+0.014}$ is scale-invariant. Analytic derivation of the intensiveness routed to TDR-24F. See §6.8.
- **(v2.12) LEM-REACH / LEM-NOANNIHIL / LEM-RETRIG / LEM-SPECCONS closed** :: `[ALG]` ✓ — band reachability, no free annihilation, two-node binding threshold, advance-spectrum conservation. See §6.5, §6.12.
- **(v2.12) BIND3-CYCLE-N24K1 certified** :: `[ALG]` (finite exact enumeration; `[conv: v18 path orientation]`) ✓ — exact taxonomy {scatter 96.4%, pure-bound 3.6%, transfer 81.8%}. See §6.12.

---

**OPEN-BIND3-PARITY-GEN — General spectator-lattice avoidance** [RID: TDRG-OPEN-BIND3-PARITY]

Status: ACTIVE | Substantially resolved at $N=24$, $k\in\{1,2\}$  
Question: Derive the general $(N,k,d)$ condition under which a third node's relative orbit-lattice avoids the defect arc of a bound dyad. Expected structure: lattice spacing and alignment versus arc width $(2k+1)$.  
Current state: odd-$d$ impossibility `[ALG]` at $N=24$ (spacing-$\{1,3\}$ lattices cannot avoid a 3-or-5-point arc); even-$d$ survivor classes characterized (co-moving $\delta_C=d/2$ frames + wide-sublattice cosets) `[NUM strong]`; $k=2$ falsification target executed and passed (zero odd survivors; deep even class populated). Remaining: full sufficiency characterization including both tick-parity offsets and the second-spectator constraint; generalization beyond $N=24$ (note $3\nmid$-structure caveats).

---

**OPEN-BIND3-MEMORY — Residence-time mechanism** [RID: TDRG-OPEN-BIND3-MEMORY]

Status: ACTIVE  
Question: Explain the persistent occupancy bias toward an initially bound **even-advance** pair in recurrent scattering cycles (BIND3-MEMORY-PARITY, §6.12), as residence-time dynamics on the conserved spectrum: how long does each pair hold each spacing between reassignment events, and why does parity protect residence?  
Constraint: any proposed mechanism must also reproduce the **absence** of bias in odd-advance classes and in non-binding-entry controls.

---

**OPEN-BIND3-REGEN — $P_3$ lattice-action theorem** [RID: TDRG-OPEN-BIND3-REGEN]

Status: ACTIVE | Spectral criterion certified  
Question: Derive the action of the $P_3$ successor-shift on the triple of pairwise orbit-lattices and characterize when reassignment creates a band-reaching or retrigger-compatible pair.  
Current state: the conservation backbone is `[ALG]` (LEM-SPECCONS); the gate consequence is certified `[NUM strong]` at $N=24$, $k=1$ (BIND3-SPECTRAL-GATE: spectrum all-above-$2k$ ⇒ zero autonomous retrigger; detector-sane). Remaining: which *orderings* of reassignment occur dynamically (the transfer graph of §6.12 as a derived object), and the residence-time link to OPEN-BIND3-MEMORY.

---

**OPEN-BIND3-NKSCAN — Stratified parameter scan** [RID: TDRG-OPEN-BIND3-NKSCAN]

Status: ACTIVE | Three pre-registered targets executed in v2.12  
Question: Run the $(N,k)$ scan of BIND3 class fractions stratified by $d$, $\gcd(d,N)$, $|d|_c/(2k)$, and conserved-spectrum class, tracking even/odd parity sectors separately.  
Executed targets: (1) $k=2$ parity prediction — PASS (BIND3-PARITY); (2) spectral criterion on the one-pass family — PASS (BIND3-SPECTRAL-GATE); (3) memory stratification — partial demotion with structure (BIND3-MEMORY-PARITY).  
Remaining targets: $N$-dependence of class fractions and the even-sector memory amplitude; the marginal class $|d|_c=2k$ tracked separately; **no extrapolation across star blow-up** (SG-12).

---

**OPEN-SPECCONS-STAR — Spectrum across birth** [RID: TDRG-OPEN-SPECCONS-STAR]

Status: ACTIVE | Theoretically loaded  
Question: Does star blow-up conserve, controllably extend, or break the relational advance spectrum? The birth creates $\theta_E=(\theta_A+N/2)$, $\delta_E=\delta_A$ with center inversion $\delta_A\mapsto-\delta_A$, adding new pairwise advances and modifying existing ones non-permutationally.  
Stakes: a controlled extension law would be a candidate exact invariant of full TDR-G dynamics; a characterized breaking law would quantify what births physically inject. Connects to TDR-24A. Either outcome is valuable; neither is assumed (SG-12).

---

## §3. Scope Guards {#sec-3-scope-guards}

**[SG-1]** No continuous space/time assumed. All $\theta_i, \delta_i \in \mathbb{Z}_N$.  
Violation: Treating phase variables as real-valued without discretization proof.

**[SG-2]** Absolute phase is gauge. Only relational differences $\Delta_{ij}$ are physical.  
Violation: Assigning physical meaning to absolute $\theta_i$ values.

**[SG-3]** Total additive momentum $P = \sum \delta_i$ is not a physical observable.  
Violation: Using $P$-conservation as a constraint on interaction rules. ($P$ is gauge-like; $P$ changes under birth.)

**[SG-4]** $N$ must be even. Required for a unique antipode at $N/2$.  
Violation: Running with odd $N$.

**[SG-5]** Narrow-band condition: $k < N/6$ is required for the holonomy exclusion theorem to forbid fully defective $K_3$. All canonical simulation branches use this condition.  
Violation: Importing results from $k \geq N/6$ runs without explicit qualification.

**[SG-6]** All numerical claims are finite-horizon unless explicitly stated. No infinite-$N$ or infinite-$T$ claim is made from finite runs.  
Violation: Asserting thermodynamic crystallization as fact rather than `[HEUR strong]`.

**[SG-7]** Policy choice is physically real. `bound_symmetric`, `largest_center`, and `all_centers` define distinct physical universes, not implementation variants. Results from one policy do not transfer to another.  
Violation: Treating policy as a numerical parameter to be optimized.

**[SG-8]** `bound_symmetric` is the canonical clean branch by convention and empirical certification, not by derivation from first principles. See OPEN TDR-19.  
Violation: Claiming `bound_symmetric` is uniquely selected by the ontology.

**[SG-9]** CLI provenance matters. Runs before the v13 CLI patch (which added `argparse`) may have silently ignored `--N`, `--k`, `--T`, `--batch`, `--max-nodes`. Pre-patch results are invalid for N-scaling claims.  
Violation: Including pre-v13 data in N-scaling fits without labeling them as suspect.

**[SG-10]** Cross-branch firewall (Programme-level SG-PROG-1 applies). No result from the continuous RTG programme (dyadic, triadic, Genesis) may be imported into TDR-G without a named bridge theorem tagged `[ALG]` or stronger. Sine coupling, continuous coordinates, $P_{\rm floor}$, and fixed-motif $K_3/K_4$ structures are `[FAIL]` as TDR-G primitives. Conversely, TDR-G coefficients must not flow to the continuous $\Phi_{2\to3}$ bridge without an explicit asymptotic limit derivation.  
Violation: Any unbridged cross-branch import. See Programme Overview §3.2.

**[SG-11]** *(v2.12)* **Pairwise bound-state scope.** The isolated period-2 dyad (LEM-RETRIG) is exact only in the two-node universe. In the full TDR-G universe, defect-component classification takes precedence over pairwise continuation: a third node can convert a bound edge into a path, star, multistar/tie, transfer bond ownership, or generate recurrent scattering. Pairwise bond survival is not a primitive invariant. The LEM-RETRIG threshold $|d|_c\le2k$ bounds only pairwise-autonomous binding; it does not bound binding regeneration or recurrent in-band occupancy in $N\ge3$ systems (BIND3-REGEN).  
Violation: Citing two-node bound-state results as $N\ge3$ persistence claims, or using $|d|_c>2k$ to exclude in-band activity in multi-node systems.

**[SG-12]** *(v2.12)* **Spectrum-conservation star firewall.** LEM-SPECCONS is certified for three-node, no-birth dynamics under canonical swap and $P_3$ events. Star blow-up creates a new node and new pairwise advances; spectrum conservation (or any controlled extension) across star blow-up is `[OPEN]` and must not be assumed.  
Violation: Extrapolating advance-spectrum conservation across birth events without a separate certificate.

**[SG-13]** *(v2.12)* **Spectral-gate scope.** BIND3-SPECTRAL-GATE forbids autonomous two-node period-2 retrigger, **not** transient in-band occupancy (any pair can be swept through the band by LEM-REACH regardless of $|d|_c$). It is scoped to no-birth three-node dynamics.  
Violation: Reading the gate as a ban on band entry, or applying it across births.

**[SG-14]** *(v2.12.14)* **Relabelling covariance.** On the canonical branch `bound_symmetric` — and on any other policy branch only once its covariance is separately established — the TDR-G step must commute with $G_{\rm cov}=\mathrm{Sym}(V)\times\mathbb{Z}_N^{\rm phase}$: every permutation of node labels (path-listing reversal included) together with the global phase shift $\theta_i\mapsto\theta_i+c$ (SG-2). Equality of the two sides is understood **modulo a relabelling of freshly born nodes**: a newborn node has no prior label, so the outputs are compared after a one-to-one matching of the newborn nodes (as a multiset of $(\theta,\delta)$), as the checks of §6.12 do. Tie conditions are declared on $G_{\rm cov}$-invariant data only; a rule that consults node IDs, listing order or creation order is an implementation presentation, not a law (Appendix B). **Not in $G_{\rm cov}$:** (i) the common token shift $\delta_i\mapsto\delta_i+c$ — it commutes with swaps, path successor shifts and ties and is broken by star blow-up unless $2c\equiv0$ (imported OFN statement, §7); it is a symmetry of the birth-free sector only, not a gauge; (ii) the mirror $(\theta,\delta)\mapsto(-\theta,-\delta)$ — the step is not mirror-equivariant at $P_3$ events (TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY, §6.12). **Branch scope and evidence:** for `bound_symmetric` the finite checks of §6.12 (TDRG-NUM-ORIENT-EQUIVARIANCE-N24) support SG-14 on their tested scope; they are not a theorem for all $N$ or all policies. `trap`, `bound_multistar` and `bound_path_tie` differ from `bound_symmetric` only in bookkeeping on ties and multistars (§6.3, dynamic equivalence). In `largest_center` the choice between equal-degree multistar centres is by node ID (TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK, §6.6), so that branch does not satisfy SG-14 — a recorded non-covariance of a non-canonical branch, to be resolved with TDR-19. `all_centers` is equivariant modulo the relabelling of newborn nodes on the tested fixture (§6.6).  
Violation: an event rule or tie-break that depends on node labels; reading the common token shift or the mirror as a gauge; citing SG-14 for a policy branch whose covariance has not been established.

---

## §4. Layer Routing {#sec-4-layer-routing}

$$\text{G0: phase topology} \;\to\; \text{G1: relational kinematics} \;\to\; \text{G2: defect geometry} \;\to\; \text{G3: interaction law} \;\to\; \text{G4: policy fork} \;\to\; \text{G5: observables}$$

| Layer | Object | Canonical tool |
|---|---|---|
| G0 | Finite phase universe | $\mathbb{Z}_N$, $N \in 2\mathbb{Z}$ |
| G1 | Relational state | $\Delta_{ij}$, $d_{ij}$, holonomy |
| G2 | Defect geometry | Antipodal band $\mathcal{D}_k$ |
| G3 | Interaction law | Swap, path-cycle, bound cycle, star blow-up |
| G4 | Policy fork | Multistar / tie treatment |
| G5 | Observables | $rN_T$, $rN_{\rm late}$, $mf$, quantiles, tails, multistar counts, motif rates |

Routing rules:
- G5 observable results do not certify G3 interaction law claims without a combinatorial bridge.
- G4 policy results are branch-specific; cross-policy comparisons require the explicit cap-protocol qualification.
- G2 defect-geometry theorems (holonomy, narrow-band exclusion) hold at all policy branches.
- No G-layer object imports from the continuous RTG programme without SG-10 bridge clearance.

<!-- AI_CONTEXT_CORE_END -->

---

## §5. High-Risk Claims Ledger {#sec-5-high-risk}

| Claim | Valid form | Forbidden overclaim | Section |
|---|---|---|---|
| N-scaling exponent | $B_{\rm bulk}/\text{step} \sim N^{-0.869}$ `[NUM]`, full-range composite fit, bulk-conditioned, $k/N=1/15$, $T=5000$, $N=120$–$1440$; window-dependent ($N^{-0.730}$ on $480$–$1440$) | Aggregate exponent $\alpha \approx 1$ as primary (tail-contaminated); $0.869$ as a structural or $N\to\infty$ exponent | §1, §6.8 |
| Thermodynamic crystallization | `[HEUR]` extrapolation of finite-$N$ fits; requires the $N\to\infty$ limit | Established theorem | §2 TDR-22b |
| `bound_symmetric` as canonical | Clean background-independent certified branch | Uniquely derived from first principles | §3 SG-8 |
| TDR-24 factorization | Pool-level identity `[ALG]` (given the microscopic birth law), verified to machine precision | Individual-run per-step factorization (not tested) | §6.4 |
| Microscopic birth law | `births_step = clean_star_components` under `bound_symmetric` `[NUM]` | Any other policy | §6.4 |
| Slot-volume model | Identity `[ALG]` (by construction); $\psi_{\rm slot}^{\rm bulk}$ N-independent `[NUM strong]` | Analytic derivation of $\psi_t$ intensiveness (the TDR-24F mechanism is closed numerically; its analytic constants are OPEN) | §6.8 |
| $V_{\rm pair\_load}$ | Load/multiplicity diagnostic; may exceed 1 `[NUM]` | Interpreting it as a probability or fraction | §6.10 |
| TDR-24F projection $q_{\rm proj}$ | $q_{\rm proj}\sim N^{1.06}$, $\bar{c}_{\rm struct}\approx5$ bounded, $\psi$ intensive `[NUM strong]` | Citing $q_{\rm proj}\sim N^{1.371}$ (fit artifact, refuted by two methods) | §2 TDR-24F |
| Policy ordering | `largest_center` > `all_centers` > `bound_symmetric` at $k/N \approx 0.0667$ under cap protocol `[NUM]` | Universal ordering at all $(N, k)$ | §6.6 |
| N=720 tail mechanism | Topological filtering failure (one event in 200 runs) `[NUM]` | Deterministic instability | §6.9 |
| $K_3$ global explosiveness | Historical continuous reference only: TRIAD v1.6.1 keeps the 96:1 healing/pump ratio as coefficient bookkeeping with the same-object correspondence `[OPEN]`; not a current fact about either branch | Importing continuous $K_3$ explosiveness or 96:1 language into TDR-G | Appendix B |
| Two-node retrigger | Exact isolated retrigger result under LEM-RETRIG (period dividing 2; fixed point at $d=0$) | Persistent pairwise bond in $N\ge3$ | §6.5, SG-11 |
| Spectral gate | Gates autonomous two-node retrigger in no-birth three-node dynamics | Forbids transient in-band occupancy or applies across births | §6.12, SG-13 |
| Advance-spectrum conservation | Exact for three-node no-birth swap/$P_3$/tie dynamics | Conserved across star blow-up | §6.12, SG-12 |

---

## §6. Main Scientific Ledger {#sec-6-ledger}

### §6.1 Primitive State and Relational Structure `[DEF]` {#sec-6-1-state}

`[DEF]` [RID: TDRG-DEF-ZN-STATE] **Phase universe.** $\mathbb{Z}_N$ with $N$ even. State is variable-size: $X_n \in \bigsqcup_{M\ge2}\mathbb{Z}_N^{2M}$, with nodes carrying phases $\theta_i \in \mathbb{Z}_N$ and velocity tokens $\delta_i \in \mathbb{Z}_N$. $M_n$ increases at each star blow-up.

`[DEF]` [RID: TDRG-DEF-PHYSICAL-STATE] **Physical state** is the quotient by global phase shift: $\theta_i \mapsto \theta_i + c$. Only $\Delta_{ij} = (\theta_i - \theta_j) \bmod N$ are physical.

`[DEF]` [RID: TDRG-DEF-REL-ADVANCE] **Relative advance:** $d_{ij} = (\delta_i - \delta_j) \bmod N$.

`[DEF]` [RID: TDRG-DEF-KINEMATICS] **Kinematic evolution:** $\Delta_{ij,n+1} = (\Delta_{ij,n} + d_{ij,n}) \bmod N$.

`[DEF]` [RID: TDRG-DEF-BAND] **Defect band:** $\mathcal{D}_k = \{\Delta \in \mathbb{Z}_N : \operatorname{dist}_{\mathbb{Z}_N}(\Delta, N/2) \leq k\}$.

`[DEF]` [RID: TDRG-DEF-EDGE-SET] **Defect edge set:** $E_{\rm def} = \{(i,j) : \Delta_{ij} \in \mathcal{D}_k\}$.

`[DEF]` [RID: TDRG-DEF-NARROW-BAND] **Narrow-band condition:** $k < N/6$. Required for holonomy exclusion.

### §6.2 Holonomy and Narrow-Band Exclusion `[THM]` {#sec-6-2-holonomy}

`[THM]` [RID: TDRG-THM-HOLONOMY] **Holonomy identity.** For any three nodes $A, B, C$:
$$\Delta_{AB} + \Delta_{BC} + \Delta_{CA} \equiv 0 \pmod{N}.$$
Consequence: the relational phases are holonomy-constrained; the defect graph inherits this constraint through $E_{\rm def}$.

`[THM]` [RID: TDRG-THM-NARROW-BAND-EXCLUSION] **Narrow-band exclusion.** Under $k < N/6$, no three nodes can all be mutually defect-related:
$$k < N/6 \;\Rightarrow\; |E_{\rm def} \cap K_3| \leq 2.$$
Proof: three antipodal defects require the holonomy sum to lie within $3k$ of $3N/2$, but holonomy forces the sum to $0, N,$ or $2N$; nearest distance $N/2 > 3k$. Contradiction.

Physical consequence: fully defective $K_3$ triangles are forbidden. Physical discrete triadic objects are partial-defect (path) or star-supported structures. *(v2.12.14, cross-citation; AZ-owned)* `AZ-ALG-ANTIPODAL-LOWORDER` (`az-v0.6`) is the same antipodal-band arithmetic extended to closed non-backtracking walks: none of length 2 or 3 under $k<N/6$, and none of odd length $L$ while $Lk<N/2$. It is a static $\mathbb{Z}_N$ graph statement — not TDR-G dynamics and not a bridge (SG-10); TDR-19 stays OPEN, and AZ's angular-spectrum results do not confirm TDR-G's N-scaling.

`[THM]` [RID: TDRG-THM-RECURRENCE] **Finite-state recurrence.** The state space $\bigsqcup_{M}\mathbb{Z}_N^{2M}$ is finite under any fixed node-count cap, and the update rule is deterministic. Therefore every orbit of $G_{\rm perm}^{(M)}$ is eventually periodic. No true chaos exists in the capped system; only long-period recurrence.

### §6.3 Interaction Laws and Policy Definitions `[DEF]` {#sec-6-3-interaction}

> **[Local guard SG-10 applies]** No rule in this section may import from the continuous RTG programme.

`[DEF]` [RID: TDRG-DEF-CONV-TICK] **Canonical step semantics (CONV-TICK).** Each simulation step executes in this order:
1. Advance phases by current velocity tokens: $\theta_i \mapsto (\theta_i + \delta_i) \bmod N$.
2. Construct $E_{\rm def}$ from the post-advance relational phases $\Delta_{ij}$.
3. Decompose $E_{\rm def}$ into connected components.
4. Classify each component as isolated edge, path, cycle, clean star, multistar, or tie.
5. Apply the selected policy to the pre-update component classification.
6. Apply all resulting swaps, cycles, bound-state decisions, and births synchronously.
7. Record observables and motif-log counters from the declared pre/post convention.

**(v2.12)** This convention is named **CONV-TICK** and is `[ENG audit: PASS]` against `genesis_mode_b_mc.py` v18: advance → snapshot ($\theta_{\rm pre}, \delta_{\rm pre}$) → classify on snapshot → apply all events against snapshot; no same-tick re-advance; post-event tokens act at the next tick. The convention was previously declared but unnamed; naming it makes it citable as a foundational commitment (it is imported by `RTG_ONTOLOGICAL_FOUNDATIONS` v0.7).

`[DEF]` Unless explicitly stated otherwise, motif quantities using `M_pre` or component counts are pre-birth, pre-policy-application quantities for that step.

`[DEF]` [RID: TDRG-DEF-SWAP] **Antipodal swap** (single defect edge $\{A,B\}$): $(\delta_A, \delta_B) \mapsto (\delta_B, \delta_A)$.

`[DEF]` [RID: TDRG-DEF-CONV-P3CYC] **Path-cycle interaction (CONV-P3CYC)** (two-edge path $P_3$, nodes $[v_1, v_2, v_3]$): oriented 3-cycle along the path direction. **(v2.12, `[script-certified v18]`)** The permutation is the **successor shift**: each node receives its forward neighbor's token along the oriented path,
$$(\delta_{v_1},\delta_{v_2},\delta_{v_3}) \mapsto (\delta_{v_2},\delta_{v_3},\delta_{v_1}),$$
implemented in v18 as `delta[v] = old[path[(i+1) % len]]` (general $P_n$: same successor shift along the oriented path). The prior wording "oriented 3-cycle along the path direction" under-determined the rotation direction; the choice flips $\sim20\%$ of three-body trajectory fates at finite horizon, so trajectory-level reproducibility requires this convention. The coarse BIND3 class taxonomy is convention-robust `[NUM]` `[scope: N=24, k=1 exact enumeration]` (§6.12).

`[DEF]` [RID: TDRG-DEF-SIGNED-CENTERED] **Centered representative.** For even $N$ and $x\in\mathbb{Z}$, $\operatorname{signed\_centered}(x,N)$ is the representative of $x \bmod N$ in the half-open interval $(-N/2,\,N/2]$. The half-open choice is a convention; it gives $\operatorname{signed\_centered}(N/2)=\operatorname{signed\_centered}(-N/2)=+N/2$, which is the source of the reversal-invariant stratum in the orientation rule below. *(v2.12.14: previously used here but defined only in the engine, function `signed_centered`.)*

`[DEF]` [RID: TDRG-DEF-SIGNED-DEFECT-ERROR] **Signed defect error.** $\operatorname{signed\_defect\_error}(\theta_i,\theta_j,N)=\operatorname{signed\_centered}\big((\theta_i-\theta_j) \bmod N - N/2,\;N\big)$, the signed distance of $\Delta_{ij}$ from the antipode. A pair is a defect edge iff $|\operatorname{signed\_defect\_error}|\le k$ (TDRG-DEF-EDGE-SET). On a defect edge $|\operatorname{signed\_defect\_error}|\le k<N/6$, so the value never reaches $\pm N/2$ and it changes sign exactly when the pair is listed in the opposite order. *(Engine: function `signed_defect_error`.)*

`[DEF]` [RID: TDRG-DEF-ORIENT] **Path orientation rule.** *(v2.12.14 `[COR]`; owner dispositions of 27 Oct 2026, option (b).)* For a path $P_n$ ($n \geq 3$) listed as $[v_1,\ldots,v_n]$: $S = \sum_i \operatorname{signed\_defect\_error}(\theta_{v_i}, \theta_{v_{i+1}}, N)$. Orient forward if $S > 0$, reversed if $S < 0$. If $S = 0$, let $E = \operatorname{signed\_centered}(\delta_{v_n} - \delta_{v_1}, N)$: forward if $0<E<N/2$, reversed if $-N/2<E<0$. If $S=0$ and $2E\equiv0 \pmod N$ — that is, $E\in\{0,\,N/2\}$ — **balanced path-tie**: no orientation can be read from the declared invariants (TDRG-ALG-ORIENT-NOGO below; SG-14). The policies treat the tie as before (`bound_path_tie`, `bound_symmetric`: inert bound state; `trap`, `bound_multistar`: ambiguous). Reference implementation: `evidence/tdrg/scripts/tdrg_orient_v2_12_14.py` (drop-in `orient_path`). **Superseded completion:** v2.12.13 stated the tie only for $S=E=0$; at $S=0\wedge E\equiv N/2$ the pinned engine (the v17 engine `genesis_mode_b_mc.py` and v18 share one `orient_path`) oriented "forward" relative to the node-ID listing of `raw_ordered_path` — a label-dependent completion (Appendix B). Every motif-log and BIND3 result of this document was computed under that completion and is kept with `[conv: v18 path orientation]`, not rerun (`EV-NOT-RERUN`; three-node census bound in §6.12).

`[ALG]` [RID: TDRG-ALG-ORIENT-NOGO] **No orientation from $(S,E)$ on the antipodal-endpoint stratum.** Reversing the listing maps $S\mapsto-S$ always (each defect-edge term is reversal-odd, TDRG-DEF-SIGNED-DEFECT-ERROR), and maps $E\mapsto-E$ except when $\delta_{v_n}-\delta_{v_1}\equiv N/2$, where $\operatorname{signed\_centered}$ returns $+N/2$ for both listings. Hence on $S=0\wedge E\equiv N/2$ the pair $(S,E)$ is reversal-invariant, and any selector that is a function of $(S,E)$ alone is either the tie or depends on the listing. The extended tie is the declared rule's covariant completion; it adds no new input. **Recorded alternative (not adopted):** for $P_3$ with centre $c$, $G=\operatorname{signed\_centered}(\delta_{v_1}-\delta_c)-\operatorname{signed\_centered}(\delta_{v_3}-\delta_c)$ is reversal-odd and never $0$ on the stratum (because $\delta_{v_3}-\delta_{v_1}\equiv N/2\neq0$; atlas check C2, exhaustive at $N=24$), so admitting the centre token as an orientation input would give a covariant non-tie rule for $P_3$; for longer paths a tie would still be needed on reversal-symmetric (palindromic) configurations. Choosing it is a law choice of the TDR-19 kind; it is kept for comparison with the adopted rule on the same universes in the later sensitivity campaign (`make_orient_g_alternative` in the reference implementation).

`[DEF]` [RID: TDRG-DEF-CYCLE-BOUND] **Cycle bound states.** All cycle components $C_n$, $n \geq 4$, are inert bound vortices: no birth, no momentum transfer.

`[DEF]` [RID: TDRG-DEF-STAR] **Star blow-up** ($K_{1,3}$ with center $A$, leaves $L_1, L_2, L_3$): new node $E$ created at $\theta_E = (\theta_A + N/2) \bmod N$, $\delta_E = \delta_A$; center inverts: $\delta_A \mapsto -\delta_A \bmod N$.

> **[Local guard SG-10 applies]** Star blow-up births a node. "Relational accounting preserved" means the birth event is exact and accountable — it does not mean node count is conserved.

`[DEF]` [RID: TDRG-DEF-MULTISTAR] **Multistar** ($K_{m,c}$-like, $m \geq 2$ valid star centers): component with multiple equally valid blow-up centers. Policy fork required.

| Policy | Multistar treatment | Path tie ($S=0$, $2E\equiv0$) | Character |
|---|---|---|---|
| `trap` | ambiguous (no birth) | ambiguous | strict unresolved |
| `bound_multistar` | inert bound state | ambiguous | semantic crystallization |
| `bound_path_tie` | inert bound state | inert | clean crystallization |
| `bound_symmetric` | inert bound state | inert | canonical clean crystallization |
| `largest_center` | one center fires | as configured | continuous inflation |
| `all_centers` | all centers fire | as configured | avalanche inflation |

`[ALG]` **Dynamic equivalence.** On state evolution, `trap`, `bound_multistar`, and `bound_path_tie` are dynamically equivalent whenever multistars/path-ties generate no births and no momentum transfer. They may differ in bookkeeping, ambiguity counters, and run-status semantics.

`[DEF]` [RID: TDRG-DEF-CANONICAL-BRANCH] **Canonical clean branch:** `bound_symmetric` = multistar bound states + balanced path-tie bound states.

### §6.4 Accounting Invariants `[ALG]` {#sec-6-4-invariants}

`[DEF]` **Valid v16 motif log.** A motif log is valid for TDR-24 claims only if:
1. Generated by `genesis_mode_b_mc.py` v16+ with active `argparse` CLI.
2. Records `births_step`, `clean_star_components`, `occ_clean_pairs`, `occ_clean_pairs_in_clean_star`, and `M_pre` at the declared stride.
3. Satisfies $rN_{\rm err} = 0$.
4. Is not cap-truncated unless explicitly classified as a tail/cap diagnostic.
5. Belongs to the declared policy branch and $k/N$ protocol.

`[ALG]` **Birth-rate invariant:**
$$rN_T = \text{birth\_steps} \cdot b/\text{step}, \qquad rN_{\rm err} = 0.$$
All reported clean runs satisfy this to machine precision.

`[ALG]` [assuming: the microscopic birth law (`[NUM]`, below) for the first identity] **TDR-24 pool-level factorization:**
$$\boxed{C_{\rm birth} = \frac{C_{\rm component}}{\chi}}, \qquad \boxed{B/\text{step} = O/\text{step} \cdot C_{\rm birth}}$$
where:
$$C_{\rm birth} = \frac{\sum_t \texttt{births\_step}}{\sum_t \texttt{occ\_clean\_pairs}}, \quad C_{\rm component} = \frac{\sum_t \texttt{occ\_clean\_pairs\_in\_clean\_star}}{\sum_t \texttt{occ\_clean\_pairs}}, \quad \chi = \frac{\sum_t \texttt{occ\_clean\_pairs\_in\_clean\_star}}{\sum_t \texttt{clean\_star\_components}}.$$
Verified to $< 10^{-18}$ in all valid v16 motif logs.

`[NUM]` **Microscopic birth law** (under `bound_symmetric`):
$$\boxed{\texttt{births\_step} = \texttt{clean\_star\_components}}$$
for all steps with nonzero births. Verified 100% in all valid v16 motif logs. Under `bound_symmetric`, every birth is generated by exactly one clean single-center star component.

`[ENG]` `[scope: 500 random inputs against the $O(n^2)$ reference]` **Edge-builder audit.** The $O(n \log n + E)$ bisect-based defect edge builder matches the $O(n^2)$ brute-force reference on 500 random inputs across $N \in \{30, 60, 90, 120\}$ (random $k$, $M \in \{4..60\}$), 0 mismatches. Certified at every run start: `graph_edges_for audit: PASS (500 trials)`.

### §6.5 Two-Node Universe `[ALG structure]` {#sec-6-5-twonode}

`[DEF]` Two-node state: $X_n = (\Delta_n, \delta_{A,n}, \delta_{B,n}) \in \mathbb{Z}_N^3$.

`[THM]` [RID: TDRG-THM-REACHABILITY-K0] **Reachability condition** ($k=0$): interaction occurs iff $\gcd(d, N) \mid (N/2 - \Delta_0)$.

`[ALG]` `[NUM exhaustive: all even $N\le40$, all $(d,\Delta_0)$, $k$ through the narrow-band regime]` [RID: TDRG-ALG-LEM-REACH] **(v2.12) LEM-REACH — band-form reachability.** The free orbit $\Delta_t=\Delta_0+td \bmod N$ equals the coset $\Delta_0+g\mathbb{Z}_N$, $g=\gcd(d,N)$. Hence: exact antipode reachable $\iff g\mid(N/2-\Delta_0)$ (the $k=0$ theorem above), and band reachable $\iff \mathcal{D}_k\cap(\Delta_0+g\mathbb{Z}_N)\neq\varnothing \iff \operatorname{dist}_N(N/2-\Delta_0,\,g\mathbb{Z}_N)\le k$. Geometric reading (`[INTERP]`, OFN-DIST-ZN scope): a uniformly winding relation visits a regular orbit-lattice of spacing $g$ on $C_N$; reachability is lattice–arc intersection. Supersedes any "every nontrivial orbit sweeps the band" reading — orbits confined to non-intersecting cosets are permanent superselection sectors at $k>0$ as well.

`[ALG]` `[NUM exhaustive: $N=2$–$40$, all $(\Delta_0,d_0)$]` `[scope: free inertia between events]` [RID: TDRG-ALG-LEM-NOANNIHIL] **(v2.12) LEM-NOANNIHIL — no free annihilation.** With the relational dyad state $(\Delta,d)$ and free evolution $F(\Delta,d)=(\Delta+d,\,d)$, the $d$-component is invariant; therefore $F^t(\Delta_0,d_0)=(0,0)\iff(\Delta_0,d_0)=(0,0)$. Every non-null dyad is non-annihilating under free evolution; annihilation, if it exists at all, is event-mediated only. Annihilation is *defined* as return to the null state $(0,0)$, not merely $\Delta=0$: phase coincidence with nonzero relative advance is a distinct relational state. This lemma replaces the former "trap / obstruction to annihilation" axiom at the ontology layer (exported to `RTG_ONTOLOGICAL_FOUNDATIONS` v0.7 as `[RESULT]` `[from: ALG]`).

`[ALG]` `[NUM exhaustive: even $N\le40$, $k\le N/6$]` `[scope: isolated dyad, CONV-TICK semantics]` [RID: TDRG-ALG-LEM-RETRIG] **(v2.12) LEM-RETRIG — two-node retrigger / binding threshold.** For band offset $\varepsilon=\Delta-N/2\in B_k=[-k,k]$, a swap maps $d\mapsto-d$ and the next offset is $\varepsilon'=\varepsilon-d$. Retrigger condition: $\varepsilon\in B_k\cap(B_k+d)$; a retrigger offset exists iff $|d|_c\le2k$; all offsets retrigger iff $d=0$. If the realized impact offset lies in the overlap, the isolated dyad forms an **exact bound state of period dividing 2**, $(\varepsilon,d)\leftrightarrow(\varepsilon-d,-d)$ (exact because CONV-TICK applies the swap against the snapshot with no same-tick re-advance); its least period is 2 for $d\neq0$, and $d=0$ is a fixed point $(\varepsilon,0)$ at which the swap fires on every tick *(v2.12.14 `[COR]`)*. The retrigger band $|d|_c\le2k<N/3$ never reaches $d\equiv N/2$, so no other degenerate case occurs. $k$ acts as a binding threshold; binding is impact-phase dependent. `[scope: isolated two-node dynamics — see SG-11]`.

`[RESULT]` `[from: THM]` Noninteracting two-node sectors are superselection sectors. **(v2.12 note:** strict superselection is a two-node statement; in $N\ge3$ universes events change individual $\delta$ tokens and births add relational channels, so pairwise sectors are not invariant — see LEM-SPECCONS §6.12 for the exact three-node conservation law that replaces it.)

`[ALG structure]` Two-node regimes:

| Regime | Condition | Behavior |
|---|---|---|
| Superselection | antipode unreachable | no interaction |
| Global bounce | antipode hit exactly | reversible bounce |
| Boundary jitter | $k>0$, band hit | localized two-step trap |
| Retrigger bound state (v2.12; period dividing 2) | $\varepsilon\in B_k\cap(B_k+d)$, $|d|_c\le2k$ | exact retrigger: a 2-cycle for $d\neq0$, a fixed point for $d=0$ (LEM-RETRIG) |

### §6.6 Policy Results `[NUM]` {#sec-6-6-policy}

> **[Local guard SG-7 applies]** Policy results are branch-specific. **(v2.12.14)** All motif-log results of §§6.6–6.10 come from the pinned engine (`upload/tdrg-records/genesis_mode_b_mc.py`, SHA-256 `4c94d874…a608`, and its logging-only extension `genesis_mode_b_mc_v18.py`, `9d787b43…675e`; one `orient_path`) and carry `[conv: v18 path orientation]`: they were computed with the label-dependent completion at $S=0\wedge E\equiv N/2$ that TDRG-DEF-ORIENT replaces. They are not rerun (`EV-NOT-RERUN`, PI decision 27 Oct 2026); the exposure is bounded only for the three-node universe (§6.12) — the many-node exposure rate is not measured.

`[NUM]` **Crystallization branch** (`bound_symmetric`): $p_{\rm ambig} = 0$; multistars inert; path ties inert; slow / suppressed growth.

`[NUM]` [conv: `largest_center`] **Continuous inflation branch:** Many multistar events, one birth per event, persistent expansion. Typical at $k/N \approx 0.0667$: $rN_T \approx 0.76$–$0.80$.

`[ALG]` [RID: TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK] `[scope: engine function choose_largest_center, pinned v17/v18 engines]` *(v2.12.14, owner finding N1)* **`largest_center` breaks equal-degree ties by node ID.** The centre that fires is the first under the key $(-\deg,\ \text{node id})$, so when two or more valid centres have the same degree the choice depends on node labels and the branch is not relabelling-covariant there (SG-14). Fixture: $K_{2,3}$ at $N=24$, $k=1$, centres of equal degree 3 with tokens 1 and 2 — exchanging the two centre labels changes which centre fires under `largest_center`, while `all_centers` and `bound_symmetric` are equivariant (`evidence/tdrg/disposition/multistar_fixture.py`, output `fe3928a4…`). The `largest_center` results of §§6.6–6.7 and §1 are kept with this scope note, not rerun (`EV-NOT-RERUN`); the canonical branch is unaffected (`bound_symmetric` binds multistars).

`[HEUR strong]` **Avalanche branch** (`all_centers`): Few birth steps, many births per event, cap-limited in many runs. Typical $b/\text{step} \approx 16$–$25$.

`[NUM]` [conv: cap protocol] **Policy ordering** at $k/N \approx 0.0667$:
$$rN_T(\texttt{largest\_center}) > rN_T(\texttt{all\_centers}) > rN_T(\texttt{bound\_symmetric}).$$
Caveat: `all_centers` often cap-limited; ordering is cap-protocol dependent.

`[NUM strong]` **Multi-birth phenomenon (universal).** $b/\text{step} > 1$ consistently across policies and N: $1.03$–$1.24$ under `bound_symmetric`, $1.01$–$1.02$ under `largest_center`. Interpretation: simultaneous clean single-center stars fire in the same step under full-locality processing. This is genuine physics, not a bookkeeping artifact.

`[NUM]` **largest_center inflation.** Under `largest_center` at high $k/N$, the late-window birth fraction approaches unity: $rN_{\rm late\_birth} = 0.9995$ at $N=90, k=8$. This is the first certified continuous-inflation signature in the campaign — almost every late step produces a birth.

**Multistar expansion character (ms_bpe)** (`[ALG]` for `largest_center`, definitional; `[NUM]` for `all_centers`).
- `largest_center`: $ms_{\rm bpe} = 1.00$ exactly — one birth per multistar event (definitional).
- `all_centers`: $ms_{\rm bpe} \approx 33.91$ at $N=60, k=4$ — all valid centers fire simultaneously on the frozen pre-update snapshot.

Structural distinction: `largest_center` is continuous controlled expansion; `all_centers` is rare avalanche expansion. The two inflationary branches differ not in whether they inflate but in the granularity of each inflation event.

### §6.7 Fixed-N Certified Results `[NUM]` {#sec-6-7-fixed-n}

`[NUM]` **T=500 grid** ($N=240$, `bound_path_tie`): $rN_T(k/N)$ is non-monotone, peaking near $k/N = 0.05$–$0.0667$. Dense-regime cooling onset at $k/N \geq 0.0667$.

`[NUM]` **k/N regime structure** (fixed $T=500$, all policies). Three regimes:
- **$k/N \approx 0.033$ (sparse/bimodal):** $p_{\rm frz} \approx 0.44$–$0.51$, $p_{\rm strong} \approx 0.41$–$0.50$. The freeze/grow split is policy-independent and set by initial conditions.
- **$k/N \approx 0.050$ (transition):** $rN_T$ attains its non-monotone maximum.
- **$k/N \geq 0.067$ (dense):** growth-branch dominance; $p_{\rm frz} \to 0$, $p_{\rm strong} \to 1$ in all policies.

Summary: $k/N$ selects entry into the growth branch; the multistar interaction axiom selects growth rate and character.

`[NUM]` **Long-horizon** ($N=120, k=8$): system does not freeze through $T=10000$. Exact late-rate values: $rN_{\rm late} = 0.0201$ at $T=5000$ and $0.0202$ at $T=10000$ — stabilizing rather than continuing to fall. $rN_{\rm late}/rN_T$ progression: $0.473, 0.600, 0.801, 0.894$ at $T=1000, 2000, 5000, 10000$. The ratio approaching $\sim 0.89$ is the signature of near-steady slow accretion, not terminal cooling (evidence for OPEN TDR-22c).

`[NUM]` **N=240 long-horizon band.** At $N=240$, $T=5000$: $rN_{\rm late}(k=12) \approx rN_{\rm late}(k=16) \approx 0.0075$. Late accretion is more strongly controlled by $N$ than by $k/N$ within the $k/N \in [0.05, 0.0667]$ band.

`[NUM]` **Defect-density scaling.** At fixed $k/N = 0.0667$, mean defect density $\rho \approx 0.12 \approx 2k/N$ (consistent with band-size estimate up to graph-dynamical correlations).

### §6.8 N-Scaling Results `[NUM strong]` {#sec-6-8-nscaling}

> **[Local guard SG-6 applies]** All claims are finite-horizon (canonical scan currently N = 120–1440, T=5000, with high-N asymptotic claims separately guarded; the v18-orientation scope of §6.6 applies).

`[NUM strong]` **Full N-scaling table** (fixed $k/N = 0.0667$, $T=5000$):

| $N$ | $k$ | bulk $mf$ | $rN_{\rm late}$ | $p_{>100}$ | $p_{>500}$ | batch | notes |
|---:|---:|---:|---:|---:|---:|---:|---|
| 120 | 8 | 117 | 0.0201 | 0.440 | 0.040 | 50 | tail-inflated raw mf=129.5 |
| 180 | 12 | — | 0.0078 | 0.133 | 0.000 | 30 | |
| 240 | 16 | 76 | 0.0076 | 0.160 | 0.000 | 50 | |
| 360 | 24 | — | 0.0044 | 0.000 | 0.000 | 30 | |
| 480 | 32 | 59 | 0.0054 | 0.060 | 0.000 | 100 | non-monotone; see TDR-23a |
| 718 | 48 | — | 0.0023 | 0.000 | 0.000 | 20 | arithmetic control |
| 720 | 48 | 61 | 0.0105 | 0.035 | 0.005 | 200 | pooled; tail from 1 run (r43) |
| 722 | 48 | — | 0.0038 | 0.050 | 0.000 | 20 | arithmetic control |
| 960 | 64 | 55 | 0.0028 | 0.010 | 0.000 | 100 | |
| 1080 | 72 | 53 | 0.0023 | 0.000 | 0.000 | 20 | factor-rich control |
| 840 | 56 | 54 | 0.0025 | 0.000 | 0.000 | 100 | factor-rich 7-divisible control ($2^3\cdot3\cdot5\cdot7$) |
| 1200 | 80 | 54 | 0.0024 | 0.000 | 0.000 | 50 | asymptotic extension |
| 1440 | 96 | 55 | 0.0019 | 0.000 | 0.000 | 50 | asymptotic extension |

`[NUM strong]` **Tail suppression with rare locking failure.** High-growth tails are strongly suppressed with increasing $N$. The pooled $N=720$ campaign (batch=200) shows $p_{>100}=0.035$ and $p_{>500}=0.005$ driven by one locking-failure run (r43). The correct reading is bulk suppression plus rare locking-failure events; $N=720$ does not have zero tail probability. Legacy batch-20 controls at N=718 and N=722 showed no >500 tails but were weakly constrained (binomial CI upper 0.168). The v17 batch-100 campaign supersedes this: N=722 has one matching locking-failure tail (1/100), while N=718 remains clean (0/100). N=722 is therefore no longer a clean arithmetic control; it is a stochastic-neighborhood tail witness. N=718 and N=840 remain the clean controls.

`[NUM]` `[scope: full-range fits; composite exponents are window-dependent — §1, §2 TDR-24A/B]` **Bulk-conditioned N-scaling** (v4 motif analysis, $k/N=1/15$, $T=5000$, $t \geq 4001$, $M \leq 500$):

| Observable | Fit (v17/v6 canonical) | $R^2$ |
|---|---|---:|
| $C_{\rm birth}^{\rm bulk}$ | $9.514 \cdot N^{-1.593}$ | 0.993 |
| $C_{\rm component}^{\rm bulk}$ | $0.7366 \cdot N^{-0.757}$ | 0.939 |
| $\chi^{\rm bulk}$ | composite ratio — not a power law (v2.12.1); $\texttt{cs}/\text{row}\sim N^{-0.73}$ | 0.86 |
| $B_{\rm bulk}/\text{step}$ | $1.041 \cdot N^{-0.869}$ | 0.973 |
| $O_{\rm bulk}/\text{step}$ | $0.1094 \cdot N^{+0.723}$ | 0.972 |
| $M_{\rm bulk}$ | $419.5 \cdot N^{-0.295}$ | 0.881 |
| $O_{\rm slot}^{\rm bulk}/\text{step}$ | $53.69 \cdot N^{+0.709}$ | 0.976 |
| $\psi_{\rm slot}^{\rm bulk}$ | $0.00204 \cdot N^{+0.014}$ | 0.015 |

(Supersedes the v4 6-point fit, $N=120$–$1080$. The v17/v6 scan spans $N=120$–$1440$. The low $R^2$ on $\psi_{\rm slot}^{\rm bulk}$ reflects that it is nearly N-flat — there is little variance for the power law to explain, which is the point: $\psi$ is intensive.)

`[NUM]` [scope: full-range fits] $0.869 \approx 1.593 - 0.723$ reflects the exact factorization $B/\text{step}=O/\text{step}\cdot C_{\rm birth}$ (§6.4) read on fitted exponents; it does not confirm a power-law form, and the composite exponents drift with the fit window. `[COR]` *(v2.12.14)* The former companion check $1.593\approx0.757+0.836$ used the $\chi$ exponent $+0.836$ superseded in v2.12.1 (§2 TDR-24B) and is withdrawn; no replacement sum is promoted.

**Slot-volume model (verified).** `[ALG]` $O_t = (2k+1) M_t \psi_t$ holds by construction. `[NUM strong]` The v6 extractor confirms across the canonical scan:
$$O_{\rm slot}^{\rm bulk}/\text{step} \approx 53.69 \cdot N^{+0.709}\ (R^2=0.976), \qquad \psi_{\rm slot}^{\rm bulk} \approx 0.00204 \cdot N^{+0.014}\ (R^2=0.015).$$
$\psi_{\rm slot}^{\rm bulk}$ is effectively intensive (scale-invariant $\approx 0.002$). Therefore the positive scaling $O_{\rm bulk}/\text{step} \sim N^{+0.723}$ is explained by slot-volume growth, not by the rejected $M^2$ pair model. The identity residual $\epsilon_{\rm slot}$ is machine-small in all valid v17 logs. **OPEN TDR-24D is structurally closed** (`[ALG]` identity; `[NUM strong]` intensiveness); the analytic reason $\psi$ is intensive is routed to OPEN TDR-24F.

Consistency: $O_{\rm slot}$ exponent $0.709 + \psi$ exponent $0.014 = 0.723 = O_{\rm bulk}/\text{step}$ exponent ✓.

`[COR]` **Range-tagged dual-suppressor fit:** the fitted $C_{\rm component}$ exponent is a composite ratio exponent, not a structural constant. The v17/v6 full-range convenience fit gives $C_{\rm component}^{\rm bulk} \sim N^{-0.757}$, but the TDR-24A decomposition shows this arises from an approximately linear denominator and near-flat numerator. Percentage splits based on $-0.757$ vs $\chi^{\rm bulk}$ are diagnostic only, not mechanism-level constants.

### §6.9 Arithmetic Controls and Tail Analysis `[NUM]` {#sec-6-9-arithmetic}

> **[Local guard SG-6 applies]**

`[NUM]` **N=720 tail** ($r43$): $C_{\rm component} = 0.782$ vs bulk $0.007$ — topological filtering failure, not ordinary bulk fluctuation.

`[NUM]` **N=722 matching tail.** A second rare locking-failure run appears at $N=722$ (1/100, final_M$\approx$2904, $C_{\rm component}\approx0.812$), structurally identical to N=720 r43. The tail is therefore a stochastic local-neighborhood phenomenon, not an N=720-singular event.

`[NUM]` **N=840 factor-rich falsification.** $N=840 = 2^3\cdot3\cdot5\cdot7$ — the first 7-divisible cell, maximally factor-rich in the tested range — is perfectly clean at batch=100 ($p_{>500}=0$). This is the decisive falsification of the deterministic arithmetic-factor hypothesis.

Rejected arithmetic explanations (all `[FAIL]`):
- Simple divisor count: $\tau(720) = 30$, but $N=1080$ ($\tau = 32$) and $N=840$ ($\tau=32$) are clean.
- $3^2 \mid N$: $N=1080$ ($3^3 \mid N$) is clean.
- 15-commensurability fraction: $P_{15}(1080) = 0.770 > P_{15}(720) = 0.711$; 1080 is clean.
- 7-divisibility: $N=840$ ($7 \mid N$) is clean.
- Deterministic instability: bulk phase is stable; matching tails at both N=720 and N=722 are rare stochastic events.

### §6.10 Multistar Locking Mechanism `[NUM]` — mixed content {#sec-6-10-mechanism}

`[NUM]` In long-horizon `bound_symmetric` runs:
- $ms_{\rm seen} \approx T$ — roughly one multistar bound state per step.
- Top components at $T=10000$ are large multistars ($20$–$50$ centers); no clean single-center stars in top 5.

`[HEUR strong]` Mechanism: defect-graph densification produces large multistar bound states, which suppress clean single-center births and yield cooling / slow accretion.

`[NUM]` **Multistar load diagnostic.** $V_{\rm pair\_load} = \texttt{occ\_multistar\_pairs} / \texttt{occ\_clean\_pairs}$ is a multistar embedding/load measure, **not a fraction**. It routinely exceeds 1 (e.g. $\approx 19.22$ at $N=240, k=16$) because multistar-associated candidate counts are not deduplicated as a probability mass. It must not be interpreted as a probability or fraction. (A correctly normalized fraction would require a separate deduplicated `ms_frac` diagnostic.) The load grows with $N$ under multistar locking, consistent with the densifying vacuum.

### §6.11 Core Observable Definitions {#sec-6-11-observables}

- `bf` :: fraction of runs with at least one birth
- `mf` :: mean final node count
- `q50, q90, q99` :: final-node quantiles
- `rN_T` :: $\sum \text{births} / (\text{batch} \cdot T)$
- `rN_s` :: $\sum \text{births} / \sum \text{steps}$
- `rN_late` :: mean second-half birth rate
- `birth_steps` :: birth-step fraction
- `b/step` :: conditional births per birth step
- `swap_rate`, `path_rate`, `cyc_rate` :: component interaction rates per step
- `p_frz` :: fraction final nodes $\leq 5$
- `p_strong` :: fraction final nodes $> 12$
- `p_ambig` :: runs with ambiguous events
- `ambig_rate` :: mean ambiguous events per actual step
- `ms_seen`, `ms_bound`, `ms_res`, `ms_trap`, `ms_bpe` :: multistar encounter and birth statistics
  - `ms_bound` :: multistar events treated as inert bound states (`bound_symmetric`)
  - `ms_res` :: multistar events resolved by birth (`largest_center` / `all_centers`)
  - `ms_trap` :: multistar events counted as ambiguous (`trap` bookkeeping)
  - `ms_bpe` :: multistar births per resolved event (1.00 for `largest_center`; ≈34 for `all_centers`)
- `pt_seen`, `pt_bound`, `pt_fail` :: path-tie statistics
- `p_gt100, p_gt200, p_gt500` :: high-growth tail probabilities
- `rho` :: mean defect edge density
- `rN_T/rN_s` :: equals 1 if no cap; $rN_s > rN_T$ indicates cap-truncated runs
- `p_cap` :: fraction of runs that hit the `max_nodes` cap
- `mean_steps_taken` :: batch-mean actual steps completed (< T when `p_cap` > 0)
- `births_step` :: per-step birth count (motif log)
- `clean_star_components` :: per-step clean single-center star components (motif log)
- `occ_clean_pairs` :: per-step sliding-window antipodal occupancy candidates (motif log)
- `occ_multistar_pairs` :: per-step multistar-embedded occupancy candidates (motif log)
- `occ_clean_pairs_in_clean_star` :: per-step candidates that produce births (motif log)
- `O_slot_per_step` :: ratio-of-sums slot volume per step, $\sum_t (2k+1) M_{\rm pre} / \text{steps}$
- `psi_slot_bulk` :: occ_clean_pairs / slot_volume in the bulk late window
- `cbar_slot_bulk` :: occ_clean_pairs / M_pre, equivalent to $(2k+1)\,\psi_{\rm slot}^{\rm bulk}$
- `cbar_struct_bulk` :: structural leaf reservoir extracted from multistar topology ($\approx 4.5$–$5.8$ in high-N bulk)
- `q_struct_to_slot_bulk` ($q_{\rm proj}$) :: projection factor $\bar{c}_{\rm slot} / \bar{c}_{\rm struct}$
- `slot_identity_err` ($\epsilon_{\rm slot}$) :: identity residual for $O = O_{\rm slot}\cdot\psi_{\rm slot}$
- `leaf_model_err` :: residual for the structural-to-slot closure model (TDR-24F)
- `V_pair_load` :: multistar embedding/load diagnostic ($\texttt{occ\_multistar\_pairs}/\texttt{occ\_clean\_pairs}$); may exceed 1, **not a fraction**

### §6.12 Three-Node Universe and BIND3 Certification `[ALG]` — mixed content (exact lemma and enumerations; numerical suites) {#sec-6-12-threenode} *(new in v2.12)*

> **[SG-11, SG-12, SG-13 apply.]** All results in this section are scoped to the three-node, no-birth universe under `bound_symmetric` with canonical v18 conventions (CONV-TICK, CONV-P3CYC) unless stated otherwise. **(v2.12.14)** The enumerations and suites were run with the v18 path orientation (label-dependent at $S=0\wedge E\equiv N/2$; replaced by TDRG-DEF-ORIENT): their numbers carry `[conv: v18 path orientation]` and are not rerun (`EV-NOT-RERUN`; census bound in the orientation-covariance block at the end of this section). LEM-SPECCONS is unaffected (ties act as identity).

`[ALG]` `[NUM: 3000 random ICs × 500 steps, zero violations]` `[scope: 3 nodes, no star blow-up]` [RID: TDRG-ALG-LEM-SPECCONS] **LEM-SPECCONS — conservation of the relational advance spectrum.** Define pairwise advances $d_{AB}=\delta_A-\delta_B$, $d_{BC}=\delta_B-\delta_C$, $d_{CA}=\delta_C-\delta_A$, with $d_{AB}+d_{BC}+d_{CA}\equiv0\pmod N$. Free advance leaves $\delta$ unchanged; the antipodal swap acts on the difference triple as a signed transposition; the $P_3$ successor-shift acts as a cyclic permutation; balanced ties act as identity. Every event is therefore a signed permutation of the difference triple, and the multiset
$$\{|d_{AB}|_c,\ |d_{BC}|_c,\ |d_{CA}|_c\}$$
is **exactly conserved** — therefore, in particular, the multiset of orbit-lattice spacings $\{\gcd(d_{ij},N)\}$ is conserved *(v2.12.14 `[COR]`: the converse fails — at $N=24$, $|d|_c=1$ and $|d|_c=5$ share $\gcd=1$)*. Under TDRG-DEF-ORIENT (v2.12.14) the extended balanced tie also acts as identity, so the lemma holds unchanged. Geometric reading (`[INTERP]`): the three-node universe has a conserved stock of pairwise orbit-lattice spacings on $C_N$; events reassign lattices to pairs, never create, destroy, or rescale them. **Generalization:** $n$-node signed-permutation invariance is conjectured for swap/path-cycle sectors; **star blow-up creates a new node and new pairwise advances and is `[OPEN]` (SG-12)**.

`[ALG]` `[scope: $N=24$, $k=1$, post-advance BIND3 ICs, exact cycle enumeration, 3456 ICs, both $P_3$ conventions]` `[conv: v18 path orientation]` [RID: TDRG-ALG-BIND3-CYCLE-N24K1] **BIND3-CYCLE-N24K1 — exact certification.** Exact finite-state cycle enumeration replaces all prior horizon-based BIND3 classifications (which are superseded as windowing-contaminated). A two-node period-2 dyad is **not a persistent primitive** in the three-node universe. Exact class taxonomy: multi-pair recurrent scattering cycles **96.4%**; pure AB-bound cycles **3.6%**; free and single-pair-partial cycles **0%**. Bond transfer occurs inside the exact cycle of **81.8%** of ICs. Cycle structure: median preperiod 0 (max 830); median period 138, max 1638, 79 distinct lengths (dominant: 15, 48, 357, 396, 228, 1638). $K_3$ fully defective components: **0** across all periods, consistent with narrow-band exclusion ($k<N/6$). The coarse class taxonomy is identical under both $P_3$ rotation conventions (3332/124 in each); trajectory-level outcomes are convention-sensitive, hence CONV-P3CYC.

`[ALG]` `[scope: $N=24$, $k=1$]` `[conv: v18 path orientation]` **d-resolved anatomy — primary retrigger-entry family plus supplementary one-pass family.**

| $d$ | $\gcd(d,N)$ | $|d|_c$ | ICs | pure AB % | scatter % | transfer % | $\langle f_{AB}\rangle$ | $\langle f_{AC/BC}\rangle$ |
|---|---|---|---|---|---|---|---|---|
| ±1 | 1 | 1 | 1152×2 | 0.0 | 100.0 | 82.4 | 0.290 | 0.167 |
| ±2 | 2 | 2 | 576×2 | 10.8 | 89.2 | 80.6 | 0.319 | 0.125 |
| ±3 | 3 | 3 | 1728×2 | 0.0 | 100.0 | 97.9 | 0.143 | 0.140 |
| ±4 | 4 | 4 | 1728×2 | 0.0 | 100.0 | 90.0 | 0.155 | 0.130 |
| ±5 | 1 | 5 | 1728×2 | 0.0 | 100.0 | 97.6 | 0.139 | 0.131 |

Rows $|d|_c\le2$ are retrigger-entry ICs (totaling the 3456 of the headline certification); $|d|_c\ge3$ are one-pass supplementary ICs (10368). **The 96.4% / 3.6% BIND3-CYCLE headline percentages refer only to the $|d|_c\le2$ retrigger-entry family. Rows $|d|_c\ge3$ are the supplementary regeneration-control family and must not be pooled into the headline taxonomy.** Exact $\pm d$ mirror symmetry of the class inventory holds in both families (mirror-inventory check: PASS). *(v2.12.14 `[COR]`: this is not node-relabelling covariance (SG-14), and the step itself is not mirror-equivariant at $P_3$ events — TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY, below.)*

`[NUM strong]` `[scope: $N=24$, $k\in\{1,2\}$, exhaustive over retrigger ICs]` [RID: TDRG-NUM-BIND3-PARITY] **BIND3-PARITY** *(replaces BIND3-KNIFE, which is `[FAIL]` `[REPLACED]` — see Appendix B)*. Pure-bound survival is controlled by **even/odd parity of the relative advance $d$, not by marginality** of the two-node retrigger band. At $k=2$: odd classes $d=\pm1,\pm3$ have **zero** survivors (0/6912); even classes $d=\pm2$ (deep, 4.3%) and $d=\pm4$ (marginal, 5.2%) both survive. Mechanism (`[ALG]` necessity, $N=24$): while the dyad executes its period-2 cycle, a spectator's relative phase advances by $2\delta_C-d$ per two ticks; for odd $d$ this step is odd, so $\gcd(2\delta_C-d,24)\in\{1,3\}$ and no coset can avoid a $(2k+1)$-point antipodal arc — spectator avoidance is arithmetically impossible. For even $d$, co-moving ($\delta_C=d/2$, exactly or antipodally shifted — the largest survivor classes) and wide-sublattice (spacing $\ge4$) spectator frames exist; all observed survivor token classes satisfy the coset-avoidance condition (zero inconsistencies). Full $(N,k,d)$ sufficiency characterization: OPEN-BIND3-PARITY-GEN.

`[NUM strong]` `[scope: $N=24$, $k=1$, 9216 ICs, no-birth]` [RID: TDRG-NUM-BIND3-SPECTRAL-GATE] **BIND3-SPECTRAL-GATE.** If every spacing in the conserved advance spectrum satisfies $|d_{ij}|_c>2k$, then **no pair exhibits autonomous two-node retrigger episodes at any time** (0 violations across 4352 all-above-threshold ICs in 27 spectrum classes; detector sanity: 1906 retrigger episodes observed in below-threshold ICs). Confirms the LEM-SPECCONS consequence: no-birth three-node dynamics can reassign but not create autonomous-retrigger-compatible spacings. The gate forbids autonomous period-2 retrigger only, **not transient in-band occupancy** (SG-13).

`[COR]` **BIND3-MEMORY correction + `[NUM strong]` BIND3-MEMORY-PARITY** [RID: TDRG-NUM-BIND3-MEMORY-PARITY] `[scope: $N=24$, $k=1$, even-advance initial bonds]`. The prior unstratified claim (initially bound families retain memory-biased occupancy, $\langle f_{AB}\rangle\approx0.30$ vs $\approx0.15$) was **composition-mixed**. Stratified by conserved-spectrum class: odd-advance initial bonds show **no** genuine bias (e.g. class $(1,2,3)$: $f_{AB}=0.154$ vs $f_{\rm other}=0.154$; matches non-binding-entry control) — the odd-sector memory claim is a composition artifact. Even-advance initial bonds retain a **strong, genuine** residence-time bias within fixed spectrum classes (e.g. $(2,2,4)$: 0.306 vs control 0.183; $(2,3,5)$: 0.382 vs 0.134; $(2,5,7)$: 0.425 vs 0.126). Binding-history memory is an even-advance parity-sector effect — the same parity that controls pure-bound survival (BIND3-PARITY) confers partial occupancy protection on the non-surviving even-$d$ majority. Control: non-binding-entry ICs relax toward near-equipartition ($f_{AB}\approx f_{AC/BC}\approx0.13$–$0.15$). *(The earlier equipartition candidate BIND3-EQUIP is `[FAIL]` — Appendix B.)*

`[NUM strong]` `[scope: $N=24$, $k=1$]` [RID: TDRG-NUM-BIND3-XFER] **BIND3-XFER — bond transfer.** Transfer of the bonded pair appears inside the exact cycle of 81.8% of retrigger-entry ICs (and 90–98% of one-pass ICs): a third node inherits the resonant token relation through $P_3$ component dynamics. Transfer is the generic mechanism of the recurrent class, not a rare side channel. Under LEM-SPECCONS this is **spectrum reassignment**, never spacing creation. Structural ($P_3$-action-level) explanation: OPEN-BIND3-REGEN.

`[NUM strong]` `[scope: $N=24$, $k=1$]` [RID: TDRG-NUM-BIND3-REGEN] **BIND3-REGEN — regeneration beyond the two-node threshold.** Initial pairs with $|d_{AB}|_c>2k$ cannot bind autonomously (LEM-RETRIG), yet three-node dynamics give pure-AB cycles 0.0%, transfer 95.2%, $\langle f_{AB}\rangle=0.146$: third-node $P_3$ token rotation regenerates band-reaching and retrigger-compatible pairs by reassigning the conserved spectrum. The LEM-RETRIG threshold bounds only pairwise-autonomous binding, not binding or in-band occupancy in $N\ge3$ systems (SG-11).

**Synthesis** `[INTERP]`: The BIND3 layer is not governed by "bound survival versus dissolution." It is governed by a **conserved advance spectrum** whose **parity/lattice-avoidance structure** controls which pairs can autonomously retrigger (SPECTRAL-GATE), which spectators can avoid disruption (PARITY), and which initial bonds leave residence-time memory (MEMORY-PARITY).

#### Orientation covariance at the antipodal-endpoint stratum *(v2.12.14)*

`[ALG]` [RID: TDRG-ALG-ORIENT-ANTIPODAL-FIXTURE] `[scope: one explicit state; pinned v18 engine]` **The v2.12.13/v18 orientation is not relabelling-covariant.** $N=24$, $k=1$, $\theta_{\rm pre}=(0,11,12)$, $\delta=(0,1,12)$: after the advance $\theta=(0,12,0)$; the defect graph is the path $0$–$1$–$2$ with $S=0$ and $E=+12=N/2$ under both listings. Exchanging the endpoint labels changes the v18 outcome (it gives $\delta'=(1,12,0)$, which is not the relabelled image of the outcome in the other labelling); under TDRG-DEF-ORIENT the event is a balanced tie and the step is equivariant (the recorded G-alternative gives $\delta'=(12,0,1)$, also equivariant). Evidence: `evidence/tdrg/disposition/antipodal_fixture.txt` (`c47d78b9…`); checker `evidence/tdrg/scripts/check_tdrg_v2_12_14.py`, gate C10 (negative control).

`[NUM]` [RID: TDRG-NUM-ORIENT-EQUIVARIANCE-N24] `[scope: N=24; three nodes exhaustive over the 331,776 gauge-reduced states (θ₀=δ₀=0) at k=1 and k=3, generators (01) and (12) of S₃; four nodes, 100,000 random (state, k∈{1,2,3}, permutation∈S₄) samples; bound_symmetric, and largest_center at four nodes; the pinned engine's own step_universe with only orient_path exchanged]` **Relabelling equivariance of the step.** Failures per generator: v18 72 / 72 at $k=1$ and 168 / 168 at $k=3$; TDRG-DEF-ORIENT 0; the G-alternative 0. Four nodes: v18 112 failures; TDRG-DEF-ORIENT and the G-alternative 0. Global phase shift: 0 failures in every variant (1/97 sample). Evidence: `evidence/tdrg/disposition/owner_relabel_equivariance_check.py` (`2f54e0fc…`), output `owner_relabel_equivariance_check_output.txt` (`a0b33690…`). A finite check, not a theorem for all $N$ or all policies.

`[NUM]` `[scope: N=24, k=1, three nodes, the whole gauge-reduced state space; atlas independent check]` **Census bound for results computed under v18.** Under the v18 completion, 77 of 9,800 eventual cycles contain a listing-dependent event and 16,322 of 331,776 states (4.9 %) flow into such a cycle; under the extended tie the same universe has 9,789 eventual cycles, 66 of which contain a tie event on the stratum. Whether any of the 3,456 retrigger-entry or 10,368 one-pass BIND3 ICs reaches the stratum is not determined (the IC construction script is missing, §8). Source: `evidence/atlas/tdrg/atlas_tdrg_orientation_covariance_check.py` (`5684da96…`), results `atlas_tdrg_orientation_covariance_check.json` (`2d15b12f…`), rerun byte-identically by the owner session (owner disposition record claude01SKePJ, §5 (i)).

`[NUM]` `[scope: NUMGEN DISC-2 ratified panel, 136 witnesses; atlas rerun of NUMGEN's audit verdict logic]` **DISC-2 witness effect.** 40 witnesses touch the stratum; under TDRG-DEF-ORIENT **20 of 136** records change verdict or class (for comparison: reverse completion 10, G-alternative 12); the ten admitted labels are unchanged; the 96 unexposed witnesses are unchanged by construction. DISC-1 and other panels are not covered; re-annotation is NUMGEN's.

`[ALG]` [RID: TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY] *(owner finding N2)* **The mirror is not a step symmetry.** Under $(\theta,\delta)\mapsto(-\theta,-\delta)$ every $\operatorname{signed\_defect\_error}$ on a defect edge changes sign, so away from ties the path orientation reverses; the successor shift along the reversed path sends $(-\delta_{v_1},-\delta_{v_2},-\delta_{v_3})\mapsto(-\delta_{v_3},-\delta_{v_1},-\delta_{v_2})$, which differs from the mirror image $(-\delta_{v_2},-\delta_{v_3},-\delta_{v_1})$ of the original update unless the three tokens are equal. `[NUM]` check: 2,661 failures among the 2,703 states with a $P_3$ event in 60,000 random three-node states ($N=24$, $k=1$; `evidence/tdrg/disposition/mirror_probe.py`, output `9f8bdf59…`). The $\pm d$ mirror identity of the BIND3 class inventories (above) is therefore an inventory statement, not equivariance of the dynamics.

---

## §7. Import Ledger {#sec-7-imports}

TDR-G imports no scientific coefficients, tensors, interaction laws or continuous-branch results under the cross-branch firewall (SG-10). All scientific claims in this document are native $\mathbb{Z}_N$ definitions, derivations, simulations or diagnostics, with the one scoped import below. *(v2.12.14: four-way register — imports, consumers, pins, exports — with the states received / statement accepted / adopted use read from records, not from queue states.)*

**Imports.**

- `[ALG]` [import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.10 §4.1 | RTG-OFN-ALG-STAR-TOKEN-SHIFT] **Common token shift and the star rule.** Under $B_c:\delta_i\mapsto\delta_i+c$, antipodal swaps, path successor shifts and ties commute with $B_c$ (they permute tokens); star blow-up (TDRG-DEF-STAR) commutes with $B_c$ iff $2c\equiv0 \pmod N$, because the centre goes to $-\delta_A-c$ instead of $-\delta_A+c$. State: **statement accepted** (owner dispositions, 27 Oct 2026; checked as one-line algebra on TDRG-DEF-STAR and against the engine function `blow_up_star_with_snapshot`, `EV-CODE`). Use: SG-14 (the token shift lies outside $G_{\rm cov}$). Custody transfer XFER-O08-01: **deferred** to v2.13 (the RID stays OFN's). OFN REQ-O09-05 is answered by TDRG-DEF-ORIENT (endpoint policy) and this entry.
- Context only (not imported): Programme Overview v1.3 SG-PROG-1–SG-PROG-4; OFN v0.10 O0–O3 motivational layer (motivates, does not derive, TDR-G interaction laws). If a bridge theorem with the continuous programme is established (OPEN-P1), the imported claims are registered here at that time.

**Consumers** (from the consumers' own records; adopted use is read only from a consumer's Import Ledger or release record):

| Consumer (edition) | What it uses | State at v2.12.14 | Effect of v2.12.14 |
|---|---|---|---|
| NUMGEN v1.21 (`numgen-v1.21`) | state, recurrence and v18 event conventions for DISC-1/DISC-2 ("RID unavailable" imports); request `pipes/TDRG/20261026-NUMGEN-orientation-policy-s0-e-half-n.md` | received; request dispositioned (accept) | TDRG-DEF-ORIENT ruling; DISC-2 effect 20 of 136 records (§6.12); RIDs available; the C7C-M4 release is NUMGEN's |
| OFN v0.10 (`ofn-v0.10`) | IMP-O08-02 to IMP-O08-16 (state, band, holonomy, narrow-band exclusion, recurrence, star, CONV-TICK, CONV-P3CYC, four lemmas); Finding A offered under XFER-O08-01; REQ-O09-05 | Finding A: statement accepted, custody deferred | owner RIDs below replace "RID unavailable"; REQ-O09-05 answered |
| AZ v0.6 (`az-v0.6`) | Threads B/C: state (`TDRG-ZN-STATE`), LEM-REACH, LEM-RETRIG, LEM-SPECCONS | reference | `TDRG-ZN-STATE` resolves (map below); narrow-band exclusion cites `AZ-ALG-ANTIPODAL-LOWORDER` (§6.2) |
| Genesis (Programme IF25) | `TDRG-EXPORT-POLICY-PHASE` | blocked (below) | none |

Notices to NUMGEN, OFN and AZ are filed in their inboxes after the tag.

**Pins.** Governing editions at this release: Programme Overview v1.3, OFN v0.10, DSN Methodology v1.4 (this edition still declares v1.2; the migration is v2.13). Claim-specific historical pins (OFN v0.6/v0.7 at §2 TDR-1/TDR-19 and LEM-NOANNIHIL; Programme v1.1 in earlier entries) stay as written: they record what the claim was stated against.

**Owner RID map** (v2.12.14). RID names carry the category of the statement at registration (Methodology v1.4 §4.2); the names in the last column were used by consumers or the atlas before registration, resolve to the owner RID, and are not separate claims.

| Owner RID | Statement | Location | Names in use elsewhere |
|---|---|---|---|
| TDRG-DEF-ZN-STATE | phase universe; variable-size state | §6.1 | `TDRG-ZN-STATE` (AZ); OFN IMP-O08-02 |
| TDRG-DEF-PHYSICAL-STATE | quotient by global phase; $\Delta_{ij}$ | §6.1 | OFN IMP-O08-02 |
| TDRG-DEF-REL-ADVANCE | relative advance $d_{ij}$ | §6.1 | OFN IMP-O08-02 |
| TDRG-DEF-KINEMATICS | free kinematic evolution | §6.1 | — |
| TDRG-DEF-BAND | defect band $\mathcal D_k$ | §6.1 | OFN IMP-O08-03 |
| TDRG-DEF-EDGE-SET | defect edge set $E_{\rm def}$ | §6.1 | — |
| TDRG-DEF-NARROW-BAND | narrow-band condition $k<N/6$ | §6.1 | — |
| TDRG-THM-HOLONOMY | holonomy identity | §6.2 | OFN IMP-O08-04 |
| TDRG-THM-NARROW-BAND-EXCLUSION | no fully defective $K_3$ under $k<N/6$ | §6.2 | OFN IMP-O08-04B |
| TDRG-THM-RECURRENCE | finite-state recurrence | §6.2 | OFN IMP-O08-08; NUMGEN DISC |
| TDRG-DEF-CONV-TICK | step semantics | §6.3 | `CONV-TICK` (OFN IMP-O08-14) |
| TDRG-DEF-SWAP | antipodal swap | §6.3 | atlas `TDRG-SWAP` |
| TDRG-DEF-CONV-P3CYC | path successor shift | §6.3 | `CONV-P3CYC` (OFN IMP-O08-15) |
| TDRG-DEF-SIGNED-CENTERED, TDRG-DEF-SIGNED-DEFECT-ERROR | conventions of the orientation rule | §6.3 | — |
| TDRG-DEF-ORIENT | path orientation rule (v2.12.14) | §6.3 | `TDRG-ORIENT` (NUMGEN request; atlas) |
| TDRG-ALG-ORIENT-NOGO | no orientation from $(S,E)$ on the stratum | §6.3 | — |
| TDRG-DEF-CYCLE-BOUND | cycle bound states | §6.3 | atlas `TDRG-CYCLE` |
| TDRG-DEF-STAR | star blow-up | §6.3 | OFN IMP-O08-09 |
| TDRG-DEF-MULTISTAR | multistar and the policy fork | §6.3 | atlas `TDRG-MULTISTAR` |
| TDRG-DEF-CANONICAL-BRANCH | `bound_symmetric` | §6.3 | — |
| TDRG-THM-REACHABILITY-K0 | reachability at $k=0$ | §6.5 | — |
| TDRG-ALG-LEM-REACH, TDRG-ALG-LEM-NOANNIHIL, TDRG-ALG-LEM-RETRIG | two-node lemmas | §6.5 | `LEM-REACH`, `LEM-NOANNIHIL`, `LEM-RETRIG` (OFN IMP-O08-05/06/07; AZ) |
| TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK | `largest_center` ID tie-break (N1) | §6.6 | — |
| TDRG-ALG-LEM-SPECCONS | advance-spectrum conservation | §6.12 | `LEM-SPECCONS` (OFN IMP-O08-16; AZ) |
| TDRG-ALG-BIND3-CYCLE-N24K1 | exact cycle enumeration | §6.12 | `BIND3-CYCLE-N24K1` |
| TDRG-NUM-BIND3-PARITY, -SPECTRAL-GATE, -MEMORY-PARITY, -XFER, -REGEN | BIND3 results | §6.12 | `BIND3-*` |
| TDRG-ALG-ORIENT-ANTIPODAL-FIXTURE, TDRG-NUM-ORIENT-EQUIVARIANCE-N24, TDRG-ALG-MIRROR-NOT-STEP-SYMMETRY | orientation covariance | §6.12 | — |
| TDRG-ART-SESSION-SCRIPTS, TDRG-ART-ORIENT-V2-12-14, TDRG-ART-ORIENT-COVARIANCE-CHECKS | artifacts | §8 | — |

**Exports.**

### Bridge-required export candidates

These are not active exports. All are blocked until a named bridge theorem exists.

- [RID: TDRG-EXPORT-POLICY-PHASE] :: TDR-G policy-induced phase/orientation statistics for Genesis phase-moment distribution $\mathcal{M}_{\rm phase}$ :: blocked by OPEN TDR-19 and an explicit discrete-continuous bridge theorem.
- [RID: TDRG-EXPORT-DISCRETE-TRIAD] :: Native discrete triad orientation / survival statistics for TDR-T :: blocked by TDR-24D/A/B and TDR-T0.

---

## §8. Artifact and Script Registry {#sec-8-artifacts}

Custody states (Methodology v1.4 §12): **placed** — in the repository, path and SHA-256; **replayed** — an output reproduced byte-for-byte from a placed input; **held** — outside the repository with SHA-256 recorded; **missing** — no original located. Held files are never reconstructed; a re-derivation is an independent contribution, not a recovery. *(v2.12.14 register; hash check `records/tdrg/TDRG_UPLOAD_HASH_CHECK_20261027.md`.)*

- [RID: TDRG-ART-GENESIS-MC] :: `genesis_mode_b_mc.py` — the engine that produced the v17 motif corpus (header label "v15.3"; "v17" is the data-campaign label of the 258-field motif schema) :: three-policy Monte Carlo engine; `argparse` CLI (`--policy`, `--N`, `--k`, `--grid-N`, `--ratios`, `--T`, `--batch`, `--max-nodes`, `--seed`, `--audit-trials`, `--motif-log`, `--motif-stride`) :: `[ENG]` **placed** `upload/tdrg-records/genesis_mode_b_mc.py`, SHA-256 `4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608`; **replayed** for two v17 files (`motif_TEST_N120_k8_T1200_b3_v17.csv`, `de0f3e42…`; canonical-scan `motif_N120_k08_T5000_b20_v17.csv`, `7ef343b0…`; `evidence/tdrg/disposition/engine_replay_log.txt`); schema-consistent, not replayed, for the other placed v17 files; the held v17 files cannot be replayed here.
- [RID: TDRG-ART-GENESIS-MC-V18] :: `genesis_mode_b_mc_v18.py` :: convention ground truth for v2.12 (CONV-TICK audit, CONV-P3CYC); differs from TDRG-ART-GENESIS-MC only by dense-birth-window logging (same `step_universe`, `orient_path` and event rules) :: `[ENG]` **placed** `upload/tdrg-records/genesis_mode_b_mc_v18.py`, SHA-256 `9d787b435c42fd2024c81e614e3c6e3e076dc2bd30ad1e7e286ada8e6dfe675e` (byte-equal to the copy on `upload/numgen-records`). Its `orient_path` is the superseded completion (§6.3); the engine is not patched in v2.12.14 — the amended rule's reference implementation is TDRG-ART-ORIENT-V2-12-14.
- [RID: TDRG-ART-MOTIF-V6] :: `tdr_motif_bootstrap_v6.py` :: current canonical motif analysis script (bulk/tail split, multi-threshold $p_{\rm tail}$, slot-volume and structural metrics, per-run CSV, DSN patch output) :: `[ENG]` **placed** `upload/tdrg-records/tdr_motif_bootstrap_v6.py`, `3ebf064d…`; its per-run CSV and DSN-patch outputs are **missing** (not identified in any upload).
- [RID: TDRG-ART-MOTIF-V4] :: `tdr_motif_bootstrap_v4.py` :: superseded by v6; produced the 6-point $N^{-0.876}$ fit :: `[ENG]` archived; **placed** `upload/tdrg-records/tdr_motif_bootstrap_v4.py`, `86e77511…` (v1–v3, v5 and `tdr_motif_analysis*.py` are placed beside it).
- [RID: TDRG-ART-MOTIF-V17-DATA] :: v17 motif log corpus :: current canonical source data for TDR-24D/F, the extended N-scaling ($N=120$–$1440$) and the N=720/722 tail diagnosis :: `[ENG]` partly **placed** (`upload/tdrg-records/`: N=120, 240, 480, 1080 at b20; N=718 and N=840 `bound_symmetric` as zip archives; TESTGRID and TEST files), partly **held** with SHA-256 in `upload/tdrg-records/SHA256SUMS_tdrg_held.txt`: N=1200 and 1440 (b50); N=720, 722, 840 and 960 (b100, T5000).
- [RID: TDRG-ART-MOTIF-V16-DATA] :: v16 motif log corpus :: archive-valid for the TDR-24 factorization and the earlier v4 scaling; superseded for v17/v6 scaling :: `[ENG]` archived; partly **placed** (`upload/tdrg-records/*_v16.csv`), partly **held** (N=720 b100, two seeds; N=960 b100; hashes in the same manifest).
- [RID: TDRG-ART-KINEMATIC-CERTS] :: genesis-layer lemma certificates (LEM-REACH, LEM-NOANNIHIL, LEM-RETRIG, first-return period) :: finite exhaustive verification as reported in v2.12 (77,552 band cases, even $N\le40$; zero failures) :: **missing** — session-certified in an earlier session; no original located. The lemmas keep their algebraic arguments in §6.5; the finite verification is `EV-SRC-REPORTED`.
- [RID: TDRG-ART-SPECCONS] :: LEM-SPECCONS verification (signed-permutation argument; 3000 random ICs × 500 steps) :: **missing**; the algebraic argument stands in §6.12; the sampled verification is `EV-SRC-REPORTED`.
- [RID: TDRG-ART-BIND3-N24K1] :: BIND3-CYCLE-N24K1 exact enumeration (3456 post-advance ICs, both $P_3$ conventions; taxonomy, d-resolved anatomy, transfer, period spectrum) :: **missing**; the numbers are `EV-SRC-REPORTED` and carry `[conv: v18 path orientation]`.
- [RID: TDRG-ART-BIND3-SUITE] :: NKSCAN falsification suite ($k=2$ parity, spectral gate, memory stratification) :: **missing**; the numbers are `EV-SRC-REPORTED` and carry `[conv: v18 path orientation]`.
- [RID: TDRG-ART-SESSION-SCRIPTS] :: scripts of the TDR-24A/B/F, TDR-25/26, OPEN-POLICY-GEOMETRY and TDRG-RESPONSE-TENSOR entries of §2 (`tdr24a_decomposition.py`, `tdr24a_provenance.py`, `tdr24a_ratelaw.py`, `tdr24b_chi_refit.py`, `tdr24b_field_structure.py`, `tdr24f_consistency_audit.py`, `tdr24f_data_recompute.py`, `tdr24_observable_rank.py`, `tdr25_burst_bridge.py`, `tdr26_early_basin_classifier.py` with its two CSV outputs, `tdr24_policy_geometry/EXPERIMENT_DESIGN.md`, `tdr24_policy_geometry_classify.py`, `tdrg_response_tensor/BRANCH_CHARTER.md`, `response_tensor.py`, `dynamical_extractor.py`) :: `[ENG]` **held** by co-owner session claude01SKePJ as its final copies and uploaded unchanged to branch `upload/tdrg-session-scripts` (commit `386e9d4`, `SHA256SUMS.txt` there); placed on `main` after the atlas hash check. They are final copies, not shown to be the exact versions that produced each historical number.
- [RID: TDRG-ART-ORIENT-V2-12-14] :: `evidence/tdrg/scripts/tdrg_orient_v2_12_14.py` :: reference implementation of TDRG-DEF-ORIENT (drop-in `orient_path`) and of the recorded G-alternative :: `[ENG]` **placed**; exercised by the v2.12.14 checker.
- [RID: TDRG-ART-ORIENT-COVARIANCE-CHECKS] :: `evidence/tdrg/disposition/` (equivariance check, antipodal and multistar fixtures, mirror probe, engine replay log; `SHA256SUMS.txt`) and the v2.12.14 builder and checker (`evidence/tdrg/scripts/build_tdrg_v2_12_14.py`, `check_tdrg_v2_12_14.py`) :: evidence for the v2.12.14 entries of §6.3, §6.6 and §6.12 :: `[ENG]` **placed**.
- Post-edition data, not cited by any claim here: `motif_N720_k48_T5000_b500_v18.csv` (held), `motif_N840_k56_largest_center_b100_v17.csv`, `motif_N840_sweep_b100_v17.csv`, `motif_PG_N840_k56_largest_center_b100_telemetry1.csv` with its manifest, `genesis_mode_b_mc_telemetry.py` (`ba99e307…`) — placed or held as received, for the OPEN-POLICY-GEOMETRY record that will use them.

---

## §9. Collaboration and Provenance {#sec-9-provenance}

**Principal investigator:** Mustafa  
**AI / collaborator roles:** Claude · ChatGPT · Gemini · Grok  
**Archive:** rtgtheory.org · Zenodo DOI 10.5281/zenodo.17568897  
**Repository:** `MustafaAksu/rtg-corpus` (governing edition = the latest `tdrg-v…` tag with its release record); earlier archive label `rtg-resonance-2025`

Key contributed insights:

| Contribution | Status | Provenance |
|---|---|---|
| Holonomy exclusion theorem | `[THM]` | triadic discrete analysis |
| Multistar hidden-referee critique | `[ALG]` | collaborator review; $K_{2,3}$ example |
| Metric-normalization bug in `all_centers` | `[ALG]` | collaborator review; fixed by `rN_T`/`rN_s` |
| `bound_multistar` semantic split | `[ALG]` | collaborator review; multistar as bound state |
| `bound_path_tie` / `bound_symmetric` cleanup | `[DEF]` (policies), exercised `[NUM]` | in-session policy evolution |
| Optimized edge-builder audit | `[ENG]` | brute-force comparison, 500 random trials |

---

## Appendix A — Version History {#appendix-a}

### v2.12.14 — October 2026

Corrections-only edition: the owner pass after the v2.12.13 advisories (Methodology v1.2 kept as declared; no layout change; no rerun). Predecessor `tdrg-v2.12.13` (SHA-256 `aa232643…053f`). Release record `records/tdrg/TDRG_v2_12_14_RELEASE_RECORD.md`; fixed dispositions `records/tdrg/TDRG_OWNER_DISPOSITION_RECONCILIATION_v2_12_13.md`; edit log `evidence/tdrg/v2.12.14/edit_log.json`.
- **§6.3 [COR/DEF]:** TDRG-DEF-ORIENT — balanced tie extended to $S=0\wedge2E\equiv0$ (relabelling-covariant; replaces the node-ID completion at $E\equiv N/2$); TDRG-ALG-ORIENT-NOGO; `signed_centered` and `signed_defect_error` defined; the G-rule recorded, not adopted.
- **§3 [NEW]:** SG-14 relabelling covariance ($\mathrm{Sym}(V)\times\mathbb{Z}_N^{\rm phase}$; token shift and mirror outside; `largest_center` exception).
- **§6.12 [NEW/COR]:** orientation-covariance block (fixture, equivariance check, census bound, DISC-2 effect, mirror not a step symmetry); the "relabeling-covariance check" renamed mirror-inventory check; LEM-SPECCONS "equivalently" → "therefore, in particular"; BIND3 results `[conv: v18 path orientation]`, `EV-NOT-RERUN`.
- **§6.5 [COR]:** LEM-RETRIG least period (period dividing 2; fixed point at $d=0$).
- **§6.6 [NEW]:** TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK; v18-orientation guard on §§6.6–6.10.
- **§1, §2, §5, §6.8 [COR]:** N-scaling range-tagged and graded `[NUM]` (window-dependent; $-0.730$ on 480–1440); the $\chi=0.836$ consistency check withdrawn; crystallization `[HEUR]`; current state of TDR-24 D/F versus A/B/C aligned; TDR-24B current-status line; the Programme v1.2 owner-review tasks recorded.
- **Tags [COR]:** live compound tags unpacked; the local alias table replaced.
- **RIDs [NEW]:** 39 definition, claim and artifact RIDs (§7 owner RID map; consumer names `TDRG-ORIENT`, `TDRG-ZN-STATE`, `CONV-*`, `LEM-*` mapped); no OPEN-module RID renamed.
- **§7 [COR]:** imports, consumers, pins and RID map; OFN Finding A statement accepted (custody deferred).
- **§8 [COR]:** custody register (placed / replayed / held / missing) with hashes; engine identity of the v17 corpus.
- **Header, §9, Appendices B and C [COR]:** governing editions; repository named; Appendix B row for the node-ID completion; K₃ 96:1 and the T-6 wedge marked historical; TDR-T gate aligned with §1.
- **Not changed:** every scientific number; Appendix A history; the footer chain and the Appendix A order (v2.13).

### v2.12 — June 2026

Genesis-kinematics and three-node (BIND3) certification arc. Two conventions pinned to script truth; four lemmas certified; one exact-enumeration certification; one candidate refuted; one conserved quantity established; three pre-registered falsification targets executed. No changes to the TDR-24 chain or N-scaling results.

- **Header [COR]:** Title v2.12; supersedes field updated; companion documents corrected to `RTG_PROGRAMME_OVERVIEW_v1.1` and `RTG_ONTOLOGICAL_FOUNDATIONS_v0.6` (stale v1.0/v0.2 references); status summary v2.12 paragraph added.
- **§1 [NEW]:** band-form reachability note on the superselection theorem; genesis-layer kinematic lemma block; BIND3 headline.
- **§2 [NEW]:** Genesis-kinematics/BIND3 frontier added to priority ordering (items 8–12, non-blocking for TDR-T); five OPEN entries registered (OPEN-BIND3-PARITY-GEN, -MEMORY, -REGEN, -NKSCAN, OPEN-SPECCONS-STAR); settled-items list extended (four lemmas + BIND3-CYCLE-N24K1); TDR-0 note updated (failed null-return component now theorem-grade via LEM-NOANNIHIL).
- **§3 [NEW]:** scope guards SG-11 (pairwise bound-state scope), SG-12 (spectrum-conservation star firewall), SG-13 (spectral-gate scope).
- **§6.3 [COR/DEF]:** canonical step semantics named **CONV-TICK**, `[ENG audit: PASS]` v18; **CONV-P3CYC** pinned — the path-cycle permutation is the successor shift $(\delta_1,\delta_2,\delta_3)\mapsto(\delta_2,\delta_3,\delta_1)$, script-certified; prior wording under-determined a choice flipping $\sim20\%$ of finite-horizon three-body fates; coarse taxonomy shown convention-robust at the exact-cycle level.
- **§6.5 [NEW]:** LEM-REACH (band-form reachability; geometric orbit-lattice reading), LEM-NOANNIHIL (no free annihilation; replaces the trap axiom upstream — exported to OFN v0.7), LEM-RETRIG (two-node binding threshold; exact period-2 bound state); two-node regime table extended; superselection two-node scope note.
- **§6.12 [NEW SECTION]:** LEM-SPECCONS (conserved advance spectrum, signed-permutation proof, no-birth scope); BIND3-CYCLE-N24K1 `[ALG/NUM strong]` (exact taxonomy 96.4/3.6/0/0; transfer 81.8%; period spectrum; $K_3=0$; convention robustness); d-resolved anatomy table; BIND3-PARITY (replaces BIND3-KNIFE `[FAIL]`; parity-controlled survival with `[ALG]` odd-impossibility); BIND3-SPECTRAL-GATE (spectrum gates autonomous retrigger; detector-sane); BIND3-MEMORY `[COR]` + BIND3-MEMORY-PARITY (even-sector memory genuine, odd-sector composition artifact); BIND3-XFER; BIND3-REGEN; synthesis statement.
- **§8 [NEW]:** v18 script registered as convention ground truth; four session-certified artifact entries with consolidation targets (`tdrg_kinematic_certs.py`, `bind3_cycle_n24k1.py`, `bind3_nkscan_suite.py`).
- **Appendix B [NEW]:** sweep-claim `[FAIL]`; BIND3-KNIFE `[FAIL]`/`[REPLACED]`; BIND3-EQUIP `[FAIL]`; unstratified BIND3-MEMORY `[COR]`; horizon-based BIND3 percentages `[RETRACTED, numbers only]`.
- **Freeze edits (pre-OFN-v0.7 review):** §7 live import reference corrected to Programme Overview v1.1; §6.12 d-table heading and ensemble-split guard added (headline 96.4%/3.6% scoped to the 3456-IC retrigger-entry family only; one-pass rows are the regeneration-control family, not poolable); §5 high-risk ledger mirrored with three BIND3 rows (two-node retrigger / spectral gate / spectrum conservation).
- **Method note:** all four lemmas were certified by exhaustive finite verification rather than sampling where the state space permitted; the BIND3 taxonomy was promoted only after exact cycle enumeration replaced horizon classification, which had produced two successive misleading sets of percentages (windowing + convention contamination). Pre-registered falsification targets with fixed pass/fail criteria caught one of our own candidate results (BIND3-EQUIP) and demoted half of another (odd-sector memory) — recorded openly per DSN discipline.

### v2.12.13 — June 2026

Feature-map injectivity test (review-directed; resolvable without grid):
- **§2 [BRANCH/NUM]:** Tested whether richer trajectory embeddings extract structure the scalar dynamical summaries lose. Cross-channel increment & level covariance both rank-1 per run; delay-embedding "rank 8" on births exposed as a sparse-series artifact via shuffle null; null-tested occupancy delay memory gap only 0.37 (<0.5). Feature non-injectivity hides no extractable structure here — richer embeddings recover no extra temporal DOF. "Improve feature injectivity" removed from no-grid levers (tried, unrewarded). Trajectory process genuinely low-complexity on this slice.
- **Method note:** the spurious births delay-rank would have been a false structure finding without the shuffle null — caught near-miss, same null-gate discipline as Zeta and the response-tensor branch.

### v2.12.12 — June 2026

Dynamical-layer inference correction (review catch):
- **§2 [BRANCH/COR]:** Retracted the over-strong "dynamical also near-saturated / weakly argues against F3" reading. On a rank-1 control manifold both layers are forced to rank ≤ 1 regardless of true dimension; the dim-1 result is excitation-insufficiency, not structure, and cannot bear on F3. Added the second limitation: compressed features test rank(feature_summary) not rank(trajectory_manifold); injectivity unverified. Retained the surviving non-dimensional finding (inter-birth CV carries real N-dependence; autocorr times flat).
- Two grid-stage instrument questions recorded: (1) minimum excitation set to break static/dynamic projection degeneracy; (2) whether compressed features need replacing by genuine trajectory embeddings before any grid dynamical-rank>1 is trusted.

### v2.12.11 — June 2026

Response-tensor branch — dynamical signal layer (Zeta geometry-saturation response):
- **§2 [BRANCH TDRG-RESPONSE-TENSOR/NUM]:** Added trajectory-level dynamical observable layer (autocorr times, Fano, inter-birth CV, birth↔occ cross-correlation), firewalled from the static exponent pipeline. Key test "does dynamical rank exceed static rank?" → on single-lever corpus both = 1; no extra dimension surfaces. Caveats: control-rank-capped at 1 lever (lower-bound only); dynamical leading direction weak + nearly single-feature (inter-birth CV dominant, slope +0.39; leading SV 0.449 barely above null 0.432). At fixed k/N the dynamical summaries are also near-saturated, consistent with Zeta.
- **Finding:** inter-birth-interval CV is the one dynamical feature with genuine N-dependence — highest-value trajectory observable for the multi-lever grid, where the dynamical-vs-static rank divergence (F3) first becomes measurable.
- **Tooling:** `dynamical_extractor.py` added. Also: spectral_baseline.py radius bug fixed (ARPACK; see tdrg_az_export, Zeta-side audit).

### v2.12.10 — June 2026

Response-tensor branch opened (PI directive; firewalled, exploratory):
- **§2 [BRANCH TDRG-RESPONSE-TENSOR]:** Isolated branch to read TDR-G intrinsic dimension from the unnormalized response tensor (no imposed dimensions, no normalization-first). Governing axiom + premature-quotienting guard recorded. Null-gated SVD dimension reader built and synthetic-validated.
- **Calibration [honest limitation]:** reliable for dim≤1 at any cell count; under-counts dim≥2 below ~40 cells (lower bound); resists noise inflation. On current single-lever corpus: intrinsic dim = 1, HIGH confidence, upper-bounded — consistent with the rank-1 finding (charter criterion (b) met).
- **Firewall:** [BRANCH/NUM diagnostic]; no promotion to canonical TDR-G without PI approval. Artifacts: BRANCH_CHARTER.md, response_tensor.py.

### v2.12.9 — June 2026

OPEN-POLICY-GEOMETRY design refinement (review: factorization framing + existing anchor):
- **§2 TDR-24B [DEF]:** Reframed goal as factorization test O(N,k/N,π)=f(N,k/N)g(π) under operator formulation (permits coupling), replacing Layer-A/B independence language. Experiment 1 now tests multiplicativity (Case A/B/C), classifier given a factorization probe (per-observable policy-ratio consistency).
- **§2 TDR-24B [COR]:** The proposed cross-N normalization anchor is the EXISTING canonical scan (N=480–1440, k/N=1/15, bound_symmetric) — adds zero new runs. Classifier Experiment-0 report uses it live. New-run count reduced 10→4 (2 policy + 2 k/N sweep).
- **Tooling:** classifier gains Experiment-0 N-anchor report + Experiment-1 factorization probe.

### v2.12.8 — June 2026

OPEN-POLICY-GEOMETRY experimental design (Layer A / Layer B separation):
- **§2 TDR-24B [DEF]:** Specified the minimal 10-run policy/k-N matrix with pre-registered Case 1/2/3 thresholds and rank readout; verified runnable against genesis_mode_b_mc.py CLI (all 3 policies + k/N sweep execute). This is the experiment that makes field-count identifiable (lifts control_rank to 2). Compute-gated — not yet executed.
- **Tooling:** `EXPERIMENT_DESIGN.md` (matrix + exact PowerShell commands + thresholds), `tdr24_policy_geometry_classify.py` (auto-classifier; correctly reports missing cells on the single-slice corpus rather than fabricating a result).
- Scope guard recorded: no further fitting/basis-reduction/rank-tests on the saturated k/N=1/15 bound_symmetric corpus.

### v2.12.7 — June 2026

k/N-axis nature (review claim tested against §6.7 data):
- **§2 TDR-24B [NUM/COR]:** Review's "k/N is a phase boundary / foliation" framing REJECTED against §6.7: rN_T(k/N) is non-monotone with a smooth peak near 0.05–0.0667; sparse→transition→dense is a continuous crossover, not a discontinuity. The discrete selector is the multistar POLICY (bound_symmetric/largest_center/all_centers), which the DSN already separates from k/N. Correct two-axis picture: (smooth k/N) × (discrete policy); a fixed-policy k/N sweep probes a smooth rank-2 manifold.
- **§2 TDR-24B [SCOPE]:** Two-layer reading adopted in corrected form — Layer A (intra-slice rank-1 geometry, established) vs Layer B (smooth k/N + discrete policy, unsampled). Field-count and regime questions are both Layer-B, blocked on the same unsampled controls.

### v2.12.6 — June 2026

Intrinsic-dimensionality quantification + geometric-language discipline (review synthesis):
- **§2 TDR-24B [NUM]:** A single log-N axis explains 88.7% of total centered log-observable variance (residual 11.3% = finite-N scatter, N=840 + occ_in_cs noise). The TDR-24 scaling layer is an overcomplete embedding of a rank-1 flow: apparent SVD rank 3 > intrinsic rank 1. Sliding exponents, composite ratios, and the κ sign-flip are chart-dependent slopes of one 1-D trajectory.
- **§2 TDR-24B [SCOPE]:** Framing kept geometric/identifiability, not ontological — "one latent generator" remains unjustified as physics (observable rank ≠ latent field count). χ, C_component, C_birth read as coordinate charts of one flow tangent (overparameterized).
- **§2 [ADMIN]:** Clarified that the pre-existing thermodynamic-crystallization [HEUR strong] claim is independent of this rank analysis and is not upgraded or affected.

### v2.12.5 — June 2026

Formal observable-rank test (review escalation to rank-deficiency framing):
- **§2 TDR-24B [NUM]:** Built and ran the observable-Jacobian rank test. Control manifold is rank 1 on the v17 corpus (k/N fixed), so resolvable scaling directions = min(obs_rank, control_rank) = 1 irrespective of true field count — the design is rank-deficient (reviewer's sharper framing, adopted over v2.12.4's "undecidable"). Centered log-observable matrix has apparent rank 3 from finite-N scatter + one noise channel, correctly capped at 1 by control rank. Frontier restated: does adding the k/N lever raise observable-Jacobian rank above 1?
- **Tooling:** `tdr24_observable_rank.py` added (numpy-free Jacobi SVD; ready for multi-k/N corpora).

### v2.12.4 — June 2026

Decidability scope on field count (review escalation; corrects both v2.12.3 and the review's own overclaim):
- **§2 TDR-24B [SCOPE]:** Entire v17 corpus is k/N=1/15 (single lever N). On a one-parameter monotonic family the field count is not resolvable: "single latent generator" is trivially true (unfalsifiable), and v2.12.3's "two independent inputs" overclaims — occ/row and cs_rate are two projections of one resolvable scaling axis, separated only dynamically (TDR-24A mechanism), not as scaling axes. Reviewer's circular-κ identity (χ·σ≡(O_cs/row)/N) confirmed exactly; σ flat. One resolvable scaling axis on this corpus.
- **§2 TDR-24B [DEF]:** Decisive experiment recorded — k/N sweep {1/30,1/15,1/8}; locked vs decoupled exponent response distinguishes one-latent from two-field. Not runnable on the k/N-fixed corpus.

### v2.12.3 — June 2026

TDR-24B field-structure test (review-proposed 3-field basis tested against data):
- **§2 TDR-24B [NUM]:** Proposed ρ·σ·κ 3-field factorization REJECTED — separability test χ·σ≈κ gives κ~N^-1.03 not N^+1 (off by two powers); posited suppression field is flat (absorption fraction N^-0.02; all occupancy channels scale identically at N^+0.90). Clean-star collapse confirmed composite (review correct) but it is the EXISTING TDR-24A cs_rate decomposition (flat hazard × N^-0.6 conditional), not a new latent. System reduces to TWO independent inputs: occupancy/row (N^+0.90) and clean-star birth rate (N^-0.73), not three.
- **§2 TDR-24B [METHOD]:** Standing methodological note adopted: most reported exponents are quotients of a few underlying fields; test primitive-vs-ratio before promoting any exponent.
- **Tooling:** `tdr24b_field_structure.py` added.

### v2.12.2 — June 2026

Errata (collaborator catch on the v2.12.1 chi consistency note; corrects notation, strengthens the finding):
- **§2 TDR-24B [COR]:** The v2.12.1 phrasing "$C_{\rm component} - \chi = -1.633$" was invalid as written (difference of ratio-valued observables is not a scaling operation). Corrected: the certified factorization $C_{\rm birth}=C_{\rm component}/\chi$ is exact value-wise at every $N$ (because $C_{\rm component}/\chi=\texttt{clean\_stars}/\texttt{occ\_clean}$ and $\texttt{births}=\texttt{clean\_star\_components}$ is certified), and the $-1.633$ is the log-space exponent of that **ratio** ($a-b$), matching $C_{\rm birth}$ directly. Number was correct; notation was wrong.
- **§2 TDR-24B [reframe, adopted from review]:** Stated the stronger structural reduction: $\chi$ is not an independent scaling field but an amplified inverse of the clean-star-count collapse; TDR-24B introduces no new scaling degree of freedom beyond TDR-24A.

### v2.12.1 — June 2026

TDR-24B chi re-fit (v17 corpus, run-level bulk filtering; cleanup feeding the TDR-24B frontier):
- **§2 TDR-24B [COR]:** v4-era $\chi^{\rm bulk}\sim N^{+0.836}$ superseded. $\chi$ is a composite ratio, not a power law — window-dependent exponent ($+0.51$ to $+0.87$). Decomposition: numerator (occ_in_clean_star/row) flat $N^{-0.03}$; denominator (clean_star_components/row) $\sim N^{-0.73}$ carries the whole exponent. The factorization closes exponent-wise: $C_{\rm component}(N^{-0.936}) - \chi(N^{+0.697}) = C_{\rm birth}(N^{-1.633})$, $R^2\,0.976$.
- **§2 TDR-24B [revised target]:** derivation target restated as the clean-star-count collapse $N^{-0.73}$ (shared with TDR-24A's clean-star supply cap), not the composite $\chi$ exponent.
- **§6.8 [COR]:** N-scaling table $\chi^{\rm bulk}$ row reclassified from $N^{+0.836}$ power law to composite ratio.
- **Tooling:** `tdr24b_chi_refit.py` added.

### v2.11.1 — June 2026

Pre-freeze errata (collaborator review; no physics change):
- **§6 [COR]:** Stale tail-suppression sentence updated — legacy batch-20 N=718/722 controls superseded by v17 batch-100: N=722 reclassified from clean arithmetic control to stochastic-neighborhood tail witness; N=718 and N=840 remain the clean controls.
- **§2 TDR-26 [tag discipline]:** Birth-anchored rule tag split: dataset fact `[NUM cross-cell, n=2]` vs classifier claim `[HEUR]` pending batch-scale validation (the `[NUM strong]` label applied to the rule as a classifier was an overpromotion).
- **Tooling:** classifier `--out-csv` multi-file overwrite fixed (global rows with `source_file` column, written once after all files).
- **Tooling [campaign-ready]:** simulator v18 (`genesis_mode_b_mc_v18.py`) adds `--motif-dense-birth-window W`: dense (stride-1) motif logging until first\_birth+W per run, then normal stride — implementing the birth-anchored campaign spec. Functionally verified (dense/sparse transition at exactly fb+W on test runs). Batch-500 campaign at N=720/722 is launch-ready.

### v2.11 — June 2026

TDR-26 N=722 cross-cell test (pre-registered; outcome: rule revised and strengthened):
- **§2 TDR-26 [FAIL]:** Absolute-step w=200 rule failed on N=722 (TP=0/FN=1): tail run r31 dormant for 433 steps (M=4, zero occupancy) before first interaction.
- **§2 TDR-26 [NUM strong]:** r31 entered the identical defective attractor as r43 (late cs 0.812/ms-abs 0.090/b-row 0.652 vs 0.782/0.110/0.633) directly from its first interaction — a clean-star birth — with no locked phase ever forming. Two entry routes (hyperactive start vs prolonged dormancy), one attractor.
- **§2 TDR-26 [REJ]:** Dormancy duration as discriminator (defective runs at opposite first-birth extremes: step 9 vs step 434); birth-before-first-multistar (universal across all 198 bulk runs).
- **§2 TDR-26 [NUM cross-cell n=2 / HEUR classifier]:** Birth-anchored rule canonical clock: [fb..fb+200: b/step≥0.30 ∧ ms_abs≤0.25] → combined TP=2/FP=0/FN=0/TN=198, ≥2× margin at both cells. Dataset fact [NUM]; classifier validity [HEUR] pending batch validation. Thresholds chosen on n=1, survived n=2.
- **§2 TDR-26 [DEF]:** Campaign spec updated: dense logging to first-birth+300 (birth-anchored).
- **Tooling:** classifier `--anchor-birth` mode added; docstring updated with the full n=2 record including the failed absolute-step rule.

### v2.10.1 — June 2026

Errata (collaborator verification of the classifier; no claim change):
- **§2 TDR-26 [COR]:** w≤100 description corrected: r43 is rank-2, not rank-1, in both raw metrics (r48 higher on cs\_frac 0.867 vs 0.715; r3 higher on b/step 0.420 vs 0.350). r43 is an extreme z-score outlier at w≤100 but cleanly separated only at w≤200. Rule TP=1/FP=0/FN=0/TN=99 independently re-verified by collaborator.
- **Tooling:** classifier docstring updated to match.
- **Queued:** N=722 cross-cell test (n=1→n=2 validation) pending upload of motif_N722 v17 log; command pre-specified.

### v2.10 — June 2026

TDR-26 early-basin discriminator study (sub-question (a), N=720 v17):
- **§2 TDR-26 [NUM strong]:** Separability timeline established: not separable at w≤50; extreme z-score but rank-2 (not separated) at w≤100; clean gap on b/step at w≤200 (r43 0.490 vs bulk max 0.250, 1.96×), widening at w≤300 (2.75×).
- **§2 TDR-26 [COR]:** cs\_frac alone is NOT the discriminator — bulk runs r48/r90/r92 reach 0.70–0.87 early cs\_frac on few candidates and all engage the lock by w=200. The discriminator is **sustained birth production** (rising vs collapsing b/step).
- **§2 TDR-26 [HEUR, n=1]:** Candidate rule at w=200 (b/step≥0.30 ∧ ms\_abs≤0.25): TP=1/FP=0/FN=0/TN=99. Explicitly tagged as fit on one defective run — not validated.
- **§2 TDR-26 [DEF]:** Decision tree resolved to the STRONG branch; next-campaign spec recorded (batch ≥500 at N=720/722, dense early logging to step 300, ~5 expected defective runs, validate/refit rule, measure basin-entry probability).
- **Tooling:** `tdr26_early_basin_classifier.py` added; per-run early metrics exported to `tdr26_early_basin_N720_v17.csv`.

### v2.9 — June 2026

TDR-25/26 bridge part 2 — N=720 onset test (collaborator-executed, Claude-verified):
- **§2 TDR-25 [REJ]:** Single-step burst-size quantile explanation of the runaway rejected. r43 max burst $26.95\times\bar{O}$ < bulk max $43.8\times$; zero r43 rows ≥30×/50×/100×. N=720 bulk confirmed in the clean-cell shedding family.
- **§2 TDR-25 [REVISED]:** v2.8 failed-relock hypothesis revised — too late-stage. r43 entered the clean-star basin in the pre-lock transient (cs-frac 0.72 at steps 1–100) and never converged (ms-absorption pinned ~0.110 vs bulk 0.734 over all 5000 steps; oscillatory, not centerless).
- **§2 TDR-25/26 [HEUR strong]:** Mechanism: early lock-nonengagement / persistent relock-defective attractor. Bifurcation = basin entry during early growth, not burst magnitude.
- **§2 TDR-26 [reframed]:** Now the basin-selection problem, with three posed sub-questions (early discriminator; finite-time decision; arithmetic-neighborhood bias).
- **Tooling [ADMIN]:** `tdr25_burst_bridge.py` onset guards added (`--onset-min-M`, `--onset-min-step`); unguarded detector documented as firing on the step-9 pre-lock transient. Guarded onsets verified at steps 122 / 812 with no preceding mega-burst.

### v2.8 — June 2026

TDR-24A → TDR-25/26 bridge study, part 1 (clean cells):
- **§2 TDR-25 [NUM strong]:** Burst-size survival functions collapse across N=480–1440 (one N-stable shedding family); distribution truncates sharply at 42–55×$\bar{O}$, no heavy tail in clean cells. Monotone unlock gradient established (births/row 0→0.4, centers 53→29, frac\_cs 0→0.045 with burst size).
- **§2 TDR-25 [NUM]:** Compositional gap identified: top-band frac\_cs ≤0.05 vs runaway 0.78–0.81; extrapolation needs ~300×$\bar{O}$ bursts, ~6× beyond truncation. Runaway is NOT a smooth quantile of single-step burst size.
- **§2 TDR-25 [HEUR strong]:** Failed-relock hypothesis posed: runaway = ordinary-scale burst with persistent snap-back failure (consistent with TDR-24A single-step provenance).
- **§2 TDR-25 [DEF]:** Falsifiable onset prediction recorded for the N=720 log (part 2); `--onset` analysis mode implemented.
- **Tooling:** `tdr25_burst_bridge.py` added (survival functions, unlock-gradient bands, onset profiler).

### v2.7.1 — June 2026

Pre-freeze corrections (collaborator review; wording + tooling, no claim changes):
- **§2 TDR-24A [COR]:** Stale "clean-star supply cap" lead-problem sentence replaced with the post-R1/R2 residual (derive $P(\text{exposure}|B)\sim N^{-0.6}$ from debris-recapture competition). Burst statement split into three distinct quantities: $P(B)\sim N^0$, $P(B|\text{cs})=0.85$–$1.00$ (coverage), $P(\text{cs}|B)\sim N^{-0.6}$. Status line set to ACTIVE / mechanism-resolved / analytic residual sharp.
- **Tooling [traceability]:** `tdr24a_ratelaw.py` now outputs coverage $P(B|\text{cs})$ and the successful-vs-sterile burst diagnostics (flood/center/recapture ratios) so every DSN claim in the R1/R2 block is reproducible from one script run. Both `tdr24a_ratelaw.py` and `tdr24a_decomposition.py` now group by (policy, T, k/N) slice with same-cell pooling and refuse silent cross-slice fitting.
- Coverage figure widened from "93–100%" to "0.85–1.00" to reflect the full $\lambda\in\{2,5,10\}$ range (the $\lambda{=}10$, N=480 cell gives 0.85).

### v2.7 — June 2026

TDR-24A rate-law pass (R1/R2/R3, collaborator-directed):
- **§2 TDR-24A [NUM strong]:** cs\_rate decomposed under two conditionings. Center-deficit conditioning rejected (threshold-dependent split). Other-burst conditioning accepted (threshold-stable): $P(B)\sim N^0$ flat (R1: shedding hazard N-independent, ~4–9% of steps, coverage 93–100%), $P(\text{cs}|B)\sim N^{-0.6}$ (R2: conditional exposure carries the entire exponent).
- **§2 TDR-24A [NUM]:** Successful bursts vs sterile: larger floods, 3–4× lower multistar recapture. Bottleneck identified as debris-recapture competition.
- **§2 TDR-24A [NUM]:** R3 — per-event attachment $N^{+0.766}$ is sublinear vs band; distinct from TDR-24F's full-band $q_{\rm proj}$ closure.
- **§2 TDR-24A [SCOPE]:** Rational-exponent caution recorded ($-0.669$ near $-2/3$ unproven; conditional $-0.58\ldots-0.61$ inconsistent with $-2/3$).
- OPEN target finalized: derive $P(\text{exposure}|\text{burst})\sim N^{-0.6}$ from debris-recapture competition.
- **Tooling:** `tdr24a_ratelaw.py` added; `tdr24a_decomposition.py` rekeyed to (policy,T,N,k) cells (collaborator requirement for canonical tooling).

### v2.6 — June 2026

TDR-24A Level-1 provenance extraction + v2.5 housekeeping:
- **§2 TDR-24A [NUM strong]:** Clean-star provenance signature established (N=480–1440, N-stable): 7–10× candidate load on clean-star rows concentrated in the `other` channel (22–33×), ~30% transient multistar center depletion with component count unchanged. Event-centered profile (N=1440): anomaly strictly single-step (offset 0 only). Burstiness grows with N (gap ratio 0.79→0.41).
- **§2 TDR-24A [NUM strong]:** Numerator decomposed exactly: cs\_rate $\sim N^{-0.669}$ × per-event attachment $\sim N^{+0.766}$ = $N^{+0.096}$ (measured $+0.095$). The flat numerator is a band-compensation, structurally analogous to TDR-24F's $q_{\rm proj}\sim(2k+1)$.
- **§2 TDR-24A [HEUR strong]:** Mechanism: clean stars are fingerprints of single-step partial-unlocking events (shed→expose→fire→re-lock). Remaining OPEN narrowed to the rate law cs\_rate $\sim N^{-0.67}$.
- **Housekeeping [COR]:** header corrected v2.2→v2.5 regression; §6.8 local guard updated to N=120–1440; stale "TDR-24F lead subproblem" line replaced; dual-suppressor paragraph demoted `[HEUR]`→`[COR]` range-tagged.
- **Tooling:** `tdr24a_decomposition.py` same-cell pooling fixed (collaborator catch); `tdr24a_provenance.py` added.

### v2.5 — June 2026

TDR-24A partial resolution (decomposition study):
- **§2 TDR-24A [NUM strong]:** $C_{\rm component}$ decomposed: numerator (occ\_in\_clean\_star/row $\sim N^{+0.10}$, near-flat) over denominator (occ\_clean/row $\sim N^{+0.945}$). Mechanism: geometric dilution — N-independent per-axis clean-candidate probability ($p\in[0.028,0.034]$, verified) times $N/2$ antipodal axes gives a linearly growing pool; a saturated clean-star supply (multistar locking, ms\_components/row flat) gives a flat numerator.
- **§2 TDR-24A [ALG candidate]:** Denominator $\sim N^1$ counting argument recorded as derivable.
- **§2 TDR-24A [COR]:** Composite $C_{\rm component}$ exponent flagged as range-dependent ($-0.72$ over 120–1080, $-0.85$ over 480–1440), not a true power law; canonical $-0.757$ is range-tagged.
- Remaining for closure: derive the N-independent clean-star supply cap from the stationary measure.
- Artifact: `tdr24a_decomposition.py`.

### v2.4 — June 2026

TDR-24F refinement (collaborator cross-check + methodology hardening):
- **§2 TDR-24F [REVISED]:** The $q_{\rm proj}\sim N^{1.371}$ figure is reclassified from "fit artifact" to **convention artifact** — reproducible under a ratio-of-aggregates convention over the full scan (verified: 1.276–1.371 depending on aggregation), but not the canonical projection law. Canonical run-level/pool-level conventions give $q_{\rm proj}\sim N^{1.04}$–$N^{1.07}$. Canonical law fixed at $N^{1.0}$.
- **§2 TDR-24F [SCOPE]:** Added high-N scope guard — $\bar{c}_{\rm struct}$ bounded (4.5–5.8) only for $N\ge480$; N=120 ($\approx12.6$) and N=240 ($\approx7.5$) are finite-size transients, excluded from asymptotic claims.
- **§2 TDR-24F [ADMIN]:** Recorded that raw-motif TDR-24F recomputation must use run-level (final\_M) bulk filtering, not row-level ($M_{\rm pre}$) filtering, to prevent tail-run leakage at locking-failure cells.
- **Tooling:** `tdr24f_data_recompute.py` upgraded to run-level bulk filtering and same-N pooling; `tdr24f_consistency_audit.py` `--csv` placeholder removed.

### v2.3 — June 2026

TDR-24F resolution (data-driven, two independent methods):
- **§2 TDR-24F [RESOLVED]:** Structural-to-slot projection mechanism closed `[NUM strong]`. From v6 per-run output (N=120–1080) and pool-level ratio-of-sums on raw v17 logs (N=480,840,1200,1440): $q_{\rm proj}\sim N^{+1.06}$ (both methods: 1.065, 1.066), $\bar{c}_{\rm struct}\approx4.5$–$5.0$ bounded, $\psi_{\rm slot}^{\rm bulk}$ intensive. The reported $q_{\rm proj}\sim N^{+1.371}$ is `[FAIL]` (fit artifact). Slot identity closes exactly: $1.066+(-0.066)=1.000$.
- **§1, §2, §5 [COR]:** Frontier gate, priority chain, dependency box, and high-risk ledger updated to reflect TDR-24F closed; remaining gate is TDR-24A → TDR-24B → TDR-24C.
- **Mechanism:** bounded structural leaf reservoir ($\approx5$/component) with projection efficiency $q_{\rm proj}\sim(2k+1)\sim N$ exactly offsetting the band; product is intensive $\psi\sim N^0$. Analytic derivation of the constant $\bar{c}_{\rm struct}\approx5$ remains `[OPEN]`.
- Audit artifacts: `tdr24f_consistency_audit.py`, `tdr24f_data_recompute.py`.

### v2.2 — June 2026

v17/v6 canonical scientific update (changes claim status; not merely errata):
- **§1, §6.8 [COR]:** Canonical bulk scaling updated to v17/v6 extended scan ($N=120$–$1440$): $B_{\rm bulk}/\text{step} \sim 1.041\,N^{-0.869}$ ($R^2=0.973$), superseding the v4 6-point $N^{-0.876}$ fit. Full bulk fit table replaced; $M_{\rm bulk}$, $O_{\rm slot}$, $\psi_{\rm slot}$ rows added.
- **§1, §2, §6.8 [PROMOTE]:** Slot-volume model promoted from `[HEUR strong]` to `[ALG / NUM strong]`. $\psi_{\rm slot}^{\rm bulk}\approx0.00204\,N^{+0.014}$ verified intensive. OPEN TDR-24D closed and moved to Settled items.
- **§2 [NEW]:** OPEN TDR-24F (structural-to-slot projection closure) added as the new lead subproblem. The reported $q_{\rm proj}\sim N^{1.371}$ is flagged as exponent-inconsistent with $\psi\sim N^{0.014}$ and must be re-derived.
- **§6.8 [NEW]:** N=840, 1200, 1440 rows added to N-scaling table.
- **§2 TDR-24N, §6.9 [COR]:** Required cells marked done; N=840 7-divisible clean control added as decisive arithmetic falsification; N=722 matching locking-failure tail recorded.
- **§2 TDR-25/26 [COR]:** Tail law revised — matching rare tails at both N=720 and N=722; stochastic neighborhood phenomenon, not N=720-singular.
- **§6.10, §5 [COR]:** $V_{\rm pair}$ corrected to $V_{\rm pair\_load}$ — a load diagnostic that may exceed 1, not a fraction. Prior "0.62 = 62%" reading retracted.
- **§8 [COR]:** Artifact registry updated to v6 script / v17 data canonical; v4/v16 archived.
- **§6.11 [NEW]:** Slot-volume and structural observables added.

### v2.1 — June 2026

Canonical-freeze errata applied over v2.0 (audit gap-closure; no scientific claims changed, only completeness):
- **§6.11 [NEW]:** Added `p_cap`, `mean_steps_taken`, `ms_res`, `ms_trap` to observable definitions; expanded `ms_bound`/`ms_bpe` semantics.
- **§6.7 [NEW]:** Added k/N three-regime characterization `[NUM]` (sparse/bimodal at 0.033, transition at 0.050, dense at ≥0.067).
- **§6.7 [COR]:** Exact long-horizon late-rate values recorded (rN_late=0.0201 at T=5000, 0.0202 at T=10000); full rN_late/rN_T ratio progression added.
- **§6.6 [NEW]:** Multi-birth promoted to `[NUM strong]` universal result; added `largest_center` rN_late_birth=0.9995 inflation result `[NUM]`; added ms_bpe 1.00 vs 33.91 expansion-character distinction `[ALG/NUM]`.
- **§6.4 [NEW]:** Added brute-force edge-builder audit record `[ENG/ALG]` (500 trials, 0 mismatches).
- **§6.8 [COR]:** Clarified exponent-consistency checks are approximate (fitted), not algebraic identities.

### v2.0 — June 2026

Full refactor to DSN_METHODOLOGY_v1.2 architecture. Active TDR-G scientific ledger content is preserved; motivational, cross-branch, and provenance material is routed to companion documents or appendices.

Errata and additions applied before canonical freeze:
- **§2 [NEW]:** Priority ordering block added at top of OPEN Registry.
- **§2 [COR]:** TDR-24C dependency corrected to require TDR-24D; extension sentence added for $B_{\rm bulk}/\text{step}$ suppression.
- **§2 [NEW]:** TDR-24N specific required batch cells added (N=718, 722, 840, 1200, 1440).
- **§2 [COR]:** "Closed OPENs" renamed to "Settled / routed items"; TDR-0 wording fixed; Finite-state recurrence `[THM]` added to settled list.
- **§2 [COR]:** TDR-22c marked as diagnostic refinement of TDR-22a.
- **§6.2 [NEW]:** Finite-state recurrence `[THM]` added — every orbit is eventually periodic.
- **§6.3 [NEW]:** Canonical step semantics `[DEF]` added (7-step order); `M_pre` convention stated.
- **§6.4 [NEW]:** Valid v16 motif log `[DEF]` added (5-condition validity criterion).
- **§6.5 [COR]:** Decorative box replaced with `[RESULT]` tagged claim.
- **§6.7 [NEW]:** N=240 long-horizon band `[NUM]` result added.
- **§6.10 [COR]:** Heading tag corrected to `/ mixed`; decorative box replaced with `[HEUR strong]` mechanism summary; $V_{\rm pair}$ multistar vacuum fraction `[NUM]` result added ($N=240$: $V_{\rm pair}\approx0.62$).
- **§7 [NEW]:** Bridge-required export candidates block added (blocked under OPEN-P1 and TDR-19).
- **§A.sim [COR]:** Noncanonical tags `[FAIL bug]`, `[HEUR design]`, `[ALG design]` converted to canonical `[FAIL]`/`[HEUR]`/`[ALG]` with `[scope: ...]` qualifiers; decorative box → `[RESULT]`.
- **Appendix B [COR]:** `[FAIL as primary]` → canonical `[FAIL]` `[scope: as primary explanation]`.
- **Appendix A marker string [COR]:** Literal HTML marker string replaced with plain text.

- **§0 [REMOVED]:** Executive Status boxed equations → promoted to §1 (Current Canonical State).
- **§1 [REMOVED]:** Local tag table → replaced by `DSN_METHODOLOGY_v1.2` reference + Local Tag Aliases.
- **§4 [REMOVED]:** Genesis Motivation / Gauge Cleansing → content now lives in `RTG_ONTOLOGICAL_FOUNDATIONS_v0.2`. New §6.3 contains a local guard pointer.
- **§25 (Part XIX) [REMOVED]:** Cross-branch scope definitions → now covered by Programme Overview SG-PROG-1 and this document's SG-10. Table of permitted/forbidden transfers absorbed into SG-10.
- **Part XX (TDR-T) [RETAINED]:** Discrete Triadic Requirements Ledger moved to Appendix C.
- **Changelogs v1.1–v1.5 [MOVED]:** To Appendix A subsections below.
- **Simulation version history §14 [MOVED]:** To Appendix A §A.sim.
- **Tag dialect normalized:** `[NUM-strong]` → `[NUM strong]`; `[HEUR-strong]` → `[HEUR strong]`; declared as local aliases for backward compatibility.
- **Persistent anchors added** to all §6 subsections.
- **AI Context Core marker:** Inserted at end of §4.

### v1.5 — May 2026

- Slot-volume formula corrected to use $M_{t,\rm pre}$ (per-step pre-birth count) rather than $M_{\rm final}$ proxy.
- Multistar clustering model added to OPEN TDR-24D: $\psi_t \approx \bar{c}(N,k)/(2k+1)$.
- TDR-24N added (finite-size neighborhood anomaly audit for N=718–1440).
- TDR-0 scope extended with six structural constraints on discrete mechanism.
- R4 triadic classification corrected: fully defective $K_3$ is forbidden `[THM]`.
- R11 module ladder added.
- Scope Guard §3 item 11 bidirectionalized.

### v1.4 — May 2026

- TDR-0 hypothesis formalized as `[HEUR]` with explicit scope guard.
- TDR-24D derivation context: uniform-distribution baseline recovers rejected M² model.
- TDR-T Triadic Requirements Ledger added.
- Dependency ordering hardened: TDR-24D → TDR-24A/B → TDR-T.

### v1.3 — May 2026

- Cross-branch scope definitions added (now SG-10 and Programme Overview SG-PROG-1).
- Scope Guard §3 item 11 added.
- TDR-24D slot-volume model added.

### v1.2 — May 2026

- TDR-24 factorization `[ALG/NUM]`: $C_{\rm birth} = C_{\rm component}/\chi$.
- Motif logging infrastructure documented.
- Birth identity certified: `births_step = clean_star_components`.
- N-scaling table extended to N=718, 722, 960, 1080.
- Arithmetic control section added; arithmetic explanations rejected.
- N=720 tail mechanism characterized.
- Growth laws updated to bulk-conditioned $B_{\rm bulk}/\text{step} \sim N^{-0.876}$.
- OPENs TDR-24A/B/C/D, TDR-25, TDR-26 added.

### v1.1 — May 2026

- CLI support documented.
- Path orientation law added.
- Cycle bound states added.
- Simulation version history recorded.
- T=2000/5000/10000 long-horizon data integrated.
- N=480 non-monotonicity registered.
- `rho` defect-density result added.
- Growth-law heuristics registered.
- OPEN TDR-22 split; OPEN TDR-24 added.

### §A.sim — Simulation Artifact Evolution `[ENG]`

| Version | Issue / change | Status |
|---|---|---|
| v1–v2 | `k13_star` naming mismatch silenced births | `[FAIL]` `[scope: implementation bug]`; early zero-inflation results invalid |
| v3 | Star string fixed; births occur | `[ENG]` |
| v4 | General $P_n$ paths; $C_4$ bound state | `[ENG]` |
| v5 | All cycles $C_n$ bound; late-rate observables | `[ENG]` |
| v6 | Signed path orientation; birth-first routing | `[HEUR]` `[scope: design choice]` |
| v7 | Strict locality; all components processed | `[ALG]` `[scope: design invariant]` |
| v7.2 | Multistar centers detected; hidden referee removed | `[ALG]` |
| v8–v10 | Policy comparison; metric bug fixed via `rN_T`/`rN_s` | `[ALG]` |
| v11–v12 | `bound_multistar`, `bound_path_tie`, clean crystallization | `[NUM]` |
| v13 | CLI support + corrected `orientation_ties` counter | `[ENG]` |

`[RESULT]` Policy and bookkeeping bugs can invert the cosmological interpretation.

---

## Appendix B — Retired and Rejected Claims {#appendix-b}

- [FAIL] Sine coupling as a primitive TDR-G interaction law — imports smooth continuum without derivation.
- [FAIL] Total additive momentum $P = \sum \delta_i$ as a conserved physical observable — gauge artifact.
- [FAIL] $\sum \delta_i^2$ conserved under birth — increases by $\delta_A^2$.
- [FAIL] All three triad edges can simultaneously defect under narrow band — holonomy exclusion theorem.
- [FAIL] Arbitrary path label fallback as tie-breaking — background-independence violation.
- [FAIL] *(v2.12.14)* Path-orientation completion by node-ID listing at $S=0\wedge E\equiv N/2$ (the v17/v18 engine's `orient_path` with `raw_ordered_path`, standing in for the v2.12.13 rule there) — not relabelling-covariant (TDRG-ALG-ORIENT-ANTIPODAL-FIXTURE): an unintended instance of the arbitrary-label fallback above. Replaced by the extended balanced tie (TDRG-DEF-ORIENT). Results computed under it are kept with `[conv: v18 path orientation]`.
- [FAIL] First valid star center as multistar resolution — hidden label/referee bias.
- [FAIL] v7 runaway inflation was universal — multistar bias artifact.
- [FAIL] *(v2.12)* "Any nontrivial dyad orbit sweeps the antipodal band" — false; orbits are cosets $\Delta_0+g\mathbb{Z}_N$ and non-intersecting cosets never reach the band. Superseded by LEM-REACH (§6.5).
- [FAIL] *(v2.12)* **BIND3-KNIFE** — "pure-bound survival is tied to the marginal class $|d|_c=2k$" — refuted by the $k=2$ scan (deep even class $d=\pm2$ survives; all odd classes have zero survivors at both $k$). Replaced by BIND3-PARITY (§6.12).
- [FAIL] *(v2.12)* **BIND3-EQUIP** — near-equipartition of band occupancy in initially bound BIND3 families — refuted by the d-resolved anatomy ($f_{AB}\approx2\times f_{AC/BC}$ in even-advance classes); equipartition holds only in non-binding-entry controls. Replaced by BIND3-MEMORY-PARITY (§6.12).
- [COR] *(v2.12)* Unstratified BIND3-MEMORY claim — composition-mixed; genuine memory is confined to even-advance spectrum classes (§6.12).
- [RETRACTED] *(v2.12, numbers only)* Horizon-based BIND3 percentages (all pre-exact-enumeration classifications, including the non-canonical-rotation and pre-advance-IC runs) — windowing and convention contamination; taxonomy categories stand; exact values are those of BIND3-CYCLE-N24K1 (§6.12).
- [FAIL] $T=500$ $mf \approx 30$–$52$ is asymptotic equilibrium — $T=1000+$ showed continued growth.
- [FAIL] Fixed $N=120, k=8$ freezes — slow accretion persists through $T=10000$.
- [FAIL] Logarithmic growth established — data favors slow accretion with nontrivial exponent.
- `[FAIL]` `[scope: as primary explanation]` $B/\text{step} \sim N^{-1}$ (aggregate) — tail-inflated; bulk-conditioned value is $N^{-0.876}$.
- `[FAIL]` `[scope: as primary explanation]` Final-$M$ mean scales as $N^{-0.416}$ — tail-contaminated; bulk-conditioned value $\approx N^{-0.26}$.
- [FAIL] Simple divisor count explains $N=720$ tail.
- [FAIL] $3^2 \mid N$ alone explains tails.
- [FAIL] 15-commensurability fraction alone explains tails.
- [FAIL] $N=720$ is deterministically unstable.
- [FAIL] $O \sim M^2 \cdot (2k/N)$ as occupancy model — wrong structural dependence; predicts negative N-scaling.
- [FAIL] $K_3$ globally explosive — only a quartic pump *channel* exists; the full six-step return has dominant healing terms (96:1 healing/pump ratio). See Triadic DSN. *(v2.12.14: historical continuous reference — TRIAD v1.6.1 keeps 96:1 as coefficient bookkeeping with the same-object correspondence OPEN; not a current fact about either branch.)*

---

## Appendix C — Discrete Triadic Requirements Ledger (TDR-T) {#appendix-c}

> **Gate condition:** Do not begin full discrete triadic dynamics until TDR-24A → TDR-24B → TDR-24C close (TDR-24D and TDR-24F are closed at the mechanism level, §1). *(v2.12.14 `[COR]`; aligned with §1 and §2.)*

### Module Ladder

| ID | Module | Purpose | Prerequisite |
|---|---|---|---|
| TDR-24D | Slot-volume identity | Derive candidate-pool scaling | closed (mechanism level) |
| TDR-24A | Topological filtering | Derive multistar suppression | Immediate |
| TDR-24B | Geometric compression | Derive component compression | Immediate |
| TDR-T0 | Discrete triad definition | Classify clean/embedded/degenerate | TDR-24 closed |
| TDR-T1 | Discrete chirality | Derive $\theta_{\rm disc}$ analog | TDR-T0 |
| TDR-T2 | Birth-policy orientation | Compute $\theta_{\rm birth}^{\rm TDR}$ | TDR-T1 |
| TDR-T3 | Safe-wedge reachability *(historical continuous reference: the sector/wedge imports were withdrawn by TRIAD v1.6.1 CN-05; to be restated natively before use)* | Determine if safe orientation reachable | TDR-T2 |
| TDR-T4 | Triad survival scaling | Large-N survival laws | TDR-T3 |

### Structural Requirements

**R0** `[ALG structure]` Continuous tensors and coefficients ($1/3$, $3/4$, $x_*$, $-32r^4$, Plücker constants) cannot be used in TDR-G unless reproduced by a native $\mathbb{Z}_N$ derivation. *(v2.12.14: $x_*$ is a historical root of the continuous T-6 chain, and TRIAD v1.6.1 withdraws its safe-wedge reading (CN-05); it is listed here only as a historical example.)*

**R1** `[DEF]` Native state space: $\mathbb{Z}_N$, $k$, $\mathcal{D}_k$, $E_{\rm def}$, component map. Discrete closure: $\Delta_{AB}+\Delta_{BC}+\Delta_{CA}\equiv0\pmod{N}$ already certified `[THM]`.

**R2** `[OPEN]` Multistar vacuum prerequisite: TDR-24A → TDR-24B → TDR-24C must close before discrete triadic dynamics (TDR-24D and TDR-24F are closed at the mechanism level).

**R3–R10** `[OPEN reserved]` Reserved for the future `RTG_DISCRETE_BIRTH_DSN` / TDR-T document. Do not cite as active OPEN Registry entries until TDR-T0 is opened.

Native discrete triad classes (under $k < N/6$):

| Class | Definition |
|---|---|
| Fully defective $K_3$ | All three edges in $E_{\rm def}$; **forbidden** under narrow band — null class only |
| Active path triad $P_3$ | Exactly two defect edges; current native interaction class |
| Clean path triad | $P_3$ not embedded in multistar component |
| Embedded path triad | $P_3$ inside multistar component |
| Star-supported triadic germ | $K_{1,3}$-like in $K_4$; birth precursor |
| Degenerate orientation class | Zero or ambiguous cyclic order |
| Multistar-shell triad | Triadic substructure inside bound multistar shell |

---

*END OF DOCUMENT — RTG_DISCRETE_GENESIS_DSN_v2.12.14*  
*Supersedes RTG_DISCRETE_GENESIS_DSN_v2.12.13 (tag `tdrg-v2.12.13`), RTG_DISCRETE_GENESIS_DSN_v2.12.12, RTG_DISCRETE_GENESIS_DSN_v2.12.11, RTG_DISCRETE_GENESIS_DSN_v2.12.10, RTG_DISCRETE_GENESIS_DSN_v2.12.9, RTG_DISCRETE_GENESIS_DSN_v2.12.8, RTG_DISCRETE_GENESIS_DSN_v2.12.7, RTG_DISCRETE_GENESIS_DSN_v2.12.6, RTG_DISCRETE_GENESIS_DSN_v2.12.5, RTG_DISCRETE_GENESIS_DSN_v2.12.4, RTG_DISCRETE_GENESIS_DSN_v2.12.3, RTG_DISCRETE_GENESIS_DSN_v2.12.2, RTG_DISCRETE_GENESIS_DSN_v2.12.1, RTG_DISCRETE_GENESIS_DSN_v2.12, RTG_DISCRETE_GENESIS_DSN_v2.11.1, RTG_DISCRETE_GENESIS_DSN_v2.0 (errata/gap-closure lineage), and TDR_G_DISCRETE_RELATIONAL_GENESIS_DSN_v1.5. v2.12 adds the genesis-kinematics and BIND3 certification arc: CONV-TICK/CONV-P3CYC pinned to script truth (v18); LEM-REACH, LEM-NOANNIHIL, LEM-RETRIG, LEM-SPECCONS certified; BIND3-CYCLE-N24K1 exact enumeration; BIND3-PARITY / SPECTRAL-GATE / MEMORY-PARITY certified by the pre-registered falsification suite; SG-11–SG-13; five new OPENs. Active TDR-G scientific ledger content is preserved or routed; structure conforms to DSN_METHODOLOGY_v1.2.*
