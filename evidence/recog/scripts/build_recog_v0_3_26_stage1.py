#!/usr/bin/env python3
"""RECOG v0.3.26, stage 1: corrected intermediate (a build stage, not an edition) -- asymptotic correction + drift-centering successor,
per the PI decision of 28 Oct 2026 ("(b) ... PREPARE RECOG ASYMPTOTIC CORRECTION + DRIFT-CENTERING SUCCESSOR").

Applies, to the adopted v0.3.25 file (tag recog-v0.3.25), three separately marked groups:
  CORR  scientific correction (Methodology v1.4 §3.6, §7; Appendix B): the asymptotic-order sentences of RECOG-ALG-A1C-TAIL-HARMONICS (i), (iii)
        and RECOG-THM-A1C-SHARPENED-SCHEDULE were false for the closed-form majorants as defined (CORR-1: the M-independent slack b'^{-p} of
        the log-majorant Lg gives the majorants constant floors; CORR-2: the uniform slack kappa in the reference term gives an order
        (a+M)^{-1/2} piece).  Corrected closed forms (Lg_corr; the M-dependent bracket) replace them; the inequalities are unchanged and
        the corrected majorants are below the adopted ones at every grid point; the limits and orders hold for the corrected forms.
        Edits: [COR] notes in the two blocks (statements corrected in place, RIDs kept); the [NUM] grid sentence; the §1 sentence;
        two Appendix B entries; artifact row RECOG-ART-A1C-CORRECTED-GRID; errata notes are in the cell records.
  DRIFT new science: RECOG-ALG-A1C-RECIPROCAL-DRIFT `[ALG]` (Lemma 21 exact first order of the reciprocal law; Lemma 22 the log-free
        drift constant K_eps; Prop. 23 the centring identity) -- adopted rows only, no (D5); §1 clause; §7 NF6/NF-REM uses; artifact row
        RECOG-ART-A1C-DRIFT-CENTERING (cell PR #93 v0.2).
  ENV   new science (requires DRIFT): RECOG-ALG-A1C-LOGFREE-ENVELOPE `[ALG]` `[assuming: (D5)]` (Cor. 24: the centred envelope E^(5) with
        every term O_a(1/(a+M)); [NUM] grid and 73-slip results with the tolerance caveat).
Rules (as v0.3.25 stage 1): assertion-gated edits, Appendix A masked for live edits, modes str/line, decoupling variants (ENV needs DRIFT),
header identity lines, status summary and footer untouched.

usage: build_recog_v0_3_26_stage1.py BASE OUT EDITLOG_JSON [--only CORR,DRIFT,ENV]
  BASE = `git show recog-v0.3.25:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md`
"""
import hashlib, json, sys

BASE_SHA = "86cae8ff094d63d077ec5c0887451775ec3a26485cfad95833d8390bda4bd7db"
APPA_START = "## Appendix A — Version History"
APPA_END = "## Appendix B —"
PREV_TAG = "recog-v0.3.25"
D5 = r"`[assuming: Dyadic row-A bridge constants $c_Q=0.79246$, $c'_Q=0.36915$ ($|D_Q|\le c_Qq^{3/2}$, $|D_Q-D_3|\le c'_Qq^2$) and the remainder decomposition $r=\Lambda_3+{\rm rest}$ with its constants, as published in the proof of DYAD-THM-LPHASE-ROWA-REMAINDER (certified by DYAD-ART-LPHASE-ROWA); proof constants, not theorem rows; registration requested (§7)]`"

