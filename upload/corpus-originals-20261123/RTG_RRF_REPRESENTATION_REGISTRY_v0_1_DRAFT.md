---
title: "RTG — RRF Representation Registry"
version: "v0.1 DRAFT"
date: "24 September 2026"
class: "working artefact / representation discipline"
status: "noncanonical; does not amend OFN, DYAD, RECOG, NUMGEN, Triadic Birth-Lift or Discrete Genesis"
parent: "RTG_PRIMORDIAL_RELATIONAL_REPRESENTATION_WRAPUP_v0_2 §20, §26"
---

# 0. Purpose, scope, lock

**Purpose.** Fix, for every representation profile currently in use in the RTG dyad/network work, what its native objects are, how it transports to the others, which observables are native / transported / re-defined, how the pole-relabeling candidate acts in it, and what is lost on each transport. The registry produces no new physics; it makes representation mistakes of the R11 type mechanically visible.

**Scope.** Isolated continuous dyad (four profiles) and a provisional raw-edge network profile. Discrete (TDR-G) state representation is referenced, not registered here (see §7).

**Status vocabulary.** DSN tags only: `[DEF]`, `[ALG]`, `[THM]`, `[NUM]`, `[HYP]`, `[OPEN]`, each with `[scope: …]` where needed. `[ALG-DISC]` marks exact algebra performed in the PRR discussion but not yet installed in an owner DSN; items marked `(ext.)` were computed by the external participant and have **not** been independently re-verified in this session.

**Representation safety lock (provisional, until OPEN-E).**

> All triad/network equations are written in profile `RRF-NET-W-RAW`. `z_NF` appears in network work only inside an explicitly transported single-dyad subexpression. No closure, incidence, comparator or holonomy law is transferred between profiles without its registered transport arrow.

Rationale: single-dyad normalisation turns linear closure `Σ ε_e W_e = 0` into `Σ ε_e h(z_e) = 0`, not `Σ ε_e z_e = 0` (Wrap-up §19).

---

# 1. Equation annotation syntax

Every reusable displayed equation carries a suffix referencing a profile ID in this registry:

```
<equation>        (rep: <PROFILE-ID>; <exactness>; <domain>)
<equation>        (transport: <SRC> → <DST>; <arrow-ID>; <domain>)
```

Examples:

```
Q_prim = |W|^2                       (rep: RRF-DYAD-W; exact; lifted)
|F̂(z) − J(z)| ≤ C_7 |z|^7            (rep: RRF-DYAD-NF; certified remainder; |z| ≤ r)
W = h(z, z̄)                          (transport: NF → W; T-h; |z| ≤ r_h)
```

The suffix is a pointer. Definitions, domains and remainders live in the profile/arrow entries below, never in the suffix. This extends the existing `[conv:]` / `[scope:]` discipline; it is an RTG documentation convention, not a claimed universal notation.

---

# 2. Representation profiles

## 2.1 `RRF-DYAD-WRAPPED`

| Field | Entry |
|---|---|
| Native state | `ζ = e^{ρ+iη} ∈ ℂ*`, equivalently `(m, ν) ∈ ℝ_{>0} × U(1)`, `m = e^ρ`, `ν = e^{iη}` |
| Domain | global on ℂ* |
| Native dynamics `[ALG-DISC]` | `m' = m·e^{−s(ν)}`, `ν' = ν·e^{i[m−1−s(ν)]}`, `s(ν) = (ν − ν^{−1})/(2i)`; exact rewrite of the primitive map (verified this session) |
| Native observables | `\|ζ\| = m`, `ζ/\|ζ\| = ν`, multiplicative ratio `R^×_{ab} = ζ_a^{−1} ζ_b` |
| Observable status | all **native**; `R^×` is **re-defined**, not the transport of `W̄_a W_b` |
| Relabeling candidate | `ζ ↦ ζ^{−1}` — exact as the action induced by `R_AB ↦ R_BA = R_AB^{−1}` under ordered-ratio semantics; identification with physical pole exchange is OPEN-A |
| Exactness | exact |
| Information loss | integer lift / winding of η is not carried |
| Genesis inheritance | `[OPEN]` (Ledger, Wrap-up §14.1) |
| DSN status | `[DEF]` profile; dynamics `[ALG-DISC]` |

## 2.2 `RRF-DYAD-LIFT`

