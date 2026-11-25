# Node Foundations — Binary Recognition: Wrap-up

**Status:** SESSION / NONCANONICAL wrap-up note. Not an owner DSN, not an adoption, no RID. Presence in the repository is not adoption.
**Date:** 25 October 2026
**Thread:** 14–15 October 2026. Base note `NODE_BINARY_TO_ANGULAR_PRELIMINARY_v0.1` and supplements v0.1.1–v0.1.6, handoff appendix, v0.2 addendum (producing session); reviews and contributions by Claude; PI direction throughout.
**Prepared by:** Claude (OFN co-owner session). PI holds every decision.
**Proposed location:** `records/ofn/NODE_BINARY_RECOGNITION_WRAPUP.md`; evidence under `evidence/ofn/binary_recognition/`. Placement is a PI decision (alternative: `records/recog/`).
**Owner pins checked against current editions (25 Oct 2026):** RECOG v0.3.24 (`recog-v0.3.24`) SG-R6, SG-R14, RECOG-ALG-SELECTION-SIN; RRF v0.8.4 (`rrf-v0.8.4`) §4.1 comparator typing and $S$-decomposition, §4.2 typed-covariance criterion; OFN v0.10 (`ofn-v0.10`) RTG-OFN-DEF-BACKGROUND-TIME, OPEN-OFN-7, SG-OFN-PRESENTATION; DYAD v6.4.22 (`dyad-v6.4.22`) §6.2 $J(P_1)$; TDR-G v2.12.13 G0. The thread itself cited RECOG v0.3.20, RRF v0.8, DYAD v6.4.10, OFN v0.8/v0.9; the passages used are present unchanged in substance in the editions above.

---

## 1. Question and answer

**Question.** Can a binary relational comparison, without assigning phase to a node at the outset, be extended to angular (phase) structure?

**Answer, in one paragraph.** Yes, discretely and conditionally. If a dyad carries one retained bit (the previous realization) and recognition is required to alternate, the update is forced and is a four-state cycle carrying a faithful $\mathbb Z_4$ phase. Extending the same idea to an $n$-bit twisted register gives a $2n$-cycle and a cyclotomic phase coordinate $Z_n$. The arithmetic of when this coordinate faithfully carries recognition is now closed for the fixed model: native parity is carried exactly by the 2-primary part of the spectrum, so the lengths at which the bridge is faithful and gauge-invariant are the powers of two, and every length has a canonical recognition quotient onto the power-of-two register $X_h$. What the model does **not** give: continuous phase, physical time, a node-count or third-node theorem, a recognition *event*, the nonlinear DYAD generator, or amplitude dynamics. Those are model-contract questions for RECOG, RRF and OFN (§7).

**Status of the thread.** The arithmetic of the fixed family $(F_n,C_n,Z_n)$ is closed. No further census is needed to establish any boundary stated below. The remaining work is a recognition-contract decision, not a computation.

## 2. The model

- Two-bit dyad: current realization $b$, retained record $p$; endpoint complementarity $(a,b)=(1-b,b)$ kept; $p$ is a record component of the same relation, not a third node. Update $F(b,p)=(f(b,p),b)$; recognition $d=b\oplus p$.
- $n$-bit twisted register: $X_n=\{0,1\}^n$, $F_n(x_0,\dots,x_{n-1})=(1-x_{n-1},x_0,\dots,x_{n-2})$, complement $C_nX=1-X$, parity $\pi_n=\bigoplus x_j$. Here $n$ counts **all** register bits (one current, $n-1$ retained); it is not an endpoint count.
- Bridge: $\lambda_n=e^{i\pi/n}$, $P_X(t)=\sum x_jt^j$, $Y_X(t)=\sum(2x_j-1)t^j$,
  $Z_n(X)=1-(1-\lambda_n)P_X(\lambda_n)=-\tfrac{1-\lambda_n}{2}Y_X(\lambda_n)$.
  $Z_n(X)=Z_n(Y)\iff\Phi_{2n}\mid P_X-P_Y$; $Z_n(X)=0\iff\Phi_{2n}\mid Y_X$.
- Basic identities [ALG]: $F_n^n=C_n$, $F_n^{2n}=\mathrm{id}$, $F_nC_n=C_nF_n$, $Z_nF_n=\lambda_nZ_n$, $Z_nC_n=-Z_n$.
- Notation: $n=2^am$, $m$ odd, $h=2^a$; $\mathrm{Zero}(n)=\{Z_n=0\}$; $\mathrm{Short}(n)=\{\mathrm{period}<2n\}$; $X_n^\times=\{Z_n\ne0\}$.

