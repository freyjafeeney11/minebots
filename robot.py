from motor import MOTOR
from sensor import SENSOR
from world import WORLD
from cmath import pi
import pybullet as p
import random as random
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf");
        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        for sensor in self.sensors.values():
            sensor.Get_Value(t)
    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Prepare_To_Act(self):
        self.motors= {} 
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                self.jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                self.desiredAngle = self.nn.Get_Value_Of(neuronName)
                #step 76, this is causing the problem, it cant find the index?
                #cant use b'' email ta?
                self.motors[bytes(self.jointName, 'ASCII')].Set_Value(self.desiredAngle, self.robotId)
                print(neuronName, self.jointName, self.desiredAngle)