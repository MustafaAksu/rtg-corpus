#!/usr/bin/env python3
"""OFN v0.11 stage 2: owner guards and negative fixtures around tools/check_compaction.py.

usage: check_ofn_v0_11_stage2.py STAGE1 CANDIDATE MAP [--fixtures]
  run from the repository root (tools/check_compaction.py, the builder and the archive path in the map are read from it).

Owner guards (stage 2 is layout only; base = 9f31badf...a822, stage-1 round 2; no claim, RID, grade or OPEN change):
 G0 BASE        STAGE1 is the frozen stage-1 intermediate and the map and its archive name it
 G1 REBUILD     build_ofn_v0_11_stage2.py reproduces CANDIDATE and MAP byte-for-byte
 G2 OFN RIDS    the RTG-OFN RID set is unchanged (none lost, none added), each declaration is kept, and every RTG-OFN
                mention in §§0–11 is kept. tools/check_compaction.py does not track RTG-OFN-* (its RID pattern skips a
                prefix preceded by "RTG-"), so this guard carries that check
 G3 ANCHORS     every HTML anchor (<a id>) and heading anchor ({#}) of STAGE1 is kept
 G4 OPEN        the 21 OPEN status lines are unchanged in order (20 ACTIVE / 1 PARTIAL)
 G5 CLAIM TEXT  in §§0–11 the multisets of claim tags, qualifiers and math spans are unchanged
 G6 REGISTERS   every table row of §12.3 (custody, consumers) and §12.4 (requests) is kept byte-identical
 G7 APPENDICES  Appendix A and Appendix B are byte-identical
 G8 HEADER      only the Document status line differs; the status summary is unchanged
 G9 HISTORY     the base "## Appendix C — Version History" region is gone from CANDIDATE, is in the archive, and the new
                Appendix C names `ofn-v0.10` for the verbatim entries; one footer line; every identifier the new Appendix C
                names occurs outside it. (OFN's history is Appendix C, which the tool counts as live text, so the tool's
                own history-appendix identifier test finds each identifier in the new entry itself and cannot fail.)
 G10 COMPACTION tools/check_compaction.py returns PASS (exit 0)

--fixtures: each fixture mutates the candidate and/or the map in a temporary directory (recomputing the declared
candidate hash where the fixture is about content). It must make tools/check_compaction.py exit 1 or make an owner
guard fail; the output says which. A passing run authorizes nothing.
"""
import copy, hashlib, importlib.util, json, os, re, subprocess, sys, tempfile

TOOL = "tools/check_compaction.py"
BUILDER = "evidence/ofn/scripts/build_ofn_v0_11_stage2.py"
STAGE1_SHA = "9f31badfa0e7a70a037c3ede3e7f55f852d09f2288508ef38edf343a5172a822"
RE_STATUS = re.compile(r"`\[(?:THM|ALG|DEF|NUM|CAND|HYP|HEUR|SPEC|INTERP|OPEN|FAIL|RETRACTED|COR|ENG|OBS|RESULT|SESSION|MATH)[^`]*\]`")
RE_QUAL = re.compile(r"`\[(?:scope|assuming|conv|family|import|proof|target|from|provenance|cert):[^`]*\]`")
RE_MATH = re.compile(r"\$\$.+?\$\$|\$[^$\n]+\$", re.S)
RE_OFN = re.compile(r"RTG-OFN-[A-Z0-9]+(?:-[A-Z0-9]+)*")
# the tool's own RID pattern, used to check identifiers named in the new Appendix C against the text outside it
RE_RID_TOOL = re.compile(r"(?<![A-Z]-)\b(?:DYAD|RECOG|GEN|TRIAD|NUMGEN|OFN|UVM|RRF|DZT|AZ|TDRG|LEG|PRE|FMS|RER|ERB|PROG|OPENM)-[A-Z0-9][A-Z0-9-]*[A-Z0-9]\b")


