#!/usr/bin/env python3
"""Number Genesis v1.21 stage 2: owner guards and negative fixtures around tools/check_compaction.py.

usage: check_numgen_v1_21_stage2.py STAGE1 CANDIDATE MAP [--fixtures]
  run from the repository root (tools/check_compaction.py and the archive path in the map are read from it).

Owner guards (co-owner GO of 26 Oct 2026: base = ab25c162...99d2 only; layout only; no claim, RID, grade or OPEN change):
 G0 BASE        STAGE1 is the accepted stage-1 intermediate, round 2 (ab25c162...99d2), and the map names it
 G1 LIVE BODY   the live body (from "## §0." to the first appendix heading) is byte-identical to stage 1
 G2 APPENDIX B  Appendix B (heading and body) is byte-identical to stage 1
 G3 APPENDIX C  the Working Thesis body is byte-identical to stage 1 (only its heading letter A -> C changes)
 G4 HEADER      one field per line; Supersedes names v1.20.8 with its full hash; DSN Methodology v1.4; the status
                summary is three sentences of the base summary; no pointer-validation or methodology-note field
 G5 HISTORY     the base "## Changelog" and the three legacy notes are gone from the candidate and are in the archive;
                Appendix A names the predecessor tag numgen-v1.20.8 for them
 G6 COMPACTION  tools/check_compaction.py returns PASS (exit 0) on STAGE1, CANDIDATE, MAP

Negative fixtures (--fixtures): each mutates the candidate and/or the map in a temporary directory (recomputing the
declared candidate hash where the fixture is about content) and must make tools/check_compaction.py exit 1. F4, F10 and F11 change bytes inside the tail
that S2-T declares as replaced; the tool accepts them as declared (a known limit of a whole-tail replace-section), so
they must make owner guard G2 or G3 fail instead.
"""
import copy, hashlib, json, os, re, subprocess, sys, tempfile

TOOL = "tools/check_compaction.py"
STAGE1_SHA = "ab25c162a727b0826adfb0b8fd5f3898969ed78260fc00e8bbcaa9e1e3b899d2"
PRED = "835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e"
NOTES = ("## v0.3 Change Note", "## v1.0 Result Note", "## v0.9 Result Note")

def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()
def body(s):
    i = s.index("\n## §0. "); j = s.index("\n## Appendix ", i); return s[i:j]
def section(s, head):
    i = s.index(head); j = s.find("\n## ", i + 1); return s[i:j if j > 0 else len(s)]

def guards(s1, cand, mp, mpath, verbose=True):
    R = {}
    def g(k, ok, msg=""):
        R[k] = bool(ok)
        if verbose: print(f"[{'PASS' if ok else 'FAIL'}] {k} {msg}")
    g("G0 BASE", sha(s1) == STAGE1_SHA and mp.get("base_sha256") == STAGE1_SHA)
    g("G1 LIVE BODY", body(s1) == body(cand))
    ab = "## Appendix B. Rejected / Guarded Formulations\n"
    g("G2 APPENDIX B", section(s1, ab) == section(cand, ab))
    wt_old = section(s1, "## Appendix A. Working Thesis\n").split("\n", 1)[1]
    wt_new = section(cand, "## Appendix C. Working Thesis\n").split("\n", 1)[1]
    wt_new = wt_new[:wt_new.rindex("\n*END OF DOCUMENT")] if "\n*END OF DOCUMENT" in wt_new else wt_new
    g("G3 APPENDIX C", wt_old == wt_new)
    head = cand[:cand.index("\n## ")]
    fields = re.findall(r"^\*\*([^*:]+):\*\*", head, re.M)
    sup = re.search(r"^\*\*Supersedes:\*\*(.*)$", head, re.M).group(1)
    summ = re.search(r"^\*\*Status summary:\*\*\s*(.*?)\s*$", head, re.M).group(1)
    base_sum = re.search(r"^\*\*Status summary \(scientific state fixed at v1\.20;[^)]*\):\*\*\s*(.*)$", s1, re.M).group(1)
    sents = [x.strip() for x in re.split(r"(?<=[.;])\s+(?=[A-Z`$(])", summ) if x.strip()]
    g("G4 HEADER", len(fields) == len(set(fields)) and PRED in sup and "v1.20.8" in sup
      and "v1.4" in (re.search(r"^\*\*DSN Methodology:\*\*(.*)$", head, re.M).group(1))
      and len(sents) == 3 and all(x in base_sum for x in sents)
      and "Pointer-validation" not in head and "Methodology note" not in head, f"fields={fields}")
    arch = open(mp["archives"][0]["path"], encoding="utf-8").read()
    gone = "\n## Changelog\n" not in cand and not any(n in cand for n in NOTES)
    in_arch = section(s1, "## Changelog\n") in arch and all(n in arch for n in NOTES)
    appa = section(cand, "## Appendix A — Version History")
    g("G5 HISTORY", gone and in_arch and "`numgen-v1.20.8`" in appa)
    r = subprocess.run([sys.executable, TOOL, s1_path, cand_path, mpath], capture_output=True, text=True)
    g("G6 COMPACTION", r.returncode == 0, "tools/check_compaction.py exit %d" % r.returncode)
    return R

def run_tool(s1, cand, mp, tmp, name):
    d = os.path.join(tmp, name); os.makedirs(d, exist_ok=True)
    cp, mpp = os.path.join(d, "cand.md"), os.path.join(d, "map.json")
    open(cp, "wb").write(cand.encode("utf-8"))
    json.dump(mp, open(mpp, "w", encoding="utf-8"), ensure_ascii=False)
    r = subprocess.run([sys.executable, TOOL, s1_path, cp, mpp], capture_output=True, text=True)
    return r.returncode, [l for l in r.stdout.splitlines() if l.startswith("FAIL")]

