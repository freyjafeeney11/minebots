from world import WORLD
from robot import ROBOT
from cmath import pi
import pybullet as p
import random as random
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import constants as c

class SIMULATION:
    def __init__(self):  
        #Cut the statements from simulate.py that connect to pybullet, set the additional search path, set gravity, and Prepare_To_Simulate()
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.robot = ROBOT() 
        self.world = WORLD()  
        pyrosim.Prepare_To_Simulate(self.robot.robotId)   
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()


    def Run(self):
        for i in range(1000):
            p.stepSimulation()
            #step 57
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()
            time.sleep(1/600)

    def __del__(self):
        p.disconnect()