def sha(b): return hashlib.sha256(b if isinstance(b, bytes) else b.encode("utf-8")).hexdigest()
def head(s): return s[:s.index("\n## ")]
def core(s): return s[s.index("\n## Local Tag Aliases"):s.index('<a id="ofn-artifacts-provenance">')]
def sect(s, a, b): i = s.index(a); return s[i:s.index(b, i + len(a))]
def appA(s): return sect(s, '<a id="ofn-historical-scenarios">', '<a id="ofn-retired-claims">')
def appB(s): return sect(s, '<a id="ofn-retired-claims">', '<a id="ofn-version-history">')
def rows(t): return [l for l in t.split("\n") if l.startswith("|")]
def decls(s): return sorted(re.findall(r"\[RID: (RTG-OFN-[A-Z0-9-]+)\]|\*\*RID:\*\* `(RTG-OFN-[A-Z0-9-]+)`", s))
def anchors(s): return set(re.findall(r'<a id="([^"]+)"', s)) | {a for l in s.split("\n") if l.startswith("#") for a in re.findall(r"\{#([A-Za-z0-9_-]+)\}", l)}
def statuses(s): return re.findall(r"^Status: (ACTIVE|PARTIAL)\b.*$", s, re.M)


def load_builder():
    spec = importlib.util.spec_from_file_location("b2", BUILDER)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def run_tool(s1p, cp, mp):
    r = subprocess.run([sys.executable, "-I", TOOL, s1p, cp, mp], capture_output=True, text=True)
    return r.returncode, [l.split("  —")[0] for l in r.stdout.splitlines() if l.startswith("FAIL")]


def guards(s1, cand, mp, s1p, cp, mpp, verbose=True, rebuild=True):
    R = {}
    def g(k, ok, msg=""):
        R[k] = bool(ok)
        if verbose: print(f"[{'PASS' if ok else 'FAIL'}] {k} {msg}".rstrip())
    arch = mp["archives"][0]
    g("G0 BASE", sha(s1) == STAGE1_SHA and mp.get("base_sha256") == STAGE1_SHA and arch["sha256"] == STAGE1_SHA
      and sha(open(arch["path"], "rb").read()) == STAGE1_SHA)
    if rebuild:
        with tempfile.TemporaryDirectory() as t:
            o, m = os.path.join(t, "c.md"), os.path.join(t, "m.json")
            subprocess.run([sys.executable, "-I", BUILDER, s1p, o, m], capture_output=True, check=True)
            g("G1 REBUILD", open(o, "rb").read() == cand.encode("utf-8") and open(m, "rb").read() == open(mpp, "rb").read())
    rb, rc = set(RE_OFN.findall(s1)), set(RE_OFN.findall(cand))
    g("G2 OFN RIDS", rb == rc and decls(s1) == decls(cand) and sorted(RE_OFN.findall(core(s1))) == sorted(RE_OFN.findall(core(cand))),
      f"{len(rb)} RTG-OFN RIDs; {len(decls(cand))} declarations")
    g("G3 ANCHORS", anchors(s1) <= anchors(cand), f"{len(anchors(s1))} anchors kept")
    g("G4 OPEN", statuses(s1) == statuses(cand) and len(statuses(cand)) == 21,
      f"{statuses(cand).count('ACTIVE')} ACTIVE / {statuses(cand).count('PARTIAL')} PARTIAL")
    cb, cc = core(s1), core(cand)
    g("G5 CLAIM TEXT", all(sorted(r.findall(cb)) == sorted(r.findall(cc)) for r in (RE_STATUS, RE_QUAL, RE_MATH)),
      f"{len(RE_STATUS.findall(cc))} claim tags, {len(RE_QUAL.findall(cc))} qualifiers, {len(RE_MATH.findall(cc))} math spans")
    r123 = lambda s: rows(sect(s, "### 12.3 ", "### 12.4 ")) + rows(sect(s, "### 12.4 ", "### 12.5 "))
    g("G6 REGISTERS", r123(s1) == r123(cand), f"{len(r123(cand))} register rows")
    g("G7 APPENDICES", appA(s1) == appA(cand) and appB(s1) == appB(cand))
    hb, hc = head(s1).split("\n"), head(cand).split("\n")
    diff = [i for i in range(max(len(hb), len(hc))) if i >= len(hb) or i >= len(hc) or hb[i] != hc[i]]
    g("G8 HEADER", len(hb) == len(hc) and len(diff) == 1 and hc[diff[0]].startswith("**Document status:**"))
    hC = "## Appendix C — Version History\n"
    region = s1[s1.index(hC):]
    newC = cand[cand.index('<a id="ofn-version-history">'):]
    rest = cand[:cand.index('<a id="ofn-version-history">')]
    ids = set(RE_RID_TOOL.findall(newC)) | set(RE_OFN.findall(newC))
    absent = sorted(x for x in ids if x not in rest)
    g("G9 HISTORY", hC not in cand and region in open(arch["path"], encoding="utf-8").read() and "`ofn-v0.10`" in newC
      and len(re.findall(r"^\*END OF DOCUMENT", cand, re.M)) == 1 and not absent,
      f"identifiers named only in Appendix C: {absent}" if absent else "")
    code, _ = run_tool(s1p, cp, mpp)
    g("G10 COMPACTION", code == 0, f"tools/check_compaction.py exit {code}")
    return R


