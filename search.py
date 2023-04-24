import os
import numpy as np
import constants as c
from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc =  PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()

avg = np.zeros(len(phc.stored)) 

avg = np.mean(phc.stored, axis = 0)

np.save('testB.npy', avg)