# ---------------------------------------------------------------- CORR texts ----------------------------------------------------------------
COR_TAIL_I_OLD = r"$\bar S'\sqrt{a+M}\to|\phi_1|/|\tfrac12+i\tau|+|\phi_3|/|\tfrac12+3i\tau|=0.74850$ and $\bar R'\sqrt{a+M}\to1.0753$ (part 1: $\approx150$ and $9.12$; the order $M^{-1/2}$ is not removed);"
COR_TAIL_I_NEW = r"$\bar S'\sqrt{a+M}\to|\phi_1|/|\tfrac12+i\tau|+|\phi_3|/|\tfrac12+3i\tau|=0.74850$ and $\bar R'\sqrt{a+M}\to1.0753$ (part 1: $\approx150$ and $9.12$; the order $M^{-1/2}$ is not removed) — `[COR]` (v0.3.26) these limits hold for the **corrected** closed forms, in which the log-majorant $\sum_{m\ge M}\log(1+m/2b')(b'+m)^{-p}$ is bounded by its first term plus the integral in the decreasing regime $M\ge b'$ and by the explicit finite sum below (`Lg_corr`, certified in RECOG-ART-A1C-DRIFT-CENTERING, G3b); the v0.3.25 forms carried the $M$-independent slack $b'^{-p}$ and had constant floors ($\bar S'\sqrt{a+M}\to\infty$), so the limits were false for them (Appendix B, RECOG-ALG-A1C-TAIL-HARMONICS-LIMITS-V0325); the corrected forms are below the v0.3.25 ones at every grid point (RECOG-ART-A1C-CORRECTED-GRID), so the inequalities (i)–(iii) and the universal ceiling are unchanged;"
COR_TAIL_III_OLD = r"with $E'\sqrt{a+M}\to5.4646$ (part 1: $187.31$);"
COR_TAIL_III_NEW = r"with $E'\sqrt{a+M}\to5.4646$ (part 1: $187.31$) for the corrected closed forms (`[COR]` v0.3.26, as in (i));"
COR_SCHED_OLD = r"and $E'''(a,M_k,r_k)=O_a\bigl((1+\log(a+M_k))/(a+M_k)\bigr)=o((a+M_k)^{-1/2})$; a pure $O((a+M_k)^{-1})$ is not claimed (the logarithmic term is $\tau A_1$)."
COR_SCHED_NEW = r"and, for the **corrected** closed forms (`[COR]` v0.3.26: `Lg_corr` in the majorant $\bar A_1$ of $|A_1|$ and the $M$-dependent bracket $q_M^{-1}\in[b'+M-\bar\epsilon_M,\,a+\Delta_a+M+\bar\epsilon_M]$ in the reference term ${\rm ref}_d$), $E'''(a,M_k,r_k)=O_a\bigl((1+\log(a+M_k))/(a+M_k)\bigr)=o((a+M_k)^{-1/2})$; a pure $O((a+M_k)^{-1})$ is not claimed for this envelope (the logarithmic term is $\tau\bar A_1$; the log-free successor is RECOG-ALG-A1C-LOGFREE-ENVELOPE). The v0.3.25 forms had a constant floor $\approx\tau\cdot2\gamma_0b'^{-2}$ ($1.1\times10^{-6}$ at $a=625$) from the slack $b'^{-2}$ of `Lg` and an order-$(a+M)^{-1/2}$ piece $\tfrac{\sqrt3}8\tfrac\kappa2(a+M)^{-1/2}$ from the uniform slack $\kappa$ in $q^+_M$, so these order sentences were false for them (Appendix B, RECOG-THM-A1C-SHARPENED-SCHEDULE-ORDER-V0325); the inequality is unchanged and the corrected $E'''$ is below the v0.3.25 one at every grid point (RECOG-ART-A1C-CORRECTED-GRID)."
COR_NUM_OLD = r"At $a=625$ (worst $r$): $E'''=0.029$ at $M=10^3$ ($E''$ of the in-block cell $0.078$; $E'$ $0.166$; part 1's $E$ $2.92$), $4.3\times10^{-3}$ at $10^4$, $4.5\times10^{-4}$ at $10^5$, $4.7\times10^{-5}$ at $10^6$, $5.8\times10^{-6}$ at $10^7$; $E'''(a+M)\to$ about $45$, $52$, $69$ for $a=625,1000,2500$ on the grid."
COR_NUM_NEW = r"At $a=625$ (worst $r$; corrected closed forms, v0.3.26): $E'''=0.029$ at $M=10^3$ ($E''$ of the in-block cell $0.078$; $E'$ $0.166$; part 1's $E$ $2.92$), $4.3\times10^{-3}$ at $10^4$, $4.5\times10^{-4}$ at $10^5$, $4.6\times10^{-5}$ at $10^6$, $4.7\times10^{-6}$ at $10^7$ (v0.3.25 forms: $4.7\times10^{-5}$, $5.8\times10^{-6}$); $E'''(a+M)$ is about $45$, $52$, $69$ for $a=625,1000,2500$ on the grid $M\le10^7$ and $E'''(a+M)/(1+\log(a+M))$ decreases from $2.2$ to $1.7$ ($a=625$) between $M=10^9$ and $10^{13}$."
S1_COR_OLD = r"computable from the same declared data, $E'''=O_a((1+\log(a+M_k))/(a+M_k))$; the record-only operation"
S1_COR_NEW = r"computable from the same declared data, $E'''=O_a((1+\log(a+M_k))/(a+M_k))$ for the corrected closed forms of v0.3.26 (`[COR]`, Appendix B); the record-only operation"
APPB_OLD = "**[FAIL | RID: RECOG-FAIL-K-FROM-SADDLE]** Derive the antipodal band width $k$ from the $P_2$ saddle spectrum alone. Reason: eigenvalues fix width–lifetime scaling, not width; invariant under local rescaling. Closed: v0.1."
APPB_NEW = APPB_OLD + "\n\n" + r"**[RETRACTED | RID: RECOG-ALG-A1C-TAIL-HARMONICS-LIMITS-V0325]** The limit sentences of RECOG-ALG-A1C-TAIL-HARMONICS (v0.3.25) for the closed-form majorants as then defined: $\bar S'\sqrt{a+M}\to0.74850$, $\bar R'\sqrt{a+M}\to1.0753$, $E'\sqrt{a+M}\to5.4646$. Reason (CORR-1, drift-centering cell `records/recog/RECOG_A1C_DRIFT_CENTERING_SESSION_v0_1.md` §4): the log-majorant `Lg(p,b',M)` of part 1b bounds $\sum_{m\ge M}\log(1+m/2b')(b'+m)^{-p}$ by an expression containing the $M$-independent slack $b'^{-p}$, so the majorants $\bar A_1$, $\bar S'$, $\bar R'$, $E'$ have constant floors and the scaled quantities grow without bound ($\bar S'\sqrt{a+M}=4.0$ at $M=10^{13}$, $a=625$); the true tails decay, the majorants did not. The inequalities, the grid values ($M\le10^7$, changed by $<0.5$ % at $M\le10^5$) and the universal ceiling $E'\le0.31$ are unaffected. Replaced by: the same limits for the corrected closed forms (`Lg_corr`: first term + integral in the decreasing regime, explicit finite sum below $b'$; certified below `Lg` and above brute-force sums, RECOG-ART-A1C-DRIFT-CENTERING G3b; the limits reached to $10^{-4}$ at $M=10^{13}$, RECOG-ART-A1C-CORRECTED-GRID), stated in §6.13b with `[COR]`. Version: v0.3.26." + "\n\n" + r"**[RETRACTED | RID: RECOG-THM-A1C-SHARPENED-SCHEDULE-ORDER-V0325]** The order sentence of RECOG-THM-A1C-SHARPENED-SCHEDULE (v0.3.25) for the envelope as then defined: $E'''=O_a((1+\log(a+M_k))/(a+M_k))=o((a+M_k)^{-1/2})$ (and $E'''\sqrt{a+M}\to0$ in the combined-tail cell). Reason (CORR-1, CORR-2): the envelope's term $\tau\bar A_1$ inherited the constant floor $\approx\tau\cdot2\gamma_0b'^{-2}$ of `Lg`, and its reference term ${\rm ref}_d$ used $q^+_M=((1-\kappa)(b'+M))^{-1}$ with the uniform slack $\kappa=\sup_m\bar\epsilon_m/(b'+m)\approx1.3\times10^{-3}$, an order-$(a+M)^{-1/2}$ piece $1.45\times10^{-4}(a+M)^{-1/2}$; hence $E'''\sqrt{a+M}\to\infty$ for the v0.3.25 forms. The inequality $|\varepsilon'''_k|\le E'''$ is unaffected (a valid majorant remains valid), as are the grid values at $M\le10^5$ ($<0.5$ %); at $M=10^6$, $10^7$ the corrected values are $2$ % and $19$ % smaller. Replaced by: the same order sentence for the corrected closed forms (`Lg_corr`; the $M$-dependent bracket of part 1b Lemma 2 in ${\rm ref}_d$), stated in §6.13b with `[COR]`; and the log-free successor RECOG-ALG-A1C-LOGFREE-ENVELOPE ($E^{(5)}=O_a(1/(a+M))$). Version: v0.3.26."
S8_CORR = r"- [RID: RECOG-ART-A1C-CORRECTED-GRID] `[v0.3.26]` :: `recog_v0_3_26_corrected_grid.py` (sha256 `61b8370d11b7a90936216874f835af864bb3af3b842e9aed3e6c08e25df01864`) + `evidence/recog/v0.3.26/corrected_grid.json` (`569b018e…e141`) :: the A1c envelope grids ($a\in\{625,1000,2500\}$, $M=10^3\ldots10^7$, all $r$) with the corrected closed forms (`Lg_corr` of RECOG-ART-A1C-DRIFT-CENTERING in $\bar A_1$, $\bar S'$, $\bar R'$, $E'$, $E'''$; the $M$-dependent bracket in ${\rm ref}_d$) next to the v0.3.25 values, and the scaled values at $M=10^9,10^{11},10^{13}$ ($\bar S'\sqrt{a+M}$, $\bar R'\sqrt{a+M}$, $E'\sqrt{a+M}$ at their stated limits to $10^{-4}$; $E'''\sqrt{a+M}\to0$); the corrected majorants are below the adopted ones at every grid point; no orbit rerun :: `[COR]` evidence (closed-form evaluation)"

