# DISC-1 Result v3 — RATIFIED: `2 ∈ Q^dyn`, `3 ∈ Q^dyn`

**Memo ID:** `NG_DISC1_RESULT_v3` · supersedes `_v2` · **Date:** 2026-09-01
**Ruling:** PI, 2026-09-01. **DISC-1B PASS · DISC-1D PASS-INT · `2 ∈ Q^dyn`, `3 ∈ Q^dyn` ratified.**
**Audit items:** 3 **CLOSED** (numerical); 4 **CLOSED** (by T1 + observed interior contingency, not by further search).
**Artifacts:** `bind3_repro_v5.py`, `bind3_enumerate_k0123_v1.py`, `bind3_disc1_enumeration_k0123.json`, `disc1_result.json`, `disc1_safeguards_v2.py` / `.log`

---

## 1. Result

| gate | verdict |
|---|---|
| DISC-1B (non-`1` breadth census, `k=1`) | **PASS** — 3253/3456 base dual-active, all carrying non-`1` classes |
| DISC-1D (same-realization discrimination) | **PASS-INT** — 64 eligible after the `1→2` fence, **22 passing**, all by interior `k=3` contingency, 0 boundary-only |
| admitted | `2:1` × 12, `3:1` × 10 → **`2, 3 ∈ Q^dyn`** |

`[COR]` v2 wrote `Q^dyn = {2, 3}`. That is an overclaim: the criterion defines membership **existentially** — admission is per label via some qualifying realization — so the experiment establishes

```
{2, 3} ⊆ Q^dyn,     Q^dyn ≠ ∅
```

and says nothing about `Q^dyn ⊆ {2, 3}`. The equality also contradicted this memo's own open follow-up that other deformation axes may admit further classes. **Currently established dynamic labels: `{2, 3}`.** A finite first discovery must not become an accidental exhaustiveness theorem — the discipline against overclaiming success is the same one that governed not manufacturing it.

Under the frozen pre-data definition these labels are locally persistent under the elementary `1→2` deformation and destroyed by the interior `1→3` comparison **for the same frozen realization**.

## 2. Item 4 closed by argument, not by search

SG-NG-26 concerns **deformation-invariant** multiplicities: if fixed `m_swap, m_P3` explained the streams throughout the declared family, T1 would force the *same* reduced class at `k = 1, 2, 3`. The observed `k=3` class change contradicts that immediately. Hence

> **DISC-1D contingency ⟹ no deformation-invariant SG-NG-26 factorization** for that realization.

Allowing `m_A, m_B` to vary with `k` does not restore the objection — that is exactly T2 periodicity triviality, every exact cycle having `N_A = a_k C_k + O(1)`, which is why periodic boundedness was demoted from dynamic evidence in the first place. My proposed "prove no common-source factorization exists" was both stronger than the frozen criterion and conflated with T2; withdrawn.

By T4 the interior defects are explicitly nonzero: `84 − 2(120) = −156` and `120 − 3(72) = −96`, so the old `2:1` and `3:1` defects diverge linearly at `k=3`.

## 3. Item 3 closed

Class simplicity predicts survival **independently of period**, verified within every short band and at fixed period:

| `k=1` period | simple `a+b ≤ 4` | complex `a+b > 4` |
|---|---|---|
| [0, 20) | 36 / 80 | **0 / 146** |
| [20, 60) | 16 / 148 | **0 / 565** |
| [60, 150) | 12 / 40 | **0 / 578** |
| **exactly 54** | **12 / 32** | **0 / 58** |

The fixed-period row is decisive: where both class types coexist at identical period, simple classes survive at 38% and complex classes never. Short cycles are necessary, nowhere near sufficient.

Persistence is also non-trivial: **0 of 22** passes have identical `(n_swap, n_p3)` at `k=1,2`; all preserve the ratio while the counts change.

The residual `n:1` structural-specialness question is an interpretive/mechanism follow-up, **not** an admission blocker — the frozen criterion required one class to be locally persistent and contingently destructible, not every class to be equally robust.

## 4. Reporting refinement adopted

The 22 passing seeds are **not** 22 independent mechanisms. At event-count transport level they reduce to exactly **two archetypes**, one per admitted class:

```
2:1   (18,9) → (16,8) → (84,120)     × 12 seeds
3:1   (18,6) → (12,4) → (120,72)     × 10 seeds
```

The count of 22 is basin/preimage prevalence; the mechanistic evidence is two class-level transport patterns. This does not weaken the existential admission rule, and it is now asserted in the safeguard certificate (S4).

## 5. Provenance task discharged

Both safeguards previously reported only in prose are now runnable artifacts in `disc1_safeguards_v1.py` / `.log` (exit 0):

- **S1** — exhaustive one-step differential of the reproduced core against `genesis_mode_b_mc_v18.py` over all 331776 reduced states for every `k ∈ {0,1,2,3}`: **0 mismatches**. Currently reproducible on demand; the *pre-enumeration execution ordering* is recorded provenance (§7), not an executable assertion — no script can certify its own historical run order.
- **S2** — independent recount of all 22 passing seeds at four `k` by driving `v18.step_universe` and reading v18's own `single_edge_swaps` / `path_interactions` counters: **0 mismatches**.
- **S3** — the item-3 within-band and fixed-period controls, asserted against the exact expected four rows with both class denominators required nonzero.
- **S4** — the two-archetype reduction, asserted against the exact expected archetypes, multiplicities and their class correspondence.

The exposed artifact set is now sufficient to re-verify the result without trusting any memo.

## 6. Queue

**Currently established dynamic labels `{2, 3}`; globally `{2, 3} ⊆ Q^dyn`, non-empty for the first time.** C7C remains downstream and is **not** unblocked: two admitted labels supply no rational arithmetic, and v1.15 keeps physical addition and multiplication separate even after multiple invariants are realized. Open follow-ups, none blocking: the `n:1` structural-specialness mechanism question; the bond-transfer classifier definition; whether further classes are admissible on other deformation axes.

## 7. Provenance record — execution ordering

Recorded as provenance, not as an executable claim. Within this session the order was: (i) `bind3_repro_v5.py` reproduced `BIND3-CYCLE-N24K1` exactly; (ii) the exhaustive S1 differential ran and returned 0 mismatches for all four `k`; (iii) only then was `bind3_enumerate_k0123_v1.py` executed to produce the enumeration; (iv) the frozen harness was run, DISC-1B before DISC-1D; (v) the S2 recount and the item-3 audit followed. `disc1_safeguards_v2.py` re-establishes S1–S4 on demand and requires `v18.py` (a copy of `genesis_mode_b_mc_v18.py`) and the enumeration JSON alongside it.

Artifact hashes for this record:

- `bind3_disc1_enumeration_k0123.json` — `dab769a075400d55fbadfb0aa3324286244a614a6e802f465e4e520a53efc83d`
- `bind3_enumerate_k0123_v1.py` — `41a86011c6ad7ccb378097aa62106bf2dfbf5acf9a4b56792a690379a6eae929`
