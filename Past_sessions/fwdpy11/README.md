<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->



### Follow along with the presentation:

## Go to: http://z.umn.edu/fwdpy11intro

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

### Does[0]compute? 

---

# fwdpy11

### May 30, 2017

Colin Pierce

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# What is fwdpy11?

fwdpy11 combines the power of fwdpp and Python to create a powerful environment for forward-time simulation.

fwdpy11 is based on pybind11, and replaces fwdpy, which was based on Cython.


# Forward simulation basics:

---
---

![](https://github.com/cpthrash/simulation_projects/blob/master/DriftN100.png?raw=true)


Yuan X, Miller DJ, Zhang J, Herrington D, Wang Y. An Overview of Population Genetic Data Simulation. Journal of Computational Biology. 2012;19(1):42-54. doi:10.1089/cmb.2010.0188.

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Common parameters
---

- Population data: array/vector
- Ploidy
- Number of generations
- Selection coefficent(s)
- Mutation
      - Neutral
      - Non-neutral
- Number of chromosomes
- Number of loci under selection
- Recombination
- Migration 
- Fitness model

![](https://cdn3.iconfinder.com/data/icons/linecons-free-vector-icons-pack/32/params-512.png)

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Population basics: A worked example
---

```
from __future__ import print_function
import numpy as np
import array
import matplotlib.pyplot as plt
```

population size

```
N=1000
```

nlist corresponds to a constant population size for 10N generations
note the "dtype" argument.  Without it, we'd be defaulting to int64,
which is a 64-bit signed integer.

```
nlist=np.array([N]*(10*N),dtype=np.uint32)
```

syntax = [data value] * (number of values)

bottleneck to 0.25N for 100 generations,
recover to N for 50 generations

```
nlist = np.concatenate(([N]*(10*N),[int(0.25*N)]*100,[N]*50)).astype(np.int32)
plt.plot(nlist[0:])
plt.ylim(0,1.5*N)
plt.show()
```


#### Potential caveat
Getting the integer type incorrect. With numpy, it must by dtype=uint32. With array.array, it must be ‘I’. Getting it wrong will result in a run-time error.

#### Why do things with NumPy arrays or Python’s array.array? Lots of reasons:

- They are fast
- The uint32 is the same type used in fwdpp
- The 32 bit integer takes half the memory as the default 64 bit intger type of a Python list.

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Population Basics: Exponential Growth
---

```
from __future__ import print_function
import numpy as np
import array
import matplotlib.pyplot as plt
```

population size

```N=1000
import math
N2=5*N
tgrowth=500
```


G is the growth rate

```
G = math.exp( (math.log(N2)-math.log(N))/float(tgrowth) )
nlist = np.array([N]*(10*N+tgrowth),dtype=np.uint32)
```


Now, modify the list according to expoential growth rate

```
for i in range(tgrowth):
     nlist[10*N+i] = round( N*math.pow(G,i+1) )
```


Now, we can show that the population does indeed grown from N=1,000 to N=5,000 during the last 500 generations
We need the + 1 below to transform from the generation's index to the generation itself

```
plt.plot(nlist[0:]) # Show the whole population 
plt.show()
plt.plot(range(10*N+1,10*N+501,1),nlist[10*N:]) # Show just the population increase
plt.show()
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# sPop

#### class fwdpy11.fwdpy11_types.Spp
Bases: ```
fwdpy11.fwdpy11_types.SinglepopBase
```

sPop is a population object representing a single deme.

```
N
```

- The current population size.


```
diploids
```

- A fwdpy11.fwdpy11_types.DiploidContainer.

```
fixation_times
```

- A list of fixation times corresponding to the elements in “fixations” for this type.

```
fixations
```

- A fwdpy11.fwdpp_types.MutationContainer of fixed variants.

```
gametes
```

- A fwdpy11.fwdpp_types.GameteContainer.

```
generation
```

- The current generation. A population starts at generation 0:

```
mcounts
```

- List of number of occurrences of elements in a population objecst “mutations” container.



#### Note
Some values may be 0. These represent extinct variants. You will typically want to avoid processing such mutations.

```
mutations
```

- List of fwdpy11.fwdpp_types.Mutation.

#### Note
The mutations list contains both extinct and extant mutations. To distinguish them, use the locations of nonzero values in “mcounts” for an instance of this type.”

#### Example

```
import fwdpy11
p = fwdpy11.Spop(1000)
print(p.N)
import numpy as np
import fwdpy11.wright_fisher as wf
```

Evolve to a final N of 500

```
nlist = np.array([p.N]*100 + [p.N/2]*100,dtype = np.uint32)
rng=fwdpy11.GSLrng(101)
wf.evolve(rng,p,nlist)
print(p.N)
print(p.generation)
```

The output from the above is:

```
1000
500
200
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# A simple evolution simulation

```
import fwdpy11 as fp11
import fwdpy11.wright_fisher as wf
import numpy as np
```

```
rng = fp11.GSLrng(42)
p = fp11.Spop(1000)
wf.evolve(rng,p)
print(p.generation)
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Another evolution simulation

```
import fwdpy11 as fp11
import fwdpy11.wright_fisher as wf
import numpy as np
```

```
rng = fp11.GSLrng(42)
p = fp11.Spop(1000)
wf.evolve(rng,p)
```


```
nlist=np.array([5000]*323,dtype=np.uint32)
wf.evolve(rng,p,nlist)
print(p.N)
print(p.generation)
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Selection

Options for selection implementation:
- Constant/fixed s
- Exponential distribution of s
- Gamma distribution of s
- Gaussian distribution of s
- Uniform distribution of s


#### class fwdpy11.regions.ExpS(beg, end, weight, mean, h=1.0, coupled=True, label=0)
Bases: ```fwdpy11.regions.Sregion```

Exponential distribution on selection coefficients

Parameters:	
- beg – the beginning of the region
- end – the end of the region
- weight – the weight to assign
- mean – the mean selection coefficient
- h – the dominance
- coupled – if True, the weight is converted to (end-beg)*weight
- label – Not relevant to recombining regions. Otherwise, this value will be used to take mutations from this region.

When coupled is True, the “weight” may be interpreted as a “per base pair” (or per unit, generally speaking) term.

#### Simple example:

```
import fwdpy11
```
#s is exp(-0.1) and recessive

```
constantS = fwdpy11.ExpS(0,1,1,0,-0.1,0)
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Regions

#### class fwdpy11.regions.Region(beg, end, weight, coupled=True, label=0)
Bases: ```object```

Representation of a “region” in a simulation.

Parameters:	
- beg – the beginning of the region
- end – the end of the region
- weight – the weight to assign
- coupled – if True, the weight is converted to (end-beg)*weight
- label – Not relevant to recombining regions. Otherwise, this value will be used to take mutations from this region.

When coupled is True, the “weight” may be interpreted as a “per base pair” (or per unit, generally speaking) term.

#### Example:

```
import fwdpy11
r = fwdpy11.Region(0,1,1)
```

A more "biological" case:
 The region covers positions 1 through 1,000, and the per-base pair "weight" is 1e-5:

```
r = fwdpy11.Region(1,1000,1e-5,True)
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Putting it all together

```
import fwdpy11 as fp11
import fwdpy11.wright_fisher as wf
import numpy as np
import fwdpy11.regions
```

```
rng = fp11.GSLrng(42)
p = fp11.Spop(1000)
print(p.N)
nlist=np.array([p.N]*323,dtype=np.uint32)
```

Our "neutral" regions will be from positions [0,1000) and [2000,3000). The regions will have equal weights, and thus will each get 1/2 of newly-arising, neutral mutations

```
nregions = [fp11.Region(0,1000,1),fp11.Region(2000,3000,1)]
```

Our "selected" regions will have positions on the continuous interval [1000,2000).  There will be two classes of such mutations, each with exponentially-distrubted selection coefficients. The first class will have a mean of s = -0.1 (deleterious), and the second will have a mean of 1e-3 (adaptive).  The former will be 100x more common than the latter, as the weights are 1 and 0.01, respectively.

```
sregions = [fp11.ExpS(1000,2000,1,-0.1),fp11.ExpS(1000,2000,.01,.01)]
```

Recombination will be uniform along the interval [0,3000).

```
rregions = [fp11.Region(0,3000,1)]
```

Neutral mutation rate

```
mu_neutral = 0.0001
```

Selected mutation rate

```
mu_selected = 0.0000005
```

Recombination

```
rec_rate = 0.005
```

```
wf.evolve_regions(rng,p,nlist,mu_neutral,mu_selected,rec_rate,nregions,sregions,rregions)
print(p.N)
print(p.generation)
```

Output should be:

```
1000
1000
323
```