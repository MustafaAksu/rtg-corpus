# Number Genesis — owner disposition of the v1.20.8 advisory (Claude co-owner session)

**Date:** 26 October 2026. **By:** Claude, NUMGEN co-owner session; this is the session that built and released v1.20.8. **To:** the other NUMGEN co-owner session (ChatGPT), the atlas owner, the PI.
**Status:** owner disposition record, one per co-owner session (hand-over of 26 Oct 2026). Nothing in a DSN changes here. Where the two co-owner records differ, the atlas owner reconciles and the PI decides.
**Object:** `numgen-v1.20.8`, `dsn/RTG_NUMBER_GENESIS_DSN.md`, SHA-256 `835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e`. Line numbers refer to that file.
**Inputs read:**
- `CONVENTIONS.md`, including §7 as amended;
- `pipes/README.md`;
- Methodology v1.4 §§0 header, 1.1, 3.3, 3.4, 4, 12, 13.6–13.9;
- `records/numgen/ATLAS_ADVISORY_NUMGEN_v1_20_8.md`, `…_INDEPENDENT_CHATGPT.md`, `…_RECONCILIATION.md` §3, and `NUMGEN_COOWNER_ENTRY_NOTE.md`;
- inbox `pipes/NUMGEN/` (one item);
- the four outbound items filed on NUMGEN's behalf.

Owner sources read at their tags:
- RECOG §6.13b (`recog-v0.3.24`, `8c64bea2…69e7c1`);
- DYAD §6.14 `DYAD-THM-LPHASE-ROWA-REMAINDER` and §6 `DYAD-THM-OPEN18` (`dyad-v6.4.22`, `2363ca40…8c29`).

All sources are `EV-SRC-READ`; no certificate was run (`EV-NOT-RERUN`).

## 1. Summary

I accept every row of reconciliation §3. Most rows are accepted with a change that fixes the owner choice. The owner decisions are:

- **NA-01 / I01–I03 (RECOG explicit-U theorems).** The acceptance matrix is in §2.
  - **Custody form:** consumer-side confirmation, recorded in §9.1 with a one-line pointer at each affected §6.6 statement.
  - **No import by RID from RECOG in v1.21.**
  - Every NUMGEN statement keeps its existential tube, its proof and its `[RESULT] [from: ALG]` grade.
- **NA-02 / I04 (Dyadic row-A).** **Execute the import** of `DYAD-THM-LPHASE-ROWA-REMAINDER` in v1.21.
  - It enters as an imported `[THM]` block at source grade.
  - Scope: block base points in `U_D` and one-step branch on `U_D,T`, with pin `dyad-v6.4.22 §6.14`, producer edition v6.4.19.
  - The §6.6 OPEN sub-item closes by import.
  - NUMGEN's own L-PHASE (existential `C`) is unchanged.
  - No other Dyadic pin moves.
- **NA-03 / I08 (domains).** An alias table plus labels at every point of theorem use; no global rename. The labels are in §3.
- **NB-07 / NB-08 (RIDs).** The priority list and proposed identifiers are in §4. GAP-LOCK 1–3 come first. Module OPEN RIDs stay lifecycle records and point to the new result RIDs. Nothing is renamed.
- **I06 (TDR-G orientation).** Hold C7C-M4 and continue the abstract WD-DOM design. The dependency goes into §2 and the release record. The outbound TDRG item gets one clarifying sender line (§6).

## 2. NA-01 / I01–I03 — acceptance matrix (RECOG v0.3.24 explicit-U theorems vs NUMGEN statements)

Domains use the labels of §3:
- `U_NG`, `U_NG,T` is NUMGEN's existential L1 tube, with no stated radius.
- `U_D` = {0<Q≤1/625} and `U_D,T` = ⋃_{j<6} T^j(U_D) are DYAD-THM-PRIM-CTR's explicit base and tube.
- RECOG's `U` is the set `U_D` (RECOG §6.13b), labelled `U_R` where RECOG's use is meant.

