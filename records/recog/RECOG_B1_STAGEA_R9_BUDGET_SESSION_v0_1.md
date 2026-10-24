# RECOG B1 Stage A — R9 error-budget decomposition and GO/NO-GO: session record

**Date:** 25 October 2026 · **Author:** RECOG co-owner (Claude) · **Status:** `[SESSION]` analysis record, **v0.2** (v0.1 at commit `4fb9aaf`; revised after the co-owner's review #5640076782: Stage A VERIFIED, Stage C estimate revised — four corrections, §6). PI decision of 25 Oct 2026: `START B1 STAGE A — APPROVED` — scope: decompose the $C_2$ error budget of the existing R9 proof, check correlations, and give a reasoned GO/NO-GO for Stage B; no certified region is widened, no new $C_2$ is proved, no heavy Arb computation is started. No DSN is edited; nothing is adopted.
**Governing edition:** `recog-v0.3.24` (`8c64bea2…e7c1`); RECOG-THM-R9-MEMORY and RECOG-THM-R9-COMPARATOR-INCOMPLETENESS (§6.13a); certificate `recog_cell_r9_memory_cert.py` (Arb). Dyadic `dyad-v6.4.22` DYAD-THM-NF-REM rows $(C_7,r)=(100,\tfrac1{20})$, $(30,\tfrac1{40})$, certificate values $85.07$, $27.60$. Study plan §B1.
**Script:** `evidence/recog/scripts/recog_b1_stageA_r9_budget.py` (mpmath, 60 digits; reproduces the certificate's bound structure and attributes it; `[NUM]` jet-model orbits in mpmath/float64); output `evidence/recog/b1_stageA/b1_stageA_r9_budget.json`, `_output.txt`. Analysis only: the certificate itself is not changed or rerun.

## 0. Summary and decision

1. **Reproduction.** $K_\Phi=258.48$ (large row), $81.43$ (small row); $C_2=2K_\Phi=516.97$, $162.87$; windows $q_0<|G|/C_2=1.480\times10^{-5}$, $4.698\times10^{-5}$ — the certificate's values to the printed digits.
2. **Attribution.** The Dyadic degree-7 remainder ceiling $C_7$ enters as $\sqrt{1+4\tau^2}\,C_7=2.517\,C_7$ (the norm of $l\mapsto\operatorname{Im}l-2\tau\operatorname{Re}l$ applied to a modulus bound) and is **97.4 % of $K_\Phi$ on the large row, 92.7 % on the small row.** The study plan's "C₇ term is only about 37–39 % of $K_\Phi$" compared $C_7$ with $K_\Phi$ without the norm factor; that figure is corrected here. Everything RECOG-side (jet cross terms $4.3/3.5$, the exact cubic log term $1.69/1.68$, the $\Delta(qg)$ part $0.86/0.72$) totals $5.88$ on either row.
3. **Levers.** (L1) a sharper summation lemma $\sum_mq_m^3\le(1+q_0)q_0^2$ from the imported one-orbit bound $q_m\le q_0/(1+\tfrac12q_0m)$ — exact, RECOG-side, factor $\approx2$ on $C_2$; (L2) Dyadic certificate values instead of ceilings — factor $1.17$ / $1.08$; (L1+L2) $C_2$: $517\to221$, $163\to75$; windows $\times2.3$ / $\times2.2$. (L3) Even with $C_7=0$ the first-order budget floors at $C_2\approx5.9$ (with L1): the small-row target $C_2\le12.2$ would be met, the large-row target $C_2\le3.06$ **cannot** be met by any first-order route. (L4) Stage C — exact $O(q_0^2)$ memory with an $O(q_0^3)$ remainder — needs (a) the degree-7 resonant NF coefficients ($z^7$, $z^4\bar z^3$, $z\bar z^6$), (b) a **degree-9** remainder row $C_9$ (the degree-8 resonant set is empty, so the $\lambda$-equivariant normal form through degree 8 has no degree-8 term; an $O(|z|^8)$ vector remainder would only give $O(q_0^{5/2})$ after summation), and (c) the second-order comparator-difference term $q_0^2\Delta g_2$ in the incompleteness criterion. Under these, the window is the positive root of $2|G|-q_0\,\|\Delta g_2\|-2C_3q_0^2>0$, at most $\sqrt{|G|/C_3}$; for $C_9\lesssim300$ (with $\|\Delta g_2\|$ small) the whole large row, for $C_9\lesssim10^4$ the whole small row would be covered. These are design estimates, not a theorem target yet (§2, §6).
4. **Correlations.** The budget adds independent worst cases; the only exploitable dependence is the $q$-dependence of the constants (evaluated at $\bar q$), worth $<1$ % because the dominant $C_7$ term is $q$-independent. The norm factor $2.517$ on $C_7$ is unavoidable for a modulus bound; a *directional* remainder bound from Dyadic (components along $\operatorname{Im}$ and $\operatorname{Re}$ separately) could recover up to that factor — a Dyadic-side lever, not a RECOG one.
5. **`[NUM]` truth gauge (jet model, no $C_7$).** Per-step $|\Delta\Phi|/q^3\le1.98$ over the first 3000 steps (mpmath), against the RECOG-side bound $5.88$ — the elementary inequalities are within $3\times$ of the jet truth; $\sum q_m^3/q_0^2\approx0.49$ (bound $2$; L1 bound $1+q_0$); $|M-q_0g|/q_0^2\approx0.937$, consistent with $1.98\times0.49$. The $170$–$550\times$ conservatism of $C_2$ noted in the plan is therefore $\approx250\times$ from $C_7$ (whose true size on the exact map is unknown to RECOG), $\approx4\times$ from the summation, and $\approx3\times$ from the inequalities.
6. **Decision proposal.** **NO-GO for Stage B as a route to the plan's targets** (a sharper $C_7$ row cannot reach $C_2\le12.2$ unless $C_7\lesssim2$, below any plausible degree-7 jet norm; the RECOG inequalities have at most $3\times$ left). **GO for Stage C preparation**: request from Dyadic the degree-7 resonant NF coefficients and a $C_8$ remainder row; RECOG then computes the exact $q^2$ term and a second averaging function. **Optional, cheap:** L1+L2 as a RECOG-side sharpening of the existing rows ($C_2$ $517\to221$, $163\to75$) — a new `[THM]` row (additive; existing rows stay in force), if the PI wants the $\times2.3$ window now. The PI decides (plan item D4).

## 1. The budget, term by term

Bound structure of `recog_cell_r9_memory_cert.py` (notation as there: $x=\widehat F/z-1$, $l=\log(1+x)$, $m=|\mu|=1.258$, $A=|a_{32}|+|a_{05}|=1.098084$ (v0.1 misprinted $1.084$; the script used the exact value), $\bar q=r^2$):

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
| L4 Stage C: exact $O(q^2)$, remainder $C_3q_0^3$ | Dyadic (degree-7 resonant NF coefficients; normal form through degree 8; $C_9$ row) + RECOG ($g_2$ with $(2+\tau\partial_\Theta)g_2=c_3$; exact $\Delta g_2$) | new theorem (design stage) | $C_3\approx\tfrac23(2.517\,C_9+\text{jet part})$ ($\sum q_m^4\le\tfrac23q_0^3(1+O(q_0))$) | upper estimate $\sqrt{|G|/C_3}$ (exact window: positive root of $2|G|-q_0\|\Delta g_2\|-2C_3q_0^2$): $C_9=100$: $6.8\times10^{-3}$; $300$: $3.9\times10^{-3}$; $10^3$: $2.1\times10^{-3}$; $10^4$: $6.8\times10^{-4}$ | large row for $C_9\lesssim300$; small row for $C_9\lesssim10^4$ (if $\|\Delta g_2\|$ is small) |

Reading of L4: the second-order route moves the dominant Dyadic constant from $q_0^2$ to $q_0^3$ and the comparison from $|G|/C$ to $\sqrt{|G|/C}$; this is why it reaches the whole row for any plausible $C_8$, where no first-order improvement can. Its RECOG part is a second averaging function $g_2(\Theta)$ in the correction $q^2g_2(\Theta)$: since $\Delta(q^2g_2)=-q^3(2g_2+\tau g_2')+O(q^4)$, the equation is $(2+\tau\partial_\Theta)g_2=c_3(\Theta)$ with $c_3$ the $q^3$ coefficient of $\Delta\Psi+\Delta(qg_1)$ — harmonics $0,\pm6,-12$ from $\mu$, $a_{32}$, $a_{05}$, $a_{05}^2$ and the degree-7 resonant monomials $z^7$ ($e^{+6i\Theta}$), $z^4\bar z^3$ (harmonic $0$), $z\bar z^6$ ($e^{-6i\Theta}$) — solvable since $2-6ik\tau\ne0$ for every integer $k$. (v0.1 wrote $1+\tau\partial_\Theta$ and listed $\bar z^7$, which is not resonant; corrected.) The per-step remainder after the correction must be $O(q^4)$ to sum to $O(q_0^3)$: this needs $|\widehat F-J_7|\le C_9|z|^9$ in a normal form through degree 8 (degree 8 is void by resonance), not an $O(|z|^8)$ bound, which sums only to $O(q_0^{5/2})$. The incompleteness criterion then reads $|q_0\Delta g_1+q_0^2\Delta g_2|>2C_3q_0^3$ with $\Delta g_2$ computed exactly from the same data; the window is the positive root of $2|G|-q_0\|\Delta g_2\|_{\rm witness}-2C_3q_0^2$, not $\sqrt{|G|/C_3}$ outright.

## 3. Correlation check

- The bound sums terms evaluated at $\bar q$ for every step; the actual steps have $q_m\le\bar q$ and the $q$-dependent terms ($e_1^{\rm cross}$, $e_1^{\log3}$, $e_2$) shrink with $q$, but they are $<8$ % of $K_\Phi$, so the gain is $<1$ %.
- The $C_7$ term is $q$-independent and direction-free; the $\sqrt{1+4\tau^2}$ factor is exactly the operator norm and is attained only if the remainder points along $(\operatorname{Im},-2\tau\operatorname{Re})$. No RECOG-side information constrains that direction; only Dyadic could.
- The summation factor and the per-step constant are independent in the proof; the jet-model truth shows both are loose (0.49 vs 2; 1.98 vs 5.88) and multiplies to the observed $0.937$.

## 4. Decision proposal (for the PI)

| Option | Content | Cost | Gain | Recommendation |
|---|---|---|---|---|
| Stage B (plan): new Dyadic $C_7$ row on a smaller disk | Arb campaign (PI machine), Dyadic release, notices | high | window $\times$ (current $C_7$ / new $C_7$) only; targets out of reach | **NO-GO** as a route to the targets (PI decision of 25 Oct 2026) |
| L1+L2 sharpened rows | RECOG lemma + certificate values; new `[THM]` row, additive, with a separate proof cell and safe ceilings | low (sandbox; a short cell and one release item) | $C_2$ $517\to221$, $163\to75$; window $\times2.3$ / $\times2.2$ | **GO** (PI decision of 25 Oct 2026): separate proof cell to follow |
| Stage C — mathematical feasibility and design only | request to Dyadic (to be drafted): degree-7 resonant NF coefficients $z^7,z^4\bar z^3,z\bar z^6$; normal form through degree 8; a $C_9$ remainder row per disk; RECOG: $g_2$ from $(2+\tau\partial_\Theta)g_2=c_3$, exact $q^2$ memory coefficient, exact $\Delta g_2$ on the witness, window as the positive root above | medium (Dyadic Arb work; RECOG algebra); no certificate campaign yet | whole rows for plausible $C_9$ (estimates); sharp $Q_0^2$ term for Dyadic P5 | **GO for feasibility/design** (PI decision of 25 Oct 2026); no theorem target claimed until (a)–(c) are in hand |

Nothing here changes RECOG-THM-R9-MEMORY or its window; no Dyadic statement is reinterpreted. The plan's §B1 note "the C₇ term is only about 37–39 %" should be corrected in the plan's next revision (it is $93$–$97$ % once the norm factor is counted).

## 5. Not done, by scope

No new $C_2$ is proved; no row is widened; no Arb computation; the L1 lemma is stated with its one-line proof and a numeric check but not registered; the Stage C request is drafted here, not sent.

## 6. Review round 1 — dispositions (co-owner review #5640076782 on `4fb9aaf`: Stage A VERIFIED; Stage C estimate revised)

| Review point | Disposition in v0.2 |
|---|---|
| $K_\Phi$, $C_2$, $C_7$ shares, L1+L2 values reproduced independently (258.485 / 81.433; 516.970 / 162.866; 97.36 % / 92.71 %; 221.323 / 75.434) | kept |
| second averaging function: $\Delta(q^2g_2)=-q^3(2g_2+\tau g_2')+O(q^4)$, operator $2+\tau\partial_\Theta$ | corrected (§2) |
| resonant degree-7 monomials are $z^7$, $z^4\bar z^3$, $z\bar z^6$; $\bar z^7$ is not resonant; an $O(|z|^8)$ remainder sums only to $O(q_0^{5/2})$ | corrected: degree-8 void by resonance; $C_9$ row required (§0, §2) |
| comparator difference $\Delta M=q_0\Delta g_1+q_0^2\Delta g_2+O(q_0^3)$: the window is not $\sqrt{|G|/C_3}$ without controlling $\Delta g_2$ | corrected: window = positive root of $2|G|-q_0\|\Delta g_2\|-2C_3q_0^2$; $\sqrt{|G|/C_3}$ kept as the upper estimate |
| $A=|a_{32}|+|a_{05}|=1.098084$, not $1.084$ | corrected (text only; the script used the exact value) |
| PI decisions: Stage B NO-GO; L1+L2 GO (separate proof cell, safe ceilings); Stage C GO for feasibility/design only; A1c START | recorded in §4 |

