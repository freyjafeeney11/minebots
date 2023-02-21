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

    def run(self):
        for i in range(1000):
            print(i)
            p.stepSimulation()
            # pyrosim.Set_Motor_For_Joint(
            # bodyIndex = robotId,
            # jointName = b'Torso_BackLeg',
            # controlMode = p.POSITION_CONTROL,
            # targetPosition = b_targetVec[i], #random.uniform(-pi/4.0, pi/4.0),
            # maxForce = c.maxForce
            # )
            # pyrosim.Set_Motor_For_Joint(
            # bodyIndex = robotId,
            # jointName = b'Torso_FrontLeg',
            # controlMode = p.POSITION_CONTROL,
            # targetPosition = f_targetVec[i], #random.uniform(-pi/2.0, pi/2.0),
            # maxForce = c.maxForce
            # )
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            time.sleep(1/240)
