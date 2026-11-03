# Row 8: claim-level repin check (Triadic §7.1 and §7.2 against governing tags)

Read-only check. Nothing in the repo was edited or committed.
Source: `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md` at `triad-v1.6.1`. It is byte-identical to the working tree (`diff` empty).
Governing files were extracted with `git show <tag>:dsn/<FILE>.md`. All line numbers below come from grep/sed on that output.

Count note: §7.2 has **12** bullets (L811–L822), not 11. §7.1 has 5 Dyadic RID bullets (L783–L787) and 6 Programme-context bullets (L800–L805).

Section renumbering: none affects the cited sections.
- Dyadic §1, §6.2, §6.9, §6.11 and §6.12 keep their headings and anchors (L45, L457, L606, L648, L704).
- Genesis §2, §6.1, §6.3, §6.4, §6.5 and §6.6 keep their anchors (L90, L640, L694, L907, L921, L963). New subsections §6.3a, §6.3a.1, §6.3b and §6.3c were inserted (L743, L784, L814, L859) without renumbering.
- RRF §3.1 is still at L270, and TDR-G §2 is still at L70.
- Programme §6.3 keeps its heading (L297), but the TRIAD paragraph was rewritten (see P1).

## A. §7.1 Dyadic RID imports (governing `dyad-v6.4.23`, Triadic pin v6.4.13)

Dyadic v6.4.23 Appendix A (L1263–1269) states: "No existing RID, grade or OPEN status changed". Dyadic §7 L1092 records Triadic v1.6.1's five imports as pinned to v6.4.13, and notice N2 is ANSWERED (L1124).

| # | Triadic line | Imported item | Governing tag | Location at tag | Statement/value at tag | Source grade at tag | RID status at tag | Verdict |
|---|---|---|---|---|---|---|---|---|
| D1 | L783 | DYAD-THM-C21 | dyad-v6.4.23 | §6.2, L467–469 (also §1 L69, export table L717) | $c_{21}=-\tfrac12-i\tfrac{2\sqrt3}{3}$ (L469); export row "$\mu=-\tfrac12-i\tau$" (L717); $\tau=\tfrac{2\sqrt3}{3}$ (§6.3 L481) | `[THM]` | assigned, DYAD-THM-C21 | **REPIN** |
| D2 | L784 | DYAD-ALG-BRIDGE-LEMMA | dyad-v6.4.23 | §6.9, L631–632 | "$\mu_p = p\bar\lambda\nu_3^{(1,p)}$" (L631). General-p proof is still cross-referenced to RECOG-ALG-LEADING-RETURN-EQUIVARIANCE (L632). | `[ALG]` | assigned | **REPIN**. Note: v6.4.20 added a separate frame qualifier, DYAD-ALG-KP-FRAME-SCALE (L633): "holds in each linear eigenframe for that frame's one-step coefficient". It does not change the lemma at p=6 in the W frame. The consumer value $\kappa_{\rm shear}=-2\sqrt3/3$ is the Genesis §6.3 policy (row G5); the bridge lemma itself does not state it. |
| D3 | L785 | DYAD-DEF-BRIDGE-EXPORT-CONTRACT item 1 | dyad-v6.4.23 | §6.12, L712–723 | Item 1 is present (L716): "$W=\mathcal L(\rho,\eta)=\rho+\omega\eta$, $v_\perp$ … `[DEF]` … no gauge choice". The table still has exactly **six items** (L716–L721: frame, μ, τ, ratio, $\mathcal P_{\rm dyad}$, bridge lemma), and the evidence matrix says "six items" (L1461). The sentence "None of these items depends on the Lie strict-kernel gauge" is at L723. | `[DEF]` | assigned | **REPIN**. Note: the ratio row (L719) now cites "Genesis v2.8.9 §6.3" (FC-DYAD-34, bookkeeping). Item 1 is unaffected. |
| D4 | L786 | DYAD-ALG-PROTECTION-MATRIX | dyad-v6.4.23 | §6.11, L701–702 | $\mathcal P_{\rm dyad}(R^2)=\begin{pmatrix}1-R^2/2&\tau R^2\\-\tau R^2&1-R^2/2\end{pmatrix}$, "linear eigenframe … cubic order" | `[ALG]` | assigned | **REPIN** |
| D5 | L787 | DYAD-DEF-PRIMITIVE-MAP | dyad-v6.4.23 | §1, L47–49 (also §6.1, L436–437) | $\rho'=\rho-\sin\eta,\ \eta'=\eta+(e^\rho-1)-\sin\eta$ (L48, L437). The alias note at L49 cites Genesis v2.8.6 G-B02, "retained in v2.8.7 §1". | `[DEF]`, **still `[v6.4.11, provisional]`** (L47) | assigned | **REPIN**. Provisional status unchanged. Genesis gen-v2.9 §1 L31 still records `GEN-DEF-PRIMITIVE-MAP` as an import/alias of DYAD-DEF-PRIMITIVE-MAP. The Triadic phrase "recognized in Genesis v2.8.6 §1" is still accurate. |

