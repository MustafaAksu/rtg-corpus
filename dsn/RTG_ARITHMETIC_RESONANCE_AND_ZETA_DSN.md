# RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.6

**Title:** RTG Arithmetic Resonance and Zeta Study — Infrastructure and Diagnostic Ledger  
**Date:** June 2026  
**Authors:** Mustafa (PI) · Claude · ChatGPT · Gemini · Grok  
**DSN Methodology:** DSN_METHODOLOGY_v1.2  
**Document class:** DSN-compatible infrastructure ledger / not a scientific result ledger  
**Programme tier:** Tier 5 — Arithmetic-diagnostic infrastructure; serves both continuous and discrete branches without belonging to either  
**Maturity:** Level A — RETAINED. Defined scope, internal consistency established, exploration begun. Thread C engineering is now certified; the one Phase-2 scientific result is a negative-clarifying diagnostic, not a Level-B-promoting bridge result.  
**Supersedes:** `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.5`  
**Companion documents:** `RTG_PROGRAMME_OVERVIEW_v1.1` · `RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1` · `RTG_DISCRETE_GENESIS_DSN_v2.12` · `RTG_GENESIS_GEOMETRY_DSN_v2.8.4` · `DSN_METHODOLOGY_v1.2`  

**Status summary:** This document remains an infrastructure ledger, not an active scientific study, and Maturity remains **Level A**. v0.6 is a **ledger-state update** over v0.5: it records that the five Thread C `[ENG-blocker]` items and the `[ENG-open]` items are now closed (AZ-1A/AZ-1B/AZ-1C `[ENG PASS]`); it registers the AZ-OPEN-EDGE architectural decision as RESOLVED (directed, both orientations); it registers one `[THM-ALG]` (PROP-AZ-CORE-EQUIV) and one `[ALG]` low-order obstruction arising from the Thread C engineering work; and it registers the **first Phase-2 diagnostic result** — the Core(G_T) Hashimoto `4|q` angular rule — together with its reclassification as **static $\mathbb{Z}_N$ antipodal-band geometry, not a TDR-G dynamical signal**. Milestone AZ-2 is recorded as **attempted, negative-clarifying**: the most tempting angular observable was tested and **disqualified** as a bridge-candidate. **No Level B promotion. No OPEN-P1 / Dyadic bridge-candidate is promoted.** A visible correction/retraction block is added (§4.3.4 and Appendix B).

**Major update (v0.6 at a glance):**
- AZ-1A / AZ-1B / AZ-1C engineering blockers closed (`[ENG PASS]`, exit-code-gated).
- AZ-OPEN-EDGE resolved: directed, both orientations.
- Real TDR-G graph-zeta Phase-2 diagnostics executed (N = 120, 180, 240).
- `[THM-ALG]` PROP-AZ-CORE-EQUIV registered (closes 2-core vs DEF-AZ-CORE mismatch).
- `[ALG]` antipodal-band low-order obstruction registered.
- `4|q` angular rule reclassified as static $\mathbb{Z}_N$ antipodal geometry (`[NUM diagnostic]` / `[HEUR/NUM strong]`).
- No TDR-G-dynamical angular signal survives matched controls.
- SG-AZ-5 repurposed from a pre-science gate to a provenance guard.

---

## Local Tag Aliases

All tags follow `DSN_METHODOLOGY_v1.2`. The following aliases are defined for this document and expand to the canonical forms shown.

| Alias | Canonical expansion | Meaning |
|---|---|---|
| `[ENG-blocker]` | `[ENG]` `[scope: blocker]` | Engineering defect that blocks all downstream scientific results in this thread |
| `[ENG-open]` | `[ENG]` `[scope: open engineering decision]` | Engineering question with no established answer; must be resolved by architectural decision before scientific work |
| `[ENG-planned]` | `[ENG]` `[scope: planned artifact]` | Artifact planned but not yet defined or registered |
| `[ENG-historical]` | `[ENG]` `[scope: historical / unverified; not source of scientific result]` | Historical artifact containing known defects; runs from it are unverified |
| `[ENG PASS]` | `[ENG]` `[scope: certified; exit-code-gated]` | Engineering item resolved and certified by an exit-code-gated check, with named artifact + hash |
| `[import-ref]` | `[DEF]` `[scope: reference-only import]` | Result owned by another DSN; cited here by reference only, ownership not transferred |
| `[bridge-candidate]` | `[HYP]` `[bridge-required]` | Item that could become an OPEN-P1 observable if the bridge study opens; not an active import |
| `[bridge-disqualified]` | `[RESULT]` `[scope: bridge-candidate ruled out]` | Item that was tested as a bridge-candidate and ruled out; recorded so it is not re-proposed |
| `[AZ-OPEN]` | `[OPEN]` `[scope: arithmetic-zeta infrastructure]` | OPEN problem internal to this arithmetic-resonance study |

---

## §0. What This Document Is

This document is not a standard scientific DSN. It is an **infrastructure and ledger document** whose function is:

1. to record the historical origin of the arithmetic-resonance thread within RTG;
2. to collect, without migrating ownership, the arithmetic-resonance results already certified in the Dyadic DSN (OPEN 9);
3. to define the TDR-G $\mathbb{Z}_N$ arithmetic structure as a bridge-candidate observable family under OPEN-P1, not as an active cross-branch import;
4. to record the (now certified) state of the graph/transfer-zeta diagnostic infrastructure and the diagnostics it has produced, under strict provenance and scope guards;
5. to state a precise success criterion that would justify opening this study as a full active Level B scientific DSN — and to record that the first Phase-2 attempt did **not** meet it.

**This document does not contain new derivations of cross-branch physics.** The two new internal results registered in v0.6 (PROP-AZ-CORE-EQUIV and the antipodal-band low-order obstruction) are graph-theoretic facts about the Thread C diagnostic objects themselves; they are Thread-C-owned engineering/math results, not cross-branch claims and not Dyadic/TDR-G-owned results. All scientific results cited from other DSNs remain owned by their source DSN.

### §0.1 v0.6 Distributed-Ownership Map

`[DEF]` **Hub status.** `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN` is a hub ledger. It may summarize and cross-index arithmetic/zeta-relevant material, and it owns its own Thread C diagnostic infrastructure and the graph-theoretic facts about that infrastructure, but it does not migrate proof ownership out of the source DSNs for any Dyadic or TDR-G physics result.

| Content family | Source of truth | Status in this document |
|---|---|---|
| Continuous $p$-resonance arithmetic, OPEN 9, low-degree vanishing, subgroup/missing-slot formalism | `RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1` | `[import-ref]`; ownership remains Dyadic |
| TDR-G $\mathbb{Z}_N$ state space, reachability, superselection, cyclic memory, advance-spectrum conservation, BIND3 arithmetic/parity diagnostics | `RTG_DISCRETE_GENESIS_DSN_v2.12` | branch-local context / `[bridge-candidate]`; no cross-branch import |
| Graph/transfer-zeta diagnostic engine, conventions, manifests, null models, certification suite | this DSN, Thread C | internal and **now `[ENG PASS]`** (was `[ENG-blocker]` through v0.5) |
| Graph-theoretic facts about the diagnostic objects (core equivalence; antipodal-band low-order cycle structure) | this DSN, Thread C | Thread-C-owned `[THM-ALG]` / `[ALG]`; not cross-branch |
| Phase-2 diagnostics computed on TDR-G defect-graph exports | this DSN, Thread C | `[NUM diagnostic]`, branch-local; reclassified static-geometry; **not** a bridge-candidate |
| Discrete-continuous comparison between Dyadic $p$-horizons and TDR-G $\mathbb{Z}_N$ horizons | future OPEN-P1 bridge document | `[bridge-candidate]` only |
| Programme placement and dependency graph | `RTG_PROGRAMME_OVERVIEW` | patch requested; this DSN cannot self-register at Tier 0 |
| Genesis cascade criterion and OPEN-M amplitude cascade | `RTG_GENESIS_GEOMETRY_DSN_v2.8.4` / `RTG_OPEN_M_DSN_v0.6` | companion/bridge context only; arithmetic-horizon or graph-zeta observables cannot substitute for UV inputs |

`[SG-AZ-0.4]` **Refresh is not promotion.** Updating source versions, importing fresher summaries, or incorporating post-audit import-ref corrections does not promote any imported claim to Zeta-owned `[ALG]`, `[THM]`, `[RESULT]`, or cross-branch evidence. All imported proof tags are inherited from the owner DSN and remain source-scoped. **v0.6 note:** the two internal `[THM-ALG]`/`[ALG]` items registered this version are Thread-C-owned graph-theoretic facts about this study's own diagnostic objects; they are not imported results and do not transfer to or from any other DSN.

## §1. Study Goal and Historical Origin

### §1.1 Primary Goal

`[DEF]` **Primary goal.** The goal of `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN` is to determine whether arithmetic horizon structure — including period length, divisibility, prime/composite obstruction, cyclic memory, and zeta/transfer spectra — plays a genuine structural role in RTG resonance dynamics, discrete relational memory, or future discrete-continuous bridge observables.

