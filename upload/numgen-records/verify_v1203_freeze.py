#!/usr/bin/env python3
# One-command freeze verification for RTG_NUMBER_GENESIS_DSN v1.20.3.  (v1.2: banner-safe base AND owner)
# Checks exactly the four co-owner conditions + the composite gate.
# Needs in the same folder: the v1.20.3 bundle, RTG_NUMBER_GENESIS_DSN_v1_20_2.md,
# RTG_NUMBER_GENESIS_DSN_v1_20_2_fingerprint_v2.json, NG_V1203_REVERSE_INVENTORY_v2.json,
# NG_V1203_MIGRATION_LEDGER_v1.json, ng_state_fingerprint_v2_3.py,
# ng_migration_checks_v2_1.py, ng_inv_live_v1_1.py.
import io, sys, json, hashlib, subprocess, re
OWNER = "RTG_NUMBER_GENESIS_DSN_v1_20_3.md"; BASE_FILE = "RTG_NUMBER_GENESIS_DSN_v1_20_2.md"
# v1.1: after the v1.20.3 freeze, v1.20.2 carries a SUPERSEDED banner, which shifts
# the line numbers the inventory is keyed to. Strip the banner into a temp copy and
# PROVE the remainder is the frozen v1.20.2 before using it as the base.
import tempfile, os
_raw = io.open(BASE_FILE, encoding="utf-8").read()
if _raw.startswith("> **[SUPERSEDED"): _raw = _raw.split("\n\n", 1)[1]
assert hashlib.sha256(_raw.encode("utf-8")).hexdigest() == "35fe1a65e831b620ec1d81819cdd614f07836395870f694dcc2d91a31dde1053", "base is not the frozen v1.20.2"
BASE = os.path.join(tempfile.mkdtemp(), "RTG_NUMBER_GENESIS_DSN_v1_20_2.md")
io.open(BASE, "w", encoding="utf-8").write(_raw)
WANT = "c3265a3a12974e300789179298a732cec579ccfad98b587755e018bcc5cfd2df"
R = []
def ck(name, ok): print(f"[{'PASS' if ok else 'FAIL'}] {name}"); R.append(ok)
def run(c): return subprocess.run([sys.executable] + c, capture_output=True, text=True).returncode
b = io.open(OWNER, "rb").read()
# v1.2: once v1.20.3 is itself superseded it carries a banner; verify the CONTENT.
if b.startswith("> **[SUPERSEDED".encode("utf-8")):
    b = b.split(b"\n\n", 1)[1]
    _tmp = os.path.join(tempfile.mkdtemp(), OWNER); open(_tmp, "wb").write(b); OWNER = _tmp
d = b.decode("utf-8")
rep = io.open("NG_V1203_MIGRATION_REPORT_v1.md", encoding="utf-8").read()
hier = io.open("NG_V1203_HIER_INVENTORY_v1.json", encoding="utf-8").read()
ck(f"1 owner SHA-256 = {WANT[:12]}…", hashlib.sha256(b).hexdigest() == WANT)
old = ["full structural migration deferred", "FP-v2.2", "proposed and reviewable"]
ck("2 three superseded metadata phrases: 0 hits in owner", not any(p in d for p in old))
ck("  (report no longer says 'my proposal' / 'sibling of its former parent')",
   "my proposal" not in rep and "sibling of its former parent" not in rep)
new = ["§2/§6 structural migration completed in this methodology-only release",
       "FP-v2.3",
       "Co-owner approved structural mappings: N-4 → §6.5, N-6 → §6.7, NG-9 → §6.10",
       "semantic parent remains N-1C-DYAD"]
ck("3 four new metadata rulings present in owner", all(p in d for p in new))
ck("  (rendering-exception sentence in report and hierarchical inventory)",
   "semantic parentage remains N-1C-DYAD → L1" in rep and "semantic parentage remains N-1C-DYAD" in hier)
L = d.split("\n"); f = lambda p: next(i + 1 for i, l in enumerate(L) if l.startswith("## " + p))
run(["ng_state_fingerprint_v2_3.py", "fingerprint", OWNER, "--s2", f"{f('§2')}:{f('§3')}", "--s6", f"{f('§6')}:{f('§7')}"])
FPN = OWNER.replace(".md", "_fingerprint_v2.json")
g = {"FP-v2.3 INV-0..4": run(["ng_state_fingerprint_v2_3.py", "compare", "RTG_NUMBER_GENESIS_DSN_v1_20_2_fingerprint_v2.json", FPN, "NG_V1203_MIGRATION_LEDGER_v1.json"]),
     "INV-S final": run(["ng_migration_checks_v2_1.py", "invS", BASE, OWNER, "NG_V1203_REVERSE_INVENTORY_v2.json", "--mode", "final"]),
     "INV-P post-write": run(["ng_migration_checks_v2_1.py", "invPpost", "NG_V1203_REVERSE_INVENTORY_v2.json", OWNER, FPN]),
     "INV-LIVE": run(["ng_inv_live_v1_1.py", OWNER])}
for k, v in g.items(): ck(f"4 composite gate — {k}", v == 0)
print("-" * 60); print("v1.20.3 FREEZE CONDITIONS MET" if all(R) else "NOT READY"); sys.exit(0 if all(R) else 1)
