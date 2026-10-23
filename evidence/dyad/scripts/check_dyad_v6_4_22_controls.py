#!/usr/bin/env python3
"""check_dyad_v6_4_22_controls.py -- negative controls for check_dyad_v6_4_22.py.
Each control mutates a temporary copy of the candidate and runs the checker (--norebuild; N0 with rebuild).
A control is as expected when the checker exits 1 with the expected gate among the failing gates.
usage: check_dyad_v6_4_22_controls.py --base V6421 --cand CANDIDATE [--out JSON]    exit 0 all as expected / 1 otherwise
"""
import argparse, json, os, re, subprocess, sys, tempfile, shutil
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))


def one(s, old, new):
    assert s.count(old) >= 1, old
    return s.replace(old, new, 1)


def sec(s, a, b, old, new):
    i = s.index(a); j = s.index(b, i); seg = s[i:j]; assert old in seg, old
    return s[:i] + seg.replace(old, new, 1) + s[j:]


CONTROLS = [
 ("Q1", "C4", "one OPEN-M R11 written bare again (§6.12)", lambda s: one(s, "which OPEN-M R11 does not fix", "which R11 does not fix")),
 ("Q2", "C4", "an OPEN-M occurrence relabelled RECOG (§6.12 factor)", lambda s: one(s, "via the OPEN-M R11 factor $3/4$", "via the RECOG R11 factor $3/4$")),
 ("Q3", "C5", "stale replay wording restored (§8)", lambda s: one(s, "owner replay; reviewer replay of the main gate separately (v6.4.19 release verification), combined G14–G15 run and separate-process M1–M4 exit codes not completed", "owner replay; reviewer full replay pending")),
 ("Q4", "C3", "constant changed in §6.14 (403/250 -> 403/251)", lambda s: sec(s, "## §6.", "## §7.", "403}{250}", "403}{251}")),
 ("Q5", "C3", "grade tag changed in §6 (ALG -> THM)", lambda s: one(s, "`[ALG]` **Eigenframe linear-part lemma.**", "`[THM]` **Eigenframe linear-part lemma.**")),
 ("Q6", "C3", "one RID tag removed", lambda s: one(s, "[RID: DYAD-ALG-P5-RADIAL]", "DYAD-ALG-P5-RADIAL")),
 ("Q7", "C2", "older Appendix A entry edited", lambda s: one(s, "- v6.4.19 — adopted 20 October 2026", "- v6.4.19 — adopted 21 October 2026")),
 ("Q8", "C7", "a section 2 Status line changed", lambda s: sec(s, "## §2.", "## §3.", "Status: ", "Status:  ")),
 ("Q9", "C6", "header status set to ADOPTED", lambda s: one(s, "**Document status:** DRAFT — v6.4.22 candidate", "**Document status:** ADOPTED — v6.4.22 candidate")),
 ("Q10", "C8", "cited hash of the h4 second-route script altered", lambda s: one(s, "dd06a1a20466dbe16da9c9b2e5bfe01a209decbedeed5a2c4a3ba33c783c1e6d", "dd06a1a20466dbe16da9c9b2e5bfe01a209decbedeed5a2c4a3ba33c783c1e6e")),
]


def run(tmp, text, base, rebuild=False):
    c = os.path.join(tmp, "cand.md"); open(c, "w", encoding="utf-8", newline="\n").write(text)
    out = os.path.join(tmp, "r.json")
    if os.path.exists(out): os.remove(out)
    cmd = [sys.executable, "-B", os.path.join(HERE, "check_dyad_v6_4_22.py"), "--base", base, "--cand", c, "--out", out]
    if not rebuild: cmd.append("--norebuild")
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=tmp)
    f = sorted((k for k, v in json.load(open(out))["gates"].items() if v is False), key=lambda x: int(x[1:])) if os.path.exists(out) else []
    return r.returncode, f


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--base", required=True); ap.add_argument("--cand", required=True)
    ap.add_argument("--out", default="check_dyad_v6_4_22_controls.json"); a = ap.parse_args()
    base = os.path.abspath(a.base); s = open(a.cand, encoding="utf-8").read(); rows = []; tmp = tempfile.mkdtemp()
    try:
        rc, f = run(tmp, s, base); rows.append({"id": "P0", "description": "unmutated candidate", "exit": rc, "failing_gates": f, "as_expected": rc == 0 and not f})
        rc, f = run(tmp, s.replace("hyperbolic saddle.", "hyperbolic  saddle.", 1), base, rebuild=True)
        rows.append({"id": "N0", "description": "one-byte edit (full rebuild)", "expected_gate": "C0", "exit": rc, "failing_gates": f, "as_expected": rc == 1 and "C0" in f})
        for cid, gate, desc, fn in CONTROLS:
            m = fn(s); assert m != s, cid
            rc, f = run(tmp, m, base)
            rows.append({"id": cid, "description": desc, "expected_gate": gate, "exit": rc, "failing_gates": f, "as_expected": rc == 1 and gate in f})
    finally:
        shutil.rmtree(tmp)
    ok = all(r["as_expected"] for r in rows)
    for r in rows: print(r["id"], r["exit"], ",".join(r["failing_gates"]), "OK" if r["as_expected"] else "UNEXPECTED")
    print("ALL CONTROLS AS EXPECTED" if ok else "CONTROL FAILURE")
    with open(a.out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump({"script": "check_dyad_v6_4_22_controls.py", "controls": rows, "all_as_expected": ok}, fh, indent=1, sort_keys=True, ensure_ascii=False); fh.write("\n")
    return 0 if ok else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as ex:
        import traceback; traceback.print_exc(); print("CRASH", type(ex).__name__, ex); sys.exit(3)
