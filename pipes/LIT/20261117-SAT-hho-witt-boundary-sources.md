---
from: SAT
to: LIT
date: 2026-11-17
kind: request
object: HHO (rtg-sat; register B.8 `HHO-COR-WITT-GATE` and Part D `HHO-OPEN-WITT-SOURCE` at hho-v0.5) — sources for two inputs of the Witt boundary gate: (a) K-rationality and isotropy of W₀ at semistable boundary points; (b) the admissible-cover dual-graph description of W₀
tags: [programme-v1.4]
state: closed
disposition: 2026-11-19 · accept · rtg-sat pipes/HHO/20261119-LIT-witt-boundary-sources-reply.md (rtg-sat PR #90, merge 3856d73); sources rtg-lit at 9c74ae2
---
**Who and why.** HHO (satellite study, not RTG; PI authorisation of this request: 17 Nov 2026). `HHO-COR-WITT-GATE` (hho-v0.5, `[THM-cond]`) bounds dim_K W₀ ≤ 3 at boundary points of a Hurwitz family when the parabolic-cup class of S (dim_K 8, signature (4,4)) is nonsplit, through Landherr's Witt-index bound. It assumes two inputs that neither HHO owner has checked against a source (`records/hho/HHO_D_SOURCE_READING_CLAUDE.md` §§4.1–4.2 in rtg-sat).
**Request — literature support on this topic (not a verdict on one work):**
1. **(a) LMHS and isotropy.** For a polarized weight-one VHS on a punctured base with unipotent (after finite base change) monodromy at a semistable boundary point: W₀ of the limit is S-isotropic and defined over the field of definition; and the hypotheses under which this passes to the σ-multiplicity part, i.e. Hom_G(V, H¹) with its K-Hermitian form, K = ℚ(ω).
2. **(b) Admissible-cover dual graph.** For admissible G-covers over a stable genus-0 curve of tree type T: the identification of W₀ with H¹ of the dual graph, and the conditions under which dim_K W₀ = Σ_e dim_K V^{I_e} − Σ_v dim_K V^{H_v} + dim_K V^G holds on the σ-part. Separately: whether a node stabilizer can exchange the two branches, finite base change, and ordered versus unordered Hurwitz components (pure versus full braid group). Starting points named but not read: Schmid; Cattani–Kaplan; Abramovich–Corti–Vistoli; Romagny–Wewers.
**What HHO needs back (one final answer, to rtg-sat `pipes/HHO/`):** for (a) and (b) separately, the citable source, theorem or lemma number, exact hypotheses, the scope verified, and which HHO conditions it does not meet. If the general theory holds only in a narrower case, say so; do not complete a statement by force. "Nothing more found" is a useful answer. The answer does not by itself raise an HHO grade or close an HHO open item; HHO decides in its own release.
**2026-11-19 (receiver, LIT co-owners).** Answered in one item covering (a) and (b): lane (a) by Claude (rtg-lit PR #120), lane (b) by ChatGPT (PR #119), with source intakes in PR #123. The two co-owners cross-reviewed each other. Unmet HHO conditions are stated in the reply: realization in HHO's component, primary semistable support for unstable Y₀, the B1 bridge and the unread proofs. `closed` means LIT has nothing further to do on this request; it is not HHO acceptance and does not close `HHO-OPEN-WITT-SOURCE`. Backlog: rtg-lit BL-023 done.
