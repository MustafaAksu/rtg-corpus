#!/usr/bin/env python3
"""DYAD v6.4.21, stage 2: compaction of the corrected intermediate (Methodology v1.4).

Layout only: current-only header with the §1 profile exception (closeout E-1), one
footer, compact Appendix A (E-2), history sections and history pointers left in
v6.4.20 (tag `dyad-v6.4.20`). Writes the candidate and the movement map that
tools/check_compaction.py verifies.

usage: build_dyad_v6_4_21_stage2.py INTERMEDIATE V6_4_20 OUT_CANDIDATE OUT_MAP
"""
import hashlib, json, re, sys

INTERMEDIATE_SHA = "f2b20419898ae1c84235a808479391f2d29fc05b2f9a0e46f606539327d29119"
V6420_SHA = "0b2d5a44eb818598bb330464dfa4f2e9d75521715f577a7c2e589e165f1a4852"
TAG = "`dyad-v6.4.20`"


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode()).hexdigest()


def header(base):
    m = re.search(r"^\*\*Status summary:\*\* (.*?)  $", base, re.M)
    summary = m.group(1)
    # keep the scientific summary; drop the two v6.4.20 release sentences (history)
    cut = summary.index(" v6.4.20 adds the ATLAS P1")
    summary = summary[:cut]
    scope = re.search(r"^\*\*Scope:\*\* (.*?)  $", base, re.M).group(1)
    return (
        "# RTG_DYADIC_OSCILLATOR_DSN_v6.4.21\n\n"
        "**Title:** RTG Dyadic Oscillator Study — Canonical Scientific Ledger  \n"
        "**Date:** 22 October 2026  \n"
        f"**Scope:** {scope}  \n"
        "**Document class:** Technical scientific ledger (Methodology v1.4 §0.5). §1 profile exception: §1 gives RID-level readouts of the certified results with their load-bearing qualifications (about 1,500 words); a pointer-only list would drop those qualifications (Methodology v1.4 §1.1 item 3).  \n"
        "**Document status:** DRAFT — v6.4.21 candidate (closeout errata and Methodology v1.4 compaction pilot); not adopted.  \n"
        f"**Supersedes:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.20` (SHA-256 `{V6420_SHA}`; tag {TAG}).  \n"
        "**Companion documents:** one current-edition table, §7.0.  \n"
        "**DSN Methodology:** v1.4 (tag `methodology-v1.4`).  \n"
        "**Programme tier:** Tier 3 — Continuous Programme, upstream source (Programme Overview §6).  \n"
        f"**Status summary:** {summary}  \n"
        "**Release record:** `records/dyad/RTG_DYADIC_v6_4_21_RELEASE_RECORD.md`. Version history: Appendix A.\n"
    )


FOOTER = "*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.21 (DRAFT candidate, 22 October 2026).*\n"


