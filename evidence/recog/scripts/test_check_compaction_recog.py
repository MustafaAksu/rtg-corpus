#!/usr/bin/env python3
"""Negative controls for tools/check_compaction.py on the RECOG profile (v0.3.23 stage 2).

    python -I evidence/recog/scripts/test_check_compaction_recog.py BASE CANDIDATE MAP [--report OUT.json]

The DYAD harness tools/test_check_compaction.py uses DYAD patterns, so on RECOG most of its controls
would be NOT APPLICABLE. This harness runs the same kinds of mutation with RECOG patterns: the real
triple must PASS and every mutated triple must FAIL. A control whose pattern is absent counts as a
failure of the harness. Run from the repository root (the archives are read with git show).
"""
import argparse, copy, hashlib, json, os, sys, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import test_check_compaction as T  # noqa: E402  (reuses its run(): writes the triple, calls the checker)


def live_once(cand, pat):
    return T.live_once(cand, pat)


def line_at(s, i):
    a = s.rfind("\n", 0, i) + 1; b = s.index("\n", i)
    return s[a:b]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("base"); ap.add_argument("candidate"); ap.add_argument("map"); ap.add_argument("--report")
    a = ap.parse_args()
    base = open(a.base, encoding="utf-8").read(); cand = open(a.candidate, encoding="utf-8").read()
    mp = json.load(open(a.map, encoding="utf-8"))
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        rc, f = T.run(base, cand, mp, tmp, "P0")
        out.append({"id": "P0", "what": "unmutated inputs", "expect": "PASS", "got": "PASS" if rc == 0 else "FAIL", "fails": f})

        def control(cid, what, mutate):
            res = mutate()
            if res is None:
                out.append({"id": cid, "what": what, "expect": "FAIL", "got": "NOT APPLICABLE"}); return
            b2, c2, m2 = res
            rc, f = T.run(b2, c2, m2, tmp, cid)
            out.append({"id": cid, "what": what, "expect": "FAIL",
                        "got": "FAIL" if rc == 1 else ("PASS" if rc == 0 else f"ERROR {rc}"), "fails": f})

        def declared(old, new, cls, pos=1):
            if base.count(old) != 1 or cand.count(old) != 1: return None
            m = copy.deepcopy(mp)
            m["operations"].insert(pos, {"id": "X", "op": "edit", "class": cls, "old": old, "new": new, "archive": ["recog-v0.3.22"]})
            return base, cand.replace(old, new, 1), m

        Q = "`[assuming: RECOG-THM-R9-MEMORY]` "

        def n1():
            i = live_once(cand, Q)
            return None if i < 0 else (base, cand[:i] + cand[i + len(Q):], mp)
        control("N1", "silent deletion of an [assuming:] qualifier (undeclared)", n1)

        def n2():
            i = live_once(cand, Q)
            if i < 0: return None
            old = line_at(cand, i)
            return declared(old, old.replace(Q, "", 1), "history-removal")
        control("N2", "deletion of an [assuming:] qualifier declared as history removal", n2)

        def n3():
            pat = "**Resonant-return family ($p\\ge5$).**"
            i = live_once(cand, pat)
            if i < 0: return None
            old = line_at(cand, i)
            return declared(old, old.replace("$p\\ge5$", "$p\\ge3$", 1) + " (tag `recog-v0.3.22`)", "ref-subst")
        control("N3", "scope widening ($p\\ge5$ → $p\\ge3$) declared as a reference substitution", n3)

        def n4():
            pat = "(RECOG-THM-R9-COMPARATOR-INCOMPLETENESS, §6.13a)."
            i = live_once(cand, pat)
            if i < 0: return None
            old = line_at(cand, i)
            return declared(old, old.replace(pat, "(RECOG-THM-R9-MEMORY, §6.13a, tag `recog-v0.3.22`).", 1), "ref-subst")
        control("N4", "result re-attributed to another RID, declared as a reference substitution", n4)

        def n4b():
            p1, p2 = "[RID: RECOG-THM-R9-COMPARATOR-INCOMPLETENESS]", "[RID: RECOG-THM-R9-MEMORY]"
            i = cand.find(p1, cand.index("#### §6.13a"))
            return None if i < 0 else (base, cand[:i] + p2 + cand[i + len(p1):], mp)
        control("N4b", "RID declaration moved to another statement (undeclared)", n4b)

        def n5():
            m = copy.deepcopy(mp); o = next((x for x in m["operations"] if x["id"] == "M05"), None)
            if o is None: return None
            bad = o["new"].replace("`recog-v0.3.22`", "`recog-v0.3.99`")
            c2 = cand.replace(o["new"], bad, 1); o["new"] = bad
            return base, c2, m
        control("N5", "pointer repointed to a nonexistent tagged edition", n5)

        def n5b():
            m = copy.deepcopy(mp); o = next((x for x in m["operations"] if x["id"] == "M05"), None)
            if o is None: return None
            bad = o["new"].replace("(tag `recog-v0.3.22`)", "(Appendix Q)")
            c2 = cand.replace(o["new"], bad, 1); o["new"] = bad
            return base, c2, m
        control("N5b", "pointer to a nonexistent appendix", n5b)

        def n6():
            m = copy.deepcopy(mp)
            fake = os.path.join(tmp, "fake_archive.md"); open(fake, "w", encoding="utf-8").write("unrelated text\n")
            for x in m["archives"]:
                x.pop("git", None); x["path"] = fake; x["sha256"] = hashlib.sha256(open(fake, "rb").read()).hexdigest()
            return base, cand, m
        control("N6", "removed passages not present in the named archive", n6)

        def n7():
            start, end = "\n#### §6.13a", "\n#### §6.13b"
            if base.count(start) != 1: return None
            ptr = "\n#### §6.13a relocated\n\nSee v0.3.22 (tag `recog-v0.3.22`).\n"
            m = copy.deepcopy(mp)
            m["operations"].insert(1, {"id": "X7", "op": "replace-section", "class": "history-section", "start": start, "end": end, "new": ptr, "archive": ["recog-v0.3.22"]})
            ci = cand.index(start); cj = cand.index(end, ci)
            return base, cand[:ci] + ptr + cand[cj:], m
        control("N7", "live results (§6.13a, R9) relocated as a history section", n7)

        def n8():
            return base, cand.replace("*END OF DOCUMENT", "*END OF DOCUMENT — extra*\n*END OF DOCUMENT", 1), mp
        control("N8", "two footer lines", n8)

        def n9():
            import re
            mm = re.search(r"`([0-9a-f]{64})`", cand[cand.index("\n## "):])
            if not mm: return None
            h = mm.group(1); h2 = ("0" if h[0] != "0" else "1") + h[1:]
            return base, cand.replace(h, h2, 1), mp
        control("N9", "source hash pin altered (undeclared)", n9)

        def n10():
            pat = "`[THM]` [RID: RECOG-THM-A1A-PHASE-EXISTENCE-U] [scope:"
            i = live_once(cand, pat)
            if i < 0: return None
            a_ = cand.rfind("\n", 0, i) + 1; b_ = cand.index("\n", i)
            return base, cand[:a_] + cand[b_ + 1:], mp
        control("N10", "a theorem paragraph deleted (undeclared)", n10)

        def n11():
            pat = "`[ALG]` [cert: check 8] **R9 partial budget"
            i = live_once(cand, pat)
            if i < 0: return None
            old = line_at(cand, i)
            return declared(old, old.replace("[cert: check 8] ", "", 1), "history-removal")
        control("N11", "evidence pointer deleted, declared as history removal", n11)

        def n12():
            pat = "Status: **CLOSED (v0.3.2) — delivered and accepted** — owner adoption"
            return declared(pat, "Status: **DELIVERED and ACCEPTED (v0.3.2)** (tag `recog-v0.3.22`) — owner adoption", "ref-subst")
        control("N12", "stale state restored (R10 wording), declared as a reference substitution", n12)

        def n13():
            m = copy.deepcopy(mp); o = next(x for x in m["operations"] if x["id"] == "M01")
            bad = o["new"].replace(" R6 stays ACTIVE.", " R6 stays ACTIVE. R9 is unconditional.", 1)
            if bad == o["new"]: return None
            c2 = cand.replace(o["new"], bad, 1); o["new"] = bad
            return base, c2, m
        control("N13", "status summary adds a sentence absent from the base", n13)

        def n14():
            pat = "Status: ACTIVE (sharpened v0.3; identifiability audited v0.3.7)"
            i = live_once(cand, pat)
            return None if i < 0 else (base, cand.replace(pat, "Status: CLOSED (sharpened v0.3; identifiability audited v0.3.7)", 1), mp)
        control("N14", "OPEN status altered (R6, undeclared)", n14)

        def n15():
            pat = "**Former OPEN R11 text (v0.3.1), retained for the record:**"
            if base.count(pat) != 1: return None
            start, end = "\n" + pat, "\nDependencies:\n- Dyadic §6.2 ($h_2$)"
            if base.count(end) != 1: return None
            m = copy.deepcopy(mp)
            m["operations"].insert(1, {"id": "X15", "op": "replace-section", "class": "history-section", "start": start, "end": end, "new": "", "archive": ["recog-v0.3.22"]})
            ci = cand.index(start); cj = cand.index(end, ci)
            return base, cand[:ci] + cand[cj:], m
        control("N15", "tagged history ([OPEN] sub-items of former R11) relocated as a history section", n15)

    ok = out[0]["got"] == "PASS" and all(r["got"] == "FAIL" for r in out[1:])
    return T.finish(a, out, ok)


if __name__ == "__main__":
    sys.exit(main())
