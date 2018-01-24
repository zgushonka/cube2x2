#!/usr/bin/python3
""" solution test """

from RubicsCube2x2 import RubicsCube2x2
from print_cube_console import show_cube_console


# [11, 18, 8, 14, 4]
#     G W
#     Y G
# O R B R Y R
# W R B B O Y
#     W W
#     O B
#     G O
#     Y G

#     side     color
#      u         w
#    l f r     g o b
#      d         y
#      b         r

def create_cube():
    new_cube = RubicsCube2x2()

    # apply seed
    seed = [4, 11, 1, 7, 15]
    for move in seed:
        new_cube.do_move(move)
    return new_cube

def solve_cube(cube):
    cube.turn_up()
    cube.turn_up()
    cube.turn_left()
    cube.L()
    cube.F()
    cube.L()
    cube.Fi()

cube = create_cube()
show_cube_console(cube)

solve_cube(cube)
show_cube_console(cube)

print('is solved - ', cube.is_solved())
