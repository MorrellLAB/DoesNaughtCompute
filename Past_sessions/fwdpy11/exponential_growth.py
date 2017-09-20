# matplotlib inline
# pylab inline
from __future__ import print_function
import numpy as np
import array
import matplotlib.pyplot as plt
#population size
N=1000

import math
N2=5*N
tgrowth=500
#G is the growth rate
G = math.exp( (math.log(N2)-math.log(N))/float(tgrowth) )
nlist = np.array([N]*(10*N+tgrowth),dtype=np.uint32)
#Now, modify the list according to expoential growth rate
for i in range(tgrowth):
     nlist[10*N+i] = round( N*math.pow(G,i+1) )
##Now, we see that the population does grown from
##N=1,000 to N=5,000 during the last 500 generations
## We need the + 1 below to transform
## from the generation's index to the generation itself
plt.plot(nlist[0:]) # Show the whole population 
plt.show()
plt.plot(range(10*N+1,10*N+501,1),nlist[10*N:]) # Show just the population increase
plt.show()