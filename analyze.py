import numpy as numpy
import matplotlib.pyplot

frontLegSensorValues = numpy.load("data/data.npy")
matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.show()
print(frontLegSensorValues)