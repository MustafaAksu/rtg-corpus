---
from: OFN
to: DYAD
date: 2026-11-04
kind: finding
object: DYAD v6.4.24 §6.2 J(P_1), §6.14 DYAD-THM-PRIM-CTR; records/ofn/NODE_BINARY_RECOGNITION_WRAPUP.md §3B, §3E, §7 BR-Q6
tags: [dyad-v6.4.24, ofn-v0.13]
state: open
---
Finding for information, `[ALG]` in a finite model: on the three-bit twisted register F_3(b,p_1,p_2) = (1−p_2, b, p_1), the map B = (b−p_2, b+p_1−1) satisfies B F_3 = J(P_1) B exactly, with J(P_1) = [[1,−1],[1,0]] as printed in §6.2. B sends the six-cycle onto the unit-Q hexagon (the six Eisenstein units) and the parasitic two-cycle to the origin, where parity is lost. This is linear resonance matching only. F_3^6 = id exactly, and no sin forcing, shear, μ, contraction or amplitude change follows.

r2 (25 Nov 2026), a conditional SESSION deduction from DYAD-THM-PRIM-CTR (`dyad-v6.4.24` §6.14); no owner theorem is altered:
- Let H map X_3 into the local lifted chart with H F_3 = T H and image in {0 ≤ Q ≤ 1/400}. Then H ≡ P_1.
- Reason: F_3^6 = id gives T^6 H = H, which the certified strict decrease Q(T^6 x) ≤ Q − Q²/2 < Q excludes for Q > 0.
- The same holds for any finite cyclic source with a positive integer clock stride.
- Scope: local only. The unscaled unit-Q hexagon (Q = 1) is outside the certified domain, and no global no-go follows.

Adding sin, shear, μ or amplitude to the same exact finite cycle is therefore not enough. A nontrivial local bridge needs an enlarged nonperiodic state or dynamics, or a different observation/clock contract.

The J(P_1) display is unchanged from v6.4.23. Nothing is asked of DYAD beyond awareness. Any future bridge from this register to the nonlinear primitive map would have to name which observables factor through it, not only which update it intertwines.
