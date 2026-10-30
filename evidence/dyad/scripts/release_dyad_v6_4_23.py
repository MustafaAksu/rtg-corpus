#!/usr/bin/env python3
"""DYAD v6.4.23 publication transform: status lines only (header status, Appendix A heading, footer).
Asserts the reviewed candidate hash (r2, PR #132 head 5894fae); each old line must occur exactly once. Prints the final
SHA-256 and size, and the number of changed lines (must be 3).
usage: release_dyad_v6_4_23.py CANDIDATE OUT"""
import hashlib, sys
CAND = "5e55602fd858c81cdd7400f1d244be1c712e770745c55decd60c28d33b45d7fb"
EDITS = [
 ("**Document status:** DRAFT — v6.4.23 candidate (inbox round D1–D7: OPEN 18 step-indexed successor RID, two registrations for RECOG, displayed-decimal corrections, consumer register); not adopted.",
  "**Document status:** ADOPTED — PI, 30 October 2026 (inbox round D1–D7: OPEN 18 step-indexed successor RID, two registrations for RECOG, displayed-decimal corrections, consumer register). Adoption record: `records/dyad/RTG_DYADIC_v6_4_23_RELEASE_RECORD.md`."),
 ("### v6.4.23 — 30 October 2026 — Draft candidate", "### v6.4.23 — 30 October 2026 — Adopted"),
 ("*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.23 (DRAFT candidate, 30 October 2026).*",
  "*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.23 (ADOPTED, 30 October 2026).*"),
]
raw = open(sys.argv[1], "rb").read()
assert hashlib.sha256(raw).hexdigest() == CAND, "not the reviewed candidate"
s = raw.decode()
for o, n in EDITS:
    assert s.count(o) == 1, o
    s = s.replace(o, n)
a, b = raw.decode().split("\n"), s.split("\n")
changed = sum(x != y for x, y in zip(a, b))
assert len(a) == len(b) and changed == 3, changed
out = s.encode(); open(sys.argv[2], "wb").write(out)
print(hashlib.sha256(out).hexdigest(), len(out), "changed lines", changed)
