# DYAD OPEN 20 / O20-∞ — P2-b: inverse-iteration domain and C⁰ flat conjugacy (proof v0.2.1)

**Version:** v0.2.1 (supersedes v0.2 `b8a1434f…19f9`; changes in §7) · **Date:** 20 October 2026 · **Author:** Dyadic DSN owner (Claude)
**Supersedes:** §3 of `DYAD_OPEN20_P1B_P2_DOMAIN_SESSION_v0_1.md` (`0ab4fab0…820c`). §1 (P1-b) and §2 (P2-a) of v0.1 stand as reviewed.
**Status:** `[SESSION]` proof record. Review of v0.2: `MATHEMATICAL ARGUMENT ACCEPTED — MINOR PROOF CORRECTIONS` (P2B-01…04 applied here). It claims **only** C⁰ results: Proposition B (C⁰ flat semi-conjugacy) and Proposition C (C⁰ flat conjugacy, from the reviewer's symmetric argument, §4). C^∞ embedding still needs P3. DYAD v6.4.17 is unchanged.
- OPEN 20 PARTIAL;
- B-∞ existence OPEN.

**Basis:** review of v0.1, `P2-a ACCEPT; P2-b PROMISING — PROOF REVISION REQUIRED`. Obligations for v0.2:
- (R1) a boundary-distance and path-continuation lemma for D2;
- (R2) uniform domain control via U_x and V_x;
- (R3) D1 uniform over the auxiliary ball;
- (R4) a proof of the summation bound;
- (R5) separate treatment of x = 0 and of the local-diffeomorphism hypotheses.

## 0. Standing hypotheses (all qualitative; ρ small)

**Coordinates.** Raw frame W ∈ ℝ² ≅ ℂ, |·| Euclidean, Q(w) = |w|².

**Maps.**
- F = T⁶.
- X_∞ is a C^∞ Borel realization of X̂ = log F.
- G = exp(X_∞) is its time-one map.

Both F and G are C^∞ near 0 and have the same ∞-jet: j^∞F = j^∞G = exp(X̂), with linear part I and no quadratic term.

Fix ρ > 0 small enough that, on the closed ball B̄₃ := B̄(0, 3ρ):

- **(H1) Local diffeomorphism.** F and G are defined and C^∞ on an open set containing B̄₃, and ‖DH(w) − I‖ ≤ c₁|w|² ≤ ½ for H ∈ {F, G}. Hence:
  - H is injective on B̄₃, because |H(u) − H(v) − (u − v)| ≤ ½|u − v| on the convex ball;
  - DH(w) is invertible, with ‖DH(w)⁻¹‖ ≤ 1 + 2c₁|w|² (Neumann series).
- **(H2) Radial decrease** (P2-a, upper side only). Q(H(w)) ≤ Q(w) − a·Q(w)² for w ∈ B̄₃, with a = ½.
  - For F this is DYAD-THM-PRIM-CTR (Q ≤ 1/400).
  - For G it follows from the common cubic jet: Q(Gw) = Q − Q² + O(|w|⁵).
  - Consequences: every ball B̄(0, r) with r ≤ 3ρ is forward-invariant, and 1/Q(H^j w) ≥ 1/Q(w) + a·j (since 1/Q′ ≥ (1/Q)(1 + aQ) = 1/Q + a).
- **(H3) Flatness.** For every N there is c_N with |F(w) − G(w)| ≤ c_N|w|^N on B̄₃.

The lower side of P2-a (1/Q ≤ 1/Q₀ + b·m) is **not** needed below.

## 1. Lemma D2 — inner radius by boundary distance (R1)

**Lemma D2.** Let O ⊂ ℝ² be open and H : O → ℝ² a C¹ map that is injective with DH invertible everywhere on O. Let B̄(p, s) ⊂ O and Λ := sup_{u ∈ B̄(p,s)} ‖DH(u)⁻¹‖ < ∞. Then:
- B(H(p), s/Λ) ⊂ H(B(p, s));
- for each y in that ball, the segment [H(p), y] lies in H(B(p, s));
- |H⁻¹(y) − p| ≤ Λ|y − H(p)|.

*Proof.*
1. **H is a diffeomorphism onto an open set.** By the inverse function theorem H is a local diffeomorphism. Being injective, H : O → H(O) is a bijective open map, hence a homeomorphism onto the open set H(O), with C¹ inverse. So H(B(p,s)) is open.
2. **Set-up of the path.** Fix y with |y − H(p)| < s/Λ and put σ(t) = H(p) + t(y − H(p)). Let T := sup{t ∈ [0,1] : σ([0,t]) ⊂ H(B(p,s))}. Then T > 0 by openness.
3. **The pulled-back path stays inside the ball.** On [0, T) the path u(t) := H⁻¹(σ(t)) ∈ B(p, s) is C¹, with |u̇| = |DH(u)⁻¹σ̇| ≤ Λ|y − H(p)|. Hence |u(t) − p| ≤ tΛ|y − H(p)| < t·s.
4. **Limit point.** u is Lipschitz, so u(T) := lim_{t↑T} u(t) exists, with |u(T) − p| ≤ TΛ|y − H(p)| < s. So u(T) ∈ B(p, s) and, by continuity, H(u(T)) = σ(T). Thus σ(T) ∈ H(B(p,s)).
5. **T = 1.** If T < 1, openness of H(B(p,s)) would extend the inclusion beyond T, contradicting the definition of T. So T = 1, and y = σ(1) = H(u(1)) with |u(1) − p| ≤ Λ|y − H(p)|. ∎

**Application** (P2B-01). Take O = B(0, 3ρ) and H = G^m:
- G(O) ⊂ O by (H2), and G is injective on O with DG invertible by (H1);
- hence G^m : O → G^m(O) is a C^∞ diffeomorphism onto an open set, for every m.

So Lemma D2 applies to every closed auxiliary ball contained in O; all balls used below lie in V̄_x ⊂ B(0, 3ρ).

## 2. Lemma D1 — uniform polynomial bound for inverse derivatives (R3)

For 0 < |x| ≤ ρ put Q₀ = |x|², s₀ = |x|/4 and
- U_x = B(x, s₀),
- V_x = B(x, 2s₀).

Every u ∈ V̄_x satisfies ½|x| ≤ |u| ≤ (3/2)|x| < 3ρ, so V̄_x ⊂ O.

**Lemma D1.** For all u ∈ V̄_x and m ≥ 0:

  ‖(DG^m(u))⁻¹‖ ≤ C₁·(1 + κ·m·Q₀)^γ,  with γ = 2c₁/a, κ = 9a/4, C₁ = exp(2c₁·(9/4)ρ²).

*Proof.*
1. (DG^m(u))⁻¹ = DG(u)⁻¹ ⋯ DG(G^{m−1}u)⁻¹, so its norm is at most Π_{j<m}(1 + 2c₁Q(G^ju)) ≤ exp(2c₁ Σ_{j<m} Q(G^ju)).
2. By (H2), Q(G^ju) ≤ 1/(A + a·j), with A := 1/Q(u) ≥ (4/9)/Q₀.
3. Σ_{j<m} 1/(A + aj) ≤ 1/A + (1/a)·log(1 + am/A) ≤ (9/4)Q₀ + (1/a)·log(1 + κmQ₀).
4. Exponentiating gives the bound. ∎

The constants depend only on c₁, a and ρ. They are uniform in x and in u ∈ V̄_x.

## 3. Proposition B — C⁰ flat semi-conjugacy (R2, R4, R5)

**Proposition B (C⁰ semi-conjugacy).** Fix N > 2γ + 4. There are ρ₁ ∈ (0, ρ] and C₃ such that, for every x with **0 < |x| ≤ ρ₁** and every n ≥ 0:
- **(i)** F^n(x) ∈ G^n(B(x, s₀/2)), so p_n(x) := (G^n)⁻¹(F^n x) is defined (unique preimage in B̄₃);
- **(ii)** the segment [G(F^n x), F(F^n x)] lies in G^{n+1}(B(p_n(x), s₀/2));
- **(iii)** |p_n(x) − x| ≤ C₃|x|^{N−2} ≤ |x|/16 < s₀/2.

Moreover:
- **(iv)** p_n → Φ_∞ uniformly on B̄(0, ρ₁). Φ_∞ is continuous, and |Φ_∞(x) − x| = O(|x|^M) for every M.
- **(v)** Φ_∞∘F = G∘Φ_∞ on B̄(0, ρ₁) (semi-conjugacy; invertibility is Proposition C).

**Case x = 0 (R5, P2B-03).** Separately: p_n(0) = Φ_∞(0) = 0 for all n. Statements (i)–(iii) are made only for 0 < |x| ≤ ρ₁.

### Summation bound (R4)

Put y_k = F^k x, δ_k := c_N|y_k|^N (take c_N > 0; if F = G the construction is the identity) and, once p_k is defined, Λ_{k+1} := sup over B̄(p_k, s₀/2) of ‖(DG^{k+1})⁻¹‖.

**Majorant defined before the induction** (P2B-02). Independently of the p_k, set β := N/2 − γ − 1 > 0 and

  b_k(x) := C₂c_N·Q₀^{N/2}·(1 + akQ₀)^{γ−N/2},  𝒮_N(x) := Σ_{k≥0} b_k(x).

The induction shows Λ_{k+1}δ_k ≤ b_k at each step; future preimages are never used to choose the radius.

- **Bound on δ_k.** By (H2) for F, |y_k|² ≤ 1/(1/Q₀ + ak). So δ_k ≤ c_N·Q₀^{N/2}·(1 + akQ₀)^{−N/2}.
- **Bound on Λ_{k+1}.** If p_k ∈ U_x then B̄(p_k, s₀/2) ⊂ V̄_x, so Lemma D1 gives Λ_{k+1} ≤ C₁(1 + κ(k+1)Q₀)^γ ≤ C₂(1 + akQ₀)^γ, with C₂ = C₁(1 + κρ²)^γ·max(1, κ/a)^γ.
- **The majorant sum.**

  𝒮_N(x) ≤ C₂c_N Q₀^{N/2}·[1 + ∫₀^∞ (1 + atQ₀)^{γ−N/2} dt] = C₂c_N Q₀^{N/2}·[1 + 1/(aβQ₀)] ≤ C₃·|x|^{N−2},  with C₃ := C₂c_N(ρ² + 1/(aβ))

  (no assumption Q₀ ≤ 1 is needed).
- **Choice of ρ₁ (strict margin).** Take ρ₁ := min(ρ, (16C₃)^{−1/(N−3)}). Then 𝒮_N(x) ≤ |x|/16 < |x|/8 = s₀/2 for 0 < |x| ≤ ρ₁.

### Induction (domains U_x and V_x, as proposed by the reviewer)

**Hypothesis I_n.** p_0,…,p_n are defined, Λ_{k+1}δ_k ≤ b_k for k < n, and |p_n − x| ≤ Σ_{k<n} b_k ≤ 𝒮_N(x) < s₀/2.

- **Base.** I₀ holds with p₀ = x.
- **Step I_n ⇒ I_{n+1}.**
  1. p_n ∈ B(x, s₀/2), so B̄(p_n, s₀/2) ⊂ B̄(x, s₀) ⊂ V̄_x.
  2. By Lemma D1 on V̄_x, Λ_{n+1} ≤ C₂(1 + anQ₀)^γ; with the bound on δ_n this gives Λ_{n+1}δ_n ≤ b_n ≤ 𝒮_N(x) < s₀/2.
  3. Apply Lemma D2 to H = G^{n+1} on B̄(p_n, s₀/2) ⊂ O with Λ = Λ_{n+1}: B(G^{n+1}p_n, s₀/(2Λ_{n+1})) ⊂ G^{n+1}(B(p_n, s₀/2)). Here G^{n+1}p_n = G(y_n) and F^{n+1}x = F(y_n), with |F(y_n) − G(y_n)| ≤ δ_n < s₀/(2Λ_{n+1}).
  4. So F^{n+1}x and the segment [G(y_n), F(y_n)] lie in G^{n+1}(B(p_n, s₀/2)). This gives (ii) and (i) for n + 1.
  5. Lemma D2 gives |p_{n+1} − p_n| ≤ Λ_{n+1}δ_n ≤ b_n, hence |p_{n+1} − x| ≤ Σ_{k≤n} b_k, i.e. I_{n+1}.
- **Uniqueness of the preimage.** p_{n+1} is the unique preimage in B̄₃, because G^{n+1} is injective there.

### Proofs of (iii)–(v)

- **(iii)** follows from I_n and 𝒮_N(x) ≤ C₃|x|^{N−2} ≤ |x|/16.
- **(iv) Uniform convergence.** For n ≥ 2, |Φ_∞(x) − p_n(x)| ≤ Σ_{k≥n} b_k ≤ (C₂c_N/(aβ))·Q₀^{N/2−1}(1 + a(n−1)Q₀)^{−β} ≤ (C₂c_Nρ₁^{2γ}/(a^{β+1}β))·(n − 1)^{−β}, independent of x (reviewer's form; the x = 0 term is zero).
  - So (p_n) is uniformly Cauchy on B̄(0, ρ₁).
  - Each p_n is continuous: it equals (G^n)⁻¹∘F^n, with (G^n)⁻¹ continuous on the open image G^n(O), O = B(0, 3ρ).
  - Hence Φ_∞ is continuous, and |Φ_∞(x) − x| ≤ C₃|x|^{N−2}.
  - p_n does not depend on N (it is the unique preimage in O). So for each M, choosing N ≥ M + 2 with N > 2γ + 4, on the corresponding ρ₁(N), gives O(|x|^M) for the same germ (P2B-03).
- **(v) Semi-conjugacy.** For x ∈ B̄(0, ρ₁), Fx ∈ B̄(0, ρ₁) by (H2).
  - Both G(p_{n+1}(x)) and p_n(Fx) lie in B̄₃ and are mapped by G^n to F^{n+1}x.
  - By injectivity, p_n(Fx) = G(p_{n+1}(x)).
  - Letting n → ∞ and using continuity of G: Φ_∞(Fx) = G(Φ_∞(x)). ∎

## 4. Proposition C — C⁰ flat conjugacy (reviewer's symmetric argument)

**Provenance.** This section records the argument derived in the external review of v0.2 (§5 of that review). It is the reviewer's SESSION derivation, written out here by the owner and checked; it was not part of v0.2.

**Proposition C.** On a neighbourhood of 0, Φ_∞ is a homeomorphism onto its image, and Φ_∞∘F∘Φ_∞⁻¹ = G (C⁰ flat conjugacy).

*Proof.*
1. **Symmetry.** (H1)–(H3) are symmetric in F and G. Proposition B with F and G exchanged gives a continuous germ Ψ_∞ = lim F^{−n}∘G^n with |Ψ_∞(x) − x| = O(|x|^M) for all M and Ψ_∞∘G = F∘Ψ_∞.
2. **Composites.** After shrinking the domains, C_F := Ψ_∞∘Φ_∞ and C_G := Φ_∞∘Ψ_∞ are defined and continuous. They are value-flat to the identity: for example |C_F(x) − x| ≤ |Ψ_∞(Φ_∞x) − Φ_∞x| + |Φ_∞x − x| = O(|x|^M), using |Φ_∞x| = O(|x|).
3. **Commutation.** C_F∘F = Ψ_∞Φ_∞F = Ψ_∞GΦ_∞ = FΨ_∞Φ_∞ = F∘C_F, and likewise C_G∘G = G∘C_G.
4. **Lemma F.**
   - For F: adopted DYAD-CAND-FLAT-CENTRALIZER (§6.17, `[THM]`) applies to C_F on a ball B_r with C_F(B_r) ⊂ B_{4r}; no regularity of C is assumed there. So C_F = id near 0.
   - For G: the same elementary proof applies verbatim, using (H1)–(H2) for G (the forward decay and the polynomial co-Lipschitz estimate). No separate owner theorem for G is imported; the argument is repeated for G.
   - So C_G = id near 0.
5. **Conclusion.** Ψ_∞∘Φ_∞ = id and Φ_∞∘Ψ_∞ = id as local germs. Hence Φ_∞ is a local homeomorphism and Φ_∞∘F∘Φ_∞⁻¹ = G. ∎

## 5. What Propositions B and C give and do not give

**They give** a C⁰ local conjugacy Φ_∞ between F and G = exp(X_∞), value-flat to the identity (|Φ_∞ − id| = O(|x|^M) for all M). Value-flatness implies DΦ_∞(0) = I at the single point 0.

**They do not give:**
- C¹ or higher regularity of Φ_∞ on a neighbourhood (the derivative at 0 alone does not allow the inverse function theorem);
- F = exp(X) with X of class C^∞ (Q∞): a vector field cannot be pulled back by derivative through a homeomorphism;
- any statement on analytic roots.

**P3 (next):**
- **P3-a:** polynomial bounds, on the controlled domain, for D^ℓF^n and D^ℓG^{−n} at every fixed ℓ (Faà di Bruno on the D1 product), keeping the D2 segments in all derivative estimates.
- **P3-b:** derivative flat estimates ‖D^ℓ(F − G)(w)‖ ≤ c_{N,ℓ}|w|^N (Taylor), replacing the value-level (H3).
- **P3-c:** Σ_n ‖p_{n+1} − p_n‖_{C^k} < ∞ on a common neighbourhood for every k, with p_{n+1} − p_n = G^{−(n+1)}∘F∘F^n − G^{−(n+1)}∘G∘F^n. This gives Φ_∞ ∈ C^∞, flat to the identity, a local C^∞ diffeomorphism (by Proposition C and DΦ_∞(0) = I with C¹ regularity), and hence F = exp(Φ_∞*X_∞).

## 6. Status

| Item | Status |
|---|---|
| P1 / P1-b | Literature: no directly applicable theorem found in accessible sources (not "none exists") |
| P2-a | Accepted (review of v0.1) |
| P2-b | Argument accepted (review of v0.2); corrections P2B-01…04 applied in v0.2.1 |
| Proposition C (C⁰ conjugacy) | Reviewer's SESSION derivation, written out in §4 |
| P3-a/b/c | Next (reviewer: may start after these corrections) |
| OPEN 20 | PARTIAL; B-∞ existence OPEN; DYAD v6.4.17 unchanged |

## 7. Changes v0.2 → v0.2.1 (review of 19 Oct 2026)

1. **P2B-01** Open domain: O = B(0, 3ρ) instead of B(0, 3ρ + ε); G(O) ⊂ O and G^m : O → G^m(O) is a diffeomorphism; auxiliary balls lie in V̄_x ⊂ O.
2. **P2B-02** Majorant b_k(x), 𝒮_N(x) defined before the induction; Λ_{k+1}δ_k ≤ b_k shown at each step; C₃ = C₂c_N(ρ² + 1/(aβ)); strict margin via ρ₁ = min(ρ, (16C₃)^{−1/(N−3)}).
3. **P2B-03** (i)–(iii) only for 0 < |x| ≤ ρ₁; x = 0 recorded separately; N ≥ M + 2 and N > 2γ + 4 for flatness of order M.
4. **P2B-04** Proposition B renamed "C⁰ flat semi-conjugacy"; invertibility moved to Proposition C (§4), the reviewer's symmetric argument with Lemma F, credited as such.
5. Uniform tail bound written in the reviewer's form.
6. **Unchanged:** Lemmas D1 and D2, the induction mechanism, the decay rates. No new numerical work.
