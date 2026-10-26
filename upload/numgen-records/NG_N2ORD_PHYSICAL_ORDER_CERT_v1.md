# N-2-ORD Certificate — Physical Order Representation

**Certificate ID:** `NG_N2ORD_PHYSICAL_ORDER_CERT_v1`
**RID:** `NUMGEN-OPEN-N2ORD` · **Target document:** `RTG_NUMBER_GENESIS_DSN_v1.6`
**Date:** 2026-08-28 · **Author/auditor:** Claude (RTG mathematical auditor / DSN editor)
**Status:** `[RESULT][from: ALG]` (ORD-1, ORD-2 preservation, ORD-3, T4) + `[RESULT][from: ALG/NUM]` (ORD-4) with exit-code-gated certificate `ng_n2ord_order_cert_v1.py` (14 assertion families, all pass, exit 0)
**Scope:** local primitive-dyad tube `U_T` with the selected generator `T`; inherits SG-PROG-2 / OPEN-P0
**Ownership:** Number Genesis (the primitive map and `Q_true` remain Dyadic-owned imports)

---

## 1. Formulation adopted (PI ruling, 2026-08-28)

Order is **reachability-first**: for admissible `y, z`,

```
y ⪯_T z   ⟺   ∃ K ∈ M_T with z = K(y).
```

`Q_true` is demoted from definition to **certified observable witness**. This is the correct architecture and materially stronger than a `Q_true`-defined order: the order is then native to the certified composition structure (SG-NG-22 compliant — the physical relation is prior to any numerical label), and it needs no external clock.

## 2. Premises

**P1 (imported).** Free monogenic tube: `T(U_T) ⊆ U_T`; `T^r x = T^s x ⟹ r = s`. [`NG_N1_UNIFIED_T_ALIGNMENT_CERT_v1`]
**P2 (imported).** L1 strict contraction: `Q_true(Fx) < Q_true(x)` for `F = T^6` on the punctured tube. [`NG_L1_PRIMITIVE_CONTRACTION_CERT_v1`]
**P3 (NEW — flagged, not silently assumed).** Injectivity of `T` on `U_T`. **This is not implied by P1**: non-collision constrains each orbit separately and says nothing about two distinct points sharing an image. Owner-source support: `det J = 1 + (e^ρ − 1)cos η → 1` at `P₁`, and the critical curve `C₀` requires `ρ ≥ ln 2`, so `det J` is bounded away from zero on a sufficiently small tube (audited: `min|det J| ≈ 0.9812` over all sampled orbit points). Only two items use P3 — the ORD-1 cross-orbit refinement and the ORD-2 **reflection** direction — and both are tagged accordingly.

## 3. Theorems

**ORD-1 — Reachability order.** `⪯_T` is reflexive (`id`), transitive (composition), and antisymmetric on all of `U_T`; it is **total on each primitive orbit**. Antisymmetry is exactly P1: `z = T^k y` and `y = T^ℓ z` give `T^{k+ℓ} y = y`, so `k + ℓ = 0`, hence `k = ℓ = 0`. *Refinement (audit contribution):* globally `⪯_T` is a **partial** order, total on orbits — the DSN should state both. Under P3, two orbits either are disjoint or one contains a tail of the other (`T^a x = T^b y`, `a ≥ b`, injectivity ⟹ `y = T^{a−b} x`), so comparability across orbits holds **exactly when the orbits merge**. This sharpens NC-3 from "no cross-orbit order" to a precise merge criterion.

**ORD-2 — Shift covariance.** `y ≺_T z ⟹ T^r y ≺_T T^r z`. Preservation uses P1 only (strictness from non-collision at the shifted point). *Audit contribution:* the **converse** (`T^r y ≺ T^r z ⟹ y ≺ z`) is a distinct claim requiring P3; the certificate separates the two directions, so the DSN must not state ORD-2 as an equivalence without the injectivity tag.

**ORD-3 — Ordered signed-history group.** With `P := ι(M_T) ⊆ G_T`: `P + P ⊆ P`, `P ∩ (−P) = {0}`, `G_T = P ∪ (−P)`; hence `a ≤_G b ⟺ b − a ∈ P` is a translation-invariant total order on the infinite cyclic group. Standard ordered-group algebra once N-1/N-2 are certified.

**T4 — Physical sign realization (the RTG-specific content).** For `[A,B] ∈ G_T` and any admissible `x`, exactly one of `A(x) = B(x)`, `B(x) ≺_T A(x)`, `A(x) ≺_T B(x)` holds, corresponding to `[A,B] = 0`, `> 0`, `< 0`. **Well-definedness certified:** the endpoint verdict is constant on each N-2 equivalence class (if `(A,B) ~ (C,D)` then `m + q = n + p`, so `m − n = p − q` and the verdict agrees) and is independent of the admissible base point `x`, since `A(x)` and `B(x)` always lie on the common orbit `O_x`. Hence the sign of a signed history is not merely the metalanguage integer `m − n`: it is the **orientation of forward reachability between the two realized endpoints**.

**ORD-4 — `Q_true` as order witness.** For every residue `j = 0..5`, `Q_true` is strictly decreasing along the `F`-chain `{T^j x, T^{6+j} x, …}`: `r < s ⟹ Q_true(T^{6s+j} x) < Q_true(T^{6r+j} x)`. Verified on the exact primitive map for all six residues and five seeds (dps=60). *Audit contribution:* strict antitonicity makes `Q_true` **order-reflecting** within a residue class, i.e. index order ⟺ reversed `Q_true` order — a **complete** witness of the reachability order restricted to that chain, not merely a consequence of it. Using all six residues rather than only `j = 0` is the PI's improvement and is confirmed.

## 4. Non-claims — demonstrated, not merely asserted

**NC-1 — No external physical time.** Structural: `⪯_T` is defined purely by existence of a connecting history in `M_T`; no clock, parameter, or index enters the definition (integers appear only in the metalanguage audit, per SG-NG-1).
**NC-2 — No per-primitive-step `Q_true` monotonicity.** Demonstrated on the real map: across the sampled orbits, single primitive steps split **192 decreases vs 168 non-decreases**. Moreover the specific tempting statement `Q_true(T³x) < Q_true(T²x)` **fails** for at least one admissible seed. The cross-residue guard is therefore *necessary*, not merely cautious — a counterexample now backs it.
**NC-3 — No total order between non-merging orbits.** Structural, sharpened by the P3 merge criterion in ORD-1.

## 5. Guards

1. `Q_true` is a witness, never the definition of order (ORD-4 may not be inverted into a definition).
2. No comparison across residues `j` is certified; NC-2b is the standing counterexample.
3. P3 must be discharged by its own certificate before the ORD-1 cross-orbit refinement or the ORD-2 reflection direction is promoted beyond `[NUM-audited]`.
4. Scope is the local tube and the selected generator; OPEN-P0 ceiling retained.
5. The order is on histories/states of one certified stream; it does **not** supply a second recurrence and cannot touch N-5A/SG-NG-20.
6. `Q_true` ownership remains Dyadic; this certificate imports the observable and adds no new dyadic claim.

## 6. Verdict

**N-2-ORD CLOSED** at `[RESULT][from: ALG]` (ORD-1/ORD-2-preservation/ORD-3/T4) and `[RESULT][from: ALG/NUM]` (ORD-4), with P3-dependent items explicitly tagged. The chain **ℕ-like repetition → ℤ-like signed comparison → physically realized order** is now closed on one local primitive-dyad object. Queue advances to the N-4 + N-5A frontier; the character of the programme changes there from compact algebraic closure to genuine construction.
