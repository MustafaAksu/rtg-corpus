---
from: GEN
to: UVM
date: 2026-10-26
kind: notice
object: GEN v2.9 §6.8 κ_f := |m||w| (renamed from κ; new [DEF]); B_* declared undefined with unknown sign; GEN-THM-SOURCED-JUNCTION (w=0 algebraic statement, minimizer clause retracted to Appendix B); UVM §0.3/§7 pin v2.8.5 (Programme IF08), UVM R2 uses m=2Q_sB_*
tags: [gen-v2.9, uvm-v0.7.1]
state: open
disposition:
---
Genesis v2.9 (adopted 25 Oct 2026) changed three things UVM imports or reuses: (1) the face-lift magnitude is written κ_f = |m||w| (same quantity as UVM's |mw|; notation only); (2) B_* in m = 2Q_sB_* is declared undefined with unknown sign, so every sgn(m)-dependent statement (9A pole–projector map) is written explicitly; (3) the local sourced-junction theorem is rescoped to its algebraic content at w=0, Δ₃>0 (two antipodal stationary solutions; physical branch OPEN, GCL-02) — the "valid minimizer" clause is retracted. UVM's imports at "RID unavailable" can now point to GEN-THM-QH-NOGO, GEN-THM-SINGLE-FACE-METRIC, GEN-THM-SOURCED-JUNCTION. Nothing is asked now; UVM decides at its own turn whether to repin (Programme IF08 pin stays v2.8.5 until then). Source: GEN v2.9 release record §9 "what would be notified" (`records/gen/GEN_v2_9_RELEASE_RECORD.md`). Filed by the atlas owner on the Genesis owners' behalf.
