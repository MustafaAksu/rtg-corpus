#### §4.2.1 AZ-owned diagnostic — seed-token resonance and tail risk (Action 1, Stage 1)

`[NUM diagnostic]` `[RID: AZ-NUM-TOKRES-S1]` `[scope: pinned TDR-G engine with TDRG-DEF-ORIENT; policy bound_symmetric; $N\in\{120,122\}$, $k=8$; four initial nodes; 800 ticks; node cap 300; endpoint $M\ge100$]` `[conv: orientation reference of TDR-G v2.12.14 (profile P1)]`
*Owned by this DSN. It is computed on the TDR-G engine, which is not changed; it is not a TDR-G result, not a bridge, and no bridge-candidate is promoted by it.*

**Statement.** In a registered, paired intervention on the engine's own initial draw — one of the four initial tokens $\delta_j$ is replaced, and the same base draw is run under every arm — replacing the token by a value $x$ with $4x\equiv0\pmod N$ raises the probability that the run ends with at least 100 nodes, against replacing it by a neighbour $x\pm1$:

| Contrast (1,500 base draws each) | Resonant arm | Comparison arm | Risk difference, registered interval | Discordant pairs | Registered reading |
|---|---|---|---|---|---|
| PC1 — $2x\equiv0$, $N=120$ | 0.2580 | 0.0153 (detuned) | $+0.2427$ $[+0.2166, +0.2681]$ | 374 / 10 | supported; Holm $p=1.780\cdot10^{-96}$ |
| PC2 — $2x\equiv N/2$, $N=120$ | 0.1853 | 0.0240 (detuned) | $+0.1613$ $[+0.1381, +0.1841]$ | 259 / 17 | supported; Holm $p=9.375\cdot10^{-57}$ |
| PC3 — $2x\equiv0$, $N=122$ | 0.2307 | 0.0113 (detuned) | $+0.2193$ $[+0.1944, +0.2436]$ | 336 / 7 | supported; Bonferroni-adjusted $p=2.375\cdot10^{-89}$ |
| PC4 — values nearest $N/4$, $N=122$ | 0.0087 | 0.0160 (native) | $-0.0073$ $[-0.0158, +0.0011]$ | 10 / 21 | equivalent to the native state within $\pm0.05$ |

PC1 and PC2 are the confirmatory family; PC3 and PC4 are a separate, supportive replication family at $N\equiv2\pmod 4$, where $2x\equiv N/2$ has no solution. Tests are exact McNemar tests on the paired outcomes. The registered controls read as required: at $N=120$ the node-label permutation left every compared quantity unchanged (0 of 400 permuted runs differ); in both cells a $\pm1$ perturbation of a non-resonant native token and the detuned replacement are equivalent to the native state within $\pm0.025$ on the draws whose native slot token is non-resonant; and the exact per-tick token law of the registration had no violation in any of the 19,900 runs. All four readings are unqualified.

**What the statement is.** The total causal effect of the token replacement on the registered endpoint, for the engine, profile, cells, horizon, cap and threshold named in the scope.

**What it is not.** No mechanism is established; the parent–child phase law of the registration is a candidate only. Nothing is shown about other $N$, other $k/N$, other policies, longer horizons or other thresholds; the endpoint is a threshold on a continuous distribution of $M$, and it is not the TDR-26 birth-anchored discriminator. Nothing is stated about TDR-26 or about any open module of TDR-G. There is no relation to the Hashimoto `4|q` rule of §4.3.3, to Dyadic cyclic-subgroup selection or to any DZT object beyond the numeral (SG-AZ-3, SG-AZ-7), and OPEN-P1 is untouched (SG-PROG-1). By the PI's outcome rule of 12 November 2026 the diagnostic does not by itself close `AZ-OPEN-PROMO`, change the maturity level, or become a TDR-G claim. The algebraic statements of the registration (the signed token alphabet and its corollaries) are offered to TDR-G through `pipes/TDRG/` and are not results of this DSN.

**Evidence.** `[artifact: AZ-ART-TOKRES-S1]` (§9): the registration, reviewed twice and accepted before the run; the campaign output of 19,900 records, run on the PI's server and deposited unchanged; the report; and a script that re-derives the registered analysis from the stored records, byte-identical to the campaign machine's output (`EV-BYTES`, `EV-HASH`, `EV-CODE`, `EV-RUN` for the analysis; the engine runs were made once, on the campaign machine). The four contrasts were recomputed from the raw records by the second co-owner with its own code (`EV-INDEP` for the aggregation, not for the runs). The run was interrupted once and resumed; the outcome rule and the authorisation naming the bytes were recorded after the run (report §8, §11).

