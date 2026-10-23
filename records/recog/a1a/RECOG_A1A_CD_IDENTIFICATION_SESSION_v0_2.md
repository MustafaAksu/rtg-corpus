# RECOG A1a — Identification of the Number Genesis Phase-Defect Constant $C_D$ (session record v0.2)

**Date:** 20 October 2026
**Status:** `[SESSION]` record. It is not an accepted cell, and no RECOG RID, grade or OPEN status is created or changed. R6 stays ACTIVE.
**Base edition:** adopted RECOG v0.3.21 (`a3459522…0ae3`).
**Supersedes:** v0.1 (`cf22e325…f218`).
**Review:** v0.1 was reviewed independently on 20 Oct 2026 (`RECOG_A1A_SESSION_v0_1_INDEPENDENT_REVIEW_20261020.md`, `43a8a2d3fe0adc843b66bcaf852158cf79601221dbc4bfa1324fd7911b445e91`). The verdict was to accept the core identity, correct the C1 argument, and tighten one numerical statement.
**What changed from v0.1:** the full list is in §9.
- The incorrect C1 sufficiency sentence is withdrawn and replaced by an explicit lemma (§3.1), proposed by the reviewer and checked here.
- The identity now holds on an explicit start domain (§4).
- C2 is closed by the two owners' own definitions.
- The numerical wording is corrected.
- The OPEN 21 source passage is quoted, so it can be checked.

## 1. Sources (exact files used)

| Source | Identity | Passages used |
|---|---|---|
| RECOG v0.3.21 | `a3459522c8f58204f83f5e65e3d1a99912f9651d1c17cc4fb0c090196f670ae3` | §6.13a, RECOG-THM-R9-MEMORY ($C_z$ track; rows $(517,\tfrac1{400})$ on $\lvert z\rvert\le\tfrac1{20}$ and $(163,\tfrac1{1600})$ on $\lvert z\rvert\le\tfrac1{40}$, not mixed) |
| Number Genesis v1.20.7 | `c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28` | N-5A-S1-INF: L-MONO, L-PHASE, L-BACKBONE, INF-1 |
| Dyadic v6.4.17 | `e07cf2b93b532554d9e1d05d2bfef3be34829b7cb892627c0bb03d1d182d4bfc` | §6.14: DYAD-THM-PRIM-CTR, DYAD-THM-NF-INV, DYAD-ALG-OPEN3-PHASE-OFFSET, DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS, DYAD-THM-OPEN3-ASYMPTOTIC-PHASE (T1, T2), DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER (line 837; row table at lines 842–843) |

- **Dyadic editions.** The current Dyadic edition is v6.4.18 (`f70308f1…458d`). The Dyadic owner reports that §6.14 is byte-identical to v6.4.17, and I reproduced the v6.4.17-side passage hash prefix `a611ab681837`.
- **Evidence boundary.** The reviewer worked from v6.4.16 and did not have v6.4.17, so the OPEN 21 constants in §5 were checked against source here only. The reviewer can check them independently from v6.4.17, which is in the project as `claude/RTG_DYADIC_OSCILLATOR_DSN_v6_4_17.md`.

## 2. NUMGEN's definitions, as stated

- **L-PHASE:** $\hat\phi_{6(m+1)}-\hat\phi_{6m}=2\pi-\tau q_m+r_m$ with $\lvert r_m\rvert\le Cq_m^{3/2}$. Here $\hat\phi_n$ is the increasing lift of $\arg W$ along primitive steps, and $W=\rho+\omega\eta=\rho-\eta/2+i\tfrac{\sqrt3}{2}\eta$ is the frame Dyadic calls $\mathcal L$.
- **INF-1:** $D_M:=2\pi M-(\hat\phi_{6M}-\hat\phi_0)=\tau\log M+C_D+o(1)$.
- **L-MONO:** $\pi/6<\delta_T<\pi/2$, where $\delta_T$ is the one-step increment of the lift.
- **L-BACKBONE:** $q_M=1/M+O(M^{-3/2})$.
- **Scope:** all four hold on a *sufficiently small* punctured primitive tube. That tube is shown to exist, but its radius is not given explicitly.

## 3. The identification

### 3.1 Lemma C1 — explicit one-step angle bound on Dyadic's tube