def fixtures(s1, cand, mp):
    out = []
    def T(op_id): return next(o for o in mp_c["operations"] if o["id"] == op_id)
    with tempfile.TemporaryDirectory() as tmp:
        def fx(fid, what, mutate):
            global mp_c
            mp_c = copy.deepcopy(mp)
            c2 = mutate(cand)
            if c2 is None:
                out.append((fid, what, "NOT APPLICABLE")); return
            mp_c["candidate_sha256"] = sha(c2)
            rc, fails = run_tool(s1, c2, mp_c, tmp, fid)
            out.append((fid, what, "caught: " + "; ".join(f.split("  — ")[0] for f in fails) if rc == 1 else f"NOT CAUGHT (exit {rc})"))
        def tail_edit(a, b):
            def m(c):
                if c.count(a) != 1: return None
                t = T("S2-T"); assert t["new"].count(a) == 1; t["new"] = t["new"].replace(a, b)
                return c.replace(a, b)
            return m
        fx("F1", "live §6.6 sentence changed (undeclared)", lambda c: c.replace("This is an exact-primitive finite-iterate theorem", "This is an exact primitive finite-iterate theorem", 1))
        def f2(c):
            mp_c["profile"]["base_history_from"] = "## §9. Import Ledger and Artifact Registry"; return c
        fx("F2", "base_history_from pointed at a live section (§9)", f2)
        def f3(c):
            mp_c["profile"]["base_history_from"] = "## Changelog (absent)"; return c
        fx("F3", "base_history_from heading absent from the base", f3)
        fx("F5", "Appendix A names an identifier absent from the live text", tail_edit(
            "NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE at their statements", "NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE-X at their statements"))
        fx("F6", "two footer lines", tail_edit("*END OF DOCUMENT —", "*END OF DOCUMENT — extra*\n*END OF DOCUMENT —"))
        def f7(c):
            h = T("S2-H"); a = "C7B global breadth, C7C-A, N-4, N-6, NG-7B and full NG-8 remain OPEN."
            b = a + " C7C-M is closed."
            if h["new"].count(a) != 1: return None
            h["new"] = h["new"].replace(a, b); return c.replace(a, b, 1)
        fx("F7", "status summary gains a sentence not in the base summary", f7)
        def f8(c):
            for a in mp_c["archives"]:
                p = os.path.join(tempfile.gettempdir(), "numgen_fake_archive.md"); open(p, "w").write("unrelated\n")
                a["path"] = p; a["sha256"] = sha(open(p, "rb").read())
            return c
        fx("F8", "archive replaced by unrelated bytes", f8)
        def f9(c):
            h = T("S2-H"); a = "(SHA-256 `" + PRED + "`; tag `numgen-v1.20.8`)"
            b = "(SHA-256 `" + PRED + "`; tag `numgen-v1.20.8`); also `RTG_NUMBER_GENESIS_DSN_v1.20.7` (`c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28`)"
            if h["new"].count(a) != 1: return None
            h["new"] = h["new"].replace(a, b); return c.replace(a, b, 1)
        fx("F9", "Supersedes lists two predecessors", f9)
    # Guard-level fixtures: changes inside the declared tail (Appendix B / C bodies) are "declared" to the tool,
    # because S2-T replaces the whole tail; byte identity of those bodies is the owner guards' job (G2, G3).
    def gfx(fid, what, key, c2):
        g = guards(s1, c2, mp, map_path, verbose=False)
        out.append((fid, what, f"caught: {key}" if not g[key] else "NOT CAUGHT"))
    ab = "## Appendix B. Rejected / Guarded Formulations\n"
    sec = section(cand, ab); lines = sec.split("\n")
    recs = [i for i, l in enumerate(lines) if l.startswith("`[REJECTED")]
    l4 = list(lines); del l4[recs[0]]
    gfx("F4", "an Appendix B record deleted inside the declared tail", "G2 APPENDIX B", cand.replace(sec, "\n".join(l4), 1))
    l10 = list(lines); l10[recs[0]], l10[recs[1]] = l10[recs[1]], l10[recs[0]]
    gfx("F10", "Appendix B records reordered", "G2 APPENDIX B", cand.replace(sec, "\n".join(l10), 1))
    gfx("F11", "Working Thesis sentence changed inside the declared tail", "G3 APPENDIX C",
        cand.replace("Full functorial cross-track compatibility remains OPEN.\n\n---\n\n*END", "Full functorial cross-track compatibility is CLOSED.\n\n---\n\n*END", 1))
    ok = all(r[2].startswith("caught") for r in out)
    for r in out: print(f"{r[0]}: {r[1]} -> {r[2]}")
    print("RESULT:", "PASS (all fixtures caught)" if ok else "FAIL")
    return 0 if ok else 1

if __name__ == "__main__":
    s1_path, cand_path, map_path = sys.argv[1:4]
    s1 = open(s1_path, "rb").read().decode("utf-8"); cand = open(cand_path, "rb").read().decode("utf-8")
    mp = json.load(open(map_path, encoding="utf-8"))
    if "--fixtures" in sys.argv:
        sys.exit(fixtures(s1, cand, mp))
    R = guards(s1, cand, mp, map_path)
    ok = all(R.values()); print("RESULT:", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
