# Atlas Closeout — Dyadic DSN v6.4.20 → errata/maintenance successor v6.4.21

**To:** the Dyadic stream owner and the PI.
**From:** the atlas owner (Claude). This note consolidates two independent completion checks of the same adopted file.
- **[C]** `records/dyad/ATLAS_VERIFICATION_DYAD_v6_4_20.md`: atlas owner, residuals R1–R8.
- **[G]** `RTG_DYADIC_v6_4_20_ATLAS_COMPLETION_REVIEW_v0_1.md`: peer reviewer, findings AR20-01 to AR20-09. It comes with `DYAD_v6_4_20_ATLAS_ROW_CHECK.csv` (a 34-row assessment) and `DYAD_v6_4_20_EXTERNAL_VERIFICATION_RECEIPT.md`.

**Date:** 22 October 2026.
**Revision:** working record at a fixed path; earlier rounds (v1.0–v1.2) are in git history. This round applies editor finding M14R-05 (`records/methodology/DSN_METHODOLOGY_v1_4_EDITOR_REVIEW.md`): contrary instructions are replaced at their own locations. Governing methodology: DSN Methodology v1.4 (tag `methodology-v1.4`).
**Status:** noncanonical closeout proposal. It is not an amendment, adoption, regrade or notice. The owner decides every item.

**Target:** `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` at tag `dyad-v6.4.20`, 2,793 lines, 411,765 bytes, SHA-256 `0b2d5a44eb818598bb330464dfa4f2e9d75521715f577a7c2e589e165f1a4852`.

**Contract being closed:** `records/dyad/ATLAS_ADVISORY_DYAD_v6_4_19.md`, 34 rows.

---

## 0. Decision requested

1. **Keep v6.4.20 as adopted.** Every scientific result stays at its current scope. Nothing is reopened, and no full NF, interval-arithmetic or smooth-embedding campaign is repeated.
2. **Issue one batched errata/maintenance successor, v6.4.21.** It implements §2 below and the size-discipline pilot (§7) in the same release, carries its own hash and tag, and sends a notice delta. v6.4.20 stays retrievable at its tag.
3. **Close the advisory administratively** with the records in §3: an owner completion matrix, an evidence supplement, notices and installation read-back.
4. **Leave Tier C research open with named targets** (§4). It does not block maintenance acceptance.

**Final review of the successor is change-focused.** It checks only that S-1 to S-6 are implemented, E-1 and E-2 are met, the compaction check passes (§7), the dependency and notice records are made, and the new edition identity is correct. Earlier verifications of unchanged scientific content are not re-run. If a mathematical statement is actually changed, only the check that change needs is added.

**What is already settled:**
- **External hash verification of v6.4.20.** [G] verified it independently: 12/12 package hashes, deterministic r2→final rebuild, checker R0–R11 12/12, and 11/11 negative controls rejected. [C] independently recomputed the hash and the 12/12 sums.
- **The release's pending prerequisite for N16–N20 is therefore met** for this edition.
- **Installation.** The project now lists `RTG_DYADIC_OSCILLATOR_DSN_v6_4_20.md`. The owner still records a read-back hash comparison.

## 1. Reconciliation of the two checks

The two checks agree on every location they share. **In the reviewed scope, no new finding requires withdrawing adopted results or reopening their evidence; scope, dependency and provenance corrections remain.** This does not reduce record defects that matter mathematically (for example the missing DG(0)=I condition) to typographical errors.

| Topic | [C] | [G] | Final reading |
|---|---|---|---|
| Overall | 28/34 implemented; 7 residuals + 1 structural | 19 of 30 A/B implemented; 8 partial; 1 unverified records; 2 routing | **[G]'s stricter per-row statuses are adopted** (§5) |
| §1 L128 OPEN 3 still PARTIAL | R1 | AR20-01 | same item |
| OPEN 9 Active list holds CLOSED Q403/b=5 | R2 | AR20-01 | same |
| DG(0)=I and existence pointers | R3 | AR20-01 / FA-03 | merged |
| §1 L112 | R4: "h₄ exact over ℚ(√3)" field label | AR20-01: "pending RECOG R11" wording | **same line, two defects; fix both** |
| UV citation at §6.11 L704 | R5 | not flagged (FB-20 IMPLEMENTED) | kept as a minor item |
| Notation table | R6: 3 overloads missing | AR20-04: same omissions **plus a false row (J_Q "not used here")** | merged; [G] adds the error |
| FC-34 | R7: accepted, not done | no disposition | **prior ACCEPT (reference note only) exists in the disposition; the implementation or a reasoned deferral record is missing** |
| Size | R8: Appendix A grew by about 92k of draft records | AR20-07: §1 is 1,438 words with no exception; "unchanged" claim needs a baseline | merged (§2 E-items) |
| N11 RECOG use | [C] marked FB-18 ✅ | **AR20-02: A1a now uses T1/T2, so not reference-only** | **[G] is right; [C] and the FINAL advisory are corrected** |
| §7 self-contained list too broad | not found | **AR20-03** | adopted |
| RAW-CUBIC historical identity | [C] ✅ with the note "match open" | **AR20-05: caveat needed at point of use; p-range** | adopted |
| OPEN 9 definitions partial | [C] ✅ | **AR20-06: caveat at the live entries** | adopted |
| Completion evidence | not raised | **AR20-08** | adopted, with the owner disposition record noted (§3) |
| Notices | planned | AR20-09 | merged |

