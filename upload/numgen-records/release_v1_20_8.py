#!/usr/bin/env python3
"""Release transform: RTG_NUMBER_GENESIS_DSN_v1_20_8_DRAFT_r3.md (9d59cfa1…e7b3) -> RTG_NUMBER_GENESIS_DSN_v1_20_8.md.

PI adoption decision, 21 Oct 2026 ("v1.20.8 DRAFT r3 (9d59cfa1…e7b3) adoption için uygundur. benimsiyorum.").
Co-owner delta review of r3: SCIENTIFIC REVIEW ACCEPTED; ARTIFACT VERIFICATION PASSED; PI OWNER ADOPTION READY.
Release scope (co-owner condition): publication metadata only; the r3 scientific body is preserved.
Refuses any input other than r3. Writes the adopted file and release_v1_20_8_edits.json.
"""
import hashlib, json

R3 = "RTG_NUMBER_GENESIS_DSN_v1_20_8_DRAFT_r3.md"
R3_SHA = "9d59cfa1edf15c4e263494c9fbc615dc915ed3b84e556df8ade61fd1fa7de7b3"
OUT = "RTG_NUMBER_GENESIS_DSN_v1_20_8.md"

src = open(R3, encoding="utf-8").read()
assert hashlib.sha256(src.encode()).hexdigest() == R3_SHA, "input is not the reviewed DRAFT r3"

E = []
def edit(i, a, b): E.append((i, a, b))

edit("R1", "# RTG Number Genesis DSN v1.20.8 — DRAFT r3\n", "# RTG Number Genesis DSN v1.20.8\n")
edit("R2", "**Date:** October 21, 2026 (DRAFT r3; v1.20.7 dated September 25, 2026)  \n",
     "**Date:** October 21, 2026 (adopted; v1.20.7 dated September 25, 2026)  \n")
edit("R3", "**Document status:** DRAFT r3 — not adopted. **Maintenance release: consumer synchronization + RID allocation + interface definition.** No theorem-level change. **Supersedes on adoption:** v1.20.7 (`c4637e7a…ab28`, frozen 2026-10-01), which remains the canonical owner until adoption.",
     "**Document status:** ADOPTED owner ledger — PI adoption 21 Oct 2026 on DRAFT r3 (`9d59cfa1…e7b3`) after the co-owner delta review (scientific review accepted; artifact verification passed). **Maintenance release: consumer synchronization + RID allocation + interface definition.** No theorem-level change. **Supersedes:** v1.20.7 (`c4637e7a…ab28`, frozen 2026-10-01), retained unchanged as the prior adopted edition. Release record: `NUMGEN_v1_20_8_RELEASE_RECORD.md`.")
edit("R4", "`NUMGEN-RESULT-N5AS1-INF1`, `NUMGEN-DEF-N5AS1-DEFECT`; canonical on adoption of this edition |",
     "`NUMGEN-RESULT-N5AS1-INF1`, `NUMGEN-DEF-N5AS1-DEFECT`; canonical from the adoption of this edition (21 Oct 2026) |")
edit("R5", "### v1.20.8 — DRAFT r3 — October 21, 2026 (not adopted)\n\n",
     "### v1.20.8 — October 21, 2026 (adopted)\n\n"
     "**Adoption.** PI decision of 21 Oct 2026 on DRAFT r3 (`9d59cfa1…e7b3`), after the co-owner delta review of r3 (scientific review accepted; artifact verification passed; adoption ready; no r4). The release pass changes publication metadata only: title, date, document status, the A1a disposition cell and this heading and paragraph. The six N-5A-S1 RIDs are canonical owner RIDs from this adoption. The draft record follows unchanged.\n\n")

dst = src
for i, a, b in E:
    assert dst.count(a) == 1, (i, dst.count(a)); dst = dst.replace(a, b)
open(OUT, "w", encoding="utf-8").write(dst)
json.dump([{"id": i, "old": a, "new": b} for i, a, b in E], open("release_v1_20_8_edits.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(OUT, hashlib.sha256(dst.encode()).hexdigest(), "edits:", len(E))
