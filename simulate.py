import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
robotId = p.loadURDF("body.urdf")
planeId = p.loadURDF("plane.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
frontLegSensorValues = numpy.zeros(100)
backLegSensorValues = numpy.zeros(100)
for i in range(100):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/10)
p.disconnect()
print(frontLegSensorValues)
print(backLegSensorValues)
numpy.save("data/data.npy", backLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save("data/data2.npy", frontLegSensorValues, allow_pickle=True, fix_imports=True)