All line numbers in [G] were re-located by the atlas owner in the target file. L864 in [G] is L863 here; the content is the same.

## 2. Errata/maintenance successor — content (DSN text)

### 2.1 Must fix (current-state correctness)

**S-1 | Current status at every point of use** [AR20-01, R1–R3; rows FA-02, FA-03]

| Location | Present wording | Replace with |
|---|---|---|
| §1 L128 | "OPEN 3 is PARTIAL: asymptotic-phase transfer (P4) OPEN." | OPEN 3 CLOSED within its defined scope (v6.4.16); P4 = `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE` (conditional on R9); primitive remainder = OPEN 21 (CLOSED, v6.4.17) |
| §1 L112 | "…not transferred to the conjugacy chart pending RECOG R11" | permanent non-transfer guard (SG-19); chart value +89√3/324 (RECOG-ALG-CHART-LAWS); R11 CLOSED |
| §2 L181 | "Primitive-variable remainder beyond formal second order not certified." | pointer to `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` (R9 premise; rows unchanged) |
| §2 OPEN 9 "Active sub-items" | CLOSED Q403 and CLOSED b=5 listed as active | move both to Closed sub-items; drop the struck "Next required artifacts" line |
| §2 closed list, OPEN 19 line | "formal centralizer of T⁶ is {exp(sX)}" | add "tangent to the identity, DG(0)=I" |
| §1 L126 | F1–F3 "No existence is asserted." | add "existence: DYAD-THM-SMOOTH-EMBEDDING (§6.17)" |
| §5 spiral-residual row | P4 transfer among the forbidden conclusions | "not implied by the per-block result alone; see DYAD-THM-OPEN3-ASYMPTOTIC-PHASE" |
| §6.14 L863 and L874 (and following "recorded distinctions") | "remains an open provenance item", "remainder not certified", "only the chart-variable law is certified" | replace in place with the current status: coefficient verification complete (v6.4.16 record: the reproduced h, J coefficients equal the P2B v2 certificate coefficients in exact arithmetic); primitive remainder → OPEN 21. The superseded wording stays in v6.4.20 (tag `dyad-v6.4.20`); Appendix A records the change once |
| §8 L1262 (DYAD-ART-ATLAS-P2) | "r2 OWNER-RUN" | the recorded r2 reviewer replays, attributed as recorded |

*Scope of the provenance pointer.* The v6.4.16 discharge is an **exact coefficient equality**, not a byte identity of files; §6.14 itself says neither file is a byte copy of the other. The pointer must say "coefficient verification complete" and must not imply that any byte-identity check was done. The earlier review's provenance-closure suggestion is read with the same limit.

*Acceptance:* a search for OPEN 3, R11, OPEN 21, P4 and P2 provenance in live content (by profile, Methodology v1.4 §1.1: §§0–9 and the live technical appendices) finds no status that contradicts the current one. An explicit historical quotation in Appendix B is not a contradictory current status.

**S-2 | N11 adopted use** [AR20-02; row FB-18]
- The live N11→RECOG row records the current adopted use and its evidence: "v0.3.22: ADOPTED USE — `RECOG-THM-A1A-CD-IDENTIFICATION` depends on T1/T2 (`DYAD-THM-OPEN3-ASYMPTOTIC-PHASE`), at RECOG's pin".
- The earlier event ("v0.3.21: RECEIVED — reference import (SG-R14)") is preserved in the notice history of v6.4.20 (tag) and in the v6.4.21 release record, with a pointer from the live row. It is not erased, and no receipt is invented.
- Do not repin. Ask RECOG to reconcile its own §7.2 mirror.
- This also corrects the advisory row FB-18 and the atlas.

