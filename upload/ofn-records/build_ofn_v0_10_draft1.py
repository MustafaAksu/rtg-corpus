# build_ofn_v0_10_draft1.py — OFN v0.10 Draft 1 assembly (OFN co-owner SESSION, 19 Oct 2026)
# Deterministic: reads the adopted v0.9 file (SHA must match its release record) and applies
# anchored, unique-match edits. Every v0.9 line outside the replaced header block is preserved;
# the checker at the end verifies that claim.
import hashlib, sys, os, difflib
BASE = sys.argv[1] if len(sys.argv) > 1 else 'RTG_ONTOLOGICAL_FOUNDATIONS_v0_9.md'
OUT  = sys.argv[2] if len(sys.argv) > 2 else 'RTG_ONTOLOGICAL_FOUNDATIONS_v0_10_DRAFT1.md'
V09_SHA = '5ae8fdabad35a370f5709afa4d5dca6491e154c75f8a6f15fbb32d251fe59795'
V082_SHA = '6e4fc3c3a999617a63482d0c19d3aa388031e8dbc55c5d7742fb6eadaf564b1d'
raw = open(BASE, 'rb').read()
assert hashlib.sha256(raw).hexdigest() == V09_SHA, 'baseline is not the adopted v0.9'
s = raw.decode('utf-8')
base_lines = s.split('\n')
log = []
def rep(old, new, tag):
    global s
    n = s.count(old)
    assert n == 1, (tag, n)
    s = s.replace(old, new); log.append(tag)
def after(anchor, block, tag):
    rep(anchor, anchor + block, tag)
def before(anchor, block, tag):
    rep(anchor, block + anchor, tag)

# ---------------------------------------------------------------- E01 header (replaced block)
h0 = s.index('**Title:**'); h1 = s.index('## Local Tag Aliases')
old_header = s[h0:h1]
new_header = f"""**Title:** Relational Time Geometry — Ontological Foundations and Model-Selection Layer
**Date:** 19 October 2026
**Scope:** Controlled integration of the co-owner-accepted FMS model-selection handoff (genuine relational-triad contract, class-C model contract and its scoped imports) into the adopted v0.9 text. No v0.9 definition body, hypothesis, local result, guard or OPEN status is revised.
**Document class:** Foundational ontology / model-selection ledger under Methodology v1.3 §0.5.
**Document status:** **DRAFT 1 — ADOPTION PENDING.** Not canonical. `RTG_ONTOLOGICAL_FOUNDATIONS_v0.9` remains the active OFN reference until a separate PI adoption decision. Every new definition, local-result registration, OPEN record and interface action below is a *proposal* (O10-P1–P7, §12.5).
**Supersedes (on adoption only):** `RTG_ONTOLOGICAL_FOUNDATIONS_v0.9`. Until then nothing is superseded.
**Companion documents:** unchanged from v0.9 for every inherited import. The v0.10 additions cite only: `RTG_GENESIS_GEOMETRY_DSN_v2.8.9` (adopted 19 Oct 2026); `RTG_DYADIC_OSCILLATOR_DSN_v6.4.16` (adopted 19 Oct 2026, lifecycle-only release) with v6.4.13–v6.4.15 as the RID sources; `RTG_RRF_REPRESENTATION_REGISTRY_v0.8.3` (adopted working standard). Inherited v0.9 pins (DYAD v6.4.10, GEN v2.8.5, RRF v0.7, …) are **not** silently re-pinned (§11.4).
**DSN Methodology:** DSN_METHODOLOGY_v1.3
**Status summary:** Draft 1 adds §5.5, the proposed genuine relational-triad model-selection contract received from FMS: verdicts Q1–Q6 with Standard C at cubic order and the local C³ regularity of Q6; the class-C transported family declared as a different conditional model (RRF v0.8.3 §0.3); two proposed OFN local results; the scoped FMS disposition; and the ψ-modulus with its readout limit. Nine new administrative imports and five reference records are added (§11.4–§11.5). The nine registered v0.9 definitions, FSP-U, the two registered local consequences and all twenty foundational OPEN statuses (nineteen ACTIVE, one PARTIAL) are retained. One new OPEN record is proposed. No physical carrier, chirality, isolation regime, exchange operation, ontology or primacy is selected.
**Authors:** Mustafa (PI) · Claude · ChatGPT · Gemini · Grok — inherited attribution; separate approval by every listed contributor is not inferred.
**Revision editor:** Claude (OFN co-owner), Draft 1. Second OFN co-owner (ChatGPT) review of this draft is pending.
**Programme document / placement:** Adopted Programme v1.2; Tier 2, namespace `RTG-OFN`; no maturity change.
**Revision base:** Adopted `RTG_ONTOLOGICAL_FOUNDATIONS_v0_9.md`, SHA-256 `{V09_SHA}`, recomputed in this session and equal to the value in `RTG_ONTOLOGICAL_FOUNDATIONS_v0_9_RELEASE_RECORD.md` §7 (1,411 lines). Assembly is a scripted, anchored edit of those bytes; the v0.9 header block is replaced by this draft header, and every other v0.9 line is preserved (§12.5).
**Governing input:** `OFN_REPLY_TO_FMS_MODEL_SELECTION_v0_8_2.md`, SHA-256 `{V082_SHA}`, accepted on 19 October 2026 by both OFN co-owners as the consolidated handoff for v0.10 (second co-owner computed the same hash independently). v0.8 and v0.8.1 are superseded working copies. The acceptance is a co-owner handoff acceptance, not owner adoption.
**Not integrated in this draft:** the separate 13 October 2026 OPEN-narrowing package (`OFN OPEN narrowing — scoped proofs and owner proposals v0.1` and its evaluation). It needs its own authorization and is neither accepted nor rejected here.
**Evidence boundary:** Owner statements were read at the cited sections; co-owner SESSION computations are listed in §12.1 with what was executed by whom. No owner certificate is rerun. FMS SESSION results enter as reference records only (RF-O10-02). Mounted hashes identify inspected bytes, not proof certification.
**v0.9 header:** preserved verbatim in the adopted v0.9 file and summarized in Appendix C.

"""
new_header = '\n'.join(l + '  ' if l.startswith('**') else l for l in new_header.split('\n'))
s = s[:h0] + new_header + s[h1:]; log.append('E01 header')
rep('# RTG_ONTOLOGICAL_FOUNDATIONS_v0.9\n', '# RTG_ONTOLOGICAL_FOUNDATIONS_v0.10 — DRAFT 1 (adoption pending)\n', 'E02 title')

