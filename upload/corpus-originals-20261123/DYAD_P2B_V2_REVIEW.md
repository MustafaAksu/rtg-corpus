# Review: P2-B v2 — signed-vector-jet sharpening (fixed normalizer)
**Reviewer:** Claude · **Date:** 22 Sep 2026 · **Inputs:** ChatGPT message, `REVIEW_DISPOSITION (1).md`, `P2B_V2_VECTOR_SHARPENING_PROOF.md`, `RECOG_LOCAL_HANDOFF.md`
**Status:** independent verification record for **P2-B v2**, which the package correctly stated had no external check yet. Every number below was recomputed from my own degree-9 reconstruction of the six-step jet and my own scalar-majorant/coordinate-polynomial code. Not a DSN amendment; no RID; nothing promoted.

## 0. Their correction to my accounting — accepted
The raw-tail share in v1 is $6199.454/(6199.454+15.818)=99.7455\%$, not $87\%$. I divided the pre-inverse raw term by the post-inverse total (which carries the common factor $L=8/7$). The conclusion — tail-dominated — stands; the number was wrong.

## 1. Exact jet through degree 9 — reproduced
- One-step: 48 nonzero coefficients; six-step: 46 nonzero coefficients through degree 9. Both counts match. $F_2=0$ confirmed.
- Vector coefficient-modulus sums: $2.078832243,\ 1.153114603,\ 1.762147545$ — identical to their displays to 9–10 digits. Ceilings $\tfrac{2079}{1000},\tfrac{577}{500},\tfrac{1763}{1000}$ valid. ✓

## 2. Tail, domains, constants — reproduced

| Quantity | My value | Their bound | ✓ |
|---|---|---|---|
| $K^{\rm vec}_{10}(1/16)$ | $331449.8716$ | $<332000$ | ✓ |
| $H(1/20)$ | $0.0514688$ | $<1/16$; $H/r_W=0.8235<10/11$ | ✓ |
| $C_{\rm poly}(1/20)$, $D_{\rm poly,6}(1/20)$ | $16.37896$, $115.80139$ | $<17$, $<116$ | ✓ |
| $J^+(1/20)$, $H(J^+)$, $S_6(H)$ | $0.05016$, $0.05164$, $0.06523$ | $<\tfrac1{10}$, $<\tfrac9{100}$, $<\tfrac9{100}$ | ✓ |
| **$C_7^{\rm NF}$ at $r_z=1/20$** | **$85.0731933$** | $<100$ | ✓ |
| **derivative at $r_z=1/20$** | **$812.8936249$** | $<1000$ | ✓ |
| $C_7^{\rm NF}$ at $r_z=1/40$ | $27.6022210$ | $<30$ | ✓ |
| derivative at $r_z=1/40$ | $216.7664114$ | $<250$ | ✓ |
| $\tfrac{16}{15}\max_jS_j(1/25)$ | $0.04941455$ | $<1/20$ | ✓ |
| corollary $q\cdot[\,\cdot\,]$ at $q=1/400$ | $0.01072459$ | $<\tfrac12$ | ✓ |
| derivative-tail lemma $n\alpha^{n-10}\le10$ | nonincreasing from $n=10$ for $\alpha\le\tfrac{10}{11}$ | — | ✓ |

The derivative constants use the advertised $C_7$ (100 / 30) inside $M''(R)\,C_7\,r\,(J^+)'(r)$ — consistent and conservative. The corollary's algebra ($|\widehat F|^2=q|1+\mu q+v|^2$, $2\Re\mu=-1$, $|\mu|^2=\tfrac{19}{12}$, $|v|\le q^2(A_J+C_7q)$) is correct.

## 3. Assessment
**Both P2-B v2 profiles are verified.** The structure is exactly the v1 argument with the majorant pushed from vector degree 7 to degree 10 and the raw disk widened to $1/16$ so that $H(1/20)$ fits — the point the proof rightly flags as essential ($H(1/20)>1/20$). Nothing about the chart changed: same $h$, same $J$, same inverse theorem. The gain is $80\times$ in $C_7$ at $2\times$ the radius, and — more important for RECOG — the **entire** P2-A v2 tube now lives inside the normalized evaluation disk, so the $1/2500$ base is retired for the reason I suggested but by an explicit check rather than inference.

Two remarks, neither a defect:
- Where the slack now sits: at $r_z=1/20$, $A(x)b^7$ splits as $b_7\!:\!2.08$, $b_8x\!:\!0.06$, $b_9x^2\!:\!0.005$, $Kx^3\!:\!45.3$, i.e. the degree-10 majorant is still $\sim95\%$ of the pre-inverse raw term and $\sim53\%$ of the final 85. One more push (exact degrees 10–12, majorant from 13) would likely bring $C_7$ to $O(10)$ on the same disk. Only worth doing if a RECOG estimate turns out to be $C_7$-limited; the present constants are already usable.
- The normalized-amplitude corollary is the first statement in this thread that is *directly* about $\widehat F$ on its own disk, without passing through $Q_{\rm prim}$. The handoff correctly says one-orbit summability is an input, not the two-history comparison; I'd add that the corollary's $c=\tfrac12$ has margin $0.0107$ vs. $\tfrac12$, so a much larger normalized disk is available if the $C_7$ domain is ever extended.

## 4. Disposition
- P2-B v2 (both profiles): **verified**; recommend it become the operative normalized profile; v1 retained as baseline.
- `RECOG_LOCAL_HANDOFF.md`: the importable statement is accurate and its "remains RECOG-owned" list is complete and correctly scoped (manifold entry, two-history memory comparison, frame reconciliation with the fixed $h$, GAP-LOCK angular conditions). Suitable for owner adoption review.
- Open, unchanged: RECOG manifold entry; full-map retained-memory theorem; quantitative GAP-LOCK; historical $\Phi_1$ byte identity; optimality.
