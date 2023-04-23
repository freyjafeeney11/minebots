import numpy as np
import time
import os
import random as random
import pyrosim.pyrosim as pyrosim
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1


    #split into two fuctions evaluate
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        s = " " + str(self.myID) + " "
        #2&>1
        os.system("python3 simulate.py " + directOrGUI + s +" 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        f = open(fitnessFileName, "r")
        #if os.path.getsize(fitnessFileName) != 0: 
        self.fitness = float(f.readline())
        print(self.fitness)
        f.close()

        os.system("rm " + str(fitnessFileName))

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        #pyrosim.Send_Cube(name="p", pos=[0,0,2] , size=[8,8,3.8])
        pyrosim.Send_Cube(name="p", pos=[6,0,3] , size=[7,4,0.05])
        pyrosim.Send_Cube(name="p2", pos=[10,0,1.5] , size=[2,2,2])
        pyrosim.End()

        #try to change it to be like dumbo? add 6 new joints and links
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        #ADD 5 TO RAISE IT UP
        pyrosim.Send_Cube(name="Torso", pos=[0,0,9] , size=[5,.5,.5], mass = 3)

        pyrosim.Send_Joint( name = "Torso_Head" , parent= "Torso" , child = "Head" , type = "revolute", position = [-0.5,4,9], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="Head", pos=[3,-4,0] , size=[1,1.5,1], mass = 1)


        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,9], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2], mass = 0.5)

        #back leg lower
        pyrosim.Send_Joint( name = "BackLeg_BackLegLow" , parent= "BackLeg" , child = "BackLegLow" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLegLow", pos=[0,0,-0.5] , size=[0.2,0.2,1],  mass = 0.5)

        #front 
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,9], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2], mass = 0.5)
        #front lower - this is right

        pyrosim.Send_Joint( name = "FrontLeg_FrontLegLow" , parent= "FrontLeg" , child = "FrontLegLow" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLegLow", pos=[0,0,-0.5] , size=[0.2,0.2,1],  mass = 0.5)  
        #left

        #this one is at the neck
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0,9], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1,0.2,0.2], mass = 0.5)

        #lower
        pyrosim.Send_Joint( name = "LeftLeg_LeftLegLow" , parent= "LeftLeg" , child = "LeftLegLow" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLegLow", pos=[0,0,-0.5] , size=[0.2,0.2,1], mass = 0.5)

        #right
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0,9], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1,0.2,0.2], mass = 0.5)

        #right leg low
        pyrosim.Send_Joint( name = "RightLeg_RightLegLow" , parent= "RightLeg" , child = "RightLegLow" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLegLow", pos=[0,0,-0.5] , size=[0.2,0.2,1],  mass = 0.5)

        #final proj
        pyrosim.Send_Joint( name = "Torso_LeftFrontWing" , parent= "Torso" , child = "LeftFrontWing" , type = "revolute", position = [0.25,-1,9], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftFrontWing", pos=[0,-1,0] , size=[0.5,3,0.01], mass = 0.2)
        pyrosim.Send_Joint( name = "Torso_RightFrontWing" , parent= "Torso" , child = "RightFrontWing" , type = "revolute", position = [0.25,0,9], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightFrontWing", pos=[0,2,0] , size=[0.5, 3,0.01], mass = 0.2)
    
        pyrosim.Send_Joint( name = "Torso_LeftBackWing" , parent= "Torso" , child = "LeftBackWing" , type = "revolute", position = [-0.25,-1,9], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftBackWing", pos=[-0.25,-1,0] , size=[0.75,3,0.01], mass = 0.2)
        pyrosim.Send_Joint( name = "Torso_RightBackWing" , parent= "Torso" , child = "RightBackWing" , type = "revolute", position = [-0.25,0,9], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightBackWing", pos=[-0.25,2,0] , size=[0.75, 3,0.01], mass = 0.2)

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "LeftLegLow")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "FrontLegLow")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "RightLegLow")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "BackLegLow")
        pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "LeftFrontWing")
        pyrosim.Send_Sensor_Neuron(name = 10 , linkName = "RightFrontWing")
        pyrosim.Send_Sensor_Neuron(name = 11 , linkName = "LeftBackWing")
        pyrosim.Send_Sensor_Neuron(name = 12 , linkName = "RightBackWing")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 17 , jointName = "LeftLeg_LeftLegLow")
        pyrosim.Send_Motor_Neuron( name = 18 , jointName = "FrontLeg_FrontLegLow")
        pyrosim.Send_Motor_Neuron( name = 19 , jointName = "RightLeg_RightLegLow")
        pyrosim.Send_Motor_Neuron( name = 20 , jointName = "BackLeg_BackLegLow")
        pyrosim.Send_Motor_Neuron( name = 21 , jointName = "Torso_LeftFrontWing")
        pyrosim.Send_Motor_Neuron( name = 22 , jointName = "Torso_RightFrontWing")
        pyrosim.Send_Motor_Neuron( name = 23 , jointName = "Torso_RightBackWing")
        pyrosim.Send_Motor_Neuron( name = 24 , jointName = "Torso_RightBackWing")
        #why isnt this working exactly
        for currentRow in range(0, c.numSensorNeurons):
            for currentColumn in range(0, c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = (currentColumn+c.numSensorNeurons) , weight = self.weights[currentRow][currentColumn])
        pyrosim.End()
    
    def Mutate(self):
        #this could be wrong
        self.weights[random.randint(0,c.numMotorNeurons),random.randint(0,1)] =  random.random() * c.numMotorNeurons - 1
    
    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

        