The update index is a formal event succession, not physical time (OFN RTG-OFN-DEF-BACKGROUND-TIME, OPEN-OFN-7). Whether $C_n$ is physical gauge or a representation-level involution is not decided (SG-OFN-PRESENTATION; RECOG SG-R14).

## 3. Results

Grades follow the programme tag order. "Check" refers to the consolidated script (§8.1).

### A. The two-bit cycle

| Tag | Statement | Scope / note | Check |
|---|---|---|---|
| [ALG] | In $F(b,p)=(f(b,p),b)$, recognition alternation $d'=1\oplus d$ alone forces $f=1\oplus p$. Reversibility, absence of fixed states and $C$-covariance follow. Equivalently: reversible + no fixed state forces the same $f$. | The two-stage Johnson / twisted-ring counter. Retention $p'=b$, the full state space and alternation are assumptions. | C1 |
| [ALG] | Orbit $(0,0)\to(1,0)\to(1,1)\to(0,1)$; $F^2=C$, $F^4=\mathrm{id}$. Realization $b_m=0,1,1,0,\dots$ ($b_{m+2}=1-b_m$); recognition $d_m=0,1,0,1,\dots$ | The realization bit does not alternate; recognition does. | C1, C2 |
| [ALG] | Reversible laws are exactly $f=p\oplus g(b)$; $C$-covariant only for constant $g$. | Covariance is not generic among reversible records. | C1 |
| [ALG] | $Z(b,p)=1-b-p+i(b-p)$: $|Z|=1$, $Z(FX)=iZ$, $Z^2=(-1)^d$. | A chosen faithful character of $\mathbb Z_4$; phase origin and handedness are conventions. | C2 |
| [ALG] | Role reversal $R(b,p)=(p,b)$: $RFR=F^{-1}$, $Z(RX)=\overline{Z(X)}$. | Orientation of the cycle is the realization/record functional asymmetry, not a time arrow. | C2 |
| [HEUR] | $\mathbb Z_4\to\mathbb Z_2$ is a two-sheeted cyclic cover; $F^2$ returns the readout and sends $Z\mapsto-Z$. | Analogy to sign return only; not spin, not $SU(2)$. | — |
| [ALG] | If $C$ is instantaneous gauge, $X/\langle C\rangle$ has two points, its invariant is $d$, its dynamics the 2-cycle. | The gauge-invariant instantaneous content is binary. | — |
| [ALG] | $\Gamma(X,Y)=\overline{Z(X)}Z(Y)$: invariant under diagonal $C$, odd under one-sided $C$, $\Gamma(Y,X)=\overline{\Gamma(X,Y)}$; $\Gamma(X,FX)=i$ for all $X$; with a retained reference $X_*$, $\Gamma(X_*,F^mX_*)=i^m$. | Four-valued relative phase needs an admitted common-reference comparison. The carrier (internal memory, second dyad, new endpoint) is not determined; no node-count theorem. | — |

### B. The register family: recognition and gauge type

| Tag | Statement | Scope / note | Check |
|---|---|---|---|
| [ALG] | $\pi_n(F_nX)=1\oplus\pi_n(X)$ and $\pi_n(C_nX)=\pi_n(X)\oplus(n\bmod2)$. | For $n=2$, $\pi_2=d$. | C3 |
| [ALG] | Every strictly alternating Boolean readout $d$ satisfies $d(C_nX)=d(X)\oplus(n\bmod2)$ (because $F_n^n=C_n$). There are exactly $2^{r_n}$ such readouts ($r_n$ = orbit count). | Even $n$: complement-invariant; odd $n$: complement-odd. Exhaustive through $n=4$; general proof one line. | C3 |
| [ALG] | Affine alternating readouts over GF(2) are exactly $\pi_n$ and $1\oplus\pi_n$, for every $n$. Proof: in $\mathbb F_2[t]/(t^n+1)$, $F_n:P\mapsto tP+1$; alternation forces $\ell(1)=1$, $\ell((t+1)P)=0$, and $R_n/(t+1)R_n\cong\mathbb F_2$, so $\ell=\mathrm{ev}_1$. | Affinity is an added readout-class restriction. Uniqueness also holds on the nonzero sector (the all-zero orbit flips one bit per step). | C3 |
| [ALG] | $n=3$: one 6-cycle and one 2-cycle ($010\leftrightarrow101$). $B(b,p_1,p_2)=(b-p_2,\,b+p_1-1)$ satisfies $BF_3=AB$, $A=\begin{pmatrix}1&-1\\1&0\end{pmatrix}$ = DYAD $J(P_1)$ (§6.2). The 6-cycle maps to the unit-$Q$ hexagon (the six Eisenstein units), the 2-cycle to the origin. | Linear resonance matching only: no $\sin$, shear, $\mu$, contraction or amplitude; $F_3^6=\mathrm{id}$ exactly. | C4 |
| [ALG] | $B$ loses parity on the zero fibre ($B(010)=B(101)=0$, opposite parity). On the hexagon, $(-1)^{\pi_3}=-W^3$, $W=\rho+\omega\eta$. | Any bridge must state which observables factor through it, not only which update it intertwines. | C4 |
| [ALG] | The $n=3$ quotient by $C_3$ is a 3-cycle plus a fixed point; one traversal of the 3-cycle swaps sheets (transition-sign product $-1$, section-independent). | Finite dynamical cocycle, not a topological bundle. | — |

