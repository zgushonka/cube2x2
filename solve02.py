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

    seed = [14, 15, 12, 9, 6, 11, 16, 5, 6, 11, 4, 17, 4, 14, 0, 15, 5, \
            13, 6, 13, 8, 12, 7, 14, 13, 6, 3, 11, 12, 5, 5, 1, 8, 5, 9, \
            9, 1, 2, 1, 15, 7, 12, 14, 13, 14, 6, 16, 9, 15, 15]
    for move in seed:
        new_cube.do_move(move)
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

print('is solved - ', cube.is_solved())
