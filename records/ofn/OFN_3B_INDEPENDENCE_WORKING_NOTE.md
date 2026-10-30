# OFN working note — what "independently specified $T_3$" requires (OPEN-OFN-3B)

**Status:** Noncanonical working note of the OFN co-owners, SESSION level. It changes no DSN text, RID, definition or OPEN status, and it does not define "independent" for OFN. It makes the independence obligation of OPEN-OFN-3B measurable and records where class C stands on each axis. No primacy conclusion follows (SG-OFN-PRIMACY).
**Date:** 30 October 2026.
**Authors:** Claude (OFN co-owner session `claude012ZC8x`) drafted the note. ChatGPT (OFN co-owner) split uniformity into U-form and U-class, split the carrier axis into C0 and C1, asked for representation-typed membership tests, and proposed the information-test table and the decision matrix (co-owner exchange of 30 October 2026, relayed by the PI). Change-focused review pending.
**Governing sources:**
- `ofn-v0.11` §8: `RTG-OFN-DEF-REDUCTION-TARGET` asks for an "independently motivated model class" and excludes "a trivial extension made by inserting the chosen $T$ as a factor".
- `ofn-v0.11` §9: OPEN-OFN-3B and its reconciliation input on class C.
- `ofn-v0.11` §5.5.3–§5.5.4: class C, the narrow-Q6 corollary and `RTG-OFN-ALG-RAW-STANDARD-C-NOGO`.
- `dyad-v6.4.22` §1: `DYAD-DEF-PRIMITIVE-MAP`.

**Evidence:**
- Script: `evidence/ofn/scripts/ofn_3b_independence_check.py` (SHA-256 `6b50baa8dec7cacfa9d57dc257e7b4dfc2b06ae485e61ab129c6b7f7e0db2152`). Command: `python3 -I evidence/ofn/scripts/ofn_3b_independence_check.py`. It exits 0 only if all seven checks pass. Python 3.13, SymPy 1.14.0.
- Positive run: `evidence/ofn/independence_3b/ofn_3b_independence_check_output.txt` (`5a3ae8cd41ea946d21f27130bee1be5d9dcb6f3725776889e3196a2410225ca0`).
- Forced-failure control (`--force-fail`, exit 1): `…/ofn_3b_independence_check_forced_fail_output.txt` (`2fd85e7d005ebdc0fe1a25b01802a2076fa8edd4ebf0e6fea89d2cfa1c9868d7`).

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

**K4 — falsifier.** For $G(x)=x+q(x)$ with $q$ a nonzero quadratic, both $\iota_0$ and $\iota_+$ fail. The symmetry hypotheses are doing real work.

**K5 — owner premise and implication** `[ALG]`. If $GA=AG$, then $A^3=-I$ gives oddness and $A^2$-equivariance follows. So $\mathcal G_A\subseteq\mathcal G_{\rm odd}\cap\mathcal G_\omega$.

The premise for C2 is the owner theorem $[N_\Phi,A]=0$ (IMP-O10-07); for $N_{\rm formal}$ it is the owner's formal commutation (IMP-O10-03). Neither theorem is re-proved here. The script checks the implication on an $A$-averaged generic jet.

**K6 — raw $T$ is in none of these classes, in the raw chart** `[ALG]` (exact at order 2).
$$T(-x)+T(x)=(0,\ \rho^2)+O(|x|^3).$$
So $T\notin\mathcal G_{\rm odd}$. The script also finds non-zero order-2 residuals for $TA-AT$ and for $T A^2-A^2T$. The source is the quadratic term of $e^\rho-1$.

**K7 — consequence for the named raw embedding.** In the raw chart, $\iota_0$ is not invariant under $T_3[T]$ for $\kappa\ne0$. After one step the third edge is $(0,-\kappa\rho^2/3)+O(|x|^3)$. Only this embedding is tested here; the general raw statement is the owner no-go `RTG-OFN-ALG-RAW-STANDARD-C-NOGO`.

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
| **C1 — target-derived representation** | Does an embedding exist once $T$-derived structure ($\Phi$, $J$, $A$) is used? | **PASS, $T$-relative.** $\Phi=\tfrac16\sum_{k=0}^5A^{-k}J^k$, with $J$ the identity-tangent sixth root built from $T$ ($J=T\circ F^{-1/6}$, $F=T^6$), is built from $T$ (IMP-O10-06/07) |
| **J — justification** | Is the coupling form $P_\kappa$ (mean feedback), the value of κ and the carrier justified without presupposing the $T$ to be recovered? | **OPEN.** The form is inherited from Genesis §6.3c / RRF §6.2a; no OFN-side selection principle is recorded |
| Reduction witness | Is $T_3\circ\iota=\iota\circ N$ exact on an invariant submanifold? | **PASS in class C** (owner lock surfaces) |
| Primacy implication | — | **NONE** (SG-OFN-PRIMACY; the 3B owner guard) |

**Information test — what class C yields beyond what was built in.** This is evidence that the construction is not tautologically empty. It is not a solution of J.

| Kind | Example (owner text, `ofn-v0.11` §5.5) | Value for 3B |
|---|---|---|
| By construction | Invariant dyad recovery on the lock surfaces | Not independent confirmation |
| Structural consequence | Defect evolves by $(1-\kappa)\sum N$ off the surfaces (Q4 capacity); closure-mode modulus $\lvert1-\kappa\rvert$ | An additional consequence of the construction |
| Nontrivial exclusion | Narrow-Q6: no local $C^3$ conjugacy to a product of planar edge maps | Not three independent dyads rewritten. **Scope:** only the stated $C^3$ planar-product decompositions; other hidden factorizations are not excluded |
| Derived dynamics | Six-step cubic on the centre manifold, independent of κ, chiral coefficients $p=\mu/3$, $q=2\mu/3$ | Content not put into the recipe by hand |
| Physical justification | Why $P_\kappa$, why this κ, why this carrier | OPEN |

## 4. What this makes measurable for 3B

| Candidate standard | Requirement | Class C |
|---|---|---|
| (a) Weakest | U-form + C1 + reduction witness | meets |
| (b) Middle | adds U-class without nonlinear $T$-data, and C0 in some declared carrier | partly meets |
| (c) Strong | adds J | does not meet (J OPEN) |

The OPEN asks for an "independently motivated model class", which points at least to (b) and arguably (c). Choosing among (a)–(c) is an OFN co-owner decision with PI adoption. This note does not make it.

What a technical owner would need to supply:
- **For (b):** a $T_3$ on a declared carrier in which the embedding holds without a $T$-derived rechart, or with a class whose definition uses at most the linear data $A$. Alternatively, a class-scoped nonexistence result.
- **For (c):** in addition, an argument for the coupling form that does not use recovery of $T$.

## 5. What this note does not do

- It does not change §8, `RTG-OFN-DEF-REDUCTION-TARGET`, OPEN-OFN-3B's status, Q6 or any RID.
- It does not choose (a), (b) or (c).
- It does not re-prove the owner commutation $[N_\Phi,A]=0$ (K5 uses it as a premise).
- It does not extend the raw no-go beyond its owner scope; K7 tests one named embedding.
- It does not treat finite jets as proofs. K2, K3 and K5 rest on the stated identities; K6 and K7 are exact order-2 residuals of the actual $T$.
- It draws no primacy conclusion.
