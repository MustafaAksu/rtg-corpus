# TDR-G v2.12.13 — independent Atlas advisory (ChatGPT, blind pass 2)

**Date:** 27 October 2026  
**Status:** [SESSION] independent advisory; no scientific owner adoption, amendment or notice.  
**Separation:** PR #82 / the other Atlas advisory **was not opened or read**. This review used the tagged governing owner and relevant independent dependencies. The TDR-G co-owner sessions have scientific disposition responsibility; Atlas reconciles; the PI controls adoption.

## 0. Source identity and reading extent

| Source | Governing edition / source | Actual reading |
|---|---|---|
| TDR-G | `tdrg-v2.12.13`, SHA-256 `aa232643f6f631694b0eda1532be213e5a517ef109cd66794f8e638e24fc053f` | Full tagged file retrieved (1,288 lines); close targeted reading §§1, 2, 3, 5, 6.1–6.3, 6.5, 6.8, 6.12, 7–8, Appendices B/C; history sampled. Proof certificates not rerun. |
| NUMGEN | `numgen-v1.21`, SHA-256 `4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701` | Targeted §6.6 P2 exposure at lines 1935,1953–1969; C7C-M HOLD lines 2037–2045; audit source read as text. |
| Audit | `upload/numgen-records/disc2_p2_antipodal_exposure_audit_v1.py` on main | Complete 112-line source read; independently inspected its centered representative, path tie and control design; no execution, no independent recount. |
| OFN | `ofn-v0.10` | Targeted Finding A §4.1 lines 248–254, XFER-O08-01, REQ-O09-05 and owner/consumer status. |
| Programme | `programme-v1.3` | Targeted §6.4, §7.2 IF03/13/21/25/32, maintenance list; v1.2→v1.3 scientific context, **not** independent full v1.2 tag-by-tag diff. |
| AZ | `az-v0.6` | Targeted Thread B/C and cross-branch/negative-geometry claims (§§3–4). |
| Atlas | `atlas-v0.5` (accepted at the owner snapshot) | Targeted H4/H9, D5.L5 TDRG.G1–G9 and D5.X1, NUMGEN DISC interfaces; derived, noncanonical. |
| Governance | `methodology-v1.4`, `CONVENTIONS.md` | Rules governing source identity, grades, two-stage changes, evidence and records, inspected on relevant provisions. |

SHA-256 values are those of the repository release/baseline records; GitHub tag text and Git blobs were retrieved. **Full file SHA-256 was not independently computed in this review.** No symbolic or numerical certificate campaign was rerun. Exact small-group reasoning below is independently derived [SESSION].

## 1. Decision and mathematical nucleus

**Decision [SESSION]: require a TDR-G scientific owner disposition on the path-selector's antipodal symmetry failure before a new C7C-M4 realization campaign; meanwhile make the other corrections in one scoped owner revision.** Do not silently repair the canonical v18 path policy, rewrite past evidence, or withdraw the ten-label NUMGEN existential lower bound without inspecting the policy-independent witnesses.

### TG13-I01 — antipodal endpoint tie: a mathematically genuine covariance obstruction [P0]

**[OWNER: TDR-G v2.12.13 §6.3 lines 568–573; NUMGEN v1.21 §6.6 lines 1953–1969; TDR-G Appendix B lines 1224–1225; §6.12 lines 808–820].**

Let `sc_N` map residues to the half-open centered convention `(-N/2,N/2]`, with even `N`. For reversed ordering of a two-edge path, the endpoint token difference changes sign modulo `N`. For `E_raw ≡ N/2 (mod N)`,
```
sc_N(E_raw) = +N/2 = sc_N(-E_raw).
```
Thus the sign test on `E` is *not antisymmetric* at this one orbit. In the `S=0, E=N/2` sector, both listings can be judged "forward" by the text unless a separately declared orientation/selection rule supplies an order. Sorting endpoint IDs produces a deterministic software path but not a node-relabeling-covariant map of abstract node-labelled relational states.

**[SESSION: explicit witness]** The deposited audit script exhibits `N=24, k=1`, `theta=(0,12,0)`, `delta=(0,1,12)`; on the endpoint ordering `(0,1,2)`, `E=sc(12)=12`; on the reversed ordering, `E'=sc(-12)=12`. A relabelling that exchanges endpoints while transporting the full state changes the selected successor shift in general. There is no intrinsic continuous “positive” sign of the antipodal element, because that group element has order two, i.e. `e=-e` in `Z_N`.

**Important qualification:** this is a counterexample to the **selector on the antipodal tie stratum**, not to the phase-gauge invariance of differences, ordinary signed permutations of the advance spectrum, or every BIND3 class result.

