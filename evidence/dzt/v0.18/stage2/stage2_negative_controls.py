#!/usr/bin/env python3
"""Negative controls for the DZT v0.18 stage-2 movement map.

    python3 -I evidence/dzt/v0.18/stage2/stage2_negative_controls.py

Each case mutates the map (and re-derives the candidate with the checker's own apply_ops) or
the files, runs tools/check_compaction.py and requires FAIL (exit 1) with the expected check
named. The base is read from the reviewed commit named in the map (git show) into a temporary
file and its SHA-256 is asserted against the map. The unmutated map must PASS. Exit 0 only if every case behaves as required.
"""
import copy, hashlib, importlib.util, json, os, subprocess, sys, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))
TOOL = os.path.join(ROOT, "tools", "check_compaction.py")
CAND = os.path.join(ROOT, "dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md")
MAP = os.path.join(ROOT, "evidence/dzt/v0.18/stage2/movement_map.json")
spec = importlib.util.spec_from_file_location("cc", TOOL); cc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cc)
sha = lambda b: hashlib.sha256(b).hexdigest()
cand = open(CAND, encoding="utf-8").read()
mp0 = json.load(open(MAP, encoding="utf-8"))
_tmp = tempfile.TemporaryDirectory()
BASE = os.path.join(_tmp.name, "stage1_intermediate.md")
_b = subprocess.run(["git", "-C", ROOT, "show", mp0["base"]], capture_output=True, check=True).stdout
if sha(_b) != mp0["base_sha256"]:
    sys.exit("base read from %s does not have the hash named in the map" % mp0["base"])
open(BASE, "wb").write(_b)
base = _b.decode("utf-8")
print("base: git show %s  sha256 %s" % (mp0["base"], sha(_b)))


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
cases.append(("P0 unmutated map", lambda: run(mp0, cand, rederive=False), 0, "RESULT: PASS"))
# 1 undeclared change in the live text
cases.append(("N1 undeclared word in the live text", lambda: run(mp0, cand.replace("is false ($p=40$ gives", "is true ($p=40$ gives", 1), rederive=False),
              1, "FAIL  mechanical scope"))
# 2 status summary adds a sentence that is not in the base (a v0.17 theorem through the header)
def n2():
    m = copy.deepcopy(mp0); h = op(m, "S2-H")
    h["new"] = h["new"].replace("No Dyadic result is re-owned here;", "The anomaly rule is proved for all $p$. No Dyadic result is re-owned here;")
    return run(m, None)
cases.append(("N2 status summary with a sentence not in the base", n2, 1, "FAIL  operation S2-H"))
# 3 a history-removal that deletes an identifier
def n3():
    m = copy.deepcopy(mp0)
    m["operations"].insert(1, {"id": "X3", "op": "edit", "class": "history-removal", "archive": ["stage1-intermediate"],
                               "old": "`[scope: finite horizon]` ✓ [RID: DZT-ALG-CASCADE-ROW]", "new": "`[scope: finite horizon]` ✓",
                               "note": "negative control"})
    return run(m, None)
cases.append(("N3 history-removal of an identified span", n3, 1, "FAIL  operation X3"))
# 4 the history appendix names an identifier absent from the live text (a recovered theorem entering through history)
def n4():
    m = copy.deepcopy(mp0); a = op(m, "S2-A")
    a["new"] = a["new"].replace("their content enters v0.18 only through the corrections above.",
                                "DZT-THM-CASCADE-DENOMINATOR is registered.")
    return run(m, None)
cases.append(("N4 Appendix A names an identifier absent from the live text", n4, 1, "FAIL  operation S2-A"))
# 5 a claim tag changed under the label of a reference substitution
def n5():
    m = copy.deepcopy(mp0)
    m["operations"].insert(1, {"id": "X5", "op": "edit", "class": "ref-subst", "archive": ["stage1-intermediate"],
                               "old": "`[ALG]` `[RID: DZT-ALG-CASCADE-NORM]`", "new": "`[THM]` `[RID: DZT-ALG-CASCADE-NORM]`", "note": "negative control"})
    return run(m, None)
cases.append(("N5 a claim tag changed under the label of a reference substitution", n5, 1, "FAIL  operation X5"))
# 6 two footer lines
def n6():
    m = copy.deepcopy(mp0); f = op(m, "S2-F")
    f["new"] = f["new"] + "*END OF DOCUMENT — second footer*\n"
    return run(m, None)
cases.append(("N6 two footer lines", n6, 1, "FAIL  presentation"))
# 7 the base is not the stage-1 intermediate
def n7():
    with tempfile.TemporaryDirectory() as d:
        b = os.path.join(d, "base.md")
        open(b, "w", encoding="utf-8", newline="").write(base.replace("is false ($p=40$ gives", "is false ($p=44$ gives", 1))
        return run(mp0, None, base_path=b)
cases.append(("N7 base differs from the stage-1 intermediate", n7, 1, "FAIL  base identity"))
# 8 predecessor named without its hash
def n8():
    m = copy.deepcopy(mp0); h = op(m, "S2-H")
    h["new"] = h["new"].replace("SHA-256 `cad20982d294775d52592c304d743695c6ec2d8cf4975c78de203db3d6a92ff2`", "SHA-256 not recorded")
    return run(m, None)
cases.append(("N8 predecessor without its hash", n8, 1, "FAIL  presentation"))

ok = True
for name, fn, want, needle in cases:
    code, out = fn()
    good = (code == want) and (needle in out)
    ok &= good
    line = next((l for l in out.split("\n") if l.startswith(needle.split("  ")[0]) and needle.split("  ", 1)[-1] in l), "")
    print("%s  %-62s exit %d (want %d)  %s" % ("OK  " if good else "BAD ", name, code, want, line[:150]))
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
