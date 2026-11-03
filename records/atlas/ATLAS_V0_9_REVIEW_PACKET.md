# RTG State Atlas v0.9 — change-focused review packet

**Date:** 3 November 2026. **Prepared by:** Claude, Atlas owner.
**Status:** DRAFT / NONCANONICAL. This is a candidate for receiving review by ChatGPT (Atlas co-owner). It has no PI acceptance and adopts no owner science. `atlas-v0.8` governs until acceptance.
**Scope decision:** PI, 3 November 2026 ("Evet başlayalım"). The edition is one change-focused refresh carrying the three sources that moved since `atlas-v0.8`. It follows the ChatGPT TRIAD v1.7 preparation note and the Atlas owner's additions to it. There is no general compaction and no Methodology migration of the atlas.

## 1. Inputs and identities

**Base:** `atlas-v0.8`, SHA-256 `47320ca55f25955ff0d5e73be690465c7f9e6ebad9fa6bbc09692d4cf86371b7`; tag object `8fb11cd5…`, commit `e7a3a0ada19ca687d598b31a3a41b93ee89e3843`.

**Source snapshot:** `origin/main` `f20f080`, after PR #145 (TRIAD v1.7 post-tag records and notices).

**Three sources moved:**

| Source | Tag | Tag object | Commit | File SHA-256 | Release record |
|---|---|---|---|---|---|
| Dyadic v6.4.23 | `dyad-v6.4.23` | `e32abf02…c343` | `ab8749b2a48d5d26082c5e5b16d5ef72298bcec3` | `9f874ccc1cd684482f26a27fca13b37102977cba2a80a75e762ecd7b300425cb` | `records/dyad/RTG_DYADIC_v6_4_23_RELEASE_RECORD.md`; post-tag `records/dyad/DYAD_v6_4_23_POST_TAG.md` |
| Ontological Foundations v0.12 | `ofn-v0.12` | `b313064f…7a3b` | `2b2573f59244851455cba16a2baa79c76cc8ec66` | `55ff8ba85d4bb48b52266bdd9a44aa84efcd2cc19903d059266fa406a6bb76aa` | `records/ofn/OFN_v0_12_RELEASE_RECORD.md` |
| Triadic v1.7 | `triad-v1.7` | `ed7da56f…06fa` | `7568941d3d30a9091af2b63a28be9abf5d916d8a` | `506f3403628ca01d5a904f885df055d9bfbdf1ef5e474e24e83d4797c122e64a` | `records/triad/TRIAD_v1_7_RELEASE_RECORD.md`; post-tag `records/triad/TRIAD_v1_7_POST_TAG.md` |

For each moved source the builder asserts four things: the file hash at the tag, the resolved tag commit, equality with the snapshot bytes, and the published hash given in the release record.

The other 15 sources are byte-equal to their v0.8 inputs. The manifest field `v0_8_input_equality` records 15 EQUAL and 3 CHANGED, and the CHANGED set is exactly {DYAD, OFN, TRIAD}.

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md` (candidate) | `c7f678edb5f2ea6c0ab58651ce3f6f97f5e2f816bcc3b07c6411d43f4429ae3a` (517,717 bytes, 1,547 lines, counted as in v0.8) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/build/refresh_v0_9.py` | `fdbf8d206f565c1ea0c98ba5c7ce8f535780cf157cd8cdad0e3e511a5e854a23` |
| `evidence/atlas/v0.9/source_manifest.json` | `d9e84879deb2f34b63f6f4812b770e5e263aa110238397231bf8ec6d2f6009c3` |
| `evidence/atlas/v0.9/edit_log.json` (44 operations) | `904ca0f0be1090ad219ec957f83e357e03c0964789967d0a3910678337f81a3d` |
| `evidence/atlas/v0.9/dispositions.json` | `5245a4f342e47627b5863742db10a0fdf6297ac1d97965093671e57dca08716a` |
| `tools/atlas_check.py` (one self-test line changed, §3) | `2141e0b991f21acfa2c4f2e0575e88d3ae5d1f43bffd00dafc4ef80d66f66373` (was `0db3a23b…004d`) |

