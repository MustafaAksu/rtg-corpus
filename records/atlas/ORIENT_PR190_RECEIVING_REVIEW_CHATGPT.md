# Session orientation reporter — ChatGPT receiving review

**Checked:** 9 November 2026, round 2.  
**Status:** [SESSION] independent tool review; not pilot acceptance, scientific adoption or merge authority.  
**PR #190 verdict: REVISE, narrowed to residual R1/R2/R4 boundary cases. R3 is discharged.**  
**PR #191 verdict: ACCEPT SCOPED. Both previous cleanup notes are resolved.**

This is the current working review. The complete first-round review remains at commit `2ec275bf8e4dfec0198ea351ef37f6e99edbe1d3`, this same path; the original harness and `round1_output.txt` are unchanged. No earlier evidence or producer output was rewritten.

## 1. Exact objects and review extent

- Reporter: PR #190, `claude/tool-orient`, head `6bb77302c25da830790f9971efaa2a068bf23aac`; `tools/orient.py`, 176 lines / 13,079 bytes; SHA-256 **`3570e1c0ecd73e7b6a602744ef599fda0f87f747d2324a3544c738ae67dc9ac5`**, Git blob **`72c031fd5bd16a543341bcfa1edb3bba65b9dd39`**. Both recomputed independently from the actual transferred source. It is unchanged in execution.
- Owner lane: PR #191, head `404bfb6da26bea100208b02be2fa07e096001f27`; base `chatgpt/atlas-session-orientation-pilot` at `6a3cc5e5b46a4dca90aded2c72babf4fc94a0ae5`, not `main`.
- Read the full revised reporter, first-round requirements, the producer's round-2 README, relevant PR metadata, PR #191's complete current diff, and repository `CONVENTIONS.md` §§2–7 before editing this review.
- Git compare shows reporter revision 1 `029524ac...` is still the merge base/ancestor of revision 2: two additional commits, zero behind. This confirms preserved ancestry in the inspected branch; it is not an audit of every attempted local command.

## 2. Executed results and test boundaries

**[EV-BYTES / EV-HASH / EV-RUN]** Python **3.13.5**, unchanged reporter bytes. Git/GitHub `subprocess.run` responses were deterministic offline fixtures; actual reporter parsing, report rendering and optional JSON output executed. File output was confined to temporary directories. Runtime network access was unavailable, so this is neither a live GitHub replay nor a blind replacement-session test.

**Original 21 controls: 21/21 PASS, zero FAIL.** The original harness, SHA-256 `f585abf7f23ebcbabcd2621795ffebb3dc7625e62ed636e6ad9af8c970762681`, is reused unchanged; only `EXPECTED` and `BLOB` are set to the reviewed reporter's identities in memory. This independently confirms the producer's 21/21 report.

**Six bounded follow-up controls: 2 PASS, 4 FAIL.** Four failing cases belong to three already-requested contracts (field-level incomplete data, exact version identity, safe output). The two positive controls retain underscore-form records and report genuinely ambiguous same-version records. These are not new pilot features or a scientific campaign.

The first receiving suite did not cover a patch-version suffix, failure to read an individual enumerated pipe item, or a dangling JSON-output symlink. That coverage gap belongs to this review as well: the 21/21 result is correct but insufficient to discharge the broader R1/R2/R4 conditions already written in round 1. Do not claim that those 21 checks failed or that they prove all response/error paths safe.

Evidence:
- `evidence/atlas/tools/orient_receiving/check_orient_round2.py` — SHA-256 `14ca8cb3f32c7d5fb09e926e97187c463c43f947ac85ac09e5f6193029e4cc7e`; loads the old hash-pinned harness instead of duplicating it.
- `evidence/atlas/tools/orient_receiving/round2_output.txt` — actual output, SHA-256 `0513ac4eefbe5073582dbf03ca75bdb611a3f5ff921de5829a6feccb07b68219`.
- The runner also emits baseline stdout, baseline detailed results, and `round2_summary.json` with the concrete observations. Large repeated baseline call lists are regenerated on demand rather than copied into Git.

```bash
target=$(mktemp)
out=$(mktemp -d)
git show 6bb77302c25da830790f9971efaa2a068bf23aac:tools/orient.py > "$target"
python3 -I evidence/atlas/tools/orient_receiving/check_orient_round2.py \
  --tool "$target" --out "$out"
# Current expected output: baseline 21/21 PASS; additional 2/6 PASS, 4 FAIL; exit 1.
# Actual case observations: "$out/round2_summary.json".
```

