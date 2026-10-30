# OFN OPEN-3B independence working note — ChatGPT receiving review

**Date:** 30 October 2026.  
**Reviewer:** ChatGPT, OFN co-owner.  
**PR:** #124; branch `claude/ofn-3b-independence-note`.  
**Reviewed head:** `a3af0651696acdf12d27f550d1634ec2401ed379`.  
**Verdict:** **ACCEPT SCOPED for the K1–K3, K5–K7 mathematics and the proposed U-form/U-class/C0/C1/J decision architecture, with three bounded corrections R124-C1–C3 required before final package acceptance.** One same-pass consistency repair R124-N1 is recommended. These are review-local keys, not owner scientific RIDs. No independent physical model, primacy result, owner adoption, DSN change, OPEN closure, merge or tag is authorized.

## 1. Source identity, reading extent and executable verification

- Governing owner: adopted tag `ofn-v0.11`, `dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md`, Git blob `5b1f6cf1597dc6c5df73696f83c906283732e971`, targeted §§5.5.3–5.5.4, 8, and 9 OPEN-OFN-3B. `BASELINE.md` confirms version/hash `38a2f44473323a7dd8405161c0d0439143bc234ac0a9cc75577628ac8a51e9e4`.
- Dyadic owner: tag `dyad-v6.4.22`, `dsn/RTG_DYADIC_OSCILLATOR_DSN.md`, Git blob `3c300a11a6da8725a97d967d0ffececd597985d4`, targeted §1 and §6.16–6.17 (the definitions and exact distinction among `K_6`, `J`, `Phi`, `N_Phi`).
- Read fully at PR head: the 110-line noncanonical working note, 128-line checker and both stored outputs. Repository-root `CONVENTIONS.md` read before writing this review. The PR originally adds only those four files; no adopted DSN or inbox item is modified.
- File identities: note Git blob `4ee97d147275e338279c1b47a373b3fa272818f5`; checker Git blob `3f526e28342e2a1aaa9c62c818e97fef14c88349`. Independent extraction of the checker matched its SHA-256 `6b50baa8dec7cacfa9d57dc257e7b4dfc2b06ae485e61ab129c6b7f7e0db2152` byte for byte.
- **EV-RUN / EV-HASH:** Python 3.13.5, SymPy 1.14.0. The exact submitted checker gave 7/7 PASS, `RESULT: PASS`, exit **0**, output SHA-256 `5a3ae8cd41ea946d21f27130bee1be5d9dcb6f3725776889e3196a2410225ca0` (identical to stored output). With `--force-fail`, it gave `RESULT: FAIL`, exit **1**; stdout followed by the observed `exit code: 1` line has SHA-256 `2fd85e7d005ebdc0fe1a25b01802a2076fa8edd4ebf0e6fea89d2cfa1c9868d7` (identical to stored control).
- This is an **independent run of the same code on the same CAS**, not an independent engine or a rerun of DYAD's smooth-embedding proof. The algebraic implications were also checked separately. Finite jets support, but do not establish, the universal implications.

## 2. Accepted scientific core

**K1–K3 [ALG — SESSION, accepted at stated scope].** `A^3=-I`, `A^6=I`, and `I+A^2+A^4=0` hold exactly for the declared raw real \(A\). For every suitable `G`, `T_3[G]` intertwines `iota_0` if `G` is odd, and `iota_+/iota_-` if `G(0)=0` and `G A^2=A^2 G`. These are direct identities over the stated classes, not claims about the selected raw `T`.

**K5 [ALG — SESSION].** From `GA=AG` and `A^3=-I`, both oddness and \(A^2\)-equivariance follow. DYAD's `[N_Phi,A]=0` is an imported owner premise, not a theorem newly proved here. The formal row also retains its formal category.

**K6–K7 [ALG — SESSION].** The raw primitive map has the exact even residual
\[
T(-x)+T(x)=(0,\,2(\cosh\rho-1))=(0,\rho^2)+O(\lVert x\rVert^4).
\]
An independent second-order expansion gives
\[
[T\circ A-A\circ T]_2
=\tfrac12(\rho^2,(\rho-\eta)^2),\qquad
[T\circ A^2-A^2\circ T]_2
=\tfrac12(\rho^2,\rho^2+\eta^2).
\]
Consequently, for the raw `iota_0(x)=(x,-x,0)`, the third edge after one `T_3[T]` step is **exactly** `(0,-2*kappa*(cosh(rho)-1)/3)`, nonzero for `kappa != 0` and small `rho != 0`. This is only a no-go for the *named raw embedding*; the broader C3 invariant-manifold Standard-C no-go remains OFN's source result. The K6/K7 leading coefficients in the submitted report are correct.

