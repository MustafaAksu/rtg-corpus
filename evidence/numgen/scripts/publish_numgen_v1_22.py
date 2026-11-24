#!/usr/bin/env python3
"""Status-only NUMGEN v1.22 publication transform.

The PI adopted exactly the round-2 candidate on 24 November 2026.
No scientific text, grade, scope, RID, frozen evidence or OPEN status may change.
Usage: python3 -I evidence/numgen/scripts/publish_numgen_v1_22.py CANDIDATE PUBLISHED
This script is supplied for native reproduction; the initial transform and reverse
check were executed on UTF-8 bytes via the GitHub connector, not by Python.
"""
import hashlib
import sys
from pathlib import Path

CANDIDATE_SHA = "fa28c0abe8bca5e9e7bb307e27ecb8f13c75399a7d804487a7a48b7a8b5c78b9"
PUBLISHED_SHA = "36b31755c1bd73f1d5f69117c63b1556afacc18c2505e1b865b7a3adf512d40b"
PAIRS = [
    ("**Document status:** DRAFT — v1.22 candidate (one content stage: receiving and synchronization), not adopted; v1.21 governs until PI adoption. Release record (DRAFT): `records/numgen/NUMGEN_v1_22_RELEASE_RECORD.md`.  ",
     "**Document status:** ADOPTED — PI, 24 November 2026 (one content stage: receiving and synchronization, including the scoped P2 re-annotation and R1–R4 review repairs). Release record: `records/numgen/NUMGEN_v1_22_RELEASE_RECORD.md`.  "),
    ("**Release record:** `records/numgen/NUMGEN_v1_22_RELEASE_RECORD.md` (DRAFT). Version history: Appendix A.",
     "**Release record:** `records/numgen/NUMGEN_v1_22_RELEASE_RECORD.md`. Version history: Appendix A."),
    ("### v1.22 — 24 November 2026 — DRAFT (not adopted)",
     "### v1.22 — 24 November 2026 — Adopted"),
    ("- **Records:** release record `records/numgen/NUMGEN_v1_22_RELEASE_RECORD.md` (DRAFT); predecessor tag `numgen-v1.21` (`4805760d…5701`).",
     "- **Records:** release record `records/numgen/NUMGEN_v1_22_RELEASE_RECORD.md`; predecessor tag `numgen-v1.21` (`4805760d…5701`)."),
    ("*END OF DOCUMENT — RTG_NUMBER_GENESIS_DSN_v1.22 (DRAFT; not adopted).*",
     "*END OF DOCUMENT — RTG_NUMBER_GENESIS_DSN_v1.22 (ADOPTED, 24 November 2026).*"),
]

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def transform(raw, reverse=False):
    expected = PUBLISHED_SHA if reverse else CANDIDATE_SHA
    if digest(raw) != expected:
        raise ValueError("input SHA-256 differs from the pinned publication object")
    s = raw.decode("utf-8")
    p = [(b, a) for a, b in reversed(PAIRS)] if reverse else PAIRS
    for old, new in p:
        if s.count(old) != 1:
            raise ValueError("publication replacement not unique")
        s = s.replace(old, new)
    out = s.encode("utf-8")
    if digest(out) != (CANDIDATE_SHA if reverse else PUBLISHED_SHA):
        raise ValueError("output SHA-256 differs from the pinned publication object")
    return out

if __name__ == "__main__":
    raw = Path(sys.argv[1]).read_bytes()
    out = transform(raw)
    if transform(out, reverse=True) != raw:
        raise ValueError("reverse publication transform failed")
    Path(sys.argv[2]).write_bytes(out)
    print("PUBLICATION_TRANSFORM_PASS", digest(out))
