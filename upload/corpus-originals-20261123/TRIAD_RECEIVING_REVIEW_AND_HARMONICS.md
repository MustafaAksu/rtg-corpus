# Triadic → Relational Emergence Registry: conditional Genesis modal branch and first common-angle calculation

**Date:** 8 October 2026  
**Status:** NONCANONICAL receiving review / proposed RER conditional entries. No modification or adoption of the adopted Triadic or Genesis owner, the existing RER v0.1, the RRF, or a physical event law.  
**Decision:** ACCEPT the source-defined Genesis modal construction for a **conditional test branch**, not for the unselected physical standalone \(K_3\) target. Retain `NO_TARGET_VECTOR_LAW_SELECTED` for that physical target.

## 1. Contract of the named branch

The supplied Genesis handoff independently defines

\[
E=\begin{pmatrix}1&0\\-\frac12&1\\-\frac12&-1\end{pmatrix},\qquad
P=\begin{pmatrix}\frac23&-\frac13&-\frac13\\0&\frac12&-\frac12\end{pmatrix},
\]
\[
T_e(\rho,\eta)=(\rho-\sin\eta,\eta+e^\rho-1-\sin\eta),\quad
\mathcal N=(P\otimes I_2)T_e^{\times3}(E\otimes I_2),\quad
\mathcal F=\mathcal N^{\circ6}.
\]

Every primitive step **reprojects** through \(P\). This is not \(P(T_e^6)^{\times3}E\), the primitive \(K_4\) shadow, or the root-closed \(M_{\rm root}\). Its local analytic expansion is
\[
\mathcal F(X)=X+G_3(X)+G_4(X)+O(\|X\|^5),\qquad X=(s,c)\in(\mathbb R^2)^2.
\]

Use \(B=\left(\begin{smallmatrix}1&-1/2\\-1/2&1\end{smallmatrix}\right)\), \(J_Q=\frac1{\sqrt3}\left(\begin{smallmatrix}1&-2\\2&-1\end{smallmatrix}\right)\), and
\[
\Phi(X)=(Q_s,Q_c,I,\Omega),\quad
\Omega=\frac{\sqrt3}{2}(s_\eta c_\rho-s_\rho c_\eta),\quad
Q_sQ_c=I^2+\Omega^2.
\]

The proper \(B\)-rotation is \(R_\theta=e^{\theta J_Q}\). This is a **kinematic readout fibre**, not a selected physical gauge/pole relabel. Events and restrictions capable of excluding states are not supplied by the named analytic model; a future physical event domain must be reviewed separately.

## 2. [ALG] Three model-specific closure results

| Local proposed record | Law/readout | Exact disposition | Proof scope |
|---|---|---|---|
| RER-GEN-C01 | \(\mathcal J_3(X)=X+G_3(X)\); unsigned \((Q_s,Q_c,I)\) | **DISPROVED_EXACT_CLOSURE_FOR_SURROGATE** | Opposite chirality, same unsigned input, different successor \(I\) at order four |
| RER-GEN-C02 | \(\mathcal J_3\); signed \(\Phi=(Q_s,Q_c,I,\Omega)\) | **EXACT_CLOSURE_FOR_SURROGATE** | \(G_3\) commutes with simultaneous proper \(B\)-rotations; signed readout separates the orbits |
| RER-GEN-C03 | \(\mathcal F=\mathcal N^6\); signed \(\Phi\) | **DISPROVED_EXACT_CLOSURE_FOR_NAMED_MODEL** | Noncollinear \(X_t, -X_t\), equal signed input, unequal successor amplitude |

The cubic claim is **exact for the polynomial map defined as \(\mathcal J_3\)**, not merely a truncated claim about \(\mathcal F\). It also permits a local quotient of the specified cubic ODE \(\dot X=G_3(X)\) on admitted flow domains, which is a different clock from \(\mathcal F\).

