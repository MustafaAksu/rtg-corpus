> **[SUPERSEDED 2026-09-30] by NG_C7C_M2_PREREG_DRAFT_v3.md (witness-typed domain, M2-1/M2-2, frozen κ_b registry). Content without this banner hashes to 1abeced01aff513550144767240cad874bb2c7877b4bdb0665039c980a18c390.**

# C7C-M2 — Interface Object and Saturated WD-DOM · Preregistration DRAFT v2

**Doc ID:** `NG_C7C_M2_PREREG_DRAFT_v2` · supersedes `_v1` (`e654abd3…794b`) · **Date:** 2026-09-29
**Co-owner audit of v1:** Π out of the interface GO; levels a/b + matrix GO after `~_b` is a true equivalence; level-b event type GO with a frozen operational criterion; existing DISC evidence GO with no new search and P2 quarantine. All four repairs are incorporated below; no other change. · **Base:** frozen v1.20.6 (`2a51c4b1…48c5`)
**Status:** DRAFT for co-owner audit. Design only — no computation, no realization search. Nothing here is a result.
**Frontier (owner, §6.6 N5-C7C-M):** *Full-interface typed WD-DOM — which relational interface information carries physical composition, and under which quotient it descends without loss.*
**Standing hard guard (v1.20.6 manifest):** interface equivalence is defined without reference to `rho_Q`.

---

## 0. Finding before drafting: the primary test as proposed is vacuous

Proposed test: *if `(x,y) ∈ D_I`, `x ≡_Q x′`, `y ≡_Q y′`, and `x′, y′` are interface-equivalent representatives, is `(x′,y′) ∈ D_I`?*

If `D_I` is defined by interface compatibility and the equivalence `~_I` compares the whole tuple `(B, 𝒫_B, ι_L, ι_R, 𝒯, Π)` — **including Π, the outer-pair compatibility** — then assuming `x′, y′` interface-equivalent already assumes the Π-data equal, and `(x′,y′) ∈ D_I` holds **by construction**. The test could not fail, so its PASS would be manufactured. This is the domain-side analogue of what WD-REP forbids for the product formula.

**Repair (proposed, §2):** Π is removed from the interface and becomes the **dependent variable** of the test. The interface is what the two factors *share* at the composition point; Π is what the composition *needs* at the outer ends. The question becomes non-trivial: does sharing an equivalent middle interface and equal labels force outer admissibility?

## 1. Carrier (unchanged, owner §6.6)

`R_pair` — certified co-realized ordered physical pairs `(A,B; domain, order, provenance)` with event-stream, common-order and prefix-cofinal repeatability requirements. `R_bd ⊆ R_pair` — bounded at the reduced class. `rho_Q : R_bd → Q^bd`, `x ≡_Q x′ :⟺ rho_Q(x) = rho_Q(x′)`. `N_A(H), N_B(H)` — finite event counts on the admissible common-order prefix poset `P` (N5-C1). Composition candidate: chain `((A,B),(B,C)) ↦ (A,C)` with the exact identity M-1A.

## 2. The interface object

For a pair `x = (A,B) ∈ R_pair`, its **right-end interface** and, for `y = (B,C)`, its **left-end interface** are

```text
𝔍^R(x) := ( B , 𝒫_x , ι^R_x )        𝔍^L(y) := ( B , 𝒫_y , ι^L_y )
```

- **`B`** — the certified event predicate (event type) at that end, in its certified sector.
- **`𝒫_x`** — the directed set of finite admissible common-order prefixes on which `x`'s counts live (N5-C1's `P` for `x`'s sector).
- **`ι^R_x : 𝒫_x → ℕ`, `H ↦ N_B(H)`** — the attachment: how `B`-events accumulate along `x`'s prefixes. Single-stream data.

A composition point additionally carries an **interface transport** — a **M2 preregistered definition**, not a theorem inherited from the owner. The owner's `D_chain` requires "a certified cofinal transport between the two comparison prefix domains" without formalizing it; M2 fixes the formal content as the certified cofinal interface equivalence of §4.

**Outer admissibility (dependent variable, not interface data):**
```text
Π(x,y) :⟺ (A,C) ∈ R_pair
```
i.e. `A` and `C` are co-realized in one admissible sector with a common-order prefix structure and prefix-cofinal repeatability — pre-bounded, as in `D_chain`.

