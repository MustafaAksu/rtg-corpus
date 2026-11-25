# Session orientation reporter — ChatGPT receiving review

**Checked:** 9 November 2026, round 3.  
**Status:** [SESSION] independent receiving review; not pilot acceptance, scientific adoption or merge authority.  
**PR #190 verdict: ACCEPT SCOPED — no remaining blocker in O190-R1–R4 for the identified revision.**  
**PR #191 verdict: ACCEPT SCOPED at `404bfb6`; its two cleanup notes remain resolved.**

This is the current working review. Earlier rounds remain at the same path in Git: round 1 at `2ec275bf8e4dfec0198ea351ef37f6e99edbe1d3`, round 2 at `06adf9a7476b3059784556ee7191200c061ba4b6`. Their harnesses and recorded outputs are unchanged. This revision supersedes the prior REVISE decision for the specific reporter bytes below; it does not erase earlier counterexamples.

## 1. Exact object and reading extent

- Reporter: PR #190, `claude/tool-orient`, head **`34e55078fcce6041169ee2cab624eef55600b202`**; `tools/orient.py`, **14,135 bytes**; SHA-256 **`dfbcb1da0a7ac4d3ec942cae4a125875caa1030ddebd103821bf5c75b0c5cd0c`**, Git blob **`6848b4f0c15713f6063be797a396f066f4dafa06`**. Both identities were recomputed from the actual source transferred into the test environment and matched GitHub/source identity. The reporter was not modified for execution.
- Read the full revision-3 reporter, the round-2 receiving requirements and complete executable runner, the producer's revision-3 README, current PR #190/#191/#192 metadata and CONVENTIONS §§2–7. The substantive delta reviewed is the remaining R1/R2/R4 correction batch; R3 was already discharged and its regression cases were retained.
- PR #191 is still the separately reviewed `404bfb6da26bea100208b02be2fa07e096001f27`, targeting `chatgpt/atlas-session-orientation-pilot`, not `main`. Content acceptance is separate from its current mergeability against a moving pilot base.

## 2. Executed verification — original contracts unchanged

**[EV-BYTES / EV-HASH / EV-RUN] Python 3.13.5.** Executed the unchanged reporter through the existing offline receiving harness. Only Git/GitHub subprocess responses are deterministic fixtures; reporter argument parsing, matching, uncertainty propagation, rendering and JSON output are actual source execution. Filesystem tests use temporary directories. No production source, pipe, ref or tag is touched.

**Results: original 21/21 PASS; existing boundary cases 6/6 PASS; zero failures; exit 0.** The previous four failures in the six-case suite are now PASS. No fixture, test predicate, expected PR set or acceptance condition was relaxed or replaced.

The new thin runner `check_orient_round3.py` first hash-checks the unchanged `check_orient_round2.py`, then changes only `TOOL_SHA` and `TOOL_BLOB` in memory. That round-2 runner in turn hash-checks the original 21-contract harness and repins its two target constants in memory. This is an independently executed replay of the same Python fixtures, not a new implementation of the reporter or a live GitHub test.

| Durable evidence | SHA-256 |
|---|---|
| `evidence/atlas/tools/orient_receiving/test_orient_receiving.py` (unchanged) | `f585abf7f23ebcbabcd2621795ffebb3dc7625e62ed636e6ad9af8c970762681` |
| `evidence/atlas/tools/orient_receiving/check_orient_round2.py` (unchanged) | `14ca8cb3f32c7d5fb09e926e97187c463c43f947ac85ac09e5f6193029e4cc7e` |
| `evidence/atlas/tools/orient_receiving/check_orient_round3.py` (pin-only runner) | `1de46f1e5fca925348afd76d939a4e692cbfa34c9a0979384f898659fb629dd6` |
| `evidence/atlas/tools/orient_receiving/round3_output.txt` (actual stdout) | `5cbdbc2fc2bdd4beaf99213e44d022e4c3872eea33b5d6f60be6dd645b4aff68` |

Reproduce from the receiving-review branch, or after it is merged:

```bash
target=$(mktemp)
out=$(mktemp -d)
git show 34e55078fcce6041169ee2cab624eef55600b202:tools/orient.py > "$target"
python3 -I evidence/atlas/tools/orient_receiving/check_orient_round3.py \
  --tool "$target" --out "$out"
# Expected: baseline 21/21 PASS; additional 6/6 PASS; exit 0.
# Reused runner writes concrete observations to "$out/round2_summary.json".
```

