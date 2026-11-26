# RRF BR-Q2 — sign typing, exact pair factorization and reconciliation proposal

**Date:** 26 November 2026. **Status:** [SESSION] / NONCANONICAL research record; not an adopted result, DSN amendment, pipe disposition or physical identification. ChatGPT preparer; Claude reviewer; PI decides adoption. Local labels P1–P5 below are not registered RIDs.

**Independence and scope:** The PI provided Claude's result summary before this derivation. This is an independently constructed rederivation and extension, not a blinded parallel derivation. The full PR #410 record and script were read after the main algebraic classification had been derived. Reconciliation is proposed, not yet reviewer-accepted. BR-Q2 is authorized separately from S2a; no result here enters the S2a/S2b candidate. S2a readback ACCEPT SCOPED (PR #404 head 98da97c311a917d1539b9c31afaba779bc75a73f, review 6076472389; #406 head a0ec75a52ead844b0dd06f9222ba48befa8009f5) and the PI_PENDING closure-wording decision remain separate.

## 1. Sources and exact question

Repository MustafaAksu/rtg-corpus, main checkpoint 14b46849791087cb264685bd5d70edd383c6cc41. CONVENTIONS read before editing. Governing owner tags below resolved to their commit and were checked as the latest relevant version-sort tags; the corresponding adoption/release records and BASELINE were inspected at their decision/identity fields. SHA-256 values independently recomputed from returned owner text; agree with the recorded published values. No owner proof certificate rerun.

| Source | Identity / reading extent |
|---|---|
| OFN binary recognition wrap-up (SESSION), records/ofn/NODE_BINARY_RECOGNITION_WRAPUP.md | blob c34b0921fcbccc186ea4e4149562ab98a8337bc0; SHA-256 2e120b9b300b3f13ff9269835a1e999cceaed5001239d551385dc04f2544d107; targeted §§2, 3B–F, 5–7, COR-BR-10/11/18; fixed register model and question, not an adopted physical model |
| pipes/RRF/20261104-OFN-binary-recognition-sign-typing.md | complete; blob 9586e2293187db961287d11f456118e5671316f6; SHA-256 37cf84755148f632fd8a872f69e3de646fe12f2f0d412a15360f240ce3bb6499; open question |
| rrf-v0.8.4 | commit d7d661c0b89c6f3d9ceea2e205bf75fccfcfbf8d; SHA-256 2fb0a0fe9d998be91618cb731e2dee7301952ffdbe374f4889dd5e61c5cbafce; §§4.1–4.2a (full targeted blocks); records/rrf/RTG_RRF_REPRESENTATION_REGISTRY_v0_8_4_ADOPTION_RECORD.md: adopted working representation standard only |
| ofn-v0.13 | commit 3f266eb4337c10d6e88a0ea90527dbe732922319; SHA-256 4a2d266bf89cd2130e901b7543bacbaf7fa3e844c60e355a2e3c23ef4f075a49; SG-OFN-PRESENTATION, RTG-OFN-DEF-BACKGROUND-TIME, OPEN-OFN-7, OPEN-OPA context; records/ofn/OFN_v0_13_RELEASE_RECORD.md |
| recog-v0.3.27 | commit 7bad433b1cea32c34c4c24f24c26b895998e735d; SHA-256 19556f913f51b98599faa6ad88c363dda0a278345677f3bd69f3b892d810e1f1; SG-R14 and comparator/event boundaries; records/recog/RECOG_v0_3_27_RELEASE_RECORD.md |
| dyad-v6.4.24 | commit f0af6392ed560b55aedc640bc166f0b87f612f7c; SHA-256 10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16; §6.2 linearization and §6.14 DYAD-THM-PRIM-CTR at stated local scope, used only for conditional non-transfer; records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md |

Governance: methodology-v1.4 §§3.3, 4.2–4.3, 12.2, 13.1/13.6 and programme-v1.5 SG-PROG-1 (S1 governing pins). Targeted source checks, not full scientific re-audits. LIT dependencies: none. No novelty claim.

Question: can the binary sign be typed by §4.2, which common-reference transports make its product invariant, and is there a bridge to a registered comparator track?

## 2. Declared finite model and P1–P2