def appendix_a(base):
    i = base.index("## Appendix A — Version History"); j = base.index("## Appendix B —")
    old = base[i:j]
    heads = re.findall(r"^### (v[0-9.]+ — .*)$", old, re.M)
    adopted = [h for h in heads if not re.search(r"DRAFT|draft record|working record", h, re.I)]
    older = [h for h in adopted if not h.startswith("v6.4.20")]
    lines = "\n".join(f"- {h}" for h in older)
    return (
        "\n## Appendix A — Version History {#appendix-a}\n\n"
        "One compact entry per edition (Methodology v1.4 §1). Full records of earlier editions — adoption metadata, draft-round records, review verdicts, replaced lines and every `[COR]` entry — are in Appendix A of v6.4.20 (tag `dyad-v6.4.20`, SHA-256 `0b2d5a44…4852`). Scientific corrections, retractions and regrades are also recorded in Appendix B.\n\n"
        "### v6.4.21 — 22 October 2026 — DRAFT candidate\n\n"
        "- **Errata [status/scope/provenance] (closeout S-1–S-6; targeted review R21-01):** current status at the point of use for OPEN 3 (CLOSED within scope), P4, OPEN 21, RECOG R11 and the P2B v2 coefficient verification (§1, §2, §5, §6.14, §8); closed OPEN 9 items moved out of the active list; N11 recorded as adopted use by RECOG (§7 notices); subclaim dependencies of DYAD-ALG-OPEN3-PHASE-OFFSET (§7); notation overloads (Appendix C); DYAD-THM-RAW-CUBIC provenance caveat and its range $p\\ge3$ (§2, Appendix F); unrecovered OPEN 9 definitions named at the point of use (§6.11). Scope tag of the primitive-variable form in §6.14 now points to OPEN 21. Field label of the archival $h_4$ corrected from $\\mathbb Q(\\sqrt3)$ to $\\mathbb Q(i\\sqrt3)$, confirmed by exact recomputation (§1, §8). RECOG R11 stated as CLOSED where the fitted-backbone identification stays open (§1, §6.5). No grade changes; no new RID.\n"
        "- **FC-DYAD-34 [bookkeeping]:** squared shear/healing ratio equals Genesis's leading ratio $16/3$ (§6.12); selects no birth policy.\n"
        "- **Compaction [layout] (Methodology v1.4 pilot):** current-only header with the §1 profile exception; one footer; this compact Appendix A; tag normalization map and the v6.4.19→v6.4.20 section map left in v6.4.20; history pointers in live text removed or repointed to the tagged edition.\n"
        "- **Records:** release record `records/dyad/RTG_DYADIC_v6_4_21_RELEASE_RECORD.md`; corrected intermediate SHA-256 `f2b20419…9119`; predecessor tag `dyad-v6.4.20`.\n\n"
        "### v6.4.20 — 21 October 2026 — Adopted\n\n"
        "- **Content:** ATLAS P1 scientific corrections and P2 interface work. 13 RIDs registered at adoption: `DYAD-ALG-KP-FRAME-SCALE`, `DYAD-THM-SMOOTH-EQUIVARIANT-CHART`, `DYAD-ALG-B5-ALLP-NONVANISHING`, `DYAD-ALG-RAW-ANGULAR-MEAN`, `DYAD-ALG-ONE-BLOCK-BURST`, `DYAD-ALG-P5-RADIAL`, `DYAD-ALG-SIXSTEP-CUBIC-JET`, `DYAD-ALG-Q3-DEG2-CANCEL`, `DYAD-DEF-CRITICAL-CURVE`, `DYAD-ALG-QC-CRITICAL-AMPLITUDE`, `DYAD-ALG-ISP-MAPS`, `DYAD-ART-ATLAS-P1`, `DYAD-ART-ATLAS-P2`. No earlier RID renamed or regraded.\n"
        "- **Grade corrections to unnumbered statements (P1):** §6.5 historical backbone ansatz `[ALG]`→`[DEF]`; §6.6 $p=6$ linear order `[THM]`→`[ALG]`; §6.6 classification by $p$ `[THM]`→`[DEF]`. The v6.4.20 footer described the r2→final step as metadata only; that was true of r2→final, while these P1 retaggings were made earlier in the cycle.\n"
        "- **Records:** `records/dyad/RTG_DYADIC_v6_4_20_RELEASE_RECORD.md`; adoption, draft-round records and the 55 replaced lines: Appendix A of v6.4.20 (tag `dyad-v6.4.20`).\n\n"
        "### Earlier editions\n\n"
        f"{lines}\n\n"
        "---\n"
    )


