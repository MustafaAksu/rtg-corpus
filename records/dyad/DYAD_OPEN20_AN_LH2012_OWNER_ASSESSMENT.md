# DYAD OPEN 20 (analytic branch) — owner assessment of the López-Hernanz (2012) application

**Date:** 23 October 2026. **From:** Dyadic DSN owner (Claude). **Status:** working record (SESSION level). This record is not an amendment, a release or a notice. Governing edition: DYAD v6.4.22 (tag `dyad-v6.4.22`). There OPEN 20 is PARTIAL: B-∞ existence and flat uniqueness are CLOSED; B-an and B-6 are ACTIVE.

## Assessed material

- **Review:** `DYAD_LH2012_SUMMABILITY_REVIEW.md`, 23 Oct 2026 (SHA-256 `e5b815eacdcf99706bd6d3f28c2f2240223bb929cae9ba2eeab7cf822bd18d9f`), with its Turkish cover note (`ef7fbc12…915b`). The PI forwarded both to the owner session. Neither is in the repository yet; per CONVENTIONS §6 they go unchanged to an `upload/…` branch. The review's script and outputs (`check_lh2012_dyad_transfer.py`, `transfer_checks.json`, `negative_controls.json`) were **not** supplied to the owner, so its "9/9, three controls" result is EV-SRC-REPORTED here.
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
- **Terminology.** Gevrey-$1/3$ ⟺ **3-summable** in $z$ ⟺ 1-summable after $t=z^3$ (with the residue-class split). This replaces the P1-c-5 wording "1/3-summable".

## 2. Independent owner check of the finite inputs (EV-RUN; EV-INDEP relative to the review's unseen script)

`evidence/dyad/scripts/dyad_lh2012_transfer_check.py`, SHA-256 `6b443e2893f142414cb5babbcaa755c2d05b08abf65b1972584600cafffa13e5`. It composes $T^6$ in exact rationals in the real chart to degree 5, using the engine of `dyad_h4_real_route_check.py`. It then works in the complexified raw frame $z=\rho+\omega\eta$, $w=\rho+\bar\omega\eta$ ($z=W$) with exact sympy.

**Gates:**

| Gate | Check |
|---|---|
| L1 | the linear part is the identity and the quadratic part is zero |
| L2 | weighted divisibility for $(z,w)=(x,x^2u)$ |
| L3 | the recorded coefficients: $\mu$; $c_{40}=-\tfrac1{16}+\tfrac{7\sqrt3}{144}i$; $d_{31}=\tfrac13-\tfrac{\sqrt3}9i$; $C=-\tfrac{61}{2160}+\tfrac{43\sqrt3}{6480}i$ |
| L4 | $A=\tfrac12+2i\sqrt3$, $B=\tfrac{11}{24}-\tfrac{5i\sqrt3}{24}$ |
| L5 | $\ell_\pm\neq0$ and $\ell_-=-\ell_+$ |
| L6 | $\alpha=-\tfrac{102}{19}-\tfrac{16\sqrt3}{19}i$ for both roots |
| L7 | $a_++a_-=\tfrac{1+i\sqrt3}{12}$ |
| L8 | $T$ has linear part $(\lambda z,\bar\lambda w)$, $\lambda=e^{i\pi/3}$, and $[T_w]_{2,0}=-\tfrac16$ |
| L9 | $a\mapsto(\bar\lambda a-\tfrac16)/\lambda^2=\tfrac{1+i\sqrt3}{12}-a$ swaps $a_\pm$ |

**Results:**
- All nine gates pass, exit 0. The output is `evidence/dyad/open20-an/lh2012_transfer_check_output.txt`.
- Negative controls: `--control C` (altered $C$) fails L3 and exits 1; `--control S` (altered $T$ coefficient) fails L8 and L9 and exits 1.
- The $(4,0)$, $(3,1)$ and $(0,4)$ values agree with the archival $h_4$ closed forms of §1/§8: $[F_w]_{3,1}=\overline{h_4^{(1,3)}}$ and $[F_w]_{4,0}=\overline{h_4^{(0,4)}}=0$.

**Owner observation** (`[ALG]`, exact; SESSION). $\ell_-=-\ell_+$ is equivalent to $B/A=2c_{40}/\mu$, and this identity holds. As a consequence:

$$\alpha=\frac{2A}{\mu}=\frac{2\bar\mu}{\mu}-4=-\frac{102}{19}-\frac{16\sqrt3}{19}i,$$

independent of the root and of $C$. So the Briot–Bouquet ratio of both branches is fixed by the six-step cubic coefficient $\mu$ (DYAD-THM-C21) alone. This also explains why control C leaves L6 unchanged.

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
