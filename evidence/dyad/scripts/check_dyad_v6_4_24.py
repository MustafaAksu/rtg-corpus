#!/usr/bin/env python3
"""check_dyad_v6_4_24.py -- change-focused gates for the DYAD v6.4.24 maintenance candidate against adopted v6.4.23.

C0  identities: base = v6.4.23 (9f874ccc...); candidate = fresh build of the base by build_dyad_v6_4_24.py
C1  determinism: two builds in clean directories are byte-identical (file and edit log)
C2  confinement: undoing every logged edit (new -> old, each new text exactly once, in reverse order) gives the base
    byte for byte; Appendix A of the base is kept byte for byte (one entry inserted)
C3  science invariants: every RID tag and Dyadic RID string of the base is kept; exactly the seven declared RIDs are added;
    the only grade tags removed are the two [THM] tags of the declared retag (X4-1, X4-2) and every added grade tag belongs
    to a logged edit; every removed math span belongs to the old text of a logged edit and every added one to its new text
C4  constants: the adopted OPEN 21 constants occur at least as often as in the base; S_A = 492/25 and S_B = 6357/1000 are the
    three-decimal ceilings of K'_j + C'_{2,j}(256/225)^2 w_j (exact Fractions) and the exact primary constants are printed;
    superseded register wordings are absent
C5  S1 integrity: the adopted DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER line and its table rows are byte-identical to the
    base; the new entry carries [assuming: RECOG-THM-R9-SHARPENED-ROWS] and its import pin; RECOG's entry is byte-identical
    at recog-v0.3.26 and recog-v0.3.27 and states 259.2 and 81.49
C6  edition lines: title, DRAFT status, Supersedes v6.4.23 with hash, release record path, Appendix A heading, one footer
C7  OPEN state: section 2 "Status:" lines identical to the base
C8  cited evidence: every script, output and source hash cited by the new Section 8 entries equals the file in the
    repository; the cited outputs report all_pass
C9  spot checks of the registered and recorded statements (exact): det DT; order of lambda; the resonance condition;
    P'(u) = alpha (c40 + mu u); the stage-2b figures quoted in Section 2 against jump_scout.json; the bound 1.76e-6
    recomputed from the INF-010 formula with K_2, K_4 rounded down
C10 Appendix F: every Dyadic-pattern string of AZ v0.7 is an owner RID, or one of the two exceptions named in the text
C11 register: the Section 7.0 hashes of RECOG v0.3.27, Genesis v2.10, Triadic v1.7, Programme v1.4 and AZ v0.7 equal
    BASELINE.md and the file at the tag
Exit 0 all pass / 1 any fail / 3 crash.
usage: check_dyad_v6_4_24.py --base V6423 --cand CANDIDATE [--norebuild] [--out JSON]
"""
import argparse, collections, hashlib, json, os, re, shutil, subprocess, sys, tempfile
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BASE_SHA = "9f874ccc1cd684482f26a27fca13b37102977cba2a80a75e762ecd7b300425cb"
BUILD = "build_dyad_v6_4_24.py"
NEW_RIDS = ["DYAD-THM-OPEN21-SHARP-ROWS", "DYAD-ALG-NOT-AREA-PRESERVING", "DYAD-ALG-P6-LINEAR-ORDER", "DYAD-ALG-HOMOLOGICAL-RESONANCE",
            "DYAD-ART-OPEN21-SHARP-ROWS", "DYAD-ART-BRIDGE-NOTE-CHECK", "DYAD-ART-OPEN20-AN-PILOT"]
