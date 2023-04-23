import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import numpy as np 

phc =  PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
np.save('testA.npy', phc.stored)