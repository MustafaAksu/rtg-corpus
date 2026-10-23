# RECOG CELL-E3A-4 — Preregistration: certified crossing of the period-9 local stable graph

**Target RID:** `RECOG-THM-TWIN-STAGE2-NONUNIVERSAL` `[THM]` [scope: diagnostic twin $T_s$, SG-R4]
**Claim to be certified:** there exists $x_\infty\in\mathcal A=\{\tfrac7{200}\le Q<\tfrac{58107}{1600000}\}$ with $D_s(T_s^nx_\infty)>0$ for all $n\ge0$; hence the universal R7 Stage-2 statement $\forall x\in\mathcal A\ \exists n:\ D_s(T_s^nx)<0$ is **false**.
**Corollary (same proof):** that survivor never meets $C_0^{(s)}$ (its determinant is strictly positive at every step).
**Not claimed:** any statement that entry into $D_s<0$ is generic, typical or of full measure (E3A-1 suggests it numerically; no measure theorem exists).

## Upstream objects (fail-closed on hashes)

| object | file | sha256 |
|---|---|---|
| E3A-3a rev. 1.2 — period-9 winding-4 saddle, safe root box (centre + exact radius $10^{-35}$) | `e3a3a_p9_saddle.json` | `01ba69c3b5a36afc6ff5baf46eaf14de86876533546f7e6f93c4b187bb642cef` |
| E3A-3a script rev. 1.2 | `recog_cell_e3a3a_p9_saddle_cert.py` | `a90dd72e7ce9964dc0b1be23c388728c5d1dd81f1297610b7f619bfeec789d9e` |
| E3A-3b rev. 1.1 — local stable graph, $r=10^{-6}$, $\gamma=100$, rational separator, all gate margins | `e3a3b_p9_stable_local.json` | `545ecf628d6bdc40fe16530624935380868ae7252d6da23ad10f88421fc4531a` |
| E3A-3b script rev. 1.1 | `recog_cell_e3a3b_p9_stable_local.py` | `ede0b7e1074463c3c526177ea9dc55486bdf46c000753f0351a6cb7903448e21` |
| E3A-1 rev. 3.1 late locus (`[NUM]`, shooting seeds only) | `e3a1r31_late_cells.jsonl` | `0a59d01ef9c8ac0026fa61dbdc60f840297a3574d6bbe81be02fedd2d2956be4` |

## Procedure

1. **Candidate shooting `[ENG/NUM]` (not part of the proof).** From E3A-1 late cells, propagate at high precision and find a step $N$ and lift integer $L$ with $T_s^N(x)$ close to $x_9+(0,2\pi L)$ (for each of the nine orbit points as entry phase, using $T_s^{N}$ and the corresponding cyclic shift). In the 3b frame $\xi=P_0^{-1}(T_s^N(x)-(0,2\pi L)-c)$, estimate the gradient of the terminal $u$-coordinate with respect to the initial point; choose a segment direction $v$ transverse to the apparent stable preimage. One or two extra near-saddle periods may be used to trade initial width for terminal side separation (local expansion $\approx37.8$ per period).
2. **Exact initial segment.** Exact rational centre $x_c$ and direction $v$ in $(\rho,\eta)$: $I=\{x_c+tv:\ -1\le t\le1\}$. Certify $q_1\le Q(x(t))<q_2$ for all $t$ (Arb, $Q=\rho^2-\rho\eta+\eta^2$ on the lift), so $I\subset\mathcal A$.
3. **Thin-segment transport `[ALG via IA]`.** Propagate $I$ for $N$ primitive steps with a Lohner kernel (mean-value step, frame oriented on the image of the long axis, exact point frames with Arb-enclosed inverses) **copied into the E3A-4 source**, so the single E3A-4 script hash freezes the proof engine. Subdivision is in the parameter $t$ only: a piece that fails is re-transported **from step 0** as two exact $t$-halves, so certification bookkeeping lives entirely on initial parameter intervals. At every step $0\le n<N$ certify $\inf D_s>0$ on every piece.
   **Coverage gate (exit-coded):** the certified pieces satisfy $[-1,1]=I_1\cup\cdots\cup I_m$ with exact rational endpoints, ordered, no gaps, only endpoint overlaps. (No overlap of image boxes is required.)
4. **Terminal chart gate.** After subtracting $(0,2\pi L)$: certify every terminal piece lies in $c+P_0R$ ($|s|,|u|<10^{-6}$ via exact $P_0^{-1}$); for the two endpoints $t=-1$ and $t=+1$ (transported as exact points) certify one has $u<h_-(s)$ and the other $u>h_+(s)$, with the registered definitions
$$h_-(s)=U_{\rm LO}-\frac{|s|+S_{\rm HI}}{\gamma},\qquad h_+(s)=U_{\rm HI}+\frac{|s|+S_{\rm HI}}{\gamma}$$
(rational constants from the 3b record).
   **All theorem-grade terminal tests occur in the one registered 3b chart around the phase-0 representative $x_9$.** If shooting first approaches cycle phase $j$, that is used only to locate the candidate; the certified time $N$ includes the $(9-j)\bmod9$ additional primitive steps and the appropriate lift translation, so that $T_s^N(I)-(0,2\pi L)\subset c+P_0R$. No cyclic copies of the frame are constructed.
5. **Conclusion `[THM]`.** $T_s^N(I)-(0,2\pi L)$ is connected, lies in $R$, and has endpoints on opposite certified sides of the stable graph; by the intermediate value theorem some $x_\infty\in I$ maps into $W^s_{\rm loc}$. Step 3 gives $D_s>0$ for $n<N$; 3b gives $D_s>0$ at every primitive step thereafter.

## Precision and escalation (fail-closed)

- Start at 1024 bits. On a piece failure, distinguish the cause: **arithmetic** (the enclosure is wide although the piece's transported geometric extent, measured by its midpoint-image spread, is small) → escalate precision ×2, up to 4096 bits; **geometric** (the piece itself is too wide) → subdivide in $t$. Fail closed if a piece cannot be certified within the precision cap and the subdivision depth cap; report every escalation and split.
- The initial width is not fixed in advance; it is chosen by step 1 so that the terminal segment spans the separator while staying inside $R$.

## Modes

`--shoot` (`[ENG/NUM]`, high-precision mpmath; not part of the proof) proposes a frozen rational candidate $(x_c, v, N, L)$ and writes it to a candidate file. `--cert` reads only that frozen candidate and runs the theorem-grade gates; the theorem does not depend on which heuristic found the segment.

## Outputs

A result record with: all upstream hashes; $x_c$, $v$, $N$, $L$, entry phase; $Q$-range certificate for $I$; per-step minimum certified $D_s$ lower bound; subdivision count; terminal piece enclosures in $(s,u)$; the two endpoint side certificates with numeric margins; precision used; `all_checks_pass`. An exit-coded gate (R8 style) re-verifies the record against the upstream hashes and recomputes the endpoint side tests.
