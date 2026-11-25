# Triadic — common-angle update and conditional orbit-separation study v0.1

**Date:** 8 October 2026  
**Status:** NONCANONICAL research note / Triadic receiving result; not an owner-DSN revision.  
**Ownership:** Genesis defines the microscopic modal law; Triadic computes the augmented effective state; RER holds noncanonical cross-level entries. No independent Emergence stream is opened.  
**Physical target:** `NO_TARGET_VECTOR_LAW_SELECTED` remains in force for the physical standalone-\(K_3\) law.

## 1. Fixed model contract — do not substitute a convenient update

Use the Genesis conditional, per-step-reprojected analytic model

\[
 E=\begin{pmatrix}1&0\\-1/2&1\\-1/2&-1\end{pmatrix},\quad
 P=\begin{pmatrix}2/3&-1/3&-1/3\\0&1/2&-1/2\end{pmatrix},\quad
 T_e(\rho,\eta)=(\rho-\sin\eta,\eta+e^\rho-1-\sin\eta),
\]
\[
\mathcal N=(P\otimes I_2)\circ T_e^{\times3}\circ(E\otimes I_2),\qquad
\mathcal F=\mathcal N^{\circ6}
 =\mathrm{id}+G_3+G_4+O(\|X\|^5),\qquad X=(s,c).
\]

Reprojection occurs **after each primitive step**. This is not standalone physical \(K_3\), the primitive \(K_4\) shadow, or the root-closed T-6 diagnostic. The linear coordinate frame is
\[
B=\begin{pmatrix}1&-1/2\\-1/2&1\end{pmatrix},\quad
\mathcal L_B(\rho,\eta)=\rho-\eta/2+i\sqrt3\eta/2,\quad
J_Q=\frac1{\sqrt3}\begin{pmatrix}1&-2\\2&-1\end{pmatrix}.
\]
Define \(\Phi=(Q_s,Q_c,I_{sc},\Omega_G)\), where
\[
Q_s=s^\top Bs,\quad Q_c=c^\top Bc,\quad I_{sc}=s^\top Bc,\quad
\Omega_G=\tfrac{\sqrt3}{2}(s_\eta c_\rho-s_\rho c_\eta),\quad
Q_sQ_c=I_{sc}^2+\Omega_G^2.
\]
All statements below are local on \(Q_s>0\) and, for uniform order bounds, along fixed nonzero reference shapes scaled to the origin. The physical event domain and physical pole-gauge action are **not selected**.

## 2. [ALG] Common-angle update derived from the vector jet

Let \(X_t=tX_0\), \(t>0\), and define \(\theta_s=\arg\mathcal L_Bs\) on a continuous local angle lift. Let \(G_{j,s}=(g_{j,\rho},g_{j,\eta})\). Direct differentiation of the argument gives
\[
\frac{d}{d\varepsilon}\bigg|_{\varepsilon=0}
 \arg\mathcal L_B(s+\varepsilon v)
=\frac{\sqrt3}{2Q_s}(s_\rho v_\eta-s_\eta v_\rho).
\]
Because \(\mathcal F(tX_0)=tX_0+t^3G_3(X_0)+t^4G_4(X_0)+O(t^5)\), the quadratic terms in the logarithm first contribute at order \(t^4\) to the angle. Consequently,
\[
\boxed{
\theta_s^+(tX_0)=\theta_s(X_0)
+t^2\Theta_2(X_0)+t^3\Theta_3(X_0)+O(t^4),
}
\]
\[
\Theta_j(X_0)=\frac{\sqrt3}{2Q_s(X_0)}
 \left(s_\rho G_{j+1,s,\eta}-s_\eta G_{j+1,s,\rho}\right)(X_0),\qquad j=2,3.
\]