### C. Faithfulness of $Z_n$ on the full cube

| Tag | Statement | Scope / note | Check |
|---|---|---|---|
| [THM] | $Z_n$ is injective on $X_n$, and $\pi_n$ descends through $Z_n$, iff $n=2^a$. | Fixed bridge, full cube. | C5 |
| [ALG] | Witness for $n\ne2^a$: odd prime $p\mid n$, $d=n/p$, $K_{n,p}(t)=\sum_{j<p}(-1)^jt^{jd}=(t^n+1)/(t^d+1)$; split positive/negative coefficients into $X,Y$. Equal image $\dfrac{\lambda-\lambda^d}{1-\lambda^d}$ (zero iff $d=1$), Hamming weights differ by one. | Checked $n\le60$, every odd prime divisor. | C5 |
| [THM] | For $n\ne2^a$ no strictly alternating Boolean readout descends through $Z_n$ on the full cube: the alternating-block state $y_j=(-1)^{\lfloor j/d\rfloor}$ and its successor both map to 0. | Independent of affinity and of gauge. | — |

### D. Zero fibre versus short orbits

| Tag | Statement | Scope / note | Check |
|---|---|---|---|
| [ALG] | $\mathrm{Short}(n)\subseteq\mathrm{Zero}(n)$ always; $Z_n\ne0\Rightarrow$ period $2n$. | | C6 |
| [THM] | $\mathrm{Zero}(n)=\mathrm{Short}(n)$ iff $n$ has at most one distinct odd prime divisor, or $n=pq$ with $p\ne q$ odd primes. First failures: $n=30$ (even), $n=45$ (odd). | Positive cases: elementary block proof (one odd prime) and binary-matrix proof ($pq$); negative cases constructive (separated $P$-/$Q$-cosets; Rédei three-prime support; even interleaving). No external vanishing-sum theorem is a dependency. | C6 |
| [ALG] | Odd $m$: $\epsilon_{\ell j}=(-1)^jy_j$, $\ell=(m+1)/2$, $S_X=\{\epsilon=+1\}$: $Z_m(X)=0\iff\sum_{u\in S_X}\zeta_m^u=0$; $S_{F^2X}=S_X+1$; $\mathrm{period}(X)=2m/|\mathrm{Stab}(S_X)|$. | Full-period zero states = vanishing subsets with trivial stabilizer. | — |
| [ALG] | Radical stripping: $M$ = odd squarefree radical, $k=n/M$: $\Phi_{2n}(t)=\Phi_{2M}(t^k)$, $\mathrm{Zero}(n)\cong\mathrm{Zero}(M)^k$ by interleaving, $|\mathrm{Zero}(n)|=|\mathrm{Zero}(M)|^{n/M}$. Same decimation as the clock relation $D_rF_n^k=F_MD_r$. | | C6 |
| [ALG] | Two odd primes, $n=kpq$: $|\mathrm{Zero}|=(2^p+2^q-2)^k$, $|\mathrm{Short}|=2^{kq}+2^{kp}-2^k$. $n=30$: 1,444 / 1,084 / 360 full-period zeros; $n=45$: 54,872 / 33,272 / 21,600. | $n=45$ fibre built structurally, not by $2^{45}$ enumeration. | C6 (witnesses) |
| [ALG] | Witnesses: $n=30$ `111111010100101010000101111111`; $n=45$ `111101010100010001011101010100110101011101010`; both $Z=0$ with period $2n$. | A full-period history can live entirely in lower-order cyclotomic components. | C6 |

### E. The nonzero sector

