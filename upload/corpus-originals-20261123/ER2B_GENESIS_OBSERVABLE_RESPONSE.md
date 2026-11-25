# ER-2B: separable and nonseparable contributions to triad observables

**Date:** 2026-10-09  
**Status:** noncanonical scoped algebra review / candidate Genesis–Triadic handoff; no source-owner theorem adoption, no new physical selection.  
**Model:** the named Genesis analytic triad model with identical primitive edge map and reprojection after each step. Only the first homogeneous cubic term of its six-step return is used here.  
**Source:** `sources/genesis_sixjet_obstruction_audit.json` included in this package (the preceding independent rational six-jet reconstruction) and the reviewed ER2B v1.1 chirality note. The new exact code loads this prior `G3` rather than regenerating the primitive six-step return. A separate exact-map numerical check uses the untruncated sine/exponential rule and is corroboration, not certificate.

## 1. Definitions and normalizations

In the complex Genesis/RER eigenframe:

\[
 z=W(s),\qquad d=W(c),\qquad
 w_1=z,\quad w_2=-z/2+d,\quad w_3=-z/2-d.
\]

Let

\[
 Q_s=|z|^2,\quad Q_c=|d|^2,\quad
 I=\Re(z\bar d),\quad S=\Omega_G=\Im(z\bar d).
\]

The signed-Gram constraint is \(Q_sQ_c=I^2+S^2\). The unweighted total edge amplitude satisfies the **exact incidence identity**

\[
 \boxed{N=\sum_{e=1}^3|w_e|^2=\tfrac32 Q_s+2Q_c.}
\]

With \(q_e=|w_e|^2\), the closure also implies

\[
 \boxed{\sum_e q_e^2=N^2/2-2S^2,\qquad
 0\le S^2\le N^2/12.}
\]

Here \(S\) is the RER-signed chirality, not the numerically different Triadic-normalized \(\Omega_T=-2S\).

## 2. Full return's two complex coefficients

The cyclically compatible cubic edge difference has the two-complex-coefficient structure

\[
 (G_{3,1}-G_{3,2})_w
 =\nu(w_1|w_1|^2-w_2|w_2|^2)
 -2i\chi w_3S.
\]

Reading the previously audited four exact real cubic output polynomials gives

\[
 \boxed{\nu=\tfrac16-i\tfrac{\sqrt3}{3},\qquad\chi=\tfrac13.}
\]

One independent coefficient extraction is to take \(w_1=1,w_2=0,w_3=-1\), where \(S=0\): then the computed complex first-minus-second edge output equals \(1/6-i\sqrt3/3\). The two-coefficient formula reproduces the **entire** earlier recorded polynomial difference. Moreover, its projected-edge representatives reproduce both independent edge output jets, not only their difference. These are exact source-jet consistency checks.

A compatible zero-sum cubic representative is

\[
 \begin{aligned}
 \delta_\nu w_e&=\nu\bigl(w_e|w_e|^2-\tfrac13\sum_jw_j|w_j|^2\bigr),\\
 \delta_\chi w_e&=\tfrac{2i\chi}{3}(w_{e+1}-w_{e-1})S.
 \end{aligned}
\]

All indices are cyclic. The physical single-dyad normalizer's coefficient \(\mu\), and the present triad \(\nu\), are **different objects**; no identification is made.

## 3. General exact responses of quadratic observables

At first order in the cubic return increment, the **nonseparable** term yields

\[
 \boxed{\begin{aligned}
 \delta_\chi S&=\tfrac23\Re\chi\,NS,\\
 \delta_\chi N&=8\Re\chi\,S^2,\\
 \delta_\chi Q_s&=\tfrac83(\Re\chi\,S^2-\Im\chi\,IS),\\
 \delta_\chi Q_c&=2\Re\chi\,S^2+2\Im\chi\,IS,\\
 \delta_\chi I&=\Im\chi\,(Q_s-\tfrac43Q_c)S.
 \end{aligned}}
\]

Thus \(\Im\chi\) is invisible in \(\delta N,\delta S\) **at this order** but can redistribute the component Gram observables. This does not imply it is physically pure phase, nor that it remains invisible at all orders.

The **separable** term yields

\[
 \boxed{\begin{aligned}
 \delta_\nu S&=\tfrac23\Re\nu\,NS,\\
 \delta_\nu N&=2\Re\nu\sum_e|w_e|^4.
 \end{aligned}}
\]

The imaginary part of \(\nu\) also cancels in \(\delta N,\delta S\) at this order, but appears in \(\delta Q_s,\delta Q_c,\delta I\).

