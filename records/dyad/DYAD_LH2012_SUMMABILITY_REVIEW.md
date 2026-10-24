# DYAD — López-Hernanz (2012): full-text summability assessment

**Date:** 23 October 2026  
**Status:** SESSION analysis; not an owner adoption, release, repository change, or numerical Stokes campaign.  
**Governing scientific owner consulted:** `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` at `dyad-v6.4.22`, particularly §2 OPEN 20. The current repository BASELINE confirms v6.4.22; canonical file identity recorded there: `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29`. This review did not re-hash the full owner DSN.  
**Article read:** the complete supplied Markdown transcription, 681 lines, including §§1–6, proofs and references, with printed-page labels 211–221. File: `2012_Summable_formal_invariant_curves_of_diffeomorphisms.md`; SHA-256 `9aa1ffa88ab87a92c5d77e0a672f409eaca17ee696dbb0f17cb605629d622978`. No original PDF was supplied or independently compared against this transcription.  
**Bibliographic check:** Cambridge's publisher page confirms ETDS 32(1), February 2012, pp. 211–221, DOI 10.1017/S0143385710000805; online publication was 14 March 2011. The technical analysis below uses the supplied full text, not the publisher abstract.

## 1. Disposition

[THM — imported application candidate; SESSION] The article supplies the missing summability theorem, not merely another Gevrey bound. Applied to the two previously studied smooth formal branches of the complexified return `F=T^6`, using their reviewed SESSION algebra and the explicit two-blow-up reduction below, it gives **3-summability in the original branch parameter z**, Gevrey order 1/3, at most six exceptional directions per branch, and sectorial realizations as strong Hakim parabolic curves for F or F inverse.

[OPEN] It does not determine whether the two formal branches converge. It does not decide B-an, B-6, convergence of log F, or physical realization. New deductions here remain SESSION; previous curve results are not silently recast as adopted owner theorems.

## 2. What the entire paper establishes

| Location | Content and limit |
|---|---|
| §1, main theorem | An isolated fixed point of a holomorphic identity-tangent germ in C² admits a summable parametrized formal invariant curve. This existential statement alone does not identify every formal invariant curve. |
| §2, Definitions 2.1–2.2 | Invariance under F is equivalent to tangency to its formal generator. Briot–Bouquet type is a precise reduced-generator form, with nonzero tangential eigenvalue and eigenvalue ratio outside positive rationals. Camacho–Sad curves reduce to that type. The generator need not converge. |
| §3, Theorems 3.1–3.2 | One-variable orbit estimates and Hakim parabolic-curve existence. These are imported ingredients, not new DYAD certificates. |
| §4, Definition 4.1 and Theorem 4.2 | Polynomial normalization and strong Hakim graphs on wide petal domains, with uniqueness in the explicitly bounded function-and-derivative class H. The proof adapts Hakim's contraction operator, with Lemma 4.4 controlling perturbations of its iterates. |
| §5, Theorem 5.1 and Corollary 5.2 | Strong Hakim graphs admit the same formal curve with Gevrey asymptotics of order 1/k. Together with the inverse map, this gives k-summability except possibly 2k directions. The proof compares exact solutions to quasi-solutions via a cohomological difference equation and exponentially small corrections. |
| §6, Theorem 6.1 | Transfers the conclusion through desingularization and Puiseux parametrization to Camacho–Sad curves, with some summation level l >= ord(F)-1. This lower bound alone is not an exact value of l. |

[THM — source] Three notions must remain separate: coefficient Gevrey growth, sectorial Gevrey asymptotics/summability, and convergence of the power series in a full disc. The paper proves the second for its stated curve class; it does not assert the third.

## 3. DYAD hypothesis transfer

### 3.1 Inputs and custody

[SESSION source] P1-c §1 proves isolatedness and local multiplicity 13 by an exact finite ideal-membership test followed by Nakayama's lemma. P1-c §2 proves exactly two smooth formal graphs tangent to [1:0]:

\[
\Gamma_\sigma:\quad w=\hat\phi_\sigma(z)
=a_\sigma z^2+a_{3,\sigma}z^3+\cdots,\qquad \sigma\in\{+,-\}.
\]

The coordinates here are the complexification of the **raw** DYAD W-frame: z=W and w is its independent complexification partner, not the normalized NF coordinate also called z elsewhere in the DSN.

The leading coefficients obey

\[
P(a)=Aa^2+Ba+C=0,
\]
\[
A=\tfrac12+2i\sqrt3,\quad
B=\tfrac{11}{24}-\tfrac{5i\sqrt3}{24},\quad
C=-\tfrac{61}{2160}+\tfrac{43i\sqrt3}{6480}.
\]

