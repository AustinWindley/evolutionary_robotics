import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
robotId = p.loadURDF("body.urdf")
run_length = 1000
backLegSensorValues = np.zeros(run_length)
frontLegSensorValues = np.zeros(run_length)

BackLeg_amplitude = np.pi/4
BackLeg_frequency = 63
BackLeg_phaseOffset = np.pi
BackLeg_targetAngles = BackLeg_amplitude * np.sin([BackLeg_frequency * i/run_length + BackLeg_phaseOffset 
                                   for i in range(run_length)])
FrontLeg_amplitude = np.pi/4
FrontLeg_frequency = 63
FrontLeg_phaseOffset = 0
FrontLeg_targetAngles = FrontLeg_amplitude * np.sin([FrontLeg_frequency * i/run_length + FrontLeg_phaseOffset 
                                   for i in range(run_length)])
# np.save("data/BackLeg_targetAngles.npy", BackLeg_targetAngles)
# np.save("data/FrontLeg_targetAngles.npy", FrontLeg_targetAngles)
# exit()

pyrosim.Prepare_To_Simulate(robotId)
for i in (range(run_length)):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = -BackLeg_targetAngles[i],
        maxForce = 20)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = FrontLeg_targetAngles[i],
        maxForce = 20)
    time.sleep(1/240)
p.disconnect()

np.save("data/backLegSensorData.npy", backLegSensorValues)
np.save("data/frontLegSensorData.npy", frontLegSensorValues)


