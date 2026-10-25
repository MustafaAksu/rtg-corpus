#!/usr/bin/env python3
"""Genesis v2.9 stage 2: owner guards and negative fixtures around tools/check_compaction.py.

usage: check_gen_v2_9_stage2.py STAGE1 CANDIDATE MAP [--fixtures]
  run from the repository root (tools/check_compaction.py and the archive path in the map are read from it).

Owner guards (PI, 25 Oct 2026: "preserving §6.3a–c, the GA-01/02 text and the nine custody states"):
 G1 LIVE BODY   the live body (from "## Local Tag Aliases" to "## Appendix A") is byte-identical to stage 1
 G2 §6.3a–c     the span "### §6.3a " … "### §6.4 " is byte-identical
 G3 GA-01       both sourced-junction statements, the §7 export line and the Appendix B corrected-claim entry are present unchanged
 G4 GA-02/F-1   the §6.8 κ_f definition, the 9A block and OPEN-GEN-II-9 items 1–3 are present unchanged
 G5 CUSTODY     the two standard clauses and the nine GEN-ART custody rows are present unchanged
 G6 APPENDIX B  Appendix B is byte-identical
 G7 COMPACTION  tools/check_compaction.py returns PASS (exit 0) on STAGE1, CANDIDATE, MAP

Negative fixtures (--fixtures): each mutates the candidate or the map in a temporary directory, recomputes the
declared candidate hash where the fixture is about content, and requires tools/check_compaction.py to exit 1 with the
named check failing (F1–F8), or a guard to fail (F9).
"""
import copy, hashlib, json, os, re, subprocess, sys, tempfile

TOOL = "tools/check_compaction.py"

def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()
def span(s, a, b):
    i = s.index(a); return s[i:s.index(b, i)]
def body(s):
    return s[s.index("\n## Local Tag Aliases"):s.index("## Appendix A — Version History")]

def lines_with(s, pred): return [l for l in s.split("\n") if pred(l)]

def guards(s1, cand, mp, mpath, verbose=True):
    R = {}
    def g(k, ok, msg=""):
        R[k] = bool(ok)
        if verbose: print(f"[{'PASS' if ok else 'FAIL'}] {k} {msg}")
    g("G1", body(s1) == body(cand), "LIVE BODY")
    g("G2", span(s1, "### §6.3a ", "### §6.4 ") == span(cand, "### §6.3a ", "### §6.4 "), "§6.3a–c")
    ga01 = lines_with(s1, lambda l: "**Local sourced-junction theorem" in l or l.startswith("`[DEF]` Genesis may export theorem-grade")
                      or l.startswith("**[RETRACTED | RID: GEN-THM-SOURCED-JUNCTION]**"))
    g("G3", len(ga01) == 4 and all(cand.count(l) == 1 for l in ga01), f"GA-01 ({len(ga01)} lines)")
    ga02 = (lines_with(s1, lambda l: l.startswith("`[DEF]` **Face-lift magnitude, sign and $B_*$.**"))
            + [span(s1, "**(OPEN-GEN-II-9A) Scalar-M eigendecomposition.**", "`[RID: GEN-THM-SCALARM-EIGEN]`")]
            + [span(s1, "Closed under scalar-M (OPEN-GEN-II-9A", "4. Scalar susceptibility")])
    g("G4", len(ga02) == 3 and all(cand.count(x) == 1 for x in ga02), "GA-02/F-1")
    cust = lines_with(s1, lambda l: l.startswith("- `[custody-A]` ::") or l.startswith("- `[indep-AC]` ::")
                      or (l.startswith("- [RID: GEN-ART-") and "`[custody-A]`" in l))
    g("G5", len(cust) == 11 and all(cand.count(l) == 1 for l in cust), f"CUSTODY ({len(cust)} lines)")
    ab = lambda s: s[s.index("## Appendix B —"):s.index("*END OF DOCUMENT")]
    g("G6", ab(s1) == ab(cand), "APPENDIX B")
    with tempfile.TemporaryDirectory() as d:
        cp = os.path.join(d, "cand.md"); open(cp, "w", encoding="utf-8").write(cand)
        mp2 = os.path.join(d, "map.json"); json.dump(mp, open(mp2, "w", encoding="utf-8"), ensure_ascii=False)
        r = subprocess.run([sys.executable, "-I", TOOL, S1P, cp, mp2], capture_output=True, text=True)
    g("G7", r.returncode == 0 and "RESULT: PASS" in r.stdout, "COMPACTION (tools/check_compaction.py)")
    return R, r.stdout

def run_tool(cand, mp):
    with tempfile.TemporaryDirectory() as d:
        cp = os.path.join(d, "cand.md"); open(cp, "w", encoding="utf-8").write(cand)
        mp2 = os.path.join(d, "map.json"); json.dump(mp, open(mp2, "w", encoding="utf-8"), ensure_ascii=False)
        r = subprocess.run([sys.executable, "-I", TOOL, S1P, cp, mp2], capture_output=True, text=True)
    return r.returncode, r.stdout

