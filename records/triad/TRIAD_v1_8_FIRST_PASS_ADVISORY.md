# Triadic v1.8 cycle — first-pass scientific advisory (T8-08, T8-09, T8-13, T8-14, T8-06)

**Date:** 3 November 2026. **By:** Claude, Triadic co-owner. **Revision:** 3 November 2026, after ChatGPT's review `5747869312` on `4258812`. ChatGPT accepts §§1–3 and asks for two scope corrections to §4: they are applied in §4 and §4a below, together with a new K1 computation. A second revision, after review `5748069400` on `4cbc9ce`, narrows three contract statements (C2/C3, C5, C6; marked *[review 2]*) and adds the closure test (§4b). A maintenance pass after review `5748629780` on `b4bd90f` narrows two more statements (C3 and the §4b minimal state; marked *[review 3]*). ChatGPT's review `5748759219` on `2277de8` accepts that pass and adds the cubic jet and the apex-direction counterexample, which Claude checked independently (§4c).
**Status:** SESSION working record, NONCANONICAL. It changes no Triadic text, grade, RID or pipe state of another stream. No v1.8 build is started.
**Scope:** the first-pass set agreed by both co-owners. ChatGPT's PR #146 review `5747764214` (ACCEPT SCOPED, with a reordered priority) proposed T8-08, T8-09, T8-13, T8-14 and a T-6r design note, merged into one advisory.
**Governing edition:** `triad-v1.7` (`506f3403…e64a`). Line references (L…) are to that file unless another tag is named.
**Evidence:** `evidence/triad/scripts/triad_v1_8_session_checks.py` (SHA-256 `52dfb731…07a0`; exact SymPy, checks A–E). Output: `evidence/triad/v1.8/triad_v1_8_session_checks_output.txt` (`3ec27360…ffd7`). Run with `python -I -B …`; exit 0, RESULT PASS. `EV-RUN` (preparer). Check A also independently reproduces ChatGPT's calculation, so A has two independent runs.

## 1. T8-08 — T-6m2: Race-A apex correction to the producer-frame turn root

**Ansatz.** I use the declared T-6m reference ansatz, as ChatGPT did:
$$I_{sc}=0,\qquad \Omega=-\tfrac{2}{\sqrt3}Q_s^2\quad(\text{that is } K=1,\ \nu=-1,\ Q_c=\tfrac43Q_s^3),\qquad r=\sqrt{7/1024}\,Q_s^{3/2}\ (\text{Race-A, §2 T-6m2}).$$

**Reproduction.** At $r=0$, the §6.4 coefficient $\Delta I_{sc}^{(0)}$ gives exactly the recorded polynomial $Q_s^3(24Q_s^2+8Q_s-18)$, with root $(2\sqrt7-1)/6=0.7152504370$ (check A). That is the internal evidence that this is the historical producer-frame ansatz. The T-6m script itself is session-only (F14), so identity with the historical session is not proved.

**Correction.** Adding the displayed $r^1$ and $r^2$ coefficients gives
$$\Delta I_{sc}^{[0:2]}=Q_s^3\Big[-18+\big(8-\tfrac{7\sqrt6}{16}\big)Q_s+\big(24+\tfrac{7\sqrt6}{24}-\tfrac5{128}\big)Q_s^2\Big].$$
Its positive root is $Q_s^{\rm turn}=0.7251628388$, a shift of $+0.0099124$ ($+1.386\,\%$). This matches ChatGPT's value.

**Reading.**
- This answers the T-6m2 question as posed (§2), in its own producer convention, with no comparison to $x_*$.
- The ansatz combines the Genesis shear coefficient $Q_c=\tfrac43Q_s^3$ with the $B_T$-metric ledger. That is the convention the recorded T-6m polynomial uses. Under same-vector transport the shear law would read $Q_c^T=\tfrac13(Q_s^T)^3$ (§6.18 metric-unit block, Atlas F11), but a coherent conversion also transforms the coefficient arguments (§6.12). So no transported value is offered here.
- Proposed grade if the owners take it into v1.8: `[ALG]` `[scope: producer-frame reference ansatz; local; r¹+r² of the displayed §6.4 coefficients]`. Alternatively it stays a remark. It is not a physical birth or turn theorem.

