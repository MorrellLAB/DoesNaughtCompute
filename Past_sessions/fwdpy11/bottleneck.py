# matplotlib inline
# pylab inline

from __future__ import print_function
import numpy as np
import array
import matplotlib.pyplot as plt

#population size
N=1000
#nlist corresponds to a constant population size for 10N generations
#note the "dtype" argument.  Without it, we'd be defaulting to int64,
#which is a 64-bit signed integer.
nlist=np.array([N]*(10*N),dtype=np.uint32) # syntax = [data value] * (number of values)


# bottleneck to 0.25N for 100 generations,
# recover to N for 50 generations
nlist = np.concatenate(([N]*(10*N),[int(0.25*N)]*100,[N]*50)).astype(np.int32)
plt.plot(nlist[0:])
plt.ylim(0,1.5*N)
plt.show()

