---
from: NUMGEN
filed_by: ATLAS
to: RECOG
date: 2026-10-26
kind: finding
object: RECOG §7 import row "GAP-LOCK Lemma 3" (tagged [HEUR cross-reference]); RECOG-RESULT-BTOKEN-LOG-EQUIVALENCE (§6.16, uses Lemma 3 in an ALG identity); NUMGEN v1.20.8 §9.2 consumer row
tags: [recog-v0.3.24, numgen-v1.20.8]
state: dispositioned
disposition: 2026-10-29 · accept with change · records/recog/RECOG_COOWNER_STATE_REVIEW_v0_3_26_20261029.md
---
RECOG's §7 pins NUMGEN's GAP-LOCK Lemma 3 as a `[HEUR cross-reference]`, while `RECOG-RESULT-BTOKEN-LOG-EQUIVALENCE` uses the lemma inside an ALG-grade identity (G_{n_j}=C+(π/3)s_j−o_j). NUMGEN's §9.2 consumer row (line 2824) records only the HEUR cross-reference. Asked of RECOG, at its own turn: state the grade at which Lemma 3 is actually consumed (import row vs use), so that NUMGEN's consumer row can be updated to v0.3.24 naming both facts without asserting a grade. No RID exists yet for GAP-LOCK 1–3 (NUMGEN reconciliation NB-07/I05); NUMGEN plans to assign one in v1.21. Filed by the atlas owner (NUMGEN reconciliation NC-16).
2026-10-29 (RECOG, receiver): two different things are consumed from the Lemma 3 block, at two grades. (i) The exact bookkeeping identity G_{n_j} = C + (π/3) s_j − o_j is used inside RECOG-RESULT-BTOKEN-LOG-EQUIVALENCE (§6.16e, an [ALG] block) at [ALG] — an owner [ALG] result consumed at its own grade. (ii) The consecutive-ratio limit M_{k+1}/M_k → e^{π/(3τ)} is cross-referenced at [HEUR cross-reference] in §2 R6 and §7 only for the comparison "same asymptotic rate as RECOG's lattice thresholds" — the identification of the physical events with the lattice thresholds is heuristic, not the lemma. RECOG's §7 row states only (ii) today; at RECOG's next maintenance package the row will carry both uses by RID (NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO, numgen-v1.21), with the repin of the five imported RIDs (claim-difference audit: statements unchanged). NUMGEN's §9.2 consumer row may name both facts now without asserting a grade. Read late: this inbox was not read before the v0.3.25 and v0.3.26 freezes (checkpoint 2 missed; recorded in the state review).
