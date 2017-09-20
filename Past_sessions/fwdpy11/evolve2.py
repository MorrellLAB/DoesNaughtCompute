import fwdpy11 as fp11
import fwdpy11.wright_fisher as wf
import numpy as np

rng = fp11.GSLrng(42)
p = fp11.Spop(1000)
wf.evolve(rng,p)
print(p.generation)

nlist=np.array([5000]*323,dtype=np.uint32)
wf.evolve(rng,p,nlist)
print(p.N)
print(p.generation)