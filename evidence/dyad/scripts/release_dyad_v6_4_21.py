#!/usr/bin/env python3
"""DYAD v6.4.21 publication transform: status lines only (header, Appendix A heading, footer).
usage: release_dyad_v6_4_21.py CANDIDATE OUT"""
import hashlib, sys
CAND = "277e640819cc35ce5cb664d396cda1feb675589db49a8d21746be568ead47510"
EDITS = [
 ("**Document status:** DRAFT — v6.4.21 candidate (closeout errata and Methodology v1.4 compaction pilot); not adopted.",
  "**Document status:** ADOPTED — PI, 22 October 2026 (closeout errata and Methodology v1.4 compaction pilot). Adoption record: `records/dyad/RTG_DYADIC_v6_4_21_RELEASE_RECORD.md`."),
 ("### v6.4.21 — 22 October 2026 — DRAFT candidate", "### v6.4.21 — 22 October 2026 — Adopted"),
 ("*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.21 (DRAFT candidate, 22 October 2026).*",
  "*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.21 (ADOPTED, 22 October 2026).*"),
]
raw = open(sys.argv[1], "rb").read()
assert hashlib.sha256(raw).hexdigest() == CAND
s = raw.decode()
for o, n in EDITS:
    assert s.count(o) == 1, o
    s = s.replace(o, n)
out = s.encode(); open(sys.argv[2], "wb").write(out)
print(hashlib.sha256(out).hexdigest(), len(out))
