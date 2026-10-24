#!/usr/bin/env python3
"""RECOG v0.3.24 publication transform: publication metadata only (header identity and status lines, the
Appendix A entry heading and its records line, the footer). No live-text change; no claim, grade, RID or
OPEN status is touched. To be run only after the PI's four adoption decisions; the decision date and the
adoption wording are arguments so that nothing is invented here.

usage: release_recog_v0_3_24.py CANDIDATE OUT "DD Month YYYY" "<adoption clause>"
  CANDIDATE = the reviewed stage-2 candidate (SHA-256 63f36a9e…cc35, commit a164704)
  <adoption clause> = the PI's scope wording, e.g. "A1b, A1c, A3 and structural maintenance adopted"
"""
import hashlib, sys

CAND = "63f36a9e4826e92ce6986f9fe722d3a08ac13ff050ce5fbcef2d1ea10866cc35"
PREV = "0d5834003ce8f6819a760ac02ec4e1b65c4d34a0eb13381d0fe4e175af9ca31a"
STAGE1 = "881be125201180b987e1f430390507c10f4167df29c19c0b19fbd07eb6dee03c"

def main(argv):
    cand_p, out_p, date, clause = argv[1:5]
    raw = open(cand_p, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == CAND, "input is not the reviewed stage-2 candidate"
    s = raw.decode("utf-8")
    EDITS = [
     ("# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.23\n", "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.24\n"),
     ("**Date:** 23 October 2026\n", f"**Date:** {date}\n"),
     ("**Document status:** ADOPTED — PI, 23 October 2026 (atlas-advisory corrections and FC-21; Methodology v1.4 compaction, with the live-file exception recorded in the release record §11). Adoption record: `records/recog/RECOG_v0_3_23_RELEASE_RECORD.md`.",
      f"**Document status:** ADOPTED — PI, {date} ({clause}; stage-1 corrections and stage-2 layout compaction reviewed). Adoption record: `records/recog/RECOG_v0_3_24_RELEASE_RECORD.md`."),
     ("**Supersedes:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22` (SHA-256 `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9`; tag `recog-v0.3.22`).",
      f"**Supersedes:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.23` (SHA-256 `{PREV}`; tag `recog-v0.3.23`)."),
     ("**Release record:** `records/recog/RECOG_v0_3_23_RELEASE_RECORD.md`. Version history: Appendix A.",
      "**Release record:** `records/recog/RECOG_v0_3_24_RELEASE_RECORD.md`. Version history: Appendix A."),
     ("### v0.3.24 — DRAFT, stage 1 (corrected intermediate; not adopted)\n", f"### v0.3.24 — {date} — Adopted\n"),
     ("- **Records:** release record `records/recog/RECOG_v0_3_24_RELEASE_RECORD.md`; predecessor tag `recog-v0.3.23` (SHA-256 `0d583400…a31a`).",
      f"- **Compaction [layout]:** SG-R12 reordered to its numerical place (`move`, byte-identical); stage-2 candidate `{CAND[:8]}…{CAND[-4:]}`.\n- **Records:** release record `records/recog/RECOG_v0_3_24_RELEASE_RECORD.md`; stage-1 intermediate (round 2) SHA-256 `{STAGE1[:8]}…{STAGE1[-4:]}`; predecessor tag `recog-v0.3.23` (SHA-256 `0d583400…a31a`)."),
     ("*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.23 (ADOPTED, 23 October 2026).*",
      f"*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.24 (ADOPTED, {date}).*"),
    ]
    for o, n in EDITS:
        assert s.count(o) == 1, o[:60]
        s = s.replace(o, n)
    out = s.encode("utf-8"); open(out_p, "wb").write(out)
    print(hashlib.sha256(out).hexdigest(), len(out), f"{len(EDITS)} metadata edits")

if __name__ == "__main__":
    main(sys.argv)
