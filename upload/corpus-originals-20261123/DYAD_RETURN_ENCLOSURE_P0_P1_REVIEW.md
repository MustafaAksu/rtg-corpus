# Review: DYAD_RETURN_ENCLOSURE_P0_P1 evidence package
**Reviewer:** Claude (math auditor / Dyadic DSN editor) · **Date:** 20 Sep 2026
**Package reviewed:** `DYAD_RETURN_ENCLOSURE_P0_P1_evidence.zip` (6 supplied inputs, 8 scripts, exact JSON jets, run logs)
**Status of this note:** independent verification record + owner-action recommendations. Not a DSN amendment; no owner RID assigned; no result status changed by this note.

## Verdict

**The audit is correct on every load-bearing claim, and I have reproduced each one with an independent exact implementation** (my own sparse-polynomial arithmetic in $\mathbb{Q}(i\sqrt3)$, written from the stated primitive map $T$, not reusing the package's code). Nothing in it was taken on trust.

## Independently verified claims `[ALG — reproduced]`

| # | Claim | My independent check | Result |
|---|-------|---------------------|--------|
| 1 | `jet1_deg5.json` is the **raw** one-step $W$-jet, not a normalized dictionary | Rebuilt $f=L\circ T\circ L^{-1}$ from $T(\rho,\eta)=(\rho-\sin\eta,\ \eta+e^\rho-1-\sin\eta)$; compared all 17 JSON coefficients | **All 17 equal.** $[f]_{(2,0)}=\tfrac{1+i\sqrt3}{12}\ne0$ ⇒ raw. |
| 2 | Raw six-step resonant coefficients | Composed $f^6$ exactly | $\mu=-\tfrac12-\tfrac{2i\sqrt3}3$, $c^{\rm raw}_{32}=-\tfrac{77}{216}+\tfrac{97i\sqrt3}{648}$, $c^{\rm raw}_{05}=-\tfrac{61}{2160}-\tfrac{43i\sqrt3}{6480}$ — **all match**; quartic channels $(4,0),(3,1),(2,2),(1,3)$ **nonzero** ($F_4\ne0$). |
| 3 | Unique quadratic change $h_2$ removing $F_4$ | Solved degree-4 cancellation; 8 real eqs, 6 unknowns | **rank 6, unique.** $h_2=-\tfrac{1+i\sqrt3}{12}z^2-\tfrac13 z\bar z+\tfrac{1-i\sqrt3}{24}\bar z^2$ — **matches**; degree-4 residual exactly zero. |
| 4 | Normalized lattice coefficient | Read $(0,5)$ of $h^{-1}F_Wh$ after $h_2$ | $a_{05}=-\tfrac{49}{8640}-\tfrac{307i\sqrt3}{25920}$ — **matches**. |
| 5 | **Obstruction** | $c^{\rm raw}_{05}-a_{05}$ exactly | $=\tfrac{-13+3i\sqrt3}{576}\ne0$ — **matches**. |
| 6 | No cubic correction can shift $a_{05}$ | Tested all 8 real $h_3$ basis directions at the $(0,5)$ slot | **All zero shift.** Obstruction is **not** a residual cubic-gauge ambiguity. |
| 7 | `normalize_p6_liegauge_exact.py` is numerical, not exact | Read source | `mp.dps=120`, tolerance pruning; header itself says "does not zero non-resonant channels"; builds from `h4`. |
| 8 | `gauge_bridge_p6.py` has no acceptance gate | Grep + package negative control | **0** assert/exit lines; perturbing target by $10^{-3}$ prints the error and **still exits 0**. |

The package's own second implementation (`independent_sympy_check.py`) also passes all six checks in my sandbox (3.1 s).

## What this means (scoped precisely)

1. **Registry correction needed (Dyadic owner, `[COR]`).** The artifact registry describes `jet1_deg5.json` as a "one-step normalized coefficient dictionary." It is the **raw** one-step $W$-jet (input to normalization, not output). This is a labeling/provenance error, not a coefficient error — the numbers in the file are right.

2. **Three distinct operations were being conflated under "normalization":**
   - archival coordinate change $\Phi_{\rm archive}=\mathrm{id}+h_4+h_{5,\rm nr}$ → preserves **every** raw coefficient through degree 5 (first effect at degree 6); $F_4$ survives;
   - log-channel projection $G_{\rm proj}=\exp(P\log F_W)$ → a defined reduced model, but **not** a solved conjugacy;
   - genuine polynomial conjugacy $f\circ h=h\circ n$ → removes degrees 2,4,6 and yields $a_{32},a_{05}$ above.
   The earlier "coefficient mismatch" between owner ledger values and independent normalizations is fully explained by this: they were different objects.

3. **The obstruction is a real limitation, precisely bounded.** The three-channel model that deletes $F_4$ but *keeps* raw $c_{05}$ is **not formally conjugate through degree 5** to the primitive return by any identity-linear coordinate change. This does **not** refute: the raw coefficients, the cubic dynamics $\mu$, local contraction, or the existence of a nonzero lattice harmonic. It excludes *transferring raw $c_{05}$ into that normalized model* as if conjugate.

4. **The bridge script's exit code must not be used as a pass criterion** anywhere in the corpus. Any historical "bridge PASS" that rested on exit 0 alone should be re-read as "ran," not "verified." (The three coefficient agreements it reports on reconstructed inputs are genuine — ~$10^{-80}$ — but that agreement is $\Phi_6^{-1}F_W\Phi_6$ returning the raw jet, which is an identity, not a proof of conjugacy to $G_{\rm proj}$.)

5. **Consistency with the owner's current ledger.** The Dyadic DSN v6.4.9 records the one-step/DSN-bridge convention coefficient $c^{(1,6)}_{05}=\tfrac{43}{17280}-i\tfrac{227\sqrt3}{155520}$ as *distinct* from the raw six-step $c^{({\rm raw},6)}_{05}$, and carries SG-10 (Im $\nu_5$ not gauge-invariant). The audit's $B_6$ value **equals** that ledger $c^{(1,6)}_{05}$ exactly, and $a_{05}=6\bar\lambda B_6$. So the owner's *one-step* ledger entry is consistent with the true normalization; the mislabeling is confined to the `jet1_deg5.json` artifact description and to any downstream use of $G_{\rm proj}$ as "the normalized return."

## Recommended owner actions (Dyadic DSN, next revision)

- `[COR]` Relabel `jet1_deg5.json` in the artifact registry: **raw one-step $W$-jet, degree ≤ 5** (input to normalization).
- `[DEF]` Add a scope guard (proposed **SG-19, "normalization-object guard"**): the terms *archival coordinate change*, *log-channel projection*, and *polynomial conjugacy* denote three distinct operations; a normalized-coefficient claim must name which one. The projected model $G_{\rm proj}$ must not be called the normalized return.
- `[COR]` Annotate `gauge_bridge_p6.py` (DYAD-ART registry): "prints diagnostics; **no exit-code acceptance gate**." Re-tag any status that rested on its exit code.
- `[ALG]` Record the exact normalized coefficients $a_{32},a_{05}$ and the unique $h_2$ (with the obstruction $c^{\rm raw}_{05}-a_{05}=\tfrac{-13+3i\sqrt3}{576}$) as an `[ALG]` result with the cert scripts from the package plus this independent reproduction — **provided** the owner adopts the stated convention (additive polynomial $h$, resonant $h_n$ set to zero, $O(|z|^7)$ as local existence only). Do not equate it with the historical "Lie strict-kernel" name until the missing `phi1_p6_deg5.json`/solver are recovered.
- `[OPEN]` Historical $\Phi_1$ provenance (missing `phi1_p6_deg5.json`, `homological_solver_p6_numeric.py`) stays open; it blocks convention *identification*, not the new result.

## Explicitly not established by this package (stays `[OPEN]`)
Explicit contraction radius $q_{\rm ctr}$ and six-phase invariant tube; quantitative $h^{-1}$ domain; $C_6/C_7$ remainder bounds; RECOG heteroclinic entry and full-map memory. The recommended next step — an explicit $|R_{\ge6}|\le C_6Q^3$ bound on the primitive contraction branch from the verified L1 radial polynomial — is the right one and does not depend on the projection question.

## Reproduction
`dyad_return_qchi_exact.py` (this review's exact $\mathbb{Q}(i\sqrt3)$ arithmetic) reproduces rows 1–6 in < 60 s. Package scripts run unmodified.
