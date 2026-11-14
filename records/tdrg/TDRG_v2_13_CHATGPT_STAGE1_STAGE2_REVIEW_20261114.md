# TDR-G v2.13 — independent co-owner review of Stage 1 and Stage 2

**Date:** 14 November 2026. **Reviewer:** ChatGPT, independent TDR-G co-owner.  
**Verdict:** **CONDITIONAL PASS / ACCEPT WITH CHANGE**. Stage 2's declared mechanical transform passes an independent byte-exact replay. Stage 1's source-pins and current-state readouts are supported, but the proposed Methodology v1.4 migration still contains an unpaired live RESULT claim (R1). The release record also needs to qualify a misleading lint metric (R2). Neither finding warrants rerunning unchanged scientific campaigns. This is a review, not owner disposition, PI adoption or publication.

**Target:** PR #265, head e9778208537278131d22bbc3ac1ae3a024aa388a (DRAFT); baseline main 903f530e58a05e21e9d5739e7ce333e76473d883.  
**Governing source:** TDR-G tagged edition tdrg-v2.12.15, SHA-256 1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64.  
**Governing methodology:** methodology-v1.4. The release plan in PR #263 is included as a file on the PR #265 branch; the two review subjects are an intermediate and final candidate, not separately adopted editions.

## 1. Source and reading manifest

- Repository root CONVENTIONS.md and BASELINE.md, at the inspected main HEAD; Methodology v1.4 targeted §§1, 1.1, 3.4, 4.4, 13.3, 13.5–13.8. The live-file rule, mandatory RESULT pairing, compaction obligations and release-record freeze were checked.
- TDR-G owner DSN at tdrg-v2.12.15: targeted header, §1, §2 priority and relevant TDR-24B/TDR-25/TDR-26, §§6.2, 6.3, 6.5, 6.6, 6.8, §7, §8, Appendix A (§A.sim), Appendix B and footer. This is a changed-dependency review, not a fresh full reread of unchanged scientific sections.
- Stage-1 intermediate at commit 1a8e02a29ed4589291b752e0a0a0901cf7e7d8b6; candidate at PR #265 head; 29-entry Stage-1 edit log, its checker including C0–C10 and controls, stored owner-run gate/control outputs.
- Full Stage-2 movement_map.json (43 operations), Stage-2 builder, check_compaction report and negative-control report, and the complete Stage-1 intermediate and candidate bytes for independent movement-map replay. The checker output is an owner-run result; the independent replay noted below is not execution of that Python checker.
- AZ at tags az-v0.6, az-v0.7 and az-v0.8: targeted AZ-ALG-ANTIPODAL-LOWORDER source sentence in §4.3.2 and AZ v0.8 §8 IMP-B. OFN at ofn-v0.12: OPEN-OFN-2 and IMP-O08-06/14. No independent rerun of TDR-G BIND3, historical motif or AZ numerical campaigns.
- Full two separate SESSION decision notes: records/tdrg/TDRG_DECISION_NOTE_LARGEST_CENTER_TDR19.md and records/tdrg/TDRG_DECISION_NOTE_XFER_O08_01.md; the short tie-probe source and its three output rows.

## 2. Source identity and computational extent

**[SESSION — independent hash and mechanical replay]** SHA-256 was computed independently from full GitHub-fetched UTF-8 bytes (not copied from the release record):

| Object | SHA-256 |
|---|---|
| Adopted base | 1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64 |
| Stage-1 intermediate | b24c17ccbc93150449842a603c2c18fd47e66bc6f27ee77152802b36d450cdcc |
| Stage-2 candidate | 1691a136d01ce3f68a241c72d13d9f17c1a184986f6869fe9b9d507a324dee18 |
| Movement map | 024a730e0482404c8c77299036d37cc7f6cd97c8b24547bc8ccb7cc31866a75b |

