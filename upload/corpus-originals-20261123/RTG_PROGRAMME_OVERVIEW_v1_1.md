# RTG_PROGRAMME_OVERVIEW_v1.1

**Title:** Relational Time Geometry — Programme Overview and Study Hierarchy  
**Date:** June 2026  
**Authors:** Mustafa (PI) · Claude · ChatGPT · Gemini · Grok  
**DSN Methodology:** DSN_METHODOLOGY_v1.2  
**Archive:** rtgtheory.org · Zenodo DOI 10.5281/zenodo.17568897  
**Status summary:** The RTG programme has two active parallel branches — a continuous effective-dynamical branch and a discrete constructive-substrate branch — with four programme-level open-problem clusters connecting them. The continuous branch has strong algebraic closure at Level B maturity (certified dynamics, open generator selection and downstream UV/Regge gates). The discrete branch has strong numerical and structural closure at Level B maturity (open interaction/policy derivation and continuum bridge). No result flows between branches without a named bridge theorem.

---

## 0. What This Document Is

This is the Tier 0 navigation document for the RTG programme. It:

- states the programme's scientific mission,
- characterizes the historical arc from ESM origins to current studies,
- defines the two-branch architecture and why both branches are scientifically necessary,
- lists all active sub-studies with scope, maturity level, and current status,
- registers the four programme-level open-problem clusters,
- specifies the programme-level scope guards that govern all sub-study documents,
- provides the cross-study dependency graph.

This document carries no derivations. Claims in this document are `[HEUR strong]` or `[HYP]` unless tagged otherwise. It is updated when new studies are opened, when programme-level open problems are resolved, or when the branch architecture changes.

---

## 1. Programme Mission

`[DEF]` **RTG (Relational Time Geometry)** is a research programme investigating whether continuous spacetime geometry — including metric structure, dimensional count, and gravitational coupling — can emerge from a pre-geometric substrate governed solely by relational distinguishability principles.

The programme's central question:

> Can a universe with no pre-given metric, no external time, and no absolute position generate the appearance of smooth 3+1 dimensional geometry through internal relational dynamics?

The programme pursues this through two structurally independent strategies that represent different hypotheses about what the primitive substrate is.

---

## 2. Historical Arc

### 2.1 ESM Studies (Phase 0)

`[ENG]` The programme originated from node-based universe models published at rtgtheory.org. These early studies explored whether a network of interacting nodes with local relational rules could exhibit organized large-scale structure. Key outputs: identification of relational interaction as the generative mechanism, rejection of externally imposed forces, first evidence of self-organizing behavior.

**Status:** Foundational provenance. Formal bridge from ESM results to current study objects has not been derived. Registered as dependency in `[bridge-required]` status.

### 2.2 L0 / L1 / L2 Studies (Phase 1)

`[ENG]` Systematic development of the relational interaction framework. The L0/L1/L2 studies introduced the continuous dyad generator $T(\rho,\eta)$, the zero-origin condition $\mathcal{O}_0 = 0$, the first dyad $(0 \to (A,B),\ A+B=0)$, and the relational quadratic form $Q = \rho^2 - \rho\eta + \eta^2$. In the current DSN corpus, $T$ is treated as the postulated/canonical effective continuous generator until OPEN-P0 is resolved.

**Status:** Partially absorbed into the Genesis DSN preamble. Formal standalone provenance document not yet created. See proposed Tier 2 document `RTG_PRIMITIVE_ONTOLOGY` in §6.

### 2.3 Current Programme (Phase 2 — active)

Two parallel branches operating simultaneously with an explicit structural firewall between them. See §3.

---

## 3. Two-Branch Architecture

### 3.1 Why Two Branches Exist

The RTG programme currently pursues two structurally different answers to the substrate question. These are not merely different technical approaches to the same model — they reflect genuinely different physical hypotheses.

`[HEUR strong]` The **continuous branch** is an effective local-dynamical programme. It begins from the postulated/canonical effective continuous generator $T(\rho,\eta)$, studies its resonance structure, birth dynamics, and metric emergence in rigorous algebraic and analytical detail. It is mathematically powerful but does not yet derive the generator from a more primitive relational axiom. Its results are certified within the chosen model and remain programme-level conditional on OPEN-P0.

