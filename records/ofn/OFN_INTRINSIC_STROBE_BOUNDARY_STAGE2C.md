# Intrinsic strobe-boundary structure — Stage 2C: full-register monodromy and presentation obstruction

**Date:** 27 November 2026.
**Status:** SESSION / NONCANONICAL. ChatGPT prepares; Claude independent review requested; PI decides. No owner RID, canonical adoption, physical gauge selection or owner OPEN closure.
**Decision:** Unrestricted base-preserving full-register-dependent fibre charts admit a formal product reduction for every parity-gated family with the declared common linear return. Every finite jet admits polynomial analytic chart representatives. For the specific Stage 2B nonzero degree-q perturbation, neither complement-preserving charts (trivial complement action on both fibres) nor charts with an autonomous target preserving the owner linear conjugacy class admit even a q-jet product reduction. This separates mathematical removability, admissibility and physical selection.

## 1. Source and scope

Main checkpoint cba0213e7ef04e6126ce87eac9c378c18f2ab30c; CONVENTIONS.md read in full. Stage 2B, merged PR #413 at 037a2d0fd3b95db75b6f0baa233fe056d219048f, final head b8874e45fbf2f5a5237bb88cf793a80f59d6632a; records/ofn/OFN_INTRINSIC_STROBE_BOUNDARY_STAGE2B.md, blob 2b7277dcc9b0b223e7a02a7e058b0635787ce891, recorded SHA-256 117923ace9f6c1db985e875c34d5efe8ae5078bc5e34714f3880cd3d7b15bbf9. Full record and independent review #415 read during entry; §§2–6 and evidence boundary rechecked. Earlier Stage 1 CRT splitting and Stage 2A norm non-identification remain scoped SESSION findings. Binary Recognition #183 fixes the register; its period conclusion is reproved below. Claude's PI-supplied 27 November response independently confirms the preliminary formal-root construction, gives the complement proof of the period constraint, emphasizes finite jets, and proposes complement-preserving admissibility. This response is session-supplied input, not a repository review or approval of this record. The complement conjecture is proved below, not taken as an assumption.

Owner sources (targeted claim reading; tag target and published SHA-256 from annotated tag and BASELINE; not fresh full-file SHA-256 computation):
- RECOG v0.3.27, tag recog-v0.3.27, target 7bad433b1cea32c34c4c24f24c26b895998e735d, SHA-256 19556f913f51b98599faa6ad88c363dda0a278345677f3bd69f3b892d810e1f1; release record records/recog/RECOG_v0_3_27_RELEASE_RECORD.md. §6.10, RECOG-ALG-NU3-CLOSED-FORM and RECOG-ALG-LEADING-RETURN-EQUIVARIANCE. This supplies the owner cubic in the Z frame, not a physical origin.
- DYAD v6.4.24, tag dyad-v6.4.24, target f0af6392ed560b55aedc640bc166f0b87f612f7c, SHA-256 10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16; release record records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md. §6.9, DYAD-ALG-BRIDGE-LEMMA and DYAD-ALG-KP-FRAME-SCALE; §6.11 DYAD-THM-Q403-PHASELAW for Stage 2B's separate cubic strobe diagnostic (not the cubic full-return coefficient used below).
- OFN v0.13, tag ofn-v0.13, target 3f266eb4337c10d6e88a0ea90527dbe732922319, SHA-256 4a2d266bf89cd2130e901b7543bacbaf7fa3e844c60e355a2e3c23ef4f075a49; §1, SG-OFN-STATE, PRESENTATION, SELECTION, TIME and INFORMATION; release record records/ofn/OFN_v0_13_RELEASE_RECORD.md. Complement gauge is not selected.
- Methodology v1.4, tag methodology-v1.4; §12.2 evidence separation and repository conventions govern. DZT v0.19 is the background diagnostic owner; its conditional norm law is not used as a premise of the obstruction below.

EV-SRC-READ: targeted owner statements and release identity checks, no owner certificate replay. No novelty claim; LIT dependencies: none.

## 2. The model and orbit-root criterion

