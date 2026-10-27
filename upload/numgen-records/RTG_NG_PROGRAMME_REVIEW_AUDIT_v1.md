# RTG Number Genesis — Programme-Review Audit v1

**Date:** August 27, 2026
**Auditor:** Claude (mathematical auditor / DSN editor role)
**Audited object:** external strategic review "Number Genesis from first principles" (three-programme reorganization proposal), submitted against `RTG_NUMBER_GENESIS_DSN_v1.2` and the project-folder corpus snapshot.
**Sources checked:** NG v1.2 (uploaded, full read) · Dyadic v6.4.9 · DZT v0.8 (project copy) + DZT v0.17 session record · AZ/Zeta v0.6 · OFN v0.7 · Genesis v2.8.4 · Discrete Genesis v2.12.13 · Programme Overview v1.1.
**Document class:** audit memo. Nothing here changes any claim status; all direction and interpretive choices are batched for PI ruling in §7.

---

## §1. Verdict Summary

The review is substantially accurate and its structural proposal is sound. Of its factual claims, all verified against sources except **one material staleness**: the review's Lane B flagship target — "prove/falsify the DZT odd-prime anomaly law" — was **already closed at theorem grade** in DZT v0.9–v0.17 (`DZT-THM-CASCADE-ODD-SUPPORT` and `DZT-THM-CASCADE-DENOMINATOR`, both `[THM]`; stream frozen at v0.17 as a closure freeze). The reviewer worked from the stale project-folder DZT v0.8 snapshot, which still carries the pattern as `[ALG finite horizon, p≤1000]` with an open proof target. I independently reproduced both theorems numerically today from the imported Dyadic closed form (60 points p=12–248, 0 mismatches; artifact `ng_review_dzt_independent_audit_v1.py`).

Consequences: Lane B must be re-anchored (§4.8); the proposed "Arithmetic Dynamics" sister programme launches with a completed flagship theorem pair rather than an open conjecture (which strengthens, not weakens, the reorganization case); and the project folder needs a DZT v0.17 upload so external reviewers stop consuming v0.8.

Beyond that correction, my main critical additions are: (i) N-5's physical substrate is genuinely under-specified — the single-generator tube cannot carry rationals non-circularly, and this must be made an explicit prerequisite module before N-5 is promoted (§4.2); (ii) N-6 in the continuous branch has a **substrate-circularity ceiling** that no current guard covers — I propose SG-NG-19 (§4.3); (iii) Track B (cardinal) is homeless under the firewall as currently conceived, but an in-branch cardinal object exists and yields two immediately provable NG-8 seed theorems (§5.3); (iv) NG-7 should be split into a closable operator half and a PI-gated source half, with the OFN v0.7 §9 narrowing imported (§5.4).

---

## §2. Claim-by-Claim Verification Table

