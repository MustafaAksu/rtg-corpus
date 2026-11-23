# ER-2B OBS-1 — source-split theorem and local radial response

**Date:** 10 October 2026  
**Status:** Noncanonical source-based review/addendum. No amendment or adoption of Genesis, Triadic, DYAD or RER owner documents.  
**Model:** Three identical 2D primitive edge maps under the Genesis zero-sum projection, reprojection after *every* primitive step, six-step return. The physical standalone K3 selection remains OPEN.

## 1. Source split: scope and proof

Fix the real linearization

\[
A=\begin{pmatrix}1&-1\\1&0\end{pmatrix},\quad A^6=I,
\qquad T(x)=Ax+q(x)+r(x)+O(\|x\|^4),
\]

with arbitrary **homogeneous quadratic** \(q:V\to V\) and arbitrary **homogeneous cubic** \(r:V\to V\), and the Genesis projected edge map

\[
\mathcal N=P_{\mathcal C}T^{\times3},\quad
P_{\mathcal C}=I_3-\tfrac13\mathbf1\mathbf1^T,\quad
r_1+r_2+r_3=0.
\]

To read the single-edge separable cubic coefficient \(\nu\), use the closed initial triad \((x,0,-x)\). In the complex eigenframe \(w=\rho-\eta/2+i\sqrt3\eta/2\), this has \(w_1=W(x),\ w_2=0\) and signed area zero. Therefore the nonseparable \(\chi\)-term vanishes in the first-minus-second cubic output, which directly reads \(\nu\) after normalization by \(W(x)|W(x)|^2\).

At the linear level, the three edge states at step \(j\) are \((A^jx,0,-A^jx)\). Let \(b_j\) be the **isolated** second-order coefficient after \(j\) steps, with

\[
b_0=0,\qquad b_{j+1}=Ab_j+q(A^jx).
\]

Because a homogeneous quadratic is even, the projected quadratic edge corrections obey

\[
\boxed{B_j^{\rm tri}=\bigl(b_j/3,-2b_j/3,b_j/3\bigr).}
\]

The cubic correction to the first-minus-second edge output then obeys

\[
D_{j+1}^{\rm tri}=AD_j^{\rm tri}
+r(A^jx)+\tfrac13 Dq(A^jx)b_j,
\]

whereas the isolated cubic coefficient obeys

\[
d_{j+1}^{\rm iso}=Ad_j^{\rm iso}
+r(A^jx)+Dq(A^jx)b_j.
\]

These recurrences prove—without requiring the specific six quadratic coefficients of Genesis—that the **direct-cubic source contribution** to the indicated cubic edge coefficient is the same, while the **quadratic-composition contribution** is one third of the isolated value. For the fixed sixth-order resonant linearization and registered edge-orbit coefficient definition:

\[
\boxed{\nu=\mu_3+\tfrac13\mu_{22}.}
\]

**Boundary:** This is a theorem about the specified *source split* and the chosen readout, not an identity of the entire isolated and triadic vector return jets, or an assertion for arbitrary incidence, projection, clocks, alternative edge laws, or physical K3 dynamics. A quadratic/cubic source split also changes under some nonlinear coordinate changes even when the complete return observable remains fixed.

The attached test constructs six primitive iterates symbolically for **all six coefficients** of an arbitrary 2D homogeneous \(q\), and verifies \(D_6^{\rm tri}[q^2]=d_6^{\rm iso}[q^2]/3\) identically. It separately verifies the direct-cubic identity for the Genesis source \(r\). This is an independent special-orbit/source-sector check, not a fresh full four-dimensional return-map certificate.

## 2. Genesis coefficients

Genesis primitive cubic:
\[
r(\rho,\eta)=\left(\eta^3/6,\ (\rho^3+\eta^3)/6\right).
\]

Genesis quadratic:
\[
q(\rho,\eta)=\left(0,\rho^2/2\right).
\]

In the common complex eigenframe, source contributions are:

| Origin of contribution | Isolated DYAD \(\mu\) | Projected triad \(\nu\) |
|---|---|---|
| Direct \(r=T_3\) | \(\frac12-\frac{i\sqrt3}{6}\) | \(\frac12-\frac{i\sqrt3}{6}\) |
| Iterated quadratic \(q\times q\) | \(-1-\frac{i\sqrt3}{2}\) | \(-\frac13-\frac{i\sqrt3}{6}\) |
| **Total** | \(-\frac12-\frac{2i\sqrt3}{3}\) | \(\frac16-\frac{i\sqrt3}{3}\) |

