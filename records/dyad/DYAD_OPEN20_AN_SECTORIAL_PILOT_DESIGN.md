# DYAD OPEN 20 (analytic branch) — written design of a sectorial pilot for one formal branch

**Date:** 23 October 2026 (revised the same day after the receiving review `records/dyad/DYAD_LH2012_PILOT_RECEIVING_REVIEW.md`: P-R3 domains, P-R4 inverse branch and full-map quotients, the §6 bookkeeping guards). **From:** Dyadic DSN owner (Claude). **Status:** working record (SESSION). It is a written design; stage 1 (exact preparation, §7) is complete and stage 2 (limited `[NUM]` scouting, §5 item 2) has been run. No sectorial sum, jump or Stokes quantity has been computed.

**Authority:** receiving review `records/dyad/DYAD_LH2012_RECEIVING_REVIEW.md` §6 ("WRITTEN PILOT DESIGN SUPPORTED"), on `records/dyad/DYAD_OPEN20_AN_LH2012_OWNER_ASSESSMENT.md`.

**Governing edition:** DYAD v6.4.22. OPEN 20 B-an and B-6 are ACTIVE.

**Notation:**
- $F=T^6$ in the complexified raw frame $z=\rho+\omega\eta$, $w=\rho+\bar\omega\eta$ ($z=W$). This $z$ is not the normalized NF coordinate.
- $\mu,c_{40},d_{31},C,A,B,\ell,\alpha$ are as in the owner assessment.
- [L12] = López-Hernanz, ETDS 32 (2012) 211–221.

**Goal of the pilot.** Produce, for one formal branch, a certified enclosure of one sectorial jump $\Delta_{\sigma,j}(z_*)$ at one nonzero point, or report that the enclosure contains 0.
- An enclosure that excludes 0 proves that the branch diverges. By Lemma 5b-1 (P1-c-5) it then also proves that $\log F$ diverges.
- An enclosure that contains 0 decides nothing.
- Neither outcome decides B-an or B-6.

## 1. Branch, coordinates and normalization

**D1. Branch.** The leading coefficients are the two roots of $P(a)=Aa^2+Ba+C$, whose discriminant is $B^2-4AC=\tfrac{1277}{4320}+\tfrac{281\sqrt3}{12960}i$. The pilot uses the root with $\operatorname{Im}a>0$ and calls it $a_{\rm pil}$:
- $a_{\rm pil}=(-B-\sqrt{\Delta})/(2A)\approx0.0256752224+0.1484934467\,i$ (principal square root);
- the other root is $(-B+\sqrt{\Delta})/(2A)\approx0.0576581110-0.0041558794\,i$.

**Crosswalk.** $a_{\rm pil}$ is the root called $a_2^-$ in P1-c (`DYAD_OPEN20_ANALYTIC_ROOTS_P1C_SESSION_v0_1.md` §2) and $a_+$ in the LH2012 owner assessment and in the earlier text of this design. No historical label is changed; below, $a_+$ means $a_{\rm pil}$.

The sign of $\operatorname{Im}a$ isolates the branch. Stage 1 certifies it with interval arithmetic on the real and imaginary parts of the exact radical (gate S1).

One branch suffices for a convergence/divergence decision, because $T(\Gamma_+)=\Gamma_-$ (owner assessment §1). It does not make the jumps of the two branches identical.

**D2. Lifted chart.** Use $(z,w)=(x,\,x^2(a_++y))$. The lifted map is analytic:

$$x'=x+x^4G(x,a_++y),\qquad y'=\frac{a_++y+x^3H(x,a_++y)}{(1+x^3G(x,a_++y))^2}-a_+.$$

