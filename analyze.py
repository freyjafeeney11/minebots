import numpy as numpy
import matplotlib.pyplot

#backLegSensorValues = numpy.load("data/data.npy")
#frontLegSensorValues = numpy.load("data/data2.npy")
b_targetVec = numpy.load("data/data3.npy")
f_targetVec = numpy.load("data/data4.npy")
#matplotlib.pyplot.plot(backLegSensorValues,  linewidth = 2, label = 'Back Leg Values')
#matplotlib.pyplot.plot(frontLegSensorValues,  linewidth = 2, label = 'Front Leg Values')
matplotlib.pyplot.plot(b_targetVec,  linewidth = 2, label = 'BackLeg Target Angles Values')
matplotlib.pyplot.plot(f_targetVec,  linewidth = 2, label = 'FrontLeg Target Angles Values')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
#print(backLegSensorValues)
#print(frontLegSensorValues)