**Acceptance criteria:** owner supplies (i) exact intended covariance group (all node permutations, perhaps joint phase/token transformations), (ii) a counterexample or formal no-go for a selector using only the declared `(S,E)`, (iii) a policy decision: mark the antipodal case as genuinely unresolved/inert; add a provably covariant input/invariant; or explicitly restrict the model with an extra structure and state its scientific consequence. A sorting-by-node-ID convention by itself must be labelled a **presentation-specific implementation**, not covariance. Require a small exact symbolic/permutation counterexample test and negative controls, not a new 3,000-trajectory campaign. TDR-G owner must decide whether the rule change is a new physical policy rather than a metadata patch.

### TG13-I02 — apparent §6.12 covariance PASS is narrower than the failed case [P0/P1]

**[OWNER: TDR-G §6.12 lines 808, 820, §3 SG-2 line 435; Appendix B lines 1224–1225].** At line 820, "Exact ±d mirror symmetry ... (relabeling-covariance check: PASS)" concerns **the inspected ±d families and coarse inventory**; it does not demonstrate equivariance of the `S=0, |E|=N/2` selector under arbitrary permutation of node labels. Likewise the §6.12 coarse class taxonomy invariance under two `P_3` rotation conventions (line 808) is weaker than trajectory-wise covariance of the selector.

**Action/criterion:** qualify the PASS by its actual finite family/test and identify its untested/failed antipodal slice; add the small failing permutation fixture. Keep `BIND3-CYCLE-N24K1` sample and exact-cycle numbers unchanged pending a scoped sensitivity audit. Appendix B's "[FAIL] arbitrary path label fallback" and hidden-referee criticisms apply to arbitrary tie-breaks; they do not automatically prove an impossibility of a *different* intrinsic covariant policy.

### TG13-I03 — DISC witness consequences must be distinguished by evidential level [P0/P1]

**[OWNER: NUMGEN v1.21 §6.6 lines 1953–1969, pipe `pipes/TDRG/20261026-NUMGEN-orientation-policy-s0-e-half-n.md`; audit script `upload/numgen-records/disc2_p2_antipodal_exposure_audit_v1.py`].** Source-reported posthoc audit: 40/136 ratified DISC-2 witnesses encounter the antipodal condition; 96 are unexposed; 216 exposed events occur in enumerated eventual cycles; alternative reverse/inert choices alter 10/20 witness verdict-or-class records. The current owner says **every admitted rational label has at least one unexposed witness**, and tested alternative policies preserve the ten-label *existential* lower bound.

**Action/criterion:** owner disposition should separate (a) per-event covariance failure; (b) exposed individual witness trajectory/verdict dependence; (c) existential label projection robust on the audited panel; (d) **unreviewed** general policy/other panels. Verify if the 96 unexposed are truly unchanged under the proposed corrected rule, then only re-evaluate newly affected witnesses. DISC-1 is not certified by a DISC-2 posthoc audit. Retain `NUMGEN C7C-M4 HOLD` until owner policy ruling; do not reclassify the existing ten labels globally from this evidence.

### TG13-I04 — LEM-RETRIG's "exact period-2" needs a nonzero/least-period qualification [P1 mathematics]

**[OWNER: TDR-G §1 line 39; §6.5 line 630, line 641; AZ v0.6 Thread B cites the same lemma].** LEM-RETRIG correctly gives the two-state update `(epsilon,d)↔(epsilon-d,-d)` under the isolated-dyad swap mechanism. Yet `d=0` is explicitly included in `|d|_c≤2k` and `all offsets retrigger iff d=0`. In the reduced relational dyad, when `d=0`, both maps return `(epsilon,0)`: the state is a **fixed point (least period 1)**, even though each tick still triggers a swap. This is not an exact least-period-two state orbit. Moreover `d=N/2` may alias `-d=d`, so least period is a property of the full pair `(epsilon,d)`, not merely event alternation.

**Action/criterion:** specify "period divides two" / "retrigger on every tick" for all `d`, and certify least period exactly 2 only for nondegenerate states with `(epsilon-d,-d)≠(epsilon,d)`. Apply at both §1 and §6.5 and the regime table; leave the overlap existence and `|d|_c≤2k` threshold untouched. A two-line exact counterexample at `d=0` suffices; no brute-force rerun.

### TG13-I05 — LEM-SPECCONS confuses a stronger spectrum with its coarser gcd image [P1 mathematics]

**[OWNER: TDR-G §6.12 lines 804–806, §3 SG-12 line 465; §1 line 39].** Signed permutation of pairwise `d` proves invariance of the multiset of centered magnitudes `{|d_ij|_c}`. Applying `gcd(d,N)` yields an invariant gcd-spacing multiset. These are **not equivalent invariants**: e.g. with `N=24`, magnitudes `1` and `5` have the same gcd spacing 1, but different centered magnitudes. The sentence "**equivalently**, the multiset ... gcd" is false if it states logical equivalence rather than consequence.

