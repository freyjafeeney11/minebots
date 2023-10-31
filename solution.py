import time
import numpy as np
import os
import random as random
import pyrosim.pyrosim as pyrosim
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = np.random.rand(c.numSensorNeurons, c.numHiddenNeurons)
        self.weights = self.weights * 2 - 1
        self.weights2 = np.random.rand(c.numHiddenNeurons, c.numMotorNeurons)
        self.weights2 = self.weights2 * 2 - 1


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
        #guess = input("what emotion is being portrayed: ")
        print(self.fitness)
        f.close()

        os.system("rm " + str(fitnessFileName))

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def Create_Body(self):

        pyrosim.Start_URDF("body.urdf")

        #ADD 5 TO RAISE IT UP
        pyrosim.Send_Cube(name="Head", pos=[0.5,0,0.25] , size=[1,0.5,0.5], mass =0)
        pyrosim.Send_Cube(name="Neck", pos=[0.25,0,0.5] , size=[0.2,0.2,0.5], mass = 0)
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[2,1,0.5], mass = 15)
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.25,0,0,0] , size=[.5,0.2,0.2], mass = 1)
        pyrosim.Send_Cube(name="FrontLeg", pos=[-0.25,0,0] , size=[.5,0.2,0.2], mass = .5)
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.25,0,0] , size=[.5,0.2,0.2], mass = .5)
        pyrosim.Send_Cube(name="RightLeg", pos=[-0.25,0,0] , size=[.5,0.2,0.2], mass = 5)
        pyrosim.Send_Cube(name="LeftLegLow", pos=[0,0,-.5] , size=[0.2,0.2,1], mass = .5)
        pyrosim.Send_Cube(name="FrontLegLow", pos=[0,0,-.5] , size=[0.2,0.2,1],  mass = .5)  
        pyrosim.Send_Cube(name="RightLegLow", pos=[0,0,-.5] , size=[0.2,0.2,1],  mass = 5)
        pyrosim.Send_Cube(name="BackLegLow", pos=[0,0,-.5] , size=[0.2,0.2,1],  mass = 5)
        pyrosim.Send_Cube(name="Thigh", pos=[0,-0.5,0] , size=[0.2,0.5,0.2], mass = 5)
        pyrosim.Send_Cube(name="ThighFront", pos=[0,0.5,0] , size=[0.2,0.5,0.2], mass = 0.1)
        pyrosim.Send_Cube(name="ThighLeft", pos=[0,-0.5,0] , size=[0.2,0.5,0.2], mass = 0.1)
        pyrosim.Send_Cube(name="ThighRight", pos=[0,0.5,0] , size=[0.2,0.5,0.2], mass = 5)
        pyrosim.Send_Cube(name="TorsoSensor", pos=[0, 0.82, 0.5], size=[1, 0.01, 0.4], mass=0)



        #added sensors
        pyrosim.Send_Joint( name = "Neck_Head" , parent= "Neck" , child = "Head" , type = "fixed", position = [0,0,0.5], jointAxis = "0 1 0")
        pyrosim.Send_Joint( name = "Torso_Neck" , parent= "Torso" , child = "Neck" , type = "revolute", position = [0.75,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Joint( name = "Torso_Thigh" , parent= "Torso" , child = "Thigh" , type = "fixed", position = [-0.75,-0.2,1], jointAxis = "0 1 0")
        pyrosim.Send_Joint( name = "Thigh_BackLeg" , parent= "Thigh" , child = "BackLeg" , type = "revolute", position = [0,-0.5,0], jointAxis = "0 1 0")        #back leg lower
        pyrosim.Send_Joint( name = "BackLeg_BackLegLow" , parent= "BackLeg" , child = "BackLegLow" , type = "revolute", position = [-.5,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Joint( name = "Torso_ThighRight" , parent= "Torso" , child = "ThighRight" , type = "fixed", position = [-0.75,0.2,1], jointAxis = "0 1 0")
        pyrosim.Send_Joint( name = "ThighRight_RightLeg" , parent= "ThighRight" , child = "RightLeg" , type = "revolute", position = [0,0.5,0], jointAxis = "0 1 0")
        pyrosim.Send_Joint( name = "RightLeg_RightLegLow" , parent= "RightLeg" , child = "RightLegLow" , type = "revolute", position = [-.5,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Joint( name = "Torso_ThighFront" , parent= "Torso" , child = "ThighFront" , type = "fixed", position = [0.75,0.2,1], jointAxis = "0 1 0")
        pyrosim.Send_Joint( name = "ThighFront_FrontLeg" , parent= "ThighFront" , child = "FrontLeg" , type = "revolute", position = [0,0.5,0], jointAxis = "0 1 0")
        pyrosim.Send_Joint( name = "FrontLeg_FrontLegLow" , parent= "FrontLeg" , child = "FrontLegLow" , type = "revolute", position = [-.5,0,0], jointAxis = "0 1 0")        #left
        pyrosim.Send_Joint( name = "Torso_ThighLeft" , parent= "Torso" , child = "ThighLeft" , type = "fixed", position = [0.75,-0.2,1], jointAxis = "0 1 0")
        pyrosim.Send_Joint( name = "ThighLeft_LeftLeg" , parent= "ThighLeft" , child = "LeftLeg" , type = "revolute", position = [0,-0.5,0], jointAxis = "0 1 0")        #lower
        pyrosim.Send_Joint( name = "LeftLeg_LeftLegLow" , parent= "LeftLeg" , child = "LeftLegLow" , type = "revolute", position = [-.5,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Joint( name = "Torso_TorsoSensor" , parent= "Torso" , child = "TorsoSensor" , type = "fixed", position = [0,0,0.5], jointAxis = "0 1 0")

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Head")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Neck")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLegLow")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "FrontLegLow")
        pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "RightLegLow")
        pyrosim.Send_Sensor_Neuron(name = 10 , linkName = "BackLegLow")
        pyrosim.Send_Sensor_Neuron(name = 11 , linkName = "Thigh")
        pyrosim.Send_Sensor_Neuron(name = 12 , linkName = "ThighFront")
        pyrosim.Send_Sensor_Neuron(name = 13 , linkName = "ThighLeft")
        pyrosim.Send_Sensor_Neuron(name = 14 , linkName = "ThighRight")
        pyrosim.Send_Sensor_Neuron( name = 15 , linkName = "TorsoSensor")
        pyrosim.Send_Hidden_Neuron( name = 16 )
        pyrosim.Send_Hidden_Neuron( name = 17 )
        pyrosim.Send_Hidden_Neuron( name = 18 )
        pyrosim.Send_Hidden_Neuron( name = 19 )
        pyrosim.Send_Hidden_Neuron( name = 20 )
        pyrosim.Send_Hidden_Neuron( name = 21 )
        pyrosim.Send_Hidden_Neuron( name = 22 )
        pyrosim.Send_Hidden_Neuron( name = 23 )
        pyrosim.Send_Hidden_Neuron( name = 24 )
        pyrosim.Send_Hidden_Neuron( name = 25 )
        pyrosim.Send_Hidden_Neuron( name = 26 )
        pyrosim.Send_Hidden_Neuron( name = 27 )
        pyrosim.Send_Hidden_Neuron( name = 28 )
        pyrosim.Send_Hidden_Neuron( name = 29 )
        pyrosim.Send_Hidden_Neuron( name = 30 )
        pyrosim.Send_Hidden_Neuron( name = 31 )
        pyrosim.Send_Motor_Neuron( name = 32, jointName = "Neck_Head")
        pyrosim.Send_Motor_Neuron( name = 33 , jointName = "Torso_Neck")
        pyrosim.Send_Motor_Neuron( name = 34 , jointName = "Thigh_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 35 , jointName = "ThighFront_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 36 , jointName = "ThighLeft_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 37 , jointName = "ThighRight_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 38 , jointName = "LeftLeg_LeftLegLow")
        pyrosim.Send_Motor_Neuron( name = 39 , jointName = "FrontLeg_FrontLegLow")
        pyrosim.Send_Motor_Neuron( name = 40 , jointName = "RightLeg_RightLegLow")
        pyrosim.Send_Motor_Neuron( name = 41 , jointName = "BackLeg_BackLegLow")
        pyrosim.Send_Motor_Neuron( name = 42 , jointName = "Torso_Thigh")
        pyrosim.Send_Motor_Neuron( name = 43 , jointName = "Torso_ThighFront")
        pyrosim.Send_Motor_Neuron( name = 44 , jointName = "Torso_ThighLeft")
        pyrosim.Send_Motor_Neuron( name = 45 , jointName = "Torso_ThighRight")
        pyrosim.Send_Motor_Neuron( name = 46 , jointName = "Torso_TorsoSensor")
        
        # hidden
        for currentRow in range(0, c.numSensorNeurons):
            for currentColumn in range(0, c.numHiddenNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = (currentColumn+c.numSensorNeurons) , weight = self.weights[currentRow][currentColumn])
        
        
        for currentRow in range(0, c.numHiddenNeurons):
           for currentColumn in range(0, c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = (currentColumn+c.numHiddenNeurons) , weight = self.weights2[currentRow][currentColumn])
        # end 
        #exit()
        pyrosim.End()
    
    def Mutate(self):
    # Mutate the first weight matrix (sensor to hidden)
        for i in range(c.numSensorNeurons):
            for j in range(c.numHiddenNeurons):
                mutation = random.uniform(-1.0, 1.0)
                self.weights[i][j] += mutation
        
        # Mutate the second weight matrix (hidden to motor)
        for i in range(c.numHiddenNeurons):
            for j in range(c.numMotorNeurons):
                mutation = random.uniform(-1.0, 1.0)
                self.weights2[i][j] += mutation

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

        