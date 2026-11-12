# RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.8

**Title:** RTG Arithmetic Resonance and Zeta Study — Infrastructure and Diagnostic Ledger  
**Date:** 12 November 2026  
**Authors:** Mustafa (PI) · Claude · ChatGPT · Gemini · Grok  
**Scope:** A reference-only index of the arithmetic-resonance results of the Dyadic DSN; the TDR-G $\mathbb{Z}_N$ arithmetic structure as a bridge-candidate observable family; and the graph/transfer-zeta diagnostic infrastructure with the diagnostics it has produced. No cross-branch import is made and nothing is claimed about the Riemann Hypothesis.  
**Document class:** Infrastructure / diagnostic ledger (Methodology v1.4 §0.5) with a declared section map (§0.3); not a scientific result ledger  
**Programme tier:** Tier 5 — Arithmetic-diagnostic infrastructure; serves both continuous and discrete branches without belonging to either  
**Maturity:** Level A — retained. Defined scope, internal consistency established, exploration begun. Thread C engineering is certified; the one Phase-2 scientific result is a negative-clarifying diagnostic, not a Level-B-promoting bridge result.  
**Document status:** DRAFT — stage-2 candidate of v0.8; not adopted. `az-v0.7` governs until the PI adopts and tags this edition.  
**Supersedes:** `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN` v0.7 (tag `az-v0.7`, SHA-256 `2294d2a3287651802824a77ea22fb8f3896f6837cca1162fd8479ff02839fc94`)  
**Companion documents:** Programme Overview v1.4 (`programme-v1.4`) · Dyadic Oscillator v6.4.24 (`dyad-v6.4.24`) · Discrete Genesis v2.12.14 (`tdrg-v2.12.14`) · Genesis Geometry v2.10 (`gen-v2.10`) · OPEN-M v0.7.1 (`uvm-v0.7.1`)  
**DSN Methodology:** v1.4 (`methodology-v1.4`)  

**Status summary:** This document remains an infrastructure ledger, not an active scientific study, and Maturity remains **Level A**. Milestone AZ-2 is recorded as **attempted, negative-clarifying**: the most tempting angular observable was tested and **disqualified** as a bridge-candidate. **No Level B promotion. No OPEN-P1 / Dyadic bridge-candidate is promoted.**

---

## Local Tag Aliases

Status tags follow DSN Methodology v1.4 §8.1 and §8.3; qualifiers follow its §3.2. The entries below are local to this document.

| Local alias | Canonical expansion | Use |
|---|---|---|
| `[ENG PASS]` | `[ENG]` `[scope: certified by the named exit-code-gated check]` | Engineering item closed by a check whose artifact is named; the availability of that artifact is stated in §9 |
| `[NUM diagnostic]` | `[NUM]` `[scope: named diagnostic campaign]` | Finite numerical evidence (Methodology §8.4) |
| `[bridge-candidate]` | `[HYP]` `[bridge-required]` | Item that could become an OPEN-P1 observable if the bridge study opens; not an active import |
| `[bridge-disqualified]` | `[RESULT]` `[from: NUM]` `[scope: bridge-candidate ruled out]` | Item that was tested as a bridge-candidate and ruled out; recorded so it is not re-proposed |
| `[AZ-OPEN]` | `[OPEN]` `[scope: arithmetic-zeta infrastructure]` | OPEN problem internal to this arithmetic-resonance study |

Labels that are not status tags:

- `[import-ref]` marks a reference-only citation of a result owned by another DSN (Methodology §4.3, the first of its three uses). A status tag printed next to it is the owner's tag at the pinned edition; ownership is not transferred.
- `[ENG-blocker]`, `[ENG-blocker-n]`, `[ENG-open]` and `[ENG-open-n]` are the item labels of the engineering defects and open engineering decisions that §4.3.1 records as closed. They name those items; they do not assert validated engineering.
- A superseded, unverified artifact is described by its registry status in §9, not by a tag.

**Identifier owner map.** The following identifiers are this study's and keep their spelling (Methodology §4.2; existing identifiers are not renamed): `PROP-AZ-CORE-EQUIV` (result, §4.3.2), `TDRG-AZ-STATIC-ZN-4Q` (diagnostic result, §4.3.3), `DEF-AZ-CORE` and the `CONV-AZ-*` keys (conventions of `AZ-ART-CONVENTIONS-FROZEN`, §9), `SG-AZ-0.4` (guard, §0.1) and `TDRG-AZ-EXPORT-BASELINE` (the identifier the graph exporter prints for itself, §9). The prefix `TDRG-` in two of them names the object they describe, not a custodian: they are not entries of the `TDRG` namespace, and `RTG_DISCRETE_GENESIS_DSN` declares no such identifier.

---

## §0. What This Document Is

This document is an **infrastructure and diagnostic ledger** (Methodology §0.5), not a scientific result ledger of either branch. Its function is:

1. to record the origin of the arithmetic-resonance thread within RTG (§1.2);
2. to index, without migrating ownership, the arithmetic-resonance results of the Dyadic DSN (OPEN 9) that this study refers to (§4.1, §8);
3. to define the TDR-G $\mathbb{Z}_N$ arithmetic structure as a bridge-candidate observable family under OPEN-P1, not as an active cross-branch import (§4.2, §8);
4. to record the state of the graph/transfer-zeta diagnostic infrastructure and the diagnostics it has produced, under strict provenance and scope guards (§4.3, §9);
5. to state a precise success criterion that would justify opening this study as a full active Level B scientific DSN (§1.1) — and to record that the first Phase-2 attempt did **not** meet it (§4.3.5).

**This document does not contain derivations of cross-branch physics.** Its two internal results (PROP-AZ-CORE-EQUIV and the antipodal-band low-order obstruction, §4.3.2) are graph-theoretic facts about the Thread C diagnostic objects themselves; they are Thread-C-owned results, not cross-branch claims and not Dyadic/TDR-G-owned results. All scientific results cited from other DSNs remain owned by their source DSN.

### §0.1 Ownership and Layer Routing Map

`[DEF]` **Hub status.** `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN` is a hub ledger. It may summarize and cross-index arithmetic/zeta-relevant material, and it owns its own Thread C diagnostic infrastructure and the graph-theoretic facts about that infrastructure, but it does not migrate proof ownership out of the source DSNs for any Dyadic or TDR-G physics result.