## B. §7.1 Programme-context references (L800–L805)

| # | Triadic line | Referenced item | Governing tag | Location at tag | Statement/value at tag | Source grade/status at tag | RID status | Verdict |
|---|---|---|---|---|---|---|---|---|
| P1 | L800 | Programme §6.3 and SG-PROG-1 (cited at v1.2) | programme-v1.3 | §6.3 TRIAD paragraph at L301; SG-PROG-1 at §8 L465 (local guard at §3.2 L106) | SG-PROG-1 is present: "No physical dynamical law, coefficient, observable identification or evidential strengthening may pass between discrete and continuous branches without a named bridge …" (L465). Appendix A L563 lists SG-PROG-1–4 as "Unchanged". **The §6.3 TRIAD paragraph was rewritten.** At v1.2 (L295) it held the "review questions … remain for its update" and "not by endorsement of a global no-cascade conclusion". At v1.3 (L301) it reads "Owns its birth/lift and diagnostic-model ledger and the T-6 export protocol. Imports Genesis …, Dyadic, RRF (CN-05 …), OFN and Programme". `grep -n -i -E 'no-cascade\|owner-review\|owner review'` on v1.3 returns nothing. | ADOPTED 24 Oct 2026 (L7) | n/a | **HOLD**. SG-PROG-1 is fine. The "§6.3 … current owner-review questions … no global no-cascade endorsement" description does not match v1.3 §6.3. The pointer text needs rewording; the interface register (IF04, IF06, IF29 at L420, L422, L445) may be the better §7.2 target. |
| P2 | L801 | OFN (cited at v0.9) | ofn-v0.12 | §3.1, L187–191 ("Interaction as Event, Not Force") | L191: "*update*, *interaction event*, *birth* … name different operations unless an owner supplies their identification". OFN §11 L1402 reads "Triadic v1.6.1 \| OFN v0.9 (pinned by Triadic) \| Triadic's repin is its decision". | ADOPTED 30 Oct 2026 (L7) | n/a (reference only) | **REPIN (pointer refresh v0.9 → v0.12)**. This is not a claim import. The adoption date must change to 30 Oct 2026. OFN v0.12 itself cites Triadic v1.6.1 SG-18 (L578) and RF-O08-02/03/08 (L1149, L1155, L1185). |
| P3 | L802 | RRF §3.1 CN-05 (cited at v0.8.2) | rrf-v0.8.4 | §3.1, L270–284 | "$B_T^{\rm plane}=2B_G,\ Q_T=2Q_G,\ I_T=2I_G,\ \Omega_T=-\sqrt3\,\omega_{\rm raw}$" (L275); "$Q_c^T=\frac{\kappa^2}{4}(Q_s^T)^3$" (L281); "`[OPEN] [scope: consumer obligation; NOT APPLIED to any owner birth formula]`" (L284) | `[DEF]` convention-only (L272); the conversion is an `[OPEN]` obligation | "RID unavailable; owner notice CN-05" (L272) | **REPIN (pointer refresh v0.8.2 → v0.8.4)**. The content is unchanged in the respect Triadic describes. v0.8.4 was adopted 20 Oct 2026 (header L6). |
| P4 | L803 | GEN-OPEN-APEX-SLOT | gen-v2.9 | §2 L378; §8 L1255 | "`[RETRACTED]` `[RID preserved: GEN-OPEN-APEX-SLOT]` … withdrawn … The distinct $d$-mode label and its primitive seed calculations remain valid … physical transverse/UV embedding … remains `[OPEN]`" | RETRACTED as `[RESULT]`; embedding `[OPEN]` | RID preserved | **REPIN (reference only)**. The receipt can say "retained unchanged through v2.9". |
| P5 | L804 | GEN-THM-K3-PLANAR-FACTOR-NOGO; GEN-THM-K3-SIXSTEP-FACTOR-NOGO | gen-v2.9 | §1 L53 and L55; §6.3a L753; §6.3a.1 L802; §8 L1273 and L1275; SG-15 L575, SG-16 L578 | Both are present with the same statements. v2.9 Appendix A L1305: "Unchanged: … §6.3a–§6.3c apart from the G-20 note and the two existence-scope wordings". | `[THM]` (both) | assigned (both) | **REPIN (reference only)**. Update the pin from "v2.8.7" to gen-v2.9. A new sibling result, GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO (v2.8.9, §6.3c L859; §1 L59), is not referenced by Triadic. |
| P6 | L805 | TDRG-OPEN-CHI-SCALING (cited at v2.12.13) | tdrg-v2.12.14 | §2, L272–283 (also L192) | Status "ACTIVE \| BLOCKS TDR-T" (L274). L277: "the derivation target is the clean-star-count collapse $\texttt{clean\_star\_components}/\text{row}\sim N^{-0.73}$ ($480$–$1440$ window) … $\chi$ is a composite ratio, not an independent scaling field". L283: "χ is **not an independent scaling field** … TDR-24B therefore introduces no new scaling degree of freedom". | `[OPEN]` ACTIVE | assigned (module RID) | **REPIN (reference only)**. The "Current status (v2.12.14)" line is new wording; v2.12.14 is a corrections-only edition that changed no scientific number (Appendix A, L975–989). TDR-24B is still a separate ACTIVE OPEN that has not been absorbed into TDR-24A. The new text adds "compute-gated on OPEN-POLICY-GEOMETRY", which is consistent with Triadic's description. |

