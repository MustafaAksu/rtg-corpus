# DZT — B1: which dynamical object (triage row 6)

**Status:** [SESSION] owner analysis record, for the second co-owner's review. **Not an adoption.** No B1 result enters, and `DZT-OPEN-LOCAL-FORMAL-ZETA` (v0.19 §2) is unchanged. This record states candidates and facts at the pinned owner editions. The choice of object is left to the owner and the PI (§5).
**Date:** 20 November 2026. **Prepared by:** the DZT co-owner (Claude).
**Governing edition:** `dzt-v0.19` (SHA-256 `2b959f46b8e23363beac087183caf4946d63d1e8d5ac597bdb7d9230143bf6ce`).
**Owner editions read:**
- Dyadic `dyad-v6.4.24` (`10fbdacc…7bc16`);
- RECOG `recog-v0.3.27` (`19556f91…`).

Both are the governing tags in `BASELINE.md`. DZT has no RECOG import today. Any use of a RECOG result in a DZT edition would be a new import, with a notice to `pipes/RECOG/`.

**Authority:**
- **PI decision D4**, 18 Nov 2026: "B1 re-examination is required; the freeze is unverified history" (`records/dzt/DZT_REACTIVATION_TRIAGE.md` §7).
- **Triage row 6**, which says: "First fix the dynamical object: $\mathcal A_{\rm raw}$ or $Q(T^{6m}x)$, with its scope pinned at the Dyadic tag." Its acceptance condition is that no B1 result enters until the object is stated with owner RIDs and the result is proved for it.
- **The PI's forwarding**, on 20 Nov 2026 at 13:14 +03:00, of the second co-owner's plan for this step. In that plan the record fixes the object, clock, coordinate, regularity and observable, and no B1 theorem, no $W^{(A,B,C)}$ acceptance and no edition follows from it.

## 1. The question as it stands

v0.19 §2 asks for a formal local zeta near $P_1$, $\zeta_{\rm loc}(z)=\exp\big(\sum_m W_mz^m/m\big)$, "with $W_m$ a locally-defined weight from $Q_{\rm true}$ contraction or certified $p$-step channel data".

This leaves three choices open:
1. What sequence $m\mapsto(\cdot)_m$ the weight is built on.
2. In which coordinate it is built.
3. With what regularity.

The recovered B1 work (v0.10–v0.17, not adopted; reading record O-8.1) answered all three implicitly. It used the scalar recurrence $Q_{m+1}=Q_m-Q_m^2+AQ_m^3$ with $A=\tfrac{47}{54}$. The Dyadic response to DZT-REQ-004 (`DYAD_RESPONSE_TO_DZT_REQ-004.md`, SHA-256 `94f3f458d1d491ea231803520636bd00d558854832669c80731fde84d4c12f55`, lines 24–27) calls this "the physical radial recurrence". The owner has since superseded that wording (F1 below).

## 2. Candidate objects

| | Object | Clock | Coordinate | Regularity | Observable | Orbit-dependent? | Owner RIDs (grade) |
|---|---|---|---|---|---|---|---|
| O1 | Raw angular mean $\mathcal A_{\rm raw}(Q)=\frac1{2\pi}\int_0^{2\pi}\lvert F_W(\sqrt Qe^{i\theta})\rvert^2d\theta$ | none (a function of $Q$, not a sequence) | raw linear frame $W$ | jet to degree 6 | the circle mean of $\lvert F_W\rvert^2$ | no | `DYAD-ALG-RAW-ANGULAR-MEAN` (`[ALG]`, scope: fixed-radius uniform-angle mean in the raw $W$-frame) |
| O2 | Primitive orbit $Q_m=Q(T^{6m}x_0)$, $x_0\in U=\{0<Q\le\tfrac1{625}\}$ | block index $m$ of $F=T^6$ | primitive $(\rho,\eta)$; $Q=\lvert W\rvert^2$ | exact map; certified inequalities | $Q_m$ (and the primitive phase) | yes | `DYAD-THM-PRIM-CTR`, `DYAD-ALG-P5-RADIAL`, `DYAD-ALG-ONE-BLOCK-BURST` (Dyadic); `RECOG-THM-A1A-RECIPROCAL-AMPLITUDE` (`[THM]`, imported by Dyadic §6.5) |
| O3 | Chart orbit $q_m=\lvert z_m\rvert^2$, $z_m=h^{-1}\big(W(T^{6m}x_0)\big)$, $x_0\in U$ | block index $m$ | conjugacy chart $W=h(z,\bar z)$, row A ($\lvert z\rvert\le\tfrac1{20}$) | exact map $\widehat F=h^{-1}F_Wh$ locally real-analytic; proof inputs: the degree-6 jet $J$ and the certified remainder $\lvert\widehat F-J\rvert\le100\lvert z\rvert^7$ | $q_m$, $\Theta_m=\arg z_m$ | yes | `DYAD-ALG-NF6`, `DYAD-THM-NF-INV`, `DYAD-THM-NF-REM` (Dyadic); `RECOG-ALG-CHART-LAWS`, `RECOG-ALG-A1C-RECIPROCAL-DRIFT` (`[ALG]`, RECOG) |
| O4 | Germ data of $F$ at $P_1$ | none | the chart, or formal | formal / finite jet | $\mu$, $a_{32}$, $a_{05}$; $X=\log F$ | no | `DYAD-THM-C21`, `DYAD-ALG-NF6`, `DYAD-ALG-CUBIC-PARABOLIC`, `DYAD-THM-FORMAL-CENTRALIZER` (scope formal) |

