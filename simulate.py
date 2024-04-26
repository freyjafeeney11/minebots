from cmath import pi
import pybullet as p
import random as random
import sys as sys
import constants as c
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
from simulation import SIMULATION

directOrGUI = sys.argv[1]
#this is throwing a error
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
p.startStateLogging(p.STATE_LOGGING_VIDEO_MP4, 'simulation.mp4')
simulation.Run()
simulation.Get_Fitness(c.motorJointRange, c.maxForce)
p.stopStateLogging(p.STATE_LOGGING_VIDEO_MP4)