Here $G$ and $H$ are quotients of the **full analytic map**, $G(x,u)=(F_z(x,x^2u)-x)/x^4$ and $H(x,u)=(F_w(x,x^2u)-x^2u)/x^5$, with their removable extensions at $x=0$. The finite jets certify the divisibility and the normalization coefficients (stage 1); they do not stand in for the remainders. Since $T$ is entire, $F$ and the lifted map are analytic on any bounded polydisc where $1+x^3G\neq0$; the pilot certifies a lower bound for $|1+x^3G|$ on its domain (E2).

**D3. Strict-transform jet and $m$.** The strict transform of $\Gamma_+$ is $y=\sum_{n\ge1}b_nx^n$ with $b_1=a_{3,+}$, the $z^3$ coefficient of $\hat\phi_+$; numerically $a_{3,+}\approx-0.0378863102-0.0333746170\,i$.
- Put $Y=y-b_1x$. Then $m(F;\xi,Y)\ge2$, and $m>1+\operatorname{Re}\alpha$ holds because $\operatorname{Re}\alpha=-102/19$.
- Stage 1 computes $b_1$ exactly in $E=\mathbb Q(i\sqrt3)[a]/(P)$ from the order-$z^6$ graph equation $\ell(k^*-3)a_3=R_3$ (P1-c): $b_1=(1-i\sqrt3)\bigl(\tfrac1{108}-\tfrac{a}{6}\bigr)$, and $b_2=a_4\neq0$, so $m=2$ (§7).
- **Coefficient field.** $a_{\rm pil}$ and the unscaled $b_n$ lie in $E$. After the horizontal scaling the normalized coefficients lie in $E(c_+)=E[c]/(c^3+\ell_+)$; stage 1 carries them there. Membership $c_+\in E$ is not claimed.

**D4. Horizontal normalization.** $\ell_+=c_{40}+\mu a_+\approx0.0961278516-0.0196970021\,i$, so $\arg(-\ell_+)\approx0.935667\pi$.
- Choose $c_+$ as the principal cube root of $-\ell_+$: $c_+\approx0.2569865579+0.3830143552\,i$, with $\arg c_+\approx0.311889\pi$.
- Put $\xi=c_+x$. All normalized coefficients are elements of $E(c_+)$.
- Then $F_1=\xi-\xi^4+O(\xi^4Y,\xi^5)$ and $F_2=Y-\alpha\xi^3Y+O(\xi^3Y^2,\xi^4Y)+\xi^{3+m}\psi(\xi)$, which is [L12] Definition 4.1 with $k=3$.

**D5. Inverse map.** $F^{-1}$ has $\xi\mapsto\xi+\xi^4+\dots$. With $\tilde\xi=\rho\xi$, $\rho^3=-1$ ($\rho=e^{i\pi/3}$), we get $\tilde\xi\mapsto\tilde\xi-\tilde\xi^4+\dots$ and the same $\alpha$ and $m$. This is the normalized form for the repelling petals; stage 1 checks it exactly on the formal inverse (gate S5). **Transport (odd $j$):** a function $\tilde u(\tilde\xi)$ computed in the $\tilde\xi$ coordinate is pulled back to $\xi$, $u(\xi)=\tilde u(\rho\xi)$, before it enters the common raw-$z$ formula of D9. The inverse-map coordinate is never mixed with the forward coordinate in a point evaluation.

## 2. Cover, overlaps and inclusion in the Hakim domains

**D6. Petals.** Take $\eta=\pi/4$.
- $F$ has petals bisected by $\arg\xi=0,\,2\pi/3,\,4\pi/3$, i.e. by $\xi^3\in\mathbb R^+$.
- $F^{-1}$ has petals bisected by $\arg\xi=\pi/3,\,\pi,\,5\pi/3$.
- Each petal has asymptotic half-opening $(\pi-\eta)/3=\pi/4$.
- The six candidate singular directions are $\arg\xi=\pi/6+j\pi/3$. In raw $z$ they are $\arg z\approx(-0.145222+j/3)\pi$, $j=0,\dots,5$.