## 3. Facts at the pinned editions (owner statements)

- **F1.** $\tfrac{47}{54}$ is the cubic coefficient of O1, and also the $(3,3)$ coefficient $[W^3\bar W^3]P_6$ of the raw radial jet (`DYAD-THM-PRIM-CTR`, Dyadic §6.5). Neither makes it the coefficient of a pointwise scalar recurrence. Dyadic §6.5, `DYAD-ALG-RAW-ANGULAR-MEAN`, calls it "an averaging operator, not a pointwise recurrence for $Q$ along arbitrary primitive orbits (the pointwise update carries the nonzero $Q^{5/2}$ term below), and not by itself a long-orbit backbone theorem". `[COR]` `[v6.4.10]` supersedes the unqualified recurrence.
- **F2.** The pointwise update of $Q$ is $Q(T^6x)-Q=-Q^2+P_5+O(\lVert x\rVert^6)$, with $P_5=\tfrac Q{24}(5\eta^3-43\eta^2\rho+4\eta\rho^2-5\rho^3)\ne0$ (`DYAD-ALG-P5-RADIAL`). On the positive ray it gives $-\tfrac5{24}Q^{5/2}$ (`DYAD-ALG-ONE-BLOCK-BURST`).
- **F3.** On O2 the certified law is the leading decay $\lvert Q_{m+1}^{-1}-Q_m^{-1}-1\rvert<\tfrac{15}2\sqrt{Q_m}$, so $Q_m^{-1}=Q_0^{-1}+m+O(\sqrt m)$ (`RECOG-THM-A1A-RECIPROCAL-AMPLITUDE`, `[THM]`, Dyadic §6.5).
- **F4.** The chart is defined, but the primitive and chart amplitudes are only compared, not identified. $W=h(z,\bar z)$ with $h=\mathrm{id}+h_2+\cdots+h_6$ ($h_2=-\tfrac{1+i\sqrt3}{12}z^2-\tfrac13z\bar z+\tfrac{1-i\sqrt3}{24}\bar z^2$). The six-step jet is $J(z)=z+\mu z^2\bar z+a_{32}z^3\bar z^2+a_{05}\bar z^5$, with:
  - $\mu=-\tfrac12-\tfrac{2i\sqrt3}3$;
  - $a_{32}=-\tfrac{97}{432}+\tfrac{197i\sqrt3}{324}$;
  - $a_{05}=-\tfrac{49}{8640}-\tfrac{307i\sqrt3}{25920}$

  (`DYAD-ALG-NF6`). The comparison is $\tfrac{225}{256}q\le Q_{\rm prim}\le\tfrac{289}{256}q$, and "$Q_{\rm prim}$ is **not** identified with $q=|z|^2$" (`DYAD-THM-NF-INV`).
