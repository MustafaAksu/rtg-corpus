# DYAD OPEN 20 — Seed Q1–Q3 and divergence step P4: co-owner written argument

**Date:** 12 November 2026. **Author:** ChatGPT, DYAD co-owner. **Status:** SESSION / NONCANONICAL WORKING DRAFT; not a theorem, certificate, disposition or adoption. **PI instruction:** start the written arguments; do not run stage 3c-b. **Governing owner:** Dyadic v6.4.24, tag dyad-v6.4.24 (SHA-256 10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16). **Open scientific status:** B-an and B-6 ACTIVE; a nonzero jump is not certified.

**Reading extent:** targeted, not exhaustive. Read the stage-3b design §§1,3–6; the stage-3c-a proof record §§3–5,8–11; the W8 r2 hand-over §§1–8; the sectorial pilot D1–D9; the owner assessment of López-Hernanz 2012 §1; and the P1-c-5 Lemma 5b-1. Read the complete LIT use-check report at rtg-lit a3628d4 (SESSION), but not the source article, its complete proof or its Proposition 5.3. The owner's 12 November inbox disposition is a proposal in PR #254 at this checkpoint; it does not change the adopted DSN. All deductions below are SESSION, not owner-adopted.

## 1. Proof contract

Work in the pilot branch Gamma-plus with normalized coordinate xi = c z and c^3 = -ell (c = c_plus). Let xi = r exp(i theta), z = xi/c and

$$
\tau(\xi)= A_3 z^{-3}+A_2 z^{-2}+A_1 z^{-1}+\kappa\log z,
\qquad A_3=-\frac{1}{3\ell},\qquad 3 A_3c^3=1.
$$

The branches of log xi, log z and log c are the ones fixed in the stage-3b design §3 and pilot D4–D5; in particular log z = log xi - log c throughout the chosen charts.

Define theta_0 = 3 pi/8, h_0 = Re(exp(i theta_0) tau), h_1 = Re(-exp(-i theta_0) tau). Keep the design's s_0, s_1 and wall constants c_0, c_1 fixed. The domains are

$$
D_0=\{\xi\in\Omega_0:\operatorname{Re}\tau>s_0,\ h_0>c_0\},\quad
D_1=\{\xi\in\Omega_1:\operatorname{Re}\tau<s_1,\ h_1>c_1\},
$$

with Omega_0 angles (-pi/5, 3pi/10), Omega_1 angles (3pi/100, pi/2), and 0<r<0.60. Write D_j(H) = D_j intersect {h_j>H} for H greater than the corresponding wall constant; H is a nested-level parameter, not the original c_1.

For each j let u_j denote the published sectorial invariant graph in the straight sector S_j of pilot D7 (with the D5 rotation for j=1). The seed Q is the restriction of u_j to D_j(H), written as a normal deviation d_j from the common formal truncation phi_N of degree N=40.

**Conditional inputs:** (L1) the uniform finite-order asymptotic statement on closed inner subsectors, conditional on the LH2012 Theorem 4.2(1) and Proposition 5.3 as read and on the LIT propagation check C3; (L3) uniqueness among invariant graphs in the Hakim class on sufficiently small petals C1/C2; and the previously specified pointwise hypotheses (G), (A), (B) of the tube lemma. The numerical W1–W8 development outputs do not promote any of those hypotheses to a certificate.

## 2. [SESSION/ALG] Q1 — a quantitative angular inclusion criterion

For r<1, define the explicit monotone upper function (take 0<r<=exp(-1))

$$
E(r)=3|A_2c^2|r+3|A_1c|r^2+
3|\kappa|r^3\bigl(|\log r|+|\log c|+\pi/2\bigr).
$$

Indeed, by the exact leading-coefficient identity,

$$
3\xi^3\tau(\xi)=1+3A_2c^2\xi+3A_1c\xi^2+
3\kappa\xi^3(\log\xi-\log c).
$$

