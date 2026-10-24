# RECOG A1c, part 1 — a finite-prefix error envelope for the known-$a$ decoder, computable from declared data: session record

**Date:** 25 October 2026 · **Author:** RECOG co-owner (Claude) · **Status:** `[SESSION]` scientific record, v0.1. PI decision of 25 Oct 2026: `A1c START APPROVED`, order: (1) known-$a$ envelope computable from the record data, (2) unknown-$a$ joint estimation and guarantee conditions, (3) limited analytic study of Q1′ injectivity. This record is part (1). No DSN is edited; nothing is adopted.
**Governing edition:** `recog-v0.3.24` (`8c64bea2…e7c1`): RECOG-THM-A1B-SLIP-SCHEDULE-U (§6.13b), RECOG-RESULT-A1C-RECORD-PHASE-READOUT (§6.16e), OPEN R6 sub-item A1c-decoder. Inputs (all adopted): DYAD-THM-PRIM-CTR, RECOG-THM-A1A-RECIPROCAL-AMPLITUDE, the one-step pointwise bound of the A1b cell (§2 of `RECOG_A1B_A1C_SESSION_v0_1.md`, used in the THM), DYAD-THM-LPHASE-ROWA-REMAINDER, Lemma C′ constants.
**Script:** `evidence/recog/scripts/recog_a1c_known_a_envelope.py`; outputs `evidence/recog/a1c/a1c_known_a_envelope.json`, `_output.txt` (envelope table; `[NUM]` 12-orbit check at $2\times10^6$ steps).

## 0. Summary

