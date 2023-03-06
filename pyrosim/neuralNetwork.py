from pyrosim.neuron  import NEURON

from pyrosim.synapse import SYNAPSE

import pyrosim.constants as c

class NEURAL_NETWORK: 

    def __init__(self,nndfFileName):

        self.neurons = {}

        self.synapses = {}

        f = open(nndfFileName,"r")

        for line in f.readlines():

            self.Digest(line)

        f.close()

    def Print(self):

        self.Print_Sensor_Neuron_Values()

        self.Print_Hidden_Neuron_Values()

        self.Print_Motor_Neuron_Values()

        print("")
    
    def Update(self):
        for key in self.neurons.values():
            if self.neurons[key.Get_Name()].Is_Sensor_Neuron():
                self.neurons[key.Get_Name()].Update_Sensor_Neuron()
            else:
                self.neurons[key.Get_Name()].Update_Hidden_Or_Motor_Neuron(self.neurons, self.synapses)
        exit();
    def Get_Neuron_Names(self):
        return self.neurons.keys()
    #step 61
    def Is_Motor_Neuron(self, neuronName):
        self.neuron1 = self.neurons[neuronName]
        if (NEURON.Is_Motor_Neuron(self.neuron1) == c.MOTOR_NEURON):
            return True
        else:
            return False
    def Get_Motor_Neurons_Joint(self, neuronName):
        return NEURON.Get_Joint_Name(self.neurons[neuronName])
    def Get_Value_Of(self, neuronName):
        return NEURON.Get_Value(self.neurons[neuronName])

# ---------------- Private methods --------------------------------------

    def Add_Neuron_According_To(self,line):

        neuron = NEURON(line)

        self.neurons[ neuron.Get_Name() ] = neuron

    def Add_Synapse_According_To(self,line):

        synapse = SYNAPSE(line)

        sourceNeuronName = synapse.Get_Source_Neuron_Name()

        targetNeuronName = synapse.Get_Target_Neuron_Name()

        self.synapses[sourceNeuronName , targetNeuronName] = synapse

    def Digest(self,line):

        if self.Line_Contains_Neuron_Definition(line):

            self.Add_Neuron_According_To(line)

        if self.Line_Contains_Synapse_Definition(line):

            self.Add_Synapse_According_To(line)

    def Line_Contains_Neuron_Definition(self,line):

        return "neuron" in line

    def Line_Contains_Synapse_Definition(self,line):

        return "synapse" in line

    def Print_Sensor_Neuron_Values(self):

        print("sensor neuron values: " , end = "" )

        for neuronName in sorted(self.neurons):

            if self.neurons[neuronName].Is_Sensor_Neuron():

                self.neurons[neuronName].Print()

        print("")

    def Print_Hidden_Neuron_Values(self):

        print("hidden neuron values: " , end = "" )

        for neuronName in sorted(self.neurons):

            if self.neurons[neuronName].Is_Hidden_Neuron():

                self.neurons[neuronName].Print()

        print("")

    def Print_Motor_Neuron_Values(self):

        print("motor neuron values: " , end = "" )

        for neuronName in sorted(self.neurons):

            if self.neurons[neuronName].Is_Motor_Neuron():

                self.neurons[neuronName].Print()

        print("")