| Content family | Source of truth | Status in this document |
|---|---|---|
| Continuous $p$-resonance arithmetic, OPEN 9, low-degree vanishing, subgroup/missing-slot formalism | `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 (`dyad-v6.4.24`) | `[import-ref]`; ownership remains Dyadic |
| TDR-G $\mathbb{Z}_N$ state space, reachability, superselection, cyclic memory, advance-spectrum conservation, BIND3 arithmetic/parity diagnostics | `RTG_DISCRETE_GENESIS_DSN` v2.12.14 (`tdrg-v2.12.14`) | branch-local context / `[bridge-candidate]`; no cross-branch import |
| Graph/transfer-zeta diagnostic engine, conventions, manifests, null models, certification suite | this DSN, Thread C | internal; `[ENG PASS]` (availability of the certifying files: §9) |
| Graph-theoretic facts about the diagnostic objects (core equivalence; antipodal-band low-order cycle structure) | this DSN, Thread C | Thread-C-owned `[THM]` / `[ALG]`; not cross-branch |
| Phase-2 diagnostics computed on TDR-G defect-graph exports | this DSN, Thread C | `[NUM diagnostic]`, branch-local; reclassified static-geometry; **not** a bridge-candidate |
| Discrete-continuous comparison between Dyadic $p$-horizons and TDR-G $\mathbb{Z}_N$ horizons | future OPEN-P1 bridge document | `[bridge-candidate]` only |
| Programme placement and dependency graph | `RTG_PROGRAMME_OVERVIEW` v1.4 (`programme-v1.4`) | registered there as a Tier 5 infrastructure entry (its §6.1, §6.5) with interfaces IF20 and IF21 (its §7.2); see §7 |
| Genesis cascade criterion and OPEN-M amplitude cascade | `RTG_GENESIS_GEOMETRY_DSN` v2.10 (`gen-v2.10`) / `RTG_OPEN_M_DSN` v0.7.1 (`uvm-v0.7.1`) | companion/bridge context only; arithmetic-horizon or graph-zeta observables cannot substitute for UV inputs |

`[SG-AZ-0.4]` **Refresh is not promotion.** Updating source versions, importing fresher summaries, or incorporating post-audit import-ref corrections does not promote any imported claim to Zeta-owned `[ALG]`, `[THM]`, `[RESULT]`, or cross-branch evidence. All imported proof tags are inherited from the owner DSN and remain source-scoped. The two internal results of §4.3.2 (`[THM]` and `[ALG]`) are Thread-C-owned graph-theoretic facts about this study's own diagnostic objects; they are not imported results and do not transfer to or from any other DSN.

### §0.2 Current State

- **Maturity:** Level A, retained. The Level B success criterion (§1.1) is not met.
- **Thread A** (continuous $p$-resonance): a reference-only index of Dyadic OPEN 9 results at `dyad-v6.4.24` (§4.1, §8). Nothing in it is owned here.
- **Thread B** (discrete $\mathbb{Z}_N$ arithmetic structure): TDR-G facts at `tdrg-v2.12.14` as branch-local context and `[bridge-candidate]` observables (§4.2, §8); `AZ-OPEN-SCOPE-ARITH` is open (§2).
- **Thread C** (graph/transfer-zeta diagnostics), owned here:
  - engine and conventions `[ENG PASS]` (AZ-1A, AZ-1B, AZ-1C; §4.3.1). The certifying files are in the repository only in part (§9): the `az_v5` package is deposited at its AZ-1B registry state and replayed; the AZ-1C, Phase-2 and proof-certificate files are source-reported;
  - `PROP-AZ-CORE-EQUIV` `[THM]`: for a both-orientations export of a finite simple graph, the re-directed 2-core equals DEF-AZ-CORE; statement and proof in §4.3.2;
  - `AZ-ALG-ANTIPODAL-LOWORDER` `[ALG]`: in the antipodal-band graph with $k<N/6$ there is no closed non-backtracking walk of length 2 or 3, and odd closure is obstructed while $Lk<N/2$ (§4.3.2);
  - `TDRG-AZ-STATIC-ZN-4Q` `[NUM diagnostic]`: the Core(G_T) `4|q` angular rule is static $\mathbb{Z}_N$ antipodal-band geometry, not a TDR-G dynamical signal, and is `[bridge-disqualified]` (§4.3.3–§4.3.5);
  - six retractions (§4.3.4, Appendix B).
- **Milestones:** AZ-0 and AZ-1 closed; AZ-2 attempted with a negative-clarifying outcome and open for a dynamical observable (§1.3, §4.3.5).
- **OPEN:** `AZ-OPEN-SCOPE-ZETA`, `AZ-OPEN-SCOPE-ARITH`, `AZ-OPEN-PROMO` (§2); three Thread C items (§4.3.6).
- **Not claimed:** anything about the Riemann Hypothesis (SG-AZ-1); any relation between Dyadic and TDR-G arithmetic (SG-AZ-3, SG-AZ-7); any cross-branch import (SG-PROG-1).

This list is navigation. The statements, scopes and evidence are in the sections named, and they govern.

### §0.3 Section Map

This document uses a declared section map (Methodology §0.5, infrastructure / diagnostic ledger). The functions of the standard layout are served as follows.

| Function (Methodology §1) | Here |
|---|---|
| Current canonical state | §0.2 |
| Active frontier / OPEN registry | §2; the Thread C scientific items in §4.3.6 |
| Scope guards | §3; `SG-AZ-0.4` in §0.1 |
| Layer routing | §0.1 |
| High-risk claims ledger | §5 |
| Main ledger | §1 (goal, success criterion, milestones), §4 (three threads), §6 (bridge-candidate connections) |
| Import ledger | §8 |
| Artifact and script registry | §9 |
| Collaboration and provenance | §10; Programme registration in §7 |
| Version history; retired and rejected claims | Appendix A; Appendix B |

The AI Context Core is the header and §0–§3.

## §1. Study Goal and Historical Origin

### §1.1 Primary Goal

`[DEF]` **Primary goal.** The goal of `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN` is to determine whether arithmetic horizon structure — including period length, divisibility, prime/composite obstruction, cyclic memory, and zeta/transfer spectra — plays a genuine structural role in RTG resonance dynamics, discrete relational memory, or future discrete-continuous bridge observables.

`[DEF]` **Immediate purpose.** The study has three immediate tasks:

1. Collect and organize the continuous arithmetic-resonance results already owned by Dyadic OPEN 9, without migrating ownership away from the Dyadic DSN.
2. Define TDR-G $\mathbb{Z}_N$ arithmetic structure as a bridge-candidate observable family under OPEN-P1, not as an active cross-branch import.
3. Stabilize the graph/transfer-zeta diagnostic infrastructure and run diagnostics under strict provenance and scope guards. This is done: the infrastructure is certified and a first diagnostic is executed and interpreted (§4.3).

`[OPEN]` **Central question.** Does arithmetic horizon structure merely organize diagnostics, or does it select physically meaningful resonance, memory, or bridge observables in RTG?

`[OPEN]` **Success criterion.** This study becomes scientifically active beyond infrastructure — and would be promoted to a full Level B DSN — only if at least one arithmetic/zeta observable is shown to be reproducible, branch-scoped, and useful for distinguishing resonance classes, memory-length regimes, TDR-G policy ensembles, or candidate OPEN-P1 bridge behavior **in a way that reflects the dynamics rather than the fixed substrate geometry.** **Status: not met.** The first observable tested (the Core(G_T) `4|q` angular rule) is reproducible and branch-scoped but is static $\mathbb{Z}_N$ substrate geometry, so it does not distinguish dynamical classes and is disqualified as a bridge observable (§4.3.4).

`[FAIL]` **Forbidden interpretation.** This study is not a proof, disproof, reformulation, or physical derivation of the Riemann Hypothesis. The RH appears in this document only as historical motivation; see §1.2.

### §1.2 Historical Origin

`[HEUR]` **Historical motivation.** This study originated from discussions connecting the Riemann Hypothesis, prime numbers, and arithmetic order to RTG resonance and memory. In RTG, this motivation is retained only in scoped form: prime and composite numbers are relevant insofar as they enter explicit mechanisms such as resonance closure, finite memory length, divisor obstruction, cyclic return, transfer spectra, or graph-zeta diagnostics. No claim is made about the Riemann Hypothesis, prime distribution, or classical zeta zeros.

The arithmetic observations that make this motivation non-trivial — that elevate it above numerology — are owned by the Dyadic DSN and are cited here by identifier only; their statements, scopes and boundary cases are the owner's and are cited once, with their limitations, in §8: the $p=5$ lattice cancellation (`DYAD-ALG-GLATTICE5`); the failure of prime-horizon first-lattice transparency at $p=7$ and the near-zero but nonzero $p=12$ cascade boundary (items of the owner's record `DYAD-OPEN-P-RESONANCE`); the low-degree pure anti-holomorphic raw vanishing for $b\in\{2,3,4\}$ in the ranges $p\ge b+2$ (`DYAD-ALG-VANISH-B2`, `DYAD-ALG-VANISH-B3`, `DYAD-ALG-VANISH-B4`); and the dyadic channel boundary at $b=4$ (`DYAD-ALG-B5-ALLP-NONVANISHING`).

These observations together motivate the study: the arithmetic horizon is not featureless, but the certified features do not follow naive prime-based intuition. The operative arithmetic mechanism appears to be **divisor structure, subgroup charge, orbit sums, cyclic-horizon closure, and secular-mode exclusion/presence**, not primality by itself.

`[HEUR]` **Scope statement.** This study investigates whether arithmetic structure — especially period length, divisibility, prime horizons, cyclic memory, advance-spectrum conservation, and transfer/zeta spectra — acts as a selection or obstruction mechanism in RTG. It collects three related threads: continuous $p$-resonance in the Dyadic branch, finite cyclic memory in TDR-G, and graph/transfer-zeta diagnostics of emergent TDR-G ensembles. It does not assert any result about the Riemann Hypothesis or classical prime distribution.

### §1.3 Milestones

`[DEF]` **Milestone AZ-0 (closed).** Create a clean ledger of what already exists: Dyadic OPEN 9 arithmetic facts, TDR-G candidate observables, and graph-zeta engineering blockers. The ledger is kept against the pinned owner editions (§8) without adding derivations or Zeta-owned scientific claims.

`[DEF]` **Milestone AZ-1 (closed).** Resolve all five `[ENG-blocker]` items in Thread C and produce at least one reproducible graph-zeta diagnostic run on a synthetic or TDR-G-generated test graph. **Status: CLOSED.** All five `[ENG-blocker]` and the three `[ENG-open]` items are resolved; the engine is certified by an exit-code-gated suite (AZ-1A synthetic engine, AZ-1B ingestion/export/provenance, AZ-1C manifest/null/statistic hardening — all `[ENG PASS]`); conventions are frozen (`AZ-ART-CONVENTIONS-FROZEN`); and reproducible runs on both synthetic and real TDR-G graphs exist. See §4.3.1.

`[DEF]` **Milestone AZ-2 (attempted; negative-clarifying).** Demonstrate that at least one arithmetic/zeta observable distinguishes two structurally distinct TDR-G ensemble classes. **Status: attempted; the first observable was disqualified.** The Core(G_T) `4|q` Hashimoto angular rule is reproducible across $N\in\{120,180,240\}$ and 5 seeds, but a core-matched random-theta antipodal-band null reproduces it with no TDR-G dynamics — so it is static $\mathbb{Z}_N$ substrate geometry, not a dynamical class discriminator. **This does not meet the Level B gate** and, importantly, it *removes* the most tempting angular observable from the bridge-candidate pool. See §4.3.3–§4.3.4. AZ-2 remains open for a genuinely dynamical observable.

---

## §2. Active Frontier / OPEN Registry

This is an infrastructure document. The registry covers scope and infrastructure questions; the scientific open items of Thread C are in §4.3.6. No experiment or artifact is requested by this section.

**OPEN 1 — Is a graph/transfer-zeta observable dynamical or substrate?** [RID: AZ-OPEN-SCOPE-ZETA]

Status: PARTIAL  
Owner study: this DSN  
Question: Determine whether a graph/transfer-zeta observable of the TDR-G defect graph is a branch-discriminating *dynamical* observable or merely an aggregate/substrate diagnostic.  
Closure criterion: no separate criterion is registered. The conditions that apply are the success criterion of §1.1 and the two null gates of §4.3.6 (a degree/reciprocal null and the $\mathbb{Z}_N$ geometry null), with the declarations SG-AZ-5 requires.  
Dependencies: the Thread C engine (§4.3.1) and its artifacts (§9).  
Closed sub-items:
- the first angular observable (the Core(G_T) `4|q` rule) is a substrate-geometry diagnostic, not dynamical :: `[NUM diagnostic]` :: [RID: TDRG-AZ-STATIC-ZN-4Q] :: §4.3.3, §4.3.4

Active sub-items:
- a dynamical (non-substrate) graph observable :: `[OPEN]` :: §4.3.6

Required before any Level B promotion.

**OPEN 2 — Are the $\mathbb{Z}_N$ arithmetic objects bridge-candidate observables?** [RID: AZ-OPEN-SCOPE-ARITH]

Status: ACTIVE  
Owner study: this DSN  
Question: Determine whether the $\mathbb{Z}_N$ cyclic memory length and divisibility structure of TDR-G are bridge-candidate observables for OPEN-P1, or purely internal to the TDR-G DSN. The full question, with the objects it concerns, is stated in §4.2.  
Closure criterion: as stated in §4.2 — OPEN-P1 at minimum formally opened, a candidate bridge observable defined, and SG-AZ-7 satisfied.  
Dependencies: OPEN-P1 (Programme); the TDR-G objects cited in §8.  

Required before any Level B promotion.

**OPEN 3 — Promotion conditions** [RID: AZ-OPEN-PROMO]

Status: ACTIVE  
Owner study: this DSN  
Question: State the exact conditions under which this document would be promoted to a full Level B active scientific DSN, including required artifact and transcript provenance.  
Closure criterion: those conditions registered in an adopted edition of this DSN. The success criterion of §1.1 is the current statement; it does not yet name the artifact and transcript provenance.  
Dependencies: none.  

Required before any Level B promotion.

**Closed modules.**

- **AZ-OPEN-ENG** [RID: AZ-OPEN-ENG-BLOCKERS] — CLOSED. All five `[ENG-blocker]` items fixed and all three `[ENG-open]` items closed; engine certified by an exit-code-gated suite. Per-item closure record in §4.3.1; artifacts and their availability in §9. The guard that depended on this module (SG-AZ-5) is a provenance guard (§3).
- **AZ-OPEN-EDGE** [RID: AZ-OPEN-EDGE-EXPORT] — CLOSED. Decision: **directed, both orientations.** Each symmetric defect pair $\{a,b\}$ is exported as the two directed edges $(a,b)$ and $(b,a)$. One-edge-per-pair makes `extract_recurrent_core` silently empty and the Hashimoto operator ill-defined; both orientations give a well-defined $2|E|\times2|E|$ Hashimoto operator. Registered in §4.3.1.1 and in the frozen conventions artifact. A consequence of this decision is PROP-AZ-CORE-EQUIV (§4.3.2).

---

## §3. Scope Guards

Programme-level guards SG-PROG-1 to SG-PROG-4 of `RTG_PROGRAMME_OVERVIEW` v1.4 (`programme-v1.4`) §8 apply in full. Their governing text is there and is not quoted here; the three entries below state only how each applies to this study. Sub-study guards specific to this document follow.

**[SG-PROG-1]** (cross-branch physical use). No physical law, coefficient, observable identification or evidential strengthening passes between the discrete and continuous branches of this study without a named, proved bridge. This is the primary firewall governing Thread B (§4) of this study. `[import: RTG_PROGRAMME_OVERVIEW v1.4 §8 | SG-PROG-1]`

**[SG-PROG-2]** (model selection is not local proof status). All Thread A results (§4.1) are conditional on the selected continuous generator and are not described as physically primitive while OPEN-P0 is open. `[import: RTG_PROGRAMME_OVERVIEW v1.4 §8 | SG-PROG-2]`

**[SG-PROG-4]** (document location does not create transfer authority). This study's Tier 5 hub placement is not a bridge: Thread B/C items are not injected into Thread A or vice versa. `[import: RTG_PROGRAMME_OVERVIEW v1.4 §8 | SG-PROG-4]`

**[SG-AZ-1] — No RH claim.**  
No statement in this study may be interpreted as a proof, disproof, reformulation, or physical derivation of the Riemann Hypothesis. The RH appears here as historical motivation only (§1.2).  
Violation: Claiming any RTG result bears on the distribution of zeta zeros, the location of non-trivial zeta zeros, or the truth of the Riemann Hypothesis.

**[SG-AZ-2] — Arithmetic resonance is not prime mysticism.**  
Prime and composite distinctions are relevant in this study only through explicitly defined mechanisms: resonance closure, divisibility obstruction, memory length, cyclic return period, spectral gap, transfer determinant, or graph-zeta diagnostics. Vague appeals to "primes appearing" or "prime structure underlying RTG" are not permissible.  
Violation: Citing a prime number as significant without identifying the explicit RTG mechanism through which it enters.

**[SG-AZ-3] — Cross-branch firewall.**  
Dyadic $p$-resonance results (Thread A) and TDR-G graph-zeta results (Thread C) remain in separate threads under SG-PROG-1 and SG-PROG-4 until a named bridge theorem connects them. Thread B items are bridge-candidates only; they are not active imports.  
Violation: Using Dyadic OPEN 9 arithmetic results as evidence for a TDR-G claim, or vice versa, without an explicit bridge theorem.

**[SG-AZ-4] — Zeta diagnostics are observables, not ontology.**  
A zeta or transfer determinant computed from a graph or operator is a diagnostic object unless explicitly proved to select dynamics, bridge layers, or observables in a named derivation.  
Violation: Asserting that a Hashimoto or transfer-zeta spectrum encodes RTG resonance ontologically without a derivation.

**[SG-AZ-5] — Provenance guard for imported graph-zeta results.**  
No graph-zeta result may be registered here, or imported elsewhere from here, unless it declares: (i) the graph object (G_T / Core(G_T) / G_birth(w) / G_cumulative), (ii) the spectrum mode (full-spectrum / leading-K / trace-moment), (iii) the null model used, (iv) the eps-angle convention for zero-eigenvalue handling, (v) the script version, (vi) the artifact paths, and (vii) a hash/provenance record.  
Violation: Reporting a Hashimoto eigenvalue, R_q value, spectral radius, or zeta pole without its graph object, spectrum mode, null model, eps-angle, script version, and hash provenance.

**[SG-AZ-6] — Ownership stays in source DSNs.**  
This document does not migrate ownership of any physics result from the Dyadic DSN or TDR-G DSN. Dyadic OPEN 9 sub-items remain owned by `RTG_DYADIC_OSCILLATOR_DSN`. TDR-G OPEN items remain owned by `RTG_DISCRETE_GENESIS_DSN`. This document may cite them as `[import-ref]` but may not retag or restate them as its own results. *(PROP-AZ-CORE-EQUIV and the antipodal-band low-order obstruction are graph-theoretic facts about this study's own Thread C diagnostic objects, owned by this DSN; they are not Dyadic/TDR-G physics results and do not fall under this guard.)*  
Violation: Registering a Dyadic OPEN 9 result as an `[ALG]` or `[OPEN]` within this document's own ledger.

**[SG-AZ-7] — Vocabulary similarity is not a bridge theorem.**  
The presence of shared vocabulary between Thread A (cyclic charge $\chi_p$, divisor structure, subgroup orbits, $p$-resonance) and Thread B/C ($\mathbb{Z}_N$ cyclic memory, orbit-lattice spacings, $\gcd$-divisibility, advance spectrum, and now the `4|q` divisor-graded angular rule) does not constitute a bridge theorem. Any claim that Dyadic OPEN 9 arithmetic structures and TDR-G $\mathbb{Z}_N$ arithmetic are related requires a named bridge theorem registered under OPEN-P1 with explicit derivation.  
Violation: Asserting or implying that Dyadic subgroup-charge $K^{\rm extra}_{p,q}$ and the TDR-G `4|q` angular rule (or $\gcd(d,N)$-divisibility) are dual, equivalent, or physically analogous without a named bridge theorem.  
**Worked example of the trap this guard exists to catch:** the Phase-2 `4|q` rule (§4.3.3) is a divisor-graded selection rule that *sounds* like the Dyadic cyclic-subgroup selection rules of Thread A. It must NOT be compared to Dyadic subgroup-charge structure as evidence of a bridge. It is not specific to TDR-G dynamics: in the tested protocol a core-matched random-$\theta$ antipodal-band null with no TDR-G dynamics reproduces it (`[NUM diagnostic]`; §4.3.3 Chain 2, $N\in\{120,180,240\}$; §4.3.4). It is read as static $\mathbb{Z}_N$ antipodal-band geometry on that evidence; nothing is asserted for every antipodal-band graph or every $N$. A "resemblance" to Dyadic cyclic selection is therefore vacuous as evidence of a bridge. This is the canonical SG-AZ-7 violation to avoid.

<!-- AI_CONTEXT_CORE_END -->

---

## §4. Three Threads

This study organizes its material into three threads. They are structurally separated by scope guards SG-AZ-3 and SG-PROG-1 and may not be merged without a named bridge theorem.

---

### §4.1 Thread A — Continuous $p$-Resonance (Dyadic OPEN 9 reference index)

**Ownership:** `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 (`dyad-v6.4.24`), §2 and §6.11.  
**Status here:** Reference only. All results are cited as `[import-ref]`. This document does not own, restate, retag, or add sub-items to Dyadic OPEN 9. SG-PROG-2, SG-AZ-3 and SG-AZ-6 apply.