Thus |3 xi^3 tau(xi)-1| <= E(r) on the union of the two chart sectors. Equivalently, for xi=r exp(i theta),

$$
\left|3r^3\operatorname{Re}\tau(\xi)-\cos(3\theta)\right|\le E(r).
\tag{Q1.1}
$$

Let S=max(|s_0|,|s_1|). Choose any radius r_0 with 0<r_0<=exp(-1), r_0<0.60 and

$$
E(r_0)+3S r_0^3<\sin(\pi/8).
\tag{Q1.2}
$$

This is an explicit finite inequality involving the four fixed coefficients and two fixed wall constants; because E(r)->0 it is satisfiable for some r_0>0. For every 0<r<=r_0, (Q1.2) follows by monotonicity of r, r^2 and r^3|log r| in that range.

**Forward sector (j=0).** The straight sector S_0 requires |theta|<=5pi/24. The lower angle bound is automatic because Omega_0 has theta> -pi/5 > -5pi/24. For theta>=5pi/24 within Omega_0, cos(3theta)<=cos(5pi/8)=-sin(pi/8). By (Q1.1) and (Q1.2),

$$
3r^3\operatorname{Re}\tau\le-\sin(\pi/8)+E(r)
<-3|s_0|r^3\le 3s_0r^3,
$$

contrary to Re tau>s_0. Hence D_0 intersect {r<=r_0} lies strictly inside the angular part of S_0.

**Inverse sector (j=1).** Here S_1 is centered at pi/3 with half-width 5pi/24; its upper bound is automatic since Omega_1 has theta<pi/2<13pi/24. Outside the lower bound theta>=pi/8, one would have theta<=pi/8 and cos(3theta)>=cos(3pi/8)=sin(pi/8). Then

$$
3r^3\operatorname{Re}\tau\ge\sin(\pi/8)-E(r)
>3|s_1|r^3\ge3s_1r^3,
$$

contrary to Re tau<s_1. So D_1 intersect {r<=r_0} lies strictly inside S_1's angular window.

**Radial petal size and an explicit level H.** The straight sectors of pilot D7 also require r^3 < k_delta delta, where k_delta=2 cos(3pi/8) and delta>0 is any allowed sufficiently small LH2012 petal parameter. Narrow r_0 further to r_0<(k_delta delta)^(1/3), if necessary. To exclude all xi with r>=r_0, bound tau on the closed annulus r_0<=r<=0.60 and both chart closures by

$$
M(r_0)=\frac1{3r_0^3}+\frac{|A_2c^2|}{r_0^2}
+\frac{|A_1c|}{r_0}
+|\kappa|\bigl(|\log r_0|+|\log c|+\pi/2\bigr).
\tag{Q1.3}
$$

Then |h_j|<=|tau|<=M(r_0) there. Choose H_seed>max(c_0,c_1,M(r_0)). This gives

$$
D_j(H_{\rm seed})\subset\{0<r<r_0\}\cap S_j
\subset\Delta_j(\delta),\qquad j=0,1.
\tag{Q1.4}
$$

The domains D_j(H_seed) are nonempty: on the bisector theta=j pi/3, both defining wedge inequalities and h_j->+infinity hold near 0, since the leading term of tau is (-1)^j/(3r^3). Thus Q1 has a written *conditional, explicitly checkable* proof. The original numeric stage-3b certificate does **not** yet include interval-evaluated (Q1.2), coefficient bounds or a selected H_seed.

**Convenient proposed numerical precheck (NOT CERTIFIED):** bounds |3A_2c^2|<=2, |3A_1c|<=2, 3|kappa|<=10, |log c|<=3 and S<=4 are consistent with the source's displayed approximations. If separately established with outward-rounded exact/ball arithmetic, r_0=10^-3 satisfies (Q1.2) with ample margin (and can still be reduced to the article's delta). These bounds are an acceptance test for future verification, not premises claimed to have been certified here.

## 3. [SESSION/THM, conditional] Q2 — literature curve enters the tube

