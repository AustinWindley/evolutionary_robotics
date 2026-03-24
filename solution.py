import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time

class SOLUTION:
    
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = np.random.rand(3,2) * 2 - 1

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system(f"start /B python simulate.py {directOrGUI} {str(self.myID)}")

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = f"fitness{str(self.myID)}.txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        fitnessFile = open(fitnessFileName)
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()
        os.system(f"del {fitnessFileName}")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-2,2,0.5] , size=[1, 1, 1])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5], size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = 
                        "revolute", position = [-0.5,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = 
                        "revolute", position = [0.5,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_FrontLeg")
        for currentRow in [0,1,2]:
            for currentColumn in [0,1]:
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, 
                                    targetNeuronName=currentColumn+3, 
                                    weight=self.weights[currentRow][currentColumn])

        pyrosim.End()
    
    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Set_ID(self, newID):
        self.myID = newID
        