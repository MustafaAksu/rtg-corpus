# RECOG A1b/A1c — slip schedule and decoder audit on the explicit start set $U$

**Date:** 23 October 2026 · **Author:** RECOG co-owner (Claude) · **Status:** `[SESSION]` scientific record, v0.1. No DSN is edited; nothing is adopted; grades below are targets for a later cell. PI decision of 23 Oct 2026: `START A1b/A1c — EXPLICIT-U FEASIBILITY AND DECODER AUDIT`.
**Base:** RECOG v0.3.23 (tag `recog-v0.3.23`, `0d583400…a31a`), in particular §6.13b (A1a; RECOG-THM-A1A-PHASE-EXISTENCE-U, FC-21) and §6.16a/§6.16e (F2(b), F2(d)). Owner sources read: NUMGEN `numgen-v1.20.8` §6.6 (canonical B-event predicate, GATE 1, GAP-LOCK Lemmas 1–3, `NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT`); Dyadic `dyad-v6.4.22` §6.14 (`DYAD-THM-LPHASE-ROWA-REMAINDER` (B) and (R), `DYAD-THM-PRIM-CTR`). Plan: `records/recog/RECOG_STUDY_PLAN_2026-10-19_r1.md` §3 A1b/A1c and Appendix A.1.
**Question (PI):** does FC-21's explicit domain $U$ carry the slip schedule and the asymptotic-phase readout, or must the results stay on $U\cap U_{\rm NUMGEN}$? Then: what does a token record determine, from which data, where, and under which assumptions — kept apart from any token-to-memory write-through (C2), which this cell does not address.
**Illustration:** `evidence/recog/scripts/recog_a1b_a1c_explicit_u.py` (sandbox, float64; `[NUM]`, not a proof input); outputs in `evidence/recog/a1b_a1c/`.

## 0. Summary

1. **A1b on explicit $U$: feasible.** For every $x_0\in U$, with no NUMGEN existential tube and no R9: the canonical B-events are exactly the $2\pi$-crossings of the principal-increment lift (Lemma A); every return gap is $6$ or $7$ and there are infinitely many $7$-gaps (Lemma B); the exact event identity $G_{n_j}=C+\tfrac\pi3s_j-o_j$ holds with the gap criterion $g_{j+1}=7\iff o_j<\Delta_j$ and $\Delta_j=\tau Q(x_{n_j})+O(Q^{3/2})\to0$ (Lemma C); hence the slip schedule
$$\tau\,\psi(a+M_k)-(k-1)\tfrac\pi3=L+\varepsilon_k,\qquad L=\tfrac\pi3n_0-2\pi\ell_0+\Psi_{W,\infty},\qquad a=Q_0^{-1},\qquad |\varepsilon_k|=O\bigl(Q_{M_k}^{1/2}\bigr),$$
with $\psi$ the digamma function, and $M_{k+1}/M_k\to e^{\pi/(3\tau)}$. The naive form $\tau\log M_k-(k-1)\tfrac\pi3$ differs from $L$ by the known term $-\tau\log(1+a/M_k)$, which is $O(1)$ while $M_k\lesssim a$; the plan's A1b formula is its $k\to\infty$ limit. FC-21 supplies the constant $L$ and the error order; the only owner inputs are the ones RECOG v0.3.23 already imports (Lemma C needs two elementary estimates whose explicit constants are left to a certificate).
2. **A1c, what a record determines.** The infinite token record $(n_0;\,g_1g_2\ldots)$ alone determines $\Psi_{W,\infty}$ modulo $2\pi$ (hence $\Psi_{z,\infty}$), and the block clock $a$ only to relative precision $O(\sqrt{Q_0})$. A prefix of $k$ slips localizes $\Psi_\infty$ to a width of order $(a+M_k)^{-1/2}$ (illustration: $|\varepsilon_k|\le0.75\sqrt{Q_{M_k}}$); the map prefix $\mapsto\Psi_\infty$ is not injective at any finite $k$. The retained memories $M_W$ and $M(z_0)$ are not determined by the record: they need the start state.
3. **Fiber result (new).** On a $C_z$ comparator fiber $\mathcal F_{q,\delta}$ the two records determine $\Psi_{\infty,b}-\Psi_{\infty,a}\equiv\delta+\Delta M\pmod{2\pi}$, so with the fiber datum $\delta$ they determine the R9 pair residue $\Delta M=M(z_b)-M(z_a)$ in the limit — the quantity that the comparator datum does not fix (RECOG-THM-R9-COMPARATOR-INCOMPLETENESS). Numerically $\Delta M$ agrees with R9's leading term $q[\Lambda_1(\alpha+\delta)-\Lambda_1(\alpha)]$ to $3\times10^{-8}$ (bound $2C_2q^2=1.6\times10^{-3}$). From finite prefixes the record-only decode error is still $2$–$6$ times $|\Delta M|\approx1.8\times10^{-5}$ after $2\times10^6$ steps; on the observed $M^{-1/2}$ law it reaches $|\Delta M|$ near $10^7$ blocks (§5).
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