| # | Review claim | Source checked | Verdict |
|---|---|---|---|
| 1 | NG central thesis / metalanguage guard as quoted | NG v1.2 §0, §1.2, SG-NG-1 | ✓ |
| 2 | AZ goal explicitly not RH proof/disproof/reformulation | DZT §1 (SG-DZT-4), AZ v0.6 §status | ✓ |
| 3 | `4\|q` rule failed dynamical null; reclassified static Z_N antipodal-band geometry | AZ v0.6 status, §4.3.3–4.3.4, AZ-2 "attempted, negative-clarifying" | ✓ |
| 4 | Genesis ladder is a research ordering, not a theorem chain | NG v1.2 line ~82 `[DEF]` | ✓ |
| 5 | N-1: `T^r x ≠ T^s x` on punctured tube; `M_T` free monogenic ≅ (ℕ,+,0) | NG v1.2 v0.9 alignment block (lines 786–825), `[RESULT][from: ALG]` | ✓ (scoped: local, existential radius, realization-not-uniqueness) |
| 6 | OPEN-P0 ceiling applies to N-1 | Programme Overview SG-PROG-2; Dyadic SG-14 | ✓ in substance; **NG v1.2 does not explicitly cite SG-PROG-2/OPEN-P0** — housekeeping item §6.7 |
| 7 | N-2: pair relation `(A,B)~(C,D) ⟺ A∘D=B∘C`; `G_T≅ℤ`; `−[A,B]=[B,A]` = orientation reversal, not `T⁻¹` | NG v1.2 N-2 block | ✓ |
| 8 | N-3: local ρ_wind ≡ 0; `G_T ≅ Ŝ¹` abstract-faithful; primitive pullback mixes harmonic sectors, no fixed-label translation | NG v1.2 N-3A/B/C | ✓ |
| 9 | Three-track (ordinal/cardinal/cyclic) architecture exists as a subsection | NG v1.2 §1.2a | ✓ |
| 10 | v1.2 priority list begins N-3C+, then N-1B-GROWTH, NG-7 | NG v1.2 §2 | ✓ (note: list numbering skips 5 and 7 — cosmetic defect) |
| 11 | N-3C+ still lists "derive exact q=4,(0,3) cubic cascade formula" as OPEN | NG v1.2 §8 item 5, §2 N-3C+ | ✓ stale, as claimed |
| 12 | Dyadic v6.4.9 closed the q=4,(0,3) cascade all-p | Dyadic v6.4.9 §6.11, **DYAD-THM-Q403-PHASELAW**, closed form `Q(L,I)=L⁵(IL²+I−L²+1)/(2(L+1)⁴(L²+L+1))`, family p=4s, s≥2, p=8 zero degeneracy | ✓ |
| 13 | DZT: `R_C(p)=Res(Φ_p,P_C)`; Case-V `M_p=Q_p/(iζ_p³)∈ℚ(ζ_p)⁺` | DZT v0.8 §1 | ✓ |
| 14 | Anomaly law: `N₊(M_p)` audit p≤1000; anomalies exactly `p=8ℓ^a`, `ℓ^a≡1 (mod 4)`, numerator `ℓ²`; proof target `Res(Φ_{8q},A_s)` with `A_s=L^{s+2}+L^s−L²+1` | DZT v0.8 (DZT-ALG-CASCADE-ANOMALY-SET, DZT-OPEN-0B-R) | ✓ faithful to v0.8, **but stale — see §3** |
| 15 | "No missing Dyadic computation blocks it" | DZT v0.8 ("upstream gate is gone") | ✓ but moot — already proven (v0.17) |
| 16 | NG-7 ↔ Foundations interface; cycle rank ≠ holonomy rank; NG-7 could supply the OFN OPEN's operator | OFN v0.7 §4.4 rank typing; `RTG-OFN-OPEN-HOLONOMY-RANK-DIAGNOSTIC` (v0.7 §OPEN block); NG-7 spec matches the closure criterion exactly | ✓, plus refinement §5.4 |
| 17 | NG-10 pointer refresh needed (Genesis v2.8.4) | NG v1.2 inline `[source: v2.7.5 §6.6]` vs import ledger "reverify" | ✓ — **reverification completed by this audit**: Genesis v2.8.4 §6.6 carries the same `Q_d*≈1.13×10⁻²` (checksum-certified). Repoint is safe. |
| 18 | "Local ℕ, ℤ construction largely CLOSED" | NG v1.2 closure verdicts | ✓ with scope tags retained; internal header staleness (N-1C "ACTIVE") is a separate defect — §6.4 |
| 19 | Lane B follow-ups: missing-slot rules, all-b≥5 persistence | Dyadic v6.4.9 §1 "active frontier" | ✓ — these are the already-queued Dyadic OPEN-9 horizon program |

One review-internal defect: the closing roadmap graphic marks **two** arrows with ✓ (`ℕ →✓ ℤ →✓ ℚ`). Only ℕ→ℤ is closed; ℤ→ℚ (N-5) is `[OPEN]`. Presumably a typo, but under status discipline the graphic overclaims by one arrow and should be fixed before any of the review's text is imported into a DSN.

---

## §3. Material Correction — DZT State (Lane B Target Already Closed)

**Session record (DZT stream, closure freeze v0.17):**

