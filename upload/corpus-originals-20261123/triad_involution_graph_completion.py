#!/usr/bin/env python3
"""
Companion to triad_formal_involution_birth_jet.py (reuses its exact jets; the parent file must sit alongside).
Question: does the S_triad-image of an age sheet c = C(s,tau) coincide with ANY age sheet?  And what is the unique
S-invariant even-order completion of the cubic graph?
  (a) degree-4 graph defect of c = C3(s) + C4(s) + O(5) is G4[C3] - 2*C4 (checked below for a generic C4), hence the
      S-image graph has quartic Phi4 = G4[C3] - C4 (DS = -I, C4 even); invariance at degree 4 iff C4 = G4[C3]/2.
  (b) with C4 := G4/2 the graph defect is re-evaluated through degree 5 (odd-degree completion terms C5 drop out of G5).
Exit 0 iff the stated identities hold.
"""
import sys
from pathlib import Path
src = (Path(__file__).resolve().parent / 'triad_formal_involution_birth_jet.py').read_text()
exec(src.split('# --------------------------------------------------------------- birth graph')[0].replace('ok_all = True', 'ok_all = True\nprint("[parent identity checks]")'))
exec(src.split('# --------------------------------------------------------------- birth graph')[1].split('results = {}')[0])
def graph_defect(Cfun):
    Bv = [X[0], X[1]] + Cfun([X[0], X[1]]); SB = vcompose(S, Bv)
    return [padd(SB[2+i], Cfun(SB[0:2])[i], -1) for i in range(2)]
def homog_s(p, d): return homog(p, d)
ok = ok_all
for kt in (Fr(1), Fr(2)):
    C3 = lambda sv, kt=kt: Cgraph_of(kt, sv)
    G = graph_defect(C3); G4 = [homog(G[i], 4) for i in range(2)]
    # (a) image graph of an arbitrary quartic C4 (test with a generic C4 and with the age-family value C4 = 0)
    gen = [padd(pscale(pmul(pmul(X[0], X[0]), pmul(X[0], X[1])), Fr(3)), pscale(pmul(pmul(X[1], X[1]), pmul(X[1], X[1])), Fr(-5))),
           pscale(pmul(pmul(X[0], X[0]), pmul(X[1], X[1])), Fr(7))]
    C34 = lambda sv, kt=kt: [padd(Cgraph_of(kt, sv)[i], compose(gen[i], sv + [X[2], X[3]])) for i in range(2)]
    Gg = graph_defect(C34)
    lin = all(homog(Gg[i], 4) == padd(G4[i], pscale(gen[i], -2)) for i in range(2))
    print(f'kt={kt}: degree-4 graph defect is G4[C3] - 2*C4 for a generic quartic C4: {"PASS" if lin else "FAIL"}'); ok &= lin
    # (b) completion
    C4 = [pscale(G4[i], HALF) for i in range(2)]
    Cc = lambda sv, kt=kt: [padd(Cgraph_of(kt, sv)[i], compose(C4[i], sv + [X[2], X[3]])) for i in range(2)]
    Gc = graph_defect(Cc)
    z4 = all(not homog(Gc[i], 4) for i in range(2)); z5 = all(not homog(Gc[i], 5) for i in range(2))
    print(f'kt={kt}: completed graph C3 + G4/2: degree-4 defect zero: {"PASS" if z4 else "FAIL"}; degree-5 defect zero: {z5}')
    if not z5: print('   G5 after completion =', [fmt(homog(Gc[i], 5)) for i in range(2)])
    ok &= z4
    print(f'   C4 = G4/2 = [{fmt(C4[0])}] , [{fmt(C4[1])}]')
print('\nall stated identities:', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