Mapping to the proposed tuple `𝔍_B = (B, 𝒫_B, ι_L, ι_R, 𝒯, Π)`: `B`, `𝒫_B`, `ι_L`, `ι_R`, `𝒯` are the interface; **Π is moved out** (§0).

## 3. `rho_Q`-independence audit (the check requested for this round)

| component | defined from | uses `rho_Q`, `≡_Q`, reduced `p:q`, or `R_bd` membership? | verdict |
|---|---|---|---|
| `B` | certified event predicate, sector | no | pre-`rho_Q` |
| `𝒫_x` | common-order prefix poset (N5-C1) | no | pre-`rho_Q` |
| `ι^R`, `ι^L` | single-stream count `N_B` on prefixes | no — one stream, no ratio | pre-`rho_Q` |
| `𝒯` | cofinal order map; `|ΔN_B| = O(1)` | no — a *single-count* bound, not a `Δ_{p:q}` bound | pre-`rho_Q` |
| `Π` | `(A,C) ∈ R_pair` | no — `R_pair` is defined before boundedness | pre-`rho_Q`; **excluded from `~_I`** |
| `~_I` (§4) | built only from the rows above | no | pre-`rho_Q` |

Two uses of rational data remain, and both are **outside** the interface by design: the domain restriction `D_mid^L, D_M2^L ⊆ R_bd × R_bd` (the operation acts on bounded pairs), and the test hypothesis `x ≡_Q x′` (the quotient being tested). Neither enters the definition of `𝔍` or `~_I`.

**Watch item.** "`|N_B(H) − N_B(𝒯H)| = O(1)`" must stay a single-stream bound. Any strengthening that compares `N_B` against another stream's count reintroduces a ratio and is forbidden.

## 4. Interface equivalence at two preregistered coarseness levels

What "the same `B`" means is the entire question, so both readings are fixed **now**:

**Certified cofinal interface equivalence (M2 definition).** For end interfaces `𝔍 = (B, 𝒫, ι)` and `𝔍′ = (B′, 𝒫′, ι′)`, an *interface isomorphism* is an order isomorphism `φ : 𝒫_{≥H₀} → 𝒫′_{≥H₀′}` between cofinal tails (principal up-sets) such that `sup_H |ι(H) − ι′(φH)| < ∞` — a **single-stream** bound on `N_B` against `N_{B′}`, never against another stream.

**Lemma M2-0 (well-posedness) `[ALG]`.** "There is an interface isomorphism" is an equivalence relation. *Reflexive:* `φ = id`. *Symmetric:* `φ⁻¹` is an interface isomorphism with the same bound, since `|ι′(H′) − ι(φ⁻¹H′)| = |ι(H) − ι′(φH)|` at `H = φ⁻¹H′`. *Transitive:* for `φ : 𝒫 → 𝒫′`, `ψ : 𝒫′ → 𝒫″` with bounds `c₁, c₂`, the image tail of `φ` and the domain tail of `ψ` are principal up-sets of the directed set `𝒫′`, so they contain a common principal up-set `𝒫′_{≥K}` (K an upper bound of the two base points); restricting to `φ⁻¹(𝒫′_{≥K})`, itself a cofinal tail, `ψ∘φ` is an order isomorphism of cofinal tails with bound `c₁ + c₂`. ∎

- **Level a — co-realization identity.** `𝔍 ~_a 𝔍′` iff `B = B′` is the **same certified stream in the same co-realized sector instance** (the same orbit) and the interface isomorphism is the identity on a common tail of the same prefix structure. An equivalence relation (the reflexive case of M2-0).
- **Level b — event-type identity across instances.** `𝔍 ~_b 𝔍′` iff (i) `B` and `B′` have the **same level-b event type** (criterion below) and (ii) an interface isomorphism exists. An equivalence relation by M2-0 and because (i) is an equality of frozen keys.

