# Co-owner execution and working memory — supporting runbook

**Date:** 9 November 2026. **Status:** [SESSION] proposal for Atlas-owner review and the PI's operational decision. This does not change adopted Methodology, platform permissions or scientific authority. It is **not another entry note**: the single Atlas entry remains `records/atlas/ATLAS_COOWNER_SESSION_ORIENTATION.md` (PR #188 until merged). Other studies keep their owner-selected entry path.

**Objective:** a new or continuing session can identify reliable inputs, preserve useful work, and resume an eligible task. Success is not measured by model rank or use of one particular tool. Keep source identity, structural checks, computation and scientific validity separate.

## 1. Start by identifying capabilities, not by assuming a workstation

Record the environment actually observed: shell available; Python available/version; Git; gh; repository clone/ref; permitted GitHub network; authenticated GitHub connector; scratch-file access. A missing executable, absent clone, authentication failure, permission denial and missing network are different conditions. Record the exact failed command and sanitized error once; do not repeatedly try variations to evade a denial. Never include tokens or sensitive environment contents.

Choose one supported mode:

| Mode | Prerequisites | Action and evidence boundary |
|---|---|---|
| **Native reporter** | Permitted shell, Python, complete-enough Git history/tags, gh, authorized GitHub access | Run the reviewed `tools/orient.py` at an identified commit/hash. Record query time, source ref, command, output status and actual return code. COMPLETE is an observation status, not adoption. |
| **Connector-assisted** | Authorized GitHub connector; optional local Python | Read the same refs, tag objects/targets, release records, file bytes, paginated PR file lists/references and pipe items through the connector. Hash complete bytes locally when possible. Declare this mode; do not claim `orient.py` ran. Mark unreadable or incompletely enumerated fields separately. |
| **Supplied snapshot** | Verified, permitted export/attachment; no live source route | Analyze the identified snapshot and state its age/coverage. It is not a live PR/queue observation. Request only the missing operational input when it affects the task. |

Do not require a Git clone merely to hash one accessible file. Fetch full content or base64 with its source ref/blob, transfer it to the execution environment without normalization, and check the Git blob as well as SHA-256. A partial fetch, displayed excerpt or lossy copy cannot support a file-hash claim. PR results must record query time and pagination; a Git commit alone does not freeze their state.

## 2. Native reporter preflight and permitted execution

For an **already available trusted clone**, inspect these commands separately so failures are attributable:

```bash
python3 --version
git --version
gh --version
git rev-parse --show-toplevel
gh auth status
```

If the repository's network operations are permitted, refresh local remote-tracking objects (no main edit or remote mutation):

```bash
git fetch origin --tags
```

Use the actual reviewed reporter at its current verified version. For the pilot's accepted revision, the bytes are pinned by commit `34e55078fcce6041169ee2cab624eef55600b202` and SHA-256 `dfbcb1da0a7ac4d3ec942cae4a125875caa1030ddebd103821bf5c75b0c5cd0c`; those are a historical reproducibility pin, not a permanent claim that this version is newest.

```bash
sha256sum tools/orient.py
python3 -I tools/orient.py ATLAS
```

Stdout needs no report-file permission. For a retained report, use a fresh scratch directory and non-existing destination, not a DSN/evidence source path:

```bash
report_dir=$(mktemp -d)
python3 -I tools/orient.py ATLAS --json "$report_dir/atlas-observation.json"
```

The reporter locates repository data through Git. Do not run it against a fabricated empty clone and present that as production state. A shallow clone may need additional permitted history for ancestry questions; fetching a specific required object is enough when full history is unnecessary. If no clone exists, a permitted temporary clone is allowed under the proposed bootstrap below; if shell/network access is unavailable, use connector-assisted mode instead of repeatedly attempting clone/download commands.

**Permission diagnosis:** the historical Claude test supplied no raw denied-command log, so its exact cause remains unknown. In Claude Code, `/permissions` shows the rule and scope; a narrowly authorized `python3 -I tools/orient.py ATLAS` command is preferable to a blanket shell grant. Do not assume Claude Code settings exist in a hosted Claude project interface. Organization-enforced restrictions require the organization's supported process, not a prompt workaround. Never use a global permission-bypass option for this pilot.

