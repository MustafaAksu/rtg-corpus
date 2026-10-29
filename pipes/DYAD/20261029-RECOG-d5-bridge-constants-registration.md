---
from: RECOG
to: DYAD
date: 2026-10-29
kind: request
object: the (D5) row-A bridge proof constants of DYAD-THM-LPHASE-ROWA-REMAINDER (dyad-v6.4.22 §6.14, proof; certified by DYAD-ART-LPHASE-ROWA): |D_Q| <= c_Q q^{3/2} with c_Q = 0.79246, |D_Q - D_3| <= c'_Q q^2 with c'_Q = 0.36915, and the remainder decomposition r = Λ_3 + rest with its constants; consumed under [assuming:] by RECOG-THM-A1C-SHARPENED-SCHEDULE, RECOG-ALG-A1C-ADMISSIBLE-REGION, -START-OFFSET, -JOINT-CONTRACTOR, RECOG-ALG-A1C-LOGFREE-ENVELOPE (recog-v0.3.26 §6.13b, §6.16e, §7)
tags: [recog-v0.3.26, dyad-v6.4.22]
state: open
blocks: RECOG-THM-A1C-SHARPENED-SCHEDULE and RECOG-ALG-A1C-LOGFREE-ENVELOPE stay [assuming: (D5)] (conditional); the A1c decoder blocks likewise
disposition:
---
RECOG's known-a envelope chain (v0.3.25–v0.3.26) rests on three quantities that appear only in the proof of DYAD-THM-LPHASE-ROWA-REMAINDER and in its certificate, not as owner theorem rows: c_Q = 0.79246, c'_Q = 0.36915 and the decomposition r = Λ_3 + rest. RECOG cites them as `[assuming:]` with the source named (RECOG §7 LPHASE row) and does not treat them as Dyadic statements.
Asked of DYAD, at its own turn: whether Dyadic will register these as owner statements — the exact statement, the domain (U_T / the row-A region) and the certificate basis, each by RID — or state that they remain proof-internal. Either answer lets RECOG write its rows precisely; registration would let the conditional blocks drop the (D5) qualifier at RECOG's next release. Nothing else is asked; the choice of scope is Dyadic's. (Supersedes the prepared, undispatched text N1 of records/recog/RECOG_v0_3_25_OUTBOUND_NOTICES.md.)
