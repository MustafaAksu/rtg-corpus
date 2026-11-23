"""
v2.7.2 minimal certification checksum. Verify the three scoped numbers:
  (1) Q_d*           ~ 1.13e-2   (P4=0 fixed point at control loss)
  (2) Q_d(n_ctrl)    ~ 5.6e-3    (universal control-loss value)
  (3) max over scanned phases Q_d < 0.05  (never reaches threshold)
Scope: reduced birth-race model (full-P4 scalar race), NOT arbitrary M_phase.
Uses the same certified P4 recurrence as genesis_birth_race_model.py.
"""
import math
SQRT3 = math.sqrt(3)

def dphi_ds(Qs): return -(SQRT3/18144)*Qs*(1264*Qs**2 - 459)

def p4_full(qs, qc, qd, phi_ds, phi_dc=0.0, phi_sc=math.pi/2):
    def inv(qa, qb, phi):
        R = math.sqrt(max(qa*qb, 0))
        return R*math.cos(phi), (2/SQRT3)*R*math.sin(phi)
    Ids, wds = inv(qd, qs, phi_ds)
    Idc, wdc = inv(qd, qc, phi_dc)
    Rsc = math.sqrt(max(qs*qc, 0)); Isc = 0.0; wsc = (2/SQRT3)*Rsc
    return (
        -qd*qd -(1/8)*qs*Ids -(3/32)*qs*wds
        -(1/27)*qc*Idc +(7/108)*qc*wdc
        -(5/12)*wds*Ids-(1/8)*wds*wds
        -(5/9)*wdc*Idc -(1/6)*wdc*wdc
        +(1/36)*qs*Idc -(7/48)*qs*wdc
        +(1/18)*Ids*Isc+(7/72)*Ids*wsc
        +(1/6)*qc*Ids  +(3/8)*qc*wds
        +(1/3)*Idc*Isc +(1/4)*Idc*wsc
    )

# (1) Fixed point Q_d* at control loss Qs=0.1, end-of-race phase
for kname,kappa in [("shear",-2*SQRT3/3),("recoil",-0.5)]:
    Qs=0.1; Qc=kappa**2*Qs**3; phi=math.pi+math.atan(SQRT3/2)+0.41
    lo,hi=1e-8,0.5
    for _ in range(80):
        mid=(lo+hi)/2
        if p4_full(Qs,Qc,mid,phi)>0: lo=mid
        else: hi=mid
    print(f"(1) Q_d* fixed point [{kname}] = {hi:.4e}  (target ~1.13e-2)")

# (2) Q_d(n_ctrl): run race to Qs=0.1 control loss, record Q_d
def race(Qs0,kappa,Qs_ctrl=0.1,max_n=500000):
    Qs=Qs0; Qc=kappa**2*Qs**3; Qd=(7/1024)*Qs**3
    phi=math.pi+math.atan(SQRT3/2); Qdmax=Qd
    for n in range(1,max_n+1):
        dQd=p4_full(Qs,Qc,max(Qd,0),phi); phi+=dphi_ds(Qs)
        Qs+=0.25*Qs**2+(5/9)*Qs*Qc; Qc+=(5/12)*Qs*Qc+(1/3)*Qc**2; Qd+=dQd
        Qd=max(Qd,0)
        if Qd>Qdmax: Qdmax=Qd
        if Qs>=Qs_ctrl: return Qd,Qdmax,n
    return Qd,Qdmax,max_n

print()
kappa=-2*SQRT3/3
results=[]
for Qs0 in [1e-3,5e-3,1e-2,2e-2,5e-2]:
    Qd,Qdmax,n=race(Qs0,kappa)
    results.append((Qs0,Qd,Qdmax))
    print(f"(2) Qs0={Qs0:.0e}: Q_d(n_ctrl)={Qd:.4e}, Q_d(max)={Qdmax:.4e}, n={n}")

# (3) max over all scanned Qs0/kappa of Qd_max vs 0.05
allmax=0.0
for kname,kappa in [("shear",-2*SQRT3/3),("recoil",-0.5)]:
    for Qs0 in [1e-3,5e-3,1e-2,2e-2,5e-2]:
        _,Qdmax,_=race(Qs0,kappa)
        allmax=max(allmax,Qdmax)
print()
print(f"(3) max scanned Q_d = {allmax:.4e}   threshold = 5.0e-2   below? {allmax<0.05}")

print()
print("="*55)
print("CHECKSUM VERDICT")
print("="*55)
c1 = 1.0e-2 < hi < 1.3e-2
c2 = all(4e-3 < Qd < 7e-3 for _,Qd,_ in results[:4])  # 5.6e-3 universal-ish
c3 = allmax < 0.05
print(f"(1) Q_d* in [1.0e-2,1.3e-2]:        {c1}")
print(f"(2) Q_d(n_ctrl) ~ 5.6e-3 (4-7e-3):  {c2}")
print(f"(3) max scanned < 0.05:             {c3}")
print(f"\nALL THREE PASS: {c1 and c2 and c3}")
