#!/usr/bin/env python3
"""Triadic v1.7 publication transform: adoption-state lines only. No claim, grade, RID, OPEN status or other text changes.

PI adoption decision: "Triadic kayıtlarını bu haliyle benimdiyorum." (Mustafa, Triadic owner session, 3 November 2026,
08:01 +03:00; quoted as written), on the accepted stage-2 candidate 2573961a…5c0d, after the co-owner reviews and the
Atlas row checks (record: records/triad/TRIAD_v1_7_RELEASE_RECORD.md §1). The decision date is an argument, so nothing is
invented here.

Changed lines:
  date     header Date line -> decision date
  status   header Document status: DRAFT/candidate -> ADOPTED
  supers   header Supersedes: ", on adoption" dropped
  records  header Records: "(written at adoption)" dropped
  s9       §9 edition line: "PI adoption pending" -> adopted by the PI on the decision date
  appA     Appendix A v1.7 heading: DRAFT -> ADOPTED
  footer   one footer line

usage: release_triad_v1_7.py CANDIDATE OUT "D Month YYYY"                 build the published file
       release_triad_v1_7.py CANDIDATE OUT "D Month YYYY" --check         gates P1-P6 on an existing OUT
       release_triad_v1_7.py CANDIDATE OUT "D Month YYYY" --check --controls   also run negative controls
Gates: P1 candidate hash; P2 OUT equals the transform; P3 exactly the declared lines differ, each once; P4 the reverse
transform recovers the candidate byte-exactly; P5 no DRAFT / adoption-pending / candidate / on-adoption marker remains in
the header fields (Scope and Status summary excepted), the §9 edition line, the Appendix A v1.7 heading or the footer;
P6 every other line is byte-identical and the claim-tag, RID and math census of the whole file is unchanged.
"""
import hashlib, re, sys

CAND = "2573961a82ce10a348f76f10feece6fefb3831f3c4dd60de5dcae78acb745c0d"
REL = "`records/triad/TRIAD_v1_7_RELEASE_RECORD.md`"
PRED = ("**Supersedes:** `RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6.1` (tag `triad-v1.6.1`, SHA-256 "
        "`95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f`)")
RECS = ("**Records:** v1.7 release record `records/triad/TRIAD_v1_7_RELEASE_RECORD.md`{}; stage-1 build "
        "`evidence/triad/scripts/build_triad_v1_7_stage1.py` with `records/triad/TRIAD_v1_7_STAGE1_IMPLEMENTATION_MATRIX.md`; "
        "stage-2 movement map `evidence/triad/v1.7/movement_map.json`; v1.6.1 adoption and release records "
        "`records/triad/OWNER_ADOPTION_v1_6_1.json` and `records/triad/RELEASE_RECORD_v1_6_1.md`.  ")
S9 = "**This edition (v1.7):** prepared by Claude from the confirmed co-owner reconciliation; change-focused review by ChatGPT; {}.  "


def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()


def edits(date):
    return [
        ("date", "**Date:** 2 November 2026  ", f"**Date:** {date}  "),
        ("status", "**Document status:** DRAFT — v1.7 stage-2 candidate (layout only, over the stage-1 intermediate "
                   "`b47d294d…a66a`); adoption pending. `triad-v1.6.1` governs until adoption and tag. Consumer acceptance is not implied.  ",
                   f"**Document status:** ADOPTED — PI, {date} (orientation-extension typing, T-6r acceptance contract, claim-level "
                   f"repins, consumer matrix and Methodology v1.4 layout; stage 1 and stage 2 reviewed). Release record: {REL}. "
                   "Consumer acceptance is not implied.  "),
        ("supers", PRED + ", on adoption.  ", PRED + ".  "),
        ("records", RECS.format(" (written at adoption)"), RECS.format("")),
        ("s9", S9.format("PI adoption pending"), S9.format(f"adopted by the PI on {date}")),
        ("appA", "### v1.7 — 2 November 2026 — DRAFT (adoption pending)", f"### v1.7 — {date} — ADOPTED"),
        ("footer", "*END OF DOCUMENT — RTG_TRIADIC_BIRTH_LIFT_DSN_v1.7 — DRAFT, stage-2 candidate; adoption pending; "
                   "`triad-v1.6.1` governs until adoption and tag.*",
                   "*END OF DOCUMENT — RTG_TRIADIC_BIRTH_LIFT_DSN_v1.7*"),
    ]


def transform(s, date, reverse=False):
    lines = s.split("\n")
    for k, old, new in edits(date):
        a, b = (new, old) if reverse else (old, new)
        idx = [i for i, l in enumerate(lines) if l == a]
        if len(idx) != 1:
            raise ValueError(f"{k}: expected exactly one line, found {len(idx)}")
        lines[idx[0]] = b
    return "\n".join(lines)


