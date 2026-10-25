#!/usr/bin/env python3
"""Genesis v2.9 publication transform: four status lines only (Document status, Date, the Appendix A v2.9 entry
heading, the footer). No live-text change; no claim, grade, RID, OPEN status or other header field is touched.
Run only after the PI's adoption decision; the decision date is an argument, so nothing is invented here.

PI decision, 25 October 2026: "çalışmayı bu haliyle benimsiyorum" (stage-2 candidate 89cef171…561a, PR #44 at 4438250).

usage: release_gen_v2_9.py CANDIDATE OUT "DD Month YYYY"           build the published file
       release_gen_v2_9.py CANDIDATE OUT "DD Month YYYY" --check   verify an existing OUT (gates P1–P6), exit 0 iff PASS
  CANDIDATE = the reviewed stage-2 candidate (SHA-256 89cef171…561a; atlas row check §7 ACCEPT FOR ADOPTION)

Gates (--check): P1 candidate hash; P2 OUT equals the transform of the candidate; P3 exactly the declared lines differ
(Document status, Appendix A v2.9 heading, footer), each once, and the Date line equals the decision date (unchanged
when the candidate already carries it); P4 the reverse transform recovers the candidate byte-exactly; P5 no
"candidate"/"not adopted" status marker remains in the header, the Appendix A v2.9 heading or the footer; P6 every
other line, including the live body, Appendix B and the claim-tag census, is byte-identical.
"""
import hashlib, re, sys

CAND = "89cef1713292e889f8c6923e7d391e36668c7909d66e2504fe553037a967561a"
REL = "`records/gen/GEN_v2_9_RELEASE_RECORD.md`"

def edits(date):
    return [
     ("status", "**Document status:** STAGE-2 CANDIDATE — not adopted (corrections of the reconciled v2.8.9 advisory and Methodology v1.4 compaction). "
                f"Release record: {REL}.  ",
                f"**Document status:** ADOPTED — PI, {date} (corrections of the reconciled v2.8.9 advisory and Methodology v1.4 compaction; "
                f"stage 1 and stage 2 reviewed). Adoption record: {REL}.  "),
     ("date", "**Date:** 25 October 2026  ", f"**Date:** {date}  "),
     ("appA", "### v2.9 — 25 October 2026 — stage-2 candidate (not adopted)", f"### v2.9 — {date} — Adopted"),
     ("footer", "*END OF DOCUMENT — RTG_GENESIS_GEOMETRY_DSN_v2.9 (stage-2 candidate; not adopted).*",
                f"*END OF DOCUMENT — RTG_GENESIS_GEOMETRY_DSN_v2.9 (ADOPTED, {date}).*"),
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
TAGS = re.compile(r"`\[(?:THM|ALG|DEF|NUM|CAND|HYP|OPEN|FAIL|RETRACTED|COR|RESULT|CONVENTION)[^`]*\]`")

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
    head_a = [l for l in ol if l.startswith("### v2.9 ")]
    foot = [l for l in ol if l.startswith("*END OF DOCUMENT")]
    bad = re.compile(r"candidate|not adopted", re.I)
    g("P5", not bad.search(hdr.split("**Status summary:**")[0]) and len(head_a) == 1 and not bad.search(head_a[0])
      and len(foot) == 1 and not bad.search(foot[0]), "NO CANDIDATE MARKER")
    keep = [i for i in range(len(cl)) if i not in diff]
    g("P6", all(cl[i] == ol[i] for i in keep) and TAGS.findall(cand) == TAGS.findall(out), "EVERYTHING ELSE BYTE-IDENTICAL")
    n = sum(R.values()); print(f"\n{n}/{len(R)} gates PASS; published {sha(out)}")
    return n == len(R)

def main(argv):
    cand_p, out_p, date = argv[1:4]
    raw = open(cand_p, "rb").read()
    assert sha(raw) == CAND, "input is not the reviewed stage-2 candidate 89cef171…561a"
    cand = raw.decode("utf-8")
    if "--check" in argv:
        sys.exit(0 if check(cand, open(out_p, encoding="utf-8").read(), date) else 1)
    out, changed = transform(cand, date)
    open(out_p, "w", encoding="utf-8").write(out)
    print(sha(out), f"{len(changed)} status lines changed ({', '.join(changed)}); Date line asserted = {date}")

if __name__ == "__main__":
    main(sys.argv)
