import math

import pybullet

import pyrosim.pyrosim as pyrosim

import pyrosim.constants as c

class NEURON: 

    def __init__(self,line):

        self.Determine_Name(line)

        self.Determine_Type(line)

        self.Search_For_Link_Name(line)

        self.Search_For_Joint_Name(line)

        self.Set_Value(0.0)
        
        # Setting default gain for now
        self.Set_Gain(0.5)

        # Leaving bias alone for now
        self.Set_Bias(0.0)

    def Add_To_Value( self, value ):

        self.Set_Value( self.Get_Value() + value )

    def Get_Joint_Name(self):

        return self.jointName

    def Get_Link_Name(self):

        return self.linkName

    def Get_Name(self):

        return self.name

    def Get_Value(self):

        return self.value
    
    def Get_Gain(self):

        return self.gain
    
    def Get_Bias(self):

        return self.bias

    def Is_Sensor_Neuron(self):

        return self.type == c.SENSOR_NEURON

    def Is_Hidden_Neuron(self):

        return self.type == c.HIDDEN_NEURON

    def Is_Motor_Neuron(self):

        return self.type == c.MOTOR_NEURON

    def Print(self):

        # self.Print_Name()

        # self.Print_Type()

        # self.Print_Value()

        self.Print_Gain()

        # print("")

    def Set_Value(self, value):

        self.value = value

    def Set_Gain(self, gain):
        
        self.gain = gain

    def Set_Bias(self, bias):

        self.bias = bias

    def Update_Sensor_Neuron(self):

        self.Set_Value(pyrosim.Get_Touch_Sensor_Value_For_Link(self.Get_Link_Name()))

    def Update_Motor_Neuron(self, neurons, synapses):
        
        self.Set_Value(0.0)
        for synapse in synapses.keys():
            if synapse[1] == self.Get_Name():
                self.Allow_Presynaptic_Neuron_To_Influence_Me(synapses[synapse].Get_Weight(), 
                                                              neurons[synapse[0]].Get_Value())
        self.Threshold()

    def Allow_Presynaptic_Neuron_To_Influence_Me(self, current_weight, presynaptic_weight):
        self.Add_To_Value(presynaptic_weight * current_weight)

    def Update_Hidden_Neuron(self, neurons, synapses):
        # new value = -value + sum for all synapses(weight at synapse j * (tanh(gain * (presynaptic_weight + presynaptic_bias))) + current_value)
        old_value = self.Get_Value()
        self.Set_Value(0.0)
        for synapse in synapses.keys():
            if synapse[1] == self.Get_Name():
                new_value = self.Allow_Recurrent_Connections(neurons, synapses)
                #print(new_value)
                self.Set_Value(new_value)
                self.Threshold()

                self.Set_Gain(math.tanh(self.Get_Gain() + (self.Get_Value() - old_value)))
                #print(self.gain)

    def Allow_Recurrent_Connections(self, neurons, synapses):
        # Sum of all synapses  
        sum = 0
        for synapse in synapses.keys():
            current_weight = synapses[synapse].Get_Weight()
            presynaptic_weight = neurons[synapse[0]].Get_Value()
            #presynaptic_bias = neurons[synapse[0]].Get_Bias()
            # not sure if this is doing w ji...
            sum += (current_weight * (math.tanh(self.Get_Gain() * presynaptic_weight)))

        new_value = -self.Get_Value() + sum
        return new_value

# -------------------------- Private methods -------------------------

    def Determine_Name(self,line):

        if "name" in line:

            splitLine = line.split('"')

            self.name = splitLine[1]

    def Determine_Type(self,line):

        if "sensor" in line:

            self.type = c.SENSOR_NEURON

        elif "motor" in line:

            self.type = c.MOTOR_NEURON

        else:

            self.type = c.HIDDEN_NEURON

    def Print_Name(self):

       print(self.name)

    def Print_Type(self):

       print(self.type)

    def Print_Value(self):

       print(self.value , " " , end="" )

    def Print_Gain(self):

        print(self.gain , " ", end="" )

    def Search_For_Joint_Name(self,line):

        if "jointName" in line:

            splitLine = line.split('"')

            self.jointName = splitLine[5]

    def Search_For_Link_Name(self,line):

        if "linkName" in line:

            splitLine = line.split('"')

            self.linkName = splitLine[5]

    def Threshold(self):

        self.value = math.tanh(self.value)
