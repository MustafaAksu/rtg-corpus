#!/usr/bin/env python3
# =============================================================================
# NUMBER GENESIS v1.20.3 MIGRATION ENGINE  v1   (methodology-only, option B)
# =============================================================================
# Inputs  : RTG_NUMBER_GENESIS_DSN_v1_20_2.md (frozen base), the APPROVED
#           per-block inventory NG_V1203_REVERSE_INVENTORY_v2.json and the
#           hierarchical inventory NG_V1203_HIER_INVENTORY_v1.json.
# Output  : a document with batches <= K applied (K = 0..11). Pure relocation:
#           no line of scientific text is created, reworded or dropped except
#           (a) the approved MIRROR-RECONCILED §2 ORD-4 copy, removed;
#           (b) the 3 approved REGISTRY-ONLY status lines, moved verbatim onto
#               <!-- REGISTRY --> rows;
#           (c) structural additions: the approved §6.9a heading, the §2 module
#               registry rows, and — final build only — header/changelog.
# Headings of moved modules are demoted one level (cap 6).
# =============================================================================
import io, re, json, sys, hashlib

BASE = "RTG_NUMBER_GENESIS_DSN_v1_20_2.md"
L = io.open(BASE, encoding="utf-8").read().split("\n")
INV = json.load(open("NG_V1203_REVERSE_INVENTORY_v2.json"))["blocks"]
HIER = json.load(open("NG_V1203_HIER_INVENTORY_v1.json"))
ORDER = HIER["batch_order"]
NEWH = "§6.9a NG-10 — Genesis saturation and counting truncation"

def lvl2(prefix): return next(i + 1 for i, l in enumerate(L) if l.startswith("## " + prefix))
S2, S3, S6, S7 = lvl2("§2"), lvl2("§3"), lvl2("§6"), lvl2("§7")

REG_STATUS = {x["line"]: x for x in INV if x["disposition"] == "REGISTRY-ONLY" and x.get("status_header")}
MIRROR = [x for x in INV if x["disposition"] == "MIRROR-RECONCILED"]
FPB = {b["line"]: b for b in json.load(open("fp1202.json"))["blocks"]}
MIRROR_LINES = set()
for x in MIRROR:
    b = FPB[x["line"]]
    MIRROR_LINES |= set(range(b["line"], b["end"] + 1))   # 1-based inclusive block span

def demote(l):
    m = re.match(r"(#{3,6}) ", l)
    return ("#" * min(len(m.group(1)) + 1, 6)) + l[len(m.group(1)):] if m else l

def module_lines(r, removed_reg):
    out = []
    for n in range(r["start"], r["end"]):
        if n in MIRROR_LINES: continue
        if n in REG_STATUS:
            removed_reg.append(n); continue
        out.append(demote(L[n - 1]))
    while out and not out[-1].strip(): out.pop()
    return out

def sub_heading_of(n):
    for k in range(n - 1, S2 - 1, -1):
        m = re.match(r"(#{3,6}) (.*)", L[k - 1])
        if m: return m.group(2).strip()
    return "?"