# ---------------------------------------------------------------- E03 §0.1 revision boundary
after("""Pilot closeout and any later definition proposal require separate decisions.
""", """
**v0.10 Draft 1 revision boundary:** this draft is the separate definition proposal anticipated above, limited to the FMS model-selection interface. It adds §5.5 and its imports, references and one proposed OPEN record. It does not change any v0.9 definition body, FSP-U, the two registered local consequences, any guard, or any of the twenty OPEN statuses. The new contract binds a *named model class* (the genuine interacting relational triad) and is not a universal axiom, a primacy verdict or a physical selection (SG-OFN-SELECTION, SG-OFN-PRIMACY).
""", 'E03 0.1 boundary')

# ---------------------------------------------------------------- E04 §0.3 adoption sentence
after("""This reconciliation release does not close scientific OPENs, accept another owner's custody, or adopt the FMS pilot closeout.
""", """
*v0.10 Draft 1:* no adoption is recorded. Proposals O10-P1–P7 (§12.5) await the second co-owner's draft review and a separate PI decision. Until then v0.9 governs, and the v0.8.2 handoff remains a co-owner-accepted working record.
""", 'E04 0.3 adoption')

# ---------------------------------------------------------------- E05 §0.4 profile row
after("""| Competing primitives and event motivation | §§2–3 |
""", """| Genuine relational-triad model-selection contract (proposed v0.10) | §5.5; imports §11.4; references §11.5 |
""", 'E05 0.4 profile row')

