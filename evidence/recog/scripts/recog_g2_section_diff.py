#!/usr/bin/env python3
"""recog_g2_section_diff.py  v0.1.1  --  G2 source-fidelity helper for Genesis, OFN and RRF

Compares the owner passages imported by RECOG v0.3.20 between a pinned and a current
edition.  Two unit kinds:
  * SECTION  -- from a heading line that starts with the given text to the next heading of
               the same or a higher level (complete section, no anchor guessing);
  * ENTRY    -- an OPEN-registry entry: from the line containing the anchor to the line
               before the next line starting with "**OPEN-" or a heading;
  * BLOCK    -- every maximal run of non-blank lines containing the anchor, plus the next
               block when it is a display ($$) or a table (|).
For every unit the report prints the source line range in each file.  Comparison is exact
on the selected lines (default) or whitespace-normalized (--norm).  A missing file or unit
fails closed (exit 2); any difference gives exit 1; all identical gives exit 0.
CLAIM_EQUIVALENT is never decided here: it is the reviewer's field-by-field verdict.

Usage:  python recog_g2_section_diff.py {genesis|ofn|rrf} PINNED.md CURRENT.md [--norm]
"""
import sys, re, hashlib, difflib

SPECS = {
  "genesis": [
    ("G1 zero origin / first dyad", "BLOCK", "**Zero-origin condition.**"),
    ("G1b first dyad", "BLOCK", "**First dyad.**"),
    ("G2 metric B, Q", "BLOCK", "**Quadratic form:**"),
    ("G3 A^T B A = B", "BLOCK", "$A^\\top BA = B$."),
    ("G4 phase variables", "BLOCK", "**Phase variables.**"),
    ("G5 plateau shear bridge", "BLOCK", "**Plateau shear bridge.**"),
    ("G6 J_Q identity", "BLOCK", "J_Q = \\tfrac{1}{\\sqrt{3}}\\begin{pmatrix}1 & -2"),
    ("G7 J_Q convention", "BLOCK", "`[CONVENTION]` (v2.7.3)"),
    ("G8 section 6.1 (whole)", "SECTION", "### §6.1 Primitive State and Generator"),
    ("G9 section 6.6 (whole)", "SECTION", "### §6.6 Phase Bridge and Cascade Condition"),
  ],
  "ofn": [
    ("O1 section 6.2a (whole)", "SECTION", "### 6.2a Minimal Constraint List for T"),
    ("O2 section 7.3 (whole)", "SECTION", "### 7.3 Antipodal Band and Width Parameter"),
    ("O3 OPEN-OFN-OPA (whole entry)", "ENTRY", "**OPEN-OFN-OPA — Orientation physicality**"),
  ],
  "rrf": [
    ("R1 profile RRF-NET-W-RAW (whole)", "SECTION", "## 2.5 `RRF-NET-W-RAW`"),
    ("R2 T-net bridge row", "BLOCK", "| `T-net` |"),
    ("R3 dependency lock (whole section 6)", "SECTION", "# 6. Dependency lock"),
    ("R4 not registered (whole)", "SECTION", "# 7. Not registered"),
    ("R5 RRF-DYAD-W profile (S_h)", "SECTION", "## 2.3 `RRF-DYAD-W`"),
    ("R6 RRF-DYAD-NF profile (common realisation)", "SECTION", "## 2.4 `RRF-DYAD-NF`"),
    ("R7 comparator typing", "SECTION", "## 4.1 Comparator typing"),
    ("R8 pole-relabeling actions", "SECTION", "## 4.2 Pole-relabeling candidate actions"),
  ],
}

def load(p):
    try:
        raw = open(p, "rb").read()
    except OSError as e:
        print(f"MISSING FILE {p}: {e}"); sys.exit(2)
    return hashlib.sha256(raw).hexdigest(), raw.decode("utf-8").splitlines()

def level(line):
    m = re.match(r"^(#{1,6}) ", line)
    return len(m.group(1)) if m else None

def section(lines, head):
    for i, l in enumerate(lines):
        if l.startswith(head):
            lv = level(l)
            j = i + 1
            while j < len(lines):
                lj = level(lines[j])
                if lj is not None and lj <= lv:
                    break
                j += 1
            return [(i + 1, j, lines[i:j])]
    return []

def entry(lines, anchor):
    for i, l in enumerate(lines):
        if anchor in l:
            j = i + 1
            while j < len(lines) and not lines[j].startswith("**OPEN-") and level(lines[j]) is None:
                j += 1
            return [(i + 1, j, lines[i:j])]
    return []

def blocks(lines):
    out, cur, s = [], [], None
    for i, l in enumerate(lines, 1):
        if l.strip():
            if not cur: s = i
            cur.append(l)
        elif cur:
            out.append((s, i - 1, cur)); cur = []
    if cur: out.append((s, len(lines), cur))
    return out

def block_units(lines, anchor):
    bl = blocks(lines); sel = set()
    for k, (_, _, b) in enumerate(bl):
        if any(anchor in l for l in b):
            sel.add(k)
            if k + 1 < len(bl) and bl[k + 1][2][0].lstrip().startswith(("$$", "|")):
                sel.add(k + 1)
    return [bl[k] for k in sorted(sel)]

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    norm = "--norm" in sys.argv
    if len(args) != 3 or args[0] not in SPECS:
        print(__doc__); sys.exit(2)
    owner, pa, pb = args
    (ha, la), (hb, lb) = load(pa), load(pb)
    print(f"OWNER {owner}\nFILE {pa}  sha256 {ha}\nFILE {pb}  sha256 {hb}")
    print(f"MODE {'whitespace-normalized' if norm else 'exact selected lines'}")
    status = 0
    for name, kind, key in SPECS[owner]:
        get = {"SECTION": section, "ENTRY": entry, "BLOCK": block_units}[kind]
        ua, ub = get(la, key), get(lb, key)
        print(f"\n=== {name} [{kind}] ===")
        if not ua or not ub:
            print(f"  UNIT MISSING in {'pinned' if not ua else 'current'}"); status = 2; continue
        for tag, us in (("pinned", ua), ("current", ub)):
            print(f"  {tag}: " + ", ".join(f"L{s}-{e}" for s, e, _ in us))
        f = (lambda L: [re.sub(r"\s+", " ", x).strip() for x in L]) if norm else (lambda L: list(L))
        A = [x for _, _, b in ua for x in f(b)]; B = [x for _, _, b in ub for x in f(b)]
        if A == B:
            print("  IDENTICAL")
        else:
            if status == 0: status = 1
            print("  DIFFERS")
            for d in difflib.unified_diff(A, B, "pinned", "current", lineterm="", n=0):
                print("    " + d[:500])
    print("\nCLAIM_EQUIVALENT: not decided by this script (reviewer verdict).")
    sys.exit(status)

if __name__ == "__main__":
    main()
