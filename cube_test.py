#!/usr/bin/python3
"""Cube 2x2x2 test"""

from RubicsCube2x2 import RubicsCube2x2
from print_cube_console import show_cube_console

#     side     color
#      u         w
#    l f r     g o b
#      d         y
#      b         r

cube = RubicsCube2x2()
cube.Di()
cube.R()

cube2 = RubicsCube2x2()
cube2.U()
cube2.Li()
cube2.turn_left()

show_cube_console(cube)
show_cube_console(cube2)

print(cube.is_equal_to(cube2))
