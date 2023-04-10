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
import os
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body.urdf");
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        s = "rm brain" + str(solutionID) + ".nndf"
        os.system(s)

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
        #self.nn.Print()

    def Prepare_To_Act(self):
        self.motors= {} 
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                self.jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                self.desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                #step 76, this is causing the problem, it cant find the index?
                #cant use b'' email ta?
                self.motors[bytes(self.jointName, 'ASCII')].Set_Value(self.desiredAngle, self.robotId)
                #print(neuronName, self.jointName, self.desiredAngle)

    def Get_Fitness(self):
        #print("here now")
        self.basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        self.basePosition = self.basePositionAndOrientation[0]
        self.zPosition = self.basePosition[2]

        #for sensor in self.sensors.values():
            #sensor.Get_Value(t)
            #numpy.append(self.array, sensor.Get_Value(time))


        #write coor to file
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(self.zPosition))
        f.close()
        os.system("mv tmp" + str(self.solutionID) + ".txt fitness" + str(self.solutionID) + ".txt")
        #return numpy.mean(self.array)