`[HEUR strong]` The **discrete branch** is a constructive-substrate programme. It begins from finite relational distinguishability on $\mathbb{Z}_N$ without importing the continuous sine/exponential interaction law, and asks whether discrete relational dynamics alone can generate organized behavior. It does not assume the continuous generator; it attempts to derive interaction structure from combinatorial principles.

| Property | Continuous Branch | Discrete Branch |
|---|---|---|
| Substrate | $\mathbb{R}^2$ continuous phases | $\mathbb{Z}_N$ cyclic finite group |
| Primitive interaction | Sine/exponential generator terms (postulated effective model) | Antipodal defect threshold (motivated by bounded distinguishability; derivation OPEN) |
| Topology | Fixed diagnostic motifs $K_3, K_4$ | Emergent, birth-driven graph |
| Momentum | Inertial primitive | Gauge artifact |
| Terminus | Thermodynamic floor / smooth geometry | Thermodynamic crystallization |
| Current maturity | Level B: certified dynamics; generator selection open | Level B: certified numerics; continuum bridge open |

### 3.2 The Firewall

`[SG-PROG-1]` **No result may flow between the discrete and continuous branches without a named bridge theorem.** Cross-branch import without a bridge is `[FAIL]` by definition, regardless of apparent structural similarity. This guard is bidirectional: continuous coefficients must not enter TDR-G, and TDR-G results must not enter the continuous $\Phi_{2\to3}$ bridge, until explicit derivations exist.

---

## 4. Maturity Classification

Every sub-study in this programme is classified on the following maturity ladder. This axis is independent of DSN proof-status tags — it describes the physical justification status of the study's model, not the rigor of results within it.

| Level | Name | Description |
|---|---|---|
| **A** | Defined model | The object/map/rule is specified and internally consistent. Exploration has begun. |
| **B** | Certified dynamics | Theorems and/or numerics establish robust behavior within the model. Results are DSN-tagged and provenance-tracked. |
| **C** | Bridge-supported | The model is derived from or exported to another study through an explicit bridge theorem. Its scope within the larger programme is formally established. |
| **D** | Physical-universality candidate | The model is shown to be selected by a general principle — a variational extremum, a limit, a universality class argument — rather than chosen by hand. |

`[SG-PROG-2]` **No continuous-branch coefficient may be called physically primitive until the generator-selection problem (OPEN-P0) is resolved.** All continuous-branch results are Level B until that OPEN is closed. They may be exact and certain within their model while remaining contingent on model justification.

---

## 5. Programme-Level Open Problems

These four open-problem clusters cannot be resolved within any single sub-study. They define the scientific frontier of the programme as a whole. Each requires coordinated work across multiple studies or the creation of new bridge studies. OPEN-P2 is split into ontological (P2A) and dynamical (P2B) sub-problems because they require different closure routes; together they constitute one programme-level cluster.

---

**OPEN-P0 — Generator selection / universality** [RID: RTG-OPEN-GENERATOR-SELECTION]

Status: ACTIVE  
Governs: All continuous-branch studies

The continuous branch is built on the specific generator
$$T(\rho,\eta) = \bigl(\rho - \sin\eta,\; \eta + e^\rho - 1 - \sin\eta\bigr).$$
This generator is not derived from relational distinguishability axioms. It is chosen as a physically motivated canonical model. Until its selection is justified by one of the routes below, all continuous-branch results are conditional on the correctness of this choice.

Required closure — one of:
- Derive $T$ from a relational variational principle or information-theoretic extremum.
- Show $T$ is the unique or canonical effective limit of TDR-G dynamics as $N \to \infty$ with appropriate scaling.
- Establish that $T$ belongs to a universality class such that any generator in that class produces the same emergent geometry.
- Formally classify $T$ as a canonical effective model and state the scope limits explicitly.

Dependencies: OPEN-P1 (discrete-continuous bridge).

---

