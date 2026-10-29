# TDR-G v2.12.14 — Post-tag publication and cross-stream closeout addendum

**Date:** 28 October 2026
**Status:** Post-adoption factual addendum; no change to the adopted release record, canonical DSN, or annotated tag.
**Governing object:** `tdrg-v2.12.14` (annotated tag object `da941f3b2f02f9f242e1c0f517120bfbaead7996`; target merge commit `05c7e78acf63dd1dc5bcbc7bb8364e152e9f0659`); DSN SHA-256 `3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392`.
**Frozen adoption record:** `records/tdrg/TDRG_v2_12_14_RELEASE_RECORD.md`, as found at the adopted tag and at publication; Git blob `3c720567f38405f5a68870d1a7ee681cac02a4f2`. The record truthfully described merge/tag as pending when it was frozen. Under adopted Methodology v1.4 §13.7, later facts belong in this dated addendum, not an edit to the frozen record.

## 1. Post-adoption release-lifecycle resolution

The following states resolve the formerly pending items of the frozen release record without overwriting it.

| Release-record item | Post-tag observed status |
|---|---|
| §1: Merge commits and tag | Complete: six authorized PRs merged by merge commits, with `tdrg-v2.12.14` annotated and pointing at PR #92's merge commit |
| §12 step 4: merge sequence | Complete: PR #87 `6d2d95b`, #91 `0a25c06`, #97 `6c0365f`, #94 `750e00c`, #95 `3f40c2e`, #92 `05c7e78` |
| §12 step 5: annotated tag | Complete: `tdrg-v2.12.14` on `05c7e78acf63dd1dc5bcbc7bb8364e152e9f0659` |
| §12 step 6: baseline | `BASELINE.md` row on `main` identifies the tagged adopted v2.12.14 DSN and hash |
| §12 step 7: outbound notices and TDR-G inbox closure | Completed in PR #99: three consumer queue items filed with `state: open`, two TDR-G inbox items closed |
| §12 step 8: atlas release follow-through | Atlas tag-verification record and atlas v0.7 refresh remain outside PR #99 |

**Scientific status unchanged.** Neither the old v18 BIND3/NKSCAN/N-scaling results nor the canonical engine were rerun or silently promoted under the amended path-orientation rule. Four older session certificates remain missing; the held large motif corpora remain held. The adoption and published tag are not altered by this addendum.

## 2. Preserved post-tag check and notice record

The following text is the post-tag closeout section prepared by the TDR-G co-owner, separated from the frozen release record in accordance with Methodology v1.4 §13.7.

## 15. Post-tag verification and notices (28 October 2026)

**Tag.** `tdrg-v2.12.14` is an annotated tag on the merge commit of #92, `05c7e78acf63dd1dc5bcbc7bb8364e152e9f0659`, which was `main` HEAD at verification. Its message carries the DSN SHA-256. `git show tdrg-v2.12.14:dsn/RTG_DISCRETE_GENESIS_DSN.md` hashes to `3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392`, which is the adopted bytes (EV-RUN; also verified independently by the ChatGPT co-owner session). The commits cited by §8 and gate C8, `c359e21` (PR #91) and `386e9d4` (session scripts, PR #97), are ancestors of `main`.

**Checker on the published tree** (`check_output_posttag.txt`): 11/11 PASS. The only line that differs from the pre-merge `check_output.txt` is C8. There the session scripts are now read from the placed tree (`source: tree`) instead of commit `386e9d4`, which is the branch-free path of round 2.

**Notices filed** (kind `notice`, state `open`; filing is a queue event, not evidence of receipt or adoption):
- `pipes/NUMGEN/20261028-TDRG-v2-12-14-adopted.md`: the TDRG-DEF-ORIENT ruling, the reference implementation, the DISC-2 effect (20 of 136), and the RIDs for the "RID unavailable" imports;
- `pipes/OFN/20261028-TDRG-v2-12-14-adopted.md`: Finding A accepted as a statement with custody deferred; REQ-O09-05 answered; the RID map for IMP-O08-*;
- `pipes/AZ/20261028-TDRG-v2-12-14-adopted.md`: `TDRG-ZN-STATE` resolves; the LEM-* map; the §6.2 citation and its scope.

**Inbox.** Both `pipes/TDRG/` items are now `closed`: the orientation request with `accept`, the NUMGEN v1.21 notice with `no action`.

**Remaining.** The atlas owner's tag-verification record and atlas v0.7 (D5 TDRG rows, D5.X1, H4, H9, N1 row, TC-17 fix). Consumer actions are each consumer's own: NUMGEN re-annotation and the C7C-M4 release, OFN repin, AZ repin. The items carried forward in §14 are unchanged.
