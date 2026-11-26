# RRF BR-Q2 — independent derivation (Claude, second co-owner)

**Date:** 26 November 2026.
**Status:** [SESSION] / NONCANONICAL. Independent derivation for the PI-authorized BR-Q2 research line. It was written before reading any ChatGPT BR-Q2 disposition; none existed on GitHub at writing time. It is not an RRF disposition, adoption, registry edit or pipe closure. Reconciliation with the preparer's own independent disposition, and the PI decision, come after. Nothing here enters the S2a candidate.
**Question:** `pipes/RRF/20261104-OFN-binary-recognition-sign-typing.md` (OFN, 4 Nov 2026). Model and statements: `records/ofn/NODE_BINARY_RECOGNITION_WRAPUP.md` (SHA-256 `2e120b9b…d107`), §2 and §3B; corrections COR-BR-10, -11 and -18.
**RRF rules applied:** `rrf-v0.8.4` §4.1 (comparator tracks, $S$-decomposition) and §4.2 (typed covariance $O(Sx)=\tau_O(O(x))$, which is not universal invariance); RECOG v0.3.27 SG-R14 (every comparator statement names its track).
**Checks:** `python -I evidence/rrf/scripts/rrf_brq2_sign_typing_checks.py`, exit 0, 76 PASS, with a negative control. Standard library only; exact arithmetic in $\mathbb Z[t]/\Phi_{2n}$ for equality tests. Output: `evidence/rrf/brq2/rrf_brq2_sign_typing_checks_output.txt`.

## 0. Setting and notation

The model is the wrap-up §2 register:
- $X_n=\{0,1\}^n$; update $F_n$; complement $C_n=F_n^n$; $G_n=\langle F_n\rangle\cong\mathbb Z_{2n}$.
- $r_n=(-1)^{\pi_n}$.
- $Z_n$ satisfies $Z_nF_n=\lambda_nZ_n$ with $\lambda_n=e^{i\pi/n}$.
- $X_n^\times=\{Z_n\ne0\}$, and $u=Z_n/|Z_n|$ on $X_n^\times$.
- Pair comparator: $\Gamma(X,Y)=\overline{Z_n(X)}\,Z_n(Y)$.

Whether $C_n$ or $F_n$ is a physical gauge or event succession is **not** decided here (OFN SG-OFN-PRESENTATION, OPEN-OFN-7; RRF OPEN-A). Every statement below is relative to the declared action of $G_n$ on the register model.

## 1. Results

**R1 — type of $r_n$.** `[ALG]` [scope: register model, action of $G_n$] [provenance: Claude derivation; checks T1]

From the wrap-up's $\pi_n(F_nX)=1\oplus\pi_n(X)$:
$$r_n(F_n^aX)=\chi(F_n^a)\,r_n(X),\qquad \chi(F_n^a)=(-1)^a .$$
So $r_n$ is a character-typed observable of $G_n$. Its law under $C_n=F_n^n$ is $\chi(C_n)=(-1)^n$, which is OFN's $\tau_{\rm sign}$. Under §4.2, $r_n$ has zero covariance defect for the pair $(r_n,\tau_\chi)$.

It is **not** reciprocal-typed. On $\{\pm1\}$, inversion is the identity, so a reciprocal-type law would force $C_n$-invariance, which fails at every odd $n$ (this confirms COR-BR-10). It is also not invariant ($C_+$) at odd $n$. The §4.1 table lists only two-state comparator types, so $r_n$ needs a type name of its own: a **single-state character type $\tau_\chi$**. In particular, $r_n$ alone is not a comparison.

**R2 — which transports make the product admissible.** `[ALG]` [scope: register model; pairs of registers each acted on by its own $G_n$] [checks T2]

For an independent pair action $(F^a,F^b)\in G_n\times G_n$:
$$r_n(F^aX)\,r_n(F^bY)=(-1)^{a+b}\,r_n(X)\,r_n(Y).$$
So the product is invariant **exactly** on the index-two subgroup
$$K=\{(F^a,F^b): a\equiv b \pmod 2\}.$$

Consequences:
- The shared complement $(C,C)=(F^n,F^n)$ lies in $K$ for every $n$.
- The single complement $(F^n,\mathrm{id})$ lies in $K$ iff $n$ is even. This is COR-BR-18, recovered as a corollary.
- A shared complement alone is not the governing condition. The admissible common-reference transport is any transport that advances both registers by **step counts of equal parity**. That is a two-register clock-parity contract.
- With a fixed reference state $Y=R$, the product $r(X)r(R)=\pm r(X)$ carries no relational content beyond R1.

The register model does not supply the clock-parity contract. Its carrier and clock are OFN questions (BR-Q5, OPEN-OFN-7), not RRF's.

**R3 — exact bridge to the register-native pair phase.** `[ALG]` [scope: $X_n^\times\times X_n^\times$] [checks T3, T4: exhaustive $n\le9$; for $n=10$, all pairs among the first 64 states]

