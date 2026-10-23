#!/usr/bin/env python3
"""Publication transform for Programme Overview v1.3: status lines only.

Input must be the reviewed stage-2 candidate (01199132…2a35). Three exact-once edits: header Document status,
Appendix A v1.3 heading, footer. Nothing else changes; the diff is printed by the release record's reproduce line.

usage (repository root): release_programme_v1_3.py CANDIDATE OUT
"""
import hashlib, sys

CAND_SHA = "01199132609a4782dbce1f572d65e2fd1406857db3835c21eb8a7edd43215a35"
EDITS = [
 ("**Document status:** DRAFT — v1.3 candidate (stage 1: corrections; stage 2: compaction); not adopted. `programme-v1.2` governs until adoption.",
  "**Document status:** ADOPTED — PI, 24 October 2026 (pass-two synchronization of the v1.2 architecture under Methodology v1.4; adoption record `records/programme/RTG_PROGRAMME_OVERVIEW_v1_3_RELEASE_RECORD.md`). Supersedes `programme-v1.2`."),
 ("### v1.3 — 23 October 2026 — DRAFT candidate", "### v1.3 — 24 October 2026 — Adopted"),
 ("*END OF DOCUMENT — RTG_PROGRAMME_OVERVIEW_v1.3 (DRAFT candidate, 23 October 2026; pass-two synchronization of the adopted v1.2 architecture under DSN Methodology v1.4; `programme-v1.2` governs until adoption).*",
  "*END OF DOCUMENT — RTG_PROGRAMME_OVERVIEW_v1.3 (ADOPTED, 24 October 2026; pass-two synchronization of the adopted v1.2 architecture under DSN Methodology v1.4).*"),
]

def sha(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()

def main(inp, out):
    s = open(inp, encoding="utf-8").read()
    assert sha(s) == CAND_SHA, "input is not the reviewed candidate"
    for old, new in EDITS:
        assert s.count(old) == 1, old[:60]
        s = s.replace(old, new)
    open(out, "w", encoding="utf-8").write(s)
    print(sha(s), len(s.encode("utf-8")), "bytes")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
