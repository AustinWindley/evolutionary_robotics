import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-2,2,0.5] , size=[1, 1, 1])
    pyrosim.End()

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0,0,1], size=[1,1,1])

    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = 
                    "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0], size=[0.2,1,0.2])
    pyrosim.Send_Joint( name = "BackLeg_LowerBackLeg" , parent= "BackLeg" , child = "LowerBackLeg" , type = 
                    "revolute", position = [0,-1,0], jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="LowerBackLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])

    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = 
                    "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0], size=[0.2,1,0.2])
    pyrosim.Send_Joint( name = "FrontLeg_LowerFrontLeg" , parent= "FrontLeg" , child = "LowerFrontLeg" , type = 
                    "revolute", position = [0,1,0], jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])

    pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = 
                    "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0], size=[1,0.2,0.2])
    pyrosim.Send_Joint( name = "LeftLeg_LowerLeftLeg" , parent= "LeftLeg" , child = "LowerLeftLeg" , type = 
                    "revolute", position = [-1,0,0], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])

    pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = 
                    "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0], size=[1,0.2,0.2])
    pyrosim.Send_Joint( name = "RightLeg_LowerRightLeg" , parent= "RightLeg" , child = "LowerRightLeg" , type = 
                    "revolute", position = [1,0,0], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="LowerRightLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])
    pyrosim.End()

Create_World()
Generate_Body()

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()