"""TDR-G owner-session probe (27 Oct 2026): is the pinned v18 step equivariant under the mirror (theta,delta)->(-theta,-delta)? usage: python3 -I mirror_probe.py ENGINE.py"""
import importlib.util, sys, itertools, random
spec = importlib.util.spec_from_file_location("eng", sys.argv[1]); eng = importlib.util.module_from_spec(spec); sys.modules["eng"]=eng; spec.loader.exec_module(eng)
N=24; k=1; rng=random.Random(1); n=0; fail=0; pathfail=0; paths=0
def step(th,dl):
    u=eng.Universe(N=N,k=k,theta=dict(th),delta=dict(dl)); eng.step_universe(u,"bound_symmetric"); return u
for _ in range(60000):
    th={i:rng.randrange(N) for i in range(3)}; dl={i:rng.randrange(N) for i in range(3)}
    u=step(th,dl); m=step({i:(-t)%N for i,t in th.items()},{i:(-d)%N for i,d in dl.items()})
    ok = all(m.theta[i]==(-u.theta[i])%N and m.delta[i]==(-u.delta[i])%N for i in range(3))
    n+=1; fail+= (not ok); paths += (u.path_interactions>0); pathfail += (not ok and u.path_interactions>0)
print(f"mirror (theta,delta)->(-theta,-delta), N=24 k=1, 3 nodes, {n} random states: step-equivariance failures {fail}; states with a P3 event {paths}; failures among them {pathfail}")
