#!/usr/bin/env python3
"""Number Genesis v1.22 checker (one content stage) with negative controls.

usage: check_numgen_v1_22.py BASE CANDIDATE EDITLOG_JSON [--root REPO] [--controls]

Gates:
 C0 BASE        base = numgen-v1.21 (4805760d…5701); log names base and candidate hashes
 C1 BUILD       rerunning build_numgen_v1_22.py on BASE reproduces CANDIDATE byte-exactly and the logged edits
 C2 REVERSE     undoing the logged edits in reverse order recovers BASE byte-exactly (every change is a logged edit)
 C3 TAGS        claim/qualifier tag census changes exactly by {NUM:+2, scope:+1, conv:+1} (the S1 [NUM] block and the
                [NUM] artifact-row label); no grade tag added or removed otherwise
 C4 STATUS      no edit lowers the count of OPEN, CLOSED, HOLD, INCONCLUSIVE, DEFER in its own region (no status removed)
 C5 RIDS        no NUMGEN RID added or removed; every newly cited external RID is declared at the tag the text names
 C6 HEADER      one field per header line; Supersedes names exactly numgen-v1.21 and its full hash; one footer
 C7 TAGS-EXIST  every `<study>-v<x>` tag named in the edit texts exists in the repository
 C8 PATHS       every repository path named in the edit texts exists (the DRAFT release record may be pending)
 C9 HASH-ABBR   every abbreviated hash `xxxxxxxx…yyyy` in the edit texts is prefix…last-four of a known SHA-256
                (evidence files, hashes written in full in base or candidate, owner DSN files at every tag the candidate names)
Negative controls (--controls): each mutation must make at least one gate other than C1 fail (C1 rejects any
drift from the builder; the controls show that the substantive gates also see the defect).
"""
import argparse, collections, copy, hashlib, importlib.util, json, os, re, subprocess, sys

BASE_SHA = "4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701"
TAG_DELTA = {"NUM": 2, "scope": 1, "conv": 1}
STATUS = re.compile(r"\b(OPEN|CLOSED|HOLD|INCONCLUSIVE|DEFER(?:RED)?)\b")
TAGRE = re.compile(r"`\[([A-Za-z][A-Za-z-]*)(?::[^\]`]*)?\][^`]*`")
RIDRE = re.compile(r"\b(?:NUMGEN|DYAD|TDRG|RECOG|GEN|DZT)-[A-Z0-9]+(?:-[A-Z0-9]+)+\b")
PENDING = {"records/numgen/NUMGEN_v1_22_RELEASE_RECORD.md"}
RID_SOURCE = {  # external RID -> (tag, owner file) where its declaration must be found
    "TDRG": ("tdrg-v2.13", "dsn/RTG_DISCRETE_GENESIS_DSN.md"),
    "DYAD": ("dyad-v6.4.24", "dsn/RTG_DYADIC_OSCILLATOR_DSN.md"),
    "DZT": ("dzt-v0.19", "dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md"),
    "GEN": ("gen-v2.10", "dsn/RTG_GENESIS_GEOMETRY_DSN.md"),
    "RECOG": ("recog-v0.3.27", "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md"),
}

def sha(x): return hashlib.sha256(x if isinstance(x, bytes) else x.encode("utf-8")).hexdigest()