`[SESSION: exact algebra and elementary enclosure]` The argument is the reviewer's; I checked it here.

Let $\omega=\tfrac{-1+i\sqrt3}2$ and $\lambda=1+\omega=e^{i\pi/3}$. Since $\omega^2=-1-\omega$, direct substitution into $T(\rho,\eta)=(\rho-\sin\eta,\ \eta+e^\rho-1-\sin\eta)$ gives the exact identity
$$W(Tx)=\lambda W+\lambda(\eta-\sin\eta)+\omega(e^\rho-1-\rho).$$

**Bounds used:**
- $Q=(\rho-\eta/2)^2+\tfrac34\eta^2$, and symmetrically in $\rho$, so $\lvert\rho\rvert,\lvert\eta\rvert\le\tfrac2{\sqrt3}\lvert W\rvert<2\lvert W\rvert$.
- On the Dyadic tube $U_T$, $\lvert W\rvert<R:=\tfrac{47}{1000}$ (DYAD-THM-PRIM-CTR).
- So $\lvert\rho\rvert<\ln2$, and therefore $e^{\lvert\rho\rvert}<2$.

With $\lvert\eta-\sin\eta\rvert\le\lvert\eta\rvert^3/6$ and $\lvert e^\rho-1-\rho\rvert\le e^{\lvert\rho\rvert}\rho^2/2$,
$$\Bigl\lvert\frac{W(Tx)}{\lambda W}-1\Bigr\rvert\le4\lvert W\rvert+\tfrac43\lvert W\rvert^2<4R+\tfrac43R^2=\tfrac{143209}{750000}<\tfrac12 .$$
(Recomputed exactly. The sharper constant $\tfrac2{\sqrt3}$ would give about $0.034$. It is not needed.)

For $\lvert\varepsilon\rvert<\tfrac12$, $\lvert\operatorname{Arg}(1+\varepsilon)\rvert<\arcsin\tfrac12=\tfrac\pi6$. So **every point of $U_T$** satisfies
$$\tfrac\pi6<\delta_T(x)<\tfrac\pi2 .$$
$U_T$ is $T$-invariant, so the whole forward orbit stays in it. Each six-step total therefore lies in $(\pi,3\pi)$ and equals $2\pi+\operatorname{Arg}(W_{m+1}/W_m)$, with Arg the principal value.

No sampling, no R9 and no NUMGEN tube is used. **v0.1 was wrong here:** it said per-step increments in $(0,\pi)$ suffice, but six such increments can sum to anything in $(0,6\pi)$. That sentence is withdrawn.

### 3.2 Lift alignment and the finite-$M$ identity

`[SESSION: derived]` By Lemma C1, for every start $x_0\in U$ and every $M$, exactly and without choosing a lift:
$$D_M=\Theta_W(0)-\Theta_W(M).$$
With $\Psi_W=\Theta_W-\tau\log Q$:
$$D_M-\tau\log M=\tau\log Q_0-\bigl(\Psi_W(M)-\Psi_W(0)\bigr)-\tau\log(MQ_M).$$

### 3.3 $MQ_M\to1$ on the explicit domain

`[SESSION: derived from owner bounds]`
1. DYAD-THM-PRIM-CTR gives $Q_{m+1}=Q_m-Q_m^2+P_5+R$ with $\lvert P_5\rvert\le\tfrac{16931}{10000}Q_m^{5/2}$ and $\lvert R\rvert\le108Q_m^3$ for $Q_m\le\tfrac1{400}$, and the orbit stays in that range.
2. It also gives $Q_m\le Q_0/(1+\tfrac12Q_0m)$.
3. Hence $Q_{m+1}^{-1}-Q_m^{-1}=1+O(\sqrt{Q_m})$, with an explicit constant from these bounds.
4. Summing gives $Q_M^{-1}=Q_0^{-1}+M+O(\sqrt M)$, so $MQ_M\to1$.

This is NUMGEN's L-BACKBONE argument, run on Dyadic's explicit $U$. No explicit error constant is asserted.

### 3.4 Limit

