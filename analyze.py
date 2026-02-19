import numpy as np
import matplotlib.pyplot as plt
# backLegSensorValues = np.load("data/backLegSensorData.npy")
# frontLegSensorValues = np.load("data/frontLegSensorData.npy")
BackLeg_targetAngles = np.load("data/BackLeg_targetAngles.npy")
FrontLeg_targetAngles = np.load("data/FrontLeg_targetAngles.npy")

# plt.plot(backLegSensorValues, linewidth = 4,label = "Back Leg")
# plt.plot(frontLegSensorValues, label = "Front Leg")
plt.plot(BackLeg_targetAngles, label = "BackLeg_targetAngles")
plt.plot(FrontLeg_targetAngles, label = "FrontLeg_targetAngles")
plt.xlabel("Steps")
plt.ylabel("Value in Radians")
plt.legend()
plt.show()