# ---------------------------------------------------------------- E06 §5.5 new section
SEC55 = r"""
<a id="ofn-triad-model-selection"></a>
### 5.5 Genuine Relational-Triad Model-Selection Contract (FMS Receiving Interface) — proposed v0.10

> **[Guards SG-OFN-SELECTION, SG-OFN-PRIMACY, SG-OFN-STATE and SG-OFN-PRESENTATION apply]** The requirements below bind the named class of genuine interacting relational-triad models. They are not universal axioms, they do not select a primitive object, and they do not physically select any model, carrier or chirality.

**Source and status.** Governing input: `OFN_REPLY_TO_FMS_MODEL_SELECTION_v0_8_2.md` (SHA-256 `6e4fc3c3…564b1d`), accepted by both OFN co-owners on 19 October 2026. Every `[DEF]` and `[RESULT]` in this section is **proposed** (O10-P2–P5) and carries no owner status until PI adoption. Technical results keep their owners' grades (§11.4); FMS SESSION results are reference-only (RF-O10-02).

#### 5.5.1 Declared test model

`[DEF]` [proposed; part of RTG-OFN-DEF-TRIAD-MODEL-CONTRACT] For the FMS interface the triad model is declared by:

| Field | Declaration |
|---|---|
| State | Oriented edge relations with incidence and chirality data. Nodes as endpoint classes are a model choice; further state fields remain open. |
| Encoding | Raw $W$ edge values are the FMS test carrier, not a physical or canonical choice. Identity encoding holds on the fixed incidence/chirality edge-value sector. |
| Closure | No exact closure is imposed; $h=\sum_e r_e$ is tracked as the raw additive cycle defect, a dynamical observable. |
| Clock | The primitive update; $T^6$ is derived sampling. No ontological definition of time follows (SG-OFN-TIME). |
| Regularity | Real-analytic laws form the admitted continuous FMS test class; this is not a universal requirement. |

Carried distinctions: coincidence $r_{BC}=0$, node identity $B=C$ and a reduction $\mathcal X_3\to\mathcal X_2$ are distinct, and any merge needs its own reduction contract. Holonomy capacity, a nonzero value, dynamical independence and a curvature reading are separate properties (§4.4).

#### 5.5.2 Verdicts Q1–Q6

`[DEF]` [proposed RID: RTG-OFN-DEF-TRIAD-MODEL-CONTRACT] [scope: genuine interacting relational-triad model class; FMS receiving interface] Within that class:

| Item | Requirement | Not required / not implied |
|---|---|---|
| **Q1** exact closure | Not universal. Exact additive closure is admissible as a flat, node-mediated sector. | Imposition on independent relational-edge models |
| **Q2** asymptotic closure | Admissible if it follows from the selected dynamics. | A requirement |
| **Q3a** full primitive edge autonomy | Not required. Boundary-conditioned isolated-dyad recovery (Standard C) is the minimum target, with an explicitly defined, physically admissible, nonempty and dynamically consistent isolation regime. Standard B remains an alternative. | That linear-order recovery suffices |
| **Q3b** partial autonomy | Not acceptable as the law of a genuine triad in asymmetric form: designating a slaved edge breaks complete-state relabeling covariance unless the designation is physical state data, i.e. a declared extra variable (route C-a). The two-factor-plus-slaved-edge construction is a mathematical witness only. | — |
| **Q4** cycle content | The class must permit nonintegrable cycle content; flat sectors remain admissible. The raw additive defect is a candidate observable. | That it is an established curvature variable |
| **Q5** exchange and coincidence | Covariance of the complete oriented state under relabeling: $F_{\pi\cdot m}(\pi X)=\pi F_m(X)$, with $m$ carrying orientation, role and model data. Clock: primitive $T$. | Active dynamical reversal on a fixed raw-edge model; identity of physical pole-role exchange with bookkeeping relabeling (OPEN-OFN-OPA) |
| **Q6** genuine coupling | Required: interaction that cannot be removed by a passive transformation into a decoupled product, under the declared state, encoding and clock. **Q6-REG:** passive transformations are local $C^3$ diffeomorphisms fixing the base point. **Governing (narrow) reading:** no local $C^3$ conjugacy to a product of three planar edge maps, and no neutral planar $C^3$ factor under the declared clock. | Decouplings below $C^3$ (OPEN, neither proved nor refuted); wider non-planar decompositions ($d\ge4$), which need separate proof |

`[DEF]` [proposed RID: RTG-OFN-DEF-STANDARD-C] [scope: as above] **Standard C at cubic order.** Write the update as $F_e(X)=T(r_e)+I_e(X)$. Standard C holds if there is a nonempty $F$-invariant regime $\mathcal R$ on which $I_e=O(|r|^4)$ for every edge $e$, i.e. the isolated dyad is recovered through the order carrying $\mu$ and the six-step return. Recovery at linear order alone does not count. *Provenance:* the order was fixed by PI decision on 18 October 2026 at session level; its OFN registration is proposed here.

Physical-isolation scope: an invariant regime on which the interaction vanishes algebraically satisfies the mathematical contract; it does not by itself show that the surroundings are physically removed. The physical-isolation reading stays open (proposed OPEN-OFN-TRIAD-CLASS).

#### 5.5.3 Proposed OFN local results

`[RESULT]` `[from: ALG]` [proposed RID: RTG-OFN-ALG-RAW-STANDARD-C-NOGO] [scope: raw additive mean-feedback κ-family, local at 0, smooth invariant regimes; OFN custody proposed] **Raw-carrier Standard C no-go.** Let $\kappa\ne0$. In the raw carrier there is no $F_\kappa$-invariant $C^3$ submanifold $M\ni0$ of positive dimension on which $I=O(|r|^3)$, a fortiori none with $I=O(|r|^4)$.
*Proof.* $T_0M$ is $A^{\times3}$-invariant, hence complex of complex dimension 1–3. From $I=O(|r|^3)$, $\sum_eT(r_e)=Ah+O(2)$ gives $h=O(|r|^2)$ and $T_0M\subset\mathcal C$; since $DF_\kappa(0)$ is invertible on $T_0M$, every $y\in M$ near 0 is $F(x)$ with $|x|\sim|y|$, so $h(y)=(1-\kappa)\sum T(x)=O(|y|^3)$. Dimension 2 ($T_0M=\mathcal C$): $\sum_eT_2(u_e)=(0,\tfrac12\sum_e\rho_e^2)\not\equiv0$. Dimension 1: $M$ is a graph $w_e=G_e(w)$ with linear parts $c_e$, $c_1=1$, $\sum c_e=0$; non-resonance at degree 2 forces $g_{e,2}(w)=h_2(c_ew)-c_eh_2(w)$ in the DYAD $h_2$ chart, and the $z\bar z$ coefficient of $\sum_eG_e$ is $c_{11}\sum_e|c_e|^2$ with $c_{11}=-1/3\neq0$. Contradiction in every case. ∎
Depends on: the raw κ-family, the DYAD quadratic chart coefficient $c_{11}=-1/3$ and local smooth invariance. Evidence: `iso_quadratic_nogo.py` (`91fd63f4…5308`) and `iso_check.py` (`b92f6659…0d75e`) check the degree-2 identities exactly; the tangent classification rests on the analytic argument. Not covered: non-manifold invariant sets, finite-amplitude regimes away from 0, and other carriers. **OPEN-C19-L** (hand derivation, SESSION): for the ER-2B C19 quadratic-carrier family with re-imposed linear closure, the argument forces $\tilde q=0$ in dimension 2 and only $\tilde v=0$ on equilateral lock lines, so the codimension-2 subfamily $\tilde v=0$ is not excluded at quadratic order. This is a gap in an exclusion, not a candidate model.

`[RESULT]` `[from: THM + ALG]` [proposed RID: RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT] [scope: real $C^3$ germs listed below; OFN custody proposed] **Narrow-Q6 corollary.** Let $F$ be (i) a raw mean-feedback map $F_\kappa$, $\kappa\in\mathbb R\setminus\{0,2\}$, or (ii) a real $C^3$ class-C germ satisfying the hypotheses of `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` (instance C1, the real polynomial representatives; instance C2, $\mathcal F_{\kappa,\Phi}$ conditionally on a real $C^3$ chart $\Phi$ with $\Phi T\Phi^{-1}$ commuting with $A$, whose existence is not asserted). Then $F$ is not locally $C^3$-conjugate to a product of three planar maps.
*Proof.* Suppose $F=\Psi^{-1}(G_1\times G_2\times G_3)\Psi$. Then $\operatorname{spec}DF(0)=\{\lambda,\bar\lambda\}^{\times2}\cup\{(1-\kappa)\lambda,(1-\kappa)\bar\lambda\}$. Each $DG_i(0)$ is real $2\times2$, so its spectrum is conjugation-closed. For $\kappa\notin\{0,2\}$ the closure pair is off the unit circle (at $\kappa=1$ it is $0$, still real), so it lies in one factor and the other two are exactly neutral with spectrum $\{\lambda,\bar\lambda\}$. For a neutral factor, $E_i=\pi_i\circ\Psi$ satisfies $E_i\circ F^6=G_i^6\circ E_i$ with $\operatorname{spec}D(G_i^6)(0)=\{1\}$; since $(1-\kappa)^6\ne1$, (H_spec) holds. This contradicts `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` ($\kappa\ne1$) or `GEN-THM-K3-SIXSTEP-FACTOR-NOGO` ($\kappa=1$) in case (i), and `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` in case (ii). ∎
Depends on: IMP-O10-01/02 at their stated scope. The six-step theorems are used; the primitive-clock family statement (Genesis `[ALG]`, no RID) is not. Agreement: the Genesis v2.8.9 notice erratum (RF-O10-05) concurs with this corollary and withdraws its earlier "[ALG]-only" sentence. Not covered: formal power series "as such" (Genesis G-JET), sub-$C^3$, non-planar or closure-mode-only factorizations; it does not distinguish class C from its third-jet equivalents (G-SEL) and asserts no realization of $J$.

#### 5.5.4 Class C: the transported κ-family as a declared conditional model

`[DEF]` [proposed; part of RTG-OFN-DEF-TRIAD-MODEL-CONTRACT] The transported family
$$F^N_\kappa(z)_e=N(z_e)-\frac{\kappa}{3}\sum_jN(z_j),$$
with $N$ the λ-equivariant normal form (or $\mathcal F_{\kappa,\Phi}$ in a Bochner chart), re-imposes additive mean-feedback in new coordinates. By RRF v0.8.3 §0.3 it is a **different conditional model**, not a passive transport of the raw κ-family and not an `RRF-NET-W-RAW` equation set (RRF representation safety lock; RF-O10-01). Its contract:

| Field | Declaration |
|---|---|
| Regularity | Formal; real $C^3$ for the polynomial representatives. Analytic or $C^\infty$ realization is conditional on DYAD OPEN 20 (B-6 / B-∞ existence). |
| Clock | Primitive $T$; $T^6$ derived sampling. |
| Domain | A local neighbourhood of 0. |
| Readout chart | Transported ($z$ or $\Phi$). Raw-$W$ readouts carry static chart offsets and must subtract them or use transported modes (§5.5.6). |
| κ range | Formal properties for $\kappa\notin\{0,1,2\}$; stability statements only for $0<\kappa<2$, $\kappa\ne1$. At $\kappa=2$ the closure multiplier lies on the unit circle and the centre-manifold reduction does not apply; this is not a Q6 failure. |
| Registration | OFN requests RRF to register class C as a *model-contract row*, not a new native profile, while OPEN-B/E1 stays locked. The decision is RRF's. |

Formal properties `[ALG — formal; OFN co-owner SESSION, recorded, not registered]`:
- **Lock surfaces.** $\mathcal S_0=\{(z,-z,0)\}$ and $\mathcal S_\pm=\{(z,\omega^{\pm1}z,\omega^{\pm2}z)\}$, $\omega=\lambda^2$, are invariant with $I\equiv0$ exactly; each edge evolves by $N\cong T$. Cyclic relabeling preserves $\mathcal S_\pm$ and a transposition with edge reversal exchanges them, so the pair carries exactly the chirality datum. In raw coordinates they are generated by the canonical $J=T\circ F^{-1/6}$ ($R_0=J^3$, $G=J^2$), whose formal uniqueness is owner-grade (IMP-O10-03).
- **Cycle-defect capacity.** For $\kappa\ne1$ the transported defect evolves by $(1-\kappa)\sum N$ off the surfaces (Q4 capacity); at $\kappa=1$ the model is flat.
- **Six-step cubic.** On the centre manifold, $f_e=\mu\bigl(w_e|w_e|^2-\tfrac13\sum_jw_j|w_j|^2\bigr)$, independent of κ, with chiral coefficients $p=\mu/3$, $q=2\mu/3$ (`transported_pq.py`, exact).
- **Realization.** A real carrier for the whole class follows from one object, an identity-tangent sixth root of $F=T^6$ (equivalently a real $J$), via Bochner averaging $\Phi=\tfrac16\sum_{k=0}^5A^{-k}J^k$; a convergent normalizer is not needed. Existence is DYAD OPEN 20 (IMP-O10-04).

Chiral convention for sign statements (Genesis §6.3a): $u=w_1+\lambda w_2$, $v=w_1+\bar\lambda w_2$, $N=|u|^2+|v|^2$, $S=\operatorname{Im}(w_1\bar w_2)=(|u|^2-|v|^2)/\sqrt{12}$, $\rho=S/N$. A sign of chirality must name its convention.

#### 5.5.5 Scoped FMS disposition (Standard C at cubic order)

| Candidate | Disposition | Basis |
|---|---|---|
| A1, κ = 1 (raw) | Excluded; retained as a flat-sector model | Q4 fails (flat); RTG-OFN-ALG-RAW-STANDARD-C-NOGO |
| B, κ = 0 (raw) | Excluded from the coupled class; retained as decoupled reference | Q6 |
| A2, 0 < κ < 2, κ ≠ 1 (raw) | Excluded under Standard C at cubic order. Q6 and Q4 capacity hold | RTG-OFN-ALG-RAW-STANDARD-C-NOGO; narrow-Q6 case (i). Loopholes: non-manifold or finite-amplitude regimes; other carriers (OPEN-C19-L) |
| C, transported κ-family | **Primary formal candidate class; real only once $J$ is realized.** A family with an in-class modulus (§5.5.7), not a single model | Standard C exactly on $\mathcal S_0,\mathcal S_\pm$; Q4 capacity; Q5 with active covariance; Q6 by IMP-O10-02 and narrow-Q6 case (ii) for real $C^3$ germs |
| C, other routes | Open under the same requirements | — |

This disposition ranks candidates under the declared contract; it is model policy, not physical selection (SG-OFN-SELECTION).

#### 5.5.6 Dynamics on the closure plane: what is and is not established

- `[ALG — leading order; SESSION]` Per six-step block, $\Delta\log(|u|^2/|v|^2)=\tfrac13(|u|^2-|v|^2)+O(|(u,v)|^4)$: the chiral axes $\mathcal S_+=\{u=0\}$, $\mathcal S_-=\{v=0\}$ are relatively attracting at cubic order. The attraction is **relative**: $\Delta\rho=S(\tfrac16-2\rho^2)+O(5)$, so $|\rho|\to1/\sqrt{12}$ while $|S|$ decays with $N$.
- The equal-amplitude set $|u|=|v|$ separates the tendencies at cubic order only; its invariance under the complete map is not shown. The coincidence surfaces are exactly invariant, lie on it and are transversally repelling there; their lying on a basin boundary is conditional on the existence of two disjoint chiral basins exchanged by the corresponding transposition-with-reversal.
- Cubic-truncation rate target `[ALG]`: on $u\to0$, $|u_m|/|v_m|\asymp m^{-1/2}$.
- **Raw-readout guard.** Read in raw coordinates, $u_W=O(|v|^2)$ on $u=0$, with the same exponent as the predicted rate; rate tests use transported modes or subtract the static offset. Single-edge ingredients are owner-grade (IMP-O10-05).
- **Single-dyad imports on the lock surfaces only.** On $\mathcal S_0,\mathcal S_\pm$ each edge is an isolated dyad, so the IMP-O10-05 results apply edgewise there, conditional on the real surfaces ($J$). Nothing transfers off the surfaces, and nothing transfers as a separator or basin statement.
- `[OPEN]` Convergence of an open set of states to the chiral surfaces under the full local dynamics; the existence, geometry and member-dependence of the full nonlinear chiral basins. Numerics (degree-5 truncated $N$, 48/48 closure-plane runs near the diagonal) support only the cubic separator at the tested amplitudes.

#### 5.5.7 Canonicity and the in-class ψ-modulus

`[INTERP]` **Canonicity.** The canonical formal lock geometry, the isolated edge dynamics on the lock surfaces and the leading reduced chiral cubic coefficients are normalizer-independent. The ambient network law is a family, not a uniquely determined model; it is not determined by the canonical generator and lock geometry. The fifth-order ψ-modulus (RF-O10-02) establishes a nontrivial formal conjugacy obstruction within the stated class. This does not classify every member, every higher-order jet or every invariant manifold. No physical selection observable is established by the formal modulus alone.

Reference summary (RF-O10-02 carries the grades): for the chart family $g_a(z)=z+az^2\bar z$, members coincide through degree 5 for $a\in\mathbb R\mu$; for $a\in i\mathbb R\mu$ formal conjugacy is obstructed at degree 5 for every real $\kappa\notin\{0,2\}$; through degree 5, $f_{\kappa,a}\cong f_{\kappa,b}\iff m(a)=m(b)$ with $m=\operatorname{Im}(a\bar\mu)$, within the reduced-map scope. $|c|$ reads $m$ only up to the reflection $m\mapsto2m_*-m$; the phase of $c$ is representation-dependent, so "$\operatorname{Im}c=0$" is not a normalization or selection principle.

#### 5.5.8 Non-claims

- No physical carrier, chirality, isolation regime or exchange operation is selected; class C is not claimed unique, and the ψ-modulus has no physical value.
- No single-dyad result is used as a network separator or basin theorem.
- The narrow-Q6 corollary is OFN-derived, not a Genesis statement; until adoption it remains OFN SESSION.
- No sub-$C^3$, non-planar or formal-series decoupling statement is made.
- Neither an exact class-C lock surface nor a raw-carrier no-go settles OPEN-OFN-3A/3B or primacy (§8).
"""
before('---\n\n<a id="ofn-continuous-selection"></a>', SEC55.lstrip('\n') + '\n', 'E06 §5.5')