**Level-b event-type criterion (frozen).** Two endpoint streams have the same level-b event type iff their certified event predicates are **instances of the same preregistered predicate schema/RID** on the **same owner-declared sector class**, with the **same gauge quotient, orientation/event semantics and common-order semantics**; orbit, seed or realization identity may differ. **Forbidden as keys:** `rho_Q`, any rational label or bounded class; any dynamic fate or PASS/FAIL outcome; a bare name or symbol ("same predicate" is not same-named). Consistent with SG-NG-20 (independently certified, co-realized streams under one RTG-native order) and SG-NG-25 (prefixes are directed finite extensions, not metric time).

`~_a ⊆ ~_b`. Both are pre-`rho_Q`.

**Typed equivalence on pairs:** `x ≈_L x′ :⟺ x ≡_Q x′ ∧ 𝔍^L(x) ~_L 𝔍^L(x′) ∧ 𝔍^R(x) ~_L 𝔍^R(x′)`, for `L ∈ {a, b}` — equal label and equivalent interfaces at **both** ends.

## 5. Domains — middle compatibility and the operation domain

```text
D_mid^L := { (x,y) ∈ R_bd × R_bd : 𝔍^R(x) ~_L 𝔍^L(y) }          (middle-interface compatibility)
D_M2^L  := { (x,y) ∈ D_mid^L : Π(x,y) }                          (operation domain)
```
`D_M2^L` preserves the owner's `D_chain` semantics — a shared or transportable middle comparison context **plus** outer `(A,C) ∈ R_pair` admissibility — with the middle context now formalized by §4. Π enters only `D_M2^L`, never the interface or `~_L`.

## 6. Primary test (reformulated, non-vacuous)

**WD-DOM(L):**
```text
(x,y) ∈ D_M2^L ,  x ≈_L x′ ,  y ≈_L y′   ⟹   (x′,y′) ∈ D_M2^L .
```
Membership of `(x′,y′)` is the **conclusion**, not a hypothesis. It splits into two legs:
- **Middle leg — structural.** `𝔍^R(x′) ~_L 𝔍^R(x) ~_L 𝔍^L(y) ~_L 𝔍^L(y′)`, so `(x′,y′) ∈ D_mid^L` by symmetry and transitivity of `~_L` (Lemma M2-0). This is why `~_b` had to be a true equivalence.
- **Outer leg — the non-trivial content.** `Π(x,y) ⟹ Π(x′,y′)`. Π concerns the outer streams `A, C`, which `≈_L` constrains only through their end-interface types, not through their joint co-realization.

**Value side** needs no new test: on admitted chains M-1A fixes the output label, and the output's end interfaces are the inputs' outer interfaces. WD-VAL for `≈_L` therefore follows from WD-DOM(L) plus M-1A.

## 7. Non-triviality — otherwise INCONCLUSIVE, never PASS

A PASS at level `L` counts only if
- **N1** `≈_L` identifies at least one pair of **physically distinct** realizations, so the quotient is coarser than realization identity; and
- **N2** there is at least one `(x,y) ∈ D_M2^L` and some `x′ ≈_L x` with `x′ ≠ x` (or `y′ ≈_L y`, `y′ ≠ y`), so the implication is ever exercised.

If N1 or N2 fails, the verdict at that level is **INCONCLUSIVE (vacuous)**.

## 8. Evidential standards, fixed in advance (outcome-independent)

- **PASS(L):** a proof of WD-DOM(L) for all `≈_L`-related admitted chains — `[ALG]` or `[THM]` under K6 — plus certified instances for N1/N2.
- **FAIL(L):** one certified counterexample: `(x,y) ∈ D_M2^L`, `x′ ≈_L x`, `y′ ≈_L y`, with `(x′,y′) ∉ D_M2^L`. Since the middle leg descends structurally (§6), this is exactly `¬Π(x′,y′)`.
- The asymmetry — proof for PASS, one witness for FAIL — is declared **before** any case is examined.
- **Evidence sources:** existing certified realizations only (N5-PHYS-1 and the continuous dyad; DISC-1/DISC-2 frozen records). M-4 stays HOLD pending the Discrete-owner P2 ruling. Three guards:
  - **G-search — no new search.** No new seed, trajectory, parameter sweep, or event-policy retuning.
  - **G-P2 — quarantine.** P2-exposed DISC-2 witnesses (40/136) cannot alone decide a TDR-G PASS or FAIL; they may be diagnostic. A decisive TDR-G case must come from P2-unexposed certified records, or its independence from any future Discrete-owner antipodal policy must be separately established by theorem or certificate.
  - **G-sufficiency — DISC certification ≠ M2 evidence.** DISC certifies *dynamic admission* of a realization; M2 asks about *composition admissibility*, a different physical predicate. A frozen record counts only if `𝔍`, the middle equivalence, and the co-realization / common-order / prefix-cofinal provenance required for `Π = [(A,C) ∈ R_pair]` can actually be reconstructed from it. If not, the verdict is **INCONCLUSIVE**, never "probable counterexample".
