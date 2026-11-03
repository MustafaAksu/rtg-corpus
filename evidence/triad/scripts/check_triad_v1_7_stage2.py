#!/usr/bin/env python3
r"""Triadic v1.7 stage 2: owner guards and negative fixtures around tools/check_compaction.py.

usage: check_triad_v1_7_stage2.py STAGE1 CANDIDATE MAP [--fixtures]
  run from the repository root (tools/check_compaction.py, the builder and the archive paths in the map are read from it).

Owner guards (stage 2 is layout only; base = b47d294d...a66a, stage-1 round 3; no claim, RID, grade or OPEN change):
 G0 BASE        STAGE1 is the frozen stage-1 intermediate and the map and its archive name it
 G1 REBUILD     build_triad_v1_7_stage2.py reproduces CANDIDATE and MAP byte-for-byte
 G2 RIDS        the set of TRIAD-* strings in the whole file is unchanged
 G3 ANCHORS     every heading anchor ({#...}) of STAGE1 is kept, in order
 G4 STATUS      every `Status:` line of the OPEN/PARTIAL/CLOSED records is unchanged, in order
 G5 CLAIM TEXT  in the live text (§1 to the end, without Appendix A) the multisets of claim tags and qualifiers (both
                backticked and plain-bracket) are unchanged; math spans are unchanged except those inside the relocated
                v1.6 per-module table (S2-M)
 G6 VERBATIM    every cell of the two Appendix B tables restated by S2-B1/S2-B2 occurs verbatim in the candidate's
                Appendix B, and each restated row keeps its RID or "[RID: none]"
 G7 HEADER      no history text in the header; one predecessor with its full hash; the status summary is a subset of
                the base header summary and §1 sentences (also checked by the tool)
 G8 HISTORY     the new Appendix A names `triad-v1.6.1` for the verbatim history, every TRIAD RID it names occurs outside
                Appendix A, and the file has exactly one footer line
 G9 COMPACTION  tools/check_compaction.py returns PASS (exit 0)

--fixtures: each fixture mutates the candidate and/or the map in a temporary directory (the candidate is re-derived from
the mutated map, so the tool's re-derivation passes unless the fixture is about undeclared change). Each must make the
tool exit 1 or make an owner guard fail. A passing run authorizes nothing.
"""
import copy, hashlib, importlib.util, json, os, re, subprocess, sys, tempfile

STAGE1_SHA = "b47d294d9dc82b78f05e02c99e04100177c78480c453438d5d4fca86e14ba66a"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
TOOL = os.path.join(ROOT, "tools", "check_compaction.py")
RE_STATUS = re.compile(r"`\[(?:THM|ALG|DEF|NUM|CAND|HYP|HEUR|SPEC|INTERP|OPEN|FAIL|RETRACTED|COR|ENG|OBS|RESULT|SESSION)\]`")
RE_QUAL = re.compile(r"`?\[(?:scope|assuming|conv|family|import|proof|target|from|provenance|cert):[^\]]*\]`?")
RE_MATH = re.compile(r"\$\$.+?\$\$|\$[^$\n]+\$", re.S)


def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()
def header(t): return t[:t.index("\n## ")]
def live(t):
    a, b = t.find("\n## Appendix A"), t.find("\n## Appendix B")
    return t[t.index("\n## "):a] + t[b:]
def appA(t): return t[t.find("\n## Appendix A"):t.find("\n## Appendix B")]
def appB(t): return t[t.find("\n## Appendix B"):]
def triad(t): return set(re.findall(r"TRIAD-[A-Z0-9]+(?:-[A-Z0-9]+)*", t))
def anchors(t): return re.findall(r"\{#([^}]+)\}", t)
def statuses(t): return re.findall(r"^Status: .*$", t, re.M)
def ms(x): return sorted(x)