# ---------------------------------------------------------------- E07 §9 registry intro
after("""A source reporting a closed additive operator or local history theorem does not automatically close OFN's broader physical question.
""", """
*v0.10 Draft 1:* the twenty identities and statuses above are unchanged. One new record, OPEN-OFN-TRIAD-CLASS, is proposed (O10-P6) at the end of this registry; it becomes a registered identity only on adoption. Reconciliation inputs from §5.5 are added to OPEN-OFN-3B, OPEN-OFN-FRUSTRATION and OPEN-OFN-OPA without status change.
""", 'E07 §9 intro')

# ---------------------------------------------------------------- E08 OPEN-3B input
after("""Next required artifact or decision: Technical-owner assignment and an admissible construction, not a trivial inserted factor.
""", """
Reconciliation input (v0.10 Draft 1): class C (§5.5.4) has exact invariant lock surfaces on which every edge evolves by the transported isolated-dyad map. This is a formal, $J$-conditional invariant-subsystem witness for a specified coupled triad law. Whether that law counts as an *independently specified admissible* $T_3$ in the sense of §8 is not decided here, since it is built from the chosen dyad map in a transported chart. In the raw carrier, RTG-OFN-ALG-RAW-STANDARD-C-NOGO (proposed) excludes smooth invariant isolation regimes through 0 for every κ ≠ 0. Status remains ACTIVE; neither outcome selects ontology.
""", 'E08 OPEN-3B input')

