import numpy as np

run_length = 1000

BackLeg_amplitude = np.pi/4
BackLeg_frequency = 63
BackLeg_phaseOffset = np.pi

FrontLeg_amplitude = np.pi/4
FrontLeg_frequency = 63
FrontLeg_phaseOffset = 0

backLegSensorValues = np.zeros(run_length)
frontLegSensorValues = np.zeros(run_length)

BackLeg_targetAngles = BackLeg_amplitude * np.sin([BackLeg_frequency * i/run_length + BackLeg_phaseOffset 
                                   for i in range(run_length)])

FrontLeg_targetAngles = FrontLeg_amplitude * np.sin([FrontLeg_frequency * i/run_length + FrontLeg_phaseOffset 
                                   for i in range(run_length)])

max_force = 20