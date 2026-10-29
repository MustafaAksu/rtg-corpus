# Initial states ON the transported closure plane, |u|/|v| = 1 +/- d; does the long-time side agree with the cubic separator?
import numpy as np
s3=np.sqrt(3); lam=0.5+1j*s3/2; lb=np.conj(lam)
n21=1/8-7j*s3/72; n32=-5/432+23j*s3/3888; n05=43/17280-227j*s3/155520
N=lambda z: lam*z+n21*z*z*np.conj(z)+n32*z**3*np.conj(z)**2+n05*np.conj(z)**5
def F(z,k): Nz=N(z); return Nz-(k/3)*Nz.sum()
def from_uv(u,v):
    w2=(u-v)/(lam-lb); w1=u-lam*w2; return np.array([w1,w2,-w1-w2])
def ratio(z): w1,w2,_=z; return abs(w1+lam*w2)/abs(w1+lb*w2)
rng=np.random.default_rng(7); agree=0; tot=0; rows=[]
for k in [0.5,1.5]:
    for d in [0.3,0.1,0.03]:
        for sgn in [+1,-1]:
            for t in range(4):
                a=0.1; ph1,ph2=rng.uniform(0,2*np.pi,2)
                r=1+sgn*d; v=a/np.sqrt(1+r*r); u=r*v
                z=from_uv(u*np.exp(1j*ph1),v*np.exp(1j*ph2))
                for n in range(6*20000): z=F(z,k)
                fin=ratio(z); ok=(fin>1)==(sgn>0); agree+=ok; tot+=1
                if not ok: rows.append((k,d,sgn,t,fin))
print(f"side preserved in {agree}/{tot} runs (initial |u|/|v| = 1±d on the closure plane, d in 0.3,0.1,0.03)")
for r_ in rows: print("disagree:",r_)