**D7. Straight sectors inside the petals.** Let $S_j=\{0<|\xi|^3<\kappa\delta,\ |\arg\xi-j\pi/3|\le5\pi/24\}$ with $\kappa=2\cos(3\pi/8)\approx0.7654$.

*Inclusion.* With $\theta$ ranging over $[-(\pi/2-\eta),\pi/2-\eta]$, the union of the discs $D(\delta e^{i\theta},\delta)$ contains every point $re^{i\psi}$ with $|\psi|\le\pi-\eta$ and $r<2\delta\cos(|\psi|-(\pi/2-\eta))$. Apply this to $\xi^3$ with $|\psi|\le5\pi/8$, so $|\psi|-(\pi/2-\eta)\le3\pi/8$; this gives $S_0\subset\Delta^3_{\pi/4,\delta}$. The other $S_j$ follow by rotation, using the $\tilde\xi$ coordinate of D5 for odd $j$.

So the template of the receiving review is contained in the true Hakim domains for every $\delta\le\delta_0$, without replacing their dynamics. $\delta_0$ itself is fixed in §4.

Adjacent $S_j,S_{j+1}$ overlap in an angular window of width $\pi/12$ centered on the singular direction $\pi/6+j\pi/3$; this includes $S_5\cap S_0$. The comparison point $z_*$ lies in such an overlap, and the jump is evaluated after both sums are pushed back to the same raw $z$ (D9).

## 3. Selected functions and branches

