# NG-7A Certificate — Additive Recurrence-Holonomy Operator / Null Theorem

**Certificate ID:** `NG_NG7A_HOLONOMY_NULL_CERT_v1`
**Parent RID:** `NUMGEN-OPEN-REC-HOL` · **Sub-RID:** `NUMGEN-OPEN-REC-HOL-OPERATOR`
**Target document:** `RTG_NUMBER_GENESIS_DSN_v1.5`
**Date:** 2026-08-28 · **Auditor/author:** Claude (RTG mathematical auditor / DSN editor)
**Status:** `[RESULT][from: ALG]` with exit-code-gated `[ENG]` certificate (`ng7a_holonomy_null_cert_v1.py`, 12 assertion families, all pass, exit 0)
**Scope:** finite directed multigraph operator layer over field coefficients (certificate executes over ℚ), with an integer/modular `Z_N` zero-control layer; loops and parallel edges included
**Ownership:** Number Genesis · **Export:** operator half of `RTG-OFN-OPEN-HOLONOMY-RANK-DIAGNOSTIC` (OFN v0.7 §4.4/§9)

---

## 1. Setting and declared domain

Finite directed multigraph `G = (V, E)`, `n = |V|`, `m = |E|`, `c` connected components. Incidence operator `D ∈ 𝔽^{V×E}`: `+1` at the head, `−1` at the tail, zero column for a self-loop. Edge cochains `a ∈ 𝔽^E` (`𝔽` a field; ℚ in the executable). Cycle space `Z = ker D`, `dim Z = β = m − n + c` (first Betti number = **cycle capacity**). Cycle-basis operator `C ∈ 𝔽^{β×E}`, rows a basis of `Z`. **Additive holonomy vector** `h(a) = C a ∈ 𝔽^β`; multi-channel data `A ∈ 𝔽^{E×d}` gives `H = C A`.

**Declared-domain convention.** Edge data must be total on the declared edge set; partial data restricts to the support subgraph, on which `(D, C, β)` are recomputed. Missing/undefined ratios are excluded from the domain, not imputed.

**Multiplicative layer.** For strictly positive data `w`, cycle holonomy `hol_×(z, w) = Π_e w_e^{z_e}`; `log` intertwines it with the additive layer. Admissible only in a certified positive multiplicative sector — this is exactly NG-0R representation mechanism 2 under SG-NG-22.

## 2. Theorems (all `[from: ALG]`; executable references in brackets)

**T1 — Null theorem (PI core).** `C Dᵀ = 0` as an operator identity; hence `A = Dᵀ X ⟹ C A = 0`. *Proof:* each row `z` of `C` satisfies `D z = 0`, so `zᵀ Dᵀ = (D z)ᵀ = 0`. [S1, T1]

**T2 — Completeness over field coefficients.** `im Dᵀ = ker(C·)`, i.e. `h(a) = 0 ⟺ a = Dᵀ x` is solvable. *Proof:* T1 gives `im Dᵀ ⊆ ker(C·)`; `dim ker(C·) = m − β = n − c = rank Dᵀ`, forcing equality. Consequently `h` descends to an isomorphism `H¹(G;𝔽) := 𝔽^E / im Dᵀ ≅ 𝔽^β`, so the holonomy vector `h` and the cohomology class `[a]` are **equivalent complete obstructions** to integrability. In the abstract-graph case the "appropriate closure operator" of the PI formulation is the zero map to 2-cochains (no 2-cells), so its kernel is all of `𝔽^E`; declaring a 2-complex/embedding later restricts that kernel and belongs to NG-7B/geometry work. [T2]

**T3 — Orientation consistency.** Edge reorientation by signs `S`: `(D, C, a) → (DS, CS, Sa)` leaves `h` invariant (`CS·Sa = Ca`). Reversing the traversal of one basis cycle negates exactly that component of `h`. Orientation-invariant statistics: the zero-set of `h`, ranks, and the class `[a]`. [T3]

**T4 — Gauge invariance.** `h(a + Dᵀ g) = h(a)` for every node potential `g`; per-component constant shifts of potentials are exact gauge (`Dᵀ 𝟙_comp = 0`) — the operator-level form of relational primacy (only differences enter). [T4]

**T5 — Cycle-basis covariance.** For any other basis `C' = M C`, `M ∈ GL(β,𝔽)`: `h' = M h`. Basis-invariant objects: the zero-set of `h`, `rank(C A)`, and `[a]`. Declared statistics must be drawn from these. [T5]

