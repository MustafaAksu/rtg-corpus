#!/usr/bin/env python3
"""RECOG v0.3.27 publication transform: publication metadata only (header identity and status lines, the Appendix A entry
heading and its records line, the footer). No live-text change; no claim, grade, RID, [COR] note, Appendix B entry or OPEN status
is touched. To be run only after the PI's separate decisions on the groups R1 (c'_Q = 0.36916 and the owner rerun), D5B (R2 option
(b): the (D5) qualifier discharged through RECOG-ALG-A1C-JET-REMAINDER-BOUNDS) or D5A (fallback (a)), C7 (R3: C7-SHARP import),
DISP (item 7: eight safe-direction displays) and PIN (R4-R6: pins and receipts). The decision date, the review number and the
adoption wording are arguments so that nothing is invented here. If the PI adopts another combination (for example R1+D5A), the
matching variant in `evidence/recog/v0.3.27/variants/` is the candidate instead and CAND must be set to its hash in a reviewed
follow-up commit. `--preview` writes the would-be file from placeholder arguments for hash inspection only (never to dsn/).

usage: release_recog_v0_3_27.py CANDIDATE OUT "DD Month YYYY" "<review number>" "<adoption clause>"
  CANDIDATE = the reviewed stage-1 intermediate (groups R1, D5B, C7, DISP, PIN; SHA-256 in CAND below)
"""
import hashlib, sys

CAND = "63acd5fff83cb116115f6eab0688372f9ebf6792bc43191b50274d8319a21df3"
PREV = "45e307f8333c81a344158ada07ad34a1a3afab6e1b93b2aa04ee09f84878dd34"

def transform(s, date, review, clause):
    EDITS = [
     ("# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.26\n", "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.27\n"),
     ("**Date:** 28 October 2026\n", f"**Date:** {date}\n"),
     ("**Document status:** ADOPTED — PI, 28 October 2026 (three groups adopted: CORR asymptotic corrections (Appendix B), DRIFT chart reciprocal drift centring, ENV log-free centred envelope under (D5); stage-1 reviewed, review #5689280577; no stage-2 compaction). Adoption record: `records/recog/RECOG_v0_3_26_RELEASE_RECORD.md`.",
      f"**Document status:** ADOPTED — PI, {date} ({clause}; stage-1 reviewed, review #{review}; no stage-2 compaction). Adoption record: `records/recog/RECOG_v0_3_27_RELEASE_RECORD.md`."),
     ("**Supersedes:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.25` (SHA-256 `86cae8ff094d63d077ec5c0887451775ec3a26485cfad95833d8390bda4bd7db`; tag `recog-v0.3.25`).",
      f"**Supersedes:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.26` (SHA-256 `{PREV}`; tag `recog-v0.3.26`)."),
     ("**Release record:** `records/recog/RECOG_v0_3_26_RELEASE_RECORD.md`. Version history: Appendix A.",
      "**Release record:** `records/recog/RECOG_v0_3_27_RELEASE_RECORD.md`. Version history: Appendix A."),
     ("### v0.3.27 — DRAFT, stage 1 (maintenance intermediate; not adopted)\n", f"### v0.3.27 — {date} — Adopted\n"),
     ("- **Records:** release record `records/recog/RECOG_v0_3_27_RELEASE_RECORD.md` (candidate); predecessor tag `recog-v0.3.26` (SHA-256 `45e307f8…dd34`).",
      f"- **Records:** release record `records/recog/RECOG_v0_3_27_RELEASE_RECORD.md`; stage-1 intermediate SHA-256 `{CAND[:8]}…{CAND[-4:]}`; predecessor tag `recog-v0.3.26` (SHA-256 `45e307f8…dd34`)."),
     ("*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.26 (ADOPTED, 28 October 2026).*",
      f"*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.27 (ADOPTED, {date}).*"),
    ]
    for o, n in EDITS:
        assert s.count(o) == 1, o[:60]
        s = s.replace(o, n)
    return s, len(EDITS)

def main(argv):
    if "--preview" in argv:
        cand_p, out_p = [a for a in argv[1:] if not a.startswith("--")][:2]
        date, review, clause = "DD Month YYYY", "NNNNNNNNNN", "ADOPTION CLAUSE TO BE SUPPLIED BY THE PI"
    else:
        cand_p, out_p, date, review, clause = argv[1:6]
    raw = open(cand_p, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == CAND, "input is not the reviewed stage-1 intermediate"
    s, n = transform(raw.decode("utf-8"), date, review, clause)
    out = s.encode("utf-8"); open(out_p, "wb").write(out)
    print(hashlib.sha256(out).hexdigest(), len(out), f"{n} metadata edits", "(PREVIEW with placeholders)" if "--preview" in argv else "")

if __name__ == "__main__":
    main(sys.argv)