FILES = {  # path -> SHA-256 cited in the candidate
 "evidence/dyad/scripts/dyad_s1_open21_sharp_rows_cert.py": "325c2a8a787a5660d5acc243e5b27fcfc91fc225460b0ada9d4b52464c0130ef",
 "evidence/dyad/scripts/dyad_bridge_note_v1_1_check.py": "a0382ceaab5c4a40c09dd2623e7c76d3f89adaa9ed1ec6713648646d75e24734",
 "upload/dyad-bridge-note/dyad_triad_antisymmetric_bridge_v1_1.md": "5ddebfe46b5572761a5154a05712fbcfe4e675f912430ee7d6bfcf0d93f4e875",
 "evidence/dyad/scripts/dyad_open20_an_stage1_prep.py": "5c22ff7aab5d9dabdf243bfc6e279616b4fdbc5ea9d8429fa513c3b2584d8568",
 "evidence/dyad/open20-an/stage1_prep.json": "2c9ae6376e0c482f2ba520a7ea8e2b38606a6821f7ac3bfa259d4d6020d04739",
 "evidence/dyad/scripts/dyad_open20_an_stage2_scout.py": "2961e6383eb9b0e5fb58c0fcb892aa6b05dc2be0faf4c766a3f85be1346008ad",
 "evidence/dyad/scripts/dyad_open20_an_stage3_apriori_route_check.py": "692dd395584eabdd880f37c1e5cbabe26ca00bcdae14dbca6827392fe31f4430",
 "evidence/dyad/scripts/dyad_open20_lit_inf014_inf015_hypothesis_check.py": "517be03623da791a9759856d18491f676175d399c62c3ace7fbf8e887531b4d4",
 "evidence/dyad/scripts/dyad_open20_an_stage2b_jump_scout.py": "2d125640243d255971a0284cac2613607791b47390ae0079d87a3488f31f96c8",
 "evidence/dyad/scripts/dyad_open20_an_stage2b_law.py": "0cfe90f884a7ce69f9670202978ffabd1473233e7c7b174e28dab61f5ce3c623"}
OUTPUTS = ["evidence/dyad/s1-open21-sharp/s1_cert.json", "evidence/dyad/bridge-note-v1-1/bridge_check.json",
           "evidence/dyad/open20-an/stage1_prep.json", "evidence/dyad/open20-an/stage3-route/route_check.json",
           "evidence/dyad/open20-an/lit-inf014-inf015/hypothesis_check.json", "evidence/dyad/open20-an/stage2b/jump_scout.json",
           "evidence/dyad/open20-an/stage2b/jump_law.json"]
REGISTER = {  # study row in BASELINE.md -> (tag, file, sha)
 "RECOG": ("recog-v0.3.27", "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md", "19556f913f51b98599faa6ad88c363dda0a278345677f3bd69f3b892d810e1f1"),
 "GEN": ("gen-v2.10", "dsn/RTG_GENESIS_GEOMETRY_DSN.md", "63c3b020d9c63a43a2e5e9a43c411fad2d07dfcab33995bd928683435bb13d62"),
 "TRIAD": ("triad-v1.7", "dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md", "506f3403628ca01d5a904f885df055d9bfbdf1ef5e474e24e83d4797c122e64a"),
 "Programme": ("programme-v1.4", "dsn/RTG_PROGRAMME_OVERVIEW.md", "37d857d08bb47771ed50fc5829584be74aab120a23e922eba7c84bae097f28c0"),
 "AZ": ("az-v0.7", "dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md", "2294d2a3287651802824a77ea22fb8f3896f6837cca1162fd8479ff02839fc94")}
GRADE = re.compile(r"`\[(?:THM-ALG via IA|ALG|THM|DEF|CAND|ENG|NUM|HYP|OBS|OPEN|COR|FAIL|RETRACTED|SESSION)\]`")


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
    ns = {"__name__": "build_v6424"}
    exec(compile(open(os.path.join(HERE, BUILD), encoding="utf-8").read(), BUILD, "exec"), ns)
    return ns["EDITS"]
