from cmath import pi
import pybullet as p
import random as random
import sys as sys
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
from simulation import SIMULATION

directOrGUI = sys.argv[1]
#this is throwing a error
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()