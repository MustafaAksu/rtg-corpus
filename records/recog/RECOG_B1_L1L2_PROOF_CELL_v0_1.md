# RECOG B1 — L1+L2 proof cell: sharpened R9 rows (summation lemma; Dyadic certificate values as ceilings)

**Date:** 25 October 2026 · **Author:** RECOG co-owner (Claude) · **Status:** `[SESSION]` proof cell, v0.1 — candidate `[THM]` rows for a later release. PI decision of 25 Oct 2026 (with review #5640170089): `START B1 L1+L2 PROOF CELL` — L1 exact; L2 from Dyadic's published numerical values with safe, rounded-up ceilings; the improvement is positive but not adopted. No DSN is edited; nothing is adopted.
**Governing edition:** `recog-v0.3.24` (`8c64bea2…e7c1`): RECOG-THM-R9-MEMORY, RECOG-THM-R9-COMPARATOR-INCOMPLETENESS (§6.13a; rows $(C_2,q_{\max})=(517,\tfrac1{400})$, $(163,\tfrac1{1600})$; proof constant $K_\Phi\le258.49/81.44$); Dyadic `dyad-v6.4.22` DYAD-THM-NF-REM (one-orbit contraction $0<q-\tfrac32q^2\le|\widehat F(z)|^2\le q-\tfrac12q^2$ on $0<q\le\tfrac1{400}$, giving $q_m\le q_0/(1+\tfrac12q_0m)$ and $\sum_mq_m^3\le2q_0^2$; $C_7=100$ (certificate value $85.07$) on $|z|\le\tfrac1{20}$, $C_7=30$ (certificate value $27.60$) on $|z|\le\tfrac1{40}$). Stage A record: `RECOG_B1_STAGEA_R9_BUDGET_SESSION_v0_1.md` v0.2.1.
**Certificate:** `evidence/recog/scripts/recog_b1_l1l2_sharpened_rows_cert.py` — mpmath interval arithmetic (60 digits; rigorous enclosures of $K_\Phi$ and $C_2'$), sympy for the integral identity; gates G1–G4, controls NC1–NC2 ALL PASS; outputs `evidence/recog/b1_l1l2/b1_l1l2_sharpened_rows_cert.json`, `_output.txt`.

## 0. Summary

| Row | Basis | $C_7$ | $K_\Phi\le$ | $C_2'$ (ceiling, 4 sig.) | old $C_2$ | window $q_0<|G|/C_2'$ | old window | gain |
|---|---|---|---|---|---|---|---|---|
| L1 large $|z|\le\tfrac1{20}$ | adopted statements only | 100 | 258.4848 | **259.2** | 517 | $2.952\times10^{-5}$ | $1.480\times10^{-5}$ | ×1.995 |
| L1 small $|z|\le\tfrac1{40}$ | adopted statements only | 30 | 81.4328 | **81.49** | 163 | $9.390\times10^{-5}$ | $4.695\times10^{-5}$ | ×2.000 |
| L1+L2 large | conditional: Dyadic certificate value $85.07$ as ceiling $85.1$ | 85.1 | 220.8471 | **221.4** | 517 | $3.456\times10^{-5}$ | $1.480\times10^{-5}$ | ×2.335 |
| L1+L2 small | conditional: Dyadic certificate value $27.60$ as ceiling $27.7$ | 27.7 | 75.6392 | **75.69** | 163 | $1.011\times10^{-4}$ | $4.695\times10^{-5}$ | ×2.154 |

The L1 rows change only RECOG's last proof step (the summation) and rest on adopted statements alone; they are `[THM]` candidates without qualification. The L1+L2 rows additionally take Dyadic's *published certificate values* as ceilings rounded up ($85.07\to85.1$, $27.60\to27.7$); they are `[THM]` `[assuming: C_7 ≤ 85.1 on |z| ≤ 1/20, resp. ≤ 27.7 on |z| ≤ 1/40]` until Dyadic registers those ceilings (notice). All four rows are additive: the adopted rows stay in force (rows not mixed). The incompleteness windows widen by the stated factors; the plan's targets ($C_2\le12.2$, $3.06$) are not reached, as Stage A predicted.

## 1. Lemma L1 (summation; RECOG-side, exact)

**Lemma.** If $q_m\le q_0/(1+\tfrac12q_0m)$ for all $m\ge0$ (DYAD-THM-NF-REM one-orbit bound), then
$$\sum_{m\ge0}q_m^3\le(1+q_0)\,q_0^2 .$$
*Proof.* $f(x)=(1+\tfrac12q_0x)^{-3}$ is decreasing on $[0,\infty)$, so $\sum_{m\ge1}f(m)\le\int_0^\infty f(x)\,dx=\bigl[-\tfrac1{q_0}(1+\tfrac12q_0x)^{-2}\bigr]_0^\infty=\tfrac1{q_0}$; adding the $m=0$ term, $\sum_{m\ge0}q_m^3\le q_0^3\bigl(1+\tfrac1{q_0}\bigr)=q_0^2+q_0^3$. $\square$
Tightness: $\sum_{m\ge1}f(m)\ge\int_1^\infty f=\tfrac1{q_0}(1+\tfrac12q_0)^{-2}$, so the exact sum of the majorant sequence lies between $q_0^3\bigl[1+\tfrac1{q_0}(1+\tfrac12q_0)^{-2}\bigr]$ and the lemma's bound; the ratio of the two is $\bigl(q_0+(1+\tfrac12q_0)^{-2}\bigr)/(1+q_0)\ge0.9975$ for $q_0\le\tfrac1{400}$ (G1 interval bracket; float sanity ratios $0.99875$, $0.99969$, $0.99995$ for $q_0=\tfrac1{400},\tfrac1{1600},10^{-4}$). The adopted $2q_0^2$ is this bound with $1+q_0$ replaced by $2$.

**Use in the R9 proof.** RECOG-THM-R9-MEMORY's last step is $|R|\le K_\Phi\sum_mq_m^3$; with L1, $|R|\le K_\Phi(1+q_0)q_0^2\le K_\Phi(1+\bar q)q_0^2$ on the row with $\bar q=q_{\max}$. Hence the row constant becomes $C_2'=\lceil K_\Phi(1+\bar q)\rceil_{4}$ (ceiling to four significant digits of the interval upper bound). Nothing else in the proof changes.

## 2. L2 (Dyadic certificate values as ceilings)

DYAD-THM-NF-REM publishes, next to the theorem ceilings, the certificate values $85.07$ (row $|z|\le\tfrac1{20}$) and $27.60$ (row $|z|\le\tfrac1{40}$). Read as round-to-nearest two-decimal prints of the Arb upper bounds, the true values are $<85.075$ and $<27.605$; the ceilings $85.1$ and $27.7$ are safe with margin. The certificate refuses any ceiling below the published value $+0.005$ (NC2). These ceilings are not Dyadic theorem statements: a RECOG row built on them carries `[assuming: …]` until Dyadic registers them (or publishes the Arb upper bounds), which the notice requests. $K_\Phi$ is then recomputed with the identical bound structure (interval-enclosed; G2 reproduces the adopted $258.48/81.43$ exactly).

## 3. Candidate DSN text (for a later stage-1 item; not adopted)

Under RECOG-THM-R9-MEMORY, after the existing rows:
> **Sharpened rows (v0.3.25 candidate; additive, rows not mixed).** `[THM]` With the summation lemma $\sum_mq_m^3\le(1+q_0)q_0^2$ (from the DYAD-THM-NF-REM one-orbit bound; RECOG-ALG-R9-SUM-LEMMA): $(C_2,q_{\max})=(259.2,\tfrac1{400})$ on $|z|\le\tfrac1{20}$ and $(81.49,\tfrac1{1600})$ on $|z|\le\tfrac1{40}$; windows of RECOG-THM-R9-COMPARATOR-INCOMPLETENESS $q_0<2.952\times10^{-5}$, resp. $9.390\times10^{-5}$. `[THM]` `[assuming: $C_7\le85.1$ on $|z|\le\tfrac1{20}$; $C_7\le27.7$ on $|z|\le\tfrac1{40}$ (Dyadic certificate values, rounded up; ceilings not yet registered by Dyadic)]` $(221.4,\tfrac1{400})$ and $(75.69,\tfrac1{1600})$; windows $3.456\times10^{-5}$, $1.011\times10^{-4}$. Certificate RECOG-ART-R9-SHARPENED-ROWS (§8). The original rows $(517,\tfrac1{400})$, $(163,\tfrac1{1600})$ remain valid and in force.

Proposed RIDs: `RECOG-ALG-R9-SUM-LEMMA` (L1), `RECOG-ART-R9-SHARPENED-ROWS` (certificate); the rows themselves as named additions to RECOG-THM-R9-MEMORY and its corollary (no renaming, no regrading).

## 4. Consumers and notices (prepared, via the PI)

- **Dyadic:** (i) informational — the summation lemma sharpens Dyadic's own "$\sum_mq_m^3\le2q_0^2$" to $(1+q_0)q_0^2$ from the same one-orbit bound (Dyadic may adopt it); (ii) request — register $85.1$ / $27.7$ (or the Arb upper bounds) as $C_7$ ceilings so the L1+L2 rows lose their `[assuming:]`; (iii) the R9 term in Dyadic's OPEN 21 constants ($C_2(\tfrac{256}{225})^2Q_0^2$) would shrink accordingly if Dyadic chooses to import the new rows.
- **OFN, RRF:** the R9 window statements they cite widen by ×2–2.3; no statement changes otherwise.

## 5. Certificate

G1 lemma (integral identity exact; rigorous bracket; float sanity); G2 reproduction of the adopted $K_\Phi$ by interval arithmetic ($258.4848$, $81.4328$; upper bounds $\le258.49/81.44$); G3 the four rows with 4-significant-digit ceilings; G4 every new $C_2'<$ old and every window wider. NC1 a mis-evaluated integral (factor $\tfrac12$) is contradicted by the explicit sum; NC2 a ceiling below the published certificate value is refused. Interval arithmetic: mpmath `iv` (outward rounding); not Arb, but the same bound structure as the Arb certificate and reproducing its values.

## 6. Not claimed

No change to the adopted rows; no claim about $C_7$ beyond Dyadic's published values; the targets of the study plan are not reached (Stage C remains the route); no second-order memory.
