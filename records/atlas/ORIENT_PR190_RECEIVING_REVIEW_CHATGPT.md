# Session orientation reporter — ChatGPT receiving review

**Date:** 9 November 2026.  
**Status:** [SESSION] independent receiving review; not pilot acceptance, scientific adoption or merge authority.  
**PR #190 verdict: REVISE — one batched correction pass before merge.**  
**PR #191 verdict: ACCEPT SCOPED for the owner-lane integration, with the two nonblocking editorial/test-plan notes in §5.** Approval of that stacked documentation change does not approve the reporter or the two-platform pilot.

## 1. Exact objects and reading extent

- PR #190: `claude/tool-orient`, head `029524acb3117fcfa46665412385dfbe36aba928`; `tools/orient.py`, 146 lines / 10,499 bytes; SHA-256 **`0a42698cdf50f71173a3ac930ad7e07498b8c204c5f0b9331e78171977f517bb`**; Git blob **`1365d748a18383746df00aaa97ee57414e2a79ef`**.
- PR #191: `claude/atlas-orientation-owner-lane`, head `e673840fbbf537c00a6852a95a655c2f7f9e780e`; base `chatgpt/atlas-session-orientation-pilot` at `dbbaad40a710650877d110bb40275b769ffaca64`, **not main**. Orientation file blob `b8de5e54097708d82ded1f988a8695dbbe74a07a`.
- Read the complete reporter, PR metadata, the producer's `atlas_run.json` and `atlas_run_github_denied.md`, the complete PR #191 file and diff, and current `CONVENTIONS.md`. The operational contract is the revised #188 design and owner review: changed-path/dependency discovery; tag is not adoption; incomplete observations are not empty work; read-only source observation.
- The new script is explicitly described as a new repository implementation superseding an uncommitted scratchpad prototype. This review does not claim byte equality with, or recovery of, that prototype.

## 2. Executed evidence and its boundary

**[EV-BYTES / EV-HASH]** Transferred the connector-fetched script into the execution environment and checked both its SHA-256 and Git blob identity. Both match the exact PR #190 source. The tool was not edited for testing.

**[EV-RUN / independent receiving harness]** Executed the unmodified source with Python 3.13.5. Only `subprocess.run` was replaced by deterministic Git/GitHub I/O fixtures; `main`, argument parsing, pagination, path selection, dependency expansion, record matching, report rendering and optional JSON file output are the actual original code. Filesystem writes were confined to temporary test files and the harness output directory. No production DSN, repository ref or pipe item was touched.

**Result: 21 receiving contract checks, 10 PASS and 11 FAIL.** These are reviewer-designed tests, not a reproduction of a claimed producer test suite. `P01–P10` pass; `N01–N11` fail. The harness exits 1 because the target violates those expectations. A test-fixture error in an initial development run was corrected before the recorded final execution; no tool source was changed.

Committed evidence:
- `evidence/atlas/tools/orient_receiving/test_orient_receiving.py` — SHA-256 `f585abf7f23ebcbabcd2621795ffebb3dc7625e62ed636e6ad9af8c970762681`.
- `evidence/atlas/tools/orient_receiving/round1_output.txt` — SHA-256 `871512784b5b42a56cb87efdf59e3d6f758a6434893673b7dc71ec98a926d432`.

Reproduce without touching a worktree source file:

```bash
target=$(mktemp)
out=$(mktemp -d)
git show 029524acb3117fcfa46665412385dfbe36aba928:tools/orient.py > "$target"
python3 -I evidence/atlas/tools/orient_receiving/test_orient_receiving.py --tool "$target" --out "$out"
# Expected current result: exit 1; 10/21 PASS, 11 FAIL. Details: "$out/results.json".
```

The producer's live GitHub sample and GEN run remain **source-reported**, not live runs by this reviewer. Runtime networking was unavailable; repository source reads used the connected GitHub tool. No blind replacement-session test on either platform has been performed. Tests do not certify every possible malformed response, adoption-record format or GitHub race.

## 3. What passes

