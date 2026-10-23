# RECOG v0.3.22 — independent Atlas advisory review

**Date:** 23 October 2026. **Reviewer:** ChatGPT. **Status:** SESSION / NONCANONICAL; not owner adoption or a DSN amendment.
**Reviewed proposal:** PR #13, `c548bab259cea349ad252fc0b4927340ab390687`, `records/recog/ATLAS_ADVISORY_NOTE_RECOG_v0_3_22_v0_1.md` (Claude pass).
**Decision:** ACCEPT THE MAINTENANCE DIRECTION, WITH SCOPED REVISIONS TO THE ADVISORY. Combine the two passes into one owner-directed proposal; do not execute the preliminary wording literally where narrowed below. One substantive owner successor is appropriate. Tier-C research is not a maintenance release gate.

## 1. Source manifest and verification boundary

[SESSION] RECOG v0.3.22 was read completely: **1,581 lines, 329,148 bytes**, including header, every section, artifacts, provenance and both appendices. Mounted bytes have SHA-256 `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9`; their Git blob `3025d5805fd5f6322b7d0d7c164cdce2de45583d` matches the connector's `recog-v0.3.22` response. Line numbers below refer to these exact bytes.

The preliminary 184-line advisory was read completely, in overlapping source slices. This is an independent source assessment after reading the peer's note, **not a blind review**.

| Source | Edition and inspection |
|---|---|
| RECOG | `recog-v0.3.22`; full reading and local byte/blob identity check |
| DYAD | `dyad-v6.4.22`; targeted current passages in §6.14 (NF6-DEG10, per-block phase, row-A L-PHASE and provenance) and §§6.15–6.16 (formal/smooth distinction, finite reproductions); current-owner identity from GitHub blob `3c300a11a6da8725a97d967d0ffececd597985d4`. Not a fresh full DYAD audit. |
| NUMGEN | v1.20.8; targeted §6.6 definitions, L-BACKBONE/L-MONO/L-PHASE/INF-1 and receipt/dependency records; mounted SHA-256 `835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e`, matching tagged blob `0c8ec462e62e2e6d0b50477c1311eda39e51311c` |
| RRF | v0.8.4; receipt/interface passages and §6.3 W3; mounted SHA-256 `2fb0a0fe9d998be91618cb731e2dee7301952ffdbe374f4889dd5e61c5cbafce`, matching tagged blob `6882fd517e548e5d6a9aecad9c958af74fe447dc` |
| RER | supplied adopted noncanonical v0.2; adoption scope and G9 source/receipt passages; mounted SHA-256 `58feee5ff1f16a37fc4ee029f24499928ea7439731de0a090d8794c1cbe57ad0`; relevant sections, not another full registry review |
| Methodology | `methodology-v1.4`; §§3.3–3.5 checked directly, with the established §§4/12/13 preservation and adoption contracts as review framework; not a new full methodology review |
| Atlas | accepted v0.2 is the routing basis of the advisory and preceding Atlas reviews; the tag object was verified. No new full-Atlas reading or reconstruction in this pass. |

Executed here: **12/12 bounded algebra/inequality checks** in `evidence/recog/atlas_review/recog_advisory_checks.py`, plus a source-syntax inventory. The written convergence proof in §5 is not inferred from numerical tests. No inherited Arb, saddle/heteroclinic, token-production or normal-form certificate campaign was rerun. Source-reported execution remains source-reported.

## 2. Corrections to the proposed actions

### 2.1 FA-03: retain the valid leading-order guard

[OWNER: RECOG v0.3.22 SG-R10, §§6.13–6.13a, L341/691/703–716] The standalone leading oscillation bound is **not** a finite-amplitude bound for the entire exact memory. R9 does not invalidate that warning. The exact theorem includes the isotropic term and a remainder:

\[
M(z_0)=q_0[c_{\rm iso}+\Lambda_1(\Theta_0)]+R,\quad
|R|\le C_2q_0^2,\quad |\Lambda_1|\le |G|.
\]

[ALG; SESSION: elementary consequence of that statement] Hence
\[
|M-c_{\rm iso}q_0|\le |G|q_0+C_2q_0^2,
\qquad |M|\le (|c_{\rm iso}|+|G|)q_0+C_2q_0^2.
\]

Replace stale research-routing wording by a pointer to these certified rows, **not** by saying that `0.007652 q0` bounds the full memory. Keep the `C_z` track, normalized `q`, and paired `(C2,qmax)` rows; comparator incompleteness requires the smaller `q0 < |G|/C2` window.

