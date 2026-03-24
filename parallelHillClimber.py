from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    
    def __init__(self):
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION()
        

    def Evolve(self):
        # self.parent.Evaluate("GUI")
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()
        for i in self.parents.keys():
            self.parents[i].Evaluate("GUI")

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        print(f"\nparent: {self.parent.fitness} child: {self.child.fitness}")
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
    
    def Mutate(self):
        self.child.Mutate()
    
    def Select(self):
        if (self.parent.fitness > self.child.fitness):
            self.parent = self.child

    def Show_Best(self):
        # self.parent.Evaluate("GUI")
        pass