import numpy as numpy
import matplotlib.pyplot

A_targetVec = numpy.load("testA.npy")
#row = A_targetVec[1,:]
matplotlib.pyplot.plot(A_targetVec,  linewidth = 2, label = 'A Fitness')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()