## 4. Genesis full cubic jet: net response

Inserting the fixed-chart coefficients \(\nu=1/6-i\sqrt3/3\) and \(\chi=1/3\), and writing \(X=(s,c)\), gives the **analytic model's six-step observable expansion**

\[
 \boxed{\begin{aligned}
 N(\mathcal F X)-N(X)&=\tfrac16N^2+2S^2+O(\|X\|^5),\\
 S(\mathcal F X)-S(X)&=\tfrac13NS+O(\|X\|^5).
 \end{aligned}}
\]

Here \(\mathcal F=\mathcal N^6\) is the same reprojection-after-each-primitive-step Genesis model; its first nonlinear vector jet is cubic. Since \(N\asymp\|X\|^2\) on the real four-dimensional state chart, the vector norm remainder can equivalently be written \(O(N^{5/2})\), locally uniformly.

The complete four signed-Gram observable increments at order four are:

\[
 \boxed{\begin{aligned}
 \Delta Q_s &=\tfrac14Q_s^2+\tfrac13Q_sQ_c+\tfrac23S^2
               -\tfrac{4\sqrt3}{9}IS+O(\|X\|^5),\\
 \Delta Q_c &=\tfrac14Q_sQ_c+\tfrac13Q_c^2+\tfrac12S^2
               +\tfrac{\sqrt3}{3}IS+O(\|X\|^5),\\
 \Delta I &=\tfrac16NI+\sqrt3\bigl(\tfrac16Q_s-\tfrac29Q_c\bigr)S
               +O(\|X\|^5),\\
 \Delta S &=\tfrac13NS+O(\|X\|^5).
 \end{aligned}}
\]

The quartic Gram-constraint variation cancels identically. These formulas are **model-specific** and do not assert that signed Gram closes for the exact analytic return at higher orders; indeed previous C03 shows it does not.

### Local positivity consequence

Because \(N>0\) off the origin and \(S^2\ge0\), the quartic part of \(\Delta N\) is uniformly positive:

\[
 \tfrac16N^2\le \Delta_4N=\tfrac16N^2+2S^2\le\tfrac13N^2.
\]

Analyticity and the uniform higher-order remainder imply there exists a **possibly small, not yet quantified** local neighborhood in which

\[
 \boxed{N(\mathcal FX)>N(X)\quad\text{for all }X\ne0\text{ therein}.}
\]

This is a conditional **local radial-outflow** statement for the projected triad model. It is notably different from the isolated DYAD primitive return's contracting \(Q_{\rm prim}\). It does not prove global runaway, select the physical triadic dynamics, or produce physical energy, time, or curvature. A uniform numerical radius would require an additional bound on the fifth-and-higher observable remainder.

Similarly, \(\Delta_4 S=NS/3\) has the same sign as nonzero \(S\). This is a **leading-order fixed-shape** amplification statement. It is not uniform sign protection for arbitrarily tiny \(|S|\), since a higher-order term can dominate near the collinear locus; earlier Genesis examples show chirality can be created from \(S=0\) under the exact primitive model.

## 5. Evidence scope and next step

- The script `scripts/check_observable_response.py` passes **24 exact symbolic assertions**. It verifies the full cubic edge jet against an **imported prior audited** `genesis_sixjet_obstruction_audit.json` (which the user and a separate reviewer previously checked), and independently differentiates both source sectors to obtain the observable increments.
- The separate script `scripts/numeric_check_exact_map.py` uses 95-digit arithmetic with the untruncated \(\sin,\exp\) primitive edge map and reprojection at each of six steps. Its selected cases converge to the quartic coefficients. This is an independent numerical sanity check, not a proof or a certified uniform enclosure.
- The first attempt at the exact-check harness used a wrong expression for the area-bound square; the corrected identity is \(N^2-12S^2=(3Q_s/2-2Q_c)^2+12I^2\). A later initial harness check erroneously identified source edge \(w_2\) with modal child \(d\); the final check correctly transports \(d=w_2+w_1/2\). Neither error was in the source model or results; the final executed script exits zero.
- No independent producer of the entire six-step jet was rerun here. The imported source JSON is preserved unchanged in `sources/` with its SHA-256 identity recorded. The original Triadic/Genesis DSNs and official RER remain unchanged.

**[HEUR] Recommended handoff:** Report these as `ER-2B OBS-1` conditional formulas to Genesis and Triadic. The scientific question then becomes why the chosen incidence/reprojection changes the local radial return sign relative to isolated DYAD, and whether any physically selected triad update retains the same property. Do not promote the local outflow to physical destabilization without selection and a uniform domain certificate.
