# RTG Number Genesis DSN v1.20.7

**Title:** RTG Number Genesis — Relational Composition, Repetition, Number Representations, and Recurrence Holonomy  
**Date:** September 25, 2026  
**Document status:** ACTIVE owner ledger; **owner synchronization + scoped algebra adoption + governance repair.** **Supersedes:** v1.20.6 (`2a51c4b1…48c5`).  
**DSN Methodology:** v1.3; §2/§6 structural migration completed in v1.20.3.  
**Methodology note:** the §2/§6 structural migration is complete (v1.20.3). The normalization of the ruled combined-grade inventory is complete (v1.20.6): the 19 raw combined `[from: X/Y]` rows resolve into 11 owner grade decisions and 8 mirror synchronizations; the §9.2 provenance mirrors are synchronized; two latent substantive definitions were extracted into DEF blocks. **Remaining inventory resolved in v1.20.7 before freeze:** all 12 bare RESULT tags and the one DEF/INTERP tag are normalized — 10 by K5 mirror pairing with from: ALG, and the rest by co-owner-ruled K1/K2 splits (C7C-WD / C7C-0; the §8 N-5 summary; the §8 paradigm note). No live bare RESULT or combined truth-status tag remains. §9.2 artifact-role labels (e.g. `ENG/ALG audit`, `NUM/ENG provenance`) classify artifacts, not claims, and are out of scope.  
**Scope:** Foundational construction of number-like representations and arithmetic compatibility from relational arrows/transitions, composition, repeatable event histories, orientation/inversion, finite multiplicity, phase/character structure, commensurability classification, and recurrence-holonomy diagnostics. Additive, difference, ratio, and multiplicative numerical forms are treated as sector-dependent representations unless a certified mechanism gives them stronger physical status.  
**Document class:** Foundational/technical bridge ledger. It does **not** modify the ontology, Dyadic, Discrete, Triadic, or Genesis dynamics.  
**Companion documents (current verified pointer targets):** `RTG_PROGRAMME_OVERVIEW_v1.2` · `RTG_ONTOLOGICAL_FOUNDATIONS_v0.8` · `RTG_DYADIC_OSCILLATOR_DSN_v6.4.10` · `RTG_DISCRETE_GENESIS_DSN_v2.12.13` · `RTG_GENESIS_GEOMETRY_DSN_v2.8.4`  
**Pointer-validation note:** the current source files listed above were revalidated during the v1.3 state-synchronization pass and retained unchanged through v1.19 (no fresh external owner-source revalidation was performed in v1.19). Section/guard pointers used below were checked in v1.17 against the live owner sources, the GAP-LOCK Lemma-3 closure record, and the ratified DISC-1 / DISC-2 artifact bundles. `DZT v0.17` is reported as the frozen current DZT state by `RTG_NG_PROGRAMME_REVIEW_AUDIT_v1.md`, but the v0.17 owner DSN is not present in the current project corpus; this Number Genesis DSN therefore does **not** use audit-reported DZT theorem status as an owner-source import.  
**Methodology:** DSN Methodology v1.3. This ledger does **not** itself constitute an OPEN-P1 physical bridge (Programme v1.2 SG-PROG-4: document location and representation theorems create no bridge authority).  
**Status summary (scientific state fixed at v1.20; theorem-level state carried through v1.20.6; v1.20.7 adopts the M2-1 transported chain identity at ALG grade and records the C7C-M2 Census-1 outcome INCONCLUSIVE / INCONCLUSIVE):** Local Track-A/Track-B number-like representations are certified on an explicit Dyadic-certified tube; the canonical section stream is a non-fixed re-blocking with theorem-grade logarithmic defect and physical slip-ratio limit (GAP-LOCK 1–3 closed); bounded commensurability yields unique rational labels (C7A) with a ratified ten-label dynamic lower bound `{1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4} ⊆ Q_RTG^dyn`; C7C-0 reciprocal is closed and C7C-M is partially resolved (exact chain identity and conditional carrier closure `[ALG]`; interface-typed WD-DOM OPEN). C7B global breadth, C7C-A, N-4, N-6, NG-7B and full NG-8 remain OPEN. The full v0.4→v1.19 status narrative is preserved in Appendix A history.  

---

## §0. Epistemic Conventions

This ledger distinguishes four layers that must not be collapsed:

1. **RTG ontology:** what is physically primitive in the programme.
2. **Standard mathematics:** mathematical structures used in the metalanguage to formulate proofs.
3. **RTG representation theorem:** proof that an RTG-native object realizes/isomorphic to a standard mathematical structure.
4. **Physical interpretation:** claim that the represented structure is physically instantiated and measurable in RTG dynamics.

`[DEF]` **Metalanguage guard.** A proof may use ordinary mathematics, including `N`, `Z`, `Q`, and `R`, in the metalanguage. “Number is emergent” means these objects are not assumed as **primitive physical coordinates or quantities** in the RTG ontology; it does not mean a proof must be written without mathematical numbers.

`[DEF]` **Standard-math tag.** `[MATH]` denotes an established mathematical construction used as input, not a novel RTG theorem.

### §0.1 Local Tag Aliases

To preserve compatibility with earlier Number Genesis drafts while conforming to the programme truth-status discipline, the following local aliases are declarations rather than new truth classes:

| Local notation | Canonical reading |
|---|---|
| `[DEF candidate]` | `[DEF]` with adoption/scope still local or provisional |
| `[ALG structure]` | `[ALG] [scope: structural]` |
| `[ALG target]` | `[OPEN] [target: ALG]` |
| `[INTERP]` | `[HEUR] [scope: interpretation]` |
| `[POSTHOC-DIAG]` | `[NUM] [scope: post-hoc diagnostic; non-admission evidence]` |
| `[MATH]` | `[THM] [scope: standard mathematical input]` |
| `[REPRO]`, `[PROVENANCE]`, `[GUARD]` | structural/metadata markers, **not** truth statuses (Methodology v1.3) |
| `[ALG consequence]` | `[RESULT] [from: ALG]` |
| `[NUM-HP]` | `[NUM] [scope: high-precision]` |
| `[RESULT-NUM-HP]` | `[RESULT] [from: NUM] [scope: high-precision]` |
| `[ENG/NUM]` | `[NUM] [artifact: executable/engineering audit]` |
| `[GUARD]` | scope/method guard; not a truth-status tag |
| `[REJECTED ...]` | rejected formulation/overclaim; not a truth-status tag |

New entries should prefer the canonical form directly.

`[HYP]` **Central thesis.** RTG does not fundamentally replace one primitive number line by another. The physically prior content is relational: admissible arrows/transitions, their orientation where physical, their composition, and the repeatable histories they generate. Number systems enter as representations/invariants of these relational structures. Track-A repetition yields exponent/count structure; signed comparison yields orientation-sensitive group structure; phase, winding, characters, finite residues, commensurability and completion supply further sector-dependent representations.

`[GUARD]` **No additive-vs-ratio primitivity by notation.** Writing one invariant as a quotient/composition law or as a difference/additive coordinate does not establish ontological priority. A primitivity claim requires a certified physical mechanism and a certified sector gauge; see SG-NG-22.

---

## §1. Current Canonical State

### §1.1 Imported RTG foundations

`[RESULT]` `[from: DEF]` `[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.8 §1.1 | RID unavailable]` **Relational primacy.** Physical content is relational; an isolated node has no physical state. Absolute phase is gauge; only relational phase differences are physical.

`[RESULT]` `[from: DEF]` `[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.8 §1.2 | RID unavailable]` **No external physical time.** The sequence of relational events constitutes RTG time. Formal step/block indices are bookkeeping devices, not external physical clocks.

`[RESULT]` `[from: THM]` `[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.1, §6.4 | RID unavailable]` **Continuous phase/winding support.** The primitive dyad has order-6 elliptic linearization `lambda = exp(± i pi/3)` and uses a lifted angle with winding index `ell`; quantities entering only through `sin eta` or `cos eta` are insensitive to `ell`.

`[DEF]` `[import: RTG_DISCRETE_GENESIS_DSN_v2.12.13 §6.1 | RID unavailable]` **Finite phase support — state space.** The discrete branch is defined on `Z_N` (N even), physical states are quotiented by global phase shift, and relational phase differences are primary.

`[THM]` `[import: RTG_DISCRETE_GENESIS_DSN_v2.12.13 §6.2 | RID unavailable]` `[scope: deterministic system under a fixed node-count cap]` **Finite phase support — recurrence.** Capped deterministic dynamics are eventually periodic.

`[GUARD]` **RF-06 state/gauge scope of the imported finite phase support.** The imported statement above is kept verbatim (K4); this note fixes its scope. (1) The global-phase quotient is the only **unrestricted** gauge. (2) The TDR-G transition state also carries tokens / relative advances; state completeness follows OFN v0.8 SG-OFN-STATE (a gauge-invariant observable is not a complete state unless the dynamics is well defined on the quotient). (3) A common token-origin shift is **not** a gauge of the star rule: OFN v0.8 RTG-OFN-ALG-STAR-TOKEN-SHIFT (fixed-star covariance iff `2c = 0`; the star step negates the center token). (4) On the frozen no-birth SWAP/P3 route used by C7B-DISC, the rule **is** equivariant under every common token shift: by direct reading of the pinned v18 transition, phase advance turns a token shift into a common phase shift, SWAP and P3 permute tokens, and path orientation uses token differences; corroborated by a finite spot check (`NG_SELFCHECK_REFERENCE_TRANSPORT_v1`). Hence the DISC phase-and-token-difference cycle key is a legitimate state key on that route. The source-side correction belongs to the Discrete Genesis owner.

`[RESULT]` `[from: DEF]` `[import: RTG_DISCRETE_GENESIS_DSN_v2.12.13 SG-10; RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 SG-14; RTG_PROGRAMME_OVERVIEW_v1.2 SG-PROG-1 | RID unavailable]` **Cross-branch firewall.** No continuous dynamical law/coefficient may be imported into TDR-G and no discrete coefficient may be imported into the continuous branch without an explicit bridge theorem.

`[GUARD]` **Programme generator-selection ceiling.** `[import: RTG_PROGRAMME_OVERVIEW_v1.2 SG-PROG-2 | RTG-OPEN-GENERATOR-SELECTION]` All N-1/N-2/N-3 results constructed from the continuous primitive map are exact/scoped results **within the selected canonical effective generator `T`**. They do not establish that `T`, or the resulting arithmetic realization, is physically primitive or universal before OPEN-P0 closes.

### §1.2 Number Genesis thesis — relational composition before numerical representation

`[HYP]` **NG thesis.** Primitive physical number-line structure is not assumed. Number-like structure is sought as the representation of certified relational composition, repetition, orientation/inversion, multiplicity, cyclic structure, and commensurability. The programme does **not** assume that additive/difference language or ratio/proportion language is universally prior.

`[DEF]` **Proof-dependency order is not ontological priority.** The sequence `N-like -> Z-like -> Q-like -> R-like` is a certification roadmap. It does not assert that the ontology itself is generated in that order.

`[DEF]` **Typed relational architecture with partial physical composition.** `[COR v1.20]` The common home was previously called a relational category; C7C-M showed global physical composition is partial, interface-sensitive, and lacks identities on the physical carrier, so "category" presumed too much. `C_NG` is a **typed relational architecture with partial physical composition**. Certified sectors may carry stronger structure — `G_adm` groupoids, `M_T` endomorphism monoids, the N-2 group completion — and those certified structures are unchanged; no global category/groupoid structure is presumed across sector or birth/interface changes:

- objects are admissible relational states/transition neighborhoods at the adopted scope;
- admissible gauge/presentation equivalences are invertible and form an isomorphism groupoid `G_adm`;
- physical transitions need not be invertible and may generate endomorphism monoids such as `M_T=<T>`;
- numerical labels are introduced only through explicit representation maps/invariants after the relevant relational structure is certified.

This formulation preserves the existing N-1A groupoid while avoiding the false implication that the primitive dynamics itself must be invertible.

`[INTERP]` **Ratio-relational terminology.** “Ratio-relational” may be used when a sector possesses a certified quotient/scaling relation. It must not mean “a primitive real-valued ratio.” The primitive object is an admissible relational arrow/comparison; a numerical quotient is one possible representation.

`[HYP]` **Candidate certification ladder:**

```text
relational distinguishability
        -> admissible relational arrow / transition
        -> composition and orientation/inversion where certified
        -> repeatable endomorphism histories
        -> N-like exponent/count representation
        -> signed-history completion / Z-like representation
        -> sector-specific cyclic / character / quotient representations
        -> co-realized commensurability classes / Q-like labels
        -> order/completion or rotation-class representation / R-like labels
```

`[DEF]` This ladder is a **research/certificate ordering**, not a theorem chain and not an ontology-order claim. Each arrow requires an explicit module closure below.

### §1.2a Counting architecture: three tracks

`[DEF]` Number Genesis must not assume that all uses of a numeral arise from one construction. The programme therefore separates three tracks:

| Track | Native object | Immediate modules |
|---|---|---|
| **A — ordinal/event history** | one-more composition of a repeatable event type | N-1A/B/C, N-2 |
| **B — cardinal/multiplicity** | finite collections of distinguishable relational states/objects; cross-branch node/network counts remain separately firewalled | NG-8A/NG-8B / future CARD modules |
| **C — cyclic/periodic count** | winding, return class, harmonic exponent | N-3A–N-3D |

`[DEF]` **Common-home clarification.** The tracks are not three unrelated number systems awaiting an arbitrary common set. They are candidate invariants/representations of the certified relational architecture `C_NG`: Track A from repeatable endomorphism histories, Track B from physically distinguishable finite collections/object-orbit multiplicity, and Track C from cyclic/character structure of the appropriate completion/representation.

`[OPEN]` **Compatibility problem.** NG-8 must prove that these different invariants admit physically implemented, structure-preserving comparison maps/functorial compatibility. Bare abstract isomorphism or reuse of the same numeral does not suffice.

### §1.3 Immediate practical targets

`[RESULT] [from: ALG]` **Completed foundational target:** N-1 — a sufficiently small punctured primitive-dyad tube realizes the free monoid on one distinguished generator `T`.

`[RESULT] [from: ALG]` **Completed signed-history target:** N-2 — the N-1 monoid admits an injective Grothendieck completion built from oriented pairs of forward histories; the resulting group is infinite cyclic and represented as `(Z,+,0)` only after construction.

`[RESULT] [from: ALG]` **Completed representation layer:** N-3A–N-3D and the representation-kinematic part of N-3C+ — local dynamically induced `eta`-winding is trivial; the abstract circle-character representation is faithful; primitive pullback is non-translational and character-mixing; finite character restriction gives the controlled modulo-`N` quotient; vector-conjugation charge/projector rules determine kinematic reachability.

`[RESULT] [from: THM]` `[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.11 | DYAD-THM-Q403-PHASELAW]` **Upstream cascade item synchronized:** the formerly OPEN N-3C+ `q=4,(0,3)` exact cascade formula is CLOSED all-`p` in the Dyadic owner. Number Genesis imports the closure only as a boundary result; it does not re-own the nonlinear coefficient theorem.

`[RESULT] [from: ALG]` **NG-8A CLOSED — orbit equinumerosity.** On the certified local tube, `m` primitive event occurrences are physically equinumerous with the `m` newly visited post-event relational states via the orbit-evaluation map.

`[RESULT] [from: ALG]` **NG-8B CLOSED — multiplication by physical re-blocking.** For every positive block size `m`, `<T^m>` is free and `(T^m)^k=T^(mk)`; re-blocking changes only the grouping of one primitive history and does not provide an independent N-5A generator.

`[RESULT] [from: ALG]` **NG-7A CLOSED — additive holonomy operator/null layer.** Null theorem `C D^T = 0`, completeness `im D^T = ker(C·)` over field coefficients, orientation/gauge/cycle-basis invariance, the typed scalar-vs-multichannel statistic, capacity-vs-content separation instances, and the TDR-G `Z_N` zero-control are certified (`NG_NG7A_HOLONOMY_NULL_CERT_v1.md`; exit-code-gated script, all pass).

`[RESULT] [from: ALG]` **N-2-ORD CLOSED — physical order representation.** Reachability-first order `y ⪯_T z ⟺ ∃K ∈ M_T, z = K(y)`: a partial order on `U_T`, total on each primitive orbit (ORD-1); `T`-shift covariant (ORD-2); the N-2 positive cone `P = ι(M_T)` makes `G_T` a translation-invariant totally ordered group (ORD-3); the sign of a signed-history class is realized as the orientation of forward reachability between its endpoints (T4); and `Q_true` strictly witnesses every fixed-residue `F`-chain (ORD-4). Certificate: `NG_N2ORD_PHYSICAL_ORDER_CERT_v1.md` (exit 0).

`[OPEN]` **Immediate in-branch frontier: C7C-M — interface-typed WD-DOM / partial-composition closure.** The product *formula* is no longer the question (`pu/qv` emerges from the exact chain identity, M-1A); the frontier is which relational interface information carries physical composition and descends without loss. C7C-WD is adopted and C7C-0 (reciprocal) is CLOSED `[ALG]`; `Q_RTG^bd` is reciprocal-closed. Two frozen native-discrete campaigns are CLOSED: DISC-1 (B PASS / D PASS-INT) and DISC-2 (B-check PASS / D-check PASS). Currently established dynamic labels are `{1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4}`. **C7B global breadth remains OPEN**; a further DISC campaign is deferred, since additional labels do not by themselves supply an operation. GAP-LOCK Lemma 3 is CLOSED `[ALG]`; N-4 remains parallel.

`[RESULT] [from: ALG]` **N-5A-S1 CLOSED at v1.11.** The canonical phase-coincidence stream is independently typed, indefinitely repeatable, co-realized with Track A, ordered by N-2-ORD reachability, and not any fixed re-blocking `T^m`. **N-5 is therefore unblocked**; SG-NG-23 still forbids treating this closure itself as a nontrivial Q-like commensurability theorem.

`[RESULT] [from: ALG]` **N-5 structural spine advanced at v1.15.** Bounded synchronization discrepancy is now a certified presentation-independent commensurability relation on indefinitely repeatable common-order event streams (C1–C4); the synthetic `13:2` periodic language is a positive mathematical control (C5); the canonical dyadic A/B pair fails every positive rational bounded class (C6); and the opposite phase-coincidence streams `B_+`,`B_-` furnish the first physical bounded class at `1:1` (N5-PHYS-1). Consequently C7A supplies a well-defined unique positive-rational invariant on every certified bounded physical pair. Under the spectrum split, N5-PHYS-1 gives `1 in Q_RTG^bd`; the ratified DISC-1 and DISC-2 campaigns give `{1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4} subseteq Q_RTG^dyn subseteq Q_RTG^bd`. Full realization of `Q_(>0)` and physical rational arithmetic remain OPEN.

`[OPEN]` **Parallel robustness target:** N-1B-GROWTH — first derive an abstract history-preserving growth law; any Genesis/TDR-G realization remains separately gated by branch/realization scope.

---

## §2. Active Frontier / OPEN Registry

### Priority ordering

**In-branch Number Genesis proof queue**

1. **C7C-M — interface-typed WD-DOM / partial-composition closure (next active target).** `[v1.20.7]` C7C-M2 instrument frozen and Census-1 executed: INCONCLUSIVE / INCONCLUSIVE — no admitted nondegenerate composable source chain in Census-1 evidence; M2-1 transported chain identity adopted (algebra only). Full-interface typed WD-DOM remains OPEN; missing evidence object: a certified composable three-stream witness. `[v1.20]` M-1A exact chain identity and M-1B conditional carrier closure are CLOSED `[ALG]`; unrestricted WD-CLOSE and naive label-only WD-DOM FAIL on `D_chain`; full-interface typed WD-DOM, associativity admissibility-transfer, and carrier identity/inverse remain OPEN; M-4 realization search HOLD pending the Discrete-owner P2 policy. `[v1.19]` **C7C-WD is ADOPTED** and **C7C-0 is CLOSED `[ALG]`** (`NG_C7C0_RECIPROCAL_CERT_v2.md`). The framework splits **domain congruence** (WD-DOM: admissibility itself must descend through `==_Q`, or the operation must be typed to a class-saturated sector) from **value congruence** (WD-VAL: equivalent representatives give equivalent outputs when composed); "whenever all four compositions are admissible" is necessary but one condition short of a quotient operation. Diag3 showed equal labels sit on dynamically different realizations, and `1` already carries realizations in two disjoint families (N5-PHYS-1 continuous dyad; DISC-2 TDR-G), so WD-DOM is a genuine RTG obligation for any *binary* `Phi`. C7C-0 discharges WD-DOM because `S` is **total** on `R_bd` (physical admissibility established for every `x in R_bd`, hence `D_S = R_bd`); unary-ness alone would not suffice for a partial operation. C7C-M inherits WD-DOM in full. Design requirement: propose an owner-native binary composition with its typed signature `Phi_{tau1,tau2}^{tau3}` and its WD-DOM obligation stated explicitly **before** any outcome-sensitive computation; the product `pu/qv` must *emerge* (WD-REP), never define `Phi`. **C7C-A** addition only if the multiplication carrier survives; laws (associativity, commutativity, distributivity, identities) remain separate downstream obligations. **Campaign hold:** design/algebra may proceed, but the first C7C-M realization search (M-4) is not opened until the Discrete-Genesis owner resolves the P2 antipodal-endpoint presentation-covariance policy used by the current SWAP/P3 implementation.
2. **C7B — global breadth.** C7B-DISC-1 and C7B-DISC-2 are CLOSED, establishing ten dynamic labels. Global breadth remains OPEN. A further campaign (DISC-3) is **deferred**, not blocked: more labels do not imply an operation, and the present spectrum already spans integers and non-integer rationals sufficiently to expose whether a physical arithmetic construction works or fails. Continue only through separately pre-registered owner-native axes and fresh domains; do not infer `Q_RTG^dyn = Q_(>0)` or that the ten established labels exhaust it.
3. **N-4 — global/domain extension in parallel.** Local N-5 work no longer depends on N-4; N-4 remains relevant to global winding/critical-curve structure. GAP-LOCK Lemmas 1–3 are CLOSED and no longer occupy the queue.
4. **N-6 — classify incommensurable/order-completion structure by R-like labels** (representation-level in the continuous branch under SG-NG-19 unless substrate-independence/bridge conditions are met).
5. **NG-8 — full functorial/cross-track counting compatibility / “two fives”.**
6. **NG-10 — Genesis saturation and counting truncation diagnostic.**
7. **NG-9 — external mathematics/physics consequences.**

**Closed at v1.5:** NG-7A (additive holonomy operator/null layer; see the NG-7 module below and §6.8).
**Closed at v1.6:** N-2-ORD (physical order representation; see §6.3a). The remaining P3-dependent refinements are tagged inside that module.
**Closed at v1.11:** N-5A-S1 (second co-realized recurrence/event stream; gates 1–5 closed locally).

**Parallel robustness queue**

- **N-1B-GROWTH** — abstract growth/history preservation first; concrete topology-changing realizations remain scope-gated.

**Arithmetic-dynamics interface — not owned by Number Genesis**

- N-3C+ representation reachability may be consumed by the Dyadic OPEN-9 missing-slot programme. The exact `q=4,(0,3)` nonlinear cascade is already CLOSED upstream. Remaining universal missing-slot/all-`b>=5` work stays with the Dyadic owner/Arithmetic-Dynamics lane and is not an NG foundational priority.

`[DEF]` **Routing-label guard.** “Arithmetic Dynamics” is used in v1.15 only as a descriptive inter-study routing label for Dyadic OPEN-9 + its transforms. It does not rename owner DSNs, move RIDs, or constitute a Programme Overview registration; that programme-level reorganization remains a separate governance action.

---

### Module registry (v1.20.3 structural migration)

<!-- REGISTRY --> Structural pointer rows. The authoritative scientific bodies of these modules live in §6; statuses below are verbatim relocations.

<!-- REGISTRY --> - **CLOSED N-1 — Relational repetition / natural-number realization** → §6: §6.2 N-1A/N-1B/N-1C formal target
<!-- REGISTRY --> - **CLOSED N-2 — Signed-history group completion** → §6: §6.3 N-2 closed signed-history construction
<!-- REGISTRY --> - **CLOSED N-2-ORD — Physical order representation** → §6: §6.3a N-2-ORD physical order representation — CLOSED at v1.6
<!-- REGISTRY --> - **CLOSED N-3A — Local deck inducibility / eta-winding** → §6: §6.4 N-3 representation layer — closed local/abstract results
<!-- REGISTRY --> - **CLOSED N-3B — Abstract circle-character representation** → §6: §6.4 N-3 representation layer — closed local/abstract results
<!-- REGISTRY --> - **CLOSED N-3C — Primitive dynamical character activity (first exact result)** → §6: §6.4 N-3 representation layer — closed local/abstract results
<!-- REGISTRY --> - **CLOSED N-3D — Finite-character quotient / representation bridge** → §6: §6.4 N-3 representation layer — closed local/abstract results
<!-- REGISTRY --> - **CLOSED N-3C+ — Roots-of-unity projectors / OPEN-9 kinematic boundary** → §6: §6.4 N-3 representation layer — closed local/abstract results
<!-- REGISTRY --> - **OPEN N-4 — Global/nonlocal dyadic history representations** → §6: §6.5 N-4 global/nonlocal extension target
<!-- REGISTRY --> - **CLOSED N-5A — Second co-realized recurrence / event stream** → §6: §6.6 N-5A / N-5 rational recurrence target
<!-- REGISTRY --> - **OPEN N-5 — Bounded synchronization commensurability / realized Q-like labels** → §6: §6.6 N-5A / N-5 rational recurrence target
<!-- REGISTRY --> - **OPEN N-6 — Continuum completion** → §6: §6.7 N-6 real completion target
<!-- REGISTRY --> - **NG-7 — Recurrence holonomy / holonomy content** → §6: §6.8 NG-7 recurrence holonomy — NG-7A closed / NG-7B open
<!-- REGISTRY --> - **OPEN NG-8 — Functorial compatibility / “two fives”** → §6: §6.9 NG-8 functorial counting compatibility
<!-- REGISTRY --> - **N-5A-S1 — Second-stream section-crossing search `[COR: v1.7 verdict]` / CLOSED v1.11** → §6: §6.6 N-5A / N-5 rational recurrence target
<!-- REGISTRY --> - **N-5A-S1-INF — CLOSED at v1.11** → §6: §6.6 N-5A / N-5 rational recurrence target
<!-- REGISTRY --> - **OPEN NG-10 — Genesis saturation and counting truncation** → §6: §6.9a NG-10 — Genesis saturation and counting truncation
<!-- REGISTRY --> - **OPEN NG-9 — External mathematics/physics consequences** → §6: §6.10 External benefit boundary
<!-- REGISTRY --> - sub-module status — **CLOSED N-1A-MIN — Abstract Oriented Dyadic Phase-Step**:
<!-- REGISTRY --> **Status:** CLOSED `[ALG]` `[scope: isolated abstract oriented dyadic phase-step]`
<!-- REGISTRY --> - sub-module status — **L1 — Primitive-frame phase-uniform contraction**:
<!-- REGISTRY --> **Status:** CLOSED `[RESULT] [from: ALG] [scope: sufficiently small punctured p=6 primitive dyad sector]`
<!-- REGISTRY --> - sub-module status — **CLOSED N-3A — Local deck inducibility / eta-winding**:
<!-- REGISTRY --> **Status:** CLOSED `[RESULT][from: ALG]` `[scope: sufficiently small one-chart N-1 tube]`

## §3. Scope Guards

**[SG-NG-1] Metalanguage ≠ ontology.** Mathematical use of `N,Z,Q,R` in a proof does not mean RTG assumes them as primitive physical quantities. Conversely, writing an isomorphism to `N` does not by itself prove physical emergence.

**[SG-NG-2] No time-reversal inference.** Group completion to `Z` does not imply that physical RTG histories are reversible. Negative elements may encode formal/oriented history differences.

**[SG-NG-3] No cross-branch dynamics transfer.** Character restriction between `S^1` and `Z_N` is a representation bridge only; it does not transfer continuous sine coupling, normal-form coefficients, TDR-G policies, birth rates, or other dynamical content.

**[SG-NG-4] Finite quotient ≠ continuum-limit theorem.** `Z -> Z/NZ` and roots-of-unity embeddings do not establish that TDR-G converges dynamically to the continuous dyad as `N->infinity`.

**[SG-NG-5] Do not assume the continuum before N-6.** Fundamental recurrence data must not be postulated as arbitrary real numbers if the stated goal is to derive the real continuum.

**[SG-NG-6] Frequency is not primitive absolute time.** Any physical frequency notion must be relational or recurrence-based; cycles per external second cannot be used as the foundational definition.

**[SG-NG-7] Holonomy ≠ curvature without bridge.** Nonzero recurrence holonomy certifies non-integrability of recurrence data, not geometric curvature by itself.

**[SG-NG-8] `p=6` is a realization, not number ontology.** The dyadic order-6 resonance is an exact property of the selected continuous generator; the Number Genesis framework must not derive arithmetic from the special value six alone.

**[SG-NG-9] Standard mathematics is not novel RTG mathematics.** Free monoids, group completion, `pi_1(S^1)`, Pontryagin duality, cyclic characters, and graph cohomology are established inputs. Novelty must lie in RTG-specific identification, bridge theorems, or consequences.

**[SG-NG-10] No external-problem overclaim.** The framework currently reformulates and may constrain problems; it has not yet solved quantum gravity, UV divergence, fine tuning, foundations of set theory, or any named external open problem.

**[SG-NG-11] Strict equivalence ≠ counting equivalence.** Gauge-orbit/isomorphism equivalence is generally finer than the event-type equivalence used for counting. A coarser counting predicate must be declared and justified; it may not silently erase physical distinctions.

**[SG-NG-12] Formal free monoid ≠ physical unbounded repetition.** Standard mathematics permits formal words `E^n` once a symbol `E` is given. RTG realizes an unbounded natural-number sector only if successor extensibility is established in the physical dynamics or explicitly assumed.

**[SG-NG-13] Spectator independence is an admissibility condition.** Inert external context may be quotiented out only when it neither influences nor is changed by the event under the declared boundary semantics.

**[SG-NG-14] Connected context is not automatically spectator.** If closure relations couple an external node to the support, incident relational variables may be constrained and may change when the internal state changes. Such data belong to the boundary interface unless causal irrelevance is proved.

**[SG-NG-15] History record is not automatically physical memory.** Treating the full past relational trajectory as part of the physical present state would make non-collapse trivial. N-1C must instead identify a present/future relational distinction, or explicitly adopt history-as-state as a physical postulate and tag that choice.

**[SG-NG-16] Winding label is not yet a certified physical counter.** The dyadic winding index may label lifted histories, but its certified invisibility to periodic trigonometric observables prevents using it as an N-1C separator without an additional bridge showing physical accessibility or future dynamical effect.

**[SG-NG-17] Boundary isomorphism requires dynamical equivariance.** Matching boundary cardinality, graph shape, or raw phase values is insufficient for strict compatibility. The attachment map, gauge-reduced constraints, orientation policy, and local transition must commute under the proposed isomorphism.

**[SG-NG-18] Typed-object non-conflation for radial coefficients.** `[COR v1.20]` Primitive ray burst (`37/40`, carrying the `-(5/24)Q^(5/2)` half-power term) ≠ raw fixed-radius angular mean (`47/54`) ≠ normalized-chart observable ≠ long-orbit backbone. Only the leading `-Q^2` transfers without an explicit representation/observable bridge. Source: Dyadic v6.4.10 `[DEF]` (distinct objects) and `[COR v6.4.10]` (half-power term; averaging operator). The former "provenance unresolved upstream" wording is withdrawn.

**[SG-NG-19] Continuum substrate ceiling.** A closure of N-6 obtained solely inside the continuous dyad is a representation/recovery theorem relative to a substrate already modeled on a continuum chart. It may not be called genesis of the continuum substrate unless (i) a theorem proves the construction is substrate-independent in the required sense, (ii) a non-continuum realization is connected by a named bridge theorem, or (iii) the continuum assumption is explicitly retained as a tagged postulate.

**[SG-NG-20] Single-generator ratio / co-realization guard.** Ratios of powers or blockings of the one certified generator `T` are standard localization/re-indexing of Track A and do not close N-5. N-5 requires two independently certified event/recurrence types **co-realized in one admissible physical sector** together with a declared RTG-native causal/order relation for comparing their occurrences. External clock synchronization or pre-existing real-valued frequencies are inadmissible foundational substitutes.

**[SG-NG-21] Reserved.** Number reserved for the pending substrate-arity / derived-cardinal non-identity guard (programme-review decision D10: the two-relata structure of the primitive dyad is arity/bookkeeping data and must not be silently identified with a derived Track-B cardinal). Reservation prevents future numbering collision; content activates only on PI ruling.

**[SG-NG-22] Relational-arrow / representation primitivity guard.** No claim that additive/difference structure is physically prior to ratio/proportion structure, or vice versa, is admissible from notation alone. A primitivity claim requires both (i) a certified physical mechanism and (ii) a certified sector gauge/covariance. Admissible examples of representation mechanisms include the free-exponent map of a certified endomorphism monoid, a genuine logarithmic group isomorphism for an independently certified positive multiplicative sector, and cover/character constructions for compact phase. An admissible relational arrow may not be silently replaced by a primitive numerical ratio, difference, logarithm, or coordinate label. In particular, quotient and angle-difference descriptions of the same `U(1)` invariant do not constitute evidence of ontological priority.

**[SG-NG-23] Non-relabeling ≠ nontrivial commensurability.** Showing that a recurrence/event stream is not a fixed blocking `T^m` is necessary for N-5A independence but does not by itself establish incommensurability, a nontrivial Q-like commensurability class, or an R-like invariant. Density limits, subleading discrepancy laws, and asymptotic slip constants must be separately typed. In particular, continuous-dyad constants built from `pi`, `exp`, `tau`, or other already-real-valued chart/normal-form data are representation-level diagnostics under SG-NG-19 and OPEN-P0 unless a substrate-independence or named bridge theorem licenses stronger foundational use.

**[SG-NG-24] Rational density ≠ physical commensurability.** A rational limiting event-density, or even a sublinear relative synchronization defect, is insufficient by itself for a genesis-grade Q-like commensurability claim. The active N-5 candidate requires a certified common-order integer synchronization defect to remain bounded, or a separately proved stronger common-measure criterion. Any weaker quotient that discards an **unbounded certified relational discrepancy** must state and physically justify that information loss explicitly. The canonical A/B pair motivates this guard: its leading event-density tends to `6`, while its certified physical 7-gap count / synchronization discrepancy grows like `log M`.

**[SG-NG-25] Prefix divergence ≠ external time.** Statements such as `N_B(H) -> infinity` in N-5 mean directed/cofinal unboundedness of **finite event counts** under certified common-order prefix extension. They do not introduce, imply, or require an external clock, global duration parameter, completed physical infinity, real-valued time coordinate, or actually completed infinite trajectory. The primitive statement is successor extensibility: every finite admissible prefix can be extended to contain further certified events.

**[SG-NG-26] Common-source finite-multiplicity triviality.** `[v1.18: definition supplied; the guard was invoked in DISC material from v1.16 onward without a section-3 entry]` If two certified streams `A, B` are fixed finite refinements/coarsenings of a common prefix-cofinal parent stream `L`, with `N_A = m_A L + O(1)` and `N_B = m_B L + O(1)` for reasons independent of the active dynamics, then their bounded class `red(m_A, m_B)` is forced by predicate multiplicity (`C7B-ALG-T1`) and is a **physical positive control**. It certifies operation of the C1–C4 bounded-defect machinery but does not by itself populate the dynamically realized spectrum `Q_RTG^dyn`. A discrimination certificate discharges this guard either by proving structurally that no such common-parent multiplicity factorization exists, or by a matched null/control dynamics under which the same predicates change class. The frozen DISC same-realization gate discharges it for admitted witnesses: a deformation-invariant factorization would force the same class at every `k` (`C7B-ALG-T1`), contradicting observed contingency; letting `m_A, m_B` vary with `k` is merely `C7B-ALG-T2` periodicity triviality and does not rescue the objection.



`[GUARD]` **Proof order ≠ ontology order.** The N-1→N-2→N-5→N-6 certificate dependencies do not imply that the represented numerical structures are ontologically generated in the same sequence.

---

## §4. Layer Routing

```text
NG0   RTG relational ontology / programme ceiling
  -> NG1   repeatable event/history composition
  -> NG2   unsigned/signed repetition algebra
       -> N-2-ORD   physical order representation [CLOSED v1.6]
  -> NG3   phase/winding/character representations
  -> NG3B  finite phase quotient / distinguishability

N-4   domain-extension module orthogonal to NG1/NG3:
      tests how far Track-A freeness and cyclic representations survive beyond the local tube

N-5A  second co-realized recurrence/event stream
  -> NG5   commensurability / rational structure
  -> NG6   continuum/order completion

NG8A/B seed ordinal-cardinal/re-blocking compatibility;
NG8 full cross-track counting compatibility remains downstream.

NG7A additive holonomy operator/null theorem
  -> NG7B RTG-native non-integrable source / geometry interface
```

| Question | Layer | Canonical object/tool |
|---|---|---|
| What is physically primitive? | NG0 | RTG ontology / OPEN-P0 programme ceiling |
| How does counting arise? | NG1 | finite histories, primitive `T` transformation monoid |
| How do signed counts arise? | NG2 | group completion / oriented history differences |
| How is order represented physically? | N-2-ORD `[CLOSED v1.6]` | reachability order `<=_T` + N-2 positive cone; `Q_true` as residue-chain witness |
| How is count represented in phase? | NG3 | winding, deck action, circle characters |
| What does finite distinguishability do? | NG3B | `Z -> Z/NZ`, character restriction |
| How far do local results extend? | N-4 | larger exact-map invariant domains / recurrence sectors |
| Where does a second recurrence come from? | N-5A | two co-realized certified event streams + common order |
| How do ratios arise? | NG5 | bounded synchronization classes -> unique rational invariant (C7A); `Q_RTG^bd`/`Q_RTG^dyn` separate bounded realization from strong dynamic admission; ten dynamic labels established by DISC-1/DISC-2; `Q_RTG^bd` reciprocal-closed (C7C-0); global breadth and full arithmetic remain OPEN |
| How does continuum/order completion arise? | NG6 | completion of N-5 classes; representation-level ceiling in continuous branch |
| How can cycle data detect non-integrability? | NG7A | edge cochains, cycle matrix, null theorem |
| What supplies nonzero physical holonomy? | NG7B | non-node-difference RTG source + geometry bridge |
| Why do numeral labels agree across tracks? | NG8 | physical comparison maps / universal counting compatibility |

Routing rules:

- NG0/NG1 claims may not be certified from a downstream normal form alone.
- NG3B may connect representation spaces across branches but never bypass cross-branch dynamical scope guards.
- N-3C+ nonlinear coefficient ownership remains Dyadic; NG exports representation reachability only.
- N-4 is a domain-extension module, not merely a representation module; it can affect both Track-A and Track-C validity.
- N-5A is closed locally; GAP-LOCK Lemmas 1–3 are closed; N-5-COMM-BD structural gates C1–C4, C5 control, C6 falsifier, N5-PHYS-1 and C7A are closed. C7B-DISC-1 and C7B-DISC-2 are CLOSED, establishing `{1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4} subseteq Q_RTG^dyn`; C7B global breadth and C7C physical arithmetic remain OPEN. Single-generator ratios remain controls only.
- NG5/NG6 must not be used retroactively as premises of N-1/N-2.
- In the continuous branch, NG6 is representation/recovery level unless SG-NG-19's stronger substrate condition is discharged.
- NG-7A is CLOSED (v1.5); nonzero holonomy/curvature claims still require the NG-7B physical-source and geometry bridges.

---

## §5. High-Risk Claims Ledger

| Claim | Valid form now | Forbidden overclaim |
|---|---|---|
| “Number is relational repetition” | `[HYP]` central programme thesis | theorem / completed derivation |
| `H_E ≅ (N,+)` | `[RESULT][from: ALG]` for the scoped local dyadic transformation monoid after L1; general RTG identification `[OPEN]` | universal physical RTG counting already proved |
| signed history gives `Z` | `[RESULT][from: ALG]` scoped N-2 signed-history completion; inverse = comparison-orientation swap; sign physically realized as reachability orientation (N-2-ORD T4) | physical time reversal |
| winding and harmonics both give `Z` | `[MATH]` standard structures | proof they are the same RTG history representation |
| `Z_N` phase vs `S^1` | exact candidate character restriction `[MATH]`; RTG bridge `[OPEN]` | discrete/continuous dynamical equivalence |
| bounded synchronization class gives unique rational invariant | `[RESULT][from: ALG]` C1–C4 + N5-PHYS-1 + C7A; `1 in Q_RTG^bd` | claim that boundedness alone is dynamic admission, that all `Q_(>0)` is physically realized, or that rational arithmetic is already derived |
| strong dynamic rational admission | `[RESULT][from: ALG]` frozen DISC-1 + DISC-2 establish ten labels `{1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4} subseteq Q_RTG^dyn` | equality with that set or with `Q_(>0)`, post-data gate retuning, or arithmetic from a label list |
| owner implementation agreement ⟹ presentation covariance | `[REJECTED]` — exhaustive equality to the pinned v18 implementation certifies implementation agreement, not node-relabeling covariance; P2 post-hoc audit finds 40/136 DISC-2 witness records convention-exposed while the ten-label projection remains robust | treating sorted-node tie-breaking as a physical invariant without an owner policy/theorem |
| equal `rho_Q` labels ⟹ interchangeable/composable physical inputs | `[REJECTED]` — `==_Q` is representation equivalence only; WD-DOM must be proved per operation (`1` already spans two disjoint realization families) | any operation defined on labels rather than realizations |
| `Q_RTG^bd` reciprocal closure | `[RESULT][from: ALG]` C7C-0 involution `S`; WD-DOM trivial for this **total** unary map (`D_S = R_bd`), not for unary maps in general | multiplication, addition, field structure, or `Q_RTG^dyn` reciprocal closure |
| completion gives `R` | `[OPEN]` | continuum already derived |
| `log R_+` gives additive line | `[MATH]` after positive real ratio object exists | use as derivation premise for `R` |
| recurrence holonomy `CA` | `[RESULT][from: ALG]` operator/null layer (NG-7A); physical source `[OPEN]` (NG-7B) | spacetime curvature theorem |
| external physics benefit | research motivation `[HYP]` | solved quantum gravity/UV/fine tuning |

---

## §6. Main Scientific Ledger

### §6.1 Thesis: relational structure before numerical container

`[HYP]` The classical number line may be understood inside RTG as a late representation of more primitive relational arrows/transitions, their certified composition, repeatable histories, orientation-sensitive comparisons, and finite/cyclic invariants. The thesis does not deny standard mathematical number systems; it changes their proposed **physical semantics** in RTG.

`[DEF]` Three notions must remain distinct:

- **relational structure:** arrows/transitions, composition, orientation/inversion where certified, and physically distinguishable collections;
- **certificate structure:** the proof-dependency order in which N-like, Z-like, Q-like, and R-like representations are established;
- **numerical representation:** additive/difference, ratio/proportion, exponent, character, winding, or completion coordinates/labels introduced only after the relevant relational structure is certified.

`[GUARD]` No numerical representation is promoted to ontological priority merely because it is convenient or because another representation can be transformed into it. In particular, proof-dependency order is not ontology order, and ratio/proportion is not assumed to be generated “later” than additive count nor vice versa.

### §6.1a NG-0R — relational-composition clarification and sector-covariance audit

**RID:** `NUMGEN-OPEN-NG0R-COV`  
**Status:** documentation layer `[DEF]/[INTERP]` + one pre-registered `[OPEN][target: ALG/NUM]` covariance audit  
**Role:** clarify the physical semantics of “ratio-relational” versus additive/difference representations without changing already-certified N-1/N-2/N-3 theorem ownership.

`[DEF]` **Arrow before numerical label.** The primitive candidate is an admissible relational arrow/comparison, not a pre-existing scalar ratio. Where a sector admits composition,
\[
R_{AB}\circ R_{BC}=R_{AC}
\]
is the structural statement. Numerical quotient, difference, logarithm, exponent, character, or winding labels may be introduced only through a certified representation.

`[DEF]` **Identity and inverse are typed.** Admissible presentation/gauge equivalences live in the groupoid `G_adm` and therefore have inverses. Physical dynamical transitions such as `T` need not be invertible. An orientation-reversal/inverse interpretation may be asserted only for the structure where it has actually been constructed (for example N-2 signed comparison).

`[RESULT] [from: MATH]` **Phase quotient/difference non-test.** For `z_A=e^{i theta_A}` and `z_B=e^{i theta_B}`,
\[
z_A z_B^{-1}=e^{i(\theta_A-\theta_B)}
\]
is one `U(1)` invariant written in multiplicative and angular notation. Verifying this identity cannot decide ontological priority.

`[RESULT] [from: MATH]` **No global additive logarithm on `U(1)`.** There is no nontrivial continuous homomorphism `U(1)->(R,+)`. A local/lifted `arg` is a section of the covering `R->U(1)`, not a global additive homomorphism. Number Genesis therefore keeps three additive-representation mechanisms distinct:

1. **Track A exponent representation:** freeness gives `T^n -> n` after the endomorphism monoid is constructed;
2. **positive multiplicative sectors:** a genuine logarithmic isomorphism may be used only if a physically instantiated `(R_+,x)`-type structure is independently certified;
3. **compact phase:** cover-lift/winding and global character-lattice representations are distinct and are already separated by N-3A/N-3B/N-3C/N-3D.

`[INTERP]` **No universal additive-or-ratio priority.** In a non-compact amplitude sector, “ratio-primitive versus difference-primitive” is equivalent to asking which physical gauge/covariance is actually certified (scaling, shift, or neither). That is a sector-level empirical/algebraic question, not an ontology axiom.

`[OPEN] [target: ALG/NUM]` **HYP-NG-0R-COV — covariance audit.** Before any amplitude-sector ratio-primitivity claim is promoted, audit the certified primitive-dyad laws under the candidate sector transformations. A positive result requires one declared transformation law to act covariantly on the gauge-reduced observables with no independent contradictory additive symmetry. A falsifier is any certified law whose gauge-reduced form breaks the proposed covariance. The phase-sector quotient/difference identity is excluded from the audit because it is representation-equivalent and non-falsifiable.

`[DEF]` **Declared primary transformation (pre-registration pin).** The first audited candidate is amplitude scaling `Q -> lambda Q` on the certified primitive-dyad sector. Predicted covariance form: naive form-invariance of `Delta Q_true = -Q_true^2 + O(Q_true^(5/2))` under pure scaling is expected to FAIL (the law carries an intrinsic scale); the covariance to be tested is translation along the flow in `ln Q` — equivalently, `Q_0 -> lambda Q_0` acting on gauge-reduced entry data only through the entry-phase shift `tau ln lambda` of the `[CAND]` phi* law (`DYAD-CAND-PHISTAR-ENTRY-PHASE`). Falsifier: a certified gauge-reduced law on the sector that admits an independent additive-`Q` symmetry or breaks the flow-translation form. Any conclusion inheriting the phi* leg is capped at `[CAND]` until that law is promoted. Secondary transformations may be declared only by ledger entry before their audit runs.

`[GUARD]` NG-0R is not a new foundational branch and does not block NG-7A, N-2-ORD, or N-5A. It is a semantics/covariance layer under the existing Number Genesis programme.

### §6.2 N-1A/N-1B/N-1C formal target

`[HYP]` **Foundational ordering:**

```text
distinction
  -> relationally admissible predicate
  -> equivalence class / event type
  -> repeatability
  -> successor extensibility
  -> free repetition representation
  -> N-like physical counting sector
```

This is an RTG construction claim, not a theorem that all mathematics requires physical equivalence or repetition.

`[DEF candidate]` The primitive event object is a finite transition neighborhood `N_e=(S_e,dS_e,X_e^- -> X_e^+)`. Strict equivalence is isomorphism in an admissible relational groupoid. Counting equivalence is induced by a declared relational map `P` and may be coarser than strict physical indistinguishability.

`[DEF candidate]` Spectator-invariance requires `P(N_e disjoint_union C)=P(N_e)` for inert `C`. The primitive Number Genesis predicate preserves physical orientation when available.

`[MATH]` Once an abstract event type `E` exists, a formal free monoid on `E` is standard mathematics. The open RTG content is whether physical event histories instantiate that formal structure and whether extension by another `E` remains admissible without a terminal bound.

`[HYP]` **Successor principle:** physical realization of unbounded natural-number structure corresponds to indefinite extensibility of finite relational history, not to a completed infinite collection present at once.

`[RESULT] [from: ALG] [scope: local primitive p=6 dyad transformation sector]` **History non-collapse after L1.** For `F=T^6`, exact primitive-map algebra gives `Delta Q_true=-Q_true^2+O(Q_true^(5/2))` uniformly in phase, hence strict positive radial contraction on a sufficiently small punctured sector. Distinct finite block powers are therefore separated by the present relational observable `Q_true`. This closes the N-1C memory obstruction in that scoped realization.

#### CLOSED N-1 — Relational repetition / natural-number realization

**RID:** `NUMGEN-OPEN-N1`  
**Status:** CLOSED `[RESULT][from: ALG]` `[scope: sufficiently small punctured primitive dyad tube]` — N-1A event identity, N-1B successor, and N-1C non-collapse are aligned on the same exact primitive generator `T`

**Question:** What RTG-native structure is sufficient for a relational event type to support repetition, successor extension, and finally a physical realization of the natural-number repetition algebra?

N-1 has one foundational spine plus one robustness branch:

```text
N-1A-MIN  isolated relational event equivalence  [CLOSED scoped]
   -> N-1A2  boundary locality / context robustness  [CLOSED scoped]
   -> N-1B-MIN  fixed-support successor extensibility  [CLOSED scoped]
   -> N-1C  operational history quotient / free-history test  [CLOSED local dyad by L1]

parallel strengthening after N-1B-MIN:
   N-1B-GROWTH  topology-changing successor robustness  [OPEN]
```

**Foundational guard:** The formal free monoid on a symbol `E` exists in standard mathematics once `E` is specified. The RTG problem is not to recreate that theorem; it is to justify (i) which physical event tokens belong to the same repeatable event type, (ii) whether such a type is dynamically repeatable, and (iii) whether repetition is indefinitely extensible. Only then may RTG claim a physical realization of an `N`-like repetition algebra.

---

##### OPEN N-1A0 — Strict Relational Equivalence

**RID:** `NUMGEN-OPEN-N1A0`  
**Status:** ACTIVE  
**Epistemic target:** `[DEF]` + elementary `[ALG]` once the admissible morphism class is fixed

`[DEF candidate]` **Relational event token.** An event token `e` is represented by a finite transition neighborhood

```text
N_e = (S_e, dS_e, X_e^- -> X_e^+),
```

where:

- `S_e` is a finite relational support sufficient to determine and record the event;
- `dS_e` is its relational boundary, containing environmental data capable of affecting the event;
- `X_e^-` and `X_e^+` are the local relational states immediately before and after the transition.

`[DEF candidate]` **Admissible relational groupoid.** Let `G_adm` be a groupoid whose objects are finite transition neighborhoods and whose invertible morphisms may change nonphysical presentation data while preserving all relationally physical transition data required by the adopted event description.

At minimum, admissible morphisms must preserve, where present in the event model:

1. relational incidence/connectivity;
2. gauge-invariant relational variables (for example phase differences rather than absolute phase);
3. the before/after transition structure;
4. boundary coupling relevant to the event;
5. physical orientation/chirality whenever that distinction is retained by the adopted event predicate.

They may change:

- node labels;
- global phase gauge;
- other presentation choices certified as nonphysical.

`[DEF candidate]` **Strict relational equivalence:**

```text
e1 ~_str e2
iff
N_e1 and N_e2 are isomorphic in G_adm.
```

`[ALG target]` Once `G_adm` is a groupoid, `~_str` is an equivalence relation:

- reflexive by identity morphisms;
- symmetric by inverse morphisms;
- transitive by composition.

**Scope note:** `~_str` is intentionally fine. Events with different physically observable amplitudes or other retained invariant data need not be strictly equivalent even if they instantiate the same counting type.

---

##### OPEN N-1A1 — Counting Equivalence

**RID:** `NUMGEN-OPEN-N1A1`  
**Status:** PARTIAL — closed for N-1A-MIN; general boundary-aware form continues in N-1A2  
**Epistemic target:** `[DEF]` after admissibility conditions on the counting map are fixed

`[DEF candidate]` **Counting-type map.** A counting type is specified by a map

```text
P : E_events -> T_types
```

that is:

1. **relationally definable** — it depends only on relationally physical data;
2. **gauge-invariant** — gauge-equivalent descriptions have the same image;
3. **spectator-invariant** — adding inert relational context does not change the event type;
4. **explicit about retained distinctions** — orientation/chirality/amplitude/topology distinctions are preserved or discarded only by declared policy, never silently.

`[DEF candidate]` **Counting equivalence:**

```text
e1 ~_P e2  iff  P(e1) = P(e2).
```

The event type associated with `tau in T_types` is the fibre

```text
E_tau := P^(-1)(tau).
```

`[ALG target]` Equality in the codomain makes `~_P` an equivalence relation.

`[DEF candidate]` **Compatibility with strict equivalence.** For an admissible counting map `P`, strict equivalence must imply counting equivalence:

```text
e1 ~_str e2  =>  e1 ~_P e2.
```

The converse is not required. Thus physically distinguishable tokens may count as instances of the same declared event type.

`[DEF candidate]` **Declared spectator-independence policy.** If `C` is inert with respect to `e` — it neither affects nor is changed by the transition — then

```text
P(N_e disjoint_union C) = P(N_e).
```

This is an admissibility condition, not yet a derived theorem. It prevents unrelated global growth from destroying local event identity.

`[DEF candidate]` **Orientation policy for primitive Number Genesis.** The primitive N-1 counting map preserves physical orientation whenever orientation is available:

```text
P_orient(E+) != P_orient(E-).
```

Coarser counting maps that deliberately identify opposite orientations are allowed for other purposes but must declare that quotient explicitly.

**Closure criterion for N-1A:** Specify `G_adm` and one primitive Number-Genesis counting map `P_NG`; prove `~_str` and `~_P` are equivalence relations; verify gauge invariance, spectator invariance, and the declared orientation policy on at least one explicit RTG-compatible event model.


##### CLOSED N-1A-MIN — Abstract Oriented Dyadic Phase-Step

**RID:** `NUMGEN-ALG-N1A-MIN`  

`[DEF]` **Minimal event token.** Let

```text
N_e = ({i,j}, empty_boundary, Delta^- -> Delta^+),
delta = Delta^+ - Delta^- != 0.
```

`Delta` is the gauge-invariant oriented dyadic phase difference. Global phase and node labels are presentation data; orientation is retained.

`[DEF]` **Primitive counting predicate.** For this model,

```text
P_NG(e) = sgn(delta) in {+,-}.
```

Amplitude and absolute phase are not part of the counting type; orientation is.

`[ALG]` **Strict-equivalence test.** Two tokens with identical reduced transition `Delta^- -> Delta^+` after admissible relabeling/global-phase gauge are strictly equivalent.

`[ALG]` **Counting-but-not-strict test.** Example:

```text
e1 : 0.3 -> 0.8
e3 : 1.1 -> 1.6
```

Both have positive orientation and therefore `e1 ~_P e3`, while their retained relational transition amplitudes differ, so `e1 !~_str e3`.

`[ALG]` **Proper refinement.** On this model,

```text
~_str  subsetneq  ~_P.
```

`[ALG conditional on adopted spectator axiom]` **Disjoint spectator test.** For a component `C` disjoint from the causal interface and inert by definition,

```text
P_NG(N_e disjoint_union C) = P_NG(N_e).
```

This verifies the adopted spectator-independence admissibility condition on the minimal model; it does not prove boundary robustness for connected context.

`[ALG]` **Orientation retention.** If `delta>0` and `delta'<0`, then

```text
P_NG(e+) != P_NG(e-),
```

so `E+` and `E-` are distinct counting types.

**Verdict:** N-1A0 and N-1A1 are closed for the isolated abstract oriented dyadic phase-step. This is the first scoped concrete closure in Number Genesis. It does **not** establish that the same event type remains well-defined under connected boundary context; that is N-1A2.

---

##### N-1A2 — Boundary Locality / Context Robustness

**RID:** `NUMGEN-OPEN-N1A2`  
**Status:** CLOSED `[ALG]` `[scope: abstract three-node boundary-aware oriented phase-step; specified local law]`

**Question:** When the event support is embedded in a connected relational environment, what boundary information is sufficient to determine the local transition, and when are two varying boundaries admissibly equivalent for strict or counting-level event identity?

`[DEF]` **State partition.** Write a neighborhood state as

```text
X = (x_S, b, y),
```

where `x_S` is the internal support state, `b` is the boundary trace, and `y` is residual external state.

`[DEF]` **Sufficient causal interface.** A boundary trace `b` is sufficient on domain `U` when there exists a local transition map

```text
x_S^+ = F_S(x_S^-, b)
```

such that, for all `X=(x_S,b,y)` and `X'=(x_S,b,y')` in `U`,

```text
pi_S F(X) = pi_S F(X').
```

Thus the residual state `y` cannot silently alter the local transition once `(x_S,b)` is fixed.

`[DEF]` **Boundary interface object.** Represent the interface as

```text
B_e = (B_e, alpha_e, b_e),
```

where `B_e` is the finite relational boundary object, `alpha_e` is its attachment/port map into the support `S_e`, and `b_e` is the reduced boundary relational state.

`[DEF]` **Admissible strict boundary isomorphism.** A support/boundary pair `(phi,psi)` is admissible only if:

1. `alpha_2 o psi = phi o alpha_1` (attachment compatibility);
2. retained boundary state agrees modulo admitted gauge;
3. all relational closure/compatibility constraints are preserved;
4. `phi_* F_1(x,b) = F_2(phi_*x,psi_*b)` on the comparison domain (transition equivariance / commuting-interface criterion);
5. orientation is preserved for the primitive Number-Genesis counting policy.

`[DEF]` **Counting-level context compatibility.** Strict compatibility may fail while the event type remains stable when the realization changes but the counting predicate does not:

```text
P(F_1(x,b_1)) = P(F_2(phi_*x,b_2)).
```

This yields the causal hierarchy:

| Environment role | Criterion | Meaning |
|---|---|---|
| spectator | varying it leaves `(x_S,b)`, `F_S`, and `P` invariant | outside causal interface |
| boundary context | varying `b` changes `F_S`, but not `P` | realization changes; event type stable |
| causal participant | varying boundary data changes `P` | must be retained in event-type classification |

###### Scoped three-node model

`[DEF]` Use support `S={i,j}` and one connected node `k`, with

```text
x = Delta_ij,
beta = Delta_ik,
Delta_jk = beta - x.
```

The phase-closure identity therefore removes one redundant incident-edge coordinate **relative to the retained internal state `x`**. On the admissible boundary fiber at fixed `x`, `beta` is a single independent coordinate.

`[DEF]` **Abstract boundary-coupled transition law.** On a local phase chart chosen so that the signed increment does not cross the branch cut, take

```text
F_S(x,beta) = x + delta_0 + gamma beta,
delta_0 = 1,
gamma = 1,
P_NG = sgn(F_S(x,beta)-x) = sgn(1+beta).
```

This law is a test object only; it is not imported from the nonlinear RTG dyadic generator.

Take `x=0.4`.

`[ALG]` **Case A2-1 — strict boundary compatibility.** Let `beta_1=beta_2=0.5`, with event 2 differing only by an admissible orientation-preserving relabeling of support/boundary names.

```text
Delta_jk = 0.5 - 0.4 = 0.1,
F_S(0.4,0.5) = 1.9,
P_NG = +1.
```

The attachment diagram commutes by the chosen relabeling, retained boundary state agrees, closure maps to closure, transition equivariance is exact, and orientation is preserved. Hence `b_1 ~=_partial b_2` and the event tokens are strictly boundary-compatible.

`[ALG]` **Case A2-2 — context-dependent same type.** Let `beta_3=0.2`.

```text
Delta_jk = 0.2 - 0.4 = -0.2,
F_S(0.4,0.2) = 1.6,
P_NG = +1.
```

Because `beta_3` differs as a gauge-invariant retained boundary coordinate, it is not strictly compatible with `beta_1` under the fixed attachment/state convention. The transition amplitude changes (`1.5` versus `1.2`), but the counting type remains `+1`. Thus the connected node acts as boundary context.

`[ALG]` **Case A2-3 — causal/type-changing boundary.** Let `beta_4=-2.0`.

```text
Delta_jk = -2.0 - 0.4 = -2.4,
F_S(0.4,-2.0) = -0.6,
P_NG = -1.
```

The boundary has changed the counting type. It is therefore causally type-relevant and cannot be discarded from the event-type analysis.

###### Boundary minimality correction and theorem

`[COR]` **Closure does not by itself prove minimality.** The closure identity proves that, conditional on the retained internal state `x`, the admissible incident-edge boundary fiber has one independent degree of freedom. The map

```text
beta |-> (Delta_ik,Delta_jk) = (beta,beta-x)
```

is a coordinate isomorphism of that fiber, not a non-injective proper quotient. The previous “proper quotient by common shift” argument is rejected.

`[DEF]` **Minimal sufficient interface relative to a transition law.** A sufficient interface coordinate `beta` is minimal for `F_S` on domain `U` iff there is no non-injective relational map `q:beta->beta'` and reduced law `F'_S` such that

```text
F_S(x,beta) = F'_S(x,q(beta))
```

for all `(x,beta)` in `U`, apart from identifications already declared gauge.

`[ALG]` **Minimality for the scoped law.** For `F_S(x,beta)=x+1+beta`, suppose such a non-injective `q` exists. Then there are `beta_a != beta_b` with `q(beta_a)=q(beta_b)`. Factorization would imply

```text
F_S(x,beta_a) = F_S(x,beta_b),
```

but

```text
F_S(x,beta_a)-F_S(x,beta_b) = beta_a-beta_b != 0,
```

a contradiction. Hence no non-injective proper quotient remains sufficient. The one-dimensional interface is minimal **for this law and domain**.

**Verdict:** N-1A2 closes for the specified abstract three-node boundary-aware phase-step model. This closure demonstrates that the event type can survive connected environmental embedding while distinguishing strict compatibility, context dependence, and type-changing causal participation. It does not establish boundary robustness for arbitrary RTG dynamics.

---

##### N-1B — Repeatability and Successor Extensibility

**RID:** `NUMGEN-OPEN-N1B`  
**Status:** PARTIAL — N-1B-MIN CLOSED `[ALG]`; N-1B-GROWTH ACTIVE  
**Scope of closure:** abstract fixed-support oriented recurrence on `S^1`; no claim yet that full RTG dynamics physically retain all same-endpoint histories

**Question:** Once an event type `E` is boundary-robustly defined, what condition distinguishes a merely classifiable event from a physically repeatable and indefinitely extensible event type?

`[DEF]` **Why fixed support comes first.** The minimal successor test isolates “one more event of the same type” from changes of support, node count, birth, or topology. Network growth is a stronger downstream test because it asks whether the same counting type survives support/topology change as well as history extension.

`[DEF]` **History as a composable event path.** Let `G_E` be the directed event graph/category whose vertices are admissible local relational states and whose oriented edges are event tokens in counting class `E`. A realized `E`-history is a finite composable path using only `E`-edges. Path order is relational event order, not an external physical clock. Ordinary natural numbers may be used in the proof metalanguage to describe finite paths (SG metalanguage guard), but they are not part of the physical successor definition.

`[DEF]` **Native successor criterion.** Successor extensibility means:

```text
Every endpoint of every reachable finite E-path has at least one outgoing admissible E-edge.
```

Equivalently, the reachable `E`-generated event graph has no terminal vertex.

###### N-1B-MIN — Fixed-support oriented recurrence

`[DEF]` Take the instantaneous relational state space `V=S^1` and the total oriented recurrence

```text
R_d : S^1 -> S^1,
R_d(x) = x (+) d,
0 < d < pi,
```

where `(+)` is circle addition and the declared branch fixes positive orientation. Each transition token

```text
e_x : x -> R_d(x)
```

is assigned the same counting type `E+` by `P_NG(e_x)=+1`.

`[ALG]` **No-terminal-vertex theorem.** `R_d` is total on `S^1`. Hence every vertex `x` has the outgoing `E+` edge `x -> R_d(x)`. Therefore the reachable `E+` event graph has no terminal vertex. For any finite composable `E+` path with endpoint `x_*`, appending `x_* -> R_d(x_*)` produces another valid `E+` path. Successor extensibility is therefore established for this abstract fixed-support model.

`[ALG]` **Periodic-endpoint guard.** If `d=2pi p/q` with coprime integers `p,q`, then repeated application returns the instantaneous phase state after a finite cycle. Endpoint recurrence does not imply history identity. In the free path category, the non-empty closed path around the cycle is a distinct morphism from the identity/empty path at the same vertex; further copies of that loop remain composable. A collapse occurs only if an additional quotient explicitly identifies the loop with the identity.

`[DEF]` **Metalanguage correction.** Natural-number-valued path length may be used to audit the construction, but it is not the RTG-native reason histories differ. The native distinction is morphism/path identity: empty path, one traversal, and repeated closed traversals are distinct compositional histories unless a physical quotient identifies them.

`[HYP]` **State-versus-history consequence.** The abstract model demonstrates a mechanism by which a compact/recurrent instantaneous state space can support indefinitely extensible composable histories. The stronger claim that RTG physically realizes an unbounded counting structure requires N-1C plus a physical-history quotient that does not collapse distinct repetitions.

`[OPEN]` **Physical history-retention question.** The event-graph proof does not by itself establish that full RTG observables distinguish two paths having the same endpoint. N-1C must state the physical history equivalence/quotient explicitly. If the quotient collapses a nontrivial recurrence loop to the identity, the intended natural-number representation fails or changes.

`[OPEN]` **N-1B-GROWTH strengthening.** Test a topology-changing realization (birth/network growth). Required target: a history-preserving mapping showing that support changes do not destroy the counting class and that every finite growth history still admits a further `E`-type extension. This is a robustness test, not a prerequisite for opening N-1C.

**N-1B-MIN verdict:**

```text
CLOSED [ALG]
[scope: abstract fixed-support oriented recurrence R_d on S^1]
```

**Failure modes retained for stronger realizations:** event occurrence changes the boundary so the next edge leaves counting class `E`; finite resources/topological caps create terminal states; orientation constraints force a different event type; the law becomes partial on the reachable sector; or the physical history quotient collapses distinct event paths.

---

##### CLOSED N-1C — Free-History Monoid / Natural-Number Representation

**RID:** `NUMGEN-OPEN-N1C`  
**Status:** CLOSED locally `[RESULT][from: ALG]` `[scope: sufficiently small punctured primitive-dyad tube]`; general branching/nondeterministic/topology-changing history-quotient semantics remain OPEN

`[MATH]` Once one abstract event type `E` is fixed, the formal words

```text
H_E^form = {epsilon, E, E o E, E o E o E, ...}
```

with concatenation form the free monoid on one generator.

**RTG proof obligations:**

1. define the physical history quotient being represented;
2. prove concatenation is well-defined on that quotient;
3. prove associativity and null-history identity;
4. prove no additional physical relation collapses distinct formal powers `E^m` and `E^n` in the intended sector;
5. prove the universal property of the resulting one-generator history object;
6. only then state the representation/isomorphism with `(N,+,0)`.

`[MATH]` The free monoid on one distinguished generator is canonically isomorphic to `(N,+,0)` by sending `E` to `1`. In fact the additive monoid `(N,+,0)` has no nontrivial automorphism: a map sending `1` to `2` is not surjective and is therefore not an isomorphism.

`[HYP]` **Physical Number-Genesis interpretation.** If N-1A supplies a relationally admissible event type and N-1B supplies indefinite successor extensibility, then the physical repetition sector realizes arbitrarily long finite histories represented by natural numbers.

**Operational history equivalence candidate `[DEF candidate]`.** Let `h1,h2` be finite histories with compatible present relational interfaces. Define

```text
h1 ~=op h2
```

iff for every admissible future continuation/probe `c` and every gauge-invariant RTG relational observable `O` defined on the resulting future sector,

```text
O(h1 o c) = O(h2 o c).
```

This is a future-distinguishability criterion: past histories are physically different only if some admissible relational continuation can distinguish them. It does **not** assume that the universe stores the full past sequence as an observable record.

`[ALG structure]` **Congruence requirement and scoped resolution.** Future-distinguishability on arbitrary pointed paths is automatically continuation-compatible on the future side, but a free-monoid quotient needs a composition convention for both sides. For deterministic fixed-generator realizations, use the induced transformation monoid instead of quotienting arbitrary paths. Let `F_E` be the physical transformation associated with one occurrence of event type `E`. Define operational equivalence of powers extensionally on an invariant sector `U`: `F_E^r ~=op F_E^s` iff every admissible initial state in `U`, every admissible continuation, and every gauge-invariant relational observable gives the same result. This equivalence is a two-sided congruence under transformation composition whenever `U` and the admissible continuation class are composition-closed. A single state/observable witness separating two powers proves those powers are not equivalent.

`[FAIL]` `[scope: memoryless wrapped-S1 recurrence]` **Pure wrapped-state recurrence does not close N-1C.** If the complete physical state is only `x in S1`, the transition is Markovian `x -> R_d(x)`, and every allowed future observable depends only on the current wrapped state and its future wrapped orbit, then any two histories ending at the same `x` are operationally equivalent. In particular, for rational return loop `L:x->...->x`,

```text
L ~=op 1_x.
```

Hence successor extensibility alone does not yield a free physical history monoid.

`[RESULT] [from: ALG]` `[scope: local primitive dyad]` **History-separation criterion satisfied locally.** The exact primitive realization does not require a stored integer counter or lifted winding: L1 plus the six-phase `T`-invariant tube proves `T^r x != T^s x` for every admissible `x` and `r!=s`, so the present reduced relational state itself separates all finite primitive histories. The analogous criterion remains OPEN for branching, nondeterministic, or topology-changing histories.

`[GUARD]` **Additive-invariant certificate is sufficient, not necessary.** If an additive functional `I` is used to separate loop powers, its codomain must itself be non-collapsing for those values (for example torsion-free in the relevant sector). Merely stating `I(E) != 0` does not prove `I(L^r) != I(L^s)` in an arbitrary codomain, and defining `I` directly as an integer-valued event counter would be circular for N-1C.

`[FAIL]` `[scope: local N-1 tube as N-1C separator]` **Dyadic eta-winding is not the local counting memory.** N-3A subsequently proves the dynamically induced local `eta`-winding/deck map is trivial on a sufficiently small one-chart N-1 tube. Nontrivial winding remains an N-4/global representation question, not the mechanism closing local N-1C.

`[OPEN]` `[scope: general branching/topology-changing histories]` **Other memory sources.** Recurrence holonomy (NG-7B), boundary-context memory, birth/topology records, frame/connection variables, or OPEN-M spin/metric data may become necessary outside the deterministic local tube. Each requires its own non-collapse proof and does not affect the local N-1 closure.


###### N-1C-DYAD — Radial Memory Test

**RID:** `NUMGEN-N1C-DYAD-RADIAL`  
**Status:** CLOSED locally `[RESULT] [from: ALG] [scope: sufficiently small punctured p=6 primitive dyad sector]`. Primitive event-type/domain alignment is closed by the unified v0.9 six-phase `T`-tube construction; only general branching/topology-changing history semantics remain OPEN.

`[DEF]` **Scoped block transformation.** Let `F:=T^6` be the exact six-step finite iterate of the primitive dyad map

```text
T(rho,eta) = (rho-sin eta,
              eta + exp(rho)-1-sin eta)
```

with primitive radial observable

```text
Q_true = rho^2-rho*eta+eta^2.
```

The order-6 block is inherited from the certified dyadic resonance and is used only as a realization-level transformation. It is not a Number-Genesis derivation of the numeral six.

`[DEF]` **Physical memory.** A present-state quantity `m` is a physical memory relative to a reduced state projection `pi` when: (i) it is relationally defined and gauge-invariant; (ii) two histories may share the same reduced present state `pi(x)` while carrying different `m`; and (iii) the difference is itself observable or alters at least one admissible future relational observable. A full past trajectory need not be retained.

`[RESULT] [from: NUM] [scope: high-precision canonical-family witness]` **Same wrapped phase / different radial state.** Independent 120-digit bisection reproduces the nontrivial canonical-family root candidate

```text
q_* = 0.315625883659561602974267621967906111219946754...
```

with a sign-changing bracket `(0.31562,0.31563)` for `eta_6(q)-q`. At the high-precision root candidate,

```text
rho_6 = 0.0307238042627433867190601685564488191195569081...,
Q_0   = 0.0996196984358791160983187970418465600227462970...,
Q_6   = 0.0908664227144426977744415962653614974931240880...,
Q_6-Q_0 = -0.00875327572143641832387720077648506252962220892....
```

A scan on `(0.005,2.0]` with step `0.005` finds exactly one sign-change bracket. This is **uniqueness at the stated scan resolution**, not a global uniqueness theorem. Exact existence/location remains `[NUM]` until the accepted interval/Arb certificate is run.

`[RESULT] [from: ALG] [conditional on an exact return root]` **Exact witness identities and active memory.** If `eta_6=eta_0=q_*` exactly on the canonical family `rho_0=0`, then one-line primitive-map algebra gives

```text
Q_0 = q_*^2,
Q_6 = Q_0 + rho_6(rho_6-q_*),
Delta eta_future = exp(rho_6)-1,
Delta rho_future = rho_6.
```

Thus any exact return with `rho_6 != 0` is immediately future-distinguishable. For the numerical root candidate, `Delta eta_future ~= 0.03120065132664946991845... > 0`.

`[NUM] [scope: witness orbit, 3000 blocks]` **Finite-horizon non-collapse.** Independent exact-map iteration gives strict `Q_true` decrease for 3000 six-step blocks, with `Q_3000 ~= 3.3638522441887575e-4`, `3000*Q_3000 ~= 1.00916`, and no wrapped-eta excursion beyond the initial `q_*`. Hence `eta`-winding `ell=0` throughout the audited 18,000 primitive steps. This is numerical support only.

`[COR]` **F1 primitive/normal-frame correction.** The v0.7 line

```text
Q_NF = |W|^2 = Q_true  (exact)
```

is false in the primitive frame. The near-identity frame correction begins at relative order `O(sqrt(Q_true))`; consequently the primitive one-block radial remainder is `O(Q_true^(5/2))`, not `O(Q_true^3)`. The freeness conclusion survives and is now proved directly below from the primitive map.

###### L1 — Primitive-frame phase-uniform contraction

**RID:** `NUMGEN-RESULT-L1-PRIMITIVE-CONTRACTION`  

`[ALG]` Exact symbolic composition of the primitive map through quartic coordinate order reproduces the certified cubic six-step jet and gives

```text
Delta rho_4 = -(25 eta^4 - 48 eta^3 rho + 48 eta^2 rho^2
                - 32 eta rho^3 + 15 rho^4)/24,

Delta eta_4 = -(10 eta^4 - 20 eta^3 rho + 36 eta^2 rho^2
                - 20 eta rho^3 + 25 rho^4)/24.
```

Substituting into `Q_true(Fx)-Q_true(x)` yields the exact homogeneous radial identities

```text
Delta Q_4 = -Q_true^2,

Delta Q_5 = Q_true*(5 eta^3 - 43 eta^2 rho
                    + 4 eta rho^2 - 5 rho^3)/24.
```

Therefore

```text
Q_true(Fx)-Q_true(x)
  = -Q_true^2
    + Q_true*(5 eta^3 - 43 eta^2 rho + 4 eta rho^2 - 5 rho^3)/24
    + O(||(rho,eta)||^6).
```

Because the theorem is local, choose the neighborhood inside `|eta|<pi`; there `eta_wrap=eta`, so the primitive Taylor coordinate and the canonical wrapped `Q_true` coincide.

Use the exact anti-correlation coordinates

```text
U = sqrt(3) rho/2,
V = eta-rho/2,
Q_true = U^2+V^2,
U = sqrt(Q) cos(phi),
V = sqrt(Q) sin(phi).
```

The degree-5 correction becomes `Q^(5/2) A(phi)` with exact phase harmonic

```text
A(phi) = -sin(phi)/3
         -13 sin(3phi)/24
         -11 sqrt(3) cos(phi)/18
         +sqrt(3) cos(3phi)/8.
```

Hence, uniformly in phase,

```text
|A(phi)| <= C5 := 7/8 + 53 sqrt(3)/72 ~= 2.149981844460424.
```

Because the exact primitive map is analytic and the anti-correlation coordinate change is linear/invertible, the omitted degree-6-and-higher terms are uniformly `O(Q_true^3)`. Consequently

```text
boxed:  Q_true(Fx)-Q_true(x) = -Q_true^2 + O(Q_true^(5/2))
```

uniformly in phase as `Q_true -> 0`.

`[RESULT] [from: ALG]` **Strict contraction.** There exist `C>0` and `epsilon>0` such that for every state with `0<Q_true<epsilon`,

```text
|Q_true(Fx)-Q_true+Q_true^2| <= C Q_true^(5/2).
```

Shrinking `epsilon` so that `C sqrt(epsilon)<1/2` and `epsilon+C epsilon^(3/2)<1` gives

```text
0 < Q_true(Fx) < Q_true(x).
```

The punctured sector is therefore forward invariant under `F`, and

```text
Q(x) > Q(Fx) > Q(F^2x) > ...
```

for every admissible initial state in that sector.

`[RESULT] [from: ALG]` **Scoped block freeness / operational non-collapse.** Since `Q_true` is a gauge-invariant present-state observable, distinct finite powers satisfy

```text
F^r not ~=op F^s   for r != s.
```

Thus the local transformation submonoid generated by `F=T^6` has no finite relation between distinct powers. The previously conditional freeness statement is unconditional on this local sector; the exact-return witness is illustrative but not required for the theorem.

`[ALG]` **T-vs-F reduction lemma.** On any composition-closed `T`-invariant sector, if `T^r=T^s`, then raising both transformations to the sixth power gives `F^r=F^s`. Therefore block-level freeness implies primitive-step transformation freeness contrapositively. This is an algebraic transfer only; it does not by itself identify the old abstract sign-based N-1A event predicate with one application of `T`.


`[RESULT] [from: ALG]` **N-1 unified primitive-dyad alignment (v0.9).** Let `V_L1={x:0<Q_true(x)<epsilon_L1}` be a punctured L1 contraction neighborhood. Because each of the finitely many maps `T^j`, `j=0,...,5`, is continuous and fixes the origin, choose `0<delta<epsilon_L1` so that

```text
T^j(U) subset V_L1   for j=0,...,5,
U := {x:0<Q_true(x)<delta}.
```

L1 gives `F(U) subset U` for `F=T^6`. Define the six-phase tube

```text
U_T := U union T(U) union T^2(U) union ... union T^5(U).
```

Then `U_T subset V_L1` and `T(U_T) subset U_T`: for `j=0,...,4`, `T(T^j U)=T^(j+1)U`, while `T(T^5 U)=T^6(U)=F(U) subset U`. Thus the exact primitive generator restricts to an endomorphism

```text
T : U_T -> U_T,
```

and L1's strict `F`-contraction holds at every point of the tube, not only on the base phase.

`[DEF]` **Primitive counting type.** For each `x in U_T`, the event token is

```text
e_x : x -> T(x).
```

The scoped counting predicate is mechanism-level:

```text
P_T(e_x) = "one forward application of the exact primitive relational dyadic generator T".
```

The word *forward* means the orientation of the directed transition rule itself; it does not introduce an external time coordinate. Distinct amplitudes/phases may make tokens strictly inequivalent while all remain counting-equivalent under `P_T`. The opposite/reversed mechanism is not silently identified with this type.

`[RESULT] [from: ALG]` **N-1A on the tube.** Strict equivalence is inherited from the admissible fixed-support relational groupoid after gauge reduction; counting equivalence is equality under `P_T`. Both are equivalence relations, and the exact `T` rule is expressed entirely in the reduced relational dyadic variables. This is a fixed-support local closure; N-1A2 remains the separate connected-boundary robustness result.

`[RESULT] [from: ALG]` **N-1B on the tube.** Since `T(U_T) subset U_T`, every admissible state has one further `T`-edge. The primitive event graph on `U_T` has no terminal vertex, so successor extensibility holds for the same event type used in N-1A.

`[RESULT] [from: ALG]` **Orbit-level non-collapse and primitive-power freeness.** Since `U_T subset V_L1`, strict block contraction holds everywhere on the tube:

```text
0 < Q_true(Fx) < Q_true(x)   for every x in U_T.
```

Take any `x in U_T` and suppose two distinct finite primitive histories meet, `T^r x=T^s x` with `r<s`. Put `y=T^r x` and `d=s-r>0`. Then `T^d y=y`, hence

```text
F^d y = T^(6d)y = (T^d)^6 y = y.
```

But repeated L1 contraction gives `Q_true(F^d y)<Q_true(y)`, contradiction. Therefore

```text
T^r x != T^s x   for every x in U_T and every r != s.
```

Thus every primitive orbit in the tube is non-periodic and separates all finite repetition histories by the present reduced relational state itself. In particular the transformation powers are distinct. Let `M_T={id,T,T^2,...}` be the transformation monoid on `U_T`; then

```text
T^r != T^s   as endomorphisms whenever r != s.
```

This is stronger than the earlier T-vs-F transformation reduction: the orbit map `T^k -> T^k x` is injective for every admissible initial state `x` in the tube. No external event counter or stored full trajectory is needed.

`[RESULT] [from: ALG]` **Free-monogenic universal property.** `M_T` is generated by the distinguished element `T` and has no relation between distinct finite powers. Therefore for every monoid `M` and every chosen element `m in M`, there exists a unique monoid homomorphism

```text
Phi : M_T -> M,
Phi(T^k) = m^k.
```

Thus `M_T` is a free monoid on one distinguished generator. In the mathematical metalanguage, fixing the generator gives the canonical isomorphism

```text
M_T ~= (N,+,0),    T^k <-> k.
```

This is a **Track-A ordinal/event-history result only**. It does not identify dyadic recurrence multiplicity with TDR-G cardinal multiplicity, winding count, or any cross-branch dynamical quantity.

`[GUARD]` **Scope of N-1 closure.** The theorem is local and existential in the L1 radius: it proves a sufficiently small punctured primitive-dyad tube exists. It does not yet provide a maximal tube, a global all-amplitude theorem, topology-changing growth robustness, or the NG-8 “two fives” bridge.

`[GUARD]` **Distinguished generator, not uniqueness theorem.** The exact primitive dyadic map `T` is the distinguished update rule supplied by this realization, and N-1 uses one application of that rule as its counting generator. N-1 does not prove that `T` is the unique possible event decomposition, nor that no coarser generator such as `T^k` could define another valid counting convention. The theorem is: once this primitive generator is selected, its local repetition monoid is free.

`[RESULT] [from: ALG]` **N-1A strict/counting alignment made explicit.** For all `x,y in U_T`, the tokens `e_x:x->T(x)` and `e_y:y->T(y)` are counting-equivalent because `P_T(e_x)=P_T(e_y)`. They are strictly equivalent only when their reduced transition neighborhoods are related by an admissible N-1A groupoid isomorphism. Thus the primitive tube realizes exactly the strict-vs-counting distinction adopted in N-1A.

`[GUARD]` **Local existence, not optimized radius.** L1 and the tube argument prove existence of sufficiently small `epsilon_L1` and `delta`; they do not provide a maximal or interval-optimized admissible radius.

`[GUARD]` **Six-step block is realization-specific.** `F=T^6` enters because this dyadic realization has the certified order-6 elliptic resonance used by L1. The numeral six is not inferred to be ontologically privileged and is not a premise of the abstract Number Genesis programme.

`[GUARD]` **Realization, not universal derivation.** N-1 is a concrete local RTG realization of the free natural-number repetition monoid. It establishes viability of the relational-repetition thesis in one primitive dyadic sector; it does not prove uniqueness, globality, or that every RTG sector must generate arithmetic in the same way.

`[OPEN]` **General history-quotient semantics.** N-1C is closed here for a deterministic transformation-monoid realization. A general equivalence/quotient theory for branching, nondeterministic, or topology-changing histories remains open and is not required for this local result.


`[GUARD]` **No winding promotion.** What is verified numerically on the witness is no `eta`-winding (`ell=0`) over the audited horizon. The internal elliptic/normal-form angle still rotates. Radial memory therefore establishes independence from `eta`-winding, not “counting without any rotation.”

`[GUARD]` **Coefficient conflation.** `[COR v1.20]` Upstream provenance is now resolved (Dyadic v6.4.10 §6.5, §6.14, `[DEF]`: distinct objects, must not be conflated). Four typed objects share only the leading `-Q^2`: the primitive-frame law `-Q^2 + O(Q^(5/2))`; the positive-ray one-block burst `Q_6 = Q_0 - Q_0^2 - (5/24)Q_0^(5/2) + (37/40)Q_0^3 + O(Q_0^(7/2))`; the raw fixed-radius uniform-angle mean `A_raw(Q) = Q - Q^2 + (47/54)Q^3 + O(Q^4)` (an averaging operator, not a pointwise recurrence); and any normalized-chart observable or long-orbit backbone. Transfer between them requires an explicit representation/observable bridge.

**Artifacts:**
- `ng_n1c_dyad_radial_memory_v1.py` — original high-precision witness and 2000-block audit.
- independent audit supplied by collaborator — 120-digit bisection, 3000-block audit, phase sweep, F1 falsification.
- `ng_l1_primitive_contraction_cert_v1.py` — exact primitive-map symbolic L1 certificate; all assertions pass.
- `NG_L1_PRIMITIVE_CONTRACTION_CERT_v1.md` — human-readable theorem/proof certificate.

**N-1 closure verdict:** `[RESULT][from: ALG]` `[scope: sufficiently small punctured primitive-dyad tube]`. Event identity, successor extensibility, and operational non-collapse are aligned on the same exact primitive generator `T`, and the resulting transformation monoid is free on one distinguished generator. The canonical mathematical representation is `(N,+,0)`. N-1B-GROWTH remains a robustness extension, not a prerequisite to this local closure.

`[INTERP]` **Bounded state does not bound history.** The N-1 dyad gives an explicit counterexample to any inference “bounded amplitude => bounded repetition”: `Q_true` remains in a bounded local sector and contracts toward the fixed point while the primitive history admits arbitrarily long finite extensions. This sharpens the guard used by NG-10.

`[GUARD]` **Continuous-branch realization only.** The N-1/N-2 construction proven here belongs to the continuous primitive dyad. Finite TDR-G phase dynamics may require a different memory or counting realization; none is imported across the branch firewall.

---

### §6.3 N-2 closed signed-history construction

`[RESULT] [from: ALG] [scope: local primitive-dyad Track-A monoid]` Let `M_T` be the N-1 free monogenic monoid. Define oriented pair equivalence by

```text
(A,B) ~ (C,D)  iff  A o D = B o C.
```

Cancellativity makes this an equivalence relation; componentwise composition gives a well-defined abelian group law; `[A,B] -> [B,A]` is the group inverse; and `iota(A)=[A,id]` embeds `M_T` injectively. The class `g=[T,id]` has infinite order, so the completion is infinite cyclic. Only after construction is the coordinate map `Psi([T^m,T^n])=m-n` introduced, yielding the standard representation `G_T ~= (Z,+,0)`.

`[INTERP]` Signed history is oriented comparison between two forward repetition histories. The inverse class swaps comparison order and does not assert physical `T^{-1}` or reverse evolution.

#### CLOSED N-2 — Signed-history group completion

**RID:** `NUMGEN-OPEN-N2`  
**Status:** CLOSED `[RESULT][from: ALG]` `[scope: local primitive-dyad Track-A monoid]`

**Question:** How does signed integer structure arise without assuming literal physical time reversal?

Let `M_T` be the free monogenic transformation monoid closed in N-1. Because it is free on one generator, it is commutative and cancellative. No inverse map `T^{-1}` is assumed.

`[DEF]` **Oriented forward-history pair.** Form `M_T x M_T`. A pair `(A,B)` compares two forward histories with an orientation: first history relative to second history. Define

```text
(A,B) ~ (C,D)    iff    A o D = B o C.
```

`[RESULT] [from: ALG]` **Equivalence relation.** Reflexivity follows from commutativity; symmetry from equality symmetry; transitivity uses cancellativity: from `A o D=B o C` and `C o F=D o E`, multiply the first equality by `F`, substitute the second, and cancel the common `D` to obtain `A o F=B o E`.

`[RESULT] [from: ALG]` **Common-forward-extension invariance.** For every `K in M_T`,

```text
(A,B) ~ (A o K, B o K).
```

Thus comparative history excess is unchanged by appending the same forward continuation to both histories. This is the native difference principle; it invokes no reversed trajectory.

Define

```text
G_T := (M_T x M_T)/~,
[A,B] + [C,D] := [A o C, B o D].
```

The operation is well-defined. The identity is `[id,id]`; the inverse is

```text
-[A,B] = [B,A].
```

Hence `G_T` is an abelian group. The inverse operation reverses the **orientation of the comparison pair**; it is not a physical application of `T^{-1}`.

`[RESULT] [from: ALG]` **Injective forward-history embedding.** The canonical map

```text
iota : M_T -> G_T,
iota(A) = [A,id]
```

is a monoid homomorphism. If `iota(A)=iota(B)`, the pair relation gives `A=B`; hence `iota` is injective. N-1 unsigned histories therefore enter the signed-history object without collapse.

`[RESULT] [from: ALG]` **Infinite cyclic completion.** Let `g=[T,id]`. Every pair class is generated by `g` and its comparison inverse `-g=[id,T]`. If a nonzero finite multiple of `g` were the identity, then `[T^k,id]=[id,id]` for some positive finite `k`, forcing `T^k=id`, contrary to N-1 freeness. Thus `G_T` is infinite cyclic.

Only after the physical pair construction is complete introduce the standard metalanguage coordinate

```text
Psi([T^m,T^n]) = m-n.
```

N-1 freeness makes `Psi` well-defined and bijective, and pairwise composition maps to addition. Therefore

```text
G_T ~= (Z,+,0).
```

`[RESULT] [from: ALG]` **Grothendieck universal property.** For every abelian group `G` and monoid homomorphism `f:M_T->G`, there is a unique group homomorphism `f_tilde:G_T->G` with `f_tilde([A,B])=f(A)-f(B)` and `f_tilde o iota=f`. Therefore `(G_T,iota)` is exactly the Grothendieck group completion of the N-1 monoid.

`[INTERP]` **RTG signed-history reading.** Positive/negative orientation records comparative excess between two forward relational histories. Swapping `[A,B]` to `[B,A]` reverses the comparison convention, not the microscopic dynamics. N-2 therefore does not require physical invertibility, reverse time evolution, or an external clock.

`[GUARD]` **N-2 scope.** This is a Track-A local signed-history comparison group derived from the N-1 primitive-dyad monoid. It does not yet identify signed history with dyadic winding, circle characters, TDR-G cardinal/multiplicity counting, or a globally valid RTG integer observable. Those are N-3/NG-8 bridge questions.

**Certificate:** `NG_N2_SIGNED_HISTORY_COMPLETION_CERT_v1.md`.

---

### §6.3a N-2-ORD physical order representation — CLOSED at v1.6

`[DEF]` **Reachability-first order.** For admissible `y, z` in the tube,
```text
y <=_T z   iff   there exists K in M_T with z = K(y).
```
Order is defined by existence of a connecting certified history, not by any numerical observable. `Q_true` enters only as a witness (ORD-4).

`[RESULT] [from: ALG] [scope: local primitive-dyad tube U_T]` **ORD-1 — reachability order.** `<=_T` is reflexive (`id`), transitive (composition), and antisymmetric on `U_T`, and is **total on each primitive orbit**. Antisymmetry is exactly N-1 non-collision: `z=T^k y` and `y=T^l z` give `T^(k+l) y = y`, hence `k=l=0`. Globally `<=_T` is a **partial** order; totality is orbit-local.

`[RESULT] [from: ALG]` **ORD-2 — shift covariance.** `y <_T z` implies `T^r y <_T T^r z` for every `r`; strictness follows from non-collision at the shifted point. `[COR v1.20]` The **reflection** direction (`T^r y <_T T^r z ⟹ y <_T z`) requires P3 injectivity; P3 is closed `[ALG]` on the shrunken tube (v1.19) and on the explicit Dyadic-certified tube (v1.20), so reflection is `[RESULT] [from: ALG]` at that scope. The former `[NUM-audited]` tag here contradicted the v1.19 P3 closure and is withdrawn.

`[RESULT] [from: ALG]` **ORD-3 — ordered signed-history group.** With `P := iota(M_T) ⊆ G_T`: `P+P ⊆ P`, `P ∩ (−P) = {0}`, `G_T = P ∪ (−P)`. Hence `a <=_G b iff b − a ∈ P` is a translation-invariant total order on the infinite cyclic signed-history group.

`[RESULT] [from: ALG]` **T4 — physical sign realization.** For `[A,B] ∈ G_T` and any admissible `x`, exactly one of `A(x)=B(x)`, `B(x) <_T A(x)`, `A(x) <_T B(x)` holds, matching `[A,B] = 0`, `> 0`, `< 0`. The verdict is constant on each N-2 equivalence class and independent of the base point (both endpoints lie on the common orbit `O_x`). The sign of a signed history is therefore **the orientation of forward reachability between its realized endpoints**, not merely the metalanguage integer `m−n`.

`[RESULT] [from: ALG] [scope: full certified local tube U_T]` **ORD-4 — `Q_true` order witness.** For every residue `j = 0..5`, put `y=T^j x`. Since `U_T` is `T`-invariant, `y in U_T`; L1 therefore gives `Q_true(Fy)<Q_true(y)` for `F=T^6`, and iteration yields
```text
r < s  =>  Q_true(T^(6s+j) x) < Q_true(T^(6r+j) x).
```
Hence `Q_true` is strictly antitone and therefore **order-reflecting** on each fixed-residue `F`-chain: reachability order on that chain is equivalent to reversed `Q_true` order. The dps=60 executable reproduces all six chains numerically, but the theorem status comes from the exact L1 result, not from sampling.

`[RESULT] [from: ALG] [v1.19]` **P3 — injectivity of `T` on a sufficiently shrunken tube.** N-1 non-collision alone does not imply injectivity across distinct orbits, but a direct derivative bound does. Let
```text
A = DT(0) = [[1,-1],[1,0]].
```
On the convex box `|rho|,|eta| <= 1/10`,
```text
DT-A = [[0, 1-cos eta], [exp(rho)-1, 1-cos eta]],
||DT-A||_2^2 <= ||DT-A||_F^2 <= 1/81 + 1/20000 < 1/4,
sigma_min(A) = (sqrt(5)-1)/2 > 1/2.
```
Integrating the derivative remainder along the segment from `x` to `y` gives
```text
||T(x)-T(y)|| >= (sigma_min(A) - sup||DT-A||_2) ||x-y|| > 0.
```
Thus `T` is injective on this box. Because the N-1 tube is existential and may be shrunk while retaining the local closure, choose the certified tube inside the box. On that shrunken tube, the ORD-2 reflection direction and the cross-orbit refinement are `[ALG]`: two primitive orbits are disjoint or one contains a tail of the other, and cross-orbit comparability holds exactly when the orbits merge. `[GUARD]` This is not an explicit maximal-radius or numerical-seed inclusion certificate.

`[GUARD]` **Non-claims and provenance.** (i) No external physical time: the order is defined by existence of a connecting history; indices are metalanguage (SG-NG-1). (ii) **No per-primitive-step `Q_true` monotonicity** — the executable supplies genuine numerical counterexamples: sampled single steps split 192 decreases vs 168 non-decreases, and `Q_true(T^3 x) < Q_true(T^2 x)` fails on at least one admissible seed. (iii) No total order between non-merging orbits is a structural consequence of the reachability definition; the executable's NC-3 line is bookkeeping, not independent computational evidence.

`[GUARD]` `Q_true` is a witness and may never be inverted into the definition of order; `Q_true` ownership remains Dyadic. N-2-ORD orders one certified stream and therefore cannot supply a second recurrence or touch N-5A/SG-NG-20.

#### CLOSED N-2-ORD — Physical order representation

**RID:** `NUMGEN-OPEN-N2-ORDER`  
**Status:** CLOSED at v1.6 `[RESULT][from: ALG]` `[scope: local primitive-dyad Track-A tube/orbits]`

The former OPEN target has been discharged by `NG_N2ORD_PHYSICAL_ORDER_CERT_v1.md`. The canonical theorem statement, guards, P3-dependent refinements, and `Q_true` witness are maintained in this §6.3a ledger block.

`[RESULT] [from: ALG]` The physical order is reachability-first, not `Q_true`-defined. Reachability is a partial order on `U_T`, total on each primitive orbit; the N-2 positive cone gives the ordered signed-history group; signed-history sign is physically realized by endpoint reachability orientation.

`[GUARD]` Primitive-step/cross-residue monotonicity is false in general; the numerical certificate supplies explicit counterexamples. `[v1.19]` P3 injectivity is now discharged algebraically on a sufficiently shrunken tube, so the ORD-2 reflection/cross-orbit merge refinements are theorem-level on that shrunken scope.


---

### §6.4 N-3 representation layer — closed local/abstract results

`[RESULT] [from: ALG]` **N-3A:** the natural lifted primitive dynamics has zero deck index on a sufficiently small forward-invariant one-chart tube, so the induced `eta`-winding homomorphism `G_T -> Deck` is trivial and maximally non-faithful.

`[RESULT] [from: THM]` **N-3B:** the already-constructed infinite cyclic history group admits the faithful abstract generator-to-generator isomorphism `G_T ~= widehat(S^1)`.

`[RESULT] [from: ALG]` **N-3C:** the actual primitive pullback of a phase character is

```text
T^* chi_m = exp(i m(exp(rho)-1)) exp(-i m sin eta) chi_m,
```

so primitive dynamics is not a constant translation of harmonic labels. Fourier expansion of the sinusoidal factor mixes character sectors.

`[RESULT] [from: THM]` **N-3D:** restriction to the finite subgroup `C_N` yields the quotient `G_T/(N G_T) ~= widehat(C_N) ~= Z_N`.

`[GUARD]` **Cross-branch representation/dynamics boundary.** For TDR-G this is admissible only as a representation bridge; all dynamical transfer remains forbidden.

`[INTERP]` Track-A history, local eta-winding, and harmonic representation are now explicitly separated: local eta-winding is dynamically trivial, while the character representation is faithful only at the abstract algebraic level.

#### CLOSED N-3A — Local deck inducibility / eta-winding

**RID:** `NUMGEN-N3A-DECK-TRIVIAL`

`[RESULT] [from: ALG]` **Natural lifted primitive map.** On

```text
M_tilde = R x R,
p(rho,eta_tilde) = (rho, eta_tilde mod 2pi),
```

the natural lift is

```text
T_tilde(rho,eta_tilde)
 = (rho - sin eta_tilde,
    eta_tilde + exp(rho)-1 - sin eta_tilde).
```

Deck translations `tau_k(rho,eta_tilde)=(rho,eta_tilde+2pi k)` commute exactly with `T_tilde`.

`[RESULT] [from: ALG]` **One-chart shrinking theorem.** Starting from the L1/N-1 base sector, continuity of the finitely many lifted iterates `T_tilde^j`, `j=0,...,6`, allows one further radius shrink so that the lifted six-phase tube lies inside `|eta_tilde|<pi/2`, projection is injective on the tube, and the lifted tube is forward invariant.

`[RESULT] [from: ALG]` **Local winding triviality.** Every finite primitive orbit remains in the same deck sheet. Hence the actual deck cocycle of every `T^r` is zero, the induced monoid winding map is trivial, and its Grothendieck extension satisfies

```text
rho_wind : G_T -> Deck(M_tilde/M),
rho_wind(h) = tau_0  for all h,
ker rho_wind = G_T.
```

`[INTERP]` Track-A signed history and physical local `eta`-winding are not the same realization. The radial-memory mechanism can distinguish arbitrarily long finite histories while the local `eta` deck index remains zero.

`[GUARD]` This is not a theorem about every bounded orbit or bounded six-cycle. It is a local theorem on the sufficiently small one-chart N-1 tube. Abstract nontrivial isomorphisms `G_T ~= Deck ~= Z` remain available by pure algebra but are not dynamically induced here.

---

#### CLOSED N-3B — Abstract circle-character representation

**RID:** `NUMGEN-N3B-CHAR-ISO`
**Status:** CLOSED `[THM]` `[scope: abstract representation of the local Track-A group]`
Depends on: N-2. The proof uses the standard theorem `widehat(S^1) ~= Z`.

Let

```text
widehat(S^1) = {chi_k : k in Z},
chi_k(z)=z^k,
```

under pointwise multiplication. With `g=[T,id]` the N-2 generator, define

```text
rho_char(g^k)=chi_k.
```

`[THM]` This is the unique group homomorphism sending `g` to `chi_1`; it is surjective and has trivial kernel. Thus

```text
G_T ~= widehat(S^1).
```

`[GUARD]` This is a faithful **abstract** representation. It does not state that one physical `T` update increments a harmonic label or that the primitive dyadic Koopman action equals this generator-to-generator isomorphism.

---

#### CLOSED N-3C — Primitive dynamical character activity (first exact result)

**RID:** `NUMGEN-N3C-PULLBACK`
**Status:** CLOSED at structural level `[RESULT][from: ALG]`; detailed resonance-sector decomposition remains OPEN

For `chi_m(eta)=exp(i m eta)`, the exact pullback is

```text
T^* chi_m(rho,eta)
 = exp(i m (exp(rho)-1))
   exp(-i m sin eta)
   chi_m(eta).
```

`[RESULT] [from: ALG]` For every `m != 0`, this is not `chi_(m+c)` for any fixed integer `c` on an open dyadic domain, because the pullback has nontrivial `rho` dependence while a pure circle character does not.

Using the standard Jacobi-Anger expansion,

```text
exp(-i m sin eta)
 = sum_n J_n(-m) chi_n(eta),
```

so

```text
T^* chi_m
 = exp(i m (exp(rho)-1))
   sum_n J_n(-m) chi_(m+n)(eta).
```

`[RESULT] [from: ALG]` Primitive `T` therefore mixes phase-character sectors with `rho`-dependent amplitudes rather than translating the harmonic index by a fixed history unit.

`[OPEN]` **N-3C+ / OPEN-9 connection.** Determine how this exact pullback reorganizes under the order-6 resonant block and whether roots-of-unity projectors give a useful character-sector proof of the dyadic p-resonance missing-slot/cancellation rules.

---

#### CLOSED N-3D — Finite-character quotient / representation bridge

**RID:** `NUMGEN-N3D-FINITE-CHAR`
**Status:** CLOSED as pure representation theory `[THM]`; discrete dynamical realization remains OPEN

For any `N>=1`, let

```text
C_N = {exp(2pi i j/N) : j=0,...,N-1} subset S^1.
```

Restriction of characters gives

```text
res_N : widehat(S^1) -> widehat(C_N),
res_N(chi_k)=psi_[k]_N.
```

`[THM]` `[scope: pure finite-character representation theory]` The restriction is surjective with kernel `{chi_(qN):q in Z}`. Composing with N-3B gives

```text
rho_N := res_N o rho_char : G_T -> widehat(C_N),
rho_N(g^k)=psi_[k]_N,
ker rho_N = N G_T,
G_T/(N G_T) ~= widehat(C_N) ~= Z_N.
```

For the TDR-G bridge application, `N` is the already-specified even phase size of the discrete branch.
Depends on: N-3B.

`[GUARD]` This is a representation-theoretic quotient only. It transfers no continuous primitive map, coefficient, threshold, normal-form datum, observable, or dynamical law into TDR-G; it does not assert that the continuous dyad is a continuum limit of the discrete theory or that the discrete theory dynamically realizes the Track-A history generator.

`[INTERP]` Finite phase distinguishability identifies abstract character labels modulo `N`; it does not identify Track-A repetition, Track-B cardinality, and Track-C cyclic count. NG-8 remains OPEN.

**Certificate:** `NG_N3_REPRESENTATION_LAYER_CERT_v1.md`.

---

#### CLOSED N-3C+ — Roots-of-unity projectors / OPEN-9 kinematic boundary

**Status:** CLOSED at representation-kinematic level `[ALG]` `[assuming: ord(lambda)=p]` `[scope: formal complex vector-map monomials]`; the formerly OPEN `q=4,(0,3)` nonlinear cascade item is CLOSED-by-import from the Dyadic owner (pointer to the separate `DYAD-THM-Q403-PHASELAW` import; not graded here); universal missing-slot/reachable-basis work remains an Arithmetic-Dynamics interface target, not an NG foundational OPEN.

Let `R(Z)=lambda Z`, with **`ord(lambda)=p`** (hence `lambda^p=1`), and let the cyclic action on a complex vector-map component be conjugation
\[
\mathcal C_R h := R^{-1}\circ h\circ R.
\]
For `M_ab=Z^a bar(Z)^b`,
\[
\mathcal C_R M_{ab}=\lambda^{a-b-1}M_{ab}.
\]
Hence the vector charge is
\[
\boxed{\chi_p(a,b)=a-b-1\pmod p.}
\]
The residue projectors
\[
\Pi_r=\frac1p\sum_{j=0}^{p-1}\lambda^{-jr}\mathcal C_R^j
\]
satisfy
\[
\Pi_rM_{ab}=\delta_{\chi_p(a,b),r}M_{ab}.
\]
In particular,
\[
\boxed{\Pi_0M_{ab}\neq0\iff a-b\equiv1\pmod p.}
\]
This is the exact representation-theoretic origin of the one-step p-resonance condition. `[COR v1.19]` The exact-order hypothesis is load-bearing: `lambda^p=1` alone is insufficient (for example `lambda=1` makes the conjugation action trivial). The output-vector `-1` charge is essential; the rule must not be derived from a scalar `rho^a chi_b` projector.

`[RESULT][from: ALG]` **First-nonlinear cyclic-average theorem.** If `f=R+h_d+O(d+1)` with `h_d` the lowest nonlinear homogeneous degree, then
\[
[f^p-id]_d=pR^{-1}\Pi_0h_d.
\]
Therefore nonresonant slots at the first nonlinear degree vanish before any cascade algebra is needed. For the primitive dyad, the first nonlinearity is quadratic and the `p=6` degree-2 resonant support is empty, so
\[
\boxed{[T^6-id]_2=0}
\]
is a pure kinematic cancellation.

`[RESULT][from: ALG]` **p=6 support audit.** Solving `a+b=D` and `a-b==1 mod 6` gives: degree 2 none; degree 3 `(2,1)`; degree 4 none; degree 5 `(3,2)` and `(0,5)`. For a pure anti-holomorphic channel `(0,b)`, the first one-step resonant support is `(0,p-1)`.

`[RESULT][from: ALG structure]` **Reachable-charge rule.** The rotation conjugation is an automorphism of the multilinear/Lie operations used in normal-form algebra. Cascade charges therefore add modulo `p`. Absence of a charge-reachable source combination forces a zero; existence of such a combination only permits the channel and does not determine its coefficient.

`[RESULT][from: existing ALG + projector theorem]` **OPEN-9 boundary witness.** For subgroup order `q=4`, target `(0,3)` has charge `0-3-1=-4 == 0 mod 4`, so the q=4 projector permits this channel for both `p=8` and `p=12`. The Dyadic OPEN-9 ledger records exact cancellation for `p=8,q=4,(0,3)` but exact survival `-13+15 sqrt(3)/2 != 0` for `p=12,q=4,(0,3)`. Therefore the p=8/p=12 split is not representation selection; it is genuine nonlinear/cyclotomic cascade algebra.

`[RESULT] [from: THM]` `[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.11 | DYAD-THM-Q403-PHASELAW]` **All-`p` cascade closure imported.** On `p=4s`, `s>=2`, the Dyadic owner gives the exact subgroup-strobe coefficient

```text
Q(L,I) = L^5 (I L^2 + I - L^2 + 1) / (2 (L+1)^4 (L^2+L+1)),
I = zeta_p^(p/4),
Q_p = i zeta_p^3 M_p,   M_p in Q(zeta_p)^+,
```

with `p=8` the exact zero degeneracy and nonzero survival for the later family as certified by the owner theorem. Number Genesis imports only the closure needed to retire its stale item; ownership of the nonlinear/cyclotomic theorem remains Dyadic.

`[ALG]` **Scalar Bessel-residue projector (separate object).** From N-3C,
\[
P_r^{sc}(T^*\chi_m)=e^{im(e^\rho-1)}\sum_{\ell\in\mathbb Z}J_{r-m+\ell p}(-m)\chi_{r+\ell p}.
\]
For `p=6,r=1,m=1`, the first sidebands are `J_{+/-6}(-1) ~= 2.0938338e-5`. These are primitive Fourier-mixing coefficients, **not** OPEN-9 Birkhoff/Lie cascade coefficients. No identification is allowed without an explicit coordinate/jet bridge.

`[GUARD]` **Representation/dynamics boundary.** Character covariance determines allowed residues and impossible charge routes. It does not determine coefficient values or cancellations among multiple allowed routes. In particular, it does not by itself prove the universal low-degree raw anti-holomorphic vanishing pattern or the OPEN-9 missing-slot multiplicities.

### §6.5 N-4 global/nonlocal extension target

`[RESULT] [from: ALG]` The local exact primitive realization is already complete at N-1/N-2, while N-3A proves that its dynamically induced `eta`-winding map is trivial on the one-chart tube.

`[OPEN]` N-4 now asks what survives on larger exact-map invariant domains where genuine `eta`-winding, critical-curve effects, or other recurrence structures may occur. Any nontrivial winding representation must be derived there rather than imported from the abstract isomorphism `G_T ~= Z`.

`[GUARD]` Six-step block count, internal elliptic rotation, lifted eta-winding, and signed history remain distinct objects unless an explicit map is proved.

#### OPEN N-4 — Global/nonlocal dyadic history representations

**RID:** `NUMGEN-OPEN-N4`  
**Status:** OPEN — local primitive realization is already supplied by N-1/N-2/N-3

**Question:** How far beyond the sufficiently small one-chart primitive tube do the Track-A repetition and signed-history representations remain valid, and what new kernels/obstructions appear when larger-amplitude phase winding, critical curves, or nonlocal recurrence sectors are admitted?

**Certified local input:**

```text
T(rho,eta) = (rho - sin eta, eta + exp(rho)-1 - sin eta)
N-1: local free primitive repetition monoid
N-2: local signed-history completion
N-3A: local eta-winding map trivial
N-3B/C: abstract character representation vs primitive harmonic mixing
```

**Required:** Extend or falsify the local results on larger invariant domains using the exact primitive map. Normal-form maps may support interpretation but cannot replace primitive certification.

**Guard:** The special role of `p=6` is realization-specific; no global history/winding theorem follows from the local order-6 sector alone.

---

### §6.6 N-5A / N-5 rational recurrence target

`[RESULT] [from: ALG]` **N-5A CLOSED locally.** Track A is the primitive `T` stream; Track B/S1 is the canonical positive phase-coincidence crossing stream. It is independently event-typed, indefinitely repeatable, co-realized on the same local orbit/tube, ordered by N-2-ORD reachability, and not any fixed blocking `T^m`.

`[RESULT] [from: ALG]` **Bounded synchronization commensurability structure CLOSED.** On a common-order prefix poset, the integer defect
```text
Delta_(p:q)=q N_A-p N_B
```
is relationally defined (C1), invariant in boundedness under finite prefix-origin changes (C2), invariant under positive common rescaling `(p,q)->(kp,kq)` (C3), and has a unique reduced positive class for indefinitely repeatable streams (C4). Prefix-cofinal repeatability supplies directed unbounded event count without external metric time (SG-NG-25).

`[RESULT] [from: ALG]` **C5 controls CLOSED.** The abstract periodic language `A^6 B A^7 B` realizes a bounded synthetic `13:2` class; the neighboring `A^6 B A^8 B` fails linearly. This validates the discrimination power of the definition.

`[GUARD]` **Synthetic control ≠ physical witness.** The C5 controls do not constitute a physical RTG witness.

`[RESULT] [from: ALG]` **C6 canonical falsifier CLOSED.** The original canonical primitive/section pair is density-resonant at `6` but boundedly commensurate at no positive rational pair because the `6:1` residual grows logarithmically and every off-resonant candidate grows linearly.

`[RESULT] [from: ALG]` **N5-PHYS-1 CLOSED.** The positive and negative phase-coincidence branches `B_+`,`B_-` are physically distinct event predicates and strictly alternate on a sufficiently small tube, giving
```text
|N_(B_+)-N_(B_-)| <= 1.
```
Thus the first genuine physical bounded class is `1:1`.

`[RESULT] [from: ALG]` **C7A bounded rational-label theorem CLOSED.** Every certified bounded physical pair has a unique positive-rational invariant `rho_Q`; `1 in Q_RTG^bd`.

`[GUARD]` **Bounded realization ≠ dynamic admission.** Bounded realization and dynamic admission are distinct.

`[RESULT] [from: ALG]` **C7B-DISC-1 CLOSED.** Frozen DISC-1B PASS and DISC-1D PASS-INT establish `2,3 in Q_RTG^dyn subseteq Q_RTG^bd`.

`[RESULT] [from: ALG]` **C7B-DISC-2 CLOSED.** Frozen B-check PASS and D-check PASS on the registered supplementary family establish eight additional labels and add further witnesses for `2` and `3`. The currently established dynamic lower bound is therefore

```text
{1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4} subseteq Q_RTG^dyn.
```

`[POSTHOC-DIAG] [v1.19]` DISC-2 antipodal-endpoint audit marks 40/136 witness records `CONVENTION-EXPOSED`, with 96 unexposed. Every admitted label retains at least one unexposed witness, so the ten-label existential lower bound is unchanged. Discrete-owner policy action is pending; DISC-1 requires the same audit.

`[OPEN]` **C7B global breadth.** Determine which additional positive rationals occur; no exhaustiveness theorem is claimed.

`[DEF]` **C7C-WD ADOPTED.** The well-definedness framework (WD-PHYS/CLOSE/DOM/VAL/DESCENT, arithmetic compatibility WD-REP only afterward) is adopted.

`[RESULT] [from: ALG]` **C7C-0 CLOSED.** The orientation swap descends to a representative-independent involution on bounded classes, so `Q_RTG^bd` is closed under `r -> r^(-1)`.

`[GUARD]` No `Q_RTG^dyn` reciprocal closure is claimed.

`[RESULT] [from: ALG]` **C7C-M partially resolved (v1.20; C7C-M2 Census-1 INCONCLUSIVE / INCONCLUSIVE at v1.20.7):** M-1A exact chain identity and M-1B conditional carrier closure on `D_chain` are CLOSED `[ALG]`; unrestricted WD-CLOSE and naive label-only WD-DOM FAIL; WD-VAL on admitted chains PASS; associativity only for admitted bracketings. `[OPEN]` full-interface typed WD-DOM (the frontier), admissibility transfer, carrier identity/inverse, physical commutativity; C7C-A not opened; M-4 HOLD (P2).

`[GUARD]` N-5 therefore has a certified physical rational-label mechanism but is **not yet a derivation of the full field `Q`**. Full realization spectrum and arithmetic remain explicit open obligations.

#### CLOSED N-5A — Second co-realized recurrence / event stream

**RID:** `NUMGEN-OPEN-N5A`  
**Status:** CLOSED locally at v1.11 `[RESULT][from: ALG]` `[scope: sufficiently small certified primitive-dyad tube]` — prerequisite discharged for N-5

**Question:** Can the Number Genesis realization supply **two independently certified repeatable event types or recurrence streams** that coexist in one physical sector and are comparable under one RTG-native causal/order relation, without importing an external clock or a pre-existing real-valued frequency?

**Why this prerequisite is necessary.** Ratios formed only from powers of the single certified generator `T` are standard localization/re-indexing of the already-constructed free monoid. They do not by themselves constitute a physical genesis of rational magnitude.

**Required closure package:**

1. certify event predicates/streams `A` and `B` independently by N-1A/N-1B-style criteria;
2. prove they are co-realized on a common admissible physical domain;
3. declare and certify one relational event-order/interleaving rule that compares their occurrences without an external clock;
4. prove the comparison does not collapse to a relabeling of one generator;
5. only then open a commensurability quotient for N-5.

**Candidate routes:**

- N-4/global exact-dyad extension where a second nondegenerate recurrence/section-crossing structure becomes available;
- a second explicitly declared event predicate on the continuous branch with its own repeatability proof;
- a cross-stream realization only behind the relevant programme/realization bridge and firewall guards.

`[GUARD]` See SG-NG-20. A pair `(T^m,T^n)` generated solely by one certified event type does not close N-5A.

---

#### OPEN N-5 — Bounded synchronization commensurability / realized Q-like labels

**RID:** `NUMGEN-OPEN-N5`  
**Active architecture RID:** `NUMGEN-OPEN-N5-COMM-BD`  
**Status:** ACTIVE `[OPEN]` — C1–C4, C5-SYN-13, C6, N5-PHYS-1 and C7A CLOSED; C7B-DISC-1 and C7B-DISC-2 CLOSED with ten established dynamic labels; C7B global breadth and full C7C arithmetic remain OPEN; C7C-WD adopted; C7C-0 CLOSED (`Q_RTG^bd` reciprocal-closed); C7C-M next; N-4 parallel

**Question:** Can rational magnitude be represented by equivalence classes of **physically bounded synchronization discrepancy** between two independently certified, co-realized event streams, rather than by a primitive scalar ratio or limiting density?

##### N5-C1 — relational definability — CLOSED

`[RESULT] [from: ALG]` Let `P` be the directed set/poset of finite admissible common-order prefixes under extension. For certified event predicates `A,B`, define
```text
N_A(H) := number of A-events in H,
N_B(H) := number of B-events in H.
```
The counts are finite relational event multiplicities on the certified common order; they are not metric durations.

For positive metalanguage integers `p,q`, define
```text
Delta_(p:q)(H) := q N_A(H) - p N_B(H).
```
This uses only declared event predicates, finite counting, and the certified common-order prefix relation. No external clock, real-valued frequency, phase velocity, or continuum ratio is introduced.

`[DEF]` **Bounded synchronization commensurability.**
```text
A ~_comm^(p:q) B
```
iff there exists a finite constant `C` such that
```text
|Delta_(p:q)(H)| <= C
```
for all sufficiently long admissible common-order prefixes in the declared comparison sector. The physical object is the bounded synchronization relation; the rational label is downstream representation.

##### Prefix-cofinal indefinite repeatability

`[DEF]` A certified stream `B` is **prefix-cofinally indefinitely repeatable** on a common-order comparison sector iff
```text
forall H in P, exists H' >= H containing at least one further B-event.
```
By finite iteration, for every finite `r` and every prefix `H`, some extension contains at least `r` additional B-events. Since `N_B` is monotone (non-decreasing) under prefix extension, `N_B` is cofinal/unbounded on the prefix poset.

`[GUARD]` This is successor extensibility through arbitrarily long **finite** relational histories. It does not assume a completed infinite trajectory.

##### N5-C2 — finite-origin/prefix invariance — CLOSED

`[RESULT] [from: ALG]` For a fixed finite initial prefix `H_0` and any extension decomposed as `H=H_0 o H_>0`,
```text
N_A(H)=N_A(H_0)+N_A(H_>0),
N_B(H)=N_B(H_0)+N_B(H_>0),
```
hence
```text
Delta_(p:q)(H_>0)
 = Delta_(p:q)(H) - Delta_(p:q)(H_0).
```
The origin change is therefore an additive constant. Bounded/unbounded synchronization status is invariant under finite origin shifts **within the same comparison sector**, equivalently on an extension cone/cofinal tail for which deleting `H_0` does not select a different branch. `[COR v1.19]` Branch selection in a genuinely branching prefix structure is not an origin shift and is not covered by C2.

##### N5-C3 — positive integer rescaling invariance — CLOSED

`[RESULT] [from: ALG]` For every positive integer `k`,
```text
Delta_(kp:kq)(H)=k Delta_(p:q)(H).
```
Therefore
```text
Delta_(p:q)=O(1) iff Delta_(kp:kq)=O(1).
```
The bounded physical relation depends on the proportion, not on a chosen common integer multiple.

##### N5-C4 — uniqueness of reduced positive class — CLOSED

`[RESULT] [from: ALG]` Suppose the same indefinitely repeatable pair is bounded for two positive pairs `(p,q)` and `(p',q')`:
```text
|q N_A-p N_B| <= C,
|q' N_A-p' N_B| <= C'.
```
Eliminating `N_A` gives
```text
|(q p' - q' p) N_B(H)| <= q' C + q C'.
```
Set `d=q p'-q' p in Z`. If `d != 0`, then `|d|>=1`; prefix-cofinal unboundedness supplies an admissible prefix with
```text
N_B(H) > q' C + q C',
```
contradicting the bound. Hence
```text
q p' - q' p = 0,
p q' = p' q.
```
Thus every boundedly commensurate indefinitely repeatable pair carries a **unique reduced positive integer proportion**.

##### N5-C5 — control package — CLOSED at mathematical-control level

`[RESULT] [from: ALG]` **One-stream reblocking zero-control.** If `B=T^m` is merely a derived blocking of one Track-A stream, then at primitive prefix length `n` the `m:1` defect is `Delta_(m:1)(n)=n-m floor(n/m)`, hence `0 <= Delta < m`; it vanishes at complete block endpoints and is uniformly bounded on arbitrary primitive prefixes. `[COR v1.19]` The prior wording "vanishes identically" was too strong. SG-NG-20 remains decisive: this is a control only and cannot substitute for two independently certified event types.

`[DEF]` **C5-SYN-13 synthetic control language.** Define the finite period
```text
W_(13:2) := A^6 B A^7 B
```
and let `P_(13:2)` contain exactly the finite prefixes of `W^m` for finite `m>=1`.

`[RESULT] [from: ALG]` **C5-SYN-13 positive synthetic control.** On this language,
```text
N_A(W)=13,
N_B(W)=2,
Delta_(13:2)(W)=0.
```
For any admissible prefix `H=W^m R`, complete-period contributions cancel:
```text
Delta_(13:2)(H)=Delta_(13:2)(R).
```
The one-period defect sequence at event boundaries is
```text
0,2,4,6,8,10,12,-1,1,3,5,7,9,11,13,0,
```
so
```text
|Delta_(13:2)(H)| <= 13
```
for every synthetic admissible prefix. `gcd(13,2)=1`, and C3/C4 identify `13:2` as the unique reduced synthetic class.
Depends on: the C5-SYN-13 DEF, N5-C3, N5-C4.

`[RESULT] [from: ALG]` **Nearby negative control.**
```text
W_fail := A^6 B A^8 B
```
has 14 A-events and 2 B-events per period, hence
```text
Delta_(13:2)(W_fail^m)=2m -> infinity.
```
The boundedness criterion is therefore discriminating rather than automatic for periodic words.

`[GUARD]` C5-SYN-13 is an abstract two-symbol common-order language. It proves mathematical non-emptiness of the criterion and a noninteger reduced class; it is **not** an RTG physical realization and places `13/2` in neither `Q_RTG^bd` nor `Q_RTG^dyn`.

##### N5-C6 — canonical A/B falsifier — CLOSED

`[RESULT] [from: ALG]` Certificate: `NG_N5C6_CANONICAL_PAIR_FALSIFIER_v1.md` + executable audit. For the admissible canonical prefixes `H_M`,
```text
N_A(H_M)=6M,
N_B(H_M)=M-(tau/(2pi)) log M+O(1),
```
so
```text
Delta_(p:q)(H_M)
=(6q-p)M+(p tau/(2pi))log M+O(1).
```
If `p != 6q`, the defect is linearly unbounded. If `p=6q`,
```text
Delta_(6q:q)(H_M)
=(3q tau/pi)log M+O(1) -> +infinity.
```
Therefore
```text
forall p,q>0:
A !~_comm^(p:q) B
```
for the canonical primitive/canonical-section pair under the bounded-defect definition, even though
```text
N_A/N_B -> 6.
```

`[RESULT] [from: ALG]` **Density-resonance separation.**
```text
rational limiting density 6
does not imply
bounded physical commensurability 6:1.
```
This is the theorem-level canonical witness behind SG-NG-24.

`[GUARD]` C6 needs no C2 premise to falsify a class: uniform boundedness over all sufficiently long admissible prefixes is defeated by one admissible cofinal/subsequence family with unbounded defect.

##### N5-PHYS-1 — opposite phase-coincidence lock — CLOSED

`[DEF]` On the same sufficiently small certified continuous-dyad tube, define two phase-coincidence event predicates:
```text
B_+ : eta_wrap=0 crossing with rho>0,
B_- : eta_wrap=0 crossing with rho<0.
```

`[RESULT] [from: ALG]` **Physical distinction / gauge audit.** The sign of the relational radial observable `rho` distinguishes the two event predicates. A half-turn in the derived angular coordinate does not constitute an admissible gauge identification of the two transition neighborhoods. Thus `B_+` and `B_-` are two physically distinct relational event predicates, not two names for one gauge orbit.

`[RESULT] [from: ALG]` **Strict alternation.** L-MONO gives, after local shrinking,
```text
0 < delta_T = pi/3 + O(Q^(1/2)) < pi/2.
```
The two coincidence rays are separated by `pi`. The strictly increasing lifted phase therefore cannot cross both rays in one primitive transition and cannot cross the same ray twice without crossing the opposite ray between them. Their event order strictly alternates up to the finite choice of the first branch:
```text
B_+, B_-, B_+, B_-, ...
```

`[RESULT] [from: ALG]` **Prefix-cofinal repeatability.** The closed phase-growth law
```text
phi_hat_(6M)=2pi M-D_M+phi_hat_0,
D_M=o(M),
```
implies the increasing lift is unbounded above on arbitrarily long finite prefix extensions. Both opposite rays are therefore crossed prefix-cofinally often without introducing metric time.

`[RESULT] [from: ALG]` **Physical bounded class.** Strict alternation implies for every admissible common-order prefix
```text
|N_(B_+)(H)-N_(B_-)(H)| <= 1.
```
Hence
```text
B_+ ~_comm^(1:1) B_-.
```
This is the first genuine RTG positive realization of N-5-COMM-BD.

##### N5-C7A — bounded realized rational-label theorem — CLOSED

`[COR] [scope: v1.15 spectrum notation]` v1.15 used `Q_RTG^real` for every physically realized bounded rational label. v1.16 separates bounded realization from strong dynamic admission so boundedness is not silently promoted to genesis-grade dynamics. If the legacy symbol `Q_RTG^real` is retained in historical material, it is not to be silently repointed. In current live statements prefer `Q_RTG^bd` and `Q_RTG^dyn` explicitly.

`[DEF]` **Bounded and dynamically admitted spectra.**
```text
Q_RTG^bd :=
{ p/q in Q_(>0) :
  exists a certified physical pair (A,B)
  with Delta_(p:q)(H)=O(1) }.

Q_RTG^dyn :=
{ r in Q_RTG^bd :
  exists at least one certified realization of r
  passing the frozen same-realization stability+contingency discrimination gate }.
```

`[DEF]` **Rational-label representation map.** For every certified bounded physical pair define
```text
rho_Q(A,B) := p/q,
```
where `(p,q)` is any positive pair with bounded synchronization defect.

`[RESULT] [from: ALG]` C2 makes boundedness independent of finite origin convention; C3 identifies positive common rescalings; C4 proves any two admissible labels satisfy `p q'=p' q`. Therefore `rho_Q` is a well-defined **unique positive-rational invariant** of every certified bounded physical pair.
Depends on: N5-C2, N5-C3, N5-C4, and the rational-label representation map DEF.

`[RESULT] [from: ALG]` From N5-PHYS-1,
```text
rho_Q(B_+,B_-)=1,
1 in Q_RTG^bd.
```
Depends on: the preceding well-definedness result and N5-PHYS-1.

`[GUARD]` This witness is bounded and is a positive control; it is not itself a dynamic realization. `1 in Q_RTG^dyn` is established **separately** by C7B-DISC-2 (26 witnesses) and must not be conflated with this bounded control.

`[GUARD]` This is a directional representation theorem:
```text
certified physical bounded pair -> unique positive-rational invariant.
```
It does **not** prove that two physically different pairs carrying the same rational invariant are physically identical. Any quotient of physical realizations by equality of `rho_Q` must be explicitly declared.

##### N5-C7B — physical realization breadth / dynamic discrimination — OPEN globally

`[OPEN]` Determine the breadth of `Q_RTG^bd` and `Q_RTG^dyn`; in particular, no current theorem establishes either spectrum to equal all `Q_(>0)`.

`[ALG]` `[scope: exact exhaustive verification on the registered finite DISC-1 panel under the frozen C7B protocol]` `[conv: pinned TDR-G v18 signed_centered boundary and declared SWAP/P3 event semantics]` **C7B-DISC-1 CLOSED — DISC-1B PASS · DISC-1D PASS-INT — finite certificate.** The frozen `N=24` TDR-G retrigger-entry panel used the same 3456 raw seeds at `k in {0,1,2,3}`. The reproduced core was one-step identical to owner `genesis_mode_b_mc_v18.py` over all `24^4=331776` reduced states for each `k` (0 mismatches), and all 22 passing seeds were independently recounted through the owner counters (0 mismatches).

Base `k=1` census:
```text
3253 / 3456 dual-active;
all 3253 carry non-1 reduced classes.
```

Frozen dynamic discrimination:
```text
64   survive the k=1 -> k=2 stability fence,
22   pass by interior k=3 contingency,
0    pass by boundary-only k=0 contingency.
```
All 22 are `DISC-1D-PASS-INT`. Their admitted classes are
```text
2:1 x 12,
3:1 x 10,
```
Evidence: owner transition `genesis_mode_b_mc_v18.py` and sealed harness `disc1_analysis_harness_v1.py` (hashes in §9.2 and the DISC-1 freeze manifest). Post-hoc robustness record (v1.20.6; not an admission result): P2 antipodal-endpoint exposure — 0/22 witnesses exposed; label projection `{2:1, 3:1}` unchanged under the tested reverse and inert alternative policies.

`[RESULT] [from: ALG]` **C7B-DISC-1 breadth (DISC-1B PASS).** Thus the original non-`1` falsifier does not fire and bounded physical breadth extends beyond the N5-PHYS-1 `1:1` control.
Depends on: the DISC-1 finite certificate (base census), the `Q_RTG^bd` DEF, C7B-ALG-T2, C7B-ALG-T3.

`[RESULT] [from: ALG]` **C7B-DISC-1 dynamic admission (DISC-1D PASS-INT).** From the admitted classes,
```text
2 in Q_RTG^dyn,
3 in Q_RTG^dyn,
{2,3} subseteq Q_RTG^dyn,
Q_RTG^dyn != empty.
```
Depends on: the DISC-1 finite certificate (discrimination verdicts), the `Q_RTG^dyn` DEF, C7B-ALG-T4.
`[ALG]` `[scope: exact exhaustive verification on the registered finite DISC-2 panel under the frozen C7B protocol]` `[conv: pinned TDR-G v18 signed_centered boundary and declared SWAP/P3 event semantics]` **C7B-DISC-2 CLOSED — B-check PASS · D-check PASS — finite certificate.** Protocol `NG_C7B_DISC2_PREREG_v1.md` (frozen `db87b455...919da9`) applied the already-certified `k`-axis (`K={0,1,2,3}`, `k_0=1`, `K_stab={2}`, `K_cont={0,3}`, same-realization guard, sealed harness `57a15421...`) to the **fresh owner-registered supplementary one-pass family** `|d|_c=3,4,5`, 10368 seeds, whose trajectories had never been inspected. Reported through legacy harness keys `disc1b`/`disc1d`; DISC-1 was not rerun. `[REPRO] [v1.18; P2 provenance qualified at v1.19]` Reproduction contract for both DISC campaigns (full hash manifest in `NG_C7B_DISC2_RESULT_v1.md`; owner-side reproduction gap recorded in `NG_TO_TDRG_REPRODUCIBILITY_GAP_v2.md`): owner source `genesis_mode_b_mc_v18.py` pinned at `9d787b43...675e`; the load-bearing unstated convention was `signed_centered` returning the representative in `(-N/2, N/2]` (differs from `[-N/2, N/2)` only at the antipode `N/2`); the IC-stage sign pairing is `d_AB^IC = -d` (post-swap member of the dyad cycle) — the wrong sign reproduces the exact IC cardinalities with the wrong IC set; cycle detection in the gauge-reduced 4-tuple `(Delta_AB, Delta_AC, d_AB, d_AC)` (a derived no-birth symmetry, not SG-2 gauge); the enumerator's transition core was certified one-step identical to v18 on `(next state, dn_swap, dn_P3)` over all `24^4` reduced states at every `k` before either panel was inspected.

```text
base dual-active 7468 / 10368 ; non-1 base classes 7336        -> B-check PASS
survive k=1->2 stability fence 208
certified witnesses 136 = 130 PASS_INT + 6 PASS_BDY_ONLY       -> D-check PASS
A1 owner recount 544/544 exact ; A2 fixed-old-class defect certificates (C7B-ALG-T4) 136/136 ; A3 domain 136/136
```

Admitted classes (witness counts): `1:1` 26, `2:1` 4, `3:1` 28, `3:2` 12, `4:1` 14, `4:3` 14, `5:1` 6, `5:2` 10, `7:2` 6, `9:4` 16.
Evidence: owner transition, sealed harness, owner recount and certificates as recorded above and in §9.2. Robustness record: P2 antipodal-endpoint exposure — 40/136 witnesses convention-exposed, 96 unexposed, every admitted label with at least one unexposed witness; label set unchanged under the tested reverse and inert alternative policies.

`[RESULT] [from: ALG]` **C7B-DISC-2 breadth (B-check PASS).** On the registered supplementary panel, 7336 of the 7468 dual-active base seeds carry non-`1` reduced bounded classes.
Depends on: the DISC-2 finite certificate (base census), the `Q_RTG^bd` DEF, C7B-ALG-T2, C7B-ALG-T3.

`[RESULT] [from: ALG]` **C7B-DISC-2 dynamic admission (D-check PASS).** From the admitted classes,

```text
{1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4} subseteq Q_RTG^dyn.
```
Depends on: the DISC-2 finite certificate (discrimination verdicts), the `Q_RTG^dyn` DEF, C7B-ALG-T4.

`[RESULT] [from: ALG]` **`1 in Q_RTG^dyn`.** Established independently of the N5-PHYS-1 bounded control by 26 dynamically discriminating SWAP/P3 realizations (24 interior, 2 boundary). `1 in Q_RTG^bd` and `1 in Q_RTG^dyn` are **separate** statements of different epistemic status; the label-neutrality ruling makes the second admissible, since membership is existential through a certified realization and not a property of the numeral.

`[COR]` **`k=0` retention was load-bearing.** All six `PASS_BDY_ONLY` witnesses hold the base class at `k=1,2,3` and break it only at `k=0` — two transport patterns, `5:2 -> 2:1 -> 2:1 -> 2:1` (x4, `C_0=2`) and `11:1 -> 1:1 -> 1:1 -> 1:1` (x2, `C_0=30`). **All 6/6 disappear if `k=0` is removed**; an earlier "four of six" statement is retracted (four is only the `2:1` block). The architectural ruling to retain `k=0` was made when DISC-1 had produced zero boundary passes, i.e. against the then-available empirical signal.

`[GUARD]` Concentration statistics (mirror-symmetric `8,26,34,34,26,8` over signed `d`; `42,52,42` over `D_AB`) are **descriptive only**. They bear on realization robustness, never on existential membership, and are not an admission condition, independence test or mechanism theorem.

`[POSTHOC-DIAG] [v1.19]` **P2 antipodal-endpoint presentation-covariance exposure.** The external review identified a specification-level degeneracy in the TDR-G two-defect path orientation rule: under the owner convention `signed_centered in (-N/2,N/2]`, when the phase-gradient tie has `S=0` and the endpoint advance difference is antipodal (`|E|=N/2=12`), reversing the endpoint listing gives the same positive tie-break value. The v18 implementation is deterministic because it sorts endpoint node IDs, but that convention is not itself node-relabeling covariant. Post-hoc audit `disc2_p2_antipodal_exposure_audit_v1.py` (exit 0) gives:

```text
40 / 136 ratified DISC-2 witnesses touch the antipodal condition at some k in {0,1,2,3};
96 / 136 never touch it;
216 antipodal events occur inside the audited eventual cycles;
reverse-at-antipode changes 10 witness verdict/class records;
inert-at-antipode changes 20 witness verdict/class records.
```

The **label projection is robust** under the tested diagnostic policies: the admitted ten-label set is unchanged, and every admitted label has at least one witness that never touches the condition. Unexposed/exposed counts by original class are `1:1 10/16`, `2:1 4/0`, `3:1 28/0`, `3:2 6/6`, `4:1 14/0`, `4:3 2/12`, `5:1 6/0`, `5:2 4/6`, `7:2 6/0`, `9:4 16/0`. Therefore the ratified existential lower bound remains

```text
{1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4} subseteq Q_RTG^dyn.
```

`[GUARD]` This is **post-hoc provenance diagnosis**, not a retroactive admission gate and not a policy replacement. The 40 affected witness records are annotated `CONVENTION-EXPOSED`; the original frozen protocol/verdict archive remains intact. A Discrete-Genesis owner ruling on the antipodal endpoint policy (or a presentation-independent path-selection theorem) is required before future campaigns. DISC-1 requires the same audit separately.

The ten labels are the **currently established** dynamic labels only; the existential criterion does not imply `Q_RTG^dyn subseteq` that set, nor `Q_RTG^dyn = Q_(>0)`.

At event-count transport level the 22 passing seeds reduce to two class-level archetypes:
```text
2:1 : (18,9) -> (16,8) -> (84,120)   x12,
3:1 : (18,6) -> (12,4) -> (120,72)   x10.
```
The `k=3` class changes give `C7B-ALG-T4` coefficients `84-2(120)=-156` and `120-3(72)=-96`, so the old classes lose boundedness linearly. By `C7B-ALG-T1` this also excludes a **deformation-invariant** SG-NG-26 common-source multiplicity factorization for the passing realizations; allowing multiplicities to vary with `k` is only `C7B-ALG-T2` periodicity triviality and is not a rescue of the guard.

`[DEF] [v1.18]` The legacy DISC lemma names `T1–T4` are namespaced as **`C7B-ALG-T1..T4`** to avoid collision with N-2-ORD `T4` (physical sign realization). Write `red(u,v) := (u/g, v/g)` with `g = gcd(u,v)` for the reduced class represented by raw counts `(u,v)`.

`[RESULT] [from: ALG]` **C7B transport lemmas** (identity certificate `ng_n5_discrimination_identity_cert_v5.py`, exit 0; interpretation in `NG_N5_DISCRIMINATION_CRITERION_v6_2.md`). `[COR v1.18.1]` raw multiplicities and reduced classes are now distinguished; the v1.18 wording called unreduced multiplicities "reduced".
- **`C7B-ALG-T1` (common-source multiplicity).** With `N_A = m_A L + O(1)`, `N_B = m_B L + O(1)` and `L` prefix-cofinally unbounded, `q N_A - p N_B = (q m_A - p m_B) L + O(1)` is bounded **iff** `q m_A = p m_B`: the unique reduced class is forced to `red(m_A, m_B)` independently of the dynamics generating `L`.
- **`C7B-ALG-T2` (periodicity triviality).** For an exactly periodic co-realized word with raw counts `a` A-events and `b` B-events per period, `b N_A - a N_B = b r_A - a r_B`; the period count cancels identically, so every exactly periodic dual-active pair is boundedly commensurate at `red(a,b)`. Periodic boundedness alone is not dynamic evidence.
- **`C7B-ALG-T3` (finite-state eventual-cycle classification).** On a closed finite invariant sector, every orbit is eventually periodic; a dual-active eventual cycle with raw per-cycle counts `a,b>0` realizes exactly one reduced bounded class `red(a,b)`, and every `p:q != red(a,b)` diverges linearly as `(qa-pb)m + O(1)`.
- **`C7B-ALG-T4` (class change ⟺ loss of boundedness).** Let the base cycle have raw counts `(A,B)`, `g = gcd(A,B)`, `(p,q) = red(A,B)`. For deformed raw counts `(A',B')`, the **old reduced class** `p:q` evaluated on the deformed cycle has defect `(q A' - p B') m + O(1) = ((B A' - A B')/g) m + O(1)`, nonzero iff `red(A,B) != red(A',B')`. The **normalized coefficient** `q A' - p B'` is what the DISC certificates report: for DISC-1 the base raw counts `(18,9)` and `(18,6)` give raw cross-determinants `-1404 = 9·(-156)` and `-576 = 6·(-96)`, while the reduced classes `2:1` and `3:1` give the reported `-156` and `-96`. Class change under deformation and linear loss of boundedness of the fixed original class are therefore equivalent; this is the strong bounded-to-unbounded contingency form used by the DISC gates.

`[GUARD]` The frozen gate is label-neutral and same-realization. The positive result does not establish rational arithmetic, does not exhaust either spectrum, and does not allow post-data retuning of deformation axes or thresholds. Further breadth requires a new pre-registration.

##### N5-C7C — physical rational arithmetic — OPEN (C7C-WD ADOPTED; C7C-0 CLOSED)

`[DEF] [v1.18]` **C7C-WD carriers and obligations** (`NG_C7C_WD_C7C0_DESIGN_v1.md`). Let
```text
R_pair := { certified co-realized ordered physical pairs (A,B; domain, order, provenance)
            satisfying the event-stream, common-order and prefix-cofinal repeatability requirements }
R_bd   := { x in R_pair : x boundedly commensurate at its reduced class }  subseteq  R_pair
rho_Q  : R_bd -> Q_RTG^bd ;      x ==_Q x'  :<=>  rho_Q(x) = rho_Q(x')
```
`==_Q` is **representation equivalence, not physical identity** (equal labels do not identify realizations). A candidate physical operation carries a typed signature `Phi_{tau1,tau2}^{tau3} : R_{tau1} x R_{tau2} -> R_{tau3}` (partial), where `tau` records the load-bearing physical interface; coherence across `tau` is a separate transport theorem, never assumed. Obligations, in order: **WD-PHYS** (constructed from certified relational objects; may not inspect labels), **WD-CLOSE** (outputs are again certified bounded realizations, not metalanguage rationals), **WD-DOM** (admissibility descends through `==_Q`, or `Phi` is typed to a class-saturated sector), **WD-VAL** (equivalent representatives give equivalent outputs when composed), **WD-DESCENT** (only after DOM+VAL: `[x]_Q Phi-bar [y]_Q := [Phi(x,y)]_Q`). **WD-REP** — any formula `rho_Q(Phi(x,y)) = F(rho_Q(x), rho_Q(y))` is a *derived representation theorem*; `F` may not define `Phi`.

`[RESULT] [from: ALG] [v1.18]` **C7C-0 CLOSED — reciprocal.** (`NG_C7C0_RECIPROCAL_CERT_v2.md`.) For `x=(A,B) in R_bd` define `S(A,B):=(B,A)`. Orientation swap leaves the certified streams, domain, co-realization, common-order sector, prefix-cofinal repeatability and provenance unchanged, so `Sx in R_pair` (WD-PHYS; **no boundedness claim at this step**). With `x` at reduced class `p:q`, exactly `Delta^{Sx}_{q:p}(H) = p N_B(H) - q N_A(H) = -Delta^x_{p:q}(H)`, so boundedness is preserved and **only here** `Sx in R_bd`, i.e. `S : R_bd -> R_bd` (WD-CLOSE). `S^2 = id`. By C7A uniqueness `rho_Q(Sx) = q/p = rho_Q(x)^(-1)`. WD-DOM is **trivial for this total unary map** because `D_S = R_bd` — not because `S` is unary; a partial unary operation could still have representative-dependent admissibility. This is precisely why `S` was the correct first test: it isolates WD-VAL and does not exercise the load-bearing binary obligation. WD-VAL and WD-DESCENT follow; `S` descends to an involution `S-bar` on `R_bd/==_Q` represented by `r -> r^(-1)`. **Hence `r in Q_RTG^bd  =>  r^(-1) in Q_RTG^bd`.** `[GUARD]` **No `Q_RTG^dyn` reciprocal-closure theorem is claimed:** that requires `A <-> B` equivariance of the same-realization stability+contingency gate, which `S` does not address. Apart from the self-reciprocal label `1`, the established dynamic spectrum contains no distinct reciprocal partners. `[COR]` v1 of the certificate let `R_bd` membership of `Sx` be concluded at the carrier-preservation step, before the sign identity had decided boundedness; repaired in v2 by the `R_pair`/`R_bd` split.

##### N5-C7C-M — chain composition: partially resolved (v1.20)

`[RESULT] [from: ALG]` **M-1A — exact chain identity. CLOSED.** For `x=(A,B)` at class `p:q` and `y=(B,C)` at class `u:v` with `Delta^{AB}_{p:q} = q N_A - p N_B`, `Delta^{BC}_{u:v} = v N_B - u N_C`, identically
```text
Delta^{AC}_{pu:qv} = v Delta^{AB}_{p:q} + p Delta^{BC}_{u:v}.
```
Pure algebra; no data. The product label `pu/qv` **emerges** (WD-REP), never defines the operation.

`[DEF]` **Chain domain.** `D_chain = { ((A,B),(B,C)) : (A,B),(B,C) in R_bd; the three streams share one certified comparison context — the same triple comparison prefix domain, or a certified cofinal transport between the two comparison prefix domains; (A,C) in R_pair }`. The middle-interface condition is **not** symbolic equality of the letter `B`: M-1A combines two bounded defects linearly on a common `H`, so `N_A, N_B, N_C` must be meaningful in one comparison context. The last condition is pre-bounded physical admissibility, **not** boundedness.

`[RESULT] [from: ALG]` **M-1B — conditional carrier closure. CLOSED.** On `D_chain`, M-1A gives `(A,C) in R_bd` at `red(pu,qv)` and `rho_Q(A,C) = rho_Q(A,B) rho_Q(B,C)`.

`[DEF]` **Transported chain data (C7C-M2 instrument; preregistration `NG_C7C_M2_PREREG_DRAFT_v4`, `248f128c…8987`).** For `x = (A,B)` at `p:q` and `y = (B′,C)` at `u:v` whose middle interfaces are aligned by a cofinal order-preserving tail map `φ` between their comparison prefix posets, with single-stream discrepancy `ε_B(H) := N_{B′}(φH) − N_B(H)` bounded on the tail, define `Δ^{AC,φ}_{pu:qv}(H) := q v N_A(H) − p u N_C(φH)`.

`[RESULT] [from: ALG]` **M2-1 — transported chain identity. CLOSED (algebra only).**
```text
Delta^{AC,phi}_{pu:qv}(H) = v Delta^{AB}_{p:q}(H) + p Delta^{B'C}_{u:v}(phi H) - p v eps_B(H)
```
Hence bounded input defects and bounded `ε_B` give a bounded transported outer defect; at `B′ = B`, `φ = id`, `ε_B = 0` this is exactly M-1A. Proved in the frozen preregistration before any case was examined; symbolically verified.

`[GUARD]` **M2-1 no-closure.** M2-1 is algebra only. It does **not** establish Π (outer `R_pair` admissibility of the transported pair), WD-DOM, carrier closure, or the existence of any admitted chain. A transport map aligns comparison contexts; it does not create co-realization. The instrument lemmas M2-0 (germ calculus) and M2-2 (value descent under WD-DOM) remain internal to the preregistration and are not owner claims.

`[RESULT] [from: ALG]` **Unrestricted WD-CLOSE: FAIL on the current carrier.** For any `x=(A,B) in R_bd`, C7C-0 gives `Sx=(B,A) in R_bd`, but the chain output `x ∘ Sx = (A,A)` is not two independent event types (SG-NG-20) and is not in `R_pair`. This is a closure counterexample, not merely an inverse-law remark.

`[RESULT] [from: ALG]` **Naive/global label-only WD-DOM: FAIL for `D_chain`.** The label-quotiented shared-middle domain is not saturated under `==_Q`: `rho_Q` carries no shared-interface provenance, equivalent representatives may be drawn from disjoint realization families (the label `1` already is), and composability changes. **This does not rule out a richer interface-typed saturated carrier; that is exactly the remaining OPEN.**

`[RESULT] [from: ALG]` **WD-VAL on admitted chains: PASS.** Equivalent admitted inputs yield equivalent outputs, by M-1A/M-1B.

`[RESULT] [from: ALG] [scope: admitted bracketings only]` **Associativity, partial.** If both bracketings of `((A,B),(B,C),(C,D))` are admitted, both produce the endpoint pair `(A,D)`. **Admissibility transfer** (one bracketing admitted ⇒ the other admitted) is **not** established.

`[OPEN]` **Identity / inverse.** Not available on the current chain carrier: the literal unit `(B,B)` and the literal inverse composite `(A,A)` both fail carrier closure. The C7C-0 reciprocal *label* theorem stands; what fails is its realization as a group inverse on this carrier. An enriched carrier is OPEN.

`[OPEN]` **Physical commutativity.** The representation-level product commutes, but domain swap-equivariance of the physical operation is not established.

`[OPEN]` **Full-interface typed WD-DOM — the frontier.** Which relational interface information carries physical composition, and under which quotient it descends without loss. **Live state (v1.20.7):** the C7C-M2 instrument is frozen and Census-1 has been executed, with outcome INCONCLUSIVE / INCONCLUSIVE because no admitted nondegenerate composable source chain exists in Census-1 evidence. Full-interface typed WD-DOM **remains OPEN**.

`[RESULT] [from: ALG]` `[scope: frozen C7C-M2 instrument; Census-1 admissible evidence, 120 records]` **C7C-M2 Census-1 — no admitted source chain at either level.** At level a, `≈_a` is the identity on the admissible set and every candidate middle chain is `x ∘ Sx`, with outer pair `(A,A) ∉ R_pair` (L1994). At level b, every dyad candidate's outer pair is the same stream, a re-indexing of it, or two streams on distinct orbits that are not co-realized. TDR-G contributes no candidate chain at either level, because every admissible record is oriented `(SWAP, P3)`. Hence the admitted-chain domain is empty at both levels.

`[GUARD]` **C7C-M2 Census-1 is not a WD-DOM verdict.** By the frozen preregistration, an empty admitted-chain domain makes WD-DOM vacuous: neither PASS nor FAIL. Level a: INCONCLUSIVE (vacuous); level b: INCONCLUSIVE (vacuous at N2; N1 is satisfied by the continuous-dyad analytic witness). Reading-matrix placement: INCONCLUSIVE / INCONCLUSIVE. Nothing here states that WD-DOM holds or fails.

**Missing evidence object (queue).** A certified nondegenerate composable three-stream configuration — `(A,B) ∈ R_bd`, `(B,C) ∈ R_bd`, `(A,C) ∈ R_pair` — within one certified comparison architecture, with a suitable middle-interface witness. Three event types are a necessary intuition, not a sufficient condition. This identifies the evidence shape only; it authorizes no realization search. A broader Census-2 is not presently priority-justified unless it can add evidence toward this witness shape; no claim is made that it would or would not do so. Provenance: `NG_C7C_M2_ANALYSIS_LOG.md` (`e7b85fd2…0139`, E0–E6) and the pins listed in §9.2.

`[HOLD]` **M-4 realization search** — pending the Discrete-owner P2 antipodal-endpoint policy ruling. `NG_C7C_M_DESIGN_v1.md` is retained as **historical**; its statements "typed by `B` suffices" and "associativity free at the realization level" are superseded by the above.

`[OPEN]` **C7C-A.** Not opened. Define and certify physical addition on bounded commensurability classes only if the composition carrier survives; before importing ordinary
```text
+ , *
```
from `Q`. Closure, associativity, distributivity, identities, inverses where appropriate, and compatibility of the physical operations with `rho_Q` remain separate obligations.

`[GUARD]` A nonempty realized rational-label spectrum is not yet the field `Q`; a reciprocal-closed bounded spectrum is not yet a multiplicative group of classes, since no binary operation has discharged WD-DOM.

`[INTERP]` The current N-5 architecture therefore distinguishes:
```text
bounded physical commensurability relation   [CLOSED structure]
unique rational invariant on bounded pairs   [C7A CLOSED]
bounded physical label spectrum              [C7B breadth OPEN]
strong dynamic label spectrum                [C7B breadth OPEN; DISC-1+DISC-2 admit
                                              1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4]
physical rational arithmetic                 [C7C-WD ADOPTED; C7C-0 CLOSED (bd reciprocal);
                                              C7C-M/C7C-A OPEN, C7C-M next].
```

`[GUARD]` Preserve SG-NG-5/6/19/20/22/23/24/25/26. No real-valued fundamental frequency, external clock, chart-derived asymptotic constant, limiting density, or cross-branch dynamical import may manufacture a genesis-grade rational class.

---

#### N-5A-S1 — Second-stream section-crossing search `[COR: v1.7 verdict]` / CLOSED v1.11

**RID:** `NUMGEN-OPEN-N5AS1-SECTION`  
**Correction memo:** `NG_N5AS1_LONG_HORIZON_CORRECTION_v1.md`  
**Artifacts:** original `ng_n5a_s1_section_search_v1.py` / `.log`; corrective `ng_n5a_s1_long_horizon_recheck_v1.py` / `.log`

`[COR]` **v1.7 gate-5 negative closure retracted.** The original 240-step exact-map run correctly observed the constant gap set `{6}` on the tested small seeds, but the inference that the section stream therefore equals `T^6` throughout the contracting tube was a finite-horizon overreach.

`[NUM] [scope: exact primitive map, 60 dps, audited orbit]` **Long-horizon counterexample to fixed re-blocking.** For seed `(rho,eta)=(0.01,0.004)`, the section `Theta=0` first produces a 7-step return **ending** at primitive step `33229`. `[COR v1.19]` The previously printed amplitude was the pre-transition value:
```text
Q_true(33228) ~= 5.344275761085416e-5,
Q_true(33229) ~= 5.363929537269259e-5,
Q_0 = 7.6e-5.
```
Both pre- and post-transition values remain below `Q_0`; thus the non-6 return occurs **deeper in the contracted small-amplitude regime**. A 200,000-step 12-section sweep on the same exact map gives the gap set `{6,7}` for all tested sections. The short-horizon `{6}` result is therefore a finite-horizon alias.

`[RESULT] [from: NUM] [scope: audited orbit]` **Gate-5 numerical verdict reversed.** A single section-crossing stream realizes at least two primitive return gaps, `6` and `7`; it is therefore not a fixed blocking `T^m` on that audited orbit. This passes the cheapest **numerical non-relabeling test**. It does not by itself close N-5A, and it is not yet an all-orbit theorem.

`[FAIL]` **HYP-N5AS1-GAP falsified.** The pre-registered prediction that contraction forces the primitive return-gap word to become the constant word `6` is false at the tested high-precision horizon.

`[COR]` **`NUMGEN-ART-ROTNUM-OBSTRUCTION` retracted in its v1.7 form.** A rational limiting rotation number does not imply an exact rigid rational rotation at finite amplitude and does not force every transverse section to have constant return time `q`. The exact-map long-horizon counterexample refutes that inference in the present realization.

`[COR] [historical formulation — superseded by v1.11/v1.16 closures]` **`NUMGEN-CAND-N5AS1-LOGSLIP` — nonlinear logarithmic phase-slip mechanism.** The Dyadic six-step Birkhoff/ISP law has nonzero phase shear
```text
Theta_(m+1) = Theta_m - tau Q_m + O(Q_m^2),
tau = 2 sqrt(3)/3 > 0,
```
while the asymptotic radial backbone has `Q_m ~ 1/(m+kappa)`. Hence the leading accumulated phase defect scales schematically like `tau sum Q_m ~ tau log(m+kappa)`, whereas `sum Q_m^2` is summable. This supplies a natural mechanism for sparse 7-step phase slips even while the instantaneous primitive rotation tends to the rational linear value `1/6`. At the time of this candidate formulation, a theorem connecting the block-phase shear to infinitely many primitive section slips remained OPEN; N-5A-S1-INF later closed the infinite-slip mechanism and GAP-LOCK Lemma 3 closed the physical consecutive-ratio statement. This paragraph is retained only as historical mechanism provenance.

`[RESULT] [from: NUM] [scope: audited orbit and finite horizons]` **Quantitative LOGSLIP prediction passes the present numerical tests.** The independent detector reproduces the first 7-step slip at primitive step `33229`. A pre-registered candidate spacing parameter
```text
rho := exp(pi/(3 tau)) = 2.4766...
```
was then tested over `4e6` primitive steps. The observed non-6 slips at `33229, 198242, 606981, 1619416` give shifted-time ratios `2.4710, 2.4746, 2.4760`, increasingly close to `rho`, while `1/Q` independently tracks the same block scale. A separate 12-section sweep shows the predicted even/odd first-slip clustering; the shifted cluster ratio is consistent with `sqrt(rho)` (predicted `1.5737`, observed about `1.5729`). These are strong finite-horizon numerical confirmations of the mechanism, not an asymptotic theorem. Artifacts: `NG_N5AS1_LOGSLIP_VERIFICATION_v1.md`, `ng_n5as1_logslip_verification_v1.py` / `.log`, plus the v1.7.1 long-horizon section sweep.

`[COR] [historical candidate — obligations later discharged]` **Predicted asymptotic slip law.** The Dyadic owner supplies the cubic-vector ISP law
```text
Theta_(m+1) = Theta_m - tau Q_m + O(Q_m^2),   tau = 2 sqrt(3)/3,
```
and the asymptotic backbone `Q_m ~ 1/(m+kappa)`. If (i) the remainder is controlled uniformly along the declared orbit/domain strongly enough that `sum O(Q_m^2)` converges, and (ii) a block-to-primitive crossing bridge proves that each additional accumulated defect of one primitive angular spacing `pi/3` produces exactly one return-time slip, then
```text
(M_k + kappa)/(M_(k-1) + kappa) -> exp(pi/(3 tau)).
```
Under the same two lemmas, `sum tau Q_m` diverges logarithmically, the accumulated defect is unbounded, and infinitely many primitive non-6 returns follow. These were the two closure obligations at the time of preregistration; they were subsequently discharged by N-5A-S1-INF/GAP-LOCK. The text is retained as historical preregistration provenance, not as a live OPEN status.

`[GUARD] [SG-NG-23]` **Non-fixed substream is not a nontrivial commensurability/incommensurability theorem.** Passing gate 5 excludes only a fixed blocking `B=T^m`. It does not prove that the pair carries a nontrivial Q-like class or is incommensurable. Conditional on the LOGSLIP asymptotic `N_slip(M)=O(log M)`, the average primitive steps per section crossing satisfies `6+O(log M/M)->6`; thus a density-only classifier would asymptotically erase the subleading slip structure. N-5 must therefore specify which physically certified relational structure its commensurability quotient preserves.

`[OPEN] [scope: continuous-dyad representation diagnostic]` The constants `pi/(3 tau)` and `rho=exp(pi/(3 tau))` may be studied as generator-dependent asymptotic diagnostics of the selected continuous dyad. They are **not** admissible as genesis-grade Q/R premises merely because they are non-rational: they are expressed using the pre-existing continuous angle/exponential structure and therefore remain behind SG-NG-19 and the OPEN-P0 generator-selection ceiling unless a substrate-independence or named bridge theorem is supplied.

`[RESULT] [from: ALG] [scope: canonical section on the certified one-chart local tube]` **Canonical section identity — gate 1 core.** For `Theta = atan2(sqrt3 * eta_wrap, 2 rho - eta_wrap)`,
```text
Theta = 0   <=>   eta_wrap = 0  and  rho > 0.
```
This is an exact identity: the canonical section is relational-phase coincidence with positive `rho`, not an arbitrary observer-chosen `Theta` level. `Theta_0 = pi` is the `rho < 0` branch. Other swept `Theta` levels remain coordinate robustness probes only.

`[DEF] [scope: fixed-support local dyad]` **Canonical B-event predicate.** On the sufficiently small one-chart N-1/N-3A tube, let `w=eta_wrap` in the unique local chart around phase coincidence. A B-event is a primitive transition token `e_x:x->T(x)` whose transition neighbourhood changes from the negative to the non-negative side of the phase-coincidence section while retaining positive `rho` on the declared local sides. Equivalently, in that chart the detector uses `w(x)<0<=w(Tx)` with the declared positive-`rho` condition. This is a **discrete transition predicate**; no continuous interpolation between `x` and `T(x)` is assumed.

`[RESULT] [from: ALG]` **Lift-free/gauge admissibility.** The B predicate uses only the gauge-reduced relational transition neighbourhood and is invariant under `eta -> eta+2 pi k`. Because the certified local tube admits a one-chart lift with projection injective (N-3A), the sign side of phase coincidence is unambiguous there and no winding/deck label enters the definition. Thus SG-NG-16 is not invoked as a counter. `[GUARD]` SG-NG-13 spectator independence is **not** discharged by the gauge-shift identity; no external spectator is added in this fixed-support scope. Any spectator/boundary extension would need its own admissibility check.

`[RESULT] [from: ALG]` **GATE 1 CLOSED — structural event admissibility.** The exact section identity, fixed-support lift-free transition predicate, gauge invariance, and an explicitly declared counting type
```text
P_B = "positive-oriented primitive T-transition across relational-phase coincidence with rho>0"
```
close the event-predicate obligation at the local tube scope. SG-NG-11 is satisfied because the coarser counting predicate is declared explicitly; strict transition-neighbourhood equivalence is not identified with counting equivalence. `[NUM]` On the audited seed orbit, the lift-free detector agrees exactly with the prior lap detector (6666 events in 40,000 steps), all audited crossing `Q_true` values are distinct, and no reverse-oriented event occurs. These are witnesses/regression checks, not the ALG warrant for gate 1.

`[RESULT] [from: ALG]` **GATE 3 CLOSED — structural co-realization.** By definition, every canonical B-event is one of the primitive `T` transition tokens on the same certified local tube and same primitive orbit as stream A. Hence A and B require neither a second domain nor external synchronization. This is a structural co-realization statement conditional only on B-events occurring; **indefinite occurrence is gate 2**. `[NUM]` The 40,000-step seed run realizes 6666 such anchors with a strictly increasing anchor list. `[GUARD]` That finite seed orbit is a numerical witness; because the N-1 tube radius is existential rather than explicit, the run is not itself used as proof that this particular seed lies in `U_T`.

`[RESULT] [from: ALG]` **GATE 4 CLOSED — common order.** For any two canonical B-event anchors on one primitive orbit inside `U_T`, N-2-ORD gives a unique forward-reachability relation: the later anchor is `T^k` of the earlier for one positive Track-A history count `k`, and antisymmetry excludes the reverse. Thus their interleaving is defined entirely by `<=_T`; no external clock or frequency is introduced. The associated word of unique Track-A reachability counts is a representation of this certified relational order, not an external time parameter. `[NUM]` On the audited seed run this represented word has alphabet `{6,7}` over 6665 gaps and contains the documented step-33229 slip. The observed word is NUM evidence for gate 5/LOGSLIP, not the theorem warrant for gate 4.

`[RESULT] [from: THM] [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.14 | DYAD-THM-PRIM-CTR]` **Explicit-domain boundary CLOSED (v1.20).** The Dyadic owner certifies an explicit primitive contraction and six-phase invariant tube: `0 < Q - (3/2)Q^2 <= Q(T^6 x) <= Q - (1/2)Q^2 < Q` for `Q <= 1/400`, with `U = {0 < Q <= 1/625}` and `U_T = U_{j<6} T^j(U)`. **Corollary `[ALG]`:** the canonical long-horizon seed `(rho,eta) = (1/100, 1/250)` has `Q_0 = 19/250000 < 1/625`, so it lies in `U`; the N-1 / N-2-ORD tube-membership premise for that seed is now theorem-grade, not `[NUM]`. **Corollary `[ALG]`:** with the owner's enclosure `U_T ⊂ {Q < 2209/10^6}` and `Q >= (1/2)(rho^2 + eta^2)`, every point of the explicit tube satisfies `|rho|,|eta| < 0.0665 < 1/10`, so the whole explicit tube sits inside the v1.19 P3 injectivity box; N-1 / N-2-ORD may be exhibited on a **named explicit tube**, not only a shrunken existential one. **Ownership unchanged:** L1 remains a Number Genesis theorem; `DYAD-THM-PRIM-CTR` is an independent upstream strengthening. **NUMGEN-side consumer acceptance recorded**; upstream Dyadic consumer-row synchronization (v6.4.10 "acceptance pending") is left to the Dyadic stream's own owner pass; Number Genesis does not edit the Dyadic owner. `[GUARD]` seed ∈ certified tube ⇏ all GAP-LOCK angular hypotheses certified by Dyadic; those remain Number Genesis obligations discharged by L-MONO / L-PHASE.

#### N-5A-S1-INF — CLOSED at v1.11

**RID:** `NUMGEN-OPEN-N5AS1-INF`  
**Certificate:** `NG_N5AS1_INF_CLOSURE_v1.md` + `ng_n5as1_inf_closure_cert_v1.py` / `.log`

`[COR] [from: ALG]` **The v1.10 `O(Q^2)` remainder hypothesis is exactly false.** The exact primitive quartic six-step jet produces a nonzero `Q^(3/2)` angular term; on the positive-`u` ray its coefficient is `-25 sqrt(3)/48`. The correct exact-map block law has remainder `O(Q^(3/2))`.

`[RESULT] [from: ALG]` **L-BACKBONE CLOSED from L1.** From
```text
q_(m+1)=q_m-q_m^2+O(q_m^(5/2))
```
and sufficient local shrinking,
```text
1/2 <= 1/q_(m+1)-1/q_m <= 3,
```
so `q_m=Theta(1/m)`. Refining the reciprocal increment gives
```text
1/q_(m+1)-1/q_m = 1+O(sqrt(q_m)),
1/q_M = M+O(sqrt(M)),
q_M = 1/M+O(M^(-3/2)).
```
Hence `sum q_m = infinity`, `sum q_m^2 < infinity`, `sum q_m^(3/2)<infinity`, and
```text
sum_(m<M) q_m = log M + C_Q + o(1).
```

`[RESULT] [from: ALG]` **L-MONO CLOSED, sharpened at v1.12.1.** In the primitive analytic coordinate `W`, the exact one-step map satisfies
```text
W(Tx)=exp(i pi/3) W+O(|W|^2).
```
Therefore, uniformly on a sufficiently small punctured local tube,
```text
delta_T(x) = pi/3 + O(Q^(1/2)).
```
After shrinking once more this implies the convenient corollary
```text
pi/6 < delta_T(x) < pi/2.
```
The asymptotic form, not the exactly-period-wide corollary, is the preferred branch-control statement. Thus the primitive angular lift is strictly increasing. A positive lap crossing of `Theta=0` forces `eta^-<0<=eta^+`; the exact primitive update then implies `rho^->0` and `rho^+>0`, so lap crossings coincide with the canonical lift-free B predicate. This also retires the gate-1 orientation caveat.

`[RESULT] [from: ALG]` **L-PHASE CLOSED from the exact primitive six-step iterate.** Exact Taylor composition gives no quadratic `F=T^6` term and the cubic primitive-coordinate jet
```text
Delta rho_3 = (8 eta - 7 rho) Q / 6,
Delta eta_3 = (eta - 8 rho) Q / 6.
```
In `W`,
```text
W(Fx)=W+(-1/2-i tau) W |W|^2+O(|W|^4),
tau=2 sqrt(3)/3.
```
Therefore, for the increasing primitive lift,
```text
phi_hat_(6(m+1))-phi_hat_(6m)
 = 2 pi - tau q_m + r_m,
|r_m| <= C q_m^(3/2).
```
This is an exact-primitive finite-iterate theorem, not an import from the continuous cubic-vector truncation.

`[RESULT] [from: ALG]` **INF-1.** With
```text
D_M := 2 pi M - (phi_hat_(6M)-phi_hat_0),
```
L-BACKBONE and L-PHASE give
```text
D_M = tau log M + C_D + o(1) -> infinity.
```

`[RESULT] [from: ALG]` **INF-2 / crossing count.** L-MONO identifies the canonical B count with the lap count:
```text
N_B(M)
 = M - D_M/(2 pi) + O(1)
 = M - (tau/(2 pi)) log M + O(1).
```
Hence `N_B(M)->infinity` (Gate 2 CLOSED). If only finitely many non-6 gaps occurred, the late word would be constant `6`, implying `M-N_B(M)=O(1)`, contradiction. More generally, an eventual fixed blocking `T^m0` would give `N_B(M)=6M/m0+O(1)`; the limit ratio forces `m0=6`, and the logarithmic deficit again contradicts fixed blocking. Therefore the ALG form of Gate 5 is CLOSED.

`[RESULT] [from: ALG]` **N-5A-S1 CLOSED.** Together with gates 1/3/4 from v1.9.1, the canonical B stream supplies a second independently certified, indefinitely repeatable, co-realized event/recurrence type under the common N-2-ORD reachability order and is not a fixed re-indexing of Track A.

`[RESULT] [from: ALG]` **Independent verification of the closure (v1.12).** Every exact assertion re-derived with an independent expansion routine. **Additional cross-check not present in the original certificate:** the cubic angular jet contracted against `grad Q` induces at degree 4
```text
(2 rho - eta) Delta rho_3 + (2 eta - rho) Delta eta_3 = (Q/6)(-6Q) = -Q^2
```
**exactly**, independently reproducing the certified L1 radial law from an expansion computed for a different purpose — two independently derived objects agreeing with no free parameters. Corollary: `Re(c21) = -1/2` is **forced** by `Delta|W|^2 = 2 Re(c21)|W|^4 = -Q^2`, so only `Im(c21) = -tau` carries new information. Certificate: `NG_N5AS1_CLOSURE_VERIFICATION_v1.md`, `ng_n5as1_closure_verification_v1.py` / `.log` (11 assertion families, exit 0).

`[GUARD] [margin note]` **L-MONO branch determination.** The stated bracket `pi/6 < Delta phi_T < pi/2` gives a six-step total in `(pi, 3 pi)`, an open interval of width **exactly** `2 pi`; it therefore does select the correct `2 pi` branch, but with zero margin. The sharper estimate already available from `W(Tx)/W = lambda + O(|W|)` is
```text
Delta phi_T = pi/3 + O(Q^(1/2)),
```
verified: `|Delta phi_T - pi/3|/sqrt(Q)` is stable (0.3979, 0.3948, 0.3934, 0.3927) across a 64-fold `Q` range while `/Q` diverges (22.8 → 180.2). **Recommendation:** promote this into the statement of L-MONO, keeping `(pi/6, pi/2)` as its corollary. No result changes; the branch determination stops resting on an exactly-critical interval width.

`[COR] [scope: v1.12 corollary only]` **Physical 7-gap count was originally promoted one lemma too early; v1.13 supplies the missing premises.** The v1.12.1 correction remains part of the error ledger, while the live theorem state is now:

`[RESULT] [from: ALG]` **GAP-LOCK Lemma 1 CLOSED — local return alphabet `{6,7}`.** L-PHASE is a local expansion at the fixed point and therefore applies at every sufficiently small basepoint:
```text
Lambda_6(x) = 2 pi - tau Q(x) + O(Q(x)^(3/2)).
```
After shrinking, `Lambda_6(x)<2pi`. L-MONO gives
```text
delta_T(x)=pi/3+O(Q^(1/2)) > 0.
```
A complete return gap `<=5` would force a six-consecutive-step angular sum `>2pi`, contradicting `Lambda_6<2pi`. A gap `>=8` would force a seven-step sum `<2pi`, while
```text
Lambda_7 = Lambda_6 + delta_T > 2pi
```
after sufficient shrinking. Hence every complete local B-return gap lies in `{6,7}`. Together with the closed infinitely-many-non-6 theorem, there are infinitely many **7-gaps exactly**.

`[NUM]` The certificate checks `Lambda_6<2pi` at all 3582 sampled basepoints and finds `min(Lambda_7-2pi)=1.0436`; long runs show only `{6,7}` in the small regime. A large-amplitude control produces an `11` gap, demonstrating that the local-smallness hypothesis is load-bearing rather than decorative. Certificate: `NG_N5AS1_GAPLOCK_PARTIAL_v1.md`; `ng_n5as1_gaplock12_cert_v1.py` / `.log` (7 assertion families, exit 0).

`[RESULT] [from: ALG]` **GAP-LOCK Lemma 2 CLOSED — physical bookkeeping.** With the local alphabet `{6,7}`, telescoping complete return gaps over the first `6M` primitive steps gives
```text
6M = 6 N_B(M) + s(M) + O(1),
```
where `s(M)` is the literal number of 7-step returns and the bounded term contains only initial/final partial-gap bookkeeping. Equivalently,
```text
E_B(M) = s(M) + O(1).
```
Since v1.12.1 already proved
```text
E_B(M) = (3 tau/pi) log M + O(1),
```
the **physical 7-gap count law**
```text
s(M) = (3 tau/pi) log M + O(1)
```
is theorem-grade. Consequently
```text
(1/k) log M_k^(phys) -> pi/(3 tau)
```
for the physical k-th 7-gap time in the mean exponential sense.

**RID:** `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO`  
`[RESULT] [from: ALG]` **Defect-threshold consecutive-ratio theorem retained.** For first crossings of fixed `pi/3` increments of the eventually monotone accumulated phase defect,
```text
M_(k+1)^(def) / M_k^(def) -> exp(pi/(3 tau))
                           = exp(sqrt(3) pi/6).
```
This remains theorem-grade at the defect-threshold level.

`[RESULT] [from: ALG]` **GAP-LOCK Lemma 3 CLOSED — event-time physical-slip locking.** Let `n_j` be successive physical B-event steps, `o_j` their phase overshoots, `s_j` the number of 7-gaps among the first `j` returns, and
```text
G_n := (pi/3)n - (phi_hat_n - phi_hat_0),    G_(6M)=D_M.
```
Lemma 1's exact `{6,7}` alphabet gives
```text
n_j = n_0 + 6j + s_j,
```
hence the exact local event identity
```text
G_(n_j) = C + (pi/3)s_j - o_j.
```
With the actual six-step deficit
```text
Delta_j := 2pi - Lambda_6(x_j) -> 0,
```
the return alphabet makes
```text
g_(j+1)=7  <=>  0 <= o_j < Delta_j.
```
At the `k`-th physical 7-gap the overshoot therefore tends to zero locally, without summing per-slip errors. Writing `n_(j_k)=6M_k+r_k`, `0<=r_k<=5`, and using the promoted one-step law `Delta phi_T=pi/3+O(Q^(1/2))` yields
```text
D_(M_k) = C + (k-1)pi/3 + o(1).
```
Combining with INF-1 `D_M=tau log M + C_D + o(1)` gives
```text
M_(k+1)^(phys)/M_k^(phys) -> exp(pi/(3tau))
                              = exp(sqrt(3)pi/6).
```
`[COR v1.19]` If `n_k` is the primitive step of the `k`-th physical slip and `M_k` its six-block index, then `n_k = 6 M_k + O(1)` (not `n_k=M_k+O(1)`). Multiplication by the fixed factor six and the bounded offset leave the consecutive-ratio limit unchanged, so primitive slip steps have the same limit.

`[COR]` **v1 bootstrap retracted as proof.** The proposed inference from a per-slip `O(sqrt q)` jump error to bounded accumulated `alpha_k` was circular; a bounded per-slip error need not have a bounded accumulated sum. The closure above replaces that bootstrap with an exact event-time identity plus a vanishing local overshoot bracket, so no accumulated-error summability premise is used.

`[COR]` **Threshold/physical wording.** The defect-threshold and physical-slip **consecutive-ratio limits now coincide** at `exp(sqrt(3)pi/6)`. Their event sequences are not identified term-by-term. The Fatou/`C_D` normalization question is optional refinement, not a GAP-LOCK blocker.

`[GUARD]` SG-NG-23 remains unchanged: N-5A closure and the physical 7-gap count law are **not** a nontrivial Q-like commensurability theorem. The average primitive steps per B event still tends to `6`, while the certified physical 7-gap count diverges logarithmically. The mean physical exponential rate and the **physical consecutive 7-gap ratio limit** are theorem-grade; GAP-LOCK Lemmas 1–3 are CLOSED.


---

`[RESULT] [from: ALG]` **N-5A gate ledger after v1.11:** gates 1–5 are CLOSED on the sufficiently small certified local primitive-dyad tube. The earlier long-horizon numerics remain regression/prediction evidence, while infinite repeatability and non-fixed re-blocking now have exact local proofs.

`[GUARD]` The closure is local/existential in radius and conditional on the selected continuous generator `T` under OPEN-P0. It does not globalize the second stream or establish a nontrivial rational label.

`[INTERP]` **Frontier reshaping.** N-4 remains important for globality, winding, critical-curve and larger-amplitude structure, but it is no longer required merely to obtain a non-fixed section return word. The same-orbit angular route remains live and should be exhausted before importing a structurally different source.


---

### §6.7 N-6 real completion target

`[HYP]` **Classification-first real representation.** Incommensurable relational comparison should receive an R-like label only after the comparison structure itself is physically certified. Candidate representations remain Cauchy completion, Dedekind/order cuts, or a rotation-number construction **if** the physical comparison stream is first proved to have the required mechanical/Sturmian/ergodic structure. Incommensurability by itself does not imply a Sturmian coding or an existing rotation number.

`[INTERP]` The programme therefore need not claim that irrational relations are ontologically manufactured by completing already-primitive rationals. Completion is a mathematical representation route for a certified order/comparison structure.

`[GUARD]` Because the current realization already uses a continuous state chart, an in-branch N-6 theorem is a recovery/representation theorem unless SG-NG-19 is discharged. The stronger claim "RTG generates the continuum substrate" remains unavailable.

#### OPEN N-6 — Continuum completion

**RID:** `NUMGEN-OPEN-N6`  
**Status:** BLOCKED on N-5; continuous-branch closure is representation/recovery level under SG-NG-19 unless the stronger substrate condition is discharged

**Question:** Can real-valued relational magnitude arise as a completion of finite recurrence-comparison observations?

**Candidate route:** build rational approximants from N-5 physical comparison classes; define an RTG-native order/convergence criterion; construct a Cauchy-, Dedekind-, or rotation-order completion; then identify the completed object with `R` only after the physical completion object exists.

`[OPEN candidate]` **Rotation/Sturmian route.** If N-5A/N-5 produce a pair whose comparison coding is provably a mechanical/Sturmian word (or another class with an equivalent rotation-number theorem), use its asymptotic slope/order cuts as the completion object. Incommensurability alone does **not** imply Sturmian coding or existence of a rotation number; those properties require their own theorem.

**Critical guards:**

- do not assume `R_+`-valued fundamental frequencies in the premises;
- the continuous dyad already lives on an `R^2` chart, so an in-branch recovery of `R` from event order is not by itself a genesis of the continuum substrate (SG-NG-19);
- a genesis-grade continuum claim requires a substrate-independence theorem, a non-continuum realization behind a named bridge, or an explicitly tagged postulate.

**Later representation:** only after completion may a positive-ratio group be represented additively by `log : R_+ -> R`.

---

### §6.8 NG-7 recurrence holonomy — NG-7A closed / NG-7B open

`[RESULT] [from: ALG] [scope: finite directed multigraph operator layer; field coefficients plus fundamental-integral-cycle completeness over abelian coefficient groups]` **NG-7A CLOSED.** Null theorem `C D^T = 0`; completeness `im D^T = ker(C·)` over field coefficients making `h = Ca` and `[a] ∈ H^1(G;F) ~= F^beta` equivalent complete obstructions; orientation, gauge, and cycle-basis invariance with the invariant statistics identified; the PI-typed statistic (scalar observable is `h`/`[a]`, never a rank; `r_hol = rank(CA)` reserved for `d>=2`, channel-GL invariant, `<= min(beta,d)`, zero iff flat); separation instances certifying **cycle capacity ≠ holonomy content** in both directions (field-general full-rank witness by a right inverse of `C`; executable `Q` witness `A=C^T`); the mandatory TDR-G `Z_N` zero-control with **cycle-sensitive** unit-defect detection; and `[v1.19]` fundamental-integral-cycle completeness over arbitrary abelian coefficient groups by spanning-forest integration. Certificate: `NG_NG7A_HOLONOMY_NULL_CERT_v1.md` (original NG-7A package) plus the v1.19 in-ledger extension.

`[RESULT] [from: ALG]` **Foundations export.** T1–T7 discharge the operator half of `RTG-OFN-OPEN-HOLONOMY-RANK-DIAGNOSTIC`. D15 OFN-side synchronization is complete in OFN v0.8 (RF-O08-10); the OFN whole target remains ACTIVE for physical source, non-Abelian extension, and curvature.

`[GUARD]` Fundamental-integral-cycle completeness over `Z_N` is now certified, but completeness for an arbitrary nonprimitive/rescaled integer cycle-row presentation is not implied. SG-NG-7 (holonomy ≠ curvature) is unchanged; the ring `Z_N` defect residue is not identified with Track-C winding/character labels absent a proved map; no non-Abelian rank exists until NG-7B defines and certifies its invariant (Case E2 additionally requires its flatness and topology guards).

`[OPEN]` **NG-7B.** Positive-source candidates are continuous frame/connection data, birth/history data, spin/quaternionic structure, or OPEN-M content. No positive holonomy or curvature claim follows from NG-7A alone.

#### NG-7 — Recurrence holonomy / holonomy content

**RID:** `NUMGEN-OPEN-REC-HOL`  
**Status:** SPLIT — **NG-7A CLOSED at v1.5**; NG-7B OPEN (physical source / non-Abelian)

**Question:** Can relative recurrence data provide the explicit non-integrability diagnostic requested by `RTG_ONTOLOGICAL_FOUNDATIONS` (originally v0.7; live pointer v0.8 §9), RID `RTG-OFN-OPEN-HOLONOMY-RANK-DIAGNOSTIC`?

**Candidate multiplicative edge data:** For oriented edge `i->j`, let `R_ij` denote a relational recurrence ratio, with reciprocal reversal `R_ji = R_ij^{-1}` where defined.

**Candidate log edge field:**

```text
a_ij = log R_ij.
```

If node potentials `x_i` exist such that

```text
a_ij = x_i - x_j,
```

then every oriented cycle has zero additive holonomy:

```text
sum_(ij in gamma) s_ij a_ij = 0,
```

or equivalently multiplicative holonomy

```text
H_gamma = product_(ij in gamma) R_ij^(s_ij) = 1.
```

Let `D` be an incidence operator and `C` a cycle-basis operator. For one channel:

```text
h = C a.
```

For `d` recurrence channels assembled as edge matrix `A`:

```text
H = C A,
r_hol = rank(H).
```

(`r_hol` is defined only for genuinely multi-channel data `d>=2`; for `d=1` the primitive observable is the holonomy vector `h` / class `[a]`, never a rank — PI terminology ruling 2026-08-28.)

**Required null theorem:**

```text
A = D^T X  =>  C A = C D^T X = 0.
```

**Required invariance work:** establish orientation convention, cycle-basis independence of rank, gauge invariance under node-potential shifts, treatment of missing/zero ratios, and relation to graph cohomology.

**Scope guard:** `r_hol > 0` is a non-integrability diagnostic, not automatically spacetime curvature. A physical geometry interpretation requires an explicit RTG bridge to frame/connection/metric data.

**Programme status.** NG-7A already supplies the certified additive operator/null half of the Foundations diagnostic. The remaining programme task is NG-7B: an RTG-native non-integrable source and any non-Abelian / geometry extension.

##### NG-7A — Additive operator / null theorem

**Sub-RID:** `NUMGEN-OPEN-REC-HOL-OPERATOR`  
**Status:** CLOSED `[RESULT][from: ALG]` `[scope: finite directed multigraph operator layer, field coefficients; Z_N zero-control certified]`  
**Certificate:** `NG_NG7A_HOLONOMY_NULL_CERT_v1.md` + `ng7a_holonomy_null_cert_v1.py` / `.log` (12 assertion families, all pass, exit 0)

`[RESULT] [from: ALG]` **Null theorem.** `C D^T = 0` as an operator identity; hence `A = D^T X ⟹ C A = 0`. Loops and parallel edges included; a self-loop has zero incidence column and is itself a cycle.

`[RESULT] [from: ALG]` **Completeness over field coefficients.** `im D^T = ker(C·)` by the exact dimension count `m − beta = n − c = rank D^T` plus the null theorem, so `h(a) = 0 ⟺ a = D^T x` solvable. `h` therefore descends to an isomorphism `H^1(G;F) := F^E / im D^T ~= F^beta`: the holonomy vector and the cohomology class `[a]` are equivalent **complete** obstructions. On an abstract graph the closure operator to 2-cochains is zero; declaring a 2-complex later restricts its kernel (NG-7B/geometry territory).

`[RESULT] [from: ALG]` **Invariance package.** Orientation: simultaneous edge reorientation `(DS, CS, Sa)` leaves `h` fixed; reversing one basis cycle negates only that component; invariant statistics are the zero-set, ranks, and `[a]`. Gauge: `h(a + D^T g) = h(a)`; per-component constant potential shifts are exact gauge (`D^T 1_comp = 0`). Basis: `C -> M C` gives `h -> M h` with the zero-set, `r_hol`, and `[a]` invariant.

`[RESULT] [from: ALG]` **Typed statistic and bounds.** `rank(C a) ∈ {0,1}` for every scalar cochain (both values realized in the certificate). For `d>=2`: `r_hol = rank(C A)` is invariant under channel recombination `A -> A R` (`R ∈ GL(d)`), satisfies `r_hol <= min(beta, d)`, and `r_hol = 0 ⟺ A = D^T X`.

`[RESULT] [from: ALG]` **Separation instances.** Flat data realize `(beta > 0, r_hol = 0)`. For the field-general full-content direction, because `C` has full row rank `beta`, choose any right inverse `R in F^(E x beta)` satisfying `C R = I_beta`; then `A=R` gives `r_hol=beta`. In the executable `Q` test suite, the simpler concrete Gram witness `A=C^T` also realizes `r_hol=beta`. Thus cycle capacity and holonomy content are certified as independent axes — the operator half of the Foundations diagnostic.

`[RESULT] [from: ALG]` **TDR-G `Z_N` zero-control.** Integer cycle vectors annihilate node-difference `Z_N` phase data mod `N`. Depends on: the NG-7A integer null identity `C D^T = 0`. Provenance: finite exact checks on rings `N = 6, 8, 12` and sampled random graphs. `[COR v1.19]` A unit defect is detected when it has nonzero projection onto the declared cycle/cohomology sector; a defect on a bridge/pendant edge may be exact node-potential data and therefore invisible to cycle holonomy.

`[RESULT] [from: ALG] [v1.19]` **Fundamental-cycle completeness over abelian coefficient groups.** Fix a spanning forest and its fundamental **integral** cycle basis. For an edge cochain with values in any abelian coefficient group (including `Z_N`), vanishing sums on all fundamental cycles imply exact node-potential data: integrate the cochain along each tree to define vertex potentials; tree-edge residuals vanish by construction, and every non-tree residual equals its fundamental-cycle sum and therefore vanishes. No division or field-rank argument is used. `[GUARD]` The integral-basis qualification is load-bearing: arbitrary nonprimitive integer rescaling of cycle rows need not preserve completeness modulo `N`.

`[GUARD]` **Declared-domain convention.** Data must be total on the declared edge set; partial data restrict to the support subgraph, on which `(D, C, beta)` are recomputed. Missing ratios are excluded, never imputed.

`[GUARD]` For a single scalar channel (`d=1`), ordinary matrix rank of `H` is at most one; a richer holonomy-rank statistic requires multiple independent channels or a separately defined non-Abelian invariant. The word *rank* must therefore be typed by codomain/data structure.

`[RESULT] [from: ALG]` `[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.8 §9 | RTG-OFN-OPEN-HOLONOMY-RANK-DIAGNOSTIC]` **Source narrowing already known:** the discrete TDR-G phase sector is node-difference-flat by construction, so it is a required zero-control rather than the first positive-source target.

##### NG-7B — RTG-native non-integrable source / non-Abelian extension

**Sub-RID:** `NUMGEN-OPEN-REC-HOL-SOURCE`  
**Status:** OPEN / physical-source layer

The live positive-source search is narrowed to non-node-difference content such as continuous frame/connection data, birth/history data, spin/quaternionic structure, or OPEN-M content. A non-Abelian version may later use loop holonomies in `SU(2)` modulo gauge/conjugation, but no "non-Abelian holonomy rank" is defined until a precise invariant is adopted and certified.

`[GUARD]` Closing NG-7A discharges only the operator/null half of the Foundations diagnostic. It does not prove that RTG supplies nonzero physical holonomy or curvature; that is NG-7B plus the relevant geometry bridge.

---

### §6.9 NG-8 functorial counting compatibility

`[HYP]` “Five nodes,” “five repeats,” “five windings,” and “fifth harmonic” are distinct relational invariants/representations. Their common numeral should arise through physically implemented compatibility maps on the certified relational architecture, not bare abstract isomorphisms.

`[RESULT] [from: ALG] [scope: local primitive-dyad tube U_T]` **NG-8A CLOSED — ordinal-to-cardinal orbit-state compatibility.** For every admissible `x in U_T` and finite `m>=0`, define the post-event visited-state collection
\[
S_m^+(x)=\{T^k x:1\le k\le m\},\qquad S_0^+(x)=\varnothing.
\]
N-1 primitive-orbit non-collision makes the orbit-evaluation map `k -> T^k x` injective; surjectivity is by construction. Thus the `m` primitive event occurrences are physically equinumerous with the `m` newly visited post-event relational states. In ordinary mathematical representation, `|S_m^+(x)|=m`.

`[GUARD]` If one instead counts orbit positions including the initial state, `{x,Tx,...,T^(m-1)x}` contains `m` positions but only `m-1` transitions between them. Event-count and state-position conventions must not be mixed.

`[RESULT] [from: ALG] [scope: local primitive-dyad tube U_T]` **NG-8B CLOSED — multiplication by physical re-blocking.** For every positive block size `m`, define `B_m=T^m`. N-1 non-collision implies `<B_m>` is free. For every `k>=0`,
\[
(T^m)^k=T^{mk}.
\]
The two sides are the same ordered primitive event history with different grouping. Re-blocking therefore realizes multiplication compatibility as repeated concatenation of an `m`-event block; it does not introduce a second independent event type.

`[GUARD]` NG-8B cannot discharge N-5A/SG-NG-20. A pair `(T^m,T^n)` remains one certified stream under two blockings.

`[OPEN]` **Full NG-8 target — compatibility of invariants on the common relational architecture.** Prove physically implemented structure-preserving maps among:

- Track A: repeatable endomorphism-history exponent/count;
- Track B: finite physically distinguishable object/state/arrow multiplicity at the declared scope;
- Track C: character/cyclic invariants of the appropriate completion/representation.

The common home is the certified typed relational architecture with partial physical composition `C_NG`; a new hypothetical universal set of numerals is not required as an ontological primitive. What remains to prove is compatibility of the distinct invariants/representations.

#### OPEN NG-8 — Functorial compatibility / “two fives”

`[OPEN]` **Three-track roadmap after N-1/N-2.** Track A supplies a concrete local endomorphism-history object and its signed completion. Track B constructs physically distinguishable finite multiplicity invariants at declared scopes. Track C constructs cyclic/character invariants. These are treated as different invariants/representations of the certified relational architecture `C_NG`, not as three objects that must be mapped into a hypothetical primitive numeral container.

**RID:** `NUMGEN-OPEN-TWO-FIVES`  
**Status:** ACTIVE conceptually; NG-8A and NG-8B CLOSED, full cross-track theorem OPEN

**Question:** Why do distinct relational invariants such as five nodes/states, five event repetitions, five windings, and the fifth harmonic admit compatible arithmetic labels and operations?

**Guard:** These physical structures are not identical. `5 in N` must not be conflated with the cyclic group `Z_5`, where `[5]=[0]`.

**Candidate theorem strategy:** construct physically implemented comparison maps/functors between the relevant invariants and prove compatibility with their native compositions. Examples of arithmetic images to test include:

```text
E^m E^n = E^(m+n)
chi_m chi_n = chi_(m+n)
(E^m)^n = E^(mn)
(chi_m)^n = chi_(mn).
```

**Open issue:** finite object/state multiplicity and recurrence/harmonic exponent arise from different constructions. Their compatibility must be proved through the shared relational architecture and declared maps; reuse of the same numeral is not evidence by itself.

##### NG-8A — Ordinal-to-cardinal orbit-state compatibility

**Sub-RID:** `NUMGEN-OPEN-TWO-FIVES-ORBIT-CARDINAL`  
**Status:** CLOSED `[RESULT][from: ALG]` `[scope: local primitive-dyad tube U_T]`  
**Certificate:** `NG_NG8A_ORBIT_CARDINAL_CERT_v1.md`

For an admissible initial state `x` and finite event count `m`, define the post-event state collection

```text
S_m^+(x) = {T x, T^2 x, ..., T^m x},
S_0^+(x) = emptyset.
```

The orbit-evaluation map from the `m` event occurrences to their post-event states is injective by N-1 primitive-orbit non-collision and surjective by construction. Therefore the event history and post-event state collection are physically equinumerous; ordinary cardinality `m` is the mathematical representation, not the premise.

`[GUARD]` The older position-set convention `{x,Tx,...,T^(m-1)x}` counts `m` positions but only `m-1` transitions. NG-8A uses the post-event convention when speaking of `m` primitive events.

`[DEF]` **State-counting predicate (SG-NG-11 discharge).** The Track-B counting equivalence used in NG-8A is identity of the gauge-reduced present state on `U_T`. Distinct tube states are distinct points of the gauge-reduced chart `(rho,eta)` and are therefore physically distinguishable at this scope by the declared full reduced present state. `[COR v1.19]` The earlier shorthand "`Q_true` and/or relational phase" was not a separating family: `(a,0)` and `(-a,0)` have the same `Q_true` and `eta`. The theorem uses identity of the full reduced state, not that insufficient shorthand. "Physically equinumerous" is asserted relative to this declared predicate.

##### NG-8B — Multiplication by physical re-blocking

**Sub-RID:** `NUMGEN-OPEN-TWO-FIVES-REBLOCK`  
**Status:** CLOSED `[RESULT][from: ALG]` `[scope: local primitive-dyad tube U_T]`  
**Certificate:** `NG_NG8B_REBLOCK_MULT_CERT_v1.md`

For each positive block size `m`, `B_m=T^m` generates the free submonoid `<T^m>`. For every `k>=0`,

```text
(T^m)^k = T^(mk).
```

The equality is identity of the same ordered primitive event history under two groupings, not merely equality of endpoints. The RTG-native operation is repeated block concatenation; `mk` is the standard mathematical representation of the resulting repeated-addition count.

`[GUARD]` `T^m` is a derived block/coarse-graining of the same Track-A stream, not a second independently certified event type. NG-8B therefore does not close N-5A or produce a physical rational ratio from one generator.

`[GUARD]` **No commutativity claim from grouping alone** *(imported from `NG_NG8B_REBLOCK_MULT_CERT_v1` §9.7)*. Within Track A the two groupings `(T^m)^k` and `(T^k)^m` flatten to the same primitive history (both are `T^(mk)`); this inherits metalanguage integer commutativity and is not a separate physical law. Any claim that a physical binary multiplication is independently commutative **across distinct counting realizations/tracks** belongs to later NG-8 compatibility work.

`[GUARD]` NG-8A/B close only the local Track-A→finite-state equinumerosity seed and Track-A multiplication/re-blocking seed. Full network/cardinal and Track-C compatibility remains OPEN.

---

### §6.9a NG-10 — Genesis saturation and counting truncation

#### OPEN NG-10 — Genesis saturation and counting truncation

**RID:** `NUMGEN-OPEN-GENESIS-TRUNCATION`  
**Status:** OPEN / cross-ledger diagnostic

`[RESULT]` `[from: NUM]` `[scope: reduced birth-race model]` `[source: RTG_GENESIS_GEOMETRY_DSN_v2.8.4 §6.6; RID: GEN-ART-SATURATION]` Genesis contains an artifact-certified saturation ceiling `Q_d* ~ 1.13e-2` in the reduced `P4` birth-race sector.

**Question:** Does a bounded dynamical amplitude imply a finite bound on distinguishable event repetition in that sector?

`[GUARD]` **Bounded amplitude does not imply bounded history.** A state variable may converge or cycle while the event history remains indefinitely extensible. A finite repetition cap follows only with an additional theorem such as a uniform positive lower bound on a monotone per-event increment, a finite-state recurrence quotient that collapses histories, or a terminal-event condition. The heuristic estimate `N_max ~ Q_d*/delta Q_d` is admissible only if a strictly positive lower bound `delta Q_d` is proved over the relevant pre-saturation sector.

**Potential benefit:** NG-10 is a direct stress test of the distinction between bounded state and unbounded history established by N-1B/N-1C.

---

### §6.10 External benefit boundary

The Number Genesis programme may eventually contribute to relational time, spectral/recurrence geometry, quantization from finite distinguishability, or continuum-limit discipline. At v0.1 these are motivations only. A publishable contribution requires at least one nontrivial RTG-specific theorem, obstruction, new invariant, or empirical consequence beyond standard algebra/topology.

---

#### OPEN NG-9 — External mathematics/physics consequences

**RID:** `NUMGEN-OPEN-EXTERNAL`  
**Status:** OPEN / hypothesis registry only

Candidate areas:

- relational time: separation of event order from duration/recurrence measure;
- spectral/recurrence reconstruction of geometry;
- finite distinguishability and harmonic aliasing/quantization;
- number/ratio interpretation of dimensionless physical observables;
- continuum-limit discipline in UV/quantum-gravity contexts.

**Current verdict:** No external open problem is claimed solved. UV divergences, quantum-gravity time, fine-tuning, physical constants, or set-theoretic foundations must not be advertised as resolved by the Number Genesis framework without a new theorem or empirical prediction.

---

## §7. Proof and Certification Programme

### N-1 minimal proof package

#### N-1A0/A1 equivalence package

1. define finite transition neighborhood `N_e=(S_e,dS_e,X_e^- -> X_e^+)`;
2. define the admissible relational groupoid `G_adm`;
3. prove orbit/isomorphism equivalence `~_str`;
4. define the primitive counting map `P_NG` and induced equivalence `~_P`;
5. prove `~_str => ~_P` for admissible `P_NG`;
6. verify gauge invariance and spectator invariance;
7. state the orientation-retention policy explicitly;
8. give at least one example where `~_P` is strictly coarser than `~_str` (e.g. different amplitudes of one event mechanism);
9. give one counterexample showing why global-state equality is too strong for evolving-network counting.

#### N-1B repeatability/successor package

1. define physical finite `E`-histories without an external clock;
2. define admissible one-event extension `h ->_E h o e`;
3. distinguish one-time recurrence, finite repeatability, and indefinite extensibility;
4. state/prove the scoped successor condition `forall h exists admissible one-E extension`, or tag it explicitly `[HYP]`;
5. identify physical obstructions that can truncate the repetition sector;
6. state clearly that potential unbounded extension does not assert a completed physical infinity.

#### N-1C monoid package

**Scoped dyadic status:** items 2–3 are discharged at the deterministic transformation-monoid level on the L1 sector: composition is ordinary transformation composition and `Q_true` separates all finite powers. General history-quotient semantics remain broader than this scoped realization.

1. define the physical history quotient/operational equivalence being represented;
2. `[CLOSED scoped]` prove composition congruence for the deterministic transformation monoid;
3. `[CLOSED scoped]` prove one generator has no extra finite power relations via L1 strict `Q_true` contraction;
4. prove/record the universal property for the scoped monogenic transformation submonoid;
5. state the mathematical isomorphism to `(N,+,0)` only after 1–4;
6. align the primitive `T` event type/domain with N-1A/N-1B and keep formal-vs-physical scope explicit.

### N-2 proof package — CLOSED

1. `[CLOSED]` cancellativity/commutativity inherited from the N-1 free monoid;
2. `[CLOSED]` oriented-pair equivalence and Grothendieck group construction;
3. `[CLOSED]` injective embedding of unsigned histories;
4. `[CLOSED]` infinite-cyclic structure and `(Z,+,0)` metalanguage representation;
5. `[CLOSED]` non-reversal interpretation: inverse is comparison-order swap, not physical `T^{-1}`;
6. `[CLOSED]` Grothendieck universal property.

### N-3 representation proof package — CLOSED / OPEN split

1. `[CLOSED]` natural lifted primitive map and deck commutation;
2. `[CLOSED]` one-chart shrinking/invariant-tube argument;
3. `[CLOSED]` local dynamically induced winding kernel `ker rho_wind = G_T`;
4. `[CLOSED]` faithful abstract character isomorphism `G_T ~= widehat(S^1)`;
5. `[CLOSED]` exact primitive character pullback and proof of non-translational label dynamics;
6. `[CLOSED]` finite-character restriction with kernel `N G_T` and explicit no-dynamics-transfer guard;
7. `[CLOSED by import]` the specific `q=4,(0,3)` nonlinear cascade item is closed by Dyadic v6.4.10 `DYAD-THM-Q403-PHASELAW`; ownership remains Dyadic;
8. `[ROUTED]` reachable-basis/universal missing-slot projector work is an Arithmetic-Dynamics/Dyadic OPEN-9 interface target, not a Number Genesis foundation blocker;
9. `[OPEN]` establish, if desired, any separate physical observability theorem for harmonic coefficients beyond their role as mathematical function-space coordinates.

### NG-7 minimal proof package

**NG-7A — operator/null half — CLOSED at v1.5** (`NG_NG7A_HOLONOMY_NULL_CERT_v1.md`)

1. `[CLOSED]` multiplicative and additive holonomy definitions with the declared-domain convention (multiplicative spot theorem exact on K3);
2. `[CLOSED]` orientation-reversal consistency (edge reorientation invariance; per-cycle sign law; invariant statistics identified);
3. `[CLOSED]` zero-holonomy theorem for node-potential data, plus field-coefficient completeness `im D^T = ker(C·)`;
4. `[CLOSED]` cycle-basis invariance (`h -> M h`; zero-set, `r_hol`, `[a]` invariant);
5. `[CLOSED]` gauge invariance including per-component constant shifts;
6. `[CLOSED]` typed scalar-vs-multichannel statistic per PI ruling (`rank(Ca) ∈ {0,1}`; `r_hol` for `d>=2` with GL(d) invariance and bounds);
7. `[CLOSED]` mandatory Foundations flat-case control including the TDR-G `Z_N` phase sector (rings `N=6,8,12` + random graphs; unit defect detected on a cycle-sensitive edge; `[COR v1.20]` fundamental-integral-cycle completeness over `Z_N` is certified (§6.8); completeness for arbitrary nonprimitive/rescaled integer cycle-row presentations is not claimed);
8. `[CLOSED]` exit-code-gated executable certificate (12 assertion families, all pass, exit 0).

**NG-7B — source/physical half**

9. identify an RTG-native non-node-difference source of edge/connection data;
10. if non-Abelian holonomy is introduced, define its invariant before calling it a rank;
11. prove any geometry/curvature interpretation only through the appropriate frame/metric bridge.

---

## §8. Immediate Next Action

`[RESULT] [from: ALG]` **NG-8A and NG-8B are now closed.** Their certificates are registered below; they no longer occupy the active proof queue.

**Paradigm synchronization complete at documentation level.** *(status metadata; not a graded claim)*

`[DEF]` **Adopted documentation semantics.** Number Genesis is explicitly composition-first and representation-after-construction.

`[GUARD]` The v1.4 paradigm release makes no universal claim that ratio/proportion is ontologically prior to addition/difference. NG-0R/SG-NG-22 require sector-specific mechanisms and gauges before either direction is promoted.

`[RESULT] [from: ALG]` **NG-7A is closed at v1.5** and **N-2-ORD at v1.6**; both certificates are registered below.

`[RESULT] [from: ALG]` **Foundational chain complete on the local object:** N-like repetition (N-1) → Z-like signed comparison (N-2) → physically realized order (N-2-ORD), all on the same certified primitive-dyad tube.

`[RESULT] [from: ALG]` **N-5 commensurability architecture now has both negative and positive physical tests.** C1–C4 establish the bounded-defect quotient structure; C5 supplies mathematical controls; C6 falsifies the density-only canonical pair; N5-PHYS-1 supplies a genuine physical `1:1` bounded class; C7A maps every certified bounded pair to a unique positive-rational invariant. `Q_RTG^bd` is nonempty. **C7B-DISC-1 and C7B-DISC-2 are CLOSED** and establish

```text
{1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4} subseteq Q_RTG^dyn.
```

`[GUARD]` This is a certified lower bound, **not** an exhaustive spectrum.

`[OPEN]` C7B global breadth and C7C physical arithmetic remain OPEN.

**Current in-branch proof queue:**

*(This queue mirrors the section 2 queue; it is not an independently editable second queue.)*

1. **C7C-M — interface-typed WD-DOM / partial-composition closure.** M-1A/M-1B CLOSED `[ALG]`; M2-1 adopted (algebra only); unrestricted WD-CLOSE and naive label-only WD-DOM FAIL; C7C-M2 Census-1 INCONCLUSIVE / INCONCLUSIVE (no admitted composable source chain); full-interface typed WD-DOM OPEN; M-4 HOLD (P2). Then `C7C-A` only if the composition carrier survives.
2. **C7B global breadth.** DISC-1 and DISC-2 CLOSED; DISC-3 deferred, not blocked.
3. **N-4 — global/domain extension in parallel.**
4. **N-6 — R-like incommensurability/completion**, SG-NG-19 retained.
5. **Full NG-8 — cross-track functorial compatibility.**
6. **NG-10 — Genesis saturation / counting truncation.**
7. **NG-9 — external consequences.**

**Closed parallel asymptotic item:** **GAP-LOCK Lemma 3** is now CLOSED `[ALG]`; the physical consecutive 7-gap ratio limit equals the defect-threshold limit `exp(sqrt(3)pi/6)`. The defect-threshold theorem is registered as `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO`.

**Closed P3 refinement `[v1.19]`:** a derivative lower-bound proves `T` injective on `|rho|,|eta|<=1/10`; the existential N-1 tube may be shrunk into this box. ORD-2 reflection and the cross-orbit merge criterion are therefore `[ALG]` on the shrunken tube. No explicit maximal radius or numerical-seed inclusion is claimed.

**Parallel semantics test:** `HYP-NG-0R-COV` may be audited without blocking the queue. The phase quotient/difference identity is not a test; the audit must use a sector transformation whose covariance could actually fail.

**Parallel robustness:** N-1B-GROWTH remains abstract-first. Concrete Genesis/TDR-G realizations remain separately scope-gated.

**Arithmetic-Dynamics handoff:** N-3C+ reachable-basis/projector machinery may be exported as representation input to the Dyadic OPEN-9 horizon programme. Number Genesis does not own the nonlinear coefficient theorems.

`[PROVENANCE]` The programme-review audit reports DZT v0.17 as a frozen closure state containing all-`p` odd-support and denominator theorems and numerically reproduces them with `ng_review_dzt_independent_audit_v1.py`. Because the v0.17 owner DSN is not presently in the project corpus, this DSN records it only as a source-synchronization note; no NG claim relies on the audit memo as a substitute owner source.

---

## §9. Import Ledger and Artifact Registry

### §9.1 Import Ledger

| Imported object | Current pointer target | Use in this DSN | Validation state carried into v1.19 |
|---|---|---|---|
| programme generator-selection ceiling | `[import: RTG_PROGRAMME_OVERVIEW_v1.2 SG-PROG-2 | RTG-OPEN-GENERATOR-SELECTION]` | scope of all continuous-`T` Number Genesis results | verified against live source; no status promotion |
| relational primacy / no external physical time | `[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.8 §1.1–§1.2 | RID unavailable]` | NG0, history/time interpretation | verified against live source |
| holonomy-rank diagnostic / discrete-flat narrowing | `[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.8 §4.4, §9 | RTG-OFN-OPEN-HOLONOMY-RANK-DIAGNOSTIC]` | NG-7A/NG-7B | **D15 SYNC COMPLETE (v1.20):** OFN v0.8 RF-O08-10 inspected NUMGEN v1.19 NG-7A/NG-7B and records the additive result and the fundamental-integral-cycle extension; OFN whole target remains ACTIVE (physical source / non-Abelian / curvature). Alignment note: OFN v0.8 quotient/presentation guards agree with C7C-WD and the P2 finding — a quotient is not the full state unless transitions descend; presentation convention is not physical invariance |
| primitive dyad map, `Q_true`, order-6 structure / winding | `[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.1, §6.4 | RID unavailable]` | N-1C-DYAD / N-4 | verified; N-1 L1 remains independently certified by NG artifacts |
| explicit primitive contraction / six-phase invariant tube | `[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.14 | DYAD-THM-PRIM-CTR]` | N-1 / N-2-ORD explicit-domain closure; canonical seed in `U` | verified (v1.20); NUMGEN-side consumer acceptance recorded; upstream consumer-row sync left to the Dyadic stream's own owner pass |
| `q=4,(0,3)` all-`p` cascade closure | `[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.11 | DYAD-THM-Q403-PHASELAW]` | retire stale N-3C+ item 5; representation/dynamics boundary | verified against owner source; ownership remains Dyadic |
| TDR-G `Z_N`, finite recurrence, cross-branch firewall | `RTG_DISCRETE_GENESIS_DSN_v2.12.13 §6.1–§6.2`, SG-10 | N-3D / NG-8 guard / NG-7 zero-control / C7B-DISC-1 owner-native search | verified against live source; per-cycle `N=24,k=1` enumerator/export still pending in accessible corpus |
| Genesis reduced-sector saturation ceiling | `RTG_GENESIS_GEOMETRY_DSN_v2.8.4 §6.6`, RID `GEN-ART-SATURATION` | NG-10 only | verified unchanged: `Q_d* approx 1.13e-2`, reduced birth-race scope retained |

`[GUARD]` Pointer refresh never upgrades claim status. Owner-source RIDs/sections govern imported scientific claims. Audit memos and reproduction scripts may support provenance checks but do not replace a missing owner DSN.

### §9.2 Artifact Registry

| Artifact | Role | Status |
|---|---|---|
| `NG_C7B_DISC2_PREREG_v1.md` | frozen DISC-2 fresh-domain / same-realization protocol; `k`-axis unchanged | `[CLOSED frozen protocol]` |
| `disc2_supplementary_enumerator_v3_1.py` + `disc2_enumeration_sup_d345.json` + `disc2_transport_sup_d345.json` | registered supplementary-family enumeration; pinned owner triple-equivalence; 10368 seeds / 41472 records / witness transport provenance | `[NUM/ENG provenance]` |
| `disc2_witness_report_v2.py` + `disc2_harness_result.json` + `disc2_witness_report.json` | sealed-harness cross-check, six-verdict reporting, blindness / label-projection record | `[RESULT/NUM provenance]` |
| `disc2_ratification_audit_v1.py` + `disc2_ratification_certs.json` | A1 exhaustive owner recount; A2 fixed-old-class defect certificates (C7B-ALG-T4); A3 membership; A4 boundary block; A5 descriptive concentration | `[RATIFICATION audit]`; cert JSON canonical **LF** |
| `NG_C7B_DISC2_RESULT_v1.md` | PI-ratified DISC-2 result and complete artifact/hash manifest; ten-label dynamic lower bound | `[RESULT] [from: ALG]` — finite exact `[ALG]` certificate on the registered panel |
| `NG_EXTERNAL_REVIEW_v118_RESPONSE_v1.md` | reconciliation of the independent v1.18 external review against the current owner; verifies I1–I7/P1–P3/5.1/5.2 and routes P2 to a dedicated post-hoc audit | `[AUDIT/RESPONSE]`, `3d12d9ae...7b3` |
| `disc2_p2_antipodal_exposure_audit_v1.py` + `.log` | post-hoc P2 antipodal-endpoint exposure audit: 40/136 convention-exposed, 96 unexposed; tested reverse/inert diagnostics preserve the ten-label projection | `[POSTHOC-DIAG]`, script `89a1466f...e1c`, log `51cde879...c47` |
| `disc2_p2_antipodal_exposure_annotation_v1.json` | per-witness annotation companion preserving the frozen ratified witness report; records `CONVENTION-EXPOSED` status and diagnostic-policy outcomes for all 136 ratified DISC-2 witnesses | `[POSTHOC-DIAG provenance]`, `43d28360...d550` |
| `NG_DISC1_DIAG3_RESULT_v3.md` | frozen-panel realization-sensitivity / witness-provenance diagnostic: the dynamic-pass predicate does not factor through reduced class, conserved spectrum, unmarked eventual cycle, or marked first-entry state; motivates the WD-DOM caution; no admission-rule change | `[POSTHOC-DIAG]`, non-admission evidence, `50972b58...3c72` |
| `NG_C7C_WD_C7C0_DESIGN_v1.md` | C7C-WD framework: `R_pair`/`R_bd`/`==_Q`, typed signatures, WD-PHYS/CLOSE/DOM/VAL/DESCENT/REP; C7C-0 design | `[DEF]` framework, `2ca016d4...33d782` |
| `NG_C7C0_RECIPROCAL_CERT_v2.md` | C7C-0 reciprocal theorem closure; `R_pair`/`R_bd` split repairs the v1 circularity; `Q_RTG^bd` reciprocal-closed; `Q_RTG^dyn` withheld | `[RESULT][from: ALG]`, archival `5abd130d...5c723e` (v1 superseded) |
| `NG_C7C_M_DESIGN_v1.md` | design-only shared-stream chain-composition candidate; exact multiplicative defect identity verified; physical carrier closure/global WD-DOM not yet certified; M-4 search held pending P2 policy | `[DESIGN ONLY]`, `2fb4ed9d...dbb9d` |
| `NG_TO_TDRG_REPRODUCIBILITY_GAP_v2.md` | governance note to the Discrete Genesis owner: BIND3 reproduction contract incomplete; v1.19 adds a required successor action for the P2 antipodal-endpoint presentation-covariance policy | `[GOVERNANCE]` — v2 pending; **v3 owner-policy update required before future SWAP/P3 campaigns** |
| `ng_n1c_dyad_radial_memory_v1.py` | original exact-map `q_*` witness and long-block audit | `[NUM]` |
| independent N-1C audit script/log supplied 2026-08-26 | independent bisection, 3000-block audit, phase-uniform numerical sweep, F1 falsification | `[NUM]` |
| `ng_l1_primitive_contraction_cert_v1.py` | exact symbolic primitive-map L1 certificate | `[RESULT] [from: ALG]` support artifact |
| `ng_l1_primitive_contraction_cert_v1.log` | execution record; all symbolic assertions pass | `[NUM]` execution record of algebraic certificate |
| `NG_L1_PRIMITIVE_CONTRACTION_CERT_v1.md` | human-readable L1 theorem/proof certificate | `[RESULT] [from: ALG]` documentation |
| `NG_N1_UNIFIED_T_ALIGNMENT_CERT_v1.md` | six-phase tube, primitive event alignment, orbit-level non-collapse, free-monogenic universal property | `[RESULT] [from: ALG]` documentation |
| `NG_N2_SIGNED_HISTORY_COMPLETION_CERT_v1.md` | pair-equivalence construction, injective embedding, infinite-cyclic Grothendieck completion, non-reversal interpretation | `[RESULT] [from: ALG]` documentation |
| `NG_N3_REPRESENTATION_LAYER_CERT_v1.md` | N-3A one-chart deck triviality, N-3B character isomorphism, N-3C pullback/mixing, N-3D finite-character quotient | `[RESULT] [from: ALG]` (N-3A, N-3C) · `[THM]` (N-3B, N-3D) documentation |
| `NG_N3C_PLUS_OPEN9_PROJECTOR_CERT_v1.md` | roots-of-unity vector projector, p=6 support audit, q=4 p=8/p=12 representation-vs-cascade boundary | `[ALG]` documentation |
| `ng_n3c_plus_projector_cert_v1.py` | exact residue/support micro-certificate; deliberately excludes nonlinear OPEN-9 coefficients | `[ENG/ALG audit]` |
| `ng_n3c_plus_projector_cert_v1.log` | execution log for the residue/support micro-certificate | `[NUM/ENG audit]` |
| `NG_NG8A_ORBIT_CARDINAL_CERT_v1.md` | NG-8A post-event orbit-equinumerosity theorem; fixes event/state off-by-one convention | `[RESULT] [from: ALG]` documentation — relayed to corpus 2026-08-28; cross-checked consistent with the independent re-certification (`NG_NG8AB_CROSSCHECK_v1.md`) |
| `NG_NG8B_REBLOCK_MULT_CERT_v1.md` | NG-8B inherited-freeness and physical re-blocking/multiplication compatibility theorem | `[RESULT] [from: ALG]` documentation — relayed to corpus 2026-08-28; cross-checked consistent with the independent re-certification (`NG_NG8AB_CROSSCHECK_v1.md`) |
| `NG_NG8AB_INDEPENDENT_RECERT_v1.md` | independent in-corpus NG-8A/NG-8B re-certification; explicit PREMISE-1/PREMISE-2 record, off-by-one and grouping verification | `[RESULT] [from: ALG]` independent re-certification |
| `ng8ab_independent_recert_v1.py` | exit-code-gated word-algebra certificate for NG-8A/NG-8B; 15 assertion families | `[ENG/ALG audit]` |
| `ng8ab_independent_recert_v1.log` | execution record; all pass, exit 0 | `[NUM]` execution record |
| `NG_NG8AB_CROSSCHECK_v1.md` | three-way cross-check: external NG-8 certificates vs independent re-certification vs DSN text; counting-convention table; zero material discrepancies | `[ENG audit]` cross-check record |
| `NG_N5AS1_SECTION_SEARCH_v1.md` | original N-5A-S1 pre-registration and 240-step short-horizon run | `[COR at v1.7.1]` original finite-horizon verdict superseded |
| `ng_n5a_s1_section_search_v1.py` / `.log` | original 240-step exact-map run (dps=50); reproduces short-horizon `{6}` alias | `[NUM]` retained provenance |
| `ng_n5a_s1_rotation_obstruction_v1.py` / `.log` | original 12-section short-horizon sweep and rotation diagnostic | `[NUM]` retained; obstruction interpretation corrected at v1.7.1 |
| `NG_N5AS1_INF_REDUCTION_v1.md` | N-5A-S1-INF reduction: sign convention pinned, `O(Q^2)` hypothesis falsified and corrected to `O(Q^(3/2))`, three lemmas named, INF-1/INF-2 combination theorems proved | `[RESULT][from: ALG]` + `[COR][from: NUM]` |
| `ng_n5as1_inf_reduction_cert_v1.py` / `.log` | exit-code-gated certificate; remainder-exponent scaling test, backbone drift, defect growth, counting identity | `[ENG/ALG audit]` |
| `NG_N5AS1_GAPLOCK_PARTIAL_v1.md` | GAP-LOCK Lemmas 1–2 CLOSED: local alphabet `{6,7}`, infinitely many 7-gaps, bookkeeping `E_B=s+O(1)`, physical count law; superseded only on Lemma-3 status by the closure record | `[RESULT][from: ALG]` + `[COR]` record |
| `NG_GAPLOCK_LEMMA3_CLOSURE_v3.md` + `ng_gaplock_lemma3_cert_v2.py/.log` | Lemma 3 CLOSED by the exact event-time defect identity; certificate finite facts only; v1 bootstrap retracted as circular | `[RESULT][from: ALG]` + `[COR]` provenance |
| `NG_N5C6_CANONICAL_PAIR_FALSIFIER_v1.md` | N5-C6 theorem: canonical A/B pair has unbounded bounded-defect candidate for every positive rational `p:q`; density limit remains 6 | `[RESULT][from: ALG]` conditional on N-5-COMM-BD definition |
| `ng_n5c6_canonical_pair_falsifier_v1.py` / `.log` | exit-code-gated algebraic audit of zero-slope uniqueness/reblocking cases | `[ENG/ALG audit]` |
| `N5-C1–C4 in-ledger proofs (v1.15)` | relational defect definition, finite-origin invariance, rescaling, reduced-class uniqueness using prefix-cofinal repeatability | `[RESULT][from: ALG]` — no separate external certificate yet |
| `C5-SYN-13 in-ledger control (v1.15)` | synthetic periodic `13:2` bounded positive control plus neighboring linear-failure control | `[RESULT][from: ALG]` — not an RTG physical realization |
| `N5-PHYS-1 in-ledger proof (v1.15)` | opposite phase-coincidence `B_+ / B_-` strict alternation and uniform `1:1` discrepancy bound | `[RESULT][from: ALG]` — local continuous-dyad physical witness |
| `N5-C7A in-ledger theorem (v1.15; notation corrected at v1.16)` | well-defined unique positive-rational invariant on every certified bounded physical pair; current notation `1 in Q_RTG^bd` | `[RESULT][from: ALG]` |
| `C7B-DISC-1 protocol (v1.15)` | frozen pre-data TDR-G SWAP/P3 discrimination architecture; historical pre-registration record | `[CLOSED protocol; superseded status by v1.16 result]` |
| `NG_DISC1_RESULT_v4.md` + `disc1_result.json` | ratified DISC-1B PASS / DISC-1D PASS-INT; `2,3 in Q_RTG^dyn`, no exhaustiveness claim | `[RESULT][from: ALG]` |
| `disc1_safeguards_v2.py/.log` + `genesis_mode_b_mc_v18.py` | owner differential, independent recount, fixed-period control, archetype regression; all safeguards pass | `[NUM/ENG provenance]` |

| `ng_n5as1_gaplock12_cert_v1.py` / `.log` | 7 assertion families incl. scope-necessity demonstration; exit 0 | `[ENG/ALG audit]` |
| `NG_N5AS1_CLOSURE_VERIFICATION_v1.md` | independent verification of the closure incl. the exact `dQ = -Q^2` cross-check and L-MONO sharpening; its v1.12 physical-slip-rate promotion is scope-corrected by `NG_N5AS1_SLIP_RATE_SCOPE_AUDIT_v1.md` | `[RESULT][from: ALG]` for closure cross-checks + `[COR]` on slip-rate interpretation |
| `ng_n5as1_closure_verification_v1.py` / `.log` | 11 assertion families, exact symbolic + high-precision, exit 0 | `[ENG/ALG audit]` |
| `NG_N5AS1_SLIP_RATE_SCOPE_AUDIT_v1.md` | v1.12 scope audit: separates theorem-grade defect threshold rate from still-open physical 7-gap locking; corrects offset/Fatou wording | `[COR]` + `[RESULT][from: ALG]` routing memo |
| `NG_TO_DYAD_RELAY_RIEMANN_LENS_v1.md` | relay to Dyadic owner: `Q_true` unique invariant form, `tau = 1/sqrt(det g)`, cubic-parabolic class | `[RESULT][from: ALG]` relay — not claimed in NG |
| `ng_riemann_lens_cert_v1.py` / `.log` | 8 assertion families, exit 0 | `[ENG/ALG audit]` |
| `NG_N5AS1_INF_EXTERNAL_BRIEF_v1.md` | filtered external-reviewer briefing (scope firewall, three lemmas, literature map) | `[ENG]` briefing |
| `NG_N5AS1_INF_CLOSURE_v1.md` | exact local closure of L-BACKBONE/L-MONO/L-PHASE; logarithmic defect/count theorem; Gate 2 + ALG Gate 5; N-5A-S1 closure | `[RESULT][from: ALG]` + `[COR][from: ALG]` |
| `ng_n5as1_inf_closure_cert_v1.py` / `.log` | exact symbolic primitive-map certificate for one-step rotation, six-step cubic phase shear, and nonzero quartic `Q^(3/2)` angular term | `[ENG/ALG audit]` |
| `NG_N5AS1_GATES134_CERT_v1.md` | gates 1/3/4 package: exact section identity and structural local-tube predicate/co-realization/order, plus finite-orbit regression witnesses | `[RESULT][from: ALG]` structural core + `[NUM]` orbit witnesses; v1.9.1 scope-calibrated |
| `ng_n5as1_gates134_cert_v1.py` / `.log` | 13-family executable regression on the seed orbit; reproduces detector, anchors and interleaving word | `[NUM/ENG audit]`; structural ALG closure is supplied by the DSN proof statements |
| `NG_N5AS1_LOGSLIP_VERIFICATION_v1.md` | independent confirmation of the correction (different crossing detector, dps=60); quantitative geometric slip law; `sqrt(rho)` section-cluster check; ALG route to gate 2; non-relabeling≠incommensurability caution | `[RESULT][from: NUM]` + `[ALG argument]` |
| `ng_n5as1_logslip_verification_v1.py` / `.log` | independent detector rerun + 4e6-step slip-law test | `[NUM]` |
| `NG_N5AS1_LONG_HORIZON_CORRECTION_v1.md` | correction memo: high-precision 7-step slip, retraction of v1.7 obstruction, revised N-5A-S1 routing | `[COR]` + `[NUM]` |
| `ng_n5a_s1_long_horizon_recheck_v1.py` / `.log` | 60-dps decisive recheck plus 12-section long sweep | `[NUM]` corrective audit |
| `NG_N2ORD_PHYSICAL_ORDER_CERT_v1.md` | N-2-ORD closure: reachability order, shift covariance, positive cone, physical sign realization, `Q_true` witness, flagged P3 premise, demonstrated non-claims | `[RESULT] [from: ALG]` documentation |
| `N-2-ORD P3 in-ledger refinement (v1.19)` | derivative lower-bound on `|rho|,|eta|<=1/10`; existential tube shrunk inside the box; injectivity, ORD-2 reflection, and cross-orbit merge criterion promoted on that scope | `[RESULT][from: ALG]` — no explicit maximal-radius/seed-inclusion certificate |
| known consumer: `RECOG v0.3.5` / `RECOG-ALG-LATTICE-CLOCK` | consumes `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO`, repinned upstream to Number Genesis v1.20.4 (RECOG v0.3.5, pre-freeze sync of 29 Sep 2026); RECOG additionally cross-references GAP-LOCK Lemma 3 at heuristic grade (HEUR in RECOG's own ledger; defect-threshold and physical event sequences are not identified term by term) | `[PROVENANCE]` consumer record, not a theorem change |
| working-methodology references (noncanonical) | PRR / RRF v0.6 (still noncanonical; candidate for PI adoption) — typed partial composition, interface identification/transport vocabulary | `[PROVENANCE]` only; no theorem import; no `RRF-*` profile as canonical fact |
| `NG-7A abelian fundamental-cycle extension (v1.19)` | spanning-forest integration proves zero fundamental integral cycle sums imply exact node-potential data over any abelian coefficient group, including `Z_N`; nonprimitive rescaled bases excluded | `[RESULT][from: ALG]` — in-ledger extension; no new physical-source claim |
| `ng_n2ord_order_cert_v1.py` | exit-code-gated certificate; abstract order layer + exact primitive-map layer (dps=60); 14 assertion families | `[ENG/ALG audit]` |
| `ng_n2ord_order_cert_v1.log` | execution record; all pass, exit 0 | `[NUM]` execution record |
| `NG_NG7A_HOLONOMY_NULL_CERT_v1.md` | NG-7A closure: null theorem, completeness, orientation/gauge/basis invariance, typed statistic, separation, `Z_N` zero-control, guards, OFN export note | `[RESULT] [from: ALG]` documentation |
| `ng7a_holonomy_null_cert_v1.py` | exit-code-gated exact certificate; 12 assertion families over ℚ and `Z_N` | `[ENG/ALG audit]` |
| `ng7a_holonomy_null_cert_v1.log` | execution record; all pass, exit 0 | `[NUM]` execution record |
| `RTG_NG_PROGRAMME_REVIEW_AUDIT_v1.md` | independent programme-review/state audit; pointer revalidation and DZT-state report | `[ENG audit memo]` — not owner-source replacement |
| `ng_review_dzt_independent_audit_v1.py` | independent numerical reproduction of audit-reported DZT norm laws for 60 points `p=12..248` | `[NUM]` audit support — no NG claim promotion |
| `NG_C7C_M2_PREREG_DRAFT_v4.md` (`248f128c…8987`) + `NG_C7C_M2_PREREG_FREEZE_MANIFEST_v1.md` (`cefb7180…b165b`) | frozen C7C-M2 preregistration (interface object, germ calculus, κ_b registry, WD-DOM quantifiers, N1/N2, evidence guards) | instrument; frozen before any case was examined |
| `NG_C7C_M2_CENSUS_PROTOCOL_v1.md` (`f2a4a9a4…5795`) | evidence-sufficiency census protocol (F1–F7; replay contract) | instrument; frozen |
| `NG_C7C_M2_CENSUS1_UDYAD_RESULT_v1.json` (`ed3c72af…eae9`) + `NG_C7C_M2_CENSUS1_UTDRG_RESULT_v1.json` (`23f298dc…d33a`) | Census-1 results: 2/2 dyad and 118/158 TDR-G records admissible; 40 excluded by P2 quarantine only | census record; not a scientific claim |
| `census1_tdrg_replay_v1.py` (`73cfa2e3…8188`) + manifest (`19e929aa…a30a`) + records (`7b7dc451…77c8`) | C-1 replay: 158/158 reproduce sealed fields, stepwise agreement, owner-v18 lockstep | reconstruction record |
| `NG_C7C_M2_ANALYSIS_OPENING_MANIFEST_v1.json` (`d170efb5…5d73`) + `NG_C7C_M2_ANALYSIS_LOG.md` (`e7b85fd2…0139`) | evidence set fixed at the start of outcome inspection; append-only analysis E0–E6 | analysis record — outcome INCONCLUSIVE / INCONCLUSIVE |
| `NG_C7C_M2_E4_TDRG_DENSITY_v1.json` (`c67342a9…6fa8`) | exact ordered TDR-G event densities; 15 classes | supporting analysis record |
| `NG_SELFCHECK_REFERENCE_TRANSPORT_v1.md` (`b39de45c…ded4`) + `ng_rf06_token_shift_spotcheck_v1.py` (`2a064eb9…f148`) | RF-06 self-check; token-shift equivariance on the no-birth SWAP/P3 route | review record; finite spot check plus code reading |

---

## Appendix A. Working Thesis

> **RTG Number Genesis treats relational arrows/transitions and their certified composition as physically prior to numerical labels. Repeatable endomorphism histories, orientation-sensitive comparisons, finite multiplicities, cyclic/character structures, and commensurability relations are then represented by familiar number systems. Neither additive/difference nor ratio/proportion notation is universally primitive without a certified sector mechanism and gauge.**

Epistemic status at v1.20: explicit-domain boundary CLOSED via `DYAD-THM-PRIM-CTR` (seed `(1/100,1/250)` in `U`; whole explicit tube inside the P3 injectivity box; L1 ownership unchanged); C7C-M partially resolved (M-1A/M-1B `[ALG]`, unrestricted closure and naive label-only WD-DOM fail, interface-typed WD-DOM OPEN); `C_NG` reframed as a typed relational architecture with partial physical composition; D15 SYNC COMPLETE; SG-NG-18 is a typed-object non-conflation guard with upstream provenance resolved. **Historical status narrative (v0.4→v1.19), moved verbatim from the header at v1.20:**

 Active foundational programme. RTG already supplies relational primacy, gauge-only absolute phase, relational event sequence rather than external physical time, a continuous dyadic phase/winding structure, and a finite discrete phase universe on `Z_N`. The central thesis — **number systems as representations/invariants of certified relational composition, repetition, comparison, and multiplicity rather than primitive physical containers** — remains `[HYP]`. Standard mathematical constructions (free monoid, group completion, circle characters, cyclic-group characters) are metalanguage inputs; scoped RTG-native physical realization is now certified for the local Track-A `N`-like and `Z`-like structures, while larger number systems, universality, and cross-track compatibility remain OPEN. **v0.4 closed N-1A2** for the scoped abstract three-node boundary-aware phase-step model. **v0.5 closed N-1B-MIN `[ALG]` `[scope: abstract fixed-support oriented recurrence on `S^1`]`.** **v0.6 sharpens N-1C by introducing operational history equivalence:** two histories are physically equivalent when no admissible relational continuation and observable can distinguish them. Under this criterion the memoryless wrapped-`S^1` recurrence does **not** realize free physical counting at a rational return: same-endpoint loop histories collapse whenever the complete future dynamics factor only through the wrapped instantaneous state. This is recorded as a scoped `[FAIL]`, not as failure of Number Genesis. The result identifies the missing ingredient precisely: a physically effective relational memory variable or cocycle that survives recurrence and can affect future relational observables. Dyadic winding is retained as a candidate representation, but its present DSN status is not yet sufficient to certify it as such a physical memory because the winding index is explicitly invisible to trigonometric observables. **v0.7 added a scoped positive dyadic realization** but its primitive-frame remainder was subsequently audited and corrected. **v0.8 closes L1 directly from the exact primitive map:** for `F=T^6`,

`Q_true(Fx)-Q_true(x) = -Q_true^2 + O(Q_true^(5/2))` uniformly in phase, with the entire degree-5 correction extracted exactly. Hence a sufficiently small punctured primitive sector has strict positive `Q_true` contraction under every block, unconditionally separating all finite block powers. The prior `Q_NF=Q_true` exactness claim and `O(Q^3)` primitive-frame remainder are entered as `[COR]`. **v0.9 closes the remaining primitive-generator alignment:** from any L1 base sector `U` with `F(U) subset U`, a sufficiently shrunken L1 base sector generates a six-phase tube `U_T = union_{j=0}^5 T^j(U)` contained inside the L1 neighborhood and invariant under `T`. One forward application of the exact primitive generator `T` defines the scoped counting type, successor is total on the tube, and L1 excludes every finite primitive-orbit collision `T^r x=T^s x` for `r!=s`. The induced transformation monoid is therefore free monogenic and canonically isomorphic, once `T` is fixed, to `(N,+,0)` in the mathematical metalanguage. **N-1 unified is CLOSED on this local primitive-dyad sector.** **v1.0 closes N-2 on the same Track-A object:** the cancellative free monoid `M_T` admits an RTG-native signed-history comparison construction on forward-history pairs `(A,B)`, with `(A,B)~(C,D)` iff `A o D = B o C`. The quotient is the Grothendieck group completion, the canonical embedding of `M_T` is injective, the inverse operation swaps comparison orientation rather than reversing the physical map, and the resulting group is infinite cyclic. Only after this construction is complete is it represented in the mathematical metalanguage as `(Z,+,0)`. **N-2 is CLOSED locally. v1.1 closes the continuous N-3 representation layer:** **N-3A** proves that the dynamically induced local `eta`-winding/deck map is identically trivial on a sufficiently small one-chart N-1 tube; **N-3B** constructs the faithful abstract isomorphism `G_T ~= widehat(S^1)`; **N-3C** derives the exact primitive pullback `T^* chi_m = exp(i m(exp(rho)-1)) exp(-i m sin eta) chi_m`, proving that the primitive dynamics does not translate character labels by a fixed integer and instead mixes harmonic sectors; **N-3D** closes the pure finite-character quotient `G_T/(N G_T) ~= widehat(C_N) ~= Z_N`, with all TDR-G dynamical content still behind the cross-branch firewall. **Track-A history and local eta-winding are therefore explicitly separated.** **v1.2 closes N-3C+ at the representation-kinematic level:** the correct vector conjugation projector gives charge `chi_p(a,b)=a-b-1 (mod p)` and recovers `a-b == 1 (mod p)` exactly; the first-nonlinear p-step term is the cyclic resonant average, so the primitive p=6 quadratic six-step cancellation is kinematic. A subgroup-projector comparison proves that the exact `p=8,q=4,(0,3)` cancellation versus `p=12,q=4,(0,3)` survival cannot be explained by q=4 character selection alone and is genuinely nonlinear/cyclotomic cascade information. Scalar Bessel residue projectors are recorded separately and explicitly guarded against identification with Birkhoff/Lie cascade coefficients. **v1.3 synchronizes the Number Genesis state with the current owner corpus:** current source pointers are refreshed; the stale N-3C+ `q=4,(0,3)` cascade item is CLOSED-by-import from Dyadic v6.4.9 `DYAD-THM-Q403-PHASELAW`; the remaining reachable-basis/missing-slot work is routed to the Dyadic arithmetic-dynamics interface rather than treated as a Number Genesis foundational target; N-5A, N-2-ORD, NG-8A/NG-8B, and the NG-7A/NG-7B split are registered as new OPEN/ALG targets; SG-NG-19 and SG-NG-20 are added. No new Number Genesis theorem is claimed by the v1.3 synchronization itself. **v1.4 is a paradigm-synchronization/content release:** it closes NG-8A and NG-8B from their executed algebraic certificates; makes explicit that the already-certified Number Genesis construction is composition-first and representation-after-construction; introduces a relational-category architecture in which admissible isomorphisms form a groupoid while physical dynamics generate endomorphism monoids; reframes N-5/N-6 as classification/representation of co-realized relational structures rather than ontological manufacture of ratio or continuum from arithmetic labels; adds the NG-0R relational-composition clarification and pre-registers a sector-covariance audit; and adds SG-NG-22, which forbids primitivity claims in either the additive or ratio direction without a certified mechanism and sector gauge. No theorem that ratio/proportion is universally more primitive than addition is claimed. **v1.5 closes NG-7A:** the additive recurrence-holonomy operator layer is certified — null theorem `C D^T = 0`, field-coefficient completeness `im D^T = ker(C·)` (so the holonomy vector `h=Ca` and the class `[a] in H^1(G;F) ~= F^beta` are equivalent complete obstructions), orientation/gauge/cycle-basis invariance, the PI-typed scalar-vs-multichannel statistic (`h` for `d=1`; `r_hol=rank(CA)` reserved for `d>=2`), operator-level separation of cycle capacity from holonomy content, and the mandatory TDR-G `Z_N` zero-control with unit-defect detection. NG-7B (physical source / non-Abelian) remains OPEN. **v1.6 closes N-2-ORD** by reachability-first physical order. **v1.7-v1.8 correct the finite-horizon N-5A-S1 obstruction and establish the quantitative LOGSLIP numerical pattern with SG-NG-23 protection.** **v1.9 closes the structural parts of N-5A-S1 gates 1, 3 and 4**: the canonical phase-coincidence transition predicate is lift-free and gauge-reduced, every such B-event is by definition co-realized with the primitive T stream on the certified local tube, and N-2-ORD supplies their common reachability order. The specific long numerical orbit remains a NUM witness unless its inclusion in an explicit certified tube is separately proved; gate 2 and the ALG form of gate 5 remain OPEN in N-5A-S1-INF. **v1.10 reduced N-5A-S1-INF to L-BACKBONE/L-MONO/L-PHASE and exposed the false `O(Q^2)` phase-remainder hypothesis. v1.11 closes all three lemmas from the exact primitive map/L1, upgrades the correction to exact Taylor algebra, proves `D_M=tau log M+O(1)` and `N_B(M)=M-(tau/2pi)log M+O(1)`, and closes N-5A-S1 (Gate 2 + ALG Gate 5). N-5 is now the active in-branch frontier.** **v1.12.1 separates the theorem-grade phase-defect threshold rate from the then-open physical 7-gap locking. v1.13 closes GAP-LOCK Lemmas 1–2: the local return alphabet is `{6,7}`, `E_B(M)=s(M)+O(1)`, and `s(M)=(3 tau/pi) log M+O(1)` is a physical 7-gap count law; GAP-LOCK Lemma 3 (within-cell locking / physical consecutive-ratio limit) remains OPEN. v1.14 synchronizes those results into the live module and adopts N-5-COMM-BD as the active bounded-synchronization commensurability target under new SG-NG-24. N-5 remains OPEN; no Q-like class is claimed closed.** **v1.15 closes the C1–C4 commensurability structure, adds SG-NG-25, closes the C5 synthetic control and C6 falsifier, closes the first genuine physical `1:1` witness N5-PHYS-1, and closes C7A as a unique realized-rational label theorem. C7B/C7C and full `Q` realization/arithmetic remain OPEN.** **v1.16 synchronizes two post-v1.15 closures: GAP-LOCK Lemma 3 is CLOSED `[ALG]` by the exact event-time defect identity, proving the physical consecutive 7-gap ratio limit `exp(sqrt(3)pi/6)`; and the frozen TDR-G DISC-1 campaign closes DISC-1B PASS and DISC-1D PASS-INT, establishing `{2,3} subset Q_RTG^dyn` with currently established dynamic labels `{2,3}`. The bounded/dynamic spectrum split is now explicit: `Q_RTG^bd` is bounded physical realization; `Q_RTG^dyn` requires the frozen same-realization stability+contingency gate. C7B breadth and C7C physical arithmetic remain OPEN; no exhaustiveness theorem is claimed.** **v1.17 is a documentation-only owner synchronization of the ratified C7B-DISC-2 campaign.** The frozen DISC-2 protocol applied the already-certified `k`-axis to the fresh owner-registered supplementary one-pass seed family (`|d|_c=3,4,5`, 10368 seeds): B-check PASS, D-check PASS, 136 same-realization witnesses (130 `PASS_INT`, 6 `PASS_BDY_ONLY`), admitting eight new labels. Currently established dynamic labels are therefore `{1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4} subseteq Q_RTG^dyn`, a certified lower bound and **not** an exhaustiveness theorem. `1` is separately established in `Q_RTG^bd` (N5-PHYS-1 positive control) and in `Q_RTG^dyn` (26 DISC-2 witnesses). C7B-DISC-1 and C7B-DISC-2 are CLOSED; **C7B global breadth and C7C remain OPEN.** No new theorem is claimed by this synchronization itself. **v1.18 synchronizes two post-v1.17 items.** (i) The **C7C-WD well-definedness framework is ADOPTED** (pre-bounded carrier `R_pair`, bounded carrier `R_bd subseteq R_pair`, representation equivalence `==_Q`, typed operation signatures, and the five obligations WD-PHYS / WD-CLOSE / WD-DOM / WD-VAL / WD-DESCENT with arithmetic compatibility WD-REP only afterward), and **C7C-0 is CLOSED `[RESULT][from: ALG]`**: the orientation swap `S(A,B)=(B,A)` is a carrier-preserving involution with `rho_Q(Sx)=rho_Q(x)^(-1)`, so `Q_RTG^bd` is closed under `r -> r^(-1)`. No `Q_RTG^dyn` reciprocal-closure theorem is claimed. Full C7C (multiplication, addition, laws) remains OPEN; **C7C-M design is the next active target.** (ii) A pre-existing provenance defect is repaired: `SG-NG-26` was invoked in the DISC material but never defined in section 3, and the C7B transport lemmas were cited as naked `T1/T2/T4`, colliding with N-2-ORD `T4`. They are now defined as **`SG-NG-26`** and the namespaced **`C7B-ALG-T1..T4`**. **v1.19 is an external-audit reconciliation and precision release.** It incorporates independently verified domain/observable/index corrections without reopening the local N-1/N-2/N-5/GAP-LOCK theorem chain; strengthens N-3C+ to require `ord(lambda)=p`; qualifies C2 to same-sector/cofinal-tail origin shifts; corrects the reblocking control and physical-slip indexing; makes the NG-7A unit-defect premise cycle-sensitive; records the upstream `37/40` frame-provenance issue without resolving it inside Number Genesis; assigns a dedicated RID to the defect-threshold ratio theorem; and registers two algebraic refinements from the audit (P3 injectivity on a sufficiently shrunken tube and fundamental-cycle completeness over abelian coefficient groups). A post-hoc DISC-2 presentation-covariance audit finds 40/136 ratified witnesses convention-exposed at the antipodal endpoint tie, but 96 unexposed witnesses remain and every one of the ten admitted labels has at least one unexposed witness; the ten-label lower bound therefore remains unchanged. Discrete-Genesis owner action on the antipodal policy remains pending. C7C-M stays the next arithmetic target, but no M-4 realization campaign is opened before that policy ruling.

Historical (v1.19): `[HYP]` programme thesis plus `[DEF]/[INTERP]` paradigm clarification. Track-A N-1 is a scoped `[RESULT][from: ALG]` local realization of a free endomorphism monoid and its N-like exponent representation; N-2 is its scoped signed-history completion and Z-like representation; N-2-ORD closes the physical order layer. N-3A–N-3D separate cover/winding, character, primitive pullback, and finite-character representations. NG-8A/B close the first finite-state equinumerosity and re-blocking multiplication seeds; NG-7A closes the additive holonomy operator/null layer while NG-7B remains OPEN. N-5A-S1 and GAP-LOCK Lemmas 1–3 are CLOSED locally; the physical consecutive 7-gap ratio is theorem-grade. At v1.15, N5-C1–C4 close the bounded synchronization commensurability structure, SG-NG-25 formalizes prefix-cofinal repeatability without external time, C5-SYN-13 supplies a noninteger mathematical control, and C6 proves the canonical primitive/section pair is density-resonant at 6 but not boundedly commensurate at any positive rational pair. N5-PHYS-1 supplies the first genuine physical bounded class through the opposite phase-coincidence streams `B_+`,`B_-`, with uniform discrepancy at `1:1`. C7A closes a well-defined unique positive-rational invariant on certified bounded physical pairs and gives `1 in Q_RTG^bd`. v1.16 closes C7B-DISC-1 with DISC-1B PASS / DISC-1D PASS-INT, establishing `2,3 in Q_RTG^dyn`. v1.17 records the ratified C7B-DISC-2 closure: B-check PASS / D-check PASS on the fresh registered supplementary family, 136 same-realization witnesses (130 interior, 6 boundary-only), eight new labels, and `1 in Q_RTG^dyn` established separately from the N5-PHYS-1 bounded control. The currently established dynamic lower bound is `{1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4} subseteq Q_RTG^dyn`, not an exhaustive spectrum. **C7B global breadth remains OPEN.** v1.18 adopts the C7C-WD well-definedness framework and closes C7C-0: `Q_RTG^bd` is reciprocal-closed via the orientation-swap involution, with no `Q_RTG^dyn` analogue claimed. **Full C7C arithmetic remains OPEN; C7C-M design is the next active sub-target, and WD-DOM (domain congruence) is its load-bearing obligation.** v1.19 reconciles the external audit: the ten-label DISC-2 lower bound survives a post-hoc presentation-covariance exposure audit because every label retains at least one unexposed witness, while 40 individual witness records are explicitly convention-exposed; P3 injectivity is promoted to `[ALG]` on a sufficiently shrunken tube; fundamental-integral-cycle completeness is added over abelian coefficient groups; and the remaining I1–I7/P1 precision corrections are synchronized without reopening prior theorem closures. N-5 is therefore scientifically advanced but not a derivation of the full field `Q`. N-6 remains representation/recovery level in the continuous branch under SG-NG-19. Full functorial cross-track compatibility remains OPEN.

---

## Appendix B. Rejected / Guarded Formulations

`[REJECTED v1.20]` **Unrestricted chain composition is closed on `R_bd`.** Counterexample: `x ∘ Sx = (A,A) ∉ R_pair` for every `x ∈ R_bd`.

`[REJECTED v1.20]` **`C_NG` is a category.** Global physical composition is partial, interface-sensitive, and without identities on the physical carrier; only certified sectors carry category/groupoid/monoid/group structure.

`[REJECTED v1.20]` **Naive label-only WD-DOM holds for the chain domain.** `D_chain` is not saturated under `==_Q`; a richer interface-typed saturated carrier remains the open question and is not excluded.

`[REJECTED v1.18]` **Equal rational label ⟹ physical interchangeability.** `x ==_Q x'` is representation equivalence; it does not license substituting `x'` for `x` as the input of a physical operation. WD-DOM must be proved (or the operation typed to a saturated sector) before descent. The label `1` already has bounded realizations in two disjoint families under different branch firewalls.

`[REJECTED v1.18]` **`Q_RTG^bd` reciprocal closure ⟹ `Q_RTG^dyn` reciprocal closure.** C7C-0 is a theorem about bounded classes only. The dynamic gate is a predicate on the *ordered* pair under a deformation family; its `A <-> B` equivariance is a separate, unproved theorem.

`[REJECTED v1.19]` **Agreement with a pinned owner implementation ⟹ presentation covariance.** Exhaustive one-step equality to `genesis_mode_b_mc_v18.py` establishes implementation agreement. It does not prove node-relabeling covariance of a tie-break rule. The P2 antipodal-endpoint audit exposes this distinction directly; affected witness records remain provenance-annotated until the Discrete owner supplies a policy ruling or presentation-independent selection theorem.

- `[REJECTED as too strong]` “Frequency is the RTG number line.”
- `[REJECTED as circular]` “Assume arbitrary real-valued frequency ratios and derive the real continuum.”
- `[REJECTED as too strong]` “Ratio/proportion notation proves that multiplicative or geometric arithmetic is ontologically prior to additive arithmetic.”
- `[REJECTED as circular]` “Treat a primitive relational arrow as an already-real-valued ratio and then derive rational/real number structure from it.”
- `[REJECTED as false mechanism]` “`arg:U(1)->R` is a nontrivial global continuous additive homomorphism.”
- `[GUARDED]` “Ratio-relational” means an arrow/comparison with a certified quotient/scaling interpretation at the stated scope; it does not mean a primitive rational number.
- `[REJECTED]` “Group completion proves physical time reversal.”
- `[REJECTED]` “`Z_5` and natural number 5 are the same object.”
- `[REJECTED as overclaim]` “Pontryagin duality proves RTG derives integers from nothing.”
- `[REJECTED as overclaim]` “Number Genesis solves UV divergences / quantum gravity / fine tuning.”
- `[GUARDED]` “Discrete `Z_N` is the continuous `S^1` theory discretized.” Only the representation-theoretic roots-of-unity/character relation is currently admissible.
- `[REJECTED as too coarse]` “A rational limiting event-density is already a physical rational commensurability class.” SG-NG-24 requires a certified bounded synchronization defect or another separately justified common-measure criterion.
- `[REJECTED as external-time smuggling]` “`N_B -> infinity` means evolution along an already-existing continuous time parameter.” Under SG-NG-25 it means only cofinal unboundedness of finite event counts under relational prefix extension.
- `[REJECTED as overclaim]` “One physical `1:1` bounded pair proves RTG realizes all positive rationals.” C7A proves a unique rational invariant on bounded physical pairs; C7B breadth remains OPEN, and bounded realization must not be conflated with `Q_RTG^dyn`.
- `[REJECTED as overclaim]` “A realized rational label automatically supplies rational addition and multiplication.” C7C remains OPEN until physical operations on commensurability classes are certified.

---

## Changelog
### v1.20.7 — October 1, 2026

**Owner synchronization + scoped algebra adoption + governance repair.** No theorem-level result changes except the adoption of M2-1, an algebraic identity proved before any outcome inspection.

**1. C7C-M2 outcome sync (scientific sync).** The frozen C7C-M2 instrument and Census-1 are recorded (§6.6 and §9.2 pins). Outcome INCONCLUSIVE / INCONCLUSIVE: no admitted nondegenerate composable source chain exists in Census-1 evidence at either level. This states neither that WD-DOM holds nor that it fails. Full-interface typed WD-DOM remains OPEN; M-4 remains HOLD pending the Discrete-owner P2 ruling. The missing evidence object — a certified composable three-stream witness — enters the queue as an evidence shape, with no search authorized.

**2. M2-1 adopted (scoped algebra).** The transported chain identity, a strict generalization of M-1A under bounded interface transport, enters the owner at ALG grade, with its transport definition and a no-closure guard: it establishes no Π, WD-DOM, carrier closure or admitted chain. M2-0 and M2-2 remain internal to the preregistration.

**3. RF-06 scope note (governance).** The imported row-1a statement is kept verbatim (K4). A scope guard fixes: global phase is the only unrestricted gauge; the transition state carries tokens (OFN SG-OFN-STATE); a common token shift is not a gauge of the star rule (OFN RTG-OFN-ALG-STAR-TOKEN-SHIFT); on the frozen no-birth DISC SWAP/P3 route it is equivariant, so the DISC reduced key stands at that scope. The source-side correction belongs to Discrete Genesis.

**4. Queue and §8 synchronized** with the C7C-M2 live state; §2 and §8 remain consistent.

**5. Methodology normalization (no scientific-state change).** Ten bare RESULT tags that are pure mirrors of already-ruled owner rows are paired with "from: ALG" under K5: the §5 ten-label row, the two §6.6 DISC summaries, the §6.6 C7C-M summary, the `1 in Q_RTG^dyn` statement, the §9.2 DISC-1 result row, the §6.3a N-2-ORD summary, and the three §8 closure summaries (NG-8A/NG-8B, NG-7A/N-2-ORD, foundational chain). Every summarized owner was checked to be single-grade ALG.

**6. Remaining grade items resolved before freeze (co-owner ruling, `NG_V1207_REMAINING_GRADE_RULINGS_v1`).** Three rows bundled parts of different status and are split under K1/K2, with substantive wording preserved — no substantive proposition was reworded; only split-boundary punctuation/capitalization, the corresponding conjunction adjustment, and bold block labels were changed (itemized in the rulings record): the §6.6 C7C-WD / C7C-0 summary into a DEF (framework adopted), an ALG result (C7C-0 involution; Q_RTG^bd closed under reciprocals) and a GUARD (no Q_RTG^dyn reciprocal closure); the §8 N-5 summary into an ALG result (C1–C7A + DISC lower-bound synthesis), a GUARD (lower bound, not exhaustive) and an OPEN item (C7B global breadth, C7C physical arithmetic); the §8 paradigm note into status metadata, a DEF (composition-first, representation-after-construction) and a GUARD (no universal ontological-priority claim; sector-specific mechanisms and gauges required). Navigation phrases such as "certificates are registered below" are not graded (K1). Result: no live bare RESULT and no live combined truth-status tag.

### v1.20.6 — September 29, 2026

**Grade-normalization patch.** Applies the co-owner rulings recorded in `NG_V1206_RULING_LEDGER.json` (groups 1–3). No new result; every change re-expresses an existing claim's grade under Methodology v1.3, splits a block whose parts differ in status, domain or evidential basis (K2), or re-types a latent definition.

- `[COR v1.20.6]` The v1.20.4–v1.20.5 header described 19 live combined-grade rows as "independent grade-decision rows". Row-by-row normalization showed that this count included summary/module/provenance mirrors: the 19 raw rows resolve into **11 owner grade decisions** (rows 1, 6, 8, 10, 11, 14, 15, 16, 17, 18, 19) and **8 mirror synchronizations** (rows 2, 3, 4, 5, 7, 9, 12, 13). The §9.2 provenance mirrors are synchronization-only and outside the 19. Two latent substantive definitions were extracted into DEF blocks as a claim-typing correction; they are not grade decisions and are not counted.
- **§9.2 mirror count: five, not four.** Four §9.2 mirrors use the `[from: X/Y]` syntax; a fifth, the DISC-2 result row, was written `RESULT NUM/ALG under frozen protocol` without `from:` and was missed by the regex behind the earlier "four". It is synchronized under the same approved mirror rule; leaving it would have left the registry contradicting the DISC-2 owner grade.
- **Criterion K1–K6** (as amended by the co-owner): decompose by assertion (substantive definitions are DEF); split on differing status, domain/assumptions or evidential basis; standard mathematics is recorded in `Depends on:`/proof provenance, and `[scope: standard mathematical input]` is used only for background-standard claims; imports carry the source grade directly; mirrors synchronize without creating authority; THM vs ALG by claim form, not as a strength ladder.
- **Owner rulings.** Row 1 split into a DEF import (Discrete Genesis §6.1) and a THM import (§6.2, fixed node-count cap). N-3B and N-3D bodies THM (Depends on N-2 / N-3B). N-3C consequence and N-3C+ core ALG/RESULT from ALG; the `q=4,(0,3)` cascade is a pointer to its separate import. C5-SYN-13 split into DEF (control language and admissible prefix set) + RESULT from ALG; negative control RESULT from ALG. C7A split into the well-definedness synthesis, the bounded witness `1 ∈ Q_RTG^bd`, and a GUARD. NG-7A `Z_N` zero-control RESULT from ALG, finite checks as provenance. **DISC-1 and DISC-2** each split (required by K2) into a finite-scope ALG certificate, a RESULT from ALG breadth consequence and a RESULT from ALG dynamic-admission consequence; exact exhaustive integer verification on a registered finite panel is finite exact verification (Methodology v1.3 L716, L556), not NUM; membership in `Q_RTG^dyn` is existential and is fully discharged by exactly verified witnesses. Hashes are recorded as evidence, not in `[conv:]`. P2 exposure is a robustness record, not part of the admission grade; DISC-1: 0/22 witnesses exposed (post-hoc audit, v1.20.6).
- **Mirrors.** Rows 2, 3, 4, 7, 9 synchronized; rows 5, 12, 13 synchronized with their usage-boundary sentences separated as GUARD blocks.
- **K1 definition repair.** `Q_RTG^bd`, `Q_RTG^dyn` (one DEF) and the `rho_Q` map (a second DEF) extracted from the C7A COR note, which remains as the historical record of the v1.15 → v1.16 notation split. A definition of a map is kept separate from the proof that it is well-defined.
- **Carried forward, not changed:** one live combined truth-status tag DEF/INTERP in §8 (written without `from:`, outside the ruled inventory; found by the v1.20.6 verification scan over all slash-combined bracket tags in any syntax); 12 bare RESULT tags without a paired `[from:]` (a pre-patch count of 13 had also counted the §9.2 DISC-2 row, which is a combined mirror and is synchronized here); §9.2 artifact-role labels and the alias-table row `[ENG/NUM]` (not claim grades).

### v1.20.5 — September 29, 2026

**Consumer-sync patch.** Records upstream consumer state; no scientific result changes. The 19 grade-decision rows and their four §9.2 mirrors are untouched; grade normalization moves to **v1.20.6**.

- **RECOG consumer record updated.** RECOG v0.3.5 (pre-freeze Number Genesis sync, 29 Sep 2026) repinned its companion pointer to Number Genesis v1.20.4 and now imports `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` from v1.20.4 for `RECOG-ALG-LATTICE-CLOCK`. The §9 row no longer says RECOG "must repin". RECOG's new heuristic-grade cross-reference to GAP-LOCK Lemma 3 is recorded on the same row. (RECOG's grade is described in words, not as a bracketed tag, so a provenance row describing another ledger's grade does not become a Number Genesis claim block.) Remaining v1.15 source pins inside RECOG (`NUMGEN-RESULT-L1-PRIMITIVE-CONTRACTION`, `NUMGEN-OPEN-N1C`; content unchanged since v1.15) are RECOG's own records and are not edited here.
- **Dyadic consumer row: left to the Dyadic stream.** The §6.2 explicit-domain block and the §9.1 import row said the upstream Dyadic consumer-row sync was "deferred to the consumer-sync pass". This pass does not edit the Dyadic owner, so both now say the sync is left to the Dyadic stream's own owner pass. NUMGEN-side acceptance of `DYAD-THM-PRIM-CTR` (v1.20) is unchanged.
- **RRF pointer.** Working-methodology reference updated from RRF v0.4 to v0.6; status unchanged (noncanonical, candidate for PI adoption; no theorem import).
- **Version bookkeeping.** Status summary and methodology note carried to v1.20.5; the grade-decision pass is renumbered v1.20.6.

### v1.20.4 — September 28, 2026

**Scientific-sync + editorial/governance correction patch.** One live scientific-state synchronization (STOP-04); the other items change no scientific result. The 19 independent scientific grade-decision rows, and their four §9.2 provenance-registry mirrors, are deliberately untouched.

- **STOP-04 `[COR]` — NG-7 live-state sync.** §6.8 still said "If closed, this module may supply a concrete operator for the Foundations' currently OPEN distinction…", while NG-7A had already discharged the operator/null half and D15 is SYNC COMPLETE. Now: "NG-7A already supplies the certified additive operator/null half of the Foundations diagnostic. The remaining programme task is NG-7B: an RTG-native non-integrable source and any non-Abelian / geometry extension."
- **Editorial — §6.3a self-reference.** A sentence relocated by v1.20.3 into §6.3a still pointed to "**§6.3a** below"; now "maintained in this §6.3a ledger block". No theorem, status or scope changes.
- **Metadata.** Status summary relabelled "scientific state fixed at v1.20; carried unchanged through v1.20.4".
- **Methodology debt recorded.** Structural migration complete ≠ Methodology v1.3 truth-grade normalization complete: 19 independent scientific grade-decision rows remain, frozen for a separate owner grade-decision pass (v1.20.5); four further combined `[from:]` occurrences in §9.2 are provenance-registry mirrors of those grades, not independent decisions. Methodology v1.3 requires one canonical status per assertion and splitting of parts with different status; these are grade decisions, not relabels.
- **`[COR v1.20.4]`** v1.20.3 reported that no relocated-body pointer rewording was needed. That scan searched for literal `§2` references and missed one forward reference, "§6.3a below", which became self-referential after relocation. A full scan of directional section references inside §6 found this single instance. The pointer is corrected here; no scientific statement changes. The v1.20.3 changelog entry is left as recorded.

### v1.20.3 — September 25, 2026

**Methodology-only structural migration (option B, module-level). Scientific state identical to v1.20.2.**

- §2 reduced to the section heading, the unchanged Priority-ordering queue, and a module registry of structural pointer rows. All 18 §2 modules relocated verbatim, as whole modules (set-up, definitions, guards, theorems, OPEN/HOLD residuals, unanchored lines), to their §6 homes, in original order, after the existing §6 content; module headings demoted one level. The single level-6 heading (L1) is capped at level 6 as a Markdown rendering exception only; its semantic parent remains N-1C-DYAD (no re-parenting).
- Approved per-block dispositions applied unchanged: 114 MOVE; 4 REGISTRY-ONLY (queue in place; 3 bare status lines relocated verbatim onto registry rows); 1 MIRROR-RECONCILED (§2 ORD-4 copy removed, §6.3a twin retained); 0 STOP.
- New structural heading §6.9a NG-10 (approved). Co-owner approved structural mappings: N-4 → §6.5, N-6 → §6.7, NG-9 → §6.10.
- Gates: FP-v2.3 no loss / no invention / identifier conservation (incl. derived HEADING-DEMOTION for the one heading-anchored block); INV-S final; INV-P post-write; INV-LIVE; §2 and §8 queues byte-identical to v1.20.2.
- Textual pointers: a scan of the relocated bodies found no "§2 …" cross-references, so no pointer rewording was needed or performed.

### v1.20.2 — September 25, 2026

**Scientific-sync patch: STOP-02 and STOP-03 only.** No other scientific edit.

- **STOP-02 `[COR]`.** §6.9 still called the common home "the certified relational-category architecture `C_NG`", contradicting the v1.20 S5 correction. Now: "the certified typed relational architecture with partial physical composition `C_NG`".
- **STOP-03 `[COR]`.** The §7 proof package still pinned the `q=4,(0,3)` cascade closure to Dyadic **v6.4.9**, which v1.20 G1 ("all live current-pointer references refreshed") had missed. Now Dyadic **v6.4.10** `DYAD-THM-Q403-PHASELAW`. The mathematics and ownership are unchanged; only the live source version is corrected.
- **Why both survived earlier scans.** The reverse-inventory generator (built for the planned migration, now v1.20.3) ran its stale-wording regex only inside §2 `RESULT/THM/ALG` blocks, so a §6 `[OPEN]` sentence and a §7 proof-package list item were structurally invisible to it. A new whole-document check, **INV-LIVE**, now scans all live text (changelog, Appendix A historical narrative, Appendix B rejected formulations, and `[COR]` quotations excluded) for withdrawn wording and superseded source pins.
- Found in the co-owner review of the v1.20.2 inventory. The planned methodology-only migration is renumbered **v1.20.3**.

### v1.20.1 — September 25, 2026

**Scientific-sync patch: STOP-01 only.** No scientific claim changes beyond the STOP-01 sync repair.

- **STOP-01 `[COR]`.** The live §6 Foundations-export sentence still described D15 as "a separate governance edit", while v1.20 S8 had already recorded **D15 SYNC COMPLETE** in §9.1 and Appendix A. Corrected to: D15 OFN-side synchronization is complete in OFN v0.8 (RF-O08-10); the OFN whole target remains ACTIVE for physical source, non-Abelian extension, and curvature. The sentence survived the v1.20 acceptance grep because that grep searched only for `pending (D15)`. A broader live-text scan (`D15|OFN-side DSN synchronization|OFN.{0,40}synchroniz|separate governance edit|pending decision`) found no other live occurrence; §9.1 and Appendix A already read SYNC COMPLETE.
- Found by the v1.20.1 migration reconciliation review (`NG_V1201_RECONCILIATION_REVIEW_v1`, pair P18). Per migration rule 2, a content drift cannot be repaired inside the methodology-only migration, so it is repaired here first, giving the migration a consistent base.
- Historical changelog entries (including the v1.5-era "OFN-side synchronization registered as pending decision" line) are untouched.

### v1.20 — September 25, 2026

**Scientific/source synchronization release; Methodology v1.3 compliance on touched blocks only.** Structural §2/§6 migration deferred to a methodology-only pass. P2: no scientific change.

- **S2 explicit-domain boundary CLOSED** via `[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.14 | DYAD-THM-PRIM-CTR]`: canonical seed `(1/100,1/250)` has `Q_0 = 19/250000 < 1/625` and lies in `U`; whole explicit tube (`Q < 2209/10^6`) sits inside the v1.19 P3 injectivity box. L1 ownership unchanged. NUMGEN-side consumer acceptance recorded; upstream Dyadic consumer-row sync deferred to the consumer-sync pass. Guard retained: tube membership ⇏ GAP-LOCK angular hypotheses.
- **S3 SG-NG-18 rewritten** as a typed-object non-conflation guard: ray burst `37/40` (with `-(5/24)Q^(5/2)`) ≠ raw angular mean `47/54` ≠ normalized observable ≠ long-orbit backbone (Dyadic v6.4.10 `[DEF]`, `[COR v6.4.10]`). "Provenance unresolved upstream" withdrawn in both live occurrences.
- **S4 C7C-M partially resolved.** M-1A exact chain identity `Delta^{AC}_{pu:qv} = v Delta^{AB} + p Delta^{BC}` and M-1B conditional carrier closure on the repaired `D_chain` CLOSED `[ALG]`; `D_chain`'s middle condition formalized as a common triple comparison prefix domain or certified cofinal transport. **Unrestricted WD-CLOSE FAIL** (`(A,A) ∉ R_pair`, a closure counterexample). **Naive/global label-only WD-DOM FAIL for `D_chain`** — scoped; a richer interface-typed saturated carrier is not excluded and is the OPEN frontier. WD-VAL on admitted chains PASS. Associativity `[ALG]` only for admitted bracketings; admissibility transfer OPEN. Identity/inverse unavailable on the current carrier (literal unit/inverse constructions fail closure; the C7C-0 reciprocal *label* theorem stands). Physical commutativity OPEN. `NG_C7C_M_DESIGN_v1.md` retained as historical; its "typed by `B` suffices" and "associativity free" statements superseded. M-4 HOLD (P2). C7C-A not opened.
- **S5 `C_NG` reframed** from "relational category" to typed relational architecture with partial physical composition; certified sector structures (`G_adm`, `M_T`, N-2 group completion) unchanged.
- **S6 `[COR]` live contradiction repaired:** ORD-2 reflection was tagged `[NUM-audited]` while P3 was closed `[ALG]` at v1.19; reflection is now `[RESULT][from: ALG]` on the shrunken/explicit tube.
- **S7 `[COR]` live contradiction repaired:** §7 proof package said "mod-N completeness explicitly not claimed" while §6.8 certifies `Z_N` completeness for a fundamental integral cycle basis; corrected, with the nonprimitive/rescaled-row exclusion stated.
- **S8 D15 SYNC COMPLETE** (OFN v0.8 RF-O08-10); OFN whole target ACTIVE; alignment note added.
- **G1 pointer refresh:** Programme v1.1→v1.2, OFN v0.7→v0.8, Dyadic v6.4.9→v6.4.10 on all live current-pointer references. **G2** header declares Methodology v1.3, document status, supersession, and the SG-PROG-4 non-bridge statement; status summary compressed to current state, narrative preserved in Appendix A. **G3** touched `[RESULT]` lines normalized to one canonical status; **migration debt** (untouched combined grades, `[INTERP]`/`[POSTHOC-DIAG]` occurrences) recorded for the structural pass. **G4** touched load-bearing imports converted to `[import: … | RID]`; historical `[source:]` records left as migration inputs. Alias table extended.
- **E1** known consumer `RECOG v0.3.1 / RECOG-ALG-LATTICE-CLOCK` registered against `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` (RECOG must repin from v1.15). **E2** PRR/RRF registered as noncanonical working-methodology references only.
- **Not changed:** ten-label lower bound; 136 frozen DISC-2 records with 40 `CONVENTION-EXPOSED`; C7C-0; GAP-LOCK 1–3; N-1/N-2/N-2-ORD ownership; NG-7A closure; N-6, N-4, NG-7B, full NG-8, C7B global breadth OPEN; historical changelog text.

### v1.19 — September 19, 2026

**External-audit reconciliation + presentation-covariance provenance pass. Existing label-level DISC admissions and prior closed theorem verdicts are retained; two independently derived algebraic refinements are added at narrower declared scopes.**

- **External review reconciled.** I1–I7 and P1–P3 were checked against the current owner. I4 had already been repaired before the reviewed draft; the remaining precision corrections are synchronized here.
- **N-3C+ exact-order correction:** cyclic projector statements now require `ord(lambda)=p`, not merely `lambda^p=1`.
- **N5-C2 domain correction:** finite-origin invariance is restricted to the same comparison sector / extension cone / cofinal tail; branch selection is not an origin shift.
- **C5 reblocking correction:** the `m:1` defect is `n-m floor(n/m)` on primitive prefixes, bounded in `[0,m)` and zero only at complete block endpoints.
- **N-5A/GAP-LOCK indexing corrections:** the first 7-gap ends at step 33229 with the previous printed amplitude identified as `Q_33228`; primitive slip steps satisfy `n_k=6M_k+O(1)`. Historical LOGSLIP OPEN/CAND wording is explicitly marked superseded. Dedicated RID `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` assigned.
- **NG-8A observable wording corrected:** physical distinguishability rests on identity of the full gauge-reduced state `(rho,eta)`, not on the insufficient shorthand `Q_true and/or eta`.
- **NG-7A correction + extension:** unit defects require nonzero cycle/cohomology projection to be detected. With a spanning forest and fundamental integral cycle basis, zero cycle sums imply exact node-potential data over any abelian coefficient group, including `Z_N`; arbitrary nonprimitive/rescaled cycle-row presentations are not promoted.
- **N-2-ORD P3 promoted on a shrunken tube:** a derivative lower bound proves `T` injective on `|rho|,|eta|<=1/10`; the existential local tube may be shrunk into that box, promoting ORD-2 reflection and the cross-orbit merge refinement to `[ALG]` at that scope. No explicit maximal radius or numerical-seed inclusion is claimed.
- **SG-NG-18 provenance neutralized:** Number Genesis no longer calls the Dyadic `37/40` ray formula a normal-form result; raw-vs-normalized frame provenance remains an upstream Dyadic/RECOG issue.
- **P2 post-hoc DISC-2 presentation-covariance audit:** 40/136 ratified witness records are `CONVENTION-EXPOSED`, 96 unexposed; 216 antipodal events occur in audited eventual cycles. Reverse/inert diagnostic policies alter individual witness records but preserve the ten-label projection, and every admitted label has at least one unexposed witness. No frozen admission gate is retroactively changed. Discrete-owner policy action remains pending; DISC-1 requires the same audit.
- Registered the external-review response, P2 audit script/log, per-witness annotation companion, and C7C-M design memo. The frozen `disc2_witness_report.json` is not rewritten.
- **C7C-M remains OPEN.** Design/algebra may continue, but M-4 realization search is held until the Discrete-owner P2 orientation policy is resolved.

### v1.18 — September 19, 2026

**Owner synchronization: C7C-WD/C7C-0 closure plus a pre-existing provenance repair. No new campaign data; one algebraic theorem imported.**

- **C7C-WD ADOPTED.** Pre-bounded carrier `R_pair`, bounded carrier `R_bd subseteq R_pair`, representation equivalence `==_Q` (not physical identity), typed signatures `Phi_{tau1,tau2}^{tau3}`, and obligations WD-PHYS / WD-CLOSE / WD-DOM / WD-VAL / WD-DESCENT with arithmetic compatibility WD-REP only afterward. **Domain congruence (WD-DOM) is split from value congruence (WD-VAL)**: "whenever all four compositions are admissible" was necessary but one condition short of a quotient operation.
- **C7C-0 CLOSED `[RESULT][from: ALG]`.** Orientation swap `S(A,B)=(B,A)` is a carrier-preserving involution with `rho_Q(Sx)=rho_Q(x)^(-1)`; `Q_RTG^bd` is closed under `r -> r^(-1)`. WD-DOM is trivial here because `S` is total on `R_bd` (`D_S=R_bd`); unary-ness alone would not suffice for a partial operation. This is why `S` was the correct first test. `[COR]` certificate v1 concluded `Sx in R_bd` at the carrier-preservation step before the sign identity had decided boundedness; v2 repairs this with the `R_pair`/`R_bd` split. `[COR]` "no reciprocal pairs among the ten labels" corrected to "apart from the self-reciprocal `1`, no distinct reciprocal partners".
- **Not claimed:** `Q_RTG^dyn` reciprocal closure (requires `A <-> B` equivariance of the dynamic gate); multiplication; addition; field structure. **C7C-M design is the next active target**, with WD-DOM its load-bearing obligation.
- **`[COR]` provenance repair, pre-existing since v1.16:** `SG-NG-26` was invoked in the DISC material but never defined in section 3 — now defined (common-source finite-multiplicity triviality). The C7B transport lemmas were cited as naked `T1/T2/T4`, colliding with N-2-ORD `T4` (physical sign realization) — now registered as **`C7B-ALG-T1..T4`** with owner-level statements.
- **`[REPRO]`** reproduction contract summary added to the C7B block: pinned owner hash, the decisive `signed_centered` boundary convention `(-N/2, N/2]`, the IC-stage sign pairing `d_AB^IC = -d`, the gauge-reduced cycle key, and the pre-inspection one-step triple-equivalence gateway.
- §1.3, §2, N-5 status, §3, C7B algebra block, N5-C7C, §4, §5, §6.6, §8, §9.2, Appendix A, Appendix B synchronized. §8 mirrors §2. v1.17 changelog text preserved unchanged.
- Certificate `NG_C7C0_RECIPROCAL_CERT_v2.md` self-ID corrected from `_v1` before registration; archival hash `5abd130d...5c723e`.
- **Pre-freeze precision patch (v1.18.1, same release):** `C7B-ALG-T1..T4` normalized by gcd — raw cycle counts `(A,B)` versus reduced class `red(A,B)` are now distinguished, and the DISC coefficients `-156`, `-96` are identified as **reduced-class** coefficients (raw cross-determinants `-1404`, `-576`); lemma block re-tagged `[DEF]` (namespacing) + `[RESULT][from: ALG]` (lemmas); WD-DOM triviality for `S` attributed to **totality on `R_bd`**, not unary-ness (a partial unary operation could have representative-dependent admissibility); two surviving naked `T4` references namespaced; N-5 guard-preservation line extended to SG-NG-26; `NG_DISC1_DIAG3_RESULT_v3.md` registered as the provenance for the realization-sensitivity claim used in the C7C-M rationale; two `v1.17` metadata fields updated without implying a fresh revalidation. No DISC verdict or theorem changes.

### v1.17 — September 3, 2026

**Documentation-only owner synchronization of the ratified C7B-DISC-2 campaign. No new theorem is claimed by this release itself.**

- **C7B-DISC-2 CLOSED — B-check PASS · D-check PASS.** Frozen protocol `NG_C7B_DISC2_PREREG_v1.md` applied the already-certified `k`-axis to the fresh owner-registered supplementary one-pass family (`|d|_c=3,4,5`, 10368 seeds, trajectories previously uninspected). 7468 base dual-active, 208 survive the `1->2` fence, **136 witnesses** (130 `PASS_INT`, 6 `PASS_BDY_ONLY`). Ratification audit: A1 owner recount 544/544 exact, A2 T4 certificates 136/136, A3 domain/same-`x` 136/136.
- **Eight new dynamic labels.** Currently established: `{1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4} subseteq Q_RTG^dyn` — a certified lower bound, **not** exhaustiveness.
- **`1 in Q_RTG^dyn`** established by 26 discriminating realizations, recorded as a statement distinct from the N5-PHYS-1 bounded control `1 in Q_RTG^bd`.
- `[COR]` **all 6/6 boundary witnesses depend on `k=0`** (an earlier "four of six" is retracted); the architectural retention of `k=0` is now empirically load-bearing.
- `[GUARD]` DISC-2 concentration statistics are descriptive only and bear on robustness, never on membership.
- **Queue reordered:** C7C-WD (representative-independent physical operations) becomes the next active target, ahead of further breadth; DISC-3 is deferred, not blocked. C7B global breadth and C7C remain OPEN.
- Governance: `NG_TO_TDRG_REPRODUCIBILITY_GAP_v2.md` remains **pending owner action** on the Discrete Genesis side.
- Artifact provenance: `disc2_ratification_certs.json` is canonical in **LF** (`1ad96df2...393d3`); a CRLF rendering of identical content hashes to `e71475c5...d9cc09`.

### v1.16 — September 2, 2026

- **GAP-LOCK Lemma 3 CLOSED `[ALG]`** by the exact event-time defect identity. The v1 bootstrap is `[COR]`-retracted as circular: per-slip `O(sqrt q)` error does not by itself bound an accumulated offset.
- Introduces `G_n=(pi/3)n-(phi_hat_n-phi_hat_0)` and the exact event identity `G_(n_j)=C+(pi/3)s_j-o_j`; the actual six-step deficit gives `g_(j+1)=7 <=> o_j<Delta_j` with `Delta_j->0` at physical slips.
- Combines event locking with INF-1 to prove the **physical consecutive 7-gap ratio limit** `M_(k+1)/M_k -> exp(sqrt(3)pi/6)`. This equals the defect-threshold consecutive-ratio limit but does not identify the two event sequences.
- **C7 semantic split synchronized:** `Q_RTG^bd` = labels realized by certified bounded physical pairs; `Q_RTG^dyn` = bounded labels with at least one realization passing the frozen same-realization stability+contingency gate. Legacy `Q_RTG^real` is not silently repointed.
- **C7B-DISC-1 CLOSED:** DISC-1B PASS and DISC-1D PASS-INT on the frozen TDR-G panel. Currently established dynamic labels are `{2,3}`; formally `{2,3} subseteq Q_RTG^dyn` and `Q_RTG^dyn != empty`. No exhaustiveness theorem.
- DISC-1 provenance synchronized: exact BIND3 reproduction, exhaustive owner differential at all `k in {0,1,2,3}`, independent owner-counter recount, fixed-period simplicity control, and two transport archetypes.
- **C7C remains OPEN.** Multiple admitted labels do not supply physical rational addition/multiplication. C7B breadth, N-4, N-6, full NG-8, NG-7B, and optional Fatou/`C_D` identification retain their scoped statuses.

### v1.15 — August 31, 2026

- **Canonical N-5 commensurability consolidation.** Promotes the bounded synchronization architecture from candidate definition to a certified structural relation while keeping full `Q` realization/arithmetic explicitly open.
- **N5-C1 CLOSED:** `Delta_(p:q)=q N_A-p N_B` is relationally defined on finite common-order prefixes with no external clock/frequency premise.
- **Prefix-cofinal indefinite repeatability formalized; SG-NG-25 added.** Event-count divergence means cofinal unboundedness under finite prefix extension, not external metric time or a completed infinity. Corrected terminology: counts are monotone/non-decreasing under arbitrary prefix extension.
- **N5-C2 CLOSED:** finite origin shifts change the defect only by a constant, so boundedness is presentation-independent.
- **N5-C3 CLOSED:** `Delta_(kp:kq)=k Delta_(p:q)`; positive common rescaling preserves the bounded class.
- **N5-C4 CLOSED:** prefix-cofinal unboundedness plus integer algebra gives uniqueness of the reduced positive proportion.
- **C5-SYN-13 CLOSED `[MATH/ALG]`:** the finite-prefix periodic language `A^6 B A^7 B` realizes a bounded synthetic `13:2` class with `|Delta|<=13`; `A^6 B A^8 B` is a neighboring linearly divergent negative control. No RTG physical `13/2` claim.
- **N5-C6 retained CLOSED:** canonical primitive/section A/B is density-resonant at 6 but boundedly commensurate at no positive rational pair.
- **N5-PHYS-1 CLOSED:** opposite phase-coincidence streams `B_+` (`rho>0`) and `B_-` (`rho<0`) are physically distinct, prefix-cofinally recurrent, strictly alternating on the local dyad tube, and satisfy `|N_(B_+)-N_(B_-)|<=1`; first genuine physical bounded class is `1:1`.
- **C7 split and C7A CLOSED:** define `Q_RTG^real` as the realized positive-rational spectrum and `rho_Q` as the unique rational invariant of a certified bounded pair. `rho_Q(B_+,B_-)=1`, hence `1 in Q_RTG^real`. Equal labels do not silently identify physical realizations.
- **C7B OPEN:** determine the physical realization spectrum. Pre-registered **C7B-DISC-1** in the native TDR-G `N=24,k=1` retrigger-entry family using SWAP vs active-P3 event counts. The per-cycle owner artifact/export (`TDRG-ART-BIND3-N24K1`, expected `bind3_cycle_n24k1.py` or equivalent) is still pending in the accessible corpus; ensemble percentages are explicitly inadmissible as ratio witnesses.
- **C7C OPEN:** physical addition/multiplication on realized commensurability classes remain uncertified.
- N-5 remains OPEN as a programme target: the physical rational-label mechanism is certified and nonempty, but neither `Q_RTG^real = Q_(>0)` nor field arithmetic is claimed. GAP-LOCK Lemma 3, N-4, N-6, DZT-owner relay and OFN/D15 synchronization remain unchanged/open as previously scoped.

### v1.14 — August 28, 2026

- **Final v1.13 synchronization + N-5 architecture release.** GAP-LOCK Lemmas 1–2 are moved from changelog/registry-only status into the live N-5A-S1 theorem block; Lemma 3 remains OPEN and non-blocking.
- **Adopted N-5-COMM-BD as the active certificate target**: candidate physical commensurability is bounded integer synchronization defect `Delta_(p:q)=q N_A-p N_B` on certified common-order prefixes. N-5 itself remains OPEN.
- Registered the N5-C1–C7 execution package: relational definability, origin/prefix invariance, physical rescaling, reduced-pair uniqueness, controls, canonical-pair falsifier, and conditional Q-like representation.
- **Adopted SG-NG-24 — rational density != physical commensurability.** The canonical A/B pair supplies the adequacy counterexample: leading density tends to `6` while the certified physical synchronization discrepancy/7-gap count diverges logarithmically.
- Updated §1.3, §2 queue, §4 routing, §5 high-risk ledger, §6.6, §8, Appendix A/B, current version labels and GAP-LOCK artifact wording.
- Removed the duplicated `## Changelog` heading inherited by v1.13. Historical correction entries remain intact.
- No Q-like commensurability class, rational arithmetic, N-6 result, GAP-LOCK Lemma 3, DZT owner relay, or OFN/D15 synchronization is silently promoted.

### v1.13 — August 28, 2026

- **GAP-LOCK Lemmas 1 and 2 CLOSED** (`NG_N5AS1_GAPLOCK_PARTIAL_v1.md`; certificate 7 families, exit 0). Prior v1.12 over-promotion `[COR]`-logged; the v1.12.1 defect-threshold theorem stands and is now supplemented rather than replaced.
- **Lemma 1 (alphabet `{6,7}`)** proved from already-certified pieces: the every-basepoint six-window law `Lambda_6 < 2pi` kills gaps `<= 5`; `Lambda_7 > 2pi` kills gaps `>= 8`; smallness is load-bearing (large-amplitude `11` marks the boundary). With the closed non-6 theorem: infinitely many 7-gaps exactly.
- **Lemma 2 (bookkeeping)** `E_B(M) = s(M) + O(1)` (observed deviation `<= 5`), so the **physical 7-gap count law** `s(M) = (3 tau/pi) log M + O(1)` and the physical mean exponential rate are restored to theorem grade — with the alphabet premise proved, not assumed.
- **Lemma 3 remains OPEN** with the obstruction identified precisely: lap-count fractional parts oscillate; the physical consecutive-ratio limit is exactly the claim that the within-cell offset converges, for which the v1.12.1 `C_D`/Fatou-normalisation question is the natural route.
- N-5A unchanged (closed); **N-5 remains the active frontier**, now receiving two certified equivalent presentations (`E_B`, `s`) of the unbounded relational discrepancy that a commensurability quotient must not erase.

### v1.12.1 — August 28, 2026

- **Scientific-scope correction to the new v1.12 LOGSLIP corollary; N-5A-S1 remains CLOSED and N-5 remains the queue head.**
- Re-ran the independent verification certificate: V1–V11 still execute cleanly. Accepted V1–V9 as closure verification; V10–V11 are numerical/derived evidence whose physical-slip interpretation required one extra theorem.
- Promoted the sharper exact local statement `Delta phi_T = pi/3 + O(Q^(1/2))` into L-MONO; retained `(pi/6,pi/2)` only as a corollary.
- `[COR]` The v1.12 identification `s(M)=6(M-N_B(M))` with **literal 7-gap count** assumed an unproved eventual return alphabet `{6,7}` and bounded endpoint bookkeeping. Existing ALG proves infinitely many non-6 returns, not that every late non-6 return is exactly 7.
- Replaced that overclaim by the theorem-grade cumulative event-count deficit `E_B(M)=6(M-N_B(M))=(3 tau/pi)log M+O(1)`.
- Proved the **defect-threshold rate**: for first crossings of fixed `pi/3` increments of the monotone accumulated defect, `M_(k+1)^(def)/M_k^(def) -> exp(pi/(3 tau)) = exp(sqrt(3)pi/6)`. This is exact at the phase-defect level.
- Opened `N-5A-S1-GAP-LOCK`: prove eventual `{6,7}` return alphabet plus one-to-one/asymptotically one-to-one locking of 7-gaps to `pi/3` defect thresholds before calling the same rate a physical 7-gap theorem.
- `[COR]` `C_D` already exists because v1.11 proved `D_M=tau log M+C_D+o(1)`. The Fatou question is now identification/normalization of that existing constant and whether it controls the within-cell locking offset, not existence of the offset.
- SG-NG-23 unchanged; no Q/R promotion. N-5A closure unaffected.

### v1.12 — August 28, 2026

- **Independent verification of the v1.11 N-5A-S1 closure.** All exact assertions re-derived with an independent expansion routine; the uploaded certificate also reruns clean. Closure **confirmed**.
- **New cross-check:** the cubic angular jet induces `dQ = -Q^2` exactly, independently reproducing the certified L1 radial law — two independently derived objects agreeing with no free parameters. Corollary: `Re(c21) = -1/2` is forced, so only `Im(c21) = -tau` is new information.
- `[GUARD]` **L-MONO margin note:** the `(pi/6, pi/2)` bracket is sufficient but yields an exactly `2 pi`-wide branch window with zero margin; recommended promotion of the already-available `Delta phi_T = pi/3 + O(Q^(1/2))` (verified half-power) into the lemma statement. No result changes.
- **New corollary — slip-count law** `s(M) = 6(M - N_B(M)) = (3 tau/pi) log M + O(1)`, tracking each observed slip to three digits.
- **Exponential slip rate promoted to `[RESULT][from: ALG]`:** `(1/k) log M_k -> sqrt(3) pi/6`, rate `exp(sqrt(3) pi/6) = 2.476632271...`. `NUMGEN-CAND-N5AS1-LOGSLIP` split into the proved rate and an `[OPEN]` offset-convergence residual (needed for consecutive-ratio convergence).
- **Riemann-lens findings merged and relayed upstream** (Dyadic-owned, not claimed here): `Q_true` is the unique `J`-invariant quadratic form (Eisenstein/hexagonal norm), so SG-1 primacy is forced not conventional; `tau = 1/sqrt(det g)` with `det g = 3/4`; `F = T^6` is a cubic parabolic germ. The Fatou/iterative-residue question is retained as the narrowly scoped target for the offset-convergence residual.
- Registered the external-reviewer briefing and the Riemann-lens certificate.
- `[GUARD]` SG-NG-23 unaffected: the proved rate is a chart-derived constant behind SG-NG-19 / OPEN-P0; the leading density is still 6.

### v1.11 — August 28, 2026

- **N-5A-S1-INF CLOSED; N-5A-S1 CLOSED; N-5 unblocked.**
- **L-BACKBONE CLOSED directly from certified L1**, correcting the v1.10 one-sided formulation. The exact recurrence `q_(m+1)=q_m-q_m^2+O(q_m^(5/2))` gives `q_m=Theta(1/m)` and the refinement `q_m=1/m+O(m^(-3/2))`; hence `sum q_m=log M+C+o(1)` and `sum q_m^(3/2)<infinity`.
- **L-MONO CLOSED** from the exact one-step linearization in primitive `W`: after local shrinking, `pi/6<delta_T<pi/2`. This is strong enough for the counting bridge. A direct primitive-map inequality proves that `eta^-<0<=eta^+` forces both endpoint `rho` values positive, so lap crossings coincide with the canonical B predicate. The former gate-1 orientation caveat is retired.
- **L-PHASE CLOSED from the exact primitive finite iterate**, not the cubic-vector surrogate: `W(Fx)=W+(-1/2-i tau)W|W|^2+O(|W|^4)`, hence the increasing block lift obeys `Delta phi_hat=2pi-tau Q+O(Q^(3/2))`.
- Upgraded the v1.10 remainder correction from numerical scaling evidence to exact algebra: the quartic primitive jet has nonzero angular coefficient `-25 sqrt(3)/48` on the positive-`u` ray, so a uniform post-leading `O(Q^2)` phase remainder is false.
- Strengthened INF-1 to `D_M=tau log M+C_D+o(1)` and INF-2 to `N_B(M)=M-(tau/(2pi))log M+O(1)`. Therefore infinitely many B-events and infinitely many non-6 gaps occur; no eventual fixed blocking `T^m` is possible.
- Gates 1–5 are now CLOSED for N-5A-S1 on a sufficiently small certified local primitive-dyad tube. SG-NG-23 remains unchanged: this supplies a second stream, not a nontrivial commensurability/Q theorem.
- Registered `NG_N5AS1_INF_CLOSURE_v1.md` and `ng_n5as1_inf_closure_cert_v1.py` / `.log`.
- Queue advanced to **N-5**; N-4 remains parallel.

### v1.10 — August 28, 2026

- **N-5A-S1-INF reduced to three named lemmas; both combination theorems proved.**
- `[COR]` **The proposed INF-1 hypothesis `|r_m| <= C Q_m^2` is falsified for the exact map**: `sup|r|/Q^2` diverges as `Q -> 0` (doubling per fourfold decrease of `Q`). The true and stable exponent is **3/2** (`sup|r|/Q^(3/2)` in `[1.3449, 1.3565]` across a 256-fold `Q_0` range), matching the half-power scale already present in the certified L1 law. The theorem survives: `sum Q_m^(3/2)` converges when `Q_m ~ 1/m`, which is all INF-1 needs.
- Pinned the lifted-phase **sign convention** (`phi` increasing, block law `2 pi - tau Q_m + r_m`, defect is a lag) — explains why observed slips are 7s and never 5s.
- **INF-1 proved** given the lemmas: `D_M = tau sum Q_m - sum r_m -> infinity`.
- **INF-2 counting bridge proved** given the lemmas: `N(M) = M - D_M/(2 pi) + O(1)`, and an eventually-fixed gap `m_0` forces `m_0 = 6` and `D_M = O(1)`, contradicting INF-1. Gate 2 and ALG gate 5 therefore close together. The bridge works at block level against the primitive return count, so no per-primitive-step phase law is required.
- Named the remaining work: **L-MONO** (also retires the gate-1 orientation caveat), **L-PHASE** (exact six-step, corrected exponent), **L-BACKBONE** (nearest to complete); suggested order cheapest-first.
- `[GUARD]` All supporting numerics remain `[NUM]` seed-orbit evidence under the explicit-radius gap; the reduction and combination theorems are seed-independent. SG-NG-23 unaffected.

### v1.9.1 — August 28, 2026

- **Scope/provenance calibration; gates 1/3/4 remain structurally CLOSED.** Re-ran `ng_n5as1_gates134_cert_v1.py`; all 13 families pass, exit 0.
- Separated the exact/structural gate claims from the finite seed-orbit witnesses. The N-1/N-3A tube is existential and has no explicit numeric radius, so the seed `(0.01,0.004)` is retained as `[NUM]` evidence rather than silently declared a point of `U_T`.
- Recast the B-event as a **lift-free discrete transition-neighbourhood predicate** on the certified one-chart tube. No continuous interpolation between primitive map states is assumed.
- Corrected SG-NG-13 wording: invariance under `eta -> eta+2pi k` certifies gauge reduction, not spectator independence. The fixed-support gate-1 scope contains no added spectator; any spectator/boundary extension remains separately gated.
- Clarified SG-NG-11 provenance: explicit declaration of `P_B` supplies the structural counting-equivalence discipline; pairwise-distinct crossing `Q_true` values in the seed run are NUM witnesses, not an all-event ALG theorem.
- Recast gate 3 as structural co-realization of the B predicate with primitive T-transition tokens on `U_T`; finite-window nontermination is not called indefinite extensibility (gate 2 remains OPEN).
- Recast gate 4 so N-2-ORD provides the ALG order on any B anchors inside `U_T`; index differences in the script are only the metalanguage representation of unique Track-A reachability counts. The observed `{6,7}` word remains NUM evidence for LOGSLIP/gate 5.
- Normalized v1.8.1 current-state labels and updated the status summary, frontier, registry and Appendix A.

### v1.9 — August 28, 2026

- **N-5A-S1 gates 1, 3 and 4 CLOSED** per PI routing (clear the cheap gates before the infinitude theorem). Certificate `NG_N5AS1_GATES134_CERT_v1.md`, 13 assertion families, exit 0.
- **Canonical-section identity established** `[ALG]`: `Theta = 0 <=> eta_wrap = 0 and rho > 0`. The section is relational-phase coincidence with positive `rho`, so gate 1's arbitrariness risk does not apply to `Theta_0 = 0`; other swept sections are demoted to robustness checks and are not certified event types.
- **Lift-free detectability certified**, discharging the SG-NG-16 / N-3A lifted-winding objection: the B-event is a present-state relational condition and a lift-free detector reproduces the lift-based sequence exactly.
- Gate 3 (co-realization on one declared domain, injective increasing anchor map) and gate 4 (interleaving fixed by `<=_T` reachability distance, no clock) closed; first load-bearing use of N-2-ORD for the SG-NG-20 co-realization requirement.
- `[GUARD]` Orientation uniqueness remains `[NUM]` on the audited domain pending a small linearization lemma; coordinate sections remain uncertified; nothing here moves the pair toward a nontrivial commensurability class (SG-NG-23 unaffected, limiting ratio still 6).
- **N-5A-S1 is now one theorem from closure**: gate 2 and the ALG form of gate 5, both inside N-5A-S1-INF.

### v1.8.1 — August 28, 2026

- **Epistemic-calibration / routing patch; no reversal of the v1.8 numerical findings.**
- Re-ran `ng_n5as1_logslip_verification_v1.py`; exit 0 and all reported slip times/ratios reproduce.
- Split the LOGSLIP statement into (a) `[RESULT][from: NUM]` finite-horizon quantitative agreement and (b) a `[CAND][target: ALG]` asymptotic theorem requiring the two named N-5A-S1-INF lemmas. Removed theorem-like wording (“must be geometrically spaced”) from the NUM result.
- Made the exact asymptotic density statement `steps-per-crossing -> 6` conditional on the still-open `O(log M)` slip-count law rather than treating it as already proved.
- **Adopted SG-NG-23** in strengthened form: non-fixed blocking does not imply incommensurability or a nontrivial Q-like class; continuous-dyad constants such as `pi/(3 tau)` or `exp(pi/(3 tau))` remain representation-level diagnostics behind SG-NG-19 / OPEN-P0 absent a stronger bridge.
- Advanced the immediate queue to **N-5A-S1-INF + gates 1/3/4**, with N-4 explicitly parallel.
- Normalized stale v1.7.1 current-state labels to v1.8.1 and updated Appendix A to reflect the live LOGSLIP state.

### v1.8 — August 28, 2026

- **Independent verification of the v1.7.1 correction.** Reimplemented with a different crossing detector (lap counting on `floor(phi/2pi)`) at dps=60: gap histogram `{6: 6664, 7: 1}` over 40 000 steps, first non-6 return at primitive step **33229** with `Q_true = 5.3443e-5 < Q_0`. The PI's script also reproduces. The v1.7 obstruction and its `[FAIL]` verdict are correctly retracted; `[COR]` recorded against the auditor's own v1.7 entry (asymptotic structure inferred from a 240-step horizon, three orders of magnitude short of the first slip).
- **`NUMGEN-CAND-N5AS1-LOGSLIP` strengthened from qualitative candidate to quantitatively confirmed law.** Pre-registered geometric slip prediction `rho = exp(pi/(3 tau)) = 2.4766` tested over 4e6 primitive steps: observed ratios 2.4710, 2.4746, 2.4760, converging. Independent second check: even/odd section clusters differ by `sqrt(rho)` (predicted 1.5737, observed 1.5729).
- **Module N-5A-S1-INF registered** with an ALG route to gate 2 (infinitely many slips from divergence of `sum tau Q_m` against convergent `sum Q_m^2`), gated on two named lemmas.
- **New guard proposal SG-NG-23 (non-relabeling ≠ incommensurability):** the limiting steps-per-crossing ratio is still exactly 6, so a density-based Q-like classification would return the rational label 6 and discard the logarithmic content; the slip-rate constant `pi/(3 tau)` is registered as the candidate carrier, with its admissibility as an RTG-native comparison invariant left PI-blocked.

### v1.7.1 — August 28, 2026

- **Scientific correction to v1.7; N-5A-S1 negative closure retracted.**
- Reproduced the original 240-step constant-`6` result, then extended the exact primitive map. For seed `(0.01,0.004)`, section `Theta=0` produces a **7-step** return at primitive step `33229` with `Q_true ~= 5.3443e-5 < Q_0=7.6e-5`.
- A long 12-section sweep gives gap set `{6,7}` for every tested section. The v1.7 “section-independent constant-6” conclusion is therefore a finite-horizon alias.
- `HYP-N5AS1-GAP` is marked **FALSIFIED**, not confirmed. Gate 5 now **survives numerically**: fixed blocking `B=T^m` is falsified on the audited orbit, while gates 1–4 remain OPEN.
- Retracted `NUMGEN-ART-ROTNUM-OBSTRUCTION` in its v1.7 form. Rational **limiting** rotation does not imply exact constant return gaps at finite amplitude.
- Registered `NUMGEN-CAND-N5AS1-LOGSLIP`: the owner Dyadic six-step phase shear `Theta_(m+1)=Theta_m-tau Q_m+O(Q_m^2)` with `tau=2sqrt(3)/3`, combined with `Q_m~1/(m+kappa)`, gives a non-summable logarithmic phase-defect mechanism consistent with sparse 7-step slips. Full infinite-slip theorem remains OPEN.
- N-4/N-5A coupling is weakened from “structural prerequisite” to parallel frontier: same-orbit angular geometry remains a live N-5A route inside the local contracting regime.
- Registered `NG_N5AS1_LONG_HORIZON_CORRECTION_v1.md` and the long-horizon recheck script/log.

### v1.7 — August 28, 2026

- **N-5A-S1 opened, executed, and closed negative in one pass** under falsification-first discipline: gate 5 (independence / non-relabeling) was run before gates 1–4 as the cheapest falsifier.
- `HYP-N5AS1-GAP` pre-registered, then **confirmed**: inside the certified tube the section-crossing return-gap word is the constant word `6`, so the candidate `B` coincides with `F = T^6` and is re-blocking, not a second event type. `[FAIL]`, RID `NUMGEN-FAIL-N5AS1-SECTION`. SG-NG-20 not discharged; gates 1–4 never reached.
- Failure shown **section-independent** by a 12-section sweep (distinct gap set `{6}`).
- **Positive byproduct registered** (`NUMGEN-ART-ROTNUM-OBSTRUCTION`): the limiting rotation number is exactly `1/6`, pinned by the `p=6` elliptic linearization, so every transverse section on the contracting tube yields a constant return gap. No second independent recurrence is constructible from the angular geometry of the same contracting orbit.
- Recorded the exploratory large-amplitude regime (non-constant word `{6,7,11}`, decaying under contraction) as scope-guarded, claim-free N-4 territory.
- **N-4/N-5A coupling upgraded from scheduling to structural**; N-5A search space re-partitioned into (a) closed negative, (b) domain extension, (c) structurally different source.
- Registered the general obstruction theorem as `[HYP]` and the generator-dependence of rotation-number rationality as a PI-blocked `[OPEN]` under OPEN-P0.

### v1.6.1 — August 28, 2026

- **Scope/status hygiene patch; N-2-ORD remains CLOSED and no frontier ordering changes.**
- Removed the stale duplicate `OPEN N-2-ORD` module block and replaced it with a CLOSED pointer to the canonical theorem in §6.3a.
- Promoted **ORD-4 from sampled `[ALG/NUM]` to exact `[RESULT][from: ALG]` on the full certified tube**: for each residue `j`, `y=T^j x` lies in the `T`-invariant tube, so the already-certified L1 theorem `Q_true(Fy)<Q_true(y)` iterates directly along every fixed-residue `F=T^6` chain. The numerical run is retained as regression/counterexample evidence, not theorem support.
- Clarified NC-3 provenance: non-merging-orbit incomparability is structural from the reachability definition; the executable NC-3 assertion is bookkeeping rather than an independent computational demonstration.
- Retained P3 as a flagged, non-proof-critical premise for order reflection/cross-orbit merge refinement only. Nonvanishing sampled Jacobian supports local nonsingularity but is not silently promoted to global tube injectivity.
- Normalized stale v1.5.1 current-state labels to v1.6.1.

### v1.6 — August 28, 2026

- **N-2-ORD CLOSED** in the PI-sharpened reachability-first formulation: order is defined by existence of a connecting certified history (`y <=_T z iff ∃K ∈ M_T, z = K(y)`), with `Q_true` demoted from definition to witness.
- ORD-1 (partial order on `U_T`, total per orbit; antisymmetry = N-1 non-collision), ORD-2 (shift covariance; reflection direction separated and P3-tagged), ORD-3 (positive cone `P = iota(M_T)` gives the translation-invariant totally ordered `G_T`), T4 (sign of a signed-history class realized as reachability orientation; well-definedness on N-2 classes and base-point independence certified), ORD-4 (`Q_true` strictly antitone and **order-reflecting** on every residue-`j` `F`-chain, all six residues).
- Registered `NG_N2ORD_PHYSICAL_ORDER_CERT_v1.md`, `ng_n2ord_order_cert_v1.py`, `.log` (14 assertion families, all pass, exit 0).
- **New flagged premise P3** (injectivity of `T` on the tube): explicitly **not** implied by N-1 non-collision; supported by `det J → 1` at `P_1` and the distance to the critical curve `C_0`, audited numerically. The ORD-2 reflection direction and the cross-orbit merge criterion depend on it and are tagged `[NUM-audited]`; a P3 micro-module is proposed to promote them.
- Non-claims upgraded from assertions to demonstrations: per-step `Q_true` monotonicity **fails** (192 vs 168 on sampled orbits) and `Q_true(T^3 x) < Q_true(T^2 x)` **fails** on an admissible seed, so the cross-residue guard now rests on a counterexample.
- Foundational chain recorded as complete on the local object: N-1 → N-2 → N-2-ORD.
- Queue advanced to the **N-4 + N-5A** frontier, with a note that the programme changes character there and that N-2-ORD now supplies the RTG-native comparison relation SG-NG-20 requires.

### v1.5.1 — August 28, 2026

- **Scope/hygiene patch; no scientific-state change. NG-7A remains CLOSED.**
- Corrected the full-holonomy separation witness at field-general scope: `A=C^T` is retained as the concrete executable witness over `Q` (and works over `R`), while the field-general theorem now uses any right inverse `R` of the full-row-rank cycle matrix `C`, so `C R=I_beta` and `r_hol=beta`. This avoids silently assuming a nondegenerate Euclidean Gram form over an arbitrary field.
- Normalized stale current-state labels from v1.4 to v1.5.1 in the pointer-validation note, routing-label guard, provenance wording, Import Ledger header, and Appendix A epistemic-status line.
- No change to the null theorem, completeness theorem, orientation/gauge/basis invariance, scalar-vs-multichannel typing, TDR-G `Z_N` zero-control, NG-7B status, or active proof queue.

### v1.5 — August 28, 2026

- **PI ruling recorded:** v1.4.1 adopted as canonical (decision D14); queue confirmed; NG-7A authorized as next module with the locked theorem package and the scalar/multi-channel terminology ruling.
- **NG-7A CLOSED** `[RESULT][from: ALG]`: null theorem `C D^T = 0`; field-coefficient completeness `im D^T = ker(C·)` making `h = Ca` and `[a] ∈ H^1(G;F) ~= F^beta` equivalent complete obstructions; orientation/gauge/cycle-basis invariance with invariant statistics identified; typed statistic per PI ruling (scalar observable is the holonomy vector/class, never a rank; `r_hol = rank(CA)` reserved for `d >= 2`, channel-GL invariant, `<= min(beta, d)`, zero iff flat); separation instances certifying cycle capacity ≠ holonomy content; mandatory TDR-G `Z_N` zero-control (rings `N = 6, 8, 12` and random graphs) with unit-defect detection; multiplicative spot theorem; declared-domain convention; loops/parallel edges included.
- Registered `NG_NG7A_HOLONOMY_NULL_CERT_v1.md`, `ng7a_holonomy_null_cert_v1.py`, and its log (12 assertion families, all pass, exit 0).
- `[GUARD]` additions with the closure: mod-`N` completeness explicitly not claimed; ring defect residue not identified with Track-C labels; no non-Abelian rank until NG-7B defines and certifies its invariant.
- Error-ledger note: the certificate's first execution failed its own T6 family because the scalar-rank check demands both values `{0,1}` be realized and the initial sampling drew only generic data; fixed by adding a flat sample without weakening the assertion.
- Foundations export recorded: operator half of `RTG-OFN-OPEN-HOLONOMY-RANK-DIAGNOSTIC` discharged; OFN-side synchronization registered as pending decision **D15**.
- Queue advanced: **N-2-ORD** is next; then N-4+N-5A → N-5 → N-6 → full NG-8. `HYP-NG-0R-COV` remains a parallel non-blocking audit.

### v1.4.1 — August 28, 2026

- **Audit-hygiene patch after the independent v1.4 import audit; no scientific state change.**
- Recorded the certificate-provenance chain for `NG_NG8A_ORBIT_CARDINAL_CERT_v1.md` / `NG_NG8B_REBLOCK_MULT_CERT_v1.md`: produced externally against v1.3, relayed to the corpus 2026-08-28, and cross-checked consistent — zero material discrepancies — with the independent in-corpus re-certification (`NG_NG8AB_INDEPENDENT_RECERT_v1.md`, `ng8ab_independent_recert_v1.py`, `.log`; all assertions pass, exit 0). NG-8A/NG-8B CLOSED status now rests on both certificate lines.
- Added the NG-8B **no-commutativity-from-grouping guard** (imported from certificate §9.7, with the deflationary within-track flattening clarification).
- Registered `NG_NG8AB_CROSSCHECK_v1.md` (three-way certificate cross-check and counting-convention table).
- Added the explicit NG-8A **state-counting predicate** `[DEF]` (SG-NG-11 discharge: distinct gauge-reduced tube states are observable-distinguishable, so "physically equinumerous" has a declared predicate).
- Reserved guard number **SG-NG-21** for the pending substrate-arity/derived-cardinal non-identity (decision D10), preventing numbering collision.
- Updated the stale §5 high-risk row for signed history to the CLOSED scoped N-2 status.
- **Pinned the declared primary transformation of `HYP-NG-0R-COV`** (amplitude scaling audited as flow-translation in `ln Q` via the `[CAND]` phi* entry-phase shift; explicit falsifier; `[CAND]` cap on the phi* leg) so the covariance audit stays pre-registered rather than post hoc.
- Provenance record: v1.4 replaced the v1.2 §6.1 two-notion `[DEF]` (count/order vs magnitude/ratio) with the three-notion `[DEF]` (relational/certificate/numerical); the earlier protection is subsumed by SG-NG-20/SG-NG-22 and the N-5A prerequisite. Recorded because tagged text was replaced without a changelog line in v1.4.

### v1.4 — August 28, 2026

- **Paradigm synchronization, not a new competing study:** retained Number Genesis as the owner DSN and made explicit the already-present composition-first / representation-after-construction semantics.
- Reframed the common foundation as a **relational category `C_NG`** with an admissible isomorphism groupoid `G_adm` plus generally non-invertible dynamical endomorphism monoids; avoided identifying primitive dynamics with a groupoid.
- Added **NG-0R** `[DEF]/[INTERP]` documentation layer and pre-registered `HYP-NG-0R-COV` as the only new falsifiable sector-covariance question from the ratio-relational reinterpretation.
- Added **SG-NG-22 relational-arrow / representation primitivity guard** and the explicit rule **proof order ≠ ontology order**.
- Clarified that `z_A z_B^-1` versus `theta_A-theta_B` in `U(1)` are two representations of the same invariant and cannot test ontological priority; recorded the absence of a nontrivial continuous homomorphism `U(1)->(R,+)`.
- Distinguished the three additive-representation mechanisms already present in NG: Track-A exponent map, genuine log-isomorphism only for a certified positive multiplicative sector, and compact-phase cover/character structures.
- Reframed N-5/N-6 in **classification-first** terms: Q-like/R-like labels classify certified commensurable/incommensurable relational structures; arbitrary primitive real-valued ratios remain rejected.
- **Closed NG-8A** from `NG_NG8A_ORBIT_CARDINAL_CERT_v1.md` using the post-event convention `S_m^+(x)={Tx,...,T^m x}`.
- **Closed NG-8B** from `NG_NG8B_REBLOCK_MULT_CERT_v1.md`; `<T^m>` inherits freeness and `(T^m)^k=T^(mk)`, with explicit guard that re-blocking is not a second N-5A generator.
- Upgraded the full NG-8 objective from a hypothetical universal counting object to **functorial/structure-preserving compatibility of Track-A, Track-B and Track-C invariants on the certified relational architecture**.
- Updated the active proof queue: NG-7A -> N-2-ORD -> N-4+N-5A -> N-5 -> N-6 -> full NG-8. NG-0R covariance audit runs in parallel and does not block the queue.
- Registered both NG-8 certificates in the Artifact Registry.

### v1.3 — August 27, 2026

- **State synchronization / no new NG theorem closure except upstream import:** refreshed verified pointers to Programme Overview v1.1, OFN v0.7, Dyadic v6.4.9, Discrete v2.12.13, and Genesis v2.8.4.
- Added explicit SG-PROG-2 / OPEN-P0 inheritance: all continuous-`T` arithmetic realizations remain conditional on generator selection at programme level.
- Synchronized N-1/N-1C headers with the already-certified local closure; the general branching/nondeterministic/topology-changing history quotient remains OPEN.
- Reclassified local eta-winding as `[FAIL]` for the N-1C separator role after N-3A's local triviality theorem; retained nonlocal/global winding as N-4 territory.
- **N-3C+ stale OPEN repaired:** imported Dyadic v6.4.9 `DYAD-THM-Q403-PHASELAW` and marked the exact `q=4,(0,3)` cascade item CLOSED-by-import. Ownership remains Dyadic.
- Routed remaining N-3C+ reachable-basis/universal missing-slot work to the Arithmetic-Dynamics/Dyadic OPEN-9 interface; removed it from the NG foundational priority head.
- Registered **N-2-ORD** `[OPEN][target: ALG]` for orbit-local physical order representation.
- Registered **N-5A** `[OPEN]` as a hard prerequisite to N-5: two independently certified event/recurrence streams must be co-realized under one RTG-native order relation.
- Tightened N-5: periodic/interleaving coding is a candidate only after its equivalence to commensurability is proved in the selected dynamical class.
- Tightened N-6 with **SG-NG-19 continuum substrate ceiling**; continuous-branch completion is representation/recovery level unless substrate-independence or a non-continuum bridge is proved.
- Added **SG-NG-20 single-generator ratio / co-realization guard**.
- Split NG-7 into **NG-7A** operator/null theorem and **NG-7B** physical-source/non-Abelian layer; imported OFN v0.7's discrete-phase-flat narrowing.
- Registered **NG-8A** ordinal→finite-state equinumerosity and **NG-8B** multiplication by physical re-blocking as `[OPEN][target: ALG]` seed theorems.
- Reordered the Number Genesis proof queue around the in-branch arithmetic foundation; N-1B-GROWTH moved to a parallel abstract-first robustness queue.
- Refreshed NG-10 to Genesis v2.8.4 §6.6 / `GEN-ART-SATURATION`; value and reduced-model scope unchanged.
- Added the programme-review audit memo and its independent DZT numerical reproduction script to the artifact registry as audit support only.
- Recorded that DZT v0.17 is audit-reported as the frozen current state but is not yet present as an owner source in the project corpus; v1.3 does not substitute the audit memo for that DSN.

### v1.2 — August 27, 2026

- Closed N-3C+ at the representation-kinematic level using the correct vector conjugation projector `C_R h = R^-1 o h o R`.
- Derived exact charge `chi_p(a,b)=a-b-1 mod p` and projector selection `a-b == 1 mod p`.
- Proved the first-nonlinear p-step cyclic-average theorem; p=6 quadratic six-step cancellation is kinematic because the resonant degree-2 support is empty.
- Reproduced the p=6 resonant slots through degree 5 and the first pure anti-holomorphic one-step resonant slot `(0,p-1)`.
- Added charge-reachability versus coefficient-cancellation boundary.
- Used the exact OPEN-9 p=8/p=12 q=4 `(0,3)` split to prove that subgroup character selection alone cannot explain the cancellation.
- Added the scalar Bessel residue projector as a separate exact object with an explicit non-conflation guard against Birkhoff/Lie cascade coefficients.
- Added `NG_N3C_PLUS_OPEN9_PROJECTOR_CERT_v1.md`, `ng_n3c_plus_projector_cert_v1.py`, and its log to the Artifact Registry.
- Reframed the immediate next action as the exact nonlinear q=4,(0,3) cubic cascade formula / reachable-basis missing-slot problem.


### v1.1 — 2026-08-27

- Closed N-3A locally: the dynamically induced eta-winding/deck cocycle is trivial on a sufficiently small one-chart N-1 tube; `ker rho_wind = G_T`.
- Closed N-3B as standard algebra: `G_T ~= widehat(S^1)` by the generator-to-generator character map, with explicit guard that this is not the primitive dynamical action.
- Closed the first exact N-3C result: `T^*chi_m = exp(i m(exp(rho)-1)) exp(-i m sin eta) chi_m`; primitive dynamics is non-translational in character labels and mixes Fourier sectors.
- Closed N-3D as pure representation theory: finite character restriction has kernel `N G_T` and quotient `G_T/(N G_T) ~= Z_N`; TDR-G dynamics remain behind the cross-branch firewall.
- Tightened N-3A scope: no claim about arbitrary bounded cycles; winding is the deck index of the natural lifted orbit relative to the one-chart trivialization, not a coordinate-floor surrogate.
- Added `NG_N3_REPRESENTATION_LAYER_CERT_v1.md` to the Artifact Registry.


### v0.8 — 2026-08-26

- Closed L1 directly from the exact primitive dyad map, without using an exact identification between normal-form amplitude and `Q_true`.
- Extracted the exact primitive six-step quartic coordinate jet and proved `Delta Q_4=-Q_true^2`.
- Extracted the exact degree-5 radial correction `Delta Q_5 = Q_true(5 eta^3-43 eta^2 rho+4 eta rho^2-5 rho^3)/24`.
- Converted the quintic correction to the anti-correlation polar frame and obtained the exact phase harmonic `A(phi)` with the explicit uniform bound `|A| <= 7/8+53 sqrt(3)/72`.
- Proved the phase-uniform primitive law `Delta Q_true=-Q_true^2+O(Q_true^(5/2))` and strict positive contraction on a sufficiently small punctured sector.
- Upgraded local block freeness from conditional to `[RESULT][from: ALG]`; the high-precision `q_*` witness is now illustrative rather than proof-critical.
- Entered F1 `[COR]`: primitive `Q_true` is not exactly the normal-form `|W|^2`; removed the false `O(Q^3)` primitive-frame remainder.
- Incorporated the independent 3000-block audit, exact witness identities conditional on an exact return root, scan-resolution-only uniqueness wording, and the `eta`-winding precision guard.
- Added the T-vs-F reduction lemma and routed the next task to primitive `T` event-type/domain alignment rather than rebasing N-1A/N-1B on `F=T^6`.
- Added Local Tag Aliases, repaired the duplicate boundary guard number (`SG-NG-17`) and malformed NG-10 `from:` tag, and added `SG-NG-18` coefficient-conflation guard.
- Added a formal Import Ledger and Artifact Registry. Current-version pointer targets are recorded from the independent audit; exact section/RID refresh is explicitly deferred where the source file was unavailable rather than guessed.

### v0.7 — 2026-08-26

- Executed `N-1C-DYAD — Radial Memory Test` on the exact primitive dyad map.
- Found a high-precision nontrivial canonical-family witness `q_* ~= 0.3156258836595616` for which `T^6` returns the wrapped phase exactly while `rho` and `Q_true` change; one future primitive step separates the phases by `exp(rho_6)-1 ~= 0.03120065132664947`.
- Added the important guard that this witness carries no `2pi` winding; radial memory therefore demonstrates history retention independently of winding and does not certify winding observability.
- Added a provisional local radial-contraction consequence from the six-step complex form; **superseded by v0.8 `[COR]`**, which removes the false exact `Q_NF=Q_true` identification and proves the primitive-frame law `Delta Q_true=-Q_true^2+O(Q_true^(5/2))` directly.
- Recast the congruence issue for deterministic fixed-generator realizations in terms of the induced transformation monoid, where extensional operational equivalence is a two-sided composition congruence on an invariant sector.
- Added a scoped definition of physical memory: present, relational, gauge-invariant information that survives a reduced-state return and is presently or prospectively observable.
- Recorded a 2000-block exact-map numerical monotonicity audit as support only; it is not used as an all-powers proof.
- Kept general N-1C OPEN pending alignment of the dyadic six-step generator with the N-1A/N-1B event-type construction.

### v0.6 — 2026-08-26

- Added the three-track counting architecture: ordinal/event history, cardinal/network multiplicity, and cyclic/periodic counting; NG-8 now carries the compatibility theorem target rather than assuming one primitive construction.
- Added operational history equivalence: histories are physically equivalent when no admissible future relational continuation/observable distinguishes them.
- Added scoped negative-control result `[FAIL] [scope: memoryless wrapped-S1 recurrence]`: rational return loops collapse to the identity history under operational equivalence if the complete physical state has no history-bearing variable beyond the wrapped phase.
- Reframed N-1C around the need for a physically effective relational memory state/cocycle; additive invariants are sufficient certificates, not necessary conditions.
- Guarded the dyadic winding index: it is a candidate history representation, not yet a certified physical counter because current dyadic results make it invisible to trigonometric observables and Foundations hold back lifted-memory physical status.
- Corrected the free-monoid wording to “canonically isomorphic once the distinguished generator is fixed”; noted that `1 -> 2` is not an automorphism of `(N,+,0)`.
- Reclassified spectator independence as a declared admissibility policy rather than a universal derived theorem.
- Added explicit N-3B relation to TDR-G `Z_N` as a representation-theoretic finite-distinguishability target only.
- Added NG-10 (Genesis saturation and counting truncation) with the guard that bounded amplitude alone does not imply bounded event history.
- Added the Genesis logarithmic phase/amplitude-ratio bridge as a downstream N-5/N-6 candidate connection, without promoting it to a derivation of `Q` or `R`.

### v0.5 — 2026-08-26

- Closed `N-1B-MIN` `[ALG]` `[scope: abstract fixed-support oriented recurrence R_d on S^1]`.
- Proved the reachable `E+` event graph has no terminal vertex because `R_d` is total; every finite `E+` path therefore has a one-edge extension.
- Recast periodic-return handling in path/category language: a non-empty closed recurrence path is not the identity/empty path unless an additional quotient imposes that relation.
- Added a metalanguage guard against using natural-number-valued path length as the physical reason histories are distinct.
- Added the physical-history-retention OPEN: the abstract path proof does not yet show that full RTG observables distinguish same-endpoint histories.
- Kept `N-1B-GROWTH` open as a topology-changing robustness test rather than a prerequisite for N-1C.
- Promoted `N-1C` to the immediate foundational target: define the physical history quotient and determine whether it is genuinely free on one generator before identifying it with `(N,+,0)`.

### v0.4 — 2026-08-26

- Closed `N-1A2` `[ALG]` `[scope: abstract three-node boundary-aware oriented phase-step with specified local law]`.
- Added explicit numerical strict-compatible (`beta=0.5`), context-dependent/same-type (`beta=0.2`), and type-changing (`beta=-2.0`) boundary cases at `x=0.4` for `F_S=x+1+beta`.
- Corrected boundary minimality: closure supplies one independent boundary coordinate relative to `x`; it does not by itself prove minimality.
- Replaced the flawed non-injective “proper quotient by common shift” argument with transition-relative minimality: any non-injective quotient of `beta` contradicts injective dependence of `F_S` on `beta` in the scoped law.
- Unblocked N-1B and selected fixed-support phase recurrence as the first successor/extensibility realization; network growth is deferred to `N-1B-GROWTH` as a stronger topology-changing test.
- Reformulated successor natively as “no terminal vertex in the reachable E-generated event graph,” avoiding dependence on a pre-assigned natural-number index.
- Added endpoint-recurrence/history-path guard: repeated phase endpoints do not by themselves terminate or identify event histories.

### v0.2 — 2026-08-26

- Refined N-1 into N-1A0 strict relational equivalence, N-1A1 counting equivalence, N-1B successor/extensibility, and N-1C free-history monoid.
- Replaced fixed-space group language by an admissible relational groupoid for local transition neighborhoods.
- Added transition-neighborhood object `(S_e, dS_e, X_e^- -> X_e^+)` and explicit boundary semantics.
- Added counting-type map `P`, strict-vs-counting equivalence guard, and fibre definition of event type.
- Added spectator-independence as a declared admissibility policy and explicit orientation-retention policy for primitive Number Genesis.
- Separated formal free-monoid existence from physical repeatability and unbounded natural-number realization.
- Added successor/extensibility condition and potential-infinity interpretation; no completed physical infinity is assumed.
- Routed immediate work to one concrete N-1A model test before attempting N-1B.

### v0.1 — 2026-08-26

- Opened Number Genesis as a dedicated RTG DSN.
- Registered central thesis: number as algebra of relational repetition `[HYP]`.
- Added N-1 through N-6 proof ladder.
- Added N-3B finite phase / character quotient bridge target.
- Added NG-7 recurrence-holonomy / holonomy-rank target.
- Added NG-8 universal counting-object (“two fives”) target.
- Added explicit metalanguage, reversibility, continuum, cross-branch, and external-overclaim guards.
- Routed immediate work to N-1, with NG-7 as parallel high-value theorem target.


---

## v0.3 Change Note

- Closed `N-1A-MIN` `[ALG]` `[scope: isolated abstract oriented dyadic phase-step]`.
- Reclassified general N-1A0/N-1A1 as `PARTIAL`: isolated identity is closed, boundary-aware identity is not.
- Opened `N-1A2 — Boundary Locality / Context Robustness`.
- Replaced the impossible “connected inert spectator” reading with a causal-interface partition `X=(x_S,b,y)`.
- Defined strict boundary compatibility through support/boundary isomorphisms satisfying attachment compatibility, gauge-reduced constraint preservation, orientation preservation, and transition equivariance.
- Added separate counting-level context compatibility and the spectator / boundary-context / causal-participant taxonomy.
- N-1B remains blocked for the boundary-aware event type until N-1A2 closes.


---

## v1.0 Result Note — N-2 Signed-History Completion

- Closed N-2 `[RESULT][from: ALG]` on the local Track-A primitive-dyad monoid.
- Defined the RTG-native pair relation `(A,B)~(C,D)` iff `A o D=B o C` using forward histories only.
- Proved equivalence, common-forward-extension invariance, well-defined abelian group law, injective embedding of `M_T`, infinite cyclicity, and the Grothendieck universal property.
- Interpreted group inverse as comparison-orientation swap `[A,B] -> [B,A]`, not physical `T^{-1}` or time reversal.
- Only after construction identified the group in the mathematical metalanguage as `(Z,+,0)`.
- Added N-1 scoping guards: distinguished generator does not imply uniqueness, local radius is existential, `T^6` is realization-specific, N-1 is a local realization rather than a universal arithmetic derivation, and general branching-history quotient semantics remain open.
- Added explicit Track-A/Track-B/Track-C NG-8 roadmap, bounded-state/unbounded-history cross-link to NG-10, continuous-branch scope guard, and alignment/N-2 proof certificates to the Artifact Registry.
- Unblocked N-3 dual `S^1` representation work.

---

## v0.9 Result Note — Unified Primitive T Alignment

`[RESULT][from: ALG]` N-1 is closed on a sufficiently small punctured primitive-dyad six-phase tube. The tube construction makes `T` an endomorphism of one common sector; mechanism-level T-step tokens supply N-1A, tube invariance supplies N-1B, and L1 plus the T-vs-F reduction excludes all finite power relations. The transformation monoid generated by `T` is therefore free monogenic and canonically represented by `(N,+,0)` once the distinguished generator is fixed. N-2 is unblocked; N-1B-GROWTH and NG-8 remain separate robustness/bridge problems.