## 3. Discharged corrections

The original unreadable-tree case now has null pipe fields and UNVERIFIED text. Missing release Status, missing tag hash, empty remote-main and invalid JSON text become structured partial reports. The original v0.10/v0.100 collision is rejected; mixed `-r1`/patch tag names no longer raise the original comparison exception. Renamed-away paths, same-repository PR URLs and transitive reference discovery in both API orders pass. Default output no longer overwrites an existing ordinary file. These are real improvements.

**R3: PASS SCOPED.** No further PR-discovery change is requested by this round. No automated adoption inference is requested: source records and human authority remain distinct.

## 4. Remaining bounded corrections

### R2 — full release-version identity (L98–100)

- **R2-E1:** with tag `atlas-v0.10` and only `RTG_STATE_ATLAS_v0.10.1_RELEASE_RECORD.md`, the tool selects that different edition and reports **COMPLETE**. The synthetic record contains the same input hash, so a hash-presence check cannot repair wrong version attribution.
- **R2-E2:** with both the exact v0.10 record and the v0.10.1 record, the tool incorrectly reports two matches and **PARTIAL / identity ambiguous**. Only the v0.10 record is eligible.

Cause: `(?![0-9])` permits the `.` or `_` separator followed by another numeric version component. The replacement is still a prefix test for this case.

**Acceptance:** parse/extract the complete version token (normalizing supported dot/underscore spelling) and compare it for equality with the tag version. Keep real duplicate same-version records ambiguous, but do not treat a later patch version as either a match or an ambiguity. The new E1/E2 and the original N04 must pass.

### R1 — individual pipe reads are also incomplete observations (L140–151, L168)

**R1-E1:** enumeration succeeds and lists one item, but `git show origin/main:<item>` fails. The tool records a top-level PARTIAL warning, then emits `inbox: none; outbound not closed: none` and `{}` counters. This repeats the original false-empty problem at the item-read level.

**Acceptance:** track incomplete/unreadable items and propagate incompleteness into affected field(s). Null fields or explicitly marked lower-bound counts with a completeness flag are acceptable. The human-readable output must not state an empty inbox/outbound set when it was not established. An unknown sender also limits outbound completeness. Preserve the working whole-tree failure behavior and the original positive cases.

### R4 — dangling symlink output collision (L170–173)

**R4-E1:** in a temporary directory, `observation.json` is a symbolic link to a nonexistent synthetic `atlas/RTG_STATE_ATLAS.md`. With default `--json observation.json` and **without** `--replace-json`, `os.path.exists` returns false and `open(..., 'w')` follows the link, creating the target with JSON report content. No production file was involved.

**Acceptance:** default creation must refuse an existing directory entry, including a dangling symlink. Exclusive creation (`open(..., 'x')` or equivalent O_EXCL) avoids the check-then-open gap; handle the refusal clearly. An explicit report replacement must reject symlink redirection or have an equally safe stated contract. This is the symlink-collision requirement already present in round-1 R4, not a ban on intentional JSON report creation.

Apply these three small corrections together and rerun the existing 21 controls plus the six follow-up controls. No broad new feature, source migration or certificate campaign is requested. The finite fixtures do not certify every malformed payload, semantic tag-order policy or concurrent GitHub race.

## 5. PR #191 disposition

**ACCEPT SCOPED at `404bfb6...`.** The leftover “deliberately unfilled” sentence is removed. Test expectations now use a PR set frozen with the answer key, with separate fixed-fixture and live-discovery scoring; they no longer require exactly four live PRs. The diff from its current pilot base changes only shared/owner sections and leaves `REVIEWER_LANE` unchanged. The owner incorporated the previous reviewer-lane commit `6a3cc5e` before the update.

That stacked PR can be considered independently for its named pilot branch. It does not authorize the reporter's merge, pilot acceptance or Methodology migration.

## 6. Next action and PI boundary

PR #190 remains **REVISE** only for the residuals in §4; PR #192 records the evidence, not approval of the tool. The owner may prepare the blind-test answer-key schema now, but freeze the final reporter commit and PR-response fixtures after the corrected tool is accepted. Fresh ChatGPT and Claude-project tests remain necessary for #188; this returning session is not a substitute. #189 remains deferred.

No merge, tag, force-push, pipe-state edit, scientific-owner change or reporter-code edit was performed by this review. Only the review/evidence branch is updated; any reviewer-lane checkpoint update is limited to that lane.
