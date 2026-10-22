#!/usr/bin/env python3
"""Negative controls for tools/check_compaction.py.

    test_check_compaction.py BASE CANDIDATE MAP [--report OUT.json]

Runs the checker on the real (BASE, CANDIDATE, MAP) triple, which must PASS, and on
mutated copies, each of which must FAIL. A control whose pattern is absent from the
inputs is reported as NOT APPLICABLE and counts as a failure of this harness.
Exit 0 only if the positive run passes and every control is rejected.
"""
import argparse, copy, hashlib, json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKER = os.path.join(HERE, "check_compaction.py")


def sha(t):
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def run(base, cand, mp, tmp, name):
    d = os.path.join(tmp, name); os.makedirs(d, exist_ok=True)
    bp, cp, mpp = (os.path.join(d, x) for x in ("base.md", "cand.md", "map.json"))
    open(bp, "w", encoding="utf-8").write(base)
    open(cp, "w", encoding="utf-8").write(cand)
    mp = copy.deepcopy(mp)
    mp["base_sha256"], mp["candidate_sha256"] = sha(base), sha(cand)
    for op in mp["operations"]:
        op.pop("_removed", None)
    json.dump(mp, open(mpp, "w", encoding="utf-8"), ensure_ascii=False)
    r = subprocess.run([sys.executable, CHECKER, bp, cp, mpp], capture_output=True, text=True)
    fails = [l for l in r.stdout.splitlines() if l.startswith("FAIL")]
    return r.returncode, fails