# ---------------------------------------------------------------- DRIFT / ENV blocks ---------------------------------------------------------
DRIFT_BLOCK = r"""**Chart reciprocal drift centring (A1c, v0.3.26; new science, separately reviewed).** Notation as above; $H_m(b):=\psi(b+m)-\psi(b)=\sum_{j<m}\tfrac1{b+j}$ and $\tilde b_m:=b+m-\tfrac{29}{216}H_m(b)$.

`[ALG]` [RID: RECOG-ALG-A1C-RECIPROCAL-DRIFT] [scope: $x_0\in U$, chart row A, block base points; adopted rows only — DYAD-ALG-NF6 ($\mu$, $a_{32}$, $a_{05}$), DYAD-THM-NF-REM ($C_7=100$, one-orbit contraction), the part-1b closed forms and $c_\theta$; no Dyadic proof constant] [proof: cell `records/recog/RECOG_A1C_DRIFT_CENTERING_SESSION_v0_1.md` v0.2 §§1–3 (Lemmas 21–22, Prop. 23); certificate RECOG-ART-A1C-DRIFT-CENTERING] (i) *Exact first order.* $\delta_m:=q_{m+1}^{-1}-q_m^{-1}-1=-\tfrac{29}{216}q_m-2\operatorname{Re}(a_{05}e^{-6i\Theta_m})q_m+R_m$, $|R_m|\le\gamma_2q_m^2$, $\gamma_2=212.6$ (of which $2C_7=200$ is the NF-REM tail ceiling $|2\operatorname{Re}(\rho_7/z)|/q\le2C_7q^2$): the isotropic coefficient is the exact $1-|\mu|^2-2\operatorname{Re}a_{32}=-\tfrac{29}{216}$ and the sixth harmonic has zero mean. (ii) *Centred drift.* $\sup_{m\ge0}|q_m^{-1}-\tilde b_m|\le K_\epsilon(a)$, an explicit constant without logarithm: $K_\epsilon=\tfrac{29}{216}\Lambda_{\rm iso}+2|a_{05}|\,\Omega+\gamma_2(2q_0+q_0^2)$ with $\Lambda_{\rm iso}\ge\sum_j|q_j-\tfrac1{b+j}|$ (convergent), $\Omega\ge\sup_m|\sum_{j<m}q_je^{-6i\Theta_j}|$ (Euler–Maclaurin for $\sum_j(b+j)^{-1\mp6i\tau}$, $|\zeta(1\pm6i\tau,x)|\le\tfrac1{6\tau}+\tfrac{1+|s|}{2x}$, plus the convergent amplitude- and phase-deviation sums under the phase model $\Theta_j=\Theta_0+\eta_\infty-\tau\log\tfrac{b+j}b+(\eta_j-\eta_\infty)$, $|\eta_j-\eta_\infty|\le\tau\Lambda_{A_1}(j)+\tfrac\tau{b+j}+c_\theta\Sigma_2(j)$; the constant $\eta_\infty$ factors out); $K_\epsilon=0.7203$, $0.4513$, $0.1860$ at $a=625,1000,2500$ ($98$ % from the $C_7$ term; the v0.3.25 majorant $\bar\epsilon_m$ is $2.2$ at $m=10^5$ and unbounded). (iii) *Centring identity.* $A_1=\sum_{m\ge M}(q_m-\tfrac1{b+m})=\Lambda^{\log}_M(b)+A_1'$ with the explicit $\Lambda^{\log}_M(b)=\sum_{m\ge M}\tfrac{29}{216}H_m(b)/((b+m)\tilde b_m)$ (enclosed over an interval of $b$ in this dependency-free form, two-sided closed-form tail) and $|A_1'|\le K_\epsilon P_2'(M)$, $P_2'$ a closed-form majorant of $\sum_{m\ge M}(q_m^{-1}\tilde b_m)^{-1}$ — no logarithm, no constant floor. Depends on: DYAD-ALG-NF6; DYAD-THM-NF-REM; RECOG-ALG-A1C-TAIL-HARMONICS (the reciprocal law $\gamma_0,\gamma_1$, $c_\theta$, the bracket $q_m^{-1}\ge b'+m-\bar\epsilon_m$ and the corrected closed forms).
`[NUM]` [scope: illustration, not a proof input; RECOG-ART-A1C-DRIFT-CENTERING] Jet model ($\rho_7=0$; 12 orbits, $3\times10^5$ blocks): $\sup_m|q_m^{-1}-\tilde b_m|=0.0066$–$0.0113$ ($\le0.061$ of $K_\epsilon$ — the jet cannot exercise the $C_7$ term); without the centre the drift reaches $0.64$–$0.83$ and exceeds $K_\epsilon$ (NC1); with the wrong sign it exceeds $K_\epsilon$ (NC2); the model's $A_1$ lies in $\Lambda^{\log}\pm K_\epsilon P_2'$ (12/12).
**Not supplied:** a bound on the exact-map drift sharper than $K_\epsilon$ (a Dyadic bound on $\operatorname{Re}(\rho_7/z)$ along an orbit, or the B1-L2 ceiling $C_7\le85.1$, would lower it); any event, carrier or Q1′ statement (SG-R6)."""
ENV_BLOCK = r"""`[ALG]` [RID: RECOG-ALG-A1C-LOGFREE-ENVELOPE] [scope: as RECOG-THM-A1C-SHARPENED-SCHEDULE with the start offset enclosed (RECOG-ALG-A1C-START-OFFSET); $a$ known] """ + D5 + r""" [proof: cell v0.2 §3 (Cor. 24); certificate RECOG-ART-A1C-DRIFT-CENTERING, gates G3c, G5] **Log-free centred envelope.** With $b\in[b^-,b^+]$ from the start-offset iteration: $c^{(5)}_k=c^{(4)}_k-\tau\,{\rm mid}\,\Lambda^{\log}_{M_k}([b^-,b^+])$ and
$$E^{(5)}_k=E^{(4)}_k-\tau\bar A_1-{\rm ref}_d^{\rm old}+\tau\,{\rm half}\,\Lambda^{\log}_{M_k}+\tau K_\epsilon P_2'(M_k)+{\rm ref}_d^{\rm new},$$
${\rm ref}_d^{\rm new}=\tfrac{\sqrt3}8\max(\sqrt{q^+}-n^{-1/2},n^{-1/2}-\sqrt{q^-})$ on the log-free bracket $q_{M}^{-1}\in[\tilde b_M(b^-)-K_\epsilon,\tilde b_M(b^+)+K_\epsilon]$, $n=a+M_k$; $|\varepsilon^{(5)}_k|\le E^{(5)}_k$ by RECOG-ALG-A1C-RECIPROCAL-DRIFT (iii) and the validity of every enclosure. **Every term of $E^{(5)}$ is $\le c(a)/(a+M)$ for all $M\ge1$** by its closed form — $\xi_{\max}$, $c_P(r)Q^\dagger$, ${\rm ref}_\kappa$, $|\varrho_D|$, $c_J^R\Sigma_2$, $c_7^R\Sigma_3$, $\tau\,{\rm half}(\omega S)$, $\tau\,{\rm half}\,\Lambda^{\log}$, $\tau K_\epsilon P_2'$ (no `Lg`, no uniform $\kappa$), and ${\rm ref}_d^{\rm new}=O((\Delta_a+K_\epsilon+\tfrac{29}{216}\log n)/n^{3/2})$ — hence $E^{(5)}(a,M,r)=O_a(1/(a+M))$ for the envelope as defined, with no constant floor. Depends on: RECOG-ALG-A1C-RECIPROCAL-DRIFT; RECOG-THM-A1C-SHARPENED-SCHEDULE (corrected forms) and its centred form $E^{(4)}$; RECOG-ALG-A1C-START-OFFSET; the listed assumption (through $E^{(4)}$ and $\Delta_a$).
`[NUM]` [scope: illustration, not a proof input; RECOG-ART-A1C-DRIFT-CENTERING] Grid ($r=5$, illustrative $b\in[a-1,a+1]$; an observation of the computed range, not the proof of the bound): $E^{(5)}(a+M)=20.6,19.6,19.3,19.2,19.15,19.15,19.15$ at $a=625$ for $M=10^4,\ldots,10^7,10^9,10^{11},10^{13}$ ($18.53$ at $a=2500$) against $E^{(4)}(a+M)=21.9,21.9,23.7,34.9,1153,1.1\times10^5,1.1\times10^7$ (the floor of the v0.3.25 majorant); the limit value is dominated by the in-block residual $c_P(r)Q^\dagger$ ($14.4$ at $r=5$), $|\varrho_D|$ ($2.3$), the start-offset slack ($1.15$) and $\tau K_\epsilon P_2'$ ($0.83$). On the $73$ slips of the 12 sampled orbits ($1.8\times10^6$ steps; the start-offset $b$-ranges): $|\varepsilon^{(5)}_k|\le E^{(5)}_k+L_{\rm tol}$ at $73/73$ (ratio $\le0.79$ with the reference-$L$ tolerance $L_{\rm tol}\approx10^{-4}$); at the latest slips $E^{(5)}\approx10^{-5}<L_{\rm tol}$, so there the test is a consistency check dominated by the tolerance (ratio $10.7$ without it), a limitation shared with the $E^{(4)}$ test; gains $E^{(4)}/E^{(5)}=1.02$–$1.87$ ($73/73>1$), modest at these $M$ because the in-block and start-offset terms dominate.
**Not supplied:** any sharpening of the in-block residual or of the start-offset slack (the dominant terms now); a universal performance statement beyond the term-by-term bound; any event, carrier or Q1′ statement (SG-R6)."""
S8_DRIFT = r"- [RID: RECOG-ART-A1C-DRIFT-CENTERING] `[v0.3.26]` :: `recog_a1c_drift_centering_cert.py` (sha256 `307b310034bf477ef4b49f194d08c4fa42d44b8bbedf7da42e125003a090482e`) + `evidence/recog/a1c_drift/` (`dbc232ba…5974`, `c9e2b2f0…6058`) :: sympy exact identities (the first-order coefficient of $1/q'-1/q-1$; the antiderivatives of the log integrals; $H_m$ as a digamma difference), interval constants ($\gamma_2$; the Euler–Maclaurin bound at $\operatorname{Re}s=1$ against mpmath's Hurwitz zeta; $K_\epsilon$ and its components), the closed-form $\Lambda^{\log}$ against direct summation, `Lg_corr` against brute-force sums (five $M$ including $M<b'$, three $p$, two $a$) and below `Lg`, the asymptotic table to $M=10^{13}$ (floors of the v0.3.25 majorants; corrected limits; $E^{(5)}(a+M)$ bounded and non-increasing from $10^4$), `[NUM]` jet-model orbits and the 12 primitive orbits ($1.8\times10^6$ steps); gates G1–G5, controls NC1–NC2, ALL PASS. Record: `RECOG_A1C_DRIFT_CENTERING_SESSION_v0_1.md` v0.2 (`13bfc30d…5c5f`) :: `[ALG]` proof inputs (certificate), `[COR]` evidence (`Lg_corr`), `[NUM]` illustrations"
R6_NONE = None