**Lemma B (alphabet $\{6,7\}$; infinitely many $7$-gaps).** `[ALG]` target. On $U_T$, $|\delta_T-\tfrac\pi3|\le\arcsin0.04654<0.0466$ by (B), so for every $y\in U_T$: $\Lambda_5(y)<\tfrac{5\pi}3+0.233<2\pi$ and $\Lambda_7(y)>\tfrac{7\pi}3-0.326>2\pi$, where $\Lambda_r(y)=\hat\varphi$-increment over $r$ steps from $y$. At an anchor, the next crossing needs an increment $2\pi-o_j\in(2\pi-\tfrac\pi2,2\pi]$; $\Lambda_5<2\pi-o_j$ excludes gaps $\le5$ and $\Lambda_7\ge2\pi>2\pi-o_j$ excludes gaps $\ge8$. Hence $g_{j+1}\in\{6,7\}$, exactly
$$g_{j+1}=7\iff\Lambda_6(x_{n_j})<2\pi-o_j\iff0\le o_j<\Delta_j:=2\pi-\Lambda_6(x_{n_j}).$$
Counting crossings in $6M$ steps: $N_B(6M)=M-D_M/2\pi+O(1)$ (Lemma A), and $s(M)=6(M-N_B(6M))+O(1)=\tfrac3\pi D_M+O(1)=\tfrac{3\tau}\pi\log M+O(1)\to\infty$ by FC-21; so infinitely many $7$-gaps (NUMGEN's Lemma 2 count law, on explicit $U$). $\square$ (RECOG's own bound $\delta_T\in(\tfrac\pi6,\tfrac\pi2)$ is too weak for this lemma; the Dyadic (B) constant is load-bearing.)

**Lemma C (the deficit at anchors).** `[ALG]` target, constants pending a certificate. For $y=T^rx_{6M}$, $0\le r\le5$:
$$\Lambda_6(y)-\Lambda_6(x_{6M})=\sum_{i<r}\bigl[\delta_T(T^ix_{6(M+1)})-\delta_T(T^ix_{6M})\bigr].$$
With $\varepsilon(x):=W(Tx)/(\lambda W(x))-1=[\lambda(\eta-\sin\eta)+\omega(e^\rho-1-\rho)]/(\lambda W)$: on $U_T$, $|\eta-\sin\eta|\le\tfrac{|\eta|^3}6\le\tfrac4{9\sqrt3}|W|^3$ and $|e^\rho-1-\rho|\le\tfrac{\rho^2}2e^{|\rho|}\le0.705|W|^2$, so $|\varepsilon(x)|\le0.705\sqrt Q+0.257Q$ and
$$|\delta_T(x)-\tfrac\pi3|\le\arcsin\bigl(0.705\sqrt{Q(x)}+0.257Q(x)\bigr)\qquad(\text{pointwise form of L-MONO on }U_T).$$
$\varepsilon$ is Lipschitz in $W$ on $U_T$ ($|\varepsilon(u)-\varepsilon(v)|\le c_\varepsilon|W(u)-W(v)|$, $c_\varepsilon\approx2.5$ from $|DN|\le\eta^2/2+e^{|\rho|}|\rho|$ and $|N|\le0.705|W|^2$), $T$ is Lipschitz in $W$ with constant $1+O(|W|)$, and $|W(x_{6(M+1)})-W(x_{6M})|\le(|\mu|+O(\sqrt Q))Q_M^{3/2}$ from the six-step jet ($|\mu|=\sqrt{19/12}$; DYAD-ALG-SIXSTEP-CUBIC-JET for the cubic part). Hence $|\Lambda_6(y)-\Lambda_6(x_{6M})|\le c_6Q_M^{3/2}$ with a crude $c_6\approx40$, and by (R)
$$\Delta_j=\tau Q_{M(j)}+O\bigl(Q^{3/2}\bigr)\to0\qquad(M(j)=\lfloor n_j/6\rfloor).$$
Illustration: $\Delta_j/Q(x_{n_j})\in[1.158,1.21]$ on all sampled anchors, $|\Delta_j/Q-\tau|\le1.4\sqrt Q$ (so the true constant is far below $40$). $\square$

