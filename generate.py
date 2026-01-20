import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5
for i in range(5):
    length, width, height = 1, 1, 1
    for j in range(5):
        length, width, height = 1, 1, 1
        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x+i,y+j,z+k] , size=[length, width, height])
            length = length * 0.9
            width = width * 0.9
            height = height * 0.9
    
pyrosim.End()