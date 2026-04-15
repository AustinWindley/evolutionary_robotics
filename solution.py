import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
class SOLUTION:
    
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        #self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons) * 2 - 1
        self.sensorToHiddenWeights = np.random.rand(c.numSensorNeurons, c.numHiddenNeurons) * 2 - 1
        self.hiddenToMotorWeights = np.random.rand(c.numHiddenNeurons, c.numMotorNeurons) * 2 - 1
        self.linkNames = ["Torso", "BackLeg", "FrontLeg", "LeftLeg", "RightLeg", 
                          "LowerBackLeg", "LowerFrontLeg", "LowerLeftLeg", "LowerRightLeg"]
        self.jointNames = ["Torso_BackLeg", "Torso_FrontLeg", "Torso_LeftLeg", "Torso_RightLeg", "BackLeg_LowerBackLeg", 
                           "FrontLeg_LowerFrontLeg", "LeftLeg_LowerLeftLeg", "RightLeg_LowerRightLeg"]

    def Start_Simulation(self, directOrGUI):
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

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        # pyrosim.Send_Sensor_Neuron(name = 0, linkName="Torso")
        # pyrosim.Send_Sensor_Neuron(name = 1, linkName="BackLeg")
        # pyrosim.Send_Sensor_Neuron(name = 2, linkName="FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name = 3, linkName="LeftLeg")
        # pyrosim.Send_Sensor_Neuron(name = 4, linkName="RightLeg")
        # pyrosim.Send_Sensor_Neuron(name = 5, linkName="LowerFrontLeg")
        # pyrosim.Send_Sensor_Neuron(name = 6, linkName="LowerBackLeg")
        # pyrosim.Send_Sensor_Neuron(name = 7, linkName="LowerLeftLeg")
        # pyrosim.Send_Sensor_Neuron(name = 8, linkName="LowerRightLeg")

        # pyrosim.Send_Hidden_Neuron( name = 9 )

        # pyrosim.Send_Motor_Neuron(name = 10, jointName = "Torso_BackLeg")
        # pyrosim.Send_Motor_Neuron(name = 11, jointName = "Torso_FrontLeg")
        # pyrosim.Send_Motor_Neuron(name = 12, jointName = "Torso_LeftLeg")
        # pyrosim.Send_Motor_Neuron(name = 13, jointName = "Torso_RightLeg")
        # pyrosim.Send_Motor_Neuron(name = 14, jointName = "FrontLeg_LowerFrontLeg")
        # pyrosim.Send_Motor_Neuron(name = 15, jointName = "BackLeg_LowerBackLeg")
        # pyrosim.Send_Motor_Neuron(name = 16, jointName = "LeftLeg_LowerLeftLeg")
        # pyrosim.Send_Motor_Neuron(name = 17, jointName = "RightLeg_LowerRightLeg")
        # for currentRow in range(c.numSensorNeurons):
        #     for currentColumn in range(c.numMotorNeurons):
        #         pyrosim.Send_Synapse(sourceNeuronName=currentRow, 
        #                             targetNeuronName=currentColumn+c.numSensorNeurons, 
        #                             weight=self.weights[currentRow][currentColumn])

        for i in range(c.numSensorNeurons):
            pyrosim.Send_Sensor_Neuron(name = i, linkName=self.linkNames[i])

        for i in range(c.numHiddenNeurons):
            pyrosim.Send_Hidden_Neuron(name = i + c.numSensorNeurons)

        for i in range(c.numMotorNeurons):
            pyrosim.Send_Motor_Neuron(name = i + c.numSensorNeurons + c.numHiddenNeurons, jointName=self.jointNames[i])

        # Sensor to Hidden
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numHiddenNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                    targetNeuronName=currentColumn + c.numSensorNeurons,
                                    weight=self.sensorToHiddenWeights[currentRow][currentColumn])
        
        # Hidden to Motor
        for currentRow in range(c.numHiddenNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow + c.numSensorNeurons,
                                     targetNeuronName=currentColumn + c.numSensorNeurons + c.numHiddenNeurons,
                                     weight=self.hiddenToMotorWeights[currentRow][currentColumn])
        # exit()
        pyrosim.End()
    
    def Mutate(self):
        firstRandomRow = random.randint(0,c.numSensorNeurons-1)
        firstRandomColumn = random.randint(0,c.numHiddenNeurons-1)
        secondRandomRow = random.randint(0,c.numHiddenNeurons-1)
        secondRandomColumn = random.randint(0,c.numMotorNeurons-1)
        #self.weights[randomRow, randomColumn] = random.random() * 2 - 1
        self.sensorToHiddenWeights[firstRandomRow, firstRandomColumn] = random.random() * 2 - 1
        self.hiddenToMotorWeights[secondRandomRow, secondRandomColumn] = random.random() * 2 - 1

    def Set_ID(self, newID):
        self.myID = newID
        