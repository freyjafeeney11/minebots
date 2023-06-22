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
        #pyrosim.Send_Cube(name="p", pos=[6,0,3] , size=[7,4,0.05])
        #pyrosim.Send_Cube(name="p2", pos=[10,0,1.5] , size=[2,2,2])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        #ADD 5 TO RAISE IT UP
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[2,1,0.5], mass = 15)

#NECK
        pyrosim.Send_Joint( name = "Torso_Neck" , parent= "Torso" , child = "Neck" , type = "revolute", position = [0.75,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="Neck", pos=[0.25,0,0.5] , size=[0.2,0.2,0.5], mass = 0)

#NEWLY ADDED HEAD
        pyrosim.Send_Joint( name = "Neck_Head" , parent= "Neck" , child = "Head" , type = "fixed", position = [0,0,0.5], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="Head", pos=[0.5,0,0.25] , size=[1,0.5,0.5], mass = 0)

        pyrosim.Send_Joint( name = "Torso_Thigh" , parent= "Torso" , child = "Thigh" , type = "fixed", position = [-0.75,-0.2,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="Thigh", pos=[0,-0.5,0] , size=[0.2,0.5,0.2], mass = 5)
        pyrosim.Send_Joint( name = "Thigh_BackLeg" , parent= "Thigh" , child = "BackLeg" , type = "revolute", position = [0,-0.5,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.25,0,0,0] , size=[.5,0.2,0.2], mass = 1)
        #back leg lower
        pyrosim.Send_Joint( name = "BackLeg_BackLegLow" , parent= "BackLeg" , child = "BackLegLow" , type = "revolute", position = [-.5,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLegLow", pos=[0,0,-.5] , size=[0.2,0.2,1],  mass = 5)


        #right
        pyrosim.Send_Joint( name = "Torso_ThighRight" , parent= "Torso" , child = "ThighRight" , type = "fixed", position = [-0.75,0.2,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="ThighRight", pos=[0,0.5,0] , size=[0.2,0.5,0.2], mass = 5)
        pyrosim.Send_Joint( name = "ThighRight_RightLeg" , parent= "ThighRight" , child = "RightLeg" , type = "revolute", position = [0,0.5,0], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name="RightLeg", pos=[-0.25,0,0] , size=[.5,0.2,0.2], mass = 1)
        #right leg low
        pyrosim.Send_Joint( name = "RightLeg_RightLegLow" , parent= "RightLeg" , child = "RightLegLow" , type = "revolute", position = [-.5,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLegLow", pos=[0,0,-.5] , size=[0.2,0.2,1],  mass = 5)

        #front 
        #[foward(pos)/backward(neg), left(pos)/right(neg), up(pos)/down(neg)]
        #Front Thigh
        pyrosim.Send_Joint( name = "Torso_ThighFront" , parent= "Torso" , child = "ThighFront" , type = "fixed", position = [0.75,0.2,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="ThighFront", pos=[0,0.5,0] , size=[0.2,0.5,0.2], mass = 0.1)
        pyrosim.Send_Joint( name = "ThighFront_FrontLeg" , parent= "ThighFront" , child = "FrontLeg" , type = "revolute", position = [0,0.5,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[-0.25,0,0] , size=[.5,0.2,0.2], mass = .5)
        #front lower 
        pyrosim.Send_Joint( name = "FrontLeg_FrontLegLow" , parent= "FrontLeg" , child = "FrontLegLow" , type = "revolute", position = [-.5,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLegLow", pos=[0,0,-.5] , size=[0.2,0.2,1],  mass = .5)  
        #left


        pyrosim.Send_Joint( name = "Torso_ThighLeft" , parent= "Torso" , child = "ThighLeft" , type = "fixed", position = [0.75,-0.2,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="ThighLeft", pos=[0,-0.5,0] , size=[0.2,0.5,0.2], mass = 0.1)
        pyrosim.Send_Joint( name = "ThighLeft_LeftLeg" , parent= "ThighLeft" , child = "LeftLeg" , type = "revolute", position = [0,-0.5,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.25,0,0] , size=[.5,0.2,0.2], mass = .5)
        #lower
        pyrosim.Send_Joint( name = "LeftLeg_LeftLegLow" , parent= "LeftLeg" , child = "LeftLegLow" , type = "revolute", position = [-.5,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLegLow", pos=[0,0,-.5] , size=[0.2,0.2,1], mass = .5)



        #final proj - WINGS HERE
        # pyrosim.Send_Joint( name = "Torso_LeftUpperWing" , parent= "Torso" , child = "LeftUpperWing" , type = "revolute", position = [0,0.5,9.5], jointAxis = "0 1 0")
        # pyrosim.Send_Cube(name="LeftUpperWing", pos=[0,-1.5,0] , size=[1.5,1.25,0.01], mass = 0.2)
        # pyrosim.Send_Joint( name = "Torso_RightUpperWing" , parent= "Torso" , child = "RightUpperWing" , type = "revolute", position = [0,-0.5,9.5], jointAxis = "0 1 0")
        # pyrosim.Send_Cube(name="RightUpperWing", pos=[0,1.5,0] , size=[1.5, 1.25,0.01], mass = 0.2)

        # #end wings
        # pyrosim.Send_Joint( name = "LeftUpperWing_LeftEndWing" , parent= "LeftUpperWing" , child = "LeftEndWing" , type = "revolute", position = [0,0.5,0], jointAxis = "0 1 0")
        # pyrosim.Send_Cube(name="LeftEndWing", pos=[0,-3,0] , size=[1,1,0.01], mass = 0.2)
        # pyrosim.Send_Joint( name = "RightUpperWing_RightEndWing" , parent= "RightUpperWing" , child = "RightEndWing" , type = "revolute", position = [0,-0.5,0], jointAxis = "0 1 0")
        # pyrosim.Send_Cube(name="RightEndWing", pos=[0,3,0] , size=[1,1,0.01], mass = 0.2)

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
        #pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "LeftUpperWing")
        #pyrosim.Send_Sensor_Neuron(name = 10 , linkName = "RightUpperWing")
        #pyrosim.Send_Sensor_Neuron(name = 11 , linkName = "LeftEndWing")
        #pyrosim.Send_Sensor_Neuron(name = 12 , linkName = "RightEndWing")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Thigh_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "ThighFront_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "ThighLeft_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "ThighRight_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "LeftLeg_LeftLegLow")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "FrontLeg_FrontLegLow")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "RightLeg_RightLegLow")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "BackLeg_BackLegLow")

        #head?
        pyrosim.Send_Sensor_Neuron(name = 17 , linkName = "Head")
        pyrosim.Send_Motor_Neuron( name = 18 , jointName = "Neck_Head")
        pyrosim.Send_Sensor_Neuron(name = 19 , linkName = "Neck")
        pyrosim.Send_Motor_Neuron( name = 20 , jointName = "Torso_Neck")
        pyrosim.Send_Sensor_Neuron(name = 21 , linkName = "Thigh")
        pyrosim.Send_Motor_Neuron( name = 22 , jointName = "Torso_Thigh")
        pyrosim.Send_Sensor_Neuron(name = 23 , linkName = "ThighFront")
        pyrosim.Send_Motor_Neuron( name = 24 , jointName = "Torso_ThighFront")

        pyrosim.Send_Sensor_Neuron(name = 25 , linkName = "ThighLeft")
        pyrosim.Send_Motor_Neuron( name = 26 , jointName = "Torso_ThighLeft")
        pyrosim.Send_Sensor_Neuron(name = 27 , linkName = "ThighRight")
        pyrosim.Send_Motor_Neuron( name = 28 , jointName = "Torso_ThighRight")
        # pyrosim.Send_Motor_Neuron( name = 21 , jointName = "Torso_LeftUpperWing")
        # pyrosim.Send_Motor_Neuron( name = 22 , jointName = "Torso_RightUpperWing")
        # pyrosim.Send_Motor_Neuron( name = 23 , jointName = "LeftUpperWing_LeftEndWing")
        # pyrosim.Send_Motor_Neuron( name = 24 , jointName = "RightUpperWing_RightEndWing")
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

        