- **Freeze rule:** `𝔍`, the interface isomorphism, `~_a`, `~_b`, the level-b event-type criterion, `D_mid^L`, `D_M2^L`, `≈_L`, N1/N2 and G-search/G-P2/G-sufficiency are frozen with this preregistration. Changing any of them after examining cases requires a new preregistration version, and the earlier verdict is retained. No search over alternative equivalences.

## 9. Preregistered reading matrix

Because `~_a ⊆ ~_b`: a FAIL(a) counterexample is also a FAIL(b) counterexample; and PASS(a) supplies non-trivial level-a instances, which are also level-b instances, so PASS(a) excludes INCONCLUSIVE(b). The **admissible combinations** are exactly:

| level a | level b | reading |
|---|---|---|
| PASS | PASS | an interface-typed quotient exists **across sector instances**; a quotient-level multiplication candidate is legitimate |
| PASS | FAIL | composition is **sector-internal**: labels multiply along co-realized chains inside one sector; the cross-instance label quotient does not carry composition |
| FAIL | FAIL *(forced by `~_a ⊆ ~_b`)* | even a literally shared stream does not make outer admissibility descend; composition is realization-specific, as DISC fate was |
| INCONCLUSIVE | PASS | no physically distinct level-a representatives exist, but a cross-instance typed quotient does |
| INCONCLUSIVE | FAIL | no non-trivial level-a instance; across instances, outer admissibility does not descend |
| INCONCLUSIVE | INCONCLUSIVE | neither level supplies an instance; report as such, no upgrade |

Excluded as logically impossible: FAIL(a) with PASS or INCONCLUSIVE(b); PASS(a) with INCONCLUSIVE(b). A report outside this table indicates an error in the analysis. Every admissible row is informative; none is the favoured outcome.

## 10. Guards

- **WD-REP:** `pu/qv` defines neither the interface nor `D_mid^L`, `D_M2^L`, nor `Π`. It may appear only as the label of an admitted output, via M-1A.
- **No law inflation:** associativity-transfer, identities, inverses, commutativity and C7C-A addition are **not** part of this PASS criterion; they remain separate downstream obligations.
- **K1–K6** (v1.20.6) govern the grading of any resulting claim.
- **Hard anti-circularity:** no `rho_Q`, `≡_Q`, reduced `p:q`, `Δ_{p:q}`, or quantity derived from them in `𝔍`, the interface isomorphism, `~_a`, `~_b`, the event-type criterion, or `D_mid^L`; Π only in `D_M2^L`.

## 11. Decisions requested (v1) — ruled; kept for the record

1. **Π out of the interface**, as the dependent variable — the repair for the vacuity in §0.
2. **Two coarseness levels** (a, b), both preregistered, with the reading matrix as written.
3. **Level b needs an operational criterion** for "same event type across sector instances". I propose: the same predicate definition evaluated on the same sector class. This must be fixed before any case is examined.
4. **Evidence sources:** using existing certified DISC witnesses as counterexample candidates while M-4 is HOLD. This is analysis of certified data, not a new search, but it touches the TDR-G route that P2 affects.

## 12. v2 status

All four v1 decisions ruled GO with repairs; the repairs are §2 (transport as M2 definition), §4 (interface isomorphism, Lemma M2-0, `~_a`/`~_b` as true equivalences, frozen level-b event-type criterion), §5 (`D_mid` + `D_M2`), §6 (membership as conclusion; middle leg structural, outer leg non-trivial), §8 (G-search, G-P2, G-sufficiency), §9 (forced `FAIL(a) ⇒ FAIL(b)` and the full table of admissible combinations). **Ready for freeze review.** No case has been examined.
