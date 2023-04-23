import os
import numpy as np
from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc =  PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
np.save('test.npy', phc.stored)