At L797, distinguish the degree-7-and-higher partial budget `2 C7 q0^2` from the complete R9 remainder `C2 q0^2`. The printed phase-independent thresholds use the amplitude `|G|`, not the phase-dependent `|Lambda1(Theta)|`, which has zeros. If this partial-budget calculation remains, name it as such and do not substitute it for the full incompleteness criterion. Old planning text may be archived; its currently used hypotheses must remain live.

### 2.2 FB-14 / FC-22: an exact involution is not an exactly commuting involution

[OWNER: RECOG v0.3.22 §6.14, L795; DYAD v6.4.22 §6.14 consumer cross-reference and §6.16 finite reproductions] The RECOG object
\[
S_h=h_6\circ(-I)\circ h_6^{-1}
\]
is an **exact involution on its defined domain**. The certified commutation is only through degree six. With `R0` the formal owner involution, write
\[
j^6S_h=j^6R_0,
\]
not `S_h = j^6 R0` as an identity of full maps. If a producer uses `S6` for the polynomial jet, name that separate object explicitly. The current DYAD finite reproduction states the equality of the truncated compositions and notes that its degree-six check reproduces `S6`.

The smooth commuting realization can be referenced at its owner-stated germ scope; do not identify it with the delivered finite-chart action, transfer finite-chart radii to it, or infer that it implements physical pole/node exchange. It does not discharge the raw linear-swap covariance premise of §6.4. R1 and RRF OPEN-A remain open.

FC-22 may transfer the **leading** section-shadow coefficient after matching frames and the second jet. It does not supply a finite-Q offset, a global domain or a physical token identity.

### 2.3 FB-10: identifier text and current assertion type

[SESSION] The proposed narrowing of the prefix complaint is accepted. Existing `THM`, `RESULT`, `CAND` or `OPEN` words inside an RID do not set its present grade; do not rename an established RID solely for that reason.

`RECOG-OPEN-INTERSECTION` needs an explicit distinction between the HYP scientific assertion and the OPEN task/R6 status. That is a clarity/typing repair, not by itself evidence of a mathematical contradiction. Repeated summaries of `RECOG-ALG-LEADING-RETURN-EQUIVARIANCE` should point to its authoritative §6.12 statement. `E2C-ENG-SPLIT-REFINEMENT` needs an owner-approved custody/identifier mapping; no silent namespace rewrite.

### 2.4 Correction before compaction; actual receipt before receipt status

[SESSION] A two-stage successor is appropriate, but substantive status/grade/scope repairs belong in stage 1. Stage 2 must not manufacture the current grade, change a theorem's hypotheses, or delete a live obligation merely because it occurs inside an old specification. Keep the corrected intermediate hash and a per-block movement map.

Calibrate the checker on RECOG's header, anchors, alias grammar, artifact and OPEN forms. Passing the DYAD pilot does not itself validate a new document profile. Check both successful moves and negative controls for scope deletion, wrong RID attachment, missing evidence pointers and stale-state preservation.

N19/N21 are prepared notices, not delivered receipts. Reading their content for this review does not invent receipt by RECOG. Preserve RECOG §7.3's notification distinction: material changes to existing exported claims need the required pre-release consumer notice; additive exports and final identity notices follow their stated release procedure. A candidate notice and a final adopted-hash notice are different records.

## 3. Disposition of the 22 peer rows

These are reviewer recommendations, not owner dispositions. `SUPPORT` means the scoped action is justified, not that its implementation is already complete.

