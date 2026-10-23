#!/usr/bin/env python3
"""DYAD v6.4.22 publication transform: status lines only (header status, Appendix A heading, footer).
Asserts the reviewed candidate hash; each old line must occur exactly once. Prints the final SHA-256 and size,
and the number of changed lines (must be 3).
usage: release_dyad_v6_4_22.py CANDIDATE OUT"""
import hashlib, sys
CAND = "c6cb222f6f6f58a5d3c1fe269f8b2b86c62131657f464a2e55d09e362cada95a"
EDITS = [
 ("**Document status:** DRAFT — v6.4.22 candidate (owner errata: current-state wording, owner labels for RECOG R11 and OPEN-M R11, three wordings, second-route $h_4$ evidence); not adopted.",
  "**Document status:** ADOPTED — PI, 23 October 2026 (owner errata: current-state wording, owner labels for RECOG R11 and OPEN-M R11, three wordings, second-route $h_4$ evidence). Adoption record: `records/dyad/RTG_DYADIC_v6_4_22_RELEASE_RECORD.md`."),
 ("### v6.4.22 — 23 October 2026 — DRAFT candidate", "### v6.4.22 — 23 October 2026 — Adopted"),
 ("*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 (DRAFT candidate, 23 October 2026).*",
  "*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 (ADOPTED, 23 October 2026).*"),
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
