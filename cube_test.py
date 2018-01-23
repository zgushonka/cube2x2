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
cube2 = RubicsCube2x2()
show_cube_console(cube)
print cube.is_equal_to(cube2)

seed = cube.do_n_random_moves(50)
print seed
show_cube_console(cube)


print cube.is_equal_to(cube2)