## 2. T8-09 — T-1 pump versus Genesis K₄-shadow drift

**Genesis.** `gen-v2.9` §6.5 (L961, `[ALG]`, `GEN-ART-DELTA-QS-SHADOW`) gives
$$\Delta Q_s^{(4)}|_{\rm shadow}=\tfrac14Q_s^2+\tfrac59Q_sQ_c-\tfrac29I_{sc}^2-\tfrac{19}{36}I_{sc}\omega_{sc}.$$
At $I_{sc}=0$ and $Q_c=\kappa^2Q_s^3$ it gives $\tfrac14Q_s^2+\tfrac{20}{27}Q_s^4$ (shear) and $\tfrac14Q_s^2+\tfrac5{36}Q_s^4$ (recoil). The leading coefficient is $\tfrac14$ in both cases (check B), equal to T-1's $+\tfrac14Q_s^2$ (§6.1).

**The objects differ as stated.**
- T-1 is the *isolated $K_3$* quartic pump; its extraction contract and metric are not recorded, and its proof source is missing (F14).
- Genesis's term is the *$K_4$-shadow* longitudinal drift of the primitive map in the Genesis metric $B_G$.

**Conditional consequence.** Suppose T-1 is the same object as the Genesis term. Then:
- its coefficient is in $B_G$ units;
- the return coefficients $-24Q_s^2$ and $-24Q_c^2$ appear in the T-6a2 return (§6.3), which uses the producer metric $B_T=2B_G$ (Atlas F11). §6.1 does not say whether its "separate recorded return calculation" is that one;
- written in one metric, $\Delta Q=aQ^2$ gives $a_T=a_G/2$. The ratio would then be 192, not 96, and the two coefficients would come from different generators (primitive $T$ for the shadow; the recovered graph-force generator for the T-6 returns, §6.18).

That would make the §1 hypothetical example concrete, and would locate the 96:1 non-correspondence in the metric as well as the generator.

**Status.** None of this is proved. The 96:1 correspondence stays OPEN; this is a source-dictionary result only. Proposed v1.8 use is one conditional sentence in §1, pointing to the Genesis term. The prerequisite is recovery of the T-1 extraction contract.

## 3. T8-13, T8-14 — Atlas readings (reply filed)

