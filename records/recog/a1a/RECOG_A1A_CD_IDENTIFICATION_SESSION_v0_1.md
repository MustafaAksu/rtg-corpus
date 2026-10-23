# RECOG A1a — Identification of the Number Genesis Phase-Defect Constant $C_D$ (session record v0.1)

**Date:** 20 October 2026
**Status:** `[SESSION]` record. It is not an accepted cell, and no RECOG RID, grade or OPEN status is created or changed. R6 stays ACTIVE.
**Base edition:** adopted RECOG v0.3.21 (`a3459522…0ae3`).
**Builds on:** the contributor's preliminary derivation in the 20 Oct handoff. This record checks that derivation against the owner texts and adds the quantitative form.

## 1. Sources (exact files used)

| Source | Identity | Passages used |
|---|---|---|
| RECOG v0.3.21 | `a3459522c8f58204f83f5e65e3d1a99912f9651d1c17cc4fb0c090196f670ae3` | §6.13a, RECOG-THM-R9-MEMORY ($C_z$ track; rows $(517,\tfrac1{400})$ on $\lvert z\rvert\le\tfrac1{20}$ and $(163,\tfrac1{1600})$ on $\lvert z\rvert\le\tfrac1{40}$, not mixed) |
| Number Genesis v1.20.7 | `c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28` (the project copy; matches RECOG's §7 pin `c4637e7a…ab28`) | N-5A-S1-INF: L-MONO, L-PHASE, L-BACKBONE, INF-1 |
| Dyadic v6.4.17 | `e07cf2b93b532554d9e1d05d2bfef3be34829b7cb892627c0bb03d1d182d4bfc` (local copy) | §6.14: DYAD-ALG-OPEN3-PHASE-OFFSET, DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS, DYAD-THM-OPEN3-ASYMPTOTIC-PHASE (T1, T2), DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER |

Dyadic's current edition is v6.4.18 (`f70308f1…458d`). The Dyadic owner reports that §6.14 is byte-identical to v6.4.17 (passage hash prefix `a611ab681837`), and I reproduced that prefix on the v6.4.17 side. The OPEN 21 passage used below is therefore the one in force.

## 2. NUMGEN's definitions, as stated

- **L-PHASE:** $\hat\phi_{6(m+1)}-\hat\phi_{6m}=2\pi-\tau q_m+r_m$ with $\lvert r_m\rvert\le Cq_m^{3/2}$. Here $\hat\phi_n$ is the increasing lift of $\arg W$ along primitive steps, and $W=\rho-\eta/2+i\tfrac{\sqrt3}2\eta$ is the frame used by Dyadic (the map $\mathcal L$).
- **INF-1:** $D_M:=2\pi M-(\hat\phi_{6M}-\hat\phi_0)=\tau\log M+C_D+o(1)$.
- **L-MONO:** each primitive step's angle increment lies in $(\pi/6,\pi/2)$ on NUMGEN's tube.
- **L-BACKBONE:** $q_M=1/M+O(M^{-3/2})$.
- **Scope:** all four hold on a *sufficiently small* punctured primitive tube. That tube is shown to exist, but its radius is not given explicitly.
- **Status of $C_D$:** NUMGEN treats the constant as existing; identifying it is listed there as the optional "Fatou/$C_D$ identification" question.

## 3. The identification

**Lift alignment** `[SESSION: derived]`.
- By L-MONO, each six-step block increment of $\hat\phi$ lies in $(\pi,3\pi)$.
- So it equals $2\pi+\operatorname{Arg}(W_{m+1}/W_m)$, where Arg is the principal value. That principal-value increment is exactly Dyadic's per-block phase increment for $\Theta_W$.
- Hence, on NUMGEN's tube, exactly and for every $M$, without choosing any lift:
$$D_M=\Theta_W(0)-\Theta_W(M).$$

**Finite-$M$ identity** `[SESSION: derived]`. Write $\Psi_W=\Theta_W-\tau\log Q$. Then
$$D_M-\tau\log M=\tau\log Q_0-\bigl(\Psi_W(M)-\Psi_W(0)\bigr)-\tau\log(MQ_M).$$
The contributor's form, $\hat\phi_0-\Psi_W(M)-\tau\log(MQ_M)$, is the same statement once the tie $\hat\phi_0=\Theta_W(0)$ is chosen.

**Limit** `[SESSION: derived; conditional]`.
- By L-BACKBONE, $MQ_M\to1$.
- By Dyadic T1 (conditional on R9), $\Psi_W(M)\to\Psi_{W,\infty}$.
- Therefore
$$\boxed{\,C_D=\tau\log Q_0-M_W=\tau\log q_0+D_\Theta(z_0)-M\,}$$
- The second equality is Dyadic T2: $M_W=M-\Delta_0(z_0)$, with $\Delta_0=D_\Theta-\tau\log(Q_0/q_0)$.
- This matches the contributor's result. The lift-free form $\tau\log Q_0-M_W$ is the preferred statement, because $M_W$ does not depend on the initial lift.
- $C_D$ depends on the starting state. The constant in "$D_M=\tau\log M+C_D+o(1)$" is a function of the starting point $x_0$ (equivalently $W_0$), not a universal constant.

## 4. Quantitative form (owner passage verified)

Combine §3 with DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER (v6.4.17 §6.14, line 837; `[THM — conditional on RECOG-THM-R9-MEMORY]`). The result is `[SESSION: derived; conditional on R9]`:
$$C_D(W_0)=\tau\log Q_0-\mathcal P_2(W_0)+E,\qquad \lvert E\rvert\le K'_jQ_0^{3/2}+C_{2,j}\bigl(\tfrac{256}{225}\bigr)^2Q_0^2 .$$
Here
$$\mathcal P_2=-\Delta_1(W_0)+Q_0\bigl[c_{\rm iso}+\Lambda_1(\Theta_{W_0})\bigr]+P_{W2}(W_0).$$

The two rows are not to be mixed:

| Row | Start domain | $K'_j$ | $C_{2,j}$ |
|---|---|---|---|
| A | $\lvert W_0\rvert\le\tfrac3{64}$ | $\tfrac{3951}{1000}$ | 517 |
| B | $\lvert W_0\rvert\le\tfrac3{128}$ | $\tfrac{971}{250}$ | 163 |

Explicitly,
$$C_D=\tau\log Q_0+\Delta_1(W_0)+\tfrac{\sqrt3}{3}Q_0-Q_0\Lambda_1(\Theta_{W_0})-\bigl(P_{W2}(W_0)-\langle P_{W2}\rangle\bigr)+E .$$
- $\Delta_1$ is $O(\sqrt{Q_0})$ and has angular mean zero.
- The isotropic $Q_0$ coefficient, $+\tfrac{\sqrt3}3$, is $-(c_{\rm iso}+\langle P_{W2}\rangle)$, the arithmetic identity recorded by Dyadic.
- $\Lambda_1$ carries the lattice harmonic $\pm6$. This is the slot that is invisible to the comparator, as R9 records.

**Domain.** The formula needs the start in the Dyadic row disk *and* in NUMGEN's tube.
- The intersection is a nonempty punctured neighbourhood of $P_1$, but with no explicit radius, because NUMGEN's tube is existential.
- An explicit version needs one extra inequality: each primitive step's increment stays in $(0,\pi)$ on the Dyadic tube $U_T$ (where $\lvert W\rvert<\tfrac{47}{1000}$). That is enough for the six-step block increment to lie in $(\pi,3\pi)$, together with $MQ_M\to1$ on that tube.
- This is open check **C1** below.

## 5. A consequence that goes beyond the handoff (candidate; routed to owners, not claimed)

`[SESSION: candidate]` Run the identity of §3 in the opposite direction.
1. NUMGEN's INF-1 gives the existence of $C_D$, and it does not use R9.
2. So, by the finite-$M$ identity and $MQ_M\to1$, $\Psi_W(M)$ converges.
3. Dyadic's offset bound $\lvert\Psi_W-\Psi_z\rvert\le K_0\sqrt{q_m}$ is unconditional (`[THM]`).
4. So $\Psi_z(M)$ converges too.

On the domain intersection, then, the **existence** of $\Psi_\infty$ and $\Psi_{W,\infty}$ would follow without R9. Dyadic records this as not established: "T1 … not an independent existence theorem for $\Psi_\infty$", and "an unconditional version (independent of R9)" is listed as not established.

Limits of the candidate:
- It would remove the R9 condition only from T1's *existence/limit-equality* part, and only on the intersection domain.
- The memory law, the $q_0$ expansion and every quantitative statement in §4 stay conditional on R9.
- The grade would be the weaker of NUMGEN's `[RESULT] [from: ALG]` and Dyadic's `[THM]`.
- It also hands NUMGEN its optional identification: $C_D=\tau\log Q_0-M_W$.

These belong to the Dyadic and Number Genesis owners. The candidate needs independent review before it is sent to either.

## 6. Numerical illustration `[NUM]` — not a proof input

`recog_a1a_cd_identity_num.py` (`efccd210…791b`; output `a1a_cd_identity_num.json` `09136040…740`):
- Runs exact primitive orbits in float64, with 12 starts: $\lvert W_0\rvert\in\{0.04,0.02,0.01\}$, all inside row A, at 4 angles each, for 16,000 blocks.
- Computes $D_M$ from the primitive per-step lift, independently of the Dyadic block phase.

Results:
- **Alignment:** $\max_M\lvert D_M-(\Theta_W(0)-\Theta_W(M))\rvert\le2.4\times10^{-9}$ on every orbit. This is float drift; the identity is exact.
- **Convergence:** the tail-corrected estimator $\hat C(M)=D_M-\tau\log M+\tau\log(MQ_M)-\mathcal P_2(W_M)$ is stable to about $10^{-6}$ between $M=1000$ and $M=16000$.
- **Prediction:** $(\hat C-[\tau\log Q_0-\mathcal P_2(W_0)])/Q_0^{3/2}$ lies in $[-0.28,+0.35]$, nearly constant over a 16-fold range of $Q_0$.
  - The maximum, 0.346, matches Dyadic's own `[NUM]` OPEN 21 ratio of $\approx0.35$.
  - Without the $\mathcal P_2$ terms the difference is $O(\sqrt{Q_0})$, so $\mathcal P_2$ is doing the work.
- **Not shown:** this shows neither an optimal constant nor the absence of higher-order terms.

## 7. Open checks before this can become an A1a cell

- **C1 (domain):** an explicit radius on which the lift alignment and $MQ_M\to1$ hold. This means an explicit bound for the per-step increment on $U_T$, or use of NUMGEN's named explicit tube if its L-MONO constant can be made explicit.
- **C2 (indexing):** NUMGEN counts from an arbitrary start $x_0$ at primitive step 0, and Dyadic uses $z_0=h^{-1}(W_0)$ at block 0. These are consistent as used here, but the two owners' statements should be confirmed to refer to the same start.
- **C3 (grade bookkeeping):** the §4 bound inherits R9's $C_2$ at statement level. RECOG's internal Arb certificate for R9 is not re-proved here; Dyadic's records say the same.
- **C4 (routing):** decide whether §5 goes to Dyadic and NUMGEN as a question, after review.

## 8. Separation (unchanged)

The A1a constant identity does not give the A1b token schedule, and A1b does not give A1c recoverability. Nothing here defines a physical event, reads $C_D$ physically, or transfers anything to the comparator $C_W^{(h)}$. R6 stays ACTIVE.