CENSUS = (re.compile(r"`\[[A-Z][A-Za-z -]*\]`"),
          re.compile(r"\b(?:TRIAD|DYAD|GEN|TDRG|RECOG|NUMGEN|RRF|UVM|RER)-[A-Z0-9-]+|RTG-OFN-[A-Z0-9]+(?:-[A-Z0-9]+)*"),
          re.compile(r"\$\$.+?\$\$|\$[^$\n]+\$", re.S))
MARK = re.compile(r"DRAFT|adoption pending|candidate|on adoption\.|written at adoption")


def gates(cand, out, date, say=print):
    res = []
    def g(k, ok, msg=""):
        res.append(bool(ok)); say(f"{k} {'PASS' if ok else 'FAIL'} {msg}".rstrip())
    g("P1", sha(cand) == CAND, "candidate is 2573961a…5c0d")
    try:
        built = transform(cand, date)
    except ValueError as e:
        g("P2", False, str(e))
    else:
        g("P2", built == out, "OUT equals the transform of the candidate")
    cl, ol = cand.split("\n"), out.split("\n")
    diff = [i for i in range(max(len(cl), len(ol))) if i >= len(cl) or i >= len(ol) or cl[i] != ol[i]]
    E = edits(date)
    expect = {i for i, l in enumerate(cl) for _, old, _ in E if l == old}
    g("P3", len(cl) == len(ol) and set(diff) == expect and len(expect) == len(E)
      and all(ol.count(new) == 1 for _, _, new in E), f"{len(diff)} lines differ; {len(E)} declared")
    try:
        g("P4", transform(out, date, reverse=True) == cand, "reverse transform recovers the candidate")
    except ValueError as e:
        g("P4", False, str(e))
    head = out[:out.index("\n## ")]
    marks = [l for l in head.split("\n") + [ol[i] for i in expect if i < len(ol)]
             if MARK.search(l) and not l.startswith("**Status summary:**") and not l.startswith("**Scope:**")]
    g("P5", not marks, f"markers left: {[m[:60] for m in marks]}" if marks else "no DRAFT/pending/candidate marker in the changed lines or header")
    other = all(cl[i] == ol[i] for i in range(min(len(cl), len(ol))) if i not in expect)
    cen = all(sorted(r.findall(cand)) == sorted(r.findall(out)) for r in CENSUS)
    g("P6", other and cen, "all other lines byte-identical; claim-tag, RID and math census unchanged")
    return all(res)


CONTROLS = [
    ("X1 extra live change", lambda t: t.replace("Tangency holds in both.", "Tangency holds in (b).", 1)),
    ("X2 status summary edited", lambda t: t.replace("is bookkeeping until source/model correspondence is proved.", "is bookkeeping.", 1)),
    ("X3 footer left as draft", lambda t: t.replace("*END OF DOCUMENT — RTG_TRIADIC_BIRTH_LIFT_DSN_v1.7*",
                                                    "*END OF DOCUMENT — RTG_TRIADIC_BIRTH_LIFT_DSN_v1.7 — DRAFT, stage-2 candidate; adoption pending; `triad-v1.6.1` governs until adoption and tag.*")),
    ("X4 claim tag changed", lambda t: t.replace("`[OPEN]`", "`[CAND]`", 1)),
    ("X5 RID added in a changed line", lambda t: t.replace("Release record: `records/triad/TRIAD_v1_7_RELEASE_RECORD.md`. Consumer",
                                                           "Release record: `records/triad/TRIAD_v1_7_RELEASE_RECORD.md`; TRIAD-ALG-EXTRA. Consumer", 1)),
    ("X6 supersedes left 'on adoption'", lambda t: t.replace(PRED + ".  ", PRED + ", on adoption.  ", 1)),
]


def main(a):
    if len(a) < 4:
        raise SystemExit(__doc__)
    cand = open(a[1], "rb").read().decode("utf-8"); date = a[3]
    if "--check" not in a:
        if sha(cand) != CAND:
            raise SystemExit("candidate is not 2573961a…5c0d")
        out = transform(cand, date)
        open(a[2], "w", encoding="utf-8", newline="\n").write(out)
        print(f"published {sha(out)}")
        return 0
    out = open(a[2], "rb").read().decode("utf-8")
    ok = gates(cand, out, date)
    print("RESULT:", "PASS" if ok else "FAIL")
    if "--controls" in a:
        allc = True
        for name, f in CONTROLS:
            m = f(out)
            if m == out:
                print(f"{name}: mutation did not apply — CONTROL INVALID"); allc = False; continue
            r = gates(cand, m, date, say=lambda s: None)
            print(f"{name}: {'caught' if not r else 'NOT CAUGHT'}"); allc &= not r
        print("CONTROLS", "PASS" if allc else "FAIL"); ok &= allc
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
