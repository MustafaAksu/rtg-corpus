# Intrinsic strobe-boundary structure — Stage 1: signed history algebra and affine-clock obstruction

**Date:** 26 November 2026.
**Status:** SESSION / NONCANONICAL, proposed for independent review; no RID, owner adoption, new DSN edition, or physical selection.
**Question:** Can quarter-strobe truncation and binary register folding arise from one admissible relational composition mechanism?
**Stage 1 verdict:** A common signed-history algebra realizes the transport, affine register and charge boundary at the mathematical level. The full affine clock is not identified by the linear folding. In odd-s sectors the full signed-lattice path image is strictly smaller than the folding kernel; primitive projection hides the missing component. The physical common-mechanism question remains OPEN.

## 1. Source and scope

- PI-accepted NONCANONICAL Gaussian record, PR #398, merge 65a42d1ba4725caf42e9f8b2d3017bf3f714a15c: records/ofn/OFN_GAUSSIAN_STROBE_REGISTER_SESSION.md, SHA-256 ac6d7e096f6b0f0c3b2507ec7931d2e8f2268fedde152522a88047e5c6e82701. Read in full, including §3 charge paths, §§4–6 Gaussian ideal and quotient, and Claude's review. Its rejected two-path-difference mechanism remains rejected.
- Binary Recognition wrap-up, PR #183 merge 1da597feb194837f56ad5d632c3ddd36c9f80abc, §2, §3F (fixed register, character and 2-primary retention). SESSION, not an owner theorem.
- OFN v0.13, ofn-v0.13, SHA-256 4a2d266bf89cd2130e901b7543bacbaf7fa3e844c60e355a2e3c23ef4f075a49. Targeted reading of §1 and SG-OFN-STATE/PRESENTATION/SELECTION/TIME/INFORMATION: full state, presentation covariance, and clock contract remain necessary.
- DYAD v6.4.24, dyad-v6.4.24, SHA-256 10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16. Targeted §6.11, DYAD-THM-Q403-PHASELAW: named raw W-frame cubic, s=p/4, charges (-3,-1), (-1,-3) and direct charge -4.
- DZT v0.19, dzt-v0.19, SHA-256 2b959f46b8e23363beac087183caf4946d63d1e8d5ac597bdb7d9230143bf6ce. Targeted §6.3, DZT-THM-CASCADE-NORM-LAW, conditional on the DYAD phase-law input. This owner result is not re-owned.

EV-SRC-READ / EV-HASH: governing tags and adoption/release records checked against the retrieved owner bytes, not a full re-audit. Methodology v1.4 and CONVENTIONS.md inspected for applicable evidence and branch rules. No prior owner extractor or certificate rerun. The following proofs are new SESSION deductions from specified algebraic models, without a mathematical novelty claim.

## 2. Common signed history algebra and the charge composition

[THM] [SESSION] Fix s>=1, n=2s, p=4s. Use the free integral signed-history ring
$$\Lambda=\mathbb Z[t]/(t^n+1),\quad t^{n}=-1,\quad t^{p}=1.$$
Write U for multiplication by t and F for the affine update F(P)=tP+1. For the complete binary register X_n embedded as P_X=sum_{j<n}x_j t^j, this update acts exactly as the fixed Binary Recognition F_n (the constant term is 1-x_{n-1}). For two histories the difference transforms by U alone: F(P)-F(Q)=t(P-Q). This distinguishes a relative displacement from the affine history itself.

There is a common primitive character evaluation e:Lambda->R_p=Z[L], L=zeta_p, t->L. It is well-defined because L^n=-1 and is onto. The centered readout Z(P)=1-(1-t)P satisfies Z(F(P))=t Z(P); its evaluation reproduces the wrap-up's characteristic-zero Z_n. The map Z on Lambda is injective because 1-t is a non-zero-divisor (1 is not a root of t^n+1). This is not a claim of injectivity after spectral evaluation or reduction.