#### §4.1.1 Certified results (cited by reference)

The Dyadic results this study refers to are listed in the first group of §8, one row per owner identifier, each with a readout, its limitations, the owner's tag and its location. They are not stated a second time here.

#### §4.1.2 Active open frontier (owned by the Dyadic DSN)

The open arithmetic frontier is the owner's: Dyadic §2 OPEN 9 (`DYAD-OPEN-P-RESONANCE`, active sub-items). It is programme context only. Progress on it is tracked in the Dyadic DSN, and this document keeps no list of its items.

#### §4.1.3 Arithmetic-resonance observation relevant to this study's goal

`[HEUR]` The $p$-resonance arithmetic horizon is not featureless, but it does not conform to naive prime-based intuition:

- $p=5$ (prime): unique non-trivial lattice cancellation (unexpected).
- $p=7$ (prime): transparency fails (confounds simple prime-transparency conjecture).
- $p=12$ (composite): near-zero nonvanishing cascade boundary (unexpected near-cancellation).
- $p=6$ (composite): the programme's canonical resonance period, selected by order-6 Birkhoff/dyadic structure rather than primality.
- $b\le4$ vs. $b=5$ boundary: arithmetic enters through direct-accumulation orbit weights $\lambda^{-(b+1)k}$, cyclotomic cancellations, and secular-mode exclusion/presence in $\beta$-mode path enumeration, not through prime status alone.

`[HEUR]` The operative arithmetic mechanism appears to be **divisor structure, subgroup charge, direct orbit weights, cyclotomic sum cancellation, reachable-basis/missing-slot structure, cyclic-horizon closure, and secular-mode exclusion/presence** rather than primality per se. SG-AZ-2 applies.

### §4.2 Thread B — Discrete $\mathbb{Z}_N$ Arithmetic Structure (bridge-candidate only)

**Ownership:** `RTG_DISCRETE_GENESIS_DSN` v2.12.14 (`tdrg-v2.12.14`).  
**Status here:** Branch-local context and bridge-candidate observable family under OPEN-P1. SG-PROG-1, SG-PROG-4, SG-AZ-3, and SG-AZ-0.4 apply. No TDR-G result is imported as a cross-branch claim, and no TDR-G fact is used as evidence for a Dyadic claim.

`[bridge-candidate]` **Observable family.** The TDR-G objects this study treats as candidate OPEN-P1 observables are listed in the second group of §8, one row per owner identifier or group of identifiers, each with a readout, its limitations, the owner's tag, scope and convention. They are not stated a second time here. The status of the family as a whole is the hypothesis that some of these objects could serve as OPEN-P1 observables; no row is a bridge, and none is used outside its branch.

`[AZ-OPEN]` **AZ-OPEN-SCOPE-ARITH.** Are the $\mathbb{Z}_N$ arithmetic objects above — memory horizon $(N,k)$, divisibility, reachable cosets, orbit-lattice spacings, advance-spectrum conservation, parity sectors, TDR-26 birth-anchored memory window, and policy-dependent N-scaling — genuinely comparable to the Dyadic $p$-resonance arithmetic horizon, or are they structurally different objects that merely share vocabulary? Answering this question requires OPEN-P1 to be at minimum formally opened, a candidate bridge observable to be defined, and SG-AZ-7 to be satisfied. The Phase-2 `4|q` angular result (§4.3.3) is NOT an answer to this question in the affirmative — it is shown to be substrate geometry (§4.3.2/§4.3.4), so it neither supplies nor supports a bridge.

**What Thread B does not contain:**

- No TDR-G result is imported as a cross-branch claim. TDR-G facts may be cited as branch-local context, clearly tagged with their source DSN, without constituting a cross-branch import.
- No claim is made that TDR-G $\mathbb{Z}_N$ structure is related to Dyadic OPEN 9 arithmetic structure.
- No cross-branch inference is made.

### §4.3 Thread C — Graph/Transfer-Zeta Diagnostics

**Ownership:** This thread is internal to this study.  
**Status:** Engineering certified (`[ENG PASS]`; availability of the certifying files in §9). One Phase-2 diagnostic produced and interpreted; it is a **negative-clarifying** result (a bridge-candidate disqualified), not a Level-B-promoting result. SG-AZ-4, SG-AZ-5, and SG-AZ-7 apply.

#### §4.3.1 Engineering closure — all `[ENG PASS]`

The five `[ENG-blocker]` items identified in the May 14 2026 review of `rtg_graph_zeta_proto_v3.py`, and the three `[ENG-open]` items, are resolved. The corrected engine is the `az_v5` package, certified by an exit-code-gated suite. Closure record:

`[ENG PASS]` **AZ-1A — synthetic Hashimoto engine certification.** The non-backtracking (Hashimoto) engine is verified on a benchmark ladder against analytic / dense reference values (directed cycles, bidirected cycles, bouquet $2^{1/4}$, disjoint unions). Sparse-vs-dense agreement to $<10^{-6}$. Closes:
- **[ENG-blocker-1]** `gen_bouquet` off-by-one — FIXED; unit-tested on single-petal walk length.
- **[ENG-blocker-2]** `gen_from_json` precedence — FIXED; schema-validated loader, unit-tested on a known small graph.
- **[ENG-blocker-4]** eigensolver $O(m^3)$ scaling — FIXED; ARPACK (`which='LM'`) sparse path with dense fallback for tiny matrices. *(See also the spectral-radius correction in §4.3.4 retraction block: the original power-iteration radius was wrong for $\pm R$ dominant pairs; ARPACK is the certified replacement, `AZ-ART-SPECTRAL-RADIUS-PATCH`.)*

`[ENG PASS]` **AZ-1B — TDR-G ingestion/export/provenance certification.** Real TDR-G defect-graph exports (CONV-AZ-GRAPH-EXPORT) ingest, validate, and round-trip with checksums; manifest validator is a loud-fail gate (exit 0 = pass). Closes:
- **[ENG-blocker-3]** directed-vs-undirected export — RESOLVED via AZ-OPEN-EDGE (both orientations; §4.3.1.1); `extract_recurrent_core` verified non-empty on known inputs.
- **[ENG-blocker-5]** script-version provenance gap — CLOSED; `az_v5` is a named, hashed package with a SHA-256 artifact registry (`AZ-ART-AZV5-REGISTRY`); the prior `v4/v5` placeholder references are superseded.

`[ENG PASS]` **AZ-1C — manifest/null/statistic hardening.** Closes the three `[ENG-open]` items and adds statistic discipline:
- **[ENG-open-3]** null-graph ensemble — RESOLVED; a degree-exact directed double-edge-swap (Null0), a reciprocal-pair-preserving swap (Null1), and a $\mathbb{Z}_N$ random-theta antipodal-band null (geometry null, raw and core-matched) are defined and implemented.
- **[ENG-open-1]** `line_err` null and **[ENG-open-2]** nonnormality normalization — SUPERSEDED; the operative statistic is the angular $R_q=|\,\overline{\exp(i q\theta_\ell)}\,|$ over Hashimoto eigenphases with $R_{\max}$ over a frozen divisor set $Q_N$, multi-test routed at the $R_{\max}$ level; zero-eigenvalue handling fixed by an eps-angle convention (CONV-AZ-ANGLE-ZERO, default $\varepsilon=10^{-10}$, with $n_{\rm eigs\,total}$ / $n_{\rm eigs\,used}$ reported).
- Manifest hardening: $k/N$ consistency check, candidate-level claims require $\ge1000$ nulls, `artifact_paths` required, `birth_window_status` required for birth-window exports.

##### §4.3.1.1 AZ-OPEN-EDGE decision (registered)

`[ENG]` **Decision: directed, both orientations.** Each symmetric defect pair $\{a,b\}$ exports as $(a,b)$ and $(b,a)$. Consequence: the Hashimoto operator is $2|E|\times2|E|$ and `extract_recurrent_core` operates correctly (one-edge-per-pair returns an empty core — silent failure). This is canonical for all downstream spectral code and is recorded in `AZ-ART-CONVENTIONS-FROZEN`. A direct consequence is PROP-AZ-CORE-EQUIV (§4.3.2).

#### §4.3.2 Internal graph-theoretic results (Thread-C-owned)

These are facts about this study's own diagnostic objects, established during the Thread C engineering and audit work. They are owned by this DSN (not imported, not cross-branch).