def build(K, final=False):
    done = set(ORDER[:K])
    mods = HIER["modules"]
    moved = [r for r in mods if r["batch"] in done]
    stay = [r for r in mods if r not in moved]
    removed_reg = []; per_dest = {}
    for r in moved:
        per_dest.setdefault(r["destination"], []).append(module_lines(r, removed_reg))
    # ---- new §2 ---------------------------------------------------------
    first = mods[0]["start"]
    sec2 = L[S2 - 1:first - 1]
    queue = stay[0]; assert queue["module"].startswith("Priority ordering")
    q = L[queue["start"] - 1:queue["end"] - 1]
    while q and not q[-1].strip(): q.pop()
    sec2 += q + [""]
    if moved:
        sec2 += ["### Module registry (v1.20.3 structural migration)", "",
                 "<!-- REGISTRY --> Structural pointer rows. The authoritative scientific bodies of these modules live in §6; statuses below are verbatim relocations.", ""]
        for r in moved:
            sec2.append(f"<!-- REGISTRY --> - **{r['module']}** → §6: {r['destination']}")
        for n in sorted(removed_reg):
            sec2.append(f"<!-- REGISTRY --> - sub-module status — **{sub_heading_of(n)}**:")
            sec2.append("<!-- REGISTRY --> " + L[n - 1].strip())
        sec2.append("")
    for r in stay[1:]:
        blk = L[r["start"] - 1:r["end"] - 1]
        sec2 += blk
    while sec2 and not sec2[-1].strip(): sec2.pop()
    sec2.append("")
    # ---- new §6 ---------------------------------------------------------
    sec6 = []; body = L[S6 - 1:S7 - 1]
    heads = [i for i, l in enumerate(body) if re.match(r"### ", l)] + [len(body)]
    sec6 += body[:heads[0]]
    for a, b in zip(heads, heads[1:]):
        chunk = body[a:b]
        while chunk and not chunk[-1].strip(): chunk.pop()
        title = re.sub(r"\s+", " ", chunk[0][4:].strip())
        sec6 += chunk
        for ml in per_dest.get(title, []): sec6 += [""] + ml
        sec6.append("")
        if title.startswith("§6.9 ") and NEWH in per_dest:
            sec6 += ["### " + NEWH, ""]
            for ml in per_dest[NEWH]: sec6 += ml + [""]
    doc = L[:S2 - 1] + sec2 + L[S3 - 1:S6 - 1] + sec6 + L[S7 - 1:]
    if final:
        doc = finalize(doc)
    return "\n".join(doc), sorted(removed_reg)

def finalize(doc):
    s = "\n".join(doc)
    def rep(o, n):
        nonlocal s
        assert s.count(o) == 1, o[:60]; s = s.replace(o, n)
    rep("# RTG Number Genesis DSN v1.20.2", "# RTG Number Genesis DSN v1.20.3")
    rep("**Document status:** ACTIVE owner ledger; scientific-sync patch. **Supersedes:** v1.20.1 (`00174c3a…c927b`), which superseded v1.20 (`f5ed40f5…3b636`).  ",
        "**Document status:** ACTIVE owner ledger; **methodology-only structural migration — scientific state identical to v1.20.2.** **Supersedes:** v1.20.2 (`35fe1a65…dd1053`).  ")
    rep("**DSN Methodology:** v1.3 (touched-block compliance in this release; full structural migration deferred to a methodology-only pass).  ",
        "**DSN Methodology:** v1.3; §2/§6 structural migration completed in this methodology-only release; scientific state unchanged from v1.20.2.  ")
    rep("## Changelog\n### v1.20.2 — September 25, 2026", """## Changelog
### v1.20.3 — September 25, 2026

**Methodology-only structural migration (option B, module-level). Scientific state identical to v1.20.2.**

- §2 reduced to the section heading, the unchanged Priority-ordering queue, and a module registry of structural pointer rows. All 18 §2 modules relocated verbatim, as whole modules (set-up, definitions, guards, theorems, OPEN/HOLD residuals, unanchored lines), to their §6 homes, in original order, after the existing §6 content; module headings demoted one level. The single level-6 heading (L1) is capped at level 6 as a Markdown rendering exception only; its semantic parent remains N-1C-DYAD (no re-parenting).
- Approved per-block dispositions applied unchanged: 114 MOVE; 4 REGISTRY-ONLY (queue in place; 3 bare status lines relocated verbatim onto registry rows); 1 MIRROR-RECONCILED (§2 ORD-4 copy removed, §6.3a twin retained); 0 STOP.
- New structural heading §6.9a NG-10 (approved). Co-owner approved structural mappings: N-4 → §6.5, N-6 → §6.7, NG-9 → §6.10.
- Gates: FP-v2.3 no loss / no invention / identifier conservation (incl. derived HEADING-DEMOTION for the one heading-anchored block); INV-S final; INV-P post-write; INV-LIVE; §2 and §8 queues byte-identical to v1.20.2.
- Textual pointers: a scan of the relocated bodies found no "§2 …" cross-references, so no pointer rewording was needed or performed.

### v1.20.2 — September 25, 2026""")
    return s.split("\n")

if __name__ == "__main__":
    K = int(sys.argv[1]); final = len(sys.argv) > 2 and sys.argv[2] == "final"
    text, reg = build(K, final)
    out = sys.argv[3] if len(sys.argv) > 3 else f"/tmp/mig_{K}.md"
    io.open(out, "w", encoding="utf-8").write(text)
    print(out, "registry-converted status lines:", reg)
