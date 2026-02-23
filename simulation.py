import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import time
from world import WORLD
from robot import ROBOT
class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
    
    def __del__(self):
        p.disconnect()
    
    def run(self):
        for t in (range(c.run_length)):
            p.stepSimulation()
            self.robot.Sense(t)

            pyrosim.Set_Motor_For_Joint(
                bodyIndex = self.robot.robotId,
                jointName = b'Torso_BackLeg',
                controlMode = p.POSITION_CONTROL,
                targetPosition = -c.BackLeg_targetAngles[t],
                maxForce = 20)
            pyrosim.Set_Motor_For_Joint(
                bodyIndex = self.robot.robotId,
                jointName = b'Torso_FrontLeg',
                controlMode = p.POSITION_CONTROL,
                targetPosition = c.FrontLeg_targetAngles[t],
                maxForce = 20)
            time.sleep(1/240)
    