**D8. Selected sums.** Let $\Delta_j$ be the component of the [L12] domain $\Delta^3_{\eta,\delta}$ that contains $S_j$ (for odd $j$, the domain of the rotated inverse map in the $\tilde\xi$ coordinate). The selected function is the fixed point of Hakim's operator ([L12] §4) **on the curved domain $\Delta_j$**, for $F$ ($j$ even) or $F^{-1}$ ($j$ odd), in the class
$$\mathcal H_{\Delta_j}=\{u\in\mathcal O(\Delta_j):\ |u(\xi)|\le|\xi|^{m-1},\ |u'(\xi)|\le|\xi|^{m-2}\},$$
with the weighted norm $\|u\|=\sup_{\Delta_j}|u(\xi)|/|\xi|^{m-1}$. By [L12] Theorem 4.2(3) it is unique in this class, and by Corollary 5.2 it is the 3-sum of $\hat Y$ in that direction. The straight sectors $S_j$ of D7 serve only to compare the selected sums; orbits may leave $S_j$, and what the operator needs is $f_u(\Delta_j)\subset\Delta_j$ (E3). This is the domain convention of [L12] §4; a straight sector is not forward-invariant even for the model map $\xi-\xi^4$ (the receiving review gives a rational counterexample).

The factor $\xi^\alpha$ and the ratio $x_0^\alpha/x_n^\alpha$ in the operator use the branch of $\log\xi$ continuous on the petal, with its cut outside the petal. Its value is fixed by $\log(e^{ij\pi/3}r)=\ln r+ij\pi/3$ on the bisector. The operator depends only on ratios along an orbit inside one petal, so the choice cancels; it is fixed only to make the computation reproducible.

**D9. Comparison in raw $z$.** For each sum $u_j$, form $\phi_j(z)=z^2\bigl(a_++b_1z+u_j(c_+z)\bigr)$ in the raw chart, on the common raw sector $c_+^{-1}(S_j\cap S_{j+1})$. Then
$$\Delta_{+,j}(z_*)=\phi_{j+1}(z_*)-\phi_j(z_*).$$
Never compare $\phi_+$ with $\phi_-$: they differ at order $z^2$.

**D10. Symmetry reduction (SESSION derivation; to be checked in the receiving review of this design).**
- $T^2$ maps $\Gamma_+$ to itself, because $T$ exchanges the two branches.
- Its linear part rotates $z$ by $\lambda^2=e^{2\pi i/3}$.
- The image of the 3-sum in direction $d$ is analytic on a sector around $d+2\pi/3$ of opening $>\pi/3$, deformed only at $O(z^2)$, and is Gevrey-1/3 asymptotic to the same formal series. By uniqueness of 3-sums (Watson's lemma) it is the 3-sum in direction $d+2\pi/3$.

So the jump on overlap $j$ vanishes if and only if the jump on overlap $j+2$ does. The six overlaps of one branch fall into two $T^2$-classes, even and odd $j$. This does not identify the two classes and does not reduce them to one scalar.

The pilot needs one overlap for a divergence certificate. A convergence statement would need analytic gluing on all six overlaps; numerically that is unreachable.

## 4. Certifiable error budget

All quantities are enclosed with interval arithmetic: `python-flint` `arb`/`acb` at stated precision, or `mpmath.iv` as fallback. Floating-point values serve only for scouting.

| Item | What is bounded | How |
|---|---|---|
| E1 map | $F$ on a polydisc of radius $r_0$: Cauchy bounds for the remainders after the normalized leading terms. **Separately**, a single-valued controlled branch of $F^{-1}$ on the region used by the odd sectors | $F$: $T$ is entire, so interval evaluation of the six-fold composition on the polydisc with Cauchy estimates. $F^{-1}$: entireness gives nothing; write $F(v)=v+R(v)$ and certify that $v\mapsto w-R(v)$ maps a stated polydisc into itself and contracts there, with explicit derivative bounds. The formal inverse jet of stage 1 does not discharge this |
| E2 blow-up | $\inf|1+x^3G|>0$ and bounds for $G,H$ on $|x|\le x_0$, $|y|\le y_0$ | interval evaluation of the exact quotients |
| E3 orbit control | uniform invariance $f_u(\Delta_j)\subset\Delta_j$ of the **curved** domain for all $u\in\mathcal H_{\Delta_j}$, and $|f_u^n(\xi)|^3\le C|\xi|^3/(1+n|\xi|^3)$ with explicit $C$, $\delta_0$; orbits are not required to stay in $S_j$ | explicit Leau–Fatou estimates for $\xi-\xi^4+$ (bounded perturbation) on $\Delta_j$, following [L12] §4 and Lemma 4.4 with every constant written out |
| E4 contraction | $\|Tu-Tv\|\le L\|u-v\|$ on $\mathcal H_{\Delta_j}$ with $L<1$, and $T(\mathcal H_{\Delta_j})\subset\mathcal H_{\Delta_j}$, in the weighted norm | constants $B,B'$ of [L12] §4 made explicit from E1–E3 |
| E5 tail | the orbit sum truncated at $N$ terms, in the weighted norm and including the factor $x_0^\alpha/x_n^\alpha$ | $\sum_{n\ge N}|x_n|^{s}\le C_s(N)$ from E3, with $|x_0^\alpha/x_n^\alpha|$ bounded through $\operatorname{Re}\alpha$ and $\operatorname{Im}\alpha\cdot\arg$ |
| E6 approximation | a numerical approximation $\tilde u$ (a polynomial in $\xi$ or a Chebyshev model on $\Delta_j$) that belongs to $\mathcal H_{\Delta_j}$ or to an explicitly validated contraction neighbourhood | a posteriori fixed-point bound $\|u-\tilde u\|\le\|T\tilde u-\tilde u\|/(1-L)$ in the weighted norm |
| E7 transport | the map back to raw $z$ (D9), and the coordinate change of D3–D5 | exact coefficients; interval evaluation |

Only the article's qualitative existence of these constants is available; every constant must be produced by the pilot. If E3 or E4 cannot be closed with $L<1$ for some $\delta_0>0$, the pilot reports that and stops.

## 5. Stages and decision rule

1. **Exact preparation (small).** $b_1$, $m$ and the normalized forward and inverse jets of D3–D5, exact in $E(c_+)$, with a checker and negative controls. **Done; see §7.** It is exact preparation only, not an inverse-domain or remainder certificate.
2. **Scouting (non-rigorous).**
   - Estimate the jump scale $e^{-A/|z|^3}$ from the growth of the coefficients of $\hat\phi_+$; P1-c computed many of them. Use a Borel-plane singularity estimate.
   - From it, choose $|z_*|$ so that the expected jump exceeds the achievable error budget while $z_*$ stays inside the overlap region $S_j\cap S_{j+1}$ of two sums of the same branch (not merely inside the union of the sectors). Until a certified admissible radius exists, $z_*$ is a candidate, not a point known to lie in $\Delta_j\cap\Delta_{j+1}$.
   - The result of this stage is an estimate only, recorded as `[NUM]` with its provenance (commands, outputs, hashes); it is not theorem/certificate evidence. **Done at the limited scope cleared by the J1 closeout review; see `records/dyad/DYAD_OPEN20_AN_STAGE2_SCOUTING_NUM.md`.**
3. **Certification (heavier; on the PI's machine if needed).** E1–E7 for two adjacent sectors around one singular direction, then an enclosure of $\Delta_{+,j}(z_*)$.
   - It is delivered as a script with a fixed command, its JSON output with hashes, and negative controls (wrong branch, wrong log branch, perturbed $\alpha$).
4. **Decision.**
   - An enclosure excluding 0 proves the branch diverges and $\log F$ diverges. It is recorded as a SESSION result for review. It does not settle B-an or B-6.
   - An enclosure containing 0 is inconclusive and recorded as such.
   - No convergence claim can come from this pilot.

## 6. Guards

- **Real slice.** The complex sectorial curves have no nonzero real-slice points near 0. Real PRIM-CTR or L-PHASE constants are not reused.
- **Truncations.** The formal object is the full series. No finite truncation is identified with a sum.
- **Prior results.** Prior SESSION results keep their custody.
- **No change** to the DSN, RIDs, OPEN statuses or notices.
- **Status of the stages:** stage 1 is complete (§7; accepted by `records/dyad/DYAD_LH2012_STAGE1_J1_CLOSEOUT_REVIEW.md`); stage 2 was cleared at receiving-review scope by the same review and by the PI's decision of 23 October 2026 and has been run (§5 item 2); stage 3 is not authorized and waits for a separate decision after its analytic bounds (E1–E6) are available.

## 7. Stage 1 — exact preparation (done, 23 October 2026; OWNER-RUN; corrected the same day)

`evidence/dyad/scripts/dyad_open20_an_stage1_prep.py` (SHA-256 `5c22ff7aab5d9dabdf243bfc6e279616b4fdbc5ea9d8429fa513c3b2584d8568`; output `evidence/dyad/open20-an/stage1_prep.json`, byte-deterministic).

**Correction J1** (stage-1 receiving review `records/dyad/DYAD_LH2012_STAGE1_RECEIVING_REVIEW.md`). The first version (`c3c11054…2cc4`, commit `272d273`) truncated the raw jets at $w$-degree 2 **before** substituting $w=x^2(a+y)$. The raw $w$-degree and the lifted $y$-degree are different truncation orders: the term $d_{13}zw^3$ with $d_{13}=[F_w]_{1,3}=-\tfrac16+\tfrac{2i\sqrt3}9\neq0$ becomes $d_{13}x^7(a+y)^3$, which the division by $x'^2$ brings to order $x^5$, inside the kept jet. The lost part of the vertical normalized jet was $\tfrac{d_{13}}{c^5}\xi^5(a^3+3a^2Y+3aY^2)$; in particular $\psi(0)$ was wrong by $d_{13}a^3/c^5$, and S5 could not see it because it inverted the wrong jet consistently. The horizontal jet, $b_1$, $b_2$, $m$, $k$ and $\alpha$ were unaffected. The corrected script substitutes into the full degree-7 jets and truncates afterwards, and adds two gates:
- **S6**, the graph-consistency identity $\psi(0)=(\alpha-2)\,b_2/c^2$, which follows from $Y(\xi)=b_2\xi^2/c^2+O(\xi^3)$ in the normalized invariance equation at order $\xi^5$;
- **S7**, a second route: direct substitution $z=\xi/c$, $w=(\xi/c)^2(a+b_1\xi/c+Y)$ into the raw jets and division by $z'^2$ must reproduce $F_2$ coefficient by coefficient.

The negative control `--control T` restores the first version's early truncation; it fails S6 and S7 (exit 1), while S1–S5 still pass, which is the signature of the defect. Exact arithmetic in the tower $\mathbb Q(i\sqrt3)\subset E=\mathbb Q(i\sqrt3)[a]/(P)\subset E(c)=E[c]/(c^3+\ell)$, implemented directly (no symbolic engine); identities in $E$ hold for both roots at once, and only S1 selects the root. $F=T^6$ is composed to degree 7 in exact rationals in the real chart and converted to $(z,w)$. Runtime under one second.

| Gate | Content | Result |
|---|---|---|
| S1 | rigorous interval enclosures of $\operatorname{Im}a$ for both roots; $a_{\rm pil}=(-B-\sqrt\Delta)/(2A)$ has $\operatorname{Im}a>0$, the other root $<0$ | PASS |
| S2 | graph equation $F_w(z,\phi)-\phi(F_z(z,\phi))$: orders $z^0$–$z^5$ vanish in $E$; orders $z^6,z^7$ are affine in $a_3,a_4$ with $L_k=\ell(k^*-k)$ (P1-c sign convention); $b_1=a_3=(1-i\sqrt3)(\tfrac1{108}-\tfrac a6)$, $b_2=a_4\neq0$, so $m=2$ | PASS |
| S3 | lifted map: $F_z(x,x^2u)-x$ divisible by $x^4$, $F_w(x,x^2u)-x^2u$ by $x^5$; $y'-y$ has no $x^0..x^2$ terms and its $x^3Y^0$ coefficient vanishes ($P(a)=0$) | PASS |
| S4 | normalized forward map in $(\xi,Y)$: $F_1=\xi-\xi^4+O(\xi^4Y,\xi^5)$, $F_2=Y-\alpha\xi^3Y+O(\xi^3Y^2,\xi^4Y)+\xi^5\psi(\xi)$, $\psi(0)\ne0$, with $\alpha=-\tfrac{102}{19}-\tfrac{16\sqrt3}{19}i$ ($x$-order $\le5$, $Y$-degree $\le2$) | PASS |
| S5 | formal inverse to the same order: both compositions are the identity; after $\tilde\xi=\rho\xi$ it has the same Definition-4.1 form with the same $\alpha$ and $m=2$ | PASS |
| S6 | $\psi(0)=(\alpha-2)\,b_2/c^2$ (graph consistency) | PASS |
| S7 | direct-substitution route reproduces $F_2$ | PASS |

Negative controls: `--control B` ($b_1$ perturbed) fails S4, S5, S6; `--control R` ($c^3=+\ell$) fails S4, S5, S6; `--control A` ($\alpha$ altered) fails S4; `--control T` (early truncation) fails S6, S7. Each exits 1.

Exact: $b_1=(1-i\sqrt3)(\tfrac1{108}-\tfrac a6)$; $b_2=\tfrac{199}{19845}+\tfrac{2603\sqrt3}{476280}i+\bigl(-\tfrac{23}{216}+\tfrac{\sqrt3}{216}i\bigr)a$. Numerical values for the pilot root (display only): $b_1\approx-0.0378863102-0.0333746170\,i$, $b_2\approx0.0061030467-0.0061397892\,i$.

What stage 1 does **not** do: no domain, contraction, tail or inverse-branch bound (E1–E6); no sectorial sum; no jump. Stage 2 was cleared and run separately (§5 item 2, §6); stage 3 waits for a separate decision.