For each fixed integer $n\ge1$, set $X_n=\{0,1\}^n$, $F(x_0,\dots,x_{n-1})=(1-x_{n-1},x_0,\dots,x_{n-2})$, $C=F^n$, $\lambda=e^{i\pi/n}$. Write $\pi(X)=\sum_j x_j\bmod 2$, $r(X)=(-1)^{\pi(X)}$, $P_X(t)=\sum_jx_jt^j$, $Z(X)=1-(1-\lambda)P_X(\lambda)$. The source identities are $F^{2n}=1$, $ZF=\lambda Z$, $ZC=-Z$. Let $X^\times=\{X:Z(X)\ne0\}$, $u=Z/|Z|$ there, $\Gamma(X,Y)=\overline{Z(X)}Z(Y)$, $P(X,Y)=r(X)r(Y)$.

**P1 [ALG] [SESSION] — character type.** Parity toggles at every step: removing the last bit and inserting its complement changes the sum by $1-2x_{n-1}$. Thus $r(F^aX)=(-1)^ar(X)$. The cyclic action has character $\chi(a)=(-1)^a$ on $\mathbb Z_{2n}$. In particular $\tau_{\rm sign}(r)=(-1)^nr$ under $C$. This is exact typed covariance, zero defect for the declared character, not a physical gauge identification. A single state readout is not a two-state comparator. For odd $n$, the reciprocal law under $C$ fails since $r^{-1}=r$; for even $n$ that equation happens to hold because $C$ acts trivially on the sign, but does not identify the semantic reciprocal type of §4.1. The full $F$ character is not an inversion law on $\{\pm1\}$.

**P2 [ALG] [SESSION] — exact transport subgroup.**
\[
P(F^aX,F^bY)=(-1)^{a+b}P(X,Y),\qquad
\Gamma(F^aX,F^bY)=\lambda^{b-a}\Gamma(X,Y).
\]
Consequently $H_n=\{(a,b)\in\mathbb Z_{2n}^2:a\equiv b\pmod2\}$ is the maximal subgroup of these pair actions preserving $P$ (index two), because $P$ is never zero. Shared complement is always in $H_n$; one-sided complement is in it iff $n$ is even. Equal elapsed step counts are not required. If relative step parity is supplied, transport outside $H_n$ is covariantly accounted for by its sign; absent that datum no invariance may be assumed. The product is an equality-of-parity comparator, $P(X,Y)=1$ iff the parities agree; $P(X,Y)P(Y,V)=P(X,V)$ on the same declared register. With a single fixed reference it is just the original readout times a fixed sign. No physical carrier, event clock, synchronization mechanism, edge-state or node-count inference follows. Route reference carrier/time to BR-Q5 / OPEN-OFN-7, event selection to RECOG BR-Q1/R6.

## 3. P3 — normalized phase and the orbit invariant

**[ALG] [SESSION]** On $X^\times$ define
\[
c(X)=r(X)u(X)^{-n}.
\]
Because $\lambda^n=-1$, $c(FX)=c(X)$ and $|c|=1$. No arbitrary orbit-origin choice is needed for this definition. Then
\[
P(X,Y)=\overline{c(X)}c(Y)
  \left(\Gamma(X,Y)/|\Gamma(X,Y)|\right)^n.
\]
The correction is one for same-orbit pairs (or whenever the two labels agree). This identity applies only to nonzero values. The correction factor is not in general determined by the simple normalized phase-power expression. It is NOT universally independent of the full exact $\Gamma$ (P4 below).

**[THM] [SESSION] — exact range of the simple global phase-power identity.** On all of $X^\times\times X^\times$, $P=(\Gamma/|\Gamma|)^n$ iff $n\in\{1,2,3,4\}$. Since the all-zero register has $Z=1,r=1$, pairwise equality is equivalent to $c\equiv1$.

Proof for small $n$: the all-zero register lies in a full $2n$-orbit (its nonzero $Z$ rotates by the primitive $2n$-th root) on which $u^n=r$. For $n=1,2$ this is the whole cube. For $n=3$ the other two states 010 and 101 have $Z=0$. For $n=4$ the singleton at index 1 has $Z=1-\lambda+\lambda^2=\lambda(2\cos(\pi/4)-1)$ with positive modulus different from one and $u^4=-1=r$. Its full 8-orbit is disjoint from the unit orbit and the two orbits exhaust the cube.