# (key, group, location, mode, region, old, new)
EDITS = [
# ---------------- §1 ----------------
("S1-CORR", "CORR", "§1 sharpened-schedule sentence: corrected closed forms", "str", "live", S1_COR_OLD, S1_COR_NEW),
("S1-DRIFT", "DRIFT", "§1: reciprocal drift sentence", "str", "live",
 r"the two tails combine exactly into one boundary term (RECOG-ALG-A1C-COMBINED-TAIL, §6.13b).",
 r"the two tails combine exactly into one boundary term (RECOG-ALG-A1C-COMBINED-TAIL, §6.13b). `[ALG]` (v0.3.26) The chart reciprocal drift is centred exactly: $q_m^{-1}=b+m-\tfrac{29}{216}[\psi(b+m)-\psi(b)]+O(1)$ with an explicit log-free constant $K_\epsilon(a)$ (RECOG-ALG-A1C-RECIPROCAL-DRIFT, §6.13b)."),
("S1-ENV", "ENV", "§1: log-free envelope sentence", "str", "live",
 r"with an explicit log-free constant $K_\epsilon(a)$ (RECOG-ALG-A1C-RECIPROCAL-DRIFT, §6.13b).",
 r"with an explicit log-free constant $K_\epsilon(a)$ (RECOG-ALG-A1C-RECIPROCAL-DRIFT, §6.13b); the centred envelope $E^{(5)}$ is $O_a(1/(a+M_k))$ term by term, with no constant floor (RECOG-ALG-A1C-LOGFREE-ENVELOPE `[assuming: (D5)]`, §6.13b)."),
# ---------------- §6.13b corrections (in place, RIDs kept) ----------------
("S613b-COR-TAIL-I", "CORR", "§6.13b RECOG-ALG-A1C-TAIL-HARMONICS (i): [COR] note, corrected closed forms", "str", "live", COR_TAIL_I_OLD, COR_TAIL_I_NEW),
("S613b-COR-TAIL-III", "CORR", "§6.13b RECOG-ALG-A1C-TAIL-HARMONICS (iii): corrected closed forms", "str", "live", COR_TAIL_III_OLD, COR_TAIL_III_NEW),
("S613b-COR-SCHED", "CORR", "§6.13b RECOG-THM-A1C-SHARPENED-SCHEDULE: [COR] order sentence", "str", "live", COR_SCHED_OLD, COR_SCHED_NEW),
("S613b-COR-NUM", "CORR", "§6.13b [NUM] grid sentence: corrected values", "str", "live", COR_NUM_OLD, COR_NUM_NEW),
# ---------------- §6.13b new blocks ----------------
("S613b-DRIFT", "DRIFT", "§6.13b: reciprocal-drift block before §6.14", "str", "live",
 "\n\n### §6.14 The $h$-Chart Ledger", "\n\n" + DRIFT_BLOCK + "\n\n### §6.14 The $h$-Chart Ledger"),
("S613b-ENV", "ENV", "§6.13b: log-free envelope block before §6.14", "str", "live",
 "\n\n### §6.14 The $h$-Chart Ledger", "\n\n" + ENV_BLOCK + "\n\n### §6.14 The $h$-Chart Ledger"),
# ---------------- §7 ----------------
("S7-NF6-DRIFT", "DRIFT", "§7 DYAD-ALG-NF6 row: drift use", "line", "live", "- [RID: DYAD-ALG-NF6]",
 "{LINE}; §6.13b RECOG-ALG-A1C-RECIPROCAL-DRIFT (v0.3.26): the exact isotropic coefficient $1-|\\mu|^2-2\\operatorname{Re}a_{32}=-\\tfrac{29}{216}$ and the sixth harmonic $a_{05}$ of the reciprocal law"),
("S7-NFREM-DRIFT", "DRIFT", "§7 DYAD-THM-NF-REM row: drift use", "line", "live", "- [RID: DYAD-THM-NF-REM]",
 "{LINE}; §6.13b RECOG-ALG-A1C-RECIPROCAL-DRIFT (v0.3.26): $C_7$ in $\\gamma_2$ (the dominant part of $K_\\epsilon$) and the one-orbit contraction in $\\sum_jq_j^2$"),
# ---------------- §8 ----------------
("S8-DRIFT", "DRIFT", "§8 artifact row RECOG-ART-A1C-DRIFT-CENTERING", "line", "live", "- [RID: RECOG-ART-A1C-Q1PRIME-FIBER]", "{LINE}\n" + S8_DRIFT),
("S8-CORR", "CORR", "§8 artifact row RECOG-ART-A1C-CORRECTED-GRID", "line", "live", "- [RID: RECOG-ART-A1C-Q1PRIME-FIBER]", "{LINE}\n" + S8_CORR),
# ---------------- Appendix B ----------------
("B-CORR", "CORR", "Appendix B: two RETRACTED entries (order sentences of the v0.3.25 majorants)", "str", "live", APPB_OLD, APPB_NEW),
]

