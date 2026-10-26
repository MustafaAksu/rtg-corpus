# N-5A-S1-GAP-LOCK — Lemmas 1 and 2 Closed; Lemma 3 Scoped

**Memo ID:** `NG_N5AS1_GAPLOCK_PARTIAL_v1` · **RID:** `NUMGEN-OPEN-N5AS1-GAPLOCK`
**Canonical base:** `RTG_NUMBER_GENESIS_DSN_v1.12.1` (sha256 `c4167e32…a6c6b`, verified)
**Date:** 2026-08-28 · **Author/auditor:** Claude
**Artifacts:** `ng_n5as1_gaplock12_cert_v1.py` / `.log` (7 assertion families, exit 0)
**Prior correction accepted:** my v1.12 promotion of the physical slip rate carried the hidden `{6,7}`-alphabet premise, and my "offset convergence open" conflated the already-convergent `C_D` with the genuinely open event-locking. Both `[COR]` against the v1.12 verification memo. The defect-threshold theorem of v1.12.1 stands as the correct stronger statement.

---

## 1. Lemma 1 (alphabet) — CLOSED

**Statement.** On a sufficiently small punctured tube, every complete canonical B-return gap lies in `{6, 7}`; combined with the closed infinitely-many-non-6 theorem, there are infinitely many 7-gaps exactly.

**Proof from already-certified pieces.** Two inputs, both in hand: (P-a) L-MONO in its promoted form, increments `δᵢ = π/3 + O(√Q)`, positive; (P-b) L-PHASE at **every** basepoint — the jet is an expansion at the fixed point, so `Λ₆(x) = 2π − τQ(x) + r(x)`, `|r| ≤ CQ^{3/2}`, holds for every small `x`, block-aligned or not. Shrink so `τQ > CQ^{3/2}` (making `Λ₆ < 2π` strict) and `c√Q < π/3`.

*No gap ≤ 5.* Crossings at `n` and `n+g`, `g ≤ 5`: the overshoot at `n` satisfies `o < δₙ` (monotone lift), and crossing again requires `o + Σ_{n+1}^{n+g} δ ≥ 2π`, hence `Σ_{n}^{n+5} δ ≥ Σ_{n}^{n+g} δ > 2π`. But that six-consecutive-step sum is `Λ₆(x_{n−1}) < 2π`. Contradiction.

*No gap ≥ 8.* Such a gap requires `o + Σ_{n+1}^{n+7} δ < 2π` with `o ≥ 0`. But `Σ_{n+1}^{n+7} = Λ₆(x_n) + δ_{n+7} ≥ (2π − τQ − CQ^{3/2}) + (π/3 − c√Q) > 2π` after shrinking. Contradiction. ∎

**Certificate support.** `Λ₆ < 2π` at all 3582 sampled basepoints across three seeds with `sup|r|/Q^{3/2} = 1.419`; `min(Λ₇ − 2π) = 1.0436 ≈ π/3`; long-run alphabets `{6:666661, 7:4}` and `{6:333327, 7:5}`. **Scope necessity demonstrated:** outside the smallness hypothesis the alphabet breaks (`{6:822, 7:8, 11:1}` at `Q₀ ≈ 1.29`) — the local hypothesis is load-bearing.

## 2. Lemma 2 (bookkeeping) — CLOSED

With the alphabet, telescoping the gap word over the first `6M` primitive steps gives `6M = 6N_B(M) + s(M) + O(1)` where `s` counts 7-gaps and the `O(1)` is boundary partial gaps (`≤ 14` from first/last event positions; observed deviation `≤ 5` at eight checkpoints). Hence

```
E_B(M) = s(M) + O(1).
```

**Consequence.** The v1.12.1 theorem-grade discrepancy `E_B(M) = (3τ/π) log M + O(1)` now transfers to the **physical 7-gap count**:

```
s(M) = (3τ/π) log M + O(1),
```

and therefore the physical mean exponential rate `(1/k) log M_k^{phys} → π/(3τ)` is restored to theorem grade — this time with the alphabet premise proved rather than assumed. The PI's demotion at v1.12.1 was correct; the promotion is now earned.

## 3. Lemma 3 (within-cell locking) — OPEN, obstruction identified

What separates the **defect-threshold** ratio theorem (proved in v1.12.1) from the **physical consecutive-slip** ratio limit is exactly this: `N_B` is a lap count, differing from `(2πM − D_M)/2π` by fractional parts `{(φ_{6M} − θ₀)/2π}` that oscillate in `[0,1)` and need not converge. The k-th *physical* 7-gap therefore sits within a bounded but possibly non-convergent offset of the k-th defect threshold. Lemma 3 is precisely the claim that this within-cell offset converges (or is asymptotically one-to-one locked), and the v1.12.1 Fatou question — whether the existing `C_D` is the canonically normalised iterative-residue constant and whether that normalisation controls the within-cell offset — is its natural route. Not attempted here.

## 4. State of GAP-LOCK

| Item | Status |
|---|---|
| 1 — eventual local alphabet `{6,7}` | **CLOSED `[ALG]`** (small-tube-local; necessity of smallness demonstrated) |
| 2 — bounded bookkeeping `E_B = s + O(1)` | **CLOSED `[ALG]`** |
| 3 — threshold ↔ physical-slip locking | OPEN (fractional-part obstruction; Fatou-normalisation route) |

N-5A remains closed throughout; nothing here reopens it. N-5 remains the active frontier, and this strengthens what N-5 receives: the physical 7-gap count law is now itself a certified invariant of the A/B pair, alongside `E_B` — two equivalent-up-to-`O(1)` presentations of the same unbounded relational discrepancy that any commensurability quotient must not erase.

## 5. Guards

1. Alphabet and count laws are local (small tube, selected generator, OPEN-P0); the large-amplitude `11` marks the boundary.
2. SG-NG-23 unchanged: `s(M)` growing logarithmically is discrepancy structure, not a nontrivial commensurability class; the rate constant remains a chart-derived diagnostic under SG-NG-19.
3. Lemma 3's status difference is deliberately preserved: defect-threshold ratios converge (theorem), physical consecutive ratios are bounded (open).
