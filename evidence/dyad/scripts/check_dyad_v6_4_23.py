#!/usr/bin/env python3
"""check_dyad_v6_4_23.py -- change-focused gates for the DYAD v6.4.23 maintenance candidate against adopted v6.4.22.

C0  identities: base = v6.4.22 (2363ca40...); candidate = fresh build of the base by build_dyad_v6_4_23.py
C1  determinism: two builds in clean directories are byte-identical (file and edit log)
C2  confinement: undoing every logged edit (new -> old, each new text exactly once, in reverse order) gives the base
    byte for byte; Appendix A of the base is kept byte for byte (one entry inserted)
C3  science invariants: every RID tag and Dyadic RID string of the base is kept; exactly the four declared RIDs are added;
    no grade tag removed and every added grade tag belongs to a logged edit; every removed math span belongs to the old
    text of a logged edit and every added one to its new text
C4  constants: 403/250, C_7 = 100 / 30, C_D = 1000 / 250, c_Q = 0.79246 occur at least as often as in the base; the corrected
    displays 0.36915, 1.51632, 1.06252, 1.61112, 85.07, 27.60, 812.89 remain only inside the [COR] lines and the
    Appendix A entry; the superseded NUMGEN deferral wordings are absent (E1)
C5  D1: the adopted DYAD-THM-OPEN18 sentence is kept verbatim with the scope note; the successor states the certified
    ranges and an interval for q_{3/4} that contains the O1 enclosure (owner_checks.json midpoint +- 1e-30); section 1 and
    section 2 cite the successor
C6  edition lines: title, DRAFT status, Supersedes v6.4.22 with hash, release record path, Appendix A heading, one footer
C7  OPEN state: section 2 "Status:" lines identical to the base
C8  cited evidence: the two owner scripts are present with the SHA-256 cited in the candidate; owner_checks.json reports
    all_pass; dyad_inbox_20261030_l902_chain.py exits 0 and its --control D exits 1
C9  D7: the raw-map identity used by OFN v0.12, T(-x)+T(x) = (0, 2(cosh rho - 1)), holds symbolically for the map of
    DYAD-DEF-PRIMITIVE-MAP (sympy)
Exit 0 all pass / 1 any fail / 3 crash.
usage: check_dyad_v6_4_23.py --base V6422 --cand CANDIDATE [--norebuild] [--out JSON]
"""
import argparse, collections, hashlib, json, os, re, shutil, subprocess, sys, tempfile
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BASE_SHA = "2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29"
SCRIPTS = {"dyad_inbox_20261030_owner_checks.py": "21aec87c555b8b68e0ea2e84833b13fae0f1a1a63f3b1c66959805e2791649e1",
           "dyad_inbox_20261030_l902_chain.py": "aac9996fed172a0784244a1233b0f0b946a6440afb1329a00c09f6f34e477553"}
NEW_RIDS = ["DYAD-THM-OPEN18-STEP-MONOTONE", "DYAD-THM-NF-REM-C7-SHARP", "DYAD-THM-LPHASE-ROWA-BRIDGE", "DYAD-ART-INBOX-20261030"]
GRADE = re.compile(r"`\[(?:THM-ALG via IA|ALG|THM|DEF|CAND|ENG|NUM|HYP|OBS|OPEN|COR|FAIL|RETRACTED)\]`")


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
def load_edits():
    ns = {"__name__": "build_v6423"}
    exec(compile(open(os.path.join(HERE, "build_dyad_v6_4_23.py"), encoding="utf-8").read(), "build_dyad_v6_4_23.py", "exec"), ns)
    return ns["EDITS"]
