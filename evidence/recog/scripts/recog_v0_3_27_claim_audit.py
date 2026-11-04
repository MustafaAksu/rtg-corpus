#!/usr/bin/env python3
"""RECOG v0.3.27 stage 1 -- claim-level audit of the Dyadic and NUMGEN imports at the current owner tags (R4, R6).

Rows: the 31 rows of the v0.3.23 audit (recog_v0_3_23_claim_audit.py, read from this repository and not modified), re-run at
dyad-v6.4.23 / numgen-v1.21, with the two rows whose owner text changed rewritten (NF-REM: certified-bound displays; GAP-LOCK
Lemma 3: owner RID assigned at v1.21), plus the rows the v0.3.27 groups add (LPHASE row-A bridge, its proof-outline constants,
SPIRAL-REM, C7-SHARP, the NF6 jet coefficients used by RECOG-ALG-A1C-JET-REMAINDER-BOUNDS).

Delimiter-anchored (R4): a statement string counts only where it occurs inside the cited entry (from the anchor's line to the
next line that opens another RID entry or a heading; rows marked scope "file" are searched in the whole file, as v0.3.23) and is
not continued by a digit, nor preceded by a digit when it starts with one -- so "85.07" is not found inside "85.0732".
Direction (item 7): every owner ceiling RECOG uses is compared with the owner's certified exact value in the same entry.
Negative controls: NC1 the v0.3.23 NF-REM needle (display 85.07) is not found; NC2 "0.36915" is not found delimiter-anchored in
the bridge entry although a plain substring test finds it; NC3 the direction check refuses c'_Q = 0.36915; NC4 the direction check
refuses the B1 window display 1.011e-4 against |G|/75.69.

EV-SRC-READ: current-source presence of the quoted statements; no comparison with earlier pinned editions; no owner certificate rerun.
usage (repository root):  python -I evidence/recog/scripts/recog_v0_3_27_claim_audit.py OUT_JSON      exit 0 iff all pass
"""
import hashlib, json, re, runpy, subprocess, sys
from fractions import Fraction as Fr
from decimal import Decimal, getcontext

TAGS = {
    "dyad": ("dyad-v6.4.23", "dsn/RTG_DYADIC_OSCILLATOR_DSN.md", "9f874ccc1cd684482f26a27fca13b37102977cba2a80a75e762ecd7b300425cb"),
    "numgen": ("numgen-v1.21", "dsn/RTG_NUMBER_GENESIS_DSN.md", "4805760d683bb3abddfdaab4737f6bb75beed392906bd4c54d8ae79245f15701"),
}
V23 = "evidence/recog/scripts/recog_v0_3_23_claim_audit.py"
V23_SHA = None  # recorded in the output, not asserted (the file is tracked in git)

