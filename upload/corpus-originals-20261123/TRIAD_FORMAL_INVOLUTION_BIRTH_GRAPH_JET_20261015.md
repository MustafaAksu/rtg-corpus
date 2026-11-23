# Triadic: formal involution vs. birth graph, exact jets through degree 5 (15 Oct 2026)

Scope: the conditional modal model 𝒩 = (P⊗I₂)∘T_e^{×3}∘(E⊗I₂), formal jets only (exact rationals, truncation degree 5).
Nothing here is analytic, uniform or physical. RER r3.1 stays unfrozen. These are record candidates, not adoptions.

## 0. [COR] Withdrawn claim
My earlier statement Ŝ_triad(B_κ(s)) = B_κ(−s) + O(|s|⁵) was unproven, and it is **false**:
- The componentwise defect starts at degree 2.
- The graph defect starts at degree 4.

## 1. Identity checks [ALG, exact jet, degree ≤ 5]
Ŝ = 𝒩³∘ℱ^{−1/2}, with ℱ = 𝒩⁶ = id + g and ℱ^{−1/2} = x − ½g + (3/8)(g∘ℱ − g) + O(7). All of the following PASS:
- Ŝ∘Ŝ = id;
- Ŝ∘𝒩 = 𝒩∘Ŝ;
- DŜ(0) = −I₄;
- ρ_Π commutes with both 𝒩 and Ŝ, for the swaps 2↔3, 1↔2, 1↔3 and the 3-cycle;
- Ŝ ≠ −I, because its quadratic jet is nonzero.

## 2. Componentwise covariance D(s) = Ŝ(B_κ(s)) − B_κ(−s) [ALG]
B_κ(s) = (s, κ̃Q(s)Ms), with M = [[1,−2],[2,−1]] and s = (r,e).

| degree | parent | child |
|---|---|---|
| 2 | [−½r² + ½re − ¼e², −¼r² + ¼e²] (κ-free) | 0 |
| 3 | [−3/16 r³ + 5/16 r²e − 5/16 re² + 1/8 e³, −1/8 r³ + 3/16 r²e − 1/16 re² − 1/16 e³] (κ-free) | 0 |
| 4 | κ-free (see log) | κ̃·[−r³e + 3/2 r²e² − 3/2 re³ + ½e⁴, ½r⁴ − 5/2 r³e + 3r²e² − 5/2 re³ + ½e⁴] |
| 5 | κ-free (see log) | ∝ κ̃ (see log) |

The degree-2 and degree-3 parent terms come from Ŝ's own nonlinear jet (Ŝ(s,0) ≠ (−s,0)). They are chart effects, not graph data.
Covariance and graph invariance are separate contracts, as the review said. D answers covariance; G below answers invariance.

## 3. Graph-invariance defect G(s) = Ŝ_c(B) − C_κ(Ŝ_s(B)) [ALG]
- G vanishes at degrees 2 and 3. It is exactly linear in κ̃: G = κ̃·G_lin, with G₀ = 0 (consistent with c = 0 being the exact 2↔3 fixed set).
- G₄ = κ̃·[¾r⁴ − 4r³e + 6r²e² − 6re³ + 11/4 e⁴, 11/4 r⁴ − 7r³e + 9r²e² − 7re³ + 2e⁴] ≠ 0.
- G₅ for the bare cubic graph: see the log (∝ κ̃).

## 4. Consequences [ALG, formal]
(a) **The defect at degree 4 is purely even-order.** For c = C₃ + C₄ + O(5), the degree-4 graph defect is G₄[C₃] − 2C₄. This was checked for a generic quartic C₄.
- So the formal Ŝ-invariant completion is unique at degree 4: C₄ = G₄/2.
- With C₄ = G₄/2, the defect vanishes through degree 5 (checked for κ̃ = 1, 2). Odd-order terms C₅ drop out of G₅.
- So "the cubic graph B_κ is not Ŝ-invariant" is a statement about that truncation. It is **not** an obstruction to the existence of an Ŝ-invariant graph tangent to it.

(b) **Ŝ does not permute the age sheets (at κ̃ = 1).** The pinned table age_family_polynomials_kt1.json (03042f84…d83c) has 𝒞₄ ≡ 0 for every τ. The degree-4 jet of each sheet is therefore the bare cubic, and the Ŝ-image of every sheet has quartic Φ₄ = G₄ − 0 = G₄ ≠ 0.
- Hence Ŝ_triad(sheet τ) is **not** an age sheet 𝒞(·, τ′) for any τ′. This holds for the formal family at all real τ, and is decided at degree 4.
- An Ŝ-compatible birth graph would have to carry the quartic G₄/2, which the Genesis-derived age family does not have.

## 5. Record-table position (agreeing with the review, plus this result)

| candidate | status |
|---|---|
| RER-DYAD-FORMAL-INVOLUTION | [THM], FORMAL_ONLY |
| RER-TRIAD-FORMAL-INVOLUTION (incl. slot commutation) | [THM], FORMAL_ONLY; jet check §1 [ALG] |
| U^{−1/2} = (ℱ^{−1/2})* | [ALG]; 𝒞(s,τ) ≠ full-state iterate |
| R_n ≈ √(19/3)(Q₀/Qₙ)^{3/2} | [ALG leading normal-form]/[NUM]; L-SHADOW-POLY [OPEN] |
| Birth graph vs Ŝ_triad | [ALG, formal, deg ≤ 5]: cubic B_κ not invariant (first defect deg 4, ∝ κ̃); unique even completion C₄ = G₄/2; age sheets not permuted (κ̃ = 1 table). Physical/Genesis birth-role transport: [OPEN] |
| Smooth/analytic realization; physical exchange | [OPEN] |

## 6. Pins
| file | SHA-256 |
|---|---|
| triad_formal_involution_birth_jet.py | 5c020986bc0ee54b4c9f0795e954e625088802253b78546a479d17fb193a9feb |
| triad_formal_involution_birth_jet.log | 34d48bd29d68f1a1e86adf38966047bc2ab96c4900b6b9b790fff628f4974012 |
| triad_involution_graph_completion.py (needs the file above alongside) | 024c9ad1ee5d36ecc088de1e8301109c75fd236d524987ce4a2e681cf89a0574 |
| triad_involution_graph_completion.log | 206ec8d3d1d1907ec459a6a989980c1259b93d35cebfe3b15f4f7a53d9e0ec84 |

Both scripts use only the Python standard library and finish in about 1 s; exit 0 means all identity checks pass.
