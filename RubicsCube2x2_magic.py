#!/usr/bin/python3

from RubicsCube2x2 import RubicsCube2x2

def magic_one(cube):
    cube.R()
    cube.U()
    cube.Ri()
    cube.U()
    cube.R()
    cube.U()
    cube.U()
    cube.Ri()

def magic_two_diagonal(cube):
    cube.Ri()
    cube.F()
    cube.Ri()
    cube.B()
    cube.B()
    cube.R()
    cube.Fi()
    cube.Ri()
    cube.B()
    cube.B()
    cube.R()
    cube.R()
    
def magic_two_near(cube):
    magic_two_diagonal(cube)
    cube.Ui()