| Tag | Statement | Scope / note | Check |
|---|---|---|---|
| [THM] | On $X_n^\times$: $Z_n$ injective $\iff\pi_n$ descends $\iff n=2^a$ or $n$ an odd prime. | Odd prime: $P_X-P_Y=c\,\Phi_{2p}$, $c\in\{0,\pm1\}$, and $c\ne0$ is the alternating pair (zero image). Otherwise the $K$-witness gives a nonzero opposite-parity collision. | C7 |
| [ALG] | Odd prime $p$: $|X_p^\times|=2^p-2$, $(2^p-2)/2p$ orbits mapped injectively into $\mathbb Z[\zeta_{2p}]$. $p=3$: the six-state hexagon, parity readable but complement-odd. | A faithful full-coordinate catalogue; modulus alone is not. | C7 |
| [ALG] | Guard: on $Y_n^\times$, colouring each $\lambda_n$-orbit, $\bar d(\lambda^jz_\mathcal O)=j\bmod2$, gives $2^r$ descending alternating readouts, complement-invariant for even $n$ (e.g. $n=6$: four target 12-cycles, 16 readouts, none affine). | The selection result concerns native parity and faithfulness, not existence of some alternating output. Choosing orbit origins is new observable selection. | — |
| [ALG] | Spectral admission ($Z\ne0$) and dynamical admission (period $2n$) coincide exactly on the §D class; coincidence does not give recognition descent (e.g. $n=6$: $(1,0,0,0,1,0)$, $(0,0,1,0,0,0)$, equal nonzero image, opposite parity). | | C7 |

### F. Where native parity lives: the 2-primary component and the folding factor

| Tag | Statement | Scope / note | Check |
|---|---|---|---|
| [THM] | Spectral-enrichment criterion: retaining components $\mathcal D\subseteq\{d\mid2n,\,d\nmid n\}$, the map $X\mapsto(P_X\bmod\Phi_d)_{d\in\mathcal D}$ is injective on $X_n$ iff no nonzero $\{-1,0,1\}$-polynomial of degree $<n$ is divisible by $\prod_{d\in\mathcal D}\Phi_d$. | One class of enrichments only. Component decomposition is over $\mathbb Q$, not integral CRT ($\mathrm{Res}(\Phi_4,\Phi_{12})=9$). | — |
| [THM] | $\pi_n$ descends through retained components $\mathcal D$ iff $2h\in\mathcal D$. Sufficiency: $\Phi_{2h}(1)=2$. Necessity: $(t^n+1)/(t^h+1)$ is ternary, degree $n-h$, value 1 at $t=1$. | E.g. $n=6$: $\{\Phi_4\}$ preserves parity, not states; $n=9$: $\{\Phi_2,\Phi_{18}\}$ preserves parity, 490 images for 512 states. | C8 |
| [THM] | $\Phi_{2hd'}(t)\equiv\Phi_{d'}(t)^h\pmod2$ for odd $d'$; hence $\Phi_{2h}\equiv(t+1)^h$ is the only component over the characteristic-2 recognition prime $(t+1)$. | Links the char-2 readout $\mathrm{ev}_1$ to the char-0 bridge; within component-retention bridges only. | C8 ($n\le64$) |
| [ALG] | Folded integer register $c_r=\sum_{k<m}(-1)^kx_{kh+r}$ ($=P_X\bmod t^h+1$): $\pi_n=\sum c_r\bmod2$; exact update $c'=(1-c_{h-1},c_0,\dots,c_{h-2})$; $C:c_r\mapsto1-c_r$; $(m+1)^h$ values. | Odd $n$: $c_0=P_X(-1)$; parity-sufficient but strictly richer than parity (e.g. $n=9$: 10 values). | C9 |
| [ALG] | Boolean folding $\varphi(X)_r=\bigoplus_kx_{kh+r}$, $X_n\to X_h$: $\varphi F_n=F_h\varphi$, $\varphi C_n=C_h\varphi$, $\pi_h\varphi=\pi_n$, onto, $\varphi=c\bmod2$. $Z_h$ is injective on $X_h$. | Every length has a canonical, gauge-compatible recognition quotient onto the power-of-two register. | C9 |
| [ALG] | $\mathrm{period}_{F_h}(\varphi X)=2h$ and $2h\mid\mathrm{period}_{F_n}(X)\mid2n$; ratio $m$ only for maximal-period sources ($n=6$: $(0,1,1,0,0,1)$ has period 4). | | C9 |
| [THM] | $\varphi$ factors through $Z_n$ on the full cube iff $n=2^a$; on $X_n^\times$ iff $n=2^a$ or odd prime. | A faithful $Z_h$ does not repair the original $Z_n$ channel. | C9 |

Information chain (each map $F$-equivariant and parity-preserving):

