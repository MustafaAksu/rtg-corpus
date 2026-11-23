# Triadic F3: Birth-age surfaces, fifth-order contact, and cross-age observable separation

**9 October 2026 · [ALG] conditional Genesis analytic modal model · NONCANONICAL.**
Genesis owns the source map. Triadic tests effective-state representations; RER records conditional results. This is **not** a physical standalone-K3 law, a birth-event selection, or an assertion that age/memory is an independent state.

## 1. Frozen source contract

Let V=R² with `Q(r,e)=r²−re+e²` and `J_Q=(1/√3)[[1,−2],[2,−1]]`. Use one-time initialization `B_κ(s)=(s,C_κ(s))`, `C_κ(s)=κ Q(s) J_Q s` for fixed κ≠0, followed by the independent conditional analytic modal update

`N=(P⊗I₂)∘T_e^{×3}∘(E⊗I₂)`, `F=N^6`, with the same reprojection after **each** primitive step and `T_e(r,e)=(r−sin e,e+exp(r)−1−sin e)`.

No graph reclosure, healing, reset, age-conditional update or post-birth projector is inserted. The byte-pinned `G3,G4` source jet comes from the prior Triadic F3-reachable study, which in turn attributes the named model to Genesis. The jet identity with historical producer bytes is not freshly audited here.

Define for **fixed finite** n the surface `M_{κ,n} = F^n(B_κ(U_n))`. Near zero, `D F(0)=I4`, and `D B_κ` has rank two, so each fixed-n surface is locally an embedded 2-manifold. There is no claimed common uniform domain for all n.

## 2. [ALG] The graph residual propagates linearly in fixed birth age

At age 0, the child graph is `c=C_κ(s)`. The source jet gives its first nonzero **normal** defect after one six-step block, using the *current parent vector* as chart:

\[
R_κ(s)=-\frac{\sqrt3κ}{6}Q(s)^2s,\qquad
c_1(s)=C_κ(s)+R_κ(s)+O(\|s\|^6).
\]

To propagate, put `A₃(s)=G_{3,s}(s,0)`, `V₅(s)=[G_{3,c}(s,C_κ(s))]_{degree 5}`. For each fixed finite n, in **initial** parent chart `s₀`:

\[
s_n(s_0)=s_0+nA_3(s_0)+O(\|s_0\|^4),\qquad
c_n(s_0)=C_κ(s_0)+nV_5(s_0)+O(\|s_0\|^6).
\]

`C_κ(s_n)=C_κ(s₀)+n DC_κ(s₀)A₃(s₀)+O(‖s₀‖⁶)`. The current-parent inverse is identity plus order 3. Therefore for each fixed finite n

\[
\boxed{c_n(s)=C_κ(s)+nR_κ(s)+O_n(\|s\|^6).}
\]

The subscript n is essential: the remainders and neighborhood are not uniform in age. This uses the original source jet and the exact symmetry `F_c(s,0)=0`, not a new physical assumption.

## 3. [ALG] Near-origin intersection and contact

For fixed distinct finite `n,m`:

\[
\boxed{
c_n(s)-c_m(s)=-(n-m)\frac{\sqrt3κ}{6}Q(s)^2s+O_{n,m}(\|s\|^6).
}
\]

Because `Q(s)=(r−e/2)²+3e²/4` is positive definite, the fifth-order coefficient is nonzero at every nonzero s when `κ(n−m)≠0`. Analytic remainders are uniform in **direction** on a sufficiently small compact angular circle for each fixed pair. Hence there exists an age-pair-dependent neighborhood in which `M_{κ,n}∩M_{κ,m}={0}`. Every fixed-age sheet passes through and is tangent to `c=0` at origin, sharing the same cubic graph; their first transverse difference has homogeneous degree five.

This does **not** give a uniform disjointness radius over all ages, a global foliation or manifold structure for the countable union, or an autonomous two-dimensional factor. In particular, the closure of the union is not characterized.

## 4. [ALG] A scalar future witness for any fixed age pair

From the source cubic parent jet, linearized in the fifth-order child difference at equal current parent `s=(r,e)`, one gets for fixed finite n,m:

\[
\boxed{
s(FX_n(s))-s(FX_m(s))
=(n-m)\frac{κ^2Q(s)^4}{18}\binom{-r-2e}{2r-3e}+O_{n,m}(\|s\|^{10}).
}
\]

Contracting with `DQ(s)=(2r−e,2e−r)` and using `(-r−2e,2r−3e)·DQ(s)=-4Q(s)` gives

\[
\boxed{Q_s(FX_n(s))-Q_s(FX_m(s))
=-(n-m)\frac{2κ^2}{9}Q(s)^5+O_{n,m}(\|s\|^{11}).}
\]

For n=1,m=0 and s=(t,0), the coefficient is `−2κ²/9 · t¹⁰`, agreeing with Genesis's additional C08 observation. This establishes failure of the **parent-only factor** across each fixed unequal-age pair locally. It does **not** establish failure of every smooth 2D factor.

## 5. Evidence and nonclaims

- Original F3-reachable 15-check script is accessible **inside its ZIP**, including `source/jet_coefficients.json`; no reupload is necessary for this check. Its source SHA-256 is `15a7d0569a1e8ceefe04260ce83e204acb2eeed20b2639eebd810e14ee992824`.
- The new checker verifies 24 symbolic identities/source-contract assertions; the wrong invariant-graph negative control intentionally fails at its named assertion.
- Separate 85-digit high-precision executions of the **untruncated** sine/exponential/reprojection map, for two historical κ choices, ages 1–3 and shrinking amplitudes, approach the predicted fifth-order coefficients. Numeric checks are not uniform-domain certifications.
- Physical birth acceptance remains `NO_TARGET_VECTOR_LAW_SELECTED`. Contract B's projector is not defined. C05–C08 are unchanged. An RER-C09 draft is proposed only, not registered or adopted.
- No age tag or memory law is inferred from these geometric distinctions. A quotient needs a specified regularity class on the countable union, observable preservation, and cross-age fibre-successor compatibility.

## 6. Recommended next step

The local intersection problem is settled for **each fixed finite age pair near the origin**. The remaining high-value test is not a repeated surface plot: seek a single explicit 2D observable-preserving `π` across all age sheets, or a counterexample for a declared admissible class of such π. State whether π extends C¹ to an ambient neighborhood, or only has compatible charts on the sheet union. No quotient is selected here.
