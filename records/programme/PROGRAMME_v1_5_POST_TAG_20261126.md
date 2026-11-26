# Programme v1.5 — Post-tag verification and receiving closeout

**Date:** 26 November 2026.
**Status:** [SESSION] Programme preparer (ChatGPT); proposed administrative closeout, pending independent review by Claude and PI-authorized integration. Programme v1.5 already governs. No new edition, scientific result or adoption decision.
**Source checkpoint:** `ad563bf62ddc1d397d3f3cc90a06428757bf8379`, main and tagged merge. Frozen release record is retained unchanged.

## 1. Publication identity

| Object | Identity |
|---|---|
| PI-adopted candidate commit | `bad1314c08287aabd6fbc7114dc391764bc96a89` |
| Candidate SHA-256 | `c07689b0f6e617c0b4a6a29d95d194b99bbbe3f4c3c8a686ccfd02d492c0811c` |
| Reviewed publication commit | `bd17fab78d76c4ec68e41ae7239673841c8b6bab` |
| PR #392 merge / tag target | `ad563bf62ddc1d397d3f3cc90a06428757bf8379` |
| Merge parents | `cefc0470dcd37dc075152adec1a6e12c700f4f38`, `bd17fab78d76c4ec68e41ae7239673841c8b6bab` |
| Annotated tag object | `programme-v1.5`: `f11c73a238573d4012ff7e6d16a7c4d55d415eaa` |
| Published DSN SHA-256 | `9c53159f64feddfba7cfcb2452f9eca1c61bac63b744cb05421417d384bf9611` |
| DSN blob | `08bf37c38ef162f4e5b57d2654bf6b47d11d61ec` |
| Release record | `records/programme/RTG_PROGRAMME_OVERVIEW_v1_5_RELEASE_RECORD.md` at the tag |
| Release-record SHA-256 | `64ccc607eb43d4892696c1218fad140fbec2ba02331a38a2326d2aa3fae5b179` |
| Release-record blob | `665d02958126050c35af7f241cba29451538460a` |
| Governing Atlas | `atlas-v0.15`; SHA-256 `483e60034ff3bb644216c5123d28b8bca253d3ba1b72cdf68bfb0056518d02df` |

