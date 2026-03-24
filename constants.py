import numpy as np

run_length = 200

amplitude = np.pi/4
frequency = 63
phaseOffset = np.pi

backLegSensorValues = np.zeros(run_length)
frontLegSensorValues = np.zeros(run_length)

max_force = 20

numberOfGenerations = 2