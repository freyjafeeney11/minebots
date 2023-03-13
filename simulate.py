from cmath import pi
import pybullet as p
import random as random
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()
simulation.Get_Fitness()