**Decision basis:**
- **DYAD:** the release record (§2 D1–D7, §4 follow-ups for the Atlas), the notice `pipes/ATLAS/20261030-DYAD-v6-4-23-adopted.md`, and the v6.4.23 text at the tag: §6.8 (L600–602), §6.14 (L797–804, L906–910) and §8 (L1171–1172).
- **OFN:** the release record (§1 PI decisions: one new RID, no 3B standard and no isolation contract selected; §3 the edit groups) and the v0.12 text at the tag (§2.4, §5.5.4, §9).
- **TRIAD:**
  - the release record and post-tag read-back, with the notice `pipes/ATLAS/20261103-TRIAD-v1-7-adopted.md`;
  - the two 29-row checks `records/atlas/ATLAS_TRIAD_v1_7_29_ROW_CHECK_OWNER.md` and `…_CHATGPT.md`;
  - the ChatGPT preparation note (relayed by the PI, 3 November 2026);
  - the v1.7 text at the tag. It differs from the reviewed candidate `2573961a…5c0d` only in its adoption-state lines (header status, supersedes, records, §9 edition line, Appendix A heading, footer).

## 2. Review scope

This is an impact refresh of three domains: 44 exact-once operations, listed in `evidence/atlas/v0.9/edit_log.json`. No other domain was re-extracted. The diff against the base is 44 insertions and 37 deletions.

**DYAD v6.4.23 (D2, H5, D3 cross-notes).**
- **Source row and D2 header.**
- **New nodes:**
  - `DYAD-THM-OPEN18-STEP-MONOTONE`: the step-indexed statement, with q₃/₄ isolated in G and Θ₄(q₃/₄)=−π/3. The labels Γ₃, Γ₄ are a presentation convention, and q₃/₄ is not NUMGEN's q_*.
  - `DYAD-THM-NF-REM-C7-SHARP`: C₇=85.1 / 27.7, with the NF-REM inputs unchanged.
  - `DYAD-THM-LPHASE-ROWA-BRIDGE`: the exact decomposition, c_Q=0.79246 and c′_Q=0.36916.

  The historical `DYAD-THM-OPEN18` keeps its line, with the owner's historical-formulation scope.
- **[COR] decimals carried:**
  - the NF-REM bracket values are now the certificate's upper bounds rounded up: 85.0732, 812.894 and 27.6023 (216.77 unchanged);
  - the L-PHASE outline uses 1.51633, 1.06253 and 1.61115, with 403/250 unchanged;
  - the `NUMGEN.N-A + DYAD.X10` check value becomes 1.61115.
- **q\*.** `*NUMGEN:qstar-witness` is typed as a different number from q₃/₄. `NUMGEN.N-Q*` is retired; the question item is closed by DYAD as accept with change.
- **RECOG.R-A1** is reworded. Both registrations are recorded, and the 0.36915 assumed by RECOG lies below the certified majorant 0.3691523…. RECOG keeps `[assuming:]` until its own re-check; the DYAD notice to RECOG is open.
- **Cross-notes.** Two RECOG nodes (`RECOG-THM-R9-MEMORY` sharpened rows, `RECOG-ALG-A1C-LOGFREE-ENVELOPE`) get a parenthetical naming the registered Dyadic row outside their `[assuming:]` brackets. RECOG's text is not changed.
- **H5** says that Dyadic registered both, and that RECOG's blocks stay conditional until RECOG re-checks.

**OFN v0.12 (D1).**
- **D1 header counts:** 5 local RESULT RIDs, 44 OFN RIDs. The builder counts 44 at the tag.
- **New node `RTG-OFN-ALG-REF-CLOSURE-COMPARISON`, (i)–(iv).** Its scope and "not covered" list are as stated by the owner. Its consumer is the TRIAD T-6r C1 interface constraint.
- **`*OFN:causal-interface`.** This records the identity F_e−N(z_e)=−(κ/3)(N(z_e)+b_e), recorded under the §5.5.4 `[ALG]` list. It is not registered and has no RID.
- **`RTG-OFN-OPEN-REF-CLOSURE`** is narrowed to the physical reading.
- **P2A/3A** gets the v0.12 next-artifact pointer.
- **P2B-CRITERION** gets the 3B evaluation frame: U-form, U-class, C0, C1, J, and candidate standards (a)–(c). No standard is selected.
- **TRIAD-CLASS** gets the isolation frame: I-comp, I-quiet, I-remove. None is selected.

**TRIAD v1.7 (D4a; D1.L5 PROG.G9).**
- **Source row and D4a header.**
- **Models line:** the two root-equivalent off-root extensions (a) literal and (b) Q_c-free, fixed only by T-6r C3; time is the coefficient-ODE time in six-step-block units.
- **T-6e:** the Gram relation is typed as the degree-3 first variation of Δ𝒢≡0. The degree-4 finite-increment terms are named, and it is not an exact discrete law. The RID is kept.
- **Tangency node:**
  - f_s, f_c per extension;
  - the D remark — (b) Ḋ=0, (a) Ḋ=rq₁D — with no RID, not a physical mode, and not a statement about the six-step map;
  - an `atlas-checked exact` entry from the Atlas row check.