**Action/criterion:** replace "equivalently" by "**therefore, in particular**" at line 806; preserve both invariants with the stronger⇒weaker direction. One-line correction in §6.12, optional explanatory note in §1/§3 if needed.

### TG13-I06 — headline scaling scope and exponent consistency are stale [P1 evidence/scope]

**[OWNER: TDR-G §1 lines 10, 49–53; §5 lines 500–501; §6.8 lines 708–723; §3 SG-6 line 447; Atlas v0.5 TDRG.G1].** The full range `N=120–1440` uses the convenience composite `-0.869`; a `N=480–1440` restricted fit is recorded as approximately `-0.730` in the Atlas diagnosis and needs owner-side scope qualification (not automatic substitution of one fit for the other). Section §1 and §6.8 line 723 assert `1.593≈0.757+0.836` although §6.8 line 714 declares `chi` a composite ratio without a single power law and the newer section refers to `cs/row∼N^{-0.73}`. `0.836` is a superseded exponent. The sentence saying three-decimal equality **confirms** power laws simultaneously is too strong for fitted exponents and non-power-law chi.

**Action/criterion:** attach fit range, conditioning, observable and status to every headline exponent; remove the obsolete chi exponent from live consistency, or label it archival without promoting a different sum; state the `N→∞` crystallization as HEUR only. Do not rerun full scans for an editorial range correction. An audited refit is necessary only if the owner chooses a new quantitative headline.

### TG13-I07 — grades and closure are misaligned at the front of the DSN [P1 documentation]

**[OWNER: TDR-G §1 lines 10, 49–63, §2 lines 71–90, §5 lines 500–507, §6.8 lines 721–729].** The status summary says TDR-24 chain must close before triad dynamics, without acknowledging D/F closures and open A/B/C; the high-risk table line 505 calls the analytic `psi`-intensiveness explanation TDR-24F OPEN while §1 lines 61–63 call F numerically resolved. `NUM strong`, `HEUR strong`, `ALG/NUM strong`, and a bare THM appearing alongside numerical fits require graded scope at use; a finite scan `R²` is not an analytic theorem.

**Action/criterion:** one current-state rewrite of §1/§5/§2 reflecting D/F status versus residual analytic constants and A/B/C; keep mathematical structural identity, numerical fit, engineering verification, conjectural continuum extrapolation distinct. Do not close TDR-T or elevate finite-N observation to asymptotic proof.

### TG13-I08 — current RID inventory and evidence custody must be separated [P1]

**[OWNER: TDR-G §2 lines 94 onward; §§6.1–6.12, §7 lines 836–853, §8 lines 856–867; Methodology v1.4 §4.4].** Owner has many `TDRG-OPEN-*`, `TDRG-ART-*`, `TDRG-EXPORT-*` keys; the core scientific theorems/definitions at §§6.1–6.5 (holonomy, narrow-band, reachability, selector, star rule), LEM-SPECCONS, BIND3-CYCLE and the §6.12 parity/spectral gate **lack stable claim RIDs**. The user-reported "34 RID" count is **unverified by this review as a scientific-RID census**: artifact and OPEN IDs are not substitutes for THM/ALG claim IDs. The §8 lines explicitly say several session-held scripts should be consolidated into the repository, not that they are present and independently replayable.

**Action/criterion:** inventory separately `DEF/THM/ALG`, OPEN, ART, EXPORT and legacy LEM names. Assign owner-approved collision-checked claim RIDs to the exported/load-bearing definitions/lemmas first, with evidence state `held / placed / replayed / missing` and exact original hash when verifiable. Do not invent certificates or require full expensive reenactment for a documentation edition.

### TG13-I09 — Methodology v1.4, current-only structure and pin hygiene [P1/P2]

**[OWNER: TDR-G header lines 1–21; §7 lines 836–853; §9 lines 871–876; Appendix A lines 891–1217; CONVENTIONS §§1–4].** The tagged header still declares Methodology v1.2, Programme v1.1, OFN v0.6 as "companion" context, a supersedes field with multiple non-immediate ancestors, a historic project repository label, and extensive date/grade overlays. These are *not* all scientific errors: old v0.6 and v1.1 can remain claim-specific proof/context pins intentionally, whereas their depiction as currently governing editions is stale (Programme now v1.3, OFN v0.10, Methodology v1.4). The historical version entries and footer chain require planned compaction, not a blanket pin rewrite.

**Action/criterion:** a staged successor: Stage 1 repairs theorem/scope/interface/RIDs under an assertion-gated edit log and owner dispositions; Stage 2 relocates history with a movement map and negative controls, respecting Methodology §13.6. A single predecessor tag/full hash, one footer, §1 concise or declared exception. Preserve every historical proof pin and original source evidence via the predecessor tag.

### TG13-I10 — cross-stream interfaces and consumer acceptance are underregistered [P1]

