# ER-2B — arbitrary quadratic primitive jet and full six-step separation obstruction

**Date:** 9 October 2026  
**Status:** New independent finite-algebra review, noncanonical; no owner theorem/adoption change.  
**Scope:** The *fixed* real two-dimensional primitive linear map \(A=\begin{pmatrix}1&-1\\1&0\end{pmatrix}\), identical on the three oriented edges of the zero-sum triad, with simultaneous zero-sum projection after **each** primitive step. The statement concerns the *cubic leading jet* of the six-step return and its full mixed-derivative obstruction, not the exact separability of the entire analytic return or physical resonance.

## 1. Inputs and automatic quadratic cancellation

Let \(V=\mathbb R^2\), \(\mathcal C=\{(r_1,r_2,r_3):r_1+r_2+r_3=0\}\), and let

\[
T(x)=Ax+q(x)+t_3(x)+O(\|x\|^4),\qquad
\mathcal N=P_{\mathcal C}\circ T^{\times3}|_{\mathcal C}.
\]

Here \(q:V\to V\) is an arbitrary homogeneous quadratic map (six real coefficients); \(t_3\) is an arbitrary homogeneous cubic map. In independent coordinates \(r_1=a\), \(r_2=b\), \(r_3=-a-b\), the linear map on \(\mathcal C\) is \(A_4=\operatorname{diag}(A,A)\). It has \(A_4^6=I\), and the eigenvalues \(e^{\pm i\pi/3}\) have no quadratic resonance. Thus, for all \(q\) and \(t_3\),

\[
\boxed{\mathcal N^6(X)=X+G_3(X)+O(\|X\|^4)}.
\]

**Warning:** \(A^6=I\) alone is insufficient for this cancellation if \(A\) is allowed to vary. For example \(A=I\) with nonzero \(q\) leaves a quadratic term \(6q\) in the sixth iterate. The theorem requires the specified primitive-sixth-root spectrum, not just any finite-order linear map.

## 2. Why arbitrary \(t_3\) contributes zero to \(\Omega_6\)

Write \(N_2=P_{\mathcal C}q^{\times3}\), \(N_3=P_{\mathcal C}t_3^{\times3}\). The direct cubic contribution to the six-step return is

\[
G_3^{(3)}=\sum_{j=0}^{5}A_4^{5-j}N_3(A_4^jX).
\]

Since \(A_4\) commutes with the common projection,

\[
G_3^{(3)}=P_{\mathcal C}h^{\times3},\qquad
h(x)=\sum_{j=0}^{5}A^{5-j}t_3(A^jx).
\]

Hence all mixed derivatives of the first-minus-second edge difference vanish:

\[
\boxed{\Omega_6[G_3^{(3)}]=0\quad\text{for every }t_3.}
\]

This theorem is exact at the declared order. It does not say the entire cubic return tensor \(G_3\) is independent of \(t_3\).

## 3. Nonseparable source of the quadratic iteration

For \(m_i=\frac13\sum_{k=1}^{3}q(A^ir_k)\), the nonseparable part of the quadratic-pair contribution has the edge representative

\[
\boxed{
\Theta_e^{(2\times2)}(X)
=-\sum_{0\le i<j\le5}
A^{5-j}Dq(A^jr_e)\left[A^{j-1-i}m_i\right].}
\]

To reconstruct the whole projected cubic tensor, include the separated edge terms and remove the common mean. These additional pieces vanish from \(\Omega_6\). The full mixed-derivative obstruction computed directly from \(G_3\) equals the one computed from the boxed double sum. This is verified in the script for all six arbitrary coefficients, not merely for the Genesis coefficient choice.

## 4. Exact *two-quadratic* classification for all six coefficients

Write the arbitrary primitive quadratic in original real coordinates as

\[
q(\rho,\eta)=\begin{pmatrix}
\alpha\rho^2+\beta\rho\eta+\gamma\eta^2\\
\delta\rho^2+\varepsilon\rho\eta+\zeta\eta^2
\end{pmatrix}.
\]

The obstruction components are quadratic polynomials in these six real coefficients. They simplify dramatically in the fixed eigenframe

\[
w=\rho-\frac12\eta+i\frac{\sqrt3}{2}\eta.
\]

Represent the complex output of \(q\) as

\[
q_w(w,\bar w)=u\,w^2+v\,w\bar w+t\,\bar w^2,
\qquad u,v,t\in\mathbb C.
\]

The six real numbers \((\Re u,\Im u,\Re v,\Im v,\Re t,\Im t)\) are an invertible linear repackaging of \((\alpha,\beta,\gamma,\delta,\varepsilon,\zeta)\).

Define **two**, not three, real quadratic coefficient functions:

