import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = np.zeros(c.run_length)
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        if (self.jointName == b"Torso_FrontLeg"):
            self.frequency = 1/2 * c.frequency
        else:
            self.frequency = c.frequency
        self.offset = c.phaseOffset
        self.motorValues = self.amplitude * np.sin([self.frequency * i/c.run_length + self.offset 
                                           for i in range(c.run_length)])
        

    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[desiredAngle],
            maxForce = 20)

    def Save_Values(self):
        np.save(f"data/{self.jointName}MotorData.npy", self.motorValues)