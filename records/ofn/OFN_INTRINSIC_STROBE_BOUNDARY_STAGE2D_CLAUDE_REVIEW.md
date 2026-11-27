# Review — Intrinsic strobe-boundary structure, Stage 2D (PR #424)

**Date:** 27 November 2026.
**Reviewer:** Claude (SESSION; independent review requested in the record's §7).
**Object:** PR #424 at head `fbc6cdb2b81eab4db8f48a80ae62bc194722dc0f`, record `records/ofn/OFN_INTRINSIC_STROBE_BOUNDARY_STAGE2D.md`. The PR also changes `OFN_COOWNER_ENTRY_NOTE.md`, in the ChatGPT lane only.
**Status:** SESSION / NONCANONICAL. A review is not adoption.

## 1. Evidence (review items 1 and 5)

- **Hashes.** Fetched the PR head read-only. The script (`be095000…`) and the output (`2495b517…`) match the record's table, `SHA256SUMS.txt` and the `upload/` copies.
- **Script inspection.** The checker imports only `math` and SymPy. It makes no file, process or network calls.
- **Replay.** Native replay on Linux, Python 3, SymPy 1.14.0, `python3 -I`: exit 0, output byte-identical to the stored run.
- **Independent checks.** Neither script imports the PR checker. Neither is committed; they are reported here as reviewer evidence.
  - Symbolic (SymPy; reviewer script SHA-256 `e3ab7bee…`). I rebuilt the six quadratic commutation equations from R_raw = [[1, −1], [K, 1−K]] with right-hand side (0, Kρ²). Results: det = K³(K−3)². The solved H_{2,1} equals the record's expression. K ∂_η H_{2,1}(R_raw z) = −2(K−2)η/(K−3).
  - Numerical (numpy, float64; reviewer script SHA-256 `1893c1d8…`). For p = 12, 16 and 20 at ε = 1/7, I solved for a common involution κ = −I + ΣH_d degree by degree, by least squares. The equations were commutation with both f₊ and f₋ plus κ² = id, using full raw (ρ, η) Taylor jets.
    - The residual norm is ≤ 2.4·10⁻¹¹ at every degree d ≤ q. It equals 0.79, 1.0 and 1.2 at d = q+1 for p = 12, 16 and 20.
    - Owner control at ε = 0, p = 12: the residual stays at 3·10⁻¹⁴ at d = q+1 = 6.
    - So a common involution exists through degree q, the first obstruction is exactly at q+1, and the obstruction is caused by ε.

## 2. Proof checks (review items 2–4, 6)

**§3, centralizer: correct.**
- *Zero-mode kernel.* At Fourier mode k = 0, the second diagonal coefficient (d−1)a₀ is nonzero, and (d−3)a₀ vanishes only at d = 3. There V₀ = (b₀/a₀)U₀, so the kernel is the span of X₃.
- *All-orders argument.* If G ≠ id is a tangent-identity centralizer element, its first correction is tX₃. Then G∘P^{−t} has trivial jet through degree 3 and is the identity by the same lowest-degree argument.
- *Rotation bound.* Taken from Stage 2C and applied to the truncations of formal elements.
- *Group structure.* J^n = A^n P^{−1} = id, and DJ(0) = R² generates μ_n. The direct product is abelian, and Cent(A^ℓ) = Cent(P) for ℓ | n.
- *Scope.* The record correctly refrains from classifying finite-jet centralizers.
- *Involutions.* The only involutions are id and 𝒦 = J^{n/2}.

**§4, lift classification: correct.**
- *Orbit propagation.* Prefix transport gives κ_{F^jX} = U_j κ_X U_j⁻¹.
- *Commutation.* Closing the orbit gives κ_X ∈ Cent(M) = Cent(P), since ℓ | n with ℓ = hk and k | m. This group is abelian, so κ_{CX} = Dκ_X D⁻¹ = κ_X, and κ_X² = id.
- *Roots.* Every root commutes with B, hence with P. Comparing g^{2h} = B gives t = 1/p and 2j ≡ 1 (mod m), so there are h roots, including the case m = 1.
- *Half-period identity.* g^ℓ = 𝒦D, because ℓ(2j−1)/2 ≡ n/2 (mod n) when k and (2j−1)/m are odd.
- *Bit flip.* H_X commutes with M from orbit closure (H_X M H_X⁻¹ = g^{2ℓ} = M), hence with D and with κ_X. This gives θ = 𝒦^{1+e}, for every formal reduction in the class.
- *Same-type exclusion at q-jet level.* The relation S^n = −K_t K_s⁻¹ excludes equal types.

**§5, common action: correct.**
- *Uniqueness through degree q.* A first correction at odd degree doubles under squaring. An even-degree correction has odd charge, which cannot vanish mod even p.
- *Failure at q+1.* The first-component residual comes only from DH_{2,1}(R_raw z)·(0, 2εKρ^q). Higher terms of κ are common to both parities and enter both commutators identically at this order.
- *Exact C^{q+1} step.* The averaging chart (z + κ(z))/2 handles the derivative +I case.
- *Parity split.* 𝒦₊ and 𝒦₋ coincide through degree q and first differ at q+1, consistent with the numerical check above.

**§6, readout restriction: correct and conditional.** Differentiating gives Dκ_X(0) = τI, given the scalar-sign classification. The nonclaims about quadratic invariants and transported observations are appropriate.

## 3. Remarks (no change to the results)

**R1 (recommended wording; the asymmetry between §4 and §5).**
- §5 excludes a register-independent nontrivial complement action on the *source*.
- The normalized product *target* action 𝒦 is register-independent and commutes with g.
- Hence a contract requiring complement to act register-independently forces e = 0 on the source (at C^{q+1} level). It still admits the reduction to the target with fixed action 𝒦.
- So register independence alone does not block reduction. What blocks it is same-type preservation, for example the fibre-observable contract of §6. A sentence in §5 or §6 would prevent the q+1 result from being read as an irreducibility criterion.

**N1 (reading of the result; advisory).**
- After Stage 2D, the comparator's presentation-invariant content in this category is a single relative ℤ₂ datum per orbit: product reduction is possible iff e_source + e_target ≡ 1.
- The Stage 2B coupling can thus be traded exactly for a change of complement-lift type. Its irreducibility is equivalent to a contract that fixes that type.
- This supports the record's next-gate formulation: the decisive question is which presentation transformations the relational observables admit, not the design of a new gate.

**N2 (provenance).** The record states that no separate reviewer approval of the Stage 2C N2 clarification is inferred. That is accurate: the #422 review approved #420 at `f256abc8` only.

## 4. Verdict

The mathematics is correct and independently replicated. The q+1 boundary was confirmed by an independent degree-by-degree solve, with an ε = 0 negative control. The classification is complete within the stated formal, base-preserving category, and the scope and nonclaims are appropriate.

**Approve.** R1 is recommended wording; N1 and N2 are advisory.