Thus \(\operatorname{Re}\mu<0\) but \(\operatorname{Re}\nu>0\). The exact factor \(1/3\) is due to the **projected quadratic variation along the source-reading triad**, not a pointwise statement that every modal quadratic derivative everywhere is just the isolated one divided by three.

The independent ER-2B source-jet analysis supplies \(\chi=1/3\), arising entirely from \(q\times q\) at this order. The attached new one-ray script imports this \(\chi\) as a source value; it does not re-extract the entire \(\chi\) tensor.

## 3. Exact quartic response and the positivity criterion

Write \(S=\Omega_G\), \(N=\sum_e|w_e|^2\), with the zero-sum complex edge condition. The ER-2B general result is

\[
\boxed{\Delta_4N=aN^2+(8b-4a)S^2,\qquad
 a=\operatorname{Re}\nu,\ b=\operatorname{Re}\chi.}
\]

The admissible range is \(0\le S^2/N^2\le1/12\) for \(N>0\), and both endpoints are attainable by admissible closed edge triples. The expression is affine in this ratio, so the quartic term is **strictly positive on every nonzero closed edge state** if and only if

\[
\boxed{a>0\quad\text{and}\quad a+b>0.}
\]

For Genesis, with \(a=1/6,b=1/3\),

\[
\boxed{\Delta_4N=\tfrac16N^2+2S^2,\qquad
\tfrac16N^2\le\Delta_4N\le\tfrac13N^2.}
\]

Moreover the two *source contributions* can be displayed independently:

\[
\begin{aligned}
\Delta_4N\big|_{T_3}&=\tfrac12N^2-2S^2
&&\in[\tfrac13N^2,\tfrac12N^2],\\
\Delta_4N\big|_{T_2\times T_2}&=-\tfrac13N^2+4S^2
&&\in[-\tfrac13N^2,0].
\end{aligned}
\]

The second expression has the useful factorization, with \(I=\operatorname{Re}(W(s)\overline{W(c)})\), \(Q_s=|W(s)|^2\), \(Q_c=|W(c)|^2\):

\[
\boxed{
\Delta_4N\big|_{T_2\times T_2}
=-\tfrac13(N^2-12S^2)
=-\tfrac13\bigl[(\tfrac32Q_s-2Q_c)^2+12I^2\bigr].
}
\]

Thus the direct primitive cubic contribution is uniformly outward at this order, while quadratic-composition is nonpositive. In the isolated DYAD, the latter wins. With the specified projection, its separable coefficient is reduced and the outward contribution wins. This is the requested **source mechanism for the sign change**, at the level of the stated fixed-chart Taylor split.

## 4. Precise local instability conclusion

Analyticity supplies a local bound

\[
N(\mathcal FX)-N(X)=\Delta_4N(X)+R(X),\qquad
|R(X)|\le C N(X)^{5/2}
\]

for some finite \(C\) on a sufficiently small four-dimensional neighborhood (because \(N\) is positive definite there). After shrinking it, one obtains

\[
\boxed{N(\mathcal FX)\ge N(X)+\tfrac1{12}N(X)^2}
\]

for every nonzero state in that smaller neighborhood. This proves that **every nonzero sufficiently small forward orbit must eventually leave any fixed such neighborhood**, provided iteration is followed while the map remains defined on it. The origin is Lyapunov-unstable for the named analytic six-step modal model.

Important correction to informal shorthand: the full analytic dynamics is **not** yet certified to satisfy \(N(\mathcal FX)-N(X)\ge N^2/6\) at finite nonzero amplitude; \(1/6\) is the quartic leading coefficient, and the higher remainder may have either sign. An explicit numerical neighborhood/radius still needs a certified analytic remainder majorant.

This statement is not global runaway, physical energy creation, a general triadic resonance law, or a choice of birth mechanism.

## 5. Next programme action

[HEUR] Replace the OBS-1 question “Why does the sign change?” with this conditional source-split theorem and its assumptions. Avoid another broad numerical scan. The next high-value action is a **mechanism/selection interface test**: determine which triadic incidence/reprojection (or node-resonance) law is physically admitted, whether it preserves the same source-response split, and whether the admitted observer measures this same \(N\). Neither the origin's instability in this selected model nor \(\nu=\mu_3+\mu_{22}/3\) alone selects that physics.

The source coefficients are independently cross-checked, but the earlier ER-2B complete \(G_3\) and \(\chi\) reconstructions retain their own provenance. No owner DSN, RID, RER entry, or adopted theorem grade is changed.
