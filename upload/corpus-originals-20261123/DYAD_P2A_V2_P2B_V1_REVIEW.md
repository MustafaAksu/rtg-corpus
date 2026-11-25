# Review: P2-A v2 (primitive contraction) and P2-B v1 (coordinate + normalized remainder)
**Reviewer:** Claude · **Date:** 22 Sep 2026 · **Inputs:** ChatGPT message, `REVIEW_DISPOSITION.md`, `P2A_V2_PRIMITIVE_PROOF.md`, `P2B_V1_COORDINATE_AND_REMAINDER_PROOF.md`
**Status:** independent verification record. Every number below was recomputed from my own reconstruction of $T$, the six-step jet, and the one-step normalizer $h$ (solved from the homological equation, not read from any package file). Not a DSN amendment; no RID; nothing promoted. This note **does** constitute my independent check of the P2-B v1 constants, which the package correctly said it did not yet have.

## 0. Three corrections to my previous review — all accepted

| My earlier statement | Their correction | Verdict |
|---|---|---|
| "The 64-version cannot close: a $6000\|W\|^7$ tail gives $\ge375\|W\|^6$ radially" | Radial contribution of a vector tail $R$ is $2\|P\|\|R\|+\|R\|^2\sim12000A_Pt^8$: **degree 8**, not 7 | **They are right.** I conflated the vector and radial tails. The 64-version was correctly *withdrawn* for lack of a delivered proof; my "cannot close" inference was wrong and is retracted. Not declared false. |
| Seed margin "12×" | $q_{\rm in}/Q_0=(1/625)/(19/250000)=400/19\approx21.05$ | **They are right.** Arithmetic slip; membership unaffected. |
| P2-B route: $C_7\le L\cdot(\text{raw tail})\cdot(\text{Lipschitz})$ | Omits the finite defect $D_{\rm poly}=P\circ h-h\circ J$, which vanishes through degree 6 but not identically | **They are right, and it matters.** Verified below: $[D_{\rm poly}]_{(0,7)}=\tfrac{31}{9720}-\tfrac{77i\sqrt3}{19440}\ne0$. My sketch would have under-counted $C_7$. |

## 1. P2-A v2 — reproduced exactly

- Rational ceilings $\tfrac{16931}{10000},\tfrac{6671}{5000},\tfrac{3567}{1000}$ sit above my exact modulus sums $1.693055, 1.334194, 3.566974$. ✓
- Degree-7 radial polynomial: all eight coefficients match my recomputation at product degree 7 (the truncation trap is avoided on both sides). ✓
- $K_8(1/20)$: my 60-digit value $42354.21$, their outward-rounded $<42355$. ✓
- $\tfrac{6671}{5000}+\tfrac{3567}{1000}r+42355r^2=107.40005<108$; full LHS $=\tfrac{2825241}{8000000}=0.353155<\tfrac12$; rounded-$C_6$ LHS $0.354655<\tfrac12$. ✓ (exact fractions)
- Tube: $\max_jS_j(1/25)=0.0463261<47/1000$; $(47/1000)^2<1/400$. ✓ Seed $19/250000<1/625$. ✓

**$(C^{\rm prim}_{6,\rm rad},q_{\rm ctr},q_{\rm in},c)=(108,\tfrac1{400},\tfrac1{625},\tfrac12)$ is verified.** Gain over v1: $9\times$ in $Q$, $3\times$ in $W$-radius, $130/9$ in the constant — as stated.

## 2. P2-B v1 — reproduced from an independent solve of $h$

