#!/usr/bin/python3
""" solution test """

from RubicsCube2x2 import RubicsCube2x2
from print_cube_console import show_cube_console
from copy import deepcopy

def create_cube():
    """Create cube and apply seed"""
    new_cube = RubicsCube2x2()

    seed = [0, 11, 8, 1, 10]
    for i in seed:
        new_cube.do_move(i)
    return new_cube


def solve_cube(cube):
    """solution"""
    # make recursive call with all movements, solve_seed and current depth.
    dynamic_solver(cube, 0, [], 0)

SOLUTIONS = []
DEPTH_LIMIT = 6

def dynamic_solver(cube, move, solve_seed, depth):

    if SOLUTIONS:
        minimal_known_depth = len(SOLUTIONS[0])
        if depth >= minimal_known_depth:
            print('drop branch at -', minimal_known_depth)
            return

    my_cube = deepcopy(cube)
    my_solve_seed = deepcopy(solve_seed)

    if move != 0:
        my_cube.do_move(move)
        my_solve_seed.append(move)
        depth += 1
    
    if my_cube.is_solved():
        SOLUTIONS.append(my_solve_seed)
        SOLUTIONS.sort(key=len)
        print('minimal known solution -', len(SOLUTIONS[0]))
        return

    if depth == DEPTH_LIMIT:
        return

    for next_move in range(1, 13):
        if (move ^ 1) != next_move: # if not back move, then do the next move
            dynamic_solver(my_cube, next_move, my_solve_seed, depth)



CUBE = create_cube()
show_cube_console(CUBE)

solve_cube(CUBE)

print('solutions - ', len(SOLUTIONS))
SOLUTIONS.sort(key=len)

for index in range(3):
    solution = SOLUTIONS[index]
    print(len(solution))
    print(solution)
    cube = deepcopy(CUBE)
    for move in solution:
        cube.do_move(move)
        # show_cube_console(cube)
    print('is solved - ', cube.is_solved())
    print('')

