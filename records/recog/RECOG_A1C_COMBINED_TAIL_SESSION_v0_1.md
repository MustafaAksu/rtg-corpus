# RECOG A1c — the combined tail $\tau S^{\rm tail}_M-R^{\rm tail}_M$: an exact telescoping identity, the leading harmonics collapse to one boundary term, and the known-$a$ envelope loses its $M^{-1/2}$ order: session record

**Date:** 26 October 2026 · **Author:** RECOG co-owner (Claude) · **Status:** `[SESSION]` scientific record, v0.1. PI decision of 25 Oct 2026 (with reviews #5645113197, #5645113367, #5645118795): a *bounded analytic feasibility cell* for the combined tail — combine the leading harmonics of $\tau S^{\rm tail}$ and $R^{\rm tail}$ and decide whether there is a definite gain against the separate-bound constant $1.9396$; if none, close negatively; no new heavy Dyadic certification. No DSN is edited; nothing is adopted.
**Governing edition:** `recog-v0.3.24` (`8c64bea2…e7c1`): RECOG-THM-A1B-SLIP-SCHEDULE-U and its proof cell (exact event identity; the finite-block identity $D_M=C_D^{\rm ext}+\tau\psi(a+M)-\tau S^{\rm tail}_M+R^{\rm tail}_M$). Dyadic `dyad-v6.4.22` §6.14: DYAD-THM-LPHASE-ROWA-REMAINDER (branch (B) and the decomposition of $r$), DYAD-THM-OPEN3-SPIRAL-REM (row-A static constant $c_1=0.261$: $|D_\Theta-D_{\Theta,1}|\le c_1q$), DYAD-ALG-OPEN3-LEADING ($D_{\Theta,1}=\operatorname{Im}(h_2/z)$, $L_\Theta$), DYAD-THM-NF-REM, DYAD-ALG-NF6, $h_2$. Parts 1b/2 and the in-block cell (PRs #54, #59, #63) for $A_0,A_1$, the amplitude brackets, $\kappa(r)$ and the enclosure algorithm. Branch `claude/recog-a1c-combined-tail` stacked on `claude/recog-a1c-inblock`.
**Certificate:** `evidence/recog/scripts/recog_a1c_combined_tail_cert.py` — imports the in-block, part-2 and part-1b scripts unchanged (hashes in the JSON); exact identities (sympy), constants in interval arithmetic, `[NUM]` 12 orbits ($1.8\times10^6$ steps), part-2 enclosures recomputed; gates G1–G5 (+G4b), controls NC1–NC2 ALL PASS; outputs `evidence/recog/a1c_comb/a1c_combined_tail_cert.json`, `_output.txt`.

## 0. Summary

1. **Exact identity (Prop. 13).** The two tails are not independent: with the Dyadic decomposition of the block remainder, $r_m=S_\Theta(z_m)+\tau D_Q(z_m)+[\operatorname{Arg}(J/z_m)+\tau q_m]+\operatorname{Arg}(\widehat F/J)(z_m)$, and $Q_m=q_m+D_Q(z_m)$, the bridge terms $\tau D_Q$ **cancel exactly** in $\tau(Q_m-\tfrac1{a+m})-r_m$, and the angular increments $S_\Theta(z_m)=D_\Theta(z_{m+1})-D_\Theta(z_m)$ **telescope**:
$$\tau S^{\rm tail}_M-R^{\rm tail}_M=\tau A_M+D_\Theta(z_M)-\Sigma^J_M-\Sigma^7_M,\qquad A_M=\sum_{m\ge M}\Bigl(q_m-\frac1{a+m}\Bigr),\ \ |\Sigma^J_M|\le c_J^R\sum_{m\ge M}q_m^2,\ \ |\Sigma^7_M|\le c_7^R\sum_{m\ge M}q_m^3 .$$
Of the four pieces only $D_\Theta(z_M)=\sqrt{q_M}\,d(\Theta_M)+O(q_M)$ is of order $M^{-1/2}$, and it is a single boundary term, not a sum.
2. **Leading harmonics (the feasibility question).** Separately, $\tau S$ and $R$ carry the harmonics $\tau\phi_k$ and $\lambda_k$ with leading constant $\tau\cdot0.7485+1.0753=1.9396$. Combined, $\lambda_k-\tau\phi_k=\ell_k$ are the harmonics of $L_\Theta$ ($\Lambda_3=L_\Theta+\tau D_3$), and $|\ell_1|/|\tfrac12+i\tau|+|\ell_3|/|\tfrac12+3i\tau|=\tfrac1{\sqrt{12}}+\tfrac1{12}=0.3720$ — a factor $5.21$ — and these two numbers are exactly the harmonic amplitudes of $d(\Theta)=D_{\Theta,1}/r$, because $L_\Theta=DD_{\Theta,1}[\mu qz]$ is the spiral derivative of $D_{\Theta,1}$ (exact, G1): the phase correlation the separate bounds miss is complete — the oscillatory tails sum to the boundary value $D_\Theta(z_M)$. **Definite gain: yes.**
3. **Known phase and the $r$-independence (Cor. 14).** At a slip block the base point's primitive angle is $-r\tfrac\pi3+O(\sqrt Q)$ (in-block cell), and $d(-r\tfrac\pi3)=-\tfrac{\sqrt3}8$ for $r\in\{0,1,2\}$, $+\tfrac{\sqrt3}8$ for $r\in\{3,4,5\}$. Together with the in-block centre $\kappa(r)=(0,0,0,\tfrac{\sqrt3}4,\tfrac{\sqrt3}4,\tfrac{\sqrt3}4)$: $\kappa(r)-d(-r\tfrac\pi3)=\tfrac{\sqrt3}8$ **for every $r$** — the $r$-dependence of the in-block cell was an artefact of the block boundary. Sharpened schedule, known $a$:
$$\tau\psi(a+M_k)-(k-1)\tfrac\pi3+\tfrac{\sqrt3}8(a+M_k)^{-1/2}+\tfrac\tau2(a+M_k)^{-1}=L+\varepsilon'''_k,\qquad|\varepsilon'''_k|\le E'''(a,M_k,r_k)=O\bigl((a+M_k)^{-1}\bigr).$$
4. **Values.** $E'''(a+M)\to$ about $45$ ($a=625$), $52$ ($1000$), $69$ ($2500$) on the grid; the dominant term is the unknown start offset $\tau A_0\le\tau\Delta_a/(a+M)=0.98\sqrt a/(a+M)$ ($50$–$70$ % of $E'''$), then the in-block $O(Q)$ residual ($\approx14/(a+M)$ at $r=5$). Against the in-block cell's $E''$: $E'''=0.029$ at $(625,10^3)$ ($E''$ $0.078$, part 1 $2.92$), $0.0043$ at $10^4$ ($0.023$), $4.5\times10^{-4}$ at $10^5$ ($0.0066$), $4.7\times10^{-5}$ at $10^6$, $5.8\times10^{-6}$ at $10^7$ ($6.2\times10^{-4}$): factors $2.7\to106$ on the tested grid; $E'''\sqrt{a+M}\to0$.
5. **Effect on part 2.** Enclosures of the 12 sample records with $(c''',E''')$: $a$-widths $6$–$44$ at $a=625$ (in-block cell: $64$–$113$; part 2: $173$–$245$), $60$–$81$ at $1000$ ($194$–$255$; $461$–$589$), $92$–$114$ at $2500$ ($309$–$401$; $726$–$965$); $L$-hulls $0.0004$–$0.0015$ wide (in-block cell: $0.008$–$0.013$; part 2: $0.022$–$0.035$); true $a$, $L$ inside 12/12. The $a$-window is now set by $2\Delta_a\approx1.7\sqrt a$ (the start-offset slack) plus the in-block residual at the first slip — i.e. by the unknown start angle, not by the tails; the $L$-window is $\approx2E'''$ at the last slip, $\approx90/(a+M_K)$.
6. **`[NUM]`.** At all $73$ slips: $|\varepsilon'''_k|\le E'''$ with ratio $\le0.85$ against the identity-corrected end estimate of $L$ (G4) and ratio $\le0.71$ including the tolerance against the naive end estimate (G4b, independent of the identity); the negative control (sign of the $D_\Theta$ centre flipped) reaches ratio $6.6$; the measured combined tail at slip blocks agrees with $d(-r\tfrac\pi3)(a+M)^{-1/2}$ within the $\tau A_0$ range in 56/73 cases, the exceptions being late slips ($M\ge1.1\times10^4$) where the truncation of the measured tail at $N$ ($|D_\Theta(z_N)|\lesssim4\times10^{-4}$) is of the same size as the quantities compared.
7. **Typing.** Prop. 13 uses the Dyadic decomposition of $r$ (an exact identity under branch (B), with $D_\Theta:=\operatorname{Arg}(h(z)/z)$) and the adopted $c_1$ (theorem row); the constants $c_J^R$, $c_7^R$ are RECOG-derived from the explicit jet and $C_7$; the (D5) bridge constants now enter **only** through the start offset $\Delta_a$ and the amplitude brackets ($c_Q,c'_Q$); the term $C=c'_Q\sum q^2$ of part 1b is gone. Grade target `[ALG]` for Prop. 13 / Cor. 14; $E'''$ `[assuming: (D5)]` as before.

## 1. Proposition 13 (exact identity) and the harmonic collapse

Chart notation as in parts 1b/3. Under branch (B) the six-step lifted increment is $2\pi+\operatorname{Arg}(F_W(W_m)/W_m)$, and with $W=h(z)$, $D_\Theta(z):=\operatorname{Arg}(h(z)/z)$ (small on the row), $\operatorname{Arg}(h(\widehat Fz)/h(z))=\operatorname{Arg}(\widehat Fz/z)+D_\Theta(\widehat Fz)-D_\Theta(z)$ and $\operatorname{Arg}(\widehat Fz/z)=\operatorname{Arg}(J/z)+\operatorname{Arg}(\widehat F/J)$ (all increments small). Hence $r_m:=\hat\varphi_{6(m+1)}-\hat\varphi_{6m}-2\pi+\tau Q_m=S_\Theta(z_m)+[\operatorname{Arg}(J/z_m)+\tau q_m]+\operatorname{Arg}(\widehat F/J)(z_m)+\tau D_Q(z_m)$ (Dyadic's decomposition, re-derived). Therefore
$$\tau\Bigl(Q_m-\frac1{a+m}\Bigr)-r_m=\tau\Bigl(q_m-\frac1{a+m}\Bigr)-S_\Theta(z_m)-[\operatorname{Arg}(J/z_m)+\tau q_m]-\operatorname{Arg}(\widehat F/J)(z_m),$$
and summing over $m\ge M$, with $\sum_{m\ge M}S_\Theta(z_m)=\lim_ND_\Theta(z_N)-D_\Theta(z_M)=-D_\Theta(z_M)$ ($D_\Theta(z)\to0$ as $z\to0$, all series absolutely convergent), gives Prop. 13. $\square$
*Harmonics.* $D_{\Theta,1}=\operatorname{Im}(h_2/z)=r\,d(\Theta)$, $d(\Theta)=-\tfrac{\sqrt3}{12}\cos\Theta+\tfrac14\sin\Theta-\tfrac{\sqrt3}{24}\cos3\Theta-\tfrac1{24}\sin3\Theta$ (re-derived from $h_2$, G1), amplitudes $\tfrac1{\sqrt{12}}$ and $\tfrac1{12}$; $L_\Theta=DD_{\Theta,1}[\mu qz]$ has harmonics $\ell_1=-\tfrac{\sqrt3}8+\tfrac{7i}{24}$, $\ell_3=\tfrac{5\sqrt3}{48}+\tfrac{11i}{48}$ with $|\ell_1|/|s_1-1|=\tfrac1{\sqrt{12}}$, $|\ell_3|/|s_3-1|=\tfrac1{12}$ exactly (G1); and $\ell_k=\lambda_k-\tau\phi_k$ (G1). So the harmonic-sum route of part 1b, applied to the combined tail, gives the constant $0.3720$ — and Prop. 13 shows why: the sum is the boundary term.
*Constants.* $|\operatorname{Arg}(J/z)+\tau q|\le c_J^Rq^2$ with $c_J^R=0.5008$ at $q^*$ (from $J/z=1+\mu q+a_{32}q^2+a_{05}\bar z^6/q$: $\operatorname{Im}a_{32}-\tfrac12\operatorname{Im}\mu^2=\operatorname{Im}a_{32}-\tfrac\tau2=0.4757$, plus the sixth harmonic $|a_{05}|$ and the cubic remainder; consistent with Dyadic's $c_J=0.5022$); $|\operatorname{Arg}(\widehat F/J)|\le c_7^Rq^3$, $c_7^R=100.23$ ($C_7=100$); $\sum_{m\ge M}q_m^p\le(1-\kappa)^{-p}P_p(b',M)$ (part 1b).

## 2. Corollary 14 (known phase; the sharpened schedule and $E'''$)

At a slip block $M$ with residue $r$ the base point's primitive angle is $\theta_{W,M}=-r\tfrac\pi3+e$, $|e|\le\bar\Delta+r\bar\alpha$ (in-block cell, Prop. 10), and the chart angle is $\Theta_M=\theta_{W,M}-D_\Theta(z_M)$ with $|D_\Theta(z_M)|\le D^+:=\sup|d|\sqrt{q^+_M}+c_1q^+_M$ ($\sup|d|=0.2955$). Hence $D_\Theta(z_M)=d(-r\tfrac\pi3)\sqrt{q_M}+\varrho_D$, $|\varrho_D|\le\sqrt{q^+_M}\,\|d'\|_\infty(\bar\Delta+r\bar\alpha+D^+)+c_1q^+_M$ ($\|d'\|_\infty=0.5348$), with $q_M\in[q^-_M,q^+_M]$, $q^-_M=(a+\Delta_a+M+\bar\epsilon_M)^{-1}$, $q^+_M=((1-\kappa)(b'+M))^{-1}$ (part 1b Lemmas 1–2). From the exact event identity $\tau\psi(a+M_k)-(k-1)\tfrac\pi3=L-o_{j_k}-P_{r_k}+\tau S^{\rm tail}-R^{\rm tail}$, Prop. 10 ($P_r=\kappa(r)\sqrt{Q_\star}+\varrho_P$) and Prop. 13:
$$\tau\psi(a+M_k)-(k-1)\tfrac\pi3+\tfrac\tau2 n^{-1}+\bigl[\kappa(r)-d(-r\tfrac\pi3)\bigr]n^{-1/2}=L+\varepsilon'''_k,\qquad n=a+M_k,\qquad\kappa(r)-d(-r\tfrac\pi3)=\tfrac{\sqrt3}8\ \forall r,$$
$$|\varepsilon'''_k|\le E''':=\xi_{\max}+c_P(r)Q^\dagger+\kappa(r)\,{\rm ref}_\kappa+\tau(A_0+A_1)+|\varrho_D|_{\max}+\tfrac{\sqrt3}8\,{\rm ref}_d+c_J^R\Sigma_2+c_7^R\Sigma_3,$$
with $\xi_{\max},c_P,{\rm ref}_\kappa,Q^\dagger$ from the in-block cell, $A_0,A_1,\Sigma_p$ from part 1b, and ${\rm ref}_d=\max(\sqrt{q^+_M}-n^{-1/2},\ n^{-1/2}-\sqrt{q^-_M})$. Every term is $O(n^{-1})$ ($A_1$: $O(\log n/n)$). $\square$

## 3. Values (tested grid; $r=5$, the worst residue)

| $a$ | $M$ | $E'''$ | $E''$ (in-block cell) | gain | $E'''\cdot(a+M)$ | of which $\tau A_0$ / in-block / $\varrho_D$ |
|---|---|---|---|---|---|---|
| 625 | $10^3$ | $0.0293$ | $0.0779$ | $2.7$ | $47.5$ | $0.015$ / $0.011$ / $0.0016$ |
| 625 | $10^4$ | $0.00425$ | $0.0231$ | $5.4$ | $45.2$ | $0.0023$ / $0.0015$ / $0.00023$ |
| 625 | $10^5$ | $4.49\times10^{-4}$ | $0.00656$ | $14.6$ | $45.2$ | $2.4\times10^{-4}$ / $1.5\times10^{-4}$ / $2.3\times10^{-5}$ |
| 625 | $10^6$ | $4.69\times10^{-5}$ | $0.00199$ | $42$ | $46.9$ | |
| 625 | $10^7$ | $5.82\times10^{-6}$ | $6.19\times10^{-4}$ | $106$ | $58.2$ | ($A_1$'s $\log$ grows) |
| 1000 | $10^3$–$10^7$ | $0.0266\to5.7\times10^{-6}$ | | $2.6\to109$ | $51$–$57$ | |
| 2500 | $10^3$–$10^7$ | $0.0200\to7.0\times10^{-6}$ | | $2.6\to88$ | $68$–$70$ | |

$E'''<E''$ at every grid point and at every sampled slip (G3, G4); no universal claim. The $M^{-1/2}$ order is gone from the envelope; what remains is $\approx(\tau\Delta_a+c_{\rm ib}(r)+\ldots)/(a+M)$ with $\tau\Delta_a=0.98\sqrt a$: the unknown start offset $a-b=-D_Q(z_0)/(q_0Q_0)$, i.e. the start angle $\Theta_0$.

## 4. Effect on part 2 (recomputed) and `[NUM]`

| $a$ | $\theta_0$ | $K$ | $a$-enclosure with $(c''',E''')$ (width) | in-block cell | part 2 | $L$-hull (width) |
|---|---|---|---|---|---|---|
| 625 | 0.3 | 7 | $[625,630.7]$ ($5.7$) | $64$ | $173$ | $0.0004$ |
| 625 | 1.7 | 7 | $[625,664.6]$ ($40$) | $113$ | $235$ | $0.0006$ |
| 625 | 3.9 | 7 | $[625,668.9]$ ($44$) | $109$ | $245$ | $0.0005$ |
| 625 | 5.1 | 6 | $[625,636.5]$ ($11$) | $89$ | $229$ | $0.0006$ |
| 1000 | 0.3 | 7 | $[946.1,1006.2]$ ($60$) | $194$ | $461$ | $0.0005$ |
| 1000 | 1.7 | 6 | $[985.5,1049.4]$ ($64$) | $255$ | $545$ | $0.0010$ |
| 1000 | 3.9 | 6 | $[978.6,1059.4]$ ($81$) | $250$ | $568$ | $0.0009$ |
| 1000 | 5.1 | 6 | $[943.3,1011.7]$ ($68$) | $246$ | $589$ | $0.0008$ |
| 2500 | 0.3 | 6 | $[2415.9,2507.5]$ ($92$) | $309$ | $726$ | $0.0008$ |
| 2500 | 1.7 | 5 | $[2476.1,2580.6]$ ($105$) | $396$ | $885$ | $0.0015$ |
| 2500 | 3.9 | 5 | $[2472.1,2585.8]$ ($114$) | $396$ | $923$ | $0.0013$ |
| 2500 | 5.1 | 5 | $[2414.0,2516.0]$ ($102$) | $401$ | $965$ | $0.0011$ |

Inner enclosures single intervals, undecided length $0.5$–$1.5$; true $a$ inside 12/12. The residual $a$-width is governed by $2\Delta_a$ (the start-offset slack, $\approx42$ at $a=625$, $85$ at $2500$) plus the in-block residual at the first slip; the $L$-hull is $\approx2E'''(a,M_K)$, i.e. $\approx90/(a+M_K)$ — the phase readout from a record of $K$ slips is now certified to $10^{-3}$ rad and better.

`[NUM]` (73 slips): $|\varepsilon'''_k|/E'''\le0.85$ against the identity-corrected end estimate of $L$ (tolerance $\tau\Delta_a/(a+N)+3/(a+N)\approx10^{-4}$), and ratio $\le0.71$ including the tolerance against the naive end estimate (G4b; its tolerance adds $|D_\Theta(z_N)|$, $\tau|\log(Q_N/q_N)|$ and $\tau|\log(q_N(a+N))|$, all $O(N^{-1/2})$); negative control (sign of the $D_\Theta$ centre flipped): ratio up to $6.6$. The residual $\varepsilon'''_k$ along an orbit has a fixed sign and decays like $1/(a+M_k)$ — the fingerprint of the start-offset term $\tau(a-b)/(a+M)$ — e.g. $a=625$, $\theta_0=0.3$: $+2.8\times10^{-2},+1.1\times10^{-2},+4.3\times10^{-3},+1.7\times10^{-3},+6.5\times10^{-4},+2.3\times10^{-4},+5.0\times10^{-5}$ at $M=178,\ldots,181391$ (bounds $0.035,0.015,0.0067,0.0032,0.0014,6.1\times10^{-4},1.6\times10^{-4}$).

## 5. Consequences and next steps

- **Answer to the feasibility question:** definite gain — the combined leading constant is $0.372$ instead of $1.940$, and in fact the oscillatory tails collapse to one boundary term whose phase is known at the slip, so the $M^{-1/2}$ order leaves the error entirely. No Dyadic certification campaign is needed: the identity uses Dyadic's published decomposition of $r$ and the adopted $c_1$.
- **The next (and last RECOG-side) lever is the start offset** $a-b$: $D_Q(z_0)=q_0^{3/2}\Phi(\Theta_0)+O(q_0^2)$ and the first anchor $n_0$ pins the start angle to $\theta_0=-n_0\tfrac\pi3+O(\sqrt{Q_0})$ (same mechanism as the in-block cell), so $a-b$ can be centred to $O(1)$, turning $\tau A_0$ from $0.98\sqrt a/(a+M)$ into $O(1/(a+M))$ with an $O(1)$ constant; the known-$a$ envelope would then be $\approx c/(a+M)$ with $c\approx20$, and the unknown-$a$ windows would shrink below $\Delta_a$. A small follow-up cell; the (D5) dependency ($c'_Q$) remains through $D_Q-D_3$.
- **DSN candidate (later release):** the sharpened schedule of Cor. 14 as an additive row of THM (S) (centre $+\tfrac{\sqrt3}8(a+M)^{-1/2}+\tfrac\tau2(a+M)^{-1}$, error $O((a+M)^{-1})$) and $E'''$ for the RESULT's envelope clause. Not adopted.
- **Part 3 (Q1′):** unchanged in substance; the `[SESSION/HEUR]` margin picture now has a much smaller certified window around it.

## 6. Not claimed

No universal $E'''<E''$; no change to adopted statements; the orders in part 3 §2.4 are not upgraded by this cell; the `[NUM]` $L$ estimate used in G4 relies on the same identity (G4b with the naive estimate is the independent check, at its coarser tolerance); constants are majorants.

## 7. Certificate

G1 exact (sympy): $d=\operatorname{Im}(h_2/z)/r$ equals the published $D_{\Theta,1}/r$; the six values $d(-s\tfrac\pi3)$; $\kappa(r)-d(-r\tfrac\pi3)=\tfrac{\sqrt3}8$ for all $r$; $\ell_k=\lambda_k-\tau\phi_k$ equals the published $L_\Theta$ harmonics; $|\ell_1|/|s_1-1|=\tfrac1{\sqrt{12}}$, $|\ell_3|/|s_3-1|=\tfrac1{12}$ and the equality with $d$'s amplitudes. G2 interval constants ($\sup|d|$, $\sup|d'|$, $c_J^R$, $c_7^R$) and the two leading constants ($0.3720$ vs $1.9396$). G3 $E'''<E''$ on the tested grid. G4/G4b the `[NUM]` slip test with both $L$ estimates. G5 the recomputed enclosures narrower than the in-block cell's on every record, true $a$ inside. NC1 flipped $D_\Theta$ sign fails G4; NC2 the separate constant is not the combined one ($1.94>5\times0.372$). Directed rounding and the rigorous $\arcsin$ enclosure as in the in-block cell v0.2.
