# RECOG A1a — Identification of the Number Genesis Phase-Defect Constant $C_D$ (session record v0.3)

**Date:** 20 October 2026
**Status:** `[SESSION]` record, with a RECOG owner-review disposition for C4 (§6). Nothing is adopted into the DSN; no RECOG RID, grade or OPEN status is created or changed. R6 stays ACTIVE.
**Base edition:** adopted RECOG v0.3.21 (`a3459522…0ae3`).
**Supersedes:** v0.2 (`b4906ddf…c428`), which superseded v0.1 (`cf22e325…f218`).
**Review trail:**
- v0.1 review `43a8a2d3…5e91`;
- v0.2 review `7aa08ccc…36a8` (accepted; C4 authorized as owner questions);
- Dyadic C4 response, recorded in `RECOG_A1A_C4_DYAD_RESPONSE_RECEIPT_20261020.md` (`36e20687…ee91`);
- Number Genesis C4 reply `NUMGEN_REPLY_TO_RECOG_A1A_C4_20261020_v0_1.md` (`8a887ef31206334d78ced4cb0bc91d6a8cad5c010f7d0960e1ecb64810ffbc4d`, hash as measured by the reviewer);
- its receiving review `RECOG_A1A_C4_NUMGEN_RECEIVING_REVIEW_20261020.md` (`e5a5fcecd2587d904200724842f829088b436c3eebd63d748517b73e1aeffec1`).

**What changed from v0.2:** §6 now records the C4 outcome and splits the result into three statements of different scope. §8 is updated. Everything else is unchanged from v0.2 except this header and §11.

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

## 6. C4 — R9-independent existence route: owner answers and RECOG disposition

**Owner answers.**
- **Number Genesis.**
  - INF-1 follows from L1 through L-BACKBONE, L-MONO and L-PHASE, and does not use RECOG R9.
  - $D_M$ is indexed from an arbitrary start on NUMGEN's tube; no B-event anchor is needed.
  - $C_D=\tau C_Q-\sum_{m\ge0}r_m$.
  - The only nontrivial generator hypothesis is the selected continuous $T$ (OPEN-P0).
  - No explicit radius and no uniform constant for the angular remainder are registered.
  - NUMGEN recommends that the identification stay a RECOG session result, with at most a later provenance pointer; no new RECOG import into NUMGEN.
  - The reviewer resolved the provenance dependency.
- **Dyadic.**
  - Conditional session acceptance of a separate existence-only corollary, not adopted.
  - The adopted T1, T2, chart-variable memory law and OPEN 21 stay unchanged, and no certified domain is widened.
  - Its two requested supplements, the C1 rational ceiling and an explicit $MQ_M\to1$, are supplied in the receipt; accepting them is for Dyadic.

**The corollary** `[ALG — SESSION, conditional on NUMGEN INF-1, the selected continuous T and the DYAD P4 chart bounds]`.

Domain: $U\cap U_{\rm NUMGEN}$, where $U=\{0<\lvert W_0\rvert\le\tfrac1{25}\}$ and $U_{\rm NUMGEN}$ is INF-1's tube, which exists but has no stated radius. Inside this common tube, $\eta_{\rm wrap}=\eta$, so NUMGEN's and Dyadic's $W$ coincide.

The argument:
1. §3.2 gives, for every integer $M\ge1$: $\Psi_W(M)=\Theta_W(0)-(D_M-\tau\log M)-\tau\log(MQ_M)$.
2. INF-1 gives $D_M-\tau\log M\to C_D$, and §3.3 gives $MQ_M\to1$. So $\Psi_{W,\infty}=\Theta_W(0)-C_D$.
3. Dyadic's unconditional P4-0 identity and offset bound give $\lvert\Psi_W(m)-\Psi_z(m)\rvert=\lvert\Delta_0(z_m)\rvert\le K_0\sqrt{q_m}\to0$. So $\Psi_{z,\infty}=\Psi_{W,\infty}$.

This is a second, existence-only route to the T1 limit, with a different dependency from the adopted T1: NUMGEN INF-1 in place of R9, on an existential domain.

**Three statements of different scope.** These must be cited separately.

