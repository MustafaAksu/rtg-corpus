#!/usr/bin/env python3
"""recog_g2_dyad_passage_diff.py  v0.3  --  G2 source-fidelity helper (RECOG v0.3.21 sync audit)

Compares the Dyadic owner claim blocks imported by RECOG v0.3.20 across editions
(pinned v6.4.10, verified v6.4.16, reported v6.4.17).

Three separate results
----------------------
* ANCHORS_FOUND      every anchor of a passage occurs in every edition (each anchor is
                     checked separately; a missing anchor or file fails closed, exit 2).
* PASSAGE_IDENTICAL  the selected claim BLOCKS agree after whitespace normalization
                     (default), or byte-for-byte with --bytes (then reported as
                     BYTE_IDENTICAL).
* CLAIM_EQUIVALENT   NOT decided by this script.  It is the reviewer's field-by-field
                     verdict (statement, hypotheses, domain/rows, chart, constants,
                     grade, evidence), recorded in the audit record.

Block selection
---------------
A block is a maximal run of non-blank lines.  For every anchor, every block containing
it is selected (so a change anywhere in that paragraph or table is detected, not only
on the anchor line).  The block immediately after a selected one is added when it is a
display equation or a table (starts with "$$" or "|"), and --extend K adds K further
blocks after each hit, for theorems whose hypotheses, display and conclusion sit in
separate paragraphs.  For EVERY file the report prints the source line range of every
selected block (L<start>-<end>, with its first characters), so the reviewer can see
whether the operative statement is covered or only a citation of it, and can adjust the
anchors or --extend accordingly.  Text outside the selected blocks is not compared.

Usage (PowerShell, env RTG):
  python recog_g2_dyad_passage_diff.py RTG_DYADIC_OSCILLATOR_DSN_v6_4_10.md `
      RTG_DYADIC_OSCILLATOR_DSN_v6_4_16.md RTG_DYADIC_OSCILLATOR_DSN_v6_4_17.md `
      [--extend K] [--bytes] > g2_dyad_passage_diff.txt
Exit codes: 0 all anchors found and all passages identical; 1 all anchors found, at
least one passage differs (inspect the diffs); 2 a file or an anchor is missing.
"""
import sys, re, hashlib, difflib, argparse

PASSAGES = {
    "C21":           ["DYAD-THM-C21]", "**Cubic coefficient:**"],
    "NF6":           ["[RID: DYAD-ALG-NF6]"],
    "NF6-OBS":       ["[RID: DYAD-ALG-NF6-OBS]"],
    "PRIM-CTR":      ["[RID: DYAD-THM-PRIM-CTR]"],
    "NF-INV":        ["[RID: DYAD-THM-NF-INV]"],
    "NF-REM":        ["[RID: DYAD-THM-NF-REM]", "certificate value $85.07$"],
    "BRIDGE-LEMMA":  ["One-step to $p$-step bridge lemma"],
    "P6-FACEFLUX":   ["`[RID: DYAD-ALG-P6-FACEFLUX]` **K"],
    "ALIAS-PHASE":   ["**OPEN 16 partial.**"],
    "LIEGAUGE-NORM": ["c_{32}^{({\\rm raw},6\\text{-step})}=", "c_\\theta^{(6)}=-119\\sqrt{3}/648$."],
    "MAP-6.1":       ["**Jacobian:**", "**Critical curve:**", "**$P_2$ saddle:**"],
    "ISP-6.4":       ["**Critical ISP amplitude:**", "**Winding-index invisibility.**"],
    "JET-6.7-6.8":   ["M+M^T=-I", "**Cubic-vector truncation only.**"],
    "CONST-6.3":     ["R^*=\\exp(\\pi/\\tau)"],
    "H2-6.2":        ["**Quadratic near-identity correction:**"],
    "NU5-1-6":       ["$p=6$: $c_{05}^{(1,6)}"],
    "47/54-6.5":     ["**Raw angular-mean recurrence coefficient.**"],
    "OPEN12":        ["[RID: DYAD-OPEN-P2-SADDLE]"],
}

def load(path):
    try:
        with open(path, "rb") as f:
            raw = f.read()
    except OSError as e:
        print(f"MISSING FILE {path}: {e}"); sys.exit(2)
    return hashlib.sha256(raw).hexdigest(), raw.decode("utf-8").splitlines()

def blocks(lines):
    """Maximal runs of non-blank lines, as (start, end, lines) with 1-based inclusive line numbers."""
    out, cur, start = [], [], None
    for i, ln in enumerate(lines, 1):
        if ln.strip():
            if not cur:
                start = i
            cur.append(ln)
        elif cur:
            out.append((start, i - 1, cur)); cur = []
    if cur:
        out.append((start, len(lines), cur))
    return out

def norm(block_lines, raw):
    return list(block_lines) if raw else [re.sub(r"\s+", " ", l).strip() for l in block_lines]

def select(bl, anchor, extend):
    sel = set()
    for i, (_, _, b) in enumerate(bl):
        if any(anchor in l for l in b):
            sel.add(i)
            j = i + 1
            if j < len(bl) and bl[j][2][0].lstrip().startswith(("$$", "|")):
                sel.add(j); j += 1
            for k in range(extend):
                if j + k < len(bl):
                    sel.add(j + k)
    return sel

def main():
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--extend", type=int, default=0)
    ap.add_argument("--bytes", action="store_true")
    a = ap.parse_args()
    if len(a.files) < 2:
        print(__doc__); sys.exit(2)
    docs = [(p,) + load(p) for p in a.files]
    for p, h, _ in docs:
        print(f"FILE {p}  sha256 {h}")
    print(f"MODE {'byte' if a.bytes else 'whitespace-normalized'} comparison; --extend {a.extend}")
    status = 0
    label = "BYTE_IDENTICAL" if a.bytes else "PASSAGE_IDENTICAL"
    for key, anchors in PASSAGES.items():
        print(f"\n=== {key} ===")
        per_doc = []
        for p, _, lines in docs:
            bl = blocks(lines)
            idx = set()
            for anc in anchors:
                s = select(bl, anc, a.extend)
                if not s:
                    print(f"  ANCHOR MISSING in {p}: {anc!r}"); status = 2
                idx |= s
            chosen = [bl[i] for i in sorted(idx)]
            print(f"  {p}: blocks={len(chosen)} lines={sum(len(b) for _, _, b in chosen)}")
            for s, e, b in chosen:
                print(f"    L{s}-{e}: {b[0].strip()[:90]}")
            per_doc.append([norm(b, a.bytes) for _, _, b in chosen])
        print(f"  ANCHORS_FOUND={'NO' if status == 2 else 'YES'}")
        flat0 = [l for b in per_doc[0] for l in b]
        for (p, _, _), sel in zip(docs[1:], per_doc[1:]):
            flat = [l for b in sel for l in b]
            if flat == flat0:
                print(f"  {p}: {label}")
            else:
                if status == 0:
                    status = 1
                print(f"  {p}: PASSAGE_DIFFERS")
                for d in difflib.unified_diff(flat0, flat, docs[0][0], p, lineterm="", n=0):
                    print("    " + d[:600])
    print("\nCLAIM_EQUIVALENT: not decided by this script (reviewer verdict, field by field).")
    sys.exit(status)

if __name__ == "__main__":
    main()
