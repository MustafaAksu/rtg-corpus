#!/usr/bin/env python3
"""OFN v0.11 publication transform: adoption-state lines only. No claim, grade, RID, OPEN status or other text changes.

PI adoption decision: "ontology DSN'i bu şekliyle benimsiyorum" (Mustafa, OFN session, 30 October 2026, 00:22 +03:00),
on the accepted stage-2 candidate df3c465f…00eb (record: records/ofn/OFN_v0_11_RELEASE_RECORD.md §8). The decision date
is an argument, so nothing is invented here.

Changed lines (release record §8, plus the header Date line as in the NUMGEN v1.21 precedent):
  date     header Date line -> decision date
  status   header Document status: DRAFT/candidate -> ADOPTED
  supers   header Supersedes: ", on adoption" dropped
  s03      §0.3 "*v0.11 (adoption pending):*" -> "*v0.11:*"
  s123     §12.3 six-DEF row: "v0.11 (adoption pending)" / "Registered on adoption of v0.11" -> registered state
  appB     Appendix B heading "### Adopted v0.11 records (adoption pending)" -> dated
  appC     Appendix C v0.11 heading DRAFT -> ADOPTED
  footer   one footer line

usage: release_ofn_v0_11.py CANDIDATE OUT "DD Month YYYY"                 build the published file
       release_ofn_v0_11.py CANDIDATE OUT "DD Month YYYY" --check         gates P1-P6 on an existing OUT
       release_ofn_v0_11.py CANDIDATE OUT "DD Month YYYY" --check --controls   also run negative controls
Gates: P1 candidate hash; P2 OUT equals the transform; P3 exactly the declared lines differ, each once; P4 the reverse
transform recovers the candidate byte-exactly; P5 no DRAFT / adoption-pending / candidate marker remains in the header
fields, the §0.3 label, the §12.3 row, the two appendix headings or the footer; P6 every other line is byte-identical and
the claim-tag, RID and math census of the whole file is unchanged.
"""
import hashlib, re, sys

CAND = "df3c465fb79f049f686f07635d889613e8ab112895cdbcd5af7af029e97400eb"
REL = "`records/ofn/OFN_v0_11_RELEASE_RECORD.md`"
ROW_HEAD = ("| `RTG-OFN-DEF-ZERO-ORIGIN`, `RTG-OFN-DEF-DISCRETE-REDUCTION-BOUNDARY`, `RTG-OFN-DEF-CONTINUOUS-REPRESENTATION`, "
            "`RTG-OFN-DEF-FINITE-DESCRIPTION`, `RTG-OFN-DEF-DIST-ZN`, `RTG-OFN-DEF-REDUCTION-TARGET` | ")
DEF_TAIL = "OFN definitions; bodies unchanged from v0.10 §§1.3, 4.1, 4.6, 8 | "


def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()


def edits(date):
    return [
        ("date", "**Date:** 29 October 2026  ", f"**Date:** {date}  "),
        ("status", "**Document status:** DRAFT — v0.11 candidate: layout-only compaction (stage 2) of the frozen stage-1 "
                   f"intermediate; adoption pending ({REL}). `ofn-v0.10` remains the governing edition until adoption and tag.  ",
                   f"**Document status:** ADOPTED — PI, {date} (owner synchronization, smooth class-C realization and two §5.5 "
                   f"contract corrections; stage 1 and stage 2 reviewed). Release record: {REL}.  "),
        ("supers", "**Supersedes:** `RTG_ONTOLOGICAL_FOUNDATIONS_v0.10` (tag `ofn-v0.10`, SHA-256 "
                   "`acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa`), on adoption.  ",
                   "**Supersedes:** `RTG_ONTOLOGICAL_FOUNDATIONS_v0.10` (tag `ofn-v0.10`, SHA-256 "
                   "`acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa`).  "),
        ("s03", "*v0.11 (adoption pending):* registers six further definition RIDs for unchanged bodies, corrects two §5.5 "
                "definitions by recorded `[COR]` (Appendix B) and adds no OPEN record.",
                "*v0.11:* registers six further definition RIDs for unchanged bodies, corrects two §5.5 "
                "definitions by recorded `[COR]` (Appendix B) and adds no OPEN record."),
        ("s123", ROW_HEAD + "v0.11 (adoption pending), " + DEF_TAIL + "Registered on adoption of v0.11 (seventeen definition RIDs in total) |",
                 ROW_HEAD + "Registered v0.11, " + DEF_TAIL + f"Registered {short(date)} (seventeen definition RIDs in total) |"),
        ("appB", "### Adopted v0.11 records (adoption pending)", f"### Adopted v0.11 records — {date}"),
        ("appC", "### v0.11 — 29 October 2026 — DRAFT (adoption pending)",
                 f"### v0.11 — {date} — ADOPTED / smooth class-C realization and owner synchronization release"),
        ("footer", "*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.11 — DRAFT, adoption pending; `ofn-v0.10` governs until adoption and tag.*",
                   "*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.11*"),
    ]


