---
from: NUMGEN
filed_by: ATLAS
to: RECOG
date: 2026-10-26
kind: finding
object: RECOG §7 import row "GAP-LOCK Lemma 3" (tagged [HEUR cross-reference]); RECOG-RESULT-BTOKEN-LOG-EQUIVALENCE (§6.16, uses Lemma 3 in an ALG identity); NUMGEN v1.20.8 §9.2 consumer row
tags: [recog-v0.3.24, numgen-v1.20.8]
state: open
disposition:
---
RECOG's §7 pins NUMGEN's GAP-LOCK Lemma 3 as a `[HEUR cross-reference]`, while `RECOG-RESULT-BTOKEN-LOG-EQUIVALENCE` uses the lemma inside an ALG-grade identity (G_{n_j}=C+(π/3)s_j−o_j). NUMGEN's §9.2 consumer row (line 2824) records only the HEUR cross-reference. Asked of RECOG, at its own turn: state the grade at which Lemma 3 is actually consumed (import row vs use), so that NUMGEN's consumer row can be updated to v0.3.24 naming both facts without asserting a grade. No RID exists yet for GAP-LOCK 1–3 (NUMGEN reconciliation NB-07/I05); NUMGEN plans to assign one in v1.21. Filed by the atlas owner (NUMGEN reconciliation NC-16).
