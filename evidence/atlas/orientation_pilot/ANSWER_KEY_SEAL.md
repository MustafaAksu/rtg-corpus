# Atlas orientation pilot — answer-key seal

**Frozen:** 9 November 2026, 12:10 +03:00, by Claude (Atlas owner). The key itself is held by the PI and is not in the repository until both blind tests are scored; it is then published unchanged beside the test records, and its hash must equal the value below.

| Sealed object | SHA-256 | Bytes |
|---|---|---|
| `ANSWER_KEY_FROZEN_20261109.md` | `b1b44898e20abfe7d247c7af4d3b6906ca5c5a73b8b2118f63dca2898c2ef2e4` | 6,023 |

## Frozen inputs (observable; the expected answers are in the sealed key)

| Input | Value |
|---|---|
| `main` | `c8333a43ab9bbe948533d92df332386b5d141533` |
| Pilot branch `chatgpt/atlas-session-orientation-pilot` (note under test, PR #188) | `e9bb4ce48917d120ba51c059be3ec7c5506ad331` |
| `records/atlas/ATLAS_COOWNER_SESSION_ORIENTATION.md` at that head | SHA-256 `3622c24b852747893787babb63a21439a9fa3093490889f216e906ece3adb28d` |
| `tools/orient.py` on `main` | SHA-256 `dfbcb1da0a7ac4d3ec942cae4a125875caa1030ddebd103821bf5c75b0c5cd0c` |
| Fixtures branch `claude/orientation-pilot-fixtures` (tests 2 and 3; no PR) | `aaabe72245fd92d1cdd01149448746e453451b9b` |
| Open PRs at the freeze | #113, #114, #160, #180, #183, #188, #189 |
| `tools/pipes_index.py --check` at the freeze | 88 items in 20 inboxes |

**Validity.** The merge of this seal (PR #194) is expected before the tests and is the one change to `main` the key allows. Any other merge to `main` or to the pilot branch after the freeze moves the inputs; the owner then re-freezes (new key, new seal) rather than reinterpreting results. The tests are run by one fresh ChatGPT session and one fresh Claude project session that receive only the note's bootstrap message (and, for tests 2 and 3, the fixture branch and path). Scoring is by the PI and the Atlas owner against the key, with the Atlas co-owner free to score independently.
