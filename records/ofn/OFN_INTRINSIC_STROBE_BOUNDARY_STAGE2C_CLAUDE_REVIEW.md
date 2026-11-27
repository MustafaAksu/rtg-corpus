# Review — Intrinsic strobe-boundary structure, Stage 2C (PR #420)

**Date:** 27 November 2026.
**Reviewer:** Claude (SESSION; independent review requested in the record's §7).
**Object:** PR #420 head `f256abc8952c635ec911596c8f833644e8a78ff9`, record `records/ofn/OFN_INTRINSIC_STROBE_BOUNDARY_STAGE2C.md`. The PR also touches the ChatGPT lane of `OFN_COOWNER_ENTRY_NOTE.md`, and only that lane.
**Status:** SESSION / NONCANONICAL. A review is not adoption. My earlier session message, cited in the record §1, was preliminary input. This document is the review of the completed proof.

## 1. Evidence (review item 1)

- **Hashes.** Fetched the PR head read-only. Script `7248372d…` and output `5cd7259a…` match the record table, `SHA256SUMS.txt` and the `upload/` copies.
- **Script.** The checker imports only `math` and SymPy and makes no file, process or network calls.
- **Replay.** Native replay on Linux with Python 3 and SymPy 1.14.0 (`python3 -I`): exit 0, output byte-identical to the stored run.
- **Independent check.** I wrote a separate check in mpmath at 40 digits that does not import the PR script. It uses bivariate truncated jets in (W, V) with full exponential and sine Taylor series and no W = 0 restriction.
  - Owner full return f₀^p for p = 12, 16, 20, 24, 28:
    - The raw quadratic jet vanishes (about 10⁻⁴⁰).
    - The W|W|² coefficient equals μ = p·tan²(π/p)·f(L) with the RECOG closed form f, to about 10⁻⁴⁰.
    - Re f = (x−1)/2 holds.
    - Re μ < 0 and Im μ < 0 at every tested p.
  - Comparator at ε = 1/7, p = 12 and p = 16 (q = 5 and q = 7):
    - All lower-degree differences of P − f₀^p are exactly zero.
    - Every degree-q monomial other than V^q vanishes (about 10⁻⁴¹).
    - The V^q coefficient equals pεκ_{p,q}, to about 10⁻⁴¹.
  - This extends the PR's full homogeneous check from p = 12 to p = 16.
  - I also verified, by exhaustive enumeration for n = 2, …, 14, that F_n^n = C_n and that 2h | d_X | 2n.

## 2. Proof checks (review items 2–6)

**§2: correct.**
- *Shortest orbit.* For the alternating blocks 0^h 1^h … 0^h (m odd), F^h moves the trailing zero block, complemented, to the front. The result is C_n X, so the orbit has length exactly 2h. The state has even weight, so its parity is positive.
- *Root criterion.* Necessity holds by normalising H = id at a shortest positive-parity state. Sufficiency holds by the orbit-by-orbit chart construction, which closes because g^{d_X} = B^{k_X}.
- *Formal root.* B commutes with log(B^m), and g^{2h} = B^{2ha+mb} = B. The linear part R^{2ha} has order m because gcd(a, m) = 1.
- *Complement quotient.* The quotient orbit length is h·k_X, giving g^h = A^{h/2}.
- *Finite-jet scope.* The limitation to finite jets and polynomial representatives is stated correctly.

**§3: correct.**
- The step weight is L^{(u−v−1+n)j} = L^{2uj} because u + v = q = n − 1. Over p steps this leaves only u = 0.
- The owner normalisation through degree q eliminates every nonzero charge, since |charge| ≤ q < p − 1.
- A homogeneous first difference is invariant under a common tangent-to-identity chart.
- The raw cubic charge-zero coefficient of an identity-tangent map with zero quadratic part is invariant under such a chart. This is consistent with the vanishing raw quadratic jet found above.

**§4: correct.**
- *Linear step.* X₃∘S = S∘X₃ implies div X₃(SW) = div X₃(W) with div = 4a₀|W|². Hence S is orthogonal. A reflection would require μ = μ̄, which b₀ ≠ 0 excludes.
- *Polar bracket.* I recomputed [a₀r³∂_r + b₀r²∂_φ, r^d U ∂_r + r^{d−1} V ∂_φ] and obtained the displayed components. The system is triangular in (U, V), with diagonal multipliers (d−3)a₀ + ikb₀ and (d−1)a₀ + ikb₀, both nonzero for k ≠ 0. This also holds at d = 2 and d = 3.
- *Induction.* J_{d+1} and J_{d+2} cancel because P has identity linear part and no quadratic term. Terms quadratic in J_d first appear at degree 2d + 1 ≥ d + 3, by which point J_d is already equivariant.
- *Final projection.* At degree q the bracket of J_{q−2} carries weights of absolute value at most q − 1 < n. Projecting onto weight −n gives c_*(1 − ω^{−n}) = 0.

**§5: correct, (A) and (B) separately.**
- Normalising H = id at a positive-parity state gives g^p = A^n = P, so g commutes with P.
- *(A).* H_{F^n X} = H_{C X} = H_X gives g^n = A^{n/2}. Taking derivatives gives (Dg)^n = R^n = −I, which contradicts ω^n = 1.
- *(B).* The rotation ω would be L^{±1}, so ω^n = −1, again a contradiction.
- The argument nowhere assumes that g is in R-equivariant normal form. This was the gap noted in the PI's message, and it is closed.
- The case p = 2^k (m = 1) is covered, because the lemma does not use the order of the linear part.

## 3. Remarks (no change to the results)

**N1 (owner-specific premise).**
- The obstruction uses a₀ ≠ 0 (divergence step) and b₀ ≠ 0 (reflection and Fourier steps).
- Here a₀ < 0 means the owner full return is nonconservative at cubic order. For a hypothetical conservative variant with a₀ = 0, the linear step as written fails.
- The record already says the signs are a point-of-use deduction. A one-line nonclaim for a₀ = 0 would make the dependence explicit.

**N2 (fibre action of complement; relevant to research path A).**
- Restriction (A) uses the identity action of complement on the fibre. The obstruction is sensitive to that choice.
- If complement acts on the fibre by an involution κ, the n-step condition becomes g^n = κ A^{n/2} κ⁻¹ (up to a common chart), and the derivative condition becomes (Dg)^n = κ(−I)κ⁻¹ or a related form.
- For κ = −I the linear contradiction disappears, since (Dg)^n = I is compatible with ω^n = 1.
- So restriction (A) gives an obstruction only together with a trivial fibre action. This concretely confirms the PI's point that complement being a gauge is not enough; its fibre action must also be justified. The record's nonclaim, "a passive transport that also changes the fibre action of complement is not ruled out", covers this. An explicit κ = −I example would make the stakes visible to Stage 2D.

**N3 (joint reading).** In this programme so far, the norm, the cubic coefficient and parity-only charts each fail as a sole certificate. The surviving invariant content is the pair (c_* ≠ 0, ω^n = 1 forced versus R^n = −I), and it exists only relative to a declared presentation class. Stage 2D should therefore declare its presentation class before constructing a mechanism.

## 4. Verdict

The mathematics is correct and independently replicated. The full homogeneous contrast now extends to p = 16. The cubic signs were checked against the RECOG closed form. The centralizer lemma closes the earlier gap without a normal-form assumption on g. Scope and nonclaims are appropriate.

**Approve.** N1 and N2 are recommended wording; N3 is advisory.
