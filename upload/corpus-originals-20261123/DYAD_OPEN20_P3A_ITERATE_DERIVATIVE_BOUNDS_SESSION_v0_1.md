# DYAD OPEN 20 / O20-∞ — P3-a: polynomial bounds for higher derivatives of forward iterates, inverse branches and their composites (SESSION v0.1)

**Version:** v0.1 · **Date:** 20 October 2026 · **Author:** Dyadic DSN owner (Claude)

**Basis.**
- `DYAD_OPEN20_P2B_DOMAIN_PROOF_SESSION_v0_2_1.md` (`6f275e73…fcf4`). Review: `PROOF REVIEW ACCEPTED — P3-a AUTHORIZED`.
- Notation and hypotheses (H1)–(H3), O = B(0, 3ρ), Lemmas D1/D2 and Propositions B/C are taken from that record and are not repeated.

**Status.** `[SESSION]` proof record for review.
- It claims polynomial-in-n bounds for D^ℓ of iterates (Lemmas A, B, C) and one structural observation (§1).
- It does **not** claim C^k convergence of p_n (that is P3-c) or any embedding.
- DYAD v6.4.17 is unchanged; OPEN 20 PARTIAL; B-∞ existence OPEN.

**Check script.** `dyad_open20_p3a_check.py` (`56d81781…7140`) writes `p3a_check.json` (`1665994e…ebd1`).
- 8 gates (J1–J5, E1–E3) and 4 negative controls (N1–N4).
- Exact arithmetic, a few seconds; run locally.
- Exit 0 = all gates pass and all controls fail.

## 0. Conventions

Notation:
- H ∈ {F, G}; B̄₃ = B̄(0, 3ρ); O = B(0, 3ρ).
- Norms of multilinear maps are operator norms.
- α := c₁/a and γ := 2c₁/a = 2α (the γ of Lemma D1).

Constants:
- c̃_j := max_{H∈{F,G}} sup_{B̄₃} ‖D^jH‖ (j ≥ 2). These are finite by (H1): H is C^∞ on an open set containing B̄₃.
- E := exp(c₁(9ρ² + 1/a)).

**Faà di Bruno (Banach form).** For C^ℓ maps f, g and the set Π_ℓ of partitions π of {1,…,ℓ}:

  D^ℓ(f∘g)(u)[h₁,…,h_ℓ] = Σ_{π∈Π_ℓ} D^{|π|}f(g(u))[ (D^{|B|}g(u)[h_B])_{B∈π} ],

so

  ‖D^ℓ(f∘g)(u)‖ ≤ Σ_{π} ‖D^{|π|}f(g(u))‖·Π_{B∈π}‖D^{|B|}g(u)‖.  (FdB)

The term |π| = 1 is Df·D^ℓg. Every other term has |π| ≥ 2, so all its blocks have size ≤ ℓ − 1.

**Orbit decay** (from (H2), any u ∈ B̄₃, u_k = H^k u, q_k = Q(u_k)):
- q_0 ≤ 9ρ²;
- q_k ≤ 1/(1/q_0 + ak) ≤ 1/(ak) for k ≥ 1.

Hence, for 0 ≤ k₀ ≤ n:

  Σ_{k₀≤i<n} q_i ≤ 9ρ² + (1/a)(1 + log(1+n)).  (Σ)

This bound is uniform in u ∈ B̄₃.

## 1. Observation — the uniform form (1 + nQ(x))^A is impossible for ℓ = 3

`[THM — SESSION]` + `[ALG]` (gates J1–J5).

**Claim 1.** In raw (ρ, η) coordinates, F = T⁶ has 3-jet

  j³F = id + P₃,  P₃(ρ, η) = −(Q/6)·(7ρ − 8η, 8ρ − η),  Q = ρ² − ρη + η² = |W|².

The facts:
- the linear part is I (J1);
- the quadratic part is 0 (J2);
- P₃ ≠ 0 (J3);
- DQ·P₃ = −Q² (J5), i.e. Q(Fw) = Q − Q² + O(|w|⁵). This exactly matches the cubic statement behind (H2).

