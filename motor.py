from cmath import pi
import pybullet as p
import random as random
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        self.amplitude = pi/2
        self.frequency = 10
        self.phaseOffset = pi/9
        self.motorValues = (self.amplitude * numpy.sin((self.frequency * (numpy.linspace(0, 2*numpy.pi, 1000)) + self.phaseOffset)))
    
    def Set_Value(self, time, robot):
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = self.motorValues[time], #random.uniform(-pi/4.0, pi/4.0),
        maxForce = 500
        )