def fixtures(s1, cand, mp, s1p):
    B = load_builder()
    out, allok = [], True

    def derive(ops):
        s = s1
        for op in ops:
            s = B.apply(s, op)
        return s

    def unique_around(s, needle, region_start=None, width=50, at=None):
        i = at if at is not None else s.index(needle, s.index(region_start) if region_start else 0)
        for w in range(width, 400, 10):
            frag = s[max(0, i - w):i + len(needle) + w]
            if s.count(frag) == 1:
                return frag
        raise SystemExit("no unique fragment")

    with tempfile.TemporaryDirectory() as tmp:
        def fx(fid, what, mutate):
            nonlocal allok
            c2, m2 = mutate(cand, copy.deepcopy(mp))
            d = os.path.join(tmp, fid); os.makedirs(d)
            cp, mpp = os.path.join(d, "cand.md"), os.path.join(d, "map.json")
            open(cp, "w", encoding="utf-8", newline="\n").write(c2)
            json.dump(m2, open(mpp, "w", encoding="utf-8"), ensure_ascii=False)
            code, fails = run_tool(s1p, cp, mpp)
            gr = guards(s1, c2, m2, s1p, cp, mpp, verbose=False, rebuild=False)
            gfail = [k for k, v in gr.items() if not v and k != "G10 COMPACTION"]
            caught = code == 1 or bool(gfail)
            allok &= caught
            by = "; ".join(fails) if code == 1 else ""
            if gfail: by = (by + " | " if by else "") + "owner guard " + ", ".join(gfail)
            out.append(f"{fid}: {what} -> {'caught' if caught else 'NOT CAUGHT'}: {by or '(tool exit %d)' % code}")

        def with_ops(m, ops):
            m["operations"] = ops
            c = derive(ops)
            m["candidate_sha256"] = sha(c)
            return c, m

        def f1(c, m):
            k = c.index("### 5.5")
            c = c[:k] + c[k:].replace("primary realized smooth mathematical candidate family", "principal realized smooth mathematical candidate family", 1)
            m["candidate_sha256"] = sha(c); return c, m
        fx("F1", "live §5.5 wording changed (undeclared)", f1)

        def f2(c, m):
            frag = unique_around(s1, "`DYAD-THM-SMOOTH-EMBEDDING`", "### 5.5")
            op = {"id": "FX-2", "op": "edit", "class": "history-removal", "archive": ["stage1-intermediate"],
                  "old": frag, "new": frag.replace("`DYAD-THM-SMOOTH-EMBEDDING`", "", 1)}
            return with_ops(m, [op] + m["operations"])
        fx("F2", "history-removal deletes a DYAD RID", f2)

        def f3(c, m):
            k = s1.index("conditional", s1.index("### 5.5"))
            frag = None
            for w in range(30, 200, 10):
                t = s1[k - w:k + 11 + w]
                if s1.count(t) == 1 and "`" not in t and "$" not in t: frag = t; break
            old = s1[k - 60:k + 71] if frag is None else frag
            sub = " conditional"
            op = {"id": "FX-3", "op": "edit", "class": "history-removal", "archive": ["stage1-intermediate"],
                  "old": old, "new": old.replace(sub, "", 1)}
            return with_ops(m, [op] + m["operations"])
        fx("F3", "history-removal deletes the qualifying word 'conditional'", f3)

        def f4(c, m):
            ops = m["operations"]; t = next(o for o in ops if o["id"] == "S2-T")
            t["new"] = t["new"].replace(" (SHA-256 `56bc991d28c4a6f3e841eec5ac8c4550528fbaac91bcfc23ab0dc2540bd2a514`, matching its release record)", "", 1)
            return with_ops(m, ops)
        fx("F4", "the relocated v0.8 baseline hash dropped from Appendix C", f4)

        def f5(c, m):
            ops = m["operations"]; t = next(o for o in ops if o["id"] == "S2-T")
            t["new"] = t["new"].replace("No scientific OPEN closed.", "No scientific OPEN closed (DYAD-THM-NONEXISTENT-GERM).", 1)
            return with_ops(m, ops)
        fx("F5", "Appendix C names an identifier absent from the live text", f5)

        def f6(c, m):
            ops = m["operations"]; h = next(o for o in ops if o["id"] == "S2-H")
            h["new"] = h["new"].replace("as a distinguished subclass.  ", "as a distinguished subclass. Class C is physically selected.  ", 1)
            return with_ops(m, ops)
        fx("F6", "status summary gains a sentence not in the base summary", f6)

        def f7(c, m):
            ops = m["operations"]; t = next(o for o in ops if o["id"] == "S2-T")
            t["new"] = t["new"] + "*END OF DOCUMENT — duplicate*\n"
            return with_ops(m, ops)
        fx("F7", "two footer lines", f7)

        def f8(c, m):
            p = os.path.join(tmp, "fake_archive.md"); open(p, "w").write("unrelated bytes\n")
            m["archives"][0]["path"] = p; return c, m
        fx("F8", "archive replaced by unrelated bytes", f8)

        def f9(c, m):
            m["profile"]["base_history_from"] = "## 9. Foundational OPEN Problems"; return c, m
        fx("F9", "base_history_from pointed at a live section (§9)", f9)

        def f10(c, m):
            ops = m["operations"]; o = next(o for o in ops if o["id"] == "S2-S2")
            o["new"] = o["new"].replace("Contributions follow", "`[THM]` Contributions follow", 1)
            return with_ops(m, ops)
        fx("F10", "pointer text in §12.2 carries a claim tag", f10)

        def f11(c, m):
            row = next(l for l in s1.split("\n") if l.startswith("| `RTG-OFN-OPEN-TRIAD-CLASS` | Registered v0.10"))
            i = s1.index(row); old = s1[i - 40:i + len(row) + 1 + 40]
            op = {"id": "FX-11", "op": "edit", "class": "history-removal", "archive": ["stage1-intermediate"],
                  "old": old, "new": old.replace(row + "\n", "", 1)}
            return with_ops(m, m["operations"] + [op])
        fx("F11", "§12.3 custody row for OPEN-TRIAD-CLASS removed as 'v0.10' history (RTG-OFN RID not tracked by the tool)", f11)

        def f12(c, m):
            a = s1.index("### 5.5"); b = s1.index('<a id="ofn-artifacts-provenance">')
            mm = re.search(r"`RTG-OFN-[A-Z0-9-]+`", s1[a:b]); rid = mm.group(0)
            frag = unique_around(s1, rid, at=a + mm.start())
            op = {"id": "FX-12", "op": "edit", "class": "history-removal", "archive": ["stage1-intermediate"],
                  "old": frag, "new": frag.replace(rid, "", 1)}
            m["profile"]["history_words"] = m["profile"]["history_words"] + [rid.strip("`")]
            return with_ops(m, [op] + m["operations"])
        fx("F12", "an RTG-OFN mention in §§5.5–11 removed under a widened history-word profile", f12)

        def f13(c, m):
            c = c.replace("Status: PARTIAL", "Status: ACTIVE", 1); m["candidate_sha256"] = sha(c); return c, m
        fx("F13", "OPEN status line changed (undeclared)", f13)

        def f14(c, m):
            k = c.index("### B.2 Adopted v0.8 corrections")
            c = c[:k] + c[k:].replace("`[COR]`", "`[THM]`", 1); m["candidate_sha256"] = sha(c); return c, m
        fx("F14", "Appendix B record changed (undeclared)", f14)

    for l in out: print(l)
    print("RESULT:", "PASS (all fixtures caught)" if allok else "FAIL")
    return allok


def main():
    a = sys.argv[1:]
    if len(a) not in (3, 4):
        raise SystemExit(__doc__)
    s1p, cp, mpp = a[:3]
    s1 = open(s1p, encoding="utf-8").read(); cand = open(cp, encoding="utf-8").read()
    mp = json.load(open(mpp, encoding="utf-8"))
    R = guards(s1, cand, mp, s1p, cp, mpp)
    ok = all(R.values())
    print("RESULT:", "PASS" if ok else "FAIL")
    if "--fixtures" in a:
        ok = fixtures(s1, cand, mp, s1p) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
