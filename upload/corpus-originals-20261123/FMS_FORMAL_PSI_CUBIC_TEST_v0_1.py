import sympy as s
k,L,Lb,a=s.symbols('k L Lb a')
h,hb,w,wb=s.symbols('h hb w wb')
# Restricted centre direction (w,0,-w); closure coordinate h=sum z_e
u=[w,0,-w]; ub=[wb,0,-wb]
z=[x+h/3 for x in u];zb=[x+hb/3 for x in ub]
# linear A-step followed by projective mean map: P_k A z
v=[L*(x+(1-k)*h/3) for x in u]
vb=[Lb*(x+(1-k)*hb/3) for x in ub]
# g3(z)=a z^2 bar z, for g=P coupling change
mean_delta=s.expand(sum(a*x*x*y for x,y in zip(v,vb))-(1-k)*sum(a*(L*x)**2*(Lb*y) for x,y in zip(z,zb)))
coef=s.expand(mean_delta).coeff(h,1).coeff(w,1).coeff(wb,1)
coef2=s.expand(mean_delta).coeff(hb,1).coeff(w,2)
print("delta=",s.factor(mean_delta))
print('delta closure h*w*bar(w) = ',s.factor(coef))
print("delta=",s.factor(mean_delta))
print('delta closure bar(h)*w^2 = ',s.factor(coef2))
print('with L^2 Lbar=L:',s.factor(coef/(a*L*L*Lb)))
assert coef == 0 and coef2 == 0
expected = -L**2*Lb*a*h**2*hb*k*(k-2)*(k-1)/9
assert s.simplify(mean_delta-expected)==0
print('PASS: mixed closure h|u|² and bar(h)u² differences cancel at cubic order.')
print('Remaining cubic closure difference is pure h²bar(h):',s.factor(mean_delta))
print('SCOPE: sampled centre line (w,0,-w), radial A-equivariant g3; quintic and full formal conjugacy UNRESOLVED.')