- `DZT-THM-CASCADE-ODD-SUPPORT` `[THM]` — odd part of the numerator of `N₊(M_p)` equals `ℓ²` **iff** `p = 8ℓ^a` with `ℓ^a ≡ 1 (mod 4)`; otherwise 1. All-p, channel-local. This is exactly the law the review proposes as Lane B's first theorem target.
- `DZT-THM-CASCADE-DENOMINATOR` `[THM]` — denominator exponent `d_p = φ(p)/4 + [p=2^k] + [p=3·2^k]`, all-p; proved via Apostol's resultant theorem, the `Φ_d(1)` norm formula, and real-subfield halving. (Note: v0.8's "no denominator formula holds" was itself superseded — the review's snapshot predates both theorems.)
- Channel universality **closed negative** (admissibility gate `q | (b+1)`; the phase×real-subfield factorization fails on substitute channels) — so "extend the norm invariant to other channels" is a *closed negative*, not an open Lane B direction.
- Track B1 (formal local NF zeta) weight audit complete (W^(A) rejected, W^(B) resolved as controlled leading-log hierarchy, W^(C) FAIL/redundant). Stream frozen at v0.17: "no v0.18 unless new science."

**Independent reproduction (today).** From the imported closed form and `M_p = Q_p/(iζ_p³)`, I computed `N₊(M_p) = ∏_{k∈(ℤ/p)^*/±1} σ_k(M_p)` at dps=60 for all p=4s, 12 ≤ p ≤ 248 (60 points):

- Every value is exactly `±(odd)²·2^(−d_p)` with `d_p` matching the denominator theorem at all 60 points, including the corner classes p=2^k (16, 32, 64, 128) and p=3·2^k (12, 24, 48, 96, 192).
- Anomalies occur exactly at p ∈ {40, 72, 104, 136, 200, 232} = 8·{5, 9, 13, 17, 25, 29}, all ≡ 1 (mod 4), with numerators 5², 3², 13², 17², 5², 29². All q≡3 (mod 4) prime-power points (24, 56, 88, 152, 184, 216) and all non-prime-power odd-part points (120, 168, …) are clean.
- 0/60 mismatches. Artifact: `ng_review_dzt_independent_audit_v1.py`.

**Residual observable (diagnostic only, no new OPEN proposed without PI):** the *sign* of `N₊(M_p)` varies (e.g. −1 at 16, 20, 24; +1 at 12, 28, 56) and is not covered by either theorem, which govern |numerator| and denominator. If the DZT ever unfreezes, a sign law would be new science of exactly the right size; I flag it only as a note.

**Actions implied:** (a) NG v1.3 must cite the v0.17 state, not v0.8, wherever N-3C+ interfaces with the cascade; (b) the project folder should receive the v0.17 file (PI action — reviewers keep consuming v0.8); (c) Lane B re-anchoring in §4.8.

---

## §4. Structural Critique of the Proposal

### §4.1 The three-programme split — endorse, with mechanics

The split (I. Number Genesis ∥ II. Arithmetic of RTG Dynamics ∥ III. Bridges/Null) is a *labeling of what already exists*: NG DSN; Dyadic-OPEN-9 + DZT; AZ. The arrows-run-in-opposite-directions argument (§12 of the review: `T → resonance → cyclotomic → number field` vs `event → history → arithmetic`) is correct and is the strongest justification given. Constraints on execution:

1. **Ownership must survive the umbrella.** "Arithmetic Dynamics" is a programme *label* over two DSNs with an existing ownership contract (Dyadic owns p-resonance facts; DZT owns transforms; SG-DZT-1–8). No ledger merge.
2. **RID stability.** The NG-I…NG-IV relayering must not rename RIDs. A mapping table (old module label → new layer) goes into the changelog; RIDs are permanent.
3. **Registration point.** Programme-level naming belongs in a Programme Overview v1.2, which is a PI decision (§7-D1). Until then the split can operate as NG-internal §-structure only.
4. **AZ disposition.** Endorse "infrastructure for now" — it matches AZ v0.6's own self-assessment (Level A, success criterion NOT met, AZ-2 negative-clarifying). Do not dissolve it: the core-matched random-theta null harness and PROP-AZ-CORE-EQUIV `[THM-ALG]` are reusable Thread-C-owned assets.
5. **Naming.** Avoid collision with the existing "AZ" short name. Suggest programme labels **NG / AD / AZ-Null**, with AD = {Dyadic OPEN-9 horizon (owner: Dyadic DSN), DZT (owner: DZT DSN, frozen v0.17)}.

