import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
robotID = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotID)
frontLegSensorValues = numpy.zeros(10000)
torsoSensorValues = numpy.zeros(10000)
for i in range(1000):
    p.stepSimulation()
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    torsoSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Torso")
    time.sleep(1/100)
p.disconnect()
print(frontLegSensorValues)
print(torsoSensorValues)
numpy.save("data/data.npy", frontLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save("data/data2.npy", torsoSensorValues, allow_pickle=True, fix_imports=True)