**S-3 | Subclaim dependencies in §7** [AR20-03; row FA-01]

In the "Dependency structure" paragraph:
- Name the self-contained part of `DYAD-ALG-OPEN3-PHASE-OFFSET`: the static-offset identity and Δ₁, Δ₂.
- Separate from it the primitive-memory expansion, which uses the R9 memory law, c_iso and Λ₁.
- Write "native OPEN 9 derivations, excluding the named RECOG imports".
- No RID is split or renamed.

**S-4 | Notation table** [AR20-04, R6; row FB-23]
- Correct the J_Q row: J_Q = 𝓛⁻¹i𝓛 is defined and used in §6.12 (L764–766).
- Add rows for:
  - U_ISP = (√3/2)ρ (§6.4) versus the start/base-point set U = {0<Q≤1/625} (§6.14; its invariant six-phase tube is U_T) versus the projection-window U of OPEN 16;
  - formal ĥ, finite h₆ and OPEN-M h_src (SG-15);
  - the majorant M(s) versus the memory M/M_W, the matrix M, the amplitude M_p and the count M(D);
  - the NF-INV κ = M′(R) versus κ_bb;
  - polar r versus the remainder r_m.

**S-5 | Provenance caveats at the point of use** [AR20-05, AR20-06; rows FA-08, FB-11, FB-09]
- At `DYAD-THM-RAW-CUBIC` (§2) and in its Appendix F row, replace "statement recovered" with "formula recovered and algebraically verified; identity with the historical proposition not yet established (Appendix E)".
- State the admissible p-range of the displayed formula.
- At the §6.11 projector inventory and at the eigenframe linear-part lemma, point to Appendix D: eight objects and the lemma statement are not recovered.
- Each unrecovered item gets a named source and a next step.
- Recover only from owner sources, never from the atlas.

**S-6 | Small fixes** [R4, R5; rows FA-05, FB-20]
- §1 L112: "h₄ exact over ℚ(√3)". If the archival h₄ coefficients are complex, write ℚ(i√3), or "components in ℚ(√3)". The owner checks this against `normalize_p6_liegauge_exact.py`.
- §6.11 L704 (P6-FACEFLUX block): add the same pointer used at §1 L140 and §6.12 L773, namely `GEN-OPEN-UVJET-SCOPE`, OPEN-M R16 `UVM-RESULT-AUDIT1` and the five inherited conditions, beside "OPEN-GEN-II-7B".

### 2.2 Size and orientation (E-1 is required; E-2 is should-fix)

**E-1 | §1 and the "unchanged" claim** [AR20-07; row FB-22] — **required record obligation**
- §1 is 1,438 words. Methodology v1.4 §1 targets 200–400 words; above 500, either relocate the content or declare a profile exception in the header with a one-line reason. One of the two is required in v6.4.21; a generic "deferred" note does not meet it.
- v6.4.21 has one current footer. The v6.4.20 r2→final comparison and the P1 retagging explanation ("r2→final changes publication metadata only; registered RID grades are retained; the P1 corrections to unnumbered statements — §6.5 backbone [ALG]→[DEF]; §6.6 [THM]→[ALG]/[DEF] — are recorded separately"; tag-map preservation is semantic) belong in the v6.4.21 release record as a correction of the v6.4.20 record, not in inherited footer prose. The v6.4.20 release record itself is not edited.

**E-2 | Appendix A size** [R8; row FB-22] — executed pilot deliverable
- The v6.4.20 draft-round records add about 92k characters: r1 44k, r2 13k, P1 13k, adoption 22k.
- Leave the long draft comparisons, review correspondence and the 55 verbatim-quoted release lines (old→new map) in v6.4.20, where they stay complete at its tag; the v6.4.21 release record cites them there and does not copy them (Methodology v1.4 §13.7, no redundant copies).
- **Appendix A keeps, per edition:** a compact change summary; the affected RIDs; every scope and grade correction; the release-record locator and predecessor tag (Methodology v1.4 §1). Appendix B keeps the required scientific correction records and the currently operative negative constraints.
- If E-1 or E-2 is not executed, the pilot is reported incomplete; it is not closed by a stated reason.

## 3. Closeout records (outside the DSN text)

