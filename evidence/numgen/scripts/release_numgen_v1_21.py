#!/usr/bin/env python3
"""Number Genesis v1.21 publication transform: status lines only (Document status, Date, the Appendix A v1.21 entry
heading, the footer). No live-text change; no claim, grade, RID, OPEN status or other header field is touched.
Run only after the PI's adoption decision; the decision date is an argument, so nothing is invented here.

PI adoption decision, 26 October 2026 (22:46 +03:00), scope fixed by two objects: stage-1 frozen intermediate
ab25c162…99d2 and stage-2 accepted candidate 05b3315f…4258 (record: records/numgen/NUMGEN_v1_21_RELEASE_RECORD.md §1, §13).

usage: release_numgen_v1_21.py CANDIDATE OUT "DD Month YYYY"           build the published file
       release_numgen_v1_21.py CANDIDATE OUT "DD Month YYYY" --check   verify an existing OUT (gates P1–P6), exit 0 iff PASS

Gates (--check): P1 candidate hash; P2 OUT equals the transform of the candidate; P3 exactly the declared lines differ,
each once, and the Date line equals the decision date (unchanged when the candidate already carries it); P4 the reverse
transform recovers the candidate byte-exactly; P5 no DRAFT/candidate/not-adopted marker remains in the header fields
above the status summary, the Appendix A v1.21 heading or the footer; P6 every other line, including the live body,
Appendix B, Appendix C and the claim-tag census, is byte-identical.
"""
import hashlib, re, sys

CAND = "05b3315fe74ec006b5610b1823522f843f55d677c01f1ec39b42144dd4be4258"
REL = "`records/numgen/NUMGEN_v1_21_RELEASE_RECORD.md`"

def edits(date):
    return [
     ("status", "**Document status:** DRAFT — v1.21 stage-2 candidate, not adopted; v1.20.8 governs until PI adoption. "
                f"Release record (DRAFT): {REL}.  ",
                f"**Document status:** ADOPTED — PI, {date} (corrections of the reconciled v1.20.8 advisory and Methodology v1.4 "
                f"compaction; stage 1 and stage 2 reviewed). Release record: {REL}.  "),
     ("date", "**Date:** 26 October 2026  ", f"**Date:** {date}  "),
     ("appA", "### v1.21 — 26 October 2026 — DRAFT (stage-2 candidate; not adopted)", f"### v1.21 — {date} — Adopted"),
     ("footer", "*END OF DOCUMENT — RTG_NUMBER_GENESIS_DSN_v1.21 (DRAFT stage-2 candidate; not adopted).*",
                f"*END OF DOCUMENT — RTG_NUMBER_GENESIS_DSN_v1.21 (ADOPTED, {date}).*"),
    ]

def transform(s, date):
    lines = s.split("\n")
    changed = []
    for k, old, new in edits(date):
        idx = [i for i, l in enumerate(lines) if l == old]
        assert len(idx) == 1, f"{k}: expected exactly one line, found {len(idx)}"
        if old != new:
            lines[idx[0]] = new; changed.append(k)
    return "\n".join(lines), changed

def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()
TAGS = re.compile(r"`\[(?:THM|ALG|DEF|NUM|CAND|HYP|OPEN|FAIL|RETRACTED|COR|RESULT|REJECTED|SESSION)[^`]*\]`")

def check(cand, out, date):
    R = {}
    def g(k, ok, m=""):
        R[k] = bool(ok); print(f"[{'PASS' if ok else 'FAIL'}] {k} {m}")
    g("P1", sha(cand) == CAND, "CANDIDATE")
    t, changed = transform(cand, date)
    g("P2", t == out, "TRANSFORM")
    cl, ol = cand.split("\n"), out.split("\n")
    diff = [i for i, (a, b) in enumerate(zip(cl, ol)) if a != b]
    exp = {old: new for k, old, new in edits(date) if old != new}
    date_ok = sum(1 for l in ol if l == f"**Date:** {date}  ") == 1
    g("P3", len(cl) == len(ol) and len(diff) == len(exp) and all(cl[i] in exp and exp[cl[i]] == ol[i] for i in diff) and date_ok,
      f"DECLARED LINES ({len(diff)} changed: {', '.join(changed)}; Date line = {date})")
    rev = out
    for k, old, new in edits(date):
        if old != new:
            rev = rev.replace(new, old) if rev.count(new) == 1 else None
            if rev is None:
                break
    g("P4", rev == cand, "REVERSE")
    hdr = out[:out.index("\n## ")]
    head_a = [l for l in ol if l.startswith("### v1.21 ")]
    foot = [l for l in ol if l.startswith("*END OF DOCUMENT")]
    bad = re.compile(r"draft|candidate|not adopted", re.I)
    g("P5", not bad.search(hdr.split("**Status summary:**")[0]) and len(head_a) == 1 and not bad.search(head_a[0])
      and len(foot) == 1 and not bad.search(foot[0]), "NO DRAFT/CANDIDATE MARKER")
    keep = [i for i in range(len(cl)) if i not in diff]
    g("P6", all(cl[i] == ol[i] for i in keep) and TAGS.findall(cand) == TAGS.findall(out), "EVERYTHING ELSE BYTE-IDENTICAL")
    n = sum(R.values()); print(f"\n{n}/{len(R)} gates PASS; published {sha(out)}")
    return n == len(R)

def main(argv):
    cand_p, out_p, date = argv[1:4]
    raw = open(cand_p, "rb").read()
    assert sha(raw) == CAND, "input is not the accepted stage-2 candidate 05b3315f…4258"
    cand = raw.decode("utf-8")
    if "--check" in argv:
        sys.exit(0 if check(cand, open(out_p, "rb").read().decode("utf-8"), date) else 1)
    out, changed = transform(cand, date)
    open(out_p, "wb").write(out.encode("utf-8"))
    print(sha(out), f"{len(changed)} status lines changed ({', '.join(changed)}); Date line asserted = {date}")

if __name__ == "__main__":
    main(sys.argv)
