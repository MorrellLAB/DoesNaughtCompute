import fwdpy11 as fp11
import fwdpy11.wright_fisher as wf
import numpy as np
import fwdpy11.regions 



rng = fp11.GSLrng(42)
p = fp11.Spop(1000)
print(p.N)
nlist=np.array([p.N]*323,dtype=np.uint32)


#Our "neutral" regions will be from positions [0,1000) and [2000,3000).
#The regions will have equal weights, and thus will each get
#1/2 of newly-arising, neutral mutations
nregions = [fp11.Region(0,1000,1),fp11.Region(2000,3000,1)]

#Our "selected" regions will have positions on the continuous
#interval [1000,2000).  There will be two classes of such mutations,
#each with exponentially-distrubted selection coefficients.
#The first class will have a mean of s = -0.1 (deleterious), and the second
#will have a mean of 1e-3 (adaptive).  The former will be 100x more common than
#the latter, as the weights are 1 and 0.01, respectively.
sregions = [fp11.ExpS(1000,2000,1,-0.1),fp11.ExpS(1000,2000,.01,.01)]

#Recombination will be uniform along the interval [0,3000).
rregions = [fp11.Region(0,3000,1)]

# Neutral mutation rate
mu_neutral = 0.0001

# Selected mutation rate
mu_selected = 0.0000005

# Recombination
rec_rate = 0.005

wf.evolve_regions(rng,p,nlist,mu_neutral,mu_selected,rec_rate,nregions,sregions,rregions)
print(p.N)
print(p.generation)