\[
\boxed{\begin{aligned}
U(q)&=-12\Re(uv)+4\sqrt3\Im(uv)-2|v|^2-4|t|^2,\\
V(q)&=-12\Re(uv)-4\sqrt3\Im(uv)+2|v|^2-8|t|^2.
\end{aligned}}
\]

(\(U,V\) here name obstruction coefficients, not the Dyadic \((U,V)\) state frame.)

For \(a=(a_1,a_2)\), \(b=(b_1,b_2)\), and

\[
\Omega_{ij}^k=\partial_{a_i}\partial_{b_j}(G_{3,1}-G_{3,2})_k,
\]

the **complete eight-component** obstruction is:

| Mixed derivative | \(\rho\) component | \(\eta\) component |
|---|---|---|
| \(\partial_{a_1}\partial_{b_1}\) | \(U(a_2-b_2)\) | \(V(a_2-b_2)\) |
| \(\partial_{a_1}\partial_{b_2}\) | \(-U(2a_1+b_1)+V(a_2+2b_2)\) | \(-U(a_2+2b_2)+V(-2a_1+a_2-b_1+2b_2)\) |
| \(\partial_{a_2}\partial_{b_1}\) | \(U(a_1+2b_1)-V(2a_2+b_2)\) | \(U(2a_2+b_2)+V(a_1-2a_2+2b_1-b_2)\) |
| \(\partial_{a_2}\partial_{b_2}\) | \(V(a_1-b_1)\) | \((V-U)(a_1-b_1)\) |

The other apparent third quadratic coefficient is exactly \(V-U\). This is a new structural reduction beyond the initial observation that the obstruction depends quadratically on six primitive coefficients.

Consequently the zero set is given *exactly* by **two** real quadratic equations:

\[
\boxed{\begin{aligned}
2\Re(uv)+|t|^2&=0,\\
2\sqrt3\Im(uv)-|v|^2+|t|^2&=0.
\end{aligned}}
\]

These conditions are necessary and sufficient for **vanishing of the full cubic obstruction \(\Omega_6^{[1]}\)** in the declared clock, incidence and edge-coordinate representation. They do not establish exact separability of the entire nonlinear \(\mathcal N^6\).

For the cyclically symmetric, identical-edge class under discussion, vanishing of all mixed derivatives of the edge difference also implies that the cubic map is separable as \(P_{\mathcal C}h^{\times3}\): the difference has the form \(h(a)-h(b)\) by mixed-derivative vanishing and edge-slot swap antisymmetry, and cyclic symmetry then reconstructs all three edge outputs. This is a claim about the *cubic jet only*.

## 5. Nonzero and zero examples; genericity

- **Genesis:** \(q(\rho,\eta)=(0,\rho^2/2)\) gives \(U=1/3\), \(V=2/3\), reproducing every previously reported \(\Omega_6\) component.
- **Zero-obstruction example:** \(q(\rho,\eta)=(\eta^2,\rho^2)\) is nonzero but gives \(U=V=0\). Thus the quadratic source need not vanish for the cubic separation obstruction to vanish.
- Since the coefficient functions are not identically zero, \(\Omega_6^{[1]}\ne0\) for a Zariski-open dense set of six-parameter quadratic jets. The zero set is a proper algebraic subset. The two defining quadrics are independent; no universal sign or universal nonvanishing theorem follows.

This answers the finite-algebra classification question for the specified \(A,P_{\mathcal C}\). It does not require numerical parameter scans or an extension to higher Taylor order.

## 6. Status and scientific interpretation

- **[ALG]** \(G_3^{(3)}\) is edge-separable for every \(t_3\); only the repeated quadratic term contributes to \(\Omega_6^{[1]}\).
- **[ALG]** The six-coefficient quadratic class is characterized by two explicit equations for zero obstruction.
- **[ALG]** Genesis lies outside the zero set, while nontrivial zero-obstruction quadratic jets exist.
- **[OPEN]** No invariant under unrestricted changes of incidence, clock, or physical node/edge ontology has been established. \(\Omega_6\) is not a curvature or physical-resonance quantity.
- **[OPEN]** This classification does not select which allowed primitive \(q\) is physically realized or the role of later emergent variables.

The next meaningful step is interpretation and exact transport of these two coefficient conditions under the admissible representation group—not another parameter sweep. A finite-clock comparison with an independently defined Pre-Legacy candidate still requires that candidate's explicit source and time convention.

**Reproducibility:** `check_closed_form.py` passes 23 exact SymPy checks from an arbitrary six-coefficient quadratic map. It reconstructs the sixfold jet, direct-cubic cancellation, the complete obstruction, the proposed double-sum mechanism, the eigenframe conditions and two example points. There is one new implementation; the original scientific owner certificate was not rerun. No owner file was changed.
