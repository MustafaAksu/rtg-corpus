# Review: FMS Model Selection Ledger v0.5 + OFN Model Selection Decision Request v0.1

**Date:** 17 October 2026 · **Reviewer:** Claude · **Status:** NONCANONICAL review. No owner file is changed.

## 1. Checks

| Item | Verdict |
|---|---|
| §7.2(6) Lemma S′ invariant-kernel proof | **Correct.** Df(a,0)(δu,δv) = (2p\|a\|²δu + p a²δū, q\|a\|²δv), so N_α = (p(e^{2iα}−1)δū, 0). Add "and symmetrically N′_α at (0, e^{iα})", which forces ℂ_v ⊆ K whenever π_v(K) ≠ 0. Without it, step (ii) does not by itself give K ∈ {0, ℂ_u, ℂ_v, ℂ²}. |
| §5.1 three-edge tangency | **Correct.** The cubic of D⁶ is invariant under tangent-to-identity changes, since D⁶ has no quadratic part. The witness w = (a₃/a₁, a₃/a₂, −2) gives Σa_e w_e = 0 and cubic value −6a₃. M must be invariant under the **primitive** D, which is what makes its tangent λ-invariant; state this explicitly. |
| §5.2 two-edge locks | Correct, for locks not depending on the third edge: the graph w_i = G(w_j) is invariant ⟺ G ∈ Cent(T). |
| R3 notation | {T^k exp(sX) : k ∈ ℤ₆, s ∈ ℝ} is ambiguous, because T⁶ = exp X ≠ id. Write k ∈ {0,…,5}, s ∈ ℝ (bijective), or k ∈ ℤ with the relation T⁶ = exp X. |
| §7.1 / §3 (H_spec form) | Consistent with K3 note v0.3 §3.2. At κ = 1 on ℝ⁶, the closure-sum factor E_h is correctly excluded only by the hypothesis. |
| §10 missing hash | `k3_six_step_factor_check.py` SHA-256 = `7d761090378781c5c74ec64abc1f215cc951cec21f139a231ee1bd8ed18ad4ff`. This also answers K3 note v0.3 §6, request 2. |

## 2. Substantive addition — the Q1/Q2 + Q3 exclusion does not depend on the carrier

**Proposition (corollary of §5.1).** Assume the following:
1. **The physical state is exactly the three edges.** Equivalently, the joint encoding E = (E₁, E₂, E₃) is a local C³ diffeomorphism ℝ⁶ → ℝ⁶ with E(0) = 0.
2. **Every edge is primitively autonomous:** E_e∘F = T∘E_e. Then F = E⁻¹∘T^{×3}∘E.
3. **Closure is a C³ codimension-2 submanifold through 0** that is preserved, either exactly (Q1) or as an invariant attracting manifold (Q2).

Then its image under E is a C³ invariant manifold of T^{×3}. By §5.1 its tangent is w_k = 0 or a two-edge lock w_i = c·w_j with |c| = 1, and c⁶ = 1 at C⁵.

**Hence a closure that genuinely involves all three edges is impossible in any carrier and any encoding**, group-type or not. This includes curved closures.

Consequences:
- **Special cases.** The raw-carrier result (§3, κ = 0 row) and the formal group-closure no-go of the G2 note §4 (which needs T⁶ ≠ I) are both special cases.
- **§8 elimination statement.** Drop "raw edge encoding" for this pair of requirements. Raw additivity matters only for the *definition* of C at κ = 1. The autonomy failures (R1, R7) already hold for every C³ submersive E.
- **Class C routes.** "A changed meaning of encoding/carrier" is **not** an escape while the state is three edges and E is a joint diffeomorphism. The genuine routes are:
  - **(C-a)** extra state variables, so that the state dimension exceeds six (connection, holonomy, node data);
  - **(C-b)** relaxing Q3 to partial autonomy (see §3);
  - **(C-c)** regularity below C³;
  - **(C-d)** non-submersive or singular encodings at 0;
  - **(C-e)** closure that is not a codimension-2 manifold through 0.

Status: `[ALG — SESSION]`. It follows directly from FMS §5.1 by conjugation; there is no new computation. Ownership goes with §5.1 (FMS/Genesis).

## 3. Decision request — two suggested edits

1. **Split Q3.**
   - **Q3a — all three edges** are exact DYAD factors.
   - **Q3b — some edges** (one or two) are exact factors and the remaining edge is slaved.

   Q3b is not empty. The G2 note §5a construction F(z) = (Nz₁, Nz₂, −Nz₁ − Nz₂) has exact transported closure and makes edges 1 and 2 exact factors onto T, via E_e = h∘z_e. It is formal only: it depends on the normalizer h, and an actual carrier needs DYAD OPEN 20. It also breaks node symmetry. So OFN should state whether partial autonomy, or symmetric autonomy, is what it requires.
2. **Add to §4 one line.** "If the physical state is exactly three edges, the closure-plus-full-autonomy exclusion holds in every carrier and encoding (§2 above). OFN's choice for class C is therefore between extra state variables, partial or asymmetric autonomy, sub-C³ regularity, or degenerate closure/encoding."

   This turns the open-ended class C into a short, checkable menu.

Everything else in the request — step order, non-goals, reply format — is endorsed.
