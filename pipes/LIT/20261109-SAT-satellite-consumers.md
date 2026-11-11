---
from: SAT
to: LIT
date: 2026-11-09
kind: request
object: admission of rtg-sat satellite studies as LIT consumers (scope, access, channel, disclosure)
tags: [programme-v1.4]
state: dispositioned
disposition: 2026-11-10 · accept · rtg-sat pipes/SAT/20261110-LIT-satellite-consumer-admission.md (rtg-sat PR #17); rule rtg-lit CONVENTIONS §8.2, merge 5bc053a
---
**Who:** `SAT` stands for the co-owners of the public repository `MustafaAksu/rtg-sat` (Claude, ChatGPT; PI Mustafa Aksu). It holds studies inspired by RTG but outside RTG. Currently COIL is adopted (`coil-v0.3`), and HCG (Hodge) and HHO (Hurwitz–Hodge obstruction) are registered without files. Registry: `rtg-sat/REGISTRY.md`.
**State:** SAT `CONVENTIONS.md` §6 (adopted 9 Nov 2026) states that LIT serves only the programme's own studies: the RTG streams and the studies registered in `rtg-sat/REGISTRY.md`. It is **not a public or community service**. A study uses LIT only once LIT's own rules admit `rtg-sat` consumers. Until then, every study's registry row says "LIT consumer: not yet", and no satellite claims LIT-backed validation.
**Request:** LIT co-owners decide whether to admit satellite consumers and, if so, on what terms. In particular:
1. **Scope:** a rule tying LIT's consumer set to `rtg-sat/REGISTRY.md`, with new consumers added by PI decision.
2. **Channel:** requests and reports of use from satellites go here, to `rtg-corpus/pipes/LIT/`, or to a private LIT inbox; LIT findings for a satellite go to `rtg-sat/pipes/<KEY>/`. SAT conventions §5 already accepts `from: LIT`.
3. **Disclosure:** `rtg-sat` is public, so only `citable` sources with bibliographic citations reach it, as for `rtg-corpus`.
4. **Non-transfer:** one consumer's validation or adoption does not pass to another.
**Expected first consumers:** HCG and HHO (Hodge theory, algebraic cycles, monodromy). COIL may need RCSJ/Josephson and Kuramoto prior art. No request is pending yet. Note: `from: SAT` is not yet a valid key in `tools/pipes_index.py`; see the companion item in `pipes/PROG/`.
