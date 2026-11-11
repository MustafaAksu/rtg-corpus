#!/usr/bin/env python3
"""recog_ra1_cprime_recheck.py -- Atlas re-check for RECOG.R-A1 (pipes/RECOG/20261030-DYAD-v6-4-23-adopted.md).

Question: do the A1c certificates of recog-v0.3.26 still pass when the (D5) row-A bridge constant c'_Q is taken at the
value Dyadic registered in DYAD-THM-LPHASE-ROWA-BRIDGE (dyad-v6.4.23: c'_Q = 0.36916; certified majorant 0.3691523046...)
instead of the value RECOG assumed (0.36915, below the majorant)?

The constant has one literal site in the chain: recog_a1c_tail_averaging_cert.py L55 (`I("0.36915")`). Every other
A1c certificate imports it from there (start_offset, unknown_a_interval, inblock_angular, joint_transfer directly;
drift_centering and drift_proof_table through start_offset; combined_tail through inblock_angular).

  run OUTDIR       builds OUTDIR/orig and OUTDIR/patch, each a copy of the eight registered A1c scripts in the
                   repository layout (scripts/ next to a1c_*/), patches L55 in `patch` (asserted exactly once),
                   runs the chain in dependency order in both trees, then runs `compare`.
                   Part 1b is run with its committed orbit length (6,000,000 steps, argv[2]).
                   Wall time on the Atlas host: about 55 minutes per tree (joint transfer about 28 minutes).
  compare OUTDIR   compares (a) committed outputs vs `orig` byte for byte (reproduction check) and (b) `orig` vs
                   `patch`: every gate, every boolean, the largest relative change of every numeric leaf.
                   Writes OUTDIR/ra1_recheck_summary.json and prints a short report.

Atlas evidence, NONCANONICAL. It reruns owner certificates with one changed input; it does not re-prove them, and it
does not decide whether RECOG drops `[assuming: (D5)]` (RECOG's decision).
usage (repository root): python -I evidence/recog/atlas_review/ra1/recog_ra1_cprime_recheck.py run OUTDIR
                         python -I evidence/recog/atlas_review/ra1/recog_ra1_cprime_recheck.py compare OUTDIR
"""
import hashlib, json, os, shutil, subprocess, sys, time

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))
EV = os.path.join(ROOT, "evidence", "recog")

# (script, output dir, output JSON, extra argv) in dependency order. Before any run, each script's SHA-256 is checked
# against the hash printed in the RECOG DSN artifact rows (RECOG-ART-A1C-SHARPENED-SCHEDULE, -DECODER, -DRIFT-CENTERING).
CHAIN = [
    ("recog_a1c_tail_averaging_cert.py",     "a1c_1b",      "a1c_tail_averaging_cert.json",     ["6000000"]),
    ("recog_a1c_start_offset_cert.py",       "a1c_so",      "a1c_start_offset_cert.json",       []),
    ("recog_a1c_unknown_a_interval_cert.py", "a1c_2",       "a1c_unknown_a_interval_cert.json", []),
    ("recog_a1c_inblock_angular_cert.py",    "a1c_inblock", "a1c_inblock_angular_cert.json",    []),
    ("recog_a1c_combined_tail_cert.py",      "a1c_comb",    "a1c_combined_tail_cert.json",      []),
    ("recog_a1c_joint_transfer_cert.py",     "a1c_joint",   "a1c_joint_transfer_cert.json",     []),
    ("recog_a1c_drift_centering_cert.py",    "a1c_drift",   "a1c_drift_centering_cert.json",    []),
    ("recog_a1c_drift_proof_table_cert.py",  "a1c_drift",   "a1c_drift_proof_table_cert.json",  []),
]
SITE = "recog_a1c_tail_averaging_cert.py"
OLD, NEW = 'I("0.36915")', 'I("0.36916")'

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def registered_hashes():
    """Script hashes as printed in the RECOG DSN artifact rows (lines naming recog_a1c_*_cert.py with a sha256)."""
    import re
    txt = open(os.path.join(ROOT, "dsn", "RTG_RELATIONAL_RECOGNITION_DSN.md"), encoding="utf-8").read()
    reg = {}
    for s, h in re.findall(r"`(recog_a1c_[a-z_]+_cert\.py)` \((?:sha256 )?`([0-9a-f]{64})`", txt):
        reg.setdefault(s, h)
    return reg

def build(out):
    reg = registered_hashes(); checks = {}
    for s, *_ in CHAIN:
        h = sha(os.path.join(EV, "scripts", s))
        assert s in reg, f"{s}: no registered hash in the RECOG DSN"
        assert h == reg[s], f"{s}: file {h} != registered {reg[s]}"
        checks[s] = h
    for v in ("orig", "patch"):
        t = os.path.join(out, v)
        if os.path.exists(t):
            shutil.rmtree(t)
        os.makedirs(os.path.join(t, "scripts"))
        for s, d, *_ in CHAIN:
            shutil.copy2(os.path.join(EV, "scripts", s), os.path.join(t, "scripts", s))
            os.makedirs(os.path.join(t, d), exist_ok=True)
    p = os.path.join(out, "patch", "scripts", SITE)
    src = open(p, encoding="utf-8").read()
    assert src.count(OLD) == 1 and src.count(NEW) == 0, "patch site not found exactly once"
    lines = src.split("\n"); idx = [i for i, l in enumerate(lines) if OLD in l]
    assert idx == [54], f"patch site not at L55: {idx}"
    open(p, "w", encoding="utf-8", newline="").write(src.replace(OLD, NEW))
    return checks

