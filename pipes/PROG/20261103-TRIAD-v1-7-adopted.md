---
from: TRIAD
to: PROG
date: 2026-11-03
kind: notice
object: Triadic v1.7 adopted; interface register IF07 (TRIAD → GEN) and IF11 (TRIAD → UVM) pin v1.6; CN-05 Programme/OFN note (§7.4)
tags: [triad-v1.7, programme-v1.3]
state: closed
disposition: 2026-11-04 · accept · records/programme/RTG_PROGRAMME_OVERVIEW_v1_4_RELEASE_RECORD.md
---
Triadic v1.7 was adopted by the PI on 3 Nov 2026 and tagged `triad-v1.7`. The DSN SHA-256 is `506f3403…e64a`; the release record is `records/triad/TRIAD_v1_7_RELEASE_RECORD.md`.

**Your pin.** Programme v1.3 lists Triadic v1.6.1 in its inventory, while the interface register rows IF07 and IF11 still pin v1.6.

**Your CN-05 entry.** Triadic §7.4 records "not recorded" for Programme. v1.3 is the Programme's pass-two edition, but it carries no CN-05 disposition.

What would help at the next Programme pass: one CN-05 line (accept, or no action), and the IF07/IF11 pins updated. Nothing blocks on this.
2026-11-04 (PROG): CN-05 received and accepted, no action (Programme v1.4 §7.3): no Programme statement uses the withdrawn T-6 sector, wedge, basin, phase-steering or route-obstruction exports, and the Programme issues no cascade verdict, source deficit or ontology selection. IF07 now carries Genesis's pin v1.7; IF11 stays v1.6 because it is OPEN M's own pin (`uvm-v0.7.1`), which the Programme records and does not set. Triadic listed at `triad-v1.7` (§6.1). Item closed.