APPA_LINES = {
 "CORR": r"- **Scientific correction (separately accepted; Appendix B):** the asymptotic-order sentences of RECOG-ALG-A1C-TAIL-HARMONICS (i), (iii) and RECOG-THM-A1C-SHARPENED-SCHEDULE were false for the closed-form majorants as defined in v0.3.25 — CORR-1: the $M$-independent slack $b'^{-p}$ of the log-majorant `Lg` gave $\bar A_1$, $\bar S'$, $\bar R'$, $E'$, $E'''$ constant floors; CORR-2: the uniform slack $\kappa$ in the reference term gave an order-$(a+M)^{-1/2}$ piece. The statements are corrected in place with `[COR]` (RIDs kept) for the corrected closed forms (`Lg_corr`; the $M$-dependent bracket), under which the limits and orders hold; the inequalities, grades and RIDs are unchanged; the corrected majorants are below the v0.3.25 ones at every grid point (RECOG-ART-A1C-CORRECTED-GRID, §8); the `[NUM]` grid values at $M=10^6,10^7$ updated. Appendix B: RECOG-ALG-A1C-TAIL-HARMONICS-LIMITS-V0325, RECOG-THM-A1C-SHARPENED-SCHEDULE-ORDER-V0325. Found by the drift-centering cell (PR #93) while checking the order of the remaining terms.",
 "DRIFT": r"- **New science, group DRIFT (separately reviewed):** RECOG-ALG-A1C-RECIPROCAL-DRIFT (§6.13b) — exact first order of the chart reciprocal law ($-\tfrac{29}{216}$ isotropic, zero-mean sixth harmonic, remainder $\gamma_2q^2$ with $\gamma_2=212.6$ dominated by $C_7$); the log-free drift constant $K_\epsilon(a)$ ($0.72$–$0.19$) bounding $|q_m^{-1}-\tilde b_m|$ for all $m$; the exact centring identity $A_1=\Lambda^{\log}_M(b)+A_1'$; adopted rows only, no (D5); RECOG-ART-A1C-DRIFT-CENTERING (§8); §7 NF6 and NF-REM rows record the uses.",
 "ENV": r"- **New science, group ENV (separately reviewed; requires DRIFT):** RECOG-ALG-A1C-LOGFREE-ENVELOPE `[assuming: (D5)]` (§6.13b) — the centred envelope $E^{(5)}$ with every term $O_a(1/(a+M))$ by its closed form, no constant floor ($E^{(5)}(a+M)\to19.15$ at $a=625$ on the grid to $10^{13}$, an observation; the bound is term by term); `[NUM]` 73-slip containment with the tolerance caveat; gains $1.02$–$1.87$ at the sampled slips.",
}
APPA_TAIL = (r"- **Unchanged:** every existing RID's statement and grade (the two `[COR]` sentences correct order claims for stated majorants; the inequalities stand); every OPEN status word (R1, R3 PARTIAL; R4, R5, R6 ACTIVE; R2, R7–R11 CLOSED)." "\n"
             r"- **Records:** release record `records/recog/RECOG_v0_3_26_RELEASE_RECORD.md` (candidate); predecessor tag `recog-v0.3.25` (SHA-256 `86cae8ff…d7db`)." "\n\n")