def run_tree(t):
    timing = []
    for s, d, j, extra in CHAIN:
        t0 = time.time()
        with open(os.path.join(t, d, j.replace(".json", "_output.txt")), "wb") as fo, \
             open(os.path.join(t, d, j.replace(".json", "_stderr.txt")), "wb") as fe:
            rc = subprocess.run([sys.executable, "-I", os.path.join("..", "scripts", s), j] + extra,
                                cwd=os.path.join(t, d), stdout=fo, stderr=fe).returncode
        timing.append({"script": s, "rc": rc, "seconds": round(time.time() - t0, 1)})
        print(f"  {os.path.basename(t)}: {s} rc={rc} {timing[-1]['seconds']}s", flush=True)
        if rc != 0:
            break
    return timing

def flat(o, p=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from flat(v, f"{p}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from flat(v, f"{p}[{i}]")
    else:
        yield p, o

def num(x):
    if isinstance(x, bool):
        return None
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        try:
            return float(x)
        except ValueError:
            return None
    return None

def compare(out):
    res = {"site": f"{SITE} L55: {OLD} -> {NEW}", "certs": [], "all_gates_pass_orig": True,
           "all_gates_pass_patch": True, "reproduction_byte_equal": True}
    for s, d, j, extra in CHAIN:
        rel = os.path.join(d, j); rtxt = rel.replace(".json", "_output.txt")
        c, o, p = (os.path.join(EV, rel), os.path.join(out, "orig", rel), os.path.join(out, "patch", rel))
        jo, jp = json.load(open(o)), json.load(open(p))
        fo, fp = dict(flat(jo)), dict(flat(jp))
        go, gp = jo.get("gates", {}), jp.get("gates", {})
        bool_flips = [k for k in fo if isinstance(fo[k], bool) and fp.get(k) is not fo[k]]
        changes = []
        for k in fo:
            a, b = num(fo[k]), num(fp.get(k))
            if a is not None and b is not None and a != b:
                changes.append((abs(b - a) / max(abs(a), 1e-300), k, a, b))
        changes.sort(reverse=True)
        imp = [k for k in fo if k.startswith(".imports.") and fo[k] != fp.get(k)]
        row = {
            "cert": s, "json": rel,
            "committed_eq_orig_json_bytes": open(c, "rb").read() == open(o, "rb").read(),
            "committed_eq_orig_output_bytes": open(os.path.join(EV, rtxt), "rb").read() == open(os.path.join(out, "orig", rtxt), "rb").read(),
            "gates_orig": go, "gates_patch": gp,
            "all_gates_orig": all(go.values()) and bool(go), "all_gates_patch": all(gp.values()) and bool(gp),
            "boolean_leaves": sum(isinstance(v, bool) for v in fo.values()), "boolean_flips": bool_flips,
            "numeric_leaves_changed": len(changes), "import_hash_fields_changed": imp,
            "max_rel_change": changes[0][0] if changes else 0.0,
            "top_changes": [{"key": k, "orig": a, "patch": b, "rel": r} for r, k, a, b in changes[:5]],
            "patch_json_sha256": sha(p), "patch_output_txt_identical_to_orig": open(os.path.join(out, "orig", rtxt), "rb").read() == open(os.path.join(out, "patch", rtxt), "rb").read(),
        }
        res["certs"].append(row)
        res["all_gates_pass_orig"] &= row["all_gates_orig"]; res["all_gates_pass_patch"] &= row["all_gates_patch"]
        res["reproduction_byte_equal"] &= row["committed_eq_orig_json_bytes"] and row["committed_eq_orig_output_bytes"]
    json.dump(res, open(os.path.join(out, "ra1_recheck_summary.json"), "w"), indent=1)
    for r in res["certs"]:
        print(f"{r['cert']:40s} repro={'EQ' if r['committed_eq_orig_json_bytes'] and r['committed_eq_orig_output_bytes'] else 'DIFF'}"
              f" gates orig/patch={sum(r['gates_orig'].values())}/{len(r['gates_orig'])} {sum(r['gates_patch'].values())}/{len(r['gates_patch'])}"
              f" flips={len(r['boolean_flips'])} changed={r['numeric_leaves_changed']} max_rel={r['max_rel_change']:.2e}"
              f" txt_same={r['patch_output_txt_identical_to_orig']}")
    print("ALL GATES PASS (orig, patch):", res["all_gates_pass_orig"], res["all_gates_pass_patch"],
          "| reproduction byte-equal:", res["reproduction_byte_equal"])
    return res

def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ("run", "compare"):
        print(__doc__); sys.exit(2)
    out = os.path.abspath(sys.argv[2]); os.makedirs(out, exist_ok=True)
    if sys.argv[1] == "run":
        checks = build(out); timing = {}
        for v in ("orig", "patch"):
            timing[v] = run_tree(os.path.join(out, v))
        json.dump({"script_hashes_checked": checks, "timing": timing, "python": sys.version},
                  open(os.path.join(out, "ra1_run_log.json"), "w"), indent=1)
    res = compare(out)
    sys.exit(0 if res["all_gates_pass_orig"] and res["all_gates_pass_patch"] else 1)

if __name__ == "__main__":
    main()