REWRITE = {
 "NF-REM": ("NF-REM", "§7 row; §6.14", "dyad", "DYAD-THM-NF-REM", "v6.4.10 §6.14 (current source v6.4.22 at v0.3.26)", "[THM]",
            "[RID: DYAD-THM-NF-REM]", [r"$C_7=100$ (certified bound $85.0732$, rounded up)", r"$C_D=1000$", r"$C_7=30$ (certified bound $27.6023$, rounded up)", r"$C_D=250$"]),
 "NG-GAPLOCK3": ("NG-GAPLOCK3", "§2 R6 (two consumption grades); §6.16e RECOG-RESULT-BTOKEN-LOG-EQUIVALENCE", "numgen", "NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO",
            "v1.20.8 §6.6 GAP-LOCK Lemma 3 (no RID)", "[RESULT] [from: ALG]",
            "[RID: NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO]", [r"**GAP-LOCK Lemma 3 CLOSED — event-time physical-slip locking.**", r"G_(n_j) = C + (pi/3)s_j - o_j."]),
}
NEW = [
 ("LPHASE-BRIDGE", "§6.13b TAIL-HARMONICS, SHARPENED-SCHEDULE, COMBINED-TAIL, ENV; §6.16e START-OFFSET (ii), decoder; §7 row (R1, R2)", "dyad",
  "DYAD-THM-LPHASE-ROWA-BRIDGE", "(D5) proof constants of DYAD-THM-LPHASE-ROWA-REMAINDER, c'_Q copied as 0.36915", "[THM] [v6.4.23]",
  "[RID: DYAD-THM-LPHASE-ROWA-BRIDGE]", [r"r=\Lambda_3(z)+[S_\Theta-L_\Theta]+\tau[D_Q-D_3]+[\operatorname{Arg}(J/z)+\tau q]+\operatorname{Arg}(\widehat F/J)$ exactly",
   r"$c_Q=0.79246$", r"$c'_Q=0.36916$", r"$0.7924576152\ldots$, $0.3691523046\ldots$", r"[scope: row-A disk $|z|\le\tfrac1{20}$"]),
 ("LPHASE-OUTLINE", "§6.13b COMBINED-TAIL ($c_J^R$, $c_7^R$ compared); fallback D5A qualifier", "dyad",
  "proof outline of DYAD-THM-LPHASE-ROWA-REMAINDER (no RID)", "(D5)", "proof text",
  "[RID: DYAD-THM-LPHASE-ROWA-REMAINDER]", [r"$|\operatorname{Arg}(J/z)+\tau q|\le c_Jq^2$, $c_J=0.50220$", r"$|\operatorname{Arg}(\widehat F/J)|\le c_7q^3$, $c_7=157.58$, from $C_7=100$ (DYAD-THM-NF-REM)"]),
 ("SPIRAL-REM", "§6.13b ($K_\\Theta$); §7 row (R2)", "dyad", "DYAD-THM-OPEN3-SPIRAL-REM", "(D5) via the LPHASE proof", "[THM] [v6.4.14]",
  "[RID: DYAD-THM-OPEN3-SPIRAL-REM]", [r"|S_\Theta(z)-L_\Theta(z)|\le K_\Theta q^2", r"| $\tfrac1{20}$ | 100 | $\tfrac{123}{125}$ |", r"| $\tfrac1{40}$ | 30 | $\tfrac{909}{1000}$ |"]),
 ("C7-SHARP", "§6.13a RECOG-THM-R9-SHARPENED-ROWS-C7; §7 row (R3)", "dyad", "DYAD-THM-NF-REM-C7-SHARP", "[assuming:] 85.1 / 27.7", "[THM] [v6.4.23]",
  "[RID: DYAD-THM-NF-REM-C7-SHARP]", [r"$C_7=85.1$ on $|z|\le\tfrac1{20}$ and $C_7=27.7$ on $|z|\le\tfrac1{40}$", r"(exact bounds $85.0731933471\ldots$, $27.6022209836\ldots$",
   r"[scope: chart and norm of DYAD-THM-NF-REM; rows not mixed]"]),
 ("NF6-JET", "§6.13b RECOG-ALG-A1C-JET-REMAINDER-BOUNDS (R2)", "dyad", "DYAD-ALG-NF6", "v6.4.10 §6.14", "[ALG]",
  "[RID: DYAD-ALG-NF6]", [r"\mu=-\tfrac12-\tfrac{2i\sqrt3}{3}", r"a_{32}=-\tfrac{97}{432}+\tfrac{197i\sqrt3}{324}", r"a_{05}=-\tfrac{49}{8640}-\tfrac{307i\sqrt3}{25920}"]),
]
FILE_SCOPE = {"CONSTANTS", "FIXED-POINTS", "H2", "NG-RATIO", "NG-L1", "NG-N1C"}  # anchors that are not entry openers, as in v0.3.23
# rows whose v0.3.23 context strings sit outside the RID's own line block (a later display, a neighbouring paragraph or a different
# section): searched in the enclosing numbered section of the anchor (heading to the next heading of the same or higher level), or
# in the file where the context string is stated in another section (SH-R0: §1 / §6.15; LIEGAUGE: the normalisation table;
# SIXSTEP-JET: the angle recursion in §6.8, the RECOG row citing the §6.7/§6.8 block)
SECTION_SCOPE = {"LPHASE-ROWA", "NG-DEFECT"}
FILE_SCOPE |= {"SH-R0", "LIEGAUGE", "SIXSTEP-JET"}

def show(tag, path):
    return subprocess.run(["git", "show", f"{tag}:{path}"], check=True, capture_output=True).stdout

def entry(text, anchor):
    lines = text.split("\n")
    hit = [i for i, l in enumerate(lines) if anchor in l]
    if not hit: return None
    i = hit[0]; j = i + 1
    while j < len(lines) and not ("[RID: " in lines[j] or lines[j].startswith("#") or "**RID:**" in lines[j]): j += 1
    return "\n".join(lines[i:j])

def section(text, anchor):
    lines = text.split("\n"); i = next(k for k, l in enumerate(lines) if anchor in l)
    h = max(k for k in range(i + 1) if lines[k].startswith("#")); lv = len(lines[h]) - len(lines[h].lstrip("#"))
    j = next((k for k in range(i + 1, len(lines)) if lines[k].startswith("#") and len(lines[k]) - len(lines[k].lstrip("#")) <= lv), len(lines))
    return "\n".join(lines[h:j])

def found(scope, needle):
    for m in re.finditer(re.escape(needle), scope):
        a, b = m.start(), m.end()
        if needle[-1].isdigit() and b < len(scope) and scope[b].isdigit(): continue
        if needle[0].isdigit() and a > 0 and scope[a - 1].isdigit(): continue
        return True
    return False

