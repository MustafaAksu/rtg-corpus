# N-5 Discrimination v5 — Literal Certificate, Stability Locality, Observational Null Taxonomy

**Memo ID:** `NG_N5_DISCRIMINATION_CRITERION_v5` · supersedes `_v4`
**Base:** `RTG_NUMBER_GENESIS_DSN_v1.15` (sha256 `d56440c6…3375`, verified)
**Date:** 2026-08-31 · **Auditor:** Claude
**Artifact:** `ng_n5_discrimination_identity_cert_v5.py` / `.log` — 8 identity rows, all literal, exit 0.

---

## 1. Certificate now literal throughout

Accepted. P1a was the same violation I had just named, applied to my own remaining line: the expression decides the orbit `0 ↦ ½ ↦ 1` and the multiplier identity `1 − K²`, not hyperbolicity and not the persistence theorem. All rows are renamed `*-ID` and state only what their expressions decide. The closing line now enumerates what the exit code does **not** assert: eventual periodicity, positivity and uniqueness of the reduced class, the biconditional readings of T1/T3, hyperbolicity and persistence in P1a, the ray-crossing theorem, sector closure, the same-realization quantifier, and D1.

The memo carries the interpretation: `0 < K < 1 ⟹ 0 < 1 − K² < 1`, so the orbit is hyperbolic attracting, and standard hyperbolic persistence supplies the open neighbourhood.

## 2. Stability locality — accepted, and it is a real hole in v4

The v4 rule allowed `k_s ∈ {0,2,3}`, so a class present at `k = 1`, absent at `k = 2`, and reappearing at `k = 3` would have counted as stable. That is not persistence under an elementary deformation; it is a distant reappearance, and it would have satisfied the letter of the criterion while inverting its meaning. The fix is to freeze the **deformation graph**, not just the set.

**Frozen:** `k ~ k' ⟺ |k − k'| = 1`. At base `k₀ = 1`:

```
K_stab = {0, 2}          (elementary neighbours — stability witnesses)
K_cont = {0, 2, 3}       (all admissible comparisons — contingency witnesses)
```

**Pass rule (same-realization):** for one seed `x` with base class `r = r_{x,1}`,

```
∃ k_s ∈ {0,2} : r_{x,k_s} = r          (both cycles dual-active)
∃ k_c ∈ {0,2,3} \ {k_s} : r_{x,k_c} ≠ r
```

the second equivalently, by T4, `|Δ_r^{(k_c)}| = |b a_{x,k_c} − a b_{x,k_c}|·m + O(1) → ∞`.

Your margin argument is also sharper than mine: if `k = 0` yields no qualifying dual-active cycles, stability does not become impossible — `k = 2` remains the local witness and `k = 3` remains available as the non-local contingency witness. `{1,2,3}` suffices for that reason, not the one I gave in v3.

**One pre-data question this raises.** `k = 0` is in `K_stab` under the `|k − k'| = 1` graph, but the owner carries a *separate* theorem for `k = 0` (zero-width band, reachability/superselection). Legitimate dynamics and elementary neighbour are different properties: if `k = 1 → 0` crosses into a boundary stratum with qualitatively different reachability, it is arguably a stratum change rather than an elementary move, which would leave `K_stab = {2}` alone. I do not have standing to rule on this — it is an owner/PI call — but it should be settled **before** the artifact is inspected, since it changes which witnesses can establish stability.

## 3. Null taxonomy demoted to observational

Accepted; my v4 causal readings overreached. Restated as observations, with interpretation explicitly separated and non-exclusive:

| Observation | What it establishes | Compatible interpretations (not established) |
|---|---|---|
| No contingency witness on the frozen axis | DISC-1D fails on the `k` axis | common-source triviality (SG-NG-26); **or** a genuinely dynamical class that happens to be stable across this finite window |
| No local persistence witness under elementary `k`-moves | DISC-1D fails on the `k` axis | the `k`-deformation is too coarse to be elementary; **or** no stable class exists in this sector |
| Stability and contingency both present on the panel but never on one seed | DISC-1D fails on the `k` axis | the same-realization guard binding — the most mechanistically diagnostic of the three, but not the only valid failure |

All three are valid failures of DISC-1D on this axis; they differ only in diagnostic value.

## 4. One reporting addition

The pass rule is existential over a 3456-seed panel. In a deterministic setting there is no sampling noise, so a single witness is a genuine witness for an existence claim — but "1 seed of 3456" and "800 of 3456" say materially different things about the physics. I would record, as **reporting requirements and not pass criteria**: the number of passing seeds, the multiset of passing classes, and the per-seed dual-activity counts across `𝒦_DISC`. A lone passing seed should be reported as such rather than presented identically to a widespread pass.

## 5. Frozen state

- **DISC-1B:** original `N=24, k=1` SWAP/P3 non-`1` census; original FAIL rule unchanged.
- **DISC-1D family:** fixed `N = 24`, three-node no-birth sector, canonical CONV-TICK / CONV-P3CYC, same SWAP/P3 predicates, frozen raw seed panel, `𝒦_DISC = {0,1,2,3}`, deformation graph `|k − k'| = 1`, base `k₀ = 1`.
- Same-realization guard in force; a comparison point qualifies only if dual-active there.
- Pass rule as §2. If no seed satisfies it, **DISC-1D fails on the `k` axis**; no further axis is introduced afterwards.
- Reporting per §3 and §4.
- **Open pre-data item:** whether `k = 0` counts as an elementary neighbour or a boundary stratum (§2).

## 6. Ledger

C1–C4 CLOSED; C5-SYN-13 mathematical periodic control; T2 periodicity triviality; T3 corrected (closed finite invariant sector); T4 class-change ⟺ loss of boundedness of the fixed class; C6 unchanged and discriminating; N5-PHYS-1 first physical positive control, `1 ∈ Q^bd`; C7A unchanged; **`Q^dyn` = ∅ until a same-realization DISC-1D pass**; DISC-1B falsifiable non-`1` census; DISC-1D as frozen above; C7C downstream.

The substantive movement across these five rounds is that the C7B target changed from *find a rational ratio* to *exhibit a bounded rational invariant that is locally robust yet dynamically contingent* — a materially stronger claim than v1.15 asked for, and one that a periodicity artifact cannot satisfy by construction.
