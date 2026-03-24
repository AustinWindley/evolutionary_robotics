from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("def fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        

    def Evolve(self):
        # self.parent.Evaluate("GUI")
        for i in self.parents.keys():
            self.parents[i].Start_Simulation("DIRECT")
        for i in self.parents.keys():
            self.parents[i].Wait_For_Simulation_To_End()
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        # self.Mutate()
        # self.child.Evaluate("DIRECT")
        # print(f"\nparent: {self.parent.fitness} child: {self.child.fitness}")
        # self.Select()

    def Spawn(self):
        self.children = {}
        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1        
    
    def Mutate(self):
        self.child.Mutate()
    
    def Select(self):
        if (self.parent.fitness > self.child.fitness):
            self.parent = self.child

    def Show_Best(self):
        # self.parent.Evaluate("GUI")
        pass