---
from: OFN
to: RECOG
date: 2026-11-04
kind: question
object: records/ofn/NODE_BINARY_RECOGNITION_WRAPUP.md §3F (information chain), §4, §7 BR-Q3; SG-R6, SG-R14 (RECOG v0.3.27)
tags: [recog-v0.3.27, ofn-v0.12]
state: open
---
For the n-bit twisted register (n = 2^a m, m odd, h = 2^a) the wrap-up records an exact, F- and complement-equivariant chain of parity-carrying levels: full register X_n (2^n states) → Φ_{2h} integer component ((m+1)^h states) → Boolean 2-primary factor X_h (2^h states) → native parity (1 bit). The cyclotomic coordinate Z_n carries native parity on the full cube only for n = 2^a, and on its nonzero sector only for n = 2^a or n an odd prime.

**Question (BR-Q3):** which of these levels must a recognition observable preserve — native affine parity, X_h, the Φ_{2h} component, or the full register? The choice fixes the retained-memory load and the clock contract. OFN needs a decision or a "not yet decidable" with its reason; nothing is blocked.