Set

\[
\mu=-\tfrac12-\tfrac{2i\sqrt3}{3},\quad
c_{40}=-\tfrac1{16}+\tfrac{7i\sqrt3}{144},\quad
\ell_\sigma=c_{40}+\mu a_\sigma\ne0.
\]

The restrictions satisfy

\[
F|_{\Gamma_\sigma}(z)=z+\ell_\sigma z^4+O(z^5),\qquad
\ell_-=-\ell_+.
\]

These are reviewed SESSION inputs, not a fresh full replay of the earlier isolation and all-order curve certificates.

### 3.2 Two blow-ups, rather than a claim based only on a name

[ALG — SESSION derivation] Put

\[
\pi_\sigma(x,y)=(z,w)=(x,x^2(a_\sigma+y)).
\]

This is the chart obtained by two point blow-ups followed by translation on the exceptional divisor. It is not a diffeomorphic coordinate change at the original origin.

The raw exact jets imply analytic functions G,H with

\[
F_z(x,x^2u)=x+x^4G(x,u),\qquad
F_w(x,x^2u)=x^2u+x^5H(x,u),
\]
\[
G(0,u)=c_{40}+\mu u,
\qquad H(0,u)=C+d_{31}u+\bar\mu u^2,
\quad d_{31}=\tfrac13-\tfrac{i\sqrt3}{9}.
\]

This divisibility holds for the full analytic germ: the quadratic part is zero, the only cubic channels have the required weighted orders, the obstructing pure-z quartic term of F_w is zero, and all total degrees >=6 have sufficiently large weighted order. It is not an inference that an arbitrary finite jet determines summability.

Since F_z/x is a unit, the lifted map is holomorphic:

\[
x'=x+x^4G(x,u),\qquad
u'=\frac{u+x^3H(x,u)}{(1+x^3G(x,u))^2}.
\]

At u=a_sigma, the coefficient of x³ in u'-u is P(u)=H(0,u)-2uG(0,u), and P(a_sigma)=0. Thus the lifted germ has order four, not three. Its formal generator has the form

