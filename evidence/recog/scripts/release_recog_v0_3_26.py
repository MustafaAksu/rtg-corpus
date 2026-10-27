#!/usr/bin/env python3
"""RECOG v0.3.26 publication transform: publication metadata only (header identity and status lines, the
Appendix A entry heading and its records line, the footer). No live-text change; no claim, grade, RID, [COR]
note, Appendix B entry or OPEN status is touched. To be run only after the PI's separate decisions on the
groups CORR (the Appendix B correction), DRIFT (Lemma 21-22, Prop. 23) and ENV (the conditional Cor. 24); the
decision date, the review number and the adoption wording are arguments so that nothing is invented here.
If the PI adopts a subset of the groups, the matching decoupling variant (`evidence/recog/v0.3.26/variants/`)
is the candidate instead and CAND must be set to its hash in a reviewed follow-up commit. `--preview` writes
the would-be file from placeholder arguments for hash inspection only (never to dsn/).

usage: release_recog_v0_3_26.py CANDIDATE OUT "DD Month YYYY" "<review number>" "<adoption clause>"
  CANDIDATE = the reviewed stage-1 intermediate (SHA-256 e360606c…3f22)
  <adoption clause> = the PI's scope wording, e.g. "three groups adopted: CORR asymptotic correction of the
  v0.3.25 majorant order sentences (Appendix B), DRIFT chart reciprocal drift centring, ENV log-free centred envelope"
"""
import hashlib, sys

CAND = "e360606c3f30fb43165877856528682b94a1e9380e86688a383b9b3a69f13f22"
PREV = "86cae8ff094d63d077ec5c0887451775ec3a26485cfad95833d8390bda4bd7db"

def transform(s, date, review, clause):
    EDITS = [
     ("# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.25\n", "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.26\n"),
     ("**Date:** 27 October 2026\n", f"**Date:** {date}\n"),
     ("**Document status:** ADOPTED — PI, 27 October 2026 (four groups adopted: B1 sharpened R9 rows, A1c-E known-a sharpened schedule, A1c-D record-only outer decoder, A1c-Q record-fiber structure; stage-1 round-2 corrections reviewed, review #5664522727; no stage-2 compaction). Adoption record: `records/recog/RECOG_v0_3_25_RELEASE_RECORD.md`.",
      f"**Document status:** ADOPTED — PI, {date} ({clause}; stage-1 reviewed, review #{review}; no stage-2 compaction). Adoption record: `records/recog/RECOG_v0_3_26_RELEASE_RECORD.md`."),
     ("**Supersedes:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.24` (SHA-256 `8c64bea231b3691b737f4143f6f4105030ee183fcc90d7f604ec83a4c869e7c1`; tag `recog-v0.3.24`).",
      f"**Supersedes:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.25` (SHA-256 `{PREV}`; tag `recog-v0.3.25`)."),
     ("**Release record:** `records/recog/RECOG_v0_3_25_RELEASE_RECORD.md`. Version history: Appendix A.",
      "**Release record:** `records/recog/RECOG_v0_3_26_RELEASE_RECORD.md`. Version history: Appendix A."),
     ("### v0.3.26 — DRAFT, stage 1 (corrected intermediate; not adopted)\n", f"### v0.3.26 — {date} — Adopted\n"),
     ("- **Records:** release record `records/recog/RECOG_v0_3_26_RELEASE_RECORD.md` (candidate); predecessor tag `recog-v0.3.25` (SHA-256 `86cae8ff…d7db`).",
      f"- **Records:** release record `records/recog/RECOG_v0_3_26_RELEASE_RECORD.md`; stage-1 intermediate SHA-256 `{CAND[:8]}…{CAND[-4:]}`; predecessor tag `recog-v0.3.25` (SHA-256 `86cae8ff…d7db`)."),
     ("*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.25 (ADOPTED, 27 October 2026).*",
      f"*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.26 (ADOPTED, {date}).*"),
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