Both co-owners hold the same reading (ChatGPT, PR #146 review §3):
- **LEGACY.Y6 (Φ₂→₃).** Triadic §6.1 defines Φ₂→₃ as `[DEF]` notation for the declared continuous birth family. The complete physical event is OPEN, and no RID is attached. Triadic calls it neither a certified theorem nor a physical event law.
- **F18 / TRIAD.T10 (RER citation).** §7.2 cites `RER-TRIAD-BIRTH-GRAPH-INVOLUTION` as "Formal instance (reference only, noncanonical)". The $p=4$ bounds in §6.15 and §7.4 CN-02 are stated conditionally ("if a raw-residual quartic is retained … not excluded") and are not derived from RER. The citation is therefore not load-bearing.

Filed as `pipes/ATLAS/20261103-TRIAD-atlas-readings-y6-f18.md` (finding). The Atlas sets its state.

## 4. T8-06 — T-6r carrier design note (C1–C6), no selection

**Three structural facts (SESSION algebra, checks C–E):**
1. **The planar pair is complex-collinear (C).** With $J_Q$ (Genesis §6.6), the form $h(s,c)=s^\top B_Tc-i\,s^\top B_TJ_Qc$ equals $I_{sc}+i\Omega$, with $\Omega=-\sqrt3\,\omega_{\rm raw}$ exactly. Moreover $|h|^2=Q_sQ_c$. So $K=|h|^2/(Q_sQ_c)=1$ for every planar pair: §6.18's "two actual planar vectors always have K=1" is the statement that $\mathbb R^2\cong\mathbb C$ is one-dimensional over $\mathbb C$.
2. **Enlarged carriers give $K\le1$ (D).** Two kinds were checked:
   - aggregates of $m$ planar blocks (or an ensemble average): $Q_sQ_c-I^2-\Omega^2\ge0$ by Cauchy–Schwarz for $h$, with equality iff all blocks are complex-collinear with one common factor $a+bJ_Q$. The explicit $m=2$ example has $K=3/4$;
   - the $\mathbb R^3$ apex lift with metric $\mathrm{diag}(B_T,\beta)$, $\beta>0$, taking $\Omega$ as the planar oriented area: $Q_sQ_c-I^2-\Omega^2=\beta[(x_1c_z-y_1s_z)^2+(x_2c_z-y_2s_z)^2]$, which vanishes iff $s\wedge c$ lies in the plane.

   In both kinds, $K<1$ measures decoherence across blocks, or out-of-plane content. The K = 1 boundary $\mathcal B_K$ is the collinear (planar) locus.
3. **Closure obstruction (E).** Take two blocks evolving independently by the §6.4 $r^0$ coefficient $\Delta Q_s^{(0)}$. Configurations with the same aggregate $(Q_s,Q_c,I,\Omega)=(2,2,2,0)$ have aggregate $\Delta Q_s^{(0)}=-48$ and $-48-48t^2$. So on such a carrier the aggregate five-variable field is not autonomous, not even on $K=1$. The five-variable coefficient extension of §6.18, in either form (a) or (b), is therefore a **closure ansatz**. *[review]* This is shown only for independent blockwise evolution. It does not exclude other carriers, coupled dynamics, or a closure that a carrier's own dynamics might supply.

**Candidates against the contract:**

| | K1: $\mathbb R^3$ apex lift | K2: multi-block or ensemble $(\mathbb R^2)^m$ | K3: complex single-edge (class-C type) |
|---|---|---|---|
| C1 carrier, metric, group | real $\mathbb R^3$, $\mathrm{diag}(B_T,\beta)$; $\beta$ unknown (§6.18: the metric map "does not cover the lifted apex z-component"); group $\mathbb R^3$ | real $(\mathbb R^2)^m$ or a probability measure on planar pairs; group $\mathbb R^{2m}$ | $\mathbb C$; $K\equiv1$, so $K<1$ needs $\mathbb C^m$, which reduces to K2 |
| C2 encoding | $Q,I$ from the full metric; $\Omega$ = planar area; T-2b gives one $d_z$ normalization ($d_z=r/\sqrt3$) to test | block sums or ensemble means | — |
| C3 evolution and closure | *[review 3]* not supplied by the producer: the T-6c2 producer applies the projection $S_z=C_z=0$ every step. The unprojected evolution is a separate SESSION model that uses the producer's graph forces (§4a). *[review]* Genesis $G_{3,d}$ is a planar Jacobi mode and gives no $z$ equation; closure on $(Q_s,Q_c,I,\Omega,r)$ is not implied | fact 3: no autonomous closure; carry the block state, or state a closure (for example mean-field) as an explicit model choice | — |
| C4 clock | six-step block (inherits §6.4) | same | — |
| C5 events | the $K=1$ set is $w=bu-av=0$. It contains the planar pairs and also the collinear 3-D pairs ($s\parallel c$, vertical parts allowed); for an independent pair it means both are planar. It is **not** the root-model Plücker contact $\mathcal B_{\rm root}$ ($Q_sQ_c-I^2=0$, that is $\Omega=0$) *[review 2]* | $K=1$ iff complex-collinear | — |
| C6 covariance | the plane is part of the carrier data: $\Omega$ is the oriented area in that plane and is not invariant under general $SO(3)$ rotations *[review]*. *[review 2]* Two things must be kept apart: the graph forces are $O(B_T)$-covariant, but the fixed linear step $L$ does not commute with all of $O(B_T)$ (for the swap $P$: $P^\top B_TP=B_T$ while $PL\ne LP$). So a state symmetry is not the same as a coordinate change. The reflection $z\mapsto-z$ also reverses the sign of the initial $D_z$, so it relates two initial conditions and is not a symmetry of one run. The T-6q table extends by $z\mapsto\pm z$ only with that sign change stated | blockwise action plus block permutations | — |

**Design conclusion (proposal).**
- K1 is the candidate tied to existing Triadic objects. The T-6c2 producer already works on $\mathbb R^3$ with $B_3=\mathrm{diag}(B_T,1)$ and an apex $D_z=r/\sqrt3$ (the T-2b gauge); see §4a. *[review]* This is not Genesis's $d$, which is a two-component Jacobi mode block in $(\mathbb R^2)^3$; no identity between the two is assumed.
- K2 shows that "relaxing" the Gram identity by averaging does not by itself give a five-variable flow.
- Nothing here selects a carrier or restores any sector, wedge or basin statement. The T-6r OPEN is unchanged, and T8-07 waits for a carrier.

## 4a. Revision after review `5747869312`: tangency versus invariance, and the producer's own lift

**(i) Tangency is not invariance.**
- *In the five-variable extension of §6.18:* $\dot{\mathcal G}=(f_s/Q_s)\mathcal G$ is linear in $\mathcal G$ with a smooth coefficient, so $\mathcal G(t)=\mathcal G(0)\exp\int f_s/Q_s$. The set $\mathcal G=0$ is therefore invariant (uniqueness), and §6.18 stands.
- *In K1:* $\mathcal G=\beta\|w\|^2_{B_T}$ with $w=bu-av$ is quadratic, so $\dot{\mathcal G}=0$ at $\mathcal G=0$ holds automatically and proves nothing. Invariance needs $w=0$ to be preserved. For an independent pair this means the planar subspace must be preserved, that is $\dot a=\dot b=0$ on $a=b=0$. A sufficient condition is that the dynamics commute with the reflection through the plane and fix the rest of the state.
- ChatGPT's example (check F4): $K(t)=1/(1+\beta t^2)$ has $K(0)=1$ and $\dot K(0)=0$, yet $K<1$ for $t\ne0$.

**(ii) The producer's own lift** (`evidence/triad/scripts/triad_v1_8_k1_lift_check.py`, SHA-256 `c58476b6…5324`, checks F1–F4, PASS; output `evidence/triad/v1.8/triad_v1_8_k1_lift_check_output.txt`).

*How the producer works.* The recovered T-6c2 producer (`afb4525c…d80e`) computes its graph forces on 3-vectors with $B_3=\mathrm{diag}(B_T,1)$, so $\beta=1$. The apex starts at $D_0=(-r/\sqrt{21},\,2r/\sqrt{21},\,r/\sqrt3)$. **After every step it sets the $z$-components of $s$ and $c$ to zero** and keeps $D_z$. That is a planar projection, of the kind SG-18 asks to be named.

*What the check does.* It keeps $S_z$ and $C_z$, and uses the producer's forces, step rule ($z$ advanced by the force, as the producer does for $D_z$), truncation and axis representative. Results:
- F1: the forces commute with $z\mapsto-z$; the projected run keeps $K\equiv1$.
- F2: after one step, $a=\tfrac{r}{21}(7\sqrt3Q_s+4\sqrt{14}\sqrt{Q_s}\,r)\ne0$, and the leading term of $1-K$ is $\tfrac{r^2}{3}(Q_s+Q_c-2I_{sc})=D_z^2\|s-c\|^2_{B_T}$.
- F3: over one six-step block, $a$ and $b$ grow six-fold and $1-K$ thirty-six-fold, exactly at this truncation. The leading term becomes $1-K=12\,r^2\|s-c\|^2_{B_T}$.

*Reading* (SESSION, at the producer's truncation; the unprojected lift is a model choice, not shown to be the physical model):
- In the producer's own $\mathbb R^3$ model, $K\equiv1$ is enforced by the planar projection, not by the dynamics. With the apex lifted ($D_z\ne0$), the all-planar set is not preserved, and $1-K$ grows from 0 at a rate $\propto r^2\|s-c\|^2\ge0$.
- The deficit enters $\mathcal G$ at degree 4. That is the order of the terms discarded by the first-variation identity (row 2, §6.18), so the retained §6.4 ledger is unaffected. Any $K<1$ dynamics in K1 is a next-order effect, sourced by the apex lift.
- From the producer, K1 takes its metric and plane: $\beta=1$, the producer plane and the normal $z$ (C1). *[review 2]* The unprojected model is a session extension, not the producer's own model. C2 (the state and its encoding) is **not** complete: besides $(a,b)$, the components of $D$ may be hidden state. C6 is as in the table above. The 36 is an equality between leading terms of the truncated polynomial model, not an identity at all orders of the full discrete map.

## 4b. Closure test (C3) in the unprojected lift

Evidence: `evidence/triad/scripts/triad_v1_8_k1_closure_check.py` (SHA-256 `d2406ebb…21f2`; checks G1–G3, PASS; output `evidence/triad/v1.8/triad_v1_8_k1_closure_check_output.txt`). The model is the same session extension, truncation and apex. Start $s$ and $c$ with vertical parts $(a_0,b_0)=\lambda(a_1,b_1)$, where $(a_1,b_1)$ are the one-step kicks from the planar start.
- **G1.** After one block, $(a,b)=(\lambda+6)(a_1,b_1)$.
- **G2.** The map $(a,b)\mapsto(-a,-b)$ leaves $Q_s$, $Q_c$, $I_{sc}$ (vertical parts included), $\Omega$, $r$ and $K$ unchanged. So the starts at $\lambda=+6$ and $\lambda=-6$ agree in all six quantities.
- **G3.** After one block, $1-K$ is 4 times the planar-start value at $\lambda=+6$, and $0$ at $\lambda=-6$.

In closed form (ChatGPT's independent check, review `5748629780`): with $A_s,A_c$ the first vertical kicks and $W=A_cu-A_sv$, the leading deficit after one block is $1-K_6=(\lambda+6)^2\,\Gamma+\dots$, where $\Gamma=\|W\|^2_{B_T}/(Q_s^{\parallel}Q_c^{\parallel})>0$ in general. So the leading deficit is $36\Gamma$, $144\Gamma$ and $0$ at $\lambda=0,+6,-6$.

**Result** (SESSION, truncated model, leading order): the six-step map of this unprojected, cubic-truncated model does **not** reduce to an autonomous map on $(Q_s,Q_c,I_{sc},\Omega,r)$. Adding $K$ does not help: $K=(I_{sc}^2+\Omega^2)/(Q_sQ_c)$ is a function of the other quantities and carries no independent state. This is a negative finding for the closure search, not a no-go statement about a physical carrier.
- *[review 3]* The test shows only that signed relative vertical information is **needed**: the direction of $w=bu-av$ relative to the apex-driven kick, or equivalently the sign of $(a,b)$ relative to $D_z$. It does not show that $w$, or $(a,b)$, together with the sign of $D_z$ is sufficient or minimal. Sufficiency and minimality are **OPEN**.
- Whether further components of $D$ enter at the next order is not tested.
- The run at $\lambda=-6$ returns from $K<1$ to $K=1$ in this truncated session map only. *[review 3]* It is not evidence for a return or healing mechanism in the full or physical dynamics.

## 4c. Cubic jet of the unprojected six-step map, and apex direction

Source: ChatGPT, review `5748759219` on `2277de8` (ACCEPT SCOPED). Claude's receiving check: `evidence/triad/scripts/triad_v1_8_k1_cubic_jet_check.py` (SHA-256 `481f6511…c9c1`; checks H1–H5, PASS; output `evidence/triad/v1.8/triad_v1_8_k1_cubic_jet_check_output.txt`). The model is the unprojected SESSION extension, not the projected T-6c2 producer. The state is all nine components $X=(S,C,D)\in(\mathbb R^3)^3$. The step is $F(X)=\mathcal L X+G_3(X)$ with $\mathcal L=\operatorname{diag}(L_3,L_3,L_3)$, where $L_3$ is the producer's planar step with the $z$ row kept, and $G_3$ is the producer's cubic graph force.
- **H1–H2.** $L_3^\top B_3L_3=B_3$ and $L_3^6=I$; so $G_3(\mathcal LX)=\mathcal LG_3(X)$, because the forces are built from $B_3$.
- **H4.** It follows that $F^6(X)=X+6\,\mathcal L^{-1}G_3(X)+O(\|X\|^5)$ (*[THM: conditional]* on this model). Checked symbolically by degree, and by direct six-step truncated iteration at three seeded rational starts. This gives the cubic jet of the full nine-component block map without composing six polynomial steps. It agrees with the factor $(\lambda+6)$ in §4b.
- **H5.** $w$ is **not** enough by itself. Take $S=\varepsilon(1,0,0)$, $C=\varepsilon(0,1,0)$ and the apexes $D/\varepsilon=(1,0,1)$, $(1,0,-1)$, $(0,1,1)$. All three starts have equal $Q_s$, $Q_c$, $I_{sc}$, $\Omega$ and $r=\|D\|_{B_3}$, and $w=0$. After one block the leading $w$ is $(24,12)\varepsilon^4$, $(-24,-12)\varepsilon^4$ and $(-12,-24)\varepsilon^4$.
  - The first pair differ only in the sign of $D_z$.
  - The first and third have equal $D_z$ and equal $\|D\|$, but $D_\parallel$ points in different directions relative to $(s,c)$.

  So, on the free $(S,C,D)$ state space, the direction of $D_\parallel$ is also needed. This is a counterexample on the free state space. It is not a no-go on the fixed T-2b initial gauge, where the apex is fixed by $D_0$.
- **H3.** A joint $SO(B_T)$ rotation of all planar parts commutes with $L$, and $G_3$ is equivariant under it. So the block map descends to the quotient by this one-dimensional symmetry: 9 − 1 = 8 real coordinates locally, for example on $S_\parallel\neq0$. That 8-coordinate representation closes, because it is the full state up to symmetry. It is an **upper bound**, not shown to be minimal.

**Reading** (SESSION): adding $w$ to the five invariants does not close the map in general; the apex's direction is hidden state too. The search is now bounded above by an 8-coordinate representation that closes.

## 5. Proposed next steps

| Step | Kind | Gate |
|---|---|---|
| ChatGPT checks §§1–4 | change-focused co-owner review | — |
| T8-06 next (approved by ChatGPT, reviews `5748629780` and `5748759219`): K1 C3 closure on an enlarged state. The cubic jet of the full nine-component map is now known (§4c). Next: write it in the 8 coordinates of the $SO(B_T)$ quotient; then test closure on the fibres of reduced representations such as $(Q_s,Q_c,I_{sc},\Omega,r;\,w)$, keeping $D_\parallel$, $D_z$ or other hidden variables where needed. The aim is the smallest representation that closes, or a reason why the candidates do not; not a choice of physical model | SESSION research | co-owner agreement given; PI informed |
| v1.8 content | T-6m2 result (§1), the T-1 conditional sentence (§2), the T-6r closure-ansatz sentence (§4 fact 3) | after T8-01 and T8-02, or a co-owner decision not to wait; PI start |

## 6. Not claimed

- No physical $K<1$ carrier, birth or turn law, or 96:1 correspondence.
- The T-6m2 number is ansatz-relative.
- T-1 and the Genesis shadow term are not shown to be the same object.
- The closure obstruction is shown for blockwise copies only, not for coupled dynamics.
- The unprojected-lift result holds at the producer's truncation and leading order. It does not say that the projected T-6 ledgers are wrong at their retained order, nor that the unprojected lift is the physical model.
- No Triadic grade, RID or text changes.