## C. §7.2 Genesis imports (governing `gen-v2.9`, Triadic pin v2.8.7)

v2.9 Appendix A L1305 states: "every other RID's statement and grade; every OPEN status" are unchanged. `grep -n 'REQ-T16' gen.md` returns nothing: Genesis records no response to any REQ-T16 request.

| # | Triadic line | Imported item | Governing tag | Location at tag | Statement/value at tag | Source grade at tag | RID status at tag | Verdict |
|---|---|---|---|---|---|---|---|---|
| G1 | L811 | Metric $B$, $Q$; invariance | gen-v2.9 | §6.1, L655 and L657 | $B=\begin{pmatrix}1&-\frac12\\-\frac12&1\end{pmatrix}$, $Q(r)=\rho^2-\rho\eta+\eta^2$ (L655); $A^\top BA=B$ (L657) | `[DEF]` / `[THM]` | GEN-DEF-PRIMITIVE-METRIC; GEN-THM-PRIMITIVE-METRIC-INVARIANCE | **REPIN** |
| G2 | L812 | $J_Q$ quarter-turn | gen-v2.9 | §6.6, L981–985 | $J_Q=\tfrac1{\sqrt3}\begin{pmatrix}1&-2\\2&-1\end{pmatrix}$, $a^\top BJ_Qb=\tfrac{\sqrt3}{2}\omega_{ab}$, $J_Q^2=-I$ (L982); $\omega_{ab}=a_2b_1-a_1b_2$ (`[CONVENTION]`, L985) | `[ALG]` | **still unassigned**. Only the artifact locator GEN-ART-JQ-PHASEDRIFT exists (§8 L1246). | **REPIN** (RID unavailable) |
| G3 | L813 | Leading birth family | gen-v2.9 | §6.3, L725–729 (also §1 L38–42) | $c_0^{[3]}=\kappa Q_sJ_Qs_*$ (L727, L40); $Q_c=\kappa^2Q_s^3$ at leading order (in the L729 clause; specializations at L731–732) | `[THM]` | **still unassigned**. GEN-ART-PHI-2TO3 is an artifact locator only (§8 L1263, `[custody-A]`). | **REPIN** (RID unavailable) |
| G4 | L814 | Birth remainder order (conditional) | gen-v2.9 | §6.3 L729; §1 L42; GCL-06 guard §2 L198–206 | "If the selected **complete child functional preserves …** fifth-order … then $c_0=c_0^{[3]}+O(\|s_*\|^5)$ and $Q_c=\kappa^2Q_s^3+O(Q_s^4)$ … raw-residual quartic … $O(\|s_*\|^4)$ … $O(Q_s^{7/2})$ … not excluded. No physical residual/child functional is selected here." (L729) | Conditional. **GCL-06 is still OPEN**: "the physical residual/child functional remains OPEN (GCL-06)" (L42); "The physical residual/child functional remains OPEN." (L206) | **still unassigned** (no GEN- RID near L198–206 or L729) | **REPIN** (conditional, unchanged) |
| G5 | L815 | Shear reference | gen-v2.9 | §6.3, L731 | $\kappa_{\rm shear}=-2\sqrt3/3$; $Q(c_{0,\rm shear}^{[3]})=\frac43Q_s^3$ | `[ALG structure]` | **still unassigned** | **REPIN** |
| G6 | L816 | Recoil reference | gen-v2.9 | §6.3, L732 | $\kappa_{\rm recoil}=-\frac12$; $Q(c_{0,\rm recoil}^{[3]})=\frac14Q_s^3$ | `[ALG structure]` | **still unassigned** | **REPIN** |
| G7 | L817 | Tetrahedral chronological protection | gen-v2.9 | §6.4, L915 and L917 (also §1 L44) | "$G_2(Z)=\sum_{j=0}^5L^{5-j}F_2(L^jZ)=0$" (L915); "$\Delta Q_u=O(\|Z\|^4)$" (L917) | `[THM]` | **still unassigned**. GEN-ART-G2-CHRONO is an artifact locator (§8 L1264, `[custody-A]`). | **REPIN** |
| G8 | L818 | Radial polynomial $\mathcal P_4$ | gen-v2.9 | §6.5, L931–941 (also §1 L46) | The polynomial is printed unchanged as $\Delta Q_d^{(4)}=-Q_d^2-\tfrac18Q_sI_{ds}-\dots+\tfrac14I_{dc}\omega_{sc}$ (L934–940), and §1 L46 identifies it as "$\mathcal{P}_4(s,c,d)$". **The identity "$\mathcal P_4=2d^TBG_{3,d}$" is not printed.** `grep -n -E 'BG_\|d\^\\top ?B\|2d\^\|P\}?_4 ?(:)?='` on gen-v2.9 finds no such line, and the same grep on gen-v2.8.9 is also empty. The only analogous identity is for $c$: "$\Delta Q_c^{(4)}=2c^\top BG_{3,c}$" (L250, L1243). | `[THM]` | **still unassigned**. GEN-ART-P4-PRIMITIVE is an artifact locator ("certifying script … not in the repository", L1265). | **HOLD (wording/source)**. The polynomial itself can be repinned. The bullet and Triadic §6 L637 present "$\mathcal P_4=2d^TBG_{3,d}$" as a printed source premise, and that is not found at the tag. Either cite the printed $\Delta Q_d^{(4)}$ (L931–941) only, or mark the $2d^TBG_{3,d}$ form as a Triadic-side definition. |
| G9 | L819 | Vector apex seeds | gen-v2.9 | §6.5, L959 (also §2 L364, §6.6 L987) | $Q_{d,1}^{[s^3]}=\tfrac{7}{1024}Q_s^3$ and $Q_{d,1}^{[c^3]}=\tfrac{61}{34992}Q_c^3$ (L959); $Q(V_s)=\frac7{1024}Q_s^3$ (L364) | `[ALG]` ("[ALG verified]" at L418 and L1244) | **still unassigned**. GEN-ART-G3D-SEED is an artifact locator (L1244). | **REPIN** (values unchanged). Notation note: "$Q(V_c)$" does not appear in Genesis (`grep 'Q\(V_c\)'` is empty). The source symbol is $Q_{d,1}^{[c^3]}$. |
| G10 | L820 | Birth-symmetry cross-invariants | gen-v2.9 | §6.6, L987 | "$I_{ds}^{(1)}=\omega_{ds}^{(1)}=-Q_s^2/16$"; "$D_{\rm birth}^{[s^3]}=\tfrac{7}{512}Q_s^3=2Q(V_s)$" | `[THM]` at L987. **Flag:** §1 L80 says this item was "promoted to `[ALG]`", and §8 L1246 lists GEN-ART-JQ-PHASEDRIFT (J_Q, birth symmetry, phase drift) as `[ALG]`. | **still unassigned** (GEN-ART-JQ-PHASEDRIFT is a locator only) | **REPIN**. The value is unchanged and the grade at the ledger entry is `[THM]`, matching Triadic. Source symbols are $I_{ds}^{(1)},\omega_{ds}^{(1)}$, not Triadic's $I_{V_s,s},\omega_{V_s,s}$. The Genesis-internal grade inconsistency (L80 and L1246 vs L987) may be worth reporting to the Genesis owner. |
| G11 | L821 | HINDEX norm definition | gen-v2.9 | §2, L383–396 (table row L393; displayed norm L387); §8 L1261 | "$\|H\|_B^2=\lambda_{\max}(B^{-1}H^\top B^{-1}H)$" (L387). The status row reads "Numerator norm is $\lambda_{\max}(B^{-1}H^\top B^{-1}H)^{1/2}$ \| `[DEF/ALG]`" (L393). The GCL-03 conditional lowering $S_f=Bc_f$ is still present (L386). | `[DEF/ALG]` row; module status "CLOSED for index type (v2.7.7); physical lowering bridge conditional" (L385) | module RID GEN-OPEN-HINDEX only (L383, L1261); no claim-level RID | **REPIN** |
| G12 | L822 | Standalone chiral admissibility polynomial | gen-v2.9 | §6.5, L949–953; §8 L1243 | "$\Delta Q_c^{(4)}\big\|_{\rm standalone}=\tfrac13Q_c^2+\tfrac14(I_{sc}+\omega_{sc})^2+\tfrac5{16}\omega_{sc}^2\ge0$" (L950) | `[THM]` | GEN-THM-DELTA-QC (L953) | **REPIN**. Note: v2.9 (GB-13) added §2 L215, "Specialization of `GEN-THM-DELTA-QC`" at $I_{sc}=0$, using `[conv: RTG canonical B-metric]` and citing Triadic §7.1 as read at `triad-v1.6.1`. This is consistent with Triadic's $I_{sc}=0$ check, so the import needs no change. |

