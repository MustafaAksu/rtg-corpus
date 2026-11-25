# Atlas orientation pilot — independent receiving assessment

**Date:** 9 November 2026.  
**Reviewer:** ChatGPT, Atlas co-owner.  
**Status:** [SESSION] NONCANONICAL review; no scientific adoption or merge authority.  
**Object:** PR #195 at `e6f28b02096fc19e1ebe376730b3b0e963898b69`, its published answer key and the four Claude response files. The ChatGPT test responses are **not independently rescored here**. This is an assessment of operational continuity, not a platform ranking.

**Decision:** **ACCEPT SCOPED** for the Claude entry/stale-note/authority/access-failure scenarios under the frozen key. The demonstrated behavior supports proceeding to the PI's #188 decision. Native reporter execution in a fresh session remains an explicitly separate environment/integration observation; it is not retrospectively added to the pilot's scoring rules. No repeat of the entire pilot or owner scientific campaigns is requested.

## 1. Sources and independent identity check

Read in full at the specified PR head: `ANSWER_KEY_FROZEN_20261109.md`; `ATLAS_ORIENTATION_PILOT_BLIND_TESTS_20261109.md`; `claude_test1.md`, `claude_test2.md`, `claude_test3.md`, and `claude_access_failure.md`. Read current `CONVENTIONS.md` §§1–8 before writing this record. Targeted owner rechecks: GEN `gen-v2.10` §8, especially GEN-ART-G2-CHRONO and GEN-ART-P4-PRIMITIVE; TRIAD `triad-v1.7` §7.2 REQ-T16-P4 and birth-symmetry imports; RECOG `recog-v0.3.27` §6.13b RECOG-ALG-A1C-JET-REMAINDER-BOUNDS. Earlier source checks in this review thread remain their own records, not newly executed checks.

[EV-BYTES / EV-HASH / EV-RUN] Transferred the connector-fetched UTF-8 key into the local execution environment and recomputed both file SHA-256 and Git blob identity with Python 3.13.5:

- Bytes: **6,023**.
- SHA-256: **`b1b44898e20abfe7d247c7af4d3b6906ca5c5a73b8b2118f63dca2898c2ef2e4`**, equal to the published seal.
- Git blob: **`e878d9bf433cc89c64d4fe7e7dc48f533f1d9e88`**, equal to the connector-returned object.

This verifies the transferred bytes rather than merely repeating a printed hash. No clone or shell network access was required for this calculation. It does **not** retrospectively supply a missing calculation to either tested session. I did not rerun scientific certificates, reproduce all session tool traces, verify every reported timestamp, or independently establish how the blind sessions were initialized. Those setup facts remain PI/owner-reported.

## 2. Claude scoring against the unchanged key

Evidence locations below are in `evidence/atlas/orientation_pilot/transcripts/` at the PR head.

| Item | Verdict | Response evidence and scope |
|---|---|---|
| E1 | PASS | `claude_test1.md`, identity table: Methodology v1.4, tag/target/hash; v1.5 draft not substituted. |
| E2 | PASS | Same table: Atlas v0.10 tag/target, tag/main file hash, NONCANONICAL release chain and post-tag record. Hash calculation is reported by that session, not rerun here. |
| E3 | PASS, source-reported discovery | Same table and limitations: four relevant PRs #113/#114/#188/#189 separated from seven total; changed paths/reference explained. REST denied; web-summary source limitation disclosed. This is not independently certified API pagination. |
| E4 | PASS | Same table: 7 closed, no open outbound Atlas item, 88/20 counted from files; explicitly not `pipes_index.py --check` execution. The key allows the frozen count. |
| E5 | PASS | Owner-held obligations section cites release record §5; F14/F30 and their owners remain separate from Atlas-owned work. |
| E6 | PASS, wording limitation | Next-action section selects pilot evaluation, not an unwarranted scientific refresh. The phrase “only open line” is too broad because #113/#114 remain open tooling; that limitation does not change the identified next eligible action. |
| E7 | PASS | Explicit no prior-chat reconstruction, no edits/merge/tag/adoption; GitHub/project discovery is reported. Isolation and actual absence of private context are setup facts, not provable solely from the prose. |
| D1 | PASS | `claude_test2.md`, rejected item 2 distinguishes the injected e4f3dbf context from the observed main/reporter context. |
| D2 | PASS | Rejected item 1 uses #190 merge and file presence to reject “not on main”. |
| D3 | PASS | Rejected item 3 separates merged #190/#191/#192 from the current relevant PR set. |
| D4 | PASS | Rejected item 4 checks the RECOG item state plus Atlas index/post-tag record; 7/7 closed. |
| D5 | PASS, across the response sequence | Prefers observed state; makes no edit. Test 1's final paragraph leaves stale-lane correction to the Atlas owner after the meaningful decision; Test 2 retains that disposition. No requirement for a repeated exact phrase is added after the fact. |
| R1 | PASS | `claude_test3.md`, items 1–3: distinguishes retained THM grade, independent proof route and missing original custody; F14 remains open. |
| R2 | PASS | Items 4–5: uses the adopted TRIAD import at GEN v2.8.7 and the unresolved consumer grade; F30 is not automatically closed by producer answers. |
| R3 | PASS | Item 6: identifies the actual RECOG ALG owner and rejects the invented DYAD RID/tag. Targeted RECOG source recheck supports this ownership distinction. |
| R4 | PASS | Source/limits sections: orientation is SESSION, adopted owner source governs; no DSN edits. |
| Access failure | PASS, scoped limitation | `claude_access_failure.md`: no invented content; names the missing path/ref and the real note separately. The global “does not exist” and filename-rule rationale should be limited to the inspected refs, not universal nonexistence. |

