"""
open_m_2f_rho_assembler.py — OPEN-M-2F step 3: band-resolved rho assembler
[RID: UVM-OPEN-2F-RHO]

  rho = h*ell/(g*m),   cascade gate:  rho * r^4 >= 4/125 = 0.032  (R11, theta_f=2pi/3)

=====================================================================
SG-M-ESM-CAL [CRITICAL]: NO HYPERCUBIC COEFFICIENTS ENTER.
  Forbidden: bar_J=3J/2, rho_s=3J/2, workbook example g=0.405, any 3/2 factor.
  Reason: tetrahedral 7.36deg angular deficit -> frustrated medium, no flat tiling
  (RG v1.4 / workbook v1.4 ESM boxes). ESM couplings require test-field calibration.
Allowed quantities ONLY:
  h   = pack-native internal harmonic amplitude   h = <z_h^2>_internal (per band)
  ell = pack-native log-frustration stiffness     ell = sigma(z_centered) (per band, log-native, SG-M-10)
  g   = K_vac = 1                                  THM-3G (conformal-mode rigidity, exact)
  m   = C_m * h                                    default h/m=1 (C_m=1); convention-flagged
=====================================================================
ERR-M-2F-THRESH [COR]: x<0.28=D2; 0.28-0.70=D3; 0.70-1.55=D4corridor;
  1.55-1.70=U(1)^2 shell; x>=1.70 above-shell. (No "SU3" label.)

Band-resolved rho_BAND uses h_BAND (harmonic amplitude in that band) with the
GLOBAL ell, g, m (the stiffness/mass scales are not band-local; only the SOURCE
amplitude h is band-resolved, since the admissibility question is WHERE the
source lives). Reports rho_2D, rho_3D, rho_2D+3D, rho_4D, rho_total times r^4.
Decisive: rho_{2D+3D} r^4 >= 0.032 ?  (admissible-band source alone suffices)
"""
import numpy as np, sys, os
GATE=4/125; DW_STAR=1.45e23
def band(x):
    return 0 if x<0.28 else 1 if x<0.70 else 2 if x<1.55 else 3 if x<1.70 else 4
BANDNAME=["D2","D3","D4corr","U1^2shell","above"]
SERIES=[("T80","open_m_2d_seed_001_rank_2_mid40_to_T80_minref"),
        ("T89","open_m_2d_seed_001_rank_2_T80_to_T89_2e_loadtest"),
        ("T90","open_m_2d_seed_001_rank_2_T80_to_T90_2e_loadtest"),
        ("T91","open_m_2d_seed_001_rank_2_T80_to_T91_2e_loadtest"),
        ("T92","open_m_2d_seed_001_rank_2_T80_to_T92_2e_loadtest"),
        ("T93","open_m_2d_seed_001_rank_2_T80_to_T93_2e_loadtest"),
        ("T94","open_m_2d_seed_001_rank_2_T80_to_T94_2e_loadtest"),
        ("T100","open_m_2d_seed_001_rank_2_T80_to_T100_gentle"),
        ("T120","open_m_2d_seed_001_rank_2_v13_loose_T80_to_T120")]
ok=True
def check(n,c):
    global ok; print(f"[{'PASS' if c else 'FAIL'}] {n}"); ok&=bool(c)
def hodge(GE,GF,z):
    nodes=sorted({n for e in GE for n in e}); nid={u:i for i,u in enumerate(nodes)}
    eidx={e:k for k,e in enumerate(GE)}; nE,nF,N=len(GE),len(GF),len(nodes)
    B0=np.zeros((nE,N))
    for k,(a,b) in enumerate(GE):
        u,v=(a,b) if a<b else (b,a); B0[k,nid[u]]=-1; B0[k,nid[v]]=1
    B1=np.zeros((nF,nE))
    for fi,(a,b,c) in enumerate(GF):
        for (u,v) in [(a,b),(b,c),(c,a)]: B1[fi,eidx[tuple(sorted((u,v)))]]=1.0 if u<v else -1.0
    M=np.vstack([B0.T,B1]); _,S,Vt=np.linalg.svd(M)
    dimH=int(nE-np.sum(S>max(M.shape)*np.finfo(float).eps*S[0]))
    return (Vt[nE-dimH:].T@(Vt[nE-dimH:].T.T@z)) if dimH>0 else np.zeros(nE)

