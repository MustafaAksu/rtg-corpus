#!/usr/bin/env python3
"""RECOG v0.3.23 publication transform: status lines only (header document status, Appendix A heading, footer).
usage: release_recog_v0_3_23.py CANDIDATE OUT"""
import hashlib, sys
CAND = "771f87f29e57c51c0d88eee945f9cbe673fa6b131b4f9d45c195579f835ebf9c"
EDITS = [
 ("**Document status:** DRAFT — v0.3.23 candidate (atlas-advisory corrections and FC-21, stage 1, reviewed; Methodology v1.4 compaction, stage 2); not adopted.",
  "**Document status:** ADOPTED — PI, 23 October 2026 (atlas-advisory corrections and FC-21; Methodology v1.4 compaction, with the live-file exception recorded in the release record §11). Adoption record: `records/recog/RECOG_v0_3_23_RELEASE_RECORD.md`."),
 ("### v0.3.23 — 23 October 2026 — DRAFT candidate", "### v0.3.23 — 23 October 2026 — Adopted"),
 ("*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.23 (DRAFT candidate, 23 October 2026).*",
  "*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.23 (ADOPTED, 23 October 2026).*"),
]
raw = open(sys.argv[1], "rb").read()
assert hashlib.sha256(raw).hexdigest() == CAND, "input is not the reviewed stage-2 candidate"
s = raw.decode("utf-8")
for o, n in EDITS:
    assert s.count(o) == 1, o
    s = s.replace(o, n)
out = s.encode("utf-8"); open(sys.argv[2], "wb").write(out)
print(hashlib.sha256(out).hexdigest(), len(out))