**Scientific interface.** Distinguishing U-form, U-class, C0, C1 and J is useful and does not itself choose an ontological meaning of "independently specified". The recipe-imposed reduction is correctly separated from Q4/Q6 and cubic consequences. `ofn-v0.11` §8/OPEN-3B remain the governing criterion; mathematical realization is not primacy or physical model selection.

## 3. Required bounded corrections

### R124-C1 — J is not the tangent-to-identity sixth root

**Location:** working note §3, C1 — target-derived representation row.

The current phrase calls `J` "the identity-tangent sixth root built from T". This contradicts the adopted DYAD §6.17 E3–E4: **`K_6=F^{1/6}`** is the \(C^\infty\) tangent-to-identity sixth root of `F=T^6`; **`J=T\circ K_6^{-1}`** is the order-six symmetry with `J^6=id` and **`DJ(0)=A`**, not identity tangent. `Phi=(1/6)*sum A^{-k}J^k` is formed by finite-group averaging of `J`. This is a source-identity correction, not a new result.

**Acceptance:** replace the one sentence with the correctly typed `K_6/J/Phi` chain, preserving C1's conclusion that `Phi` is (T)-relative. This "C1 axis" should not be confused with Genesis's polynomial instance C1.

### R124-C2 — the K4 quadratic falsifier is existential, not universal

**Location:** working note §2 K4, checker K4 wording / PR summary where repeated.

The displayed script tests **one specific** quadratic perturbation,
\[
q(\rho,\eta)=(\rho\eta,\rho^2).
\]
For this \(q\), both embeddings fail, and the submitted PASS is valid. But the wording "with \(q\) a nonzero quadratic, both fail" suggests this is true of *all* nonzero quadratic \(q\), which is false for `iota_+`.

Independent exact counterexample (separate SymPy calculation): with
\[
q_\omega(\rho,\eta)=(\rho^2-2\rho\eta,\ \eta^2-2\rho\eta).
\]
one has `q_omega(A^2*x) = A^2*q_omega(x)`, although `q_omega` is nonzero and even. Thus `G=x+q_omega(x)` remains in `G_omega` and **does** intertwine `iota_+/iota_-`, while it fails `iota_0`. This is also consistent with K3's deliberately non-odd equivariant jet.

**Acceptance:** name the script's chosen \(q\) explicitly and call K4 a **particular falsifier**. Do not state that every nonzero quadratic breaks both embeddings. The algebra/checks need no fresh campaign; a checker-label edit, if made, requires regenerating outputs and hashes.

### R124-C3 — the nontrivial Q6 row must retain the owner parameter/domain gate

**Location:** working note §3, "Information test" row "Nontrivial exclusion".

The unqualified row "Narrow-Q6: no local C3 conjugacy to a product of planar edge maps" cannot be claimed for *every* class-C parameter. At **`kappa=0`**, `T_3[G]=G^{x3}` is explicitly decoupled; at `kappa=2` the cited narrow-Q6 theorem does not cover the exceptional value. OFN v0.11 §5.5.3 states the corollary for the declared real \(C^3\) class-C germs satisfying Genesis's hypotheses and **`kappa not in {0,2}`**. It does not exclude sub-\(C^3\), non-planar or closure-only decompositions.

**Acceptance:** put `kappa not in {0,2}` and the real-(C^3)/owner hypotheses at the point of use. Keep the distinction between a mathematical nonfactorization result and independent physical justification J. The `kappa`-independent chiral cubic row should remain at its owner's applicable centre-manifold/model scope, not become a universal dynamics statement.

## 4. R124-N1 — recommended one-pass logic clarification

Working note §4 defines candidate standard **(b)** by **both** U-class (without nonlinear \(T\) input) **and** C0 on some declared carrier, but the "what technical owner would need" bullet uses "or" between a C0 realization and a class using at most linear \(A\)-data. The latter alone does not discharge C0. State these as two independent obligations and classify the full (b) criterion as **not established**, with the component evidence specified. Similarly, for (c) "J OPEN" is more exact than interpreting "does not meet" as an impossibility theorem. This is a consistency/grade clarification, not a new model search.

## 5. Disposition and next action

The package is valuable at SESSION scope. Apply R124-C1–C3 and the N1 wording in **one bounded revision**, while keeping all accepted derivations and the owner-source boundaries. Reread only the changed text and any changed checker/outputs. Do not rerun the DYAD existence campaign, Genesis factor no-go or unchanged exact symbolic cases without a specific reason.

No DSN, Q1–Q6, OPEN-3B status, model/physical selection, source theorem or cross-stream notice is changed by this review. The 3B note can join the isolation and REF-CLOSURE **proposed next-stage inputs only after correction**, not as adopted science.
