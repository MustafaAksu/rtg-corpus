#!/usr/bin/env python3
"""RECOG v0.3.25 publication transform: publication metadata only (header identity and status lines, the
Appendix A entry heading and its records line, the footer). No live-text change; no claim, grade, RID or
OPEN status is touched. To be run only after the PI's four adoption decisions (B1, A1c-E, A1c-D, A1c-Q); the
decision date and the adoption wording are arguments so that nothing is invented here. `--preview` writes the
would-be file from placeholder arguments for hash inspection only (never to dsn/).

usage: release_recog_v0_3_25.py CANDIDATE OUT "DD Month YYYY" "<adoption clause>"
  CANDIDATE = the reviewed stage-1 round-2 intermediate (SHA-256 657cf302…fe72, commit 92b3333; review #5664522727)
  <adoption clause> = the PI's scope wording, e.g. "four groups adopted: B1 sharpened R9 rows, A1c-E known-a
  sharpened schedule, A1c-D record-only outer decoder, A1c-Q record-fiber structure"
"""
import hashlib, sys

CAND = "657cf302052ea2390ad170d9c03924ce6442b93cc85d076484c769bb0de9fe72"
PREV = "8c64bea231b3691b737f4143f6f4105030ee183fcc90d7f604ec83a4c869e7c1"

def transform(s, date, clause):
    EDITS = [
     ("# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.24\n", "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.25\n"),
     ("**Date:** 24 October 2026\n", f"**Date:** {date}\n"),
     ("**Document status:** ADOPTED — PI, 24 October 2026 (four groups adopted: A1b slip-schedule theorem, A1c infinite-record readout with two OPEN R6 sub-items, A3 quadrature typing and pole-stratum periodic inventory, structural maintenance of the v0.3.23 live-file exception; stage-1 corrections and stage-2 layout compaction reviewed). Adoption record: `records/recog/RECOG_v0_3_24_RELEASE_RECORD.md`.",
      f"**Document status:** ADOPTED — PI, {date} ({clause}; stage-1 round-2 corrections reviewed, review #5664522727; no stage-2 compaction). Adoption record: `records/recog/RECOG_v0_3_25_RELEASE_RECORD.md`."),
     ("**Supersedes:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.23` (SHA-256 `0d5834003ce8f6819a760ac02ec4e1b65c4d34a0eb13381d0fe4e175af9ca31a`; tag `recog-v0.3.23`).",
      f"**Supersedes:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.24` (SHA-256 `{PREV}`; tag `recog-v0.3.24`)."),
     ("**Release record:** `records/recog/RECOG_v0_3_24_RELEASE_RECORD.md`. Version history: Appendix A.",
      "**Release record:** `records/recog/RECOG_v0_3_25_RELEASE_RECORD.md`. Version history: Appendix A."),
     ("### v0.3.25 — DRAFT, stage 1 (corrected intermediate; not adopted)\n", f"### v0.3.25 — {date} — Adopted\n"),
     ("- **Records:** release record `records/recog/RECOG_v0_3_25_RELEASE_RECORD.md` (candidate); predecessor tag `recog-v0.3.24` (SHA-256 `8c64bea2…e7c1`).",
      f"- **Records:** release record `records/recog/RECOG_v0_3_25_RELEASE_RECORD.md`; stage-1 intermediate (round 2) SHA-256 `{CAND[:8]}…{CAND[-4:]}`; predecessor tag `recog-v0.3.24` (SHA-256 `8c64bea2…e7c1`)."),
     ("*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.24 (ADOPTED, 24 October 2026).*",
      f"*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.25 (ADOPTED, {date}).*"),
    ]
    for o, n in EDITS:
        assert s.count(o) == 1, o[:60]
        s = s.replace(o, n)
    return s, len(EDITS)

def main(argv):
    if "--preview" in argv:
        cand_p, out_p = [a for a in argv[1:] if not a.startswith("--")][:2]
        date, clause = "DD Month YYYY", "ADOPTION CLAUSE TO BE SUPPLIED BY THE PI"
    else:
        cand_p, out_p, date, clause = argv[1:5]
    raw = open(cand_p, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == CAND, "input is not the reviewed stage-1 round-2 intermediate"
    s, n = transform(raw.decode("utf-8"), date, clause)
    out = s.encode("utf-8"); open(out_p, "wb").write(out)
    print(hashlib.sha256(out).hexdigest(), len(out), f"{n} metadata edits", "(PREVIEW with placeholders)" if "--preview" in argv else "")

if __name__ == "__main__":
    main(sys.argv)