For any charge k in Z use the auxiliary affine composition (u,a)(v,b)=(uv,a+u b) of unit multipliers and translations in Lambda. Then
$$(t^k,1)^s=(t^{ks},G_s(k)),\qquad G_s(k)=\sum_{j=0}^{s-1}t^{kj},$$
$$(1-t^k)G_s(k)=1-t^{ks}.$$
These are charge representations of the same signed transport algebra, not independent choices of a physical generator for each k. The strobe boundary d=1-t^s has d^2=-2t^s; thus (d)^2=(2). The boundary 1-t^{ks} generates (d) for odd k, (2) for k=2 mod 4, and zero for k=0 mod 4.

Let M=Lambda/2Lambda=F_2[t]/(t^n+1), with its bit coefficient identification X_n. Imposing relative s-step transport equivalence gives the universal linear quotient annihilating (1-U^s)M:
$$M/dM\simeq\mathbb F_2[t]/(t^s+1),\qquad B(X)_j=x_j\oplus x_{j+s}.$$
Indeed Lambda/(d) imposes t^s=1 and 2=0, and the two blocks fold. Its kernel in M is dM, exactly the doubled registers (Y,Y), and the induced affine update is F_s. The same d is sent by e to 1-i, the Gaussian boundary. This is an explicit common algebraic carrier and composition of transport/translation; the physical admissibility of this carrier and its clock are not established.

[THM] [SESSION] [selection conditional] For any positive r dividing n the analogous ideal d_r=(1-t^r)Lambda has index 2^r, since Lambda/d_r=F_2[t]/(t^r+1). Multiplication by 1-t^r is injective (its roots and those of t^n+1 are disjoint). Hence [Lambda:d_r^2]=2^{2r}; d_r^2=(2) implies r=n/2=s. The converse follows from d^2=-2t^s. Thus an exactly two-layer ideal split of 2 selects the quarter-strobe within this divisor family **if** that split is imposed. The signed-history law itself does not physically select the split or this strobe over all other divisor choices.

## 3. Affine-clock obstruction and the maximal affine s-return readout

[THM] [SESSION] [scope: all X_n, affine-linear readouts over F_2] The linear folding is not a quotient identifying the full affine s-step dynamics:
$$BF_n=F_s B,\qquad BF_n^s=C_s B\ne B.$$
Here C_s complements every bit, never the identity. In M, F^s(P)=t^s P+g_s, with g_s=G_s(1). The set of displacement vectors F^s(P)-P is dM+g_s. Its linear span is dM+F_2 g_s, of dimension s+1, since B(g_s) is the all-ones vector, nonzero. It is the ideal generated by g_s: d=(1-t)g_s, and multiplication by t preserves the span. An affine-linear map is invariant under F^s on every P iff its linear part annihilates this span. Therefore the maximal such affine factor is the quotient
$$M/(g_s)\simeq\mathbb F_2[t]/(1+t+\cdots+t^{s-1}),$$
with 2^{s-1} states (one for s=1).

A concrete affine realization is H_s(X)=1-(1-t)P_{B(X)} modulo t^s+1 in F_2[t]. Multiplication by 1-t on the folded ring has kernel spanned by g_s (polynomial divisibility by (t^s+1)/(t+1)); thus H_s has exactly the above fibres, each of size 2^{s+1}. It satisfies
$$H_s F_n=tH_s,\qquad H_s F_n^s=H_s.$$
This is universal only for the declared affine-linear readout class, not for arbitrary set maps or physical observations. Native parity descends through H_s iff s is even: doubled-register kernel has even parity, while the extra g_s identification changes it by s mod 2. The map B alone always preserves native parity.

On the phase quotient C=R_p/2R_p, the induced affine map is P->LP+1. For p not a power of 2, 1-L is a unit (Phi_p(1)=1); the affine origin can be shifted to P_*=(1-L)^{-1}. Its s-step affine defect lies in the Gaussian layer J=(1-i)C because G_s(1)=(1-i)/(1-L). Hence C/J is the maximal affine s-return factor in this spectral carrier. When p is a power of two, E_n is faithful and the extra one-bit quotient remains necessary: the maximal affine factor has 2^{s-1} states. In the non-power-of-two case native parity has already been lost through E_n. Thus quotient equivalence of the spectral affine clock does not recover the complete recognition state.