def main(out):
    v23 = runpy.run_path(V23)
    rows_in = []
    for r in v23["ROWS"]:
        rows_in.append(REWRITE.get(r[0], r))
    rows_in += NEW
    src, ids = {}, {}
    for k, (tag, path, sha) in TAGS.items():
        b = show(tag, path); got = hashlib.sha256(b).hexdigest()
        assert got == sha, f"{tag}: sha {got} != {sha}"
        src[k] = b.decode("utf-8"); ids[k] = {"tag": tag, "path": path, "sha256": got}
    rows, ok = [], True
    for key, loc, owner, rid, pin, tagform, anchor, pats in rows_in:
        text = src[owner]
        scope_kind = "file" if key in FILE_SCOPE else ("section" if key in SECTION_SCOPE else "entry")
        sc = text if scope_kind == "file" else (section(text, anchor) if scope_kind == "section" else entry(text, anchor))
        if key == "LPHASE-OUTLINE":  # the proof outline follows the theorem entry; scope: from the theorem to the bridge lemma
            i = text.index(anchor); sc = text[i:text.index("[RID: DYAD-THM-LPHASE-ROWA-BRIDGE]")]; scope_kind = "theorem-to-bridge"
        a = sc is not None and anchor in text
        miss = [p for p in pats if sc is None or not found(sc, p)]
        good = a and not miss; ok &= good
        rows.append({"key": key, "recog_location": loc, "owner": ids[owner]["tag"], "owner_rid_or_section": rid, "recog_previous_pin": pin,
                     "current_owner_tag_form": tagform, "scope": scope_kind, "anchor_found": a, "statement_strings": len(pats), "missing": miss,
                     "class": "P (quoted statement present, delimiter-anchored, at the current tag)" if good else "CHECK"})
    # direction checks: owner ceiling used by RECOG >= owner's certified exact value (same entry)
    getcontext().prec = 40
    br = entry(src["dyad"], "[RID: DYAD-THM-LPHASE-ROWA-BRIDGE]"); c7 = entry(src["dyad"], "[RID: DYAD-THM-NF-REM-C7-SHARP]")
    def exact(sc, lead): return Decimal(re.search(re.escape(lead) + r"(\d+)\\ldots", sc).group(0)[:-6])
    DIR = [("c_Q", br, Decimal("0.79246"), exact(br, "0.7924")), ("c'_Q", br, Decimal("0.36916"), exact(br, "0.3691")),
           ("C_7 (1/20)", c7, Decimal("85.1"), exact(c7, "85.07")), ("C_7 (1/40)", c7, Decimal("27.7"), exact(c7, "27.60"))]
    dirs = []
    for name, sc, ceil, ex in DIR:
        assert found(sc, str(ceil)), name
        dirs.append({"constant": name, "ceiling_used": str(ceil), "owner_certified_exact_prefix": str(ex), "ceiling_ge_exact": ceil >= ex}); ok &= ceil >= ex
    # negative controls
    nf = entry(src["dyad"], "[RID: DYAD-THM-NF-REM]")
    G = (Decimal(481897).sqrt() / 90720) / Decimal("75.69")
    nc = {"NC1_old_NF_REM_needle_absent": not found(nf, r"$C_7=100$ (certificate value $85.07$)"),
          "NC2_036915_substring_present_but_not_delimited": ("0.36915" in br) and not found(br, "0.36915"),
          "NC3_direction_refuses_036915": not (Decimal("0.36915") >= exact(br, "0.3691")),
          "NC4_direction_refuses_window_1011e-4": not (Decimal("1.011e-4") <= G) and Decimal("1.010e-4") <= G}
    ok &= all(nc.values())
    json.dump({"sources": ids, "v0_3_23_rows_from": {"path": V23, "sha256": hashlib.sha256(open(V23, "rb").read()).hexdigest()},
               "rows": rows, "direction_checks": dirs, "B1_window_certified": str(G), "negative_controls": nc, "all_pass": ok,
               "evidence_state": "EV-SRC-READ: current-source presence of the quoted statements, delimiter-anchored inside the cited entry; no comparison with earlier pinned editions; no owner certificate rerun"},
              open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for r in rows: print(("PASS " if r["class"].startswith("P") else "FAIL ") + r["key"], r["scope"], r["missing"] or "")
    for d in dirs: print(("PASS " if d["ceiling_ge_exact"] else "FAIL ") + "direction " + d["constant"], d["ceiling_used"], ">=", d["owner_certified_exact_prefix"])
    for k, v in nc.items(): print(("PASS " if v else "FAIL ") + k)
    print("ALL PASS" if ok else "FAILURES", f"({len(rows)} rows, {len(dirs)} direction checks, {len(nc)} negative controls)")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main(sys.argv[1])
