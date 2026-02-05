import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
robotId = p.loadURDF("body.urdf")

backLegSensorValues = numpy.zeros(1000)
pyrosim.Prepare_To_Simulate(robotId)
for i in (range(1000)):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    time.sleep(1/60)
p.disconnect()

print(backLegSensorValues)