**Claim 2.** j³(F^n) = id + nP₃ for all n ≥ 1.
- Proof: induction. F(F^{n−1}w) = F^{n−1}w + P₃(F^{n−1}w) + O(|w|⁴) = w + (n−1)P₃(w) + P₃(w) + O(|w|⁴).
- Checked for n ≤ 8 in J4; control N1 (n-independent cubic) fails.

Hence ‖D³F^n(0)‖ = n‖D³F(0)‖ > 0. This grows without bound in n, while (1 + nQ(0))^A = 1.

**Consequence.** No bound of the form ‖D³F^n(x)‖ ≤ C(1 + nQ(x))^A, uniform in x, can hold near x = 0. The same applies to G, which has the same 3-jet.

The bounds below are therefore stated as **C_ℓ(1 + n)^{A_ℓ}, uniform in the base point**:
- Uniformity in x is what P3-c needs on a common neighbourhood of 0.
- The flat factor in P3-c is also uniform in x: |F^n x|^N ≤ (an)^{−N/2} for n ≥ 1.

Note on ℓ = 1: the refined form ‖DH^n(x)‖ ≤ e^{c₁Q(x)}(1 + anQ(x))^{α} does hold, by the D1 computation with the forward product. It is not needed below.

## 2. Lemma A — forward iterates

`[THM — SESSION]`

**Lemma A.** For every ℓ ≥ 1 there is C_ℓ such that, for H ∈ {F, G}, u ∈ B̄₃ and n ≥ 0:

  ‖D^ℓH^n(u)‖ ≤ C_ℓ(1 + n)^{A_ℓ},  A_ℓ := (2α + 1)(ℓ − 1) + α.

*Proof.*

1. **ℓ = 1.**
   - DH^n(u) = DH(u_{n−1})⋯DH(u_0), and ‖DH(w)‖ ≤ 1 + c₁Q(w) by (H1).
   - So ‖DH^n(u)‖ ≤ exp(c₁Σ_{i<n}q_i) ≤ E(1 + n)^{α} by (Σ). Take C₁ = E.

2. **ℓ ≥ 2, recursion.**
   - Apply (FdB) to H^{n+1} = H∘H^n: D^ℓH^{n+1}(u) = DH(u_n)·D^ℓH^n(u) + R_{ℓ,n}.
   - R_{ℓ,n} collects the partitions with |π| = j ≥ 2.
   - By induction on ℓ, ‖R_{ℓ,n}‖ ≤ K_ℓ(1 + n)^{E_ℓ}, where:
     - K_ℓ := Σ_{π, |π|≥2} c̃_{|π|}·Π_{B∈π} C_{|B|};
     - E_ℓ := max_{|π|≥2} Σ_{B∈π} A_{|B|}.

3. **Linear recursion.**
   - With e_n := ‖D^ℓH^n(u)‖ and e_0 = 0 (since ℓ ≥ 2): e_{n+1} ≤ (1 + c₁q_n)e_n + K_ℓ(1 + n)^{E_ℓ}.
   - So e_n ≤ Σ_{k<n} [Π_{k<i<n}(1 + c₁q_i)]·K_ℓ(1 + k)^{E_ℓ}.
   - Each product is ≤ E(1 + n)^{α} by (Σ), and there are n ≤ (1 + n) terms.
   - Hence e_n ≤ E·K_ℓ(1 + n)^{α + 1 + E_ℓ}. Take C_ℓ := E·K_ℓ.

4. **Exponent.**
   - Write s := 2α + 1. With A_m = s(m − 1) + α, a partition of ℓ into j blocks gives Σ A = sℓ − j(s − α).
   - This is decreasing in j, since s − α = α + 1 > 0, so E_ℓ = sℓ − 2(s − α).
   - Then α + 1 + E_ℓ = s(ℓ − 1) + α = A_ℓ. ∎

Exponent recursion: gate E1 (ℓ ≤ 12, 35 values of α). Control N2 (slope 2α) fails.

