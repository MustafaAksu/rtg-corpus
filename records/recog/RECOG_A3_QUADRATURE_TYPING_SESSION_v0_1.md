# RECOG A3 — Pole-comparator quadrature typing (R4 sub-item 1): session record

**Date:** 23 October 2026 · **Author:** RECOG co-owner (Claude) · **Status:** `[SESSION]` scientific record, v0.1. No DSN is edited; nothing is adopted; grades below are targets for a later cell. PI decision of 23 Oct 2026 (with the round-2 review of PR #23): `A3 AUTHORIZED` — *prove the mathematical typing of the pole-comparator quadrature and show explicitly why this typing alone is not an intrinsic type-change criterion; R4 does not close automatically.*
**Governing edition:** `recog-v0.3.23` (DSN SHA-256 `0d5834003ce8f6819a760ac02ec4e1b65c4d34a0eb13381d0fe4e175af9ca31a`); Dyadic `dyad-v6.4.22`. Study plan: `records/recog/RECOG_STUDY_PLAN_2026-10-19.md` §A3.
**Certificate:** `evidence/recog/scripts/recog_a3_quadrature_typing.py` — exact sympy gates Q1–Q6 and negative controls NC1–NC2 (ALL PASS); `[NUM]` periodic-orbit probe; outputs `evidence/recog/a3_quadrature/a3_quadrature_typing.json`, `_output.txt`.
**Guards in force:** SG-R2 (all angles are pole-comparator angles $\eta$; $\arg W\ne\eta$), SG-R3 (pointwise type is chart-dependent off fixed points), SG-R4 (no twins here; nothing exported), SG-R6 (a comparison value changing is not an event).

## 0. Summary

1. **Typing in the primitive chart (exact).** On the quadrature $\mathcal Q=\{\operatorname{Re}\widehat C_{\rm pole}=0\}=\{\cos\eta=0\}$ the one-step Jacobian is the nontrivial unipotent shear $J=\begin{pmatrix}1&0\\e^\rho&1\end{pmatrix}$ with $1$-eigenspace the comparator direction $\partial_\eta$ (Q2). The discriminant identity $\Delta_J=c(c-4e^\rho)$, $c=\operatorname{Re}\widehat C_{\rm pole}$, is re-verified (Q1).
2. **What is chart-free about $\mathcal Q$ (comparator geometry).** Three characterizations in terms of the dyad observables $(\rho,\eta)$ only — none of them mentions eigenvalues:
   (a) $\rho(Tx)-\rho(x)=-\operatorname{Im}\widehat C_{\rm pole}(x)$, so $|\rho(Tx)-\rho(x)|\le1$ with equality **exactly on $\mathcal Q$**: the quadrature is the locus of extremal one-step radial transfer;
   (b) $\partial_\eta[\rho\circ T-\rho]=-\operatorname{Re}\widehat C_{\rm pole}$: $\mathcal Q$ is the critical locus of the radial transfer along the comparator fiber (the radial row decouples from $\eta$ to first order);
   (c) $\det_{d\rho\wedge d\eta}DT-1=(e^\rho-1)\operatorname{Re}\widehat C_{\rm pole}$: $\mathcal Q\cup\{\rho=0\}$ is the area-neutral locus of the one-step transport for the swap-invariant comparator area form $d\rho\wedge d\eta$, separating area expansion from contraction (Q3).
   So the "coordinate-free counterpart via comparator geometry" asked for in R4 sub-item 1 exists, but it is a *transfer/area* statement, not a *type* statement.
3. **Why the typing alone is not intrinsic (explicit).** Two global unimodular charts retype $\mathcal Q$ (Q4): chart A, $\varphi_A=(\rho+\varepsilon\sin\eta,\ \eta)$, gives on $\mathcal Q$ a Jacobian with $\det=1$ and $\operatorname{tr}=2+\varepsilon e^\rho\cos\eta'$, hence **hyperbolic** for $\varepsilon=+\tfrac12$ ($\operatorname{tr}=2.4207$ at $\rho=0$) and **elliptic** for $\varepsilon=-\tfrac12$ ($\operatorname{tr}=1.5793$); chart B, $\varphi_B=(\rho,\ \eta+\tfrac e{e-1}e^\rho)$, makes the Jacobian the **identity** on the whole branch $\eta=\pi/2$ (the shear strength $e^\rho$ is a chart artefact). A genuine conjugacy (constant linear chart) preserves $\operatorname{tr},\det$ everywhere (NC1). This is SG-R3 made explicit on $\mathcal Q$: pointwise, off fixed points, only the rank and the sign of $\det$ survive a chart change; "parabolic" does not.
4. **$(t,d)$-plane route.** Multipliers are intrinsic only on periodic points. A quadrature crossing contributes the factor $\det J=1$ to $d_n$ and is not separable in $t_n$ (two-step example, Q5). The `[NUM]` probe (periods $\le8$, $|L|\le2$, $\rho\in[-2.5,2.5]$) finds 18 orbits, none with a point on $\mathcal Q$ (closest $|\cos\eta|=0.031$). So no periodic-orbit signature of $\mathcal Q$ is available; none is expected.
5. **By-product for R4 sub-item 2 (exact).** Inside the swap-fixed stratum $\Sigma=\{\sin\eta=0\}$, $\rho$ is preserved and $\eta\mapsto\eta+e^\rho-1$; hence the wrapped-periodic orbits contained in $\Sigma$ are exactly $e^\rho-1=m\pi$, $m\ge0$: $m=0$ gives $P_1,P_2$; $m=2k$ the known winding fixed points; **$m$ odd gives new period-2 orbits** $\{(\ln(1+m\pi),0),(\ln(1+m\pi),\pi)\}$ alternating between the pole strata $\widehat C_{\rm pole}=+1$ and $-1$, with $(\operatorname{tr}M_2,\det M_2)=(1,\,1-m^2\pi^2)$ — hyperbolic and orientation-reversing (Q6; the probe finds $m=1$ to $10^{-10}$).
6. **Disposition proposal for R4.** Sub-item 1 is answered in reframed form: *comparator-geometric counterpart — yes (items 2a–c); conjugacy-intrinsic type-change — no (item 3); periodic-orbit signature — none (item 4).* R4 stays ACTIVE on sub-item 2 (inventory), to which item 5 contributes an exact partial inventory. Nothing closes here; a later cell may reword sub-item 1 and register the statements.

## 1. Objects and conventions

Primitive map in the lifted chart (Dyadic §6.1): $T(\rho,\eta)=(\rho-\sin\eta,\ \eta+e^\rho-1-\sin\eta)$; $(\rho,\eta)$ are the dyad observables (log amplitude ratio, relative phase), not an arbitrary chart. Pole comparator (RECOG-DEF-POLE-COMPARATOR): $\widehat C_{\rm pole}=e^{i\eta}$; pole swap $S(\rho,\eta)=(-\rho,-\eta)$ sends $\widehat C_{\rm pole}\mapsto\overline{\widehat C_{\rm pole}}$. Quadrature: $\mathcal Q=\{\widehat C_{\rm pole}=\pm i\}=\{\cos\eta=0\}$, two branches $\eta=\pm\pi/2$ mod $2\pi$, swapped by $S$ (so $\mathcal Q$ is swap-invariant as a set). Jacobian $J=DT=\begin{pmatrix}1&-c\\e^\rho&1-c\end{pmatrix}$, $c=\cos\eta$. A *chart* here is a diffeomorphism $\varphi$ of the lifted plane respecting $\eta$-periodicity; the transformed one-step Jacobian at $x$ is $D\varphi_{Tx}\,J_x\,D\varphi_x^{-1}$ (SG-R3). "Type" means elliptic/parabolic/hyperbolic of a $2\times2$ real matrix.

## 2. Statements

**Proposition 1 (primitive-chart typing of $\mathcal Q$).** `[ALG]` target [scope: primitive chart]. $\operatorname{tr}J=2-c$, $\det J=1+(e^\rho-1)c$, $\Delta_J=c(c-4e^\rho)$ (as RECOG §6.5). On $\mathcal Q$: $J=\begin{pmatrix}1&0\\e^\rho&1\end{pmatrix}$, $(J-I)\ne0$, $(J-I)^2=0$, $J\partial_\eta=\partial_\eta$. Both branches identical. *Certified Q1–Q2.* $\square$

**Proposition 2 (comparator-geometric characterizations).** `[ALG]` target [scope: dyad observables $(\rho,\eta)$; no chart]. With $\Delta\rho:=\rho\circ T-\rho$:
(a) $\Delta\rho=-\operatorname{Im}\widehat C_{\rm pole}$; $|\Delta\rho|\le1$ with equality iff $x\in\mathcal Q$ ($\Delta\rho=-1$ on $\eta=\pi/2$, $+1$ on $\eta=-\pi/2$).
(b) $\partial_\eta\Delta\rho=-\operatorname{Re}\widehat C_{\rm pole}$, zero iff $x\in\mathcal Q$.
(c) $\det_{d\rho\wedge d\eta}DT=1+(e^\rho-1)\operatorname{Re}\widehat C_{\rm pole}$; the form $d\rho\wedge d\eta$ is $S$-invariant ($\det DS=+1$); the one-step transport is area-expanding where $(e^\rho-1)\cos\eta>0$, contracting where $<0$, neutral exactly on $\mathcal Q\cup\{\rho=0\}$.
*Certified Q3.* Remarks: (a)–(c) are statements about canonical observables and survive any relabelling that fixes those observables; they are the sense in which $\mathcal Q$ is "intrinsic". None of them is a statement about eigenvalues of $DT$; in particular (c) refines SG-R3's orientation character (sign of $\det$) to the comparator-area multiplier, whose *value* is meaningful because the area form is canonical. $\square$

**Proposition 3 (the parabolic type is not chart-invariant on $\mathcal Q$).** `[ALG]` target.
(i) *General form (standard fact, cited, not re-proved here):* for $x$ with $Tx\ne x$ — true on all of $\mathcal Q$ since $|\Delta\rho|=1$ — and any $A\in GL^+(2,\mathbb R)$ there is a chart $\varphi$ with $D(\varphi T\varphi^{-1})_{\varphi(x)}=A$, because $\operatorname{Diff}$ acts transitively on oriented frames at two distinct points; hence the only pointwise chart-invariants are the rank and $\operatorname{sign}\det$ (SG-R3).
(ii) *Explicit witnesses (certified Q4):* chart A, $\varphi_A(\rho,\eta)=(\rho+\varepsilon\sin\eta,\eta)$, $\det D\varphi_A\equiv1$: transformed $\operatorname{tr}=2-c+\varepsilon e^\rho(\cos\eta'-\cos\eta)$ with $\eta'=\eta+e^\rho-1-\sin\eta$, $\det$ unchanged; on $\mathcal Q$: $\operatorname{tr}=2+\varepsilon e^\rho\cos\eta'$, $\det=1$. At $(\rho,\eta)=(0,\pi/2)$: $\cos\eta'=\sin1>0$, so $\varepsilon=\tfrac12$ gives $\operatorname{tr}=2.4207$ (hyperbolic) and $\varepsilon=-\tfrac12$ gives $\operatorname{tr}=1.5793$ (elliptic). Chart B, $\varphi_B(\rho,\eta)=(\rho,\eta+\alpha e^\rho)$, $\alpha=\tfrac e{e-1}$: on the branch $\eta=\pi/2$ (where $\rho'=\rho-1$) the transformed Jacobian is $I$; on $\eta=-\pi/2$ it is the shear of strength $e^\rho(1+e)$. Both charts are global unimodular shears of the lifted plane and descend to the cylinder.
(iii) *Negative controls:* a constant linear chart preserves $\operatorname{tr}$ and $\det$ identically (NC1); chart A at $\varepsilon=0$ reproduces Proposition 1 (NC2).
*Consequence:* "$\mathcal Q$ is parabolic" is a primitive-chart sentence; the chart-free content of $\mathcal Q$ is Proposition 2. $\square$

**Proposition 4 (no periodic-orbit signature).** `[ALG]` target for the identity; `[NUM]` for the probe. For a period-$n$ point, $(t_n,d_n)=(\operatorname{tr}M_n,\det M_n)$ is chart-invariant and $d_n=\prod_i\det J_{x_i}$; a point of the orbit on $\mathcal Q$ contributes the factor $1$ to $d_n$ and no separable factor to $t_n$ (two-step example: $\operatorname{tr}(J_{Tx}J_x)|_{\eta=\pi/2}=2+(1+e^\rho)\sin(e^\rho-2)$ depends on the partner point; Q5). The probe (§3) finds no periodic point on $\mathcal Q$ up to period 8 in its box. $\square$

**Proposition 5 (periodic orbits inside the swap-fixed stratum).** `[ALG]` target. On $\Sigma=\{\sin\eta=0\}$: $T(\rho,k\pi)=(\rho,k\pi+e^\rho-1)$. A wrapped-periodic orbit contained in $\Sigma$ therefore has $e^\rho-1\in\pi\mathbb Z_{\ge0}$, and conversely every $\rho_m=\ln(1+m\pi)$, $m\ge0$, gives one: $m=0$: $P_1=(0,0)$, $P_2=(0,\pi)$; $m=2k$: the winding fixed points $(\rho_{2k},0)$ with $(t,d)=(1,1+2\pi k)$ and $(\rho_{2k},\pi)$ with $(t,d)=(3,1-2\pi k)$; $m$ odd: the period-2 orbits $(\rho_m,0)\leftrightarrow(\rho_m,\pi)$ with $M_2=J_{(\rho_m,\pi)}J_{(\rho_m,0)}$, $(t_2,d_2)=(1,\,1-m^2\pi^2)$, hyperbolic ($\Delta=4m^2\pi^2-3>0$) and orientation-reversing. No point of $\Sigma$ lies on $\mathcal Q$. *Certified Q6 (symbolic $m$, $k$).* Remark: the odd-$m$ orbits alternate between the pole-level pair-symmetry strata $\widehat C_{\rm pole}=+1$ and $-1$ of RECOG §6.5; they are the first periodic orbits of the primitive $T$ beyond the fixed points recorded in RECOG/Dyadic. $\square$

## 3. `[NUM]` periodic-orbit probe (exploratory; no completeness claim)

Newton on $T^n x=x+(0,2\pi L)$, $n\le8$, $|L|\le2$, seeds on a $41\times48$ grid in $\rho\in[-2.5,2.5]$, $\eta\in[0,2\pi)$; residual $<10^{-13}$; minimal period enforced; orbits near $P_1$ with $|x|<10^{-3}$ rejected ($T^6=\mathrm{id}+O(|x|^3)$ produces false convergence). 18 orbits:

| $n$ | $L$ | $(t_n,d_n)$ | $\min|\cos\eta|$ | consecutive points on opposite sides of $\mathcal Q$ | identification |
|---|---|---|---|---|---|
| 1 | 0 | $(1,1)$, $(3,1)$ | 1 | — | $P_1$, $P_2$ |
| 1 | 1 | $(1,7.2832)$, $(3,-5.2832)$ | 1 | — | winding $k=1$, $\rho=\ln(1+2\pi)$ (Prop. 5) |
| 1 | 2 | $(1,13.566)$, $(3,-11.566)$ | 1 | — | winding $k=2$ (Prop. 5) |
| 2 | 1 | $(1,-8.8696)$ | 1 | yes | $m=1$ orbit, $\rho=\ln(1+\pi)$, $d_2=1-\pi^2$ (Prop. 5) |
| 2 | 1 | $(-2.0889,4.7631)$ | 0.414 | no | new, elliptic-type multiplier, $x_0=(1.7760,1.1436)$ |
| 2 | 2 | $(10.381,2.2043)$ | 0.491 | no | new, $x_0=(1.4581,4.1988)$ |
| 4 | 2 | $(13.193,1.1337)$ | 0.379 | yes | new |
| 5 | 2 | $(45.654,-0.6514)$; $(-46.548,-0.3634)$ | 0.298; 0.031 | yes | new (hyperbolic) |
| 6 | 2 | $(113.81,-0.9447)$; $(-122.32,0.9384)$ | 0.203; 0.045 | yes | new |
| 7 | 2 | $(288.81,-1.0293)$; $(-309.82,1.2996)$ | 0.162; 0.062 | yes | new |
| 8 | 2 | $(745.32,-1.0615)$; $(-797.01,1.4247)$ | 0.146; 0.070 | yes | new |

Reading: no periodic point lies on $\mathcal Q$; the $L=2$ family for $n\ge4$ has $|t_n|$ growing roughly geometrically (hyperbolic, near $\eta\approx\pi$, small $\rho$) — a candidate for the B3 census with Krawczyk certificates on the PI machine. "Opposite sides" is a discrete jump, not a crossing (SG-R6: not an event). Coordinates are in the JSON to $10^{-10}$.

## 4. Consequences for R4 (proposals, not adoptions)

- **Sub-item 1** ("coordinate-free counterpart of $\cos\eta=0$ via periodic-orbit multipliers in the $(t,d)$-plane or via comparator geometry"): answered in reframed form. Via comparator geometry: yes — $\mathcal Q$ is the extremal-radial-transfer locus and (with $\rho=0$) the comparator-area-neutral locus (Prop. 2). Via multipliers: no signature (Prop. 4). As a type-change locus: not chart-intrinsic (Prop. 3); what was called "type change" in the primitive chart is the sign of $\operatorname{Re}\widehat C_{\rm pole}$ in disguise ($\operatorname{sign}\Delta_J=-\operatorname{sign}c$ for $\rho>-\ln4$), i.e. a comparator datum, not a dynamical invariant. Proposed wording for a later cell: *"$\mathcal Q$ has a comparator-geometric characterization (extremal radial transfer; area-neutral transport) but no chart-free eigenvalue type; the primitive-chart rotational/stretching dichotomy is the sign of $\operatorname{Re}\widehat C_{\rm pole}$."* Proposed RID: `RECOG-ALG-QUADRATURE-TYPING` with Props. 1–4 as named sub-statements.
- **Sub-item 2** (inventory): Prop. 5 gives the complete inventory inside $\Sigma$ (exact) and the probe a `[NUM]` list outside it. Proposed RID: `RECOG-ALG-SWAP-STRATUM-PERIODIC-INVENTORY`. R4 remains ACTIVE on the global inventory (B3).
- **SG-R3** is confirmed and sharpened: besides rank and $\operatorname{sign}\det$, the comparator-area multiplier $\det_{d\rho\wedge d\eta}DT$ is meaningful once $(\rho,\eta)$ are fixed as observables — a convention statement, to be checked against RRF's profile rules before any DSN wording.
- Nothing here bears on R6: a crossing of $\mathcal Q$ is a comparison-value change (SG-R6).

## 5. Open items

1. Whether the comparator-area multiplier (Prop. 2c) is accepted as an intrinsic observable depends on the status of $(\rho,\eta)$ as canonical dyad observables (Dyadic/RRF); this record only uses them as the DSN defines them.
2. B3 census: certify the probe's 11 new orbits (Krawczyk, exact rational boxes), extend the box and periods; look for any periodic point on $\mathcal Q$ (none expected to be forced).
3. Whether the odd-$m$ pole-strata-alternating orbits have a recognition reading is for R6, not R4; not pursued here.