**[OWNER: TDR-G §7 lines 836–853; Programme v1.3 §6.4 and IF03/13/21/25/32; OFN v0.10 §4.1 lines 248–254 and §11 REQ-O09-05; AZ v0.6 §§3–4; NUMGEN v1.21 §6.6].** TDR-G §7 says there are no scientific imports and lists only Programme v1.1/OFN v0.6 context. Current partners include (i) OFN constraints and Finding A *offered* under XFER-O08-01, **not accepted into TDR-G**; (ii) NUMGEN DISC consumer and a pending scientific path-orientation request; (iii) AZ Thread B/C branch-local citations, while its tested `4|q` graph angle is disqualified as a TDR-G dynamical bridge candidate; (iv) GEN possible continuous phase use **blocked** absent OPEN-P1 theorem. A notice being filed does not assert use; an older pinned context is not an error solely due to edition age.

**Action/criterion:** four-way §7 Imports / Exports / Consumers / Pins, or equivalent explicit matrix, separating *received / statement accepted / adopted-use* and named scopes. OFN Finding A remains OFN-owned until TDR-G accepts custody; NUMGEN C7C-M4 remains HOLD; AZ owns its graph algebra, not TDR-G model physics. Programme IF entries are authority for routing only, not transfer of owner results.

### TG13-I11 — OFN Finding A is a different covariance question from P2 endpoint relabeling [P1]

**[OWNER: OFN v0.10 §4.1 lines 248–254, §11 REQ-O09-05; TDR-G §6.3 lines 566–576, §3 SG-2 line 435].** OFN's `RTG-OFN-ALG-STAR-TOKEN-SHIFT` checks `B_c:δ_i→δ_i+c` and the star map `(δ_A',δ_E')=(-δ_A,δ_A)`. The difference changes by `-2c`, so its fixed-map condition is `2c=0 ​(mod N)` (even N: c=0 or N/2), **conditional on the same covariantly selected component**. TDR-G P2 instead tests permutation of **node labels** for path orientation. One result cannot discharge the other; a path selector that is not covariant can also obstruct global state equivariance, beyond the fixed-local-map result.

**Action/criterion:** two distinct owner disposition entries: XFER-O08-01 for common-token shift and REQ-O09-05 for full-selector/antipodal policy; explicitly scope any adopted use. Do not treat OFN Finding A as an implicit TDR-G theorem or as a full-model gauge/no-go.

### TG13-I12 — physical interpretation and AZ negative result stay limited [P2]

**[OWNER: TDR-G §3 SG-10 lines 459–460, §6.8 lines 708–731; AZ v0.6 §§3–4].** AZ's first static-`Z_N`/Hashimoto `4|q` angular signal was reclassified as **substrate geometry**, not TDR-G dynamic evidence or an OPEN-P1 bridge. This negative result cannot be repurposed as confirmation of TDR-G's policy N-scaling or the continuous Dyadic arithmetic story. The TDR-G `bound_symmetric` policy is empirically useful but remains owner OPEN TDR-19 as a selected physical law; `N→∞` suppression is extrapolative.

**Action/criterion:** a scoped consumer/navigation sentence if AZ is cited, maintaining the discrete-continuous firewall and the independent policy-selection OPEN.

## 2. Proposed owner handoff and acceptance gates

1. **Immediate scientific owner question:** rule on `S=0, |E|=N/2`, give minimal exact covariance test and decide the physical policy scope (I01–I03); publish a targeted witness-effect table, not a whole new DISC or BIND3 campaign. Preserve upstream original evidence unchanged.
2. **Single batched Stage-1 pass:** resolve LEM-RETRIG least-period caveat (I04), LEM-SPECCONS logical direction (I05), scaling/grade wording (I06–I07), priority scientific RIDs and proof custody (I08), and interface dispositions (I10–I11) without silent adoption or grade promotion.
3. **Stage-2 documentation pass:** migration to Methodology v1.4 and current-only compaction with explicit movement map and archived history (I09); references to AZ and negative results scoped (I12). Each source ID, domain and negative result remains traceable to its earlier tag.
4. **Receiving checks:** verify the exact changed claims, selector counterexample and bounded witness sensitivity, with an assertion-gated source diff; no full numerical campaign by default. The other blind Atlas pass is reconciled *after both reports are frozen*; PI decides dispositions; TDR-G co-owners prepare the successor.

## 3. Limits

This review **does not claim** that the P2 selector admits no possible covariant completion with extra data; that the 96 unexposed witnesses prove a universal policy-independent spectrum; that any existing exact enumeration is false globally; that `d=0` invalidates the LEM-RETRIG overlap criterion; or that stale source pins alone justify re-running scientific tests. Independent derivations are tagged [SESSION], not adopted owner theorems.

**No canonical owner file changed, no notice marked accepted, no scientific release authorized.**