| Peer row | Receiving assessment / required scope |
|---|---|
| FA-01 | SUPPORT WITH STAGING CORRECTION (§2.4). Current-only header; preserve qualified live claims, rejection constraints, OPEN questions and actual evidence; archive obsolete prose at its pinned predecessor. Expand the stale F2 target search as in IRR-03 below. |
| FA-02 | SUPPORT. NUMGEN v1.20.8 has the requested definition and INF-1 RIDs. Their formulas and allocation guard match the RECOG imports. Repin claim by claim; keep the overlap-domain distinction. |
| FA-03 | REVISE AS §2.1. The old reference-only T1/T2 wording is stale; the leading-amplitude warning is not false. Current rows and partial budgets must not be conflated. |
| FA-04 | SUPPORT. Replace the stale flag by the owner's lifted-versus-wrapped inventory; retain that distinction and the winding index. |
| FA-05 | SUPPORT WITH RECEIPT BOUNDARY. N11 is used in A1a; N13 already records its use. Update current consumers, but retain actual input pins and distinguish prepared/sent/received/accepted/adopted-use. Fix the note's cross-reference `FC-RECOG-18` to `FC-RECOG-19`. |
| FA-06 | SUPPORT for the successor. v0.3.22 was adopted under v1.3; migration is a new-release action, not retroactive noncompliance. |
| FA-07 | SUPPORT RECOVERY, WITH DISCLOSED ACCESS LIMIT. Recover exact originals where available; do not recreate historical adoption or hashes. A new release needs its own explicit adoption record. Historical absence and the inherited scientific grades remain separate. |
| FB-08 | SUPPORT. Map each consumed claim to the new DYAD RID; retain missing-RID exceptions for genuinely unassigned results. A dependency loop is not created merely by the critical-curve definition pointing to RECOG's stronger fold result. |
| FB-09 | SUPPORT CLAIM-LEVEL AUDIT, NOT BLIND REPIN. Preserve actual proof-source editions and distinguish current counterpart from historical producer input. New anchors do not make old line references false at their own pins. |
| FB-10 | ACCEPT THE NARROWING, with §2.3. No renaming from prefix/grade mismatch. |
| FB-11 | SUPPORT OWNER DECISION. Prioritize externally consumed claims; an explicitly identified substatement under an existing result may suffice. Do not register every small internal consequence automatically or assign new owner RIDs from the advisory. |
| FB-12 | VERIFIED by exact formulas and numerical display: raw ratio 41.2694355..., post-H2 ratio 59.1194304.... Label the actual coefficients/frame; do not silently replace the raw calculation by an NF claim. |
| FB-13 | SUPPORT, including the qualification at L457 (IRR-04). Magnitudes transform by the named linear scale; leading coefficients are unchanged under the specified tangent-to-identity changes, not arbitrary rescaling. |
| FB-14 | REVISE AS §2.2. Correct jet equality; preserve exact involution versus finite-order commutation and physical-action boundaries. |
| FB-15 | SUPPORT. RRF v0.8.4 quotes same-space W3 and labels different-space transport as an OPEN extension. RER records its G3 input. Reflect their actual recorded use, without inventing an unsent notice receipt. |
| FB-16 | SUPPORT NARROWLY. Existing mutual citation already distinguishes DYAD's bridge RID and RECOG's general-p proof/result. State this instead of an obsolete recommendation; do not silently transfer ownership of the general theorem. |
| FB-17 | OPTIONAL EDITORIAL IMPROVEMENT. A local block-index rename is reasonable with a reversible symbol map; a notation dictionary also resolves the overload. Keep imported `D_M` and memory `M(z0)` distinguishable. |
| FB-18 | SUPPORT INVENTORY. Record claim, exact artifact identity/hash, locator, availability, execution and missing dependencies separately. File absence or no second Arb run alone is not a proof refutation. |
| FC-19 | WRITTEN DERIVATION VERIFIED IN THIS SESSION (§5). Available premises give existence on the explicit U without R9 or INF-1. Owner review/adoption still required; no silent domain enlargement of the existing NUMGEN-based result. |
| FC-20 | VALID ROUTE, CONDITIONAL ON THE THRESHOLD DEFINITION. Specify first-passage indices, eventual direction/monotonicity and vanishing overshoot before deriving the ratio; equal rate does not identify two event streams. Optional research, not a maintenance gate. |
| FC-21 | CONDITIONAL ROUTE ONLY. Apply the finite-order equivariance argument after checking the actual GEN map, common block linear action and domain/closure restriction. It does not recover the missing original `GEN-ART-G2-CHRONO` bytes. GEN owns the conclusion. |
| FC-22 | SUPPORT AS SCOPED JET COROLLARY. The second-jet match gives the same leading coefficient, with the same O(1) limitations; see §2.2. Owner verification, no new physical exchange claim. |

The four routed items can remain with their designated owners. For GAP-LOCK Lemma 3, distinguish its ALG use in the exact log-equivalence proof from the separate HEUR cross-reference in R6. VF-1 can be cited directly as `DYAD-ALG-NF6-DEG10`; that is identifier/provenance routing, not a new parity proof.

## 4. Additional point-of-use findings

### IRR-01 — RESULT grammar in live scientific blocks (next-release action)

[SESSION: complete-source syntax inventory] In §§1–6 through L1111 there are **19 line-leading RESULT blocks** not carrying the single canonical `[from: TAG]` form: **16 without a from field**, and three noncanonical combined/qualified forms at L487, L927, L1003. Locations: L487, 548, 837, 853, 865, 873, 905, 927, 956, 995, 999, 1003, 1019, 1021, 1030, 1052, 1054, 1108, 1110. This bounded scan excludes §9 credits, history, table cells and headings; it is not a claim that every other tag has been validated.

