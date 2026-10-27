# C7C-WD / C7C-0 — Well-Definedness Framework and the Reciprocal Theorem

**Memo ID:** `NG_C7C_WD_C7C0_DESIGN_v1` · **Date:** 2026-09-03 · **Auditor:** Claude
**Base:** `RTG_NUMBER_GENESIS_DSN_v1.17` (sha256 `46ca8283…4e647a`, frozen)
**Status:** design note. Algebra verified symbolically (`sympy`, two identities, exact). **No trajectory or campaign data used.**

---

## 1. Why the frozen C7C-WD wording is one condition short

v1.17 asks whether a candidate `Φ` satisfies `ρ_Q(Φ(x,y)) = ρ_Q(Φ(x',y'))` whenever `x ≡_Q x'`, `y ≡_Q y'`, and all four compositions are admissible. That is **value congruence**, and it is necessary. But it silently assumes admissibility is already class-invariant — it says nothing about whether `(x,y) ∈ D_Φ ⟺ (x',y') ∈ D_Φ`. Without that, "whenever admissible" can be vacuously satisfied by an operation admissible for one representative pair and forbidden for every other, and the record would show a passing value-congruence check for an object that isn't a partial operation on classes at all.

This isn't a hypothetical gap. The programme already has two disjoint realization families sharing a label: `1` has a continuous-dyad bounded realization via N5-PHYS-1 and separate TDR-G dynamic realizations via DISC-2. Equal `ρ_Q` already spans physically different families under different branch firewalls. A branch-native `Φ` could be admissible for one `x` with `ρ_Q(x) = 1` and inadmissible for another with the same label. Domain congruence is the condition that rules this out, and it is a genuine RTG-native obligation, not mathematical bookkeeping.

## 2. Carrier and equivalence

```
R_bd = { certified bounded physical realizations x = (A, B; domain, order, provenance) }
ρ_Q : R_bd → Q_RTG^bd

x ≡_Q x'  :⟺  ρ_Q(x) = ρ_Q(x')
```

`≡_Q` is representation equivalence, **not** physical identity — this is the same directionality guard already in the owner text: equal labels do not identify realizations.

**Typed carrier.** No assumption that the global quotient `R_bd / ≡_Q` is uniformly composable. A candidate operation carries an explicit type signature

```
Φ_{τ1,τ2}^{τ3} : R_{τ1} × R_{τ2} ⇀ R_{τ3}
```

where `τ` records whatever physical interface is load-bearing — branch, common-order architecture, event type, domain, or comparison-interface. If arithmetic later proves coherent across different `τ`'s, that is a **transport/coherence theorem**, stated and proved separately, never assumed by writing one untyped `Φ`.

## 3. The five obligations

1. **WD-PHYS.** `Φ` is constructed from certified relational objects and admissible interfaces. It may not inspect `p, q, r, s` and manufacture the answer from the labels.
2. **WD-CLOSE.** Every admissible output is again a certified bounded realization in `R_bd`, not a bare rational number produced in the metalanguage.
3. **WD-DOM.** `(x,y) ∈ D_Φ ⟺ (x',y') ∈ D_Φ` whenever `x ≡_Q x'`, `y ≡_Q y'` — or `Φ` is explicitly typed/restricted to a class-saturated sector where this holds.
4. **WD-VAL.** `Φ(x,y) ≡_Q Φ(x',y')` whenever both sides are admissible (the frozen v1.17 condition, retained, now explicitly named as one of two).
5. **WD-DESCENT.** Only after WD-DOM and WD-VAL: `[x]_Q ⊙ [y]_Q := [Φ(x,y)]_Q` is a well-defined partial operation on classes. The descent step itself is standard quotient algebra; the RTG-native content is entirely in proving 3 and 4.

**WD-REP**, arithmetic compatibility, comes only after WD-DESCENT: if `ρ_Q(Φ(x,y)) = F(ρ_Q(x), ρ_Q(y))` for `F(r,s) = rs` or `r+s`, that is a **derived representation theorem**. `F` may not define `Φ`. This is the same discipline as C7A, where the rational label was the output of a certified relation, never its premise.

## 4. C7C-0 — reciprocal

**Construction (WD-PHYS).** For a certified bounded ordered pair `x = (A, B)`, define the orientation-swap `S(x) = (B, A)` — the stream-order reversal already implicit in the ordered-pair architecture. No new mechanism is introduced.

**Claim.** If `x` carries reduced class `p:q`, so `Δ^x_{p:q}(H) = q N_A(H) − p N_B(H) = O(1)`, then `S(x)` is bounded at `q:p` with `ρ_Q(S(x)) = ρ_Q(x)⁻¹`.

**Proof.** `Δ^{Sx}_{q:p}(H) = p N_B(H) − q N_A(H) = −Δ^x_{p:q}(H)`, verified symbolically as an exact identity, not an approximation. Boundedness is preserved because the two defects differ only by sign, so `Sx ∈ R_bd` follows directly from `x ∈ R_bd` — this discharges **WD-CLOSE** for this specific `Φ = S`. `S² = id` was also verified directly (swap-of-swap returns the original pair).

**WD-DOM for `S` is trivial rather than merely satisfied.** `S` is unary, so there is no second input to desynchronize; `D_S = R_bd` and the domain-congruence question `(x) ∈ D_S ⟺ (x') ∈ D_S` collapses to `R_bd ⟺ R_bd`. This is exactly why `S` was identified as a clean first test: it sidesteps the load-bearing half of WD entirely and isolates WD-VAL, which the sign identity discharges directly.

**Result.** `r ∈ Q_RTG^bd ⟹ r⁻¹ ∈ Q_RTG^bd`. A nontrivial arithmetic-compatibility theorem, theorem-ready at the algebraic level.

## 5. What is explicitly *not* claimed

**`r ∈ Q^dyn ⟹ r⁻¹ ∈ Q^dyn` is withheld.** The same-realization stability-and-contingency gate is a predicate on the *ordered* pair `(A, B)` under a declared deformation family; nothing here shows that predicate is invariant under exchanging the roles of `A` and `B`. That would be a separate theorem, and the current ten dynamic labels contain no reciprocal pairs — smuggling the stronger claim through C7C-0 would produce an unfounded extension of the ratified spectrum.

**No multiplication or addition construction is attempted here.** WD-DOM is the load-bearing obligation for any *binary* `Φ`, and `S` was chosen precisely because it doesn't need to discharge it. C7C-M inherits the full five-obligation list with a genuine domain-congruence proof burden.

## 6. Scientific order, as ruled

```
C7C-WD carrier/descent definitions  →  C7C-0 reciprocal  →  C7C-M design (not yet attempted)
```

C7C-0 is ready for certification as an `[ALG]` theorem on the existing symbolic argument; no campaign or trajectory data is required to close it. C7C-M should not begin until a candidate owner-native binary composition is proposed with its domain-congruence obligation stated explicitly, per §3.

## 7. Guards

Nothing here touches `Q^dyn`, C7B breadth, or any ratified label. `S` acts within the certified bounded-pair architecture only. The reciprocal theorem, if certified, extends `Q_RTG^bd` closure properties; it does not touch `Q_RTG^dyn`, which remains exactly `{1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4} ⊆ Q^dyn` per v1.17.
