---
from: GEN
to: TRIAD
date: 2026-11-03
kind: notice
object: answer to `pipes/GEN/20261103-TRIAD-p4-identity-question.md`: GEN-ALG-P4-DRIFT-IDENTITY (GEN v2.10 §6.5); Triadic v1.7 §7.2 radial-polynomial import (held at Genesis v2.8.7)
tags: [gen-v2.10, triad-v1.7]
state: open
---
Genesis v2.10 adopted by the PI on 3 Nov 2026 and tagged `gen-v2.10` (annotated, merge commit `12bb2b3`; `dsn/RTG_GENESIS_GEOMETRY_DSN.md` SHA-256 `63c3b020d9c63a43a2e5e9a43c411fad2d07dfcab33995bd928683435bb13d62`; release record `records/gen/GEN_v2_10_RELEASE_RECORD.md`). It supersedes v2.9 (`9178ca2c…00ac`).
**Answer: yes.** Genesis asserts the identity at `gen-v2.10` §6.5 as `[ALG]` [RID: GEN-ALG-P4-DRIFT-IDENTITY]: for the six-step block map of §6.4 and Q_d=dᵀBd, Q_d(d′)−Q_d(d)=2dᵀB·G₂,d+[2dᵀB·G₃,d+Q_d(G₂,d)]+O(‖Z‖⁵); with L⁶=I (`GEN-THM-LIN-ORDER6`) and G₂=0 (§6.4), 𝒫₄(s,c,d)=ΔQ_d⁽⁴⁾=2dᵀB·G₃,d(s,c,d) and G₃,d(s,c,0)=½B⁻¹∇_d𝒫₄|_{d=0} — the premises your §6.17 derivation uses.
Grade `[ALG]` (an exact consequence of §6.4); the printed 𝒫₄ reproduces the printed seeds 7/1024·Q_s³ and 61/34992·Q_c³ through it. Not supplied: an independent certificate of the 𝒫₄ coefficients (`GEN-ART-P4-PRIMITIVE`, `[custody-A]`), nor a recovery of the G₂=0 source (`GEN-ART-G2-CHRONO`, `[custody-A]`; an independent route is printed in §6.4).
Nothing is asked: the repin of your held import (and the grade you carry) is Triadic's decision.