All three domains use the lifted primitive chart and the frame W = ρ+ωη (the same object as NUMGEN's W; NUMGEN L-MONO), with Q = Q_true primitive. The block clock is F = T⁶ from the start, with M the block count, in all three.

| NUMGEN statement (v1.20.8 §6.6) | RECOG / other counterpart | Event predicate / anchor | Lift | Domain (NUMGEN → counterpart) | Clock / index | Estimate typed | Counterpart grade | **State in v1.21** |
|---|---|---|---|---|---|---|---|---|
| L-BACKBONE `NUMGEN-RESULT-N5AS1-L-BACKBONE` (q_m = Θ(1/m), 1/q_M = M+O(√M)) | `RECOG-THM-A1A-RECIPROCAL-AMPLITUDE`: \|Q_{m+1}⁻¹−Q_m⁻¹−1\| < (15/2)√Q_m | none (amplitude only) | — | `U_NG` → `U_R` (starts), orbit in `U_D` | block m | **increment error** only (type 1). It is not a backbone/tail constant | THM | independent agreement; recorded, not consumed; 15/2 is never entered as the L-BACKBONE constant |
| L-MONO `NUMGEN-RESULT-N5AS1-L-MONO` (δ_T = π/3+O(√Q); π/6<δ_T<π/2 after shrinking) | `RECOG-THM-A1A-LIFT-ALIGNMENT` (π/6<δ_T<π/2 on explicit `U_D,T`); DYAD (B): \|δ_T−π/3\| ≤ arcsin 0.04654 on `U_D,T` | — | same increasing lift, principal one-step increments (NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT) | `U_NG,T` → `U_D,T` | one step | branch bound | THM (both) | independent agreement; DYAD (B) enters with the NA-02 import; RECOG's version recorded, not consumed |
| L-PHASE `NUMGEN-RESULT-N5AS1-L-PHASE` (Λ₆ increment 2π−τq_m+r_m, \|r_m\| ≤ C q_m^{3/2}, C existential) | `DYAD-THM-LPHASE-ROWA-REMAINDER` (R): \|r_m\| ≤ (403/250) Q_m^{3/2}, base points in `U_D` | — | same (I1–I5) | `U_NG` (existential C) → `U_D` base points | block m; q_m (NUMGEN) ≡ Q_m (DYAD), primitive | remainder ceiling | THM (DYAD) | **consumed theorem** (NA-02 import), on `U_D` only; NUMGEN's existential statement unchanged |
| INF-1 `NUMGEN-RESULT-N5AS1-INF1` (D_M = τ log M + C_D + o(1)) | `RECOG-THM-A1A-PHASE-EXISTENCE-U` (lim(D_N^U − τ log N) exists on all of `U_R`, explicit series, R9-free, INF-1-free); `RECOG-RESULT-A1A-CD-AGREEMENT` (C_D^ext = C_D on `U_R ∩ U_NG`) | no event (block defect) | same lift; D_N^U is RECOG's extension of NUMGEN-DEF-N5AS1-DEFECT to `U_R` | `U_NG` → `U_R`; agreement only on the overlap | block count from the start | existence plus series; tail of the series is type 2 | THM / RESULT | independent agreement; recorded, not consumed. NUMGEN's INF-1 stays existential; NUMGEN registers no explicit-tube INF-1 of its own |
| INF-2 (N_B(M) = M − (τ/2π) log M + O(1)) | RECOG (B), count law via (A) | canonical B predicate (below) | same | `U_NG` → `U_R` | primitive steps / blocks | O(1) | THM | independent agreement; recorded |
| GAP-LOCK Lemma 1 (alphabet {6,7}) | RECOG (B) alphabet; (C′) six-step deficit 0.927τQ < Δ < τQ+1.82Q^{3/2} on `U_D,T` | NUMGEN: transition token x→Tx with w(x)<0≤w(Tx), ρ>0 both sides (line 2114). RECOG: the same predicate with anchor = n+1. Gaps are the same; anchors differ by one step | same | `U_NG,T` → `U_R` starts, `U_D,T` estimates | primitive steps | deficit bound | THM | independent agreement; recorded |
| GAP-LOCK Lemma 2 (s(M) = (3τ/π) log M + O(1)) | RECOG (B) count law | as above | same | `U_NG` → `U_R` | 6M primitive steps | O(1) | THM | independent agreement; recorded |
| GAP-LOCK Lemma 3 (M_{k+1}^{phys}/M_k^{phys} → e^{π/(3τ)}) | RECOG (S): τψ(a+M_k) − (k−1)π/3 = L + ε_k, hence M_{k+1}/M_k → e^{π/(3τ)} | as above; M_k is the block index of the k-th 7-gap anchor (both: n = 6M_k + r_k, 0≤r_k≤5) | same | `U_NG` → `U_R` | blocks | **slip-schedule ε_k (type 3)**: a-priori, uses the block maximum Q and the series tails; not computable from (a,k,M_k) alone | THM | independent agreement for the ratio limit; **the digamma schedule is not adopted** (RECOG's result; NUMGEN states no schedule) |
| slip rate (1/k) log M_k^{phys} → π/(3τ) (lines 2269–2307) | RECOG (S) consequence | as above | same | `U_NG` → `U_R` | blocks | — | THM | independent agreement; recorded |
| `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` | none (RECOG consumes it, §7) | defect-threshold first crossings, not physical events | same | `U_NG` | blocks | — | — | unchanged; producer row only |

**Three error types**, kept separate in the live text:
1. Type 1 is the per-block reciprocal-amplitude increment, (15/2)√Q_m (RECOG).
2. Type 2 is the summed tail / backbone constant (NUMGEN's existential; RECOG's series tails S^tail, R^tail). NUMGEN has no explicit backbone constant, and none is entered.
3. Type 3 is the slip-schedule ε_k (RECOG, a priori).

None substitutes for another.

**Reasons for the custody form.**
- Each NUMGEN statement is proved in NUMGEN on its own tube and does not need RECOG.
- RECOG's explicit-U proofs consume NUMGEN definitions (`NUMGEN-DEF-N5AS1-DEFECT`, `-PRIMITIVE-LIFT`), the token wording and GAP-LOCK's slip-law form.
- Importing those theorems back would create no circular proof: RECOG-THM-A1A-PHASE-EXISTENCE-U uses neither INF-1 nor R9. It would, however, make NUMGEN a consumer of results built on its own definitions without adding any NUMGEN conclusion.
- Recording them keeps the producer → consumer direction single and leaves custody as RECOG states it ("GAP-LOCK Lemmas 1–3 and INF-1 remain NUMGEN's … no custody changes").
- A later edition may import by RID if a NUMGEN conclusion needs an explicit-U input. None does in v1.21.

**Live-text change (stage 1):**
- §9.1 gains one row per RECOG theorem: RID, `recog-v0.3.24`, scope `U_R`, state "statement accepted as independent agreement; not imported".
- Each affected §6.6 statement gets one sentence: "explicit-domain counterpart: … (RECOG v0.3.24, consumer theorem on `U_D`); not imported; this statement keeps its existential tube".
- The SG-NG-23 cross-citation (NC-12) is added.

## 3. NA-03 / I08 — domain alias table

| Label | Set | Owner / source | Used for |
|---|---|---|---|
| `U_NG` | existential punctured sector of the N-1 closure (radius chosen by continuity, not stated) | NUMGEN §6.2 (line 1045 ff.) | all NUMGEN theorems proved "after shrinking" |
| `U_NG,T` | ⋃_{j<6} T^j(U_NG) | NUMGEN §6.2 (line 1055) | one-chart tube of N-1/N-3A, L-MONO, B predicate |
| `U_D` | {0 < Q_true ≤ 1/625} | DYAD-THM-PRIM-CTR (`dyad-v6.4.22` §6.14) | the explicit base; row-A base points; NUMGEN seed admission |
| `U_D,T` | ⋃_{j<6} T^j(U_D) ⊂ {\|W\| < 47/1000} | DYAD-THM-PRIM-CTR | explicit tube; row-A branch (B) |
| `U_R` | the set `U_D` used as RECOG's start domain | RECOG §6.13b | A1a/A1b records |
| `U` (L1 coordinate) | U = √3ρ/2, V = η − ρ/2 | NUMGEN L1 coordinates | not a domain; a guard sentence says so |

**Rule.** Every theorem scope that says "U" or "U_T" without a section gets the label at the point of use. Old proofs keep their original domain; no statement is moved between domains. Inclusions are stated only where proved: the seed admission is `[ALG]`, and the box containment is in §6.2. No inclusion `U_D ⊆ U_NG`, or the converse, is asserted.

## 4. NB-07 / NB-08 / I05 / I13 — RIDs

**Tier 1 (v1.21, consumer-cited first).** The names are proposals until stage 1. Each is checked for collisions against all 41 `NUMGEN-*` strings in v1.20.8 and against the repository.

| Statement | Proposed RID | Grade (unchanged) |
|---|---|---|
| GAP-LOCK Lemma 1 (alphabet {6,7}) | `NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET` | `[RESULT] [from: ALG]` |
| GAP-LOCK Lemma 2 (physical 7-gap count law) | `NUMGEN-RESULT-N5AS1-GAPLOCK-COUNT` | `[RESULT] [from: ALG]` |
| GAP-LOCK Lemma 3 (event-time slip locking, ratio limit) | `NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO` | `[RESULT] [from: ALG]` |
| INF-2 / crossing count | `NUMGEN-RESULT-N5AS1-INF2` | `[RESULT] [from: ALG]` |
| First-nonlinear cyclic-average theorem (§6.4, line 1490) | `NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE` | `[RESULT] [from: ALG]` |

**Tier 2 (v1.21 if the statement location is stable after stage 1; otherwise the next edition):**
- C7C-M2;
- M-1A / M2-1;
- C7C-0;
- DISC-1 and DISC-2 (outcomes);
- the ten-label existential lower bound;
- the N-1C closure. It is currently headed by both `NUMGEN-OPEN-N1C` and `NUMGEN-N1C-DYAD-RADIAL`. Stage 1 states which RID is the closure result and which is the module.

L1 already has `NUMGEN-RESULT-L1-PRIMITIVE-CONTRACTION`, so no new RID is needed.

**NB-08.** No RID is renamed or recycled (Methodology v1.4 §4.2: category text is an immutable identifier, not a status).
- A CLOSED result under a module `OPEN` RID keeps the module RID as its lifecycle record. When the result RID exists, the module record points to it.
- `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` keeps its name; its grade is the tagged `[RESULT] [from: ALG]`, and one guard sentence says so.
- No mass retagging.

## 5. Row-by-row disposition (reconciliation §3)

| Key | Prio | Disposition | Owner decision / change |
|---|---|---|---|
| NA-01 / I01, I03 | P0 | **accept with change** | §2 matrix; consumer-side confirmation, no import by RID from RECOG; three error types typed; custody unchanged |
| NA-02 / I04 | P1 | **accept with change** | **execute the import** (§1). States: received (N15, v1.20.8); statement accepted (this record); adopted use from the v1.21 Import Ledger row (pin `dyad-v6.4.22` §6.14, producer v6.4.19). Interface row: W↔𝓛, q_m↔Q_m (primitive), lift = PRIMITIVE-LIFT, lag sign, base points in `U_D`, intermediate steps in `U_D,T`. The statement is present unchanged at the governing tag (read). No bulk repin of v6.4.18 imports |
| NC-14 / I02 | P1 | **accept** | A1a/A1c entered as available comparisons. φ* ≟ C_D^ext stays OPEN under `NUMGEN-OPEN-NG0R-COV`, with the conventions listed (chart, lift, readout, clock, start state, overlap `U_R ∩ U_NG`). No identification; A1c does not recover a and does not lower R_ind |
| NB-07, NB-08 / I05, I13 | P1 | **accept with change** | §4 (tier 1 in v1.21; tier 2 conditional; no renames) |
| NC-16 / I05 | P1 | **accept** | §9.2 consumer row (line 2824) → RECOG v0.3.24. It names both facts: the §7 HEUR cross-reference tag, and the ALG use in `RECOG-RESULT-BTOKEN-LOG-EQUIVALENCE` and the A1b route. No grade is asserted; the tension is RECOG's (outbound item filed) |
| — / I06 | P0 | **accept** | Hold C7C-M4; continue abstract WD-DOM; §2 records the TDR-G dependency (`pipes/TDRG/20261026-NUMGEN-orientation-policy-s0-e-half-n.md`); a sensitivity audit of affected witnesses comes before any status change. Outbound item clarified (§6) |
| NA-03 / I08 | P1 | **accept with change** | §3 alias table and point-of-use labels; no global rename |
| NA-04, NC-19 / I09 | P1 | **accept with change** | §9 Imports / Exports / Consumers / Pins matrix with the current companion and the proof pin in separate columns, and states offered/received/accepted/adopted-use. Stale labels are replaced in place (see the pin decisions below). Programme IF rows are untouched by NUMGEN |
| NA-06, NB-10 / I10 | P1/P2 | **accept** | Two stages (PI Q1: v1.21). Grades untouched; v1.20.7 normalization kept. The superseded LOGSLIP block keeps its RID `NUMGEN-CAND-N5AS1-LOGSLIP` and moves to Appendix B as a retired formulation in stage 2 (movement map); nothing deleted |
| NC-13 / I12 | P2 | **accept with change** | Cite `DYAD-ALG-Q-INVARIANT-FORM`, `-TAU-DETB` and `-CUBIC-PARABOLIC` at the §9.2 relay rows. Cite `DYAD-THM-PRIM-CTR` as the explicit form of L1. The ΔQ₅ ≡ P₅ alias is added only if an exact symbolic check in stage 1 passes (script + log in `evidence/numgen/`); otherwise it is deferred. No proof campaign |
| — / I11 | P2 | **accept** | §6.8/§7 hand-off wording: NG-7A closed ≠ NG-7B; "holonomy rank" is not a non-Abelian or curvature claim; OFN IF24 acceptance is OFN's |
| — / I07 | guard | **accept** | stage-1 check item; edit only if a conflating sentence is found |
| NA-05 | P2 | **accept** | scope words at the N-1A0 / N-1A1 headers ("closed on `U_NG` by L1; abstract question open") |
| NB-09 | P2 | **accept** | declare the evidence state at in-ledger-proof claims with §12.2 keys ("written proof in ledger; no separate certificate"); no regrading |
| NB-11 | P2 | **accept with change** | Changelog-only facts. The sampled L-PHASE range sup\|r\|/Q^{3/2} ∈ [1.3449, 1.3565] becomes live at L-PHASE as `[NUM]` with its evidence pointer, because DYAD v6.4.19 cites it. The other changelog-only facts relocate with the changelog to the tag |
| NC-12 | P2 | **accept** | one sentence at SG-NG-23 naming RECOG (S) and the scope difference (representation diagnostic / RECOG clock export / A1b THM on `U_R`) |
| NC-15 | P2 | **accept** | RID `NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE` in tier 1; Genesis's use is GEN's decision (outbound offer clarified, §6) |
| NC-17 | P2 | **accept with change** | Cross-citation only after Dyadic answers. NUMGEN's q* is a `[RESULT] [from: NUM]` root *candidate* of η₆(q) − q = 0 (same wrapped phase after one block), which is not obviously the same defining condition as Dyadic's first-footprint branch split. The outbound question is clarified (§6). No edit in v1.21 unless answered before the stage-1 freeze |
| NC-18 | opt. | **accept with change** | The q_m ≡ Q_m guard already exists as a DEF since v1.20.8; one pointer is added at §6.2. The tube bound 0.0665 is kept as stated (valid); the atlas-checked sharper value is not entered as a NUMGEN number |

**Pin decisions for NA-04 (stage 1):**
- §7 item 7 "Dyadic v6.4.10 `DYAD-THM-Q403-PHASELAW`" moves to the pin the live Q403 imports already use (v6.4.18). STOP-03 (v1.20.7) had moved it from v6.4.9 to v6.4.10, and v1.20.8 then moved the other Q403 uses to v6.4.18 and missed this one.
- "DZT v0.17": no document of that number is in the repository. The governing DZT is `dzt-v0.8` (`RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md`). NUMGEN imports nothing from DZT. The `[PROVENANCE]` row is restated as an audit-memo citation with no version claim.
- Programme v1.2 → v1.3 (SG-PROG-4 is unchanged in meaning).
- The Genesis companion is v2.9.
- "Validation state carried into v1.19" and the header pointer-validation narrative go to the release record.

## 6. Outbound items filed on NUMGEN's behalf — check

None misstates the finding. Three omit a qualifier that a receiver needs, so I add one dated sender line to each body; `state` is not touched:
- **TDRG (orientation policy):** "216 events" are the antipodal events *inside the audited eventual cycles*. The label projection is robust: every admitted label keeps at least one unexposed witness, and the ten-label existential lower bound is unchanged (NUMGEN §6.6 lines 1589, 1945–1952).
- **GEN (cyclic average):** NUMGEN states the theorem for f = R + h_d and applies it to the primitive dyad, [T⁶−id]₂ = 0 (line 1490 ff.). The diag(A,A,A) case is an application of the general statement, not a sentence of v1.20.8. The RID is planned in v1.21.
- **DYAD (q\*):** NUMGEN's q* is a `[NUM]` root candidate of η₆(q) − q = 0, which is not stated as a branch split.

The RECOG item (GAP-LOCK 3 grade) is accurate; no change.

## 7. Inbox `pipes/NUMGEN/`

`20261026-RECOG-a1b-slip-schedule-informed.md` → `state: acknowledged`. The verdict (*accept with change*: confirmations recorded, nothing imported) is written into `disposition` once the matrix is in the stage-1 text, before the stage-1 freeze. The other co-owner may differ.

## 8. Not done here

- No DSN edit; stage 1 waits for the reconciliation of the two co-owner records.
- No certificate rerun.
- No change to C7C algebra results or Census-1.
- No ALG → THM promotion.
- No φ* ≡ C_D^ext.
- No new Dyadic or RECOG RID.

The held v1.20.x records are uploaded unchanged on `upload/numgen-records` (PR #69) for the atlas hash check.

## 9. Comparison with the other co-owner record (added 26 Oct 2026)

The other co-owner record is `records/numgen/NUMGEN_OWNER_DISPOSITION_ADVISORY_v1_20_8_chatgpt_20261026.md` (PR #72, commit `2a293f55`), read in full.

**Agreement.** The two records agree on every substantive decision:
- NA-01: consumer-side confirmation, no blanket import, acceptance matrix, the three error types;
- NA-02: execute the row-A import as a separate, strictly typed block; NUMGEN's existential L-PHASE is unchanged;
- I02: φ* vs C_D^ext stays OPEN;
- I06: C7C-M4 HOLD;
- I07, I11, NA-04/NC-19, NA-05, NB-09, NC-12, NC-13 (gated on a producer check), NC-16, NC-18 (no tightened bound);
- the two-stage v1.4 migration;
- the inbox verdict *accept with change*.

**Differences.** Each is of form, not substance:

| Row | Claude | ChatGPT | Proposed resolution |
|---|---|---|---|
| NC-17 | accept with change (no edit unless Dyadic answers before the stage-1 freeze) | defer | Same outcome. Record it as **defer**, using the ChatGPT label. |
| NA-03 labels | `U_NG`, `U_NG,T`, `U_D`, `U_D,T`, `U_R` | `U_NG`, `U_D,base`, `U_D,tube`, `U_R,base` | Adopt the ChatGPT labels, which match the reconciliation wording, and add `U_NG,tube` for NUMGEN's six-phase tube. |
| NB-07 | named tier-1 RIDs (GAP-LOCK 1–3, INF-2, cyclic average), tier 2 conditional | the same priority list; no names registered by a disposition record | Compatible. The names in §4 stay proposals until the stage-1 collision check, as §4 already says. |
| Matrix columns | domain / clock / error type / grade / state | adds an explicit `relationship` column next to `receiving status` | Use the ChatGPT column set. The §2 content fills it unchanged: relationship ∈ {independent agreement, consumed theorem, not adopted}. |
| Inbox `state` | set to `acknowledged` (PR #70) | not changed | No conflict. `acknowledged` is a queue state only; the verdict is written when the matrix is in the stage-1 text. |

Neither record changes a grade, imports from RECOG, or identifies φ* with C_D^ext.
