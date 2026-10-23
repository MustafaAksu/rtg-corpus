#!/usr/bin/env python3
"""check_dyad_v6_4_22.py -- change-focused gates for the DYAD v6.4.22 errata candidate against adopted v6.4.21.

C0  identities: base = v6.4.21 (a412f34d...); candidate = fresh build of the base
C1  determinism: two builds in clean directories are byte-identical (file and edit log)
C2  confinement: Appendix A of the base is kept byte-for-byte (one entry inserted before the v6.4.21 entry); outside
    Appendix A the line count is unchanged except the one inserted Appendix C row, and every changed line carries the
    new text of a logged edit
C3  science invariants: RID-tag set and RID-tag sequence equal; Dyadic RID strings equal; grade-tag sequence equal; no
    math span removed, and every added math span belongs to a logged edit
C4  R11 owners: every live "R11" is written "RECOG R11", "RECOG OPEN R11" or "OPEN-M R11" (Appendix C symbol cell
    and quoted labels excepted; header metadata excluded); each OPEN-M occurrence sits in an OPEN-M context (cascade gate / h / theta_f / factor / source formula)
    and each RECOG occurrence in a RECOG context (final-chart / chart ledger / CLOSED / reconciliation); expected counts
C5  stale wordings absent from live text (F1-F3, F5, W1-W3)
C6  edition lines: title, DRAFT status, Supersedes v6.4.21 with hash, release record path, Appendix A heading, one footer
C7  OPEN state: section 2 "Status:" lines identical to the base; OPEN 20 sentence present
C8  cited h4 second-route script: present, SHA-256 as cited, and it exits 0 (its --control K exits 1)
Exit 0 all pass / 1 any fail / 3 crash.
usage: check_dyad_v6_4_22.py --base V6421 --cand CANDIDATE [--norebuild] [--out JSON]
"""
import argparse, collections, hashlib, json, os, re, shutil, subprocess, sys, tempfile
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BASE_SHA = "a412f34d4db6a6fa92705a5c33334127b3efc3a30a903fecb3c91bd0cf1cdc7d"
H4R = "dd06a1a20466dbe16da9c9b2e5bfe01a209decbedeed5a2c4a3ba33c783c1e6d"
GRADE = re.compile(r"`\[(?:THM-ALG via IA|ALG|THM|DEF|CAND|ENG|NUM|HYP|OBS|OPEN|COR|FAIL|RETRACTED)\]`")
EXPECT_R11 = {"OPEN-M": 13, "RECOG": 9}
OPENM_CTX = ("cascade", "$h$", "\\theta_f", "factor", "source formula", "gate")
RECOG_CTX = ("final-chart", "chart ledger", "CLOSED", "reconciliation")


def sha(b): return hashlib.sha256(b).hexdigest()
def split_a(s):
    i = s.index("## Appendix A — Version History"); j = s.index("## Appendix B —")
    return s[:i], s[i:j], s[j:]
def maths(s):
    c = collections.Counter()
    for l in s.split("\n"):
        l = l.replace("$$", "$")
        c.update(l.split("$")[1::2] if l.count("$") % 2 == 0 else [l])
    return c