- **T-6l:** the coercive bound 6(√3−1)K≤A_θ^corr≤6(√3+1)K. It is the leading coefficient only, with no persistence without a remainder.
- **T-6u:** the 𝒫₄ identity keeps its gen-v2.8.7 pin (F30).
- **96:1:** the metric-dictionary caveat (hypothetical 192). The single statement stays in TRIAD §1.
- **Export node:** points to the §7.4 consumer matrix. A v1.6 receipt is not acceptance of a later delta; Programme CN-05 is not recorded, RRF is convention-only, OFN reference-only, GEN `[CAND]`.
- **Frontier:** the T-6r acceptance contract C1–C6, and the T-6q coordinate sign table with its bookkeeping label and the open complete-state action.
- **L5:**
  - F11, F13 and F14 are reworded: the metric caveat, the RID state at gen-v2.9, and custody (`accepted_r4_2/` held by the PI; H₁, H₂ missing; T-6c2 and T-6l recovered).
  - F20 (+ TRIAD.T9) is retired.
  - New: F30 (the two Genesis questions, pipes open), F31 (GEN imports T-6s/t/u at `[CAND]`), F32 (owner-recorded form debt F-1, F-2, A-1, row 29) and PROG.G9 (Programme IF07/IF11 at v1.6, no CN-05 record).

**Pipes (NUMGEN.N-I1).** The atlas owner sets its own three inbox items on this branch:
- the TRIAD row-check request is `closed` (accept; the two 29-row checks);
- the DYAD and TRIAD notices are `dispositioned` (accept; this packet). They are closed after the tag.

The row then states 53 items in 20 inboxes: 15 closed, 5 dispositioned, 33 open. The builder asserts both the snapshot counts (14/3/36) and the branch counts (15/5/33). `tools/pipes_index.py --check` passes, and `pipes/ATLAS/INDEX.md` is regenerated.

**Not changed on purpose:**
- **Consumer pins.** Consumers' own pins to `dyad-v6.4.22` stay as they are, because they are the consumers' records: OFN IMP-O08-12/20; RECOG; NUMGEN §6.6; GEN G-20; IF16.
- **OFN v0.11 phrasing.** Sentences of the form "OFN v0.11 consumes / states …" (H1, H8, RRF.F5, OFN.O11) describe statements that are unchanged at v0.12.
- **F18** is retained: TRIAD v1.7 §7.2 keeps the same RER citation.
- **The T-6s/t/u nodes** are unchanged; their content is unchanged in v1.7.
- **The TDR-G T3 ladder line** names "TRIAD v1.6.1 wedge / x\*" as TDR-G's own historical reference.
- **`*ATLAS:checked-D2`** keeps its dated v0.1 record ("1.51632·1.06252 … ≈1.61112"), as evidence as then read.

## 3. Mechanical checks

**Build.** Two builds in separate processes give identical bytes for the atlas and for all ten evidence files. To reproduce, run `python3 -I evidence/atlas/build/refresh_v0_9.py` from the repository root. It needs this branch's three pipe-state edits in the working tree.

**Shared checker:** zero FAIL. The CLI run with the v0.9 manifest and retired keys exits 0.

| check | PASS | UNVERIFIED | DOCUMENTED-UNRESOLVED | WARN |
|---|---|---|---|---|
| sources | 72 | | | |
| coverage | 132 | | | |
| qualifiers | 3 | | | |
| links | 495 | 5 | 11 | |
| artifacts | 109 | 3 | | |
| keys | 128 | | | |
| process | | | | |
| wording | | | | 13 |

The UNVERIFIED and DOCUMENTED-UNRESOLVED rows are the same items as in v0.8, with line numbers shifted. The 13 wording WARN are the v0.8 ones less the F20 line; the new text adds none.

**Tool change.** In `tools/atlas_check.py`, self-test NC7 mutated the literal source-table row `| v6.4.22 | \`dyad-v6.4.22\``. With DYAD at v6.4.23 the mutation became a no-op and the control reported "not as expected". It now mutates the DYAD row of any edition (one line, regex). The check logic is unchanged, and the self-test runs 18/18.

**H→L5 map:** no dangling key, no high row without an H, 120 L5 rows.

**Retired keys:** NUMGEN.N-Q\*, F20 and TRIAD.T9 (and their space-written forms). The builder asserts that none occurs in the candidate. The reasons are in `retired_l5_keys.json` and `dispositions.json`.

**Dispositions:** 3 retired, 6 reworded, 9 retained, 4 new.