`[DEF]` **Immediate purpose.** The study has three immediate tasks:

1. Collect and organize the continuous arithmetic-resonance results already owned by Dyadic OPEN 9, without migrating ownership away from the Dyadic DSN.
2. Define TDR-G $\mathbb{Z}_N$ arithmetic structure as a bridge-candidate observable family under OPEN-P1, not as an active cross-branch import.
3. Stabilize the graph/transfer-zeta diagnostic infrastructure and run diagnostics under strict provenance and scope guards. **(v0.6: this is now done — infrastructure certified, first diagnostic executed and interpreted.)**

`[OPEN]` **Central question.** Does arithmetic horizon structure merely organize diagnostics, or does it select physically meaningful resonance, memory, or bridge observables in RTG?

`[OPEN]` **Success criterion.** This study becomes scientifically active beyond infrastructure — and would be promoted to a full Level B DSN — only if at least one arithmetic/zeta observable is shown to be reproducible, branch-scoped, and useful for distinguishing resonance classes, memory-length regimes, TDR-G policy ensembles, or candidate OPEN-P1 bridge behavior **in a way that reflects the dynamics rather than the fixed substrate geometry.** **v0.6 status: NOT met.** The first observable tested (the Core(G_T) `4|q` angular rule) is reproducible and branch-scoped but is static $\mathbb{Z}_N$ substrate geometry, so it does not distinguish dynamical classes and is disqualified as a bridge observable (§4.3.4).

`[FAIL]` **Forbidden interpretation.** This study is not a proof, disproof, reformulation, or physical derivation of the Riemann Hypothesis. The RH appears in this document only as historical motivation; see §1.2.

### §1.2 Historical Origin

`[HEUR]` **Historical motivation.** This study originated from discussions connecting the Riemann Hypothesis, prime numbers, and arithmetic order to RTG resonance and memory. In RTG, this motivation is retained only in scoped form: prime and composite numbers are relevant insofar as they enter explicit mechanisms such as resonance closure, finite memory length, divisor obstruction, cyclic return, transfer spectra, or graph-zeta diagnostics. No claim is made about the Riemann Hypothesis, prime distribution, or classical zeta zeros.

The concrete arithmetic observations that make this motivation non-trivial — i.e., that elevate it above numerology — are owned by the Dyadic DSN and cited here by reference:

- `[import-ref]` **$p=5$ lattice cancellation is unique.** $G_{\rm lattice}(5)=0$ with both sides nonzero and equal: a non-trivial degree-4 lattice bridge cancellation with no analogue at other tested $p$. `[ALG]` `[RID: DYAD-ALG-GLATTICE5]` `[source: RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1 §6.11]`
- `[import-ref]` **$p=7$ prime-horizon transparency fails.** $G_{06}(7) \neq 0$: the prime-horizon first-lattice transparency conjecture is `[FAIL]`. This means primes do not transparently propagate in the way the initial conjecture suggested. `[ALG/FAIL]` `[RID: DYAD-OPEN-P-RESONANCE, sub-item]`
- `[import-ref]` **$p=12$ cascade boundary is near-zero but not zero.** Exact value $-13 + 15\sqrt{3}/2 \neq 0$, $|-13+15\sqrt{3}/2| \approx 0.0096$: a cascade boundary that is numerically small but algebraically nonzero. The structure of this near-cancellation remains open. `[ALG]` `[RID: DYAD-OPEN-P-RESONANCE, sub-item]`
- `[import-ref]` **Low-degree pure anti-holomorphic raw vanishing is now certified.** $F_{\rm raw}^p(0,b)=0$ for $b\in\{2,3,4\}$ in the exact ranges $p\ge b+2$, proved by automatic $\beta$-mode path enumeration with no source $\beta$-set containing the secular mode. `[ALG]` `[RID: DYAD-ALG-VANISH-B2; DYAD-ALG-VANISH-B3; DYAD-ALG-VANISH-B4]`
  `[COR v0.4]` Boundary precision: the clean statement is $p\ge b+2$, not "$p\ne b+1$". Nonzero boundary cases include the direct-resonant $p=b+1$ cases and additional small-$p$ cross-contribution cases: $p=3,4$ for $b=3$ and $p=4,5$ for $b=4$.
- `[import-ref]` **The dyadic channel boundary is closed at $b=4$.** Universal pure anti-holomorphic raw vanishing holds iff $b\le4$ for the dyadic map and fails at $b=5$ for every $p\ge6$; all-$b\ge5$ persistence and general-coefficient versions remain `[OPEN]`. `[ALG]` `[source: RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1 §6.11]`

These observations together motivate the study: the arithmetic horizon is not featureless, but the certified features do not follow naive prime-based intuition. The operative arithmetic mechanism appears to be **divisor structure, subgroup charge, orbit sums, cyclic-horizon closure, and secular-mode exclusion/presence**, not primality by itself.

`[HEUR]` **Scope statement.** This study investigates whether arithmetic structure — especially period length, divisibility, prime horizons, cyclic memory, advance-spectrum conservation, and transfer/zeta spectra — acts as a selection or obstruction mechanism in RTG. It collects three related threads: continuous $p$-resonance in the Dyadic branch, finite cyclic memory in TDR-G, and graph/transfer-zeta diagnostics of emergent TDR-G ensembles. It does not assert any result about the Riemann Hypothesis or classical prime distribution.

### §1.3 Milestones

`[DEF]` **Milestone AZ-0 (closed by v0.2; refreshed by v0.3–v0.5; carried unchanged in v0.6).** Create a clean ledger of what already exists: Dyadic OPEN 9 arithmetic facts, TDR-G candidate observables, and graph-zeta engineering blockers. v0.3 refreshed AZ-0 against the current source DSNs (`Dyadic v6.4.8.1`, `Discrete Genesis v2.12`); v0.4–v0.5 added precision corrections and mechanism-level reference entries without adding new derivations or Zeta-owned scientific claims.

`[DEF]` **Milestone AZ-1 (CLOSED — v0.6).** Resolve all five `[ENG-blocker]` items in Thread C and produce at least one reproducible graph-zeta diagnostic run on a synthetic or TDR-G-generated test graph. **Status: CLOSED.** All five `[ENG-blocker]` and the three `[ENG-open]` items are resolved; the engine is certified by an exit-code-gated suite (AZ-1A synthetic engine, AZ-1B ingestion/export/provenance, AZ-1C manifest/null/statistic hardening — all `[ENG PASS]`); conventions are frozen (`AZ-ART-CONVENTIONS-FROZEN`); and reproducible runs on both synthetic and real TDR-G graphs exist. See §4.3.1.

`[DEF]` **Milestone AZ-2 (ATTEMPTED — negative-clarifying — v0.6).** Demonstrate that at least one arithmetic/zeta observable distinguishes two structurally distinct TDR-G ensemble classes. **Status: attempted; the first observable was disqualified.** The Core(G_T) `4|q` Hashimoto angular rule is reproducible across $N\in\{120,180,240\}$ and 5 seeds, but a core-matched random-theta antipodal-band null reproduces it with no TDR-G dynamics — so it is static $\mathbb{Z}_N$ substrate geometry, not a dynamical class discriminator. **This does not meet the Level B gate** and, importantly, it *removes* the most tempting angular observable from the bridge-candidate pool. See §4.3.3–§4.3.4. AZ-2 remains open for a genuinely dynamical observable.

---

## §2. Active Frontier / OPEN Registry

### §2.1 Priority ordering

This is an infrastructure document. The OPEN Registry covers scope and infrastructure questions only.

**Resolved since v0.5 (no longer blocking):**

1. **AZ-OPEN-ENG** — RESOLVED. All five `[ENG-blocker]` and three `[ENG-open]` items closed; engine certified (§4.3.1). The guard that depended on this (SG-AZ-5) is repurposed as a provenance guard (§3).
2. **AZ-OPEN-EDGE** — RESOLVED. Directed, both orientations is canonical. Rationale and consequence registered (§4.3.1.1).

**Infrastructure (still open; required before any Level B promotion):**

3. **AZ-OPEN-SCOPE-ZETA** — Determine whether a graph/transfer-zeta observable of the TDR-G defect graph is a branch-discriminating *dynamical* observable or merely an aggregate/substrate diagnostic. **v0.6 partial answer:** the first angular observable (`4|q` rule) is a substrate-geometry diagnostic, not dynamical (§4.3.4). The question stays open for other observables.
4. **AZ-OPEN-SCOPE-ARITH** — Determine whether the $\mathbb{Z}_N$ cyclic memory length and divisibility structure of TDR-G are bridge-candidate observables for OPEN-P1, or purely internal to the TDR-G DSN.
5. **AZ-OPEN-PROMO** — State the exact conditions under which this document would be promoted to a full Level B active scientific DSN, including required artifact and transcript provenance.

---

