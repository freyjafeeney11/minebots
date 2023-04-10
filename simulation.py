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
    def __init__(self, directOrGUI, solutionID):
        self.solutionID =  solutionID
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        #p.setWindVelocity([10, 0, 0])
        self.robot = ROBOT(solutionID) 
        self.world = WORLD()  


        pyrosim.Prepare_To_Simulate(self.robot.robotId)   
        self.robot.Prepare_To_Sense()

        print("is error here?")

        for neuronName in self.robot.nn.Get_Neuron_Names():
            air_density = 1.293
            #https://en.wikipedia.org/wiki/Drag_coefficient
            drag_coefficient = 0.82
            #speed = self.robot.sensors[neuronName].velocity
            #robotid, link name, forceObj, posObj, flags

            #torso
            if neuronName == 0:
                self.area = 1.5
                self.force = -0.5*(air_density*drag_coefficient*self.area*5)

            #wings
            if neuronName == 21 | 22 | 23 | 24:
                self.area = 1.75
                self.force = -0.5*(air_density*drag_coefficient*self.area*5)
            #legs
            else:
                self.area = 0.2
                self.force = -0.5*(air_density*drag_coefficient*self.area*5)
            print("is error after apply call?")
            p.applyExternalForce(self.robot.robotId, int(neuronName), [0, 0, self.force], [0, 0, 0], p.LINK_FRAME)

        self.robot.Prepare_To_Act()

    def Run(self):
        for i in range(1000):
            p.stepSimulation()
            #step 57
            self.robot.Sense(i)
            print("is error here h?")
            self.robot.Think()
            self.robot.Act()
            #time.sleep(1/200)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()