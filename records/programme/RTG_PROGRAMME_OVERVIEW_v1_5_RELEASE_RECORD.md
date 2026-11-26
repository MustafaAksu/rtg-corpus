# Programme Overview v1.5 — DRAFT release and receiving record

**Date:** 26 November 2026.
**Status:** [SESSION] / DRAFT; revision 2 after independent review 7185447417 (ACCEPT WITH CHANGES); B1–B3 and O1–O3 addressed, readback pending; not adopted. Governing edition remains `programme-v1.4`.
**Authority:** Standing Programme maintenance by the existing Atlas team: ChatGPT prepares Programme updates and receiving dispositions; Claude independently reviews; the PI decides policies, adoption and publication. Technical scientific owners retain their authority; Atlas build/review roles are unchanged. The decision is independent of this edition's adoption; no separate Programme owner session or Methodology amendment. See the independent decision record `records/programme/PROGRAMME_EDITORIAL_ASSIGNMENT_20261126.md`. The PI authorized preparation only; exact-hash adoption and SAT policy assent remain pending.

**PI decision (verbatim).** Direct PI message in the RTG Dyadic project's Atlas co-owner conversation, 26 November 2026. The exact message time is not exposed in the accessible conversation metadata; the decision preceded creation of PR #392 (2026-11-26T07:07:33Z, verified GitHub metadata), which is an upper bound, not the decision timestamp. In the immediately preceding reply the roles above were proposed for Programme only. The PI answered:

> Evet bu görev dağılımı kalıcı olsun ve **Programme v1.5 hazırlığınına başla lütfen**

The role assignment is already decided; Programme v1.5 adoption is not. Claude's shared ENTRY acceptance is conditional on the two wording corrections in review 7185447417, which this revision applies.
**Source checkpoint:** `c92deb13c153d695a88136f24a9aac28eaf41622`; base tag `programme-v1.4`, annotated object `73641f15a14f0cb5e3f7f5f3b1bbff8de1e1857b` → `514e17f3078b2569779bce67b7855d0f668fe316`; main/tag blob `2e78ea684d3a2ff9934f02e55d32d556db022ed5` identical; predecessor release record `records/programme/RTG_PROGRAMME_OVERVIEW_v1_4_RELEASE_RECORD.md`. Methodology v1.4 §§0.5, 1.1, 13.1, 13.5–13.9; CONVENTIONS §§1–9; `pipes/README.md`; accepted #360 advisory (merge `bc5bd11ec2dae9b623ed231a6d18f8da705294bf`).
**LIT dependencies:** none used in this maintenance preparation.

## 1. Candidate and checks

| Object | SHA-256 |
|---|---|
| Adopted base | 37d857d08bb47771ed50fc5829584be74aab120a23e922eba7c84bae097f28c0 |
| Round-1 reviewed DRAFT candidate at 322ab8a42a8de71b232e8a6156c2740a7cd16882 | abe033d06206f1615ad72a5234882645e8a63bf18d59c0a28e5ce6ec9b7fb618 |
| Current revision-2 DRAFT candidate (PI exact-hash adoption pending) | c07689b0f6e617c0b4a6a29d95d194b99bbbe3f4c3c8a686ccfd02d492c0811c |
| Published fixed-name DSN (separate final SHA-256) | PENDING — computed after PI adoption by metadata-only publication transformation; not the draft hash |
| `evidence/programme/v1.5/edit_map.json` | f344c91e78fb8d153ce2ba03bf97d4c49c07ee9c920c9659d7c266a4a9cad482 |
| `evidence/programme/v1.5/edit_log.json` | 5c4cabbe826dde05118b6c3942e17ff0425fc5f3819326cf084320d58937250c |
| `evidence/programme/scripts/build_programme_v1_5.js` | d160abadeafa46269b741b2a2491f4a6376e591856eb230b1d41c0967f32e668 |
| `evidence/programme/v1.5/check_output.txt` | ddd8251318e7b4d5b3f292bf86bc44f6171dff54bb041e7f17c946e31ee35d44 |

Round-1 map, log and check-output bytes remain accessible unchanged at the reviewed head `322ab8a42a8de71b232e8a6156c2740a7cd16882`; SHA-256 respectively `39e46756323a63685be039fdba35081ae65e89c94de6eb374224330c177f38e5`, `da07c796dcb2a148fa11603e174d6c56a9242c89e44e4e4b7c8f9217a5273831`, `5762b24bbfe5cdbf57cfc1ad184fd21ad06e7d33d1c45db7e89badf5efeeef03`. The builder is byte-identical across the two rounds.

