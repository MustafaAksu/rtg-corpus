# OFN working note — closure constraint versus reference removal (OPEN-OFN-REF-CLOSURE)

**Status:** Noncanonical working note of the OFN co-owners, at SESSION level. It changes no DSN text, RID, definition or OPEN status. It supplies the "explicit comparison construction" that OPEN-OFN-REF-CLOSURE names as its next artifact.
**Date:** 30 October 2026.
**Authors:** Claude (OFN co-owner session `claude012ZC8x`), drafting. ChatGPT (OFN co-owner) proposed the topic and fixed the separation of node-origin gauge, lossless edge parametrization and node/edge actions used below (co-owner exchange of 30 October 2026, relayed by the PI).
**Review:** `records/ofn/OFN_REF_CLOSURE_CHATGPT_REVIEW.md` (PR #122 review `5710046981`): ACCEPT SCOPED for R1–R5. Its two findings are applied in this revision:
- R122-S1: the criterion concerns the specified global map $\kappa_n$, not every isomorphism of the spaces, and not local invertibility on $U(1)$.
- R122-S2: the $SO(d)$ count is configuration-dependent.

The review's scope clean-ups (R1 holds for general connected graphs; the holonomy-loss statement is for $C_n$) are applied too. The script is unchanged, so its hashes stand.
**Governing sources:** `ofn-v0.11` §2.4 (build-sequence row for $K_3$; `[HYP]` reference-consumption reading) and §9 OPEN-OFN-REF-CLOSURE. Its closure criterion: "Define both spaces, equivalence relations and maps, then prove or disprove the claimed identification in a stated model; matching counts alone are insufficient."
**Evidence:** `evidence/ofn/scripts/ofn_ref_closure_check.py` (SHA-256 `4c469b4143733e2f240e76bba7d93f562f7183ee33bd54f004771ba1b4340402`). Command: `python3 -I evidence/ofn/scripts/ofn_ref_closure_check.py`; it exits 0 only if all nine checks pass. Outputs, from Python 3.13 and SymPy 1.14.0:
- positive run: `evidence/ofn/ref_closure/ofn_ref_closure_check_output.txt` (`40bf3f52bac0029fc6e3a522a61ae571bf8be2ec95fd9464258ee0dd2582cf13`);
- forced-failure control (`--force-fail`, exit 1): `…/ofn_ref_closure_check_forced_fail_output.txt` (`eb10f5aff22c3724e83e043d1c9015e4e5547790fa7222b379f10067a849f028`).

## 1. Stated model

**Carrier.** An abelian group $H$, written additively. The examples are $\mathbb R^d$ (vector differences), $U(1)=\mathbb R/\mathbb Z$ (phases), $\mathbb Z_N$ (discrete phases) and $\mathbb Z$ (lifted integer advances). Which carrier a branch uses is a branch-local declaration (the OPEN's dependency "branch-local edge/mode conventions"); the note does not choose one.

**Graph.** $G=(V,E)$ is connected, with oriented edges. For the cycle graph $C_n$ ($K_3=C_3$), the orientation is coherent around the cycle. One directedness and closure convention is used throughout, as OPEN-OFN-3A requires.

**Spaces and maps:**

| Object | Definition |
|---|---|
| node differences | $d:H^V\to H^E$, $(ds)_{ij}=s_i-s_j$ |
| $Q_{\rm node}$ | $H^V/H_{\rm diag}$ — quotient by the common node origin (diagonal node action $s_i\mapsto s_i+c$) |
| $C_0$ (closure sector) | $\{r\in H^E:$ the oriented sum around every cycle is $0\}$ — "edge-closure reduction" is the passage to $C_0$ |
| $Q_{\rm edge}$ | $H^E/H^E_{\rm diag}$ — edges measured relative to one another, i.e. one relation used as the reference (diagonal edge action $r_e\mapsto r_e+c$) |
| $\kappa_n$ | on $C_n$, the composite $C_0\hookrightarrow H^E\twoheadrightarrow Q_{\rm edge}$ |

"Removal of one relational reference" is not defined in OFN. The note compares the three precise readings (a)–(c) of §3.

## 2. Results

**R1 — closure sector = node differences modulo the common origin** `[THM]` (standard mathematics; the scope is the stated model). For connected $G$ and abelian $H$, $d$ induces a group isomorphism $Q_{\rm node}\xrightarrow{\ \cong\ }C_0$.

*Proof.*
- **Kernel.** $\ker d$ consists of the constant node assignments, because $G$ is connected.
- **Image inside $C_0$.** $d(H^V)\subseteq C_0$, since sums around a cycle telescope.
- **Onto $C_0$.** Given $r\in C_0$, fix a spanning tree and a root with $s=0$, and integrate $r$ along tree paths. Then $ds$ agrees with $r$ on tree edges. On a non-tree edge they also agree, because both have zero sum around that edge's fundamental cycle.

Script R1 checks this exhaustively for $K_3$, $C_4$ and $K_4$ over $\mathbb Z_N$, $N=2,\dots,7$.

**R2 — forgetting one edge is a lossless parametrization of $C_0$, not a reduction** `[THM]` (standard; stated on $C_n$). On $C_n$, the map $C_0\to H^{E\setminus\{e_0\}}$ is bijective, with inverse $r_{e_0}=-\sum_{e\ne e_0}r_e$. On all of $H^E$ it is not injective: its kernel $\{(0,\dots,0,h)\}\cong H$ is carried isomorphically by the cycle sum (holonomy).

Moreover $Q_{\rm node}$ depends only on $V$. So on any graph, in the node-difference sector, deleting an edge that keeps $G$ connected changes nothing (R1; script R2 checks $C_n$). Connectivity must be kept: otherwise the node-difference description changes.

**R3 — closure reduction versus one relation as reference** `[THM]` (exact; elementary). On $C_n$,
$$\ker\kappa_n\cong H[n]=\{c\in H:\ nc=0\},\qquad \operatorname{coker}\kappa_n\cong H/nH .$$
Hence $\kappa_n$ is an isomorphism if and only if multiplication by $n$ is bijective on $H$.

**Scope of R3.** The criterion is for the specified global comparison $\kappa_n$: inclusion followed by the quotient, i.e. taking the diagonal class of the closed tuple itself. It does not exclude other isomorphisms. Choosing an edge always gives $C_0\cong H^{n-1}\cong Q_{\rm edge}$; for $K_3$, for example, $\alpha(a,b,-a-b)=[(a,b,0)]$ works for every abelian $H$, including $\mathbb Z$, $U(1)$ and $\mathbb Z_N$ with $3\mid N$. But $\alpha\ne\kappa_3$: it depends on the chosen edge, and it implies no physical equivalence.

Nor does R3 exclude local invertibility. On $U(1)$, $\kappa_3$ is globally 3-to-1, yet in small lifted coordinates $D\kappa_3=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ with $\det=3$, so it is a local diffeomorphism. The global torsion obstruction does not exclude a local phase-chart identification.

*Proof.*
- **Kernel.** $r\in C_0$ lies in $H^E_{\rm diag}$ exactly when $r=(c,\dots,c)$ with $nc=0$.
- **Cokernel.** A class $[r]\in Q_{\rm edge}$ has a representative in $C_0$ if and only if $\sum_e(r_e-c)=0$ for some $c$, i.e. $\sum_e r_e\in nH$. So $[r]\mapsto\sum_er_e \bmod nH$ identifies the cokernel with $H/nH$.

For $K_3$ ($n=3$):

| Carrier | $\kappa_3$ |
|---|---|
| $\mathbb R^d$ | isomorphism. In coordinates the scalar edge-index block is $I+J$ with $\det=3$; the full matrix on $(\mathbb R^d)^2$ has $\det=3^d$ (script R3b, also $n=4,5$) |
| $U(1)$ | surjective, 3-to-1; kernel $\{(0,0,0),(\tfrac13,\tfrac13,\tfrac13),(\tfrac23,\tfrac23,\tfrac23)\}$ (script R3c) |
| $\mathbb Z_N$ | isomorphism iff $\gcd(3,N)=1$; kernel and cokernel of order $\gcd(3,N)$ (script R3a, $n=3,4$, $N=2,\dots,12$) |
| $\mathbb Z$ | injective, not surjective; cokernel $\mathbb Z/3$ (directly from R3; not enumerated) |

**R4 — node action and edge action are different actions** `[THM]` (exact). The diagonal node action fixes every edge value. On $C_n$, the diagonal edge action by $c$ preserves $C_0$ if and only if $nc=0$; for $U(1)$ and $n=3$ that means only the cube roots of unity. The common node phase rotation of a $U(1)$ carrier is therefore not the same as rotating the relations together, although both carry the name "$U(1)$ rotation" (script R4).

**R5 — counts agree where the identification fails** (control). On $K_3$, $|Q_{\rm node}|=|C_0|=|Q_{\rm edge}|=N^2$ for every $N$, yet $\kappa_3$ is not bijective for $N\in\{3,6,9,12\}$ (script R5). This is the closure criterion's warning, "matching counts alone are insufficient", in an explicit instance.

## 3. Answer at the stated scope

Is edge-closure reduction (passage to $C_0$) the same construction as removal of one relational reference? It depends on which reference is meant:

| Reading of "removing one reference" | Relation to closure reduction |
|---|---|
| **(a) Fix the common node origin** ($Q_{\rm node}$) | The same construction, canonically, for every abelian carrier and connected graph (R1). This reference is the node origin, not a relation |
| **(b) Delete one relation** | On node-difference data: no change while $G$ stays connected, and forgetting the edge's value is a lossless parametrization of $C_0$ (R2). On independent edge data on $C_n$: deletion loses exactly the holonomy, while closure imposes it as a constraint; these are different operations. On a graph with several cycles, the other cycles' data remain |
| **(c) Use one relation as the reference** ($Q_{\rm edge}$) | The specified global comparison $\kappa_n$ is an isomorphism if and only if multiplication by $n$ is bijective on the carrier (R3). For $K_3$: yes over $\mathbb R^d$; no over $U(1)$ (3-to-1 globally, a local diffeomorphism), over $\mathbb Z_N$ with $3\mid N$, or over $\mathbb Z$. Edge-dependent isomorphisms such as $\alpha$ exist in every case but are a different comparison |

A geometric rotational reference — the diagonal $SO(d)$ on $\mathbb R^d$ node vectors for $d\ge2$ — is yet another action. The number of dimensions it removes depends on the configuration stratum: $\dim SO(d)-\dim\operatorname{Stab}$. For a non-collinear triangle, after translations, the stabilizer of the two relative vectors is $SO(d-2)$, so the orbit has dimension $2d-3$ (1, 3, 5 for $d=2,3,4$). Collinear and null configurations have other stabilizers. This action is not analysed further here.

**Consequence for the `[HYP]` of §2.4.** The reduction "three node-difference edges minus one closure relation" equals reading (a) always. The specified comparison $\kappa_3$ with reading (c) is an isomorphism only on carriers where multiplication by 3 is bijective. Whether any of these is the *physical* "reference consumption" meant by the HYP is not decided by the mathematics. None of the maps above is a physical process.

## 4. What remains open, and a possible disposition

- **Physical reading.** Whether "spending one relation as a rotational reference" has a physical meaning, and which of (a)–(c), if any, it is. This stays with the `[HYP]` and OFN's ontology.
- **Carrier declaration.** Each branch that uses the counting argument must declare its carrier. On $U(1)$, $\mathbb Z_N$ with $3\mid N$, or $\mathbb Z$, the global comparison $\kappa_3$ is not an isomorphism (other, edge-dependent isomorphisms exist).
- **Out of scope:** non-abelian carriers (holonomy as conjugacy class) are outside this note. Graphs with cycles of different lengths and orientations are outside the R3/R4 comparison only; R1 covers every connected graph, including $K_4$.
- **Possible disposition (for the co-owners, not decided here).** The note answers the OPEN's mathematical question in the stated model: (a) is proved, (b) is a parametrization, and the specified comparison (c) gets an exact torsion/divisibility criterion. A later OFN edition could record R1–R4 as an OFN-local `[ALG]`/`[THM]` result and narrow OPEN-OFN-REF-CLOSURE to its physical reading, or close it at mathematical scope with the HYP kept open. Any status change needs a stage-1 build, review and PI adoption. Notify targets, if a disposition is made: TRIAD, GEN, OPEN-OFN-3C.

## 5. What this note does not do

- It does not change §2.4, the HYP, OPEN-OFN-REF-CLOSURE's status, OPEN-OFN-3C or any RID.
- It does not select a carrier or a physical reading of "reference".
- It does not treat the finite enumerations as proofs beyond their stated range. R1–R4 rest on the stated proofs, and the enumerations are checks of them.