**T6 — Typed statistic (PI architectural ruling, locked).** For scalar data (`d = 1`) the primitive observable is the **holonomy vector `h`** (equivalently `[a] ∈ H¹`); `rank(C a) ∈ {0,1}` always — both values realized in the certificate — so "holonomy rank" is *never* used for a scalar channel. For genuinely multi-channel data (`d ≥ 2`), `r_hol := rank(C A)` is defined and satisfies: invariance under channel recombination `A → A R`, `R ∈ GL(d,𝔽)`; the bound `r_hol ≤ min(β, d)`; and `r_hol = 0 ⟺ A = Dᵀ X` (per-channel T2). [T6]

**T7 — Separation: cycle capacity ≠ holonomy content.** On every test graph with `β > 0`: flat multi-channel data realize `(β > 0, r_hol = 0)`, and the Gram witness `A = Cᵀ` realizes `r_hol = β`. Capacity (topology) and content (data) are certified as independent axes — the operator-level form of the Foundations distinction. [T7]

**T8 — TDR-G `Z_N` zero-control (mandatory import test).** Integer cycle vectors annihilate node-difference `Z_N` phase data modulo `N` (rings `N = 6, 8, 12` and random graphs); a single unit defect on one edge is detected (`h ≢ 0 mod N`). **Mod-`N` completeness is deliberately not claimed**: over `ℤ/N` the converse enters cut-lattice/critical-group territory and would be its own scoped OPEN if ever needed. [T8]

**T9 — Multiplicative spot theorem.** On `K3` with node weights `p`, ratio data `w_e = p_head/p_tail` gives exact cycle product `1`; a single-edge `×7` defect gives product `≠ 1` (exact rationals). [T9]

**T10 — Edge cases.** Forest: `β = 0`, `h` empty, every cochain integrable. Self-loop: node-difference data vanish on it, while any nonzero loop datum is a detectable defect — the smallest non-integrability witness. Support-subgraph convention verified on `K4` minus an edge. [T10]

## 3. Executable certificate

`ng7a_holonomy_null_cert_v1.py`: exact arithmetic (sympy rationals; integers mod `N`), fixed seed, graph suite {K3, K4, two disjoint triangles (`c = 2`), forest, multigraph with parallel edges and a self-loop, Petersen (`β = 6`), seeded random connected graphs, `Z_N` rings}. 12 assertion families, all pass, exit 0 (`ng7a_holonomy_null_cert_v1.log`).

**Falsification-first note (self-caught).** The first execution failed T6 because the scalar-rank check requires both values `{0,1}` to be *realized* and the initial sampling drew only generic (rank-1) data. Fixed by adding a flat sample; the assertion itself was not weakened. Recorded per programme error-ledger discipline.

## 4. Guards

1. **Scalar terminology guard (PI-locked).** `h`/`[a]` for `d = 1`; `r_hol` only for `d ≥ 2`. No exceptions.
2. **SG-NG-7 unchanged.** Nonzero holonomy certifies non-integrability of the data, never geometric curvature by itself.
3. **No Track-C identification.** The ring `Z_N` defect statistic is numerically a total-defect residue; it is *not* identified with Track-C winding/character labels absent a proved map (cf. NG-8A guard 4).
4. **Non-Abelian reserved for NG-7B.** No "non-Abelian holonomy rank" exists until a conjugation-invariant is defined and certified; the Case E2 route additionally requires its flatness and topology guards.
5. **Mod-`N` completeness not claimed** (see T8).
6. **Realization scope.** This layer is abstract operator theory (SG-NG-9 discipline: novelty lies in the RTG typing, separation, and control structure, not in reinventing graph cohomology). Any RTG-physical instantiation inherits the realization's own scope and, where the continuous generator enters, the OPEN-P0 ceiling.

## 5. Export note (Foundations interface)

T1–T7 discharge the **operator half** of `RTG-OFN-OPEN-HOLONOMY-RANK-DIAGNOSTIC`: a certified operator now separates cycle capacity (`β`) from holonomy content (`h`, `r_hol`), with the complete obstruction property and the typed statistic the OFN entry requested. The **physical-source half remains OPEN as NG-7B**, with the OFN v0.7 §9 narrowing intact (discrete phase sector proven flat; live candidates: continuous frame/connection, birth/history, spin/quaternionic, OPEN-M content). OFN-side DSN synchronization is a separate governance edit, proposed as decision **D15**.

## 6. Closure verdict

**NG-7A CLOSED** at `[RESULT][from: ALG]`, scope as declared, certificate exit 0. NG-7B remains OPEN. Queue advances to N-2-ORD.