**Negative controls:** shared 18/18 and focused 12/12.

| ID | Mutation | Caught by |
|---|---|---|
| U1 | H5 cites NUMGEN.N-Q\* | H→L5 dangling |
| U2 | F20 reused | `keys` FAIL |
| U3 | TRIAD source row reset to v1.6.1 | `sources` FAIL / stale guard |
| U4 | new DYAD RID misspelled | `links` FAIL |
| U5 | 1.61112 reintroduced in the L-PHASE node | stale guard |
| U6 | c′_Q=0.36915 written as the registered constant | scope guard |
| U7 | D claimed constant in extension (a) | scope guard |
| U8 | Gram relation typed as an exact six-step law | scope guard |
| U9 | new OFN RID misspelled | `links` FAIL |
| U10 | T-6r C3 dropped | scope guard |
| U11 | "consumer acceptance pending" reintroduced | stale guard |
| U12 | isolation contract shown as selected | scope guard |

**Fidelity checks** were done by hand against the tagged files, not by the checker. Each is `EV-SRC-READ`.
- **DYAD:**
  - L602: the step-indexed statement, the intervals, the q₃/₄ enclosure, the "presentation convention" scope and η₆(q₃/₄)−q₃/₄≈−0.5537.
  - L799–804: the NF-REM table, the [COR], C₇=85.1/27.7 and the exact bounds.
  - L906–910: the outline decimals 1.51633, 1.06253, 1.61115, the [COR], and c_Q, c′_Q with the exact values.
  - L1171–1172: DYAD-ART-OPEN18 and DYAD-ART-INBOX-20261030.
- **OFN:** §2.4 [HYP] and the result (i)–(iv) with its scope; the §5.5.4 causal-interface bullet; the §9 REF-CLOSURE question, closure criterion and next artifact; the 3A pointer; the 3B frame; the TRIAD-CLASS isolation frame.
- **TRIAD:**
  - L34: the 96:1 single statement.
  - L148–162: T-6r and C1–C6.
  - L172–180: the T-6q table.
  - L489–497: the coercive bound.
  - L758–766: the Gram typing, the extensions and the D remark.
  - L814 and L823: the held 𝒫₄ pin.
  - L848–861: the §7.4 matrix and notes.
  - L15: custody.
- **Genesis (for F30, F31):**
  - At `gen-v2.9`: L80 (§1), L419 (§2), L987 (§6.6) and L1246 for the birth-symmetry grade.
  - L250 and L1243: only the c-mode 2cᵀBG₃,c identity is printed.
  - L232, L243, L360 (§2): the `[CAND]` imports.
- **Programme (for PROG.G9):** `programme-v1.3` §7.2 IF07 and IF11 at v1.6.

**RID presence:** the four new DYAD RIDs and the one new OFN RID are each declared at their tags and named in the candidate. The TRIAD RID set at `triad-v1.7` equals the set at `triad-v1.6.1` (46).

**Earlier evidence used.** The Atlas row check of 2 November 2026 hand-checked the TRIAD row-1 algebra and reran both owner row-1–3 scripts (PASS, byte-identical outputs). No owner certificate is rerun for this edition.

## 4. Questions for receiving review

1. **Retirement of NUMGEN.N-Q\*.** Is the retirement right, given that NUMGEN still defers the cross-citation (v1.21 NC-17) and its DYAD notice is open? The atlas keeps the NUMGEN-side note at the witness node instead of an L5 row.
2. **RECOG cross-notes.** Are the parentheticals placed outside RECOG's `[assuming:]` brackets an acceptable way to show the registered Dyadic rows without editing RECOG's statement?
3. **`*OFN:causal-interface` as a separate node.** The atlas made the identity its own node instead of folding it into CLASS-C. Is that the right home? OFN records it under an existing `[ALG]` list, not as a registered result.
4. **F30 and F31.** F30 and F31 are typed D-PIN/D-GRADE and D-GRADE with TRIAD co-keys. Would GEN co-keys (GEN.D-series) be the better home, given that the receiver is Genesis?
5. **F32.** Should the TRIAD form debt sit in L5 at all, or only in the TRIAD release record?

## 5. Publication boundary

This packet adopts nothing and changes no owner file.

The order after review is:
1. Receiving review, with revisions if needed.
2. PI acceptance.
3. Release record `records/atlas/RTG_STATE_ATLAS_v0.9_RELEASE_RECORD.md`.
4. Merge commit (not squash).
5. Annotated tag `atlas-v0.9`.
6. Tag verification.
7. Closing the two dispositioned ATLAS inbox items.