[DEF] [SESSION] Let p=4s>=12, n=p/2=2s=hm, h=2^{v_2(n)}, m odd. Let X_n be the full twisted binary register, F_n its shift with complement of the last bit, C_n the bitwise complement and sigma=(-1)^pi_n. Thus sigma(F_n X)=-sigma(X), sigma(C_n X)=sigma(X) since n is even. The fibre maps f_+,f_- fix the origin, are real local diffeomorphisms (formal germs or invertible finite jets as appropriate), and share the linear part R(W,V)=(LW,L^{-1}V), L=zeta_p, V=conjugate(W). Use A=f_- o f_+, B=A^h; composition is right to left. Product reduction means H(X,z)=(X,H_X(z)), H_X(0)=0, H_{F_n X} o f_{sigma(X)}=g o H_X for a single autonomous germ g. The base and primitive step index are fixed. Nothing here selects an admissible physical chart group, a clock or a fibre carrier.

[THM] [SESSION] Every orbit length d_X satisfies 2h | d_X | 2n; k_X=d_X/(2h) is an odd divisor of m. Proof (Claude's simpler complement argument): F_n^n=C_n, F_n^{2n}=id and C_n has no fixed point. Hence d_X | 2n but d_X does not divide n. Its 2-adic valuation must be v_2(n)+1. Also F_n^{d_X/2}X=C_nX, because n is an odd multiple of d_X/2 on this orbit. The shortest length 2h is attained: take m successive blocks of length h alternating all-zero and all-one, starting and ending with all-zero. F_n^h complements this state, so its orbit length divides 2h and is at least 2h by the first argument. Every orbit contains positive-parity states.

[THM] [SESSION] In any category of invertible germs or invertible finite jets closed under composition and inverse, unrestricted full-register product reduction exists iff B has a 2h-th root in that category (up to common target conjugacy). Necessity: choose a positive-parity state on a shortest orbit and normalize the target by its chart so that H_X=id. The orbit equation then gives g^{2h}=B. Sufficiency: choose a positive-parity start on each orbit, H_X=id, and set H_{F_n X}=g o H_X o f_{sigma(X)}^{-1} along the orbit. At its end H returns to id since the source monodromy is A^{d_X/2}=B^{k_X} and g^{d_X}=B^{k_X}. The construction covers the full register, not just one long orbit.

[THM] [SESSION] Unrestricted reduction exists formally, for every such parity-only gated family, provided R^p=id (the declared R satisfies this). B^m=A^n is tangent to the identity. Choose integers a,b with 2ha+mb=1. Then
$$g=B^a\circ\exp\!\left(\frac{b}{2h}\log(B^m)\right).$$
The log denotes the unique formal tangent-to-identity iterative logarithm, equivalently the logarithm in the nilpotent tangent-to-identity finite-jet group at each order. B commutes with B^m, hence with its logarithm and all formal powers (by uniqueness, or the substitution-operator log series). Thus
$$g^{2h}=B^{2ha}(B^m)^b=B.$$
For the primitive rotation R, Dg(0)=R^{2ha} has order m: gcd(a,m)=1 for m>1; m=1 yields the identity. This is a different linear type from R of order p. At any finite order k the same construction in the finite jet group gives compatible charts. Their polynomial truncations are analytic local diffeomorphisms and satisfy the conjugacy equations modulo degree k+1, not necessarily exactly. For a C^k family use only its k-jet. The result does not establish convergence of the infinite formal series or an exact C-infinity/analytic root. Merely asserting that a common R has some finite order unrelated to p does not establish B^m tangent to identity; the order-dividing-p premise is retained.

[THM] [SESSION] For the conditional complement quotient (X,z)~(C_n X,z) with identity fibre action on source and target, allowed base-preserving charts satisfy H_{C_n X}=H_X. This quotient is well-defined since sigma(C_n X)=sigma(X); the quotient orbit lengths are d_X/2=h k_X, and h is even. The identical orbit argument gives the necessary and sufficient root condition g^h=A^{h/2} after a common target conjugacy, by using the shortest quotient orbit. The condition also implies g^n=A^{n/2}. This gives Claude's suggested equation without trying to combine equations for roots conjugated by different orbit charts. No physical assertion that complement acts trivially on a continuous fibre is made.

## 3. Full-return jet and the nonradial channel

[THM] [SESSION] Specialize to the Stage 2B analytic comparator
$$G_\sigma(\rho)=e^\rho-1+\epsilon\sigma\rho^q,\quad S(\eta)=\sin\eta,\quad q=n-1\ge5,\quad \epsilon\ne0,$$
with the same raw shear and W frame as Stage 2B. Let f_0 denote the unperturbed owner family member, not an additional parity, and P=A^n the full p-step fibre monodromy starting at positive parity. Then in the raw W component
$$j^q(P-f_0^p)=c_* V^q,\qquad
c_*=p\epsilon\kappa_{p,q},\qquad
\kappa_{p,q}=\frac{(L-1)L^{q-1}}{(1+L)^q}\ne0.$$
The V component is the real conjugate. Proof: the first difference is at degree q, so insertion into or of any other nonlinear term raises its degree. In the rotation-removed W map the degree-q one-step source is epsilon sigma (L-1)rho^q/L, rho=(W+LV)/(1+L). For W^u V^v with u+v=q, its time weight including alternating sign at step j is L^{(u-v-1+n)j}=L^{2uj}. The sum over p steps vanishes unless u=0 in the range 0<=u<=q<n. The surviving term is as stated. In particular the first modification to the entire full-return jet is not just a pure-V evaluation; it is exactly the displayed homogeneous difference. For a finite block of ell steps the pure V^q rotation-removed difference is ell sigma epsilon kappa_{p,q}, including A, A^{h/2}, B, the quarter strobe and full p-return as applicable.

The owner map f_0 has a common tangent-to-identity polynomial normalizing chart through degree q: the usual homogeneous conjugacy operator with multiplier L^{u-v}-L eliminates every term whose charge u-v-1 is nonzero modulo p. Since q=n-1<p-1, the only allowed charges through q are zero. In this chart f_0 and its powers are rotation-equivariant through q, with the conjugate real component transported along with the W component. Conjugating two maps with common lower jets and a first difference at q by the same tangent-to-identity chart preserves their homogeneous difference at q (by degree counting). Consequently in the normalized common coordinates,
$$P(W)=W+\mu W|W|^2+\sum_{k=4}^{q} P_{k,0}(W)+c_*\overline W^{\,q}+O(|W|^{q+1}),$$
where all P_{k,0} are rotation-equivariant homogeneous maps of degree k. The quadratic term vanishes; rotation equivariance at even degrees forces zero. The complex cubic mu is the full p-return coefficient, not the DZT quarter-strobe coefficient Q_p. The common chart does not change the cubic coefficient of the identity-tangent full return.

[ALG] [SESSION] [depends on: RECOG-ALG-NU3-CLOSED-FORM, DYAD-ALG-BRIDGE-LEMMA, DYAD-ALG-KP-FRAME-SCALE] Write theta=2pi/p, x=cos(theta), and let f(L)=L^{-1}nu_3(L) in the RECOG Z frame. Its closed form at the inspected owner pin is
$$f(L)=-\frac{L^5-L^4-L^3-2L^2+1}{2L(L-1)(L+1)(L^2+L+1)}.$$
Then
$$\Re f(L)=\frac{x-1}{2},\qquad
\Im f(L)=\frac{2x^3+x^2-3x-1}{2\sin(\theta)(1+2x)}.$$
These follow from half-sum and half-difference with L->L^{-1}; the checker verifies the rational identities symbolically. On p>=12, sqrt(3)/2<=x<1; the numerator polynomial is increasing there (derivative 6x^2+2x-3>0), and at x=1 equals -1. Both parts are strictly negative. The positive scale gives mu=p tan^2(pi/p) f(L) in the W frame. Hence write mu=a_0+i b_0 with a_0<0 and b_0<0. This is a point-of-use deduction from the owner cubic formula, not a claim that every parity-gated family shares its signs or a finite-amplitude contraction theorem.

## 4. Centralizer lemma: the missing step in the complement conjecture

[THM] [SESSION] Suppose P is an identity-tangent real planar q-jet, q=n-1>=5, with the structure in §3, c_*!=0 and a_0 b_0!=0. Any invertible origin-preserving real q-jet g commuting with P must have linear part S(W)=omega W, |omega|=1, and omega^n=1. This is a necessary condition; no sufficiency claim for every omega or centralizer classification.

Proof, linear step. Compare cubic terms in g P=P g:
$$S X_3(W)=X_3(SW),\qquad X_3(W)=\mu W|W|^2.$$
Regard X_3 as a polynomial vector field. Its divergence is 4a_0|W|^2. Under linear intertwining, divergence at SW equals divergence at W by similarity of derivative matrices. Since a_0!=0, S preserves the Euclidean norm, hence is orthogonal. A reflection conjugates multiplication by mu to multiplication by conjugate(mu), incompatible with b_0!=0. Thus S is rotation by omega.

Proof, nonlinear step. A homogeneous real degree-d vector field H in polar coordinates (r,phi) can be written as r^d U(phi) partial_r + r^{d-1} V(phi) partial_phi. The cubic field is a_0 r^3 partial_r + b_0 r^2 partial_phi. The Lie bracket [X_3,H] has components
$$r^{d+2}((d-3)a_0 U+b_0 U'),\qquad
r^{d+1}((d-1)a_0 V+b_0 V'-2b_0 U).$$
Here U,V are finite Fourier series; harmonic 0 means rotation equivariance. On every nonzero Fourier mode k the diagonal multipliers are (d-3)a_0+ik b_0 and (d-1)a_0+ik b_0. Both are nonzero since b_0!=0. Therefore the bracket has no non-equivariant kernel on any homogeneous degree d, and preserves each angular mode. This also applies to degree 3, which is why the nonzero imaginary part is used; it is not enough merely to know that the cubic is nonzero.

Write J=S^{-1}g=id+J_2+...+J_q and P'=S^{-1}PS. Then J P=P' J. P and P' have identical rotation-equivariant lower jets through q-1. Induct over d=2,...,q-3. At degree d+2 compare the non-equivariant part: all contributions using already equivariant J_j (j<d) and lower P terms are equivariant, and J_{d+1},J_{d+2} cancel because P and P' have identity linear and zero quadratic terms. The only non-equivariant dependence on J_d is its bracket with X_3 (up to sign). Hence J_d is equivariant by the Fourier lemma. At d=q-2 compare degree q in the same equation, now allowing P_q-P'_q. The bracket with X_3 preserves angular weights. The W component of a degree-d polynomial map has weights u-v-1 in [-d-1,d-1]; the conjugate component gives the opposite weights. Equivalently these are the Fourier indices of its polar components. For d=q-2 the absolute weight is at most q-1<n. Thus this bracket cannot supply weight -n, and all already-equivariant contributions have weight 0. Direct J_{q-1},J_q cancel. Project the W equation to weight -n, whose only degree-q monomial is V^q. It requires
$$c_*(1-\omega^{-n})=0,$$
since the coefficient of S^{-1}P(SW) is c_* omega^{-q-1}. Therefore omega^n=1. QED. The argument takes place entirely in q-jets; no q+1 differentiability or infinite-order convergence is required.

## 5. Two presentation obstructions

[THM] [SESSION] For the Stage 2B comparator with epsilon!=0, there is no q-jet product conjugacy by full-register-dependent origin-preserving charts with either of the following restrictions:
(A) complement chart equality H_{C_n X}=H_X (identity fibre action on source and target);
(B) autonomous target linear part real-linearly conjugate to the owner R, even without restriction (A).

Proof: take one positive-parity source state and normalize the target chart at that state to identity by a common target change. Since F_n^p=id, g^p=P=A^n as q-jets. Thus g commutes with P. Make the common owner normalization in §3 on source and target (the chart at the chosen start remains identity, and linear conjugacy class is unchanged). Apply §4 to obtain (Dg(0))^n=I. Under (A), the n-step equation and H_{C_n X}=H_X give g^n=A^{n/2}; taking derivatives gives (Dg(0))^n=R^n=-I, contradiction. Under (B) the same -I follows directly by linear conjugacy to R. This proves both independently, including m=1 where the linear part of the full monodromy alone cannot force conformality. The quotient root criterion in §2 is an equivalent formulation of (A); no assumption that a prospective root starts in an R-equivariant normal form is used.

[ALG] [SESSION] For unrestricted charts a product target normalized at a shortest positive-parity orbit necessarily has rotational derivative omega satisfying omega^{2h}=L^{2h} and omega^n=1. The explicit formal construction in §2 has order m and satisfies both conditions. No claim that every multiplier satisfying these necessary conditions admits a root. This reconciles the Stage 2B parity-only obstruction with the unrestricted full-register construction: the latter changes the linear rotation type and cannot preserve the stipulated trivial complement action. A passive transport that also changes the fibre action of complement is not ruled out by (A). Neither (A) nor (B) has been selected as a physical admissibility principle by OFN/RRF.

## 6. Disposition and next research gate

- [THM] [SESSION] A parity-only gate with common R^p=id cannot yield formal irreducible content under unrestricted full-register charts of this type. At every finite order such content can be removed using analytic polynomial chart representatives. This does not imply exact smooth or analytic product reduction, or removal under all observable-preserving contracts.
- [THM] [SESSION] The explicit Stage 2B comparator has irreducible q-jet content under each of the two conditional presentation restrictions. The DZT cubic norm remains blind to this scoped obstruction; no modification of its owner theorem or the Stage 2A scope follows.
- [OPEN] Physical admissibility: is complement a gauge, and if so with what action on the fibre? Is the owner primitive linear conjugacy class retained by the physically admissible observation contract? Neither criterion is forced by the signed history ring or by the current OFN commitments. Keep complete-state/readout, gauge action and clock separate.
- [OPEN] Intrinsic origin: derive an actual relational composition producing a nonzero admissible invariant, rather than imposing sigma rho^q. If unrestricted formal product reduction is the intended equivalence, any new parity-only gate with the common R^p=id is insufficient; a richer X-dependent law with incompatible orbit monodromies or a nonperiodic base is a possible route, not a selected mechanism. The p-dependent q, free epsilon and independent continuous fibre remain unselected. The exact analytic/smooth root question is separate and not a prerequisite for the q-jet comparison.

## 7. Evidence and requested review

EV-RUN / EV-CODE / EV-COVER: native Python with SymPy 1.14.0 in the ChatGPT execution container, from /tmp with isolated Python invocation, exit 0, 27 November 2026. The checker uses integer combinatorics, symbolic rational identities and exact cyclotomic-field arithmetic. The real-coordinate raw Taylor recurrence is a new bounded implementation of the same mathematical extraction method as Stage 2B, not an independent engine or owner replay. Coverage:
- n=2,4,...,14: 21,844 states; complement identity, period divisibility, quotient orbit lengths and attained shortest orbit.
- p=12,16,...,256: 62 exact linear root-multiplier and lower-charge checks, including faithful and generic sectors. These check multipliers, not construction of all nonlinear root jets.
- symbolic real/imaginary cubic formula; exact full-return W cubic on W=V=t at p=12,16,20,24 (rotation-equivariant cubic form comes from the owner result).
- p=12,16,20,24: 34 pure-V raw jet comparisons over distinct requested horizons in {2,h,2h,s,p}, both signs at epsilon=1/7, including A and full p-return, against epsilon=0. Lower pure-V coefficients agree; q-coefficient drift matches the derived formula.
- p=12: six exact W=t,V=j t lines j=0,...,5 identify the full homogeneous W-component difference through q=5 for positive initial parity, since polynomial degrees in j are <=5; lower differences vanish and top contrast is p epsilon kappa V^q. Reality supplies the conjugate component. All-p statements and nonlinear centralizer lemma rest on written proofs, not finite extrapolation.

Intake: upload/ofn-strobe-boundary-stage2c-20261127 at 7e1177dc33a2e4d746f4245558dd5e0dd209fa1d. SHA-256 values computed on native executed bytes; connector readback Git blob identities match independently computed native Git blob hashes for both files before exact-blob placement.

| File under evidence/ofn/intrinsic_strobe_boundary/ | SHA-256 |
|---|---|
| scripts/strobe_boundary_stage2c_check.py | 7248372de4798bda29c9ee23be8c1f10a7cc6a338c4f5dfe91e9b657fb39a394 |
| runs/strobe_boundary_stage2c_output.txt | 5cd7259ad85ab270700a417c277dcafa92f19fd09bb11238e3a496ea0b1296fe |

Reproduce from a repository checkout (or invoke by absolute path from a separate directory): python3 -I evidence/ofn/intrinsic_strobe_boundary/scripts/strobe_boundary_stage2c_check.py

Requested independent review: (1) verify intake/placement SHA-256 and replay byte-for-byte; (2) verify the shortest orbit construction, both root criteria, the common linear period premise, the fractional root in the formal and finite jet categories; (3) independently check the full-return homogeneous contrast and the sign of both cubic parts with their frame scale; (4) check the divergence and polar Fourier bracket arguments, including induction at d=2 and projection at d=q-2, for arbitrary real q-jets; (5) verify both restricted no-go proofs separately, including power-of-two p; (6) check conditional complement typing and the physical nonclaims. The earlier Claude message is not a review of this completed proof. PI decision remains pending.

*END OF STAGE 2C SESSION RECORD.*