For $n\ge5$, take the singleton at index 2. Set $\theta=\pi/n$; then $z=1-e^{2i\theta}+e^{3i\theta}$ and $r=-1$. At $n=5$, $z=1-2\cos(2\pi/5)>0$, so $u^5=1\ne-1$. At $n>5$,
\[
\operatorname{Im}z=2\cos(5\theta/2)\sin(\theta/2)>0,\quad
\operatorname{Im}(e^{-i\theta}z)=\sin(2\theta)-2\sin\theta<0.
\]
These imply $0<\arg z<\theta$, hence $u^n$ lies in the open upper half-plane and is not $-1$. Thus $c$ differs from the all-zero label. This is an analytic proof for every $n$, not extrapolation from a census.

The theorem concerns this particular phase-power expression. It does not classify all possible nonlinear decoders of the normalized phase alone.

## 4. P4 — complete classification for the full algebraic Hermitian pair value

**[THM] [SESSION] [scope: fixed finite register, exact complex algebraic value]** There exists a function $D_n$ on the attained image of $\Gamma|_{X^\times\times X^\times}$ with $D_n(\Gamma(X,Y))=P(X,Y)$ if and only if $n=2^a$ for some integer $a\ge0$, or $n=3$. On the full cube (allowing $Z=0$) the condition is exactly $n=2^a$.

### Positive direction

For $n=1$, $Z=r$ is real and $\Gamma=P$. For $n=3$ on the nonzero sector, P3 gives $D_3=(\Gamma/|\Gamma|)^3$.

