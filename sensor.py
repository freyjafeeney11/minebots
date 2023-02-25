from cmath import pi
import pybullet as p
import random as random
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import constants as c

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        #moved frontlegsensors into sensor constructor. was this right?
        self.values = numpy.zeros(1000)

    def Get_Value(self, time):
        #step 63
        self.values[time] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
    
    def Save_Values(self):
        numpy.save("data/data.npy", self.values, allow_pickle=True, fix_imports=True)