from solution import SOLUTION
import constants as c
import copy


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1


    def Evolve(self):
        for i in range(c.populationSize):
            self.parents[i].Evaluate("GUI")
            # for currentGeneration in range(c.numberOfGenerations):
            #     self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Select()
        self.Print()
    
    def Spawn(self, nextAvailableID):
        #step33 .. not sure if i did this right
        self.child.Set_ID(nextAvailableID) 
        self.child = copy.deepcopy(self.parent)
        self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if ((self.child.fitness) < (self.parent.fitness)):
            self.parent = self.child

    def Print(self):
        print("\nparent: " + str(self.parent.fitness) + " child: " + str(self.child.fitness))

    def Show_Best(self):
        pass