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
    show_cube_console(new_cube)

    seed = [17, 16, 6, 3, 18, 15, 10, 9, 6, 10, 16, 14, 4, 11, 3, 3, \
    10, 10, 2, 14, 4, 16, 3, 2, 18, 6, 14, 17, 12, 5, 18, 12, 14, 17, 3, \
    14, 6, 14, 15, 13, 1, 10, 13, 8, 5, 1, 12, 2, 10, 11]
    for i in seed:
        new_cube.do_move(i)
    return new_cube

def solve_cube(cube):
    """manual solution"""
    show_cube_console(cube)
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