The cubic Genesis vector dictionary yields **common-angle-independent**
\[
\boxed{
\Theta_2(\Phi)=-\frac{\sqrt3}{4}Q_s-\frac{\sqrt3}{9}Q_c
+\frac{I_{sc}\Omega_G}{3Q_s}
-\frac{2\sqrt3 I_{sc}^2}{9Q_s}.
}
\]
This is homogeneous quadratic in the original vector coordinates. It is the exact phase drift of the **cubic jet through the displayed order**, not an exact physical nonlinear phase law.

Write the complete ordered pair using the common-frame chart
\[
\mathcal L_Bs=a e^{i\theta},\qquad
\mathcal L_Bc=(h+ik)e^{i\theta},\qquad
 a=\sqrt{Q_s}>0,\quad h=I_{sc}/a,\quad k=-\Omega_G/a.
\]
Then
\[
\boxed{\Theta_2=-\sqrt3\left(\frac{a^2}{4}+\frac{h^2}{3}+\frac{k^2}{9}\right)-\frac{hk}{3}.}
\]

For the quartic parent vector jet, define its fifth-degree angle numerator
\[
N_4(X)=\frac{\sqrt3}{2}\left(s_\rho G_{4,s,\eta}-s_\eta G_{4,s,\rho}\right).
\]
Exact Laurent substitution shows that it has **only** common-angle frequencies \(\pm1\) and \(\pm3\); the allowable \(\pm5\) terms cancel:
\[
\boxed{
\Theta_3(a,h,k,\theta)=\frac2{a^2}\operatorname{Re}
\left(P_1(a,h,k)e^{i\theta}+P_3(a,h,k)e^{3i\theta}\right).
}
\]
The full exact homogeneous-quintic coefficient polynomials \(P_1,P_3\) are recorded in `data/COMMON_ANGLE_JET.json`, not abbreviated by decimal fitting.

For the noncollinear Genesis witness \(s_0=(1,0), c_0=(0,1)\), take \(a=1,h=-1/2,k=\sqrt3/2\). Here
\[
\boxed{
\begin{aligned}
\theta_s^+={}&\theta_s-\frac{\sqrt3}{3}t^2\\
&+t^3\bigg[\frac{65\sqrt3}{1728}\cos\theta_s
-\frac{19}{192}\sin\theta_s
-\frac{199\sqrt3}{3456}\cos3\theta_s
-\frac{863}{3456}\sin3\theta_s\bigg]+O(t^4).
\end{aligned}}
\]
The signed-Gram successors begin at orders \(t^2,t^4,t^5\), with the order-five Fourier polynomials pinned in the preceding study. Together these give the **complete augmented jet at the respective controlled orders**, not an exact finite polynomial update for the analytic model.

## 3. [ALG — new conditional orbit-separation result] The successor readout embeds one common-angle circle

Retain all four signed-Gram successor components for the same witness shape \(X_0=((1,0),(0,1))\). The leading quintic common-angle output is
\[
\Psi_5(\theta)=M\begin{pmatrix}\cos\theta\\\sin\theta\\\cos3\theta\\\sin3\theta\end{pmatrix},\qquad
M=\begin{pmatrix}
65/288&161\sqrt3/864&73/192&-59\sqrt3/5184\\
-11/48&-17\sqrt3/144&17/48&-13\sqrt3/432\\
-11/32&-7\sqrt3/27&-137/1152&271\sqrt3/10368\\
25\sqrt3/216&55/288&-709\sqrt3/3456&53/3456
\end{pmatrix}.
\]
Exact arithmetic gives \(\operatorname{rank}M=3\) (as expected from the Gram constraint) and a real kernel spanned by
\[
v=(-1716859\sqrt3,\ 2492295,\ -160036\sqrt3,\ 1413576)^\top.
\]
Put \(q=v_1+iv_2\) and \(r=v_3+iv_4\). The exact nonzero obstruction is
\[
\boxed{\operatorname{Im}(r\bar q^{\,3})
=31867336191987863672583168\sqrt3\ne0.}
\]

