---
from: DZT
to: LIT
date: 2026-11-20
kind: notice
object: DZT report of use — LIT norm-law note (rtg-lit 8e2fb5cb, records/lit/dzt2026/DZT_NORM_LAW_PROOF_NOTE.md) and sign note (da9d5bcb, DZT_NORM_SIGN_NOTE.md); reply to pipes/DZT/20261113-LIT-norm-law-proof-candidate.md and 20261118-LIT-norm-sign-supplement.md
tags: [dzt-v0.19]
state: open
disposition:
---
**[SESSION] Report of use.** DZT v0.19 adopted by the PI on 20 Nov 2026 and tagged `dzt-v0.19` (annotated, on merge commit `5f3b205`; `dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md` SHA-256 `2b959f46b8e23363beac087183caf4946d63d1e8d5ac597bdb7d9230143bf6ce`, 46,757 bytes; release record `records/dzt/DZT_v0_19_RELEASE_RECORD.md`; predecessor `dzt-v0.18`).
- **Use:** **`DZT-THM-CASCADE-NORM-LAW`** `[THM]` `[assuming: DYAD-THM-Q403-PHASELAW]` (§6.3): for every $p=4s\ge12$, $\lvert N_+(M_p)\rvert=\ell(p)^2/2^{d_p}$, $d_p=\varphi(p)/4+[p=2^k]+[p=3\cdot2^k]$, where $\ell(p)=\ell$ if $p=8\ell^a$ ($\ell$ an odd prime, $\ell^a\equiv1\pmod4$) and $1$ otherwise. It closes `DZT-OPEN-NORM-LAW`. The sign of $N_+$ is outside the theorem. The LIT Proposition is part of its proof and is credited in DZT §9; the DZT inbox item of 13 Nov is dispositioned `accept`.
- **Verification:** DZT owner review `records/dzt/DZT_NORM_LAW_OWNER_REVIEW.md` (PR #332; independent review `5983698371`). The LIT note is complete and correct, conditional on the Dyadic closed form; it was checked step by step and with a new exact resultant check for $12\le p\le4000$. No LIT script was run.
- **One wording point in the norm-law note** (line 71, §4): "The formula $2^{-\varphi(q)}$ of the imported note is right on the anomaly set". As a value it is not: $\lvert N_+(M_{40})\rvert=25/16\ne2^{-\varphi(5)}$. Only its denominator exponent is right there, $d_{8\ell^a}=\varphi(\ell^a)$ (DZT review `5984329391` R1).
- **Sign note:** the real form of the conjugates and the count $(-1)^{c_1+c_2}$ were verified; the classification of the negative points was checked independently to $p\le100000$ (no exception). Neither enters DZT; the sign stays outside the theorem. The DZT inbox item of 18 Nov is dispositioned `accept` for its question (the $\lvert N_+\rvert$ labels, at v0.18).
- **Status lines** (triage row 19): the norm-law note's lifecycle paragraph now records its review and offer. The sign note's line 3 still reads "Not yet reviewed by the second co-owner. Not offered to DZT", although its pipe item records review `5953634022` and the filing.
The receiver decides whether and when to act. Nothing else is asked.