The official OpenAI data-analysis documentation distinguishes network-isolated Python execution from connected-source access. The official Claude Code documentation distinguishes prompt instructions from enforced permissions. These are environment types, not claims that every ChatGPT/Claude surface has identical capabilities. References, checked 9 Nov 2026: https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt ; https://code.claude.com/docs/en/permissions .

## 3. Proposed bootstrap wording — remove test-only ambiguity

The original test outputs, key and seal remain immutable. For future operational starts, the owner can restore this explicit bootstrap in the existing entry note:

> Take the named stream's co-owner role. Read its selected entry note and CONVENTIONS directly from the authorized GitHub connection or repository; do not assume project synchronization includes records/. Verify the governing adopted tag and release record, current work refs, PRs, inbox and owner sources needed for the next task. First identify your actual tool capabilities. You may create temporary scratch files or a temporary clone, refresh local refs, compute hashes and execute the reviewed read-only reporter using normally authorized tools. Do not modify shared repository content, push, merge, tag, change pipe states or adopt science as part of this entry check. Do not bypass an environment permission denial. If native execution is unavailable, use equivalent authorized connector queries and report their coverage. Do not infer missing prior-session reasoning or claim an unperformed computation. Return the next eligible action, the durable checkpoint and any blocking missing input.

For ordinary **ongoing** work, the task and CONVENTIONS determine branch/PR write authority. The entry-check prohibition is not a permanent ban on preserving work to an authorized co-owner branch. Tests 2/3 must keep injections in disposable fixtures; source protection is not a restriction to remove.

## 4. Use the same note as durable stream working memory

Treat orientation as the **entry/resumption view of persistent repository working memory**, not an end-of-chat handover and not automatic model memory. Preserve the fixed path and existing owner/reviewer lane boundaries. Avoid a parallel MEMORY.md or a second scientific summary.

Three layers have distinct authority:

- **Derived observations:** current tags, hashes, PRs and queue states; regenerate on entry or material state change, never trust an old copied census as live.
- **Human-maintained working intent:** goal, next eligible action, explicit PI decision pending, last durable work ref, blockers and a concise decision rationale. The same long-running session uses these during a context recap, interruption or multi-day investigation.
- **Existing source/evidence records:** complete calculations, code, results, negative findings, reviews and adopted DSNs in their established homes. The short note links to them; repeated summaries do not upgrade a SESSION finding to owner science.

Within **each existing lane**, use a compact checkpoint:

```text
Goal / current question:
Last durable work: branch + pushed commit + PR; exact file/section
Decision held: status + recorded rationale/source (including rejected route if useful)
Evidence: what was read/run; unresolved assumptions and missing inputs
Resume: exact command or next file/operation; last completed vs next unexecuted step
Next 1-3 actions / acceptance criteria:
Reopen trigger: what new evidence would change the present decision
```

Store decisions and concise scientific reasoning summaries, not private scratchpad history or claims of recovered hidden reasoning. Preserve negative results and abandoned-route reasons with their scope so the next session does not repeat the same failed attempt. Use the owner's existing records for detail.

**Checkpoint triggers:** a meaningful decision, counterexample, new result, rejected approach, material review, blocker, completed long computation, or imminent long work/context pressure. Update before switching away while access still exists; do not wait for a maximum-length warning. No timer, every-message update or empty note for dormant work is required.

**Durability does not require immediate main merge.** A pushed commit on the authorized co-owner branch plus its discoverable PR is durable but unadopted. Refreshing sessions inspect active PR heads as well as the merged entry note. A local-only file is not durable across session loss; say so. The PI's main-merge and adoption rights remain unchanged. The owner maintains shared entry/PI fields; each co-owner updates its own lane. Git preserves replaced checkpoints; keep the live note concise.

## 5. One maintenance pass; no new governance edition

Suggested single owner maintenance pass: resolve F1–F3, restore the bootstrap, link this execution guidance, and add working-memory/checkpoint use to the existing lanes. Keep PR #189 deferred. Do not change the original transcripts or relax the frozen key after scoring.

Close F4 prospectively with one **narrow fresh-session smoke test** in a configured native environment: pin reporter/ref, run it, record stdout/JSON and status, and distinguish source-observation completeness from tool availability. Do not rerun all scientific or E/D/R tests. In connector-only environments, run the equivalent-read capability check and retain the explicit execution-mode label; native execution remains NOT RUN, not falsely PASS. Whether the proposed workflow is adopted remains the PI's decision.