**C-1 | Owner completion matrix** [AR20-08]
- `ATLAS_DISPOSITION_DYAD_v6_4_19_SESSION_v0_1.md` already gives the owner's **pre-implementation** decisions: ACCEPT 30, REVISE 1, INVESTIGATE 1, DEFER 2.
- The missing piece is the **completion** column: for each of the 34 rows, the actual v6.4.20 or successor edit (section/RID), the rejection rationale, or a deferral with its missing premise and next test.
- [G]'s CSV is a reviewer assessment and does not replace this matrix.
- FC-34: the prior ACCEPT stands; record its implementation or a reasoned, dated deferral.

**C-2 | Evidence supplement** [AR20-08; row FB-17]
- Provide a small hash-pinned package with:
  - the v6.4.17/.18 release-record addenda (`DYAD_v6_4_17_v6_4_18_RELEASE_RECORD_ADDENDA_v0_1_1.md`);
  - the two OPEN 9 recovery sources;
  - `OPEN9_full_onestep_normalization_table_v2.md`;
  - the P1 and P2 session records.
- Several of these were in the project before the cleanup. Their absence from the release ZIP means "not independently inspected here", not "never done".

**C-3 | Notices** [AR20-09; rows FB-19, FB-21, FB-13, FB-25]
- Prepare N16–N20 now, citing `0b2d5a44…4852`. Add the N11 correction to N19 (RECOG).
- The successor gets its own notice delta.
- Route all notices through the PI.
- Keep separate fields for sent, received, statement accepted and adopted use.
- Notices not yet accepted or adopted by other streams do not block adoption of v6.4.21; they stay listed as pending (§5).

| Notice | Recipients | Content |
|---|---|---|
| N16 | Genesis; OFN | `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` (C2 hypothesis met at C^∞); c_θ chart value +89√3/324; ℚ(ζ₅) field label for ν₅^(5) |
| N17 | DZT; AZ | Appendix F crosswalk; Q₁₂ sign; VANISH-B2 explanation; RAW-CUBIC status with its caveat (S-5) |
| N18 | NUMGEN | §7.0a export table; φ* status; FC-33 lag-sign corollary (base points only); FC-32 for information |
| N19 | RECOG; RRF | R9 claim-level import row; S_h = j⁶R₀ routing; **N11 adopted-use correction (S-2)**; FC-32 offered; frame rule |
| N20 | Triadic; plus RER/ER-2B through the PI | **new v6.4.20 content only:** `DYAD-ALG-KP-FRAME-SCALE` frame qualifier (κ_shear unchanged) and `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` (no triad transfer). RER v0.2 already records `DYAD-THM-SMOOTH-EMBEDDING` from v6.4.18 (C^∞ existence, generator uniqueness under DX(0)=0, qualitative radius bound; analyticity and triad transfer kept separate); N20 does not ask RER to close smooth existence. That earlier acceptance does not extend to the new v6.4.20 results |

**C-4 | Installation read-back.** Read back the project copy of v6.4.20 (now synchronized from `rtg-corpus`) and compare it with `0b2d5a44…4852`. Record this separately from the external byte verification. Repeat for v6.4.21 after its installation.

## 4. Research items (may stay open; not maintenance blockers)

| Row | Status | Next step |
|---|---|---|
| FC-31 large-p cascade | named target | [G] supplied an independent SESSION expansion (`OPTIONAL_SESSION_COROLLARIES.md`). The owner reviews it before any adoption; coordinate with DZT. |
| FC-32 R9-free existence on U | SESSION only | RECOG decides on the H-NG discharge. DYAD may register only the row-A corollary Σ\|r_m\| < ∞. OPEN 21 keeps R9. |
| FC-33 lag sign | planned for N18 | Scoped corollary at base points; NUMGEN checks anchor indexing and seven-step coverage. |
| FC-34 16/3 bookkeeping | prior ACCEPT (reference note only); implementation or reasoned deferral record missing | Add the one-line §6.12 cross-reference, or record a dated deferral with its reason. It selects no birth policy. |

**Protected boundaries (unchanged).** Nothing here requires closing B-an or B-6, all b ≥ 6, a physical UV deficit, DZT's all-p anomaly law, physical pole exchange or class-C selection, or quantitative smooth radii. The finite-chart, base-point/tube, raw/normalized and statement/certificate distinctions stay in force.

## 5. Final per-row status of the 34-row contract (v6.4.20)

**Implemented (19):** FA-04, FA-05*, FA-06, FA-07, FB-09, FB-10, FB-12, FB-13, FB-14, FB-15, FB-16, FB-20*, FB-24, FB-25, FB-26, FB-27, FB-28, FB-29, FB-30.
(* FA-05 and FB-20: **main scope implemented; the named residual in S-6 is open.** They are not counted as unconditionally complete.)