NEW_RIDS = {
 "CORR": {"RECOG-ART-A1C-CORRECTED-GRID", "RECOG-ALG-A1C-TAIL-HARMONICS-LIMITS-V0325", "RECOG-THM-A1C-SHARPENED-SCHEDULE-ORDER-V0325"},
 "DRIFT": {"RECOG-ALG-A1C-RECIPROCAL-DRIFT", "RECOG-ART-A1C-DRIFT-CENTERING"},
 "ENV": {"RECOG-ALG-A1C-LOGFREE-ENVELOPE"},
}
GROUPS = ["CORR", "DRIFT", "ENV"]

def appa_edit(groups):
    head = "## Appendix A — Version History\n\nOne compact entry per edition (Methodology v1.4 §1). Full records of earlier editions — adoption metadata, draft-round records, review verdicts, the stacked status summaries and the freeze history — are in Appendix A and the header of v0.3.22 (tag `recog-v0.3.22`, SHA-256 `0dcce9e4…bcd9`). Scientific corrections and retired claims: Appendix B.\n\n"
    old = head + "### v0.3.25 — 27 October 2026 — Adopted"
    new = head + "### v0.3.26 — DRAFT, stage 1 (corrected intermediate; not adopted)\n"
    new += r"- **Basis:** PI decision of 28 Oct 2026 (option (b) for the correction finding of the drift-centering cell, PR #93, reviews #5674661826: `PREPARE RECOG ASYMPTOTIC CORRECTION + DRIFT-CENTERING SUCCESSOR` — one maintenance round; no long orbit rerun; the Appendix B rationale, the corrected closed forms, the corrected order sentences, and Lemma 21–22, Prop. 23 and the conditional Cor. 24 as separate acceptances). Each group below carries its own acceptance decision." + "\n"
    for g in GROUPS:
        if g in groups: new += APPA_LINES[g] + "\n"
    new += APPA_TAIL + "### v0.3.25 — 27 October 2026 — Adopted"
    return ("A-1", "ALL", "Appendix A: v0.3.26 draft entry (per variant)", "str", "appA", old, new)

