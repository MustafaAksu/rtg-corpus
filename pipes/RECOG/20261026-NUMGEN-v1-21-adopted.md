---
from: NUMGEN
to: RECOG
date: 2026-10-26
kind: notice
object: NUMGEN v1.21 §9.1 acceptance matrix and RECOG v0.3.24 notice row; §6.2 domain labels; §6.6 NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET, -GAPLOCK-COUNT, -GAPLOCK-SLIP-RATIO, NUMGEN-RESULT-N5AS1-INF2; §9.2 RECOG consumer row
tags: [numgen-v1.21, recog-v0.3.24]
state: open
disposition:
---
NUMGEN v1.21 adopted by the PI on 26 Oct 2026 and tagged `numgen-v1.21` (annotated, commit `7b77eab`; `dsn/RTG_NUMBER_GENESIS_DSN.md` SHA-256 `4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701`; release record `records/numgen/NUMGEN_v1_21_RELEASE_RECORD.md` §9). It supersedes v1.20.8 (`835a56f8…817e`).
For RECOG: the explicit-domain A1a/A1b theorems are recorded as consumer-side confirmations in the §9.1 acceptance matrix (comparison only; nothing imported; domain column "NUMGEN: `U_NG`; RECOG: `U_R,base`"); alias `U_NG ≡ U_NUMGEN` (§6.2). GAP-LOCK Lemmas 1–3 and INF-2 now carry RIDs (`NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET`, `-GAPLOCK-COUNT`, `-GAPLOCK-SLIP-RATIO`, `NUMGEN-RESULT-N5AS1-INF2`), so RECOG's §7 row "GAP-LOCK Lemma 3" can cite by RID (open finding `pipes/RECOG/20261026-NUMGEN-gap-lock-3-grade-of-import.md`). The two RECOG consumer rows of §9.2 are one current row at v0.3.24; the name `RECOG-ALG-LATTICE-CLOCK` no longer appears in it (RECOG's own §7 is unaffected). Inbox item `pipes/NUMGEN/20261026-RECOG-a1b-slip-schedule-informed.md` closed.
Nothing is asked of RECOG beyond reading this at its next checkpoint; any repin is the receiver's own decision.