def short(date):
    d, m, y = date.split()
    return f"{int(d)} {m[:3]} {y}"


def transform(s, date, reverse=False):
    lines = s.split("\n")
    for k, old, new in edits(date):
        a, b = (new, old) if reverse else (old, new)
        idx = [i for i, l in enumerate(lines) if l == a]
        if len(idx) != 1:
            raise ValueError(f"{k}: expected exactly one line, found {len(idx)}")
        lines[idx[0]] = b
    return "\n".join(lines)


CENSUS = (re.compile(r"`\[[A-Z][A-Za-z -]*\]`"), re.compile(r"RTG-OFN-[A-Z0-9]+(?:-[A-Z0-9]+)*|\b(?:DYAD|GEN|TDRG|RECOG|NUMGEN|RRF|TRIAD)-[A-Z0-9-]+"),
          re.compile(r"\$\$.+?\$\$|\$[^$\n]+\$", re.S))


def gates(cand, out, date, say=print):
    res = []
    def g(k, ok, msg=""):
        res.append(bool(ok)); say(f"{k} {'PASS' if ok else 'FAIL'} {msg}".rstrip())
    g("P1", sha(cand) == CAND, "candidate is df3c465f…00eb")
    try:
        built = transform(cand, date)
    except ValueError as e:
        built = None; g("P2", False, str(e))
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
             if re.search(r"DRAFT|adoption pending|candidate|on adoption\.", l) and not l.startswith("**Status summary:**")
             and not l.startswith("**Scope:**")]
    g("P5", not marks, f"markers left: {[m[:60] for m in marks]}" if marks else "no DRAFT/pending/candidate marker in the changed lines or header")
    other = all(cl[i] == ol[i] for i in range(min(len(cl), len(ol))) if i not in expect)
    cen = all(sorted(r.findall(cand)) == sorted(r.findall(out)) for r in CENSUS)
    g("P6", other and cen, "all other lines byte-identical; claim-tag, RID and math census unchanged")
    return all(res)


CONTROLS = [
    ("X1 extra live change", lambda t: t.replace("primary realized smooth mathematical candidate family", "principal realized smooth mathematical candidate family", 2)),
    ("X2 status summary edited", lambda t: t.replace("twenty-one foundational OPENs (twenty ACTIVE, one PARTIAL)", "twenty-one foundational OPENs (twenty-one ACTIVE)", 1)),
    ("X3 footer left as draft", lambda t: t.replace("*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.11*", "*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.11 — DRAFT, adoption pending; `ofn-v0.10` governs until adoption and tag.*", 1)),
    ("X4 claim tag changed", lambda t: t.replace("`[OPEN]`", "`[CAND]`", 1)),
    ("X5 RID added in a changed line", lambda t: t.replace("(seventeen definition RIDs in total) |", "(seventeen definition RIDs in total; RTG-OFN-DEF-EXTRA) |", 1)),
]


def main(a):
    if len(a) < 4:
        raise SystemExit(__doc__)
    cand = open(a[1], "rb").read().decode("utf-8"); date = a[3]
    if "--check" not in a:
        if sha(cand) != CAND:
            raise SystemExit("candidate is not df3c465f…00eb")
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