Let $n=2^a$, $a\ge1$. The polynomial $\Phi_{2n}(t)=t^n+1$ is the minimal polynomial of $\lambda$. In the dual-number ring $A=\mathbb F_2[\epsilon]/(\epsilon^2)$, $(1+\epsilon)^n+1=0$ because $n$ is even. Hence evaluation at $\lambda\mapsto1+\epsilon$ defines a well-defined ring homomorphism
\[
E:\mathbb Z[\lambda]\longrightarrow A .
\]
It intertwines complex conjugation with the identity because $(1+\epsilon)^{-1}=1+\epsilon$. In particular
\[
E(Z(X))=1+\epsilon\,\pi(X),\qquad E(\Gamma(X,Y))=1+\epsilon(\pi(X)+\pi(Y)).
\]
It follows that no $Z$ is zero and $P$ is determined by $\Gamma$. Explicitly if $G(t)$ is the unique reduced integer polynomial of degree less than $n$ representing $\Gamma$, then
\[
D_n(\Gamma)=(-1)^{G'(1)\bmod2}.
\]
The constant coefficient in the dual-number image is one. This is an exact algebraic decoder on the attained image, not a continuity assertion, not an arbitrary finite-precision measurement protocol, and not an assertion about dynamical comparison tracks.

### Negative direction I: composite non-dyadic lengths

For any composite $n$ with an odd prime divisor $p$ and $d=n/p>1$, let $q=\lambda^d$ and take the binary polynomials
\[
P_X(t)=\sum_{\substack{0\le j<p\\ j\ {\rm even}}}t^{jd},\quad
P_Y(t)=\sum_{\substack{0\le j<p\\ j\ {\rm odd}}}t^{jd}.
\]
Their difference $K(t)=(t^n+1)/(t^d+1)$ is the alternating block-root polynomial in wrap-up §3C. Since $q^p=-1$ and $q\ne-1,1$, evaluation gives $P_X(\lambda)=P_Y(\lambda)=1/(1-q)$ (geometric sums). Therefore
\[
Z(X)=Z(Y)=(\lambda-q)/(1-q)\ne0
\]
because $d>1$ and $d<n$. Their Hamming weights differ by one. Taking the all-zero register as first reference gives identical nonzero $\Gamma$ and opposite $P$. Thus no decoder exists. This covers every composite non-power-of-two length; it does not require injectivity of the spectral coordinate.

### Negative direction II: odd primes $p\ge5$

This case requires a pair-product collision even though the individual $Z$ values are faithful on the admitted nonzero sector. Set $n=p$, $\zeta=e^{2\pi i/p}$, $\ell=(p+1)/2$ so $\lambda=-\zeta^\ell$. Associate to each $X$ the subset $S_X\subset\mathbb Z_p$ by $u=\ell j$ and $u\in S_X$ iff $(-1)^j(2x_j-1)=1$. This is a bijection onto subsets (the index map is a permutation). Since $\sum_{u=0}^{p-1}\zeta^u=0$, 
\[
Z(X)=-(1-\lambda)\sum_{u\in S_X}\zeta^u,\qquad
r(X)=(-1)^{p(p-1)/2+|S_X|}.
\]
The second identity follows by multiplying the signed bits; in a product of two signs the fixed offset cancels. Thus $\Gamma=|1-\lambda|^2\overline{s_X}s_Y$ with $s_X=\sum_{S_X}\zeta^u$.

Choose the four subsets
\[
S_X=\{0,-1\},\quad S_Y=\{0,2\},\quad
S_U=\{0\},\quad S_V=\{0,1,2,3\}.
\]
All sums are nonzero: the two length-two factors are nonzero for odd $p$, and the fourth sum equals their product. The exact equality
\[
(1+\zeta)(1+\zeta^2)=1+\zeta+\zeta^2+\zeta^3
\]
implies $\Gamma(X,Y)=\Gamma(U,V)$; however $P(X,Y)=(-1)^{2+2}=1$ and $P(U,V)=(-1)^{1+4}=-1$. This excludes every remaining odd prime. Combined with the positive and composite cases it proves the claimed nonzero-sector classification.

### Zero fibre and full cube

For any $n$ not a power of two choose an odd prime divisor $p$, $d=n/p$ (possibly $d=1$). The signed-bit polynomial with coefficients $y_j=(-1)^{\lfloor j/d\rfloor}$ is $(1+t+\cdots+t^{d-1})K(t)$. It vanishes at $\lambda$, so the corresponding binary state has $Z=0$. Its successor also has $Z=0$ and opposite sign. A common all-zero reference register then gives $\Gamma=0$ with both possible products. Thus no function of $\Gamma$ can extend a parity decoder over all zero-fibre pairs. Dyadic lengths have no such fibre by the dual-number proof (and the direct $n=1$ calculation).

This completes the full-cube statement.

### P3/P4 consequence

The two factorization questions are inequivalent. For dyadic $n\ge8$, the simple phase-power formula fails, but exact $\Gamma$ recovers $P$. In those cases the orbit-label ratio itself can be recovered from full $\Gamma$ as $D_n(\Gamma)/(\Gamma/|\Gamma|)^n$. No extra independent reference label is required for that exact algebraic decoding problem. It is a different question whether an actual physical reference/comparison operation supplies $\Gamma$ or the relevant clock parity.

## 5. P5 — linear hexagon is not a registered DYAD transport

**[ALG] [SESSION]** In the wrap-up §3B $n=3$ example, $B$ intertwines $F_3$ with the linearization $A$ only. With $B(x)=(x_0-x_2,x_0+x_1-1)$, $\omega=e^{2\pi i/3}$, $W=\rho+\omega\eta$, the all-zero state has $W=-\omega=\lambda^{-1}$ and $Z=1$. The two rotations agree, hence $Z=\lambda W$ on the hexagon; both vanish on the other two states. Consequently $\Gamma=\overline{W(BX)}W(BY)$ on this linear image; $r=-W^3$ on its unit hexagon and $P=(\overline{W(BX)}W(BY))^3$. This is an exact statement about that linear observation model, not a registered state/domain/clock transport to the nonlinear W-track. The zero fibre is not parity-readable.

**[THM] [SESSION, conditional consequence of DYAD-THM-PRIM-CTR]** The unscaled hexagon has $Q=1$, outside the cited local domain. For an exact intertwining $H F=T^s H$ with finite periodic $F^m=1$ and positive integer stride $s$, if its image is inside the certified local contraction domain $Q\le1/400$, then $T^{6sm}H(X)=H(X)$. At a nonzero image point successive six-step blocks strictly decrease $Q$, remain in the domain and cannot return. Therefore $H(X)=P_1$ there. This conditional local obstruction is the wrap-up's §3B r2 consequence, not a new DYAD owner result; it does not imply a global obstruction or apply to an enlarged nonperiodic carrier or changed observation contract.

No registered transport to $C_{\rm pole}$, $C_W$, $C_z$, $C_W^{(h)}$ or $C^W_{\rm cov}$ is established (SG-R14 and rrf-v0.8.4 §§4.1–4.2). No discrete-to-continuous physical import, no physical pole gauge, no OPEN-A/B/E closure, no derivation of a physical recognition event.

## 6. Reconciliation with Claude's actual PR #410

Read in full after derivation: records/rrf/RRF_BRQ2_CLAUDE_INDEPENDENT_DERIVATION_20261126.md at head 856004b3d00cf41ae5c46816134e85737b7a117d (blob 8bc59453f76ef118d3c786d9b6b1fb558a70a634) and its script (blob 54b36cc1e6cda2df833c2272bafa77cd638ae8c0). The 76 PASS result is reviewer-reported; not rerun by this preparer. Our independent exact checker uses a separate implementation with SymPy cyclotomic polynomials.

| Reviewer row | Proposed disposition and boundary |
|---|---|
| R1 | Accept scoped. Character-typed single-state sign. Clarify that even-n complement satisfies the reciprocal equation numerically without establishing reciprocal type. |
| R2 | Accept. Exact index-two kernel, synchronization contract at equal step parity. Covariant comparison with known relative parity outside the kernel is also mathematically possible; no physical reference supplied. |
| R3 | Accept identity and orbit constancy; **amend the universal extra-datum wording**. The correction is necessary to this expression across distinct labels, not necessarily independent information relative to full Gamma. P4 gives the positive dyadic family and negative lengths exactly. |
| R4 | Accept bounded finite evidence at its reported scope, not the exact counts as independently reproduced here. P3 proves all-n phase-power boundary; P4 proves all-n exact-Gamma factorization. Our separate tests confirm the factor/collision cases for n<=9 and selected constructive tests. |
| R5 | Accept linear-only scope and refusal of nonlinear registered track. There is an exact linear image identity, not a physical bridge; keep the two notions distinct. |

No blanket assertion that all phase-only decoders fail at n>=5; P3 classifies only the specified nth power. No claim of physical observability of the exact ring decoder. Proposed scientific grades are SESSION deductions [ALG]/[THM], not adoption by OFN or any owner. No claim of priority or novelty.

## 7. Evidence, limitations, acceptance

Command: python -I evidence/rrf/scripts/rrf_brq2_gamma_factorization_checks.py (SymPy 1.14.0).

- Script SHA-256: 818c5c11bcb7b9a7d739e2cc190995afe2cb148b7a1f94e1d925c27d55a2f964.
- Output evidence/rrf/brq2/rrf_brq2_gamma_factorization_checks_output.txt SHA-256: 1c0c007c0512e7b246a2dc14647c5cb11d817039a24b194ebbffb0a04e80a132.
- EV-RUN in native Python container; integer polynomial remainder/equality calculations, no floating-phase tests. Positive cases n=1,2,3,4,8 exhaust ordered nonzero pairs; negative n=5,6,7,9 stop at first exact opposite-product collision. No count of all collisions claimed. Constructive checks up to 32: all tested non-dyadic zero and relevant nonzero collision witnesses, sampled dyadic dual-number decoding including 16 and 32, exact phase controls for small n and n>=6, plus perturbed-sign negative control. The n=5 positive-real singleton sign follows the analytic argument. The unbounded statements are established by the written proofs, not by finite tests; native program output alone does not certify semantic/physical claims. No owner certificate executed.

Suggested RRF response (proposal only): register-local single-state character type and pair law under stated $F$ action; common-reference equality of step parity (or supplied relative-parity correction for covariant use); define exact algebraic Gamma and distinguish P3/P4. Do not add a native RRF profile or identify any DYAD track. Keep physical gauge and clock/carrier selection OPEN, and send scoped answer to OFN only after reviewer/PI decision. BR-Q2 remains open in the inbox; no receiving disposition written.

Independent reviewer acceptance criteria: (A) recheck dual-number quotient, composite collision, odd-prime subset-product collision, zero fibre and exact phase-power proof including n=4/5; (B) rerun checker and verify both hashes, note finite coverage; (C) agree or correct R3 amendment and R5 scope; (D) no changes to canonical DSNs, S2a frozen input, existing pipe states, evidence of other streams, or owner roles. PI decides registration/communication and any future successor edition. The shared orientation file is left untouched in this PR to avoid conflicts with the open S2a and reviewer-lane PRs; record and PR provide the durable checkpoint for a later consolidated orientation update.