**AZ-OPEN-ENG** [RID: AZ-OPEN-ENG-BLOCKERS] — **RESOLVED (v0.6)**

Status: RESOLVED | Was: ACTIVE / blocks all Thread C scientific results  
Resolution: All five `[ENG-blocker]` items fixed and all three `[ENG-open]` items closed; engine certified by exit-code-gated suite. See §4.3.1 for the per-item closure record and §9 for artifacts.

**AZ-OPEN-EDGE** [RID: AZ-OPEN-EDGE-EXPORT] — **RESOLVED (v0.6)**

Status: RESOLVED | Decision: **DIRECTED, BOTH ORIENTATIONS.** Each symmetric defect pair $\{a,b\}$ is exported as the two directed edges $(a,b)$ and $(b,a)$. One-edge-per-pair makes `extract_recurrent_core` silently empty and the Hashimoto operator ill-defined; both orientations give a well-defined $2|E|\times2|E|$ Hashimoto operator. Registered in §4.3.1.1 and in the frozen conventions artifact. A consequence of this decision is PROP-AZ-CORE-EQUIV (§4.3.2): under both-orientations export the re-directed undirected 2-core equals the frozen non-backtracking recurrent core DEF-AZ-CORE.

---

## §3. Scope Guards

Programme-level guards from `RTG_PROGRAMME_OVERVIEW_v1.1` apply in full. Sub-study guards specific to this document follow.

**[SG-PROG-1]** No result may flow between the discrete and continuous branches without a named bridge theorem. This is the primary firewall governing Thread B (§4) of this study. `[source: RTG_PROGRAMME_OVERVIEW_v1.1]`

**[SG-PROG-2]** No continuous-branch coefficient may be described as physically primitive until OPEN-P0 is resolved. All Thread A results (§4.1) carry this programme-level condition. `[source: RTG_PROGRAMME_OVERVIEW_v1.1]`

**[SG-PROG-4]** No result from Tier 4 or Tier 5 may be used to strengthen a result in Tier 3 without an explicit bridge theorem. This study is Tier 5 and must not inject Thread B/C items into Thread A or vice versa. `[source: RTG_PROGRAMME_OVERVIEW_v1.1]`

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

**[SG-AZ-5] — Provenance guard for imported graph-zeta results (REVISED v0.6).**  
*(Through v0.5 this guard read "no graph-zeta scientific result before engineering blockers are resolved." The blockers are now resolved (§4.3.1), so the guard is repurposed — its job is no longer to gate science behind engineering, but to enforce provenance on any graph-zeta result entering or leaving this ledger.)*  
No graph-zeta result may be registered here, or imported elsewhere from here, unless it declares: (i) the graph object (G_T / Core(G_T) / G_birth(w) / G_cumulative), (ii) the spectrum mode (full-spectrum / leading-K / trace-moment), (iii) the null model used, (iv) the eps-angle convention for zero-eigenvalue handling, (v) the script version, (vi) the artifact paths, and (vii) a hash/provenance record.  
Violation: Reporting a Hashimoto eigenvalue, R_q value, spectral radius, or zeta pole without its graph object, spectrum mode, null model, eps-angle, script version, and hash provenance.

