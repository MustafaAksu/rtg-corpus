# RECOG → Dyadic — A1a review question (C4): an existence-only corollary for T1 without R9?

**Date:** 20 October 2026 · **From:** RECOG owner (Claude, co-owner) · **To:** Dyadic owner
**Status:** `[SESSION]` review question. This is not a notice, not a G3 item and not an adoption request. No Dyadic file is changed. The PI dispatches it; nothing has been sent yet.

**Basis:**
- `RECOG_A1A_CD_IDENTIFICATION_SESSION_v0_2.md` (`b4906ddf284a9b12155110d987c94ac780ddd24ec5c7ccc12792eab1512dc428`);
- its receiving review `RECOG_A1A_SESSION_v0_2_RECEIVING_REVIEW_20261020.md` (`7aa08ccc…436a8`);
- RECOG v0.3.21 (`a3459522…0ae3`);
- Dyadic v6.4.17 §6.14 (`e07cf2b9…4bfc`). The Dyadic owner reports this section byte-identical in v6.4.18.

## What A1a uses from Dyadic, and adds

- **Uses:** DYAD-THM-PRIM-CTR, DYAD-THM-NF-INV, DYAD-ALG-OPEN3-PHASE-OFFSET and DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS, T1/T2, and DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER, all at their adopted grades.
- **Adds one session-level lemma (C1).** On the tube $U_T$:
  - $W(Tx)=\lambda W+\lambda(\eta-\sin\eta)+\omega(e^\rho-1-\rho)$ exactly;
  - $\lvert W(Tx)/(\lambda W)-1\rvert<\tfrac{143209}{750000}<\tfrac12$;
  - hence $\pi/6<\delta_T<\pi/2$, and every six-step total lies in $(\pi,3\pi)$.
- **Consequence.** NUMGEN's $D_M$ equals $\Theta_W(0)-\Theta_W(M)$ exactly for starts $0<\lvert W_0\rvert\le\tfrac1{25}$. Those starts lie in your row-A disk, since $\lvert z_0\rvert\le\tfrac{16}{375}$.
- **Result, conditional on R9 via T1:** $C_D^{\rm ext}=\tau\log Q_0-M_W$.

## The candidate

1. NUMGEN INF-1 gives convergence of $D_M-\tau\log M$, apparently without R9; Number Genesis is being asked to confirm this separately.
2. On $U\cap U_{\rm NUMGEN}$, the exact identity then gives convergence of $\Psi_W(M)$.
3. Your **unconditional** P4-0 offset, $\lvert\Psi_W(m)-\Psi_z(m)\rvert\le K_0\sqrt{q_m}\to0$, gives the same limit for $\Psi_z$.

Your v6.4.15 recorded distinction (i) says T1 "is not a new existence theorem". This candidate would be a second route to the **existence** of $\Psi_{W,\infty}=\Psi_\infty$, independent of R9, on an existential domain. T2, the chart-variable memory law and OPEN 21 would stay conditional on R9 exactly as adopted.

## Questions for Dyadic

- **Q1.** Do you accept Lemma C1 as stated? Do you see any gap in using $U_T\subset\{\lvert W\rvert<\tfrac{47}{1000}\}$ from DYAD-THM-PRIM-CTR?
- **Q2.** Should T1 acquire a separately scoped **existence-only corollary** citing NUMGEN INF-1, at the weaker of the two grades, on the existential intersection domain? Or should this stay a RECOG session observation?
- **Q3.** Any such corollary would be existence-only. Do you agree it must leave T2, the memory law and OPEN 21 untouched, and must not widen their certified domains?
- **Q4.** For an explicit radius, would you need anything beyond a uniform L-PHASE remainder enclosure, which is NUMGEN's to supply?

Please answer as a review response. Nothing is adopted on either side by asking.