Fix an r_0 satisfying Q1. Set C_tau>0 such that |tau(xi)|<=C_tau r^-3 for 0<r<=r_0 in the sectors. Such a bound follows directly from the four displayed terms in tau (an explicit possible C_tau is 1/3+|A_2c^2|r_0+|A_1c|r_0^2+|kappa|r_0^3(|log r_0|+|log c|+pi/2)). Set

$$
C_B=C_\tau+(1+S)r_0^3,\qquad
K=\varepsilon_{\rm tube}e^{-|\operatorname{Im}\alpha|\pi/2}
  C_B^{-3} C_\tau^{-3}>0.
$$

On D_j, the two positive tube-base factors are at most C_B r^-3 and C_tau r^-3. With q_1=q_2=9, the tube radii of design §3 therefore obey

$$
R_j(\xi)\ge K\,r^{\operatorname{Re}\alpha+18}
=K\,r^{240/19},\quad \operatorname{Re}\alpha=-102/19.
\tag{Q2.1}
$$

Because Q1 places D_j(H_seed) inside one closed inner subsector of its LH2012 petal, the conditional L1 statement gives, for a finite constant C_j and all sufficiently small r there,

$$
|d_j(\xi)|=\left|\frac{\phi_j(z)-\phi_{40}(z)}{z^2}\right|
\le C_j r^{39}.
\tag{Q2.2}
$$

No numerical value of C_j is required: it is the finite-order, uniform asymptotic constant for that subsector. Divide:

$$
\frac{|d_j(\xi)|}{R_j(\xi)}
\le\frac{C_j}{K}r^{39-240/19}
=\frac{C_j}{K}r^{501/19}\longrightarrow0.
\tag{Q2.3}
$$

Narrow the seed radius to r_1<=r_0 so that (C_j/K)r_1^(501/19)<1 for both j, then increase H_seed using (Q1.3) with r_1. The published curves lie **strictly** inside their respective tubes on D_j(H_seed). This establishes Q2 *conditional on L1/C3*, not as a proof of the unpublished constants or the article's Proposition 5.3.

## 4. [SESSION/THM, conditional] Q3 — restricted-graph invariance

The selected u_0 is an invariant graph of F on its petal, and u_1 an invariant graph of the declared branch G=F^(-1), expressed in the D5-rotated coordinate and transported to the common xi coordinate. For each point of the graph over D_j(H_seed), Q2 makes it a point of the applicable tube; (G), (A1) and (A2) then give

$$
\xi'\in D_j(h_j(\tau(\xi))+\sigma)
\subset D_j(H_{\rm seed}).
$$

Thus the image of the *restricted selected graph* is again a point of the same graph on D_j(H_seed), in the domain where the source graph is defined. This is exactly the invariance required of seed (Q). It does not assert invariance of a literal straight sector in isolation; the published curves live on the curved LH2012 petals.

**Seed verdict:** Q1 follows from one explicit coefficient inequality and the petal size; Q2 follows under L1/C3; Q3 follows under the design's (G),(A) and the source invariance. The seed is not unconditional until the required estimates and imported assumptions are discharged at the declared evidence level.

## 5. [SESSION/THM, conditional] P4 — a nonzero point jump implies divergence

**Hypotheses.** Assume (i) the seed and tube-extension lemma provide analytic sectorial graphs phi_0, phi_1 on D_0,D_1, identified with the published curves on the seed domains; (ii) the common arc gamma:[t_*,infinity)->D_0 intersect D_1 of stage-3b §5 and W5 has a connected open neighbourhood U inside D_0 intersect D_1, approaches xi=0 and arg xi -> pi/6; (iii) at xi_* the values of the two graphs are contained in disjoint rigorously certified discs in the *same* d-coordinate; and (iv) the small-petal uniqueness L3/C1/C2 of LH2012, as checked by LIT at SESSION scope, applies to F and to G in the D5 chart.

**Claim.** Under (i)–(iv), the formal branch Gamma-plus does not converge.

