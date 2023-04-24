import os
import numpy as np
from glider import GLIDER

phc =  GLIDER()
phc.Evolve()
phc.Show_Best()

avg = np.zeros(len(phc.stored)) 

avg = np.mean(phc.stored, axis = 0)

np.save('testA.npy', avg)