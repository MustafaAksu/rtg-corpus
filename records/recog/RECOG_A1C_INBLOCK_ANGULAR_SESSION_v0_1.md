# RECOG A1c — in-block angular envelope sharpening: the partial-block angular sum is a known multiple of $\sqrt Q$ plus $O(Q)$; sharpened schedule and envelope $E''$: session record

**Date:** 25–26 October 2026 · **Author:** RECOG co-owner (Claude) · **Status:** `[SESSION]` scientific record, v0.1. PI decision of 25 Oct 2026: `START A1C IN-BLOCK ANGULAR ENVELOPE SHARPENING — APPROVED` — certify the five-step angular sum with the real step dependencies and sign correlations, keeping the adopted A1b domain and the primitive representation; success criterion: a strictly smaller upper bound, then its effect on the known-$a$ envelope and on part 2's parameter intervals. No DSN is edited; nothing is adopted.
**Governing edition:** `recog-v0.3.24` (`8c64bea2…e7c1`): RECOG-THM-A1B-SLIP-SCHEDULE-U (§6.13b), its proof cell `RECOG_A1B_A1C_SESSION_v0_1.md` §2 (exact event identity, partial block, one-step pointwise bound), RECOG-THM-A1A-LIFT-ALIGNMENT, DYAD-THM-PRIM-CTR ($U_T\subset\{Q<2209\times10^{-6}\}$). Parts 1b/2 (PRs #54, #59) for $\bar S',\bar R'$, the block-amplitude bracket and the enclosure algorithm. Branch `claude/recog-a1c-inblock` stacked on `claude/recog-a1c-part3`.
**Certificate:** `evidence/recog/scripts/recog_a1c_inblock_angular_cert.py` — imports the part-1b and part-2 scripts unchanged (hashes in the JSON); exact identities (sympy), constants in interval arithmetic (mpmath `iv`), `[NUM]` 12 orbits ($1.8\times10^6$ steps) and the part-2 enclosures recomputed; gates G1–G5, controls NC1–NC2 ALL PASS; outputs `evidence/recog/a1c_inblock/a1c_inblock_angular_cert.json`, `_output.txt`.

## 0. Summary

1. **The one-step angle law has four silent phases (Lemma 12).** In the primitive frame $W=\sqrt Qe^{i\theta}$, $\delta_T-\tfrac\pi3=\sqrt Q\,g(\theta)+\varrho$ with $g(\theta)=\tfrac23\cos^2(\theta-\tfrac\pi6)\sin(\tfrac\pi3-\theta)$ and $|\varrho|\le c_\delta Q$, $c_\delta=0.793$ on $U_T$. At the six block phases $\theta=-s\tfrac\pi3$: $g=0$ for $s\in\{1,2,4,5\}$, $g(-\pi)=-\tfrac{\sqrt3}4$, $g(0)=+\tfrac{\sqrt3}4$ — the first-order angular deviation vanishes at four of the six steps and the two others cancel over a block (which is why the six-step deficit has no $\sqrt Q$ term, Lemma C′).
2. **The partial block is known (Prop. 10).** The slip anchor has $\theta=o_{j_k}\in[0,\Delta)$, so the point $s$ steps before it has $\theta=-s\tfrac\pi3+O(\sqrt Q)$, and
$$P_{r}=\sum_{i<r}\bigl(\tfrac\pi3-\delta_T(x_{6M+i})\bigr)=\kappa(r)\sqrt{Q_\star}+\varrho_P,\qquad\kappa(r)=\bigl(0,0,0,\tfrac{\sqrt3}4,\tfrac{\sqrt3}4,\tfrac{\sqrt3}4\bigr)_r,\qquad|\varrho_P|\le c_P(r)\,Q^\dagger,$$
with $Q_\star$ the anchor amplitude, $Q^\dagger$ the in-block amplitude ceiling and $c_P(r)$ explicit ($c_P(5)\approx15$). Instead of the theorem's worst case $5\arcsin(0.705\sqrt Q)\approx3.5\sqrt Q$, the partial block contributes a term of known sign and size $\le0.433\sqrt Q$, which can be moved into the schedule centre since $r_k=n_{j_k}\bmod6$ is in the record (in fact $r_k\equiv n_0+k-1\pmod 6$), leaving an $O(Q)$ error. The overshoot $o_{j_k}\in[0,\Delta_{j_k})$ is centred the same way ($\tfrac\tau2(a+M)^{-1}$).
3. **Sharpened schedule and envelope (Cor. 11).** For known $a$,
$$\tau\psi(a+M_k)-(k-1)\tfrac\pi3+\kappa(r_k)(a+M_k)^{-1/2}+\tfrac\tau2(a+M_k)^{-1}=L+\varepsilon''_k,\qquad|\varepsilon''_k|\le E''(a,M_k,r_k),$$
$E''=\xi_{\max}+c_P(r)Q^\dagger+\kappa(r)\,|\sqrt{Q_\star}-(a+M)^{-1/2}|_{\max}+\tau\bar S'+\bar R'$. All in-block terms are now $O((a+M)^{-1})$; $E''\sqrt{a+M}\to\tau\cdot0.7485+1.0753=1.9396$ (part 1b: $5.46$; part 1: $187.3$). Values ($a=625$, worst $r$): $E''=0.078$ at $M=10^3$ ($E'$ $0.166$), $0.023$ at $10^4$ ($0.057$), $0.0066$ at $10^5$ ($0.0177$), $0.0020$ at $10^6$, $0.00062$ at $10^7$ — factors $2.1\to2.8$; for $r\le2$ the in-block term is $<10^{-3}$ of $E''$.
4. **Effect on part 2.** The enclosures of the 12 sample records recomputed with the corrected centres and $E''$: $a$-widths $64$–$113$ at $a=625$ (part 2: $173$–$245$), $194$–$255$ at $1000$ ($461$–$589$), $309$–$401$ at $2500$ ($726$–$965$) — factors $2.1$–$2.7$; $L$-hulls $0.008$–$0.013$ wide (part 2: $0.022$–$0.035$); true $a$ and $L$ inside in 12/12; single components.
5. **`[NUM]`.** On all $73$ slips of the 12 orbits: $|P_{r_k}-\kappa(r_k)\sqrt{Q_\star}|\le c_P(r_k)Q^\dagger$ with ratio $\le0.11$, and $|\varepsilon''_k|\le E''$ with ratio $\le0.40$. NC1 (phase direction reversed) and NC2 ($r$ shifted by one) violate the residual bound.
6. **Scope and typing.** Lemma 12 and Prop. 10 use only the primitive map and the adopted A1b inputs (lift alignment, Lemma C′, $U_T$); grade target `[ALG]`. Cor. 11's $E''$ inherits part 1b's dependency `[assuming: Dyadic row-A bridge/remainder constants as published]` through $\bar S',\bar R'$ and the amplitude bracket; the in-block part itself needs no Dyadic constant. The adopted THM is unchanged; the sharpened schedule is a candidate addition (same scope), not a replacement.

## 1. Lemma 12 (one-step angle law in the primitive frame)

$W=\rho+\omega\eta$, $\omega=e^{2\pi i/3}$, $\lambda=e^{i\pi/3}$; $T:(\rho,\eta)\mapsto(\rho-\sin\eta,\ \eta+e^\rho-1-\sin\eta)$. Exactly (G1): $W(Tx)=\lambda W+\lambda(\eta-\sin\eta)+\omega(e^\rho-1-\rho)$, $\rho=\tfrac{2}{\sqrt3}\operatorname{Re}(We^{-i\pi/6})=\tfrac2{\sqrt3}\sqrt Q\cos(\theta-\tfrac\pi6)$, $\eta=\tfrac2{\sqrt3}\sqrt Q\sin\theta$. With $\varepsilon:=W(Tx)/(\lambda W)-1$ and $\varepsilon_1:=\omega\rho^2/(2\lambda W)=\lambda\rho^2/(2W)=\tfrac23\sqrt Q\cos^2(\theta-\tfrac\pi6)e^{i(\pi/3-\theta)}$:
- $|\varepsilon|\le\bar\varepsilon(Q):=e_{\sqrt{}}\sqrt Q+e_1Q$, $e_{\sqrt{}}=\tfrac23e^{2\cdot0.047/\sqrt3}=0.70385$, $e_1=\tfrac{(2/\sqrt3)^3}6=0.25660$ (the A1b constants $0.705$, $0.257$ re-derived; $\sqrt Q<0.047$ on $U_T$);
- $|\varepsilon-\varepsilon_1|\le c_2Q$, $c_2=\tfrac{(2/\sqrt3)^3}{6}(1+e^{0.0543})=0.52751$ (from $\tfrac{|\eta|^3}6+\tfrac{|\rho|^3}6e^{|\rho|}$);
- $\delta_T-\tfrac\pi3=\operatorname{Arg}(1+\varepsilon)$, and $|\operatorname{Arg}(1+\varepsilon)-\operatorname{Im}\varepsilon_1|\le c_2Q+\tfrac{\bar\varepsilon^2}{2(1-\bar\varepsilon)}\le c_\delta Q$, $c_\delta=0.7927$ on $U_T$ (increasing in $Q$; evaluated at $Q=2209\times10^{-6}$).
Hence $\delta_T-\tfrac\pi3=\sqrt Q\,g(\theta)+\varrho$, $g(\theta)=\operatorname{Im}\varepsilon_1/\sqrt Q=\tfrac23\cos^2(\theta-\tfrac\pi6)\sin(\tfrac\pi3-\theta)$, $|\varrho|\le c_\delta Q$. Values: $g(-s\tfrac\pi3)=(\tfrac{\sqrt3}4,0,0,-\tfrac{\sqrt3}4,0,0)$ for $s=0,\ldots,5$ (exact, G1); $\sup|g|=0.4517$, $\sup|g'|=0.6908$ (G2). *Reading:* at $\theta=-\tfrac\pi3,-\tfrac{4\pi}3$ the point lies on $\rho=0$ ($e^\rho-1-\rho=0$ exactly); at $\theta=-\tfrac{2\pi}3,-\tfrac{5\pi}3$ the factor $e^{i(\pi/3-\theta)}$ is real, so $\varepsilon_1$ changes the amplitude, not the angle. $\square$

## 2. Proposition 10 (partial block) and Corollary 11 (sharpened schedule)

Notation as in the A1b cell: slip anchor $n_{j_k}=6M+r$, $0\le r\le5$; $Q_\star=Q(x_{n_{j_k}})$; $Q^\dagger$ an upper bound for every amplitude of the block (part 1b Cor. 3: $Q^\dagger=f^{\circ5}(\bar Q_M)$ with $f(Q)=Q(1+\bar\varepsilon(Q))^2$); $\bar\varepsilon^\dagger=\bar\varepsilon(Q^\dagger)$, $\bar\alpha=\arcsin\bar\varepsilon^\dagger$, $\bar\Delta=\tau Q^\dagger+1.82Q^{\dagger3/2}$.

**Proposition 10.** `[ALG]` target [scope: $x_0\in U$, the adopted A1b setting] $P_r=\kappa(r)\sqrt{Q_\star}+\varrho_P$ with $\kappa(r)=-\sum_{s=1}^rg(-s\tfrac\pi3)$, i.e. $\kappa=(0,0,0,\tfrac{\sqrt3}4,\tfrac{\sqrt3}4,\tfrac{\sqrt3}4)$, and
$$|\varrho_P|\le\sum_{s=1}^{r}\Bigl[c_\delta Q^\dagger+\sqrt{Q^\dagger}\,\|g'\|_\infty(\bar\Delta+s\bar\alpha)+|g(-s\tfrac\pi3)|\sqrt{Q^\dagger}\bigl((1-\bar\varepsilon^\dagger)^{-s}-1\bigr)\Bigr]=:c_P(r)\,Q^\dagger .$$
*Proof.* The anchor's angle is $\theta_{n_{j_k}}=o_{j_k}\in[0,\Delta_{j_k})$ (Lemma A). For the point $s=r-i$ steps before it, $\theta_{6M+i}=o-\sum_{t=i}^{r-1}\delta_T(x_{6M+t})\equiv-s\tfrac\pi3+e_i\pmod{2\pi}$ with $|e_i|\le\bar\Delta+s\bar\alpha$ (one-step pointwise bound, Lemma C′). Amplitudes: $\sqrt{Q_{6M+i}}=\sqrt{Q_\star}\prod_{t=i}^{r-1}|1+\varepsilon_t|^{-1}$, so $|\sqrt{Q_{6M+i}}-\sqrt{Q_\star}|\le\sqrt{Q_\star}((1-\bar\varepsilon^\dagger)^{-s}-1)$. By Lemma 12, $\tfrac\pi3-\delta_T(x_{6M+i})=-\sqrt{Q_{6M+i}}\,g(\theta_{6M+i})-\varrho_i$, and
$|\sqrt{Q_{6M+i}}g(\theta_{6M+i})-\sqrt{Q_\star}g(-s\tfrac\pi3)|\le\sqrt{Q^\dagger}\|g'\|_\infty|e_i|+|g(-s\tfrac\pi3)|\,|\sqrt{Q_{6M+i}}-\sqrt{Q_\star}|$ ($g$ is $2\pi$-periodic). Summing over $s=1..r$ gives the claim. $\square$
*Remarks.* (i) $r_k$ is determined by the record: $n_{j_k}=n_0+6j_k+(k-1)$, so $r_k\equiv n_0+k-1\pmod6$. (ii) Only $s=3$ contributes to $\kappa$ and to the amplitude-drift term; for $r\le2$, $P_r=O(Q)$ outright.

**Corollary 11 (sharpened schedule and envelope).** `[ALG]` target, scope as the THM; conditional through $\bar S',\bar R'$ and the amplitude bracket as part 1b. From the exact identity $\tau\psi(a+M_k)-(k-1)\tfrac\pi3=L-o_{j_k}-P_{r_k}+\tau S^{\rm tail}_{M_k}-R^{\rm tail}_{M_k}$:
$$\tau\psi(a+M_k)-(k-1)\tfrac\pi3+\kappa(r_k)\,(a+M_k)^{-1/2}+\tfrac\tau2(a+M_k)^{-1}=L+\varepsilon''_k,$$
$$|\varepsilon''_k|\le E''(a,M_k,r_k):=\xi_{\max}+c_P(r_k)Q^\dagger+\kappa(r_k)\max\bigl(\sqrt{Q^\dagger}-(a+M)^{-1/2},\ (a+M)^{-1/2}-\sqrt{Q^\dagger_{\rm lo}}\bigr)+\tau\bar S'(a,M_k)+\bar R'(a,M_k),$$
where $\xi_{\max}=\max(\tfrac\tau2(a+M)^{-1},\ \bar\Delta-\tfrac\tau2(a+M)^{-1})$ bounds $|\tfrac\tau2(a+M)^{-1}-o_{j_k}|$ and $Q^\dagger_{\rm lo}=\underline Q_M(1-\bar\varepsilon^\dagger)^{10}$ is an in-block amplitude floor ($\underline Q_M^{-1}=(a+\Delta_a+M+\bar\epsilon_M)(1+\tfrac{c_Q\sqrt{q_M}}{1-c_Q\sqrt{q_M}})$ from part 1b's Lemmas 1–2 and the bridge). *Proof.* Prop. 10, the overshoot centring, and $|\kappa\sqrt{Q_\star}-\kappa(a+M)^{-1/2}|\le\kappa|\sqrt{Q_\star}-(a+M)^{-1/2}|$ with $Q_\star\in[Q^\dagger_{\rm lo},Q^\dagger]$. $\square$

## 3. Values

$a=625$ (the $a$-dependence is weak); in-block term = $\xi_{\max}+c_PQ^\dagger+\kappa\cdot$ref.error:

| $M$ | $E''$, $r\le2$ | $E''$, $r=5$ (in-block part) | $E'$ (part 1b; in-block part) | gain | $E''\sqrt{a+M}$ ($r=5$) |
|---|---|---|---|---|---|
| $10^3$ | $0.0672$ | $0.0779$ ($0.0113$) | $0.1660$ ($0.0994$) | $2.1$ | $3.14$ |
| $10^4$ | $0.0217$ | $0.0231$ ($0.00148$) | $0.0574$ ($0.0358$) | $2.5$ | $2.38$ |
| $10^5$ | $0.00642$ | $0.00656$ ($1.5\times10^{-4}$) | $0.0177$ ($0.0113$) | $2.7$ | $2.08$ |
| $10^6$ | $0.00197$ | $0.00199$ ($1.5\times10^{-5}$) | $0.00551$ ($0.00354$) | $2.8$ | $1.99$ |
| $10^7$ | $0.000618$ | $0.000619$ ($1.4\times10^{-6}$) | $0.00173$ ($0.00112$) | $2.8$ | $1.96$ |

Asymptotic constant $E''\sqrt{a+M}\to1.9396$: the whole remaining $M^{-1/2}$ budget is the two tails ($\tau\bar S'$: $0.864$, $\bar R'$: $1.075$), which are tight at leading order (part 1b §3). Further gains therefore need the Dyadic-side remainder structure, not RECOG-side bookkeeping. No universal ceiling is claimed for $E''$ (scan values, `[NUM]`: $E''(625,1,5)=0.162$, $E''(625,100,5)=0.144$, $E''(2500,1,5)=0.067$).

## 4. Effect on the unknown-$a$ intervals (part 2 recomputed)

Same 12 records ($1.8\times10^6$ steps), Lemma-8 interval from part 2, boxes classified with the corrected centres $c''_k(a)$ and $E''$ (part-2 algorithm, `classify` replaced; inner/outer as in part 2 v0.2.1):

| $a$ | $\theta_0$ | $K$ | outer $a$-enclosure (width) | part 2 width | $L$-hull (width) | part 2 $L$ width |
|---|---|---|---|---|---|---|
| 625 | 0.3 | 7 | $[625,689.1]$ ($64$) | $173$ | $[7.6975,7.7075]$ ($0.010$) | $0.028$ |
| 625 | 1.7 | 7 | $[625,737.6]$ ($113$) | $235$ | $[8.0963,8.1050]$ ($0.009$) | $0.023$ |
| 625 | 3.9 | 7 | $[625,734.2]$ ($109$) | $245$ | $[8.2172,8.2254]$ ($0.008$) | $0.022$ |
| 625 | 5.1 | 6 | $[625,713.8]$ ($89$) | $229$ | $[8.3139,8.3265]$ ($0.013$) | $0.035$ |
| 1000 | 0.3 | 7 | $[885.5,1079.3]$ ($194$) | $461$ | $[8.2476,8.2558]$ ($0.008$) | $0.022$ |
| 1000 | 1.7 | 6 | $[884.2,1139.5]$ ($255$) | $545$ | $[8.6347,8.6466]$ ($0.012$) | $0.031$ |
| 1000 | 3.9 | 6 | $[885.3,1135.0]$ ($250$) | $568$ | $[8.7516,8.7627]$ ($0.011$) | $0.030$ |
| 1000 | 5.1 | 6 | $[863.0,1109.2]$ ($246$) | $589$ | $[8.8627,8.8731]$ ($0.010$) | $0.028$ |
| 2500 | 0.3 | 6 | $[2319.7,2628.2]$ ($309$) | $726$ | $[9.3153,9.3240]$ ($0.009$) | $0.023$ |
| 2500 | 1.7 | 5 | $[2321.1,2716.8]$ ($396$) | $885$ | $[9.6883,9.7013]$ ($0.013$) | $0.034$ |
| 2500 | 3.9 | 5 | $[2316.1,2712.3]$ ($396$) | $923$ | $[9.8008,9.8129]$ ($0.012$) | $0.032$ |
| 2500 | 5.1 | 5 | $[2277.5,2678.6]$ ($401$) | $965$ | $[9.9275,9.9389]$ ($0.011$) | $0.030$ |

True $a$ and estimated $L$ inside in all cases; inner enclosures single intervals, undecided length $0.5$–$1.4$. Relative $a$-widths now $10$–$18$ % at $a=625$, $19$–$26$ % at $1000$, $12$–$16$ % at $2500$.

## 5. `[NUM]` residual check (not a proof input)

All $73$ slips of the 12 orbits: $P_{r_k}$ computed from the simulated lift, $Q_\star$ from the simulated anchor; $|P_{r_k}-\kappa(r_k)\sqrt{Q_\star}|/c_P(r_k)Q^\dagger\le0.112$ (the bound is a majorant with the $\|g'\|\,s\bar\alpha$ term dominating); $|\varepsilon''_k|/E''\le0.399$ (against the $L$ estimated at the run's end, tolerance $\tau\sqrt{Q_{\rm end}}$). Sample ($a=625$, $\theta_0=1.7$, first slip $M=467$, $r=5$): $P_5=1.40\times10^{-2}$, $\kappa\sqrt{Q_\star}=1.29\times10^{-2}$, residual $1.1\times10^{-3}$ against the bound $1.5\times10^{-2}$; old in-block bound $0.199$. NC1 (the phase direction reversed, $\kappa\to-\kappa$) and NC2 ($r\to r+1\bmod6$) violate the residual bound on the same data.

## 6. Consequences and next steps

- **DSN candidate (later release):** a sharpened form of THM (S) with the known partial-block and overshoot centres and the $O(Q)$ in-block error (additive; the adopted form stays valid), plus the RESULT's envelope clause with $E''$. Not adopted.
- **Part 2:** certified $a$-windows shrink by $2.1$–$2.7$; still far from the heuristic fiber scale (part 3), as expected: the window is set by $E''(a,M_1)\approx2/\sqrt{a+M_1}$ at the first slip, i.e. by the tails.
- **Remaining levers:** the two tails are tight at leading order within RECOG; the next factor would have to come from Dyadic ($r_m$ beyond the row-A majorants) or from using the tails' oscillation *sign* at the slip (a known-phase refinement of part 1b, `[SESSION]` idea).

## 7. Not claimed

No change to the adopted THM; no universal ceiling for $E''$; the `[NUM]` ratios are observations; $c_P$ is a majorant, not optimal; nothing about unknown-$a$ beyond the recomputed enclosures.

## 8. Certificate

G1 exact: the one-step identity, $\rho=\tfrac2{\sqrt3}\operatorname{Re}(We^{-i\pi/6})$, the formula for $g$, the six phase values, $\kappa(r)$. G2 interval constants ($e_{\sqrt{}}\le0.705$, $e_1\le0.257$, $c_2$, $c_\delta$, $\sup|g|$, $\sup|g'|$ by grid with second-derivative correction). G3 $E''<E'$ at every $(a,M,r)$ of the grid; the asymptotic constant. G4 the `[NUM]` residual bounds at all slips. G5 the recomputed part-2 enclosures: narrower than part 2's on every record, true $a$ inside. NC1–NC2 on the same data. Imports: part-1b script `2d446dd7…3cf0`, part-2 script `746bf4b0…3380` (v0.2.1), unchanged.