## 4. Full-lattice ordered sums: the missing parity-sensitive layer

[THM] [SESSION] Define in Lambda, without division,
$$S_s(u,v)=\sum_{0\le j<k<s}t^{uj+vk},\qquad D=(1-t^{-1})(1-t^{-3}).$$
This is the lift of the two charge-path sums in the named DYAD cubic, not a lift of the entire nonlinear map or its rational coefficients. Direct finite summation gives
$$(1-t^u)S_s(u,v)=G_s(v)-G_s(u+v).$$
For (u,v)=(-3,-1),(-1,-3), let P_{u,v}=D S_s(u,v). Then
$$P_{u,v}=1-t^{sv}-(1-t^v)G_s(-4).$$
The full-lattice cancellation G_s(-4)=0 holds iff s is even. Proof: in Lambda tensored with Q the polynomial t^n+1 has distinct roots. The geometric sum vanishes on every root except those with t^4=1, where it equals s. When s is even no such root satisfies t^n=-1; when s is odd t=+i,-i do, so precisely the Phi_4 component survives. Lambda is torsion-free as a Z module. For s>=2 the primitive p-th root has order p>4 and the corresponding sum is zero after e, as in the reviewed DYAD charge calculation. The case s=1 here is only an algebraic boundary/control, not an adopted DYAD cascade formula.

[THM] [SESSION] Write d also for its reduction modulo 2. The full-register multiplication image of each denominator-cleared path is exactly
$$\operatorname{im}(m_{\overline P_{u,v}}:M\to M)=
\begin{cases}
dM=\ker B,&s\ \mathrm{even},\\
d(t+1)M=\{(Y,Y):\pi_s(Y)=0\},&s\ \mathrm{odd}.
\end{cases}$$
The two dimensions are s and s-1. This gives a genuine sector-resolved comparison **before** primitive projection, not a substitution of equal norms.

Proof: for even s the full-lattice G_s(-4)=0, and 1-t^{sv}=d modulo 2 for odd v (t^{2s}=1). For odd s, d=t^s+1 is squarefree over F_2 and M=F_2[t]/d^2. In the primary factor (t+1)^2 set epsilon=t+1, epsilon^2=0. Then t^{-4}=1, G_s(-4)=1 (s odd), and both 1-t^{sv} and 1-t^v are epsilon. Thus P_{u,v}=0 in this factor. In every other primary factor of d^2, 1-t^{-4} is a unit because in characteristic 2 its only possible root is 1. Hence G_s(-4)=0 there, and P_{u,v}=d. By CRT the generated ideal in M is d(t+1)M. The injection F_2[t]/d -> dM, Y -> dY, is exactly duplication; its even-parity subspace is the ideal (t+1). This proves the formula, including s=1. For odd s>=3, 1-L is a unit in R_p, so e modulo 2 identifies the images of dM and d(t+1)M with the same Gaussian layer J. The prior record's spectral image equality is therefore compatible with the strict full-register deficit. The missing dimension is the parity of the duplicated block Y, not the parity of the whole doubled vector (which is always zero).

[THM] [SESSION] [obstruction] If s is odd, no F_2-linear quotient of M through which native parity descends can make the charge -4 summation vanish as an operator: augmentation of G_s(-4)P is s times augmentation of P, equal to augmentation of P mod 2. More generally for any s, in any U-equivariant linear quotient with a nonzero descended parity functional, 1-U^k cannot be surjective (for any k), since parity annihilates its image. In particular D cannot be inverted on such a quotient. A carrier retaining parity cannot simply use the primitive unit-sector inversion as a common full-state operation. These are linear-readout obstructions, not no-go theorems for arbitrary nonlinear enlarged carriers.

## 5. What this does not derive

