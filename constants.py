import numpy as np

run_length = 1000

amplitude = np.pi/4
frequency = 63
phaseOffset = np.pi

backLegSensorValues = np.zeros(run_length)
frontLegSensorValues = np.zeros(run_length)

max_force = 20

numberOfGenerations = 10
populationSize = 10

numSensorNeurons = 9
numMotorNeurons = 8
numHiddenNeurons = 1

motorJointRange = 0.2