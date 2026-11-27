# RRF v0.9 — independent release readback

**Date:** 27 November 2026.
**Status:** [SESSION] / NONCANONICAL. Reviewer lane (Claude, independent reviewer / second co-owner). This is a readback of the publication preparation only. Merge, tag and BASELINE remain PI actions.
**Reviewed:** PR #417, exact head `638a1a8b412b8e80bd40408b1b22cf6bcfb88c2f`. The two commits after the reviewed and adopted candidate are `ef28cc7d` (adoption record and release record) and `638a1a8b` (status metadata and notices).
**Adoption basis:** PR #417 comment `7213581950` ("v0.9 u benimsiyorum") for exact candidate `8de7a8cd` / `2950dbc0…942d`, with metadata-only finalization subject to this readback. Closure criteria: comment `7202555052`.

## Verdict

**ACCEPT SCOPED — ready for publication.** The publication-ready DSN is the PI-adopted candidate with exactly 20 status-only line substitutions. No scientific statement, grade, scope, constant, transport, source pin, profile or OPEN state is changed. The release record carries G1 and the three adapter limits. The two outbound notices are filed with valid front matter and request no automatic adoption.

## Checks (native)

| Check | Result |
|---|---|
| `python -I evidence/rrf/scripts/publish_rrf_v0_9.py` | exit 0. Three negative controls PASS (coefficient, missing edit, wrong anchor). `RRF_V0_9_PUBLICATION_PASS 20 metadata lines 121216 28c9c101…075d`. |
| Independent line diff, adopted `8de7a8cd` → `638a1a8b` | 654/654 lines. Exactly 20 changed, at lines 5, 8, 9, 74, 204, 293, 331, 338, 357, 475, 477, 479, 486, 500, 508, 573, 575, 577, 647 and 653, which are the release record's list. All 20 were read: date, status and supersession wording; "candidate" becomes "registered" for the six local IDs and four OPEN IDs; closure-criteria status; edition wording; Appendix A; footer. The four OPEN rows are byte-identical and ACTIVE. |
| Final DSN | 121,216 bytes, SHA-256 `28c9c101c715b402b5ed60eeab8bfa2c7e5e637fef3cd2b00961dfa60553075d`. |
| Ancestry | `98da97c3` (S2a freeze) and `8de7a8cd` (adopted candidate) are both ancestors of HEAD, and remain so after trial integration on current `main` `136d1c59`. |
| `rrf_s2b_reviewer_checks.py` at the publication head | C1–C5 PASS. The archive and import accounting is unaffected by the metadata transform. |
| `check_rrf_s2b.py` at the publication head | fails on candidate identity, by design. The adapter certifies the S2b candidate `2950dbc0…` and must be replayed at `8de7a8cd` (release record §1, §4). On `main` after publication it will keep failing; this is not a custody break. |
| `tools/dsn_lint.py --prev rrf-v0.8.4` | informational: +12,601 bytes (+11.6 %), 0 near-duplicate paragraphs, one footer, 67 RIDs |
| Pipes | `pipes OK: 199 items in 20 inboxes`. Two new notices: PROG (IF30/31/33; the IF31 γ≡κ wording matches Programme L454) and RER (IF33/G7–G10/CND01). Their front-matter tags are existing tags only, and their bodies make use conditional on the verified `rrf-v0.9`. |
| Trial integration | `main` `136d1c59` + #417 (`638a1a8b`) + #418 merge cleanly. Pipes 199/20. The publication checker still PASSes. |
| BASELINE row (release record §6) | The format matches the existing OWNER-row pattern. It is to be installed only in the publication transaction. |

## Non-blocking notes

- The orientation shared block is updated by the preparer. The Claude lane is updated here only.
- After the tag, the post-tag record should list the actual merge commits, the tag object and target, and the tagged DSN hash. Notice front matter can then gain the `rrf-v0.9` tag as a separate follow-up, as the release record states.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