- **F5.** The chart law has isotropic cubic coefficient $\tfrac{245}{216}$, not $\tfrac{47}{54}$. The law is $\lvert J\rvert^2=q-q^2+\big[\tfrac{245}{216}+2\Re(a_{05}e^{-6i\Theta})\big]q^3+O(q^4)$, with $\tfrac{245}{216}=\lvert\mu\rvert^2+2\Re a_{32}$ (`RECOG-ALG-CHART-LAWS`, `[ALG]`). Dyadic §6.14 cross-references it: "$\tfrac{245}{216}\ne\tfrac{47}{54}$ — the concrete instances of the SG-19 non-transfer rule". RECOG's refusal line excludes $\tfrac{47}{54}$ and "a pointwise $47/54$ law" from the chart.
- **F6.** The chart orbit law is $\delta_m:=q_{m+1}^{-1}-q_m^{-1}-1=-\tfrac{29}{216}q_m-2\Re(a_{05}e^{-6i\Theta_m})q_m+R_m$, with $\lvert R_m\rvert\le212.6\,q_m^2$. The isotropic coefficient is "the exact $1-\lvert\mu\rvert^2-2\Re a_{32}=-\tfrac{29}{216}$", and the sixth harmonic has zero mean. The centred drift obeys $\sup_m\lvert q_m^{-1}-(b+m-\tfrac{29}{216}H_m(b))\rvert\le K_\epsilon$, with $H_m(b)=\sum_{j<m}\tfrac1{b+j}$; this is `RECOG-ALG-A1C-RECIPROCAL-DRIFT` (`[ALG]`, scope $x_0\in U$, chart row A).
- **F7.** $F=T^6$ is tangent to the identity at $P_1$ (`DYAD-ALG-CUBIC-PARABOLIC`); hence $DF^m(P_1)=I$ for every $m$.
- **F8.** The formal centralizer is $\{\exp(sX)\}$ with $X=\log F$ (`DYAD-THM-FORMAL-CENTRALIZER`, scope formal). The lattice phase $\arg c_{05}-6\Theta$ is invariant under linear but not under nonlinear equivariant gauge (`RECOG-ALG-LATTICE-CLOCK`).

## 4. What this means for B1 ([SESSION] analysis)

**(a) O1 cannot carry the index $m$.** O1 is a function of $Q$. Iterating $\mathcal A_{\rm raw}$ is an averaged model, not the dynamics (F1). That model's reciprocal drift is $1-\tfrac{47}{54}=+\tfrac7{54}$. The certified orbit law on O3 has $-\tfrac{29}{216}$ instead (see (c)). No orbit law with $\tfrac7{54}$ is established, on O2 or on O3.

**(b) On O2 no autonomous logarithmic orbit law is established; the logarithmic part can be masked.**
- The derivation (`[SESSION]`, from F4 and F6): $Q_m-q_m=\lvert h(z_m)\rvert^2-\lvert z_m\rvert^2=2\Re\big(\bar z_mh_2(z_m)\big)+O(q_m^2)$. This is a nonzero cubic form in $z_m$ that depends on the angle (F4). Hence
$$\frac1{Q_m}=b+m-\frac{29}{216}H_m(b)-\frac{2\Re\big(\bar z_mh_2(z_m)\big)}{q_m^2}+O(1).$$
- The angular term is $O(q_m^{-1/2})=O(\sqrt m)$, with a sign that turns slowly as $\Theta_m$ drifts. It can be larger than the logarithmic term $-\tfrac{29}{216}H_m(b)$, which is present. Because it depends on the phase and vanishes at some phases, it is not shown to dominate at every $m$. This agrees with the certified $O(\sqrt m)$ of F3.
- Consequence: for a weight built on the primitive $Q_m$, the leading correction can come from an orbit-dependent, angle-dependent term of order up to $\sqrt m$ rather than from the logarithm. No autonomous logarithmic law for $Q_m$ alone is established.
- `[NUM]` illustration (§6): on three orbits from $U$ and $10^6$ blocks, $1/Q_m-1/Q_0-m$ oscillates with amplitude of about $0.4$–$0.75\sqrt m$ (up to 739 at $m=10^6$).