| Level | Target | Dynamics | States |
|---|---|---|---|
| full register | $X_n$ | $F_n$ | $2^n$ |
| $\Phi_{2h}$ component | $c\in\mathbb Z^h$ | affine signed shift | $(m+1)^h$ |
| Boolean 2-primary factor | $X_h$ | $F_h$ | $2^h$ |
| recognition | $\pi$ | $\pi\mapsto1\oplus\pi$ | 2 |

### G. Refinement and continuum

| Tag | Statement | Scope / note | Check |
|---|---|---|---|
| [ALG] | Bit replication $\mathrm{rep}_k$: $Z_{kn}\mathrm{rep}_k=Z_n$, $F_{kn}^k\mathrm{rep}_k=\mathrm{rep}_kF_n$, $C_{kn}\mathrm{rep}_k=\mathrm{rep}_kC_n$, $\pi_{kn}\mathrm{rep}_k=(k\bmod2)\pi_n$. The register itself realizes the angular-refinement inclusions. | All $n,k$ by proof. | C10 |
| [THM] | If $F_f^kE=EF_c$, both readouts alternate at their own clocks and $d_fE=d_c$, then $k$ is odd. | Coarse and fine recognition are different clock-typed observables; decimated parities $\pi_n(D_rY)$ alternate per coarse block and XOR to the fine parity. | — |
| [ALG] | Distinguished-orbit subsystem: $\varinjlim\mathcal O_n\cong\mathbb Q/\mathbb Z$ (discrete dual $\widehat{\mathbb Z}$); under the stagewise recognition filter it reduces to the Prüfer 2-group. The full Boolean tower is larger (XOR exponent 2). | Stagewise dyadic selection is conditional on the recognition contract. | — |
| [ALG] | Prüfer$_d$ and $\mathbb Z_2$ are Pontryagin dual (residue records ↔ angular characters). Circle-metric completion of the Prüfer group gives $S^1$ (dual $\mathbb Z$). The solenoid is the non-split extension $0\to\mathbb Z_2\to\Sigma_2\to S^1\to0$, dual $\mathbb Z[1/2]$; connected, not path-connected. Translation is not a group endomorphism; it acts on characters by eigenvalues. | Standard mathematics, cited externally (§8.3). Binary records select none of these topologies or clocks. | — |

### H. Amplitude

| Tag | Statement | Scope / note | Check |
|---|---|---|---|
| [ALG] | $|Z_n|$ is invariant under $F_n$, $C_n$ and replication: static, gauge-invariant orbit data, not a radial variable. Not a complete orbit label ($n=8$: 16 full orbits, 12 radii). | No process built from $F$ and replication changes amplitude sector. | — |
| [ALG] | $n=4$: $Z_4(X_4)=\mu_8\sqcup\varepsilon\mu_8$, $\varepsilon=\sqrt2-1$; $\mathbb Z[\zeta_8]^\times\cong\mu_8\times\langle\varepsilon\rangle$ (external). Galois $\lambda\mapsto\lambda^3$ sends $[\varepsilon]\mapsto[\varepsilon]^{-1}$. | The register selects two cosets; the unit theorem does not select them. | — |
| [ALG] | Nonunit images appear at $n=6,7,8$ (norms 4, 8, 17); $n=8$ preserves parity while admitting nonunits. | Unit arithmetic and recognition descent are independent axes. | — |

## 4. Consolidated selection table (fixed $F_n,C_n,Z_n$)

| Requirement | Admissible $n$ |
|---|---|
| Full-cube injectivity / parity descent | $2^a$ |
| $\mathrm{Zero}(n)=\mathrm{Short}(n)$ | at most one odd prime divisor, or $pq$ |
| Nonzero-sector injectivity / native-parity descent | $2^a$ or odd prime |
| Every alternating Boolean readout complement-invariant | even $n$ |
| Native parity, gauge-invariant, readable on the admitted sector | $2^a$, $a\ge1$ |
| Folding $\varphi$ readable through $Z_n$ (full / sector) | $2^a$ / $2^a$ or odd prime |
| Parity readable through a component-retention bridge | iff $\Phi_{2h}$ retained (any $n$) |

**Reading.** Powers of two are not selected as physical register lengths. They are the lengths at which the canonical recognition quotient $X_n\to X_h$ is the identity. The odd part $m$ carries information that native recognition does not see; that is not a statement that it is physically empty. Within this family, a six-step cycle with a faithfully readable admitted sector exists only at $n=3$, at the price of complement-odd recognition.

## 5. Non-claims and scope guards