\[
\widetilde X_\sigma
=x^3\left[
 (\ell_\sigma+O(x,y))x\partial_x
 +(\beta_\sigma x+\ell_\sigma\alpha y+O((x,y)^2))\partial_y
\right],
\]
\[
\alpha=\frac{P'(a_\sigma)}{\ell_\sigma}
=k_*-2=-\frac{102}{19}-\frac{16i\sqrt3}{19}\notin\mathbb Q_{>0}.
\]

The logarithm has the same reduced linear data: the lifted map is tangent to the identity at order four, so logarithmic corrections start at total degree seven. The factor x³ and the additional horizontal x factor persist in the formal logarithm.

This is precisely Definition 2.1 of the paper. The strict transform of Gamma_sigma is transverse to x=0. The same type follows from the earlier P1-c-2 K7 computation, but the explicit chart above makes the source matching testable.

### 3.3 Normalized coordinates and the exact summation level

[ALG — SESSION] Rescale horizontally by xi=c_sigma x, with

\[
c_\sigma^3=-\ell_\sigma.
\]

Subtract a finite polynomial jet from y so that the strict-transform graph vanishes to order m>=2. This is an analytic polynomial operation and assumes no convergence of the full formal curve. Since Re(alpha)=-102/19, the paper's additional requirement

\[
m>1+\Re\alpha
\]

is automatic for m>=2. A polynomial strict transform is already convergent and causes no obstruction to the conclusion.

The normalized map has the §4 form

\[
\widetilde F_1(\xi,y)=\xi-\xi^4+O(\xi^4y,\xi^5),
\]
\[
\widetilde F_2(\xi,y)=y-\alpha\xi^3y+
O(\xi^3y^2,\xi^4y)+\xi^{3+m}\psi(\xi).
\]

Therefore the relevant k is **3**. Applying only Theorem 6.1 to the original order-three F would yield l>=2 and would not identify l=3; the branch-specific reduction does identify it.

## 4. New imported consequence and its boundaries

[THM — imported application candidate; SESSION] Theorem 4.2, Theorem 5.1 and Corollary 5.2 give:

\[
\boxed{\hat\phi_\sigma\text{ is 3-summable in }z,
\quad \text{with Gevrey order }1/3.}
\]

Polynomial blow-down, finite jet addition and linear rescaling preserve this summability. No divergent reparametrization is needed because z=x in the chosen blow-up chart.

The sums parameterize the strong Hakim curves of the lifted map, and their blow-downs are parabolic curves of F or F inverse. The terminology "strong" refers to the normalized lifted graph and its H-class bounds; an arbitrary numerical orbit is not such a selected sum.

The result is stronger than the previously reviewed BFM coefficient upper bound. It does not assert an optimal Gevrey order, actual non-summability on every exceptional ray, or divergence. A convergent series is also 3-summable.

**Notation correction for future live records:** Gevrey-1/3 corresponds to **3-summability**, not "1/3-summability in z". After the ramification t=z³, the residue-class decomposition into three series can be expressed with ordinary order-one summation; a fractional power must not be silently suppressed.

## 5. Sectors, exceptional directions, and the correct gap

[THM — source; ALG — substitution] For any eta in (0,pi/2), the wide domains in §4 have asymptotic opening

\[
\frac{2(\pi-\eta)}3>\frac\pi3.
\]

F supplies three attracting petal directions and F inverse supplies three repelling directions per selected branch. In the normalized xi coordinate, the only possible singular summation directions are

\[
\arg\xi=\frac\pi6+\frac{j\pi}3,\qquad j=0,\ldots,5.
\]

In the original z coordinate this becomes the candidate-ray set

\[
\mathcal D_\sigma
=\{d:\arg(-\ell_\sigma)+3d=\pi/2\pmod\pi\}.
\]

There are at most six genuine obstructions, not necessarily six. Since ell_minus=-ell_plus, the candidate-ray sets coincide, although the attracting and repelling roles are interchanged.

For example eta=pi/4 permits proper sectors of opening below pi/2 but above pi/3, with positive adjacent overlap. Radii must be reduced to a common positive radius; the paper does not supply a numeric radius for DYAD.

[ALG — SESSION] Compare **two sectorial sums of the same formal branch**, expressed as graphs over the same original z:

\[
\Delta_{\sigma,j}(z)
=\phi_{\sigma,j+1}(z)-\phi_{\sigma,j}(z).
\]

On proper common subsectors, their shared Gevrey-1/3 expansion yields

\[
|\Delta_{\sigma,j}(z)|\le C\exp(-A/|z|^3)
\]

with suitable positive constants. This is an upper bound, not a proven leading asymptotic or a computed Stokes constant. Algebraic prefactors and additional structure may occur.

Do not compare phi_plus to phi_minus for this purpose:

\[
\hat\phi_+(z)-\hat\phi_-(z)
=(a_+-a_-)z^2+O(z^3),\quad a_+\ne a_-.
\]

That is a nonzero algebraic difference, not a Stokes jump.

### 5.1 Gluing criterion, derived here rather than quoted as a theorem in the paper

[THM — SESSION consequence] Choose finitely many compatible sectorial sums covering a punctured disc, including the final-to-first overlap. Then

\[
\boxed{\hat\phi_\sigma\text{ converges}
\iff \Delta_{\sigma,j}\equiv0\text{ on every overlap}.}
\]

Proof: a convergent curve has the same sums by uniqueness. Conversely, identical overlap functions glue to a single holomorphic function on the punctured disc. The common asymptotic expansion gives boundedness near zero on a finite subcover, hence the singularity is removable; the Taylor series is the given formal curve.

This does not reduce the question to a single unspecified "Stokes constant". The paper does not calculate the full jump data or establish a finite-parameter description of those jumps for DYAD.

## 6. An additional DYAD symmetry reduction

[ALG/THM — SESSION derivation, not a statement of the paper] The two branches tangent to [1:0] have the same convergence status. In fact

\[
T(\Gamma_+)=\Gamma_-,\qquad T(\Gamma_-)=\Gamma_+.
\]

Reason: T commutes with F=T⁶, so it maps an F-invariant formal curve to another such curve. In the raw complex frame its linear part is (lambda z, conjugate(lambda) w), lambda=exp(i*pi/3), and the z² coefficient of T_w is -1/6. The leading coefficient of its image is

\[
a\longmapsto
\frac{\bar\lambda a-1/6}{\lambda^2}
=\frac{1+i\sqrt3}{12}-a.
\]

But a_plus+a_minus=-B/A=(1+i*sqrt(3))/12. The roots are distinct, so T exchanges them. The all-order identification uses the previously proved uniqueness of the two smooth formal branches, not just this quadratic identity. Since T is an analytic local diffeomorphism, convergence of either branch implies convergence of the other.

\[
\boxed{\hat\phi_+\text{ converges}\iff\hat\phi_-\text{ converges}.}
\]

This can reduce a convergence/divergence investigation to one branch. It does not by itself prove that all six jump conditions are equivalent or reduce them to a single scalar.

## 7. What this means for OPEN 20

[OWNER: DYAD v6.4.22 §2] B-infinity existence and flat uniqueness are closed at local smooth-germ scope. B-an asks convergence of the tangent-to-identity square root F^(1/2), and B-6 asks convergence of F^(1/6). Both remain open.

[SESSION inference] The article proves neither square-root convergence nor square-root divergence. In particular:

- A nonzero curve jump would prove divergence of that branch, and by the previous conditional Briot–Bouquet lemma would imply divergence of log F. This rules out an analytic generator with **zero linear part**. It does not, by itself, rule out an analytic square root.
- If the curve converges, restriction to it yields an analytic one-variable parabolic germ. Any analytic tangent-to-identity root of F preserves that curve, so an obstruction to the corresponding one-variable root would obstruct the full root. The paper supplies no such obstruction or horn-map computation.
- Sectorial curve sums do not supply a full two-dimensional sectorial normalization or classification. Those would be additional work before claiming a complete root-compatibility criterion.

These complex curves are not real DYAD trajectories. On the real slice w=conjugate(z), |w|=|z|; on the sectorial graphs |w|=O(|z|²). Thus sufficiently near the origin these graphs have no nonzero real-slice points. Neither the real PRIM-CTR tube nor the L-PHASE row-A constants may be reused as complex-sector enclosures without a new argument.

## 8. Computational use and next work

[ALG — evidence] A new, small exact check independently composes the real primitive map six times through degree five with fractions.Fraction, then changes to (z,w) using exact SymPy arithmetic. It checks the raw coefficients, weighted divisibility, reduced quadratic, eigenvalue ratio for both algebraic roots, ell != 0, opposite ell values and the T action on a2. Nine positive gates passed. Three altered-input controls (ratio, branch action, coefficient) exited 1 at their intended gates. No Stokes gap or large-degree trajectory campaign was executed.

[HEUR] Recommended next sequence:

1. Record the explicit Definition-2.1 -> Theorem-4.2 -> Corollary-5.2 transfer as a small SESSION import note, with the distinction between original order three and lifted order four.
2. Fix one branch, the normalized coordinate, a finite petal cover, graph parametrization and all adjacent overlaps. Use the article's H-class to specify which functions an algorithm approximates.
3. Build a bounded pilot with analytic/interval control of Hakim's fixed-point operator or Borel–Laplace reconstruction. The article offers an orbit-sum construction and exponential-correction method, but its delta and constants are existential.
4. A certified enclosure of the **actual** jump excluding zero would prove curve divergence. A floating-point value or an interval containing zero does not prove anything either way. Convergence requires an analytic gluing identity on all relevant overlaps, not numerical agreement at sample points.

The logarithmic correction and full-map dependence must be included before equating an extracted numerical prefactor with an invariant Stokes constant. The full formal series, not a finite truncation alone, is the theorem's object.

## 9. Source/evidence manifest

| Source | Read | Identity and limit |
|---|---|---|
| Attached LH2012 transcription | Full, all 681 lines | SHA-256 `9aa1ffa88ab87a92c5d77e0a672f409eaca17ee696dbb0f17cb605629d622978`; no PDF-byte verification |
| GitHub BASELINE | Full current response | v6.4.22 governing; not an independent replay of release checks |
| DYAD at tag dyad-v6.4.22 | §2 OPEN registry, especially OPEN20 | Source-read, no owner modifications |
| P1-c SESSION v0.1 | Full local record; relevant repository passages compared | SHA-256 `9f6f09d8d2efd8fbd42e518c4bdc852bfae15099c4abda8d6f1a8c94d0c70902` |
| P1-c-2 SESSION v0.1 | Full relevant reduction/literature/result sections; repository comparison | SHA-256 `7e7aa09f0ee5b8d2c9b7a82e7ad4832fea7bf057dbea000595f1ade45f298788` |
| P1-c-5 SESSION v0.1 | §§1–5 | SHA-256 `11917ba21d5b7a23338df3bb343d4ddfd446ca38747a41c3af1cbcc3c709e36b` |
| P1-c-2b SESSION v0.1.1 | Full | SHA-256 `578c8f028ab94aba9896ba4a7001d297f407a8a3747c4f1871a173e9221df356` |
| New exact script and results | Code written and executed in this session | `check_lh2012_dyad_transfer.py`, `transfer_checks.json`, `negative_controls.json`; finite algebra only |

All prior SESSION results retain their prior custody and grades. This document is a reading/application assessment with explicit new deductions, not an assertion of owner adoption. No files, branches, pull requests, releases, tags, notices or canonical statuses were changed in the repository.