**Proof of injectivity.** If two distinct angles \(\theta,\varphi\) had the same \(\Psi_5\), their trigonometric-vector difference would be a nonzero real multiple of \(v\). Yet
\[
\frac{e^{3i\theta}-e^{3i\varphi}}
{(e^{i\theta}-e^{i\varphi})^3}
=-\frac{\sin(3\delta)}{4\sin^3\delta}\in\mathbb R,
\qquad \delta=(\theta-\varphi)/2.
\]
Such a difference would require \(r/q^3\) real, contradicting the nonzero obstruction. Likewise \(\Psi_5'(\theta)\) cannot vanish, because its corresponding cubic ratio is \(-3\in\mathbb R\). Thus \(\Psi_5:S^1\to\mathbb R^4\) is a smooth embedding.

The full analytic readout has the uniform \(C^1\) expansion on that fixed orbit
\[
\Phi(\mathcal F(tR_\theta X_0))
=t^2\Phi(X_0)+t^4D\Phi(X_0)G_3(X_0)
+t^5\Psi_5(\theta)+O_{C^1}(t^6).
\]
Small \(C^1\) perturbations of this compact embedded circle remain embeddings. Therefore, **for all sufficiently small positive \(t\)** within the named analytic model's local domain, the four successor signed-Gram readouts distinguish **every** common angle on this fixed reference-shape orbit.

**Precise implication:** any present-state factor that is required to predict all four successor signed-Gram observables on this orbit cannot identify distinct values of the current common angle. The result blocks nontrivial phase lumping **on this orbit and for this exact observation task**. It does not prove globally minimal state dimension, prohibit alternative observables, or establish that physical gauge should retain this angle.

## 4. Closure contract and next target

On the \(Q_s>0\) patch the augmented coordinates
\[
Y=(Q_s,Q_c,I_{sc},\Omega_G,\theta_s),\qquad
Q_sQ_c=I_{sc}^2+\Omega_G^2
\]
reconstruct the complete ordered pair. Thus the analytic map induces an **exact** local update on \(Y\) wherever the output remains in the chart. That fact is a change of coordinates, not emergence-driven compression: the four-dimensional physical vector pair still has four independent coordinates.

What has been learned beyond that trivial closure is the **order at which each kind of information matters**:

| Dynamical approximation | Common-frame information needed to predict signed-Gram successors |
|---|---|
| Exact cubic surrogate \(\mathrm{id}+G_3\) | None; \(SO(B)\) equivariance supplies quotient closure |
| Analytic six-step map, order \(t^4\) readout | None for the displayed quartic readout increment |
| Analytic six-step map, order \(t^5\) readout | First and third angular harmonics |
| Fixed noncollinear witness orbit, exact analytic map at small \(t>0\) | No two different common angles can be lumped while preserving all four successor signed-Gram values |
| Physical standalone \(K_3\) | OPEN, target not selected |

The priority after this note is **Genesis source verification** of the chosen \(E,P,T_e\) and per-step schedule, and an **RER receiving review** of the conditional angle-separation claim. Further work can test different observable targets, event-domain restrictions or additional conditional models. Do **not** introduce a memory variable to repair a present-angle loss without first establishing a separate memory necessity result.

## 5. Evidence and custody

- The exact rational source recurrence `sources/make_jet.py` was rerun from the named \(\mathcal N\) definition in a disposable directory; the resulting jet file matches `sources/jet_coefficients.json` **byte-for-byte**.
- `scripts/check_common_angle.py` independently reads this jet, derives \(\Theta_2\), obtains all quartic-phase harmonics, cross-checks earlier four-observable Fourier coefficients, and verifies rank/kernel/chord-separation identities.
- The checker passes 51 exact assertions; two deliberate false-claim controls fail at their intended assertions. These are source-constrained model-algebra checks, not physical simulations or an independent source-ownership adoption.
- Prior source files, Genesis owner, Triadic owner and RER v0.1 are all unchanged. Earlier conditional subrecords C01–C03 remain as proposed. The new C04 below is also proposal-only.