Methodology v1.4 §3.4 makes RESULT a synthesis marker, not a grade. Attach one justified grade to each conclusion or split heterogeneous conclusions. In particular, `[from: NUM strong, ALG]` and `[from: THM, ALG, RESULT]` are not single grades. Preserve registry-relative conclusions, conditional assertions and physical nonclaims. This requires owner review in stage 1, not an automatic global relabel in stage 2.

### IRR-02 — A missing remainder in the high-risk summary

[OWNER: RECOG v0.3.22 L416 versus L572] The §5 radial-neutrality row prints
`Q(T^6(t,0))-t^2 = 6 gamma t^6`, while the governing §6.7 example includes `+O(t^8)`. Restore that remainder or explicitly say 'degree-six term'. The cubic-neutrality conclusion remains unchanged. This repairs an overstrong summary; it is not a new refutation of the owner result.

### IRR-03 — Stale F2 follow-ons beyond the initial list

[SESSION: source comparison] FA-01 should also cover L927 ('remaining F2(a)'), L956 ('Next: F2(c0)') and L972–974 (F2(c1) posed as the current follow-on). Their subsequent owner sections record the scoped closures. Replace these at their points of use with current result pointers and the actual R6 residual. Preserve F2(a3)'s selection question, registry-relative limits, lack of independent write-through, and W1–W5. Do not close R6.

### IRR-04 — Frame wording and exact/rounded quantities

[OWNER: RECOG v0.3.22 L451/L457, L703/L713–714/L797] L451 correctly says that the leading coefficient's magnitude changes under linear rescaling; L457 ends with an unrestricted 'leading coefficient ... frame-independent'. Restrict the latter to the stated tangent-to-identity comparison; refer arbitrary complex linear scaling to the frame rule. Do not infer norm-by-norm strict contraction under arbitrary coordinate changes.

[ALG/NUM; SESSION] `|G| = sqrt(481897)/90720 ≈ 0.007651984290981194`. Replace the rounded equality `|G|=0.0076520` by an approximation or a certified upper bound. Likewise keep `|G|/517` and `|G|/163` exact, with approximate displays `1.4800743309e-5` and `4.6944688902e-5`. The partial-budget thresholds `|G|/(2 C7)` are different and are not the full incompleteness windows. This can be combined with FA-03/FB-12/13 rather than creating another review cycle.

## 5. FC-19 — R9-free existence on the explicit U

[THM; SESSION: deduction from the following owner premises, not registered or adopted]
Fix `x0` in `U={0<Q0<=1/625}`, put `a=Q0^{-1}>0`, `Q_m=Q(T^{6m}x0)`, and use the increasing primitive lift of the RECOG A1a interface. The local extension is `D_N^U`; agreement with NUMGEN's `D_N` is asserted only on their common domain.

**Premises actually used:**
1. DYAD v6.4.22 §6.14, `DYAD-THM-LPHASE-ROWA-REMAINDER`: block base points stay in U; intermediate points in U_T; the lifted block increment is `2pi-tau Q_m+r_m`, with `|r_m| <= (403/250)Q_m^{3/2}`. This theorem is not conditional on R9.
2. RECOG v0.3.22 §6.13b, `RECOG-THM-A1A-RECIPROCAL-AMPLITUDE`: `Q_m^{-1}=a+m+O(sqrt(m))`, hence `m Q_m -> 1`; its proof uses the primitive contraction/radial bound, not R9.
3. The interface/lift alignment identifies the same block clock, starting point, sign and observable. No B-event re-anchoring occurs.

**Claim.** For every such fixed `x0`,
\[
C_D^{\rm ext}(x_0)=\lim_{N\to\infty}(D_N^U-\tau\log N)
\]
exists and is finite, without R9 or NUMGEN INF-1.

**Proof.** Write `u_m=Q_m^{-1}=a+m+e_m`, where `e_m=O(sqrt(m))`. For sufficiently large m, `u_m >= (a+m)/2`. Thus
\[
Q_m-\frac1{a+m}=-\frac{e_m}{u_m(a+m)}=O(m^{-3/2}).
\]
Both `sum_m |Q_m-1/(a+m)|` and `sum_m Q_m^{3/2}` converge; the finitely many initial terms are harmless. The second also proves `sum_m |r_m|<infinity`.

