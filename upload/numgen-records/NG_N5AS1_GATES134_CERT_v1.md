# N-5A-S1 Gates 1 / 3 / 4 Certificate — Event Predicate, Co-realization, Interleaving

**Certificate ID:** `NG_N5AS1_GATES134_CERT_v1` · **RID:** `NUMGEN-OPEN-N5AS1` (gates 1, 3, 4)
**Canonical base:** `RTG_NUMBER_GENESIS_DSN_v1.8.1` (sha256 `10225d7a…83bd6`, verified)
**Date:** 2026-08-28 · **Author/auditor:** Claude
**Artifacts:** `ng_n5as1_gates134_cert_v1.py` / `.log` (13 assertion families, all pass, exit 0)
**Verdict:** **Gates 1, 3, 4 CLOSED** for the canonical section on the declared domain. Gate 2 and the ALG form of gate 5 remain the N-5A-S1-INF target.

---

## 1. The central finding — the canonical section is not an arbitrary choice

`[RESULT] [from: ALG]` **Canonical section identity.** For `Θ = atan2(√3 η_wrap, 2ρ − η_wrap)`,

```
Θ = 0   ⟺   η_wrap = 0  and  ρ > 0.
```

Immediate from `atan2`: vanishing requires `√3 η_wrap = 0` and `2ρ − η_wrap > 0`. So the section originally chosen is **exactly relational-phase coincidence with positive `ρ`** — a physically meaningful relational condition, not a coordinate level set. This matters because gate 1's real risk was that `Σ` is an observer-declared artifact; for `Θ₀ = 0` it is not. (`Θ₀ = π` is the `ρ < 0` branch of the same condition; the other ten sections swept earlier, e.g. `Θ₀ = π/3 ⟺ η_wrap = ρ`, are coordinate sections admissible as robustness checks only, and I recommend the DSN say so explicitly.)

**Consequence — no lift is involved.** Because the event is a sign change of `η_wrap` with `ρ > 0`, it is a **present-state relational condition**. A lift-free detector reproduces the lift-based event sequence exactly (6666 events over 40 000 steps, first at 6, last at 39 997, including the documented slip at 33229). This discharges what would otherwise have been the strongest objection to gate 1: SG-NG-16 and N-3A forbid using a lifted winding label as a certified physical counter, and `Θ`-lap counting could have looked like exactly that. It is not `η`-winding, and the certificate demonstrates the equivalence rather than asserting it.

## 2. Gate 1 — event predicate admissibility: CLOSED

| Item | Result |
|---|---|
| Section is a relational condition (identity above) | `[ALG]` |
| Lift-free detectability | `[RESULT][from: ALG/NUM]` — detectors agree exactly |
| Gauge invariance: predicate unchanged under `η → η + 2πk`, depends only on gauge-reduced state | `[ALG]` (SG-NG-13 at this scope) |
| Well-definedness: `Q_true > 0` throughout (min 5.04×10⁻⁵), `atan2` nonsingular; matches N-1 punctured-sector scope | `[ALG/NUM]` |
| Orientation retention: 6666 positive vs **0** negative crossings of the same oriented section | `[NUM on the audited domain]` — see caveat |
| SG-NG-11 discharge: declared counting predicate `P_B` = "oriented crossing of relational-phase coincidence with `ρ > 0`"; all crossing neighbourhoods pairwise distinct, so the coarser counting predicate is declared rather than silently assumed | `[ALG]` |

**Caveat (flagged, not buried).** The absence of negative crossings is certified on the audited domain only. The ALG mechanism is that the `P₁` linearization has eigenvalues `exp(±iπ/3)`, so the rotation sense through the section is fixed for small `Q`; turning that into a domain-wide statement is a small lemma, not yet written. Tagged `[NUM]` accordingly.

## 3. Gate 3 — co-realization: CLOSED

Every B-event is anchored to a primitive `T`-transition of the **same orbit** on the **same declared domain** — there is no second domain, no separate parameterization, and no external construction. The anchor map is injective and strictly increasing. Both streams run together across the sampled window (40 000 A-events, 6666 B-events) with neither terminating first. *Scope note:* indefinite extensibility is gate 2, not gate 3; what is certified here is co-realization on one declared domain.

## 4. Gate 4 — common interleaving order: CLOSED

Successive B-anchors are related by forward reachability (`b = T^k a`, `k ≥ 1`) and never in reverse, so the interleaving is fixed by `⪯_T` alone — the N-2-ORD order, with no clock, step-parameter, or frequency used. The interleaving word is the sequence of **reachability distances** (counts of intervening A-events), an RTG-native quantity; observed alphabet `{6, 7}` over 6665 letters, and it contains the documented slip at step 33229, so this is the same object the gate-5 evidence measured. The order induced on B-events by `⪯_T` coincides with their realization order.

This is the first place N-2-ORD does load-bearing work rather than being a completed formality: SG-NG-20 requires a declared RTG-native order relation for co-realization, and `⪯_T` supplies it.

## 5. State of N-5A-S1 after this certificate

| Gate | Status |
|---|---|
| 1 — relational/gauge-admissible event predicate | **CLOSED** (`[ALG]`, one `[NUM]` caveat on orientation) |
| 2 — repeatability / infinitely many crossings | **OPEN** — N-5A-S1-INF |
| 3 — co-realization | **CLOSED** `[ALG]` |
| 4 — common order via N-2-ORD | **CLOSED** `[ALG]` |
| 5 — independence / non-relabeling | numerically survives; ALG form OPEN (N-5A-S1-INF) |

**N-5A-S1 is now one theorem away from closure**, exactly as the PI's routing anticipated. The remaining substance is N-5A-S1-INF: infinitely many slips from the logarithmically divergent accumulated phase defect, gated on its two named lemmas (uniform control of the phase-law remainder; the six-step-block to primitive-return bridge).

## 6. Guards

1. Gates 1/3/4 are certified for the **canonical section `Θ₀ = 0`** on the declared domain and audited orbit. Coordinate sections `Θ₀ ∉ {0, π}` are robustness checks, not certified event types.
2. Orientation uniqueness is `[NUM]` on the audited domain pending the small linearization lemma.
3. Nothing here bears on gate 2 or on SG-NG-23: closing these gates does **not** move the pair toward a nontrivial commensurability class, and the limiting steps-per-crossing ratio remains 6.
4. Scope: local tube, selected generator `T`, OPEN-P0 / SG-PROG-2 ceiling retained. `Q_true`, `Θ`, and the shear law remain Dyadic-owned imports.
