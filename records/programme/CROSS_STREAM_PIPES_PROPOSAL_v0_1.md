# Cross-stream pipes — proposal v0.1 (for PI decision)

**Date:** 26 October 2026. **From:** Claude (atlas owner). **To:** the PI. **Status:** proposal; nothing is created until the PI decides. Answers the PI's two questions of 26 Oct 2026: "let us put cross-stream exchange on a standard" and "streams should have in/out pipes; a finding or expectation is written there".

## 1. What exists already

- Methodology v1.4: imports are recorded by the **consumer** in its Import Ledger by RID, at the producer edition actually used (`[import: …]`; §1.1 item 4 one current pin per use); OPEN records carry consumer fields; release records list "what would be notified".
- `CONVENTIONS.md` §7: a notice has four states per recipient — **sent, received, statement accepted, adopted use**; pending consumer decisions do not block the sender's release; notices are routed through the PI.
- PI decisions so far: no notices are sent during the first round of owner passes; requests to other streams are not forwarded now (26 Oct); an item that concerns a stream is looked at when that stream's turn comes.
- Practice of the last ten days: the atlas advisories, the Genesis and RECOG release records and the NUMGEN reconciliation each produced items addressed to *another* stream (e.g. NUMGEN → TDR-G orientation policy; Genesis → UVM κ_f/B_*; RECOG → NUMGEN A1b "informed"; Programme E-P13-1/E-P13-2). Today they live in six different records and reach a stream only if someone remembers them.

## 2. Proposal: one inbox per stream, written by anyone, read by the owner at its turn

**Layout.** `pipes/<stream>/` with one file per item, fixed name `pipes/<stream>/<YYYYMMDD>-<from>-<slug>.md`, and one generated index `pipes/<stream>/INDEX.md` (a tool rebuilds it; never hand-edited). No "out" folder: an outgoing item of stream A is simply a file in stream B's inbox whose `from` is A — the sender's record is the same file, so nothing is written twice. A stream's own release record keeps listing "what would be notified" (CONVENTIONS §7) by pointing at the pipe files it created.

**Item schema** (YAML front matter, then a short body):

```
from: NUMGEN            # stream or atlas; sessions sign with their stream, not their model
to: TDRG
date: 2026-10-26
kind: finding | request | offer | notice | question
object: TDRG §6 TDRG-ORIENT; NUMGEN v1.20.8 §6.6 lines 1901–1945   # RIDs/sections at tags
tags: [numgen-v1.20.8, tdrg-v2.12.13]
state: open            # open → acknowledged → dispositioned → closed   (receiver changes it)
blocks: C7C-M4 realization campaign          # optional: what the sender holds pending the answer
disposition:           # filled by the receiver, with date and record pointer
---
One to ten lines: the finding or expectation, with the owner lines quoted or cited, and what the sender
needs (a decision, a RID, a scope sentence, nothing).
```

**Rules.**
1. Anyone with repository access may write an item (on a `<stream>/*` or `claude/*`/`chatgpt/*` branch, PR as usual); only the **receiving owner** changes `state` and fills `disposition`, and only when that stream's turn comes or the PI asks for it earlier. Writing an item is not "sending a notice": nothing is expected of the receiver until then (this keeps the PI's current rule).
2. One item, one question. Scientific content stays in the owner DSNs and records; the pipe item cites them. No hashes, RIDs or approvals are invented; "not available" is written as such.
3. The four CONVENTIONS §7 states map onto `state`: *sent* = file exists; *received* = `acknowledged`; *statement accepted* = `dispositioned` with the receiver's verdict (accept / accept with change / reject / defer); *adopted use* = `closed` with a pointer to the receiver's release record or Import Ledger row.
4. The custody standard for the exchange itself (the PI's question 3): the **producer stays owner**; a consumer that uses a result records it in its own Import Ledger by RID at the producer edition (Methodology v1.4) — that row is the only place "adopted use" is asserted; a consumer that *independently proves* a statement on its own domain (RECOG's explicit-U theorems vs NUMGEN's) records it under its own RID with a "consumer-side confirmation, no custody change" sentence, and the producer records it in a **Consumers** block as *independent agreement*, never as its own theorem. The pipe item is where the hand-off is proposed; the two ledgers are where it is settled.
5. The atlas reads the pipes like any record: open items become `~` edges or diagnostics; closed items retire them. The Programme's interface register (§7.2) stays the owner-declared truth; the pipes are the working queue in front of it.
6. Tool: `tools/pipes_index.py` rebuilds every `INDEX.md` (one table per stream: date, from, kind, state, object, file) and checks the schema (front matter fields, allowed `state` values, `from`/`to` are known stream keys, tags are existing git tags). Negative controls: unknown stream key, invalid state, hand-edited index.

**Why now rather than after the first round.** The NUMGEN cycle has four items that already need a home (TDR-G orientation policy / C7C-M4 hold; RECOG GAP-LOCK grade tension; Genesis cyclic-average RID for G₂=0; Dyadic q* cross-citation), the Genesis cycle left two (UVM κ_f/B_*, Programme κ_f row), RECOG left one (NUMGEN "informed" of A1b). Writing them into pipes now costs one PR and changes nothing in the PI's rule that receivers act only at their turn; it removes the risk that they are forgotten by then. If the PI prefers to wait, the same seven items are listed in §4 of this record and the proposal is re-read after the first round.

## 3. What is not proposed

No automatic notifications, no obligation on receivers, no change to Methodology or CONVENTIONS text until the pipes have run for one cycle (then a one-paragraph §7 amendment: "notices are written to the receiver's pipe; the PI decides when a stream reads its inbox"). No science in pipes. No merging of pipes with the Programme's §7.2 register.

## 4. Items that would be filed on day one

| to | from | kind | object | blocks |
|---|---|---|---|---|
| TDRG | NUMGEN (via atlas reconciliation I06) | request | orientation policy at S=0, \|E\|=N/2 (TDRG-ORIENT); 40/136 DISC-2 witnesses | NUMGEN C7C-M4 |
| RECOG | NUMGEN/atlas (NC-16) | finding | GAP-LOCK Lemma 3 import tagged HEUR in §7 while used at ALG in RECOG-RESULT-BTOKEN-LOG-EQUIVALENCE | — |
| GEN | NUMGEN/atlas (NC-15) | offer | first-nonlinear cyclic-average theorem as an independent route to G₂=0 (GEN-ART-G2-CHRONO custody (a) missing) | — |
| DYAD | NUMGEN/atlas (NC-17) | question | DYAD-THM-OPEN18 branch split q_* vs NUMGEN q*≈0.3156258836 — same object? | — |
| UVM | GEN (release record §9) | notice | κ_f = \|m\|\|w\| renaming; B_* undefined; sourced-junction rescoping | UVM repin |
| PROG | GEN/atlas (PROG.G8) | finding | §8.2 κ table lacks κ_f row; E-P13-1 | next Programme edition |
| NUMGEN | RECOG (§6.13b "NUMGEN is informed") | notice | A1b slip schedule on explicit U; GAP-LOCK/INF-1 custody unchanged | — |

## 5. Decision asked of the PI

(a) Adopt the layout and schema of §2 now (atlas owner creates `pipes/`, the index tool and the seven day-one items in one PR; receivers do nothing until their turn), or (b) keep this proposal on file and revisit after the first round of owner passes.