**[SG-AZ-6] — Ownership stays in source DSNs.**  
This document does not migrate ownership of any physics result from the Dyadic DSN or TDR-G DSN. Dyadic OPEN 9 sub-items remain owned by `RTG_DYADIC_OSCILLATOR_DSN`. TDR-G OPEN items remain owned by `RTG_DISCRETE_GENESIS_DSN`. This document may cite them as `[import-ref]` but may not retag or restate them as its own results. *(v0.6 clarification: PROP-AZ-CORE-EQUIV and the antipodal-band low-order obstruction are graph-theoretic facts about this study's own Thread C diagnostic objects, owned by this DSN; they are not Dyadic/TDR-G physics results and do not fall under this guard.)*  
Violation: Registering a Dyadic OPEN 9 result as an `[ALG]` or `[OPEN]` within this document's own ledger.

**[SG-AZ-7] — Vocabulary similarity is not a bridge theorem.**  
The presence of shared vocabulary between Thread A (cyclic charge $\chi_p$, divisor structure, subgroup orbits, $p$-resonance) and Thread B/C ($\mathbb{Z}_N$ cyclic memory, orbit-lattice spacings, $\gcd$-divisibility, advance spectrum, and now the `4|q` divisor-graded angular rule) does not constitute a bridge theorem. Any claim that Dyadic OPEN 9 arithmetic structures and TDR-G $\mathbb{Z}_N$ arithmetic are related requires a named bridge theorem registered under OPEN-P1 with explicit derivation.  
Violation: Asserting or implying that Dyadic subgroup-charge $K^{\rm extra}_{p,q}$ and the TDR-G `4|q` angular rule (or $\gcd(d,N)$-divisibility) are dual, equivalent, or physically analogous without a named bridge theorem.  
**v0.6 worked example of the trap this guard exists to catch:** the Phase-2 `4|q` rule (§4.3.3) is a divisor-graded selection rule that *sounds* like the Dyadic cyclic-subgroup selection rules of Thread A. It must NOT be compared to Dyadic subgroup-charge structure as evidence of a bridge. It is proven static $\mathbb{Z}_N$ substrate geometry that would appear for *any* antipodal-band graph on *any* $\mathbb{Z}_N$ (§4.3.2, §4.3.4); a "resemblance" to Dyadic cyclic selection is therefore vacuous. This is the canonical SG-AZ-7 violation to avoid.

---

## §4. Three Threads

This study organizes its material into three threads. They are structurally separated by scope guards SG-AZ-3 and SG-PROG-1 and may not be merged without a named bridge theorem.

---

### §4.1 Thread A — Continuous $p$-Resonance (Dyadic OPEN 9 import ledger)

**Ownership:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1`, §2 and §6.11.  
**Status here:** Reference only. All results cited as `[import-ref]`. This document does not own, retag, or add sub-items to Dyadic OPEN 9. v0.6 carries the Thread A ledger forward from v0.5 unchanged in content; no Thread A item is altered by the Thread C work.

#### §4.1.1 Certified results (imported by reference)

`[import-ref]` `[THM]` **Raw cubic theorem.** The raw cubic coefficient of the $p$-step map is exact. `[RID: DYAD-THM-RAW-CUBIC]`

`[import-ref]` `[ALG]` **Finite one-step ledger, $p=5,6,7$.** Exact coefficients:
- $p=6$: $c_{05}^{(1,6)} = 43/17280 - i\,227\sqrt{3}/155520$ in the one-step engine/DSN bridge convention; distinct from the raw six-step Lie-gauge coefficient $c_{05}^{({\rm raw},6\text{-step})}=-61/2160-i\,43\sqrt{3}/6480$
- $p=5$: $\nu_5^{(5)}$ exact over $\mathbb{Q}(\sqrt5, \sqrt{10+2\sqrt5})$
- $p=7$: $c_{06}^{(7)}$ exact over $\mathbb{Q}(\zeta_7)$

`[RID: DYAD-ALG-P567-LEDGER]`

`[import-ref]` `[ALG]` **$p=5$ lattice cancellation.** $G_{\rm lattice}(5)=0$; both $F_1^5(0,4)$ and $F_{\rm raw}^5(0,4)$ are nonzero and equal. This remains the unique non-trivial degree-4 lattice bridge cancellation in the certified finite ledger. `[RID: DYAD-ALG-GLATTICE5]`

`[import-ref]` `[ALG]` **$G_{04}(10)=0$ reinterpretation.** Not divisor inheritance: $(0,4)$ is dynamically active in $J^{extra,raw}_{10,5,D}$. Sub-horizon inheritance conjecture `[RETRACTED]` `[scope: reframed]`. `[source: DYAD-OPEN-P-RESONANCE]`

`[import-ref]` `[ALG]` **Cascade boundary $p=12$, $q=4$, $(0,3)$.** Exact value $-13 + 15\sqrt{3}/2 \neq 0$; $|-13+15\sqrt{3}/2| \approx 0.0096$. `[source: DYAD-OPEN-P-RESONANCE]`

`[import-ref]` `[FAIL]` **Universal $q=4$, $(0,3)$ cancellation.** Not universal; $p=12$ is a counterexample. `[source: DYAD-OPEN-P-RESONANCE]`

`[import-ref]` `[FAIL]` **Prime-horizon first-lattice transparency.** $G_{06}(7) \neq 0$: exact $p=7$ counterexample. Primes do not transparently propagate at the first lattice horizon. `[source: DYAD-OPEN-P-RESONANCE]`

`[import-ref]` `[ALG]` **Degree-2 raw-vanishing.** $F_{\rm raw}^p(0,2)=0$ for all $p\ge4$; resonant exception $p=3$ nonzero. `[RID: DYAD-ALG-VANISH-B2]`

`[import-ref]` `[ALG]` **Degree-3 raw-vanishing.** $F_{\rm raw}^p(0,3)=0$ for all $p\ge5$, by automatic $\beta$-mode path enumeration; boundary cases $p=3$ and $p=4$ are nonzero, with $p=4$ arising from cross-path contribution rather than the direct-resonant $p=b+1$ case alone. `[RID: DYAD-ALG-VANISH-B3]`

`[import-ref]` `[ALG]` **Degree-4 raw-vanishing.** $F_{\rm raw}^p(0,4)=0$ for all $p\ge6$, by automatic $\beta$-mode path enumeration; boundary cases $p=4$ and $p=5$ are nonzero, with $p=4$ a small-$p$ cross-contribution case and $p=5$ the direct-resonant/lattice-anomaly boundary. `[RID: DYAD-ALG-VANISH-B4]`

`[import-ref]` `[ALG]` **Channel classification boundary at $b=4$ (dyadic map).** Universal pure anti-holomorphic raw vanishing for $p\ge b+2$ holds for $b\in\{2,3,4\}$ and fails at $b=5$ for every $p\ge6$. The all-$p$ $b=5$ failure is proved by secular-mode extraction plus cyclotomic non-division, not merely finite scan. The all-$b\ge5$ persistence and general-coefficient versions remain `[OPEN]`. `[source: RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1 §6.11]`

`[import-ref]` `[ALG, exact]` **Direct-accumulation weight vanishing.** For channel $(0,b)$, the direct accumulation weight is $\lambda^{-(b+1)k}$, and the $p$-fold orbit sum vanishes when $p\nmid(b+1)$. This is an arithmetic kernel of the $b\le4$ vanishing boundary. Scope precision: the all-$p$ $b=5$ failure is not a consequence of the direct-weight argument alone; it uses a separate secular-coefficient nonvanishing and cyclotomic non-division proof for the dyadic map (`DYAD-OPEN-B5-ALLP`, with `DYAD-ART-B5-SECULAR` as the secular-coefficient artifact). `[RID: DYAD-ALG-DIRECT-WEIGHT]` `[source: RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1 §6.11]`

`[import-ref]` `[ALG, exact]` **Cyclotomic cross-term identity.** $\tfrac12[(\sum_j\lambda^{2j})^2-\sum_j\lambda^{4j}]=0$ for all $p\ge5$. This exact cyclotomic sum cancellation is used in the degree-4 vanishing proof to eliminate the only possible cross-path contribution in the clean range. `[RID: DYAD-ALG-CROSS-IDENTITY]` `[source: RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1 §6.11]`

`[import-ref]` `[ALG]` `[conv: raw Birkhoff-strobe]` **Degree-2 $q=3$ anti-holomorphic cancellation theorem.** For all $p>3$ with $3\mid p$, $\operatorname{Coeff}_{(0,2)}[\tau_{\le D}(L_p^{-p/3} f_p^{p/3}-\mathrm{Id})]=0$ for all $D\ge2$. Two-component structure: (a) reachability — the $(0,2)$ slot is dynamically active in the one-step map for $p>3$, so the zero is not vacuous; (b) cancellation — the $s$-step strobe kills the reachable slot by a geometric phase sum of a primitive $s$-th root of unity at the direct-averaging layer, anchored by the eigenframe linear-part lemma. This is a closed general sub-horizon cancellation theorem and a clear source-scoped example of composite-horizon cyclic-subgroup structure producing a selection rule. `[RID: DYAD-ALG-Q3-CANCEL]` `[source: RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1 §2 OPEN 9]`

`[import-ref]` `[ALG]` **Subgroup-charge projector formalism.** Current OPEN 9 canonical objects include $\mathcal{Q}(p)$, $s=p/q$, $\chi_p(a,b)=a-b-1\pmod p$, $K^{\rm extra}_{p,q}$, $\Pi^{\rm extra}_{p,q}$, $J^{extra,raw}_{p,q,D}$, $\mathcal{B}^{extra}_{p,q,D}$, $Z^{\rm miss}_{p,q,D}$, $C^{\rm mult}_{\rm sub}$, $C^{\rm uniq}_{\rm sub}$, and $\Delta_{\rm overlap}$. The closed cardinality lemma $|K^{\rm extra}_{p,q}|=s-1$ makes the formalism computable without raw case enumeration in the registered sub-horizon setting. `[source: DYAD-OPEN-P-RESONANCE]`

`[import-ref]` `[ALG, exact]` **$p=6$ / $K_4$ face-flux identity.** $\lambda=e^{i\pi/3}=e^{iF_f/2}$ with $F_f=2\pi/3$. The identity is exact in Dyadic, but any transfer to OPEN-M source amplitude remains `[CAND/conditional]` and is not a Zeta result. `[RID: DYAD-ALG-P6-FACEFLUX]`

#### §4.1.2 Active open frontier (imported by reference, owned by Dyadic DSN)

The following items are owned by `RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1` OPEN 9. They are listed here as programme context only. Progress on them is tracked in the Dyadic DSN, not here.

- Exact cubic cascade formula for $q=4,(0,3)$: why does $p=8$ cancel while $p=12$ survives at $-13+15\sqrt3/2$?
- Universal missing-slot rules $Z^{\rm miss}_{p,q,D}$ via reachable-basis projector formalism.
- Bridge-gap smooth baseline: exact form of $G_{32}/K_p$ and whether a smooth baseline exists beyond the nonconstant tested ratio.
- All-$b\ge5$ persistence extension beyond the certified all-$p$ $b=5$ failure; general-coefficient version of the boundary.
- Universal $\nu_5^{(p)}$ theorem, only after subgroup-strobe definitions and cancellation rules are stabilized.
- Near-cancellation structure of $-13+15\sqrt3/2\approx0.0096$ at the $p=12$, $q=4$, $(0,3)$ cascade boundary; algebraic nonzero is closed, structural explanation remains `[OPEN]`.

`[COR]` **v0.3 frontier correction (carried).** Low-degree anti-holomorphic vanishing for $b\in\{2,3,4\}$ is no longer a Zeta-listed open frontier. It is a Dyadic `[ALG]` import-ref item in §4.1.1.

#### §4.1.3 Arithmetic-resonance observation relevant to this study's goal

`[HEUR]` The $p$-resonance arithmetic horizon is not featureless, but it does not conform to naive prime-based intuition:

- $p=5$ (prime): unique non-trivial lattice cancellation (unexpected).
- $p=7$ (prime): transparency fails (confounds simple prime-transparency conjecture).
- $p=12$ (composite): near-zero nonvanishing cascade boundary (unexpected near-cancellation).
- $p=6$ (composite): the programme's canonical resonance period, selected by order-6 Birkhoff/dyadic structure rather than primality.
- $b\le4$ vs. $b=5$ boundary: arithmetic enters through direct-accumulation orbit weights $\lambda^{-(b+1)k}$, cyclotomic cancellations, and secular-mode exclusion/presence in $\beta$-mode path enumeration, not through prime status alone.

`[HEUR]` The operative arithmetic mechanism appears to be **divisor structure, subgroup charge, direct orbit weights, cyclotomic sum cancellation, reachable-basis/missing-slot structure, cyclic-horizon closure, and secular-mode exclusion/presence** rather than primality per se. SG-AZ-2 applies.

### §4.2 Thread B — Discrete $\mathbb{Z}_N$ Arithmetic Structure (bridge-candidate only)

**Ownership:** `RTG_DISCRETE_GENESIS_DSN_v2.12`.  
**Status here:** Branch-local context and bridge-candidate observable family under OPEN-P1. SG-PROG-1, SG-PROG-4, SG-AZ-3, and SG-AZ-0.4 apply. No TDR-G result is imported as a cross-branch claim, and no TDR-G fact is used as evidence for a Dyadic claim. v0.6 carries Thread B forward unchanged.

`[bridge-candidate]` **$\mathbb{Z}_N$ finite-state substrate.** TDR-G is defined on $\mathbb{Z}_N$ with even $N$, variable node count, relational phases $\Delta_{ij}=(\theta_i-\theta_j)\bmod N$, and absolute phases gauge. The defect band is $\mathcal{D}_k=\{\Delta\in\mathbb{Z}_N: \operatorname{dist}_{\mathbb{Z}_N}(\Delta,N/2)\le k\}$. This gives Thread B a concrete arithmetic memory horizon $(N,k)$, but not yet a bridge to Dyadic $p$-resonance. `[source: RTG_DISCRETE_GENESIS_DSN_v2.12 §1]`

`[bridge-candidate]` **Reachability / superselection.** For $k=0$, two-node interaction occurs iff $\gcd(d,N)\mid(N/2-\Delta_0)$; unreachable pairs are superselection sectors. v2.12 adds the band-form extension LEM-REACH: $\mathcal{D}_k$ is reachable iff $\mathcal{D}_k\cap(\Delta_0+g\mathbb{Z}_N)\neq\varnothing$; superselection persists at $k>0$ in the two-node universe. `[THM/ALG in source]` `[scope: branch-local]`

`[bridge-candidate]` **Retrigger / binding threshold.** LEM-RETRIG gives an exact two-node period-2 retrigger criterion: $\varepsilon\in B_k\cap(B_k+d)$, possible iff $|d|_c\le2k$. This is arithmetic memory inside TDR-G only; it is not evidence for Dyadic resonance closure. `[ALG in source]` `[scope: two-node TDR-G]`

`[bridge-candidate]` **Advance-spectrum conservation.** LEM-SPECCONS states that in the three-node no-birth universe the multiset $\{|d_{AB}|_c,|d_{BC}|_c,|d_{CA}|_c\}$ is exactly conserved under swap/$P_3$/tie events. Equivalently, the multiset of orbit-lattice spacings $\{\gcd(d_{ij},N)\}$ is conserved. Star blow-up creates new nodes and new pairwise advances; generalization beyond the no-birth sector remains source-scoped/open. `[ALG]` `[scope: 3 nodes, no star blow-up]`

`[bridge-candidate]` **BIND3 arithmetic/parity diagnostics.** In the exact three-node $N=24,k=1$ BIND3 enumeration, the isolated period-2 bound dyad is not a persistent primitive: most bound-entry ICs become multi-pair recurrent scattering cycles with bond transfer; pure-bound survival is confined to even-advance parity sectors; conserved spectrum gates autonomous retrigger. BIND3-KNIFE is `[FAIL]`/`[REPLACED]`, and the odd-sector memory claim is `[COR]` as a composition artifact. `[ALG/NUM strong in source]` `[scope: N=24,k=1; no-birth/three-node]`

`[bridge-candidate]` **$k/N$ and N-scaling.** TDR-G v2.12 reports that $k/N$ controls entry into the growth regime and that the canonical clean branch (`bound_symmetric`) shows bulk-conditioned birth rate
$$B_{\rm bulk}/\text{step}\sim1.041\cdot N^{-0.869},\quad R^2=0.973$$
at fixed $k/N=1/15$, $T=5000$, over $N=120$–$1440$, excluding tail runs $M>500$. This strongly supports thermodynamic crystallization but remains `[HEUR strong]` rather than theorem-grade. `[NUM strong / HEUR strong in source]`

`[bridge-candidate]` **TDR-26 birth-anchored discriminator.** Discrete Genesis v2.12 records a birth-anchored dataset fact over $[\mathrm{fb},\mathrm{fb}+200)$, where $\mathrm{fb}$ is first-birth step: the rule $b/\text{step}\ge0.30\wedge ms_{\rm abs}\le0.25$ is satisfied by both known defective/crystallization-failure runs and by none of the 198 known bulk runs across $N=720$ and $N=722$ (combined TP=2, FP=0, FN=0, TN=198). Source tag split must be preserved: the dataset separation is `[NUM cross-cell, n=2]`, while the classifier/out-of-sample claim remains `[HEUR]` pending batch-scale validation. For this DSN it is a branch-local memory-window observable only, not a bridge theorem. `[source: RTG_DISCRETE_GENESIS_DSN_v2.12 TDR-26]`

`[bridge-candidate]` **TDR-24 frontier.** The immediate discrete frontier is the TDR-24 derivation chain: slot-volume identity, topological filtering, and geometric compression. It must close before discrete triadic dynamics can be studied. This DSN may track arithmetic/zeta observables that could assist TDR-24 or future OPEN-P1, but cannot promote them without source-DSN closure and bridge routing.

`[AZ-OPEN]` **AZ-OPEN-SCOPE-ARITH.** Are the $\mathbb{Z}_N$ arithmetic objects above — memory horizon $(N,k)$, divisibility, reachable cosets, orbit-lattice spacings, advance-spectrum conservation, parity sectors, TDR-26 birth-anchored memory window, and policy-dependent N-scaling — genuinely comparable to the Dyadic $p$-resonance arithmetic horizon, or are they structurally different objects that merely share vocabulary? Answering this question requires OPEN-P1 to be at minimum formally opened, a candidate bridge observable to be defined, and SG-AZ-7 to be satisfied. **v0.6 note:** the Phase-2 `4|q` angular result (§4.3.3) is NOT an answer to this question in the affirmative — it is proven to be substrate geometry (§4.3.2/§4.3.4), so it neither supplies nor supports a bridge.

**What Thread B does not contain:**

- No TDR-G result is imported as a cross-branch claim. TDR-G facts may be cited as branch-local context, clearly tagged with their source DSN, without constituting a cross-branch import.
- No claim is made that TDR-G $\mathbb{Z}_N$ structure is related to Dyadic OPEN 9 arithmetic structure.
- No cross-branch inference is made.

### §4.3 Thread C — Graph/Transfer-Zeta Diagnostics

**Ownership:** This thread is internal to this study.  
**Status (v0.6):** Engineering **CERTIFIED** (`[ENG PASS]`); was entirely engineering-blocked through v0.5. One Phase-2 diagnostic produced and interpreted; it is a **negative-clarifying** result (a bridge-candidate disqualified), not a Level-B-promoting result. SG-AZ-4, SG-AZ-5 (revised), and SG-AZ-7 apply.

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

`[THM-ALG]` **PROP-AZ-CORE-EQUIV — the export core equals DEF-AZ-CORE.**  
*Scope: finite simple undirected graph, exported with both orientations; no multiedges, no self-loops.*  
For a both-orientations export, the re-directed undirected 2-core equals the frozen non-backtracking recurrent core DEF-AZ-CORE (the set of directed edges lying on at least one non-backtracking closed walk). Proof: leaf-stripping/backtracking argument ($\Rightarrow$) plus a bridge/non-bridge construction ($\Leftarrow$) covering the bridge-between-lobes case; no strong-connectivity assumption is used (a bidirected cycle splits into clockwise/counterclockwise SCCs, so the correct statement is only that every directed 2-core edge lies in *some* cyclic SCC). Certified on 2,141,014 graphs (exhaustive to 7 vertices incl. barbell/lollipop/theta/figure-8; plus random) with zero counterexamples. `[RID: PROP-AZ-CORE-EQUIV]` `[artifact: AZ-ART-PROP-CORE-EQUIV]`  
Consequence: the uploaded export object labeled `Core(G_T)` (a 2-core) IS DEF-AZ-CORE; the earlier 2-core-vs-DEF-AZ-CORE labeling mismatch is closed.

`[ALG]` **Antipodal-band low-order obstruction.**  
*Scope: antipodal-band graph on $\mathbb{Z}_N$, edge iff displacement within $k$ of $N/2$ (mod $N$), narrow band $k<N/6$; both orientations.*  
(1) There is no closed non-backtracking walk of length 2 or 3 under $k<N/6$. (2) Length 4 is the first possible/constructible non-backtracking closure scale in the full antipodal-band geometry. (3) **Odd-closure obstruction threshold:** for odd $L$, closed non-backtracking walks are impossible when $Lk<N/2$; when $Lk\ge N/2$ the displacement obstruction is removed, but existence still depends on the discrete displacement set and the available vertices/edges (the threshold is a necessary obstruction bound, not a sufficiency theorem). Verified: at $N=120,k=8$, existence is confirmed by an explicit $L=9$ walk ($\operatorname{Tr}(B^9)\ne0$), and $\operatorname{Tr}(B^L)=0$ for odd $L\in\{1,3,5,7\}$. `[RID: AZ-ALG-ANTIPODAL-LOWORDER]` `[artifact: AZ-ART-ANTIPODAL-LOWORDER]`  
Note on scope: claims (1)–(3) are about the full antipodal-band graph on $\mathbb{Z}_N$; they are not asserted as existence statements for arbitrary induced/random core subgraphs.  
**Not promoted:** the full "$R_q$ elevated iff $4\mid q$" angular rule is NOT `[ALG]`. The exact spectral theorem claimed in an earlier draft (THM-AZ-ANTIPODAL-4Q v1: "$\operatorname{Tr}(B^L)=0$ for all odd $L$" and "dominant eigenphases exactly at 4th roots of unity") is `[RETRACTED]` (see §4.3.4). The connection from the low-order obstruction to the angular rule is `[HEUR/NUM strong]` only.

#### §4.3.3 Phase-2 diagnostic result — the `4|q` angular rule (static $\mathbb{Z}_N$ geometry)

`[NUM diagnostic]` `[RID: TDRG-AZ-STATIC-ZN-4Q]`

This result rests on two distinct evidence chains, with distinct scope and sample size; they must not be conflated.

**Chain 1 — Null0/Null1 statistical excess.** *Scope: $N=120$, $k=8$, `bound_symmetric`, Core(G_T), full-spectrum $R_q$, degree-exact Null0 and reciprocal-pair Null1, 1000 nulls, 5 seeds.* The Core(G_T) angular spectrum shows elevated $R_q$ on divisors $q$ with $4\mid q$ (e.g. $q\in\{4,8,12,20,24\}$ at $N=120$) and is silent on $q$ with an odd prime factor ($q\in\{3,5,15\}$, $R_q\approx0$). The generic even-$q$ elevation is an artifact of the bidirected export and collapses under Null1, but the $4\mid q$ signal persists above the reciprocal-pair baseline. In the registered Null1 runs the $4\mid q$ signal persists above the reciprocal-pair baseline; exact per-$q$ $z$-scores are artifact-scoped and must be read from the registered Null1 reports (`AZ-ART-PHASE2-N120-CORE`). `[artifact: AZ-ART-PHASE2-N120-CORE]`

**Chain 2 — static-geometry reclassification.** *Scope: $N\in\{120,180,240\}$, core-matched random-theta antipodal-band null; per-$q$ comparison (this is a per-$q$ comparison artifact, NOT a 1000-null × 5-seed empirical-$p$ report).* A core-matched random-theta antipodal-band null — random $\theta$ on $\mathbb{Z}_N$ with the SAME antipodal defect rule, then the SAME core extraction, with NO TDR-G dynamics — reproduces the qualitative $4\mid q$ rule, and the strong-signal set tracks the 2-adic divisor structure of $N$ ($q=16$ appears only at $N=240=2^4\cdot3\cdot5$). Therefore the angular `4|q` rule is **static $\mathbb{Z}_N$ antipodal-band geometry, not a TDR-G dynamical signal**; the dynamical interpretation is retracted. `[artifact: AZ-ART-THETA-CORE-MATCHED]`

The underlying mechanism is partly understood (the antipodal-band low-order obstruction §4.3.2: $L=2,3$ excluded, $L=4$ first constructible, so low-order cycles are 4-dominated). The full causal link to "$R_q$ elevated iff $4\mid q$" is `[HEUR/NUM strong]`, not exact: a predicted weakening of the rule with larger $k/N$ was tested and FALSIFIED ($R_4$ rises, not falls), so the mechanism is incompletely captured by low-order domination alone.

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

#### §4.3.5 AZ-2 status

`[RESULT diagnostic]` **AZ-2 attempted; negative-clarifying. No Level B promotion.**  
The first angular-spectrum candidate (the Core(G_T) `4|q` rule) was tested and **disqualified as a bridge-candidate**, because the effect is static $\mathbb{Z}_N$ substrate geometry rather than a dynamical class discriminator. This is the opposite of the AZ-2 Level-B gate condition: rather than an observable that distinguishes TDR-G dynamical ensembles, the most tempting observable was shown to be substrate geometry that any antipodal-band $\mathbb{Z}_N$ graph would exhibit. `[bridge-disqualified]` `[RID: TDRG-AZ-STATIC-ZN-4Q]`

This is a genuinely useful negative: it removes the angular Hashimoto spectrum from the OPEN-P1 bridge-candidate pool and sharpens the SG-AZ-7 guard with a concrete worked example (§3). A genuine bridge-candidate must be a TDR-G-**dynamical** observable; the static angular spectrum is geometry-saturated and is not one. AZ-2 remains OPEN for such an observable.

#### §4.3.6 Scientific open items (Thread C) — revised

`[OPEN]` **A dynamical (non-substrate) graph observable.** The angular spectrum is geometry-saturated. Candidate dynamical observables that are NOT fixed by the $\mathbb{Z}_N$ antipodal substrate: birth-window graph evolution (the $G_{\rm birth}(w)$ sequence), advance-spectrum statistics along the trajectory, or inter-birth-interval structure (cf. the TDR-G response-tensor branch's one surviving N-dependent feature, inter-birth-interval CV). Any such observable must be null-gated against BOTH a degree/reciprocal null AND the $\mathbb{Z}_N$ geometry null before it can be called dynamical.

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
| TDR-G arithmetic structure | Branch-local / `[bridge-candidate]` from Discrete Genesis v2.12 | Active cross-branch import; evidence for Dyadic/bridge claim | SG-PROG-1, SG-AZ-3 |
| TDR-G BIND3 / advance-spectrum | Three-node/no-birth or specified source scope only | Full TDR-G theorem through star blow-up or continuum bridge | SG-PROG-1, SG-AZ-3 |
| TDR-26 discriminator | Branch-local dataset separation `[NUM cross-cell, n=2]`; classifier `[HEUR]` | Theorem-grade, universal, or cross-branch evidence | SG-PROG-1, SG-AZ-3, SG-AZ-7 |
| **Thread C engineering** | **`[ENG PASS]` — certified, exit-code-gated, hashed artifacts (§4.3.1, §9)** | Treating any single run as certified without its manifest/hash/null provenance | SG-AZ-5 (revised) |
| **PROP-AZ-CORE-EQUIV** | **`[THM-ALG]`, scope: finite simple undirected, both-orientations, no multiedges/self-loops** | Applying it to arbitrary directed exports or multigraphs; claiming strong connectivity of the transition graph | SG-AZ-6 (Thread-C-owned) |
| **Antipodal-band low-order obstruction** | **`[ALG]`: no $L=2,3$ closure under $k<N/6$; $L=4$ first constructible closure; odd closure impossible when $Lk<N/2$ (necessary obstruction bound)** | "$\operatorname{Tr}(B^L)=0$ for all odd $L$"; exact 4th-root spectrum; treating $Lk\ge N/2$ as a sufficiency/existence theorem; promoting the full `4|q` rule to `[ALG]` | §4.3.4 retraction |
| **`4|q` angular rule** | **`[NUM diagnostic]` / `[HEUR/NUM strong]`: static $\mathbb{Z}_N$ antipodal-band geometry** | TDR-G dynamical signal; bridge-candidate; analogue of Dyadic subgroup charge | SG-AZ-4, SG-AZ-7 |
| Graph-zeta diagnostics generally | Certified engine; results require full provenance | Reporting a spectral value without graph object/spectrum mode/null/eps-angle/version/hash | SG-AZ-5 (revised) |
| Continuous $p$-resonance results | Reference-only from Dyadic DSN; conditionally physical under OPEN-P0 | Physically primitive or generator-independent | SG-PROG-2 |

---

## §6. Bridge-Candidate Connections

This section records the potential connections between threads and between this study and the programme-level open problems. All items are `[bridge-candidate]`, `[bridge-disqualified]`, or `[OPEN]`; none is an active import.

**To Dyadic OPEN 9:**  
Thread A collects the current Dyadic arithmetic horizon as an import-ref ledger from `RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1`. The active arithmetic frontier remains cubic cascade $q=4,(0,3)$, universal missing-slot rules, bridge-gap smooth baseline, near-cancellation structure, all-$b\ge5$ persistence/general-coefficient extension, and the universal $\nu_5^{(p)}$ theorem.

**To OPEN-P1 (discrete-continuous bridge):**  
Thread B defines the TDR-G $\mathbb{Z}_N$ arithmetic structure as a candidate observable family for OPEN-P1; these remain branch-local until a named bridge theorem exists; SG-AZ-7 blocks vocabulary-similarity promotion.  
**v0.6 [bridge-disqualified]:** the Core(G_T) `4|q` angular Hashimoto observable is REMOVED from the bridge-candidate pool. It was the most tempting candidate (a divisor-graded selection rule, superficially like Dyadic cyclic-subgroup selection), and it is exactly the SG-AZ-7 trap: it is static $\mathbb{Z}_N$ substrate geometry (§4.3.2–§4.3.4), so a resemblance to Dyadic subgroup-charge structure is vacuous. Recorded here so it is not re-proposed.

**To Genesis OPEN 1 (phase-moment distribution):**  
`[OPEN]` Whether $p$-resonance arithmetic selects the physical phase moments for the cascade condition $\langle\mathcal{P}_4\rangle>0$ is downstream of both Thread A and the Genesis study; recorded only as a candidate after the relevant Genesis/Triadic phase-import gates resolve.

**To Genesis OPEN 1 / cascade criterion:**  
`[bridge-candidate]` Genesis v2.8.4 closes OPEN 1C and certifies that the $\mathcal{P}_4$-only cascade is impossible in the reduced birth-race model; the cascade question routes through OPEN M. A Thread C spectral observable could in principle serve as an independent discriminator for crystallizing-vs-growth TDR-G policy branches — but only a DYNAMICAL one would qualify; the angular spectrum does not (§4.3.4). Speculative; `[SG-AZ-3, SG-AZ-4, SG-PROG-1, SG-AZ-7 apply]`.

**To OPEN M:**  
`[bridge-candidate]` The $p=6/K_4$ face-flux identity $\lambda=e^{iF_f/2}$ is a Dyadic import-ref. The SU(2) energy ratio $E_{\rm full}/E_{\rm half}=4$ is source-scoped, but the OPEN-M cascade test is linear in $\|H\|_B$ (amplitude), so the legal correction is $\times2$, not $\times4$; applying $\times4$ is a certified dimensional type error under AUDIT-1-DIMENSIONAL in the OPEN-M ledger. No arithmetic-horizon or graph-zeta result in this DSN contributes to or supersedes that verdict. `[SG-AZ-6, SG-PROG-4]`

**To Programme Overview §6:**  
This study is a Tier 5 infrastructure entry. The Programme Overview should be updated to register `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.6`. See §7 Note.

---

## §7. Note on Programme Overview Update

`[DEF]` The Programme Overview `RTG_PROGRAMME_OVERVIEW_v1.1` should be patched to register this study at its current version. Proposed Tier 5 entry:

```md
**`RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN`** (current: v0.6)

Physical question: Does arithmetic horizon structure — period length, divisibility, prime/composite
obstruction, cyclic memory, advance-spectrum conservation, and zeta/transfer spectra — play a genuine
structural role in RTG resonance dynamics, discrete relational memory, or future discrete-continuous
bridge observables?

Maturity: Level A — infrastructure and ledger. Thread C engineering certified (AZ-1 closed,
[ENG PASS]); first Phase-2 diagnostic executed and reclassified as static Z_N substrate geometry;
no Zeta-owned cross-branch scientific result; no bridge-candidate promoted.
Imports from (by reference only): RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1 (OPEN 9 ledger).
Branch-local context from: RTG_DISCRETE_GENESIS_DSN_v2.12 (Z_N arithmetic, reachability,
advance-spectrum/BIND3/N-scaling; bridge-candidate only).
Bridge-candidate connections: OPEN-P1 (TDR-G Z_N arithmetic as candidate observable family);
NOTE the Core(G_T) 4|q angular observable is bridge-DISQUALIFIED (static Z_N geometry).
Cross-branch: SG-PROG-1, SG-PROG-4, SG-AZ-3, SG-AZ-0.4 apply; threads separated until a named
bridge theorem exists.
```

Also: in the cross-study dependency graph, keep the dashed `[reference / bridge-candidate]` edges from Dyadic OPEN 9 and to `[RTG_DISCRETE_CONTINUOUS_BRIDGE]`, and the dashed branch-local context edge from `RTG_DISCRETE_GENESIS_DSN_v2.12`; annotate the latter `[TDR-G arithmetic context; no cross-branch import; 4|q observable bridge-disqualified]`.

---

## §8. Import Ledger

This document makes no active cross-branch imports. All Dyadic OPEN 9 results cited in §4.1 are `[import-ref]` — owned by `RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1`. TDR-G facts cited in §4.2 are branch-local context / `[bridge-candidate]`. The Thread C internal results (§4.3.2) and Phase-2 diagnostic (§4.3.3) are owned by this DSN and are not imports.

### Reference imports from `RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1`

- [RID: DYAD-THM-RAW-CUBIC] :: Raw cubic theorem :: `[import-ref]` `[THM]`
- [RID: DYAD-ALG-P567-LEDGER] :: Finite one-step ledger $p=5,6,7$ :: `[import-ref]` `[ALG]`
- [RID: DYAD-ALG-GLATTICE5] :: $p=5$ lattice cancellation $G_{\rm lattice}(5)=0$ :: `[import-ref]` `[ALG]`
- [RID: DYAD-OPEN-P-RESONANCE — sub-items] :: $G_{04}(10)=0$ reinterpretation; $p=12$ cascade boundary; $p=7$ transparency `[FAIL]`; universal $q=4,(0,3)$ `[FAIL]`; subgroup-projector/missing-slot formalism :: `[import-ref]`
- [RID: DYAD-ALG-VANISH-B2] :: $F_{\rm raw}^p(0,2)=0$ for $p\ge4$; exception $p=3$ :: `[import-ref]` `[ALG]`
- [RID: DYAD-ALG-VANISH-B3] :: $F_{\rm raw}^p(0,3)=0$ for $p\ge5$; boundary $p=3,4$ :: `[import-ref]` `[ALG]`
- [RID: DYAD-ALG-VANISH-B4] :: $F_{\rm raw}^p(0,4)=0$ for $p\ge6$; boundary $p=4,5$ :: `[import-ref]` `[ALG]`
- [RID: DYAD-OPEN-P-RESONANCE — b-boundary] :: vanishing iff $b\le4$, $b=5$ failure for $p\ge6$ :: `[import-ref]` `[ALG]` :: dyadic-map scope; all-$b\ge5$/general-coefficient `[OPEN]`
- [RID: DYAD-ALG-DIRECT-WEIGHT] :: direct weight $\lambda^{-(b+1)k}$, orbit-sum vanishing for $p\nmid(b+1)$ :: `[import-ref]` `[ALG, exact]`
- [RID: DYAD-ALG-CROSS-IDENTITY] :: cyclotomic cross-term identity for $p\ge5$ :: `[import-ref]` `[ALG, exact]`
- [RID: DYAD-ALG-Q3-CANCEL] :: degree-2 $q=3$ anti-holomorphic cancellation (raw Birkhoff-strobe) :: `[import-ref]` `[ALG]`
- [RID: DYAD-OPEN-P-RESONANCE — subgroup cardinality] :: $|K^{\rm extra}_{p,q}|=s-1$ :: `[import-ref]` `[ALG]`
- [RID: DYAD-ALG-P6-FACEFLUX] :: $p=6/K_4$ face-flux identity :: `[import-ref]` `[ALG, exact]` :: OPEN-M transfer `[CAND/conditional]`

### Branch-local context from `RTG_DISCRETE_GENESIS_DSN_v2.12`

- [RID: TDRG-ZN-STATE] :: $\mathbb{Z}_N$ system, defect band $\mathcal{D}_k$, relational phases, absolute-phase gauge :: `[bridge-candidate]`
- [RID: LEM-REACH] :: band-form reachability/superselection :: `[bridge-candidate]` `[THM/ALG in source]`
- [RID: LEM-RETRIG] :: two-node retrigger threshold :: `[bridge-candidate]` `[ALG in source]`
- [RID: LEM-SPECCONS] :: three-node no-birth advance-spectrum conservation :: `[bridge-candidate]` `[ALG in source]`
- [RID: BIND3-*] :: cycle enumeration / NKSCAN; survival parity, spectral gate, even-sector memory correction :: `[bridge-candidate]` `[ALG/NUM strong in source]`
- [RID: TDR-24 / N-SCALING] :: $k/N$ growth control, `bound_symmetric` $N^{-0.869}$ scaling, crystallization `[HEUR strong]`, TDR-24 frontier :: `[bridge-candidate]`
- [RID: TDR-26-BIRTH-ANCHOR] :: birth-anchored discriminator over $[\mathrm{fb},\mathrm{fb}+200)$, $N=720,722$ :: `[bridge-candidate]` `[NUM cross-cell, n=2; classifier HEUR]`

### Bridge-required / bridge-disqualified export candidates

- [RID: AZ-EXPORT-ZETA-SPECTRUM] :: Hashimoto/transfer-zeta spectral statistics :: engine now `[ENG PASS]`; cross-branch use still blocked by OPEN-P1
- [RID: TDRG-AZ-STATIC-ZN-4Q] :: Core(G_T) `4|q` angular rule :: **`[bridge-disqualified]`** — static $\mathbb{Z}_N$ geometry; removed from bridge-candidate pool (§4.3.4, §6)
- [RID: AZ-EXPORT-ADVANCE-SPECTRUM] :: TDR-G advance-spectrum statistics as candidate OPEN-P1 observable :: branch-local until OPEN-P1 defines a bridge observable
- [RID: AZ-EXPORT-TDR26-BIRTH-WINDOW] :: TDR-26 birth-anchored memory-window discriminator :: branch-local until OPEN-P1 + source batch-scale validation

---

## §9. Artifact and Script Registry

**Current status (v0.6):** the engine and Phase-2 artifacts are real and named. `[COR]` SHA-256 hashes are stored in `AZ-ART-AZV5-REGISTRY` and the per-result artifact manifests; this DSN lists RID-level artifact identities and points to that hash source rather than duplicating hashes inline (SG-AZ-5 provenance is satisfied by the manifest reference). The prior `v3 historical / v4,v5 planned` placeholder registry is superseded.

- [RID: AZ-ART-AZV5-REGISTRY] :: `az_v5` package + SHA-256 manifest (lib/hashimoto, graphgen, graphio, manifest; benchmark_ladder; validate_solver; az1b_certify; phase2_harness; benchmarks) :: certified engine, exit-code-gated; **canonical hash source** :: `[ENG PASS]`
- [RID: AZ-ART-CONVENTIONS-FROZEN] :: `CONVENTIONS_FROZEN.md` (CONV-AZ-GRAPH-EXPORT, DEF-AZ-CORE, CONV-AZ-SPECTRUM-MODE, CONV-AZ-STATS-MULTITEST, CONV-AZ-NULLS, CONV-AZ-ANGLE-ZERO, SG-PLAN-*) :: frozen conventions :: `[ENG PASS]`
- [RID: AZ-ART-AZ1B-CERTIFY] :: `az1b_certify.py` ingestion/export/provenance + manifest-hardening certification suite :: `[ENG PASS]`
- [RID: AZ-ART-SPECTRAL-RADIUS-PATCH] :: `spectral_radius_patch.py` (ARPACK `which='LM'`; replaces buggy power-iteration that mis-handles $\pm R$ dominant pairs; certified to dense $<10^{-6}$) :: `[ENG PASS]`
- [RID: AZ-ART-PROP-CORE-EQUIV] :: `prove_core_equiv.py` + `CORE_EQUIV_CERT_aggregate.json` + `CORE_EQUIV_CERT_n7.json` (2,141,014 graphs, 0 counterexamples) :: certificate for `[THM-ALG]` PROP-AZ-CORE-EQUIV
- [RID: AZ-ART-ANTIPODAL-LOWORDER] :: `THM_AZ_ANTIPODAL_4Q.md` (corrected v2: low-order obstruction `[ALG]`; angular rule `[HEUR/NUM]`; retraction of v1 exact theorem) :: certificate for `[ALG]` antipodal-band low-order obstruction
- [RID: AZ-ART-PHASE2-N120-CORE] :: `run_phase2_baseline.py` + `AZ_PHASE2_MULTIN_RESULT.md` + the three registered Null1 reports `AZ_PHASE2_N120_CORE_NULL1_v1.json`, `AZ_PHASE2_N180_CORE_NULL1_v1.json`, `AZ_PHASE2_N240_CORE_NULL1_v1.json` (per-q tables, Null0+Null1, 1000 nulls, 5 seeds) :: certificate for `[NUM diagnostic]` TDRG-AZ-STATIC-ZN-4Q Chain 1
- [RID: AZ-ART-THETA-CORE-MATCHED] :: `AZ_THETA_CORE_MATCHED.json` (core-matched random-theta antipodal-band null reproduces 4|q; per-q, N=120/180/240) :: certificate for the static-geometry reclassification (Chain 2)
- [RID: AZ-ART-ZETA-V3] :: `rtg_graph_zeta_proto_v3.py` :: Historical; superseded by `az_v5`; all v3 runs `[unverified]` :: `[ENG-historical]`

---

## §10. Collaboration and Audit Record

Authors: Mustafa (PI) · Claude · ChatGPT · Gemini · Grok

- **June 2026 — v0.6 ledger-state update (with audit patch round).** Prepared from v0.5 plus the Thread C engineering/audit/Phase-2 work and the attached structured audits. Scope: recorded AZ-1 closure (AZ-1A/1B/1C `[ENG PASS]`); registered AZ-OPEN-EDGE resolution; registered `[THM-ALG]` PROP-AZ-CORE-EQUIV and `[ALG]` antipodal-band low-order obstruction; registered the Phase-2 `4|q` result and its reclassification as static $\mathbb{Z}_N$ geometry; added the §4.3.4 retraction block; revised SG-AZ-5 from a pre-science gate to a provenance guard; added the SG-AZ-7 worked example; recorded AZ-2 as attempted/negative-clarifying with no Level B promotion; populated §9 with real hashed artifacts. Post-draft audit patches applied: (1) odd-closure threshold softened to a necessary obstruction bound, not a sufficiency/existence theorem; "$L=4$ shortest" → "first constructible closure scale"; (2) G_cumulative retraction reason corrected (Null1/topology control, not a radius-bug artifact); (3) the `4|q` evidence split into Chain 1 (Null0/Null1 statistical excess) and Chain 2 (core-matched theta per-$q$ comparison) with distinct scope and sample size; (4) §9 artifact hashes pointed to the manifest source and the shorthand `N120/180/240` path expanded to exact registered file names; (5) per-$q$ $z$-score claim made artifact-scoped rather than quoting an inline range. Maturity remains Level A. No cross-branch import; no bridge-candidate promoted. Multiple internal self-corrections (spectral-radius bug, core-definition mismatch, v1 exact-theorem counterexample, falsified $k/N$ prediction) are recorded permanently per error-culture policy.
- **June 2026 — v0.5 precision patch.** Corrected stale v0.3 wording; sharpened direct-weight/$b=5$ attribution; expanded degree-2 $q=3$ theorem; added `[ENG-open-3]`; added SG-AZ-1/2 guards on the zeta-pole item. Thread C engineering-blocked at that time.
- **June 2026 — v0.4 post-audit correction patch.** Added Dyadic import-ref mechanisms, TDR-26 branch-local discriminator, SG-AZ-7, blocker sequencing, Genesis/OPEN-M precision notes.
- **June 2026 — v0.3 source-refresh patch.** Pointer updates to Dyadic v6.4.8.1 / Discrete Genesis v2.12; Thread A/B refresh.
- **June 2026 — v0.1/v0.2.** Initial draft and consistency pass.

---

## Appendix A — Version History

### v0.6 — June 2026

Ledger-state update over v0.5. Thread C engineering certified; first Phase-2 diagnostic registered and reclassified. Maturity Level A retained; no Level B promotion; no bridge-candidate promoted.

- **Header [COR]:** Version → v0.6; Supersedes → v0.5; Maturity note expanded; status summary and "major update" list added.
- **Local Tag Aliases [NEW]:** `[ENG PASS]` and `[bridge-disqualified]` aliases added.
- **§0 / §0.1 [COR]:** Function (4) reworded from "register blockers" to "record certified state + diagnostics under provenance/scope guards." Ownership map adds Thread-C-owned engine, graph-theoretic facts, and Phase-2 diagnostic rows.
- **§1.1 [COR]:** Immediate purpose (3) marked done; success criterion sharpened to require dynamics-not-substrate and recorded NOT met.
- **§1.3 [COR]:** AZ-1 marked CLOSED; AZ-2 marked attempted/negative-clarifying.
- **§2 [COR]:** AZ-OPEN-ENG and AZ-OPEN-EDGE marked RESOLVED; AZ-OPEN-SCOPE-ZETA partial answer recorded.
- **§3 [COR]:** SG-AZ-5 repurposed from pre-science gate to provenance guard; SG-AZ-6 clarified for Thread-C-owned facts; SG-AZ-7 worked example added.
- **§4.1 / §4.2 [NO CONTENT CHANGE]:** Thread A import-ref ledger and Thread B bridge-candidates carried forward unchanged.
- **§4.3 [MAJOR]:** Engineering closure (§4.3.1, AZ-1A/1B/1C `[ENG PASS]`); AZ-OPEN-EDGE decision (§4.3.1.1); internal results (§4.3.2: PROP-AZ-CORE-EQUIV `[THM-ALG]`, antipodal-band low-order obstruction `[ALG]`); Phase-2 result (§4.3.3, TDRG-AZ-STATIC-ZN-4Q); retraction block (§4.3.4); AZ-2 status (§4.3.5); revised open items (§4.3.6).
- **§5 [COR]:** High-risk ledger gains rows for Thread C engineering, PROP-AZ-CORE-EQUIV, the low-order obstruction, and the `4|q` rule with their exact valid forms and forbidden overclaims.
- **§6 [COR]:** OPEN-P1 connection records the `4|q` observable as `[bridge-disqualified]`.
- **§7 [COR]:** Programme Overview entry updated to v0.6 with bridge-disqualified annotation.
- **§8 [COR]:** Import ledger gains the bridge-disqualified `4|q` entry; engine marked `[ENG PASS]`.
- **§9 [REPLACED]:** Placeholder registry replaced with real hashed artifacts (AZV5-REGISTRY, CONVENTIONS-FROZEN, AZ1B-CERTIFY, SPECTRAL-RADIUS-PATCH, PROP-CORE-EQUIV, ANTIPODAL-LOWORDER, PHASE2-N120-CORE, THETA-CORE-MATCHED).
- **§10 [COR]:** Audit record updated.
- **Audit patch round [COR]:** (1) §4.3.2 odd-closure threshold reworded as a necessary obstruction bound (not sufficiency); "$L=4$ shortest" → "first constructible closure scale"; matching §5 row updated. (2) §4.3.4 + Appendix B: G_cumulative retraction reason corrected to Null1/topology control (radius bug primarily affected the Core "generic" claim). (3) §4.3.3 split into Chain 1 (Null0/Null1 excess, 1000 nulls × 5 seeds) and Chain 2 (core-matched theta per-$q$ comparison) with distinct scope/sample size; inline "$z\sim6$–$28$" replaced by artifact-scoped wording. (4) §9 hashes pointed to the manifest source; `N120/180/240` shorthand expanded to exact file names.

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

---

*END OF DOCUMENT — RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.6*  
*Supersedes v0.5. Infrastructure and ledger document. Thread C engineering certified (`[ENG PASS]`, AZ-1 closed); one Phase-2 diagnostic registered and reclassified as static $\mathbb{Z}_N$ substrate geometry; no Zeta-owned cross-branch scientific result; no OPEN-P1/Dyadic bridge-candidate promoted (the `4|q` angular observable is bridge-disqualified). Maturity: Level A. Promotion to Level B requires a reproducible, null-gated, TDR-G-DYNAMICAL (non-substrate) observable plus satisfaction of the success criterion in §1.1.*