`[THM]` `[RID: PROP-AZ-CORE-EQUIV]` `[proof: written derivation, below]` **PROP-AZ-CORE-EQUIV — the export core equals DEF-AZ-CORE.**  
*Scope: finite simple undirected graph, exported with both orientations; no multiedges, no self-loops.*  
Let $G$ be such a graph, exported as the directed edges $(a,b)$ and $(b,a)$ for every edge $\{a,b\}$. Let $R(G)$ be DEF-AZ-CORE: the set of directed edges that lie on a directed cycle of the Hashimoto transition digraph, in which $(u,v)\to(v,w)$ is a transition iff $w\ne u$. Let $H$ be the 2-core of $G$, the largest subgraph in which every vertex has degree at least 2 (possibly empty). Then $R(G)$ is the set of both orientations of the edges of $H$: for a both-orientations export, the re-directed undirected 2-core equals the frozen non-backtracking recurrent core DEF-AZ-CORE.

*Reading on which the statement depends.* A directed cycle of the transition digraph is a closed walk $v_0,v_1,\dots,v_L=v_0$ in $G$ with $v_{i+1}\ne v_{i-1}$ for every $i$, indices mod $L$ — non-backtracking also where the walk closes. If backtracking is allowed at the closing point, a pendant path attached to a cycle lies on a closed walk and the statement is false.

*Proof.* Two standard facts. (i) The union of two subgraphs of minimum degree $\ge2$ has minimum degree $\ge2$, so $H$ exists and contains every subgraph of minimum degree $\ge2$. (ii) Deleting vertices of degree $\le1$ with their edges until none is left yields $H$: a vertex of $H$ never reaches degree $\le1$, and what is left has minimum degree $\ge2$. An edge is deleted only with one of its endpoints, so $H$ is the subgraph induced on its vertex set.

*$R(G)$ lies in the orientations of $E(H)$.* Let $W$ be a closed walk that is non-backtracking at every index mod $L$, and let $S$ be the subgraph formed by its edges. At each $v_i$ the walk uses the edges $\{v_{i-1},v_i\}$ and $\{v_i,v_{i+1}\}$; they are distinct because $v_{i-1}\ne v_{i+1}$ and $G$ has no multiple edges. So every vertex of $S$ has degree $\ge2$ in $S$, and $S\subseteq H$ by (i).

*Every orientation of every edge of $H$ is in $R(G)$.* Let $e=\{u,v\}\in E(H)$.  
Case 1: $e$ is not a bridge of $H$. Then $e$ lies on a simple cycle of $H$, of length $\ge3$ because $G$ is simple. Traversed in either direction it is a closed walk that is non-backtracking at every index, and the two directions contain $(u,v)$ and $(v,u)$.  
Case 2: $e$ is a bridge of $H$. Let $A$ and $B$ be the components of $H-e$ that contain $u$ and $v$. $A$ contains a cycle: otherwise $A$ is a tree; if $A$ is the single vertex $u$, then $\deg_H(u)=1$; if $A$ has at least two vertices, it has at least two leaves, one of them $x\ne u$, and $\deg_H(x)=\deg_A(x)=1$; both contradict minimum degree $\ge2$ in $H$. Likewise $B$ contains a cycle. Choose simple cycles $C_A\subseteq A$ and $C_B\subseteq B$, a shortest path $P_A$ in $A$ from $u$ to $C_A$, ending at $a$, and a shortest path $P_B$ in $B$ from $v$ to $C_B$, ending at $b$ (either path may have length 0). A shortest path to a cycle meets it only in its last vertex. Consider the closed walk that starts at $u$, crosses $e$ to $v$, follows $P_B$ to $b$, goes once around $C_B$, returns along $P_B$ to $v$, crosses $e$ back to $u$, follows $P_A$ to $a$, goes once around $C_A$ and returns along $P_A$ to $u$. It is non-backtracking at every index, the closing one included: inside a simple path or a simple cycle of length $\ge3$ no step reverses the previous one; at $v$, $e$ is followed by the first edge of $P_B$ or, if $P_B$ is empty, by an edge of $C_B$, and both lie in $B$ and differ from $e$; at $b$ the walk arrives by the last edge of $P_B$, which is not an edge of $C_B$, leaves along $C_B$, returns by the other edge of $C_B$ at $b$ and leaves by the last edge of $P_B$, so consecutive edges differ each time (if $P_B$ is empty, the edges at $b=v$ are $e$, the two cycle edges and $e$, and consecutive ones differ); on the way back the edge before the second crossing of $e$ is the first edge of $P_B$ or an edge of $C_B$, different from $e$. The $A$ side is the same, and the walk closes at $u$, arriving by an edge of $A$ and continuing with $e$. The walk contains $(u,v)$ and $(v,u)$. $\square$

No strong-connectivity assumption is used or claimed (a bidirected cycle splits into clockwise/counterclockwise SCCs, so the correct statement is only that every directed 2-core edge lies in *some* cyclic SCC).

*Corroboration; not the basis of the grade.* (a) The June 2026 work reports a machine check on 2,141,014 graphs (exhaustive to 7 vertices incl. barbell/lollipop/theta/figure-8; plus random) with zero counterexamples. `[artifact: AZ-ART-PROP-CORE-EQUIV]` Its files are not in the repository (`EV-SRC-REPORTED`, `EV-NOT-RERUN`; §9). (b) A separate check made for this edition compares $R(G)$, computed from the definition, with the 2-core on all 2,131,019 labelled simple graphs with at most 7 vertices and finds no mismatch. `[artifact: AZ-ART-CORE-EQUIV-CHECK]` (`EV-CODE`, `EV-RUN`, 12 November 2026; §9). It is not a rerun of (a) and does not reproduce its count.  
Consequence: the uploaded export object labeled `Core(G_T)` (a 2-core) IS DEF-AZ-CORE; the earlier 2-core-vs-DEF-AZ-CORE labeling mismatch is closed.

`[ALG]` **Antipodal-band low-order obstruction.**  
*Scope: antipodal-band graph on $\mathbb{Z}_N$, edge iff displacement within $k$ of $N/2$ (mod $N$), narrow band $k<N/6$; both orientations.*  
(1) There is no closed non-backtracking walk of length 2 or 3 under $k<N/6$. (2) Length 4 is the first possible/constructible non-backtracking closure scale in the full antipodal-band geometry. (3) **Odd-closure obstruction threshold:** for odd $L$, closed non-backtracking walks are impossible when $Lk<N/2$; when $Lk\ge N/2$ the displacement obstruction is removed, but existence still depends on the discrete displacement set and the available vertices/edges (the threshold is a necessary obstruction bound, not a sufficiency theorem). Verified: at $N=120,k=8$, existence is confirmed by an explicit $L=9$ walk ($\operatorname{Tr}(B^9)\ne0$), and $\operatorname{Tr}(B^L)=0$ for odd $L\in\{1,3,5,7\}$. `[RID: AZ-ALG-ANTIPODAL-LOWORDER]` `[artifact: AZ-ART-ANTIPODAL-LOWORDER]`  
Note on scope: claims (1)–(3) are about the full antipodal-band graph on $\mathbb{Z}_N$; they are not asserted as existence statements for arbitrary induced/random core subgraphs.  
**Not promoted:** the full "$R_q$ elevated iff $4\mid q$" angular rule is NOT `[ALG]`. The exact spectral theorem claimed in an earlier draft (THM-AZ-ANTIPODAL-4Q v1: "$\operatorname{Tr}(B^L)=0$ for all odd $L$" and "dominant eigenphases exactly at 4th roots of unity") is `[RETRACTED]` (see §4.3.4). The connection from the low-order obstruction to the angular rule is `[HEUR]` only; the numerical observations it rests on are the `[NUM diagnostic]` chains of §4.3.3.

#### §4.3.3 Phase-2 diagnostic result — the `4|q` angular rule (static $\mathbb{Z}_N$ geometry)

`[NUM diagnostic]` `[RID: TDRG-AZ-STATIC-ZN-4Q]`

This result rests on two distinct evidence chains, with distinct scope and sample size; they must not be conflated.

**Chain 1 — Null0/Null1 statistical excess.** *Scope: $N=120$, $k=8$, `bound_symmetric`, Core(G_T), full-spectrum $R_q$, degree-exact Null0 and reciprocal-pair Null1, 1000 nulls, 5 seeds.* The Core(G_T) angular spectrum shows elevated $R_q$ on divisors $q$ with $4\mid q$ (e.g. $q\in\{4,8,12,20,24\}$ at $N=120$) and is silent on $q$ with an odd prime factor ($q\in\{3,5,15\}$, $R_q\approx0$). The generic even-$q$ elevation is an artifact of the bidirected export and collapses under Null1, but the $4\mid q$ signal persists above the reciprocal-pair baseline. In the registered Null1 runs the $4\mid q$ signal persists above the reciprocal-pair baseline; exact per-$q$ $z$-scores are artifact-scoped and must be read from the registered Null1 reports (`AZ-ART-PHASE2-N120-CORE`). `[artifact: AZ-ART-PHASE2-N120-CORE]`

**Chain 2 — static-geometry reclassification.** *Scope: $N\in\{120,180,240\}$, core-matched random-theta antipodal-band null; per-$q$ comparison (this is a per-$q$ comparison artifact, NOT a 1000-null × 5-seed empirical-$p$ report).* A core-matched random-theta antipodal-band null — random $\theta$ on $\mathbb{Z}_N$ with the SAME antipodal defect rule, then the SAME core extraction, with NO TDR-G dynamics — reproduces the qualitative $4\mid q$ rule, and the strong-signal set tracks the 2-adic divisor structure of $N$ ($q=16$ appears only at $N=240=2^4\cdot3\cdot5$). Therefore the angular `4|q` rule is **static $\mathbb{Z}_N$ antipodal-band geometry, not a TDR-G dynamical signal**; the dynamical interpretation is retracted. `[artifact: AZ-ART-THETA-CORE-MATCHED]`

The underlying mechanism is partly understood (the antipodal-band low-order obstruction §4.3.2: $L=2,3$ excluded, $L=4$ first constructible, so low-order cycles are 4-dominated). The full causal link to "$R_q$ elevated iff $4\mid q$" is `[HEUR]`, not exact: a predicted weakening of the rule with larger $k/N$ was tested and FALSIFIED ($R_4$ rises, not falls), so the mechanism is incompletely captured by low-order domination alone.

#### §4.3.4 Visible correction / retraction block

```
[RETRACTED] G_cumulative as the lead spectral signal.
  Reason: the apparent ~1.5x excess was a degree-only Null0 signal and did not
  survive the reciprocal-pair / topology-matched Null1 control (ratio ~1.00). It is
  therefore not a robust TDR-G dynamical or bridge-candidate observable. (The
  spectral-radius bug primarily affected the Core(G_T) "generic" claim, not the
  G_cumulative retraction, which is a nulling/topology-control result.)

[RETRACTED] "Core(G_T)/G_T spectrally generic" (the original README headline).
  Reason: artifact of the spectral-radius bug (reported 2.879 vs true 3.306 on the
  real N=120 core). The corrected analysis shows Core(G_T) carries the 4|q structure;
  it is the signal-bearing object, not generic.

[RETRACTED] 4|q rule as a TDR-G dynamical arithmetic law.
  Reason: reproduced by the core-matched random-theta antipodal-band null with no
  TDR-G dynamics. Reclassified as static Z_N antipodal-band geometry (TDRG-AZ-STATIC-ZN-4Q).

[RETRACTED] exact [ALG] THM-AZ-ANTIPODAL-4Q (v1): "Tr(B^L)=0 for all odd L" and
  "dominant eigenphases exactly at 4th roots of unity."
  Reason: explicit N=120,k=8 length-9 odd closed non-backtracking walk
  (0->68->16->84->32->99->46->113->60->0); Tr(B^9)=4212 != 0. The salvageable
  low-order facts are kept as [ALG] (§4.3.2); the angular consequence stays [HEUR/NUM strong].

[RETRACTED] even-non-4|q suppression (q in {2,6,10}) as a TDR-G dynamical residue.
  Reason: not stable across N under the core-matched theta null — present at N=120,
  gone at N=180, reversed at N=240. No robust dynamical angular signal remains.

[RETRACTED] falsified prediction "the 4|q rule weakens as k/N rises."
  Reason: tested at N=120, k in {4,8,12,16,19}; R_4 rises (0.75 -> 0.97), does not fall.
  The low-order-domination mechanism does not govern the k-dependence.
```

The block is kept as registered. Its spelling `[HEUR/NUM strong]` is the pre-migration form; the current form of that statement is in §4.3.2 and §4.3.3.

