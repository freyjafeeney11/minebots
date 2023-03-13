from cmath import pi
import pybullet as p
import random as random
import sys as sys
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
from simulation import SIMULATION

directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()