| Field | Entry |
|---|---|
| Native state | `(ρ, η) ∈ ℝ²`, η unwrapped |
| Domain | global on ℝ² as a chart; global-on-cylinder only with a declared lift/history |
| Native dynamics `[SOURCE: DYAD]` | `ρ' = ρ − sin η`, `η' = η + e^ρ − 1 − sin η` |
| Native observables | lifted differences `(Δρ, Δη)` along a trajectory; fixed points `P_1 = (0,0)` elliptic, `P_2 = (0,π)` hyperbolic (`tr J = 3`, `det J = 1`) `[SOURCE: RECOG]`; winding fixed points `(log(1+2πk), 0/π)` on the global cylinder `[SOURCE: RECOG]` |
| Observable status | `(Δρ, Δη)` **lifted realisation** of `R^×`; not equal to `log R^×` without branch data |
| Relabeling candidate | `S_lift = L^{−1} S_6 L` — degree-6 certified `(ext.)`; **not** `(ρ,η) ↦ (−ρ,−η)`, which fails at quadratic order: `T∘S_o − S_o∘T = (0, 2(cosh ρ − 1))` `[SOURCE: RECOG, T = T_s + T_b]` |
| Exactness | dynamics exact; swap action certified through degree 6 |
| Information loss | none relative to WRAPPED; adds branch data |
| Guard | `η ≠ arg ζ` globally without a chosen lift |
| DSN status | `[DEF]`; dynamics `[SOURCE]` |

## 2.3 `RRF-DYAD-W`

| Field | Entry |
|---|---|
| Native state | `W = ρ + ωη`, `ω = (−1 + i√3)/2` |
| Domain | lifted/local; does not descend to the wrapped cylinder without branch data |
| Native dynamics | linearised map = rotation by `λ = e^{iπ/3}` in the W-frame; `λ^6 = 1` `[SOURCE: OFN six-step]` |
| Native observables | `Q_prim = ρ² − ρη + η² = \|W\|²`; Hermitian comparator `C_W(a,b) = W̄_a W_b`; normalised `Ĉ = e^{i(Θ_b − Θ_a)}` |
| Observable status | `Q_prim`, `C_W` **native** (raw bilinear forms) |
| Relabeling candidate | `S_6 = h∘(−I)∘h^{−1}`; `𝒥_{≤6}(S_6² − I) = 0`, `𝒥_{≤6}(f∘S_6 − S_6∘f) = 0` `[ALG-DISC (ext.)]`; first terms `S_6(W) = −W + s_2(W,W̄) + O(3)` |
| Covariance of native observables under `S_6` `[ALG-DISC (ext.)]` | `C_W(S W_a, S W_b) − C_W(W_a, W_b) = O(3)` (not invariant beyond quadratic order); `C_W(S W_a, W_b) = −C_W(W_a, W_b) + O(3)` |
| Exactness | `L` exact linear bijection; swap action degree-6 certified |
| Information loss | none relative to LIFT |
| Guard | `Re W, Im W` are structure-adapted components, not spatial axes `[SOURCE: OFN]` |
| DSN status | `[DEF]`; `Q_prim = \|W\|²` `[THM, exact]` |

## 2.4 `RRF-DYAD-NF`

| Field | Entry |
|---|---|
| Native state | `z`, with `W = h(z, z̄)`, `h` the delivered degree-6 normaliser |
| Domain | `\|z\| ≤ r_h` (certified injectivity/inverse radius) and the remainder domain of the return enclosure; **local only** |
| Native dynamics | formal normal form `f̂(z) = λz + a z\|z\|² + b z\|z\|⁴ + c z̄⁵ + …`; resonant monomials `z^p z̄^q` with `p − q ≡ 1 (mod 6)`, hence all of odd degree |
| Symmetry `[ALG-DISC]` | `f̂(λz) = λ f̂(z)` (formal all-order ℤ₆ equivariance); therefore `f̂(−z) = −f̂(z)`, `−1 = λ³` |
| Native observables | `q = \|z\|²`; self-return multiplier `χ_m(z) = f̂^m(z)/z`; NF comparator `C_z(a,b) = z̄_a z_b` |
| Observable status | `q`, `χ_m`, `C_z` **native / re-defined**; `Q_prim = \|h(z,z̄)\|²` and `C_W = \overline{h(z_a)} h(z_b)` **transported** |
| Relabeling candidate | `z ↦ −z`: exact symmetry of the formal normal form; degree-6 certified in the delivered analytic chart; conjugacy-invariant under λ-equivariant residual normaliser gauge `[ALG-DISC; scope: residual gauge group not fully classified — RECOG quintic caveat]` |
| Covariance under `−I` | `q`, `χ_m` invariant (exact); `C_z(−z_a,−z_b) = C_z`, `C_z(−z_a, z_b) = −C_z` (exact) |
| Common-realisation condition `[DEF, proposed]` | two z-states may be compared by `C_z` only if they are images under the **same registered `h`** of states in the **same registered W-frame**, or if an explicit certified frame transport between their charts is registered |
| Exactness | formal all-order / degree-6 certified / certified remainder `C_7\|z\|^7` |
| Information loss | none inside domain; no global content |
| Guard | `q ≠ Q_prim` beyond leading order; `z̄_a z_b ≠ \overline{h(z_a)} h(z_b)` in general |
| DSN status | `[DEF]`; symmetry `[ALG-DISC]`; `h` certificate per DYAD v6.4.10 draft |

