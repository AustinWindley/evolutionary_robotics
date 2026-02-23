import numpy as np

run_length = 1000

amplitude = np.pi/4
frequency = 63
phaseOffset = np.pi

# FrontLeg_amplitude = np.pi/4
# FrontLeg_frequency = 63
# FrontLeg_phaseOffset = 0

backLegSensorValues = np.zeros(run_length)
frontLegSensorValues = np.zeros(run_length)

max_force = 20