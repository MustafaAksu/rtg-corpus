# RECOG v0.3.23 — FC-21 proof cell: R9-free existence of $C_D^{\rm ext}$ on all of $U$

**Date:** 23 October 2026 · **Author:** RECOG co-owner (Claude) · **Status:** `[SESSION]` proof record for the new science block of v0.3.23 stage 1. Not adopted. It needs its own review verdict (decoupling rule, PI decision of 23 Oct 2026: if this review is not finished when the maintenance rows are ready, v0.3.23 is released without the block, built by `build_recog_v0_3_23_stage1.py --without-fc21`).

**Proposed RID:** `RECOG-THM-A1A-PHASE-EXISTENCE-U` (RECOG v0.3.23 §6.13b). Artifact RID `RECOG-ART-A1A-EXISTENCE-U` (§8) points to this record and to the illustration.

**Sources read (EV-SRC-READ):**
- Dyadic `dyad-v6.4.22`, `dsn/RTG_DYADIC_OSCILLATOR_DSN.md`, SHA-256 `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29`. §6.14: the interface-objects entry (I1–I5, line 892), `DYAD-THM-LPHASE-ROWA-REMAINDER` (statement and proof outline lines 894–902, recorded distinctions from line 904), `DYAD-THM-PRIM-CTR` (lines 785–787).
- RECOG `recog-v0.3.22`, `dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`, SHA-256 `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9`. §6.13b: `RECOG-DEF-A1A-PHASE-INTERFACE`, `RECOG-THM-A1A-LIFT-ALIGNMENT`, `RECOG-THM-A1A-RECIPROCAL-AMPLITUDE`, the finite-block identity, `RECOG-THM-A1A-PHASE-EXISTENCE-ALT`.
- NUMGEN `numgen-v1.20.8` §6.6: `NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT` (the lift definition, for the comparison in check 1 only).
- Prior written proofs: atlas advisory FC-RECOG-21 (`records/recog/ATLAS_ADVISORY_RECOG_v0_3_22.md`, `5c888118…dd85`) and its source, the independent review §5 (`records/recog/ATLAS_ADVISORY_RECOG_INDEPENDENT_REVIEW.md`, `d6fb7c60…204d`). This cell re-derives the result and checks the four points both RECOG dispositions asked for.

## 1. Statement

`[THM]` [RID: RECOG-THM-A1A-PHASE-EXISTENCE-U] [scope: conditional on the postulated $T$; $x_0\in U=\{0<Q_0\le\tfrac1{625}\}$]

Let $x_m=T^{6m}x_0$, $Q_m=Q(x_m)=\lvert W(x_m)\rvert^2$ with $W=\rho+\omega\eta$, and $a:=Q_0^{-1}$. Let $N$ be the block count and $D_N^U=2\pi N-(\hat\phi_{6N}-\hat\phi_0)$ the A1a extension of NUMGEN's defect formula on $U$. Then H-NG holds, and

$$C_D^{\rm ext}(x_0)=\lim_{N\to\infty}\bigl(D_N^U-\tau\log N\bigr)=\tau H(a)+\tau\sum_{m\ge0}\Bigl(Q_m-\frac1{a+m}\Bigr)-\sum_{m\ge0}r_m,$$

$$H(a)=-\log a+\sum_{m\ge0}\Bigl[\frac1{a+m}-\log\Bigl(1+\frac1{a+m}\Bigr)\Bigr]=-\psi(a),$$

where $r_m$ are the row-A block remainders of `DYAD-THM-LPHASE-ROWA-REMAINDER`, $\psi$ is the digamma function, and all three series converge absolutely. By `RECOG-THM-A1A-PHASE-EXISTENCE-ALT`, $\Psi_{W,\infty}$ and $\Psi_{z,\infty}$ exist, $\Psi_{z,\infty}=\Psi_{W,\infty}=\Theta_W(0)-C_D^{\rm ext}$, and $C_D^{\rm ext}=\tau\log Q_0-M_W$. Neither `RECOG-THM-R9-MEMORY` nor NUMGEN INF-1 is used.

## 2. Premises (owner text)

