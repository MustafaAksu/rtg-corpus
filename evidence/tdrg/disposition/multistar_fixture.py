"""TDR-G owner-session fixture (27 Oct 2026): K_{2,3} multistar with two equal-degree centres; checks centre-swap equivariance per policy. Run from this folder: python3 -I multistar_fixture.py ENGINE.py"""
import sys
src=open('owner_relabel_equivariance_check.py').read().replace('\nmain()\n','\n'); exec(src)
N=24; k=1
# K_{2,3}: centres 0,1 at post-advance theta 0; leaves 2,3,4 at 12. Centres carry different tokens.
post={0:0,1:0,2:12,3:12,4:12}; dl={0:1,1:2,2:0,3:0,4:0}
pre={i:(post[i]-dl[i])%N for i in post}
for pol in ('largest_center','all_centers','bound_symmetric'):
    u=run(pre,dl,N,k,pol)
    print(pol, 'births', u.births, 'centre tokens after', u.delta[0], u.delta[1], '| swap centres (0 1) equivariant:', equiv(pre,dl,N,k,pol,(1,0,2,3,4)))