I independently interpreted all 43 movement-map operations (40 exact anchored history-label substitutions, the header, Appendix A and footer replacements) against the Stage-1 bytes. The generated candidate was byte-for-byte **identical** to the PR #265 DSN and had the exact candidate SHA-256 above. This is an independent reimplementation of the declared map transform, not merely a replay of the Python checker.

Across the adopted base, intermediate and final candidate the 81 TDRG/owner RID declarations in §§2–9 remained identical. All 21 registered OPEN records retained their heading, RID and status after purely historical version-label removal. No missing original registered RID was found.

**[OWNER-RUN, not independently executed here]** Stage-1 checker reports 11/11 gates and 9/9 negative controls. Stage-2 tools/check_compaction.py reports PASS, 268 live claim blocks (244 byte-identical, 24 declared transforms, 0 unexplained) and 8/8 negative controls. These check structural eligibility and byte identity, not unrestricted semantic equivalence or scientific adoption.

## 3. Stage-1 scientific/interface findings

**[SESSION] PASS — qualified current-state edits.** AZ-ALG-ANTIPODAL-LOWORDER's algebraic statement is text-identical at az-v0.6, az-v0.7 and az-v0.8. Its surrounding angular-interpretation commentary is not identical, and the TDR-G citation correctly targets the unchanged narrow-band algebraic statement, not AZ's numerical angular diagnostic. OFN v0.12 actually contains RTG-OFN-OPEN-DISC-INTERACTION and the importer entries IMP-O08-06 (LEM-NOANNIHIL) and IMP-O08-14 (CONV-TICK). The AZ v0.8 IMP-B recipient still intentionally cites TDR-G at tdrg-v2.12.14; TDR-G's new consumer row reproduces that pin rather than inventing repinning/adopted use.

**[SESSION] PASS — scientifically scoped maintenance.** The §1 summary uses the detailed source grades: [ALG] band reachability from LEM-REACH; distinct [NUM] and [HEUR strong] policy-branch grades from §6.6; [ALG] for finite exact BIND3 enumeration and [NUM strong] for BIND3 parity/gate results at their historical scopes. No grade was changed in §§2–9. TDR-6 remains PARTIAL; TDR-19 and XFER-O08-01 remain open. The failed-relock historical hypothesis is explicitly superseded and preserved verbatim in Appendix B; its live §2 replacement remains. Moving §A.sim to §8 preserves its literal table and the final interpretive sentence. The Stage-1 readout is 407 words: above the 200–400-word target, below the 500-word documented exception threshold; informational, nonblocking.

### R1 — REQUIRED: unpaired RESULT becomes a live claim under Methodology v1.4

**Exact location:** Final candidate §8, immediately below the relocated “Simulation artifact evolution” table. The unchanged historical sentence reads:

> [RESULT] Policy and bookkeeping bugs can invert the cosmological interpretation.

Under adopted **Methodology v1.4 §3.4**, a RESULT must have exactly one canonical [from: STATUS] pairing, with the interpretation's actual assumptions/evidence visible. Previously this sentence was inside historical Appendix A §A.sim. The Stage-1 edit copies it into the **live artifact registry §8**. The Stage-1 checker verifies literal equality, not current v1.4 claim-typing compliance. A mechanical PASS does not discharge the required scientific/evidential grade decision.

**Acceptance alternatives:**
1. In Stage 1, the responsible owner selects and justifies the correct [RESULT] [from: …] grade and scope, with an explicit dependency on the relevant source engineering/interpretive evidence. A review checks the newly typed claim.
2. If no grading decision is intended in this maintenance edition, move only the engine lineage facts into §8 and preserve this **historical interpretation** via its immutable predecessor Appendix A (with a pointer rather than a new live unpaired RESULT). Confirm that any adjustment to PI's D3(a) placement decision is authorized.

Do **not** silently assign [from: ALG] or claim full Methodology v1.4 conformity with the live unpaired result. A bounded Stage-1 correction followed by rebuilding Stage 2 and rerunning the two-stage mechanical checks suffices. No historical numerical campaign needs rerunning.

