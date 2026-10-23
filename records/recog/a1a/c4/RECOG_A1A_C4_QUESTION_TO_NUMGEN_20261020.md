# RECOG → Number Genesis — A1a review question (C4): $C_D$ identification and an R9-independent existence route

**Date:** 20 October 2026 · **From:** RECOG owner (Claude, co-owner) · **To:** Number Genesis owner
**Status:** `[SESSION]` review question. This is not a notice, not a G3 item, not an import request and not an adoption request. No NUMGEN file is changed. The PI dispatches it; nothing has been sent yet.

**Basis:**
- `RECOG_A1A_CD_IDENTIFICATION_SESSION_v0_2.md` (`b4906ddf284a9b12155110d987c94ac780ddd24ec5c7ccc12792eab1512dc428`);
- its receiving review `RECOG_A1A_SESSION_v0_2_RECEIVING_REVIEW_20261020.md` (`7aa08ccc…436a8`): accepted at session-record level, with C4 authorized for routing as a question;
- RECOG v0.3.21 (`a3459522…0ae3`), adopted.

## What A1a found (session level)

The definitions used are NUMGEN v1.20.7 (`c4637e7a…ab28`), N-5A-S1-INF: $D_M:=2\pi M-(\hat\phi_{6M}-\hat\phi_0)$, with $\hat\phi$ the increasing primitive lift of $\arg W$.

1. **Exact finite-block identity.** On Dyadic's explicit invariant tube, with starts $0<\lvert W_0\rvert\le\tfrac1{25}$ (i.e. $Q_0\le\tfrac1{625}$), for every $M$:
   $$D_M-\tau\log M=\tau\log Q_0-\bigl(\Psi_W(M)-\Psi_W(0)\bigr)-\tau\log(MQ_M),\qquad\Psi_W=\Theta_W-\tau\log Q .$$
   Two ingredients:
   - Branch control comes from an explicit one-step bound, $\pi/6<\delta_T<\pi/2$, everywhere on the tube. The error constant is $\tfrac{143209}{750000}<\tfrac12$.
   - $MQ_M\to1$ comes from Dyadic's explicit contraction bounds. No NUMGEN radius is used for either.
2. **Identification, conditional on RECOG R9 through Dyadic T1:**
   $$C_D^{\rm ext}(W_0):=\lim_{M}(D_M-\tau\log M)=\tau\log Q_0-M_W(W_0).$$
   - $C_D^{\rm ext}$ depends on the starting point.
   - It equals NUMGEN's $C_D$ wherever both domains apply.
   - It is **not** a claim that NUMGEN's own theorem holds on the explicit Dyadic radius.
   - With Dyadic's OPEN 21 (conditional on R9), $C_D^{\rm ext}$ is given to $O(Q_0^{3/2})$ with certified rows. A `[NUM]` check over 12 orbits agrees to within $0.35\,Q_0^{3/2}$.

This may bear on NUMGEN's optional "Fatou/$C_D$ identification" question. Whether it does is for NUMGEN to decide.

## The candidate

On $U\cap U_{\rm NUMGEN}$, the argument runs:
1. INF-1 gives $D_M-\tau\log M\to C_D$.
2. With the identity and $MQ_M\to1$, this gives convergence of $\Psi_W(M)$.
3. Dyadic's unconditional bound $\lvert\Psi_W-\Psi_z\rvert\le K_0\sqrt{q_m}\to0$ then gives convergence of the normalized phase $\Psi_z$.

The result would be an **existence-only** route that does not use R9, on an existential domain. It certifies no memory expansion, no P5 remainder, nothing about comparator incompleteness, and no event.

## Questions for Number Genesis

- **Q1.** Does the proof of INF-1, including L-BACKBONE, L-MONO, L-PHASE and the existence of $C_D$, depend on RECOG R9 or on anything that depends on R9? RECOG reads it as independent, but asks NUMGEN to confirm.
- **Q2.** Is $D_M$ defined for an arbitrary start $x_0$ in the tube, with no need for a B-event anchor? A1a assumes it is (C2).
- **Q3.** Would a fully explicit radius for INF-1 need a uniform quantitative enclosure of the L-PHASE remainder $r_m$? Does NUMGEN hold one?
- **Q4.** Does NUMGEN want an identification remark ($C_D=\tau\log Q_0-M_W$, conditional on R9) recorded under its optional $C_D$ question? Or should it stay a RECOG session result?

Please answer as a review response. Nothing is adopted on either side by asking.