## 2.5 `RRF-NET-W-RAW` — provisional

| Field | Entry |
|---|---|
| Native state | oriented raw edge relations `W_e` plus declared incidence/attachment structure (edge → pole-identification sites) |
| Domain | lifted; per-edge local |
| Permitted native equations | cycle sums `Σ_{e∈γ} ε_{γe} W_e`; raw edge comparators `W̄_a W_b` for **incident** edges (relative orientation supplied by incidence); incidence maps `D`, cycle operator `C` |
| Forbidden implicit substitution | `W_e ↦ z_e` inside any of the above |
| Relabeling action | per-edge orientation reversal `W_e ↦ −W_e` **together with** incidence sign `ε_{γe} ↦ −ε_{γe}`; incidence-dressed quantities invariant; bare `W̄_a W_b` for non-incident edges has no gauge-invariant sign |
| Exactness | linear closure exact in this profile |
| Information loss | none declared; holonomy content see §5 |
| Status | provisional until OPEN-E; canonical choice of network state variables (OPEN-E1) cannot be closed before OPEN-B (identification primitive) |
| DSN status | `[DEF, provisional]` |

---

# 3. Transport graph

```
RRF-DYAD-NF  --T-h-->  RRF-DYAD-W  --T-L-->  RRF-DYAD-LIFT  --T-exp-->  RRF-DYAD-WRAPPED
                                  (no native/global NF → WRAPPED arrow; local composite T-exp∘T-L∘T-h exists)
RRF-NET-W-RAW  <--(edge-wise, per registered W-frame)--  RRF-DYAD-W
```

| Arrow | Map | Type | Inverse | Domain | Observable transport | Constraint transport | Gauge transport | Loss |
|---|---|---|---|---|---|---|---|---|
| `T-h` | `W = h(z,z̄)` | certified local nonlinear diffeomorphism | local-certified `h^{−1}` | `\|z\| ≤ r_h` | `q → Q_prim = \|h\|²`; `C_z` → `C_W` only via `\overline{h}h` | single-dyad only; closure not transported | `−I ↦ S_6` | none in domain |
| `T-L` | `(ρ,η) = L^{−1}W` | global linear bijection | global | ℝ² | `Q_prim = ρ²−ρη+η²` | linear closure transported exactly | `S_6 ↦ L^{−1}S_6L` | none |
| `T-exp` | `ζ = e^{ρ+iη}` | covering / quotient wrap | **none without lift** | global | `(Δρ,Δη) ↦ R^× = e^{Δρ+iΔη}` (loses `k`) | additive cycle sums ↦ multiplicative `H_×`; `Σ Δη = 2πk` collapses to `H_× = 1` | `S_lift ↦ ζ^{−1}` at linear order only | integer winding |
| `T-net` | edge-wise embedding of `RRF-DYAD-W` states | identity on each edge, requires registered shared W-frame per incidence site | — | per edge | `C_W` for incident edges | closure **native** here | orientation ↔ incidence sign | none |

Rule: an observable or constraint written in a destination profile without a row in this table is **untransported** and must be tagged `[OPEN: transport]`.

---

# 4. Comparator and swap matrices

## 4.1 Comparator typing

| Profile | Comparator | Type | Status |
|---|---|---|---|
| WRAPPED | `ζ_a^{−1} ζ_b` | multiplicative ratio, ℂ*-valued | native / re-defined |
| LIFT | `(Δρ, Δη)` | additive lifted difference | lifted realisation (branch-dependent) |
| W | `W̄_a W_b` | Hermitian bilinear form | native |
| NF | `z̄_a z_b` | Hermitian bilinear form in NF chart | native / re-defined |
| NF (transport of W comparator) | `\overline{h(z_a)} h(z_b)` | transported observable | transported |

`z̄_a z_b ≠ \overline{h(z_a)} h(z_b)` in general. `[SOURCE: RECOG raw/post-H₂ guard; Wrap-up §11]`

