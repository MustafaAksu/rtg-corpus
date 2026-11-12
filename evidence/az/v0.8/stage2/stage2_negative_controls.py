#!/usr/bin/env python3
"""Negative controls for the AZ v0.8 stage-2 movement map.

    python3 -I evidence/az/v0.8/stage2/stage2_negative_controls.py

Each case mutates the map (and re-derives the candidate with the checker's own apply_ops) or
the files, runs tools/check_compaction.py and requires FAIL (exit 1) with the expected check
named. The unmutated map must PASS. Exit 0 only if every case behaves as required.
"""
import copy, hashlib, importlib.util, json, os, subprocess, sys, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))
TOOL = os.path.join(ROOT, "tools", "check_compaction.py")
BASE = os.path.join(ROOT, "evidence/az/v0.8/stage1_intermediate.md")
CAND = os.path.join(ROOT, "dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md")
MAP = os.path.join(ROOT, "evidence/az/v0.8/stage2/movement_map.json")
spec = importlib.util.spec_from_file_location("cc", TOOL); cc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cc)
sha = lambda b: hashlib.sha256(b).hexdigest()
base = open(BASE, encoding="utf-8").read()
cand = open(CAND, encoding="utf-8").read()
mp0 = json.load(open(MAP, encoding="utf-8"))


def run(mp, cand_text, base_path=BASE, rederive=True):
    mp = copy.deepcopy(mp)
    with tempfile.TemporaryDirectory() as d:
        if rederive:
            cc.PROFILE.clear(); cc.PROFILE.update(mp.get("profile", {}))
            cand_text, _ = cc.apply_ops(open(base_path, encoding="utf-8").read(), copy.deepcopy(mp))
        cp, mpth = os.path.join(d, "cand.md"), os.path.join(d, "map.json")
        open(cp, "w", encoding="utf-8", newline="").write(cand_text)
        mp["candidate_sha256"] = sha(cand_text.encode("utf-8"))
        for o in mp["operations"]:
            for k in [k for k in o if k.startswith("_")]:
                del o[k]
        json.dump(mp, open(mpth, "w", encoding="utf-8"), ensure_ascii=False)
        r = subprocess.run([sys.executable, TOOL, base_path, cp, mpth], capture_output=True, text=True, cwd=ROOT)
        return r.returncode, r.stdout


def op(mp, i):
    return next(o for o in mp["operations"] if o["id"] == i)


cases = []
# 0 positive
cases.append(("P0 unmutated map", lambda: run(mp0, cand, rederive=False), 0, "RESULT: PASS"))
# 1 undeclared change in the live text
cases.append(("N1 undeclared word in the live text", lambda: run(mp0, cand.replace("**Status: not met.**", "**Status: met.**", 1), rederive=False),
              1, "FAIL  mechanical scope"))
# 2 status summary adds a sentence that is not in the base
def n2():
    m = copy.deepcopy(mp0); h = op(m, "S2-H")
    h["new"] = h["new"].replace("**No Level B promotion.", "The angular rule is a dynamical signal. **No Level B promotion.")
    return run(m, None)
cases.append(("N2 status summary with a sentence not in the base", n2, 1, "FAIL  operation S2-H"))
# 3 a history-removal that deletes a claim tag and an identifier
def n3():
    m = copy.deepcopy(mp0)
    old = "so it is not specific to the dynamics. `[bridge-disqualified]` `[RID: TDRG-AZ-STATIC-ZN-4Q]`"
    m["operations"].insert(1, {"id": "X3", "op": "edit", "class": "history-removal", "archive": ["stage1-intermediate"],
                               "old": old, "new": "so it is not specific to the dynamics.", "note": "negative control"})
    return run(m, None)
cases.append(("N3 history-removal of a tagged, identified span", n3, 1, "FAIL  operation X3"))
# 4 the history appendix names an identifier that the live text does not carry (D4: no Action 1 entry through history)
def n4():
    m = copy.deepcopy(mp0); a = op(m, "S2-A")
    a["new"] = a["new"].replace("No new scientific result;", "The diagnostic `AZ-NUM-TOKRES-S1` is registered. No new scientific result;")
    return run(m, None)
cases.append(("N4 Appendix A names an identifier absent from the live text", n4, 1, "FAIL  operation S2-A"))
# 5 a reference substitution that changes a statement
def n5():
    m = copy.deepcopy(mp0); r = op(m, "S2-R1")
    r["new"] = "is established (Dyadic Appendix E, `dyad-v6.4.24`)."
    return run(m, None)
cases.append(("N5 reference substitution that changes a statement", n5, 1, "FAIL  operation S2-R1"))
# 6 two footer lines
def n6():
    m = copy.deepcopy(mp0); f = op(m, "S2-F")
    f["new"] = f["new"] + "*END OF DOCUMENT — second footer*\n"
    return run(m, None)
cases.append(("N6 two footer lines", n6, 1, "FAIL  presentation"))
# 7 the base is not the reviewed intermediate
def n7():
    with tempfile.TemporaryDirectory() as d:
        b = os.path.join(d, "base.md")
        open(b, "w", encoding="utf-8", newline="").write(base.replace("Level A, retained.", "Level B.", 1))
        return run(mp0, None, base_path=b)
cases.append(("N7 base differs from the reviewed intermediate", n7, 1, "FAIL  base identity"))
# 8 an owner pin changed in the live text through a declared 'reference substitution'
def n8():
    m = copy.deepcopy(mp0)
    m["operations"].insert(1, {"id": "X8", "op": "edit", "class": "ref-subst", "archive": ["stage1-intermediate"],
                               "old": "`[THM]` `[RID: PROP-AZ-CORE-EQUIV]`", "new": "`[ALG]` `[RID: PROP-AZ-CORE-EQUIV]`", "note": "negative control"})
    return run(m, None)
cases.append(("N8 a claim tag changed under the label of a reference substitution", n8, 1, "FAIL  operation X8"))

ok = True
for name, fn, want, needle in cases:
    code, out = fn()
    good = (code == want) and (needle in out)
    ok &= good
    line = next((l for l in out.split("\n") if l.startswith(needle.split("  ")[0]) and needle.split("  ", 1)[-1] in l), "")
    print("%s  %-62s exit %d (want %d)  %s" % ("OK  " if good else "BAD ", name, code, want, line[:150]))
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
