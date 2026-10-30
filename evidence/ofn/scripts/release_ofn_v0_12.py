#!/usr/bin/env python3
"""OFN v0.12 publication transform: adoption-state lines only. No claim, grade, RID, OPEN status or other text changes.

PI adoption decision: "PI olarak, bende OFN v0.12 ikinci tur adayını benimsiyorum" (Mustafa, OFN session, 30 October 2026,
14:26 +03:00), on the round-2 candidate 5e1da260…6a42 after the co-owner's ACCEPT SCOPED — OWNER ADOPTION READY (PR #126
review 5711501720). Record: records/ofn/OFN_v0_12_RELEASE_RECORD.md §5. The decision date is an argument.

Changed lines (release record §5; the header Date line already carries the decision date and is not touched):
  status   header Document status: DRAFT -> ADOPTED
  supers   header Supersedes: ", on adoption" dropped
  s123     §12.3 new-RID row: adoption-pending wording -> registered state
  appC     Appendix C v0.12 heading DRAFT -> ADOPTED
  footer   one footer line

usage: release_ofn_v0_12.py CANDIDATE OUT "DD Month YYYY"                       build the published file
       release_ofn_v0_12.py CANDIDATE OUT "DD Month YYYY" --check [--controls]  gates P1-P6 (and negative controls)
Gates: P1 candidate hash; P2 OUT equals the transform; P3 exactly the declared lines differ, each once; P4 the reverse
transform recovers the candidate byte-exactly; P5 no DRAFT / adoption-pending marker remains in the header fields or the
changed lines; P6 every other line is byte-identical and the claim-tag, RID and math census of the whole file is unchanged.
"""
import hashlib, re, sys

CAND = "5e1da260f944c40ebdcab29f57bdd37600f04e47a797b768ab5e0126a0e76a42"
REL = "`records/ofn/OFN_v0_12_RELEASE_RECORD.md`"
ROW = "| `RTG-OFN-ALG-REF-CLOSURE-COMPARISON` | "


def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()


def edits(date):
    return [
        ("status", "**Document status:** DRAFT — v0.12 candidate (one content stage; no layout stage); adoption pending "
                   f"({REL}). `ofn-v0.11` remains the governing edition until adoption and tag.  ",
                   f"**Document status:** ADOPTED — PI, {date} (closure-versus-reference result; isolation and triadic-independence "
                   f"frames recorded, none selected; reviewed in two rounds). Release record: {REL}.  "),
        ("supers", "**Supersedes:** `RTG_ONTOLOGICAL_FOUNDATIONS_v0.11` (tag `ofn-v0.11`, SHA-256 "
                   "`38a2f44473323a7dd8405161c0d0439143bc234ac0a9cc75577628ac8a51e9e4`), on adoption.  ",
                   "**Supersedes:** `RTG_ONTOLOGICAL_FOUNDATIONS_v0.11` (tag `ofn-v0.11`, SHA-256 "
                   "`38a2f44473323a7dd8405161c0d0439143bc234ac0a9cc75577628ac8a51e9e4`).  "),
        ("s123", ROW + "v0.12 (adoption pending), OFN RESULT from ALG | Registered on adoption of v0.12 (five OFN local results in total) |",
                 ROW + f"Registered v0.12, OFN RESULT from ALG | Registered {short(date)} (five OFN local results in total) |"),
        ("appC", "### v0.12 — 30 October 2026 — DRAFT (adoption pending)",
                 f"### v0.12 — {date} — ADOPTED / closure-versus-reference result; isolation and independence frames"),
        ("footer", "*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.12 — DRAFT, adoption pending; `ofn-v0.11` governs until adoption and tag.*",
                   "*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.12*"),
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
    g("P1", sha(cand) == CAND, "candidate is 5e1da260…6a42")
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
    ("X3 footer left as draft", lambda t: t.replace("*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.12*", "*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.12 — DRAFT, adoption pending; `ofn-v0.11` governs until adoption and tag.*", 1)),
    ("X4 claim tag changed", lambda t: t.replace("`[OPEN]`", "`[CAND]`", 1)),
    ("X5 RID added in a changed line", lambda t: t.replace("(five OFN local results in total) |", "(five OFN local results in total; RTG-OFN-DEF-EXTRA) |", 1)),
    ("X6 isolation contract selected", lambda t: t.replace("Isolation frame (recorded; none selected).", "Isolation frame. I-comp is selected.", 1)),
]


def main(a):
    if len(a) < 4:
        raise SystemExit(__doc__)
    cand = open(a[1], "rb").read().decode("utf-8"); date = a[3]
    if "--check" not in a:
        if sha(cand) != CAND:
            raise SystemExit("candidate is not 5e1da260…6a42")
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