def fixtures(s1, cand, mp):
    out = []
    def op(m, i): return next(o for o in m["operations"] if o["id"] == i)
    def content(c, m):  # content fixtures: declare the mutated candidate's hash so only the rule under test can fail
        m = copy.deepcopy(m); m["candidate_sha256"] = sha(c); return c, m
    F = []
    # F1 an undeclared edit inside §6.3c
    c = cand.replace("**G-SEL.** No physical model", "**G-SEL.** No physical models", 1); F.append(("F1 undeclared edit in §6.3c", *content(c, mp), "mechanical scope"))
    # F2 history entry names an identifier absent from the live text
    m = copy.deepcopy(mp); o = op(m, "S2-A"); o["new"] = o["new"].replace("`GEN-THM-QH-NOGO`", "`GEN-THM-QH-NOGO`, `GEN-THM-NOT-A-RID`", 1)
    c, _ = derive(s1, m); F.append(("F2 history names a non-live RID", *content(c, m), "operation S2-A"))
    # F3 status summary sentence not in the base summary or §1
    m = copy.deepcopy(mp); o = op(m, "S2-H"); o["new"] = o["new"].replace("Internal typing/model questions therefore remain OPEN", "Physical branch selection is settled. Internal typing/model questions therefore remain OPEN", 1)
    c, _ = derive(s1, m); F.append(("F3 status summary adds a claim", *content(c, m), "operation S2-H"))
    # F4 archive identity mismatch
    m = copy.deepcopy(mp); m["archives"][0]["sha256"] = "0" * 64; F.append(("F4 archive hash mismatch", cand, m, "archive identity"))
    # F5 a claim-bearing section relocated as history
    m = copy.deepcopy(mp); m["operations"].append({"id": "S2-X", "op": "replace-section", "class": "history-section", "archive": ["stage1-intermediate"],
        "start": "### §6.3c ", "end": "### §6.4 ", "new": "### §6.3c (relocated)\n\nSee the archive.\n\n"})
    c, _ = derive(s1, m); F.append(("F5 §6.3c relocated as history", *content(c, m), "operation S2-X"))
    # F6 two predecessors in Supersedes
    m = copy.deepcopy(mp); o = op(m, "S2-H"); o["new"] = o["new"].replace("tag `gen-v2.8.9`).", "tag `gen-v2.8.9`) · `RTG_GENESIS_GEOMETRY_DSN_v2.8.8`.", 1)
    c, _ = derive(s1, m); F.append(("F6 two predecessors in Supersedes", *content(c, m), "presentation"))
    # F7 two footer lines
    m = copy.deepcopy(mp); o = op(m, "S2-F"); o["new"] = o["new"] + "*END OF DOCUMENT — inherited footer*\n"
    c, _ = derive(s1, m); F.append(("F7 two footer lines", *content(c, m), "presentation"))
    # F8 a block moved out of its section
    blk = [b for b in body(s1).split("\n\n") if b.startswith("`[THM]` **Universal no-go** (§6.7, `GEN-THM-QH-NOGO`)")][0]
    m = copy.deepcopy(mp); m["operations"].append({"id": "S2-M", "op": "move", "class": "reorder", "block": blk, "before": "### §6.7 "})
    c, _ = derive(s1, m); F.append(("F8 move across sections", *content(c, m), "operation S2-M"))
    allok = True
    for name, c, m, must in F:
        rc, txt = run_tool(c, m)
        hit = any(l.startswith("FAIL") and must in l for l in txt.split("\n"))
        ok = rc == 1 and hit
        allok &= ok
        print(f"[{'CAUGHT' if ok else 'MISSED'}] {name}: exit {rc}; must fail '{must}'")
    # F9 guard: a content change the map declares honestly (a ref-subst inside the GA-01 statement) must still fail G1/G3
    m = copy.deepcopy(mp); m["operations"].append({"id": "S2-R", "op": "edit", "class": "ref-subst",
        "old": "selection of the physical branch is OPEN (GCL-02, §6.8). The foam", "new": "selection of the physical branch is OPEN (GCL-02, §6.8, see Appendix B). The foam"})
    c, m = content(derive(s1, m)[0], m)
    R, _ = guards(s1, c, m, None, verbose=False)
    ok = not R["G1"] and not R["G3"]
    allok &= ok
    print(f"[{'CAUGHT' if ok else 'MISSED'}] F9 GA-01 text changed through a declared edit: guards G1, G3 must fail (failed {sorted(k for k, v in R.items() if not v)})")
    print("\nall fixtures caught" if allok else "\nFIXTURE MISSED")
    return allok

def derive(s1, m):
    sys.path.insert(0, "tools")
    import check_compaction as cc
    return cc.apply_ops(s1, copy.deepcopy(m))

S1P = None

def main(argv):
    global S1P
    S1P, cp, mpath = argv[1:4]
    s1 = open(S1P, encoding="utf-8").read(); cand = open(cp, encoding="utf-8").read(); mp = json.load(open(mpath, encoding="utf-8"))
    if "--fixtures" in argv:
        sys.exit(0 if fixtures(s1, cand, mp) else 1)
    R, tool_out = guards(s1, cand, mp, mpath)
    n = sum(R.values())
    print(f"\n{n}/{len(R)} guards PASS; stage 1 {sha(s1)[:8]}…, candidate {sha(cand)}")
    sys.exit(0 if n == len(R) else 1)

if __name__ == "__main__":
    main(sys.argv)
