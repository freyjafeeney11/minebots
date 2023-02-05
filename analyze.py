import numpy as numpy
import matplotlib.pyplot

frontLegSensorValues = numpy.load("data/data.npy")
torsoSensorValues = numpy.load("data/data2.npy")
matplotlib.pyplot.plot(frontLegSensorValues,  linewidth = 3, label = 'Front Leg Values')
matplotlib.pyplot.plot(torsoSensorValues,  linewidth = 3, label = 'Torso Values')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
print(frontLegSensorValues)
print(torsoSensorValues)