# OFN working note — what "independently specified $T_3$" requires (OPEN-OFN-3B)

**Status:** Noncanonical working note of the OFN co-owners, SESSION level. It changes no DSN text, RID, definition or OPEN status, and it does not define "independent" for OFN. It makes the independence obligation of OPEN-OFN-3B measurable and records where class C stands on each axis. No primacy conclusion follows (SG-OFN-PRIMACY).
**Date:** 30 October 2026.
**Authors:** Claude (OFN co-owner session `claude012ZC8x`) drafted the note. ChatGPT (OFN co-owner) split uniformity into U-form and U-class, split the carrier axis into C0 and C1, asked for representation-typed membership tests, and proposed the information-test table and the decision matrix (co-owner exchange of 30 October 2026, relayed by the PI).
**Review:** `records/ofn/OFN_3B_INDEPENDENCE_CHATGPT_REVIEW.md` (PR #124 review `5710527539`): ACCEPT SCOPED for K1–K3 and K5–K7 and for the axis framework. Applied in this revision:
- R124-C1: $J$ versus $K_6$.
- R124-C2: K4 limited to the tested $q$.
- R124-C3: the hypotheses of narrow-Q6.
- R124-N1: (b) is conjunctive, and J is "not shown".

The review's exact identity $T(-x)+T(x)=(0,2(\cosh\rho-1))$ is adopted in K6–K7. The script was edited for these scope statements and rerun, and its hashes are updated.
**Governing sources:**
- `ofn-v0.11` §8: `RTG-OFN-DEF-REDUCTION-TARGET` asks for an "independently motivated model class" and excludes "a trivial extension made by inserting the chosen $T$ as a factor".
- `ofn-v0.11` §9: OPEN-OFN-3B and its reconciliation input on class C.
- `ofn-v0.11` §5.5.3–§5.5.4: class C, the narrow-Q6 corollary and `RTG-OFN-ALG-RAW-STANDARD-C-NOGO`.
- `dyad-v6.4.22` §1: `DYAD-DEF-PRIMITIVE-MAP`.

**Evidence:**
- Script: `evidence/ofn/scripts/ofn_3b_independence_check.py` (SHA-256 `139f7934fe749b6b144811d0b6d9c6ebc2b6ce9a60ec21049f2c1c15d929cc70`). Command: `python3 -I evidence/ofn/scripts/ofn_3b_independence_check.py`. It exits 0 only if all seven checks pass. Python 3.13, SymPy 1.14.0.
- Positive run: `evidence/ofn/independence_3b/ofn_3b_independence_check_output.txt` (`bbdb5511c6d35d5da315774cc25a9a5d30c5564cde1139c260326aa5d6d60a00`).
- Forced-failure control (`--force-fail`, exit 1): `…/ofn_3b_independence_check_forced_fail_output.txt` (`88b8e9c69bd3d89750f6e2b5bcdca962750223556ddca7a1a7072eea51d078d8`).

## 1. Setting

**The two representations.**
- *Raw:* the lifted chart $x=(\rho,\eta)$ at $P_1$, with $T(\rho,\eta)=(\rho-\sin\eta,\ \eta+(e^\rho-1)-\sin\eta)$ and $A=DT(0)=\begin{pmatrix}1&-1\\1&0\end{pmatrix}$.
- *Transported:* the chart of `DYAD-THM-SMOOTH-EQUIVARIANT-CHART`, in which the edge law is $N_\Phi=\Phi T\Phi^{-1}$ (C2). $N_{\rm formal}$ is the formal normal form.

These are different presentations, and the class-C model is declared in the transported one (§5.5.4). Every membership statement below names its representation.

**The uniform recipe** (class-C form). For a single-edge law $G$:
$$T_3[G](x_1,x_2,x_3)_e=G(x_e)-\frac{\kappa}{3}\sum_jG(x_j).$$

**Embeddings.**
$$\iota_0(x)=(x,-x,0),\qquad \iota_\pm(x)=(x,A^{\pm2}x,A^{\pm4}x).$$
In the complex transported coordinate, $A^2$ is multiplication by $\omega$.

**Classes.**
- $\mathcal G_{\rm odd}=\{G: G(-x)=-G(x)\}$.
- $\mathcal G_\omega=\{G: G(0)=0,\ G(A^2x)=A^2G(x)\}$.
- $\mathcal G_A=\{G: GA=AG\}$.

## 2. Results

**K1–K3 — the recipe is uniform on the stated classes** `[ALG]` (exact; the jet checks are supporting).
- If $G\in\mathcal G_{\rm odd}$, then $\sum_jG(\iota_0(x)_j)=0$, hence $T_3[G]\circ\iota_0=\iota_0\circ G$.
- If $G\in\mathcal G_\omega$, then $\sum_jG(\iota_\pm(x)_j)=(I+A^2+A^4)G(x)=0$ (K1), hence $T_3[G]\circ\iota_\pm=\iota_\pm\circ G$.

The script checks both with generic jets: degree 5 for odd $G$, and degree 4 for $G\in\mathcal G_\omega$. The $\mathcal G_\omega$ jet is deliberately not odd, so oddness is not used for $\iota_\pm$.

**K4 — falsifier (specific).** For the tested quadratic $q(\rho,\eta)=(\rho\eta,\rho^2)$, $G=x+q$ breaks both $\iota_0$ and $\iota_+$. This shows the symmetry hypotheses are not vacuous. It does **not** mean that every nonzero quadratic breaks the chiral embeddings. An $A^2$-equivariant quadratic preserves $\iota_\pm$ although it is not odd: the reviewer's example $q_\omega(\rho,\eta)=(\rho^2-2\rho\eta,\ \eta^2-2\rho\eta)$ satisfies $q_\omega(A^2x)=A^2q_\omega(x)$ (verified locally), consistent with K3.

**K5 — owner premise and implication** `[ALG]`. If $GA=AG$, then $A^3=-I$ gives oddness and $A^2$-equivariance follows. So $\mathcal G_A\subseteq\mathcal G_{\rm odd}\cap\mathcal G_\omega$.

The premise for C2 is the owner theorem $[N_\Phi,A]=0$ (IMP-O10-07); for $N_{\rm formal}$ it is the owner's formal commutation (IMP-O10-03). Neither theorem is re-proved here. The script checks the implication on an $A$-averaged generic jet.

**K6 — raw $T$ is in none of these classes, in the raw chart** `[ALG]` (exact).
$$T(-x)+T(x)=\bigl(0,\ 2(\cosh\rho-1)\bigr)=(0,\ \rho^2)+O(|x|^4).$$
So $T\notin\mathcal G_{\rm odd}$. The script also finds non-zero order-2 residuals for $TA-AT$ and for $T A^2-A^2T$. The source is the even part of $e^\rho-1$.

**K7 — consequence for the named raw embedding.** In the raw chart, $\iota_0$ is not invariant under $T_3[T]$ for $\kappa\ne0$. After one step the third edge is exactly $\bigl(0,-\tfrac{2\kappa}{3}(\cosh\rho-1)\bigr)$. Only this embedding is tested here; the general raw statement is the owner no-go `RTG-OFN-ALG-RAW-STANDARD-C-NOGO`.

**Membership summary (representation-typed):**

| Law | Representation | $\mathcal G_{\rm odd}$ | $\mathcal G_\omega$ | Basis |
|---|---|---|---|---|
| $T$ | raw lifted chart | no | no | K6 |
| $N_\Phi=\Phi T\Phi^{-1}$ | transported $C^\infty$ chart | yes | yes | owner $[N_\Phi,A]=0$ + K5 |
| $N_{\rm formal}$ | formal normal form | yes | yes | owner formal commutation + K5 |

## 3. The independence axes and where class C stands

| Axis | Question | Class C |
|---|---|---|
| **U-form** | Is the formula $G\mapsto T_3[G]$ fixed in advance and valid on a whole class, without retuning to the particular $T$? | **PASS** (K2, K3). $P_\kappa$ itself refers to nothing in $T$ |
| **U-class** | Is the class defined without the nonlinear $T$? | **Split by embedding.** For $\iota_0$: $\mathcal G_{\rm odd}$ uses no $T$-data; only the vector structure of the chart is declared. For $\iota_\pm$ (the chiral pair): $\mathcal G_\omega$ uses $\omega=A^2$, $A=DT(0)$, so it is **relative to linear $T$-data**. That is a scoped dependence, not a defect |
| **C0 — direct-carrier realization** | Is there an embedding in the declared starting carrier with no $T$-derived rechart? | **FAIL for the named raw mean-feedback family under Standard C.** K6–K7 show this for $\iota_0$; the owner no-go covers smooth $C^3$ invariant manifold germs through 0 for every $\kappa\ne0$. **Scope:** the no-go concerns the named raw κ-family and Standard-C $C^3$ germs only. It does not exclude other carriers, other $T$-independent charts or other triadic laws |
| **C1 — target-derived representation** | Does an embedding exist once $T$-derived structure ($\Phi$, $J$, $A$) is used? | **PASS, $T$-relative.** $\Phi=\tfrac16\sum_{k=0}^5A^{-k}J^k$ is built from $T$ (IMP-O10-06/07). Here $K_6=F^{1/6}$ ($F=T^6$) is the identity-tangent sixth root, and $J=T\circ K_6^{-1}$ is the finite-order generator with $J^6=\mathrm{id}$ and $DJ(0)=A$ (`dyad-v6.4.22` §6.16–§6.17) |
| **J — justification** | Is the coupling form $P_\kappa$ (mean feedback), the value of κ and the carrier justified without presupposing the $T$ to be recovered? | **OPEN.** The form is inherited from Genesis §6.3c / RRF §6.2a; no OFN-side selection principle is recorded |
| Reduction witness | Is $T_3\circ\iota=\iota\circ N$ exact on an invariant submanifold? | **PASS in class C** (owner lock surfaces) |
| Primacy implication | — | **NONE** (SG-OFN-PRIMACY; the 3B owner guard) |

**Information test — what class C yields beyond what was built in.** This is evidence that the construction is not tautologically empty. It is not a solution of J.

| Kind | Example (owner text, `ofn-v0.11` §5.5) | Value for 3B |
|---|---|---|
| By construction | Invariant dyad recovery on the lock surfaces | Not independent confirmation |
| Structural consequence | Defect evolves by $(1-\kappa)\sum N$ off the surfaces (Q4 capacity); closure-mode modulus $\lvert1-\kappa\rvert$ | An additional consequence of the construction |
| Nontrivial exclusion | Narrow-Q6 (`RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT`): for real $C^3$ class-C germs under the hypotheses of `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` (instances C1 and C2, $\kappa\notin\{0,2\}$), no local $C^3$ conjugacy to a product of three planar maps | Not three independent dyads rewritten. **Scope:** only those germs, κ values and $C^3$ planar-product decompositions. Not covered: formal series as such, sub-$C^3$, non-planar or closure-mode-only factorizations; $\kappa=2$ is not a proved failure |
| Derived dynamics | Six-step cubic on the centre manifold, independent of κ, chiral coefficients $p=\mu/3$, $q=2\mu/3$ | Content not put into the recipe by hand |
| Physical justification | Why $P_\kappa$, why this κ, why this carrier | OPEN |

## 4. What this makes measurable for 3B

| Candidate standard | Requirement | Class C |
|---|---|---|
| (a) Weakest | U-form + C1 + reduction witness | meets |
| (b) Middle | adds U-class without nonlinear $T$-data, and C0 in some declared carrier | partly meets |
| (c) Strong | adds J | not shown (J OPEN) |

The OPEN asks for an "independently motivated model class", which points at least to (b) and arguably (c). Choosing among (a)–(c) is an OFN co-owner decision with PI adoption. This note does not make it.

What a technical owner would need to supply:
- **For (b):** a $T_3$ that meets both conditions: (i) the class is defined without nonlinear $T$-data (at most the linear data $A$), and (ii) the embedding holds in a declared carrier without a $T$-derived rechart (C0). Alternatively, a class-scoped nonexistence result.
- **For (c):** in addition, an argument for the coupling form that does not use recovery of $T$.

## 5. What this note does not do

- It does not change §8, `RTG-OFN-DEF-REDUCTION-TARGET`, OPEN-OFN-3B's status, Q6 or any RID.
- It does not choose (a), (b) or (c).
- It does not re-prove the owner commutation $[N_\Phi,A]=0$ (K5 uses it as a premise).
- It does not extend the raw no-go beyond its owner scope; K7 tests one named embedding.
- It does not treat finite jets as proofs. K2, K3 and K5 rest on the stated identities; K6 and K7 are exact identities of the actual $T$; the commutation residuals in K6 are exact at order 2.
- It draws no primacy conclusion.
