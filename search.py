import os
import constants as c
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import numpy as np 

emotion = input("What emotion do you want to see? \n\ta. Happy\n\tb. Sad\n\tc. Lazy\n")
if emotion == "a" or emotion == "A":
    emotion == "happy"
if emotion == "b" or emotion == "B":
    emotion = "sad"
    
if emotion == "c" or emotion == "C":
    emotion == "lazy"

phc =  PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
avg = np.zeros(len(phc.stored)) 

avg = np.mean(phc.stored, axis = 0)

np.save('testA.npy', avg)