**(c) On O3 the orbit law is owner-certified (F6).**
- $q_m^{-1}=b+m-\tfrac{29}{216}H_m(b)+O(1)$, that is $q_m=\tfrac1m+\tfrac{29}{216}\tfrac{\ln m}{m^2}+O(m^{-2})$; the $O(m^{-2})$ term depends on the orbit.
- The recovered B1 has the opposite sign and a different value: $Q_m=\tfrac1m-\tfrac7{54}\tfrac{\ln m}{m^2}+\dots$.
- `[NUM]` illustration (§6): the first-order chart amplitude $\lvert W-h_2(W)\rvert^2$ tracks $-\tfrac{29}{216}H_m(b)$ to within $0.09$ at every printed $m$ on all three orbits. At $m=10^6$ the values are $-0.96$ against $-0.92$; the recovered value would be $+0.89$.

**(d) O4 is orbit-free.** Germ-level data are $\mu$ (`DYAD-THM-C21`) and the chart isotropic coefficient $\tfrac{245}{216}$ (F5). This record does not establish whether $\tfrac{245}{216}$ is invariant under the full residual-gauge class of the chart.
- `[HEUR]`: for a resonant cubic gauge, the bracket with the cubic term changes only the angular part of the quintic coefficient; this suggests that the radial part is invariant at that order.
- The sixth harmonic $a_{05}$ is not gauge-invariant in phase (F8).

**Recommendation to the owner and the PI.** Pose B1 on O3, or directly on O4. Do not pose it on O1, which is not a sequence, or on O2, where an angle-dependent $O(\sqrt m)$ term can mask the logarithmic part and no autonomous law is established.

## 5. Proposed fixed object (for review and for the PI's decision)

- **Clock:** block index $m\ge0$ of $F=T^6$; base points $x_m=T^{6m}x_0$, $x_0\in U$ (`DYAD-THM-PRIM-CTR`).
- **Coordinate:** $z_m=h^{-1}(W(x_m))$ in the chart of `DYAD-ALG-NF6`, row A ($\lvert z\rvert\le\tfrac1{20}$); rows are not mixed.
- **Regularity:** two things are kept apart.
  - The exact chart map $\widehat F=h^{-1}F_Wh$ is locally real-analytic: $T$ is analytic and $h$ is a polynomial with an inverse on $\lvert W\rvert\le\tfrac9{100}$ (`DYAD-THM-NF-INV`).
  - The proof inputs for B1 are the degree-6 jet and its certified remainder (`DYAD-THM-NF-REM`).
  No formal all-order statement and no analytic zeta theorem is established.
- **Observable:** $q_m=\lvert z_m\rvert^2$ and $\Theta_m$. The primitive $Q_m$ is a comparison quantity only (F4).
- **Certified inputs:** `RECOG-ALG-A1C-RECIPROCAL-DRIFT` and `RECOG-ALG-CHART-LAWS` (RECOG-owned, `recog-v0.3.27`). Germ data: $\mu$, $a_{32}$, $a_{05}$ (`DYAD-ALG-NF6`).
- **Weight:** $W_m$ must be defined on this object and pass the B1-0 gate. B1-0's "certified Dyadic local data" are then the chart objects above, with SG-19 non-transfer.

## 6. Evidence

`evidence/dzt/b1_object/b1_object_illustration.py` (SHA-256 `4988de5c02c1e693c335730e5d4f31780048e2e87a6a9f00a2b9c2bad336d25c`) was written for this record. Its output is `b1_object_illustration_output.txt` (`40f27ac2feb5f1af583715d2722bf1009f993bb154f6fb54ec99ccf6c5bc7b7a`).
- **Part 1, exact:** $\lvert\mu\rvert^2=\tfrac{19}{12}$, $2\Re a_{32}=-\tfrac{97}{216}$, their sum $\tfrac{245}{216}$, $1-\tfrac{245}{216}=-\tfrac{29}{216}$, and $\tfrac{245}{216}-\tfrac{47}{54}=\tfrac{19}{72}$.
- **Part 2, `[NUM]` illustration only:** three orbits of $T$ from $U$, $10^6$ blocks each, in double precision. The chart amplitude is taken to first order ($h_2$ only, which leaves an $O(1)$ error in $1/q$). It is not a proof input; F6 is the certified statement.
- No recovered script was run. The recovered B1 scripts (`dzt_b1_wB_audit.py` `4ecbfbfc…934b`, `dzt_b1_leadinglog_tower.py` `ed240349…c3b9a`, `dzt_b1_polylog_hierarchy.py` `f4d6515c…59f7`) are `EV-BYTES`, `EV-NOT-RERUN`.

