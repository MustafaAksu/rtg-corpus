# RTG State Atlas v0.11 — acceptance record (draft)

**Status:** CANDIDATE, 10 November 2026. Receiving review complete (§3); PI acceptance not yet given. `atlas-v0.10` stays the governing tagged Atlas until the PI accepts, the PR is merged and the tag `atlas-v0.11` exists and is verified.
**Object:** a derived, NONCANONICAL Atlas. Acceptance adopts no owner science.
**Recorded by:** Claude, Atlas owner, on branch `claude/atlas-v0.11-d3-pilot` (PR #204). Under CONVENTIONS §4 this record comes before the merge and the tag.

## 1. Object

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md`, v0.11 candidate | `8d7a43f05a42c6a69b50eb97b98dd96ddda7eea327333ae5cc73e03dee46f358` (520,271 bytes, 1,542 newline-terminated lines) |
| base `atlas-v0.10` | `443b5990e6082599d1f43fca7d4d24e512e7a632ec395aa56f05bed16f53dbf7` (521,243 bytes) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged, v0.2) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.11/source_manifest.json` | `2773f774169448dcb79c0a4b91f3ffb97b0eec80a3331c156203c2749d072b90` |
| `evidence/atlas/v0.11/build_v0_11.py` | `fe57dd68a22b9355abe80a38482cec2508f4eb24149f76dcca79bf45e17fd70f` |
| `evidence/atlas/v0.11_pilot/build_stage1.py` | `b1f1569b08fabf98b4b875323e8dc44efd5e4e64dc1ca858588cfd1074c72615` |
| `evidence/atlas/v0.11_pilot/stage2a/build_stage2a.py` | `dac25a8ab69625b8459ece5eff49bb294a60f10fbe8ad3a3869a3f28c5ba59a0` |
| `evidence/atlas/v0.11_pilot/stage2b/build_stage2b.py` | `00fa70acd94d4c1b605d1494b2232a877f48ec50627f8bc7294f5cfcbb94f427` |
| `tools/atlas_preservation.py` (rev. 3) | `6a4047b0dd3e10e15feeb9262d8b09816e82fa2f85a6d7ce939cc69d580e1d62` |
| `tools/atlas_check.py` (unchanged since v0.9) | `2141e0b991f21acfa2c4f2e0575e88d3ae5d1f43bffd00dafc4ef80d66f66373` |

**The chain.** Each step is built by a script that asserts the hash of its input.

| Step | Output SHA-256 | Bytes | Content | Review |
|---|---|---|---|---|
| `atlas-v0.10` | `443b5990…dbf7` | 521,243 | base | — |
| stage 1 | `0f8ba5c0…a6c2` | 521,832 | six scientific identifiers with two record lines: the second home becomes a typed cross-reference (Method §4.4) | PR #204 reviews 5839419629, 5840025491: accepted |
| stage 2a | `ace0b408…a5d6` | 519,983 | D3: 21 span deletions, owner-edition labels (§4.1) and method detail beyond a pointer (§4.7) | review 5841129271: ACCEPT SCOPED |
| stage 2b | `66f0b2eb…20da` | 520,271 | D3: three stale `(D5)` `[assuming:]` tags replaced by the import of `recog-v0.3.27` | review 5841306614: accepted |
| v0.11 | `8d7a43f0…f358` | 520,271 | three self-version edits: title (L1), manifest path (L4), end line (L1542) | review 5841306614: accepted |

**Against v0.10:** 23 lines differ (1, 4, 373, 392, 419, 420, 462, 667, 668, 718, 725, 726, 736, 738, 739, 740, 752, 753, 774, 776, 823, 1351, 1542); the other 1,519 are byte-identical; no line is added or removed. Net −972 bytes.

## 2. Basis and limits

**Basis:** Method v0.2; the stage records `records/atlas/ATLAS_V0_11_D3_PILOT_STAGE1_DISPOSITIONS.md` and `records/atlas/ATLAS_V0_11_D3_PILOT_STAGE2_RESULT.md`; the files under `evidence/atlas/v0.11_pilot/` and `evidence/atlas/v0.11/`.

**No source moved.** The source snapshot is that of v0.10, `main` `fa3db80a935a20b1eff64b0e14c6d0436f861852`; the v0.11 manifest copies all 18 source entries unchanged. On 10 November 2026 all 18 source tags were still the newest tags of their studies. This edition is therefore not a refresh: no source was re-extracted, no L5 disposition pass was run, and the pipe census of v0.10 is not recounted.

**Checks.**
- Comparator (`atlas_preservation.py`), per stage: MECHANICAL PASS with 0 FAIL at each of stage 1 (12 pending, 7 mapped, 2 context reviews), stage 2a (15 pending) and stage 2b (3 pending). MECHANICAL PASS is not semantic equivalence; the pending items are what the reviews read.
- `tools/atlas_check.py --manifest evidence/atlas/v0.11/source_manifest.json` on the candidate: 0 FAIL — sources 72, coverage 132, qualifiers 3, links 499 PASS / 5 UNVERIFIED / 11 documented-unresolved, artifacts 110 / 3 UNVERIFIED, keys 31, wording 12 WARN; the same counts as v0.10 (`evidence/atlas/v0.11/atlas_check_report.md`).
- Every builder rerun reproduced its committed output byte for byte.

**Limits.**
- The comparator was not run across the self-version step or across the whole chain in one map. A changed title heading changes the recorded heading context of every region, so the tool reports the whole file; that step is checked by a plain line diff instead (exactly three lines). This is a limitation of the tool, recorded here, not worked around.
- The checks are structural. No owner certificate was rerun.
- The `(D5)` correction was read against the owner text at `recog-v0.3.27` (DSN lines 43, 180, 764, 1056 and Appendix A v0.3.27); it changes source conditions as the owner did, no result and no grade.
- Seven other identifiers with more than one record line (five `*GEN:`/`*NUMGEN:` pseudo records, two `GEN-ART-` rows) are untouched: a recorded, deferred debt.
- K1/K2 were applied to D3 only. In the other domains the labelled material is under 0.5 % of the file (stage-2 record §11) and is left for the refresh in which a domain is next opened.

## 3. Decision

**PI direction (project conversation, 10 November 2026).**
- 14:02 +03:00, route A: keep the structure; shrink only as far as the Method's own rules reach (stage-2 record §8).
- 14:40 +03:00, on closing: "değmez. burada kapatalım. umudum tüm diğer alt başlıkları /stream leri elden geçirdikten sonra (Mesela AZ felan) içeriğin biraz daha toparlanması o zaman bakarız." ("Not worth it. Let us close here. My hope is that once all the other sub-headings/streams have been gone through (AZ, for example) the content will come together somewhat more; we look at it then.")

This closes the compaction work and directs that the pilot's content become v0.11. It is not yet the acceptance of the object in §1, which waits for the review below.

**Receiving review.** ChatGPT, Atlas co-owner: stage 1 and stage 2a accepted (reviews above). **Final review, PR #204 review 5841306614, on commit `8cd20d1a0ec3af869df050014c9a4bced20d2394`: ACCEPT SCOPED — PI adoption ready.** The reviewer recomputed independently: the candidate hash and size; exactly 23 changed lines against v0.10, none added or removed; stage 2a → 2b only L736, L740, L823; stage 2b → v0.11 only L1, L4, L1542; the manifest hash, with 18/18 source entries byte-equal to v0.10 and only `atlas`, `frozen_at`, `previous_atlas_tag`, `note` changed. The three stage-2b items were read against `recog-v0.3.27` (§2 R6, §6.13b, §6.16e) and accepted; grades, domains and OPEN states unchanged; START-OFFSET (ii) needs no correction. Not rerun by the reviewer: `atlas_check.py`, the builders, owner certificates. The 5 UNVERIFIED links, 3 UNVERIFIED artifacts and 11 documented-unresolved links are those of v0.10 and were not counted as new blockers.

**PI acceptance:** not yet given. It is recorded here verbatim when given, with the object hash it refers to.

## 4. Publication (after acceptance; the PI executes)

1. `BASELINE.md`: the owner sets the ATLAS row to v0.11, the hash of §1 and this record, in PR #204 before the merge.
2. Merge PR #204 into `main` with a merge commit, not squash.
3. Create and push the annotated tag `atlas-v0.11` on that merge commit, after checking that the file hash at `main` is `8d7a43f0…f358`.
4. After the tag the Atlas owner writes the tag-verification record.

The CLI block is issued with the acceptance. A merge, a tag or a passing check is not an adoption.

## 5. Carried forward

- Everything in §5 of `records/atlas/RTG_STATE_ATLAS_v0.10_RELEASE_RECORD.md`, unchanged (TRIAD, GEN, DYAD, TDR-G, Programme items; the pipe items filed after `fa3db80`).
- **Size.** The file stays near 520 kB. The token figure of Method §4.6 is not reachable by compaction under "no fact is dropped for size"; restating it is a Method v0.3 delta, drafted and reviewed separately. The PI will look at size again after the remaining streams (AZ and others) have been reworked.
- **Standing rule proposed for Method v0.3:** K1 and K2 are applied in span-deletion form whenever a domain is opened for a refresh.
- **Advisory note to the PI** on dormant-owner findings (H2, H11, AZ.A1, H3): next owner action after this edition.
