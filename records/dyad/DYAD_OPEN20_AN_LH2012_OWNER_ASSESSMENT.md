# DYAD OPEN 20 (analytic branch) — owner assessment of the López-Hernanz (2012) application

**Date:** 23 October 2026. **From:** Dyadic DSN owner (Claude). **Status:** working record (SESSION level). This record is not an amendment, a release or a notice. Governing edition: DYAD v6.4.22 (tag `dyad-v6.4.22`). There OPEN 20 is PARTIAL: B-∞ existence and flat uniqueness are CLOSED; B-an and B-6 are ACTIVE.

## Assessed material

- **Review:** `DYAD_LH2012_SUMMABILITY_REVIEW.md`, 23 Oct 2026 (SHA-256 `e5b815eacdcf99706bd6d3f28c2f2240223bb929cae9ba2eeab7cf822bd18d9f`), with its Turkish cover note (`ef7fbc12…915b`). The PI forwarded both to the owner session. The review, its script `check_lh2012_dyad_transfer.py` (`71bf1c70…853d`) and its JSON outputs are now on `upload/dyad-lh2012-review` (`incoming/dyad-lh2012-review/`, PR #20); the owner checked them against that folder's `SHA256SUMS.txt` (7/7 OK) and the review hash above. **Owner replay (EV-RUN, 23 Oct 2026):** the script exits 0, and its `--negative ratio|branch|coefficient` runs exit 1; all four JSON outputs are byte-identical to the uploaded ones. The Turkish cover note is not on the upload branch; its bytes (`ef7fbc12…915b`) are in the owner session and go to the PI for upload.
- **Article:** L. López-Hernanz, "Summable formal invariant curves of diffeomorphisms", *Ergodic Theory Dynam. Systems* 32 (2012) 211–221, DOI 10.1017/S0143385710000805 [L12].
  - The owner read the supplied Markdown transcription in full: 681 lines, SHA-256 `9aa1ffa88ab87a92c5d77e0a672f409eaca17ee696dbb0f17cb605629d622978` (EV-SRC-READ).
  - The transcription was not compared with the PDF. Neither file is committed: the article is under publisher copyright and this repository is public. The PI keeps the source privately; it is cited here by hash.
- **Prior SESSION inputs, unchanged:**
  - P1-c (`DYAD_OPEN20_ANALYTIC_ROOTS_P1C_SESSION_v0_1.md`): isolatedness, the two smooth formal branches $\Gamma_\pm$ tangent to $[1:0]$, and $k^*$.
  - P1-c-2 (`…P1C2_SESSION_v0_1.md`): K7, the Briot–Bouquet type after two blow-ups. It records [L12] as "abstract only" and plans "P1-c-2b: read the [L12] full text … to settle its hypotheses and the summability level".
  - P1-c-5 (`…P1C5_SESSION_v0_1.md`): Lemma 5b-1, convergent generator ⇒ convergent Briot–Bouquet curve.

This assessment is that planned step.

## 1. Owner verdict

**ACCEPT the application, at SESSION level.**

[L12] Theorem 4.2, Theorem 5.1 and Corollary 5.2, applied to the lifted Briot–Bouquet germ of each branch, give the following (`[THM]` `[import: L12 Thm 4.2, Thm 5.1, Cor 5.2]` `[assuming: P1-c branch results (SESSION)]`):

- $\hat\phi_\pm$ is **3-summable in the raw parameter $z=W$** (Gevrey order $1/3$), with at most six singular directions, namely $\arg(-\ell_\sigma)+3\arg z\equiv\pi/2\pmod\pi$.
- Its sums are strong Hakim parabolic curves of the lifted map, so after blow-down they are parabolic curves of $F$ or $F^{-1}$.

The owner checked the argument step by step. Each step holds:

1. **The lifted map is analytic and tangent to the identity.** The lifted map is $x'=x+x^4G$ and $u'=(u+x^3H)/(1+x^3G)^2$, which is analytic. At $u=a_\sigma$, $u'-u=x^3P(u)+\dots$ with $P(a_\sigma)=0$. So the lifted germ has order 4 and $k=3$. Using $\operatorname{ord}F=3$ (so $k=2$) would be wrong.
2. **The generator of the lifted map is of Briot–Bouquet type in the sense of [L12] Definition 2.1.** The lifted map is $\mathrm{id}+x^3V$ with $V_x\in(x)$. Each power of $F^*-\mathrm{id}$ maps the ideal $(x^3)$ into itself, and maps $x$ into $(x^4)$. Hence the formal logarithm satisfies $X(x)\in(x^4)$ and $X(y)\in(x^3)$, and its degree-4 part equals that of the map (corrections start at degree 7). This gives $\lambda=\ell_\sigma\neq0$ and $\mu/\lambda=\alpha=P'(a_\sigma)/\ell_\sigma\notin\mathbb Q_{>0}$.
3. **The Briot–Bouquet curve is the strict transform of $\Gamma_\sigma$.** The strict transform $y=\hat\phi_\sigma/z^2-a_\sigma$ is a formal graph transverse to $x=0$, and the Briot–Bouquet curve is unique.
4. **Normalized coordinates exist.** Rescale $\xi=c_\sigma x$ with $c_\sigma^3=-\ell_\sigma$ and subtract a polynomial jet. The condition $m>1+\operatorname{Re}\alpha$ holds for $m\ge2$ because $\operatorname{Re}\alpha=-102/19$.
5. **Summability transfers back.** $w=x^2(a_\sigma+y(x))$ with $x=z$, so summability passes to $\hat\phi_\sigma(z)$ without reparametrization. The singular directions map as stated.

**Further points accepted as written:**

- **Gluing criterion.** $\hat\phi_\sigma$ converges ⟺ the jumps $\Delta_{\sigma,j}$ between sums of the **same** branch vanish on every overlap, including last-to-first. On common subsectors the bound $|\Delta|\le Ce^{-A/|z|^3}$ is an upper bound only.
- **Branch exchange.** $T(\Gamma_+)=\Gamma_-$, so $\hat\phi_+$ converges ⟺ $\hat\phi_-$ converges. The all-order statement uses P1-c's uniqueness of the two branches.
- **Consequences for B-an and B-6.** A nonzero jump ⇒ the branch diverges ⇒ $\log F$ diverges (Lemma 5b-1). This does **not** decide $F^{1/2}$ or $F^{1/6}$. A convergent branch gives an invariant analytic curve for any analytic tangent-to-identity root. B-an and B-6 are unchanged.
- **Real slice.** The sectorial curves have no real-slice points near the origin ($|w|=O(|z|^2)$ against $|w|=|z|$). Real tube and L-PHASE constants do not transfer.
- **Terminology** (corrected after the receiving review, R1). [L12] gives **3-summability** in $z$, which **implies** Gevrey order $1/3$. A Gevrey-$1/3$ coefficient bound alone does **not** give 3-summability; the application rests on the [L12] summability theorem, not on the earlier coefficient bound. Under the residue-class split after $t=z^3$, 3-summability in $z$ becomes 1-summability of the three component series in $t$. "3-summable" replaces the P1-c-5 wording "1/3-summable".

## 2. Independent owner check of the finite inputs (EV-RUN; EV-INDEP relative to the review's unseen script)

`evidence/dyad/scripts/dyad_lh2012_transfer_check.py`, SHA-256 `adbe4c47b563c75c2ccf71e4846548aacd0a4406ffcee2cd3560d89b5935dbbc` (revised after the receiving review; the first version `6b443e28…13e5`, reviewed at commit `be9ea79`, used a floating-point nonzero test in L5). It composes $T^6$ in exact rationals in the real chart to degree 5, using the engine of `dyad_h4_real_route_check.py`. It then works in the complexified raw frame $z=\rho+\omega\eta$, $w=\rho+\bar\omega\eta$ ($z=W$) with exact sympy.

**Gates:**

| Gate | Check |
|---|---|
| L1 | the linear part is the identity and the quadratic part is zero |
| L2 | weighted divisibility for $(z,w)=(x,x^2u)$ |
| L3 | the recorded coefficients: $\mu$; $c_{40}=-\tfrac1{16}+\tfrac{7\sqrt3}{144}i$; $d_{31}=\tfrac13-\tfrac{\sqrt3}9i$; $C=-\tfrac{61}{2160}+\tfrac{43\sqrt3}{6480}i$ |
| L4 | $A=\tfrac12+2i\sqrt3$, $B=\tfrac{11}{24}-\tfrac{5i\sqrt3}{24}$ |
| L5 | $\ell_\pm\neq0$ **exactly** (R2): a root with $\ell=0$ would be $a=-c_{40}/\mu$, and $P(-c_{40}/\mu)=-\tfrac{49}{8640}+\tfrac{307\sqrt3}{25920}i\neq0$ in $\mathbb Q(i\sqrt3)$; $\ell_-=-\ell_+$ exactly (equivalently $\ell_+\ell_-=-\tfrac{22487}{2540160}+\tfrac{16661\sqrt3}{7620480}i\neq0$) |
| L6 | $\alpha=-\tfrac{102}{19}-\tfrac{16\sqrt3}{19}i$ for both roots |
| L7 | $a_++a_-=\tfrac{1+i\sqrt3}{12}$ |
| L8 | $T$ has linear part $(\lambda z,\bar\lambda w)$, $\lambda=e^{i\pi/3}$, and $[T_w]_{2,0}=-\tfrac16$ |
| L9 | $a\mapsto(\bar\lambda a-\tfrac16)/\lambda^2=\tfrac{1+i\sqrt3}{12}-a$ swaps $a_\pm$ |

**Results:**
- All nine gates pass, exit 0. The output is `evidence/dyad/open20-an/lh2012_transfer_check_output.txt`.
- Negative controls: `--control C` (altered $C$) fails L3 and L5, exit 1; `--control S` (altered $T$ coefficient) fails L8 and L9, exit 1; `--control Z` sets $C=Bc_{40}/\mu-A(c_{40}/\mu)^2$, which puts the root at $-c_{40}/\mu$ (here a double root, since $B/A=2c_{40}/\mu$), and fails L3, L5 and L6, exit 1. Numeric root values are display-only.
- The $(4,0)$, $(3,1)$ and $(0,4)$ values agree with the archival $h_4$ closed forms of §1/§8: $[F_w]_{3,1}=\overline{h_4^{(1,3)}}$ and $[F_w]_{4,0}=\overline{h_4^{(0,4)}}=0$.

**Owner observation** (`[ALG]`, exact; SESSION). $\ell_-=-\ell_+$ is equivalent to $B/A=2c_{40}/\mu$, and this identity holds. As a consequence:

$$\alpha=\frac{2A}{\mu}=\frac{2\bar\mu}{\mu}-4=-\frac{102}{19}-\frac{16\sqrt3}{19}i,$$

independent of the root and of $C$, through the polynomial identity $P'(a)=\tfrac{2A}{\mu}(c_{40}+\mu a)$. The premise is $B\mu=2Ac_{40}$, which ties the quartic coefficients $d_{31}$ and $c_{40}$ to $\mu$; it holds for this map. So in **this** reduction the ratio equals $2\bar\mu/\mu-4$; it does not follow that every germ with the same cubic coefficient has this ratio. The ratio does not determine any jump.

**Limit.** This is finite algebra only: it checks the inputs of the imported theorems, not the theorems themselves.

## 3. Status and custody

- **Grade.** It stays SESSION. It can enter the DSN only together with the P1-c branch results, which are themselves SESSION and not in the ledger. That needs a receiving review of the combined statement and a later owner release; neither is started. No RID is proposed now.
- **Carried item "O20-an (López-Hernanz source)".** The [L12] full text has now been read, from a transcription; PDF bytes were not verified. The P1-c-2 open line "Summability of φ± ([L12]): lead only; full text needed" is answered by this record.
- **Not changed:**
  - B-an and B-6 (ACTIVE);
  - the convergence of $\hat\phi_\pm$ (open);
  - any RID, grade or DSN text;
  - N16–N21 (unsent; no new notice).

## 4. Next work (PI decides priority)

1. **Pilot design for one branch, written only.** Fix the normalized coordinate, a six-sector cover in $z$ with the overlaps around the singular rays, and the [L12] class $\mathcal H$ fixing which sums are meant. Then name what an enclosure of a jump would have to bound, including the contraction constants of the Hakim operator, which [L12] gives only existentially.
2. **A certified computation afterwards, on the PI's machine if heavy.**
   - A certified enclosure of an actual jump that excludes 0 would prove that the branch diverges. That would then give divergence of $\log F$, though not B-an.
   - Floating-point agreement or an interval containing 0 proves nothing either way.
   - Convergence needs an analytic gluing identity.

## 5. Addendum — LIT literature validation (3 November 2026, SESSION)

**Source.** Pipe item `pipes/DYAD/20261103-LIT-lh2012-summability-chain.md` (LIT finding, tag `dyad-v6.4.23`). It cites LIT inferences INF-005 to INF-008 at `rtg-lit` commit `44bad61d81af2f970b13368a8b7da87b9721442d`. The DYAD owner has no access to the private `rtg-lit` repository. What follows records LIT's statement as filed, not an owner re-check of the cited works.

**What LIT reports.** Every link of the [L12] route used in §1 has a deduction that both LIT co-owners checked:

| Link | Published support | LIT ID |
|---|---|---|
| [L12] Prop. 5.3 ⇒ Thm 5.1 (sectorial $1/k$-Gevrey) | Jiménez-Garrido–Sanz–Schindl, *J. Geom. Anal.* 30 (2020), Thm 5.2, with $M_p=\Gamma(1+p/k)$ | INF-005 |
| Thm 5.1 ⇒ Cor. 5.2 (Ramis $k$-summability, at most $2k$ excluded directions, sums = strong Hakim curves of $F$ or $F^{-1}$) | Malgrange–Ramis, *Ann. Inst. Fourier* 42 (1992), 1.4 and Def. 1.5 | INF-008 |
| Cor. 5.2 ⇒ the polynomial blow-down in the chart $z=x$ (step 5 of §1) | Malgrange–Ramis 1992, Prop. 2.3 | INF-008 §5 |
| [L12] Lemma 5.4 ($\hat\gamma$ is $1/k$-Gevrey), both steps | Brochero Martínez–López-Hernanz, *Astérisque* 323 (2009), Thm 1.1; written Gevrey Briot–Bouquet proof | INF-006, INF-007 |

**Scope of LIT's check, as LIT states it:**
- Watson's lemma, Borel–Ritt–Gevrey, Phragmén–Lindelöf and the Ramis–Sibuya theorem are cited classical inputs; they are not re-proved.
- [L12]'s own proofs of Prop. 5.3 and Thm 4.2 were read, not re-proved.
- Malgrange–Ramis 1992 is accepted at its checked parts (§1, and §2 up to 2.3). It stands in for Ramis 1980, which LIT did not obtain.
- LIT BL-014 (Lagrange inversion and composition, [L12] Thm 6.1) is open. It does not block this route, which bypasses Thm 6.1.

**Effect on this record.**
- The literature basis of the §1 verdict is stronger. LIT states that its earlier limitation (the Fruchard–Zhang proof being only sketched) does not apply to this cited route. The DYAD records did not carry that limitation themselves.
- The grade stays **SESSION** (§3), and the verdict is unchanged.
- B-an and B-6 stay ACTIVE: $k$-summability decides nothing about convergence.
- No statement about the real model or a physical carrier follows.
- **Stage-3 constants.** The explicit Leau–Fatou and Hakim constants that the sectorial pilot needs for E3/E4 remain open (LIT BL-004/BL-005). Stage 3 stays not authorized.

**Citation rule for a later import.** If the OPEN 20 analytic result ever enters the DSN (§3), its Import Ledger `Verification:` line cites the works above with LIT-ID@version:label and the `rtg-lit` commit (CONVENTIONS §8):
- `jimenezgarrido2020-phragmen@arxiv-v1:Theorem 5.2`
- `malgrange1992-multisommables@vor:1.5`
- `brochero2009-gevrey@vor:Theorem 1.1`
- `lopezhernanz2012-summable-curves@vor`

Nothing is imported now.

## 6. Addendum — LIT findings INF-014 and INF-015: local orbit structure along Γ_σ (4 November 2026, SESSION)

**Items:**
- `pipes/DYAD/20261103-LIT-flower-thm13-lifted-germs.md`: INF-014, rtg-lit merge `e7b1ad93…`. Source: López-Hernanz–Rosas, ETDS 45 (2025), Theorem 1.3, form (A).
- `pipes/DYAD/20261104-LIT-imrn2021-asymptotic-orbits.md`: INF-015, rtg-lit merge `d0ebb8c1…`. Source: López-Hernanz–Raissy–Ribón–Sanz, IMRN 2021, Theorems 5.1 and 7.1, read from arXiv:1710.03728v1.

Both items were filed by LIT's co-owner on draft PRs #171 and #174.

**What LIT states** (conditional on DYAD's data; both SESSION, checked by LIT's co-owner):
- **(a) Flower theorem, INF-014.** At each lifted point p_σ, the germ has form (A) with M = 3, a = ℓ_σ and b = αℓ_σ, so Re(b/a) = Re α < 0. Consequences:
  - no two-dimensional forward basin exists near p_σ;
  - every forward orbit of F with z_j → 0 and w_j/z_j² → a_σ eventually lies on one of three attracting parabolic curves.
- **(b) Stable manifolds, INF-015.** No condition on Re α is needed: k = 3, p = 0, μ = 1, and all three attracting directions are saddle directions. Consequences:
  - every orbit of F asymptotic to Γ_σ to all orders eventually lies on one of three parabolic curves asymptotic to Γ_σ;
  - no two-dimensional stable manifold of such orbits exists.
- **(c) Identification with the 3-sums.** Under (a) the two orbit classes coincide. Near each attracting direction the curves coincide with the blow-downs of LH2012's 3-sum graphs. That identification is a further LIT step (INF-015 Part B; INF-012 B), not a statement of the sources.

**Owner check of the DYAD inputs** (`EV-RUN`, exact; `evidence/dyad/scripts/dyad_open20_lit_inf014_inf015_hypothesis_check.py`, run `evidence/dyad/open20-an/lit-inf014-inf015/run.sh`):

| Gate | Result |
|---|---|
| H1 | 2A = αμ = 1 + 4i√3 and B = αc₄₀ = 11/24 − 5i√3/24. Hence P′(u) = α·G(0,u) identically, and b/a = α on both branches |
| H2 | ℓ_σ ≠ 0 on both branches: the zero u₀ = −c₄₀/μ = (1 + i√3)/24 of u ↦ c₄₀ + μu has P(u₀) ≠ 0. Also ℓ₊ + ℓ₋ = 0 (Vieta) |
| H3 | Re α = −102/19 < 0; α is not real |
| H4 | The lift has order 4 as a **full analytic germ**. The conditions involve only raw monomials of total degree ≤ 4, which the exact degree-4 jet of F = T⁶ decides |
| H5 | Raw terms of degree ≤ 3 are only the identity, μz²w and μ̄zw². The jet gives c₄₀ and d₃₁ as recorded |

The two controls (α + 1/19; μ̄ in place of μ) each fail H1 and exit 1. The input is `stage1_prep.json` at its pin `2c9ae637…4739`.

**Owner reading.**
- **Accepted at SESSION scope.** The DYAD-side hypotheses of INF-014 and INF-015 are certified exactly here, and the theorems are published. The DYAD owner did not read the sources themselves; LIT did.
- **Qualifications carried with the statement:**
  - FL-Q1 (INF-014: the flower paper's §8 sectorial coordinates; DYAD's case is covered by LH2012 Theorem 4.2);
  - IMRN-Q1 (the reading of "order of F" in the proof of Theorem 7.1);
  - IMRN 2021 read from arXiv v1, not from the journal version;
  - the LIT identification step (c).
  With these open, the statement is not a `[THM]` import.
- **What it adds.** It gives the formal branches Γ_σ a dynamical meaning: every orbit of the six-step return that converges to 0 through p_σ (z_j → 0, w_j/z_j² → a_σ) ends on one of three parabolic curves per branch. These curves realize Γ_σ on sectors. It supports the selected-sum convention of the pilot (design D8) through an independent uniqueness basis.
- **What it does not decide.** Nothing about B-an or B-6: it says nothing on the convergence of Γ_σ, log F or F^{1/2}. It gives no Stokes value and no E3/E4 constant; the stage-3 route check of the design record §8 is unaffected. It does not cover the inverse map, other infinitely-near points or a physical carrier.
- **Real slice (co-owner scope check, 4 Nov 2026; checked here).** The results concern the complexified germ only.
  - On the real slice w = z̄, so a nonzero real orbit tending to 0 has \|w_n/z_n²\| = 1/\|z_n\| → ∞. It never approaches the finite points p_σ (w/z² → a_σ), and it is not asymptotic to Γ_σ, whose w/z² tends to a_σ.
  - No real-orbit statement follows: none on PRIM-CTR, L-PHASE or a physical carrier.
  - This agrees with the pilot's real-slice guard (design record §6).
- **Exact relation worth recording (co-owner proposal).** P′(u) = α·(c₄₀ + μu) identically (H1). It shows why the eigenvalue ratio is the same α on both roots. It is a candidate `[ALG]` line for v6.4.24. It changes no constant.
- **DSN.** Proposed for the v6.4.24 S3 paragraph (backlog) as one `[SESSION]` sentence with the LIT-ID@version:label citations:
  - `lopezhernanz2025-flower@vor:Theorem 1.3`
  - `lopezhernanz2021-stable-manifolds@arxiv-v1:Theorem 5.1`
  - `lopezhernanz2021-stable-manifolds@arxiv-v1:Theorem 7.1`
  Nothing is imported now.
