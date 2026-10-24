# RECOG B1 Stage A — R9 error-budget decomposition and GO/NO-GO: session record

**Date:** 25 October 2026 · **Author:** RECOG co-owner (Claude) · **Status:** `[SESSION]` analysis record, v0.1. PI decision of 25 Oct 2026: `START B1 STAGE A — APPROVED` — scope: decompose the $C_2$ error budget of the existing R9 proof, check correlations, and give a reasoned GO/NO-GO for Stage B; no certified region is widened, no new $C_2$ is proved, no heavy Arb computation is started. No DSN is edited; nothing is adopted.
**Governing edition:** `recog-v0.3.24` (`8c64bea2…e7c1`); RECOG-THM-R9-MEMORY and RECOG-THM-R9-COMPARATOR-INCOMPLETENESS (§6.13a); certificate `recog_cell_r9_memory_cert.py` (Arb). Dyadic `dyad-v6.4.22` DYAD-THM-NF-REM rows $(C_7,r)=(100,\tfrac1{20})$, $(30,\tfrac1{40})$, certificate values $85.07$, $27.60$. Study plan §B1.
**Script:** `evidence/recog/scripts/recog_b1_stageA_r9_budget.py` (mpmath, 60 digits; reproduces the certificate's bound structure and attributes it; `[NUM]` jet-model orbits in mpmath/float64); output `evidence/recog/b1_stageA/b1_stageA_r9_budget.json`, `_output.txt`. Analysis only: the certificate itself is not changed or rerun.

## 0. Summary and decision

1. **Reproduction.** $K_\Phi=258.48$ (large row), $81.43$ (small row); $C_2=2K_\Phi=516.97$, $162.87$; windows $q_0<|G|/C_2=1.480\times10^{-5}$, $4.698\times10^{-5}$ — the certificate's values to the printed digits.
2. **Attribution.** The Dyadic degree-7 remainder ceiling $C_7$ enters as $\sqrt{1+4\tau^2}\,C_7=2.517\,C_7$ (the norm of $l\mapsto\operatorname{Im}l-2\tau\operatorname{Re}l$ applied to a modulus bound) and is **97.4 % of $K_\Phi$ on the large row, 92.7 % on the small row.** The study plan's "C₇ term is only about 37–39 % of $K_\Phi$" compared $C_7$ with $K_\Phi$ without the norm factor; that figure is corrected here. Everything RECOG-side (jet cross terms $4.3/3.5$, the exact cubic log term $1.69/1.68$, the $\Delta(qg)$ part $0.86/0.72$) totals $5.88$ on either row.
3. **Levers.** (L1) a sharper summation lemma $\sum_mq_m^3\le(1+q_0)q_0^2$ from the imported one-orbit bound $q_m\le q_0/(1+\tfrac12q_0m)$ — exact, RECOG-side, factor $\approx2$ on $C_2$; (L2) Dyadic certificate values instead of ceilings — factor $1.17$ / $1.08$; (L1+L2) $C_2$: $517\to221$, $163\to75$; windows $\times2.3$ / $\times2.2$. (L3) Even with $C_7=0$ the first-order budget floors at $C_2\approx5.9$ (with L1): the small-row target $C_2\le12.2$ would be met, the large-row target $C_2\le3.06$ **cannot** be met by any first-order route. (L4) Stage C — exact $O(q_0^2)$ memory with an $O(q_0^3)$ remainder — changes the window to $q_0<\sqrt{|G|/C_3}$; with a Dyadic $C_8\le300$ the whole large row and with $C_8\le10^4$ the whole small row would be covered.
4. **Correlations.** The budget adds independent worst cases; the only exploitable dependence is the $q$-dependence of the constants (evaluated at $\bar q$), worth $<1$ % because the dominant $C_7$ term is $q$-independent. The norm factor $2.517$ on $C_7$ is unavoidable for a modulus bound; a *directional* remainder bound from Dyadic (components along $\operatorname{Im}$ and $\operatorname{Re}$ separately) could recover up to that factor — a Dyadic-side lever, not a RECOG one.
5. **`[NUM]` truth gauge (jet model, no $C_7$).** Per-step $|\Delta\Phi|/q^3\le1.98$ over the first 3000 steps (mpmath), against the RECOG-side bound $5.88$ — the elementary inequalities are within $3\times$ of the jet truth; $\sum q_m^3/q_0^2\approx0.49$ (bound $2$; L1 bound $1+q_0$); $|M-q_0g|/q_0^2\approx0.937$, consistent with $1.98\times0.49$. The $170$–$550\times$ conservatism of $C_2$ noted in the plan is therefore $\approx250\times$ from $C_7$ (whose true size on the exact map is unknown to RECOG), $\approx4\times$ from the summation, and $\approx3\times$ from the inequalities.
6. **Decision proposal.** **NO-GO for Stage B as a route to the plan's targets** (a sharper $C_7$ row cannot reach $C_2\le12.2$ unless $C_7\lesssim2$, below any plausible degree-7 jet norm; the RECOG inequalities have at most $3\times$ left). **GO for Stage C preparation**: request from Dyadic the degree-7 resonant NF coefficients and a $C_8$ remainder row; RECOG then computes the exact $q^2$ term and a second averaging function. **Optional, cheap:** L1+L2 as a RECOG-side sharpening of the existing rows ($C_2$ $517\to221$, $163\to75$) — a new `[THM]` row (additive; existing rows stay in force), if the PI wants the $\times2.3$ window now. The PI decides (plan item D4).

## 1. The budget, term by term

Bound structure of `recog_cell_r9_memory_cert.py` (notation as there: $x=\widehat F/z-1$, $l=\log(1+x)$, $m=|\mu|=1.258$, $A=|a_{32}|+|a_{05}|=1.084$, $\bar q=r^2$):

| Term | Meaning | large row $(100,\tfrac1{400})$ | small row $(30,\tfrac1{1600})$ |
|---|---|---|---|
| $e_1^{C_7}=\sqrt{1+4\tau^2}\,C_7$ | Dyadic degree-7 remainder through the $\Psi$-norm | **251.66** (97.4 %) | **75.50** (92.7 %) |
| $e_1^{\rm cross}=\sqrt{1+4\tau^2}\,(A+C_7\bar q)(2m+(A+C_7\bar q)\bar q)/2$ | products of jet moduli in the $x^2/2$ term | 4.27 | 3.54 |
| $e_1^{\log3}=\sqrt{1+4\tau^2}\,(m+A\bar q+C_7\bar q^2)^3/(3(1-X))$ | cubic term of $\log(1+x)$ — the exact next order, not slack | 1.69 | 1.68 |
| $e_2$ ($g_{\max}D_1$, $\tau g_1(1+D_1\bar q)$, $g_1B_2$, $\tfrac{g_2}2(\tau+B_2\bar q)^2$) | the $\Delta(q\,g(\Theta))$ part | 0.86 (0.58, 0.05, 0.04, 0.18) | 0.72 (0.46, 0.05, 0.03, 0.18) |
| $K_\Phi$ | sum | 258.48 | 81.43 |
| factor 2 | $\sum q_m^3\le2q_0^2$ (imported) | ×2 | ×2 |
| $C_2$ | | 516.97 | 162.87 |
| window $|G|/C_2$ | $|G|=7.6520\times10^{-3}$ | $1.480\times10^{-5}$ | $4.698\times10^{-5}$ |

Targets (plan): $C_2\le|G|\cdot1600=12.24$ (incompleteness on the whole small row), $C_2\le|G|\cdot400=3.06$ (whole large row).

## 2. Levers

| Lever | Side | Exactness | $C_2$ large / small | window large / small | Reaches target? |
|---|---|---|---|---|---|
| L1 $\sum q_m^3\le(1+q_0)q_0^2$ | RECOG | exact lemma from $q_m\le q_0/(1+\tfrac12q_0m)$: $\sum_{m\ge0}(1+\tfrac12q_0m)^{-3}\le1+\tfrac2{q_0}\int_0^\infty(1+x)^{-3}dx=1+q_0^{-1}$ (numeric check: ratio to bound $0.997$) | 259.1 / 81.5 | $2.95\times10^{-5}$ / $9.39\times10^{-5}$ | no |
| L2 certificate values $C_7=85.07/27.60$ | Dyadic (values already in the owner text) | exact (ceilings replaced by certified values) | 441.5 / 150.8 | $1.73\times10^{-5}$ / $5.08\times10^{-5}$ | no |
| L1+L2 | | | **221.3 / 75.4** | **$3.46\times10^{-5}$ / $1.01\times10^{-4}$** | no ($\times2.3$, $\times2.2$) |
| L3 $C_7\to0$ (floor of the first-order budget, with L1) | hypothetical | — | 5.90 / 5.87 | $1.30\times10^{-3}$ | small row yes, large row **no** |
| directional $C_7$ (Re/Im components) | Dyadic | would need a new owner statement | up to ÷2.5 on the $C_7$ term | — | no by itself |
| L4 Stage C: exact $O(q^2)$, remainder $C_3q_0^3$ | Dyadic (degree-7 NF jet, $C_8$ row) + RECOG (second averaging function) | new theorem | $C_3\approx\tfrac23(2.517\,C_8+\text{jet part})$ | $q_0<\sqrt{|G|/C_3}$: $C_8=100$: $6.8\times10^{-3}$; $300$: $3.9\times10^{-3}$; $10^3$: $2.1\times10^{-3}$; $10^4$: $6.8\times10^{-4}$ | large row for $C_8\lesssim300$; small row for $C_8\lesssim10^4$ |

Reading of L4: the second-order route moves the dominant Dyadic constant from $q_0^2$ to $q_0^3$ and the comparison from $|G|/C$ to $\sqrt{|G|/C}$; this is why it reaches the whole row for any plausible $C_8$, where no first-order improvement can. Its RECOG part is a second averaging function $g_2(\Theta)$ with $g_2+\tau g_2'=$ (the $q^3$ coefficient of $\Delta\Psi$, carrying $e^{-6i\Theta}$ and $e^{-12i\Theta}$ harmonics from $a_{05}^2$ and the degree-7 resonant monomials $z^4\bar z^3$, $z\bar z^6$, $\bar z^7$), solvable since $1-6ik\tau\ne0$.

## 3. Correlation check

- The bound sums terms evaluated at $\bar q$ for every step; the actual steps have $q_m\le\bar q$ and the $q$-dependent terms ($e_1^{\rm cross}$, $e_1^{\log3}$, $e_2$) shrink with $q$, but they are $<8$ % of $K_\Phi$, so the gain is $<1$ %.
- The $C_7$ term is $q$-independent and direction-free; the $\sqrt{1+4\tau^2}$ factor is exactly the operator norm and is attained only if the remainder points along $(\operatorname{Im},-2\tau\operatorname{Re})$. No RECOG-side information constrains that direction; only Dyadic could.
- The summation factor and the per-step constant are independent in the proof; the jet-model truth shows both are loose (0.49 vs 2; 1.98 vs 5.88) and multiplies to the observed $0.937$.

## 4. Decision proposal (for the PI)

| Option | Content | Cost | Gain | Recommendation |
|---|---|---|---|---|
| Stage B (plan): new Dyadic $C_7$ row on a smaller disk | Arb campaign (PI machine), Dyadic release, notices | high | window $\times$ (current $C_7$ / new $C_7$) only; targets out of reach | **NO-GO** as a route to the targets |
| L1+L2 sharpened rows | RECOG lemma + certificate values; new `[THM]` row, additive | low (sandbox; a short cell and one release item) | $C_2$ $517\to221$, $163\to75$; window $\times2.3$ / $\times2.2$ | optional; PI's call |
| Stage C preparation | request to Dyadic: degree-7 resonant NF coefficients, $C_8$ remainder row (both rows); RECOG: second averaging function, exact $q^2$ memory coefficient, incompleteness on $q_0<\sqrt{|G|/C_3}$ | medium (Dyadic Arb work; RECOG algebra) | whole large row for $C_8\lesssim300$; whole small row for $C_8\lesssim10^4$; sharp $Q_0^2$ term for Dyadic P5 | **GO (prepare the request)** |

Nothing here changes RECOG-THM-R9-MEMORY or its window; no Dyadic statement is reinterpreted. The plan's §B1 note "the C₇ term is only about 37–39 %" should be corrected in the plan's next revision (it is $93$–$97$ % once the norm factor is counted).

## 5. Not done, by scope

No new $C_2$ is proved; no row is widened; no Arb computation; the L1 lemma is stated with its one-line proof and a numeric check but not registered; the Stage C request is drafted here, not sent.
