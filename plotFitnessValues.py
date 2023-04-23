import numpy as numpy
import matplotlib.pyplot

#backLegSensorValues = numpy.load("data/data.npy")
#frontLegSensorValues = numpy.load("data/data2.npy")
A_targetVec = numpy.load("testA.npy")
#B_targetVec = numpy.load("testB.npy")
#matplotlib.pyplot.plot(backLegSensorValues,  linewidth = 2, label = 'Back Leg Values')
#matplotlib.pyplot.plot(frontLegSensorValues,  linewidth = 2, label = 'Front Leg Values')
matplotlib.pyplot.plot(A_targetVec,  linewidth = 2, label = 'A Fitness')
#matplotlib.pyplot.plot(B_targetVec,  linewidth = 2, label = 'B Fitness')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
#print(backLegSensorValues)
#print(frontLegSensorValues)