For `x>=0`,
\[
0\le x-\log(1+x)\le x^2/2.
\]
The two inequalities follow by differentiation and equality at zero. Therefore
\[
t_m=\frac1{a+m}-\log\left(1+\frac1{a+m}\right)
\]
is summable. Telescoping logarithms gives
\[
H(a):=\lim_{N\to\infty}\left[\sum_{m=0}^{N-1}\frac1{a+m}-\log N\right]
=-\log a+\sum_{m=0}^{\infty}t_m.
\]
The exact lifted law gives
\[
D_N^U=\tau\sum_{m=0}^{N-1}Q_m-\sum_{m=0}^{N-1}r_m.
\]
Consequently
\[
\boxed{C_D^{\rm ext}=\tau H(a)
+\tau\sum_{m=0}^{\infty}\left(Q_m-\frac1{a+m}\right)
-\sum_{m=0}^{\infty}r_m.}
\]
Every correction series is absolutely convergent. This proves the claim. The same estimates give an orbitwise `O(N^{-1/2})` tail, with constants not evaluated here; no uniform numerical bound on a new domain is claimed. QED.

**Phase consequence.** The existing exact finite-block identity is
\[
D_N^U-\tau\log N=\tau\log Q_0-
(\Psi_W(N)-\Psi_W(0))-\tau\log(NQ_N).
\]
Since `NQ_N -> 1`, it yields convergence of `Psi_W`, and the vanishing finite-chart offset yields the corresponding `Psi_z` limit. Equivalently, the now-proved H-NG premise supplies the existing conditional `RECOG-THM-A1A-PHASE-EXISTENCE-ALT`. No R9 invocation is hidden in the summability step.

**Scope and ownership.** This is an explicit-domain derivation of existence and the associated identity, not the R9 lattice-memory expansion. It supplies neither `c_iso`, `Lambda1`, `C2`, R9 comparator incompleteness nor an R9-free quantitative OPEN21 theorem. It gives no result for all starts in `U_T` outside `U`, no physical memory/token mechanism, and no independent extension of NUMGEN's adopted domain. It parallels NUMGEN's existing summability argument but combines the cited explicit-domain owner premises. RECOG should register/adopt any new explicit-domain consequence under its own identity and retain the original NUMGEN-based route; merely editing the existing restricted result's domain would conceal a scientific change. Adoption of this Tier-C deduction is optional for the maintenance release.

## 6. Evidence recovery and completion contract

[SESSION] At the inspected PR13 snapshot, `records/recog/` contains only the preliminary advisory, and `evidence/` has atlas/dyad subdirectories, no RECOG directory. The mounted runtime has no original RECOG release records; none was found in member-name searches of its **seven available ZIPs**. This is a bounded availability report, not a search of every historical commit, other account or external archive. Some earlier attachments are no longer available in this session. No original was reconstructed or uploaded as if recovered.

The owner should maintain a source-recovery inventory with original names, printed hashes, RID/use, exact source location, access state and next recovery action. Expand abbreviated filename groups only after obtaining their actual names. Distinguish full-hash verification from short-hash corroboration. The separately delivered registry inventory is a starting list, not a declaration that an artifact never existed.

The merged advisory should request: completed per-row dispositions; one reviewed owner successor; recorded intermediate and final identities; explicit correction and compaction deltas; per-profile checker/control results; current import and consumer tables; and honest recovery/notice limitations. 'Noted for a future release' alone is not implementation of an accepted current-state correction. Optional research and consumer adoption delays remain separately tracked. A missing archived record is not itself a mathematical counterexample; its treatment as an accepted release limitation needs the owner's/PI's explicit decision.

## 7. Administrative checks separate from RECOG science

[SESSION] `atlas-v0.2` is an annotated tag object `4cf0b9be5bb71d1c120acaa3c248873c263d163d` pointing to merge `6c526669181e4950a7d0361f178f9b49f8940c37`. Its message gives the expected Atlas SHA-256 `9963aead02fad686a9a5bd4d1824882a890ef6279d50899c4090e0e5092331c5`. This tag/metadata check is not a new whole-Atlas byte replay.

PR #12's decision-only delta records the acceptance and limitations, but its header still says DRAFT / PI decision pending at `ca78cbf55ef4bb175f048826358ca538876727eb`. Align that one status line with its completed §3; no Atlas content revision or tag movement is necessary. The post-publication acceptance-record commit should be cited separately from the already published tag.

The inspected `claude/dyad-sources` tip `f1fbb3ae981fcc5cfcd7aadf950961e45dd3ca8e` is an ancestor of the Atlas merge (comparison ahead 15, behind 0), so its commits remain in main history. The `missing-files` comparison returned 404; its custody was not established. No branch deletion, PR merge, release tag or owner adoption is performed by this review.