`[SESSION: derived; conditional on R9 through T1]`
- Dyadic T1 gives $\Psi_W(M)\to\Psi_{W,\infty}$. This is conditional on RECOG-THM-R9-MEMORY, and the start must lie in the row disk; §4 shows every start in $U$ does.
- Therefore
$$\boxed{\,C_D(W_0)=\tau\log Q_0-M_W(W_0)=\tau\log q_0+D_\Theta(z_0)-M(z_0)\,}$$
- The second form is Dyadic T2, $M_W=M-\Delta_0(z_0)$.
- The first form does not depend on how the starting phase is lifted. It does depend on the start: $C_D$ is a function of $x_0$, not a universal constant.

## 4. Domains

**Identity domain.** $U=\{0<Q_0=\lvert W_0\rvert^2\le\tfrac1{625}\}$, that is, $0<\lvert W_0\rvert\le\tfrac1{25}$.
- Lemma C1 and §3.3 hold on $U$ itself.
- DYAD-THM-NF-INV gives $\lvert z_0\rvert\le\tfrac{16}{15}\lvert W_0\rvert\le\tfrac{16}{375}<\tfrac1{20}$. So every start in $U$ lies in row A's chart disk, and T1 and T2 apply.
- NUMGEN's existential tube is no longer needed for §3.

**Quantitative domain (§5).** Intersect $U$ with the OPEN 21 primitive domains:
- row A: $0<\lvert W_0\rvert\le\tfrac1{25}$ (inside $\tfrac3{64}$);
- row B: $0<\lvert W_0\rvert\le\tfrac3{128}$ (inside $\tfrac1{25}$).

**C2 — indexing (closed by definition).**
- Both owners index the same orbit from the same start $x_0$. NUMGEN's $D_M$ uses $\hat\phi_0$ at primitive step 0 and $\hat\phi_{6M}$. Dyadic uses $W_m=W(T^{6m}x_0)=h(z_m)$ with $z_m=\widehat F^m(z_0)$ and $z_0=h^{-1}(W_0)$.
- NUMGEN's $D_M$ does not require $x_0$ to be a B-event anchor.
- So $Q_m$, $\Theta_W(m)$ and $\hat\phi_{6m}$ all refer to the point $T^{6m}x_0$.

## 5. Quantitative form

`[SESSION: derived; conditional on R9]`

**Owner passage** (v6.4.17 line 837, row table lines 842–843; v6.4.18 §6.14 owner-reported as identical):
$$\lvert M_W-\mathcal P_2(W_0)\rvert\le K'_jQ_0^{3/2}+C_{2,j}\bigl(\tfrac{256}{225}\bigr)^2Q_0^2,$$
with rows
- A: $\lvert z\rvert\le\tfrac1{20}$, $w_A=\tfrac3{64}$, $K'_A=\tfrac{3951}{1000}$, $C_{2,A}=517$, and secondary single constant $K_A=\tfrac{8831}{250}$;
- B: $\lvert z\rvert\le\tfrac1{40}$, $w_B=\tfrac3{128}$, $K'_B=\tfrac{971}{250}$, $C_{2,B}=163$, and $K_B=\tfrac{883}{100}$.

The theorem is graded `[THM — conditional on RECOG-THM-R9-MEMORY]`.

**Combined with §3.4**, on the §4 quantitative domains:
$$C_D(W_0)=\tau\log Q_0-\mathcal P_2(W_0)+E,\qquad\lvert E\rvert\le K'_jQ_0^{3/2}+C_{2,j}\bigl(\tfrac{256}{225}\bigr)^2Q_0^2 ,$$
where $\mathcal P_2=-\Delta_1(W_0)+Q_0[c_{\rm iso}+\Lambda_1(\Theta_{W_0})]+P_{W2}(W_0)$. Explicitly,
$$C_D=\tau\log Q_0+\Delta_1(W_0)+\tfrac{\sqrt3}{3}Q_0-Q_0\Lambda_1(\Theta_{W_0})-\bigl(P_{W2}(W_0)-\langle P_{W2}\rangle\bigr)+E .$$
- The isotropic coefficient is $\tfrac{\sqrt3}3=-(c_{\rm iso}+\langle P_{W2}\rangle)$, with $c_{\rm iso}=-\tfrac{4\sqrt3}{27}$ and $\langle P_{W2}\rangle=-\tfrac{5\sqrt3}{27}$. The reviewer checked this independently.
- R9's $C_2$ is used at statement level only. RECOG's internal Arb certificate is not re-proved here.
- This is a primitive-phase statement. It is not an exact-map statement about $C_W^{(h)}$, and it is not the R9 $C_z$ comparator-incompleteness corollary.

