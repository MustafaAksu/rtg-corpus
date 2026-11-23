# Triadic F3 reachable-factor test — birth-initialized conditional analytic modal model

**8 October 2026** · **NONCANONICAL** · Genesis = named model owner; Triadic = effective-factor calculation; RER = conditional recording. Not a physical standalone K3 choice; no DSN or RRF change.

## Source and event scope

Use the independent Genesis conditional source law, with its specified reprojection after each primitive edge step:

\[
E=\begin{pmatrix}1&0\\-\frac12&1\\-\frac12&-1\end{pmatrix},\quad
P=\begin{pmatrix}\frac23&-\frac13&-\frac13\\0&\frac12&-\frac12\end{pmatrix},\quad
T_e(\rho,\eta)=(\rho-\sin\eta,\eta+e^\rho-1-\sin\eta).
\]
\[
\mathcal N=(P\otimes I_2)\circ T_e^{\times3}\circ(E\otimes I_2),\qquad
\mathcal F=\mathcal N^6.
\]

The one-time-birth **mathematical contract A** initializes the graph
\[
B_\kappa(s)=(s,C_\kappa(s)),\quad C_\kappa(s)=\kappa Q(s)J_Qs,\quad
Q(r,e)=r^2-re+e^2,\quad J_Q=\frac1{\sqrt3}\begin{pmatrix}1&-2\\2&-1\end{pmatrix},
\]
and subsequently uses only `F`; no reclosure, healing, reset, projection to graph, gauge shift or physical birth event is selected. The physically chosen target remains `NO_TARGET_VECTOR_LAW_SELECTED`.

## F3-R1 [ALG]: signed-Gram nonclosure already on birth age zero

Define signed Gram `Phi=(Q_s,Q_c,I_sc,Omega_G)`, with the source's metric convention `Omega_G= sqrt(3)/2 (s_eta c_rho-s_rho c_eta)`. Since `B_k(-s)=-B_k(s)`, both initial readouts are equal. At `s=(t,0)`, the named analytic model has
\[
Q_s(\mathcal F B_\kappa(t,0))-Q_s(\mathcal F B_\kappa(-t,0))
=\frac5{32}t^5+O(t^6).
\]
This is independent of fixed `kappa`: the parent map is even in `c`, and `C_kappa(s)=O(s^3)`, so no child-dependent parent amplitude contribution enters the displayed degree five. It follows that `Phi` is not an autonomous factor even for states restricted to the one-time birth *initial* surface. Same-age / same-readout is a direct witness, not only failed equivariance.

The `Q_s` delay map on the initial birth surface has Jacobian determinant
\[
\det D_s\big(Q_s(B_\kappa(s)),\;Q_s(\mathcal F B_\kappa(s))\big)\big|_{s=(t,0)}
=-\frac1{64}t^5+O(t^6),
\]
so any local `C^1` factor preserving `Q_s` and its next measurement has continuous dimension at least two there. This does not supply a common invariant 2D factor on all birth ages.

## F3-R2 [ALG]: cross-age failure of the parent-vector candidate

For fixed nonzero `kappa`, `g_kappa(s)=F_s(B_kappa(s))` has derivative identity at zero and is locally invertible. Choose two states with **exactly the same parent vector** `s`:
\[
X_0(s)=B_\kappa(s)\in M_{\kappa,0},\quad
X_1(s)=\mathcal F\big(B_\kappa(g_\kappa^{-1}(s))\big)\in M_{\kappa,1}.
\]
Use the previously verified C07 normal defect at matched parent:
\[
 c(X_1)-c(X_0)=\mathcal R_\kappa(s)+O(\lVert s\rVert^6),\qquad
 \mathcal R_\kappa(s)=-\frac{\sqrt3\kappa}{6}Q(s)^2s.
\]
The source's cubic and quartic parent vector jets are **even in the child mode** (a consequence of the two equal edge roles). Their first child-sensitivity therefore appears in the cubic parent field. Applying its child derivative to the fifth-degree defect gives
\[
\boxed{
 s(\mathcal F X_1(s))-s(\mathcal F X_0(s))
=\frac{\kappa^2Q(s)^4}{18}
\binom{-r-2e}{2r-3e}+O(\lVert s\rVert^{10}),\quad s=(r,e).}
\]
For `s=(t,0)` the coefficient is `kappa^2(-1/18,1/9)t^9`, nonzero for `kappa != 0`. Thus `pi(s,c)=s` is **not** an autonomous factor of the union of the first two birth-age surfaces, even though it is an exact coordinate on the initial graph and every fixed finite age surface admits a local two-coordinate chart.

This does **not** rule out every different nonlinear 2D factor or prove the need for an age/memory variable. It does identify a concrete cross-age conflict for one natural present-state reduction. In fact, independently of the cross-age calculation, signed Gram already fails at age zero by F3-R1.

## Exact domain and dimensional status

`DB_kappa` has rank two and `D F(0)=I`. For each fixed finite `n` the embedded surfaces `M_{kappa,n}=F^n(B_kappa(U_n))` have dimension two on some suitable local neighborhood `U_n` (not a uniform one for every n). Their countable union has four-dimensional Lebesgue measure zero and need not be a single invariant surface. Its closure may be larger. No global physical domain/clock/event rule, uniform radius, convergence of time interpolations or longer-horizon factor has been proved.

### Age-labeled representation (logical upper bound, not a physical proposal)

For each fixed `n`, where the parent projection has a local inverse on `M_{kappa,n}`, the exact reduced chart can be written as `(s,n)`, with branch-dependent two-dimensional parent update and `n^+=n+1`. This illustrates why fixed-age two-dimensionality is compatible with failure of autonomous *parent-only* closure. It is not a proof that `n` is indispensable, minimal or a new physical memory carrier.

## Evidence and custody

- Source G3/G4 file: a byte copy of the existing F3 receiving package `jet_coefficients.json` (SHA-256 `15a7d0569a1e8ceefe04260ce83e204acb2eeed20b2639eebd810e14ee992824`).
- Exact SymPy proof checks use the model jet as source input. They do **not** authenticate historical Genesis microscopic producer runs independently of the declared source formula.
- Direct high-precision checks reconstruct the **full analytic** sine/exponential six-step map; they do not rely on truncating it or impose a child reclosure. They approach the two predicted leading coefficients for both historical reference choices of `kappa`.
- Nonzero asymptotic leading coefficients imply local failures for sufficiently small positive `t`. No explicit numerical radius is certified.

## RER disposition and next step

Propose **RER-GEN-C08** (or another registry-selected local ID): *birth-initialized restricted observables*: signed Gram fails at age zero (degree five), and the parent-vector projection fails across ages 0 and 1 (degree nine), under the named conditional map A. Keep C05-C07 and the physically selected target unchanged. Request Genesis birth/event/clock/attachment conditions before any physical promotion or contract B study. For more general two-dimensional factors, test shared fibres and their successors rather than presupposing an age label.
