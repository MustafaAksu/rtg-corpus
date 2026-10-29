import numpy as np
s3=np.sqrt(3); lam=0.5+1j*s3/2
n21=1/8-7j*s3/72; n32=-5/432+23j*s3/3888; n05=43/17280-227j*s3/155520
N=lambda z: lam*z+n21*z*z*np.conj(z)+n32*z**3*np.conj(z)**2+n05*np.conj(z)**5
def F(z,k):
    Nz=N(z); return Nz-(k/3)*Nz.sum()
rng=np.random.default_rng(1)
for k in [0.5,1.5]:
    for trial in range(3):
        z=(rng.normal(size=3)+1j*rng.normal(size=3))*0.08
        for n in range(6*20000+1):
            if n in (0,600,6000,60000,120000):
                w1,w2,w3=z; u=w1+lam*w2; v=w1+np.conj(lam)*w2
                print(f"k={k} trial={trial} n={n:6d} |sum z|={abs(z.sum()):.2e} |u|/|v|={abs(u)/abs(v):.3e} |z|={np.linalg.norm(z):.3e}")
            z=F(z,k)
