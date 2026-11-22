"""
open_m_3g_mini_protocol.py — OPEN-M-3g-mini: conformal stiffness extraction
[RID candidate: UVM-NUM-3G-MINI]

Theory spine [ALG]:
  E_vac(s) = (1/2) K_vac sum_e (z_e + s)^2  under uniform dilation r->e^s r
           = E_0 + K_vac (sum_e z_e) s + (1/2) N_E K_vac s^2   IDENTICALLY.
  => bare per-edge conformal stiffness g_bare = K_vac (exact);
     linear term = 0 at vacuum equilibrium (sum z = 0);
     relaxed K_conf <= bare (internal-mode softening), so g_relaxed <= K_vac
     and rho = ell/g moves FAVORABLY under relaxation.

THEOREM [ALG] (conformal-mode rigidity of the log-vacuum):
  In log-edge coordinates v_e = ln r_e, the configuration manifold M is
  invariant under translation along (1,...,1) (scale-invariance of the log).
  On any fixed-scale slice, 1.(v - v_em) is constant, hence
     E_min(s) = E_min(0) + c1 s + (1/2) N_E K_vac s^2  EXACTLY:
  relaxed K_conf = bare K_conf = N_E K_vac, for ANY topology and frustration.
  => g_conf = K_vac per edge, exactly. OPEN-M-3g-mini closes analytically;
  the numerical scans below are verification, not measurement.

Protocol (verification; same scans apply to the real cluster npz as a sanity check):
  1. verify sum_e z_e ~ 0 at the relaxed vacuum (equilibrium check)
  2. bare scan: dilate, do NOT relax, fit E(s) quadratic -> K_bare; check = N_E*K_vac
  3. relaxed scan: dilate, relax internal coordinates at fixed scale
     (project out the global dilation direction), fit -> K_relaxed <= K_bare
  4. report g_conf = K_relaxed / N_E (per-edge convention, matching h,m per-edge Hodge convention)
All checks must pass; exit code gated.
"""
import numpy as np
np.random.seed(7)
ok=True
def check(n,c):
    global ok; print(f"[{'PASS' if c else 'FAIL'}] {n}"); ok&=bool(c)

# --- synthetic cluster: random geometric graph ---
N=40
X=np.random.randn(N,3)*1.5
D=np.linalg.norm(X[:,None,:]-X[None,:,:],axis=2)
edges=[(i,j) for i in range(N) for j in range(i+1,N) if D[i,j]<2.0]
NE=len(edges); Kvac=1.0
r_em=np.array([D[i,j]*np.exp(0.1*np.random.randn()) for i,j in edges])  # frustrated targets

def rgeo(X): return np.array([np.linalg.norm(X[i]-X[j]) for i,j in edges])
def E(X): z=np.log(rgeo(X)/r_em); return 0.5*Kvac*np.sum(z*z)
def grad(X):
    g=np.zeros_like(X); r=rgeo(X); z=np.log(r/r_em)
    for k,(i,j) in enumerate(edges):
        d=(X[i]-X[j])/r[k]; f=Kvac*z[k]/r[k]
        g[i]+=f*d; g[j]-=f*d
    return g
def scale_var(X): return np.sum(np.log(rgeo(X)))      # conjugate of dilation mode
def scale_grad(X):
    g=np.zeros_like(X); r=rgeo(X)
    for k,(i,j) in enumerate(edges):
        d=(X[i]-X[j])/r[k]
        g[i]+=d/r[k]; g[j]-=d/r[k]
    return g
def relax(X,steps=3000,lr=0.02,fix_scale=False):
    """If fix_scale: holonomic constraint sum_e ln r_e = const, enforced by
    tangent-space projection PLUS per-step restoration (exact rescale) —
    no drift, unlike instantaneous-direction projection (T-6f lesson)."""
    X=X.copy(); c0=scale_var(X)
    for _ in range(steps):
        g=grad(X)
        if fix_scale:
            cg=scale_grad(X); cg2=np.sum(cg*cg)
            g=g-(np.sum(g*cg)/cg2)*cg            # tangent projection
        X-=lr*g
        X-=X.mean(0)
        if fix_scale:
            X*=np.exp((c0-scale_var(X))/NE)      # exact constraint restoration
    return X