The 19 + 8 + 3 + 4 split is a working summary, not a closure type.

**Partial, closed by the successor (§2):**

| Row | Closed by |
|---|---|
| FA-01 | S-3 |
| FA-02 | S-1 |
| FA-03 | S-1 |
| FA-08 | S-5 |
| FB-11 | S-5 |
| FB-18 | S-2 |
| FB-22 | E-1, E-2 |
| FB-23 | S-4 |

**Records or routing (§3):**

| Row | Closed by |
|---|---|
| FB-17 | C-2 |
| FB-19 | C-3 |
| FB-21 | C-3 |

**Research (§4):** FC-31, FC-32, FC-33, FC-34 (FC-34: prior ACCEPT; implementation or reasoned deferral record missing). FC-32's SESSION result is not adopted silently during maintenance; OPEN 21 keeps its R9 dependency.

**Completion criterion for the advisory:**
- v6.4.21 is adopted, with S-1 to S-6 implemented and E-1 and E-2 executed;
- the compaction check (§7) passes on the stage-2 delta, and the stage-1 scientific and scope changes have had their targeted review;
- C-1 to C-4 are on record, with FC-34 implemented or deferred with a dated reason;
- the atlas is refreshed from the adopted successor.

Notices sent but not yet accepted by other streams are recorded as pending; they do not block adoption of v6.4.21.

**Two closures are kept separate (Methodology v1.4 §13.5):** acceptance of the Dyadic maintenance release ≠ completed synchronization of every consumer. Dyadic can complete its own corrections, evidence package and notices while other streams' adoption decisions are still pending. Pending consumer decisions do not reopen the Dyadic successor, and the corpus is not described as fully synchronized until they are recorded.

## 6. Atlas self-corrections recorded with this closeout

- FB-18 / N11: the advisory's "reference-only" reading is stale. A1a uses T1/T2.
- p=7: Re μ₇^Z = −1.31779. The FINAL advisory printed 1.316.
- Carried from the FINAL advisory §5: RRF v0.8.4 already records smooth existence; S_h = j⁶R₀ was already in Dyadic; CAND-prefixed RIDs stay immutable.
- Atlas source table: RER is listed as "v0.2 DRAFT r4.6 (2026-10-19)". It will read **v0.2 ADOPTED 21 Oct 2026, NONCANONICAL**, keeping the exception for the two blocked ER-2B records (T6D, CARRIER). H1's RER.E2 item is re-checked against v0.2, which already records smooth existence.
- The atlas DYAD slice will be regenerated from the adopted successor, keeping any open residual as an L5 line.

## 7. Pilot implementation (Methodology v1.4)

v6.4.21 is the single target release. It combines the closeout errata with a mechanically checked compaction. There is no separate compaction release and no full scientific re-audit. Methodology v1.4 is adopted (tag `methodology-v1.4`), so the pilot cites it directly.

**Two build stages, one target:** `adopted v6.4.20 → corrected intermediate → compacted v6.4.21 candidate`.
1. **Stage 1 — corrections.** S-1 to S-6, the accepted FC-34 action, and the E-1 footer/record wording. The intermediate's hash is recorded. Its delta gets the targeted review its content needs; unchanged mathematics and its certificates are not reopened. An intermediate file is not an adopted version.
2. **Stage 2 — compaction.** Layout, deduplication, navigation and history relocation only, under Methodology v1.4 §§1, 1.1 and 13.6: current-only header (*Supersedes* = v6.4.20 and its hash); one footer; §1 compacted or an exception declared (E-1); Appendix A compacted, with the draft-round records left in v6.4.20 at its tag (E-2); superseded prose and stacked overlays removed from live sections. A movement map records every changed block. New substantive claims, including Tier C results, cannot enter here.

**Checks.** `tools/check_compaction.py` checks the stage-2 delta against the intermediate, not against v6.4.20, so stale statuses corrected in stage 1 are not required to survive. It preserves qualified claim blocks (statement, status, assumptions, scope, RID association, OPEN obligations, evidence links), accounts for every removed passage, and reports its parser limits. Its negative controls must reject silent assumption deletion, scope widening, wrong RID association and broken source links. `tools/dsn_lint.py` gives the informational size report. Both reports go in the release record. A passing check does not authorize publication.

**Release.** Owner/PI adoption is recorded in `records/dyad/RTG_DYADIC_v6_4_21_RELEASE_RECORD.md`, then merge and the tag `dyad-v6.4.21`. Earlier release records are not edited.

*End of closeout proposal. No DSN was edited; no notice was sent.*