### RID check for the "RID unavailable" Genesis imports

`grep -o -E 'GEN-(THM|ALG|DEF|OPEN|ART|...)-[A-Z0-9-]+'` was run on gen-v2.9 to list every GEN RID. It found no result RID for any of the following, so they all stay "RID unavailable":
- $J_Q$ (G2)
- the $\Phi_{2\to3}$ birth theorem (G3)
- the remainder clause (G4)
- the shear and recoil policies (G5, G6)
- chronological protection (G7)
- $\mathcal P_4$ (G8)
- the vector apex seeds (G9)
- birth symmetry (G10)

The only GEN identifiers attached to these statements are artifact locators: GEN-ART-JQ-PHASEDRIFT, GEN-ART-PHI-2TO3, GEN-ART-G2-CHRONO, GEN-ART-P4-PRIMITIVE and GEN-ART-G3D-SEED.

New result RIDs registered in v2.9 are GEN-THM-QH-NOGO, GEN-THM-SINGLE-FACE-METRIC and GEN-THM-SOURCED-JUNCTION (Appendix A L1302). None of them applies to these imports.

## D. Separate checks

**(a) Genesis RIDs at gen-v2.9**
- `GEN-OPEN-APEX-SLOT`: exists. It is `[RETRACTED]` with the RID preserved (§2 L378), and §8 L1255 reads "RETRACTED as `[RESULT]` … physical transverse/UV embedding remains `[OPEN]`".
- `GEN-THM-K3-PLANAR-FACTOR-NOGO`: exists, `[THM]`, scope §6.3a (§1 L53, §6.3a L753, §8 L1273, SG-15 L575). Its statement is unchanged per Appendix A L1305.
- `GEN-THM-K3-SIXSTEP-FACTOR-NOGO`: exists, `[THM]`, scope §6.3a.1 (§1 L55, L802, §8 L1275, SG-16 L578). Its statement is unchanged.