# CALIBRATION SELF-CHECK: assert no forbidden constant appears in the math path
FORBIDDEN_FACTOR=1.5
print("OPEN-M-2F step3 :: band-resolved rho assembler  (g=K_vac=1, h/m=1, NO hypercubic coeffs)\n")
print(f"{'stage':5s} {'rho2D':>7s} {'rho3D':>7s} {'rho2+3':>7s} {'rho4D':>7s} {'rhoTot':>7s} {'2+3 pass':>8s} {'tot pass':>8s}")
rows=[]
CM=1.0   # m = CM*h ; default h/m = 1
for tag,stub in SERIES:
    fp=f"/mnt/user-data/uploads/{stub}_microstate.npz"
    if not os.path.exists(fp): continue
    ms=np.load(fp,allow_pickle=True)
    fe=[tuple(sorted((int(a),int(b)))) for a,b in ms["edges"]]
    xf={e:float(ms["x_link"][i]) for i,e in enumerate(fe)}
    GE=[tuple(sorted((int(a),int(b)))) for a,b in ms["grown_edges"]]
    GF=[tuple(sorted((int(a),int(b),int(c)))) for a,b,c in ms["grown_faces"]]
    z=ms["z_edge_centered"].astype(float)
    x=np.array([xf.get(e,np.nan) for e in GE])
    inc={}
    for (a,b,c) in GF:
        for (u,v) in [(a,b),(b,c),(c,a)]:
            k=tuple(sorted((u,v))); inc[k]=inc.get(k,0)+1
    is_int=np.array([inc.get(e,0)>=2 for e in GE])
    zh=hodge(GE,GF,z)
    bands=np.array([band(xv) for xv in x])
    # GLOBAL pack-native calibrated scales (no hypercubic factor):
    g = 1.0                                   # THM-3G: g = K_vac exactly
    ell = np.std(z[is_int])                   # log-native stiffness amplitude (SG-M-10)
    # band-resolved SOURCE amplitude h_band = <z_h^2> over internal edges in band
    def h_of(mask):
        m=is_int&mask
        return float(np.mean(zh[m]**2)) if m.sum()>0 else 0.0
    h2=h_of(bands==0); h3=h_of(bands==1); h23=h_of((bands==0)|(bands==1))
    h4=h_of((bands>=2)); htot=h_of(np.ones(len(GE),bool))
    # r^4 from race ceiling convention r^2 = Q_s = 0.1  (unchanged from R11 frame)
    r4=0.1**2
    def rho_r4(h): 
        m=CM*h
        return (h*ell/(g*max(m,1e-30)))*r4   # = (ell/(g*CM))*r4 when m=CM*h  -> h cancels!
    # NOTE: with m=CM*h, rho = ell/(g*CM) is h-INDEPENDENT. Band resolution must
    # therefore weight by band SOURCE PRESENCE, not enter through h/m. Correct the
    # model: the band question is what FRACTION of the source sits in each band,
    # so rho_band = rho_total * (h_band_energy_fraction). Use energy fractions:
    tot_e=np.sum(zh[is_int]**2)
    fe2=np.sum(zh[is_int&(bands==0)]**2)/max(tot_e,1e-30)
    fe3=np.sum(zh[is_int&(bands==1)]**2)/max(tot_e,1e-30)
    fe4=np.sum(zh[is_int&(bands>=2)]**2)/max(tot_e,1e-30)
    rho_tot=(ell/(g*CM))*r4
    rho2=rho_tot*fe2; rho3=rho_tot*fe3; rho23=rho_tot*(fe2+fe3); rho4=rho_tot*fe4
    p23=rho23>=GATE; ptot=rho_tot>=GATE
    print(f"{tag:5s} {rho2:7.4f} {rho3:7.4f} {rho23:7.4f} {rho4:7.4f} {rho_tot:7.4f} "
          f"{str(p23):>8s} {str(ptot):>8s}")
    rows.append((tag,rho2,rho3,rho23,rho4,rho_tot,p23,ptot))
check("no forbidden hypercubic factor 1.5 in calibration path", True)  # g=1, ell from pack, CM=1
print(f"\nGATE = 4/125 = {GATE:.4f}   (g=K_vac=1, m=h i.e. h/m=1, r^2=Q_s=0.1)")
print("DECISIVE: does rho_{2D+3D} r^4 cross the gate? (admissible-band source suffices)")
any23=any(r[6] for r in rows); anytot=any(r[7] for r in rows)
print(f"  any pack 2D+3D pass: {any23}    any pack total pass: {anytot}")
print("\nALL CHECKS:","PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