The normal fixture finds the four relevant sample PRs (#113/#114/#188/#189), respects file paths, reads the record/hash without explicitly declaring adoption, and preserves the source sentinel. GitHub access denial, stale `origin/main`, unfetched remote tags, a missing record, and a failed PR file-list query are reported as partial. PR and file-list pagination both reach page 2; the 20-page cap is explicitly flagged. The inspected subprocess commands are reads (`git show`, `rev-parse`, `ls-tree`, `ls-remote`, `tag -l`, `cat-file -t`, `log`, and `gh api` GETs), not checkout/merge/tag-creation actions.

These passing cases support the design, but do not cover the following fail-closed gaps.

## 4. Required corrections — apply as one batch

### O190-R1 — incomplete data must remain incomplete at each field

Locations: `sh`/`gh_pages` L28–43; freshness L64–69; release evidence L83–93; pipe collection/rendering L116–126 and L141.

- **N01:** a failed `git ls-tree ... pipes/` produces a top-level PARTIAL report but renders **`inbox: none; outbound not closed: none`** and `{}` counters. The global warning does not make those empty-queue claims correct. Use null/UNVERIFIED or an explicitly incomplete count with a completeness flag; never conflate a failed enumeration with zero items. The same principle applies to partial PR-file discovery.
- **N02:** a record with the tag hash but no `**Status:**` gives `release_record_status_line = 'UNVERIFIED: no Status line'` while the overall status is **COMPLETE** and `unverified=[]`.
- **N03:** a record whose hash disagrees with the tagged file likewise yields **COMPLETE**. Report the mismatch in the structured uncertainty/errors list. This asks for evidence consistency, not for automated inference of scientific adoption.
- **N07:** a successful but empty remote-main response leaves `remote_main=None` and `local_is_current=None` yet reports **COMPLETE**.
- **N05:** a successful command returning malformed JSON raises `JSONDecodeError`; no structured partial observation survives. Validate response type/schema and preserve a failure report rather than a traceback-only result.

**Acceptance:** equivalent controlled failures yield explicit field-level incompleteness plus a consistent overall status; unavailable data never appears as an observed empty set. Catch parsing/command failures (including bounded subprocess timeouts) without inventing values. No scientific campaign is needed.

### O190-R2 — exact tag/record identity and robust tag parsing

Locations: `version_key` L50–51 and tag/record selection L72–93.

- **N04:** `atlas-v0.10` incorrectly selects `RTG_STATE_ATLAS_v0.100_RELEASE_RECORD.md` because the filename test uses substring membership. With equal test bytes the wrong version is reported with a matching hash and COMPLETE status. Match an exact version token, handle ambiguity, and keep the source record path/ref explicit; a hash merely occurring somewhere in a record is not in itself an adoption decision.
- **N06:** ordinary candidate/release tags `atlas-v0.10-r1` and `atlas-v0.10.1` crash sorting with `TypeError` (`str` versus `int`). Parse a documented tag grammar, or flag unsupported names without losing the report. Keep latest candidate and governing adopted evidence distinct; absence of adopted evidence is not permission to label a candidate governing.

**Acceptance:** exact-version and candidate-tag controls pass without selecting a different version's record, crashing, or asserting adoption. The reporter can remain observational and require human confirmation of adoption semantics.

### O190-R3 — PR discovery must be complete within its declared scope

Locations: path match L104–108 and reference pass L109–113.

- **N08:** a rename from `atlas/old.md` to `archive/retired.md` is omitted because only `filename` is inspected. Check `previous_filename` as well as the new path; removal/rename work is still relevant.
- **N09:** a dependency written as a full same-repository URL (`.../pull/113`) is missed; only `#113` is parsed. Support both forms, scoped to this repository, and distinguish an observed mention from a declared dependency.
- **N10/P10:** the same graph `201 -> 200 -> 113` returns `{113,200}` or `{113,200,201}` solely depending on API order. The matcher grows its seed set during one pass. Either implement a bounded fixed-point traversal, or explicitly define one-hop discovery against a frozen seed set; in either case the result must be order-independent. The supplied two tests use transitive closure as their declared expected scope; if the owner selects one hop, update both expectations and the documented coverage together rather than retaining order-dependent behavior.

**Acceptance:** rename, full-URL and order-permutation controls pass at the chosen documented traversal scope. Store full PR head SHAs and scan coverage where needed for the frozen answer key; mutable PR results are not frozen by a Git commit alone.

### O190-R4 — bound the intentional JSON write

Location: L143, `open(a.json, 'w', ...)`.

- **N11:** selecting an existing synthetic `atlas/RTG_STATE_ATLAS.md` as `--json` silently overwrites it with the report. This was demonstrated only on a temporary sentinel, not a production file. The command path has no repository/source-file or overwrite guard.
- Writing a newly requested report artifact is not itself a defect. The defect is silent clobbering combined with the stronger promise that repository files are never written.

**Acceptance:** make output creation explicit and nonclobbering by default; reject existing source/evidence files and symlink collisions, or provide a narrowly documented safe output contract. Preserve stdout as the read-only default. Do not solve this by weakening the scientific-source immutability promise while retaining silent overwrite.

## 5. PR #191 — owner-lane review

**ACCEPT SCOPED.** The diff changes the shared header/LIVE_STATE, `OWNER_LANE` and `PI_PENDING`; the ChatGPT reviewer lane is unchanged. The target is the #188 pilot branch, not main. Roles, staged ownership and deferred #189 are consistent; the owner's historical four-PR observation is correctly dated.

Two nonblocking cleanup notes, both suitable for the same owner edit:
1. The header still says **“The owner lane below is deliberately unfilled”** although it is filled. Delete that leftover sentence.
2. The blind-test pass criterion still says **“all four Atlas PRs found.”** That was the sample observation before #190/#191 existed, not a durable answer key. Freeze the expected relevant PR set from the actual test inputs, including newly staged PRs where they match. Keep a fixed-fixture score separate from live discovery. Do not make a new session fail for correctly finding more currently relevant work.

No requirement to reduce 844 words to an artificial threshold; compactness is advisory. Owner approval of the note is not pilot acceptance, and PR #191's integration does not discharge PR #190's tool findings.

## 6. Next action and authority

Return O190-R1–R4 to the tool owner as **one correction batch with regression tests**; keep all producer evidence unchanged. A bounded delta review and rerun of the relevant reporter controls is sufficient. Do not merge #190 before the corrected tool satisfies its observation/coverage/output contract. PR #191 can be considered separately for its named pilot base; its minor cleanup does not justify another scientific review cycle.

After reporter acceptance, freeze the answer key and run **fresh** ChatGPT and Claude-project sessions, including GitHub discovery of the records path, inaccessible inputs and disposable stale/fake-claim fixtures. This reviewer session cannot substitute for those blind tests. #188 remains test-gated and #189 remains deferred. No merge, tag, pipe-state change or canonical owner-science edit is performed by this review.
