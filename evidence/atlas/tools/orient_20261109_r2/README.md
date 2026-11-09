# orient.py round 2 — 9 November 2026

- `atlas_run.md` / `atlas_run.json`: live ATLAS run of the revised `tools/orient.py` (SHA-256 `3570e1c0ecd73e7b6a602744ef599fda0f87f747d2324a3544c738ae67dc9ac5`) on `origin/main` at the time of the run (recorded inside).
- `test_orient_receiving_r2pin.py`: the receiving harness of PR #192 (`chatgpt/orient-pr190-receiving-review` at `2ec275bf`, `evidence/atlas/tools/orient_receiving/test_orient_receiving.py`), unchanged except for the two pin constants (`EXPECTED`, `BLOB`), which now name the revised tool. The fixtures and the 21 contracts are the reviewer's.
- `receiving_output.txt` / `receiving_results.json`: its run against the revised tool, 21/21.
- `json_guard.txt`: a second invocation with the same `--json` destination; the tool refuses to replace the existing report.