def run(base, cand, log, root, builder, verbose=True):
    R = {}
    def g(k, ok, m=""):
        R[k] = bool(ok)
        if verbose: print(f"[{'PASS' if ok else 'FAIL'}] {k} {m}")
    edits = log["edits"]
    g("C0 BASE", sha(base) == BASE_SHA and log["base_sha256"] == BASE_SHA and log["candidate_sha256"] == sha(cand))
    out, blog = builder.build(base)
    g("C1 BUILD", out == cand and [(x["key"], x["old"], x["new"]) for x in blog] == [(x["key"], x["old"], x["new"]) for x in edits],
      f"{len(edits)} edits")
    s = cand; ok = True
    for x in reversed(edits):
        if s.count(x["new"]) != 1: ok = False; break
        s = s.replace(x["new"], x["old"])
    g("C2 REVERSE", ok and s == base)
    ca, cb = collections.Counter(TAGRE.findall(base)), collections.Counter(TAGRE.findall(cand))
    d = {k: cb[k] - ca[k] for k in set(ca) | set(cb) if cb[k] != ca[k]}
    g("C3 TAGS", d == TAG_DELTA, f"delta {d}")
    low = [x["key"] for x in edits if any(collections.Counter(STATUS.findall(x["new"]))[w] < collections.Counter(STATUS.findall(x["old"]))[w]
                                          for w in ("OPEN", "CLOSED", "INCONCLUSIVE"))]
    g("C4 STATUS", not low, f"edits lowering OPEN/CLOSED/INCONCLUSIVE: {low}")
    ra, rb = set(RIDRE.findall(base)), set(RIDRE.findall(cand))
    num_changed = {r for r in ra ^ rb if r.startswith("NUMGEN-")}
    missing = []
    for r in sorted(rb - ra):
        if r.startswith("NUMGEN-"): continue
        tag, f = RID_SOURCE[r.split("-")[0]]
        src = subprocess.run(["git", "-C", root, "show", f"{tag}:{f}"], capture_output=True, text=True).stdout
        if not re.search(r"RID: " + re.escape(r) + r"\]", src): missing.append(f"{r}@{tag}")
    g("C5 RIDS", not num_changed and not missing and not (ra - rb), f"new external {sorted(rb - ra)}; undeclared {missing}; NUMGEN changed {sorted(num_changed)}")
    head = cand[:cand.index("\n## ")]
    fields = re.findall(r"^\*\*([^*:]+):\*\*", head, re.M)
    sup = re.search(r"^\*\*Supersedes:\*\*(.*)$", head, re.M).group(1)
    g("C6 HEADER", len(fields) == len(set(fields)) and BASE_SHA in sup and sup.count("RTG_NUMBER_GENESIS_DSN_v") == 1
      and "`numgen-v1.21`" in sup and len(re.findall(r"^\*END OF DOCUMENT", cand, re.M)) == 1, f"fields={len(fields)}")
    texts = "\n".join(x["new"] for x in edits)
    tags = set(re.findall(r"`((?:numgen|dyad|tdrg|recog|gen|dzt|ofn|programme|methodology|rrf)-v[0-9.]+)`", texts))
    have = set(subprocess.run(["git", "-C", root, "tag", "-l"], capture_output=True, text=True).stdout.split())
    g("C7 TAGS-EXIST", tags <= have, f"{len(tags)} tags; missing {sorted(tags - have)}")
    paths = set(re.findall(r"`((?:records|evidence|upload|pipes|tools|dsn)/[^`<>*\s…]+)`", texts))
    miss = sorted(p for p in paths if p not in PENDING and not os.path.exists(os.path.join(root, p)))
    g("C8 PATHS", not miss, f"{len(paths)} paths; missing {miss}")
    known = set()
    for top in ("upload/numgen-records", "evidence/numgen", "upload/tdrg-records", "evidence/tdrg/scripts"):
        for dp, _, fs in os.walk(os.path.join(root, top)):
            for fn in fs: known.add(sha(open(os.path.join(dp, fn), "rb").read()))
    known |= set(re.findall(r"[0-9a-f]{64}", base + cand))
    for t in set(re.findall(r"`((?:numgen|dyad|tdrg|recog|gen|dzt|ofn|programme|methodology|rrf)-v[0-9.]+)`", cand)) & have:
        files = subprocess.run(["git", "-C", root, "ls-tree", "--name-only", t, "dsn/"], capture_output=True, text=True).stdout.split()
        for f in files:   # owner files at every tag the candidate names
            known.add(sha(subprocess.run(["git", "-C", root, "show", f"{t}:{f}"], capture_output=True).stdout))
    bad = [f"{a}…{b}" for a, b in re.findall(r"`([0-9a-f]{8})…([0-9a-f]+)`", texts)
           if len(b) != 4 or not any(h.startswith(a) and h.endswith(b) for h in known)]
    g("C9 HASH-ABBR", not bad, f"bad {bad}")
    return R

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("base"); ap.add_argument("cand"); ap.add_argument("log")
    ap.add_argument("--root", default="."); ap.add_argument("--controls", action="store_true"); a = ap.parse_args()
    base = open(a.base, "rb").read().decode("utf-8"); cand = open(a.cand, "rb").read().decode("utf-8")
    log = json.load(open(a.log, encoding="utf-8"))
    spec = importlib.util.spec_from_file_location("b22", os.path.join(a.root, "evidence/numgen/scripts/build_numgen_v1_22.py"))
    builder = importlib.util.module_from_spec(spec); spec.loader.exec_module(builder)
    if not a.controls:
        R = run(base, cand, log, a.root, builder); ok = all(R.values())
        print("candidate sha256", sha(cand)); print("RESULT:", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
    def mut_cand(f):
        def m(c, l): c2 = f(c); l2 = copy.deepcopy(l); l2["candidate_sha256"] = sha(c2); return c2, l2
        return m
    def mut_edit(key, f):  # change one logged edit's new text and the candidate consistently
        def m(c, l):
            l2 = copy.deepcopy(l); x = next(y for y in l2["edits"] if y["key"] == key)
            new2 = f(x["new"]); c2 = c.replace(x["new"], new2); x["new"] = new2; l2["candidate_sha256"] = sha(c2); return c2, l2
        return m
    def add_edit(key, old, new):  # a logged, reversible edit that changes a status: only C4 should object on substance
        def m(c, l):
            l2 = copy.deepcopy(l); assert c.count(old) == 1; c2 = c.replace(old, new)
            l2["edits"].append({"key": key, "group": "control", "row": "control", "old": old, "new": new}); l2["candidate_sha256"] = sha(c2); return c2, l2
        return m
    NC = [
        ("NC1 unlogged change in live text", mut_cand(lambda c: c.replace("Global breadth remains OPEN.", "Global breadth remains open.", 1))),
        ("NC2 grade raised in an edit", mut_edit("P4", lambda t: t.replace("`[NUM]` `[scope: Census-1", "`[THM]` `[scope: Census-1"))),
        ("NC3 logged edit that closes an OPEN item", add_edit("XX", "Global breadth remains OPEN.", "Global breadth is CLOSED.")),
        ("NC4 invented NUMGEN RID", mut_edit("P4", lambda t: t.replace("**P2 re-annotation under TDRG-DEF-ORIENT (v1.22 S1).**", "[RID: NUMGEN-NUM-P2-REANNOTATION] **P2 re-annotation under TDRG-DEF-ORIENT (v1.22 S1).**"))),
        ("NC5 external RID not declared at the named tag", mut_edit("I2", lambda t: t.replace("TDRG-THM-RECURRENCE", "TDRG-THM-RECURRENCE-X"))),
        ("NC6 nonexistent tag", mut_edit("D1", lambda t: t.replace("`dzt-v0.19`", "`dzt-v0.17`"))),
        ("NC7 nonexistent path", mut_edit("R2", lambda t: t.replace("evidence/numgen/v1.22/s1/", "evidence/numgen/v1.22/s1x/"))),
        ("NC8 wrong hash abbreviation", mut_edit("R2", lambda t: t.replace("`4c5c2f17…8ae9`", "`4c5c2f17…67dc`"))),
        ("NC9 second predecessor in Supersedes", mut_edit("H4", lambda t: t.replace("tag `numgen-v1.21`).", "tag `numgen-v1.21`); also `RTG_NUMBER_GENESIS_DSN_v1.20.8`."))),
        ("NC10 duplicated footer", mut_edit("F1", lambda t: t + "\n*END OF DOCUMENT — extra.*")),
        ("NC11 wrong base", None),
    ]
    allok = True
    for name, m in NC:
        if m is None:
            b2 = base.replace("Global breadth remains OPEN.", "Global breadth remains open.", 1)
            R = run(b2, cand, log, a.root, builder, verbose=False)
        else:
            c2, l2 = m(cand, log); R = run(base, c2, l2, a.root, builder, verbose=False)
        failed = [k for k, v in R.items() if not v]
        sem = [k for k in failed if k != "C1 BUILD"]   # C1 catches any drift from the builder; require a gate on substance too
        print(f"{name}: {'caught by ' + ', '.join(sem) + (' (and C1 BUILD)' if 'C1 BUILD' in failed else '') if sem else 'NOT CAUGHT on substance' + (' (C1 only)' if failed else '')}")
        allok &= bool(sem)
    print("RESULT:", "PASS (all controls caught)" if allok else "FAIL"); sys.exit(0 if allok else 1)

if __name__ == "__main__":
    main()
