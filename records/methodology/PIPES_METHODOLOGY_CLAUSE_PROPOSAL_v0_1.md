# Proposal — Methodology clause for cross-stream pipes (v0.1, for the next Methodology edition)

**Date:** 26 October 2026. **From:** Claude (atlas owner), on the PI's instruction of 26 Oct 2026 ("routing through the PI is unnecessary bureaucracy; co-owners check the pipe at defined points and decide autonomously; an incoming note is only a request or an offer"). **Status:** proposal; Methodology v1.4 is unchanged. The pilot runs under `CONVENTIONS.md` §7 and `pipes/README.md`; after one cycle the PI decides whether this clause enters Methodology v1.5.

## Proposed text (new §13.10 "Cross-stream items", or an addition to §13.5/§13.7)

> **Cross-stream items.** A stream communicates a request, offer, finding, question or notice to another stream by filing an item in the receiver's inbox (`pipes/<STREAM>/`), with the receiver, the object (RIDs/sections at tags), the kind and, where applicable, the work it blocks. An item has no scientific status: the producer remains the owner of the result it cites; the receiver's co-owners read their inbox at the checkpoints of their own cycle — the start of an owner pass, before a stage-1 freeze, before a release record — and decide autonomously what to do (accept, accept with change, reject with reason, defer), recording the verdict in the item and, for any use, in their Import Ledger by RID at the producer edition (§1.1 item 4) or in their release record. No item is routed through, or waits for, the PI; the PI decides adoption of editions, not the handling of items. Filing an item is not sending a notice; the four notice states of CONVENTIONS §7 are derived from the item's `state` and the receiver's ledgers. Release records list the items they filed under "what would be notified".

## Why a clause and not only a convention

Methodology v1.4 §1.1 item 4 already fixes *where* adopted use lives (the consumer's pin per use). What is missing is the rule that cross-stream communication is **asynchronous and owner-decided**: no producer may declare a consumer's use, and no consumer waits for the PI to be allowed to look. Writing that once, in Methodology, removes the "routed through the PI" sentence from CONVENTIONS §7 for good and makes the checkpoints part of every stream's release discipline (§13.5 release checks: "the inbox was read; items dispositioned or deferred are listed").

## Evidence after one cycle (to be attached when the PI decides)

Number of items filed/dispositioned/closed; whether any receiver missed an item at its checkpoint; whether any item was mistaken for adopted use; tool failures. `tools/pipes_index.py` keeps the counts.
