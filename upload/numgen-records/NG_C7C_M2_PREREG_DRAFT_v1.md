> **[SUPERSEDED 2026-09-29] by NG_C7C_M2_PREREG_DRAFT_v2.md (co-owner audit repairs). Content without this banner hashes to e654abd3a184f3fc47d6987803748ae42cc435073fcb45e1d3f199b51b74794b.**

# C7C-M2 — Interface Object and Saturated WD-DOM · Preregistration DRAFT v1

**Doc ID:** `NG_C7C_M2_PREREG_DRAFT_v1` · **Date:** 2026-09-29 · **Base:** frozen v1.20.6 (`2a51c4b1…48c5`)
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

A composition point additionally carries a **transport** `𝒯 : 𝒫_x → 𝒫_y`, cofinal and order-preserving, with `|N_B(H) − N_B(𝒯H)| = O(1)` — the formal content of the owner's "certified cofinal transport between the two comparison prefix domains" (`D_chain`).

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

Two uses of rational data remain, and both are **outside** the interface by design: the domain restriction `D_I ⊆ R_bd × R_bd` (the operation acts on bounded pairs), and the test hypothesis `x ≡_Q x′` (the quotient being tested). Neither enters the definition of `𝔍` or `~_I`.

**Watch item.** "`|N_B(H) − N_B(𝒯H)| = O(1)`" must stay a single-stream bound. Any strengthening that compares `N_B` against another stream's count reintroduces a ratio and is forbidden.

## 4. Interface equivalence at two preregistered coarseness levels

What "the same `B`" means is the entire question, so both readings are fixed **now**:

- **Level a — co-realization identity.** `𝔍 ~_a 𝔍′` iff `B = B′` is the **same certified stream in the same co-realized sector instance** (the same orbit), and `𝒯` is an order isomorphism of the same prefix structure.
- **Level b — event-type identity across instances.** `𝔍 ~_b 𝔍′` iff `B` and `B′` are the **same certified event type** (same predicate, same sector class) possibly on **different** sector instances, and a transport `𝒯` exists as in §2.

`~_a ⊆ ~_b`. Both are pre-`rho_Q`.

**Typed equivalence on pairs:** `x ≈_L x′ :⟺ x ≡_Q x′ ∧ 𝔍^L(x) ~_L 𝔍^L(x′) ∧ 𝔍^R(x) ~_L 𝔍^R(x′)`, for `L ∈ {a, b}` — equal label and equivalent interfaces at **both** ends.

## 5. Typed admissibility domain

```text
D_I^L := { (x,y) ∈ R_bd × R_bd : 𝔍^R(x) ~_L 𝔍^L(y) } .
```
Defined by interface compatibility alone. `Π` does **not** appear in `D_I`.

## 6. Primary test (reformulated, non-vacuous)

**WD-DOM(L):** for all `(x,y) ∈ D_I^L` with `Π(x,y)`, and all `x′ ≈_L x`, `y′ ≈_L y` with `(x′,y′) ∈ D_I^L`:
```text
Π(x,y)  ⟹  Π(x′,y′) .
```
Outer admissibility must descend through label-plus-interface equivalence. It is **not** implied by construction, because Π concerns the *outer* streams `A, C`, which `≈_L` constrains only through their interface types, not through joint co-realization.

**Value side** needs no new test: on admitted chains M-1A fixes the output label, and the output's end interfaces are the inputs' outer interfaces. WD-VAL for `≈_L` therefore follows from WD-DOM(L) plus M-1A.

## 7. Non-triviality — otherwise INCONCLUSIVE, never PASS

A PASS at level `L` counts only if
- **N1** `≈_L` identifies at least one pair of **physically distinct** realizations, so the quotient is coarser than realization identity; and
- **N2** there is at least one admitted chain `(x,y) ∈ D_I^L` with `Π(x,y)` and some `x′ ≈_L x`, `x′ ≠ x`, so the implication is ever exercised.

If N1 or N2 fails, the verdict at that level is **INCONCLUSIVE (vacuous)**.

## 8. Evidential standards, fixed in advance (outcome-independent)

- **PASS(L):** a proof of WD-DOM(L) for all `≈_L`-related admitted chains — `[ALG]` or `[THM]` under K6 — plus certified instances for N1/N2.
- **FAIL(L):** one certified counterexample: `(x,y)` admitted with `Π`, `x′ ≈_L x`, `(x′,y) ∈ D_I^L`, `¬Π(x′,y)`.
- The asymmetry — proof for PASS, one witness for FAIL — is declared **before** any case is examined.
- **Evidence sources:** existing certified realizations only (N5-PHYS-1 and the continuous dyad; DISC-1/DISC-2 witnesses). No new realization search: M-4 stays HOLD pending the Discrete-owner P2 ruling.
- **Freeze rule:** `𝔍`, `~_a`, `~_b`, `D_I`, `≈_L`, N1/N2 are frozen with this preregistration. Changing any of them after examining cases requires a new preregistration version, and the earlier verdict is retained. No search over alternative equivalences.

## 9. Preregistered reading matrix

| level a | level b | reading |
|---|---|---|
| PASS | PASS | an interface-typed quotient exists **across sector instances**; a quotient-level multiplication candidate is legitimate |
| PASS | FAIL | composition is **sector-internal**: labels multiply along co-realized chains inside one sector, and the cross-instance label quotient does not carry composition |
| FAIL | — | even a literally shared stream does not make outer admissibility descend; composition is realization-specific, as DISC fate was |
| INCONCLUSIVE at either level | | the level supplies no instance; report it and do not upgrade it |

Every row is informative; none is the favoured outcome.

## 10. Guards

- **WD-REP:** `pu/qv` defines neither the interface nor `D_I` nor `Π`. It may appear only as the label of an admitted output, via M-1A.
- **No law inflation:** associativity-transfer, identities, inverses, commutativity and C7C-A addition are **not** part of this PASS criterion; they remain separate downstream obligations.
- **K1–K6** (v1.20.6) govern the grading of any resulting claim.
- **Hard anti-circularity:** no `rho_Q`, `≡_Q`, reduced `p:q`, `Δ_{p:q}`, or quantity derived from them in `𝔍`, `~_a`, `~_b` or `D_I`.

## 11. Decisions requested

1. **Π out of the interface**, as the dependent variable — the repair for the vacuity in §0.
2. **Two coarseness levels** (a, b), both preregistered, with the reading matrix as written.
3. **Level b needs an operational criterion** for "same event type across sector instances". I propose: the same predicate definition evaluated on the same sector class. This must be fixed before any case is examined.
4. **Evidence sources:** using existing certified DISC witnesses as counterexample candidates while M-4 is HOLD. This is analysis of certified data, not a new search, but it touches the TDR-G route that P2 affects.
