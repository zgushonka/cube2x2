#!/usr/bin/python3
""" solution test """

from RubicsCube2x2 import RubicsCube2x2
from print_cube_console import show_cube_console

import RubicsCube2x2_magic

#     B B
#     O R
# O Y B G W Y
# R G Y O G O
#     R W
#     B G
#     W Y
#     W R

#     side     color
#      u         w
#    l f r     g o b
#      d         y
#      b         r

def create_cube():
    new_cube = RubicsCube2x2()
    show_cube_console(new_cube)

    seed = [3, 4, 1, 16, 13, 18, 5, 12, 13, 18, 11, 6, 11, 3, 7, 4, \
            12, 2, 13, 2, 15, 1, 14, 3, 2, 13, 10, 18, 1, 12, 12, 8, 15, 12, \
            16, 16, 8, 9, 8, 4, 14, 1, 3, 2, 3, 13, 5, 16, 4, 4]
    for i in seed:
        new_cube.do_move(i)
    return new_cube

def solve_cube(cube):
    cube.rotate_left()
    cube.turn_left()
    cube.Fi()

    cube.Bi()
    cube.Li()
    cube.B()

    cube.D()

    cube.Li()
    cube.Fi()
    cube.L()

    cube.D()
    cube.D()

    cube.L()
    cube.B()
    cube.Li()

    cube.rotate_left()
    cube.rotate_left()

    cube.U()
    cube.U()
    RubicsCube2x2_magic.magic_one(cube)
    cube.Ui()
    RubicsCube2x2_magic.magic_one(cube)

    RubicsCube2x2_magic.magic_two_diagonal(cube)
    cube.turn_left()
    RubicsCube2x2_magic.magic_two_near(cube)


cube = create_cube()
show_cube_console(cube)

solve_cube(cube)
show_cube_console(cube)

print 'is solved - ', cube.is_solved()
