# Programme Overview v1.4 — ChatGPT change-focused receiving review

**Date:** 4 November 2026  
**Verdict:** **CONDITIONAL PASS — one bounded source-typing correction (R1) required before PI adoption.** No new scientific computation or multi-round review is required.  
**Status:** [SESSION] receiving-review record only; not a Programme owner disposition, scientific adoption, release approval or amendment to the candidate.  
**Target:** PR #178, `claude/programme-v1.4`, candidate at head `7bf31aa8305e23f7c3c973fdb33f9c84ac7a5212`.  
**Candidate SHA-256:** `d109c78b9924b325e590159796b01223b82959211809106eea3dce009f6673bd` (73,376 UTF-8 bytes).  
**Base:** adopted `programme-v1.3`, SHA-256 `1b8358b3e1d3abb853e226786d21e6559c289b7c85570dac0ff1ebc2dabaea06` (68,875 bytes).  
**Review specification:** `records/programme/RTG_PROGRAMME_OVERVIEW_v1_4_RELEASE_RECORD.md` §4, PR #178.

## 1. Reading, evidence and independent validation

**Source identity and reading extent.** Read the complete candidate and adopted v1.3 texts for structure, change locations, and exact transformations; reviewed every one of the 71 edit-log replacements, with targeted scientific/administrative comparison of candidate §§5–9 and all review §4 topics. Read `CONVENTIONS.md` (full), Methodology v1.4 §3.3 and governance rules (targeted), source Import Ledgers at their adopted tags: `dyad-v6.4.23` §7, `triad-v1.7` §§7.1–7.4, `gen-v2.10` §7, `numgen-v1.21` §9.1, `recog-v0.3.27` §7, `ofn-v0.12` §§11.2–11.5, `tdrg-v2.12.14` §§1–2/7/Appendix C, `uvm-v0.7.1` §7, RRF v0.8.4 source-receipt and class-C passages, and GEN v2.10 §6.8. This was a change/dependency review, not a new full reading of every untouched science section.

**EV-INDEP — identities.** Independently computed SHA-256 from UTF-8 GitHub contents using a local JavaScript implementation with a successful `abc` SHA-256 known-answer self-test. v1.3: 68,875 bytes and hash `1b8358b3…aea06` MATCH; v1.4: 73,376 bytes and hash `d109c78b…73bd` MATCH.

**EV-INDEP — exact replay.** Independently applied all **71 logged old/new operations** in order to the tagged v1.3 text. Each old payload occurred exactly once at its application; the entire rebuilt v1.4 text equalled the PR candidate exactly. This proves edit-log fidelity, not source-semantic equivalence.

**EV-INDEP — status invariants.** All five Programme OPEN RIDs remain identical and ACTIVE; the four SG-PROG-1–4 guard lines match their v1.3 texts exactly. Appendix B's body matches v1.3 exactly; the changed document footer after the appendix is not an appendix-body change.

**EV-SRC-REPORTED / EV-NOT-RERUN — checker.** The PR stores `check_output.txt`: C0–C16 **17/17 PASS**, 18/18 negative controls caught, C8 checking 48 consumer pin occurrences. The Python builder/checker and the 18 negative controls were **not run by this reviewer**. Source existence/pin presence is not proof of an import's type or adoption.

## 2. R1 — required: distinguish claim imports from reference-only feedback

**Location and source conflict (current candidate inherited from v1.3):**

