# C7C-0 — Reciprocal Theorem Closure Certificate

**Certificate ID:** `NG_C7C0_RECIPROCAL_CERT_v2` · supersedes `_v1` · **RID:** `NUMGEN-C7C-0`
**Base:** `RTG_NUMBER_GENESIS_DSN_v1.17` (sha256 `46ca8283…4e647a`), `NG_C7C_WD_C7C0_DESIGN_v1.md` (sha256 `2ca016d4…33d782`)
**Date:** 2026-09-03 · **Auditor:** Claude
**Status:** `[RESULT] [from: ALG]` closure artifact, PI ruling of 2026-09-03 incorporated (two rounds). No numerical certificate is required; the SymPy identities in the design note are regression checks on elementary algebra, not evidence.

`[COR]` v1 of this certificate let `R_bd` membership of `Sx` be concluded from carrier-preservation alone in §2, before §3's sign identity had actually decided boundedness — the same governance species (a claim outrunning the expression that decides it) this programme has repeatedly caught elsewhere. Repaired below by introducing the pre-bounded carrier `R_pair` and moving the `R_bd`-membership conclusion to §3, where the sign identity is proved.

---

## 1. Carriers and equivalence

```
R_pair := { certified co-realized ordered physical pairs (A,B; domain, order, provenance)
            satisfying the event-stream, common-order, and prefix-cofinal
            repeatability requirements }

R_bd ⊆ R_pair := { x ∈ R_pair : x is boundedly commensurate at its reduced class }

ρ_Q : R_bd → Q_RTG^bd
x ≡_Q x'  :⟺  ρ_Q(x) = ρ_Q(x')          (representation equivalence, not physical identity)
```

`R_pair` is the carrier of physically admissible ordered pairs before boundedness is checked; `R_bd` is its subset that is actually bounded. Separating them is what closes the circularity below.

## 2. `S` — definition and physical admissibility (WD-PHYS)

`S(A, B) := (B, A)`.

For `x = (A, B) ∈ R_bd ⊆ R_pair`: swapping the ordered comparison does not alter the two certified event streams, their physical domain, their co-realization, their common-order prefix sector, their prefix-cofinal repeatability (SG-NG-25), or their provenance. Only comparison orientation changes. Therefore

```
x ∈ R_bd  ⟹  Sx ∈ R_pair.
```

Equivalently, `S` is physically admissible on every input in `R_bd`. **No boundedness claim for `Sx` is made at this step** — `R_pair` membership is a weaker, orientation-blind statement, and boundedness is exactly what §3 must still establish independently.

## 3. Sign identity and boundedness preservation (WD-CLOSE)

For `x` with reduced class `p:q`, `Δ^x_{p:q}(H) = q N_A(H) − p N_B(H) = O(1)`. Exactly:

```
Δ^{Sx}_{q:p}(H) = p N_B(H) − q N_A(H) = −Δ^x_{p:q}(H).
```

Since the two defects differ only by sign, and `Sx ∈ R_pair` from §2, boundedness of `Δ^{Sx}_{q:p}` follows and **only here** may we conclude

```
Sx ∈ R_bd,     hence     S : R_bd → R_bd.
```

`S² = id`: `S(S(A,B)) = S(B,A) = (A,B)`.

## 4. Uniqueness and the label

By C7A (unique reduced positive-rational label on every certified bounded pair), `ρ_Q(Sx)` is the unique reduced class of `q:p`, i.e. `ρ_Q(x)⁻¹`.

## 5. WD ledger

| obligation | status | note |
|---|---|---|
| WD-PHYS | discharged | orientation swap preserves the certified physical-pair interface; `Sx ∈ R_pair` (§2), **before** boundedness is checked |
| WD-CLOSE | discharged | the sign identity (§3) is what actually places `Sx` in `R_bd`; not smuggled in via §2 |
| WD-DOM | **trivial** | `S` is unary: `D_S = R_bd`, so `(x) ∈ D_S ⟺ (x') ∈ D_S` collapses to `R_bd ⟺ R_bd`. This is why `S` was chosen as the first test — it isolates WD-VAL and does not test the load-bearing binary obligation |
| WD-VAL | discharged | §3–4; `x ≡_Q x' ⟹ Sx ≡_Q Sx'` follows from the sign identity applied to each representative |
| WD-DESCENT | discharged | given DOM (trivial) and VAL, `[x]_Q ↦ [Sx]_Q` is well defined |

## 6. Theorem

**C7C-0 Reciprocal Theorem.** Let `x = (A,B)` be any certified bounded realization with `ρ_Q(x) = p/q`. Define `S(A,B) = (B,A)`. Then

```
S : R_bd → R_bd,     S² = id,     ρ_Q(Sx) = q/p = ρ_Q(x)⁻¹.
```

`S` respects `≡_Q` and descends to an involution

```
S̄ : R_bd/≡_Q → R_bd/≡_Q,     [x]_Q ↦ [Sx]_Q,     represented numerically by r ↦ r⁻¹.
```

Therefore

```
r ∈ Q_RTG^bd  ⟹  r⁻¹ ∈ Q_RTG^bd.
```

`[RESULT] [from: ALG]`.

## 7. Non-claims

**`Q^dyn` is not closed under reciprocal by this certificate.**

```
r ∈ Q_RTG^dyn  ⇏(currently)  r⁻¹ ∈ Q_RTG^dyn.
```

This would require a separate theorem establishing equivariance of the same-realization stability-and-contingency gate under `A ↔ B` — a predicate on the *ordered* pair under a declared deformation family, which `S` does not address. Not attempted here.

**`[COR]`, per ruling.** The design note's claim "the current ten dynamic labels contain no reciprocal pairs" is corrected: `1⁻¹ = 1`, so `1` is self-reciprocal. The accurate statement is: **apart from the self-reciprocal label `1`, the currently established dynamic spectrum `{3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4}` contains no distinct reciprocal partners.**

## 8. Owner-facing statement

> `[RESULT] [from: ALG]` **C7C-0 CLOSED** — orientation swap on certified bounded pairs descends to a representative-independent involution on bounded commensurability classes, represented by reciprocal; hence `Q_RTG^bd` is closed under `r ↦ r⁻¹`. No `Q_RTG^dyn` reciprocal-closure theorem is claimed.

## 9. Guards

Nothing here touches `Q_RTG^dyn`, C7B breadth, or any ratified label. `S` acts within the certified bounded-pair architecture only. `C7C-M` is not opened by this certificate and should not begin until this closure is frozen, per ruling.