- **P1** `DYAD-THM-LPHASE-ROWA-REMAINDER` `[THM]` (v6.4.19; the statement lines (B) and (R) are byte-identical at the tags `dyad-v6.4.19` and `dyad-v6.4.22`). "Let $x\in U=\{0<Q\le\tfrac1{625}\}$." (B) for every $y\in U_T$, $\lvert W(Ty)/(\lambda W(y))-1\rvert\le\varepsilon$, $\varepsilon\le0.04654$; "the six-step lifted increment equals $2\pi+\operatorname{Arg}(F_W(W)/W)$". (R) "For every $m\ge0$, $\hat\varphi_{6(m+1)}-\hat\varphi_{6m}=2\pi-\tau Q_m+r_m$, $\lvert r_m\rvert\le\tfrac{403}{250}Q_m^{3/2}$." Proof outline: "Block base points stay in $U$ ($F(U)\subset U$)." Not conditional on R9: its inputs are DYAD-THM-NF-REM ($C_7=100$), DYAD-THM-PRIM-CTR, DYAD-THM-OPEN3-SPIRAL-REM and exact identities of §6.14.
- **P2** Interface objects I1–I5 (Dyadic §6.14, line 892): frame $W=\mathcal L(\rho,\eta)$; "$\delta_T(y)=\operatorname{Arg}(W(Ty)/W(y))$ (principal value); $\hat\varphi$ is the increasing lift whose one-step increments are $\delta_T$ (NUMGEN's L-MONO lift), $\hat\varphi_{6m}$ taken at the block base point $x_m=F^mx$. Observable $Q_m=Q_{\rm prim}(x_m)=\lvert W(x_m)\rvert^2$ — the primitive quantity, not the chart variable $q=\lvert z\rvert^2$. … Domain: block base points in $U$, intermediate steps in $U_T$."
- **P3** `DYAD-THM-PRIM-CTR` `[THM]`: $Q_m\le Q_0/(1+\tfrac12Q_0m)$; $U_T=\bigcup_{j<6}T^j(U)$, $T(U_T)\subseteq U_T$.
- **P4** `RECOG-THM-A1A-LIFT-ALIGNMENT` `[THM]`: for every $x\in U_T$, $\tfrac\pi6<\delta_T(x)<\tfrac\pi2$; each block increment of $\hat\phi$ is $2\pi+\operatorname{Arg}(W_{m+1}/W_m)$.
- **P5** `RECOG-THM-A1A-RECIPROCAL-AMPLITUDE` `[THM]` [scope: $x_0\in U$]: $\lvert Q_{m+1}^{-1}-Q_m^{-1}-1\rvert<\tfrac{15}2\sqrt{Q_m}$. Its proof uses `DYAD-THM-PRIM-CTR` only.
- **P6** `RECOG-THM-A1A-PHASE-EXISTENCE-ALT` `[THM]` [assuming: H-NG] [scope: $x_0\in U$]: H-NG ⇒ $\Psi_{W,\infty}$, $\Psi_{z,\infty}$ exist and the stated equalities. "R9 is not used."

## 3. The four checks against `dyad-v6.4.22`

