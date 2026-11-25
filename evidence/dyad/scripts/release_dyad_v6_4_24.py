#!/usr/bin/env python3
"""DYAD v6.4.24 publication transform: status lines only (header status, Appendix A heading, footer).
Asserts the reviewed candidate hash (r2, PR #213 head 23e610e; co-owner read-back 5857204402); each old line must occur
exactly once. Prints the final SHA-256 and size, and the number of changed lines (must be 3).
usage: release_dyad_v6_4_24.py CANDIDATE OUT"""
import hashlib, sys
CAND = "014e1ac3be8c21d0e70afb72f23f7592528b01ffc5cd6390628721cc69e98958"
SUMMARY = ("S1 result on RECOG's sharpened R9 rows, three RID registrations, consumer register, bridge-note source, "
           "state of the OPEN 20 analytic-branch pilot")
EDITS = [
 ("**Document status:** DRAFT — v6.4.24 candidate (" + SUMMARY + "); not adopted.",
  "**Document status:** ADOPTED — PI, 11 November 2026 (" + SUMMARY + "). Adoption record: `records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md`."),
 ("### v6.4.24 — 11 November 2026 — Draft candidate", "### v6.4.24 — 11 November 2026 — Adopted"),
 ("*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.24 (DRAFT candidate, 11 November 2026).*",
  "*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.24 (ADOPTED, 11 November 2026).*"),
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