# 1. vacuum equilibrium
X0=relax(X,steps=8000)
z0=np.log(rgeo(X0)/r_em)
check(f"equilibrium: |sum z| / (N_E*rms z) small  (got {abs(z0.sum())/(NE*z0.std()+1e-30):.2e})",
      abs(z0.sum())<5e-3*NE*max(z0.std(),1e-6)+1e-6)

# 2. bare scan
ss=np.linspace(-0.1,0.1,11)
Xc0=X0-X0.mean(0)
Eb=[E(X0.mean(0)+np.exp(s)*Xc0) for s in ss]
cb=np.polyfit(ss,Eb,2); Kbare=2*cb[0]
check(f"bare K_conf = N_E*K_vac exactly (fit {Kbare:.6f} vs {NE*Kvac})",
      abs(Kbare-NE*Kvac)<1e-6*NE)
check(f"bare linear term = K_vac*sum z (fit {cb[1]:.3e} vs {Kvac*z0.sum():.3e})",
      abs(cb[1]-Kvac*z0.sum())<1e-6*NE)

# 3. relaxed scan
Er=[]
for s in ss:
    Xs=X0.mean(0)+np.exp(s)*Xc0
    Xs=relax(Xs,steps=2000,fix_scale=True)
    Er.append(E(Xs))
cr=np.polyfit(ss,Er,2); Krel=2*cr[0]
check(f"relaxed K_conf <= bare ({Krel:.3f} <= {Kbare:.3f})", Krel<=Kbare+1e-6)
softening=1-Krel/Kbare
g_conf=Krel/NE
print(f"    N_E={NE}; softening fraction = {softening:.3f}")
print(f"    g_conf (relaxed, per-edge) = {g_conf:.4f}  [bare = {Kvac}]")
print(f"    => rho = ell/g_conf amplification vs bare proxy: x{1/max(g_conf,1e-9):.2f}")
print("    NOTE: zero softening is the THEOREM, not a synthetic artifact —")
print("    g_conf = K_vac holds for any topology/frustration (see header).")
check("g_conf positive (stable conformal mode)", g_conf>0)

# --- THEOREM verification on a second, differently-built cluster ---
np.random.seed(99)
N2=30; X2=np.random.randn(N2,3)*1.1
D2=np.linalg.norm(X2[:,None,:]-X2[None,:,:],axis=2)
edges2=[(i,j) for i in range(N2) for j in range(i+1,N2) if D2[i,j]<1.9]
edges_bak,r_bak,NE_bak=edges,r_em,NE
edges=edges2; NE=len(edges2)
r_em=np.array([D2[i,j]*np.exp(0.25*np.random.randn()) for i,j in edges2])  # stronger frustration
X0b=relax(X2,steps=8000)
Xc0b=X0b-X0b.mean(0)
Erb=[]
for sv in ss:
    Xs=X0b.mean(0)+np.exp(sv)*Xc0b
    Xs=relax(Xs,steps=2000,fix_scale=True)
    Erb.append(E(Xs))
Krel2=2*np.polyfit(ss,Erb,2)[0]
check(f"THEOREM check, cluster 2 (different N, topology, frustration): K_rel = N_E*K_vac ({Krel2:.3f} vs {NE*Kvac})",
      abs(Krel2-NE*Kvac)<2e-2*NE*Kvac)
edges,r_em,NE=edges_bak,r_bak,NE_bak

print("\nALL CHECKS:","PASS" if ok else "FAIL")
import sys; sys.exit(0 if ok else 1)