PI decisions (26 November 2026, 10:45 +03:00): [7185805217](https://github.com/MustafaAksu/rtg-corpus/pull/392#issuecomment-7185805217). Independent ACCEPT readback [7185742029](https://github.com/MustafaAksu/rtg-corpus/pull/392#issuecomment-7185742029); publication ACCEPT [7186050211](https://github.com/MustafaAksu/rtg-corpus/pull/392#issuecomment-7186050211); post-tag VERIFIED [7186466617](https://github.com/MustafaAksu/rtg-corpus/pull/392#issuecomment-7186466617). Standing Programme assignment: `records/programme/PROGRAMME_EDITORIAL_ASSIGNMENT_20261126.md` (ChatGPT prepares, Claude reviews, PI decides policy/adoption/publication; Atlas roles unchanged).

**EV-SRC-READ / reported EV-RUN:** PI's server transcript records the actual merge, published DSN/Atlas hash checks, BASELINE check, native pipes OK 183 items / 20 inboxes, annotated tag push and object/peeled commit. Claude independently ran the native ten-line publication verifier with exact inverse recovery, trial merge and pipe check, then verified the actual tag. Those are their native executions; no fresh native run is claimed by the preparer.

**EV-HASH / EV-BYTES:** Connector readback in this session confirmed the tag object/target/message, both merge parents, merged/closed #392 and actual main. Fresh full SHA-256 computations of the tagged DSN, frozen release record and accepted Atlas matched their recorded hashes; file blobs at main/tag/publication (where applicable) matched. BASELINE agrees; Atlas unchanged. The full nontruncated Git tree census gives 183 item files in 20 inbox directories, including two empty inboxes.

## 2. Receiving decisions

The frozen release §3 ledger lists P01–P13. All thirteen open and four previously closed items at the tagged checkpoint were read; the thirteen names and verdicts match the reviewed ledger. P01 is eligible for closure under the separate PI assent. These are implementation of the reviewed Programme dispositions, not new scientific judgments.

| Key | File in pipes/PROG/ | Verdict | Scope (summary; full adopted scope in release §3) |
|---|---|---|---|
| P01 | `20261109-SAT-satellite-interface.md` | accept with change | Adopted §6.5 registry link, common SAT filing key and scoped notice policy; separate PI assent in 7185805217. No satellite amendment or repin. |
| P02 | `20261111-AZ-v0-7-adopted.md` | accept with change | §§6.1,6.5,7.2,9.2 reflect subsequent AZ v0.10 state; guards and grade unchanged. |
| P03 | `20261112-AZ-v0-8-adopted.md` | accept with change | §6.7 executed reduction only; Methodology migration recorded; no merger or promotion. |
| P04 | `20261112-TDRG-v2-12-15-adopted.md` | accept with change | §§6.4,7.3 actual A→B→C/T0 export gate; no bridge. |
| P05 | `20261114-AZ-v0-9-adopted.md` | accept with change | AZ S1 diagnostic and TDRG v2.12.15 context pin; not TDR-G result or Level B. |
| P06 | `20261116-AZ-v0-10-adopted.md` | accept with change | AZ S2, inventory and actual context pins; no numerical rerun. |
| P07 | `20261116-TDRG-v2-13-adopted.md` | accept with change | TDR-G migration and separate exports; custody and launch gate remain open. |
| P08 | `20261119-DZT-v0-18-adopted.md` | accept with change | DZT migration; IF18 DYAD v6.4.24; IF19 open; recovered editions not adopted lineage. |
| P09 | `20261120-DZT-v0-19-adopted.md` | accept with change | Conditional absolute norm law, sign excluded; Level A, B1/B2 open. |
| P10 | `20261122-ATLAS-programme-receiver-pass.md` | accept | Requested receiving pass completed at adopted scope; not a new Atlas edition. |
| P11 | `20261124-NUMGEN-v1-22-adopted.md` | accept with change | IF13 split pins/evidence; IF14 two grades, IF24 scoped references, IF27 comparison; IF12/37/38 retained. M4 HOLD and Census-1 unchanged. |
| P12 | `20261125-OFN-v0-13-adopted.md` | accept with change | OFN criterion pointer; IF03 actual TDR-G OFN v0.12 pin; IF24/28/31/32 typed uses; IF02 DYAD OFN v0.12 context. No custody change. |
| P13 | `20261125-UVM-v0-7-2-adopted.md` | accept with change | IF08/10/11 current/historical pins; IF09 C3, IF23 retained; IF29 RRF reference only. No physical source delivery. |

All 13 transitions set `state: closed` and `disposition: 2026-11-26 · <verdict> · records/programme/RTG_PROGRAMME_OVERVIEW_v1_5_RELEASE_RECORD.md §3 Pxx`. Sender payloads, objects, tags, routing and other fields stay unchanged. Four earlier closed items remain byte-identical. The 12 accept-with-change verdicts and one accept are the adopted receiving ledger, not new imports. Closing a queue item does not imply that the sender received a reply or that another consumer repinned/adopted a result.

## 3. Checks and exact scope

Regenerated the PROG index connector-side from all seventeen actual item front matters using the read Python parser/rendering contract; original index matches before edits. Validated the 17 original/resulting items against the inspected field, filename, inbox, tag-existence (current GitHub tag refs), disposition and body-length rules. Each of thirteen inverse metadata replacements recovers the exact original bytes, with body and every nonreceiver field unchanged. Proposed PROG has 0 open / 17 closed; global item count remains 183 / 20 inboxes. Exactly fifteen paths: thirteen receiving items, generated PROG index, this dated post-tag record. No adopted DSN, frozen release record, BASELINE, original evidence, Atlas, other inbox/index, or tag changes.

**Pre-merge gate:** Claude independently checks actual scope and native `python3 -I tools/pipes_index.py --check` on a tagged checkout/trial merge, with Programme, Atlas and frozen release record identity checks. Scoped connector validation is not a native full-inbox run; unchanged items outside PROG were not reread. Review and PI-authorized merge pending.

## 4. Separate follow-up

Receiving closeout only; no outgoing items or satellite writes in this PR. Scoped affected-consumer notices can be filed in the ordinary maintenance cycle after checking actual consumer pins and impact; no blanket repin. SAT §6.5 permits relevant RTG owners to file, and Atlas to act on request, not a monitoring duty. The provisional SAT sentence in `pipes/README.md` can be aligned to the adopted §6.5 in a later bounded housekeeping change; no schema or Methodology revision is necessary. This is not a blocker for the 13 closures. Atlas may record the Programme source at its next authorized refresh; no Atlas v0.16.

All five Programme OPENs remain ACTIVE; maturity assignments, guards, actual consumer pins and 38 IF identities remain unchanged. No scientific gate, bridge, custody transfer, UVM C3, NUMGEN M4, physical selection or satellite claim is closed or adopted by this queue change.