def live_once(cand, pat):
    """Index of the first occurrence of pat in the live body (after the header, before Appendix A)."""
    start = cand.index("\n## ")
    end = cand.find("\n## Appendix A")
    i = cand.find(pat, start, end if end > 0 else None)
    return i


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("base"); ap.add_argument("candidate"); ap.add_argument("map")
    ap.add_argument("--report")
    a = ap.parse_args()
    base = open(a.base, encoding="utf-8").read()
    cand = open(a.candidate, encoding="utf-8").read()
    mp = json.load(open(a.map, encoding="utf-8"))
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        rc, f = run(base, cand, mp, tmp, "P0")
        out.append({"id": "P0", "what": "unmutated inputs", "expect": "PASS", "got": "PASS" if rc == 0 else "FAIL", "fails": f})

        def control(cid, what, mutate):
            res = mutate()
            if res is None:
                out.append({"id": cid, "what": what, "expect": "FAIL", "got": "NOT APPLICABLE"}); return
            b2, c2, m2 = res
            rc, f = run(b2, c2, m2, tmp, cid)
            out.append({"id": cid, "what": what, "expect": "FAIL", "got": "FAIL" if rc == 1 else ("PASS" if rc == 0 else f"ERROR {rc}"), "fails": f})

        Q = "`[assuming: RECOG-THM-R9-MEMORY]` "

        def n1():  # silent assumption deletion, undeclared
            i = live_once(cand, Q)
            if i < 0: return None
            return base, cand[:i] + cand[i + len(Q):], mp
        control("N1", "silent deletion of an [assuming:] qualifier (undeclared)", n1)

        def n2():  # assumption deletion declared as history removal
            i = live_once(cand, Q)
            if i < 0: return None
            line_start = cand.rfind("\n", 0, i) + 1; line_end = cand.index("\n", i)
            old = cand[line_start:line_end]; new = old.replace(Q, "", 1)
            if base.count(old) != 1: return None
            m = copy.deepcopy(mp)
            m["operations"].insert(1, {"id": "X2", "op": "edit", "class": "history-removal", "old": old, "new": new, "archive": ["dyad-v6.4.20"]})
            return base, cand.replace(old, new, 1), m
        control("N2", "deletion of an [assuming:] qualifier declared as history removal", n2)

        def n3():  # scope widening declared as a reference substitution
            pat = "$p\\ge5$"
            i = live_once(cand, pat)
            if i < 0: return None
            line_start = cand.rfind("\n", 0, i) + 1; line_end = cand.index("\n", i)
            old = cand[line_start:line_end]
            if base.count(old) != 1: return None
            new = old.replace(pat, "$p\\ge3$", 1) + " (tag `dyad-v6.4.20`)"
            m = copy.deepcopy(mp)
            m["operations"].insert(1, {"id": "X3", "op": "edit", "class": "ref-subst", "old": old, "new": new, "archive": ["dyad-v6.4.20"]})
            return base, cand.replace(old, new, 1), m
        control("N3", "scope widening ($p\\ge5$ → $p\\ge3$) declared as a reference substitution", n3)

        def n4():  # wrong RID association, declared
            pat = "(`DYAD-THM-OPEN3-SPIRAL-REM`, §6.14)."
            i = live_once(cand, pat)
            if i < 0: return None
            line_start = cand.rfind("\n", 0, i) + 1; line_end = cand.index("\n", i)
            old = cand[line_start:line_end]
            if base.count(old) != 1: return None
            new = old.replace(pat, "(`DYAD-THM-OPEN3-ASYMPTOTIC-PHASE`, §6.14, tag `dyad-v6.4.20`).", 1)
            m = copy.deepcopy(mp)
            m["operations"].insert(1, {"id": "X4", "op": "edit", "class": "ref-subst", "old": old, "new": new, "archive": ["dyad-v6.4.20"]})
            return base, cand.replace(old, new, 1), m
        control("N4", "result re-attributed to another RID, declared as a reference substitution", n4)

        def n4b():  # wrong RID association, undeclared swap
            p1, p2 = "`DYAD-THM-OPEN3-SPIRAL-REM`", "`DYAD-THM-OPEN3-ASYMPTOTIC-PHASE`"
            i = live_once(cand, p1)
            if i < 0: return None
            return base, cand[:i] + p2 + cand[i + len(p1):], mp
        control("N4b", "result re-attributed to another RID (undeclared)", n4b)

        def n5():  # broken source link: pointer to a tag that does not exist
            ops = [o for o in mp["operations"] if o["op"] == "edit" and o.get("class") == "ref-subst" and "`dyad-v6.4.20`" in o["new"]]
            if not ops: return None
            m = copy.deepcopy(mp); o = next(x for x in m["operations"] if x["id"] == ops[0]["id"])
            bad = o["new"].replace("`dyad-v6.4.20`", "`dyad-v6.4.99`").replace("v6.4.20", "v6.4.99")
            c2 = cand.replace(o["new"], bad, 1); o["new"] = bad
            return base, c2, m
        control("N5", "pointer repointed to a nonexistent tagged edition", n5)

        def n5b():  # broken link: reference to an appendix that does not exist
            ops = [o for o in mp["operations"] if o["op"] == "edit" and o.get("class") == "ref-subst"]
            if not ops: return None
            m = copy.deepcopy(mp); o = next(x for x in m["operations"] if x["id"] == ops[0]["id"])
            bad = re.sub(r"\(tag `dyad-v6\.4\.20`[^)]*\)|tag `dyad-v6\.4\.20`", "Appendix Q", o["new"], count=1)
            if bad == o["new"]: return None
            c2 = cand.replace(o["new"], bad, 1); o["new"] = bad
            return base, c2, m
        control("N5b", "pointer to a nonexistent appendix", n5b)

        def n6():  # removed passage not in the archive
            m = copy.deepcopy(mp)
            fake = os.path.join(tmp, "fake_archive.md")
            open(fake, "w", encoding="utf-8").write("unrelated text\n")
            for x in m["archives"]:
                x.pop("git", None); x["path"] = fake; x["sha256"] = hashlib.sha256(open(fake, "rb").read()).hexdigest()
            return base, cand, m
        control("N6", "removed passages not present in the named archive", n6)

        def n7():  # a live result relocated out of the file as "history"
            start, end = "\n### §6.17", "\n## §7."
            if base.count(start) != 1 or end not in base: return None
            i = base.index(start); j = base.index(end, i)
            ptr = "\n### §6.17 relocated\n\nSee v6.4.20 (tag `dyad-v6.4.20`).\n"
            m = copy.deepcopy(mp)
            m["operations"].insert(1, {"id": "X7", "op": "replace-section", "class": "history-section", "start": start, "end": end, "new": ptr, "archive": ["dyad-v6.4.20"]})
            ci = cand.index(start); cj = cand.index(end, ci)
            return base, cand[:ci] + ptr + cand[cj:], m
        control("N7", "live results (§6.17) relocated as a history section", n7)

        def n8():  # two footers
            return base, cand.replace("*END OF DOCUMENT", "*END OF DOCUMENT — extra*\n*END OF DOCUMENT", 1), mp
        control("N8", "two footer lines", n8)

        def n9():  # a source hash pin changed, undeclared
            m = re.search(r"`([0-9a-f]{64})`", cand[cand.index("\n## "):])
            if not m: return None
            h = m.group(1); h2 = ("0" if h[0] != "0" else "1") + h[1:]
            return base, cand.replace(h, h2, 1), mp
        control("N9", "source hash pin altered (undeclared)", n9)

        def n10():  # a block with a result silently dropped
            pat = "`[THM]` `[v6.4.18]`"
            i = live_once(cand, pat)
            if i < 0: return None
            line_start = cand.rfind("\n", 0, i) + 1; line_end = cand.index("\n", i)
            return base, cand[:line_start] + cand[line_end + 1:], mp
        control("N10", "a result paragraph deleted (undeclared)", n10)

    ok = out[0]["got"] == "PASS" and all(r["got"] == "FAIL" for r in out[1:])
    for r in out:
        flag = "ok " if (r["got"] == r["expect"]) else "BAD"
        print(f'{flag} {r["id"]:4} expect {r["expect"]:4} got {r["got"]:14} {r["what"]}')
        for f in r.get("fails", [])[:3]:
            if r["id"] != "P0":
                print("        ", f[:150])
    print("RESULT:", "PASS" if ok else "FAIL", f"({sum(r['got']=='FAIL' for r in out[1:])}/{len(out)-1} controls rejected)")
    if a.report:
        json.dump({"result": "PASS" if ok else "FAIL", "runs": out}, open(a.report, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