**OPEN-P1 — Discrete-to-continuous bridge** [RID: RTG-OPEN-DISCRETE-BRIDGE]

Status: ACTIVE  
Governs: TDR-G ↔ Continuous branch

`[HYP]` The TDR-G dynamics on $\mathbb{Z}_N$ in the $N \to \infty$ limit with appropriate $k/N$ scaling may converge to the continuous generator $T$ or to an effective description within the continuous programme.

`[HYP]` Alternatively, the continuous branch is an effective asymptotic description of fundamentally discrete dynamics, making TDR-G the more primitive branch.

Both hypotheses are currently unproven. The bridge study is not yet open as a formal sub-study.

Required for progress:
- Identify the correct scaling regime ($k/N$, $T/N$, observables) for a continuum limit.
- Test whether TDR-G large-$N$ observables converge to dyadic-map predictions.
- If convergence fails, classify the mismatch as evidence against one hypothesis.

Dependencies: TDR-G crystallization result (OPEN TDR-22), Dyadic backbone law.

---

**OPEN-P2A — Ontological primacy of the triad** [RID: RTG-OPEN-TRIAD-PRIMACY-ONTO]

Status: ACTIVE  
Governs: Programme ontology

`[HYP]` The minimal physically complete relational object is not the dyad $K_2$ but the triad $K_3$ — the simplest non-trivially closed relational complex. Under this hypothesis, the dyadic map studies a dynamical subsystem, not the fundamental primitive.

This is a philosophical/ontological question. It cannot be resolved purely by technical work within the current studies. It requires a new ontological analysis starting from first principles of relational distinguishability.

---

**OPEN-P2B — Dynamical reduction of triad to dyad** [RID: RTG-OPEN-TRIAD-REDUCTION]

Status: ACTIVE  
Governs: Continuous branch architecture

`[HYP]` There exists a triadic map $T_3(s,c)$ such that under $c = 0$, or under a symmetry-reduced invariant submanifold, the induced longitudinal dynamics reduce to the dyadic generator $T$ up to coordinate/gauge equivalence.

This is mathematically testable. If it can be shown, the dyad becomes a subsystem of a more primitive triadic dynamics, and the programme ordering becomes: triadic ontology → dyadic subsystem → birth/coupling event → network. If it fails, the dyad-first ordering gains support.

Required: Construct $T_3$ explicitly and test the reduction.

---

**OPEN-P3 — RTG-to-Regge / smooth geometry bridge** [RID: RTG-OPEN-REGGE-BRIDGE]

Status: ACTIVE  
Governs: Genesis geometry study, downstream physics

`[SG-PROG-3]` **No smooth gravitational coupling $\kappa_{\text{RTG}}$ may be defined before the smooth metric branch is established.** This guard is consistent with the Genesis DSN dependency: $\text{OPEN-M}_{\text{smooth}} \prec \text{OPEN-0}_{\text{smooth}}$.

Required closure:
- UV jet derivation: $\alpha_f$ from minimal non-block-diagonal quaternionic UV generator (OPEN II.7b in Genesis DSN).
- RTG-to-Regge dictionary: map RTG minimal hinge-star curvature to discrete Regge curvature.
- Emergent coupling: derive $\kappa_{\text{RTG}} = \mathcal{G}_e / J_e$ from the certified smooth metric branch.

---

## 6. Study Hierarchy and Status

### Tier 0 — Programme Overview (this document)

- `RTG_PROGRAMME_OVERVIEW` — current document

### Tier 1 — Methodology

- `DSN_METHODOLOGY_v1.2` — canonical tag registry, document architecture, claim grammar

### Tier 2 — Foundational / Infrastructure (partially exists)

- `RTG_PRIMITIVE_ONTOLOGY` `[proposed]` — zero-origin condition, first dyad, postulated/canonical effective continuous generator, quadratic form $B$, and model-selection scope. Currently partially covered by `RTG_ONTOLOGICAL_FOUNDATIONS_v0.2` and Genesis preamble material. Should be extracted as a short, stable, `[ARCHIVE-READY]` document serving as the shared foundation for all continuous-branch studies.

