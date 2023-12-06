import os
import constants as c
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import numpy as np 

emotion = input("What emotion do you want to see? \n\t1. Happy\n\t2. Sad\n\t3. Lazy\n")
while (emotion != 'happy' and emotion != 'sad' and emotion!='lazy'):
    print("Please enter happy, emotion or lazy.")
    emotion = input("What emotion do you want to see? \n\t1. Happy\n\t2. Sad\n\t3. Lazy\n")

with open("chosen_emotion.txt", "a") as file:
    file.write(emotion)

phc =  PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
avg = np.zeros(len(phc.stored)) 

avg = np.mean(phc.stored, axis = 0)

np.save('testA.npy', avg)