# ---------------------------------------------------------------- E09 FRUSTRATION input
after("""This is the source-model null case, not a claim that every possible discrete extension is flat. Its physical/general extension remains open.
""", """
Reconciliation input (v0.10 Draft 1): §5.5.2 Q4 requires the genuine-triad class to *permit* nonintegrable cycle content and treats the raw additive defect as a candidate observable only. Class C has defect capacity for κ ≠ 1 (§5.5.4). Capacity, a nonzero value and a curvature reading remain distinct; status remains PARTIAL.
""", 'E09 FRUSTRATION input')

# ---------------------------------------------------------------- E10 OPA input
after("""This passive-relabeling/distinct-role dichotomy is exhaustive only for the isolated-dyad question in the registered family; G1-P1's composition question remains routed to RRF and OFN/OPEN-P0, so passive dyad relabeling does not close orientation for a composed system.
""", """
Reconciliation input (v0.10 Draft 1): the proposed Q5 (§5.5.2) requires complete-state relabeling covariance in the genuine-triad class and does not require active dynamical reversal on a fixed raw-edge model. Whether physical pole-role exchange is the same operation as bookkeeping relabeling stays here. For class C, radial contraction removes flat ambiguity among admissible smooth commuting realizations (DYAD Lemma F / F3, IMP-O10-04); existence remains open, and identifying any realization with pole exchange needs a separate ontological and representation contract (this OPEN; RRF OPEN-A). Status unchanged.
""", 'E10 OPA input')

# ---------------------------------------------------------------- E11 new OPEN record (end of registry, before §10)
NEWOPEN = """<a id="ofn-open-triad-class"></a>
**OPEN-OFN-TRIAD-CLASS — Physical selection inside the genuine relational-triad class** [proposed RID: RTG-OFN-OPEN-TRIAD-CLASS] *(proposed v0.10; not registered before adoption)*

Status: ACTIVE (proposed) | Layer: O3→O4
Question: Which physical criterion, if any, selects a member of the admitted class-C family (the in-class ψ-modulus) and gives Standard C its physical-isolation reading and the chiral surfaces a physical chirality reading?
Closure criterion: A stated principle or effective-limit argument fixing the modulus (or an explicit equivalence class) in a declared carrier and encoding, with the RRF readout contract; separately, a physical-isolation criterion and a chirality dictionary. A formal invariant, a chart convention such as "Im c = 0", or a numerical basin preference does not close it.
Dependencies: §5.5; DYAD OPEN 20 (realization of $J$); RF-O10-02 (modulus and its reflection-limited readout); RRF model-contract row; FMS basin-boundary work; sub-$C^3$ decouplings (Q6-REG); OPEN-C19-L; OPEN-OFN-OPA for exchange.
Notify: FMS, RRF, DYAD, GEN, TRIAD.
Next required artifact or decision: PI decision on this record; then an RRF readout contract. A torus-invariant scalar reading the sign of $m-m_*$ is needed only if RRF requires a full physical readout.

---

"""
NEWOPEN = '\n'.join(l + '  ' if l.split(':')[0] in ('Status','Question','Closure criterion','Dependencies','Notify') else l for l in NEWOPEN.split('\n'))
before('<a id="ofn-rejections"></a>', NEWOPEN, 'E11 new OPEN')

