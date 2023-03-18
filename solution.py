import numpy as np
import time
import os
import random as random
import pyrosim.pyrosim as pyrosim
class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = np.array([[np.random.rand(), np.random.rand()], 
                                [np.random.rand(), np.random.rand()], 
                                [np.random.rand(), np.random.rand()]])
        self.weights = self.weights * 2 - 1


    #split into two fuctions evaluate
    def Start_Simulation(self, directOrGUI):
        self.Create_Brain()
        s = " " + str(self.myID) + " "
        os.system("python3 simulate.py " + directOrGUI + s + "&")

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"

        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.readline())
        print(self.fitness)
        f.close()
        os.system("del fitness" + str(self.myID) + ".txt")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        length = 1
        width = 1
        height = 1
        x=-2
        y=2
        z=0.5
        pyrosim.Send_Cube(name="Demo", pos=[x,y,z] , size=[length,width,height])
        pyrosim.End()
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-0.5,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.5,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[1,1,1])
        pyrosim.End()
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        #why isnt this working exactly
        for currentRow in range(0, 3):
            for currentColumn in range(0, 2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = (currentColumn+3) , weight = self.weights[currentRow][currentColumn])
        pyrosim.End()
    
    def Mutate(self):
        #step60 - i dont know if this is chosing the column correctly
        self.weights[random.randint(0,2)]
        self.weights[random.randint(0,2),random.randint(0,1)] =  random.random() * 2 - 1
    
    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
        