### R2 — REQUIRED RECORD CLARIFICATION: lint newly referenced foreign RID

**Exact location:** DRAFT release record §8 (size report) and the corresponding interpretation. The raw lint output says “new_rids: 1” and “growth_per_new_rid: -39008.0”. The only new identifier compared with the predecessor is an **existing OFN owner RID** appearing in an updated TDR-G connection: RTG-OFN-OPEN-DISC-INTERACTION, verified at ofn-v0.12. There is **no newly registered TDR-G RID**; all 81 owner declarations in the live scientific sections persist.

Under Methodology v1.4 §13.8, growth per new RID is N/A when no RID is added. Keep the raw lint output and its counting method unaltered, but annotate this as a scanner/reference-count false positive: “0 new TDR-G RID declarations; growth per new owner RID = N/A”. This is **record-only** and does not require changing the DSN or scientific grades.

## 4. Nonblocking limitations and advisory notes

- **Crystallization grade conflict:** §2 TDR-24B contains a historical note using [HEUR strong], while TDR-22b and the live §1 readout use [HEUR]. The release record expressly leaves this unresolved. Do not change the grade as a compaction edit; identify it as an owner-scientific review task.
- **Summary scope:** The new header says “genesis-layer kinematics are exact” and refers to BIND3 certification. §1 and §6.12 narrow the relevant BIND3 enumeration to N=24, k=1, no birth, v18 path orientation, with some historical artifacts still missing. No general-N or all-policy BIND3 proof follows from the header. A future readout may make this explicit, but unchanged §1/§6.12 source scopes currently control.
- **Consumer pins:** §7's absolute prose “no claim-specific historical pin remains in live sections” should be read as an assertion about TDR-G's own current imports; its AZ consumer row intentionally still records AZ's historical tdrg-v2.12.14 source pin. A narrower wording is advised if this line is touched.
- **Stage-2 history compaction:** Appendix A's one-line older-edition summaries are derived navigation, not replacement proofs. The full original historical text remains at the adopted predecessor tag. The independent mechanical replay checks only the declared transformation, not the truth of every newly worded historical précis.
- **TDR-19 largest_center note:** The source-reported tie incidences are 1023/1235 at N=90,k=6; 1117/1281 at N=120,k=8; 718/935 at N=240,k=16 (T=500, 2–3 seeds). The wrapper counts degree ties and returns the original centre choice, so this is useful bounded SESSION incidence evidence, not a new law or counterfactual outcome. L0–L4 options should remain separate from v2.13 and any candidate law-change campaign needs prior design and PI authorization.
- **XFER-O08-01 note:** A custody transfer does not follow from mathematical statement acceptance. X1 is a reasonable **proposal**, not an agreed transfer. First solicit OFN's explicit disposition via its inbox; only coordinated owner records/releases can reassign custody and notify consumers. The v2.13 maintenance candidate correctly leaves the transfer open.

## 5. Decision and narrowly scoped next action

**Stage 1: CONDITIONAL PASS** (R1 required to claim v1.4 live-format conformance; R2 release-record correction).  
**Stage 2: PASS for the current declared mechanical map**, conditional on re-running it if the Stage-1 bytes change.  
**Decision notes: ACCEPT AS ADVISORY**, not science adopted or policy/custody transfer.

Request a single correction round addressing R1 and R2, then rerun the 11 Stage-1 gates/9 negative controls and Stage-2 movement-map and 8 negative controls; a changed Stage-1 hash requires a new Stage-2 candidate and map identity. Seek a targeted readback of the corrected spans and then an atlas row check, followed by the PI's separate adoption and authorized merge/tag. Do not perform unchanged BIND3/NKSCAN/scaling campaigns or implement TDR-19/XFER actions during this maintenance review.

PR #263's plan content already sits on PR #265; it does not require an independent merge merely to preserve the plan. Any later closeout of the duplicate plan PR is an administrative owner choice. No DSN, engine, inbox, canonical tag or main-branch change was performed in this review.