**(b) RRF v0.8.4 planar convention**
§3.1 still records the convention as convention-only and the conversion as an obligation:
- L272: "`[DEF] [scope: typed metric convention for identical identified planar vectors only …]`"
- L275: "$B_T^{\rm plane}=2B_G,\ Q_T=2Q_G,\ I_T=2I_G,\ \Omega_T=-\sqrt3\,\omega_{\rm raw}$"
- L281: "$Q_c^T=\frac{\kappa^2}{4}(Q_s^T)^3$"
- L284: "`[OPEN] [scope: consumer obligation; NOT APPLIED to any owner birth formula]` … The equality above is the conditional units conversion, not a modified physical child law"

So the answer is yes. The heading (L270) still carries the label "(convention-only; proposed consumer receipt)", and the import tag is "Triadic v1.6 §7.4 and CN-05; RID unavailable".

**(c) TDRG-OPEN-CHI-SCALING at tdrg-v2.12.14**
It is unchanged in the respect Triadic describes:
- status ACTIVE (L274)
- χ is not an independent scaling field (L277, L283)
- the derivation target is the clean-star-count collapse $\sim N^{-0.73}$ (L275, L277)

TDR-24B is still a separate OPEN, not absorbed into TDR-24A. Only a "Current status (v2.12.14)" summary line was added, and the edition changed no scientific number (Appendix A L975–989).

