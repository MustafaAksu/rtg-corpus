# T-6u v1.6 — exact leading-coefficient proof and interpretation boundary

**Date:** 30 September 2026. **Status:** draft-supporting derivation; source-conditional and not adopted.

## 1. Premises, not re-derived microscopic facts

Use Genesis v2.8.4 §§6.3–6.6: the stated B,J_Q,omega convention, a tangent-identity six-step block with G2=0, the printed radial quartic P4=2d^TBG3d, and the leading policy family c0=kappa Qs J_Qs+O(|s|^5). These are preserved source inputs. The new code does not claim to generate that P4 from the absent microscopic route-census implementation.

Differentiating P4 at d=0 yields Vd=(1/2)B^-1 grad_d P4. Its pure-parent and pure-child parts are

\[
V_s=-\frac{Q_s}{16}s-\frac{\sqrt3Q_s}{32}J_Qs,
\qquad
V_c=-\frac{Q_c}{54}c+\frac{7Q_c}{108\sqrt3}J_Qc.
\]

Because s and J_Qs are B-orthogonal with equal squared norm Qs,

\[
Q(V_s)=\left(\frac1{256}+\frac3{1024}\right)Q_s^3
=\frac7{1024}Q_s^3,
\qquad Q(V_c)=\frac{61}{34992}Q_c^3.
\]

The index 1 in Qd,1 denotes the first generated return-block seed at zero apex. It is not the quartic radial value at d=0, which vanishes.

## 2. The factor-two source reading has different semantics

The same source gives I(Vs,s)=omega(Vs,s)=-Qs^2/16. Substituting into the s3 radial channel gives

\[
D_{\rm birth}^{[s^3]}
=-\frac18Q_sI(V_s,s)-\frac3{32}Q_s\omega(V_s,s)
=\frac7{512}Q_s^3=2Q(V_s).
\]

This is an exact leading **channel evaluation at the seeded state**, not a second value of the initial-state norm and not the entire next-block radial increment. In a finite map, omitted squared-increment and other terms may be of comparable order after a birth substitution. The source's channel notation must not be silently converted into a complete step law.

The second table row therefore defines sqrt(D_birth/Qc) as an increment-equivalent diagnostic. The dimensional resemblance does not identify its physical meaning with sqrt(Qd,1/Qc).

## 3. General ratio and finite four-case bound

For fixed kappa≠0 and Qs>0, cancellation of the common leading Qs^3 factor gives

\[
R_{\rm vec}=\frac{\sqrt7}{32|\kappa|},\qquad R_\Delta=\sqrt2R_{\rm vec}.
\]

The two policy magnitudes are 2sqrt(3)/3 and 1/2. Thus the four positive ratios are

\[
\frac{\sqrt{21}}{64},\quad\frac{\sqrt{42}}{64},\quad
\frac{\sqrt7}{16},\quad\frac{\sqrt{14}}{16}.
\]

The last is the largest, so the least shortfall relative to the *stipulated* sqrt(2) benchmark is 16/sqrt(7). Its strict sixfold margin follows from

\[
(16/\sqrt7)^2-36=4/7>0.
\]

No claim is made for arbitrary kappa (small |kappa| gives arbitrarily large ratios), arbitrary finite amplitudes, or independently derived physical UV source maps.

## 4. Higher-order policy dependence is not only the c3 norm

The complete zero-apex cubic source includes s3,s2c,sc2,c3. On c=kappa Qs J_Qs the squared norm is exactly the following polynomial in the trial amplitude Qs:

\[
\begin{aligned}
Q(V_d)={}&\frac7{1024}Q_s^3
-\frac{5\sqrt3\kappa}{1728}Q_s^4
-\frac{1073\kappa^2}{62208}Q_s^5
+\frac{5\sqrt3\kappa^3}{648}Q_s^6\\
&+\frac{445\kappa^4}{46656}Q_s^7
-\frac{5\sqrt3\kappa^5}{972}Q_s^8
+\frac{61\kappa^6}{34992}Q_s^9.
\end{aligned}
\]

The certificate checks that this birth-basis expression agrees with direct substitution into the source derivative. It is the norm of the **homogeneous cubic vector only**, not the norm expansion of an unspecified all-order coupled return.

The squared isolated c3 channel is O(Qs^9), or O(Qs^6) relative to the leading seed. Cross terms and the s2c/sc2 channels enter earlier. This does not alter the leading ratio; it prevents an incorrect finite-remainder inference. Unknown higher vector jets and the full birth remainder require separate control.

## 5. What the comparison cannot identify

Qc is an imposed birth input; Qd,1 is a generated output; D_birth is a channel increment at that output. HINDEX instead acts on a specified source operator with declared domain/codomain metrics. The seed comparison contains no such operator-valued map.

The approximately 1.488 isometric ansatz is not reinstated as a physical source. Numerical disagreement with it does not prove that every enlarged-carrier construction is impossible. The negative pure-d radial channel does not by itself prove saturation for arbitrary coupled states or a global absence of cascade.

Programme v1.2 §6.3 expressly does not adopt the OPEN-M “two times short” headline as a programme-certified deficit. The four-case shortfall is therefore a conditional model diagnostic, not a replacement programme conclusion.

## 6. Evidence provenance

The new script has 47 executed exact checks, using SymPy rational/algebraic arithmetic. Decimal displays do not enter acceptance. Two explicit negative controls reject a conflated numerator and a false mixed-channel-independence claim.

The absent original T-6u script is not rerun. A development run of the new script initially rejected a comparison of differently arranged Boolean interval expressions; the final test compares their exact solution set with [0,2]. The development log is retained as a tooling record, not reported as a failed scientific result. The final producer run, negative controls and mechanical draft checks are separately logged.

New calculation is not independent of the source formulas. Independent revision-editor scrutiny, source/RID governance and owner adoption are still required. No source or frozen record is modified by this proof package.
