import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
#         BackLeg_targetAngles = BackLeg_amplitude * np.sin([BackLeg_frequency * i/run_length + BackLeg_phaseOffset 
#                                    for i in range(run_length)])

        # FrontLeg_targetAngles = FrontLeg_amplitude * np.sin([FrontLeg_frequency * i/run_length + FrontLeg_phaseOffset 
        #                                    for i in range(run_length)])
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset
        pass