def ops_for(base):
    ops = []

    def edit(i, cls, old, new, note=""):
        ops.append({"id": i, "op": "edit", "class": cls, "old": old, "new": new,
                    "archive": ["dyad-v6.4.20"], "note": note})

    ops.append({"id": "M01", "op": "replace-header", "class": "presentation", "new": header(base),
                "archive": ["dyad-v6.4.20"], "note": "current-only header; §1 profile exception (E-1); Supersedes = v6.4.20 + hash"})
    edit("M02", "ref-subst",
         "Legacy compound spellings in live text are rendered by the normalization map below;",
         "Legacy compound spellings in live text are rendered by the tag normalization map of v6.4.20 (tag `dyad-v6.4.20`, Local Tag Aliases);")
    ops.append({"id": "M03", "op": "replace-section", "class": "history-section", "tag_examples": True,
                "region": "R1", "start": "**Tag normalization map (v6.4.20).**", "end": "**Section headings.**", "new": "",
                "archive": ["dyad-v6.4.20"], "note": "legacy-spelling map (v6.4.19 → v6.4.20); claim tags appear only as spelling examples"})
    edit("M04", "ref-subst",
         "| retired identifiers; promoted in v6.2 to `DYAD-ALG-VANISH-B3`, `DYAD-ALG-VANISH-B4` `[ALG]` | Appendix A, v6.2 |",
         "| retired identifiers; promoted in v6.2 to `DYAD-ALG-VANISH-B3`, `DYAD-ALG-VANISH-B4` `[ALG]` | Appendix A of v6.4.20 (tag `dyad-v6.4.20`), v6.2 |")
    edit("M05", "history-removal",
         "used when no downstream handoff is specified. `[v6.4.20]` Rebuilt from live items only; the former list (items 0–5, including the closed items 1, 4 and 4b) is relocated verbatim to Appendix A (H-4).",
         "used when no downstream handoff is specified.")
    edit("M06", "history-removal",
         "are not violations. (v6.4.19 text: Appendix A H-6.)", "are not violations.")
    edit("M07", "ref-subst",
         "SG-17 and SG-18 do not occur in this ledger or in its Appendix A history;",
         "SG-17 and SG-18 do not occur in this ledger or in its version history (tag `dyad-v6.4.20`, Appendix A);")
    edit("M08", "ref-subst",
         "Its historical occurrence and evidence are preserved (Appendix A).",
         "Its historical occurrence and evidence are preserved (Appendix A of v6.4.20, tag `dyad-v6.4.20`).")
    edit("M09", "ref-subst",
         "it is withdrawn (Appendix A H-7).",
         "it is withdrawn (v6.4.20 Appendix A H-7, tag `dyad-v6.4.20`).")
    edit("M10", "ref-subst",
         "consolidates the v6.4.14–v6.4.16 lists relocated to Appendix A H-2):**",
         "consolidates the v6.4.14–v6.4.16 lists in v6.4.20 Appendix A H-2, tag `dyad-v6.4.20`):**")
    edit("M11", "ref-subst",
         "*`[v6.4.20]` v6.4.15 \"Not established\" list relocated to Appendix A H-2;",
         "*`[v6.4.20]` v6.4.15 \"Not established\" list in v6.4.20 Appendix A H-2 (tag `dyad-v6.4.20`);")
    edit("M12", "ref-subst",
         "*`[v6.4.20]` v6.4.16 \"Not established\" list relocated to Appendix A H-2;",
         "*`[v6.4.20]` v6.4.16 \"Not established\" list in v6.4.20 Appendix A H-2 (tag `dyad-v6.4.20`);")
    edit("M13", "history-removal",
         "existence is DYAD-THM-SMOOTH-EMBEDDING (§6.17). `[v6.4.20]` (v6.4.12/v6.4.13 wording: Appendix A H-9.)",
         "existence is DYAD-THM-SMOOTH-EMBEDDING (§6.17).")
    edit("M14", "ref-subst",
         "*`[v6.4.20]` v6.4.17 \"Not established\" list relocated to Appendix A H-3;",
         "*`[v6.4.20]` v6.4.17 \"Not established\" list in v6.4.20 Appendix A H-3 (tag `dyad-v6.4.20`);")
    edit("M15", "history-removal",
         "(§6.2, §6.11, §6.12, SG-15). (v6.4.19 paragraph: Appendix A H-5.)",
         "(§6.2, §6.11, §6.12, SG-15).")
    ops.append({"id": "M18", "op": "replace-section", "class": "history-section", "navigation": True, "region": "R2",
                "start": "\n## Appendix G — Old→new section map {#appendix-g}", "end": "\n---\n\n*END OF DOCUMENT",
                "new": "\n## Appendix G — Old→new section map {#appendix-g}\n\nThe v6.4.19→v6.4.20 section map is Appendix G of v6.4.20 (tag `dyad-v6.4.20`). v6.4.21 keeps every heading anchor of v6.4.20.\n",
                "archive": ["dyad-v6.4.20"], "note": "navigation history of the previous release"})
    ops.append({"id": "M16", "op": "replace-section", "class": "history-appendix",
                "start": "\n## Appendix A — Version History {#appendix-a}", "end": "\n## Appendix B —",
                "new": appendix_a(base), "archive": ["dyad-v6.4.20"],
                "note": "E-2: draft-round records, adoption records, replaced lines and pre-v6.4.20 entries left in v6.4.20; compact entries"})
    edit("M17", "ref-subst",
         "See COR items in Appendix A v6.4.10.",
         "See the v6.4.10 COR items in Appendix A of v6.4.20 (tag `dyad-v6.4.20`).")
    ops.append({"id": "M19", "op": "replace-footer", "class": "presentation", "new": FOOTER,
                "archive": ["dyad-v6.4.20"], "note": "one footer (E-1)"})
    return ops


def apply(base, ops):
    s = base
    for op in ops:
        if op["op"] == "edit":
            assert s.count(op["old"]) == 1, op["id"]
            s = s.replace(op["old"], op["new"])
        elif op["op"] == "replace-section":
            i = s.index(op["start"]); j = s.index(op["end"], i + len(op["start"]))
            assert s.count(op["start"]) == 1, op["id"]
            s = s[:i] + op["new"] + s[j:]
        elif op["op"] == "replace-header":
            i = s.index("\n## ")
            s = op["new"] + s[i:]
        elif op["op"] == "replace-footer":
            lines = s.split("\n")
            k = next(n for n, l in enumerate(lines) if l.startswith("*END OF DOCUMENT"))
            s = "\n".join(lines[:k]) + "\n" + op["new"]
    return s


def main(inter, prev, out, mapout):
    b = open(inter, "rb").read(); p = open(prev, "rb").read()
    assert sha(b) == INTERMEDIATE_SHA and sha(p) == V6420_SHA
    base = b.decode()
    ops = ops_for(base)
    cand = apply(base, ops).encode()
    open(out, "wb").write(cand)
    mp = {"study": "DYAD", "target": "v6.4.21", "stage": "compaction",
          "base": "corrected intermediate (stage 1)", "base_sha256": sha(b),
          "candidate_sha256": sha(cand),
          "archives": [{"name": "dyad-v6.4.20", "git": "dyad-v6.4.20:dsn/RTG_DYADIC_OSCILLATOR_DSN.md", "sha256": V6420_SHA}],
          "operations": ops}
    json.dump(mp, open(mapout, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(sha(cand), len(cand), "bytes;", len(ops), "operations")


if __name__ == "__main__":
    main(*sys.argv[1:5])