| # | Point | Finding |
|---|---|---|
| 1 | **Lift branch.** Is the $\hat\varphi$ of P1 the $\hat\phi$ of $D_N^U$? | Yes. Both are the lift of $\arg W$ built from principal one-step increments $\delta_T$ (P2; NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT: $\hat\phi_{n+1}=\hat\phi_n+\delta_T(T^nx)$). By P4 these increments lie in $(\tfrac\pi6,\tfrac\pi2)$ on $U_T$, so this is the increasing lift used by A1a; the frame is the same ($W=\mathcal L(\rho,\eta)=\rho+\omega\eta$ at $p=6$, DYAD-ALG-KP-FRAME-SCALE). The representative $\hat\phi_0$ cancels in $D_N^U$. |
| 2 | **Domain.** Do the block base points stay where P1 applies? | Yes. P1 is stated for base points $x\in U$ with intermediate steps in $U_T$, and records $F(U)\subset U$. A1a starts at $x_0\in U$, so every $x_m\in U$ and every intermediate point lies in $U_T$ (P3). No start in $U_T\setminus U$ is covered. |
| 3 | **Indexing.** Do P1's $Q_m$ and A1a's $Q_m$ coincide, and does the sum run over the right blocks? | Yes. Both are $Q(T^{6m}x_0)$, the primitive amplitude at block base point $m$, counted from the start (P2; NUMGEN's block-sampled amplitude has the same definition). $D_N^U$ involves the increments for $m=0,\dots,N-1$, exactly the terms of (R) used below. |
| 4 | **Amplitude inversion.** Is $Q_m-\tfrac1{a+m}$ summable from P5 alone? | Yes, see step 3 of the proof; P5 needs no R9. |

## 4. Proof

1. *Telescoping.* By checks 1–3, $D_N^U=\sum_{m<N}\bigl[2\pi-(\hat\phi_{6(m+1)}-\hat\phi_{6m})\bigr]=\sum_{m<N}(\tau Q_m-r_m)$.
2. *Remainders.* By P3, $Q_m\le\min(Q_0,\tfrac2m)$ for $m\ge1$. Hence $\sum_m\lvert r_m\rvert\le\tfrac{403}{250}\bigl(Q_0^{3/2}+2^{3/2}\sum_{m\ge1}m^{-3/2}\bigr)<\infty$.
3. *Amplitudes.* Summing P5, $Q_m^{-1}=a+m+e_m$ with $\lvert e_m\rvert<\tfrac{15}2\sum_{k<m}\sqrt{Q_k}\le\tfrac{15}2\bigl(\sqrt{Q_0}+2\sqrt2\sqrt m\bigr)=O(\sqrt m)$. Then
$$Q_m-\frac1{a+m}=\frac{(a+m)-Q_m^{-1}}{Q_m^{-1}(a+m)}=-\frac{e_mQ_m}{a+m},\qquad\Bigl\lvert Q_m-\frac1{a+m}\Bigr\rvert\le\frac{2\lvert e_m\rvert}{m(a+m)}=O(m^{-3/2})\quad(m\ge1),$$
so $\sum_m(Q_m-\tfrac1{a+m})$ converges absolutely.
4. *Harmonic part.* $\sum_{m<N}\log(1+\tfrac1{a+m})=\log\tfrac{a+N}a$, so
$$\sum_{m<N}\frac1{a+m}-\log N=\sum_{m<N}t_m-\log a+\log\frac{a+N}N,\qquad t_m=\frac1{a+m}-\log\Bigl(1+\frac1{a+m}\Bigr)\in\Bigl[0,\frac1{2(a+m)^2}\Bigr],$$
which tends to $H(a)$. Since $\sum_{m<N}\tfrac1{a+m}=\psi(a+N)-\psi(a)$ and $\psi(x)-\log x\to0$, $H(a)=-\psi(a)$.
5. *Limit.* $D_N^U-\tau\log N=\tau\sum_{m<N}(Q_m-\tfrac1{a+m})+\tau\bigl(\sum_{m<N}\tfrac1{a+m}-\log N\bigr)-\sum_{m<N}r_m$; each part converges by steps 2–4. This is H-NG, with the stated series.
6. *Phase.* P6 applies with H-NG now proved. Its proof uses the finite-block identity, P5, P4-0 and the offset bounds; it uses neither R9 nor INF-1. $\square$

The tails are $O(N^{-1/2})$ for each fixed orbit (from steps 2–3); no uniform constant is stated.

## 5. What this does not supply

$c_{\rm iso}$, $\Lambda_1$, $C_2$, memory coefficients or remainders without R9; an R9-free OPEN 21 or an R9-free form of A1a (c); the chart-variable form $\tau\log q_0+D_\Theta(z_0)-M(z_0)$ of (b) without R9; `RECOG-THM-R9-COMPARATOR-INCOMPLETENESS`; starts in $U_T\setminus U$; any extension of NUMGEN's adopted domain or grade; any physical memory, token or event mechanism. `RECOG-RESULT-A1A-PHASE-EXISTENCE-NG` and `RECOG-RESULT-A1A-CD-AGREEMENT` are unchanged and stay the records of the NUMGEN route; `RECOG-THM-A1A-CD-IDENTIFICATION` keeps its R9 route. Dyadic offered the same route as FC-DYAD-32 (notice N19, prepared and not sent); this cell does not depend on that notice.

## 6. Illustration (`[NUM]`, not a proof input)

`evidence/recog/scripts/recog_v0_3_23_value_checks.py`, Part B; output `evidence/recog/v0.3.23/value_checks.json`. Float64 primitive orbits from 12 starts in $U$ ($Q_0\in\{\tfrac1{625},10^{-3},4\cdot10^{-4}\}$ × 4 phases), 20000 blocks each:
- sampled one-step branch $\max\varepsilon\le0.0240$ (bound $0.04654$); sampled $\max\lvert r_m\rvert/Q_m^{3/2}\approx1.42$ (bound $\tfrac{403}{250}=1.612$);
- the identity of step 5 holds to rounding ($<10^{-11}$);
- the $\psi$-corrected partial series $-\tau\psi(a)+\tau\sum_{m<N}(Q_m-\tfrac1{a+m})-\sum_{m<N}r_m$ changes by less than $3\times10^{-3}$ between $N=10^4$ and $2\times10^4$, while the raw $D_N-\tau\log N$ still moves by about $\tau a/N$ there (the slow $\log\tfrac{a+N}N$ term of step 4);
- $H(a)=-\psi(a)$ to $<10^{-11}$.

## 7. Review request

Change-focused review of this block (its own verdict, separate from the maintenance rows): the statement in §1, the four checks of §3 against `dyad-v6.4.22`, the proof of §4, the scope of §5, and the stage-1 edits S1-6, S5-1, S613b-14, S7-17, S8-3, A-2 that place it (`evidence/recog/v0.3.23/stage1_edits.json`, group `FC21`).
