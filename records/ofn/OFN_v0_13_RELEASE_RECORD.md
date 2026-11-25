# OFN v0.13 release record

**Date:** 24 November 2026  
**Status:** DRAFT — receiving/synchronization maintenance candidate; not adopted.  
**Governing OFN:** `ofn-v0.12` and `records/ofn/OFN_v0_12_RELEASE_RECORD.md`.  
**Methodology:** `methodology-v1.4`.  
**Builder:** ChatGPT, OFN co-owner. Round 1 reviewed by Claude (PR #382: ACCEPT WITH CHANGE); round-2 delta/native readback and Atlas review pending.  
**Authority:** PI authorized the reconciled maintenance build, branch creation and the two receiving-record merges; the current instruction requests completion of ChatGPT's build responsibilities. No PI adoption, publication, tag or pipe-state change is authorized by that instruction.

## 1. Inputs and source checkpoint

- Reviewed advisory: `records/ofn/ATLAS_ADVISORY_OFN_SYNC_20261124.md`, PR #373, merge `9c51ba897ac2c8fb02fa0c22c639a62e76b3cea6` (navigation/advisory, not scientific owner).
- Independent receiving records: `records/ofn/OFN_RECEIVING_DISPOSITION_CHATGPT_20261124.md` (#378, merge `742692ed663e93f96467d041ac542c2aa1ac4e74`) and `records/ofn/OFN_RECEIVING_DISPOSITION_CLAUDE_20261124.md` (#379, merge `de80f558736b33a0e31de58733d547301f9a35c6`).
- Joint scope: `records/ofn/OFN_RECEIVING_RECONCILIATION_CLAUDE_20261124.md`, including the revised S2 extraction and R379-1/2. ChatGPT reviews 6042097108 and 6042580858; the latter accepted the revised receiving record, not this candidate.
- Build checkpoint: main `c5acda99de18598108e9b5e368ad15fa74f5488d`. The stage-1 branch fast-forwarded from the reconciliation merge to this commit before the build; it includes the newly adopted NUMGEN v1.22. Its annotated tag object `a81ae6d512e40a2f3e8de308e4035136d260613a` points to that checkpoint. The later NUMGEN reference/receipt delta in F3 below is explicitly submitted for candidate review rather than silently changing a reconciled claim pin.
- Freeze readback: main `085e567be4c522f4b7e62044e2755e3af9d7a9b0`. Comparison from the build checkpoint shows UVM document, evidence, records and BASELINE changes only. No OFN or OFN inbox change. UVM references are retained at their prior specific claim pins; the newer UVM material has not received a claim comparison in this pass. The inbox still contains nine open and three closed notices. No tag freshness alone establishes a mismatch.
- Base tag `ofn-v0.12`: annotated tag object `b313064f7d9453eb26c00c75248cfea84ee87a3b`, target `2b2573f59244851455cba16a2baa79c76cc8ec66`. Exact base bytes verified against the published digest.

## 2. Candidate and reproducible artifacts

| Object | SHA-256 |
|---|---|
| Adopted OFN v0.12 base | 55ff8ba85d4bb48b52266bdd9a44aa84efcd2cc19903d059266fa406a6bb76aa |
| OFN v0.13 DRAFT candidate | 8659d0bc046a204aae2dc0a7a9d3de3c302771e4b66fbde607730933cdbb283e |
| evidence/ofn/v0.13/edit_map.json | 6ad9a1274ef7140733ae1b5034d528a415c5d29c5fbf58e9c669b1911947b2f1 |
| evidence/ofn/v0.13/edit_log.json | 54b65a989e0167029837bbd71d981b267d878337f64f8a01ff6f6ffcf3ed3a5c |
| evidence/ofn/scripts/build_ofn_v0_13.js | 75c7811b092e467f461f36d6bcb516a675dfa0073003f330f51b4f8d136805bf |
| evidence/ofn/v0.13/source_verification.json | 3e23c0afb35d98c9dc59efd85a1d602fe59cdfee7172b355aec47dc789760ea4 |
| evidence/ofn/scripts/check_ofn_v0_13.js | 3d0bf326b75fa695ff0d1d2e9033d27c95485ba8167f9f11c1607301edcfe763 |
| evidence/ofn/v0.13/check_output.txt | 4584a2ab39f92e9cc1cbdc01a97659dc2aaf8d9151bfa05210d53b368c90d845 |
| evidence/ofn/v0.13/negative_controls_output.txt | e587dca5ffbab44ff1bb3a05ccfcc3e44583ada611a3f1c23c6e208414f6561d |

Round-2 candidate: 212,184 UTF-8 bytes, 1,613 newline-terminated lines. 145 exact, ordered, original-base-line-addressed edits; each old payload is checked at its immutable address. Edit map contains the full old/new payloads and reasons. Edit log records both payload hashes and each before/after document hash. No compaction stage. Round-1 candidate commit `8c052f6a809b95b2b7c5182db043b61575aceede`; source-verification commit `06eb42cfefd63d14f4e2a8c781e1507b3b56fd9e`; validation commit `94b53578e1e8f555ceaba43ff927f296aacf8bbb`.

**[EV-RUN, EV-HASH]** Builder and checker function bodies were actually executed in the connection-assisted JavaScript runtime, with a self-tested SHA-256 implementation. The independent replay reconstructs every unchanged segment and each new payload, checks all 290 payload hashes and document hash links, and reverses to the exact base. The saved scripts expose those functions through Node CLI adapters. Claude ran the native CLI adapters independently on round 1 (Node v22.23.5, Python 3.13.18; PR #382 §1): candidate/log and both checker outputs byte-identical, native SHA-256 matched. Round 2 was rebuilt and checked in connector JavaScript; independent native replay of the revised hash is pending. The checker CLI uses Node's native SHA-256. This is structural/build verification, not a new mathematical proof or independent scientific engine.

To reproduce from a checkout of the candidate:

```sh
tmp=$(mktemp -d)
git show ofn-v0.12:dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md > "$tmp/base.md"
node evidence/ofn/scripts/build_ofn_v0_13.js "$tmp/base.md" evidence/ofn/v0.13/edit_map.json "$tmp/out.md" "$tmp/log.json"
cmp "$tmp/out.md" dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md
cmp "$tmp/log.json" evidence/ofn/v0.13/edit_log.json
node evidence/ofn/scripts/check_ofn_v0_13.js "$tmp/base.md" evidence/ofn/v0.13/edit_map.json evidence/ofn/v0.13/edit_log.json dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md evidence/ofn/v0.13/source_verification.json --controls
python3 -I tools/dsn_lint.py dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md --prev "$tmp/base.md"
python3 -I tools/pipes_index.py --check
```

Claude's round-1 native DSN lint was informational (+5.5%); pipes check OK (149 items at the reviewed checkout); 22 import and 44 section-anchor locators re-resolved from tags without problems. These results apply to round 1, not the new head or current main. Round-2 native replay and independent delta review remain requested.

## 3. Content boundary and edit rationale

| Finding | Candidate disposition (not adoption) |
|---|---|
| F1 | Finding A's statement acceptance/import at TDR-G v2.13 is recorded separately from custody. Nine obsolete deferred-target sites and the associated scope label are corrected; XFER-O08-01 remains open, a separate two-owner decision. OFN owns the RID; fixed-map algebra and Appendix C history unchanged. |
| F2 | Answered token-sum referral recorded. Birth nonconservation is not gauge dependence. The declared phase gauge and relabelling invariance are retained; no physical-observable adoption or conservation law follows. |
| F3 | Corrected STAR event domain and CONV-TICK classification precedence; unchanged advance/snapshot/synchronous-event order and local fixed-map result. Three-node lemma retained; newer token/spectrum laws cited at TDR-G v2.13. Conditional one-step census interface in RF-O08-04 remains reference-only: given selected centre histogram, not autonomous selection, a reachability test, new OFN result or bridge. Historical v18 record retained. |
| F4 | A1c's D5B discharge recorded at RECOG v0.3.27, including its certified supporting source RIDs and applicable windows. D5A fallback not adopted. No removal of R9 where required, no claim of an unknown-a closure/identification beyond the source. |
| F5 | Matched source pins, IMP-O08-12 reference-map scope label, gamma/kappa convention attribution to OFN as recorded by RRF, and accurate historical-proof verification limits. DYAD v6.4.24 OPEN21 sharpened rows are a conditional companion, not a replacement for the earlier closing result. Older proof sources and R9 premises retained. |
| F6 | Repin only the matched Triadic reference components and consumer row. The corrected §6.18 coefficient-level Gram relation, coefficient-ODE clock, positive-Q domain and non-unique off-root extension remain explicit; no new discrete conservation, stability or physical theorem. GEN v2.8.5 components held. |
| F7 | Programme v1.4 source/criterion pointers and six interface roles; IF03 was correct when Programme adopted and the later current-use register update is Programme-owned. No Programme file edit or owner assignment by OFN. |
| F8 | Current diagnostic homes DZT v0.19 and AZ v0.10; reference only, no imported operator or bridge. DZT v0.17 remains recovered unadopted history. |
| F9 | Evidence accessibility/verification state and remaining qualifications recorded accurately. No O6 allocation. Prior P4 receiving audit did not certify all prerequisites; no promotion or new FMS work in this release. |

**Post-reconciliation bounded delta (review explicitly requested).** NUMGEN v1.22 was adopted and tagged before the build. At §6.6 and §9.1, the owner now records its own scoped P2 re-annotation and OFN receipt/export roles. RF-O08-01 separates (a) original v1.21 audit 40/136 exposed, (b) TDR-G's record of the Atlas rerun, and (c) NUMGEN's later owner execution: 158/158 frozen positive controls; DISC-2 40 exposed, 20 changed, 124 PASS, same ten-label projection; DISC-1 0/22 exposed and unchanged. Census-1 remains INCONCLUSIVE / INCONCLUSIVE and M-4 HOLD pending approved design/preregistration. No retroactive witness admission, certificate replacement or OFN DISC/BIND3 rerun. This is a reference/receipt update only: old NUMGEN claim pins remain v1.21 as stated. See NUMGEN v1.22 release record and `records/numgen/NUMGEN_v1_22_S1_P2_REANNOTATION.md`. No new NUMGEN notice was present in the freeze OFN inbox. Main readback `3164c3d90dffa00c5052219c4c55b782968a0d6c` on 25 November shows a later open notice, scoped to §9.1 receipt/export, not §6.6 P2. The P2 update originates in the OFN source read; see P10 below.

**Preservation:** no new or removed OFN RID; no definition, truth-grade or OPEN-status change; no selection of generator, carrier, primitive object, chirality, isolation contract or independence standard. Standard C, Q1–Q6, SG-OFN guards, REF-CLOSURE and class-C core preserved; all inherited Appendix A/B/C content and anchors preserved. The two authorized §9 edits are the OPEN-OFN-2 accounting wording and the matched contraction source pin. Eight newly cited external RIDs are existing source identities, not OFN registrations. No custody transfer and no source-owner DSN edits.

## 3a. Round 2 — response to Claude (25 November 2026)

PR #382 review record `records/ofn/OFN_v0_13_CANDIDATE_REVIEW_CLAUDE_20261125.md` at `adf12462e20f14ce4cd9bde30721b1a7285282b2`; comment 7154977429 on #381. Verdict ACCEPT WITH CHANGE on `2cc3af56d3c85a0193c4c9a996d92bdb140d0afe`, candidate `7f026a9d3da6c2572281972e7c35c7635fb74888307d9cfe28088087b14613d7`. Review evidence remains separate.

| Finding | Disposition |
|---|---|
| N1 | ACCEPT. E1393 separates the §9.1 receipt (REQ-O09-03 fulfilled; N-1A2 vocabulary only) from the §6.6 P2 re-annotation. Direct read of `numgen-v1.22` lines 1971, 2782, 2813; full source digest matched. |
| N2 | Original nine reconciled items retained; later main has a tenth open notice, P10 proposed for scoped receipt only. |
| N3 | Optional: deferred; valid historical campaign pin unchanged. |
| N4 | Round-1 native evidence recorded in §2; round-2 replay pending. |
| N5 | Claude's supplied checkpoint in his lane; dated shared/ChatGPT readback updated. |

The entire DSN delta is the single E1393 clause (+71 UTF-8 bytes). Builder from adopted base, C0–C10 and NC1–NC20 executed; check/controls outputs byte-identical to round 1. Source report retains the original checks with a dated round-2 delta, not a new eleven-source proof audit. Old bytes and digests retained in Git at the reviewed head. No scientific status, custody or selection change.

## 4. Verification extent and gates

Source report records exact full-byte SHA-256 comparisons of 11 tagged owner/governance texts: DYAD v6.4.24, GEN v2.10, TRIAD v1.7, TDR-G v2.13, RECOG v0.3.27, Programme v1.4, NUMGEN v1.22, DZT v0.19, AZ v0.10, RRF v0.8.4 and Methodology v1.4. All match expected recorded hashes. RRF identity is a working-standard cross-reference, not a fresh scientific adoption audit.

Reading extent: receiving records and revised reconciliation read in full; targeted declaring-line/claim-block and affected-section comparisons at the stated tags; new NUMGEN owner §6.6/§9.1 and release/adoption evidence; historical intake digests and scoped evidence references as in receiving records. Not a full proof audit of all eleven source documents. GEN §6.1/§6.3a–c and matched cited blocks checked; RECOG affected source sections and cited blocks checked, not a blanket repin of its older reference rows. DYAD 15 declaring lines match, 14 extracted claim blocks identical; OPEN21 companion scope added. TDR-G STAR/CONV-TICK actual affected-domain changes distinguished from labels and cross-reference differences. TRIAD S2 r2 repaired missing/ambiguous span acceptance; §6.18 substantive scope retained, CN-02 request sentence recognized. GEN v2.8.5 has not received full claim comparison. Programme matched guard/criterion use; IF03 maintenance remains on Programme side.

| Gate | Actual outcome |
|---|---|
| C0–C2 | Adopted base identity, exact 145-edit replay, 290 payload hashes, full document hash chain and exact reverse recovery PASS |
| C3–C6 | 44/44 own RIDs (17 DEF, 5 ALG results, 1 HYP, 21 OPEN), protected content, 20 ACTIVE + 1 PARTIAL, 101 anchors and inherited history PASS |
| C7–C8 | Stale live phrases removed; required scopes and limitations retained PASS |
| C9 | 11 source identities, eight new external RID references, 24 explicit import RID checks and 21 anchor checks PASS |
| C10 | DRAFT-only boundary PASS |
| NC1–NC20 | All 20 intentional negative controls caught by their intended gate |

The source report is a captured result of connector reads; the saved checker validates its identity and contents rather than fetching all source tags anew. The explicit import checks cover the 22 changed body imports matched by the checker, not every inherited historical proof or locator. No claim of semantic equivalence solely from a structural PASS. The checker was refined during execution to recognize the authorized contraction-pin edit and the exact NUMGEN wording; neither refinement altered candidate bytes. No earlier owner science campaign was repeated.

S-P4 evidence: PR #378's synthetic controls identify the wrong-direction ideal gate; PR #379's reported same-CAS execution of the unchanged FMS script checks both constructed elimination ideals, each generated by L/1026. This closes the gate-adequacy concern only for those constructed ideals, not the universal finite-a classification or source bilinearity/stabilizer/completeness prerequisites. See the two receiving records and `evidence/ofn/receiving_20261124_claude/`. No FMS regrade; separate FMS finding not filed by this build.

## 5. Receiving ledger — proposed post-tag dispositions

P01–P09 are the original agreed proposals. P10 is a late scoped receipt proposal pending co-owner confirmation. Nine notices open at original branch freeze; ten open on main at `3164c3d90dffa00c5052219c4c55b782968a0d6c`; three closed in both. These notices do not themselves establish adoption or consumer acceptance of OFN v0.13.

| P | File under pipes/OFN/ | Proposed disposition after adoption/tag |
|---|---|---|
| P01 | 20261030-DYAD-v6-4-23-adopted.md | Accept scoped receipt; N4/N14 used, N6 received without import. |
| P02 | 20261103-GEN-v2-10-adopted.md | Accept; matched factor scopes and companion pointer, no imported OFN claim inferred. |
| P03 | 20261103-TRIAD-v1-7-adopted.md | Accept scoped; interface constraint and real carrier, split pin with §6.18 boundary. |
| P04 | 20261104-PROG-v1-4-adopted.md | Accept; six interface roles, IF03 later update Programme-owned. |
| P05 | 20261104-RECOG-v0-3-27-adopted.md | Accept with change; D5B only at supported scope, R9 retained where required. |
| P06 | 20261111-DYAD-v6-4-24-adopted.md | Accept; matched pins and reference-map label, conditional OPEN21 companion. |
| P07 | 20261112-TDRG-v2-12-15-adopted.md | Accept with change; token-sum answer and corrected STAR/CONV-TICK scope. |
| P08 | 20261116-TDRG-v2-13-adopted.md | Accept with change; Finding A statement use distinguished from open custody. |
| P09 | 20261119-DZT-v0-18-adopted.md | Accept with change; current diagnostic reference homes DZT v0.19/AZ v0.10. |
| P10 (late; proposed) | 20261124-NUMGEN-v1-22-adopted.md | Accept scoped receipt: REQ-O09-03 fulfilled; L-BACKBONE typing; N-1A2 vocabulary only; NG-7A reference-only; proof pins retained. Separate from P2. Co-owner confirmation pending. |

The three previously closed items stay closed and are not reopened. After an adopted tag, record the nine agreed dispositions and, subject to receiving review of P10, the tenth disposition; regenerate/check the index in the appropriate receiving transaction. Review outgoing notices to DYAD, GEN, TRIAD, TDR-G, RECOG, Programme, DZT, AZ, NUMGEN and, if affected by the attribution clarification, RRF. No notice in this list has been prepared as a pipe item, sent, accepted or adopted by a consumer in this build. A separate S-P4 finding to FMS belongs to its own evidence/owner process, not a prerequisite for this maintenance edition.

## 6. Remaining obligations and approval boundary

[OPEN] Full historical GEN v2.8.5 claim comparison, historical DYAD proof-source comparisons where not performed, incomplete recovered-source authentication, universal FMS P4 prerequisites and separate finding, six-constraint list and physical selection questions remain open at their stated scopes. Finding A custody awaits an actual joint decision. PR #183 remains separate. LIT dependencies: none.

**Requested reviews:** other OFN co-owner — round-2 native replay and E1393 delta, N2/P10 scoped receipt and record changes (all 145 edits covered by round-1 review); Atlas — change-focused registry/interface impact and release-record consistency. Do not require unchanged expensive scientific campaigns to be repeated without cause.

**PI_PENDING:** after those reviews, decide whether to adopt the exact DRAFT hash (or require revisions). Only an explicitly authorized adoption may produce the publication-status transform, final digest, BASELINE update, merge and adopted tag. Then perform the receiving closures and notices. This record is draft, not an adoption/release decision.
