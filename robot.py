from motor import MOTOR
from pyrosim.neuron  import NEURON
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
        #adding this to try total distance travelled instead of distance from origin
        self.total_dist = 0.0
        self.ZPrev = 0.0
        self.YPrev = 0.0
        self.XPrev = 0.0

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
        self.touchValues = 0
        # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        for sensor in self.sensors.values():
            sensor.Get_Value(t)
            # if sensor.linkName == 'BackLegLow':
            #     print(sensor.linkName)
            #     if(sensor.Get_Value(t)):
            #         self.touchValues += sensor.Get_Value(t)

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

    def Get_Fitness(self, jointRange, maxForce):

        self.basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        self.basePosition = self.basePositionAndOrientation[0]
        self.xPosition = self.basePosition[0]
        self.yPosition = self.basePosition[1]
        self.zPosition = self.basePosition[2]

        position_of_head = p.getLinkState(self.robotId, 1, computeLinkVelocity=1)
        po = p.getJointInfo(self.robotId, 1)
        z_position_of_head = position_of_head[0][2]
        # print("HERE: " + str(po))

        lying_down = p.getLinkState(self.robotId, 14, computeLinkVelocity=1)
        # -1 means touching
        lying_down = lying_down[0][2]

        # emotion = c.emotion

        with open("poll_chat.txt", "r") as twitch_pull:
            consensus = float(twitch_pull.readline().strip())
            print(f'consensus is: {str(consensus)}')

        with open("chosen_emotion.txt", "r") as file:
            emotion = file.readline().strip()
            print(emotion)
    # got the joint range to change and force
        joint_change = sum(max(0, abs(abs(self.nn.Get_Value_Of(neuronName) * c.motorJointRange) - jointRange)) for neuronName in self.nn.Get_Neuron_Names() if self.nn.Is_Motor_Neuron(neuronName))
        force_change = sum(max(0, abs(abs(self.nn.Get_Value_Of(neuronName) * c.maxForce) - maxForce)) for neuronName in self.nn.Get_Neuron_Names() if self.nn.Is_Motor_Neuron(neuronName))
        

        # happy
        if emotion == 'happy':
            self.total = consensus * (self.xPosition * 0.6) + (z_position_of_head * 0.9) + (self.zPosition * 0.5) + (joint_change * 0.05) + (force_change * 0.8)
        # sad
        if emotion == 'sad':
            self.total = consensus * (self.xPosition * 0.3) + (-z_position_of_head * 0.9) + (self.zPosition * 0.3) + (-joint_change * 0.05) + (-force_change * 0.7)
        # lazy
        if emotion == 'lazy':
            self.total = consensus * (-self.xPosition * 0.01) + (-z_position_of_head * 0.9) + (-self.zPosition * 0.5) + (-joint_change * 0.05) + (-force_change * 0.9)

        # sad
        print(z_position_of_head)

        # self.ZPrev = self.zPosition
        # self.YPrev = self.yPosition
        # self.XPrev = self.xPosition

        #write coor to file
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(self.total))
        f.close()
        os.system("mv tmp" + str(self.solutionID) + ".txt fitness" + str(self.solutionID) + ".txt")
        #return numpy.mean(self.array)