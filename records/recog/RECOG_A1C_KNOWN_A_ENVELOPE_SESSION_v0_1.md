# RECOG A1c, part 1 — a finite-prefix error envelope for the known-$a$ decoder, computable from declared data: session record

**Date:** 25 October 2026 · **Author:** RECOG co-owner (Claude) · **Status:** `[SESSION]` scientific record, **v0.2** (v0.1 at commit `3db8bea`; revised after review #5640174052 — A1C-K1 window intersection, A1C-K2 part-1b target, typing; §5). PI decision of 25 Oct 2026: `A1c START APPROVED`, order: (1) known-$a$ envelope computable from the record data, (2) unknown-$a$ joint estimation and guarantee conditions, (3) limited analytic study of Q1′ injectivity. This record is part (1). No DSN is edited; nothing is adopted.
**Governing edition:** `recog-v0.3.24` (`8c64bea2…e7c1`): RECOG-THM-A1B-SLIP-SCHEDULE-U (§6.13b), RECOG-RESULT-A1C-RECORD-PHASE-READOUT (§6.16e), OPEN R6 sub-item A1c-decoder. Inputs (all adopted): DYAD-THM-PRIM-CTR, RECOG-THM-A1A-RECIPROCAL-AMPLITUDE, the one-step pointwise bound of the A1b cell (§2 of `RECOG_A1B_A1C_SESSION_v0_1.md`, used in the THM), DYAD-THM-LPHASE-ROWA-REMAINDER, Lemma C′ constants.
**Script:** `evidence/recog/scripts/recog_a1c_known_a_envelope.py`; outputs `evidence/recog/a1c/a1c_known_a_envelope.json`, `_output.txt` (envelope table; `[NUM]` 12-orbit check at $2\times10^6$ steps).

## 0. Summary

1. **Result (Prop. 1).** For $x_0\in U$ with $a=Q_0^{-1}$ known and the $k$-th $7$-gap at block $M_k$, the THM's error term obeys $|\varepsilon_k|\le E(a,M_k)$ with the **explicit, monotone function of the declared data only**
$$E(a,M)=\tau Q^*+1.82\,Q^{*3/2}+5\arcsin\bigl(0.705\sqrt{Q^*}+0.257Q^*\bigr)+\tau\,\bar S(a,M)+\bar R(a,M),$$
($Q^*$, $\bar S$, $\bar R$ in §1), so the **known-$a$ / declared-data token-prefix interval** $L\in[c_k-E(a,M_k),\,c_k+E(a,M_k)]$, $c_k=\tau\psi(a+M_k)-(k-1)\tfrac\pi3$, holds for every $k$, and $\Psi_{W,\infty}=L-\tfrac\pi3n_0+2\pi\ell_0$ inherits it. After $K$ slips the safe interval is the intersection $I_K=[\max_{j\le K}(c_j-E_j),\ \min_{j\le K}(c_j+E_j)]$, which contains $L$ and is never wider than any constituent; it need not equal the last window (the windows are not proved to nest, their centres move; v0.1's "the intersection is the last window" is withdrawn — on the 12 sampled orbits all 62 adjacent pairs happen to nest, a `[NUM]` observation only). This turns the "a-priori envelope" qualifier of the RESULT into a computable one *given $a$*; it is not an unknown-$a$ record-only decoder. Grade target `[ALG]` (elementary consequences of adopted theorems; constants explicit; the script's float64 table is an illustration of the formula, not a directed-rounding certificate).
2. **Size.** $E(a,M)\approx187/\sqrt{a+M}$ for large $M$: $E=2.9$ at $M=10^3$, $1.8$ at $10^4$, $0.59$ at $10^5$, $0.19$ at $10^6$, $0.059$ at $10^7$ (almost independent of $a\in[625,2500]$); for $a=625$ and $M\le300$, $E>\pi$, i.e. the window is **vacuous modulo $2\pi$** there, and it determines $\Psi_\infty$ to better than one radian only from $M\approx3\times10^4$ on. $E$ is $93$–$95$ % the reciprocal-amplitude tail $\tau\bar S$; the block terms and $\bar R$ are $<7$ %.
3. **`[NUM]` check.** On 12 orbits in $U$ ($2\times10^6$ steps, 5–7 slips each, all gaps $\in\{6,7\}$): $\max_k|\varepsilon_k|/E(a,M_k)=0.0079$; every $L$ lies in the intersection of its windows; $E/(0.75\sqrt{Q_{M_k}})\in[118,251]$ — the certified envelope is $120$–$250\times$ above the observed error. ($\Psi_\infty$ is estimated at the run's end with tail scale $\sqrt{Q_{\rm end}}=1.7\times10^{-3}$; the ratio is insensitive to this.)
4. **Lever (part 1b, target as corrected by the review).** The looseness is almost entirely input (I2) summed by absolute values ($|e_m|\lesssim37.5\sqrt{a+m}$). The raw reciprocal-amplitude error $e_m=Q_m^{-1}-(a+m)$ **cannot in general be brought to $O(\log m)$**: with $W=h(z)=z+h_2(z)+O(|z|^3)$ and $h_2(t)=ct^2$, $c=-\tfrac{3+i\sqrt3}8$, on the real ray, $Q_{\rm prim}=q-\tfrac34q^{3/2}+O(q^2)$ and $Q_{\rm prim}^{-1}=q^{-1}+\tfrac34q^{-1/2}+O(1)$; along phase subsequences the $\sqrt m$-order contribution is genuine (review #5640174052, A1C-K2; v0.1's $O(\log m)$ target is withdrawn). What can be sharpened is the **tail sum** $S^{\rm tail}_M=\sum_{m\ge M}(Q_m-\tfrac1{a+m})$ itself: express $Q_m$ through the normalized $q_m$ and the explicit angular contribution of $h_2$, use the normalized phase law, and bound the oscillating part by averaging — keeping $Q_{\rm prim}$ and $q$ distinct. That is the reformulated part 1b (tail averaging), not done here.
5. **Scope.** Nothing about unknown $a$ (part 2), nothing about injectivity (part 3), no event or WRITE statement (SG-R6); the envelope majorises the THM's own error term and uses no quantity outside $(a,k,M_k)$.

## 1. The envelope and its proof

Notation as in the THM: block base amplitudes $Q_m=Q(x_{6m})$, $a=Q_0^{-1}$; the $k$-th slip anchor $n_{j_k}=6M_k+r_k$, $0\le r_k\le5$; $\tau=2/\sqrt3$.

**Inputs.** (I1) $Q_m\le q̄_m:=1/(a+m/2)$ [DYAD-THM-PRIM-CTR]. (I2) $Q_{m+1}^{-1}=Q_m^{-1}+1+\delta_m$, $|\delta_m|<\tfrac{15}2\sqrt{Q_m}$ [RECOG-THM-A1A-RECIPROCAL-AMPLITUDE]. (I3) on $U_T$, $|W(Tx)/(\lambda W(x))-1|\le0.705\sqrt{Q(x)}+0.257Q(x)$ [A1b cell §2]. (I4) $|r_m|\le\tfrac{403}{250}Q_m^{3/2}$ [DYAD-THM-LPHASE-ROWA-REMAINDER]. (I5) the THM's error term: $|\varepsilon_k|\le\Delta_{j_k}+5\arcsin(0.705\sqrt{Q}+0.257Q)+\tau|S^{\rm tail}_{M_k}|+|R^{\rm tail}_{M_k}|$ with $Q$ the largest amplitude among the points of the slip block and $\Delta\le\tau Q+1.82Q^{3/2}$ at the anchor (Lemma C′).

**Lemma 1 (in-block amplitude).** With $f(Q)=Q(1+0.705\sqrt Q+0.257Q)^2$ (increasing), every point $T^ix_{6M}$, $0\le i\le5$, has $Q\le Q^*(a,M):=f^{\circ5}(q̄_M)$. *Proof.* $|W(Tx)|=|W(x)||1+\varepsilon|\le|W(x)|(1+0.705\sqrt Q+0.257Q)$ by (I3); iterate from $Q_{6M}\le q̄_M$ (I1). $\square$

**Lemma 2 (reciprocal-amplitude error).** $Q_m^{-1}=a+m+e_m$ with $|e_m|\le\bar e_m:=\tfrac{15}2\bigl[a^{-1/2}+4(\sqrt{a+(m-1)/2}-\sqrt a)\bigr]$ for $m\ge1$, $\bar e_0=0$. *Proof.* $e_m=\sum_{k<m}\delta_k$, $|e_m|\le\tfrac{15}2\sum_{k<m}\sqrt{Q_k}\le\tfrac{15}2\sum_{k<m}(a+k/2)^{-1/2}$ by (I2), (I1); the summand decreases, so $\sum_{k=0}^{m-1}g(k)\le g(0)+\int_0^{m-1}g=a^{-1/2}+4[\sqrt{a+(m-1)/2}-\sqrt a]$. $\square$

**Lemma 3 (two-sided amplitude bracket and $\bar S$).** $Q_m\in\bigl[\tfrac1{a+m+\bar e_m},\ \min(\tfrac1{a+m/2},\tfrac1{a+m-\bar e_m})\bigr]$ (the second entry of the min only when $a+m>\bar e_m$), hence $|Q_m-\tfrac1{a+m}|\le D_m:=\max\bigl(\tfrac1{a+m}-\tfrac1{a+m+\bar e_m},\ \min(\cdots)-\tfrac1{a+m}\bigr)$. For $a+m\ge5625$ (and $a\ge1$): $\bar e_m\le\tfrac{15}2\cdot5\sqrt{a+m}=37.5\sqrt{a+m}\le\tfrac{a+m}2$, so $D_m\le2\bar e_m/(a+m)^2\le75\,(a+m)^{-3/2}$. Therefore, with $m_c=\max(M,\lceil5625-a\rceil)$,
$$|S^{\rm tail}_M|\le\bar S(a,M):=\sum_{m=M}^{m_c-1}D_m+75\bigl[(a+m_c)^{-3/2}+2(a+m_c)^{-1/2}\bigr].$$
*Proof.* Lemma 2 and (I1); $\tfrac1{a+m-\bar e}-\tfrac1{a+m}=\tfrac{\bar e}{(a+m)(a+m-\bar e)}\le\tfrac{2\bar e}{(a+m)^2}$ when $\bar e\le\tfrac{a+m}2$; integral comparison for the tail. $\square$

**Lemma 4 ($\bar R$).** $|R^{\rm tail}_M|\le\bar R(a,M):=\tfrac{403}{250}\bigl[(a+M/2)^{-3/2}+4(a+M/2)^{-1/2}\bigr]$. *Proof.* (I4), (I1), integral comparison. $\square$

**Proposition 1 (computable known-$a$ envelope).** `[ALG]` target [scope: as RECOG-THM-A1B-SLIP-SCHEDULE-U; $a$ known]. $|\varepsilon_k|\le E(a,M_k)$ with $E$ as in §0, for every $k$; hence $L\in I_K:=[\max_{j\le K}(c_j-E(a,M_j)),\ \min_{j\le K}(c_j+E(a,M_j))]$ after $K$ slips. $E(a,\cdot)$ is decreasing in $M$, but the windows need not nest (their centres $c_j$ move), so $I_K$ is in general a proper subset of the last window and must be formed as the intersection. *Proof.* (I5) with Lemmas 1–4; the anchor and the $r_k$ partial-block points lie in block $M_k$. $\square$

**Values** ($E$; in brackets $\tau\bar S$, $\bar R$, block terms):

| $a$ | $M=10^3$ | $10^4$ | $10^5$ | $10^6$ | $10^7$ |
|---|---|---|---|---|---|
| 625 | 2.918 (2.606, 0.192, 0.120) | 1.816 (1.680, 0.086, 0.050) | 0.591 (0.546, 0.029, 0.016) | 0.187 (0.173, 0.009, 0.005) | 0.059 (0.055, 0.003, 0.002) |
| 1000 | 2.758 | 1.783 | 0.590 | 0.187 | 0.059 |
| 2500 | 2.532 | 1.667 | 0.585 | 0.187 | 0.059 |

Asymptotically $E\sqrt{a+M}\to187.3$ ($\tau\cdot150$ from the $\bar S$ tail constant $2\times75$, plus $6.45$ from $\bar R$ and the block terms' contribution at the same rate).

## 2. `[NUM]` check (not a proof input)

12 orbits ($Q_0\in\{\tfrac1{625},\tfrac1{1000},\tfrac1{2500}\}$, phases $0.3,1.7,3.9,5.1$), $2\times10^6$ primitive steps, F2(b) predicate, lift by principal increments; $\Psi_\infty$ estimated by $\Theta_W(M_{\rm end})-\tau\log Q_{\rm end}$ (tail scale $\sqrt{Q_{\rm end}}=1.7\times10^{-3}$). Per orbit 5–7 slips; all gaps $\in\{6,7\}$. Results: $\max_k|\varepsilon_k|/E(a,M_k)=0.0079$; $L\in I_K$ for every orbit (12/12); on these runs all 62 adjacent window pairs nest, so $I_K$ coincided with the last window (an observation, not a property); $E/(0.75\sqrt{Q_{M_k}})\in[118,251]$; last windows (half-width $E$) $0.34$–$0.46$ at $M_k\approx1.6$–$3.1\times10^5$. The float64 evaluation of $E$ illustrates the formula; the bound is the formula. Earlier slips ($M_k\le2\times10^3$) have $E>2.5$: their windows carry almost no information modulo $2\pi$.

## 3. Consequences and next steps

- **For RECOG-RESULT-A1C-RECORD-PHASE-READOUT:** the "a-priori envelope" clause can be upgraded to "computable from $(a,k,M_k)$ by $E(a,M_k)$ of this record" in the next release (proposal; `[ALG]`); the OPEN R6 sub-item A1c-decoder keeps its unknown-$a$ half.
- **Part 1b (reformulated; recommended before part 2):** *tail averaging in the right variable.* Not a bound on the raw $e_m$ (obstructed at order $\sqrt m$ by the $h_2$ term, §0 item 4) but a sharper bound on $S^{\rm tail}_M=\sum_{m\ge M}(Q_m-\tfrac1{a+m})$: write $Q_m=|h(z_m)|^2=q_m+2\operatorname{Re}(\bar z_mh_2(z_m))+O(q_m^2)$ with the normalized $q_m$ (Dyadic $q$-law, $q_m^{-1}=q_0^{-1}+m+O(\log m)$ in the chart) and the explicit $h_2$ angular term, whose phase follows the normalized phase law; sum the oscillating part by one averaging step and the non-oscillating part exactly. Expected outcome: $\bar S=O(\sqrt{Q_M})$ with an $O(1)$ constant instead of $150/\sqrt{a+M}$, keeping $Q_{\rm prim}$ and the chart $q$ distinct throughout (SG-R14; Dyadic I1–I5 interface). RECOG-side, exact-rational inputs ($h_2$, $\mu$, the $q$-law).
- **Part 2 (unknown $a$):** with two slips $k_1<k_2$, $c_{k_2}-c_{k_1}=\tau[\psi(a+M_{k_2})-\psi(a+M_{k_1})]-(k_2-k_1)\tfrac\pi3$ is a strictly monotone function of $a$ whose value is known up to $E(a,M_{k_1})+E(a,M_{k_2})$; a guarantee for $a$ follows only when that is below the function's variation over the admissible $a$-range — with the present $E$ this never happens for $a\ge625$, so part 2 depends on the reformulated part 1b. The least-squares decoder stays `[NUM]`.
- **Part 3 (Q1′):** unaffected.

## 4. Not claimed

No change to the THM or the RESULT; no claim for unknown $a$; the envelope is an upper bound, not an estimate of the error; the `[NUM]` ratios are observations on 12 orbits.

## 5. Review round 1 — dispositions (co-owner review #5640174052 on `3db8bea`: PARTIAL/CONDITIONAL ACCEPTANCE; Lemmas 1–4 and Prop. 1 acceptable; $E$ table and the asymptotic constant $187.309$ independently reproduced)

| Review point | Disposition in v0.2 |
|---|---|
| A1C-K1: decreasing $E$ does not imply nested windows; the safe interval is $I_K=[\max_j(c_j-E_j),\min_j(c_j+E_j)]$ | corrected in §0, Prop. 1 and §2; the 62/62 nesting on the samples marked `[NUM]` |
| A1C-K2: the raw $e_m$ cannot be made $O(\log m)$ ($Q_{\rm prim}^{-1}=q^{-1}+\tfrac34q^{-1/2}+O(1)$ via $h_2$); reformulate part 1b as tail averaging in the right variable | $O(\log m)$ target withdrawn; part 1b restated as a sharpening of $S^{\rm tail}_M$ through the normalized $q_m$ and the explicit $h_2$ angular term (§0 item 4, §3) |
| typing: "known-$a$ / declared-data token-prefix interval", not "certified record-only interval"; float64 output is not directed-rounding evidence | wording changed throughout; illustration/bound distinction stated |
| no rerun of the $2\times10^6$-step illustrations | none performed |

