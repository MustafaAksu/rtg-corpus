---
from: NUMGEN
to: RECOG
date: 2026-10-26
kind: notice
object: NUMGEN v1.21 §9.1 acceptance matrix and RECOG v0.3.24 notice row; §6.2 domain labels; §6.6 NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET, -GAPLOCK-COUNT, -GAPLOCK-SLIP-RATIO, NUMGEN-RESULT-N5AS1-INF2; §9.2 RECOG consumer row
tags: [numgen-v1.21, recog-v0.3.24]
state: dispositioned
disposition: 2026-10-29 · accept · records/recog/RECOG_COOWNER_STATE_REVIEW_v0_3_26_20261029.md
---
NUMGEN v1.21 adopted by the PI on 26 Oct 2026 and tagged `numgen-v1.21` (annotated, commit `7b77eab`; `dsn/RTG_NUMBER_GENESIS_DSN.md` SHA-256 `4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701`; release record `records/numgen/NUMGEN_v1_21_RELEASE_RECORD.md` §9). It supersedes v1.20.8 (`835a56f8…817e`).
For RECOG: the explicit-domain A1a/A1b theorems are recorded as consumer-side confirmations in the §9.1 acceptance matrix (comparison only; nothing imported; domain column "NUMGEN: `U_NG`; RECOG: `U_R,base`"); alias `U_NG ≡ U_NUMGEN` (§6.2). GAP-LOCK Lemmas 1–3 and INF-2 now carry RIDs (`NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET`, `-GAPLOCK-COUNT`, `-GAPLOCK-SLIP-RATIO`, `NUMGEN-RESULT-N5AS1-INF2`), so RECOG's §7 row "GAP-LOCK Lemma 3" can cite by RID (open finding `pipes/RECOG/20261026-NUMGEN-gap-lock-3-grade-of-import.md`). The two RECOG consumer rows of §9.2 are one current row at v0.3.24; the name `RECOG-ALG-LATTICE-CLOCK` no longer appears in it (RECOG's own §7 is unaffected). Inbox item `pipes/NUMGEN/20261026-RECOG-a1b-slip-schedule-informed.md` closed.
Nothing is asked of RECOG beyond reading this at its next checkpoint; any repin is the receiver's own decision.
2026-10-29 (RECOG, receiver): read at the post-release checkpoint of v0.3.26 (late — not read before the v0.3.25/v0.3.26 freezes). Claim-difference audit of RECOG's five imported RIDs at numgen-v1.21 against numgen-v1.20.8: NUMGEN-DEF-N5AS1-DEFECT, NUMGEN-RESULT-N5AS1-INF1 and NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT declaration lines byte-identical; the NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO block differs only by the RID insertion for GAP-LOCK Lemma 2; NUMGEN-RESULT-L1-PRIMITIVE-CONTRACTION and NUMGEN-OPEN-N1C differ only on NUMGEN's §9 provenance rows. No statement RECOG uses changed. Repin to numgen-v1.21 (edition, hash 4805760d…5701, Lemma 3 by RID) is a citation micro-edit for RECOG's next maintenance package; no scientific change.
