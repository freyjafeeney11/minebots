import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import numpy as np 

phc =  PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
avg = np.zeros(len(phc.stored)) 

avg = np.mean(phc.stored, axis = 0)

np.save('testA.npy', avg)