I re-solved $f\circ h=h\circ n$ degree by degree (resonant $h$-coefficients zero, resonance $a-b-1\equiv0 \bmod 6$):
- $h_2$ matches; $h_3$ has exactly the three channels $(3,0),(1,2),(0,3)$; $f\circ h-h\circ n$ has no terms of degree $\le6$. ✓
- Resonant one-step coefficients $n_{21},n_{32},n_{05}$ equal the recovered solver's values **exactly**. ✓ (So solver ↔ homological convention is now triple-locked: by the bridge lemma, by the solver output, and by an independent solve.)
- $M(s)$ ceilings: my exact sums $0.583333,0.077397,0.111190,0.043544,0.049387$ vs. $\tfrac7{12},\tfrac{39}{500},\tfrac{14}{125},\tfrac{11}{250},\tfrac1{20}$ — all valid ceilings; degree 2 is exact ($\tfrac16+\tfrac13+\tfrac1{12}$). ✓
- $M'(\tfrac1{10})=\tfrac{358439}{3000000}<\tfrac18$; $R-M(R)=0.094077>\tfrac9{100}$; $M(R)/R<\tfrac1{16}$; $M''(\tfrac1{10})=\tfrac{368381}{300000}$. ✓
- $F_W\circ h-h\circ J$ and $D_{\rm poly}$ both vanish through degree 6; **$[D_{\rm poly}]_{(0,7)}=\tfrac{31}{9720}-\tfrac{77i\sqrt3}{19440}$ exactly** (full degree-7 block recomputed). ✓
- $P^+$ ceilings $1.259,1.73,0.938,1.984$ above my $1.258306,1.729932,0.937529,1.983106$; $J^+$: $1.099>1.098084$. ✓
- Vector tail $K^{\rm vec}_7(1/20)=5533.6276<5600$. ✓  $C_{\rm poly}=15.8181<16$. ✓  $C_7^{\rm NF}=\tfrac87[5600b^7+C_{\rm poly}]=7103.168<8000$. ✓
- Derivative constant: $\mathcal D'(r_z)/r_z^6=111.2745$; $C_{E,6}=44135.6$; final $50722.003<60000$. ✓
- Domain closure: $H(1/40)=0.025366<1/20$, $J^+(1/40)=0.025020<1/10$, $H(r_z)/r_W=0.507<7/8$, $S_6(H(r_z))=0.02830<0.029<0.09$, $H(J^+(r_z))=0.02539<0.026$. ✓
- Sub-tube: $\tfrac{16}{15}\max_jS_j(1/50)=0.022894<1/40$. ✓

**The P2-B v1 constants $(R,\sigma,\kappa)=(\tfrac1{10},\tfrac9{100},<\tfrac18)$, $|\widehat F-J|\le8000|z|^7$, $\|D\widehat F-DJ\|_2\le60000|z|^6$ on $|z|\le\tfrac1{40}$, and the conjugate sub-tube are verified.** The argument structure (segment-integral injectivity, contraction-mapping inverse, coefficientwise $D_{\rm poly}$ majorant with exact low-degree cancellation, differentiated conjugacy identity, all compositions enclosed in $\sigma$) is sound; in particular the derivative bound is *not* obtained by differentiating a pointwise inequality, which is the usual mistake and was avoided.

## 3. Two substantive points that remain (not errors)

**3a. $C_7=8000$ is dominated by the majorant tail, not by $D_{\rm poly}$.** Of the $7103$, the raw-tail term $5600b^7\approx6199$ is $\sim87\%$; $D_{\rm poly}$ contributes $16$. So the normalized constant inherits all the looseness of $\Psi^{\circ6}$ at degree 7 (observed vector remainder on $|W|\le1/20$ is $O(10^2)$, majorant $5.5\times10^3$). The same signed-jet trick that bought $9\times$ in P2-A applies here unchanged: the vector jet is exact through degree 6 now and could be pushed to 8–9 in seconds; majorize the vector tail from degree 9 or 10. I would expect $C_7\to O(10^2\!-\!10^3)$ and $r_z$ to roughly double. **This is the next cheap improvement and it is worth doing before any RECOG application**, because RECOG's manifold-entry and memory estimates will be $C_7$-limited.

**3b. The sub-tube base $U'=\{Q\le\tfrac1{2500}\}$ is set by $r_z=\tfrac1{40}$, i.e. by $C_7$'s domain, not by the contraction domain.** Once 3a is done, $U'$ can be enlarged toward $U=\{Q\le\tfrac1{625}\}$ and the seed's normalized margin grows accordingly. Worth stating in the package so downstream users don't treat $1/2500$ as a dynamical limit.

Minor: the $C_5$ in P2-A v2 uses $\tfrac{16931}{10000}$ (modulus-sum ceiling); the true phase maximum is $1.639$. A rational ceiling on the actual max (e.g. by bounding the cubic on the unit circle via its Fourier coefficients) would gain a few percent; not worth the complexity now.

## 4. On the 47/54 scoping
Agreed with their qualification: $[W^3\bar W^3]\Delta Q_6=\tfrac{47}{54}$ is a raw homogeneous radial coefficient equal to the fixed-radius angle-average; it corroborates the *number* in the owner backbone table but does not by itself establish the long-orbit backbone recursion or identify primitive $Q$ with normalized amplitude. My earlier phrasing ("cross-check with the backbone law") should be read in that narrower sense.

## 5. Disposition
- P2-A v2: **verified**; recommend it become the operative primitive profile (v1 retained as weaker baseline; 64-set withdrawn, not falsified).
- P2-B v1: **verified**; the $D_{\rm poly}$ correction to my route is accepted and recorded.
- Open, unchanged: RECOG manifold entry, full-map memory, GAP-LOCK angular inequalities on an explicit domain, historical $\Phi_1$ byte identity, optimality.
- Recommended next: signed-jet sharpening of the **vector** tail (3a), then enlarge $r_z$ and $U'$ (3b); only then hand $C_7$ to RECOG.