def builder():
    spec = importlib.util.spec_from_file_location("b2", os.path.join(HERE, "build_triad_v1_7_stage2.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def tool(base_p, cand_p, map_p):
    r = subprocess.run([sys.executable, "-I", "-B", TOOL, base_p, cand_p, map_p], capture_output=True, text=True, cwd=ROOT)
    return r.returncode, [l for l in r.stdout.splitlines() if l.startswith("FAIL")]


def guards(base, cand, mp, map_bytes=None, rebuild=True):
    G = {}
    G["G0"] = sha(base) == STAGE1_SHA == mp.get("base_sha256") and any(a.get("sha256") == STAGE1_SHA for a in mp["archives"])
    if rebuild:
        with tempfile.TemporaryDirectory() as d:
            bp, cp, mpp = (os.path.join(d, x) for x in ("b.md", "c.md", "m.json"))
            open(bp, "w", encoding="utf-8", newline="\n").write(base)
            subprocess.run([sys.executable, "-I", "-B", os.path.join(HERE, "build_triad_v1_7_stage2.py"), bp, cp, mpp],
                           capture_output=True, check=True, cwd=ROOT)
            G["G1"] = open(cp, encoding="utf-8").read() == cand and (map_bytes is None or open(mpp, "rb").read() == map_bytes)
    G["G2"] = triad(cand) == triad(base)
    G["G3"] = anchors(cand) == anchors(base)
    G["G4"] = statuses(cand) == statuses(base)
    lb, lc = live(base), live(cand)
    removed_math = []
    for op in mp["operations"]:
        if op["id"] == "S2-M":
            i = base.index(op["start"]); j = base.index(op["end"], i)
            removed_math = RE_MATH.findall(base[i:j])
    mb = list(RE_MATH.findall(lb))
    for x in removed_math:
        if x in mb: mb.remove(x)
    G["G5"] = ms(RE_STATUS.findall(lb)) == ms(RE_STATUS.findall(lc)) and ms(RE_QUAL.findall(lb)) == ms(RE_QUAL.findall(lc)) \
        and ms(mb) == ms(RE_MATH.findall(lc))
    B = appB(cand); ok6 = True
    for oid, cells in mp.get("verbatim_cells", {}).items():
        ok6 &= all(c in B for c in cells)
    ok6 &= B.count("`[SUPERSEDED]` [RID:") == 8 and B.count("`[SUPERSEDED]` [RID: none]") == 2
    G["G6"] = ok6
    h = header(cand)
    sup = re.search(r"^\*\*Supersedes:\*\*(.*)$", h, re.M)
    G["G7"] = "History —" not in h and sup is not None and len(re.findall(r"[0-9a-f]{64}", sup.group(1))) == 1
    A = appA(cand)
    outside = cand.replace(A, "")
    G["G8"] = "`triad-v1.6.1`" in A and all(r in outside for r in triad(A)) and \
        sum(1 for l in cand.split("\n") if l.startswith("*END OF DOCUMENT")) == 1
    return G


def main(argv):
    if len(argv) < 4: raise SystemExit(__doc__)
    base = open(argv[1], encoding="utf-8").read(); cand = open(argv[2], encoding="utf-8").read()
    map_bytes = open(argv[3], "rb").read(); mp = json.loads(map_bytes)
    G = guards(base, cand, mp, map_bytes)
    code, fails = tool(argv[1], argv[2], argv[3])
    G["G9"] = code == 0
    for k, v in G.items(): print(f"{k}: {'PASS' if v else 'FAIL'}")
    ok = all(G.values())
    print(f"candidate sha256: {sha(cand)}; GUARDS: {'ALL PASS' if ok else 'FAIL'}")
    if "--fixtures" in argv:
        ok &= fixtures(argv[1], base, cand, mp)
    sys.exit(0 if ok else 1)


def fixtures(base_p, base, cand, mp):
    b = builder()
    def derive(m):
        s = base
        for op in m["operations"]: s = b.apply(s, op)
        return s
    F = []
    def fx(name, mut):
        F.append((name, mut))
    def op(m, oid): return next(o for o in m["operations"] if o["id"] == oid)

    fx("F1 undeclared live edit in §6.18", lambda m, c: (m, c.replace("Tangency holds in both.", "Tangency holds in (b).")))
    def f2(m, c):
        o = op(m, "S2-B1"); o["new"] = o["new"].replace("conjugate-pair algebra survives", "conjugate-pair algebra fails"); return m, None
    fx("F2 restated Appendix B cell altered", f2)
    def f3(m, c):
        h = op(m, "S2-H"); h["new"] = h["new"].replace("is met.  \n**Programme tier", "is met. The physical carrier is selected.  \n**Programme tier"); return m, None
    fx("F3 status summary gains a sentence", f3)
    def f4(m, c):
        f = op(m, "S2-F"); f["new"] = f["new"] + "*END OF DOCUMENT — second*\n"; return m, None
    fx("F4 two footer lines", f4)
    def f5(m, c):
        o = op(m, "S2-B2"); o["new"] = o["new"].replace("[RID: TRIAD-EXPORT-PROTOCOL-1]", "[RID: none]", 1); return m, None
    fx("F5 restated row drops its RID", f5)
    def f6(m, c):
        o = op(m, "S2-M"); o["new"] = o["new"].replace("Current module status", "`[ALG]` Current module status"); return m, None
    fx("F6 pointer text carries a claim tag", f6)
    def f7(m, c):
        h = op(m, "S2-H"); h["new"] = h["new"].replace("**Repository:**", "**History — v1.6.1:** adopted.  \n**Repository:**"); return m, None
    fx("F7 history text in the header", f7)
    def f8(m, c):
        m["archives"][0]["sha256"] = "0" * 64; return m, None
    fx("F8 archive identity wrong", f8)
    def f9(m, c):
        o = op(m, "S2-A"); o["new"] = o["new"].replace("Predecessor: `triad-v1.6.1`.", "Predecessor: `triad-v1.6.1`; TRIAD-ALG-NONEXISTENT added."); return m, None
    fx("F9 Appendix A names an identifier absent from the live text", f9)
    fx("F10 OPEN status line changed (undeclared)", lambda m, c: (m, c.replace("Status: ACTIVE after r4 correction", "Status: CLOSED after r4 correction")))
    def f11(m, c):
        e = op(m, "S2-E02"); old = e["old"]
        i = old.index(" pending."); j = old.index("  \n**Source custody:**")
        e["new"] = old[:i] + old[j:]; return m, None
    fx("F11 history-removal also deletes the qualifying word 'pending'", f11)

    ok = True
    with tempfile.TemporaryDirectory() as d:
        for name, mut in F:
            m = copy.deepcopy(mp); c0 = cand
            m2, c2 = mut(m, c0)
            if c2 is None: c2 = derive(m2)
            if c2 == cand and m2 == mp:
                print(f"{name}: mutation did not apply -> FAIL"); ok = False; continue
            m2["candidate_sha256"] = sha(c2)
            for o in m2["operations"]: o.pop("_removed", None)
            cp, mpp = os.path.join(d, "c.md"), os.path.join(d, "m.json")
            open(cp, "w", encoding="utf-8", newline="\n").write(c2)
            json.dump(m2, open(mpp, "w", encoding="utf-8"), ensure_ascii=False)
            code, fails = tool(base_p, cp, mpp)
            G = guards(base, c2, m2, rebuild=False)
            bad = [k for k, v in G.items() if not v]
            caught = code != 0 or bad
            why = "; ".join(fails[:3]) + (f" | owner guard {', '.join(bad)}" if bad else "")
            print(f"{name} -> {'caught: ' + why if caught else 'NOT CAUGHT'}")
            ok &= bool(caught)
    print(f"RESULT: {'PASS (all fixtures caught)' if ok else 'FAIL'}")
    return ok


if __name__ == "__main__":
    main(sys.argv)