The raw-map witness is
\[
X_t=((t,0),(0,t)),\qquad X_t'=-X_t,\qquad
\Phi(X_t)=\Phi(X_t')=\left(t^2,t^2,-\frac{t^2}{2},-\frac{\sqrt3t^2}{2}\right),
\]
\[
\boxed{Q_s(\mathcal F(X_t))-Q_s(\mathcal F(X_t'))
=\frac{349}{288}t^5+O(t^7).}
\]
Both input vectors are nonzero, and their Gram determinant is \(3t^4/4>0\). The coefficient is independently reproduced from the explicit analytic update using only exact rational truncated composition. Analyticity proves different successor readouts for all sufficiently small positive \(t\) on a common admitted neighborhood. It does not give a certified numerical radius or test an unspecified physical event law.

## 3. [ALG — new Triadic calculation] The actual common-angle dependence at quintic readout order

Choose the Euclidean chart
\[
\mathcal L_B(\rho,\eta)=\rho-\eta/2+i\sqrt3\eta/2.
\]
On \(Q_s>0\), put
\[
a=\sqrt{Q_s},\qquad h=I/a,\qquad k=-\Omega/a,
\]
\[
\mathcal L_Bs=a e^{i\theta_s},\qquad
\mathcal L_Bc=(h+ik)e^{i\theta_s}.
\]

For any fixed reference shape \(X_0\) on this chart, let \(X_\theta=R_\theta X_0\) and scale the complete state by \(t\). Since \(G_3\) is equivariant, its readout correction at order \(t^4\) has no common-angle dependence. The first common-angle-dependent coefficient is
\[
\Phi(\mathcal F(tX_\theta))
=t^2\Phi(X_0)+t^4D_4\Phi(X_0)
+t^5D_5\Phi(\theta)+O(t^6),
\]
\[
\boxed{D_5\Phi(\theta)
=2\operatorname{Re}\big(C_1(a,h,k)e^{i\theta}+C_3(a,h,k)e^{3i\theta}\big).}
\]
Here \(C_1,C_3\in\mathbb C^4\) are **exact, generally nonzero polynomials of total degree five in \(a,h,k\)**. Their full coefficients are in `data/angular_quintic_harmonics.json`; the corresponding homogeneous cubic and quartic vector jets are in `data/jet_coefficients.json`. **There is no fifth harmonic at this order**. This follows by exact substitution into \(D\Phi(X)G_4(X)\), not by restricting to one ray. As a separate identity check, each quintic observable polynomial \(f\) satisfies
\[
\boxed{(\mathcal D_{\rm rot}^2+1)(\mathcal D_{\rm rot}^2+9)f=0,\qquad
\mathcal D_{\rm rot}f=Df(X)\operatorname{diag}(J_Q,J_Q)X.}
\]
This independently excludes fifth (and other) harmonics for the degree-five terms.

For the nondegenerate fixed shape \(s_0=(1,0),c_0=(0,1)\) (so \(a=1,h=-1/2,k=\sqrt3/2\)), the parent-amplitude component is
\[
\boxed{
D_5Q_s(\theta)=
\frac{65}{288}\cos\theta
+\frac{161\sqrt3}{864}\sin\theta
+\frac{73}{192}\cos3\theta
-\frac{59\sqrt3}{5184}\sin3\theta.
}
\]
At \(\theta=0\), this is \(349/576\); at \(\theta=\pi\), it is \(-349/576\). Their difference is the independently checked \(349/288\).

### Residual-symmetry consequence

At that fixed nondegenerate shape, **both first and third Fourier coefficients are nonzero**. A constant common rotation by \(\alpha\) preserving every successor readout along the orbit would have to satisfy \(e^{i\alpha}=1\) as well as \(e^{3i\alpha}=1\). Thus no nontrivial global cyclic subgroup \(C_n\) of the simultaneous proper \(B\)-rotations supplies a quotient valid on a neighborhood containing this orbit, already at the displayed order. In particular, storing only \(e^{3i\theta_s}\) cannot restore even the leading broken closure.

This does **not** rule out a different model-specific representation, a nonrotation equivalence relation, an event-restricted domain, or a smaller approximate statistic chosen for different observables. It is not a theorem about physical gauge selection.

### Compression limit

Retaining \(e^{i\theta_s}\) along with signed Gram coordinates gives the complete common angle; \(e^{3i\theta_s}=(e^{i\theta_s})^3\) adds no independent data. The resulting present-state representation reconstructs the full pair exactly on \(Q_s>0\) and therefore closes the named analytic map, but it is **lossless state reparameterization, not demonstrated emergent state compression**. The Fourier calculation is a first-order obstruction to coarse *cyclic-angle* quotients; it does not prove a universal minimal reduced state or any need for historical memory.

## 4. Source custody and verification

**Source-derived:** The supplied Genesis handoff fixes \(E,P,T_e\), the reprojection clock, the cubic vector dictionary, the quartic readout and the parity witness. The attached response explicitly disclaims physical target selection and source-byte authentication against its earlier parity archive. The RER draft v0.1 continues to govern the distinction between static structure and physical emergence.

**Newly checked here:** A standalone exact rational four-component composition produced all cubic/quartic vector coefficients and the two antisymmetric ray coefficients. The cubic dictionary, its rotation infinitesimal, all four derived quartic invariant increments, and all four quintic common-angle Fourier decompositions were cross-checked in a separate symbolic validator. The first/third-only harmonic result and the displayed coefficients are new calculations at the **named-model** scope, not claims contained in Genesis v2.8.5.

- `scripts/make_jet.py`: exact rational truncation at vector degree 4; outputs `data/jet_coefficients.json`.
- `scripts/harmonics.py`: exact Laurent/Fourier extraction from the quintic observable effect; outputs `data/angular_quintic_harmonics.json`.
- `scripts/validate.py`: 43 exact point-of-use/cross-model checks, plus one negative control that asserts the false absence of the third harmonic.

**Not checked:** Exact identity of an earlier source parity archive or historical extractor, full higher-order harmonics of the analytic map, any physical event domain, full microscopic network incidence, a physical common-frame gauge, and any minimal state/memory theorem. Fresh scripts cannot automatically authenticate older producer custody; their source contract is the currently attached explicit formula.

## 5. Proposed registry handling and next test

Add **three target-specific conditional subrecords**, not a new owner theorem or physical-model selection. Their six-field structures appear in `data/RER_TRIAD_CONDITIONAL_ENTRIES.json`. Keep the original RER-T02 and physical `NO_TARGET_VECTOR_LAW_SELECTED` unchanged. The present exercise answers T-START/T-FIBRE **for this branch only**.

Suggested next scoped question:

> For the declared analytic modal map, is there any proper, noninvertible present-state factor that closes to a controlled order, or does the first-harmonic dependence force full common-phase retention within the stated smooth symmetry-compatible class?

The next exact calculation should derive the common-angle update \(\theta_s^+=\arg\mathcal L_Bs^+\) and attempt a closed augmented jet to a specified order, keeping the remainder explicit. Do not initiate memory augmentation until a proposed present-state factor has a demonstrated failure, and do not promote this branch to a physical standalone \(K_3\) law without Genesis/owner selection.