## 7. The recovered B1 items under the proposed object (none enters; triage row 6)

| Item (recovered, unadopted) | Rests on | Status after this record |
|---|---|---|
| DZT-B1-0, the admissible-weight gate | definitions | Usable as a gate. Criterion 2's data list must name chart objects (§5) |
| $W^{(A)}$ `[FAIL]` (det and trace of the linearization) | $DF^m(P_1)=I$ | Independent of the O1/O2/O3 choice (F7): $\det(I-DF^m)=0$ and $\operatorname{tr}DF^m=2$. It survives, as a candidate for later entry with the Dyadic import |
| $W^{(B)}$ pure $\mathrm{Li}_2$ `[FAIL]` | "$A=\tfrac{47}{54}\ne1$ forces a log correction" | The recovered reason uses O1. On O3 the drift coefficient is $-\tfrac{29}{216}\ne0$ (F6), so a log correction is present and pure $\mathrm{Li}_2$ still fails, for the corrected reason. This becomes a proof only once $W_m$ is defined on O3 |
| DZT-B1-1 "RESULT": leading-log tower $c_r=(A-1)^r$, $Q_m^{\rm LL}=1/(m-(A-1)\ln m)$, $A=\tfrac{47}{54}$ | O1 coefficient applied as an orbit law | **Wrong object and wrong coefficient at the pin.** On O3 the orbit drift is $-\tfrac{29}{216}\ln m$ (the recovered value is $+\tfrac7{54}\ln m$); on O2 an angle-dependent $O(\sqrt m)$ term can mask the logarithmic part, and no autonomous law is established. It must be rebuilt on O3 if wanted; its recovered `[ALG]` has no basis at `dyad-v6.4.24` |
| DZT-B1-WC, $W^{(C)}$ "FAIL at certification level" | invariant data $\{c_{21},A\}$ with $A=\tfrac{47}{54}$ | Its invariant data used the raw coefficient. The chart isotropic coefficient is $\tfrac{245}{216}$ (F5), and the gauge behaviour of $a_{32}$ and $a_{05}$ must be taken from the chart (F8). Re-examine |
| Dyadic responses to REQ-003 and REQ-004 | REQ-004 lines 24–27: "$A=\tfrac{47}{54}$ … the physical radial recurrence" | Superseded at the owner (F1). If cited, cite by path and hash (`c8b5ee22…8e09`, `94f3f458…2f55`), not as RIDs (triage row 12) |

## 8. Next steps

1. Independent review of this record by the second co-owner.
2. The PI's (or owner's) decision on the object; this record proposes O3 (§5).
3. Then define $W_m$ on O3 and redo $W^{(B)}$, B1-1 and $W^{(C)}$. That work imports RECOG results. A question to RECOG (`pipes/RECOG/`) on the gauge status of $\tfrac{245}{216}$ would precede any invariance claim (§4 (d)).

Not decided here: no object, grade, RID or edition. `DZT-OPEN-LOCAL-FORMAL-ZETA` stays as stated in `dzt-v0.19`.

## 9. PI decision on the object

**Decision (PI, 20 November 2026, 23:20 +03:00, project conversation with the DZT co-owner, verbatim):** "O3". It answers the question of the same conversation, which named the candidates of §2 and the proposal of §5. The answer came after the record was merged (PR #341, `b1106fc`) on reviews `5992705393`, `5998598925` and `5998658151`.

**What the decision covers:** O3 is the object of `DZT-OPEN-LOCAL-FORMAL-ZETA` (B1), as fixed in §5 (clock, coordinate, regularity, observable, certified inputs). The B1 weight $W_m$ is to be defined on it, and the recovered B1 claims are to be tested on it one by one (§7).

**What it does not cover:**
- no B1 result, grade, RID or edition;
- no import yet of the RECOG RIDs named in §5 (that needs an edition and an import row);
- the gauge question for $\tfrac{245}{216}$ (O4, §4 (d)), which is asked of RECOG separately: `pipes/RECOG/20261120-DZT-b1-chart-drift-question.md`.

`DZT-OPEN-LOCAL-FORMAL-ZETA` stays as stated in `dzt-v0.19` until an edition restates it.