[THM] [SESSION] [conditional on the generic ideal equality in PR #398] At the fixed owner normalization in the generic DZT sector, (Q_p)=g^{-1} in R_p, g=(1-i)R_p. In R_p[Q_p] the generator 1-i becomes invertible: (1-i)Q_p is a unit in R_p. There is therefore no unital homomorphism from this enlarged scalar ring to a nonzero ring that kills 1-i. Direct reduction of the unscaled cascade coefficient to the Gaussian fold quotient is obstructed. This does not prohibit a denominator-cleared readout or a specified filtered integral lift; rational rescaling changes the premise.

The common Lambda model gives the signed shift and the strobe charge sums without two unrelated boundary definitions, but supplies neither a common physical event rule nor the DYAD nonlinear generator. The charge-path lift is an algebraic observation of the named raw coefficient calculation; no exact full nonlinear intertwiner, physical clock, gauge selection, or amplitude normalization is obtained. The earlier local periodic-source obstruction in Binary Recognition §3B is not bypassed. The different sectors and the affine-clock obstruction must not be hidden by a numerical match.

[OPEN] **Stage 2 — parity-retaining graded realization.** For odd s>=3, test an explicitly typed observation carrier retaining the Phi_4 sector along with the primitive Phi_p sector. The first carries the parity-sensitive lower component; the second supplies the named cascade cancellation. Seek a single state/update/observation contract in which the two sector roles follow from a composition law rather than independent readout postulates. Require a well-defined affine clock, retention of the named recognition bit, recovery of the existing raw charge coefficient in its own frame (or an explicit transport), and an exact reduction or controlled error with stated domain. The above obstructions reject a naive identification of the two clocks or primitive unit inversions on a parity-preserving quotient. No physical selection or owner OPEN closure is proposed; another failed route may be the correct next result.

## 6. Native exact checks and requested review

EV-CODE / EV-RUN / EV-COVER: Python 3 / SymPy 1.14.0, native run 26 Nov 2026. A development assertion evaluating i with Python complex powers failed due to floating arithmetic; it was replaced by integer real/imaginary evaluation using exponents modulo 4 before freezing this script. The final checker uses integer signed-lattice convolution, bit-vector operations and exact polynomial arithmetic. Not an owner extractor replay.

- s=1..7: exhaustive 21,844 full binary states, signed affine update, fold covariance, complement strobe, affine displacement span, centered readout and parity.
- s=1..64: 576 geometric charge identities (k=-4..4), 128 ordered boundary identities and 128 full-register image gcd checks. The odd/even cases act as exact contrast controls.
- p=4,8,...,256: 64 spectral quotient checks, including 7 power-of-two and 57 other lengths; odd-s full-lattice survival and primitive charge cancellation at p>=8. No large native DYAD campaign.
- The all-s statements are proved above; finite checks do not supply their quantifiers. The additional divisor-selection and localization implications are written proofs, not finite regression claims.

Received unchanged on upload/ofn-strobe-boundary-stage1-20261126, commit fbe559978bdaf9761512444a2c9024040653ed6d, hash-checked before exact-blob placement.

| File under evidence/ofn/intrinsic_strobe_boundary/ | SHA-256 |
|---|---|
| scripts/strobe_boundary_stage1_check.py | 20de515656436b17de8257c3ef700dce1c04eb08abbc76858b3f900e113f5fe7 |
| runs/strobe_boundary_stage1_output.txt | ccb3105ebc08f6f75dc417ad46a4ca011b43e0491477ad6168e8d873bd0f3623 |

Reproduce: python3 evidence/ofn/intrinsic_strobe_boundary/scripts/strobe_boundary_stage1_check.py

Independent review requested: §§2–4 (especially universality restricted to affine-linear readouts, odd-s primary factor, block parity and full-state versus spectral image), §5 scope and finite replay. All results remain SESSION/NONCANONICAL; PI adoption/merge and cross-stream routing remain separate. No canonical file, existing evidence, pipe or tag changes.

*END OF STAGE 1 SESSION RECORD.*
