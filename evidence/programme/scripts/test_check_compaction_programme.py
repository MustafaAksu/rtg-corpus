#!/usr/bin/env python3
"""Negative controls for the Programme v1.3 compaction (stage 2), plus Programme-specific invariants.

    python -I evidence/programme/scripts/test_check_compaction_programme.py INTERMEDIATE CANDIDATE MAP [--report OUT.json]

Two checkers run on every triple:
  * tools/check_compaction.py (shared tool, Programme profile from the map);
  * the Programme invariants below (programme_invariants): the five OPEN-P RIDs and their ACTIVE lines, the SG-PROG-1..4
    paragraphs, the §6.1 inventory table, the §7.2 register and Appendix B are byte-identical to the stage-1 intermediate;
    every <a id> anchor of the intermediate except the removed Appendix C anchor survives.
The shared tool cannot see that a guard paragraph is live (it carries no claim tag), so N9 is caught by the invariants
only; that is why both run. The real triple must PASS both; every mutation must FAIL at least one.
"""
import argparse, copy, hashlib, json, os, re, sys, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import test_check_compaction as T  # noqa: E402

OPEN_RIDS = ["RTG-OPEN-GENERATOR-SELECTION", "RTG-OPEN-DISCRETE-BRIDGE", "RTG-OPEN-TRIAD-PRIMACY-ONTO",
             "RTG-OPEN-TRIAD-REDUCTION", "RTG-OPEN-REGGE-BRIDGE"]

def block(t, start, end):
    i = t.find(start); j = t.find(end, i + 1)
    return t[i:j] if i >= 0 and j > i else None

def programme_invariants(inter, cand):
    probs = []
    for r in OPEN_RIDS:
        if cand.count(f"**RID:** `{r}`") != 1: probs.append(f"RID {r}")
    if cand.count("**Status:** ACTIVE") != 5: probs.append("ACTIVE count")
    for n in (1, 2, 3, 4):
        a, b = block(inter, f"**[SG-PROG-{n}]", "\n\n"), block(cand, f"**[SG-PROG-{n}]", "\n\n")
        if a != b: probs.append(f"SG-PROG-{n} text")
    for name, s, e in (("§6.1 table", "| Key | Document (fixed path) |", "\nGenesis's own header"),
                       ("§7.2 register", "| IF | From → To |", "\n### 7.3"),
                       ("Appendix B", "## Appendix B — Adopted Replacements", "\n---\n")):
        if block(inter, s, e) != block(cand, s, e): probs.append(name)
    anchors = set(re.findall(r'<a id="[^"]+"></a>', inter)) - {'<a id="prog-sources"></a>'}
    missing = [a for a in anchors if a not in cand]
    if missing: probs.append(f"anchors {missing}")
    return probs