- **Programme §6.2 L287:** “OFN ... receives scoped technical feedback from DYAD, RECOG, GEN, TRIAD, OPEN M, NUMGEN and TDR-G **as imports** (OFN §11).” **[OWNER: OFN v0.12 §§11.2–11.3]** The actual `IMP-O08-*` / `IMP-O09-*` claim-level imports identify **DYAD, RECOG, GEN and TDR-G**; its `RF-O08-*` / `RF-O09-*` entries discuss **TRIAD, OPEN M and NUMGEN** as reference-only technical feedback. A text claim that all seven are imported is unsupported. Correct this partition in place.
- **Programme §6.3 L305:** OPEN-M “Imports Genesis, Dyadic, Triadic, OFN, Programme and Pre-Legacy priors.” **[OWNER: UVM v0.7.1 §7]** UVM's GEN/DYAD/TRIAD technical imports must be distinguished from its OFN constitutional/model-selection reference, Programme governance reference, and Pre-Legacy historical/provenance priors. Do not imply all six are scientific imports.
- **Programme §7.1 L380:** Under “Continuous declared imports”, `OFN <-- DYAD, RECOG, GEN, TRIAD, UVM, NUMGEN, TDRG` repeats the same overstatement and places the **discrete TDR-G mathematical imports** under the continuous-import heading. Give foundation-owned claim imports a distinct line, noting TDR-G's scope and SG-PROG-1, and show TRIAD/UVM/NUMGEN as reference-only input rather than adopted claim imports.
- **Programme §7.1 L385:** `NUMGEN -?-> OFN ... (recorded by OFN as import; open items remain)` is incorrect. **[OWNER: OFN v0.12 §11.3 RF-O08-09/10 and RF-O09-04]** NUMGEN is presently reference-only/feedback in OFN; a future claim import is the receiver's decision.
- **Programme IF03 L420:** `OFN → TDRG` is currently typed only as “constraint”. **[OWNER: TDR-G v2.12.14 §7]** TDR-G explicitly imports `RTG-OFN-ALG-STAR-TOKEN-SHIFT` at its **OFN v0.10 claim-level pin** for SG-14, while treating general OFN O0–O3 commitments as context. Type the limited claim import and the background reference separately; do not auto-repin v0.10.
- **Programme IF24 L441:** `NUMGEN → OFN` is marked “feedback (recorded import)”. **[OWNER: OFN v0.12 §11.3 RF-O08-09/10]** The additive holonomy and local-history results are source reports/reference-only; use “reference-only technical feedback”, not “recorded import”.
- **Programme IF32 L449:** `DYAD, GEN, TRIAD, UVM, TDRG → OFN` is labelled “declared-import (scoped feedback)” with the content field “IMP-O10-*”. **[OWNER: OFN v0.12 §§11.2–11.5]** This combines four genuine technical import sources (DYAD/GEN/TDR-G, with RECOG handled separately under IF28) with TRIAD/UVM reference-only feedback. The IMP/RF distinction and relevant §11 source scope should be reflected, either as a mixed-type row or separated without recycling an IF ID.

**Consequence:** This is a **D-GRADE/D-SCOPE source-use attribution** error, not a refutation of an imported theorem or evidence that a reported feedback statement is false. The issue is significant because Programme owns the typed interface map: labelling reference-only statements “imported” risks wrongly granting transfer or consumer acceptance. It is therefore **R1 required for adoption**, but the remedy is a small text-only batch (7 existing loci), not new scientific analysis.