def resolve(txt, mode, old, new):
    if mode == "line":
        lines = txt.split("\n")
        hits = [l for l in lines if l.startswith(old)]
        assert len(hits) == 1, f"expected 1 line starting with prefix {old!r}, found {len(hits)}"
        return hits[0], new.replace("{LINE}", hits[0])
    return old, new

def apply(s, edits):
    i = s.index(APPA_START); j = s.index(APPA_END)
    live = s[:i] + "\x00APPA\x00" + s[j:]
    appa = s[i:j]
    record = []
    for k, grp, loc, mode, region, old, new in edits:
        txt = live if region == "live" else appa
        old_full, new_full = resolve(txt, mode, old, new)
        n = txt.count(old_full)
        assert n == 1, f"{k}: expected 1 match, found {n}"
        assert old_full != new_full, f"{k}: no-op edit"
        txt = txt.replace(old_full, new_full)
        if region == "live": live = txt
        else: appa = txt
        record.append({"key": k, "group": grp, "location": loc, "mode": mode, "region": region,
                       "old_sha256": hashlib.sha256(old_full.encode()).hexdigest(),
                       "new_sha256": hashlib.sha256(new_full.encode()).hexdigest(),
                       "old": old_full, "new": new_full})
    assert live.count("\x00APPA\x00") == 1
    return live.replace("\x00APPA\x00", appa), record