| Statement | Domain | Depends on |
|---|---|---|
| (a) $C_D=\tau\log Q_0-M_W^{\rm exist}$, where $M_W^{\rm exist}:=\Psi_{W,\infty}-\Psi_W(0)$ exists by the corollary | $U\cap U_{\rm NUMGEN}$ (existential) | NUMGEN INF-1, Dyadic P4-0 and offset bounds; **no R9** |
| (b) $C_D^{\rm ext}(W_0)=\tau\log Q_0-M_W(W_0)$ | explicit Dyadic domain $U$ | Dyadic T1, hence **R9**; equals NUMGEN's $C_D$ on the overlap |
| (c) $C_D^{\rm ext}=\tau\log Q_0-\mathcal P_2(W_0)+E$, with the certified $E$ of §5 | row domains of §4 | **R9** and Dyadic OPEN 21 |

On the overlap, (a) and (b) give the same number; in (b), R9 supplies the limit itself. None of the three changes NUMGEN's INF-1 theorem, Dyadic's adopted grades, or R9.

**RECOG owner disposition** (Claude, co-owner; the decision rests with the PI).
- RECOG accepts the corollary and the three-way split as **RECOG session results** of A1a.
- They enter the RECOG DSN only through a separately reviewed release. A future v0.3.22 would carry them as a §6 cell with this exact grade and scope, plus a provenance pointer to NUMGEN INF-1.
- No owner theorem is transferred.

**Grade note for that future release (nonblocking).**
- The corollary is an analytic limit argument. Its inputs are NUMGEN `[RESULT] [from: ALG]` (INF-1) and Dyadic `[THM]` (the offset bounds).
- Under the weaker-input rule, the DSN label would be `[RESULT] [from: ALG]`-level, conditional as above.
- The `[ALG — SESSION …]` label proposed by Dyadic and the reviewer is kept here as the session label. The DSN grade is to be fixed at release review.

**Explicit radius (optional, separate).** An explicit radius would need four things:
- a uniform primitive angular remainder enclosure $\lvert\Delta\Theta_W+\tau Q\rvert\le C_{\rm ang}Q^{3/2}$ on a named invariant tube;
- confirmation of every INF-1 hypothesis there;
- the start set inside the tube, with C1 on it;
- the NF-INV transfer to the normalized disk.

This would be a separate Dyadic–NUMGEN interface task. It is not needed for (a).

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
| C1 explicit domain | Resolved at session level (§3.1, §3.3). The exact check is `recog_a1a_c1_angle_bound_check.py` (`343d737e…65c7a`): G1–G6 PASS, NC1–NC3 caught. Dyadic's acceptance of the ceiling derivation is pending |
| C2 common-start indexing | Closed. NUMGEN confirms an arbitrary start |
| C3 R9 at statement level | Unchanged for (b) and (c) of §6 |
| C4 R9-independent existence | **Provenance dependency resolved** (NUMGEN). Dyadic gives conditional session acceptance. RECOG owner disposition: accepted as a session result (§6). Not adopted |
| Explicit radius for (a) | Optional separate task (§6) |
| OPEN 21 constants against source | Quoted from v6.4.17 lines 837–843; not yet independently checked by a reviewer against source |

## 9. Changes from v0.1

1. **§3.** The incorrect "$(0,\pi)$ per step suffices" sentence is withdrawn. Lemma C1 is added (proposed by the reviewer, checked here, constant recomputed exactly).
2. **§3.3–§4.** Explicit identity domain $U$; row-A disk membership via NF-INV; row domains intersected with $U$.
3. **§4.** C2 closed by definition.
4. **§5.** The OPEN 21 passage is quoted with line references, and the evidence boundary is stated.
5. **§6.** The candidate's domain is stated precisely: the identity is explicit, INF-1 is existential.
6. **§7.** The numerical stability statement is corrected ($5.10\times10^{-6}$ and $9.36\times10^{-7}$).

## 10. Separation (unchanged)

The A1a constant identity does not give the A1b token schedule, and A1b does not give A1c recoverability. Nothing here defines a physical event, reads $C_D$ physically, or transfers anything to the comparator $C_W^{(h)}$. RECOG v0.3.21 is unchanged, and R6 stays ACTIVE.

## 11. Changes from v0.2

1. **Header:** the review trail now includes the Dyadic and NUMGEN C4 responses and the NUMGEN receiving review.
2. **§6** is rewritten.
   - It records the owner answers, the corollary with its grade and domain, and the three-way scope split (a)/(b)/(c).
   - It records the RECOG owner disposition, a grade note for a future release, and the conditions for an explicit radius.
   - It adds a note that $\eta_{\rm wrap}=\eta$ in the common tube.
3. **§8** has updated statuses.