- Not a derivation of continuous phase, physical time, duration, or the circle metric.
- Not a node-count, third-node or birth theorem; $n$ counts register bits.
- Not a recognition event or event-written memory (RECOG SG-R6). Parity is a deterministic readout.
- Not an identification of $Z_n$ or $\Gamma$ with a registered RECOG/RRF comparator track (RECOG SG-R14; RRF §4.1).
- Not a physical gauge rule: $C_n$ is a representation-level involution until OFN/RRF say otherwise (SG-OFN-PRESENTATION).
- Not the nonlinear DYAD map: the $n=3$ bridge is linear resonance only.
- Finite enumeration certifies finite statements; unbounded statements rest on the written proofs in the source notes; infinite topology is external mathematics.
- Analogies (double cover, sheet swap) are [HEUR] only.

## 6. Corrections record

Self-caught and review-caught errors from the thread, kept as permanent record.

| ID | Tag | Erroneous statement | Corrected statement | Origin |
|---|---|---|---|---|
| COR-BR-1 | [COR] | Relative phase is "the exact point where a third node is forced". | Common-reference comparison is required; its carrier is undetermined; no node-count theorem. | Claude, v0.1 review |
| COR-BR-2 | [RETRACTED] | The dyadic solenoid is totally disconnected. | Connected, not path-connected. | Claude, v0.1.1 review |
| COR-BR-3 | [COR] | $S^1$ and $\mathbb Z_2$ are two completions of the same tower. | Different arrows; Pontryagin-dual constructions; solenoid is the extension in §3G. | Claude, v0.1.1–v0.1.2 reviews |
| COR-BR-4 | [RETRACTED] | $\varphi(2n)<n$ for all $n\ge3$; extra orbits come from a growing kernel. | $\varphi(2n)=n$ iff $n=2^a$; $n=4$ has two 8-cycles and zero kernel. | Claude, v0.1.2 review |
| COR-BR-5 | [COR] | Modulus fibres are classified by Galois classes of free units; the unit coset is Galois-invariant. | Not established; Galois inverts $[\varepsilon]$; equal-modulus $n=8$ pair is non-unit (norm 17). | Claude, v0.1.3 review |
| COR-BR-6 | [COR] | $Z_8^8$ is non-real for most states. | Exactly 128 of 256. | Claude, v0.1.3 review |
| COR-BR-7 | [RETRACTED] | Over GF(2), $t^n+1=(t+1)^n$ for all $n$. | Only for $n=2^a$; $t^n+1=(t^m+1)^h$. The affine-uniqueness proof holds in $\mathbb F_2[t]/(t^n+1)$. | Claude, v0.1.3 review |
| COR-BR-8 | [RETRACTED] | $\mathrm{Zero}(n)=\mathrm{Short}(n)$ for all $n$ (from a census $n\le22$). | False at $n=30$; complete classification §3D. | Claude, v0.1.3 review |
| COR-BR-9 | [COR] | Shared $K$-witness image $1/(1+\lambda^d)$. | $1/(1-\lambda^d)$ for $P_X$; image $(\lambda-\lambda^d)/(1-\lambda^d)$. | Claude, v0.1.5 review |
| COR-BR-10 | [RETRACTED] | At odd $n$, $r_n=(-1)^{\pi_n}$ is RRF $C_-$-typed with zero defect. | $r^{-1}=r$; correct type $\tau_{\rm sign}(r)=(-1)^nr$; zero defect for the sign action, not for inversion. | Claude, v0.1.6 review |
| COR-BR-11 | [COR] | $\Gamma$ is a W-track Hermitian comparator. | Same algebraic shape only; no registered state/domain/transport bridge. | Claude, v0.1.6 review |
| COR-BR-12 | [COR] | Retaining $\Phi_2$ is information-equivalent to a parity coordinate; $\Phi_{2h}$ is the minimal bit-cost target. | Parity-sufficient but strictly richer; minimal Boolean equivariant parity carrier is $\pi$ itself, then $X_h$ (§3F chain). | Claude, appendix review |
| COR-BR-13 | [COR] | "Original register period $2n$" (RECOG co-owner folding review §4). | $2h\mid\mathrm{period}\mid2n$. | PI, on that review |
| COR-BR-14 | [COR] | Base note headline "phase without a third node". | Narrowed per COR-BR-1: the constraint is on retained information and reference transport; endpoint count undetermined. | v0.1.1 disposition |

## 7. Open questions and routing

Wrap-up-local labels, not registry IDs. Routing is a proposal; notices go through the PI.