def main(argv):
    base, out, log = argv[1:4]
    groups = set(GROUPS)
    if "--only" in argv:
        groups = set(argv[argv.index("--only") + 1].split(","))
        assert groups <= set(GROUPS), groups
    assert not ("ENV" in groups and "DRIFT" not in groups), "ENV depends on DRIFT (K_eps, Lambda^log); build them together"
    raw = open(base, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == BASE_SHA, "base is not adopted v0.3.25 (tag recog-v0.3.25)"
    s = raw.decode("utf-8")
    keys = [e[0] for e in EDITS]
    assert len(keys) == len(set(keys)), "duplicate edit keys"
    edits = [e for e in EDITS if e[1] in groups]
    edits.append(appa_edit(groups))
    t, record = apply(s, edits)
    data = t.encode("utf-8")
    open(out, "wb").write(data)
    new_rids = sorted(set().union(*(NEW_RIDS[g] for g in groups)))
    json.dump({"base_sha256": BASE_SHA, "base_tag": PREV_TAG, "groups": sorted(groups),
               "intermediate_sha256": hashlib.sha256(data).hexdigest(),
               "declared_new_recog_rids": new_rids, "edit_count": len(record), "edits": record},
              open(log, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(hashlib.sha256(data).hexdigest(), len(record), "edits", "groups:", ",".join(sorted(groups)))

if __name__ == "__main__":
    main(sys.argv)