One content stage, 82 exact ordered original-base-line edits; no compaction. Revision 2 changes only the new payloads of four existing edits E0313/E0333/E0429/E0446. Candidate 641 newline-terminated lines, 81061 UTF-8 bytes. [EV-HASH, EV-BYTES, EV-RUN] Connector JavaScript actually rebuilt forward and reversed exactly, checked payload/document hash links and 13 structural gates, rejected 7 synthetic mutations; output retained. These are bounded structural checks, not a full semantic proof. The unchanged native Node adapter was independently run by Claude at the round-1 head (see below); revision-2 native replay is pending. For changed-head readback, run from checkout:

```sh
work=$(mktemp -d)
git show programme-v1.4:dsn/RTG_PROGRAMME_OVERVIEW.md > "$work/base.md"
node evidence/programme/scripts/build_programme_v1_5.js "$work/base.md" evidence/programme/v1.5/edit_map.json "$work/candidate.md" "$work/log.json"
cmp "$work/candidate.md" dsn/RTG_PROGRAMME_OVERVIEW.md
cmp "$work/log.json" evidence/programme/v1.5/edit_log.json
python3 -I tools/dsn_lint.py dsn/RTG_PROGRAMME_OVERVIEW.md --prev "$work/base.md"
python3 -I tools/pipes_index.py --check
```

The seven negative controls were executed again in connector JavaScript for revision 2; the native adapter replays the positive checks, not the negative harness. No new native execution, linter, pipe checker, trial merge, scientific certificate or campaign was performed by the preparer.