**Proposition (A1b on $U$).** `[ALG]` target (`[THM]` once Lemma C's constants are certified). For $x_0\in U$ and the $k$-th $7$-gap at $n_{j_k}=6M_k+r_k$:
1. Exact event identity (Lemma A and the alphabet): $G_{n_j}=C+\tfrac\pi3s_j-o_j$ with $C=\tfrac\pi3n_0-2\pi\ell_0+\hat\varphi_0$; at $j=j_k$, $s_{j_k}=k-1$ and $0\le o_{j_k}<\Delta_{j_k}$.
2. Partial block: $D_{M_k}=G_{n_{j_k}}-\sum_{i<r_k}\bigl(\tfrac\pi3-\delta_T(x_{6M_k+i})\bigr)$, so $|D_{M_k}-C-(k-1)\tfrac\pi3|\le\Delta_{j_k}+5\arcsin(0.705\sqrt{Q_{M_k}}+0.257Q_{M_k})=O(\sqrt{Q_{M_k}})$. This is NUMGEN's GAP-LOCK Lemma 3 with an explicit error order, on explicit $U$.
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

**Q1 — infinite record.** From item 4 of the Proposition, $L=\lim_k[\tau\log M_k-(k-1)\tfrac\pi3]$ is a function of $\mathcal R(x_0)$ alone ($n_0$ and the $7$-gap positions), with no state datum and without knowing $a$. Hence
$$\Psi_{W,\infty}\equiv L-\tfrac\pi3n_0+2\pi\ell_0\pmod{2\pi}$$
is determined by the record, and $\Psi_{z,\infty}=\Psi_{W,\infty}$ (RECOG-THM-A1A-PHASE-EXISTENCE-ALT with H-NG from FC-21; the lift tie $\Theta_W(0)=\Theta_z(0)+D_\Theta(z_0)$ changes nothing mod $2\pi$). The block clock $a$ enters only through $\tau\psi(a+M_k)$; late slips are insensitive to it ($\partial_a\approx\tau/M_k$), the early slips fix it to relative precision of order $\sqrt{Q_0}$ (illustration: a two-parameter least-squares decoder $(\hat a,\hat L)$ gives $|\hat a-a|/a\le4\%$ and $|\hat L-L|\le1.8\times10^{-3}$ after $3\times10^5$ blocks). Consistently, record level sets have empty interior (a record-constant open set would make $\Psi_\infty$ locally constant, which it is not), but the schedule decoder does not pin $a$ exactly.

**Q2 — finite prefix.** The first $k$ slips localize $L$ to a window of width $\lesssim2\max_{j\le k}|\varepsilon_j|\approx1.5\sqrt{Q_{M_k}}\approx1.5(a+M_k)^{-1/2}$ (illustration constant). Orbits whose $\Psi_\infty$ differ by less than that share the prefix: the prefix decoder is not injective, and its resolution improves only like $M_k^{-1/2}$, i.e. by a factor $e^{-\pi/(6\tau)}\approx0.64$ per slip.

**Q3 — comparator fiber.** For a pair on $\mathcal F_{q,\delta}$ ($q_a=q_b=q$, $\Theta_{z,b}(0)-\Theta_{z,a}(0)=\delta$), RECOG-THM-R9-COMPARATOR-INCOMPLETENESS gives $\lim_m(\Theta_{b,m}-\Theta_{a,m})=\delta+\Delta M$, so
$$\Psi_{z,\infty,b}-\Psi_{z,\infty,a}=\delta+\Delta M,\qquad\Delta M=M(z_b)-M(z_a),$$
and by Q1 the left side is $(L_b-L_a)-\tfrac\pi3(n_{0,b}-n_{0,a})+2\pi(\ell_{0,b}-\ell_{0,a})\pmod{2\pi}$: the two records plus the fiber datum $\delta$ determine $\Delta M$ in the limit (as a real number, since $|\Delta M|\ll2\pi$). $M(z_a)$ itself is not determined ($\Psi(z_a)$ needs the state); the *difference* needs only the comparator datum.
Illustration ($q=1.225\times10^{-3}$, $\delta=\tfrac\pi6$, $\alpha\in\{0,0.5,1,1.5\}$): the direct $z$-track value $\Delta\Psi_\infty-\delta$ equals R9's leading $q[\Lambda_1(\alpha+\delta)-\Lambda_1(\alpha)]=-2q\Lambda_1(\alpha)$ to $3\times10^{-8}$ (certified bound $2C_2q^2=1.6\times10^{-3}$) — a `[NUM]` cross-check of the corollary on the exact map. Record-only decode after $2\times10^6$ steps: see §5 for the error against $|\Delta M|\approx1.8\times10^{-5}$.

**Resolution cost.** To read $\Delta M$ from prefixes the decode error must fall below $|\Delta M|\approx2|G|q$. With the single-orbit window $\approx0.75(a+M)^{-1/2}$ this needs $M\gtrsim(0.75/(2|G|q))^2\approx10^9$ blocks at $q=\tfrac1{625}$; the pair errors on the sampled fibers cancel to $\approx0.05(a+M)^{-1/2}$ (observed, §5), which would bring the threshold to $\sim10^7$ blocks. Either way the lattice memory is token-readable in principle and invisible to every token prefix of the lengths used so far.

**Classification.**

| Quantity | Decoder input | Domain and assumptions | Status |
|---|---|---|---|
| $\Psi_{W,\infty}=\Psi_{z,\infty}$ (mod $2\pi$) | infinite record $\mathcal R$; no state datum | $x_0\in U$; Lemmas A–C, FC-21 | determined (limit); `[ALG]` target |
| $a=Q_0^{-1}$ | early slips of $\mathcal R$ | same | relative precision $O(\sqrt{Q_0})$; not exact from the schedule |
| $\Psi_\infty$ from $k$ slips | prefix | same | window $\sim1.5(a+M_k)^{-1/2}$; non-injective |
| $M_W$, $M(z_0)$ | — | — | not from the record; needs $x_0$ (phase and amplitude) |
| $\Delta M$ on $\mathcal F_{q,\delta}$ | two records + $\delta$ | pair in $U$; same lemmas; R9 only to name $\Delta M$ | determined (limit); from prefixes only after $M\sim(c/2|G|q)^2$, $c\in[0.05,0.75]$ |
| any token-to-memory write-through (C2) | — | — | not addressed; unchanged (RECOG-RESULT-R9-NO-TOKEN-WRITETHROUGH) |

## 4. Consequences for R6 and F5 (proposals, not adoptions)

- **F2(d) anti-tautology guard:** add the finite-versus-limit qualifier the plan asked for: $\Psi_\infty$ is a function of the complete token history (so $R_{\log}$-type in the limit), while every finite prefix leaves a window $\gg|\Delta M|$. The $R_{\log}$ verdict for the B/7-gap token stands; $R_{\rm ind}$ for R9's $M$ stands (needs the state).
- **F3 ladder:** the fiber result is an exact C0 statement — the records and $\Delta M$ are both functions of the common phase $\alpha$ — not a C1 residual and not C2. "Comparator-invisible" memory is token-visible, in the limit, because the tokens are phase crossings. No grade changes.
- **F5 scoping:** a token stream that is a readout of the carrier's phase cannot witness write-through; the sufficient witness (PI's scope) must show the carrier's update changing at a token (non-smooth or event-gated), which no readout does. Negative, and it narrows F5's search: candidates must be carriers that are *not* functions of the phase the tokens already read.
- **R6 residual:** unchanged. Tokenisation/selection principle still missing.

## 5. Illustration data

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

1. **Certificate for Lemma C** (explicit $c_\varepsilon$, the $T$-Lipschitz constant on $U_T$, $|W(T^6x)-W(x)|$ ceiling): exact rational/interval, sandbox; then the Proposition is `[THM]` on $U$.
2. **A1b registration:** proposed RID `RECOG-THM-A1B-SLIP-SCHEDULE-U` in §6.13b, with Lemmas A–C as sub-statements; NUMGEN informed (explicit-domain instance of GAP-LOCK; no custody change).
3. **A1c registration:** the classification as a `[DEF]`/`[RESULT] [from: ALG]` block in §6.16e–f (finite-versus-limit qualifier; fiber decodability as C0), after review.
4. **Long-orbit check on the PI machine:** the fiber decode at $N\approx6\times10^7$–$10^8$ primitive steps per orbit (two orbits per fiber), to see whether the record-only error crosses $|\Delta M|$ on the observed $M^{-1/2}$ law; the script runs as is with `N_steps` as its first argument (about 2 min per $10^6$ steps here; memory $\sim200$ bytes per step, so a chunked variant is needed above $\sim2\times10^7$). This is a test of the pair cancellation, not of the statements above.
5. **F5:** pose with the readout boundary of §4.
