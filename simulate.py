from cmath import pi
import pybullet as p
import random as random
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import constants as c
from simulation import SIMULATION
from world import WORLD
from robot import ROBOT


simulation = SIMULATION()
simulation.Run()
world = WORLD()
robot = ROBOT()

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,c.gravity)
# robotId = p.loadURDF("body.urdf")
# planeId = p.loadURDF("plane.urdf")
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)
# frontLegSensorValues = numpy.zeros(c.size)
# b_targetVec = numpy.zeros(c.size)
# f_targetVec = numpy.zeros(c.size)
# backLegSensorValues = numpy.zeros(c.size)
# b_targetVec = (c.b_amplitude * numpy.sin((c.b_frequency * (numpy.linspace(0, 2*numpy.pi, c.size)) + c.b_phaseOffset)))
# f_targetVec = (c.f_amplitude * numpy.sin((c.f_frequency * (numpy.linspace(0, 2*numpy.pi, c.size)) + c.f_phaseOffset)))
# for i in range(c.size):
#     p.stepSimulation()
#     pyrosim.Set_Motor_For_Joint(
#     bodyIndex = robotId,
#     jointName = b'Torso_BackLeg',
#     controlMode = p.POSITION_CONTROL,
#     targetPosition = b_targetVec[i], #random.uniform(-pi/4.0, pi/4.0),
#     maxForce = c.maxForce
#     )
#     pyrosim.Set_Motor_For_Joint(
#     bodyIndex = robotId,
#     jointName = b'Torso_FrontLeg',
#     controlMode = p.POSITION_CONTROL,
#     targetPosition = f_targetVec[i], #random.uniform(-pi/2.0, pi/2.0),
#     maxForce = c.maxForce
#     )
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     time.sleep(c.timeSleep)
# p.disconnect()
# print(frontLegSensorValues)
# print(backLegSensorValues)
# numpy.save("data/data3.npy", b_targetVec, allow_pickle=True, fix_imports=True)
# numpy.save("data/data4.npy", f_targetVec, allow_pickle=True, fix_imports=True)
# numpy.save("data/data.npy", backLegSensorValues, allow_pickle=True, fix_imports=True)
# numpy.save("data/data2.npy", frontLegSensorValues, allow_pickle=True, fix_imports=True)