**Round-1 independent review (EV-SRC-READ of reviewer-reported EV-RUN, [7185447417](https://github.com/MustafaAksu/rtg-corpus/pull/392#issuecomment-7185447417), exact head `322ab8a42a8de71b232e8a6156c2740a7cd16882`).** ACCEPT WITH CHANGES; no blocking scientific or interface error. Claude reports a clean Node v22.23.5 rebuild of 82 edits, C0–C12 PASS, byte-identical candidate and log, all four evidence hashes matched, informational lint (+5,725 bytes, +7.7%, zero near-duplicate paragraphs), clean trial merge at `c92deb1`, and native pipes OK 183 items / 20 inboxes. NC1–NC7 were not run natively. These results belong to round 1; they do not assert a new native run at the revised head. Claude checked changed interface rows and selected unchanged rows against actual consumer tags; all 19 inventory rows agreed with the tag/BASELINE inventory, and the thirteen dispositions were accepted at scope.

**Revision-2 review corrections:** B1 standing decision quotation/independent record and ENTRY cleanup; B2 IF09 explicitly discussion-only `UVM-PROP-JPERP-01` (not an RID or adopted result); B3 IF26 full `DYAD-THM-OPEN21-SHARP-ROWS`, P12 context wording, Atlas work-list A6 path. O1 satellite request/checker basis versus convention text; O2 Atlas permission on request, not duty; O3 TDR-G AZ reference context. Reopened UVM stage-1 §6, DYAD v6.4.24 §6.14 full declaration, SAT request 3 and Atlas A6 row. No pin, grade, proposed verdict or gate changed. Exact round-1 replay and changed-lines comparison passed before rebuilding from the tagged base. All 82 original addresses retained; only four new payloads differ. Five programme OPEN RIDs/statuses ACTIVE, architecture, maturity definitions, SG-PROG-1–4 and high-risk guards, 38 IF identities, anchors, predecessor history and Appendix B preserved; the four §5 edits are source-pointer/dependency-report edits, not closure-criterion changes.

## 2. Source manifest and reading extent

Eight updated inventory source files were re-fetched at the tags and their full digests recomputed to match BASELINE at the checkpoint; source versions are not consumer pins. Latest matching tag refs checked for all nineteen existing inventory homes. The following is targeted source reading, not a new owner proof audit.

| Source | Tag | SHA-256 (fresh tagged-text hash) | Reading scope |
|---|---|---|---|
| OFN | ofn-v0.13 | 4a2d266bf89cd2130e901b7543bacbaf7fa3e844c60e355a2e3c23ef4f075a49 | §§5.5,9,11–12 and release/post-tag record; IF03/24/28/31/32 |
| NUMGEN | numgen-v1.22 | 36b31755c1bd73f1d5f69117c63b1556afacc18c2505e1b865b7a3adf512d40b | §6.6 P2/M4 and §9.1 pins; notice and adopted release/post-tag record |
| DYAD | dyad-v6.4.24 | 10fbdacc19544596480acae03faeba076f21103a01b903a8d3305cfa8ed7bc16 | §1 map, §§6.14,7 actual RECOG/OFN/GEN/TRIAD pointers |
| UVM | uvm-v0.7.2 | 2bd854dfd0168906159f8add900ad70c86782bc8d06b420614308959f807880f | header, §§0.3,7,9; release and review/notice; C3 |
| DZT | dzt-v0.19 | 2b959f46b8e23363beac087183caf4946d63d1e8d5ac597bdb7d9230143bf6ce | header, §§2,6.3,7 and two notices |
| TDRG | tdrg-v2.13 | 98b4cba5ecb30f23f9dd97be27a7896191aa514ddefc402fd129ea673f0357f6 | header, §§1–2,7, Appendix C gate references and notices |
| AZ | az-v0.10 | 0cc84c9a587bab270624a824d5e004a327f20f41f0c03307e01a6725afe80e6e | header, §8 IMP-A/B, diagnostic references; four notices |
| ATLAS | atlas-v0.15 | 483e60034ff3bb644216c5123d28b8bca253d3ba1b72cdf68bfb0056518d02df | accepted snapshot identity; no re-extraction or v0.16 |

Read Programme v1.4 §§0–4, §5, §§6–9 and Appendices A/B (full relevant text), its release record, #360 advisory and all 13 open pipe payloads; CONVENTIONS, Methodology profile/release rules and Atlas Method authority boundary. Additional tagged passages: GEN v2.10 §7, §6.4 references; TRIAD v1.7 §§2,7.1–7.4; RECOG v0.3.27 §7 and GAP-LOCK consumption; RRF v0.8.4 remains the declared standard at its existing pins; no new RRF scientific review or source-status decision. Previously verified source identity records are not fresh all-source hash checks for unchanged homes. No blanket review of the other 38-IF endpoints; unchanged rows retain their recorded scope pending a particular affected-use finding. RRF/PRR status/placement and historical Programme v1.2 evidence recovery are separate; no archive re-scan or private LIT claim.

## 3. Receiving proposals (not queue edits)

At checkpoint the actual `pipes/PROG/INDEX.md` has 13 open, 4 closed. All thirteen payloads inspected. Proposals are made in Programme's delegated receiver role, reviewed separately by Claude. Close applicable items after the verified tag using the adopted record; keep any genuinely unresolved policy matter open if the PI changes the proposed disposition. Sender payloads and the four already-closed items stay unchanged.

| Key | File in pipes/PROG/ | Proposed verdict | Scoped acceptance/change |
|---|---|---|---|
| P01 | `20261109-SAT-satellite-interface.md` | accept with change | §6.5 SAT policy proposal: registry pointer instead of duplicate manifest; SAT sender key with study in object/body; relevant RTG owner/Atlas may propose receiver-specific notices on verified adopted tags. No SAT repo policy amendment or automatic repin; PI policy adoption pending. |
| P02 | `20261111-AZ-v0-7-adopted.md` | accept with change | §6.1/6.5/7.2/9.2 AZ corrections and historical v0.7 notice, then current v0.10 state. SG-PROG unchanged; no new grade. |
| P03 | `20261112-AZ-v0-8-adopted.md` | accept with change | AZ v0.8 Methodology migration and summary reduction complete; §6.7 executed reduction only, no merger; Level A. |
| P04 | `20261112-TDRG-v2-12-15-adopted.md` | accept with change | TDR-G v2.12.15 corrected export row; actual gate A→B→C/T0 retained; §6.4/7.3; no token law imported as a bridge. |
| P05 | `20261114-AZ-v0-9-adopted.md` | accept with change | AZ v0.9 S1 diagnostic and actual TDR-G v2.12.15 context pin; not TDR-G result or Level B. |
| P06 | `20261116-AZ-v0-10-adopted.md` | accept with change | AZ v0.10 S2 diagnostic, current inventory and unchanged actual context pins. No numerical rerun. |
| P07 | `20261116-TDRG-v2-13-adopted.md` | accept with change | TDR-G v2.13 Methodology migration; separate exports, open custody, remaining gate; not new science. |
| P08 | `20261119-DZT-v0-18-adopted.md` | accept with change | DZT v0.18 migration and IF18 actual DYAD v6.4.24 pin; IF19 open; v0.9–v0.17 recovered unadopted history, no lineage promotion. |
| P09 | `20261120-DZT-v0-19-adopted.md` | accept with change | DZT v0.19 conditional absolute norm law, sign excluded; Level A retained; B1/B2 open. |
| P10 | `20261122-ATLAS-programme-receiver-pass.md` | accept | Requested receiving pass performed at draft scope in this record; all nine original notices addressed, plus three later source notices. Queue closure after review/adopted tag, not by this proposal. |
| P11 | `20261124-NUMGEN-v1-22-adopted.md` | accept with change | NUMGEN v1.22 inventory, IF13 split pin/evidence, IF14 two grades, IF24 scoped references, IF27 comparison only; IF12/37/38 unchanged actual proof pins. M4 HOLD and Census-1 unchanged. |
| P12 | `20261125-OFN-v0-13-adopted.md` | accept with change | OFN v0.13 criterion pointers, IF03 actual TDR-G v0.12 import, IF24/28/31/32 typed uses; IF02: DYAD's OFN v0.12 programme context retained. No custody or criterion change. |
| P13 | `20261125-UVM-v0-7-2-adopted.md` | accept with change | UVM v0.7.2 inventory, IF08/10/11 scoped current and historical pins, IF09 C3 gate, IF23 unchanged; RRF reference-only added to IF29. No physical source delivered. |

SAT: checked `rtg-sat/CONVENTIONS.md` §§3–5 and `REGISTRY.md` at observed main `1b2de67c5e5bf9e87490b121443ba66ab57a55a9`, and `tools/sat_check.py` sender/schema/tag-handling code; RTG `tools/pipes_index.py` accepts SAT and only valid stream keys in `filed_by`. The satellite checker permits RTG senders including ATLAS and validates local satellite tags, so actual external RTG tag identity must be verified separately. The route is expressly requested in SAT item P01 request 3, but RTG senders are not yet expressly described by the satellite conventions' §5 text. Any amendment belongs to the SAT co-owners; Atlas filing is permitted when requested by the relevant owner or PI, with no standing monitoring duty. Proposed resolution: stable registry link, one SAT key, receiver-specific scoped notice process. No satellite inventory copy, satellite amendment, automatic repin, new recipient decision or cross-repository filing. Separate policy assent is part of PI adoption of the proposed §6.5; if withheld, retain P01 open and remove that policy paragraph before adoption.

## 4. Review map and retained limits

- Inventory §§6.1–6.5: OFN v0.13, NUMGEN v1.22, DYAD v6.4.24, UVM v0.7.2, DZT v0.19, TDR-G v2.13, AZ v0.10, Atlas v0.15; no new homes. Verify all edited lines against the source manifest, not newer tags by themselves. RRF remains reference/working-standard scope; PRR files do not create a governing home. FMS is reference-only SESSION, not an OFN adopted theorem.
- P0/P2B criterion home moves to OFN v0.13 with criteria unchanged; P3 UVM current dependency report adds no deficit factor or UV/Regge closure. §4 preserves all A–D assignments; no promotion of AZ/DZT/UVM. §6.4 preserves TDR-G A/B/C/T0 launch gate and the D/F analytic residuals, separately TDR-19/bridge.
- IF03 actual TDR-G OFN v0.12 pin (not v0.13). IF08/10/11 UVM current and historical pins; IF09 remains open. IF12/37/38 deliberately unchanged: v6.4.18/v6.4.22, GEN v2.9, NUMGEN v1.21 respectively. IF13 state/recurrence v2.13, SG-10/frozen harness v2.12.13, finite re-annotation rule v2.13 separate evidence input. IF14 ALG identity versus HEUR locking cross-reference; RECOG pins stay v1.21 and historical pins. IF18 DYAD v6.4.24; IF19 open; IF20 DYAD v6.4.24, IF21 TDRG v2.12.15 branch-local reference. IF23 PREL v0.8 unchanged. IF24 v1.21 references and v1.22 receipt/P2 separate, N-1A2 vocabulary only. IF26 R9 sharper-row companion conditional. IF27 comparison-only, IF28 actual OFN RECOG use, IF29 UVM reference-only RRF, IF31 OFN attribution, IF32 split pins incl UVM v0.7.1 reference. IF02 actual DYAD OFN v0.12 context retained; IF30 RRF old pins not repinned. IF36 atlas-v0.15 source manifest remains frozen. Other IF rows not reopened for mere age of pin.
- §6.7 records AZ's executed v0.8 summary reduction; no new split or merger. §9.2: TDR-G/DZT/AZ maintenance done, NUMGEN/OFN/UVM new editions reflected; Pre-Legacy remains the original sequence item. All scientific OPENs and evidence gaps kept. No scientific owner DSN edits, no extra Programme/Atlas release, no automatic consumer notices or adopted use.

## 5. Next decision and publication boundary

Claude: changed-head readback of B1–B3 and O1–O3, including the independent decision record and shared ENTRY wording; verify the rebuilt candidate/log and current hashes, and rerun only the affected native checks. The thirteen receiving verdicts, pins and scientific guards are unchanged; no new whole-source review requested. If accepted, PI decides exact-hash adoption and SAT policy. Only that decision authorizes publication metadata transformation, final hash, BASELINE, merge and annotated `programme-v1.5`. The release record must name both the exact adopted candidate SHA-256 and the separately computed published fixed-name DSN SHA-256, with the metadata-only transformation recorded; the published value is not asserted before adoption. Then close actual receiver items and file scoped notices only where an actual change warrants them. This draft does not update BASELINE, adopted Atlas, any pipe, tag or source owner file. The existing Atlas v0.15 remains governing derived snapshot; no Atlas v0.16.