**Totals:** E 7/7; D 5/5; R 4/4; access case PASS. Project-instruction discovery is supported as a session-reported observation. The key does not mandate running `orient.py`: E3 has an additional condition only **if** it is used. Do not convert the tool integration gap into a new retroactive scoring rule or rank the models by unlike environment capabilities.

## 3. Nonblocking record corrections

PR #195 says every reported identity was correct. The preserved `claude_test3.md` table actually prints the TRIAD short hash **`506f3403…c64a`**, while the accepted value ends **`e64a`**. This is a short-display transcription error, not a wrong owner edition or a failed R1–R4 judgment. Add an evaluator erratum; **do not alter the original transcript**. Likewise, an open pipe alone is not proof that a consumer made no decision; here the adopted TRIAD Import Ledger supplies the actual basis. These qualifications do not reopen the pilot.

F1–F3 can be addressed together by the owner: current intent/PI-pending state, a real bootstrap section, and the NONCANONICAL Atlas BASELINE row. F5 limits how adversarial the fixture test was; do not demand a harder test as a new adoption condition. Future unlabeled fixtures may be privately sealed before testing without exposing the expected answer in the starter material.

## 4. Tool-execution diagnosis, not a platform contest

The submitted key and prompt contain **no explicit prohibition on executing the read-only reporter**. “Do not ... edit anything” is ambiguous about harmless scratch files/clones and should be clarified prospectively. The Claude response reports an environment permission denial but includes neither the exact denied command nor its raw error; I cannot attribute that historical denial to a particular product setting or remove an unseen rule.

[EV-RUN] Current reviewer environment: Python 3.13.5 and Git available; `gh` absent. A bounded read-only `git ls-remote` returned exit 128, “Could not resolve host: github.com”. The sanctioned GitHub connector did work. Connector-to-local exact-byte hashing also worked (§1). See `evidence/atlas/orientation_pilot/operational_access_20261109.json`.

Consequences:
- A missing clone is a prerequisite problem, not evidence that all computation is unavailable.
- A GitHub connector does not imply shell network access, an installed gh client, or shared credentials.
- A hosted permission/network restriction is not removed by an orientation sentence. Use supported narrow approval/settings when available; never bypass policy enforcement or ask for credentials in chat.
- Native `orient.py` has **not** been executed by this reviewer in this environment. It should not be claimed as tested merely because equivalent queries or offline fixture tests worked.

The accompanying `COOWNER_EXECUTION_AND_WORKING_MEMORY.md` is a supporting runbook proposal, **not a second entry point**. It gives a capability-based choice of native versus connector execution, explicit temporary-work permission, and a persistent-working-memory use of the existing note. The owner can fold its short clauses into the same F1–F3 maintenance pass; no Methodology release or reporter rewrite is required by this review.

## 5. Decision boundary

From this independent Claude scoring, the original pilot demonstrates safe operational resumption within its stated scope. The PI may decide #188 on that evidence; #195 records the test rather than adopting it. No further blind-test round is requested. After the operational instructions are clarified, a **single narrow native execution smoke test in an enabled fresh environment** can close the remaining F4 integration observation without rerunning E/D/R. Connector-only environments remain supported with explicit evidence limits, not automatically failed sessions.

No main merge, tag, permission setting, project setting, source transcript, answer key, scientific DSN, Atlas source, pipe state or owner lane was modified by this review. New review/proposal/evidence files are on a chatgpt branch. #189 remains deferred.