Because $u^n(F^aX)=(-1)^a u^n(X)$, the orbit label
$$c(X)=r_n(X)/u(X)^n,\qquad |c|=1,$$
is constant on every $G_n$-orbit. It follows that
$$\boxed{\,r_n(X)\,r_n(Y)=\overline{c(X)}\,c(Y)\,\bigl(\Gamma(X,Y)/|\Gamma(X,Y)|\bigr)^n\,}$$
and, for $X,Y$ on a common $G_n$-orbit, $r_n(X)r_n(Y)=(\Gamma/|\Gamma|)^n$ exactly. Both sides carry the same $K$-law: $\Gamma(F^aX,F^bY)=\lambda_n^{\,b-a}\Gamma(X,Y)$, and $\lambda_n^n=-1$.

So the n-th power of the normalized pair phase reproduces the sign product. **The extra datum required is the orbit-label ratio** $\overline{c(X)}c(Y)$, which is a reference datum, not a quantity computable from $\Gamma$.

**R4 — when the bridge needs no labels.** `[NUM]` [scope: exhaustive finite census, as stated; not a general-$n$ claim] [checks T5–T7]

- The label is identically 1 on $X_n^\times$, so $r_Xr_Y=(\Gamma/|\Gamma|)^n$ holds globally, for $n=1,2,3,4$. It is not constant for every $n=5,\dots,12$ (2, 3, 4, 9, 10, 25, 44 and 64 distinct labels).
- No function of $\Gamma$ alone reproduces the product at $n=5,6,7,9$ on $X_n^\times$ (100, 1152, 2352 and 104,652 exact $\Gamma$-equal pairs with opposite products). No such clash occurs at $n=1,2,3,4,8$. For $n=8$ this says nothing about $n\ge16$.
- Zero fibre: whenever $\mathrm{Zero}(n)\neq\varnothing$ ($n=3,5,6,7,9,10$ in range), $\Gamma=0$ carries both product values, so no extension through $\Gamma$ exists there.

**R5 — W-track shape at $n=3$, linear only.** `[ALG]` [scope: the 6-cycle image of the wrap-up linear map $B$; unit-$Q$ hexagon] [checks T8]

On the 6-cycle, $(-1)^{\pi_3}=-W^3$ (wrap-up §3B), and
$$r_3(X)r_3(Y)=\bigl(\overline{W_X}W_Y\bigr)^3=C_W(X,Y)^3 .$$
This is a coincidence of algebraic shape with the cube of the W-track Hermitian comparator, through the linear resonance matching $B$ only.
- The hexagon ($Q=1$) is outside the certified DYAD domain.
- The wrap-up's local no-go (§3B r2, DYAD-THM-PRIM-CTR) excludes an exact local intertwining of the finite cycle with the nonlinear map.
- No registered transport `T-*` connects $X_n$ to any DYAD state space.

## 2. Answer to BR-Q2 (co-owner recommendation; RRF decision after reconciliation)

1. **May $r_n$ with $\tau_{\rm sign}$ serve under §4.2?** Yes, as a typed observable. It is character-typed for the declared $G_n$ action, with zero defect for $\tau_\chi$. It is not reciprocal-typed, and alone it is not a comparator. Whether it serves as *recognition* is RECOG's question (BR-Q1, R6), not RRF's.
2. **Which common-reference transport makes $r_n(X)r_n(Y)$ admissible?** Exactly the transports in $K$: a shared clock-parity contract between the two registers. A shared complement is one element of $K$, not the criterion. RRF types this requirement; it cannot supply its carrier.
3. **Which comparator track connects by an explicit bridge?**
   - No registered RRF track. $C_{\rm pole}$, $C_W$, $C_z$, $C_W^{(h)}$ and $C^W_{\rm cov}$ are DYAD-state tracks, and no register→DYAD transport is registered (BR-Q6).
   - Register-native: R3's identity connects the product to $(\Gamma/|\Gamma|)^n$, exactly on a common orbit and in general with an orbit-label reference datum. The label-free form holds only for $n\le4$ in the census.
   - R5 is a linear-only shape coincidence with $C_W^3$ at $n=3$, not a bridge.

   If OFN wants $\Gamma$ used, it should be proposed as a *register-local candidate comparator* with domain $X_n^\times$ and transport law $\Gamma\mapsto\lambda^{b-a}\Gamma$, under its own name. It must not be identified with the W-track (COR-BR-11 stands).
4. **Proposed registry consequences (not applied).** At a later edition, after reconciliation and a PI decision:
   - add a single-state "character type $\tau_\chi$" row to the §4.1 typing vocabulary;
   - record $K$ as the admissibility condition;
   - record R3 with the label datum, and R5 as linear-only.

   Nothing here closes OPEN-A or decides physical gauge.

## 3. Counterexample and risk search

The checks above were designed to falsify the stated claims:
- **Product invariance:** a non-$K$ pair transport preserving the product would contradict R2. None was found over all $(a,b)\in\mathbb Z_{2n}^2$ (state subset as coded for $n\ge5$; the "iff" follows from the one-line proof).
- **Label-free bridge:** T5 searched for a label-free bridge and found the counterexamples listed in R4.
- **Integrity of the checks:** a single flipped sign fails the checks (negative control).

The only general claims are R1–R3, each with a proof and an exhaustive check. R4 is a finite census by design.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