1. **Result (Prop. 1).** For $x_0\in U$ with $a=Q_0^{-1}$ known and the $k$-th $7$-gap at block $M_k$, the THM's error term obeys $|\varepsilon_k|\le E(a,M_k)$ with the **explicit, monotone function of the declared data only**
$$E(a,M)=\tau Q^*+1.82\,Q^{*3/2}+5\arcsin\bigl(0.705\sqrt{Q^*}+0.257Q^*\bigr)+\tau\,\bar S(a,M)+\bar R(a,M),$$
($Q^*$, $\bar S$, $\bar R$ in §1), so the known-$a$ decoder has the certified record-only interval $L\in[c_k-E(a,M_k),\,c_k+E(a,M_k)]$, $c_k=\tau\psi(a+M_k)-(k-1)\tfrac\pi3$, and $\Psi_{W,\infty}=L-\tfrac\pi3n_0+2\pi\ell_0$ inherits it. This closes the "a-priori envelope" qualifier of the RESULT into a computable one; grade target `[ALG]` (elementary consequences of adopted theorems; constants explicit).
2. **Size.** $E(a,M)\approx187/\sqrt{a+M}$ for large $M$: $E=2.9$ at $M=10^3$, $1.8$ at $10^4$, $0.59$ at $10^5$, $0.19$ at $10^6$, $0.059$ at $10^7$ (almost independent of $a\in[625,2500]$); for $a=625$ and $M\le300$, $E>\pi$, i.e. the window is **vacuous modulo $2\pi$** there, and it determines $\Psi_\infty$ to better than one radian only from $M\approx3\times10^4$ on. $E$ is $93$–$95$ % the reciprocal-amplitude tail $\tau\bar S$; the block terms and $\bar R$ are $<7$ %.
3. **`[NUM]` check.** On 12 orbits in $U$ ($2\times10^6$ steps, 5–7 slips each, all gaps $\in\{6,7\}$): $\max_k|\varepsilon_k|/E(a,M_k)=0.0079$; every $L$ lies in the intersection of its windows; $E/(0.75\sqrt{Q_{M_k}})\in[118,251]$ — the certified envelope is $120$–$250\times$ above the observed error. ($\Psi_\infty$ is estimated at the run's end with tail scale $\sqrt{Q_{\rm end}}=1.7\times10^{-3}$; the ratio is insensitive to this.)
4. **Lever.** The looseness is almost entirely input (I2): $|Q_{m+1}^{-1}-Q_m^{-1}-1|<\tfrac{15}2\sqrt{Q_m}$ summed by absolute values gives $|e_m|\lesssim37.5\sqrt{a+m}$, whereas the increments oscillate (they are driven by the raw-frame quartic term, phase $e^{\pm3i\Theta}$) and their sum is observed to stay $O(\log m)$. A **RECOG-side averaging lemma for the reciprocal amplitude** (a second-order reciprocal law $Q_{m+1}^{-1}=Q_m^{-1}+1+\kappa_1Q_m+O(Q_m^{3/2})$ with an averaging function for the oscillating $\sqrt Q$ part) would make $\bar S=O(\log(a+M)/(a+M))$ and $E=O(\sqrt{Q_M})$ with a constant of order one — the natural part 1b. Not done here.
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

**Proposition 1 (computable known-$a$ envelope).** `[ALG]` target [scope: as RECOG-THM-A1B-SLIP-SCHEDULE-U; $a$ known]. $|\varepsilon_k|\le E(a,M_k)$ with $E$ as in §0; $E(a,\cdot)$ is decreasing in $M$, so the intersection of the windows over $k\le K$ is the last window. *Proof.* (I5) with Lemmas 1–4; the anchor and the $r_k$ partial-block points lie in block $M_k$. $\square$

**Values** ($E$; in brackets $\tau\bar S$, $\bar R$, block terms):

| $a$ | $M=10^3$ | $10^4$ | $10^5$ | $10^6$ | $10^7$ |
|---|---|---|---|---|---|
| 625 | 2.918 (2.606, 0.192, 0.120) | 1.816 (1.680, 0.086, 0.050) | 0.591 (0.546, 0.029, 0.016) | 0.187 (0.173, 0.009, 0.005) | 0.059 (0.055, 0.003, 0.002) |
| 1000 | 2.758 | 1.783 | 0.590 | 0.187 | 0.059 |
| 2500 | 2.532 | 1.667 | 0.585 | 0.187 | 0.059 |

Asymptotically $E\sqrt{a+M}\to187.3$ ($\tau\cdot150$ from the $\bar S$ tail constant $2\times75$, plus $6.45$ from $\bar R$ and the block terms' contribution at the same rate).

## 2. `[NUM]` check (not a proof input)

12 orbits ($Q_0\in\{\tfrac1{625},\tfrac1{1000},\tfrac1{2500}\}$, phases $0.3,1.7,3.9,5.1$), $2\times10^6$ primitive steps, F2(b) predicate, lift by principal increments; $\Psi_\infty$ estimated by $\Theta_W(M_{\rm end})-\tau\log Q_{\rm end}$ (tail scale $\sqrt{Q_{\rm end}}=1.7\times10^{-3}$). Per orbit 5–7 slips; all gaps $\in\{6,7\}$. Results: $\max_k|\varepsilon_k|/E(a,M_k)=0.0079$; $L$ in every window intersection (12/12); $E/(0.75\sqrt{Q_{M_k}})\in[118,251]$; last windows (half-width $E$) $0.34$–$0.46$ at $M_k\approx1.6$–$3.1\times10^5$. Earlier slips ($M_k\le2\times10^3$) have $E>2.5$: their windows carry almost no information modulo $2\pi$.

## 3. Consequences and next steps

- **For RECOG-RESULT-A1C-RECORD-PHASE-READOUT:** the "a-priori envelope" clause can be upgraded to "computable from $(a,k,M_k)$ by $E(a,M_k)$ of this record" in the next release (proposal; `[ALG]`); the OPEN R6 sub-item A1c-decoder keeps its unknown-$a$ half.
- **Part 1b (recommended before part 2):** a reciprocal-amplitude averaging lemma — show $e_m=\kappa\log(a+m)+O(1)$ or at least $|e_m|\le c_1\log(a+m)+c_2$ from the raw six-step jet (the $O(\sqrt Q)$ increment is the quartic term $F_4$ with phase $e^{\pm3i\Theta}$; one averaging step as in A1a/R9 removes it). This would bring $E$ to $O(\sqrt{Q_M})$ with an $O(1)$ constant and make the known-$a$ window informative from $M\sim10^3$ instead of $10^6$. It is RECOG-side and exact-rational (the degree-4 jet is in the A1b certificate).
- **Part 2 (unknown $a$):** with two slips $k_1<k_2$, $c_{k_2}-c_{k_1}=\tau[\psi(a+M_{k_2})-\psi(a+M_{k_1})]-(k_2-k_1)\tfrac\pi3$ is a strictly monotone function of $a$ whose value is known up to $E(a,M_{k_1})+E(a,M_{k_2})$; a guarantee for $a$ follows only when that is below the function's variation over the admissible $a$-range — with the present $E$ this never happens for $a\ge625$ (variation $\le\tau\log(1+M_{k_1}/a)\cdot$ small), so part 2 depends on part 1b. The least-squares decoder stays `[NUM]`.
- **Part 3 (Q1′):** unaffected.

## 4. Not claimed

No change to the THM or the RESULT; no claim for unknown $a$; the envelope is an upper bound, not an estimate of the error; the `[NUM]` ratios are observations on 12 orbits.