- `RTG_PROVENANCE_L0_L1_L2` `[proposed]` — formal record of what the L0/L1/L2 studies established and how those results connect to current study objects. Currently implicit history.

### Tier 3 — Continuous Programme

**`RTG_DYADIC_OSCILLATOR_DSN`** (current: `RTG_DYADIC_OSCILLATOR_DSN_v6.0`)

Physical question: What does the postulated continuous 2-body resonant map do? Why does it heal and fracture?  
Maturity: **Level B** — certified dynamics; generator selection (OPEN-P0) open.  
Scope: Dyad map $T$, Birkhoff coordinates, ISP crossing geometry, normalized $p$-step coefficients, $p$-resonance generalization (OPEN 9), projection program.  
Key certified outputs: $c_{21}$, $\mu_6 = -\frac{1}{2} - i\frac{2\sqrt{3}}{3}$, $\tau = \frac{2\sqrt{3}}{3}$, backbone law $Q_m \sim 1/(m+\kappa)$, OPEN 11 `[THM-ALG via IA]`, OPEN 18 `[THM-ALG via IA]`.  
Exports to: `RTG_TRIADIC_BIRTH_LIFT_DSN`, `RTG_GENESIS_GEOMETRY_DSN`.

---

**`RTG_TRIADIC_BIRTH_LIFT_DSN`** (current: `RTG_TRIADIC_BIRTH_LIFT_DSN_v1.0`)

Physical question: How does dyadic fracture create a new relational mode ($K_3$ birth), and how does a triad acquire dimensional capacity ($K_4$ lift)?  
Maturity: **Level B/C locally** — birth kinematics and diagnostic lift ledger are certified within scope; depends on dyadic bridge; physical birth-policy phase audit and sufficiency export remain open.  
Scope: $\Phi_{2\to3}$ birth map, $Q_c \sim Q_s^3$ `[THM]`, $K_3$ order separation with a limited quartic secular pump channel and revoked global-explosiveness claim, $K_4$ back-reaction and apex governor $\Delta Q_d^{(4)} = -32r^4$, Race-A/generalized ODE diagnostics, Plücker boundary structure, and necessary torsion-safe wedge geometry.  
Note: The $K_3$ birth stage and the $K_4$ dimensional lift stage address distinct physical questions (mode birth vs dimensional capacity) and may be separated into two studies in a future version.  
Imports from: `RTG_DYADIC_OSCILLATOR_DSN` (dyadic fracture state $s_*$, $\mu_6$, Birkhoff frame).  
Exports to: `RTG_GENESIS_GEOMETRY_DSN`.

---

**`RTG_GENESIS_GEOMETRY_DSN`** (current: `RTG_GENESIS_GEOMETRY_DSN_v2.0`)

Physical question: How does a network of birth-coupled oscillators generate smooth metric geometry? What are the conditions for a smooth metric branch to exist?  
Maturity: **Level A/B** — strong local no-go theorem and metric criterion `[THM]`; UV closure (OPEN-P3) open; generator selection (OPEN-P0) upstream-open.  
Scope: Quaternionic extension, block-diagonal no-go `[THM]`, single-face smooth metric criterion `[THM]`, primitive tetrahedral $Q_d$-quartic drift polynomial `[THM]`, triad chiral admissibility surface (OPEN 1C), constrained soft-mode susceptibility, UV closure program (OPEN M), and Regge/coupling bridge gates (OPEN 0-Regge, OPEN 0).  
Imports from: `RTG_DYADIC_OSCILLATOR_DSN`, `RTG_TRIADIC_BIRTH_LIFT_DSN`.  
Exports to: `RTG_REGGE_BRIDGE` (planned).

### Tier 4 — Discrete Programme

**`RTG_DISCRETE_GENESIS_DSN`** (current: `RTG_DISCRETE_GENESIS_DSN_v2.0`)

