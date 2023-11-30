from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        self.stored = np.zeros((c.populationSize, c.numberOfGenerations))
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)
            # interactive
            if currentGeneration % 5 == 0:
                self.Prompt_User(currentGeneration)
                # write guess to a file and generation number
    
    def Evolve_For_One_Generation(self, currentGeneration):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select(currentGeneration)
        #self.Print()
    
    def Prompt_User(self, currentGeneration):
       if currentGeneration % 5 == 0:
            self.Show_Best()
            guess = input(f"Generation {currentGeneration}, What emotion does the robot look like it is portraying?: ")
            with open('user_guesses.txt', 'a') as file:
                file.write(f"Generation {currentGeneration}, User guess - {guess}\n")

    
    def Spawn(self):
        self.children = {}
        #this could be where the error is
        for i in range(c.populationSize):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

        #step33 .. not sure if i did this right
        # self.child.Set_ID(nextAvailableID) 
        # self.child = copy.deepcopy(self.parent)
        # self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        for i in self.children:
            c = self.children[i]
            c.Mutate()

    def Select(self, currentGeneration):
        for i in range(c.populationSize):
            #maximum
            if ((self.children[i].fitness) > (self.parents[i].fitness)):
                self.parents[i] = self.children[i]
                self.stored[i, currentGeneration] = self.parents[i].fitness

    def Print(self):
        for i in self.parents.keys():
            print("  \n")
            print("\nparent: " + str(self.parents[i].fitness) + " child: " + str(self.children[i].fitness) + "\n")
            print("  \n")

    def Show_Best(self):
        #maximum
        minval = -1000;
        for i in self.parents.keys():
            if self.parents[i].fitness > minval:
                minval = self.parents[i].fitness

        for i in self.parents.keys():
            if self.parents[i].fitness == minval:
                self.parents[i].Start_Simulation("GUI")
                print("best fitness: " + str(self.parents[i].fitness))

    def Evaluate(self, solutions):
        for i in range(0, c.populationSize):
            solutions[i].Start_Simulation("DIRECT")
        for i in range(0, c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()