## 6. Independent-existence candidate (routed to owners; not claimed)

`[SESSION: candidate]` The argument:
1. NUMGEN INF-1 gives the existence of $C_D$ without R9.
2. With §3.2 and §3.3, $\Psi_W(M)$ converges.
3. Dyadic's unconditional bound $\lvert\Psi_W-\Psi_z\rvert\le K_0\sqrt{q_m}$ gives the same limit for $\Psi_z$.

So the **existence** of $\Psi_{W,\infty}$ and $\Psi_\infty$ would follow without R9.

**Domain.** Lemma C1 and §3.3 are explicit on $U$, but INF-1 uses NUMGEN's L-PHASE remainder constant, which is existential. So the candidate holds on the intersection of $U$ with NUMGEN's tube: a punctured neighbourhood of $P_1$ with no explicit radius. An explicit version needs an explicit L-PHASE constant.

**Limits.** This is an existence route only. The memory law, the $q_0$ expansion and §5 stay conditional on R9. The candidate needs owner review by Dyadic (T1's "not an independent existence theorem" note) and Number Genesis (its optional "$C_D$ identification" question). C2 is now closed (§4).

## 7. Numerical illustration `[NUM]` — not a proof input

`recog_a1a_cd_identity_num.py` (`efccd210…791b`) produces `a1a_cd_identity_num.json` (`09136040…740`). The reviewer reproduced it byte for byte. Its starts all lie in $U$: $\lvert W_0\rvert\in\{0.04,0.02,0.01\}$, at 4 angles each, run for 16,000 blocks.

- **Alignment:** $\max\lvert D_M-(\Theta_W(0)-\Theta_W(M))\rvert=2.41\times10^{-9}$. This is float drift; the identity is exact by §3.2.
- **Convergence of the tail-corrected estimator** $\hat C(M)=D_M-\tau\log M+\tau\log(MQ_M)-\mathcal P_2(W_M)$:
  - maximum change from $M=1000$ to $16000$: $5.10\times10^{-6}$ (v0.1 wrongly said about $10^{-6}$);
  - maximum change from $M=4000$ to $16000$: $9.36\times10^{-7}$.
- **Prediction:** $(\hat C-[\tau\log Q_0-\mathcal P_2(W_0)])/Q_0^{3/2}\in[-0.28,+0.35]$, with a maximum absolute value of $0.3459$. This is well inside the P5 majorants and close to Dyadic's own `[NUM]` OPEN 21 ratio. It is not a remainder certificate.

## 8. Status of the open checks

| Check | Status |
|---|---|
| C1 explicit domain | **Resolved at session level** by Lemma C1 (§3.1) and §3.3 on $U$; to be confirmed when this revision is reviewed |
| C2 common-start indexing | **Closed** by the owners' definitions (§4) |
| C3 R9 at statement level | Unchanged: §3.4 and §5 stay conditional on R9 |
| C4 routing of §6 | Open: needs PI routing to Dyadic and Number Genesis, after review of this revision |

## 9. Changes from v0.1

1. **§3.** The incorrect "$(0,\pi)$ per step suffices" sentence is withdrawn. Lemma C1 is added (proposed by the reviewer, checked here, constant recomputed exactly).
2. **§3.3–§4.** Explicit identity domain $U$; row-A disk membership via NF-INV; row domains intersected with $U$.
3. **§4.** C2 closed by definition.
4. **§5.** The OPEN 21 passage is quoted with line references, and the evidence boundary is stated.
5. **§6.** The candidate's domain is stated precisely: the identity is explicit, INF-1 is existential.
6. **§7.** The numerical stability statement is corrected ($5.10\times10^{-6}$ and $9.36\times10^{-7}$).

## 10. Separation (unchanged)

The A1a constant identity does not give the A1b token schedule, and A1b does not give A1c recoverability. Nothing here defines a physical event, reads $C_D$ physically, or transfers anything to the comparator $C_W^{(h)}$. RECOG v0.3.21 is unchanged, and R6 stays ACTIVE.
