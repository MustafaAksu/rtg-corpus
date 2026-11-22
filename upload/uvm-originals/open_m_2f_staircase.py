"""
open_m_2f_staircase.py — OPEN-M-2F: Delta-omega staircase projection of ESM packs
[RID: UVM-OPEN-2F]  cross-ref: Dyadic (p=6 local resonance), Pre-Legacy 1.3 (ladder), Bridge.

Tests whether harmonic loading (sigma_h_int) rises only when internal edges enter
the x>=0.70 (4D/non-gauged corridor) band of the Pre-Legacy dimensional ladder:
  x<0.28 : D=2 (planar, U(1));  0.28<=x<0.70 : D=3 (proton window, soft-SU2);
  0.70<=x<1.55 : D=4 corridor (NOT gauged, loop density fails);  x>=1.55 : SU(3)-ish.

CONVENTION NOTE [load-bearing]: uses the pack-native ladder coordinate x_link
(range 0..1.55, pre-binned to the Pre-Legacy thresholds), NOT |domega|/DeltaOmega*_SI.
The pipeline runs at DeltaOmega_eff=1.22e21, ~119x below the SI critical bandwidth
1.45e23; using the SI scale would place ALL edges at x<0.05 (spurious all-2D).
x_link is the pipeline's internal-scale ladder coordinate -> correct for this test.
"""
import numpy as np, sys
THRESH=[0.28,0.70,1.55]
BANDS=["D2 (x<0.28)","D3 (0.28-0.70)","D4corr (0.70-1.55)","SU3 (x>=1.55)"]
def band_of(x):
    return 0 if x<0.28 else 1 if x<0.70 else 2 if x<1.55 else 3
PACKS={
 "RUN10 dirty-pass":"open_m_2d_seed_001_rank_2_v13_loose_T80_to_T120",
 "RUN11 polished":"open_m_2d_seed_001_rank_2_T120_defect_polish",
 "T80->T120 clean-norim":"grown_cluster_v13"}  # microstate available; T80 r0 had no microstate upload
ok=True
def check(n,c):
    global ok; print(f"[{'PASS' if c else 'FAIL'}] {n}"); ok&=bool(c)

import os
def grown_xlink_and_harm(stub):
    fp=f"/mnt/user-data/uploads/{stub}_microstate.npz"
    if not os.path.exists(fp): return None
    ms=np.load(fp,allow_pickle=True)
    # map full-edge x_link onto grown edges
    full_edges=[tuple(sorted((int(a),int(b)))) for a,b in ms["edges"]]
    xfull={e:float(ms["x_link"][i]) for i,e in enumerate(full_edges)}
    GE=[tuple(sorted((int(a),int(b)))) for a,b in ms["grown_edges"]]
    x=np.array([xfull.get(e,np.nan) for e in GE])
    miss=np.isnan(x).sum()
    # internal-edge mask (incidence>=2 among grown faces)
    GF=ms["grown_faces"].astype(int)
    inc={}
    for (a,b,c) in GF:
        for (u,v) in [(a,b),(b,c),(c,a)]:
            k=tuple(sorted((int(u),int(v)))); inc[k]=inc.get(k,0)+1
    is_int=np.array([inc.get(e,0)>=2 for e in GE])
    z=ms["z_edge_centered"].astype(float)
    return x,is_int,z,miss,GE

print("OPEN-M-2F :: Delta-omega staircase projection (pack-native x_link)\n")
for tag,stub in PACKS.items():
    r=grown_xlink_and_harm(stub)
    if r is None:
        print(f"--- {tag}: microstate not available, skipped ---"); continue
    x,is_int,z,miss,GE=r
    check(f"{tag}: all grown edges have x_link ({miss} missing)", miss==0)
    xi=x[is_int]
    print(f"--- {tag}: {len(GE)} grown edges, {is_int.sum()} internal ---")
    print(f"    internal x_link: min={xi.min():.3f} median={np.median(xi):.3f} "
          f"mean={xi.mean():.3f} max={xi.max():.3f}")
    fr=[ (band_of(0)==0) ]  # placeholder
    counts=[0,0,0,0]
    for xv in xi: counts[band_of(xv)]+=1
    fr=[c/len(xi) for c in counts]
    print("    internal band fractions: "+"  ".join(f"{BANDS[i]}={fr[i]:.2f}" for i in range(4)))
    # harmonic loading per band: sigma of z on internal edges within each band
    for bi in range(4):
        m=is_int & np.array([band_of(xv)==bi for xv in x])
        if m.sum()>1:
            print(f"      {BANDS[bi]:18s}: n={int(m.sum()):3d}  sigma(z)={np.std(z[m]):.4f}  <|z|>={np.abs(z[m]).mean():.4f}")
    # corridor fraction = key OPEN-M-2F coordinate
    corr_frac=fr[2]+fr[3]
    print(f"    >>> internal corridor fraction (x>=0.70) = {corr_frac:.3f}")

print("\nKEY TEST: does internal sigma(z) rise with corridor fraction across packs?")
print("(directional, n=3; full test needs the per-step growth trajectory)")
print("\nALL CHECKS:","PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