def build(tmp, base):
    shutil.copy(os.path.join(HERE, BUILD), tmp)
    out, log = os.path.join(tmp, "c.md"), os.path.join(tmp, "log.json")
    r = subprocess.run([sys.executable, "-I", "-B", BUILD, os.path.abspath(base), out, log], cwd=tmp, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return open(out, "rb").read(), open(log, "rb").read()
def git_show(ref):
    r = subprocess.run(["git", "-C", ROOT, "show", ref], capture_output=True)
    assert r.returncode == 0, ref
    return r.stdout
def ceil3(x):
    n = -((-x.numerator * 1000) // x.denominator)
    return Fr(n, 1000)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--base", required=True); ap.add_argument("--cand", required=True)
    ap.add_argument("--norebuild", action="store_true"); ap.add_argument("--out", default="check_dyad_v6_4_24.json")
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
    # C2
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
    olds, news, gdecl, gold = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
    for e, w, o, n in EDITS:
        olds.update(maths(o)); news.update(maths(n)); gdecl.update(GRADE.findall(n)); gold.update(GRADE.findall(o))
    added, removed = maths(C) - maths(B), maths(B) - maths(C)
    math_ok = all(olds[k] >= v for k, v in removed.items()) and all(news[k] >= v for k, v in added.items())
    gb, gc = collections.Counter(GRADE.findall(B)), collections.Counter(GRADE.findall(C))
    per_edit_removed = {e: dict(collections.Counter(GRADE.findall(o)) - collections.Counter(GRADE.findall(n))) for e, w, o, n in EDITS}
    per_edit_removed = {e: v for e, v in per_edit_removed.items() if v}
    retag = per_edit_removed == {"X4-1": {"`[THM]`": 1}, "X4-2": {"`[THM]`": 1}}      # with C2, this is every removed grade tag
    net = collections.Counter()
    for e, w, o, n in EDITS:
        net.update(GRADE.findall(n)); net.subtract(GRADE.findall(o))
    grade_ok = retag and all(gc[k] - gb[k] == net[k] for k in set(gc) | set(gb) | set(net))
    xo = {e: (o, n) for e, w, o, n in EDITS if e in ("X4-1", "X4-2")}
    retag_decl = all(o.startswith("`[THM]` ") and n.startswith("`[ALG]` ") and "retagged from [THM]" in n for o, n in xo.values()) and len(xo) == 2
    G["C3"] = rid_ok and dy_ok and math_ok and grade_ok and retag_decl
    info["C3"] = {"rid_tags_added": sorted((rc - rb).elements()), "rid_tags_removed": sorted((rb - rc).elements()),
                  "dyad_strings_added": sorted(dy(C) - dy(B)), "math_removed_undeclared": [k for k, v in removed.items() if olds[k] < v][:5],
                  "math_added_undeclared": [k for k, v in added.items() if news[k] < v][:5],
                  "grade_net_change": {k: v for k, v in net.items() if v}, "grades_removed_per_edit": per_edit_removed}
    # C4
    keep = ["\\tfrac{3951}{1000}", "\\tfrac{971}{250}", "\\tfrac{33882112}{50625}", "\\tfrac{10682368}{50625}", "\\tfrac{8831}{250}", "\\tfrac{883}{100}", "\\tfrac{403}{250}"]
    same = {k: (B.count(k), C.count(k)) for k in keep}
    f = (Fr(256, 225)) ** 2
    pA, pB = Fr(2592, 10) * f, Fr(8149, 100) * f
    SA, SB = ceil3(Fr(3951, 1000) + pA * Fr(3, 64)), ceil3(Fr(971, 250) + pB * Fr(3, 128))
    s1_ok = (pA == Fr(1048576, 3125) and pB == Fr(133513216, 1265625) and SA == Fr(492, 25) and SB == Fr(6357, 1000)
             and SA < Fr(8831, 250) and SB < Fr(883, 100)
             and all(x in C for x in ("\\tfrac{1048576}{3125}", "\\tfrac{133513216}{1265625}", "\\tfrac{492}{25}", "\\tfrac{6357}{1000}")))
    stale = ["not yet sent", "`[v6.4.11, provisional]`", "(current edition v0.3.26, §7.0)", "(v1.6.1, adopted 19 Oct 2026)", "`RTG_PROGRAMME_OVERVIEW_v1.3`",
             "(v2.9, adopted 25 Oct 2026)", "| AZ | v0.6 | June 2026", "retained through v0.3.26;"]
    left = [x for x in stale if x in C]
    G["C4"] = all(b <= c for b, c in same.values()) and s1_ok and not left
    info["C4"] = {"counts_base_cand": same, "S_A": str(SA), "S_B": str(SB), "stale_left": left}
    # C5
    def line_with(s, key):
        ls = [l for l in s.split("\n") if key in l]; return ls
    old_thm_b, old_thm_c = line_with(B, "[RID: DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER]"), line_with(C, "[RID: DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER]")
    rows_b = [l for l in B.split("\n") if l.startswith("| A | $\\lvert z\\rvert\\le\\tfrac1{20}$ | $\\tfrac3{64}$ | $\\tfrac{3951}{1000}$ | $517$") or l.startswith("| B | $\\lvert z\\rvert\\le\\tfrac1{40}$ | $\\tfrac3{128}$ | $\\tfrac{971}{250}$ | $163$")]
    rows_c = [l for l in C.split("\n") if l in rows_b]
    new = line_with(C, "[RID: DYAD-THM-OPEN21-SHARP-ROWS]")
    r26 = [l for l in git_show("recog-v0.3.26:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md").decode().split("\n") if "[RID: RECOG-THM-R9-SHARPENED-ROWS]" in l]
    r27 = [l for l in git_show("recog-v0.3.27:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md").decode().split("\n") if "[RID: RECOG-THM-R9-SHARPENED-ROWS]" in l]
    G["C5"] = (len(old_thm_b) == 1 and old_thm_b == old_thm_c and len(rows_b) == 2 and rows_c == rows_b and len(new) == 1
               and new[0].startswith("`[THM]` `[assuming: RECOG-THM-R9-SHARPENED-ROWS]` [RID: DYAD-THM-OPEN21-SHARP-ROWS] `[v6.4.24]`")
               and "RTG_RELATIONAL_RECOGNITION_DSN v0.3.26 §6.13a | RECOG-THM-R9-SHARPENED-ROWS" in new[0]
               and len(r26) == 1 and r26 == r27 and "259.2" in r26[0] and "81.49" in r26[0])
    info["C5"] = {"recog_entry_identical_26_27": r26 == r27}
    # C6
    head = C[:C.index("## Local Tag Aliases")]
    G["C6"] = (C.startswith("# RTG_DYADIC_OSCILLATOR_DSN_v6.4.24\n") and "**Document status:** DRAFT — v6.4.24 candidate" in head
               and "**Supersedes:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.23` (SHA-256 `" + BASE_SHA + "`; tag `dyad-v6.4.23`)." in head
               and "`records/dyad/RTG_DYADIC_v6_4_24_RELEASE_RECORD.md`" in head and "### v6.4.24 — 11 November 2026 — Draft candidate" in cA
               and len(re.findall(r"^\*END OF DOCUMENT", C, re.M)) == 1 and "*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.24 (DRAFT candidate, 11 November 2026).*" in C
               and C.count("<!-- AI_CONTEXT_CORE_END -->") == B.count("<!-- AI_CONTEXT_CORE_END -->"))
    # C7
    s2 = lambda s: [l for l in s[s.index("## §2."):s.index("## §3.")].split("\n") if "Status:" in l]
    G["C7"] = s2(B) == s2(C)
    # C8
    ok8, det = True, {}
    for p, h in FILES.items():
        fp = os.path.join(ROOT, p); hh = sha(open(fp, "rb").read()) if os.path.exists(fp) else None
        det[p] = hh == h; ok8 = ok8 and hh == h and h in C
    for p in OUTPUTS:
        fp = os.path.join(ROOT, p)
        good = os.path.exists(fp) and json.load(open(fp, encoding="utf-8")).get("all_pass") is True
        det[p] = good; ok8 = ok8 and good
    G["C8"] = ok8; info["C8"] = det
    # C9
    import sympy as sp, mpmath as mp
    rho, eta = sp.symbols("rho eta", real=True)
    T = (rho - sp.sin(eta), eta + sp.exp(rho) - 1 - sp.sin(eta))
    detJ = sp.simplify(sp.Matrix([[sp.diff(t, v) for v in (rho, eta)] for t in T]).det())
    c_det = sp.simplify(detJ - (1 + (sp.exp(rho) - 1) * sp.cos(eta))) == 0 and "\\det J=1+(e^\\rho-1)\\cos\\eta" in C
    lam = sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    c_ord = sp.simplify(lam ** 6 - 1) == 0 and all(sp.simplify(lam ** j - 1) != 0 for j in range(1, 6))
    c_res = all((sp.simplify(lam ** x * sp.conjugate(lam) ** y - lam) == 0) == ((x - y - 1) % 6 == 0) for x in range(0, 8) for y in range(0, 8) if 2 <= x + y <= 7)
    s3 = sp.sqrt(3) * sp.I
    mu, c40 = sp.Rational(-1, 2) - sp.Rational(2, 3) * s3, sp.Rational(-1, 16) + sp.Rational(7, 144) * s3
    d31 = sp.Rational(1, 3) - sp.Rational(1, 9) * s3
    al = sp.Rational(-102, 19) - sp.Rational(16, 19) * s3
    A_, B_ = sp.conjugate(mu) - 2 * mu, d31 - 2 * c40
    c_P = sp.simplify(sp.expand(2 * A_ - al * mu)) == 0 and sp.simplify(sp.expand(B_ - al * c40)) == 0
    js = json.load(open(os.path.join(ROOT, "evidence/dyad/open20-an/stage2b/jump_scout.json"), encoding="utf-8"))["info"]["table_base"]
    tb = {r_["r"]: float(r_["abs_deltaY"]) for r_ in js}
    c_2b = abs(tb["0.45"] / 1.6e-5 - 1) < 0.05 and abs(tb["0.24"] / 7.3e-50 - 1) < 0.05 and "1.6\\cdot10^{-5}" in C and "7.3\\cdot10^{-50}" in C
    jl = json.load(open(os.path.join(ROOT, "evidence/dyad/open20-an/stage2b/jump_law.json"), encoding="utf-8"))["info"]["local_slopes"]
    c_law = all(0.98 < float(x["slope_over_minus_2pi"]) < 1.0 for x in jl)
    mp.mp.dps = 40
    alm = mp.mpc(mp.mpf(-102) / 19, -16 * mp.sqrt(3) / 19); K2, K4 = mp.mpf("0.72268998"), mp.mpf("5.54117445")
    rho_al = abs(alm) * abs(alm + 1) / 2 * mp.power(2, abs(alm.real + 2)) * mp.exp(abs(alm.imag) * mp.pi / 6)
    s = 5 - alm.real
    B0 = mp.exp(abs(alm.imag) * mp.pi / 3) * 2 * rho_al * (1 + K2) ** 2 * (1 + abs(alm) + K4) * mp.power(3, s / 3) / (s - 3)
    c_lit = 1 / B0 < mp.mpf("1.76e-6") and 1 / B0 > mp.mpf("1.75e-6") and "1.76\\cdot10^{-6}" in C
    G["C9"] = bool(c_det and c_ord and c_res and c_P and c_2b and c_law and c_lit)
    info["C9"] = {"detDT": bool(c_det), "lambda_order_6": bool(c_ord), "resonance_condition": bool(c_res), "P_prime_identity": bool(c_P),
                  "stage2b_figures": bool(c_2b), "stage2b_slopes": bool(c_law), "X_bound": mp.nstr(1 / B0, 8), "X_bound_ok": bool(c_lit)}
    # C10
    az = git_show("az-v0.7:dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md").decode()
    strs = sorted(set(re.findall(r"DYAD-[A-Z0-9]+(?:-[A-Z0-9]+)*", az)))
    not_rid = [x for x in strs if "[RID: %s]" % x not in C]
    G["C10"] = not_rid == ["DYAD-ALG-Q3-CANCEL", "DYAD-OPEN-B5-ALLP"] and az.count("DYAD-ALG-Q3-CANCEL") == 1
    info["C10"] = {"az_strings": len(strs), "not_owner_rid": not_rid}
    # C11
    base_md = open(os.path.join(ROOT, "BASELINE.md"), encoding="utf-8").read()
    ok11, d11 = True, {}
    for study, (tag, path, h) in REGISTER.items():
        row = [l for l in base_md.split("\n") if l.startswith("| %s |" % study)]
        good = len(row) == 1 and h in row[0] and sha(git_show("%s:%s" % (tag, path))) == h and h in C and "`%s`" % tag in C
        d11[study] = good; ok11 = ok11 and good
    G["C11"] = ok11; info["C11"] = d11
    ok = all(v is not False for v in G.values())
    for k in sorted(G, key=lambda x: int(x[1:])): print(k, {True: "PASS", False: "FAIL", None: "SKIP"}[G[k]])
    print("ALL PASS" if ok else "FAIL")
    with open(a.out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump({"gates": G, "info": info, "all_pass": ok, "candidate_sha256": sha(CB), "base_sha256": sha(BB)}, fh, indent=1, sort_keys=True, ensure_ascii=False); fh.write("\n")
    return 0 if ok else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:
        print("CRASH", repr(e)); sys.exit(3)