## Summary of verdicts

- **HOLD (2):**
  - P1 (L800): Programme v1.3 §6.3 no longer carries the owner-review/no-cascade text. SG-PROG-1 is unchanged.
  - G8 (L818): the "$\mathcal P_4=2d^TBG_{3,d}$" form is not printed at gen-v2.9 (or gen-v2.8.9). The polynomial itself is unchanged. Triadic §6 L637 makes the same "source premise" statement.
- **REPIN (21):** D1–D5, P2–P6 and G1–G7, G9–G12.
  - Pointer refreshes: P2 (OFN v0.9 → v0.12, adopted 30 Oct 2026) and P3 (RRF v0.8.2 → v0.8.4, adopted 20 Oct 2026).
  - Notation notes, values unchanged: G9 (source symbol is $Q_{d,1}^{[c^3]}$, not $Q(V_c)$) and G10 ($I_{ds}^{(1)}$ / $\omega_{ds}^{(1)}$).
  - Flag: G10 has a Genesis-internal grade inconsistency, `[THM]` at L987 vs `[ALG]` at L80 and L1246.
- **Status checks:**
  - DYAD-DEF-PRIMITIVE-MAP is still provisional.
  - Export contract item 1 is present and the contract still has six items.
  - GCL-06 is still OPEN.
  - No Genesis "RID unavailable" import has gained an RID at gen-v2.9.
  - Genesis has no REQ-T16 response.