The per-case observations and large baseline call lists are reproducible from these pinned scripts; they need not be duplicated in Git for every replay. The producer's live ATLAS/GEN observations remain **EV-SRC-REPORTED / EV-NOT-RERUN** by this reviewer. No fresh ChatGPT or Claude-project blind session has been run here.

## 3. Disposition of R1–R4

| Contract | Verdict | Executed/read-back result |
|---|---|---|
| **R1 — incomplete observations** | **PASS SCOPED** | The original tree-read failure still yields null pipe collections. An enumerated item that cannot be read is now named in `pipes.unreadable`, with `pipes.complete=false`; the rendered counts are explicitly INCOMPLETE lower bounds rather than `inbox: none`. The overall report remains PARTIAL/UNVERIFIED. Original access, JSON, missing Status/hash and freshness controls also pass. |
| **R2 — release-version identity** | **PASS SCOPED** | Whole numeric dot/underscore version tokens are normalized and compared for equality. A v0.10 tag does not select v0.100 or v0.10.1; the exact v0.10 record alongside v0.10.1 is unambiguous; v0_10 remains supported; two actual same-version record representations remain ambiguous. Candidate/release sorting does not raise the original mixed-type exception. This is source matching, not an automated adoption decision. |
| **R3 — PR discovery** | **PASS SCOPED, regression retained** | Renamed-away paths, same-repository PR URLs, paginated discovery and both API orderings of the 201→200→113 graph still pass. The tested relevant PR membership is order-independent. An observed reference remains a discovery relation, not proof of scientific dependency or acceptance. |
| **R4 — intentional report output** | **PASS SCOPED** | Default output uses exclusive creation, retains the existing-file protection and refuses the tested dangling symlink without creating its target. The link itself remains intact. Source inspection confirms the explicit symlink check and O_NOFOLLOW where available. Optional `--replace-json` is an intentional overwrite mode for a report owned by the caller; it must not be pointed at scientific/evidence source files. Stdout remains the read-only default. |

The four earlier boundary failures are concretely closed: R2-E1/E2 use only the correct record; R1-E1 has an unreadable-item list and incomplete flag; R4-E1 reports no source-target creation. The two positive boundary controls remain PASS.

## 4. Scoped limitations, not new blockers

- This finite suite covers the agreed R1–R4 counterexamples and regressions, not every malformed payload, concurrent GitHub mutation, version naming policy or adversarial filesystem arrangement. It is not a universal security certification.
- The reporter observes the newest local tag and release-record evidence. Humans still verify the governing adopted edition; a matching hash, Status string or COMPLETE observation is not adoption.
- JSON output is the explicit write exception. Refusal to write a requested destination and a complete repository observation are distinct outcomes; the stdout must be read. Use fresh temporary report destinations for the pilot. No cross-platform hostile-parent-directory or hard-link security claim was tested.
- The PR #190 description still includes first-revision examples and the overbroad phrase that the tool never writes. Before merge, align that description with revision 3 and its explicit optional JSON-write exception. This is nonblocking metadata cleanup, not another code-review round.

## 5. Owner lane, pilot and next step

**PR #191 remains ACCEPT SCOPED** for integration into the #188 pilot branch. Its stale unfilled-lane sentence and fixed-four-PR test criterion were already corrected; the current head is unchanged. If its base has advanced, refresh it through a normal merge/follow-up commit preserving both lanes, not a force-push. Content acceptance is not a claim that GitHub currently reports it mergeable.

**No additional reporter correction cycle is requested.** The PI may now consider merging #190 and this review/evidence PR #192 into `main`, and #191 into its named pilot base. No merge or tag is performed by this review.

After those integrations, freeze the actual reporter commit/hash, repository refs and captured PR responses for the answer key **before** either blind test. Do not retain a historical count of four or seven relevant PRs as the live expected answer: merges change that set. Keep frozen-fixture scoring separate from live-discovery scoring. Run fresh ChatGPT and Claude-project sessions; this returning reviewer session is not blind. #188 remains gated on that pilot evaluation; #189 stays deferred. No scientific-owner edition, Methodology migration or new release tag is implied.
