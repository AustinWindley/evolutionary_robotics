import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import time
import constants as c

class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK(f"brain{self.solutionID}.nndf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()  
        self.Prepare_To_Act()
        os.system(f"del brain{self.solutionID}.nndf")
           
    def Prepare_To_Sense(self):
        self.sensors = {}
        self.motors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)
                # jointName = jointName.decode("utf-8")
    
    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        self.nn.Print()
        #stateOfLinkZero = p.getLinkState(self.robotId, 0)
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        #positionOfLinkZero = stateOfLinkZero[0]
        basePosition = basePositionAndOrientation[0]
        #xCoordinateOfLinkZero = positionOfLinkZero[0]
        xPosition = basePosition[0]
        
        with open(f"tmp{str(self.solutionID)}.txt", "w") as f:
            f.write(str(xPosition))
        os.rename("tmp"+str(self.solutionID)+".txt" , "fitness"+str(self.solutionID)+".txt")