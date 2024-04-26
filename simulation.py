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
import os
import subprocess
import asyncio
from twitchio.ext import commands

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.solutionID =  solutionID
        self.directOrGUI = directOrGUI

        # Define the directory to save the video
        videos_dir = os.path.join(os.getcwd(), "videos")
        os.makedirs(videos_dir, exist_ok=True)  # Create the "videos" directory if it doesn't exist
        
        # Specify the full path to the video file within the "videos" directory
        video_path = os.path.join(videos_dir, "simulation.mp4")

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



            v = p.getBaseVelocity(self.robot.robotId)[0][0]
            speed_x = p.getBaseVelocity(self.robot.robotId)[0][0]

            # self.forceTorso = -0.5*(c.fluidDensity * c.dragCoefficient * 1 *float(speed_x))

            # self.forceWing = -0.5*(c.fluidDensity * c.dragCoefficient*2.5*float(speed_x))

            # self.forceLegs = -0.5*(c.fluidDensity * c.dragCoefficient*0.2*float(speed_x))

            #p.applyExternalForce(self.robot.robotId, -1, forceObj = [30,0,20], posObj = [0, 0, 0], flags = p.LINK_FRAME)

            #torso
            #p.applyExternalForce(self.robot.robotId, 0, forceObj = [0, 0, self.forceTorso], posObj = [0, 0, 0], flags = p.LINK_FRAME)

            #legs
            #for i in range(1, 8):
                #p.applyExternalForce(self.robot.robotId, i, forceObj = [0, 0, self.forceWing], posObj = [0, 0, 0], flags = p.LINK_FRAME) 

            #wings
            #for i in range(9, 12):
                 #p.applyExternalForce(self.robot.robotId, i, forceObj = [0, 0, self.forceLegs], posObj = [0, 0, 0], flags = p.LINK_FRAME)               

            #step 57
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()
            #time.sleep(1/200)
        ######################
        # Stream the recorded video to Twitch
        #self.stream_to_twitch()

        # Delete the recorded video file
        #os.remove("simulation.mp4")

    def Get_Fitness(self, motor, force):
        self.robot.Get_Fitness(c.motorJointRange, c.maxForce)

    def stream_to_twitch(self):
        async def start_stream():
            bot = TwitchBot()
            await bot.start()
            await bot.start_stream('simulation.mp4')
        
        asyncio.run(start_stream())

    def __del__(self):
        p.disconnect()