**Proof.** Suppose instead that Gamma-plus has a convergent representative phi(z) at z=0. Its normalized graph Y=S(xi) has S(xi)=O(xi^2) because the constant and linear terms have been removed and m=2 (pilot D3). Analyticity of the map and formal invariance imply exact analytic graph invariance as germs for both F and its local inverse G. For a sufficiently small delta, on each applicable curved petal S is holomorphic and satisfies |S(xi)|<=|xi| and |S'(xi)|<=1. It is a parabolic invariant graph in the LH2012 class. By L3/C1/C2, its restriction is u_0 in the forward petal and u_1 in the rotated inverse petal.

For large t the arc gamma(t) lies in the small straight sectors around 0 and pi/3: its angular distance pi/6 to either bisector is strictly less than 5pi/24, and its radius tends to 0. Pilot D7 puts those sectors into *every sufficiently small permitted* curved petal. By the seed identities, phi_0=phi=phi_1 on a nonempty open neighbourhood of a large-t tail point inside U. Both functions are holomorphic on the connected U, hence the identity theorem makes phi_0=phi_1 on U. In particular phi_0(xi_*)=phi_1(xi_*), contradicting the disjoint-disc condition (iii). QED.

**Consequences at their inherited grades.** The unique other formal branch Gamma-minus also diverges because the analytic local diffeomorphism T exchanges the two formal branches (pilot D1 / owner assessment). Under P1-c-5 Lemma 5b-1 (SESSION), convergence of the formal vector field X-hat=log F would imply convergence of both invariant curves, so divergence of Gamma-plus implies divergence of X-hat. **Neither inference excludes convergent canonical roots F^(1/2) or F^(1/6): B-an and B-6 remain OPEN.** A nonzero jump at one point does not prove any first Fourier harmonic (INF-016 remains a deferred, distinct question).

The proof uses equality on the *small petal itself*; no identity-theorem continuation of u_j along an entire large petal is needed. The only identity-theorem continuation used is the equality of phi_0 and phi_1 across U, which is essential.

## 6. Outstanding obligations and acceptance criteria

1. **Quantified Q1:** retrieve exact coefficient enclosures for A_2, A_1, kappa, c, tau(xi_*), s_0,s_1 and choose a radius r_0 satisfying (Q1.2). Record a rigorous numerical or symbolic bound, not a floating-point display. Ensure the petal parameter delta is treated existentially and that H_seed can be selected after delta, with no unproved uniformity in delta.
2. **Literature L1/C3:** the owner has read and accepted LIT's use-check at SESSION scope (PR #254); LIT has not re-proved LH2012 Proposition 5.3. A future theorem-grade import must carry that source limitation. The uniform-asymptotics constant C_j is existential; a numeric value is not needed for the logical existence of H_seed.
3. **Q3:** prove that the D5 inverse branch is the same branch used for u_1 on the chosen overlap, preserving the chart and the selected graph. The stage-3c-a proof record §4.3 provides the proposed inverse-branch derivation; its numerical gates remain development outputs.
4. **Tube lemma:** the analytic extension and Rouché step in the stage-3c-a proof record §5 use (G),(A),(B). Their W3–W8 results are development checks, not certification, and should not be described as a completed theorem application.
5. **P4:** retain the explicit hypotheses (i)–(iv) at every point of use. A nonzero point jump and its raw-variable transport require a *separately authorized* 3c-b run, recorded hashes, independent replay and scientific review. W8's tail-threshold correction using the upper bound of |A_3| also remains a prerequisite.
6. **Status:** do not edit the Dyadic canonical DSN or claim OPEN 20/B-an/B-6 closure from this draft. The science may be promoted only through a later owner review and PI authorization.

**Suggested next scoped owner step:** turn (Q1.2) and (Q1.3) into a small exact/ball-arithmetic check against the frozen coefficient package, and separately review the conditional P4 lemma. This is a written-argument task, not stage 3c-b.
