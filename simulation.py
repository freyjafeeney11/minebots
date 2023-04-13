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
        #p.setWindVelocity(0, 0, 10)

        #p.setWindVelocity([10, 0, 0])
        self.robot = ROBOT(solutionID) 
        # for neuronName in range(13):
        #     air_density = 1.293
        #     #https://en.wikipedia.org/wiki/Drag_coefficient
        #     drag_coefficient = 0.5
        #     #speed = self.robot.sensors[neuronName].velocity
        #     #robotid, link name, forceObj, posObj, flags

        #     #torso
            
        #     if neuronName == 0:
        #         self.area = 1
        #         self.force = -0.5*(air_density*drag_coefficient*self.area*5)

        #      #wings
        #     if neuronName == 9 or 10 or 11 or 12:
        #         self.area = 0.05
        #         self.force = -0.5*(air_density*drag_coefficient*self.area*5)
        #     #legs
        #     else:
        #         self.area = 0.2
        #     self.force = -0.5*(air_density*drag_coefficient*self.area*5)
        #     p.applyExternalForce(self.robot.robotId, neuronName, [0, 0, self.force], [0, 0, 0], p.LINK_FRAME)
        #     print("applied force to " + str(neuronName))

        self.world = WORLD()  
        # for i in range(12):
        #     p.applyExternalForce(self.robot.robotId, i, [0, 0, 10], [0, 0, 0], p.LINK_FRAME)


        pyrosim.Prepare_To_Simulate(self.robot.robotId)   
        self.robot.Prepare_To_Sense()


        self.robot.Prepare_To_Act()

    def Run(self):
        for i in range(1000):
            p.stepSimulation()

            v, _ = p.getBaseVelocity(self.robot.robotId)
            mag = numpy.linalg.norm(v)
            direction = [-v[i]/mag for i in range(3)]
            direction = numpy.array(direction)

            self.force = -0.5*(1.293*0.5*1.5*mag**2)


            p.applyExternalForce(self.robot.robotId, -1, forceObj = [30,0,0], posObj = [0, 0, 0], flags = p.LINK_FRAME)
            p.applyExternalForce(self.robot.robotId, -1, forceObj = direction*self.force, posObj = [0, 0, 0], flags = p.LINK_FRAME)


            #step 57
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()
            #time.sleep(1/200)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()