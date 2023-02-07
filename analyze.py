import numpy as numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/data.npy")
frontLegSensorValues = numpy.load("data/data2.npy")
matplotlib.pyplot.plot(backLegSensorValues,  linewidth = 2, label = 'Back Leg Values')
matplotlib.pyplot.plot(frontLegSensorValues,  linewidth = 2, label = 'Front Leg Values')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
print(backLegSensorValues)
print(frontLegSensorValues)