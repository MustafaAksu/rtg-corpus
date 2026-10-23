#!/usr/bin/env python3
r"""
recog_cell_f2a_sh_section_shadow.py — [ENG] symbolic check for RECOG CELL-F2(a2) (RECOG-ALG-SH-SECTION-SHADOW).
Scope: representation-level S_h = h o (-I) o h^{-1} only; NO identification with the physical pole relabeling (RRF OPEN-A untouched).
Input: the registered DYAD-ALG-NF6 quadratic term h_2(z, zb) = -(1+i sqrt3)/12 z^2 - 1/3 z zb + (1-i sqrt3)/24 zb^2 (higher h_n enter at O(t^3)).
Checks, on the canonical section W = t > 0 (exact sympy arithmetic):
 (1) h(t) = t + c t^2 + O(t^3),  c = -(3 + i sqrt3)/8
 (2) h^{-1}(t) = t - c t^2 + O(t^3)
 (3) S_h(t) = -t + 2c t^2 + O(t^3) = -t - (3 + i sqrt3)/4 t^2 + O(t^3)
 (4) arg S_h(t) - pi = (sqrt3/4) t + O(t^2);   arg S_h(-t) = -(sqrt3/4) t + O(t^2)  (opposite side of the positive ray)
 (5) leading displacement coefficient (sqrt3/4)/tau = 3/8, tau = 2 sqrt3/3   =>  Delta m = ±3/(8 sqrt Q) + O(1)
 (6) cross-check with F2(b): arg(h^{-1}(t)/t) = (sqrt3/8) t + O(t^2)  (the chart-shadow constant f(0)), and (sqrt3/8)/tau = 3/16
"""
import sympy as sp, sys
t = sp.symbols('t', positive=True); s3 = sp.sqrt(3); I = sp.I
def h2(z, zb): return -(1 + I*s3)/12*z**2 - sp.Rational(1, 3)*z*zb + (1 - I*s3)/24*zb**2
def h(z, zb): return z + h2(z, zb)                     # through O(|z|^2); h_3..h_6 contribute O(t^3)
def hc(z, zb): return sp.conjugate(h2(sp.conjugate(z), sp.conjugate(zb)))
ok = True
def chk(name, cond):
    global ok; print(f"[{'PASS' if cond else 'FAIL'}] {name}"); ok = ok and bool(cond)
c = sp.simplify(h2(t, t)/t**2)
chk("(1) c = -(3 + i sqrt3)/8", sp.simplify(c + (3 + I*s3)/8) == 0)
hinv = t - c*t**2                                        # real-ray inverse through O(t^2)
chk("(2) h(h^{-1}(t)) = t + O(t^3)", sp.simplify(sp.series(sp.expand(hinv + h2(hinv, sp.conjugate(hinv))), t, 0, 3).removeO() - t) == 0)
z = -hinv; S = sp.expand(z + h2(z, sp.conjugate(z)))
S2 = sp.series(S, t, 0, 3).removeO()
chk("(3) S_h(t) = -t - (3 + i sqrt3)/4 t^2 + O(t^3)", sp.simplify(S2 - (-t - (3 + I*s3)/4*t**2)) == 0)
dev = sp.series(sp.im(S2/(-t))/sp.re(S2/(-t)), t, 0, 2).removeO()      # tan(arg S_h - pi) to O(t)
chk("(4) arg S_h(t) - pi = (sqrt3/4) t + O(t^2)", sp.simplify(dev - s3/4*t) == 0)
tm = sp.symbols('u', positive=True)                      # S_h(-u): same algebra with t -> -u on the negative ray
zneg = -(-tm - c*tm**2); Sn = sp.series(sp.expand(zneg + h2(zneg, sp.conjugate(zneg))), tm, 0, 3).removeO()
devn = sp.series(sp.im(Sn/tm)/sp.re(Sn/tm), tm, 0, 2).removeO()
chk("(4') arg S_h(-t) = -(sqrt3/4) t + O(t^2)", sp.simplify(devn + s3/4*tm) == 0)
tau = 2*s3/3
chk("(5) (sqrt3/4)/tau = 3/8", sp.simplify((s3/4)/tau - sp.Rational(3, 8)) == 0)
a = sp.series(sp.im(hinv/t)/sp.re(hinv/t), t, 0, 2).removeO()
chk("(6) arg(h^{-1}(t)/t) = (sqrt3/8) t + O(t^2) and (sqrt3/8)/tau = 3/16", sp.simplify(a - s3/8*t) == 0 and sp.simplify((s3/8)/tau - sp.Rational(3, 16)) == 0)
print("F2(a2) SYMBOLIC CHECK PASS" if ok else "F2(a2) SYMBOLIC CHECK FAIL"); sys.exit(0 if ok else 1)