Physical question: Can a discrete relational universe on $\mathbb{Z}_N$ exhibit inflation-like growth and organized topology from relational distinguishability principles alone?  
Maturity: **Level B** — certified finite-state theorems, accounting identities, and simulation branches; interaction onset (OPEN TDR-1), multistar axiom (OPEN TDR-19), TDR-24 derivation chain, and continuum bridge (OPEN-P1) open.  
Scope: $\mathbb{Z}_N$ cyclic phase space, antipodal defect band $\mathcal{D}_k$, holonomy and narrow-band exclusion theorems, swap/path-cycle/star blow-up interaction laws, policy fork characterization (`bound_symmetric`, `largest_center`, `all_centers`), $N$-scaling laws, TDR-24 factorization `[ALG/NUM]`, microscopic birth law `[NUM]`, and thermodynamic crystallization frontier.  
Key certified output: $k/N$ controls entry into growth branch; multistar axiom controls growth character.  
Cross-branch firewall: `[SG-PROG-1]` applies. No imports from continuous branch; no exports to continuous branch until OPEN-P1 bridge is derived.

---

**`RTG_DISCRETE_BIRTH_DSN`** `[planned — gated]`

Physical question: Can discrete triadic dynamics ($K_3$-like structures within $\mathbb{Z}_N$) be studied natively without importing continuous coefficients?  
Maturity: **Level A** (not yet opened as active study).  
Gate conditions: Requirements R0–R11 in the TDR-G Triadic Requirements Ledger (Appendix C of `RTG_DISCRETE_GENESIS_DSN_v2.0`) must be satisfied before this study opens. Currently blocked by the TDR-24D → TDR-24A → TDR-24B → TDR-24C chain, with TDR-24D as the immediate prerequisite.

### Tier 5 — Bridge Studies (planned)

**`RTG_DISCRETE_CONTINUOUS_BRIDGE`** `[proposed — OPEN-P1]`  
Physical question: Does TDR-G converge to the continuous programme in any well-defined limit?  
Maturity: **Level A** (not yet formally opened).

**`RTG_GENERATOR_SELECTION`** `[proposed — OPEN-P0]`  
Physical question: What selects the continuous generator $T$?  
Maturity: **Level A** (not yet formally opened).

**`RTG_REGGE_BRIDGE`** `[proposed — OPEN-P3]`  
Physical question: How does RTG smooth geometry connect to discrete Regge gravity and produce $\kappa_{\text{RTG}}$?  
Maturity: **Level A** (not yet formally opened).

---

## 7. Cross-Study Dependency Graph

```
ESM / L0 / L1 / L2 studies
         │ [ENG provenance — bridge-required to current objects]
         ▼
RTG_PRIMITIVE_ONTOLOGY  ──────────────────────────────────────────────────┐
         │                                                                  │
         ▼                                                                  │
RTG_DYADIC_OSCILLATOR_DSN                                                  │
  (c₂₁, μ₆, τ, backbone, ISP, OPEN 9 p-family)                            │
         │                                                                  │
         ▼                                                                  │
RTG_TRIADIC_BIRTH_LIFT_DSN                                                 │
  (Φ₂→₃, Q_c~Q_s³, limited K₃ pump channel, K₄ apex governor)                             │
         │                                                                  │
         ▼                                                                  │
RTG_GENESIS_GEOMETRY_DSN  ◄─────────────────────────────────────────────────┘
  (no-go THM, metric criterion THM, UV closure OPEN)
         │
         ▼ [OPEN-P3]
RTG_REGGE_BRIDGE  ──► κ_RTG


RTG_DISCRETE_GENESIS_DSN
  (Z_N substrate, holonomy/narrow-band theorems, policy branches, N-scaling, crystallization frontier)
         │
         ▼ [OPEN-P1 — no current bridge]
[RTG_DISCRETE_CONTINUOUS_BRIDGE]
         │
         ▼ [if bridge succeeds]
[contributes to OPEN-P0 — generator selection]


OPEN-P0 (generator selection) ◄── depends on OPEN-P1 (bridge)
OPEN-P2 cluster (dyad/triad ordering) ──► P2A informs ontology; P2B is testable via triad→dyad reduction
OPEN-P3 (Regge bridge) ──► requires RTG_GENESIS_GEOMETRY_DSN UV closure first
```

