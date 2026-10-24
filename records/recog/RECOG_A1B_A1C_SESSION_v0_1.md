# RECOG A1b/A1c — slip schedule and decoder audit on the explicit start set $U$

**Date:** 23 October 2026 · **Author:** RECOG co-owner (Claude) · **Status:** `[SESSION]` scientific record, **v0.2.2** (v0.1 at commit `a2bf585`; v0.2 at `3b0b232` after review #5630982748 `PROMISING — GAPS FOUND — THM PROMOTION DEFERRED`; v0.2.1 after round-2 review #5631395296 `ROUND-2 CONDITIONAL ACCEPTANCE`: grid-free certificate gates, $K=1.82$, two scope refinements; v0.2.2: one sentence of §4 corrected after review #5638820480 of the theorem candidate — see §7c; dispositions in §7). No DSN is edited; nothing is adopted; grades below are targets for a later cell. PI decision of 23 Oct 2026: `START A1b/A1c — EXPLICIT-U FEASIBILITY AND DECODER AUDIT`.
**Base:** RECOG v0.3.23 (tag `recog-v0.3.23`, `0d583400…a31a`), in particular §6.13b (A1a; RECOG-THM-A1A-PHASE-EXISTENCE-U, FC-21) and §6.16a/§6.16e (F2(b), F2(d)). Owner sources read: NUMGEN `numgen-v1.20.8` §6.6 (canonical B-event predicate, GATE 1, GAP-LOCK Lemmas 1–3, `NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT`); Dyadic `dyad-v6.4.22` §6.14 (`DYAD-THM-LPHASE-ROWA-REMAINDER` (B) and (R), `DYAD-THM-PRIM-CTR`). Plan: `records/recog/RECOG_STUDY_PLAN_2026-10-19_r1.md` §3 A1b/A1c and Appendix A.1.
**Question (PI):** does FC-21's explicit domain $U$ carry the slip schedule and the asymptotic-phase readout, or must the results stay on $U\cap U_{\rm NUMGEN}$? Then: what does a token record determine, from which data, where, and under which assumptions — kept apart from any token-to-memory write-through (C2), which this cell does not address.
**Certificate (v0.2):** `evidence/recog/scripts/recog_a1b_sixstep_deficit_cert.py` — exact six-step jet in $\mathbb Q(i\sqrt3)$ to degree 9, Dyadic tail ceiling, explicit grid-free deficit bounds on all of $U_T$ in exact rational arithmetic (G1–G8 and two negative controls PASS; output `evidence/recog/a1b_a1c/a1b_sixstep_deficit_cert.json`).
**Illustration:** `evidence/recog/scripts/recog_a1b_a1c_explicit_u.py` (sandbox, float64; `[NUM]`, not a proof input); outputs in `evidence/recog/a1b_a1c/`.

## 0. Summary

1. **A1b on explicit $U$: feasible.** For every $x_0\in U$, with no NUMGEN existential tube and no R9: the canonical B-events are exactly the $2\pi$-crossings of the principal-increment lift (Lemma A); for every $y\in U_T$ the six-step deficit $\Delta(y)=2\pi-\Lambda_6(y)$ satisfies $\Delta(y)>0.927\,\tau Q(y)>0$ and $|\Delta(y)-\tau Q(y)|<1.82\,Q(y)^{3/2}$ (Lemma C′, certified grid-free from rational ceilings on the exact six-step jet and the Dyadic tail ceiling); every return gap is $6$ or $7$ and there are infinitely many $7$-gaps (Lemma B, now from Lemma C′ for the $5$-gap exclusion and from the Dyadic (B) bound for the $8$-gap exclusion); the exact event identity $G_{n_j}=C+\tfrac\pi3s_j-o_j$ holds with the gap criterion $g_{j+1}=7\iff o_j<\Delta_j$; hence the slip schedule
$$\tau\,\psi(a+M_k)-(k-1)\tfrac\pi3=L+\varepsilon_k,\qquad L=\tfrac\pi3n_0-2\pi\ell_0+\Psi_{W,\infty},\qquad a=Q_0^{-1},\qquad |\varepsilon_k|=O\bigl(Q_{M_k}^{1/2}\bigr),$$
with $\psi$ the digamma function, explicit $|\varepsilon_k|\le\tau Q+1.82Q^{3/2}+5\arcsin(0.705\sqrt Q+0.257Q)+\tau|S^{\rm tail}_{M_k}|+|R^{\rm tail}_{M_k}|$ with $Q$ the largest amplitude in the $k$-th slip block ($\Delta_{j_k}\le\tau Q+KQ^{3/2}$ by Lemma C′; the tail sums are FC-21's) — an a-priori error envelope, not yet a decoder interval computable from the declared data alone (that needs uniform majorants via $Q_m\le Q_0/(1+Q_0m/2)$; §6, 1‴), and $M_{k+1}/M_k\to e^{\pi/(3\tau)}$. The naive form $\tau\log M_k-(k-1)\tfrac\pi3$ differs from $L$ by the known term $-\tau\log(1+a/M_k)$, which is $O(1)$ while $M_k\lesssim a$; the plan's A1b formula is its $k\to\infty$ limit. FC-21 supplies the constant $L$ and the tail terms; every other input is in RECOG v0.3.23 or in the certificate. With the v0.2 certificate the Proposition is a `[THM]` candidate on $U$ (it awaits the cell's own review; nothing is promoted here).
2. **A1c, what a record determines.** The infinite token record $(n_0;\,g_1g_2\ldots)$ alone determines $\Psi_{W,\infty}$ modulo $2\pi$ (hence $\Psi_{z,\infty}$) as the limit of the schedule; this needs no state datum and no value of $a$. For a prefix of $k$ slips: with $a$ known, $\Psi_\infty$ is localized to a window $\le2\max_{j\le k}|\varepsilon_j|$ (explicit; illustration $|\varepsilon_k|\le0.75\sqrt{Q_{M_k}}$); with $a$ unknown, the joint determination of $(a,L)$ from $k$ slips is `[NUM]` only (illustration: $|\hat a-a|/a\le3.5\%$, $|\hat L-L|\le1.3\times10^{-3}$ after $3\times10^5$ blocks) and no general error guarantee is given. The retained memories $M_W$ and $M(z_0)$ are not determined by the schedule limit $L$; whether the *complete* record determines them is the injectivity question of §3 Q1′, left open, with both answers' consequences stated.
3. **Fiber result (new).** On a $C_z$ comparator fiber $\mathcal F_{q,\delta}$ the two records determine $\Psi_{\infty,b}-\Psi_{\infty,a}\equiv\delta+\Delta M\pmod{2\pi}$, so with the fiber datum $\delta$ they determine the R9 pair residue $\Delta M=M(z_b)-M(z_a)$ in the limit — the quantity that the comparator datum does not fix (RECOG-THM-R9-COMPARATOR-INCOMPLETENESS). Numerically $\Delta M$ agrees with R9's leading term $q[\Lambda_1(\alpha+\delta)-\Lambda_1(\alpha)]$ to $3\times10^{-8}$ (bound $2C_2q^2=1.6\times10^{-3}$); this is a `[NUM]` check of the leading term at $q=1.2\times10^{-3}$, outside the certified incompleteness window $q_0<|G|/C_2$, and not a new certified witness. From finite prefixes the record-only decode error is still $2$–$6$ times $|\Delta M|\approx1.8\times10^{-5}$ after $2\times10^6$ steps; on the observed $M^{-1/2}$ law it reaches $|\Delta M|$ near $10^7$ blocks (§5).
4. **What this is and is not.** The record is the sequence of $2\pi$-crossings of the same lift whose asymptotic phase is $\Psi_\infty$: the token stream *reads* the phase, as ticks read a clock. This is C0 in the F3 ladder (both the records and $\Delta M$ are functions of the common phase $\alpha$); it is not an independent retention (the F2(d) $R_{\log}$ verdict for the B/7-gap token is unchanged, now with the finite-versus-limit qualifier the plan asked for), and it is not a token-to-memory write-through (C2 stays absent; RECOG-RESULT-R9-NO-TOKEN-WRITETHROUGH unchanged). For F5 it gives a boundary: readability of $\Psi_\infty$ from tokens is not a witness of write-through; a write-through witness has to show the carrier *changing* at a token, which a readout cannot.

## 1. Objects and conventions

Frame $W=\rho+\omega\eta$, $Q=|W|^2$, $\lambda=e^{i\pi/3}$; on $U_T$, $|\eta|\le\tfrac2{\sqrt3}|W|<0.055$, so the lifted $\eta$ and $\eta_{\rm wrap}$ coincide and NUMGEN's $W=\rho+\omega\eta_{\rm wrap}$ is the Dyadic frame. Start $x_0\in U=\{0<Q_0\le\tfrac1{625}\}$; primitive orbit $x_n=T^nx_0$; block base points $x_{6m}\in U$, intermediate points in $U_T$ (DYAD-THM-PRIM-CTR); block amplitude $Q_m:=Q(x_{6m})$; $a:=Q_0^{-1}$.

Lift: $\theta_n=\arg W(x_n)\in[0,2\pi)$; $\delta_T(x)=\operatorname{Arg}(W(Tx)/W(x))$ (principal); $\hat\varphi_{n+1}=\hat\varphi_n+\delta_T(x_n)$, $\hat\varphi_0=\theta_0$ (`NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT`; the A1a lift). Block phase $\Theta_W(M)=\hat\varphi_{6M}-2\pi M$; $\Psi_W(M)=\Theta_W(M)-\tau\log Q_M$; $\Psi_{W,\infty}=\lim_M\Psi_W(M)$ (exists on $U$: RECOG-THM-A1A-PHASE-EXISTENCE-U). $D_M=2\pi M-(\hat\varphi_{6M}-\hat\varphi_0)=G_{6M}$ with $G_n:=\tfrac\pi3n-(\hat\varphi_n-\hat\varphi_0)$.

Token: canonical B-event $x_n\to x_{n+1}$ with $\eta(x_n)<0\le\eta(x_{n+1})$ and $\rho>0$ on both sides (NUMGEN GATE 1); anchor $n_j$ = index of $x_{n+1}$, $j\ge0$; gap $g_{j+1}=n_{j+1}-n_j$; $s_j$ = number of $7$-gaps among the first $j$ returns; overshoot $o_j=\hat\varphi_{n_j}-2\pi\lfloor\hat\varphi_{n_j}/2\pi\rfloor$; lap $\ell_j=\lfloor\hat\varphi_{n_j}/2\pi\rfloor$. **Record** of the orbit: $\mathcal R(x_0)=(n_0;\,g_1,g_2,\ldots)$, equivalently the set $\{n_j\}$. The $k$-th $7$-gap starts at anchor $j_k$; $n_{j_k}=6M_k+r_k$, $0\le r_k\le5$. These are the F2(b) conventions (`recog_cell_f2b_token_bridge.py`), under which $\ell_0=1$.

## 2. A1b — the slip schedule on explicit $U$

**Inputs** (all in RECOG v0.3.23): RECOG-THM-A1A-LIFT-ALIGNMENT ($\tfrac\pi6<\delta_T<\tfrac\pi2$ on $U_T$; six-step totals in $(\pi,3\pi)$); DYAD-THM-LPHASE-ROWA-REMAINDER, (B) $|W(Ty)/(\lambda W(y))-1|\le\varepsilon\le0.04654$ on $U_T$ and (R) $\hat\varphi_{6(m+1)}-\hat\varphi_{6m}=2\pi-\tau Q_m+r_m$, $|r_m|\le\tfrac{403}{250}Q_m^{3/2}$, at block base points; DYAD-THM-PRIM-CTR ($Q_m\le Q_0/(1+\tfrac12Q_0m)$); RECOG-THM-A1A-PHASE-EXISTENCE-U (FC-21) with its series. The primitive map itself: $W(Tx)=\lambda W+\lambda(\eta-\sin\eta)+\omega(e^\rho-1-\rho)$ (exact; lift-alignment proof).

**Lemma A (B-events are the lift crossings).** `[ALG]` target. For $x_n\in U_T$: the transition $x_n\to x_{n+1}$ is a canonical B-event iff $\lfloor\hat\varphi_{n+1}/2\pi\rfloor=\lfloor\hat\varphi_n/2\pi\rfloor+1$.
*Proof.* ($\Leftarrow$) A crossing with $0<\delta_T<\tfrac\pi2$ means $\theta_n\in(-\tfrac\pi2,0)$ and $\theta_{n+1}=\theta_n+\delta_T\in[0,\tfrac\pi2)$ (principal angles). $\Im W=\tfrac{\sqrt3}2\eta$, so $\eta_n<0\le\eta_{n+1}$. From $\eta_{n+1}-\eta_n=e^{\rho_n}-1-\sin\eta_n$: $e^{\rho_n}-1=\eta_{n+1}+(\sin\eta_n-\eta_n)>0$ because $\sin\eta>\eta$ for $\eta<0$; so $\rho_n>0$, and $\rho_{n+1}=\rho_n-\sin\eta_n>\rho_n>0$. ($\Rightarrow$) $\eta_n<0$ gives $\theta_n\in(-\pi,0)$; $\eta_{n+1}\ge0$ with $\rho_{n+1}>0$ gives $\theta_{n+1}\in[0,\pi)$ (for $\eta_{n+1}=0$, $W=\rho>0$). Then $\theta_{n+1}-\theta_n\in(0,2\pi)$ and $\equiv\delta_T\pmod{2\pi}$ with $\delta_T\in(\tfrac\pi6,\tfrac\pi2)$, so it equals $\delta_T$: the lift crosses a multiple of $2\pi$ at this step. $\square$
Consequences: consecutive anchors are consecutive laps, $\ell_j=\ell_0+j$ (no step advances by $2\pi$); $o_j\in[0,\delta_T(x_{n_j-1}))\subset[0,\tfrac\pi2)$. NUMGEN certifies lift-free detectability on its existential tube; on $U_T$ it is this lemma.

**One-step pointwise bound (kept from v0.1).** With $\varepsilon(x):=W(Tx)/(\lambda W(x))-1=[\lambda(\eta-\sin\eta)+\omega(e^\rho-1-\rho)]/(\lambda W)$: on $U_T$, $|\eta-\sin\eta|\le\tfrac{|\eta|^3}6\le\tfrac4{9\sqrt3}|W|^3$ and $|e^\rho-1-\rho|\le\tfrac{\rho^2}2e^{|\rho|}\le0.705|W|^2$, so $|\varepsilon(x)|\le0.705\sqrt Q+0.257Q$ and
$$|\delta_T(x)-\tfrac\pi3|\le\arcsin\bigl(0.705\sqrt{Q(x)}+0.257Q(x)\bigr)\qquad(\text{pointwise form of L-MONO on }U_T).$$

**Lemma C′ (six-step deficit on all of $U_T$).** `[ALG via exact computation + imported ceiling]`; certificate `recog_a1b_sixstep_deficit_cert.py`. For $y\in U_T$ the six one-step increments lie in $(\tfrac\pi6,\tfrac\pi2)$, so $\Lambda_6(y)=2\pi+\operatorname{Arg}(W(T^6y)/W(y))$ (lift alignment). The raw six-step map is $W(T^6y)=W+\mu|W|^2W+\sum_{d=4}^{9}F_d(W,\bar W)+R_{\ge10}$ with the $F_d$ computed exactly in $\mathbb Q(i\sqrt3)$ by six-fold composition (degree-2 part zero, degree-3 part $\mu|W|^2W$ with $\mu=-\tfrac12-\tfrac{2\sqrt3}3i$, real-ray quartic $-\tfrac{5+25i\sqrt3}{48}$ as in Dyadic §6.2; the coefficient sums $c_7=2.0788$, $c_8=1.1531$, $c_9=1.7621$ reproduce Dyadic's vector ceilings $\tfrac{2079}{1000},\tfrac{577}{500},\tfrac{1763}{1000}$) and $|R_{\ge10}|\le332000|W|^{10}$ on $|W|\le\tfrac1{16}$ (DYAD-THM-NF-REM ingredients). With $c_4=1.7300$, $c_5=0.9376$, $c_6=1.9832$: $W(T^6y)/W(y)=1+\mu Q+E$, $|E|\le e(Q):=\sum_{d=4}^9c_dQ^{(d-1)/2}+332000Q^{9/2}$, and $\Delta(y):=2\pi-\Lambda_6(y)=-\operatorname{Arg}(1+\mu Q+E)$. Grid-free bounds (round-2 route, exact rational arithmetic): with $t=|W|\le T=\tfrac{47}{1000}$ and rational ceilings $r\ge|{\rm coefficient}|$ (checked by $r^2\ge a^2+3b^2$), $H:=\sum_{d=4}^9c_dT^{d-4}+332000T^6=1.78218<\tfrac{1783}{1000}$, so $e(Q)\le Ht^3$ on $U_T$; with $d=T^2/2+HT^3$, $B=(\tau+HT)/(1-d)$ and $\tau$ bracketed by $1.154700538<\tau<1.154700539$, the elementary arctan bounds give uniformly on $U_T$
$$\frac{\Delta-\tau t^2}{t^3}\le\frac{H+\tau(T/2+HT^2)}{1-d}=1.8170<1.818,\quad\frac{\tau t^2-\Delta}{t^3}\le H(1+\tau T^2)+\tfrac{B^3T^3}3=1.7876<1.788,\quad\frac{\Delta}{\tau t^2}\ge\frac{1-HT/\tau}{1+HT^3}-\frac{B^3T^4}{3\tau}=0.92725>0.927,$$
hence
$$\Delta(y)>0.927\,\tau Q(y)>0,\qquad|\Delta(y)-\tau Q(y)|<K\,Q(y)^{3/2},\quad K=1.82\ \text{(published ceiling)}.$$
(The 40-digit pointwise evaluation $\sup e/(\tau Q)=0.0725$ and the 50-point grid value $1.8162$ of v0.2 are kept in the certificate as an illustration only; v0.2's "$K=1.8162$" was a downward rounding and is withdrawn.) Negative controls: $\Im\mu\to+\tau$ makes the deficit non-positive; a tail ceiling inflated by $10^8$ fails the positivity gate. Consequences: $\Lambda_6(y)<2\pi$ at **every** point of $U_T$, not only at block base points; $\Delta_j=\tau Q(x_{n_j})+O(Q^{3/2})\to0$ along anchors. (This replaces v0.1's Lemma C and its Lipschitz route; the observed $|\Delta/Q-\tau|\le1.44\sqrt Q$ sits under $K$.) $\square$

**Lemma B (alphabet $\{6,7\}$; infinitely many $7$-gaps).** `[ALG]` target. ($\ge8$ excluded.) On $U_T$, $|\delta_T-\tfrac\pi3|\le\arcsin0.04654$ by (B), so $\Lambda_7(y)>\tfrac{7\pi}3-0.326>2\pi\ge2\pi-o_j$ for every $y$: a gap $\ge8$ would need $\Lambda_7(x_{n_j})<2\pi-o_j$. ($\le5$ excluded; corrected in v0.2.) A gap $\le5$ would need $o_j+\Lambda_5(x_{n_j})\ge2\pi$. Since $o_j<\delta_T(x_{n_j-1})$ (the lift was below the lap before the anchor step), $o_j+\Lambda_5(x_{n_j})<\delta_T(x_{n_j-1})+\Lambda_5(x_{n_j})=\Lambda_6(x_{n_j-1})<2\pi$ by Lemma C′ at the pre-anchor point $x_{n_j-1}\in U_T$. (v0.1 argued from $\Lambda_5<2\pi$ alone, which does not give $\Lambda_5<2\pi-o_j$; the review is right.) Hence $g_{j+1}\in\{6,7\}$, exactly
$$g_{j+1}=7\iff\Lambda_6(x_{n_j})<2\pi-o_j\iff0\le o_j<\Delta_j:=2\pi-\Lambda_6(x_{n_j}).$$
Counting crossings in $6M$ steps: $N_B(6M)=M-D_M/2\pi+O(1)$ (Lemma A), and $s(M)=6(M-N_B(6M))+O(1)=\tfrac3\pi D_M+O(1)=\tfrac{3\tau}\pi\log M+O(1)\to\infty$ by FC-21; so infinitely many $7$-gaps (NUMGEN's Lemma 2 count law, on explicit $U$). $\square$ (Load-bearing inputs: Lemma C′ for the $5$-gap exclusion, the Dyadic (B) constant for the $8$-gap exclusion; RECOG's own bound $\delta_T\in(\tfrac\pi6,\tfrac\pi2)$ is too weak for either.)

**Proposition (A1b on $U$).** `[THM]` candidate (every constant explicit; the cell's review is pending). For $x_0\in U$ and the $k$-th $7$-gap at $n_{j_k}=6M_k+r_k$:
1. Exact event identity (Lemma A and the alphabet): $G_{n_j}=C+\tfrac\pi3s_j-o_j$ with $C=\tfrac\pi3n_0-2\pi\ell_0+\hat\varphi_0$; at $j=j_k$, $s_{j_k}=k-1$ and $0\le o_{j_k}<\Delta_{j_k}$.
2. Partial block: $D_{M_k}=G_{n_{j_k}}-\sum_{i<r_k}\bigl(\tfrac\pi3-\delta_T(x_{6M_k+i})\bigr)$, so $|D_{M_k}-C-(k-1)\tfrac\pi3|\le\Delta_{j_k}+5\arcsin(0.705\sqrt{Q}+0.257Q)$ with $Q$ the largest amplitude among the points involved (one-step pointwise bound above), $=O(\sqrt{Q_{M_k}})$. This is NUMGEN's GAP-LOCK Lemma 3 with an explicit error order, on explicit $U$.
3. Harmonic form (FC-21): with $S_M=\sum_{m<M}(Q_m-\tfrac1{a+m})$, $R_M=\sum_{m<M}r_m$ and $H(a)=-\psi(a)$,
$$D_M=\tau\bigl(\psi(a+M)-\psi(a)\bigr)+\tau S_M-R_M=C_D^{\rm ext}+\tau\psi(a+M)-\tau(S_\infty-S_M)+(R_\infty-R_M),$$
and $C_D^{\rm ext}=\hat\varphi_0-\Psi_{W,\infty}$ (finite-block identity). Therefore
$$\tau\psi(a+M_k)-(k-1)\tfrac\pi3=L+\varepsilon_k,\qquad L=C-C_D^{\rm ext}=\tfrac\pi3n_0-2\pi\ell_0+\Psi_{W,\infty},$$
$|\varepsilon_k|\le\Delta_{j_k}+5\arcsin(\cdots)+\tau|S^{\rm tail}_{M_k}|+|R^{\rm tail}_{M_k}|=O(\sqrt{Q_{M_k}})=O((a+M_k)^{-1/2})$. ($\hat\varphi_0$ cancels between $C$ and $C_D^{\rm ext}$; $L$ is independent of the lift representative because $\ell_0$ and $\Psi_\infty$ shift together.)
4. Limits: $\tau\log M_k-(k-1)\tfrac\pi3=L-\tau\log(1+a/M_k)+O(M_k^{-1})+\varepsilon_k\to L$ and $M_{k+1}/M_k\to e^{\pi/(3\tau)}$. The plan's A1b formula is item 4; item 3 is its finite-$k$ form.

Illustration (12 orbits in $U$, $2\times10^6$ primitive steps, §5): predicate–crossing mismatches $0$; alphabet $\{6,7\}$; identity spread $\le10^{-10}$; criterion violations $0$; $\max\Lambda_5=5.236<2\pi<7.33=\min\Lambda_7$; $|\varepsilon_k|/\sqrt{Q_{M_k}}\le0.75$ at every slip; the naive form's deviation is reproduced by $-\tau\log(1+a/M_k)$ to $\le0.6\sqrt Q$.

**What FC-21 buys.** Before: the schedule needed INF-1 ($U_{\rm NUMGEN}$, no radius) and gave $o(1)$. Now: on all of $U$, with $L$ identified as $\tfrac\pi3n_0-2\pi\ell_0+\Psi_{W,\infty}$ and $|\varepsilon_k|=O((a+M_k)^{-1/2})$. Not supplied: anything outside $U$; an R9-free value of $M_W$ (the schedule reads $\Psi_\infty$, not $M_W$); sharper constants than Lemma C's crude ones.

**Custody.** GAP-LOCK Lemmas 1–3 and INF-1 stay NUMGEN's. The explicit-$U$ instances above are consequences of RECOG and Dyadic inputs, like FC-21; if adopted they are registered under RECOG identity (proposed `RECOG-THM-A1B-SLIP-SCHEDULE-U`, with Lemmas A–C as named sub-statements) and notified to NUMGEN as information. The B-event predicate and the slip law's wording remain NUMGEN's.

## 3. A1c — decoder audit

A *decoder* is a map from the token record (and declared side data) to a quantity of the orbit. Three questions: (Q1) what does the infinite record determine; (Q2) what does a finite prefix determine; (Q3) on a comparator fiber, is the R9 residue decodable.

**Q1 — infinite record (schedule decoder).** From item 4 of the Proposition, $L=\lim_k[\tau\log M_k-(k-1)\tfrac\pi3]$ is a function of $\mathcal R(x_0)$ alone ($n_0$ and the $7$-gap positions), with no state datum and without knowing $a$. Hence
$$\Psi_{W,\infty}\equiv L-\tfrac\pi3n_0+2\pi\ell_0\pmod{2\pi}$$
is determined by the record, and $\Psi_{z,\infty}=\Psi_{W,\infty}$ (RECOG-THM-A1A-PHASE-EXISTENCE-ALT with H-NG from FC-21; the lift tie $\Theta_W(0)=\Theta_z(0)+D_\Theta(z_0)$ changes nothing mod $2\pi$). The block clock $a$ enters only through $\tau\psi(a+M_k)$; late slips are insensitive to it ($\partial_a\approx\tau/M_k$); a two-parameter least-squares decoder $(\hat a,\hat L)$ reads it from the early slips (illustration: $|\hat a-a|/a\le3.5\%$, $|\hat L-L|\le1.3\times10^{-3}$ after $3\times10^5$ blocks) — a `[NUM]` observation with no general error guarantee; the schedule limit does not determine $a$.

**Q1′ — does the complete record determine the start state? (open; raised by the review).** Record level sets have empty interior (a record-constant open set would make $\Psi_\infty$ locally constant, which it is not). More is plausible: two starts with the same $\Psi_\infty$ but different $a$ have lifted phases that approach each other only like $\tau\log(Q_{a,m}/Q_{b,m})=O(m^{-1/2})$, and the expected number of crossing steps at which the section separates them, $\sum_m O(m^{-1/2})$ per block, diverges, so their records should differ infinitely often. If the record map is injective, then *every* orbit quantity — $M_W$, $M(z_0)$, $z_0$ itself — is a function of the complete record, and the $R_{\log}$/$R_{\rm ind}$ distinction of F2(d) rests entirely on the finite-versus-limit qualifier; if it is not, there are distinct starts with identical token histories, which is a direct non-recoverability witness. Either way the statement "$M_W$ is not determined by the record" of v0.1 is withdrawn: what is established is that the schedule limit $L$ does not determine $M_W$ (it needs $\Psi_W(x_0)$). The injectivity question is the next analytic item (§6). *Scope (round-2 refinement):* even a positive answer would establish only retrospective reconstruction of the start state from the complete itinerary; it would not turn R9's physically registered carrier $M$ into $R_{\log}$ nor establish token-gated write-through — F2(d)'s carrier/evidence distinction stays separate from the information content of the infinite record.

**Q2 — finite prefix.** *With $a$ known:* the $k$-th slip gives $|L-(\tau\psi(a+M_k)-(k-1)\tfrac\pi3)|\le|\varepsilon_k|$ with the explicit bound of the Proposition, so $L$ lies in a window of width $2|\varepsilon_k|$ (illustration $\le1.5\sqrt{Q_{M_k}}\approx1.5(a+M_k)^{-1/2}$); the resolution improves like $M_k^{-1/2}$, a factor $e^{-\pi/(6\tau)}\approx0.64$ per slip, and any two starts whose $L$ differ by less than the window can share the prefix. *With $a$ unknown:* the $k$ slips give $k$ equations in $(a,L)$ with errors $\varepsilon_j$; the joint window is not derived here (the illustration's least-squares fit is `[NUM]` only). What is proved for unknown $a$ is the limit statement of Q1.

**Q3 — comparator fiber.** For a pair on $\mathcal F_{q,\delta}$ ($q_a=q_b=q$, $\Theta_{z,b}(0)-\Theta_{z,a}(0)=\delta$), RECOG-THM-R9-COMPARATOR-INCOMPLETENESS gives $\lim_m(\Theta_{b,m}-\Theta_{a,m})=\delta+\Delta M$, so
$$\Psi_{z,\infty,b}-\Psi_{z,\infty,a}=\delta+\Delta M,\qquad\Delta M=M(z_b)-M(z_a),$$
and by Q1 the left side is $(L_b-L_a)-\tfrac\pi3(n_{0,b}-n_{0,a})+2\pi(\ell_{0,b}-\ell_{0,a})\pmod{2\pi}$: the two records plus the fiber datum $\delta$ determine $\Delta M$ in the limit (as a real number, since $|\Delta M|\ll2\pi$). $M(z_a)$ itself is not determined ($\Psi(z_a)$ needs the state); the *difference* needs only the comparator datum.
Illustration ($q=1.225\times10^{-3}$, $\delta=\tfrac\pi6$, $\alpha\in\{0,0.5,1,1.5\}$): the direct $z$-track value $\Delta\Psi_\infty-\delta$ equals R9's leading $q[\Lambda_1(\alpha+\delta)-\Lambda_1(\alpha)]=-2q\Lambda_1(\alpha)$ to $3\times10^{-8}$ (certified bound $2C_2q^2=1.6\times10^{-3}$) — a `[NUM]` check of the leading term on the exact map at an amplitude outside the certified incompleteness window ($q_0<|G|/517=1.48\times10^{-5}$); it is not a certified witness and is not used as one. Record-only decode after $2\times10^6$ steps: see §5 for the error against $|\Delta M|\approx1.8\times10^{-5}$.

**Resolution cost.** To read $\Delta M$ from prefixes the decode error must fall below $|\Delta M|\approx2|G|q$. With the single-orbit window $\approx0.75(a+M)^{-1/2}$ this needs $M\gtrsim(0.75/(2|G|q))^2\approx10^9$ blocks at $q=\tfrac1{625}$; the pair errors on the sampled fibers cancel to $\approx0.05(a+M)^{-1/2}$ (observed, §5), which would bring the threshold to $\sim10^7$ blocks. Either way the lattice memory is token-readable in principle and invisible to every token prefix of the lengths used so far.

**Classification.**

| Quantity | Decoder input | Domain and assumptions | Status |
|---|---|---|---|
| $\Psi_{W,\infty}=\Psi_{z,\infty}$ (mod $2\pi$) | infinite record $\mathcal R$; no state datum | $x_0\in U$; Lemmas A–C, FC-21 | determined (limit); `[ALG]` target |
| $a=Q_0^{-1}$ | early slips of $\mathcal R$ | same | `[NUM]`: relative error $\le3.5\%$ on the runs; no guarantee; not determined by the schedule limit |
| $\Psi_\infty$ from $k$ slips | prefix, $a$ known | same | window $2|\varepsilon_k|$, a-priori envelope (not yet computable from declared data alone); illustration $\le1.5(a+M_k)^{-1/2}$ |
| $\Psi_\infty$ from $k$ slips | prefix, $a$ unknown | same | joint $(a,L)$ window not derived; `[NUM]` only |
| $M_W$, $M(z_0)$ | schedule limit $L$ | — | not determined by $L$ (needs $\Psi_W(x_0)$); determination by the complete record = injectivity, open (Q1′) |
| $\Delta M$ on $\mathcal F_{q,\delta}$ | two records + $\delta$ | pair in $U$; same lemmas; R9 only to name $\Delta M$ | determined (limit); from prefixes only after $M\sim(c/2|G|q)^2$, $c\in[0.05,0.75]$ |
| any token-to-memory write-through (C2) | — | — | not addressed; unchanged (RECOG-RESULT-R9-NO-TOKEN-WRITETHROUGH) |

## 4. Consequences for R6 and F5 (proposals, not adoptions)

- **F2(d) anti-tautology guard:** add the finite-versus-limit qualifier the plan asked for: $\Psi_\infty$ is a function of the complete token history (so $R_{\log}$-type in the limit); the finite-prefix envelope tends to $0$ as $k\to\infty$, and within the illustration's observed horizon ($M\lesssim3.3\times10^5$) the prefix window exceeds $|\Delta M|$ by a factor $2$–$6$ (`[NUM]`; v0.2.1 said "every finite prefix leaves a window $\gg|\Delta M|$", which is not true in general — corrected in v0.2.2). The $R_{\log}$ verdict for the B/7-gap token stands. $R_{\rm ind}$ for R9's $M$ stands as a statement about finite histories; a positive Q1′ would make $M$ a function of the complete history (information content) without changing its carrier status, so the $R_{\rm ind}$ classification is not automatically lowered by Q1′.
- **F3 ladder:** the fiber result is an exact C0 statement — the records and $\Delta M$ are both functions of the common phase $\alpha$ — not a C1 residual and not C2. "Comparator-invisible" memory is token-visible, in the limit, because the tokens are phase crossings. No grade changes.
- **F5 scoping:** a token stream that is a readout of the carrier's phase cannot witness write-through; the sufficient witness (PI's scope) must show the carrier's update changing at a token (non-smooth or event-gated), which no readout does. Negative, and it narrows F5's search: candidates must be carriers that are *not* functions of the phase the tokens already read.
- **R6 residual:** unchanged. Tokenisation/selection principle still missing.

## 5. Certificate and illustration data

**Certificate** `evidence/recog/scripts/recog_a1b_sixstep_deficit_cert.py` → `evidence/recog/a1b_a1c/a1b_sixstep_deficit_cert.json` (gates G1–G8 and negative controls NC1, NC2 PASS; 4 s). Degree parts of the exact six-step jet: 1, 0, 1, 4, 6, 7, 8, 9, 10 terms for degrees 1–9. Coefficient sums $c_4\ldots c_9=1.7300,\ 0.9376,\ 1.9832,\ 2.0788,\ 1.1531,\ 1.7621$ (40-digit evaluation of exact $\mathbb Q(i\sqrt3)$ coefficients, $|a+bi\sqrt3|=\sqrt{a^2+3b^2}$). Grid-free (G6–G8, exact rationals): rational coefficient-sum ceilings, $H=1.78218<1.783$; upper branch $1.8170<1.818$, lower $1.7876<1.788$, positivity ratio $0.92725>0.927$; published $K=1.82$. Illustration (40-digit, G3/G4): $e/(\tau Q)=0.0725$ at $Q_{\max}=\tfrac{2209}{10^6}$; grid value $1.8162$. Imported: the tail ceiling $332000|W|^{10}$ on $|W|\le\tfrac1{16}$ (DYAD-THM-NF-REM ingredients) — the only non-RECOG input besides the tube radius.

`evidence/recog/scripts/recog_a1b_a1c_explicit_u.py`, run with $N=2\times10^6$ primitive steps per orbit; output `evidence/recog/a1b_a1c/a1b_a1c_explicit_u_2e6.json`, console `…_output.txt`. Float64; the event-anchored lift of F2(b) rev. 2; $h^{-1}$ from the F2(b) module (DYAD-ALG-NF6 coefficients regenerated there, $h_2$ checked against the registered value). $\Psi_\infty$ is estimated by $\Phi(z_M)=\Psi_z(M)+q_Mg(\Theta_M)$ at the last block (R9's averaging function as an estimator; its drift over the last decade of blocks is $<10^{-10}$).

| $Q_0$ | $\theta_0$ | events | predicate≠crossing | gaps | identity spread | criterion viol. | $\max\Lambda_5$ | $\min\Lambda_7$ | $\max|\Delta/Q-\tau|/\sqrt Q$ | slips | $\max_k|\varepsilon_k|/\sqrt{Q_{M_k}}$ | $\hat a$ (true) | $|\hat L-L|$ | last $M_{k+1}/M_k$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.6e-03 | 0.3 | 333332 | 0 | [6, 7] | 3e-10 | 0 | 5.236 | 7.328 | 1.44 | 7 | 0.55 | 611 (625) | 1.3e-03 | 2.490 |
| 1.6e-03 | 1.7 | 333332 | 0 | [6, 7] | 4e-10 | 0 | 5.236 | 7.329 | 1.43 | 7 | 0.75 | 646 (625) | 9.6e-04 | 2.486 |
| 1.6e-03 | 3.9 | 333332 | 0 | [6, 7] | 5e-10 | 0 | 5.236 | 7.329 | 1.43 | 7 | 0.73 | 647 (625) | 9.5e-04 | 2.485 |
| 1.6e-03 | 5.1 | 333332 | 0 | [6, 7] | 4e-10 | 0 | 5.236 | 7.329 | 1.42 | 7 | 0.33 | 614 (625) | 9.7e-04 | 2.484 |
| 1.0e-03 | 0.3 | 333332 | 0 | [6, 7] | 3e-10 | 0 | 5.236 | 7.329 | 1.42 | 7 | 0.54 | 983 (1000) | 9.8e-04 | 2.489 |
| 1.0e-03 | 1.7 | 333332 | 0 | [6, 7] | 4e-10 | 0 | 5.236 | 7.330 | 1.43 | 6 | 0.75 | 1026 (1000) | 8.3e-04 | 2.500 |
| 1.0e-03 | 3.9 | 333332 | 0 | [6, 7] | 5e-10 | 0 | 5.236 | 7.330 | 1.44 | 6 | 0.72 | 1027 (1000) | 8.9e-04 | 2.498 |
| 1.0e-03 | 5.1 | 333333 | 0 | [6, 7] | 3e-10 | 0 | 5.236 | 7.330 | 1.44 | 6 | 0.33 | 985 (1000) | 8.7e-04 | 2.495 |
| 4.0e-04 | 0.3 | 333332 | 0 | [6, 7] | 3e-10 | 0 | 5.236 | 7.330 | 1.42 | 6 | 0.56 | 2471 (2500) | 7.2e-04 | 2.508 |
| 4.0e-04 | 1.7 | 333332 | 0 | [6, 7] | 5e-10 | 0 | 5.236 | 7.330 | 1.43 | 5 | 0.72 | 2540 (2500) | 6.8e-04 | 2.535 |
| 4.0e-04 | 3.9 | 333333 | 0 | [6, 7] | 3e-10 | 0 | 5.236 | 7.330 | 1.44 | 5 | 0.70 | 2540 (2500) | 7.0e-04 | 2.529 |
| 4.0e-04 | 5.1 | 333333 | 0 | [6, 7] | 3e-10 | 0 | 5.236 | 7.330 | 1.44 | 5 | 0.33 | 2477 (2500) | 6.4e-04 | 2.523 |

Target $e^{\pi/(3\tau)}=2.4766$; $2\pi=6.283$; the uniform one-step deviation $\max|\delta_T-\pi/3|=0.452\sqrt Q\le0.0178<\arcsin0.04654=0.0466$ on every orbit.

Fiber pairs ($q=1.225\times10^{-3}$, $\delta=\pi/6$), after $2\times10^6$ steps ($M\approx3.3\times10^5$ blocks, $k=6$ common slips):

| $\alpha$ | $\Delta M$ (direct) | $\Delta M-$ R9 leading | naive decode error | decode error, true $a$ | record-only decode error | error$/|\Delta M|$ |
|---|---|---|---|---|---|---|
| 0.0 | 1.876e-05 | 1.3e-08 | -3.0e-03 | -6.6e-05 | -9.2e-05 | 4.9 |
| 0.5 | -1.859e-05 | -2.1e-08 | 3.1e-03 | -3.1e-05 | 1.0e-04 | 5.6 |
| 1.0 | 1.805e-05 | 2.9e-08 | -3.1e-03 | -3.0e-04 | -3.7e-05 | 2.1 |
| 1.5 | -1.715e-05 | -3.7e-08 | 3.2e-03 | 1.0e-04 | 7.0e-05 | 4.1 |

R9 bound on the remainder of $\Delta M$: $2C_2q^2=1.6\times10^{-3}$. The record-only pair error is $\approx0.05\,(a+M)^{-1/2}$ on these runs (the two orbits' errors largely cancel; single-orbit windows are $\approx0.75\sqrt Q$), so the pair decode would reach $|\Delta M|$ near $M\sim10^7$ blocks, about $6\times10^7$ primitive steps per orbit — a PI-machine run, not a sandbox one. The cancellation is observed, not proved; the single-orbit estimate of §3 stands as the bound.

Not a proof input: the runs illustrate the lemmas' inequalities and the schedule's error order on sampled orbits; the inequalities are proved (A, B) or proved up to explicit constants (C) in §2.

## 6. Open items and next steps

1. **Done in v0.2/v0.2.1:** Lemma C′ certified grid-free in exact rational arithmetic (`recog_a1b_sixstep_deficit_cert.py`, gates G6–G8); Lemma B repaired. Remaining for `[THM]`: the cell's own review of the final wording (round-2 disposition: conditional acceptance; hold the RID until checked).
1′. **Injectivity of the record map (Q1′):** analytic item; a counting argument on crossing-step differences along a $\Psi_\infty$-level set, or a counterexample. Decides the limit form of $R_{\rm ind}$.
1″. **Finite-prefix window with unknown $a$:** derive a joint $(a,L)$ bound from two slips, or record it as `[NUM]` only.
1‴. **Known-$a$ decoder interval from declared data only:** replace $|\varepsilon_k|$ by a majorant computable from $(a,k,M_k)$ using $Q_m\le Q_0/(1+Q_0m/2)$ and FC-21's reciprocal-amplitude/remainder estimates; until then the window is an a-priori envelope.
2. **A1b registration:** proposed RID `RECOG-THM-A1B-SLIP-SCHEDULE-U` in §6.13b, with Lemmas A–C as sub-statements; NUMGEN informed (explicit-domain instance of GAP-LOCK; no custody change).
3. **A1c registration:** the classification as a `[DEF]`/`[RESULT] [from: ALG]` block in §6.16e–f (finite-versus-limit qualifier; fiber decodability as C0), after review.
4. **Long-orbit check on the PI machine:** deferred, as the review recommends, until items 1′ and 1″ are done; then a separate `[NUM]` experiment on whether the pair cancellation follows the $M^{-1/2}$ law (chunked variant of the script needed above $\sim2\times10^7$ steps).
5. **F5:** pose with the readout boundary of §4.

## 7. Review round 1 — dispositions (co-owner review #5630982748 on `a2bf585`)

| Review point | Disposition in v0.2 |
|---|---|
| Lemma A VERIFIED | kept |
| Lemma B GAP: $\Lambda_5<2\pi$ does not exclude a $5$-gap; need $o_j+\Lambda_5(x_{n_j})\le\Lambda_6(x_{n_j-1})<2\pi$ on $U_T$ | accepted; Lemma B rewritten with the reviewer's route; $\Lambda_6<2\pi$ at every point of $U_T$ now certified (Lemma C′) |
| Lemma C CONDITIONAL: explicit constant on all of $U_T$ needed | replaced by Lemma C′: exact six-step jet to degree 9 + Dyadic tail ceiling; $\Delta\ge0.927\tau Q$, $|\Delta-\tau Q|\le1.82Q^{3/2}$ on $U_T$; certificate with negative controls |
| A1b schedule CONDITIONAL on B and C | now `[THM]` candidate; promotion deferred to the cell's review, as the reviewer asked |
| $a$ from early slips: `[NUM]`, no guarantee | stated as such |
| finite-prefix $O((a+M_k)^{-1/2})$ NOT VERIFIED (unknown $a$) | split: known $a$ — explicit window; unknown $a$ — `[NUM]` only, joint bound open (§6, 1″) |
| "$M_W$ not determined by the record" NOT VERIFIED; injectivity needed | withdrawn as stated; replaced by Q1′ (injectivity open) with both consequences; the proved statement is "not determined by the schedule limit $L$" |
| fiber identity VERIFIED; record-based decode CONDITIONAL | kept; the decode is conditional on A1b |
| $\Delta M$ numerics outside the certified window | stated; not used as a certified witness |
| long run not yet | deferred (§6, item 4) |
| C2 still absent | unchanged |

## 7b. Review round 2 — dispositions (co-owner review #5631395296 on `3b0b232`: `ROUND-2 CONDITIONAL ACCEPTANCE`)

| Review point | Disposition in v0.2.1 |
|---|---|
| G4 relied on a 50-point grid; $K=1.8162$ was a downward rounding | accepted; grid-free gates G6–G8 added in exact rational arithmetic along the reviewer's route ($H<1783/1000$, $\tau$ bracket, three uniform inequalities); published $K=1.82$, $\Delta>0.927\tau Q$; grid kept as illustration |
| Lemma B / schedule / limit: accepted conditional on the C′ patch | patch done; `[THM]` RID still held until the cell checks the wording |
| Q1′ injectivity OPEN; even if positive, no automatic $R_{\rm ind}\to R_{\log}$ | scope note added in §3 and §4 |
| known-$a$ prefix: a-priori envelope, not a record-only decoder interval | relabelled; computable majorant listed as §6 item 1‴ |
| unknown-$a$ prefix OPEN; least-squares `[NUM]` | unchanged |
| long run not needed | unchanged (deferred) |
| proceed to A3 | PI decision `A3 AUTHORIZED` (23 Oct 2026); A3 opens as a separate cell |

## 7c. v0.2.2 — correction carried from the theorem-candidate review (#5638820480)

| Point | Disposition |
|---|---|
| §4 F2(d) sentence "every finite prefix leaves a window $\gg|\Delta M|$" is not true in general: the envelope $|\varepsilon_k|\to0$ | corrected; the $|\Delta M|$ comparison is scoped to the illustration's horizon as `[NUM]`. No other change; certificates not rerun. |