# ---------------------------------------------------------------- E12 §11.4 / §11.5 imports and references
IMPS = r"""
### 11.4 v0.10 Draft 1 Claim-Level Imports (proposed)

These entries support §5.5 only. Inherited §11.2 entries keep their v0.9 pins: the Genesis v2.8.5 and Dyadic v6.4.10 imports there are **not** re-pinned to v2.8.9 / v6.4.16, because no inherited statement was re-inspected against the newer editions for this draft. Source statements below were read in the cited owner files; no owner certificate is rerun.

<a id="imp-o10-01"></a>
- **IMP-O10-01** :: Raw-family six-step factor no-go :: `RTG_GENESIS_GEOMETRY_DSN_v2.8.9` (SHA-256 `d143673e…c6fc`, computed by OFN) :: §5.5.3 narrow-Q6 case (i); §5.5.5
  Source identity: `GEN-THM-K3-PLANAR-FACTOR-NOGO`, `GEN-THM-K3-SIXSTEP-FACTOR-NOGO` (κ = 1); `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO` (γ ≡ κ ∈ ℝ∖{0,2}, under (H_spec)). Source status: `THM`. Unchanged since v2.8.7.
  Depends on: the raw mean-feedback family and (H_spec). The primitive-clock family statement under (H_prim) is a Genesis companion without RID and is not imported; (H_prim) does not extend anything to κ = 2. Does not cover class C.

<a id="imp-o10-02"></a>
- **IMP-O10-02** :: Transported chiral six-step factor no-go :: `RTG_GENESIS_GEOMETRY_DSN_v2.8.9` §6.3c :: §5.5.3 narrow-Q6 case (ii); §5.5.5
  Source identity: `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO`. Source status: `THM` (conditional). §6.3c read in full.
  Depends on: real $C^3$ germs; (H-JET) third jet equal to the mean-feedback form over $N_3(z)=\lambda z+nz^2\bar z$; (H-μ) $\mu=6\bar\lambda n\ne0$; κ ∈ ℝ∖{0,2}; (H_spec); factor dimension $d\in\{1,2,3\}$; closed under $C^3$ conjugacy; algebraic dependency Lemma S (adopted branch). Guards G-JET, G-20, G-SEL, G-OFN apply. Class C satisfies (H-JET) with $n=n_{21}$, $\mu=\mu_6\ne0$ for instance C1, and for C2 conditionally on Φ.

<a id="imp-o10-03"></a>
- **IMP-O10-03** :: Uniqueness of the formal ℤ₆ generator $J$ :: `RTG_DYADIC_OSCILLATOR_DSN_v6.4.13` §6.16 :: §5.5.4
  Source identity: `DYAD-THM-FORMAL-Z6-GENERATOR`, resting on `DYAD-THM-FORMAL-CENTRALIZER` (Theorem C). Source status: `THM` (formal).
  Depends on: formal maps commuting with $F=T^6$, $J^6=\mathrm{id}$, $DJ(0)=A$. Formal only; no convergence asserted. The FMS SESSION classification of the formal centralizer is corroboration, not a premise.

<a id="imp-o10-04"></a>
- **IMP-O10-04** :: Flat centralizer, smooth corollaries and the realization target :: `RTG_DYADIC_OSCILLATOR_DSN_v6.4.13` §6.17 and OPEN 20 :: §5.5.4; OPEN-OFN-OPA input
  Source identity: `DYAD-CAND-FLAT-CENTRALIZER` (Lemma F), status `THM`, on its D1–D3 domain with value-level flat contact; `DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES` (F3), status `THM — conditional` on existence of the smooth object. `CAND` in these strings is an identity, not a status (Methodology v1.3). OPEN 20 is PARTIAL: B-∞ flat uniqueness CLOSED for existing $C^\infty$ objects; B-an, B-6 and B-∞ existence open.
  Depends on: an *existing* $C^\infty$ identity-tangent root; existence is not imported. The Borel-and-iterate route is a proposal only, and RRF L-SHADOW-POLY is not imported.

<a id="imp-o10-05"></a>
- **IMP-O10-05** :: Single-dyad OPEN 3 results, edgewise on the lock surfaces only :: `RTG_DYADIC_OSCILLATOR_DSN_v6.4.14` / `v6.4.15` (OPEN 3 records); lifecycle status per `v6.4.16` :: §5.5.6
  Source identity: `DYAD-ALG-OPEN3-LEADING` (`ALG`, v6.4.14); `DYAD-THM-OPEN3-SPIRAL-REM` (`THM`, per-row constants are suprema of majorants, v6.4.14); `DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS` (`THM`, v6.4.15); `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE` (`THM`, conditional on RECOG R9, v6.4.15). Section anchors are as located in the owner OPEN 3 record; not re-verified line by line for this draft.
  Depends on: an isolated dyad. Applied only on $\mathcal S_0,\mathcal S_\pm$, edgewise, conditional on the real surfaces ($J$). Static leading offsets transfer edgewise and class-wide at leading order. Nothing transfers off the surfaces or as a separator or basin statement. v6.4.16 (lifecycle-only) records OPEN 3 CLOSED within its scope and opens OPEN 21; no graded RID changed (RF-O10-04).

### 11.5 v0.10 Draft 1 Reference-Only Records (proposed)

<a id="rf-o10-01"></a>
- **RF-O10-01 — RRF representation contract for class C** :: RRF v0.8.3 §0.3, representation safety lock, §2.4b–c, §6.2

Re-imposing linear addition or projection in new coordinates creates a different conditional model (§0.3). Network equations live in `RRF-NET-W-RAW`; $z_{NF}$ may appear in network work only inside transported single-dyad subexpressions (safety lock, provisional until OPEN-E). Every realization contract declares regularity and clock (§6.2). In the $C^\infty$ and analytic categories an odd chart exists iff a tangent-to-identity square root of $F$ exists, and B-6 ⟺ B-an ∧ B-3, registered by RRF as algebraic consequences of DYAD owner results, not existence proofs.
Action: §5.5.4 declares class C under §0.3 and requests a model-contract row. RRF decides. RRF v0.8.3 is a working standard; this is a reference, not a theorem import.

<a id="rf-o10-02"></a>
- **RF-O10-02 — In-class ψ-modulus and its readout limit (FMS SESSION, OFN-audited at stated scope)** :: FMS ψ quintic notes (phase invariant; finite invariant; reflection v0.1.1); OFN co-owner audit scripts (§12.1)

| Statement | Grade and evidence |
|---|---|
| $a\in\mathbb R\mu$: $N_a=N$ through degree 5 ($g_a$ agrees with an element of $\mathrm{Cent}(N)$) | `[ALG — SESSION]` |
| $a\in i\mathbb R\mu$, first order in $a$: formal conjugacy within the connected linear stabilizer obstructed at degree 5 for every real κ ∉ {0,2}; exceptional set empty | `[ALG — SESSION; two independent exact computations]` (FMS 9×9 minor; OFN 32×32 minor constant in $t=(1-\kappa)/\kappa$), executed by both co-owners |
| $c(\kappa,a)=-\tfrac1{486}+\tfrac{7t}{648}+i\bigl[\tfrac{17\sqrt3}{2916}+\tfrac{2\sqrt3\,t}{81}-\tfrac29\operatorname{Im}(a\bar\mu)\bigr]$, the $u^3\bar v^3$ coefficient of $A\circ F_6-A$, $A=\vert u\vert^2$; unchanged by the 24 equivariant cubic generators; torus rotates its phase; $\vert c\vert$ invariant under every formal conjugacy | Closed form and generator invariance: OFN executed, both co-owners. Invariance of $\vert c\vert$: FMS proposition (read), with OFN re-deriving the degree-5 linearity and computing $\mathrm{Stab}(f_3)=\mathbb T^2\rtimes\mathbb Z_2$ exactly |
| Through degree 5, within the reduced-map scope: $f_{\kappa,a}\cong f_{\kappa,b}\iff m(a)=m(b)$, $m=\operatorname{Im}(a\bar\mu)$; for full transported models only the "not conjugate" direction carries over (κ ∉ {0,2}) | `[ALG — SESSION; FMS symbolic P4 reported, OFN sampled verification]`. The universal κ statement rests on FMS P4, whose proof text OFN has not audited; OFN's independent reflection audit at κ ∈ {1, 1/2, 3} (controls solvable, reflected pairs GB = [1]) was executed by both co-owners |
| $\vert c\vert^2=A(t)^2+\tfrac4{81}(m-m_*)^2$, $m_*=\tfrac{17\sqrt3}{648}+\tfrac{\sqrt3}{9}t$: $\vert c\vert$ reads $m$ only up to $m\mapsto2m_*-m$ | Algebraic identity, checked symbolically by both co-owners |

Open: the other seven first-order moduli of the S₃ class that charts do not reach; jets beyond degree 5; κ ∈ {0,2}; a torus-invariant scalar reading the sign of $m-m_*$ (only if RRF requires it); the physical readout.
Action: reference-only. No theorem is registered in OFN, and no physical value or selection is implied. The basin boundary's dependence on the member is not proved.

<a id="rf-o10-03"></a>
- **RF-O10-03 — ER-2B and the C19 loophole** :: `RTG_ER2B_CONSOLIDATED_STUDY` v0.3.1 (noncanonical), A.4, C09, C11/C20, C19

The A.4 cubic identity was reproduced by OFN. ER-2B's "chirality attenuating" (C11/C20) refers to absolute $|S|$ and does not conflict with relative attraction (§5.5.6). The C19 subfamily $\tilde v=0$ is not excluded (OPEN-C19-L, §5.5.3).
Action: noncanonical context only.

<a id="rf-o10-04"></a>
- **RF-O10-04 — DYAD v6.4.12–v6.4.16 source row** :: DYAD v6.4.12 (formal centralizer, Corollary U), v6.4.13 ($J$, Lemma F, F1–F3, OPEN 20 B-6), v6.4.14 (OPEN 3a), v6.4.15 (OPEN 3b), v6.4.16 (SHA-256 `33c14c5c…59e0` per its release record, not re-hashed by OFN)

v6.4.16 is a **lifecycle-only** release: OPEN 3 CLOSED within its scope, OPEN 21 (`DYAD-OPEN-PRIMITIVE-PHASE-REMAINDER`) opened, OPEN 3c recorded as a model discrepancy, OPEN 20 unchanged, no scientific RID grade changed.
Action: notice N9 is answered at owner level when v0.10 is adopted; until then the session-level answer stands. N12 was not read for this draft.

<a id="rf-o10-05"></a>
- **RF-O10-05 — Genesis v2.8.9 adoption and its OFN-Q6 notice erratum** :: Genesis v2.8.9 release record; `GENESIS_V2_8_9_NOTICE_ERRATUM_OFN_Q6_v0_1.md`

The erratum withdraws the earlier "[ALG]-only" sentence on narrow Q6, agrees with the OFN corollary, and asks that the raw-family route cite the six-step theorem and that the κ = 1 wording be exact. Both are applied in §5.5.3.
Action: received. The corollary stays OFN-derived and OFN-registered on adoption.
"""
before('---\n\n<a id="ofn-artifacts-provenance"></a>', IMPS.lstrip('\n') + '\n', 'E12 §11.4-11.5')

