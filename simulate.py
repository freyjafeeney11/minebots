from cmath import pi
import pybullet as p
import random as random
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy

b_amplitude = pi/2
b_frequency = 10
b_phaseOffset = pi/9

f_amplitude = pi/6
f_frequency = 11
f_phaseOffset = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
frontLegSensorValues = numpy.zeros(1000)
b_targetVec = numpy.zeros(1000)
f_targetVec = numpy.zeros(1000)
backLegSensorValues = numpy.zeros(1000)
b_targetVec = (b_amplitude * numpy.sin((b_frequency * (numpy.linspace(0, 2*numpy.pi, 1000)) + b_phaseOffset)))
f_targetVec = (f_amplitude * numpy.sin((f_frequency * (numpy.linspace(0, 2*numpy.pi, 1000)) + f_phaseOffset)))
for i in range(1000):
    p.stepSimulation()
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_BackLeg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = b_targetVec[i], #random.uniform(-pi/4.0, pi/4.0),
    maxForce = 30
    )
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_FrontLeg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = f_targetVec[i], #random.uniform(-pi/2.0, pi/2.0),
    maxForce = 30
    )
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/240)
p.disconnect()
print(frontLegSensorValues)
print(backLegSensorValues)
numpy.save("data/data3.npy", b_targetVec, allow_pickle=True, fix_imports=True)
numpy.save("data/data4.npy", f_targetVec, allow_pickle=True, fix_imports=True)
numpy.save("data/data.npy", backLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save("data/data2.npy", frontLegSensorValues, allow_pickle=True, fix_imports=True)