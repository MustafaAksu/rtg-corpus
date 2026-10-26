> **[SUPERSEDED 2026-09-03] Retained for lineage only. Section 2 let R_bd membership of Sx be concluded from carrier-preservation alone, before section 3 sign identity actually decided boundedness. Canonical: NG_C7C0_RECIPROCAL_CERT_v2.md. Do not cite as current.**

# C7C-0 — Reciprocal Theorem Closure Certificate

**Certificate ID:** `NG_C7C0_RECIPROCAL_CERT_v1` · **RID:** `NUMGEN-C7C-0`
**Base:** `RTG_NUMBER_GENESIS_DSN_v1.17` (sha256 `46ca8283…4e647a`), `NG_C7C_WD_C7C0_DESIGN_v1.md` (sha256 `2ca016d4…33d782`)
**Date:** 2026-09-03 · **Auditor:** Claude
**Status:** `[RESULT] [from: ALG]` closure artifact, PI ruling of 2026-09-03 incorporated. No numerical certificate is required; the SymPy identities in the design note are regression checks on elementary algebra, not evidence.

---

## 1. Carrier and equivalence

```
R_bd = { certified bounded physical realizations x = (A, B; domain, order, provenance) }
ρ_Q : R_bd → Q_RTG^bd
x ≡_Q x'  :⟺  ρ_Q(x) = ρ_Q(x')          (representation equivalence, not physical identity)
```

## 2. `S` — definition and carrier preservation

`S(A, B) := (B, A)`.

**`[COR]` carrier-preservation stated explicitly, per ruling.** For `x = (A, B) ∈ R_bd`: swapping the ordered comparison does not alter the two certified event streams, their physical domain, their co-realization, their common-order prefix sector, or their prefix-cofinal repeatability (SG-NG-25). Only comparison orientation changes. Hence

```
(A, B) ∈ R_bd  ⟹  (B, A) ∈ R_bd
```

**before** the defect calculation is invoked — this is `S : R_bd → R_bd`, not merely a formula applied after the fact.

## 3. Sign identity and boundedness preservation

For `x` with reduced class `p:q`, `Δ^x_{p:q}(H) = q N_A(H) − p N_B(H) = O(1)`. Exactly:

```
Δ^{Sx}_{q:p}(H) = p N_B(H) − q N_A(H) = −Δ^x_{p:q}(H).
```

Since the two defects differ only by sign, `Sx ∈ R_bd` follows directly from `x ∈ R_bd`. This discharges **WD-CLOSE**.

`S² = id`: `S(S(A,B)) = S(B,A) = (A,B)`.

## 4. Uniqueness and the label

By C7A (unique reduced positive-rational label on every certified bounded pair), `ρ_Q(Sx)` is the unique reduced class of `q:p`, i.e. `ρ_Q(x)⁻¹`.

## 5. WD ledger

| obligation | status | note |
|---|---|---|
| WD-PHYS | discharged | `S` is the stream-order reversal already implicit in the ordered-pair architecture; no new mechanism, no inspection of `p,q` |
| WD-CLOSE | discharged | §3 |
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