# ---------------------------------------------------------------- E13 §12.1 evidence row
after("""| Accepted Draft-2 assembly and release checks | Original assembly evidence retained; the supplied Draft-2 validator is rerun, then recorded publication edits generate the final file | Direct baseline/candidate/final preservation, both exact diffs, deterministic replay and selected negative controls; no original physics code is executed |
""", """| *v0.10 Draft 1:* governing handoff v0.8.2 | SHA-256 `6e4fc3c3…564b1d`, computed by both co-owners | Single input for §5.5; co-owner handoff acceptance, not adoption |
| *v0.10 Draft 1:* OFN co-owner SESSION scripts | `iso_check.py` (`b92f6659…0d75e`), `iso_quadratic_nogo.py` (`91fd63f4…5308`), `transported_pq.py` (`2dcd4331…20bf6`), `transported_chiral_pq.py` (`09129ffc…73ac`), `transported_sim.py`, `basin_test.py`, `OFN_PSI_KAPPA_EXTENSION_v0_1.py` (`6566009c…5f88`), `OFN_PSI_KAPPA_ALL_MINOR_CHECK_v0_1.py` (`c56a01ac…a9e3`), `OFN_PSI_INVARIANT_C_CHECK_v0_1.py` (`18f10aa4…b114`), `OFN_PSI_INVARIANT_C_GAUGE_CHECK_v0_1.py` (`d3e5cedf…9781`), `OFN_PSI_REFLECTION_AUDIT_v0_1.py` (`e6d9b089…235a`), `OFN_STAB_F3_CHECK_v0_1.py` (`8b415461…e5ea9`) | Session evidence for §5.5 and RF-O10-02. The last six were executed by both co-owners; scripts are held by the PI and the co-owners, not attached to the project |
| *v0.10 Draft 1:* FMS ψ scripts and notes | Notes read; `FMS_PSI_QUINTIC_FINITE_INVARIANT_v0_1.py` (`ad44f66a…445f4c`) and `FMS_PSI_QUINTIC_REFLECTION_TEST_v0_1.py` (`5af23da9…f409`) not rerun by OFN | Reference-only (RF-O10-02) |
| *v0.10 Draft 1:* Genesis v2.8.9; DYAD v6.4.13–v6.4.16; RRF v0.8.3 | Genesis SHA computed by OFN; DYAD v6.4.16 and RRF hashes per their records; cited sections read | Source statements at owner grade; no certificate rerun |
""", 'E13 §12.1 rows')

# ---------------------------------------------------------------- E14 §12.3 custody rows
after("""| `RTG-OFN-HYP-FSP-U` | Registered OFN HYP | No capacity axiom adopted; same-sector compatibility question sharpened under its existing OPEN |
""", """| `RTG-OFN-DEF-TRIAD-MODEL-CONTRACT` | *Proposed v0.10*, OFN definition | Registers on adoption (O10-P2) |
| `RTG-OFN-DEF-STANDARD-C` | *Proposed v0.10*, OFN definition; order fixed by PI decision 18 Oct 2026 at session level | Registers on adoption (O10-P2) |
| `RTG-OFN-ALG-RAW-STANDARD-C-NOGO` | *Proposed v0.10*, OFN RESULT from ALG | Registers on adoption (O10-P4); OPEN-C19-L gap recorded |
| `RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT` | *Proposed v0.10*, OFN RESULT from THM + ALG | Registers on adoption (O10-P4); Genesis erratum concurs |
| `RTG-OFN-OPEN-TRIAD-CLASS` | *Proposed v0.10*, OFN OPEN | Registers on adoption (O10-P6) |
""", 'E14 §12.3 rows')

# ---------------------------------------------------------------- E15 §12.5 proposals
P = """
### 12.5 v0.10 Draft 1 Proposals and Assembly Record

| Key | Proposal | Effect if adopted |
|---|---|---|
| **O10-P1** | Source synchronization limited to the new material: Genesis v2.8.9, DYAD v6.4.13–v6.4.16 (v6.4.16 lifecycle-only), RRF v0.8.3; inherited pins unchanged | §11.4–§11.5 pins become active OFN references |
| **O10-P2** | Register `RTG-OFN-DEF-TRIAD-MODEL-CONTRACT` (§5.5.1, §5.5.2, §5.5.4) and `RTG-OFN-DEF-STANDARD-C` | Two new OFN definitions (eleven in total) |
| **O10-P3** | Declare class C a different conditional model under RRF v0.8.3 §0.3 and send the RRF model-contract-row request | Interface request issued; registration remains RRF's decision |
| **O10-P4** | Register the two local results of §5.5.3 under OFN custody | Four registered OFN local results in total |
| **O10-P5** | Adopt the scoped FMS disposition (§5.5.5) and the canonicity/modulus wording (§5.5.6–§5.5.7) with RF-O10-02 as reference-only | FMS receiving interface answered at owner level |
| **O10-P6** | Register OPEN-OFN-TRIAD-CLASS; add the reconciliation inputs to OPEN-OFN-3B, FRUSTRATION and OPA without status change | 21 OPEN records: twenty inherited statuses unchanged, one new ACTIVE |
| **O10-P7** | Interface actions: DYAD N9 answered at owner level; Genesis notice erratum received; RRF request (O10-P3) | Outbound notices to DYAD, Genesis, RRF, FMS |

**Assembly.** Draft 1 is generated by `build_ofn_v0_10_draft1.py` from the adopted v0.9 bytes (SHA-256 `5ae8fdab…9795`, matching its release record). The script applies anchored unique-match edits only; its checker confirms that every v0.9 line outside the replaced header block occurs unchanged and in order in this draft, and that all v0.9 RIDs, anchors and the twenty OPEN status lines are preserved. Edit log: E01 header; E02 title; E03 §0.1 boundary; E04 §0.3; E05 §0.4 row; E06 §5.5; E07 §9 intro; E08 OPEN-3B input; E09 FRUSTRATION input; E10 OPA input; E11 new OPEN; E12 §11.4–§11.5; E13 §12.1 rows; E14 §12.3 rows; E15 this section; E16 Appendix B record; E17 Appendix C entry; E18 footer.

**Review needed before adoption:** second co-owner review of this draft against v0.8.2; PI decisions on O10-P1–P7, individually or together. The OPEN-narrowing package of 13 October 2026 is a separate input.
"""
before('---\n\n<a id="ofn-historical-scenarios"></a>', P.lstrip('\n') + '\n', 'E15 §12.5')