Exact `S`-decomposition available in any profile with a registered involution `S` `[ALG-DISC]`:
`C = C_− · C_+`, `C_−(x) = (C(x)/C(Sx))^{1/2}`, `C_+(x) = (C(x)·C(Sx))^{1/2}`; `C_−(Sx) = C_−(x)^{−1}`, `C_+(Sx) = C_+(x)`. `C_+ ≠ 1` measures failure of typed covariance of `C`; `C_+` is S-even and cannot decide orientation.

## 4.2 Pole-relabeling candidate actions

| Profile | Action | Status |
|---|---|---|
| WRAPPED | `ζ ↦ ζ^{−1}` | exact as ordered-ratio relabeling candidate |
| LIFT | `L^{−1} S_6 L` | degree-6 certified `(ext.)`; not `(−ρ,−η)` |
| W | `S_6 = h(−I)h^{−1}` | degree-6 certified `(ext.)` |
| NF | `z ↦ −z` | formal all-order symmetry; degree-6 certified in delivered chart |

> These actions are representation-level candidates for the same physical pole exchange. Their mutual identification, and identification with physical relabeling, is **OPEN-A**. In particular `ζ ↦ ζ^{−1}` (WRAPPED) and `z ↦ −z` (NF) agree at linear order only; whether they are the same physical operation is not established.

Typed-covariance criterion for gauge status (Wrap-up §10.2): `O(Sx) = τ_O(O(x))` for every admissible `O`, with `τ_O` the type's relabeling law — not universal invariance.

---

# 5. Cycle-invariant matrix

| Invariant | Value space | Arity | Required structure | Invariant under | Present in certified local dyad tube? | Present in current genesis models? |
|---|---|---|---|---|---|---|
| `H_×(γ) = Π_{e∈γ} R_e` | ℂ* | cycle ≥ 3 | multiplicative edge relations, coherent endpoint gauge | diagonal carrier gauge `x_i ↦ g x_i` | potentially (network needed) | node-mediated ⇒ `H_× = 1` built in |
| `H_2(γ) = Π_{e∈γ} σ_e` | ℤ₂ | cycle ≥ 3 | pole-identification connection `σ_e` | incidence-dressed node/frame sign gauge `σ_{uv} ↦ g_u σ_{uv} g_v` | definable in tube (no winding needed) | not independently represented (node-mediated attachment) |
| `k` | ℤ | history / path-lift; cycle when spatially closed | coherent lifted history | node-coherent `2π`-lift gauge `θ_i ↦ θ_i + 2πn_i` | trivial (`k = 0`, no wrap crossing) `[SOURCE: NUMGEN]` | trivial |

Obstruction statements (one-way, `[THM/ALG scope]`): `H_× ≠ 1 ⇒` no pure node-presentation reduction; `H_2 = −1 ⇒` present node-mediated identification scheme insufficient (either pole-role identification or an added ℤ₂ edge field is required); additive `Ca ≠ 0 ⇒` node-potential representation insufficient `[SOURCE: NUMGEN NG-7A]`. No coupling among the three is claimed.

---

# 6. Dependency lock: OPEN-B → OPEN-E1 → OPEN-E2

- **OPEN-B** (genesis identification primitive: node identity vs pole-role identity) must be resolved before a **canonical** choice of network state variables (**OPEN-E1**).
- Provisional network work may proceed in `RRF-NET-W-RAW` with incidence data, provided any node-mediated Jacobi/mode reduction is explicitly marked as that branch.
- **OPEN-E2** (joint constrained normal form of the coupled triad) starts only after E1. The single-dyad `h` is not the answer to E2.

---

# 7. Not registered in v0.1

- TDR-G discrete state profile (node phase/advance data; edges reconstructed from nodes) — to be registered once OPEN-B fixes whether `σ_e` is added.
- Any profile for effective geometry (metric/connection/curvature) — no representation decision exists; deliberately last in the PRR ladder.
- Genesis inheritance fields for all profiles — pending the Genesis Identification & Inheritance Ledger (Wrap-up §14.1).

---

# 8. Claims this registry does NOT make

1. That any profile is the physical/primordial carrier.
2. That the four relabeling candidates in §4.2 are the same physical operation.
3. That `H_×`, `H_2`, `k` couple or share a carrier.
4. That the provisional network lock is a result; it is a safety convention revisable at OPEN-E.
5. That items marked `(ext.)` have been re-verified here.

---

# 9. Change log

- v0.1 DRAFT (24 Sep 2026): initial registry from PRR Wrap-up v0.2 §20/§26 and the follow-up discussion; four dyad profiles, provisional network profile, transport graph, comparator/swap matrices, cycle-invariant matrix, dependency lock.
