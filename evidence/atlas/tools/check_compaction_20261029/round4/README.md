# check_compaction.py round 4 — 10 November 2026

Answers the round-3 readback of PR #114 (`records/atlas/TOOL_CHECK_COMPACTION_PR113_ROUND3_READBACK_CHATGPT.md`): a `relocate_hashes` declaration on a header or footer operation could authorize an undeclared live deletion.

Fix (tool SHA-256 `d2977b3e24fd54a1d85fe53ea88f65dd51a9e26890b56b17ab5855716b57d87c`): a declaration on `replace-header` / `replace-footer` is invalid, and for other operations only occurrences of the hash in the live region of the removed span (after the header, outside the history region, not on a footer line) count towards the net removal.

- `test_check_compaction_profile_output.txt`: producer profile tests, 19/19, fixture file unchanged (`45c3cbb5…`).
- `receiving_round1.*`, `receiving_round2_binding.*`: the reviewer's earlier harnesses, unchanged, 7/7 and 3/3.
- `test_metadata_binding_r4pin.py`, `receiving_round3_metadata.txt`: the reviewer's round-3 harness with only `CHECKER_SHA256` moved; 4/4 (both negatives now FAIL, both paired positives PASS).
- `reg/`: the eight regression runs (DYAD, RECOG ×2, GEN ×2, NUMGEN ×2, Programme); all exit 0 and byte-identical to `../regression_fix/`.
- Not rerun: the OFN v0.11 campaign of `../round3/ofn_v0_11/` (inputs not in this workspace).