| Label | Question | Owner |
|---|---|---|
| BR-Q1 | What additional structure turns a readable comparison into a recognition **event**? | RECOG (R6, SG-R6) |
| BR-Q2 | May $r_n=(-1)^{\pi_n}$, with $\tau_{\rm sign}(r)=-r$ at odd $n$, serve a recognition or comparison role? Which common-reference transport makes $r_n(X)r_n(Y)$ admissible, and which comparator track, if any, is connected by an explicit bridge? | RRF §4.1–§4.2; RECOG SG-R14 |
| BR-Q3 | Must recognition preserve native affine parity (1 bit), the Boolean 2-primary factor $X_h$ ($h$ bits), the $\Phi_{2h}$ integer component, or the full register? This fixes the memory load and the clock contract. | RECOG, with RRF |
| BR-Q4 | Is $C_n$ physical gauge or a representation-level involution? Is $F_n$ a physical event succession? | OFN (SG-OFN-PRESENTATION, OPEN-OFN-7), RRF OPEN-A |
| BR-Q5 | What carries the retained record $p$ and the shared reference: internal dyad memory, a second dyad, or a new endpoint? | OFN; Triadic for any endpoint reading |
| BR-Q6 | A bridge from the $n=3$ linear six-cycle to the nonlinear DYAD map must name which observables factor through it and supply $\sin$, shear, $\mu$ and amplitude change. | DYAD, RECOG |
| BR-Q7 | Which refinement maps, topology and clock contract (circle, $\mathbb Z_2$, solenoid) does a physical continuum use? | OFN |
| BR-Q8 | Which law, if any, moves states between amplitude sectors? $F$ and replication do not. | Node Foundations / OFN |

Already answered for RRF: covariant quantities are admissible in principle (RRF §4.2 typed covariance); the question is the specific observable/action/domain/reference contract.

## 8. Evidence and sources

### 8.1 Consolidated check script (this session)

`evidence/ofn/binary_recognition/scripts/binary_recognition_wrapup_checks.py` — standard library only, exact integer polynomial arithmetic modulo cyclotomic polynomials; no floating point decides a predicate.

- Output: `evidence/ofn/binary_recognition/wrapup/binary_recognition_wrapup_checks.json`
- Command (from `evidence/ofn/binary_recognition/scripts/`): `python binary_recognition_wrapup_checks.py --out ../wrapup/binary_recognition_wrapup_checks.json` — rerun reproduces the stored output byte-for-byte.
- Result: **PASS, 403/403**, exit 0 (EV-RUN, 25 Oct 2026, ~4 s).
- Negative controls (`--control <name>`), each exit 1: `zero-equals-short-for-all-n`, `sector-injective-only-at-powers-of-two`, `parity-needs-original-component`.
- SHA-256 script: `d4e540deb7107b28b51fe4cb88bebf4e8ce975c972bd79f4a470b8545496f6d3`
- SHA-256 output: `3b9843083a9407cc1d8edb73d03198f3ee5004c6330508624b4bd59c308f2257`

Coverage: C1 two-bit classification; C2 Gaussian representation and role reversal; C3 parity, gauge type, affine uniqueness ($n\le10$), all-readout $C$-type ($n\le4$ exhaustive); C4 three-bit orbits and DYAD linear bridge; C5 full-cube descent ($n\le12$), $K$-witnesses ($n\le60$); C6 Zero/Short exhaustive ($n\le16$), radical-stripping counts, $n=30,45$ witnesses; C7 sector injectivity ($n\le14$); C8 parity-component theorem over all component subsets ($n\le12$), mod-2 uniqueness ($n\le64$); C9 folding factor, periods, descent through $Z_n$ ($n\le14$); C10 replication ($n\le6$, $k\le5$).

This is one implementation, written in this session; it is not independent of the reviews that produced the theorems. The unbounded theorems rest on the written proofs in the source notes (§8.2); the script is a finite regression.

### 8.2 Source notes of the thread (EV-BYTES; not yet in the repository)

Received in session, read in full. Hashes of the bytes as received:

| File | SHA-256 |
|---|---|
| `NODE_BINARY_TO_ANGULAR_PRELIMINARY_v0_1.md` | `1287e7a89bd9edae9a7500c243af096c05585801992af5c04212163ac9f760ef` |
| `NODE_BINARY_TO_ANGULAR_REVIEW_ADDENDUM_v0_1_1.md` | `3e2bed9303acfed02c8480fbe2792e5f13482bf5a65c45bfd0c8e5ef46cc480d` |
| `NODE_PARITY_DUALITY_CYCLOTOMY_ADDENDUM_v0_1_2.md` | `ce54560789ca986c6a269f0f8ca0843ee4587c9cb6d9976e66f44d500fbde7bf` |
| `NODE_PARITY_DESCENT_AMPLITUDE_ADDENDUM_v0_1_3.md` | `ba43577e7866d335f6c915ffdc6fab8eed57920cf0cc838b6d384e819c18a829` |
| `NODE_REFINEMENT_ZERO_FIBRE_ADDENDUM_v0_1_4.md` | `82fbeb74b115302d14d9251d35718470e5342e05d46c87a6b83c47ddce9d3593` |
| `NODE_ZERO_FIBRE_CLASSIFICATION_v0_1_5.md` | `8b9a37d959d3f9232346d9812e022e18e2ff27dcce1bbc7c18c8b905fd4e61fc` |
| `NODE_NONZERO_SECTOR_INJECTIVITY_v0_1_6.md` | `1f1e6deb4e22ee373c34b78bcfd4d1d4c72b6fa861f61276510cf8f17063e790` |
| `PARITY_PRIMARY_COMPONENT_FOLDING_ADDENDUM_v0_2.md` | `6bb6c2ed934d81a4de5c9e381923c95d1109f6c8b87c99b3af27d525940e5fde` |
| `review_exact_checks.json` (v0.1.1, 79 checks) | `587510b7f4075bf691cb12e5b1fe3f369fb0f768cf2fe183c9927235207f4dbb` |
| `parity_duality_cyclotomy_checks.json` (v0.1.2, 203) | `22c885089062aa512aaf9e58ea335838ccb60e5d9bb5f89f87b4ecf9b2380145` |
| `parity_amplitude_checks.json` (v0.1.3, 509) | `68c4aab909a4162b2e44cef89152b47ca402f58874d399b9602c3d9c862b6498` |
| `refinement_zero_fibre_checks.json` (v0.1.4, 727) | `d397f750abfebf1d2b3e7d9139fca9cb104f233634286a872bc4128091d3e2b8` |
| `zero_short_classification_checks.json` (v0.1.5, 535) | `a6c7381fa764474ce8a2962f54dc4e5eca347bdc841af90fda837c76f688a700` |
| `sector_injectivity_checks.json` (v0.1.6, 1,106) | `13c92d1d1c192fcc4d55be05f51b570fedb56092a932bf478a0553e8738147cd` |
| `NODE_BINARY_TO_ANGULAR_v0_1_4.zip` (scripts, manifests, nested v0.1.3 package) | `7c96c88e31968918ba0a2ab308edbcc041474ae21a08efcfd0a216078cad8bd5` |

**Not available to this session** (EV-SRC-REPORTED only): the v0.1.5 and v0.1.6 packages and their scripts (reported 535 + 180 and 1,106 + 424 checks); `HANDOFF_RECOG_RRF.md`; `HANDOFF_RECOG_RRF_CLARIFIED_v0_1.md`; `NODE_RECOG_RRF_HANDOFF_APPENDIX_v0_1.md` and its 205-check record; the RECOG co-owner review "Boolean Folding and Recognition Contract". Their contents are cited here only as summarized in session messages; no hash is given for them.

### 8.3 External mathematics (cited by the producing session; EV-SRC-REPORTED)

T. Y. Lam, K. H. Leung, *On Vanishing Sums of Roots of Unity*, J. Algebra 224 (2000) 91–109, arXiv:math/9511209 (Example 2.5, Theorems 3.1/3.3; context only). J. Baez, AMS Visual Insight "2-adic integers" (2014) and diary 12 Nov 2017 (solenoid). M. Cruz-López, A. Verjovsky, arXiv:1308.1853 (solenoidal groups). K. Conrad, *The Character Group of Q*. LMFDB number field 4.0.256.1. W. Stein, *Algebraic Number Theory, a Computational Approach*, §8.1. mathlib `Polynomial.cyclotomic_eq_minpoly_rat`. Gullerud–Mbirika, arXiv:1902.03483 (Eisenstein units). Texas Instruments CD4017B (Johnson counter terminology only).

## 9. Suggested repository steps (PI)

1. Upload the §8.2 files unchanged on an `upload/binary-recognition` branch; hash-check against §8.2; place under `evidence/ofn/binary_recognition/sources/`.
2. If available on the PI's machine, upload the v0.1.5, v0.1.6 and handoff packages the same way; then §8.2 "not available" shrinks.
3. Decide placement of this note (`records/ofn/` or `records/recog/`).
4. Route BR-Q1–BR-Q3 to RECOG/RRF and BR-Q4/BR-Q5/BR-Q7 to OFN as notices. No owner DSN changes are implied by this note.
5. Atlas: if the atlas owner wants rows, §4 and §3F are the current-state content; §6 stays here.