---

## 8. Programme-Level Scope Guards

These guards apply to all sub-study documents. Each sub-study's §3 (Scope Guards) section must reference the applicable programme guards.

**[SG-PROG-1]** No result may flow between the discrete and continuous branches without a named bridge theorem tagged `[ALG]` or stronger, cited in the importing document's Import Ledger.  
Violation: Cross-branch import without bridge is `[FAIL]` by definition.

**[SG-PROG-2]** No continuous-branch coefficient may be described as physically primitive or physically inevitable until OPEN-P0 (generator selection) is resolved.  
Violation: Presenting $T$ or results derived from it as uniquely selected by nature overstates the current physical justification.

**[SG-PROG-3]** No smooth gravitational coupling $\kappa_{\text{RTG}}$ may be defined before the smooth metric branch is established (Genesis OPEN M $\prec$ OPEN 0 dependency).  
Violation: Defining $\kappa_{\text{RTG}}$ before OPEN M closure is closed would produce a formula without a certified foundation.

**[SG-PROG-4]** No result from Tier 4 or Tier 5 (discrete or bridge studies) may be used to strengthen or promote a result in Tier 3 (continuous studies) without an explicit bridge theorem.  
Violation: Using TDR-G numerical results as evidence for continuous-branch claims conflates constructive-substrate evidence with effective-dynamical evidence.

---

## 9. Naming Conventions

All documents in the RTG programme follow this naming scheme for new versions:

```
[BRANCH]_[STUDY_NAME]_DSN_v[MAJOR]_[MINOR].md
```

The dual-name convention for the continuous studies preserves the historical ontological labels (Dyadic, Triadic, Genesis) while making the scientific question legible through a subtitle:

| Shortname | Full name | Historical label preserved |
|---|---|---|
| `RTG_DYADIC_OSCILLATOR_DSN` | RTG Dyadic Oscillator Study | Dyadic |
| `RTG_TRIADIC_BIRTH_LIFT_DSN` | RTG Triadic Birth and Lift Study | Triadic |
| `RTG_GENESIS_GEOMETRY_DSN` | RTG Genesis Geometry Study | Genesis |
| `RTG_DISCRETE_GENESIS_DSN` | RTG Discrete Relational Genesis Study | TDR-G |

Study prefixes for RIDs are updated accordingly: `DYAD`, `TRIAD`, `GEN`, `TDRG` remain valid (backward compatible with existing RIDs).

---

## Appendix A — Version History

### v1.1 — June 2026
- **§0/§5:** Rephrased programme-level OPENs as four clusters; clarified that OPEN-P2A/P2B are sub-problems of one P2 cluster.
- **§2–§4:** Normalized generator-selection language: $T$ is a postulated/canonical effective continuous generator until OPEN-P0 closes.
- **§3/§6:** Corrected discrete interaction wording from derived to motivated/open; aligned TDR-G status with OPEN TDR-1, TDR-19, and TDR-24.
- **§6/§7:** Updated current DSN filenames to Dyadic v6.0, Triadic v1.0, Genesis v2.0, and Discrete v2.0; replaced stale Triadic/Genesis pump language with limited-pump / chiral-admissibility wording.
- **§6:** Updated discrete triadic gate reference from obsolete §26 to Appendix C of `RTG_DISCRETE_GENESIS_DSN_v2.0`.

### v1.0 — June 2026

Initial release. Created from the RTG hierarchy analysis (`RTG_HIERARCHY_ANALYSIS_v1.0`) incorporating critique notes from the multi-AI programme design review. Registers OPEN-P0 through OPEN-P3, the maturity ladder, programme-level scope guards SG-PROG-1 through SG-PROG-4, the five-tier study hierarchy, and the dependency graph.

---

*END OF DOCUMENT — RTG_PROGRAMME_OVERVIEW_v1.1*  
*This document is the Tier 0 navigation and scientific framing reference for the RTG programme. It does not contain derivations. All sub-study DSN documents reference this document for programme-level scope guards and open problem context.*
