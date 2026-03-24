import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import time
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        if self.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)
    
    def __del__(self):
        p.disconnect()
    
    def run(self):
        for t in (range(c.run_length)):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            if self.directOrGUI == "GUI":
                time.sleep(1/120)

    def Get_Fitness(self):
        self.robot.Get_Fitness()
    