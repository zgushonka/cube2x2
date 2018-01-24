#!/usr/bin/python3
""" solution test """

from RubicsCube2x2 import RubicsCube2x2
from print_cube_console import show_cube_console

#     B Y
#     B G
# R O Y R Y O
# B W O W B G
#     G O
#     W W
#     R R
#     Y G

#     side     color
#      u         w
#    l f r     g o b
#      d         y
#      b         r

def create_cube():
    """Create cube and apply seed"""
    new_cube = RubicsCube2x2()
    # show_cube_console(new_cube)

    seed = [10, 9, 17, 14, 11, 8, 3, 2, 17, 3, 9, 7, 15, 4, 14, 14, 3, 3, \
            13, 7, 15, 9, 14, 13, 11, 17, 7, 10, 5, 16, 11, 5, 7, 10, 14, \
            7, 17, 7, 8, 6, 12, 3, 6, 1, 16, 12, 5, 13, 3, 4]
    for move in seed:
        new_cube.do_move(move)
    return new_cube

def solve_cube(cube):
    """manual solution"""
    cube.turn_right()
    cube.turn_up()
    cube.turn_right()
    cube.turn_right()
    cube.Ri()
    cube.turn_right()
    cube.D()

    cube.Li()
    cube.Fi()
    cube.L()

    cube.D()


CUBE = create_cube()
show_cube_console(CUBE)

solve_cube(CUBE)
show_cube_console(CUBE)

print('is solved - ', CUBE.is_solved())
