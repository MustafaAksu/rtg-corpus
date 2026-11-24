#!/usr/bin/env python3
"""OFN S-P4 check (SESSION): run the unchanged FMS reflection test and test BOTH ideal containments for its P4 step.

usage: python3 evidence/ofn/scripts/ofn_p4_ideal_check_claude.py FMS_DIR
  The wrapper changes into FMS_DIR (the FMS script opens its dependencies by relative path).
  FMS_DIR holds the unchanged FMS_PSI_QUINTIC_REFLECTION_TEST_v0_1.py with its two dependencies
  (FMS_PSI_QUINTIC_CONJUGACY_TEST_v0_1.py, FMS_PSI_QUINTIC_KAPPA_ALL_v0_1.py), copied from upload/corpus-originals-20261123/.

What it does. The FMS script's P4 success predicate accepts when every generator g of the elimination ideal
I_el = I ∩ Q(√3,i)[r,t] is a multiple of L = 1026 r − 17√3 − 72√3 t, i.e. it tests I_el ⊆ ⟨L⟩. The theorem needs the
other direction, L ∈ I_el (then every solution satisfies L = 0). This wrapper runs the script unchanged, records the two
lex Gröbner bases of the P4 step (generators w, z, r, T), extracts I_el, and checks:
  C1  L reduces to 0 modulo the elimination basis (L ∈ I_el)          — the direction the theorem needs
  C2  every elimination generator is a multiple of L (I_el ⊆ ⟨L⟩)     — the direction the FMS predicate tests
  C3  control: the predicate form of C2 also accepts g = L·(r − 1), for which C1 fails (wrong-direction gate)
Exit 0 iff C1, C2 and C3 hold for both swap branches and the FMS script itself reports ALL PASS.
"""
import os, runpy, sys
import sympy as sp

d = os.path.abspath(sys.argv[1])
os.chdir(d)                                               # the FMS script opens its dependencies by relative path
sys.path.insert(0, d)
captured = []
_orig = sp.groebner


def spy(F, *gens, **kw):
    G = _orig(F, *gens, **kw)
    if len(gens) == 4:                                    # the P4 call: groebner(eqs, w, z, r, T, ...)
        captured.append((gens, G))
    return G


sp.groebner = spy
code = 0
try:
    runpy.run_path(os.path.join(d, "FMS_PSI_QUINTIC_REFLECTION_TEST_v0_1.py"), run_name="__main__")
except SystemExit as e:
    code = e.code or 0
sp.groebner = _orig
print(f"\nFMS script exit code: {code}")

ok = code == 0 and len(captured) == 2
for n, (gens, G) in enumerate(captured):
    w, z, r, T = gens
    L = sp.expand(1026 * r - 17 * sp.sqrt(3) - 72 * sp.sqrt(3) * T)
    el = [g for g in G.exprs if not (g.has(w) or g.has(z))]
    Gel = sp.groebner(el, r, T, order="lex", domain=G.domain) if el else None
    c1 = Gel is not None and Gel.reduce(L)[1] == 0
    c2 = bool(el) and all(sp.rem(sp.expand(g), L, r) == 0 for g in el)
    bad = sp.expand(L * (r - 1))
    c3 = sp.rem(bad, L, r) == 0 and _orig([bad], r, T, order="lex", domain=G.domain).reduce(L)[1] != 0
    print(f"swap branch {n}: elimination basis {el}")
    print(f"  C1 L in I_el: {c1}   C2 I_el in <L>: {c2}   C3 wrong-direction control (L(r-1) passes C2-form, fails C1): {c3}")
    ok &= c1 and c2 and c3
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