def run_both(inter, cand, mp, tmp, name):
    rc, fails = T.run(inter, cand, mp, tmp, name)
    inv = programme_invariants(inter, cand)
    return rc, fails, inv

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inter"); ap.add_argument("cand"); ap.add_argument("map"); ap.add_argument("--report")
    a = ap.parse_args()
    inter = open(a.inter, encoding="utf-8").read(); cand = open(a.cand, encoding="utf-8").read()
    mp = json.load(open(a.map, encoding="utf-8"))
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        rc, f, inv = run_both(inter, cand, mp, tmp, "P0")
        out.append({"id": "P0", "what": "unmutated inputs", "expect": "PASS", "got": "PASS" if rc == 0 and not inv else "FAIL", "tool_fails": f, "invariants": inv})

        def control(cid, what, mutate, expect_tool=None):
            res = mutate()
            if res is None:
                out.append({"id": cid, "what": what, "expect": "FAIL", "got": "NOT APPLICABLE"}); return
            i2, c2, m2 = res
            rc, f, inv = run_both(i2, c2, m2, tmp, cid)
            got = "FAIL" if (rc != 0 or inv) else "PASS"
            out.append({"id": cid, "what": what, "expect": "FAIL", "got": got, "tool_rc": rc, "tool_fails": f, "invariants": inv})

        def declared(old, new, cls, archive=("programme-v1.2",)):
            if inter.count(old) != 1 or cand.count(old) != 1: return None
            m = copy.deepcopy(mp)
            m["operations"].insert(0, {"id": "X", "op": "edit", "class": cls, "old": old, "new": new, "archive": list(archive)})
            return inter, cand.replace(old, new, 1), m

        control("N1", "undeclared deletion of a [DEF] tag in §4", lambda: (inter, cand.replace("`[DEF]` Maturity describes", "Maturity describes", 1), mp))
        control("N2", "undeclared edit of the §6.1 inventory table", lambda: (inter, cand.replace("| v6.4.22 | `dyad-v6.4.22` |", "| v6.4.21 | `dyad-v6.4.22` |", 1), mp))
        def n3():
            m = copy.deepcopy(mp)
            start = "\n<a id=\"prog-corrections\"></a>\n## Appendix B — Adopted Replacements of v1.1 Programme Statements"
            end = "\n---\n\n*END OF DOCUMENT"
            i = cand.find(start); j = cand.find(end, i + 1)
            if i < 0 or j < 0: return None
            m["operations"].append({"id": "X3", "op": "replace-section", "class": "history-section", "start": start, "end": end, "new": "", "archive": ["programme-v1.2"]})
            return inter, cand[:i] + cand[j:], m
        control("N3", "Appendix B relocated as history (claim-tag spellings in prose)", n3)
        control("N4", "ref-subst that changes a non-reference word", lambda: declared("No merger is enacted.", "No merger is proposed.", "ref-subst"))
        def n5():
            m = copy.deepcopy(mp)
            for op in m["operations"]:
                if op["id"] == "M01": op["new"] = op["new"].replace("programme-v1.2", "programme-v1.9")
            return inter, cand.replace("(tag `programme-v1.2`), PREL.", "(tag `programme-v1.9`), PREL.", 1), m
        control("N5", "pointer to a nonexistent tagged edition (declared)", n5)
        control("N6", "two footer lines", lambda: (inter, cand.rstrip("\n") + "\n*END OF DOCUMENT — duplicate.*\n", mp))
        control("N7", "OPEN-P status changed, declared as ref-subst", lambda: declared("**RID:** `RTG-OPEN-REGGE-BRIDGE`  \n**Status:** ACTIVE", "**RID:** `RTG-OPEN-REGGE-BRIDGE`  \n**Status:** CLOSED", "ref-subst"))
        def n8():
            m = copy.deepcopy(mp)
            start = "**[SG-PROG-2] — Model selection is not local proof status.**"
            i = cand.find(start); j = cand.find("\n\n", i)
            if i < 0: return None
            m["operations"].append({"id": "X8", "op": "replace-section", "class": "history-section", "start": start, "end": "\n\n", "new": "", "archive": ["programme-v1.2"]})
            return inter, cand[:i] + cand[j:], m
        control("N8", "SG-PROG-2 removed, declared as history-section (tool-blind; invariants catch it)", n8)
        control("N9", "undeclared removal of an <a id> anchor", lambda: (inter, cand.replace('<a id="prog-guards"></a>\n', "", 1), mp))
        control("N10", "§7.2 register row edited undeclared", lambda: (inter, cand.replace("| GEN §7 | v6.4.13 |", "| GEN §7 | v6.4.22 |", 1), mp))

    ok = out[0]["got"] == "PASS" and all(r["got"] == "FAIL" for r in out[1:])
    for r in out:
        tag = "ok " if (r["id"] == "P0" and r["got"] == "PASS") or (r["id"] != "P0" and r["got"] == "FAIL") else "MISS"
        print(f"{tag} {r['id']:4s} expect {r['expect']} got {r['got']:14s} {r['what']}")
        if r.get("invariants"): print(f"         invariants: {r['invariants']}")
    n = sum(1 for r in out[1:] if r["got"] == "FAIL")
    print(f"RESULT: {'PASS' if ok else 'FAIL'} ({n}/{len(out)-1} controls rejected)")
    if a.report:
        json.dump({"result": "PASS" if ok else "FAIL", "controls": out}, open(a.report, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
