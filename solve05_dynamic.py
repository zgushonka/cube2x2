#!/usr/bin/python3
""" solution test """

from RubicsCube2x2 import RubicsCube2x2
from print_cube_console import show_cube_console
from copy import deepcopy

def create_cube():
    """Create cube and apply seed"""
    new_cube = RubicsCube2x2()
    # show_cube_console(new_cube)

    seed = [17, 16, 6, 3, 18, 15, 10, 9, 6, 10, 16, 14, 4, 11, 3, 3, \
    10, 10, 2, 14, 4, 16, 3, 2, 18, 6, 14, 17, 12, 5, 18, 12, 14, 17, 3, \
    14, 6, 14, 15, 13, 1, 10, 13, 8, 5, 1, 12, 2, 10, 11]
    for i in seed:
        new_cube.do_move(i)
    return new_cube



def solve_cube(cube):
    """solution"""
    # make recursive call with all movements, solve_seed and current depth.
    dynamic_solver(cube, 0, [], 0)

SOLUTIONS = []
DEPTH_LIMIT = 5

def dynamic_solver(cube, move, solve_seed, depth):
    my_cube = deepcopy(cube)
    my_solve_seed = deepcopy(solve_seed)

    my_cube.do_move(move)
    my_solve_seed.append(move)
    
    if my_cube.is_solved():
        SOLUTIONS.append(my_solve_seed)
        print('solution - ', my_solve_seed)
        return

    depth += 1
    if depth > DEPTH_LIMIT:
        return

    if len(SOLUTIONS) != 0:
        return

    for next_move in range(7, 19):
        if next_move != (move + 1):
            dynamic_solver(my_cube, next_move, my_solve_seed, depth)


CUBE = create_cube()
show_cube_console(CUBE)

solve_cube(CUBE)
# show_cube_console(CUBE)

print('solutions - ', len(SOLUTIONS))

for solution in SOLUTIONS:
    print(len(solution))
    print(solution)
    print('')

print('is solved - ', CUBE.is_solved())