def build(tmp, base):
    shutil.copy(os.path.join(HERE, "build_dyad_v6_4_23.py"), tmp)
    out, log = os.path.join(tmp, "c.md"), os.path.join(tmp, "log.json")
    r = subprocess.run([sys.executable, "-I", "-B", "build_dyad_v6_4_23.py", os.path.abspath(base), out, log], cwd=tmp, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return open(out, "rb").read(), open(log, "rb").read()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--base", required=True); ap.add_argument("--cand", required=True)
    ap.add_argument("--norebuild", action="store_true"); ap.add_argument("--out", default="check_dyad_v6_4_23.json")
    a = ap.parse_args()
    BB, CB = open(a.base, "rb").read(), open(a.cand, "rb").read(); B, C = BB.decode(), CB.decode()
    EDITS = load_edits()
    G, info = {}, {}
    G["C0"] = sha(BB) == BASE_SHA
    t1, t2 = tempfile.mkdtemp(), tempfile.mkdtemp()
    try:
        b1, l1 = build(t1, a.base)
        if a.norebuild: G["C1"] = None
        else:
            b2, l2 = build(t2, a.base); G["C1"] = b1 == b2 and l1 == l2
        G["C0"] = G["C0"] and (b1 == CB or a.norebuild)
    finally:
        shutil.rmtree(t1); shutil.rmtree(t2)
    # C2: reverse application
    r, rev_ok, bad = C, True, []
    for eid, what, old, new in reversed(EDITS):
        if r.count(new) != 1: rev_ok = False; bad.append(eid); continue
        r = r.replace(new, old)
    bL, bA, bR = split_a(B); cL, cA, cR = split_a(C)
    entry_old, entry_new = next((o, n) for e, w, o, n in EDITS if e == "ED-8")
    a_ok = cA.count(entry_new) == 1 and cA.replace(entry_new, entry_old) == bA
    G["C2"] = rev_ok and r == B and a_ok
    info["C2"] = {"edits": len(EDITS), "reverse_failures": bad, "reverse_equals_base": r == B, "appendix_a_kept": a_ok}
    # C3
    rid = lambda s: re.findall(r"\[RID:\s*([^\]]+)\]", s)
    dy = lambda s: set(re.findall(r"(?<![A-Za-z0-9-])DYAD-(?:ALG|THM|DEF|OPEN|ART|CAND|NUM|CF)-[A-Z0-9]+(?:-[A-Z0-9]+)*", s))
    rb, rc = collections.Counter(rid(B)), collections.Counter(rid(C))
    rid_ok = not (rb - rc) and sorted((rc - rb).elements()) == sorted(NEW_RIDS)
    dy_ok = dy(B) <= dy(C) and dy(C) - dy(B) == set(NEW_RIDS)
    olds, news = collections.Counter(), collections.Counter()
    gdecl = collections.Counter()
    for e, w, o, n in EDITS: olds.update(maths(o)); news.update(maths(n)); gdecl.update(GRADE.findall(n))
    added, removed = maths(C) - maths(B), maths(B) - maths(C)
    math_ok = all(olds[k] >= v for k, v in removed.items()) and all(news[k] >= v for k, v in added.items())
    gb, gc = collections.Counter(GRADE.findall(B)), collections.Counter(GRADE.findall(C))
    grade_ok = not (gb - gc) and all(gdecl[k] >= v for k, v in (gc - gb).items())
    G["C3"] = rid_ok and dy_ok and math_ok and grade_ok
    info["C3"] = {"rid_tags_added": sorted((rc - rb).elements()), "rid_tags_removed": sorted((rb - rc).elements()),
                  "dyad_strings_added": sorted(dy(C) - dy(B)), "math_removed_undeclared": [k for k, v in removed.items() if olds[k] < v][:5],
                  "math_added_undeclared": [k for k, v in added.items() if news[k] < v][:5], "grades_added": dict(gc - gb)}
    # C4
    keep = ["\\tfrac{403}{250}", "C_7=100", "C_7=30", "C_D=1000", "C_D=250", "c_Q=0.79246"]
    same = {k: (B.count(k), C.count(k)) for k in keep}
    cor_lines = [l for l in C.split("\n") if l.startswith("`[COR]` `[v6.4.23]`") or l.startswith("- **[COR] displayed decimals:**")]
    rest = "\n".join(l for l in C.split("\n") if l not in cor_lines)
    stale = ["whose import NUMGEN defers", "whose import NUMGEN has deferred", "a later NUMGEN edition may import this RID", "0.36915", "1.51632", "1.06252", "1.61112\\,", "certificate value $1.61112$", "certificate value $85.07$", "certificate value $27.60$", "certificate value $812.89$"]
    left = [x for x in stale if re.search(re.escape(x) + r"(?![0-9])", rest)]
    G["C4"] = all(b <= c for b, c in same.values()) and not left   # existing occurrences are kept by C2; new text may cite them
    info["C4"] = {"counts_base_cand": same, "stale_left_outside_COR": left, "cor_lines": len(cor_lines)}
    # C5
    old18 = "`[THM-ALG via IA]` `[RID: DYAD-THM-OPEN18]` **OPEN 18 closed.** First-footprint branch monotonicity: $dQ/dq>0$ and $d\\Theta/dq<0$ on both branches $\\Gamma_3$, $\\Gamma_4$; $q=q_*$ is the branch split. Certificate: `open18_arb_cert_final.cpp`."
    succ_i = C.find("[RID: DYAD-THM-OPEN18-STEP-MONOTONE]"); succ = C[succ_i:C.find("\n", succ_i)]
    G["C5"] = (C.count(old18) == 1 and C.count(old18 + " `[scope: historical first-footprint formulation;") == 1
               and "$q\\in(0,\\,1.26021520256]$" in succ and "$q\\in[1.26021320256,\\,2]$" in succ
               and "Uniqueness is stated in $G$ only" in succ
               and "**OPEN 18 closed (step-indexed).**" in C and "- **OPEN 18** `DYAD-THM-OPEN18-STEP-MONOTONE`" in C)
    # numerical validity of the stated interval: it must contain the O1 enclosure (midpoint +- 1e-30, owner_checks.json)
    from decimal import Decimal as Dm, getcontext; getcontext().prec = 60
    mi = re.search(r"q_\{3/4\}\\in\[([0-9.]+),\\ ([0-9.]+)\]", succ)
    oc5 = json.load(open(os.path.join(ROOT, "evidence", "dyad", "inbox-20261030", "owner_checks.json"), encoding="utf-8"))
    m5 = Dm(oc5["info"]["D1"]["O1"]["q_star_36_digits"]); e5 = Dm(oc5["info"]["D1"]["O1"]["enclosure_half_width"])
    encl_ok = bool(mi) and Dm(mi.group(1)) <= m5 - e5 and Dm(mi.group(2)) >= m5 + e5
    G["C5"] = G["C5"] and encl_ok
    info["C5"] = {"interval": mi.groups() if mi else None, "contains_O1_enclosure": encl_ok}
    # C6
    head = C[:C.index("## Local Tag Aliases")]
    G["C6"] = (C.startswith("# RTG_DYADIC_OSCILLATOR_DSN_v6.4.23\n") and "**Document status:** DRAFT — v6.4.23 candidate" in head
               and "**Supersedes:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.22` (SHA-256 `" + BASE_SHA + "`; tag `dyad-v6.4.22`)." in head
               and "`records/dyad/RTG_DYADIC_v6_4_23_RELEASE_RECORD.md`" in head and "### v6.4.23 — 30 October 2026 — Draft candidate" in cA
               and len(re.findall(r"^\*END OF DOCUMENT", C, re.M)) == 1 and "*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.23 (DRAFT candidate, 30 October 2026).*" in C
               and C.count("<!-- AI_CONTEXT_CORE_END -->") == B.count("<!-- AI_CONTEXT_CORE_END -->"))
    # C7
    s2 = lambda s: [l for l in s[s.index("## §2."):s.index("## §3.")].split("\n") if "Status:" in l]
    G["C7"] = s2(B) == s2(C)
    # C8
    ok8, det = True, {}
    for f, h in SCRIPTS.items():
        p = os.path.join(HERE, f); hh = sha(open(p, "rb").read()) if os.path.exists(p) else None
        det[f] = hh; ok8 = ok8 and hh == h and h in C
    oc = os.path.join(ROOT, "evidence", "dyad", "inbox-20261030", "owner_checks.json")
    ok8 = ok8 and os.path.exists(oc) and json.load(open(oc, encoding="utf-8"))["all_pass"] is True
    p = os.path.join(HERE, "dyad_inbox_20261030_l902_chain.py"); td = tempfile.mkdtemp()
    try:
        r0 = subprocess.run([sys.executable, "-I", "-B", p, "--out", os.path.join(td, "a.json")], capture_output=True, text=True)
        rd = subprocess.run([sys.executable, "-I", "-B", p, "--out", os.path.join(td, "b.json"), "--control", "D"], capture_output=True, text=True)
    finally:
        shutil.rmtree(td)
    ok8 = ok8 and r0.returncode == 0 and rd.returncode == 1
    G["C8"] = ok8; info["C8"] = det
    # C9
    import sympy as sp
    rho, eta = sp.symbols("rho eta", real=True)
    T = lambda r, e: (r - sp.sin(e), e + sp.exp(r) - 1 - sp.sin(e))
    s1, s2_ = T(-rho, -eta), T(rho, eta)
    G["C9"] = sp.simplify(s1[0] + s2_[0]) == 0 and sp.simplify((s1[1] + s2_[1]) - 2 * (sp.cosh(rho) - 1)) == 0 and \
        "T(-x)+T(x)=(0,2(\\cosh\\rho-1))" in C
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