### §4.2 N-5 promotion — agree on target, but the physical substrate is missing and must be made a prerequisite module

The review argues N-5 (ℤ→ℚ) should move up because it is "the most natural next question." Directionally right, but the review under-weights a structural fact: **the certified sector has exactly one distinguished generator.** Ratios formed from powers of a single generator (`T^m` vs `T^n`) are the standard localization of the already-constructed monoid — pure `[MATH]` (SG-NG-9 territory), not a physical genesis of ℚ. NG v1.2's own candidate relation `E_A^p ~ E_B^q` presupposes two independently repeatable processes A, B, and never says where the second one comes from. Worse, the natural second process on the tube is degenerate by NG's *own results*: N-3A proves local winding trivial, and the memoryless wrapped-S¹ `[FAIL]` shows phase-return loops collapse operationally. The tube supplies one free counter and no certified second recurrence.

So N-5, as promoted, is **blocked in substance** on one of: (a) N-4-scale domain extension (where a second frequency — e.g. amplitude-dependent internal rotation vs block count — can become nondegenerate; note the review's own ordering N-4 before N-5 accidentally respects this, but the dependency should be explicit, not accidental); (b) a second certified event type from an N-1A-style construction (e.g. a declared Poincaré-section-crossing event predicate — legitimate, but it is a *new counting map P* and must be registered as such, not smuggled); or (c) a cross-stream realization (firewalled; PI-gated).

**Recommendation:** promote N-5 only together with a new prerequisite sub-module **N-5A — Second-generator existence** (registered `[OPEN]`, with the candidate list above and a cheapest-falsification test for each candidate), plus a guard **SG-NG-20 (single-generator ratio guard):** *ratios of powers of one certified generator are metalanguage localization of the Track-A monoid and do not close N-5; N-5 requires two independently certified event types with a declared physical closure criterion.* This blocks the cheapest fake closure before it is ever attempted.

### §4.3 N-6 — a substrate-circularity ceiling that no current guard covers

The continuous-branch realization lives on a continuum state space (the (ρ,η) chart is an ℝ²-manifold). For ℕ and ℤ this is harmless: the freeness proof consumes only distinguishability of iterates, not the continuum structure of the substrate. For ℚ (order/interleaving data) it is still mostly harmless. For ℝ it bites: deriving "ℝ-like completion" from dynamics whose substrate already *is* a continuum can only ever be a **representation-level** theorem ("the substrate's continuum can be re-coordinatized by recurrence-comparison classes"), never a genesis of the continuum. SG-NG-5 does not cover this — it forbids continuum assumptions in the *premises of the derivation*, not in the *substrate of the realization*. A genesis-grade N-6 would require a realization whose substrate is not already a continuum — i.e. the discrete branch — which is firewalled (SG-PROG-1) and excluded by NG's own continuous-branch-only guard.

**Recommendation:** add **SG-NG-19 (continuum substrate ceiling):** *N-6 closures obtained in the continuous branch are representation-level results relative to a continuum substrate; a genesis-level N-6 claim requires either a discrete-substrate realization behind a named bridge theorem, or an explicitly tagged postulate.* Additionally, add a lightweight "presupposition" line to each Nk module stating which substrate structures it consumes (continuum chart / U(1) fiber / graph cardinality). This makes the ceiling auditable and closes the substrate side-door on exactly the overclaim Appendix B already rejects in its premise-form.

This does **not** kill N-6 — it clarifies what N-6 can honestly deliver in-branch (see §5.2 for the constructive route), and routes the stronger claim to a future bridge.

### §4.4 Track B is homeless under the firewall — and NG-8 is blocked on it

The review makes NG-8 the deepest target but does not say where Track B (cardinal) will get its construction. The natural cardinal objects — nodes, components, births — live in TDR-G and Genesis, behind SG-PROG-1/SG-NG-3. As written, NG-8 has one certified leg (Track A), one abstract leg (Track C, faithful only abstractly), and one leg with no in-branch source at all. §5.3 supplies an in-branch Track B candidate and two provable seed theorems; without something of that kind, NG-8 should not be advertised as reachable.

### §4.5 N-1B-GROWTH at Lane-A slot 1 — flag the hidden cross-stream dependency

N-1B-GROWTH as scoped in v1.2 asks for a *topology-changing* realization (birth/network growth). The continuous dyad has no topology change. The realizations on offer are Genesis birth events or TDR-G star blow-ups — both cross-stream. So slot A1 is either (a) a bridge-flavored module requiring a PI ruling on whether a Genesis birth event is an admissible N-1A event model (realization-level import, not coefficient import — likely permissible, but it is a judgment call), or (b) an abstract growth test law in the N-1A2 style — cheap but correspondingly weak. The review presents A1 as a pure in-branch item; it is not. Recommend the ordering keep A1 but with the dependency and the (a)/(b) fork stated, and the fork batched to PI (§7-D4).

### §4.6 N-3C+ demotion — right conclusion, refine the mechanics

Since the stale OPEN (item 5) is closed upstream, what remains of N-3C+ is item 6: lifting the charge-reachability rule into the reachable-basis projector formalism for universal missing-slot proofs. That is Lane B material (the representation layer of the Dyadic missing-slot program), not a Number Genesis foundation. Correct v1.3 move: mark item 5 CLOSED-by-import (`[import-ref: DYAD-THM-Q403-PHASELAW, Dyadic v6.4.9 §6.11]`), re-route item 6 to the AD-lane interface, remove N-3C+ from the NG priority list. This implements the review's demotion with clean bookkeeping instead of a wholesale drop.

### §4.7 N-4 taxonomy

The review files N-4 under NG-II (representation of count). In v1.2, N-4 is really the *domain-extension* module for both the Track-A realization and the representation layer (it is where nontrivial winding could first appear). Listing it inside NG-II obscures that NG-I's locality is also at stake there. Cosmetic: present N-4 as a domain-extension module orthogonal to the NG-I/NG-II split.

### §4.8 Lane B re-anchoring (post-correction)

With the anomaly and denominator theorems closed and channel universality closed negative, Lane B's honest state is: the arithmetic-resonance transform story for this channel is **complete**, and the live arithmetic frontier is the one already queued **in the Dyadic stream**: the σ_b secular-source symbolic recursion phase (step factor σ_{b+1}=R_b(λ)σ_b), the b=21 extraction run (p=23,47,95,191, dps=200), the meromorphic-vs-log-corrected fork at λ=1, universal missing-slot rules, and the all-b≥5 persistence extension. Lane B's first target should therefore read "execute the queued Dyadic OPEN-9 horizon program," with DZT remaining frozen unless a genuinely new transform-level object appears (the sign observable of §3 is the only candidate currently visible, and it is minor). The review's Lane B ordering after its first item survives unchanged.

---

## §5. Contributions

### §5.1 N-5 constructive route — commensurability as interleaving order (no real-valued periods)

Once N-5A supplies two recurrent event streams, define commensurability **operationally via event order only**: the physical datum is the comparison word w ∈ {A,B}^ℕ recording which stream's recurrence event fires next (ties resolved by a declared convention). Then:

- **Commensurate** ⟺ w is eventually periodic; the closure class of the periodic block (p occurrences of A per q of B) *is* the rational, with `(p,q)~(kp,kq)` invariance holding at the word level (block repetition), exactly discharging v1.2's "prove rescaling independence" obligation without ever invoking ℚ as physical input.
- Composition/product on closure classes: word concatenation over synchronized closure events gives addition of ratios; re-blocking (see §5.3, NG-8B) gives multiplication. Both are defined on words before any representation map.

This meets SG-NG-5 and SG-NG-6 by construction: no ℝ₊-valued frequency, no external clock — only relational event order (which is also exactly the causal-order time-semantics layer; consistent with the programme's time-semantics tri-layer, no import needed).

### §5.2 N-6 route — rotation number as the completion object (representation-level, per SG-NG-19)

For incommensurate streams the comparison word is Sturmian, and the standard rotation-number machinery gives precisely the physically honest completion: the asymptotic slope of w exists (subadditivity), is invariant under admissible re-anchoring, and is **rational iff the interleaving is eventually periodic** — i.e. Poincaré's rational-rotation ⟺ periodic-orbit dichotomy becomes the *physical* commensurability criterion. The real number then enters as an equivalence class of order-histories (Dedekind cut on comparison words: "does mA precede nB eventually?"), with the three-distance/Sturmian structure as the finite-observation theory of approximants. This is v1.2 §6.7's third bullet, promoted to primary candidate and made concrete. Under SG-NG-19 it is registered as a representation-level result: it shows the substrate's continuum is *recoverable from event order alone*, which is a real theorem, honestly scoped.

### §5.3 NG-8 seed theorems — an in-branch Track B and two provable compatibility legs

**Anti-vacuity guard first:** any two free monogenic monoids are abstractly isomorphic, so NG-8's content must be *physically implemented comparison maps*, never bare isomorphisms.

- **NG-8A (ordinal → cardinal, orbit-set map).** In-branch cardinal object: finite sets of *distinct relational states*. The map "run the history, collect the visited states" sends the length-m history to the orbit set {x, Tx, …, T^{m−1}x}. N-1's freeness theorem says exactly that these m states are pairwise distinct — so the map is count-preserving: m repetitions produce a set of cardinality m. Trivial *given* N-1, but it is the first genuinely physical Track-A→Track-B arrow, and it is provable today. `[ALG target, one session]`.
- **NG-8B (multiplication as re-blocking).** The submonoid ⟨T^m⟩ ⊂ M_T is free monogenic on T^m (freeness inherited), and the inclusion realizes k ↦ mk physically as "count in blocks of m." This is the physical content of `(E^m)^n = E^{mn}` from the review's compatibility list — the multiplicative leg of NG-8, provable now from N-1 alone. `[ALG target, one session]`. (The L1 T-vs-F reduction lemma is the m=6 instance already in the ledger.)
- **Track B enrichment (harder, later):** spectral multiplicity as a second in-branch cardinal — ranks of the N-3C+ residue projectors Π_r, and a Krylov-type statement (dimension of span of orbit observables = history length under an explicit genericity condition) tying ordinal m to a *linear-algebraic* cardinal m. Registered as a candidate only; needs a genericity certificate.

These give NG-8 a concrete on-ramp instead of "deepest target, start last."

### §5.4 NG-7 — split, formalize, and connect to Case E2

- **NG-7A (operator half — closable now).** Additive form: edge cochain a ∈ C¹(G;ℝ^d); holonomy = class in H¹; `r_hol = rank(C·A)`. Null theorem `C·Dᵀ = 0` is ∂∂ = 0. Cycle-basis independence: bases differ by GL(β₁,ℤ), rank invariant. Gauge invariance: A ↦ A + DᵀX fixes C·A. Missing/zero ratios: declare the multiplicative domain and treat undefined edges by subgraph restriction (state the convention; it is the only genuine design choice). Items 1–7 of the v1.2 proof package are one `[ALG]` + one `[ENG]` certificate away. Closing NG-7A **discharges the operator half of `RTG-OFN-OPEN-HOLONOMY-RANK-DIAGNOSTIC`** (OFN v0.7 closure criterion matches this spec verbatim: affine rank / cycle rank / holonomy rank with node-difference data forced to zero for all β₁).
- **NG-7B (source half — the real OPEN, PI-gated).** OFN v0.7 §9 has already *narrowed the search*: the discrete phase sector is proven holonomy-flat (all edge data are node differences; validated on K₈, β₁=21), so the candidate sources are continuous frame/connection data, spin structure, birth history, or OPEN-M content. NG v1.2's candidate list should import this narrowing. The non-abelian upgrade (holonomy homomorphism ρ: π₁ → SU(2) mod conjugation; holonomy rank = independent-generator count of the image) is exactly the object the planned **Case E2** rung-3 test (rank π₁ ≥ 2, matrix-flat SU(2), flatness + topology guards) will exercise — NG-7A should be built so E2 can consume it directly.
- Citation fix: NG v1.2 cites "RTG_ONTOLOGICAL_FOUNDATIONS_v0.6 OPEN-HOLONOMY-RANK-DIAGNOSTIC"; the canonical RID is `RTG-OFN-OPEN-HOLONOMY-RANK-DIAGNOSTIC`, current source v0.7.

### §5.5 Candidate small module — physical order representation (N-2-ORD)

The ladder uses the order on ℕ/ℤ downstream (N-5 orientation conventions; N-6 Dedekind cuts) without ever registering *order* as physically represented. On the tube, L1 gives strict `Q_true` monotonicity along F-blocks, so block-graded history length is ordered by a present-state observable; the per-primitive-step refinement needs the (Q-band, phase-index) pair and a half page of care. Propose registering **N-2-ORD** `[ALG target]`: the signed-history order on G_T is realized on each orbit by a declared present/future observable comparison procedure (block-graded version first). Cheap, and it hardens the N-6 Dedekind route.

### §5.6 Proposed guards (consolidated)

- **SG-NG-19** — continuum substrate ceiling (§4.3).
- **SG-NG-20** — single-generator ratio guard (§4.2).
- **SG-NG-AD-1** (inter-programme, if the split is registered) — no arithmetic-dynamics structure (cyclotomic coefficients, resonance laws, field norms) may be used as evidence for a genesis claim without an NG-native derivation; numerals and number fields appearing in AD theorems are metalanguage relative to NG.
- **SG-NG-AD-2** — NG genesis results confer no physical-primitivity status on AD coefficients; SG-PROG-2/OPEN-P0 continues to cap everything on both sides.

### §5.7 Completed pointer revalidation (was deferred in NG v1.2 line 8)

All performed against the live project sources today; **no value changed anywhere**, so per the v1.2 guard these are pure pointer refreshes with no status effect:

| NG v1.2 citation | Verified current target | Notes |
|---|---|---|
| OFN v0.6 §1.1 (relational primacy) | **OFN v0.7 §1.1** | content present verbatim-equivalent |
| OFN v0.6 §1.2 (no external physical time) | **OFN v0.7 §1.2** ("Background Independence") | content present; OPEN-OFN-7 cross-ref intact |
| Dyadic v6.0 §6.2, §6.4 (order-6 elliptic; winding ℓ, invisibility) | **Dyadic v6.4.9 §6.1** (P₁ elliptic order-6) **+ §6.4** (ℓ definition; `[ALG]` winding-index invisibility) | §-number shift for the fixed-point item (6.2→6.1); §6.4 unchanged |
| Discrete v2.4 SG-10; Dyadic v6.0 SG-14 (firewall) | **Discrete v2.12.13 SG-10; Dyadic v6.4.9 SG-14** | guard numbers unchanged in both |
| Genesis v2.7.5 §6.6 (NG-10 ceiling `Q_d*≈1.13×10⁻²`) | **Genesis v2.8.4 §6.6** | value unchanged, checksum-certified in v2.8.4 |
| OFN v0.6 OPEN-HOLONOMY-RANK-DIAGNOSTIC | **OFN v0.7, RID `RTG-OFN-OPEN-HOLONOMY-RANK-DIAGNOSTIC`** | full RID; import §9 narrowing (discrete sector flat) |
| Dyadic v6.4.9 companion pointer | unchanged | additionally cite DYAD-THM-Q403-PHASELAW §6.11 at N-3C+ |
| DZT (not currently cited in NG) | **DZT v0.17 (frozen)** for any N-3C+/AD interface | do not cite v0.8's OPEN-0B-R as open |

---

## §6. NG v1.3 Housekeeping Checklist (verified edits only; no new science)

1. **N-3C+ / §8:** mark item 5 CLOSED-by-import (`DYAD-THM-Q403-PHASELAW`, Dyadic v6.4.9 §6.11; family p=4s, s≥2; p=8 zero degeneracy; closed form recorded as `[import-ref]`). Re-route item 6 to the AD interface. Replace §8's "Immediate technical module" (now stale) — successor per PI ruling D2/D3.
2. **Priority list (§2):** remove N-3C+; fix the numbering gap (currently 1,2,3,4,6,8,9,10,11); reorder per PI ruling on Lane A.
3. **Pointer refreshes:** apply the §5.7 table (all pre-verified). Update §9.1 import-ledger rows accordingly and change the stale column header "Validation state at v0.8" → "at v1.3". Remove the line-8 "revalidation pending" disclaimer for the rows now verified.
4. **Header/status synchronization:** N-1C header ("Status: ACTIVE — … immediate foundational target") and N-1C-DYAD wording predate the v0.9 closure — align with the N-1 closure verdict while keeping the *general* history-quotient semantics OPEN (line-839 guard stays). Normalize the "OPEN N-1"-style heading prefixes on closed modules (N-1, N-1A2 headers vs their CLOSED statuses).
5. **§1.2a table:** Track C module list "N-3, N-3B" → "N-3A–N-3D".
6. **NG-7:** citation fix (§5.7); import the OFN v0.7 §9 source-narrowing into the candidate list; optionally split NG-7A/7B per §5.4 (PI ruling D5).
7. **Add explicit programme-ceiling line:** next to the "distinguished generator" guard, cite SG-PROG-2/OPEN-P0 inheritance explicitly (NG currently carries the logic locally but not the programme-level RID; DZT sets the precedent).
8. **New guards:** SG-NG-19, SG-NG-20 (per PI ruling D6); SG-NG-AD-1/2 only if the programme split is registered (D1).
9. **If adopted:** register N-5A (`[OPEN]`, prerequisite of N-5), NG-8A/NG-8B (`[ALG target]`), N-2-ORD (`[ALG target]`), NG-7A/7B split.
10. **Changelog:** record the review-import as a structural v1.3 (two-pass rule: structural repair first, content integration second; per policy, this cluster of pointer repairs + one genuine state change (N-3C+ item-5 closure-by-import) justifies the version bump).

Separately (not an NG edit): **upload DZT v0.17 to the project folder** so the canonical snapshot matches the frozen state.

---

## §7. Batched PI Decisions

- **D1 — Register the three-programme architecture** (NG / AD / AZ-Null) in a Programme Overview v1.2, or keep it NG-internal for now? (Affects SG-NG-AD-1/2 registration.)
- **D2 — Lane A ordering.** Review proposes A1 N-1B-GROWTH → A2 N-4 → A3 N-5 → A4 N-6 → A5 NG-8, NG-7 parallel. My amendments: insert N-5A before N-5; take NG-8A/8B early (cheap, provable now, and they de-risk the "deepest target"); resolve the N-1B-GROWTH fork (D4). Choose ordering.
- **D3 — Lane B first target** post-correction: adopt "execute the queued Dyadic OPEN-9 horizon program (σ_b recursion / b=21 run / λ=1 fork; missing-slot rules; all-b≥5)" as Lane B's head, DZT stays frozen. Confirm.
- **D4 — N-1B-GROWTH realization fork:** (a) Genesis-birth-event realization (needs a ruling that a birth event is an admissible N-1A event model — realization-level, not coefficient import), or (b) abstract growth test law first. Choose.
- **D5 — NG-7A/7B split** and NG-7A execution (one `[ALG]`+`[ENG]` certificate; discharges the operator half of the OFN OPEN). Approve/defer.
- **D6 — New guards** SG-NG-19 / SG-NG-20 adoption.
- **D7 — Housekeeping v1.3** per §6: approve execution (I can produce the full v1.3 in one two-pass edit once D1–D6 are ruled, or execute the pure-housekeeping subset (§6 items 1–5, 7) immediately with the science-ordering items deferred).
- **D8 — Project-knowledge refresh:** upload DZT v0.17 (and confirm OFN v0.7, Zeta v0.6, Dyadic v6.4.9, Genesis v2.8.4, Discrete v2.12.13 remain the live masters — all consistent with today's checks).

---

## Artifact Registry (this audit)

| Artifact | Role | Status |
|---|---|---|
| `ng_review_dzt_independent_audit_v1.py` | independent reproduction of DZT-THM-CASCADE-ODD-SUPPORT + DZT-THM-CASCADE-DENOMINATOR from the imported closed form; 60 points p=12–248, 0 mismatches | `[NUM]` audit support |
| `RTG_NG_PROGRAMME_REVIEW_AUDIT_v1.md` | this document | audit memo |

*End of audit. No claim statuses were changed by this document.*