#### §4.3.5 AZ-2 status

`[RESULT]` `[from: NUM]` `[scope: diagnostic]` **AZ-2 attempted; negative-clarifying. No Level B promotion.**  
The first angular-spectrum candidate (the Core(G_T) `4|q` rule) was tested and **disqualified as a bridge-candidate**, because the effect is static $\mathbb{Z}_N$ substrate geometry rather than a dynamical class discriminator. This is the opposite of the AZ-2 Level-B gate condition: rather than an observable that distinguishes TDR-G dynamical ensembles, the most tempting observable was reproduced, in the tested null protocol (§4.3.3 Chain 2), by a core-matched random-$\theta$ antipodal-band null without TDR-G dynamics, so it is not specific to the dynamics. `[bridge-disqualified]` `[RID: TDRG-AZ-STATIC-ZN-4Q]`

This is a genuinely useful negative: it removes the angular Hashimoto spectrum from the OPEN-P1 bridge-candidate pool and sharpens the SG-AZ-7 guard with a concrete worked example (§3). A genuine bridge-candidate must be a TDR-G-**dynamical** observable; the static angular spectrum is geometry-saturated and is not one. AZ-2 remains OPEN for such an observable.

#### §4.3.6 Scientific open items (Thread C)

`[OPEN]` **A dynamical (non-substrate) graph observable.** The angular spectrum is geometry-saturated. Candidate dynamical observables that are NOT fixed by the $\mathbb{Z}_N$ antipodal substrate: birth-window graph evolution (the $G_{\rm birth}(w)$ sequence; the object has two different definitions in the deposited files, §9, and has to be fixed before use), advance-spectrum statistics along the trajectory, or inter-birth-interval structure (cf. the TDR-G response-tensor branch's one surviving N-dependent feature, inter-birth-interval CV). Any such observable must be null-gated against BOTH a degree/reciprocal null AND the $\mathbb{Z}_N$ geometry null before it can be called dynamical.

`[OPEN]` **Analytic completion of the `4|q` mechanism.** The low-order obstruction (§4.3.2) is `[ALG]`; the full angular-weight derivation and the (falsified-prediction) $k$-dependence are not yet understood. This is a clean branch-local analytic target — but note it concerns substrate geometry, not dynamics, so closing it would not produce a bridge.

`[OPEN]` **Transfer-zeta determinant / poles as cascade or policy diagnostic.** Untested under the certified engine; subject to SG-AZ-1/SG-AZ-2 (no RH/prime-mysticism reading of pole locations) and SG-AZ-5 (provenance).

---

## §5. High-Risk Claims Ledger

| Claim | Valid form | Forbidden overclaim | Guard |
|---|---|---|---|
| RH motivation | Historical `[HEUR]` only (§1.2) | Any proof, disproof, reformulation, or physical derivation of the Riemann Hypothesis | SG-AZ-1 |
| Prime relevance | Only through explicit mechanisms | Vague appeal to "primes appearing" | SG-AZ-2 |
| Dyadic OPEN 9 results | `[import-ref]` — ownership stays in Dyadic DSN | Retagging as this study's own `[ALG]`/`[THM]`/`[OPEN]` | SG-AZ-6, SG-AZ-0.4 |
| Low-degree anti-holomorphic boundary | Dyadic-map-specific `[import-ref]`: $b\le4$ vanishing, $b=5$ all-$p$ failure | General-coefficient or all-$b\ge5$ theorem; cross-branch theorem | SG-AZ-6 |
| TDR-G arithmetic structure | Branch-local / `[bridge-candidate]` from Discrete Genesis v2.12.14 | Active cross-branch import; evidence for Dyadic/bridge claim | SG-PROG-1, SG-AZ-3 |
| TDR-G BIND3 / advance-spectrum | Three-node/no-birth or specified source scope only | Full TDR-G theorem through star blow-up or continuum bridge | SG-PROG-1, SG-AZ-3 |
| TDR-26 discriminator | Branch-local dataset separation `[NUM cross-cell, n=2]`; classifier `[HEUR]` | Theorem-grade, universal, or cross-branch evidence | SG-PROG-1, SG-AZ-3, SG-AZ-7 |
| **Thread C engineering** | **`[ENG PASS]` — certified, exit-code-gated (§4.3.1); availability of the artifacts per entry in §9** | Treating any single run as certified without its manifest/hash/null provenance | SG-AZ-5 |
| **PROP-AZ-CORE-EQUIV** | **`[THM]` (proof in §4.3.2), scope: finite simple undirected, both-orientations, no multiedges/self-loops; closed walks non-backtracking at every step including the closing one** | Applying it to arbitrary directed exports or multigraphs; claiming strong connectivity of the transition graph; reading the enumeration certificate as the proof | SG-AZ-6 (Thread-C-owned) |
| **Antipodal-band low-order obstruction** | **`[ALG]`: no $L=2,3$ closure under $k<N/6$; $L=4$ first constructible closure; odd closure impossible when $Lk<N/2$ (necessary obstruction bound)** | "$\operatorname{Tr}(B^L)=0$ for all odd $L$"; exact 4th-root spectrum; treating $Lk\ge N/2$ as a sufficiency/existence theorem; promoting the full `4|q` rule to `[ALG]` | §4.3.4 retraction |
| **`4|q` angular rule** | **`[NUM diagnostic]`: static $\mathbb{Z}_N$ antipodal-band geometry; the link to the low-order obstruction is `[HEUR]`** | TDR-G dynamical signal; bridge-candidate; analogue of Dyadic subgroup charge | SG-AZ-4, SG-AZ-7 |
| Graph-zeta diagnostics generally | Certified engine; results require full provenance | Reporting a spectral value without graph object/spectrum mode/null/eps-angle/version/hash | SG-AZ-5 |
| Continuous $p$-resonance results | Reference-only from Dyadic DSN; conditionally physical under OPEN-P0 | Physically primitive or generator-independent | SG-PROG-2 |

---

## §6. Bridge-Candidate Connections

This section records the potential connections between threads and between this study and the programme-level open problems. All items are `[bridge-candidate]`, `[bridge-disqualified]`, or `[OPEN]`; none is an active import.

**To Dyadic OPEN 9:**  
Thread A indexes the Dyadic arithmetic horizon by reference to `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 (`dyad-v6.4.24`) (§8). The active arithmetic frontier is the owner's (Dyadic §2 OPEN 9) and is not listed here.

**To OPEN-P1 (discrete-continuous bridge):**  
Thread B defines the TDR-G $\mathbb{Z}_N$ arithmetic structure as a candidate observable family for OPEN-P1; these remain branch-local until a named bridge theorem exists; SG-AZ-7 blocks vocabulary-similarity promotion.  
**`[bridge-disqualified]`:** the Core(G_T) `4|q` angular Hashimoto observable is REMOVED from the bridge-candidate pool. It was the most tempting candidate (a divisor-graded selection rule, superficially like Dyadic cyclic-subgroup selection), and it is exactly the SG-AZ-7 trap: it is static $\mathbb{Z}_N$ substrate geometry (§4.3.2–§4.3.4), so a resemblance to Dyadic subgroup-charge structure is vacuous. Recorded here so it is not re-proposed.

**To Genesis OPEN 1 (phase-moment distribution):**  
`[OPEN]` Whether $p$-resonance arithmetic selects the physical phase moments for the cascade condition $\langle\mathcal{P}_4\rangle>0$ is downstream of both Thread A and the Genesis study; recorded only as a candidate after the relevant Genesis/Triadic phase-import gates resolve.

**To Genesis OPEN 1 / cascade criterion:**  
`[bridge-candidate]` In Genesis v2.10, OPEN 1C (triad chiral admissibility surface, `GEN-OPEN-CHIRAL-ADMISS`) is closed `[THM]`. Separately, within OPEN 1 (`GEN-OPEN-PHASE-DIST`, active) the $\mathcal{P}_4$-only cascade is impossible `[RESULT]` `[scope: reduced birth-race model]` — a statement about the reduced model, not about arbitrary phase measures; cascade then requires a non-$\mathcal{P}_4$ source, and the question routes through OPEN-GEN-II-7B (`GEN-OPEN-UVJET-ALPHAF`) and OPEN M. A Thread C spectral observable could in principle serve as an independent discriminator for crystallizing-vs-growth TDR-G policy branches — but only a DYNAMICAL one would qualify; the angular spectrum does not (§4.3.4). Speculative; `[SG-AZ-3, SG-AZ-4, SG-PROG-1, SG-AZ-7 apply]`.

**To OPEN M:**  
`[bridge-candidate]` The $p=6/K_4$ face-flux identity $\lambda=e^{iF_f/2}$ is a Dyadic import-ref. The SU(2) energy ratio $E_{\rm full}/E_{\rm half}=4$ is source-scoped, and the OPEN-M cascade test is linear in the admitted source amplitude $\|H\|_B$. OPEN-M v0.7.1 certifies no numerical deficit factor: R16 (`UVM-RESULT-AUDIT1`, `[COR]`) withdraws the earlier "legal SU(2) correction $=2\times$" as a physical conclusion — the $2\times$ branch is conditional on two unproved bridges (the source identification and an $E\propto A^2$ constitutive relation), and the $4\times$ energy factor is likewise not directly admissible in the amplitude-linear inequality — and R15 (`UVM-NUM-2F-RHO`) is a calibration-conditional proxy diagnostic. No arithmetic-horizon or graph-zeta result in this DSN contributes to or supersedes that verdict. `[import: RTG_OPEN_M_DSN v0.7.1 R15, R16 | UVM-NUM-2F-RHO; UVM-RESULT-AUDIT1]` (reference only) `[SG-AZ-6, SG-PROG-4]`

**To Programme Overview §6:**  
This study is a Tier 5 infrastructure entry and is registered in Programme Overview v1.4 (its §6.1, §6.5 and §7.2). See §7.

---

## §7. Programme Registration

`[DEF]` This study is registered in `RTG_PROGRAMME_OVERVIEW` v1.4 (`programme-v1.4`): the document inventory (its §6.1; Tier 5, canonical infrastructure), the study entry (its §6.5), the cross-study dependency graph (its §7.1; a reference edge from Dyadic to Thread A and an edge from TDR-G to Threads B/C) and the interface register (its §7.2; IF20 Dyadic → AZ, reference-only, and IF21 TDR-G → AZ). The Programme's maintenance proposals for this study (its §6.7 and §9.2) are Programme records; the reduction of restated owner text asked for in its §6.7 is carried out in this edition by the PI's decision, and no merger with another study is made.

---

## §8. Import Ledger

This document makes no active cross-branch imports and no load-bearing import: no result of this DSN is derived from a row below. Each owner result is cited once, here; §1.2, §4.1, §4.2 and §6 refer to these rows. The Thread C internal results (§4.3.2) and the Phase-2 diagnostic (§4.3.3) are owned by this DSN and are not imports.

Row format: identifier :: readout of the owner statement, with its limitations :: source edition and location :: owner tag and inherited scope. A readout is not the statement: the owner's text at the pinned edition governs. The remaining fields of Methodology §4.3 are the same for every row of a group and are given once, by key:

- **IMP-A** (rows of the first group). Local use: reference-only index of Thread A (`[import-ref]`); no local consequence is derived. Depends on: the owner's definitions and conventions and the selected continuous generator (SG-PROG-2); no bridge is used or claimed (SG-AZ-3). Verification: owner statements read at `dyad-v6.4.23` for edition v0.7 (`EV-SRC-READ`; `records/az/AZ_v0_7_RELEASE_RECORD.md`); no owner artifact inspected or rerun (`EV-NOT-RERUN`). Synchronization: checked against `dyad-v6.4.24` — the difference between the two owner editions changes no statement of a cited identifier (it changes the owner's table of consumer strings, which names this document).
- **IMP-B** (rows of the second group). Local use: branch-local context and `[bridge-candidate]` observable family of Thread B; not a cross-branch import (SG-PROG-1, SG-AZ-3, SG-AZ-0.4). Depends on: the owner's definitions, clock and orientation conventions as the owner states them; any use beyond branch-local context requires a named OPEN-P1 bridge, and none exists. Verification: owner statements read at `tdrg-v2.12.14` for edition v0.7 (`EV-SRC-READ`); no owner artifact inspected or rerun for these rows (`EV-NOT-RERUN`). Synchronization: `tdrg-v2.12.14` is the governing edition; nothing pending.

### Reference imports from `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 (`dyad-v6.4.24`) — clauses IMP-A

- [RID: DYAD-THM-RAW-CUBIC] :: Raw cubic theorem (raw one-step map, $p\ge3$; owner caveat on the historical proposition). It is not a statement about the raw $p$-step map. Owner caveat: the formula is recovered and algebraically verified; its identity with the historical proposition is not yet established (Dyadic Appendix E, `dyad-v6.4.24`). :: `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 §2 OPEN 9 :: `[THM]`
- [RID: DYAD-ALG-P567-LEDGER] :: Finite one-step ledger $p=5,6,7$ ($p=6$: in the one-step engine/DSN bridge convention; distinct from the raw six-step Lie-gauge coefficient) :: `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 §2 OPEN 9 / §6.11 (located by identifier) :: `[ALG]`
- [RID: DYAD-ALG-GLATTICE5] :: $p=5$ lattice cancellation $G_{\rm lattice}(5)=0$; both $F_1^5(0,4)$ and $F_{\rm raw}^5(0,4)$ are nonzero and equal. This remains the unique non-trivial degree-4 lattice bridge cancellation in the certified finite ledger. :: `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 §6.11 :: `[ALG]`
- [RID: DYAD-OPEN-P-RESONANCE] :: items of the owner's OPEN 9 record (the sub-labels are not identifiers). $G_{04}(10)=0$ reinterpretation `[ALG]`: Not divisor inheritance: $(0,4)$ is dynamically active in $J^{extra,raw}_{10,5,D}$. Sub-horizon inheritance conjecture `[RETRACTED]` `[scope: reframed]`. Cascade boundary $p=12$, $q=4$, $(0,3)$ `[ALG]`: Exact value $-13 + 15\sqrt{3}/2 \neq 0$; $|-13+15\sqrt{3}/2| \approx 0.0096$. Universal $q=4$, $(0,3)$ cancellation `[FAIL]`: Not universal; $p=12$ is a counterexample. Prime-horizon first-lattice transparency `[FAIL]`: $G_{06}(7) \neq 0$: exact $p=7$ counterexample. Subgroup-charge projector / missing-slot formalism `[ALG]`: The closed cardinality lemma $|K^{\rm extra}_{p,q}|=s-1$ makes the formalism computable without raw case enumeration in the registered sub-horizon setting. Owner evidence boundary (Dyadic Appendix D, `dyad-v6.4.24`): $\chi_p$, $K^{\rm extra}_{p,q}$ and the cardinality lemma are defined; the other eight objects ($\mathcal{Q}(p)$, $\Pi^{\rm extra}_{p,q}$, $J^{extra,raw}_{p,q,D}$, $\mathcal{B}^{extra}_{p,q,D}$, $Z^{\rm miss}_{p,q,D}$, $C^{\rm mult}_{\rm sub}$, $C^{\rm uniq}_{\rm sub}$, $\Delta_{\rm overlap}$) keep their names without a recovered definition, so they are not usable here for independent computation. :: `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 §2 OPEN 9 :: owner tags per item, as printed
- [RID: DYAD-THM-Q403-PHASELAW] :: cubic cascade $q=4,(0,3)$ phase/factorization law, $p=4s$, $s\ge2$; $p=8$ is the zero degeneracy ($Q_8=0$). This closes the exact cascade formula for the family $p=4s$; it is not a generic-$s$ formula. :: `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 §6.11 :: `[THM]` `[scope: all $p=4s$, $s\ge2$]`
- [RID: DYAD-ALG-VANISH-B2] :: $F_{\rm raw}^p(0,2)=0$ for $p\ge4$; exception $p=3$ :: `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 §2 OPEN 9 / §6.11 (located by identifier) :: `[ALG]`
- [RID: DYAD-ALG-VANISH-B3] :: $F_{\rm raw}^p(0,3)=0$ for $p\ge5$; boundary $p=3,4$, by automatic $\beta$-mode path enumeration; boundary cases $p=3$ and $p=4$ are nonzero, with $p=4$ arising from cross-path contribution rather than the direct-resonant $p=b+1$ case alone. :: `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 §2 OPEN 9 / §6.11 (located by identifier) :: `[ALG]`
- [RID: DYAD-ALG-VANISH-B4] :: $F_{\rm raw}^p(0,4)=0$ for $p\ge6$; boundary $p=4,5$, by automatic $\beta$-mode path enumeration; boundary cases $p=4$ and $p=5$ are nonzero, with $p=4$ a small-$p$ cross-contribution case and $p=5$ the direct-resonant/lattice-anomaly boundary. :: `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 §2 OPEN 9 / §6.11 (located by identifier) :: `[ALG]`
  For the three vanishing rows: Boundary precision: the clean statement is $p\ge b+2$, not "$p\ne b+1$". Nonzero boundary cases include the direct-resonant $p=b+1$ cases and additional small-$p$ cross-contribution cases: $p=3,4$ for $b=3$ and $p=4,5$ for $b=4$.
- [RID: DYAD-ALG-B5-ALLP-NONVANISHING] :: channel boundary at $b=4$: vanishing for $b\in\{2,3,4\}$, failure at $b=5$ for every $p\ge6$. The all-$p$ $b=5$ failure is proved by secular-mode extraction plus cyclotomic non-division, not merely finite scan. No "iff $b\le4$" statement is made (the owner withdrew that shorthand). :: `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 §6.11 :: `[ALG]`; dyadic-map scope; all-$b\ge5$/general-coefficient `[OPEN]`; `DYAD-OPEN-B5-ALLP` is the closed lifecycle identifier
- [RID: DYAD-ALG-DIRECT-WEIGHT] :: direct weight $\lambda^{-(b+1)k}$, orbit-sum vanishing for $p\nmid(b+1)$. Scope precision: the all-$p$ $b=5$ failure is not a consequence of the direct-weight argument alone; it uses a separate secular-coefficient nonvanishing and cyclotomic non-division proof for the dyadic map (`DYAD-ALG-B5-ALLP-NONVANISHING`, with `DYAD-ART-B5-SECULAR` as the secular-coefficient artifact; `DYAD-OPEN-B5-ALLP` is the closed lifecycle identifier). :: `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 §2 OPEN 9 :: `[ALG]` (exact)
- [RID: DYAD-ALG-CROSS-IDENTITY] :: cyclotomic cross-term identity for $p\ge5$. This exact cyclotomic sum cancellation is used in the degree-4 vanishing proof to eliminate the only possible cross-path contribution in the clean range. :: `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 §2 OPEN 9 :: `[ALG]` (exact)
- [RID: DYAD-ALG-Q3-DEG2-CANCEL] :: degree-2 $q=3$ anti-holomorphic cancellation (raw Birkhoff-strobe). For all $p>3$ with $3\mid p$, $\operatorname{Coeff}_{(0,2)}[\tau_{\le D}(L_p^{-p/3} f_p^{p/3}-\mathrm{Id})]=0$ for all $D\ge2$. Two-component structure: (a) reachability — the $(0,2)$ slot is dynamically active in the one-step map for $p>3$, so the zero is not vacuous; (b) cancellation — the $s$-step strobe kills the reachable slot by a geometric phase sum of a primitive $s$-th root of unity at the direct-averaging layer, anchored by the eigenframe linear-part lemma (the owner keeps that lemma `[ALG]`; its statement is not recovered, Dyadic Appendix D, `dyad-v6.4.24`). This is a closed general sub-horizon cancellation theorem and a clear source-scoped example of composite-horizon cyclic-subgroup structure producing a selection rule. :: `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 §6.11 :: `[ALG]` `[conv: raw Birkhoff-strobe]`
- [RID: DYAD-ALG-P6-FACEFLUX] :: $p=6/K_4$ face-flux identity. The identity is exact in Dyadic, but any transfer to OPEN-M source amplitude remains a conditional candidate in the owner documents and is not a Zeta result. :: `RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 §2 OPEN 9 / §6.11 (located by identifier) :: `[ALG]` (exact)

### Branch-local context from `RTG_DISCRETE_GENESIS_DSN` v2.12.14 (`tdrg-v2.12.14`) — clauses IMP-B

- [RID: TDRG-DEF-ZN-STATE] :: $\mathbb{Z}_N$ phase universe, variable-size state (the consumer name `TDRG-ZN-STATE` resolves to it through the owner's §7 map) :: `RTG_DISCRETE_GENESIS_DSN` v2.12.14 §6.1 :: owner `[DEF]`
- [RID: TDRG-DEF-PHYSICAL-STATE] :: physical state as the quotient by global phase shift; relational phases $\Delta_{ij}$ (absolute-phase gauge) :: `RTG_DISCRETE_GENESIS_DSN` v2.12.14 §6.1 :: owner `[DEF]`
- [RID: TDRG-DEF-BAND] :: defect band $\mathcal{D}_k$. This gives Thread B a concrete arithmetic memory horizon $(N,k)$, but not yet a bridge to Dyadic $p$-resonance. :: `RTG_DISCRETE_GENESIS_DSN` v2.12.14 §6.1 :: owner `[DEF]`
- [RID: TDRG-ALG-LEM-REACH] :: band-form reachability/superselection ($k=0$: `TDRG-THM-REACHABILITY-K0`); superselection persists at $k>0$ in the two-node universe. :: `RTG_DISCRETE_GENESIS_DSN` v2.12.14 (located by identifier) :: owner tags `[THM]` (the $k=0$ statement) and `[ALG]` (band form); `[scope: branch-local]`
- [RID: TDRG-ALG-LEM-RETRIG] :: two-node retrigger threshold; bound state of period dividing 2, possible iff $|d|_c\le2k$. This is arithmetic memory inside TDR-G only; it is not evidence for Dyadic resonance closure. :: `RTG_DISCRETE_GENESIS_DSN` v2.12.14 (located by identifier) :: owner `[ALG]`; `[scope: two-node TDR-G]`
- [RID: TDRG-ALG-LEM-SPECCONS] :: three-node no-birth advance-spectrum conservation; the gcd multiset as a consequence only — the converse fails (owner counterexample at $N=24$: $|d|_c=1$ and $|d|_c=5$ share $\gcd=1$). Star blow-up creates new nodes and new pairwise advances; generalization beyond the no-birth sector remains source-scoped/open. :: `RTG_DISCRETE_GENESIS_DSN` v2.12.14 (located by identifier) :: owner `[ALG]`; `[scope: 3 nodes, no star blow-up]`
- [RID: TDRG-ALG-BIND3-CYCLE-N24K1; TDRG-NUM-BIND3-PARITY; TDRG-NUM-BIND3-SPECTRAL-GATE; TDRG-NUM-BIND3-MEMORY-PARITY; TDRG-NUM-BIND3-XFER; TDRG-NUM-BIND3-REGEN; TDRG-OPEN-BIND3-NKSCAN] :: cycle enumeration / NKSCAN; survival parity, spectral gate, even-sector memory correction. BIND3-KNIFE is `[FAIL]`/`[REPLACED]`, and the odd-sector memory claim is `[COR]` as a composition artifact. :: `RTG_DISCRETE_GENESIS_DSN` v2.12.14 (located by identifier) :: owner tags `[ALG]` (cycle enumeration) and `[NUM strong]` (the `NUM` identifiers); `[scope: N=24,k=1; no-birth/three-node]` `[conv: v18 path orientation]`; these numbers were computed with the orientation completion the owner has since superseded and are not rerun by the owner
- [RID: TDRG-OPEN-NSCALING; TDRG-OPEN-CRYSTALLIZATION] :: TDR-G v2.12.14 reports that $k/N$ controls entry into the growth regime and that the canonical clean branch (`bound_symmetric`) shows bulk-conditioned birth rate $B_{\rm bulk}/\text{step}\sim1.041\cdot N^{-0.869},\quad R^2=0.973$ at fixed $k/N=1/15$, $T=5000$, over $N=120$–$1440$, excluding tail runs $M>500$ (full-range composite fit). The exponent is window-dependent: read on $N=480$–$1440$ the same scan gives $N^{-0.730}$, and $-0.869$ is the owner's full-range value, not a structural constant. Thermodynamic crystallization in the $N\to\infty$ limit is a `[HEUR]` extrapolation in the source, not theorem-grade. :: `RTG_DISCRETE_GENESIS_DSN` v2.12.14 §1 :: owner tags `[NUM]` (fit) and `[HEUR]` (limit); `[conv: v18 path orientation]`
- [RID: TDRG-OPEN-LOCKING-FAIL] :: OPEN TDR-26 birth-anchored discriminator over $[\mathrm{fb},\mathrm{fb}+200)$, $N=720,722$ (combined TP=2, FP=0, FN=0, TN=198). Source tag split must be preserved: the dataset separation is `[NUM cross-cell, n=2]`, while the classifier/out-of-sample claim remains `[HEUR]` pending batch-scale validation. For this DSN it is a branch-local memory-window observable only, not a bridge theorem. :: `RTG_DISCRETE_GENESIS_DSN` v2.12.14 §2 OPEN TDR-26 :: owner tags as split in the statement
- [RID: TDRG-OPEN-TOPO-FILTER; TDRG-OPEN-CHI-SCALING; TDRG-OPEN-THERMO-SUPPRESS] :: In TDR-G v2.12.14 the slot-volume identity (TDR-24D) and the structural-to-slot projection (TDR-24F) are closed at the mechanism level, with their analytic constants open; the gate before discrete triadic dynamics is TDR-24A (topological filtering, `TDRG-OPEN-TOPO-FILTER`) → TDR-24B (pair-to-component compression, `TDRG-OPEN-CHI-SCALING`) → TDR-24C (thermodynamic suppression, `TDRG-OPEN-THERMO-SUPPRESS`). This DSN may track arithmetic/zeta observables that could assist TDR-24 or future OPEN-P1, but cannot promote them without source-DSN closure and bridge routing. :: `RTG_DISCRETE_GENESIS_DSN` v2.12.14 §2 :: owner OPEN modules; mechanism-level closures as the statement says

### Bridge-required / bridge-disqualified export candidates

- [RID: AZ-EXPORT-ZETA-SPECTRUM] :: Hashimoto/transfer-zeta spectral statistics :: engine `[ENG PASS]`; cross-branch use still blocked by OPEN-P1
- [RID: TDRG-AZ-STATIC-ZN-4Q] :: Core(G_T) `4|q` angular rule :: **`[bridge-disqualified]`** — static $\mathbb{Z}_N$ geometry; removed from bridge-candidate pool (§4.3.4, §6)
- [RID: AZ-EXPORT-ADVANCE-SPECTRUM] :: TDR-G advance-spectrum statistics as candidate OPEN-P1 observable :: branch-local until OPEN-P1 defines a bridge observable
- [RID: AZ-EXPORT-TDR26-BIRTH-WINDOW] :: TDR-26 birth-anchored memory-window discriminator :: branch-local until OPEN-P1 + source batch-scale validation

---

## §9. Artifact and Script Registry

**Availability and evidence states.** The Thread C files are in the repository only in part. A partial recovery was deposited unchanged under `upload/az-records/` on 11 November 2026; it is hash-checked and replayed in `records/az/AZ_UPLOAD_HASH_CHECK_20261111.md` (replay in `evidence/az/az_v5_replay/`). Each entry below states its own state with the keys of Methodology §12.2. Where an entry says *source-reported*, its certification and hashes are reported from the June 2026 Thread C work (`EV-SRC-REPORTED`), its bytes are not in the repository and nothing was rerun (`EV-NOT-RERUN`); such an artifact is not described as recreated. SG-AZ-5 provenance for a source-reported artifact is by pointer to the registry and the per-result manifests and cannot be inspected from the repository until the files are supplied unchanged and hash-checked against the registry. The existing grades are kept with this verification limit; it applies wherever this document calls a Thread C artifact hashed or certified (§4.3.1, §5). This DSN lists RID-level artifact identities and does not duplicate the registry's hashes inline, except the identity of each deposited file.

- [RID: AZ-ART-AZV5-REGISTRY] :: `az_v5` package + SHA-256 manifest, as received: the AZ-1A/AZ-1B registry of ten files (lib/hashimoto, graphgen, graphio, manifest; benchmark_ladder; validate_solver; az1b_certify; two benchmark files; the synthetic benchmark report) :: certified engine, exit-code-gated; **canonical hash source** for these ten files :: `[ENG PASS]`  
  Availability: deposited at its AZ-1B registry state. The registry `upload/az-records/az_v5/benchmarks/AZ_ARTIFACT_REGISTRY.json` (SHA-256 `6686706490c0f4d1d90629aaf6594176faff333096d4b0e3834128ff75ba875a`) and nine of its ten entries are original bytes with hashes equal to the registry (`EV-BYTES`, `EV-HASH`); the tenth, the synthetic benchmark report, is regenerated with the registry's hash and is not the original file. Replayed: the AZ-1A ladder, the solver acceptance and the AZ-1B gate, exit code 0, and the registry regenerated byte-identically (`EV-RUN`).  
  Not covered: `phase2_harness`, which earlier editions listed under this identifier, is not an entry of the received registry and is not in the repository. The Phase-2 harness, and any later registry state that may have covered it, are source-reported.
- [RID: AZ-ART-CONVENTIONS-FROZEN] :: `CONVENTIONS_FROZEN.md` (CONV-AZ-GRAPH-EXPORT, DEF-AZ-CORE, CONV-AZ-SPECTRUM-MODE, CONV-AZ-STATS-MULTITEST, CONV-AZ-NULLS, CONV-AZ-ANGLE-ZERO, SG-PLAN-*) :: frozen conventions :: `[ENG PASS]`  
  Availability: a file of that name is deposited (`upload/az-records/CONVENTIONS_FROZEN.md`, SHA-256 `1c4b715aea0785c22c2f194d9cf8ba6a1b3c76dc2608366dedd58160ed478f2d`; `EV-BYTES`). It contains CONV-AZ-GRAPH-EXPORT, DEF-AZ-CORE, CONV-AZ-SPECTRUM-MODE, CONV-AZ-STATS-MULTITEST and CONV-AZ-NULLS; it does not contain CONV-AZ-ANGLE-ZERO or a manifest convention. It is therefore not shown to be the frozen state this DSN cites; that state, and CONV-AZ-ANGLE-ZERO in particular, is source-reported.
- [RID: AZ-ART-AZ1B-CERTIFY] :: `az1b_certify.py` ingestion/export/provenance + manifest-hardening certification suite :: `[ENG PASS]`  
  Availability: deposited (`upload/az-records/az_v5/az1b_certify.py`, SHA-256 `7a0f8aa5b9aa5e6debd3510c3c6e330b68bb15632ab1cbe8d0dfacddb1bcc02b`), hash equal to the registry, replayed with exit code 0 (`EV-BYTES`, `EV-HASH`, `EV-RUN`). The deposited suite exercises the loader, the export convention and the manifest validator on synthetic graphs and one example manifest; it reads no TDR-G export. The part of AZ-1B that concerns real TDR-G exports (§4.3.1) is source-reported.
- [RID: AZ-ART-SPECTRAL-RADIUS-PATCH] :: `spectral_radius_patch.py` (ARPACK `which='LM'`; replaces buggy power-iteration that mis-handles $\pm R$ dominant pairs; certified to dense $<10^{-6}$) :: `[ENG PASS]`  
  Availability: source-reported.
- [RID: AZ-ART-PROP-CORE-EQUIV] :: `prove_core_equiv.py` + `CORE_EQUIV_CERT_aggregate.json` + `CORE_EQUIV_CERT_n7.json` (2,141,014 graphs, 0 counterexamples) :: enumeration certificate reported for PROP-AZ-CORE-EQUIV; corroboration, not the basis of its grade (§4.3.2)  
  Availability: source-reported.
- [RID: AZ-ART-CORE-EQUIV-CHECK] :: `evidence/az/core_equiv_check/az_core_equiv_check.py` (SHA-256 `bd1ee6f7bf31a3db35f88d45006ff7c1f8ac32960a2bf9cf178ed228d6170b9a`) and its output `output_nmax7.txt` :: finite check of PROP-AZ-CORE-EQUIV made for this edition: the recurrent core computed from the definition against the 2-core on all 2,131,019 labelled simple graphs with at most 7 vertices, 0 mismatches; cross-checked on the 1,099 graphs with at most 5 vertices against the deposited `build_hashimoto` and the deposited exporter's core routine; four negative-control checks of three kinds (a wider closed-walk definition, on one graph and over all labelled graphs on 5 vertices; no stripping; one orientation per pair), each reporting a difference as it must :: corroboration of PROP-AZ-CORE-EQUIV (§4.3.2)  
  Availability: in the repository; inspected and executed on 12 November 2026, Python 3.13.18, exit code 0 (`EV-BYTES`, `EV-CODE`, `EV-RUN`). It is not `AZ-ART-PROP-CORE-EQUIV` and does not reproduce it.
- [RID: AZ-ART-ANTIPODAL-LOWORDER] :: `THM_AZ_ANTIPODAL_4Q.md` (corrected v2: low-order obstruction `[ALG]`; angular rule heuristic with numerical support; retraction of v1 exact theorem) :: certificate for `[ALG]` antipodal-band low-order obstruction  
  Availability: source-reported.
- [RID: AZ-ART-PHASE2-N120-CORE] :: `run_phase2_baseline.py` + `AZ_PHASE2_MULTIN_RESULT.md` + the three registered Null1 reports `AZ_PHASE2_N120_CORE_NULL1_v1.json`, `AZ_PHASE2_N180_CORE_NULL1_v1.json`, `AZ_PHASE2_N240_CORE_NULL1_v1.json` (per-q tables, Null0+Null1, 1000 nulls × 5 seeds) :: Phase-2 diagnostic evidence (Chain 1)  
  Availability: source-reported. An unregistered smoke report of the same family is deposited (`upload/az-records/phase2/AZ_PHASE2_N120_NULL1_smoke.json`, SHA-256 `561c66ac8e5d359d5806d9aa058e988b682412ddb4a84e71371e754e89e22284`; `EV-BYTES` only); it is not one of the registered reports and supports no statement of §4.3.3.
- [RID: AZ-ART-THETA-CORE-MATCHED] :: `AZ_THETA_CORE_MATCHED.json` (core-matched random-theta antipodal-band null reproduces 4|q; per-q, N=120/180/240) :: certificate for the static-geometry reclassification (Chain 2)  
  Availability: source-reported.
- [RID: AZ-ART-ZETA-V3] :: `rtg_graph_zeta_proto_v3.py` :: historical; superseded by `az_v5`; all v3 runs unverified; not the source of any result of this DSN  
  Availability: source-reported.
- `conv_az_graph_export.py`, self-identifier `TDRG-AZ-EXPORT-BASELINE` (no `AZ-ART` identifier was assigned to it in the June 2026 work; the identifier is this study's, see the owner map) :: graph exporter for CONV-AZ-GRAPH-EXPORT (both orientations; objects G_T, Core(G_T), G_birth(w), G_cumulative)  
  Availability: deposited (`upload/az-records/export/conv_az_graph_export.py`, SHA-256 `fab14ae1d2b151f405bda105103ec3fcca32841542369304d1d1a5b35517fe1e`; `EV-BYTES`); its self-test replayed (`EV-RUN`). As received, the loader `lib/graphio` of the deposited package does not read its object files without an adapter, and the deposited files do not show that it produced the registered Phase-2 exports.

**Two definitions of `G_birth(w)` in the deposited files — recorded, not resolved.** The deposited `CONVENTIONS_FROZEN.md` defines `G_birth(w)` as the birth-window graph over `[t_first_birth, t_first_birth + w]`, default `w = 200`; the deposited exporter defines it as the snapshot at the tick of the `w`-th birth. Which of the two the June 2026 work used cannot be read from the deposited files. No registered result of this DSN uses `G_birth(w)` (the Phase-2 results use Core(G_T)); the object is named only as a candidate in §4.3.6 and in the graph-object list of SG-AZ-5, and has to be fixed by an explicit definition before any result is registered on it.

---

## §10. Collaboration and Audit Record

Authors: Mustafa (PI) · Claude · ChatGPT · Gemini · Grok

- **November 2026 — v0.7 corrections edition.** Prepared from v0.6 (tag `az-v0.6`) against the current adopted owner editions (Dyadic v6.4.23, TDR-G v2.12.14, Genesis v2.10, Programme v1.4, OPEN-M v0.7.1), limited to list (i) of `records/az/AZ_REACTIVATION_TRIAGE.md` as decided by the PI on 10 Nov 2026. No new science and no Thread C change; edit-level record in `records/az/AZ_v0_7_RELEASE_RECORD.md`.
- **June 2026 — v0.6 ledger-state update (with audit patch round).** Prepared from v0.5 plus the Thread C engineering/audit/Phase-2 work and the attached structured audits. Scope: recorded AZ-1 closure (AZ-1A/1B/1C `[ENG PASS]`); registered AZ-OPEN-EDGE resolution; registered `[THM-ALG]` PROP-AZ-CORE-EQUIV and `[ALG]` antipodal-band low-order obstruction; registered the Phase-2 `4|q` result and its reclassification as static $\mathbb{Z}_N$ geometry; added the §4.3.4 retraction block; revised SG-AZ-5 from a pre-science gate to a provenance guard; added the SG-AZ-7 worked example; recorded AZ-2 as attempted/negative-clarifying with no Level B promotion; populated §9 with real hashed artifacts. Post-draft audit patches applied: (1) odd-closure threshold softened to a necessary obstruction bound, not a sufficiency/existence theorem; "$L=4$ shortest" → "first constructible closure scale"; (2) G_cumulative retraction reason corrected (Null1/topology control, not a radius-bug artifact); (3) the `4|q` evidence split into Chain 1 (Null0/Null1 statistical excess) and Chain 2 (core-matched theta per-$q$ comparison) with distinct scope and sample size; (4) §9 artifact hashes pointed to the manifest source and the shorthand `N120/180/240` path expanded to exact registered file names; (5) per-$q$ $z$-score claim made artifact-scoped rather than quoting an inline range. Maturity remains Level A. No cross-branch import; no bridge-candidate promoted. Multiple internal self-corrections (spectral-radius bug, core-definition mismatch, v1 exact-theorem counterexample, falsified $k/N$ prediction) are recorded permanently per error-culture policy.
- **June 2026 — v0.5 precision patch.** Corrected stale v0.3 wording; sharpened direct-weight/$b=5$ attribution; expanded degree-2 $q=3$ theorem; added `[ENG-open-3]`; added SG-AZ-1/2 guards on the zeta-pole item. Thread C engineering-blocked at that time.
- **June 2026 — v0.4 post-audit correction patch.** Added Dyadic import-ref mechanisms, TDR-26 branch-local discriminator, SG-AZ-7, blocker sequencing, Genesis/OPEN-M precision notes.
- **June 2026 — v0.3 source-refresh patch.** Pointer updates to Dyadic v6.4.8.1 / Discrete Genesis v2.12; Thread A/B refresh.
- **June 2026 — v0.1/v0.2.** Initial draft and consistency pass.

---

## Appendix A — Version History

### v0.8 — November 2026
Methodology v1.4 migration with a declared section map (§0.3), the reduction asked for in Programme §6.7, and availability corrections. Each owner result is cited once, in §8; restated Dyadic and TDR-G text is removed from §1.2, §4.1, §4.2 and §6. PROP-AZ-CORE-EQUIV is `[THM]` on a written proof (§4.3.2), replacing the bare `[THM-ALG]`; a finite check is registered (`AZ-ART-CORE-EQUIV-CHECK`). The static-geometry reading of the `4|q` rule (`TDRG-AZ-STATIC-ZN-4Q`) is stated at the scope of its numerical evidence (SG-AZ-7, §4.3.5). §9 gives per-artifact availability after the partial recovery of 11 November 2026. Dyadic pin: `dyad-v6.4.24`. No new scientific result; Level A retained. Corrections: Appendix B. Record: `records/az/AZ_v0_8_RELEASE_RECORD.md`.

### v0.7 — November 2026
Corrections-only edition. Owner pins, identifiers and imported statements synchronized with the adopted owner editions (Dyadic v6.4.23, TDR-G v2.12.14, Genesis v2.10, Programme v1.4, OPEN-M v0.7.1); the withdrawn OPEN-M "legal ×2" reading removed; the Thread C evidence files recorded as not available in the repository. No grade of an AZ-owned result changed. Full entry: Appendix A of `az-v0.7`; record: `records/az/AZ_v0_7_RELEASE_RECORD.md`.

### v0.6 — June 2026
Ledger-state update. AZ-1 closed (AZ-1A, AZ-1B, AZ-1C `[ENG PASS]`); AZ-OPEN-EDGE resolved (directed, both orientations); PROP-AZ-CORE-EQUIV and the antipodal-band low-order obstruction registered; the first Phase-2 diagnostic (the Core(G_T) `4|q` rule) registered and reclassified as static $\mathbb{Z}_N$ geometry; retraction block added (§4.3.4, Appendix B); SG-AZ-5 repurposed as a provenance guard; AZ-2 attempted, negative-clarifying; Level A retained. Full entry: Appendix A of `az-v0.7`.

### v0.5 — June 2026
Precision patch over v0.4. No Zeta-owned scientific content added. (Header/§1.3/§4.1 wording corrections; `[ENG-open-3]` added; zeta-pole SG-AZ-1/2 guard.)

### v0.4 — June 2026
Post-audit correction patch. Added Dyadic import-ref mechanisms, TDR-26 discriminator, SG-AZ-7, blocker sequencing, Genesis/OPEN-M precision notes.

### v0.3 — June 2026
Source-refresh and distributed-ownership patch. Pointer updates to Dyadic v6.4.8.1 / Discrete Genesis v2.12; Thread A/B refresh; §0.1 ownership map added.

### v0.2 — June 2026
Consistency pass after multi-AI audit of v0.1. Tag-alias normalization; "four"→"five" blocker fixes; High-Risk Claims Ledger added.

### v0.1 — June 2026
Initial release. Infrastructure-and-ledger document; three threads defined; five `[ENG-blocker]`, two `[ENG-open]`, four scientific `[OPEN]` items registered (all then blocked).

---

## Appendix B — Retired and Rejected Claims

### Rejected framings at v0.1
`[FAIL]` "Transfer-Zeta / TDR-G Ensemble" as complete scope description.  
`[FAIL]` $\mathbb{Z}_N$ arithmetic as an internal Thread B topic (violates SG-PROG-1/4; demoted to bridge-candidate).  
`[FAIL]` Prime-horizon transparency as a live conjecture (Dyadic `[FAIL]`, exact $p=7$ counterexample).  
`[FAIL]` Any RH-related claim (SG-AZ-1).

### Retractions registered at v0.6 (Thread C)
`[RETRACTED]` G_cumulative as the lead spectral signal — degree-only Null0 signal that did not survive the reciprocal-pair/topology-matched Null1 control (ratio ~1.00). The spectral-radius bug primarily affected the Core(G_T) "generic" claim, not this retraction.  
`[RETRACTED]` "Core(G_T)/G_T spectrally generic" (original README headline) — artifact of the spectral-radius bug (2.879 vs true 3.306).  
`[RETRACTED]` `4|q` rule as a TDR-G dynamical arithmetic law — reproduced by core-matched random-theta antipodal-band null; reclassified static $\mathbb{Z}_N$ geometry (TDRG-AZ-STATIC-ZN-4Q).  
`[RETRACTED]` exact `[ALG]` THM-AZ-ANTIPODAL-4Q v1 ("$\operatorname{Tr}(B^L)=0$ all odd $L$"; "exact 4th-root eigenphases") — explicit $N=120,k=8$ length-9 odd closed non-backtracking walk, $\operatorname{Tr}(B^9)=4212\ne0$. Salvageable low-order facts retained as `[ALG]` (§4.3.2).  
`[RETRACTED]` even-non-$4\mid q$ suppression ($q\in\{2,6,10\}$) as a TDR-G dynamical residue — not stable across $N$ under the core-matched theta null (present $N=120$, gone $N=180$, reversed $N=240$).  
`[RETRACTED]` predicted weakening of the `4|q` rule with larger $k/N$ — falsified ($R_4$ rises 0.75→0.97 with $k$).

### Corrections registered at v0.7
`[COR]` §6 "To OPEN M" (as printed in v0.6): "the legal correction is $\times2$, not $\times4$; applying $\times4$ is a certified dimensional type error under AUDIT-1-DIMENSIONAL in the OPEN-M ledger." Withdrawn as a current statement. Reason: OPEN-M v0.7.1 R16 (`UVM-RESULT-AUDIT1`) withdrew the "legal $2\times$" verdict as a physical conclusion and records that no certified numerical deficit factor exists. Replacement: §6 "To OPEN M". The sentence reported an owner reading; it was never an AZ result, and no AZ grade depended on it.

### Corrections registered at v0.8
`[COR]` §4.3.2 / §5 / §0.1, tag of PROP-AZ-CORE-EQUIV (as printed through v0.7): `[THM-ALG]`. Reason: the bare spelling is not a Methodology v1.4 tag, and the printed basis mixed a proof sketch with a finite enumeration whose files are not in the repository. Replacement: `[THM]` on the written proof now in §4.3.2 (PI decision of 12 November 2026); the enumeration is recorded as source-reported corroboration, and a separate finite check is registered (`AZ-ART-CORE-EQUIV-CHECK`). The statement and its scope are unchanged; the reading of "closed non-backtracking walk" on which it depends is now explicit.  
`[COR]` §4.3.2 / §4.3.3 / §5, tag of the link from the low-order obstruction to the `4|q` angular rule (as printed through v0.7): `[HEUR/NUM strong]`. Reason: a mixed tag (Methodology v1.4 §8.4). Replacement: `[HEUR]` for the link, with the numerical observations named as the `[NUM diagnostic]` chains of §4.3.3. No claim is strengthened; the falsified $k/N$ prediction stays recorded. The retraction block of §4.3.4 keeps its registered spelling.  
`[COR]` §3 SG-AZ-7 worked example and §4.3.5 (as printed through v0.7): the `4|q` rule "is proven static $\mathbb{Z}_N$ substrate geometry that would appear for *any* antipodal-band graph on *any* $\mathbb{Z}_N$", and is "substrate geometry that any antipodal-band $\mathbb{Z}_N$ graph would exhibit". Reason: the universal statement follows neither from the low-order obstruction of §4.3.2 nor from Chain 2 of §4.3.3, which is a `[NUM diagnostic]` at $N\in\{120,180,240\}$ with one null family; taken literally it is false (the full antipodal graph at $k=0$ is a perfect matching, its 2-core is empty and it carries no angular signal). Found in the change-focused review of this edition. Replacement: the rule is reproduced without TDR-G dynamics in the tested null protocol and is therefore not specific to the dynamics; nothing is asserted for every antipodal-band graph or every $N$. The `[NUM diagnostic]` result, the reclassification within its stated scope and the `[bridge-disqualified]` verdict are unchanged.  
`[COR]` §9, availability (as printed in v0.7): "none of these files, including the hash registry `AZ-ART-AZV5-REGISTRY`, is in the repository as of this edition". Reason: a partial recovery was deposited and hash-checked on 11 November 2026. Replacement: the per-entry availability of §9. Three findings of that intake are registered with it: the received registry is the AZ-1A/AZ-1B state of ten files and does not cover `phase2_harness`, which the entry `AZ-ART-AZV5-REGISTRY` listed; the deposited conventions file does not contain CONV-AZ-ANGLE-ZERO; and the deposited files define `G_birth(w)` in two different ways.  
`[COR]` §4.3.1, scope of the AZ-1B certification as it can be checked: the deposited certification suite reads no TDR-G export, so the "real TDR-G defect-graph exports" part of AZ-1B is source-reported (§9). The `[ENG PASS]` record is kept with that limit.  
`[COR]` Local Tag Aliases: `[ENG-planned]` and `[ENG-historical]` removed, `[import-ref]`, `[ENG-blocker]` and `[ENG-open]` declared as labels and not as aliases of `[ENG]` or `[DEF]`; `[bridge-disqualified]` and `[RESULT diagnostic]` paired with `[from: NUM]` (Methodology v1.4 §3.4, §8.4). No claim changes status by this.

---

*END OF DOCUMENT — RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.8 — DRAFT, stage-2 candidate; adoption pending; `az-v0.7` governs until adoption and tag.*