**R1 acceptance criteria:** In one batch, revise the seven loci above; preserve scientific scopes, source editions, intentional historical pins and IF identifiers IF01–IF38; add a checker/negative-control assertion for *claim import versus reference-only* in §6.2/§7.1/IF24/IF32 (and IF03's explicit source RID); rebuild and register the changed SHA-256, edit log and publication-transform test hash. A scoped delta review of R1 is sufficient; do not rerun the unchanged owner's scientific certificates.

## 3. Decisions on the five release-record review questions

| Review item | Verdict and support |
|---|---|
| §4(1) Changed interface pins IF02–IF07, IF12, IF14, IF16, IF25–IF27, IF29, IF31; new IF37–IF38 | **PASS WITH R1 SOURCE-TYPING CORRECTION.** Confirmed TRIAD §7.1 claim-level DYAD v6.4.23 repin; GEN §7 retains v6.4.13/v6.4.22/v6.4.23 mixed DYAD pins; TRIAD §7.2 still holds some GEN v2.9 claims and the radial polynomial at v2.8.7 despite GEN v2.10 existing; GEN §7 uses TRIAD v1.7; UVM §7 uses TRIAD v1.6, intentionally; NUMGEN §9.1 uses DYAD v6.4.18/v6.4.22, GEN v2.9 `GEN-ART-SATURATION`; GEN §7 uses `NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE` v1.21. `GEN-ART-SATURATION` is an **artifact locator**, not a separate theorem RID; IF37 must not be read as a new theorem. IF03's actual OFN import is under-typed (R1). |
| §4(2) TDR-G “executed in part” | **ACCEPT.** [OWNER: TDR-G v2.12.14 §2] Of the four Programme v1.2 review tasks: antipodal path-tie **discharged**, state/gauge **advanced but still open**, counting observables **open**, growth fits/statistical-rank interpretation **open**. Owner v2.12.14 is a corrections-only edition under declared Methodology v1.2; v1.4 migration deferred to v2.13. Thus “not executed” would hide material partial completion; “executed” would incorrectly imply closure. |
| §4(3) CN-05 and IF11 | **PASS.** TRIAD v1.7 §7.4 previously recorded no Programme CN-05 disposition; the Programme candidate may record receipt and acceptance with **no operational action** since it imports no withdrawn phase-steering, wedge, no-basin or cascade verdict. IF07 follows GEN v2.10's TRIAD v1.7 import; IF11 remains UVM v0.7.1's valid TRIAD v1.6 pin. “Accept; no action required” is not an assertion of new imported science. |
| §4(4) κ_f row | **PASS.** [OWNER: GEN v2.10 §6.8] `κ_f := |m||w|` is a face-lift magnitude distinct from the triadic birth κ, κ_phys, κ_RTG and γ. The corrected class-C κ/γ row matches the OFN v0.12 and RRF v0.8.4 parameter convention; it is not a physical parameter identification. |
| §4(5) DYAD, GEN, TRIAD import summaries | **PASS** for those three source summaries in Programme §6.3: DYAD's claim-level scientific inputs are RECOG-owned; GEN's OFN linkage is companion/reference-only; TRIAD's RRF/OFN/Programme/TDR-G relations are references, not scientific claim imports. The additional R1 problem is the unchanged **OFN/UVM** summary and IF map, not these three corrected summaries. |

**Launch gate:** [OWNER: TDR-G v2.12.14 §§1–2/Appendix C] D/F closed at mechanism scope, A→B→C unresolved, Appendix C aligned; one older §7 `TDRG-EXPORT-DISCRETE-TRIAD` gate still names D/A/B. Candidate records this as a residual, not permission to launch.

## 4. R2 — nonblocking source-of-truth wording

Programme §6.1 L253 (inherited from v1.3) says `BASELINE.md` is “the authority” whenever it conflicts with the Programme table. **[OWNER: CONVENTIONS.md §2]** The true governing document is the latest **adopted tag + release/adoption record**; `BASELINE.md` is an identity/inventory manifest and may itself lag. Prefer “on disagreement, verify the adopted tag and owner release record; update the stale table/BASELINE entry” rather than making the manifest the ultimate source of truth. This is **ADVISORY**, not an additional scientific gate. It can be folded into R1's text maintenance.

## 5. Final disposition and publication boundary

**CONDITIONAL PASS — apply R1 before PI adoption.** The candidate is mechanically reproducible, the core scientific OPEN/maturity/guard constraints are preserved, the updated owner versions and principal pin decisions are sound, and TDR-G's partial-pass status is well supported. The required correction is **source-authority typing** at seven existing positions; it changes neither mathematical owner claims nor the programme OPEN states.

No Programme, owner, Atlas, release record or pipe item has been modified by this review. Do not merge, tag or announce adoption based on the checker PASS alone. After an R1 patch, perform a narrow changed-line review, then submit the full publication candidate to the PI; the PI's subsequent acceptance and merge/tag decisions are separate.