def build(tmp, base):
    shutil.copy(os.path.join(HERE, "build_dyad_v6_4_22.py"), tmp)
    out, log = os.path.join(tmp, "c.md"), os.path.join(tmp, "log.json")
    r = subprocess.run([sys.executable, "-I", "-B", "build_dyad_v6_4_22.py", os.path.abspath(base), out, log], cwd=tmp, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return open(out, "rb").read(), open(log, "rb").read()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--base", required=True); ap.add_argument("--cand", required=True)
    ap.add_argument("--norebuild", action="store_true"); ap.add_argument("--out", default="check_dyad_v6_4_22.json")
    a = ap.parse_args()
    BB, CB = open(a.base, "rb").read(), open(a.cand, "rb").read(); B, C = BB.decode(), CB.decode()
    G, info = {}, {}
    G["C0"] = sha(BB) == BASE_SHA
    t1, t2 = tempfile.mkdtemp(), tempfile.mkdtemp()
    try:
        b1, l1 = build(t1, a.base)
        log = json.loads(l1)
        if a.norebuild: G["C1"] = None
        else:
            b2, l2 = build(t2, a.base); G["C1"] = b1 == b2 and l1 == l2
        G["C0"] = G["C0"] and (b1 == CB or a.norebuild)
    finally:
        shutil.rmtree(t1); shutil.rmtree(t2)
    edits = log["edits"]; news = [e["new"] for e in edits]
    bL, bA, bR = split_a(B); cL, cA, cR = split_a(C)
    entry = next(e["new"] for e in edits if e["key"] == "ED-8")
    a_ok = cA.replace(entry, "", 1) == bA and cA.count(entry) == 1
    bl, cl = (bL + bR).split("\n"), (cL + cR).split("\n")
    why = []
    import difflib
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, bl, cl, autojunk=False).get_opcodes():
        if tag == "equal": continue
        for l in cl[j1:j2]:
            if not any(n.strip("\n") and (l in n or any(part and part in l for part in n.split("\n") if len(part) > 20)) for n in news):
                why.append(l[:100])
    G["C2"] = a_ok and not why and len(cl) - len(bl) == 1
    info["C2"] = {"appendix_a_kept": a_ok, "unexplained": why[:5], "line_delta": len(cl) - len(bl)}
    rid = lambda s: re.findall(r"\[RID:\s*[^\]]+\]", s)
    dy = lambda s: set(re.findall(r"(?<![A-Za-z0-9-])DYAD-(?:ALG|THM|DEF|OPEN|ART|CAND|NUM|CF)-[A-Z0-9]+(?:-[A-Z0-9]+)*", s))
    added = maths(C) - maths(B); removed = maths(B) - maths(C)
    declared = collections.Counter()
    for e in edits: declared.update(maths(e["new"]))
    math_ok = not removed and all(declared[k] >= v for k, v in added.items())
    gb, gc = collections.Counter(GRADE.findall(bL + bR)), collections.Counter(GRADE.findall(cL + cR))
    gdecl = collections.Counter()
    for e in edits: gdecl.update(GRADE.findall(e["new"]))
    grade_ok = not (gb - gc) and all(gdecl[k] >= v for k, v in (gc - gb).items())
    G["C3"] = rid(B) == rid(C) and dy(B) == dy(C) and grade_ok and math_ok
    info["C3"] = {"math_removed": list(removed)[:5], "math_added_undeclared": [k for k, v in added.items() if declared[k] < v][:5]}
    live = cL + cR; cnt = collections.Counter(); bad = []
    body = live[live.index("## Local Tag Aliases"):]  # header metadata excluded
    for l in body.split("\n"):
        for m in re.finditer(r"R11", l):
            pre = l[:m.start()]
            if pre == "| " or pre.endswith('"RECOG ') or pre.endswith('"OPEN-M '): continue  # symbol cell; quoted labels in the guard cell
            win = l[max(0, m.start() - 220):m.end() + 220]
            if pre.endswith("OPEN-M "):
                cnt["OPEN-M"] += 1
                if not any(k in win for k in OPENM_CTX): bad.append(("OPEN-M ctx", l[m.start() - 60:m.end() + 40]))
            elif pre.endswith("RECOG ") or pre.endswith("RECOG OPEN "):
                cnt["RECOG"] += 1
                if not any(k in win for k in RECOG_CTX): bad.append(("RECOG ctx", l[m.start() - 60:m.end() + 40]))
            else: bad.append(("unqualified", l[max(0, m.start() - 60):m.end() + 40]))
    G["C4"] = not bad and dict(cnt) == EXPECT_R11; info["C4"] = {"counts": dict(cnt), "bad": bad[:5]}
    stale = ["this edition's SHA-256", "reviewer full replay pending", "earlier statements omitting it are superseded",
             "the earlier form without it is superseded", "former heading tag", "superseded by v6.4.20 (this edition", "planned notice N17"]
    G["C5"] = not any(x in live for x in stale); info["C5"] = [x for x in stale if x in live]
    head = C[:C.index("## Local Tag Aliases")] if "## Local Tag Aliases" in C else C[:3000]
    G["C6"] = (C.startswith("# RTG_DYADIC_OSCILLATOR_DSN_v6.4.22\n") and "**Document status:** DRAFT — v6.4.22 candidate" in head
               and "**Supersedes:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.21` (SHA-256 `" + BASE_SHA + "`; tag `dyad-v6.4.21`)." in head
               and "`records/dyad/RTG_DYADIC_v6_4_22_RELEASE_RECORD.md`" in head and "### v6.4.22 — 23 October 2026 — DRAFT candidate" in cA
               and len(re.findall(r"^\*END OF DOCUMENT", C, re.M)) == 1 and "*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 (DRAFT candidate, 23 October 2026).*" in C
               and C.count("<!-- AI_CONTEXT_CORE_END -->") == 1)
    s2 = lambda s: [l for l in s[s.index("## §2."):s.index("## §3.")].split("\n") if "Status:" in l]
    G["C7"] = s2(B) == s2(C) and "OPEN 20 is PARTIAL: B-∞ existence and flat uniqueness are CLOSED; B-an and B-6 are OPEN." in C
    p = os.path.join(HERE, "dyad_h4_real_route_check.py")
    ok8 = os.path.exists(p) and sha(open(p, "rb").read()) == H4R and H4R in C
    if ok8:
        r0 = subprocess.run([sys.executable, "-I", "-B", p], capture_output=True, text=True)
        rk = subprocess.run([sys.executable, "-I", "-B", p, "--control", "K"], capture_output=True, text=True)
        ok8 = r0.returncode == 0 and rk.returncode == 1
    G["C8"] = ok8
    ok = all(v is not False for v in G.values())
    for k in sorted(G, key=lambda x: int(x[1:])): print(k, {True: "PASS", False: "FAIL", None: "SKIP"}[G[k]])
    print("ALL PASS" if ok else "FAIL")
    with open(a.out, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"gates": G, "info": info, "all_pass": ok, "candidate_sha256": sha(CB), "base_sha256": sha(BB)}, f, indent=1, sort_keys=True, ensure_ascii=False); f.write("\n")
    return 0 if ok else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as ex:
        import traceback; traceback.print_exc(); print("CRASH", type(ex).__name__, ex); sys.exit(3)