# ---------------------------------------------------------------- E16 Appendix B record
after("""The inherited Appendix B records remain unchanged. Both v0.9 reconciliation entries are accepted on 13 October 2026 with O09-P1–P4; no source-owner proof grade, result custody or scientific-OPEN status changes through that acceptance.
""", """
### Proposed v0.10 records — Draft 1, 19 October 2026

**OFN10-C01 — FMS model-selection interface (proposed).** Original: v0.9 §12.4 records FMS-01 as covered by existing requirements and says any later definition expansion needs a separate proposal. Proposed: §5.5 adds the genuine relational-triad contract (Q1–Q6, Standard C, Q6-REG, class-C model contract), two local results, the scoped FMS disposition and one OPEN record, from the co-owner-accepted handoff v0.8.2. Withdrawn working-record claims stay withdrawn and are not imported: "normalizer changes affect only fifth and higher order"; "the remaining class members are not conjugate" (replaced by RF-O10-02); "|u|/|v| drifts monotonically in every run"; "|c| reads m given κ". No inherited record is changed.
""", 'E16 Appendix B')

# ---------------------------------------------------------------- E17 Appendix C entry
after("""## Appendix C — Version History
""", """
### v0.10 — 19 October 2026 — Draft 1 / adoption pending (not adopted)

- **Base and input:** adopted v0.9 (SHA-256 `5ae8fdab…9795`, verified against its release record) plus the co-owner-accepted handoff v0.8.2 (SHA-256 `6e4fc3c3…564b1d`).
- **Proposed content:** §5.5 genuine relational-triad model-selection contract; IMP-O10-01–05; RF-O10-01–05; OPEN-OFN-TRIAD-CLASS; reconciliation inputs to OPEN-OFN-3B, FRUSTRATION and OPA; O10-P1–P7.
- **Preserved:** every v0.9 line outside the header block, the nine definitions, FSP-U, the two local results, all guards and the twenty OPEN statuses. Inherited import pins are not re-pinned.
- **Not done:** no adoption, no owner-file change, no custody transfer, no physical selection. The 13 October OPEN-narrowing package is not integrated.
- **Editor:** Claude (OFN co-owner). Second co-owner review pending.
""", 'E17 Appendix C')

# ---------------------------------------------------------------- E18 footer
fi = s.index('*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.9*')
NEWFOOT = """*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.10 — DRAFT 1*
*ADOPTION PENDING. Not canonical; OFN v0.9 (adopted 13 October 2026) remains active. Proposals O10-P1–P7 await co-owner review and a separate PI decision.*
*Preserved v0.9 footer: "END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.9 / ADOPTED 13 October 2026; active canonical OFN, superseding v0.8. Reconciliation and OPEN sharpening only; definitions, scientific-OPEN statuses and technical custody are unchanged. Programme v1.3 synchronization is the next consumer action. FMS pilot closeout is not enacted by this release."*"""
NEWFOOT = NEWFOOT.replace('DRAFT 1*\n', 'DRAFT 1*  \n').replace('decision.*\n', 'decision.*  \n')
s = s[:fi] + NEWFOOT + '\n'; log.append('E18 footer')

open(OUT, 'w', encoding='utf-8', newline='\n').write(s)

# ---------------------------------------------------------------- checker
import re
out_lines = s.split('\n')
hdr_lines = set(old_header.split('\n'))
footer_old = {'*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.9*  ',
              '*ADOPTED 13 October 2026; active canonical OFN, superseding v0.8. Reconciliation and OPEN sharpening only; definitions, scientific-OPEN statuses and technical custody are unchanged. Programme v1.3 synchronization is the next consumer action. FMS pilot closeout is not enacted by this release.*',
              '# RTG_ONTOLOGICAL_FOUNDATIONS_v0.9'}
hs = base_txt_pre = raw.decode('utf-8')
hstart = hs[:hs.index('**Title:**')].count('\n'); hend = hs[:hs.index('## Local Tag Aliases')].count('\n')
keep = [l for k, l in enumerate(base_lines) if not (hstart <= k < hend) and l not in footer_old]
# in-order subsequence check
it = iter(out_lines); missing = [l for l in keep if not any(l == x for x in it)]
ok_seq = not missing
rid = lambda t: sorted(set(re.findall(r'RTG-OFN-[A-Z0-9-]+', t)))
base_txt = raw.decode('utf-8')
rid_ok = set(rid(base_txt)) <= set(rid(s))
anchors_ok = set(re.findall(r'<a id="([^"]+)"', base_txt)) <= set(re.findall(r'<a id="([^"]+)"', s))
st = lambda t: re.findall(r'^Status: (ACTIVE|PARTIAL)(?! \(proposed\))', t, re.M)
status_ok = st(base_txt) == st(s) and len(st(s)) == 20
newrids = sorted(set(rid(s)) - set(rid(base_txt)))
print('edits:', len(log), log[-1])
print('v0.9 lines preserved in order (outside header/footer):', ok_seq, len(keep), 'missing', len(missing))
print('v0.9 RIDs preserved:', rid_ok, '; anchors preserved:', anchors_ok)
print('inherited OPEN status lines:', len(st(s)), st(s).count('ACTIVE'), 'ACTIVE /', st(s).count('PARTIAL'), 'PARTIAL; unchanged:', status_ok)
print('new (proposed) RIDs:', newrids)
print('output sha256:', hashlib.sha256(s.encode('utf-8')).hexdigest(), 'lines', len(out_lines))
sys.exit(0 if (ok_seq and rid_ok and anchors_ok and status_ok) else 1)