**Remarks.**
- (a) The bound holds on all of B̄₃, which is forward-invariant. Forward iterates need no controlled sub-domain.
- (b) A_ℓ grows linearly in ℓ. No common exponent across ℓ is claimed (reviewer's point 4).
- (c) The crude bound ‖D²H‖ ≤ c̃₂ ignores the decay ‖D²H(w)‖ = O(|w|). Sharper exponents are possible but are not needed.

## 3. Lemma B — inverse branches, globally on their domains

`[THM — SESSION]`

**Branches.**
- By P2B-01, G^m|_O is an injective local diffeomorphism.
- Γ_m := (G^m|_O)⁻¹ : G^m(O) → O is the C^∞ inverse branch, defined on the open set G^m(O).
- It is the branch used in p_n = Γ_n∘F^n.

**Lemma B.** For every ℓ ≥ 1 there is C̄_ℓ such that, for every m ≥ 0 and every y ∈ G^m(O):

  ‖D^ℓΓ_m(y)‖ ≤ C̄_ℓ(1 + m)^{B_ℓ},  B_ℓ := (7α + 1)(ℓ − 1) + 2α.

*Proof.* Put u = Γ_m(y) ∈ O ⊂ B̄₃.

1. **ℓ = 1.**
   - DΓ_m(y) = (DG^m(u))⁻¹ = Π DG(G^ju)⁻¹, and ‖DG(w)⁻¹‖ ≤ 1 + 2c₁Q(w) (H1, Neumann).
   - By (Σ) the norm is ≤ E²(1 + m)^{2α} = E²(1 + m)^{γ}. Take C̄₁ = E².
   - This is Lemma D1 made global on O.

2. **ℓ ≥ 2.**
   - Differentiating G^m∘Γ_m = id ℓ times with (FdB) gives D^ℓ(G^m∘Γ_m) = 0. Hence

     D^ℓΓ_m(y) = −(DG^m(u))⁻¹ Σ_{|π|≥2} D^{|π|}G^m(u)[(D^{|B|}Γ_m(y))_{B∈π}],

     a recursion in orders ≤ ℓ − 1.
   - By ℓ = 1, Lemma A (u ∈ B̄₃) and induction:

     ‖D^ℓΓ_m(y)‖ ≤ C̄₁(1 + m)^{γ}·Σ_{|π|≥2} C_{|π|}(1 + m)^{A_{|π|}}·Π_B C̄_{|B|}(1 + m)^{B_{|B|}}.

   - The exponent is γ + max_{|π|=j≥2}(A_j + Σ_B B_{|B|}).

3. **Exponent.**
   - With b := 7α + 1, A_j = s(j − 1) + α and B_m = b(m − 1) + γ, a partition into j blocks gives

     γ + A_j + ΣB = b(ℓ − 1) + γ − [(b − s)(j − 1) − α − jγ].

   - The bracket is ≥ 0 iff b ≥ s + γ + (α + γ)/(j − 1). For j ≥ 2 this is at most s + 2γ + α = 7α + 1 = b.
   - So B_ℓ = b(ℓ − 1) + γ works. ∎

Exponent recursion: gate E2. Control N3 (slope 7α) fails at j = 2.

**Corollary B′ (segments; reviewer's point 2).**
- Setting: as in the induction of Proposition B, with 0 < |x| ≤ ρ₁ and y_n = F^n x.
- Claim: the closed segment [G(y_n), F(y_n)] lies in G^{n+1}(B(p_n, s₀/2)) ⊂ G^{n+1}(O).
- Consequence: Lemma B with m = n + 1 bounds every D^ℓΓ_{n+1} at every point of that segment.

*Proof.*
- The D2 ball B(G(y_n), s₀/(2Λ_{n+1})) is convex.
- It contains both endpoints, because |F(y_n) − G(y_n)| ≤ δ_n < s₀/(2Λ_{n+1}) (Proposition B, induction step 3).
- It is contained in G^{n+1}(B(p_n, s₀/2)). ∎

## 4. Lemma C — the composites p_n = Γ_n∘F^n on a common neighbourhood

`[THM — SESSION]`

**Common domain.**
- W_n := {w ∈ O : F^n(w) ∈ G^n(O)} is open, and p_n = Γ_n∘F^n is C^∞ on W_n.
- Claim: B̄(0, ρ₁) ⊂ W_n for every n.
  - For 0 < |x| ≤ ρ₁, Proposition B gives F^n x = G^n p_n(x) with p_n(x) ∈ U_x ⊂ O.
  - For x = 0, F^n(0) = 0 = G^n(0).
- Hence all p_n are C^∞ on one open set containing B̄(0, ρ₁). All partitions in (FdB) below are evaluated in this set (reviewer's point 3):
  - D^jΓ_n is evaluated at F^n x ∈ G^n(O) (Lemma B);
  - D^{|B|}F^n is evaluated at x ∈ B̄₃ (Lemma A).

**Lemma C.** For every ℓ ≥ 1 there is Ĉ_ℓ such that, for x ∈ B̄(0, ρ₁) and n ≥ 0:

  ‖D^ℓp_n(x)‖ ≤ Ĉ_ℓ(1 + n)^{P_ℓ},  P_ℓ := (7α + 1)(ℓ − 1) + (ℓ + 2)α.

*Proof.*
1. By (FdB), ‖D^ℓp_n(x)‖ ≤ Σ_π C̄_{|π|}(1 + n)^{B_{|π|}}·Π_B C_{|B|}(1 + n)^{A_{|B|}}.
2. The exponent for |π| = j is b(j − 1) + γ + s(ℓ − j) + jα. This is increasing in j (b − s + α > 0), so the maximum is at j = ℓ, giving P_ℓ. ∎

Exponent: gate E3. Control N4 (one α short) fails.

**What Lemma C does not give.**
- It does not give convergence of p_n in C^ℓ: the bounds grow polynomially in n.
- Convergence must come from the telescoping difference p_{n+1} − p_n = Γ_{n+1}∘F∘F^n − Γ_{n+1}∘G∘F^n. Its flat factor (F − G)(F^n x) and that factor's derivatives decay like n^{−(N−ℓ)/2} uniformly in x, by (H3) at derivative level and §0. That is P3-b/P3-c.

## 5. Outlook for P3-b / P3-c

`[HEUR]` — not claimed.

**P3-b (derivative flatness).**
- ‖D^j(F − G)(w)‖ ≤ c_{N,j}|w|^{N−j} on B̄₃ for every N and j.
- This is Taylor's theorem applied to F − G, whose ∞-jet at 0 vanishes. It will be written out with constants.

**P3-c (summable telescoping).**
- Write p_{n+1} − p_n = ∫₀¹ DΓ_{n+1}(G y_n + t(F − G)y_n)·(F − G)(y_n) dt, with y_n = F^n x.
- This uses Γ_{n+1}(G y_n) = p_n, valid because G y_n = G^{n+1}p_n with p_n ∈ O.
- By Corollary B′ the segment lies in the domain of Γ_{n+1} for **every** x ∈ B̄(0, ρ₁). The representation therefore holds identically on the open ball B(0, ρ₁) and can be differentiated in x there; no perturbation argument is needed.
- Differentiate ℓ times in x with (FdB). Each term is a product of:
  - a Lemma B factor, (1 + n)^{B_{·}};
  - Lemma A factors, (1 + n)^{A_{·}};
  - one P3-b factor ≲ |y_n|^{N−j} ≤ (an)^{−(N−j)/2}.
- For each k, choosing N > 2(max exponent + 1) + k makes Σ_n ‖p_{n+1} − p_n‖_{C^k(B̄(0,ρ₁))} finite.
- **One neighbourhood for all k.**
  - Fix ρ₁ once, with one N₀ > 2γ + 4 in Proposition B. The domain control (W_n ⊃ B̄(0, ρ₁), Corollary B′) uses only N₀.
  - P3-b gives derivative flatness for **every** N on all of B̄₃, without shrinking.
  - So the C^k summability for larger k uses larger N on the same ball B̄(0, ρ₁).
  - This is to be confirmed in P3-c.

## 6. Status

| Item | Status |
|---|---|
| P2-a, P2-b, Proposition C | Review accepted (SESSION) |
| §1 Observation (no uniform (1 + nQ)^A form for ℓ = 3) | `[THM — SESSION]`, with `[ALG]` gates J1–J5 |
| Lemma A, Lemma B (+ Corollary B′), Lemma C | `[THM — SESSION]` — **submitted for review** |
| P3-b | Next (routine Taylor) |
| P3-c | OPEN |
| O20-∞ (C^∞ embedding), O20-an | OPEN |

This record does not adopt any DYAD owner theorem. Adopted version: v6.4.17.
