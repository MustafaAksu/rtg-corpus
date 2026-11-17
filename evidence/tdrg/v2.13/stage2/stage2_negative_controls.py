#!/usr/bin/env python3
"""Negative controls for the TDR-G v2.13 stage-2 movement map (adapted from evidence/az/v0.8/stage2/stage2_negative_controls.py).

    python3 -I evidence/tdrg/v2.13/stage2/stage2_negative_controls.py

Each case mutates the map (and re-derives the candidate with the checker's own apply_ops) or
the files, runs tools/check_compaction.py and requires FAIL (exit 1) with the expected check
named. The base is read from the stage-1 commit named in the map (git show) into a temporary
file and its SHA-256 is asserted against the map. The unmutated map must PASS. Exit 0 only if every case behaves as required.
"""
import copy, hashlib, importlib.util, json, os, subprocess, sys, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))
TOOL = os.path.join(ROOT, "tools", "check_compaction.py")
CAND = os.path.join(ROOT, "dsn/RTG_DISCRETE_GENESIS_DSN.md")
MAP = os.path.join(ROOT, "evidence/tdrg/v2.13/stage2/movement_map.json")
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
cases.append(("N1 undeclared change in the live text", lambda: run(mp0, cand.replace("Status: ACTIVE — PARTIAL", "Status: CLOSED", 1), rederive=False),
              1, "FAIL  mechanical scope"))
def n2():
    m = copy.deepcopy(mp0); h = op(m, "S2-H")
    h["new"] = h["new"].replace("on the canonical branch (SG-14).", "on the canonical branch (SG-14). TDR-6 is closed.")
    return run(m, None)
cases.append(("N2 status summary with a sentence not in the base", n2, 1, "FAIL  operation S2-H"))
def n3():
    m = copy.deepcopy(mp0)
    m["operations"].insert(1, {"id": "X3", "op": "edit", "class": "history-removal", "archive": ["stage1-intermediate"],
                               "old": "`[DEF]` [RID: TDRG-DEF-CANONICAL-BRANCH] **Canonical clean branch:**",
                               "new": "**Canonical clean branch:**", "note": "negative control"})
    return run(m, None)
cases.append(("N3 history-removal of a tagged, identified span", n3, 1, "FAIL  operation X3"))
def n4():
    m = copy.deepcopy(mp0); a = op(m, "S2-A")
    a["new"] = a["new"].replace("Plan `records/tdrg/TDRG_v2_13_EDIT_PLAN.md`", "TDRG-ALG-NEW-INVARIANT registered. Plan `records/tdrg/TDRG_v2_13_EDIT_PLAN.md`")
    return run(m, None)
cases.append(("N4 Appendix A names an identifier absent from the live text", n4, 1, "FAIL  operation S2-A"))
def n5():
    m = copy.deepcopy(mp0)
    m["operations"].insert(1, {"id": "X5", "op": "edit", "class": "history-removal", "archive": ["stage1-intermediate"],
                               "old": "Status: ACTIVE | Theoretically loaded", "new": "Status: ACTIVE", "note": "negative control"})
    return run(m, None)
cases.append(("N5 history-removal of a span not marked as history", n5, 1, "FAIL  operation X5"))
def n6():
    m = copy.deepcopy(mp0); f = op(m, "S2-F")
    f["new"] = f["new"] + "*END OF DOCUMENT — second footer*\n"
    return run(m, None)
cases.append(("N6 two footer lines", n6, 1, "FAIL  presentation"))
def n7():
    with tempfile.TemporaryDirectory() as d:
        b = os.path.join(d, "base.md")
        open(b, "w", encoding="utf-8", newline="").write(base.replace("Status: ACTIVE | Theoretically loaded", "Status: ACTIVE", 1))
        return run(mp0, None, base_path=b)
cases.append(("N7 base differs from the stage-1 intermediate", n7, 1, "FAIL  base identity"))
def n8():
    m = copy.deepcopy(mp0)
    m["operations"].insert(1, {"id": "X8", "op": "edit", "class": "ref-subst", "archive": ["stage1-intermediate"],
                               "old": "`[ALG]` [RID: TDRG-ALG-ORIENT-NOGO]", "new": "`[THM]` [RID: TDRG-ALG-ORIENT-NOGO]", "note": "negative control"})
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
