#!/usr/bin/python3
""" solution test """

# import sys
# print(sys.version)

import random
from copy import deepcopy
from RubicsCube2x2 import RubicsCube2x2
from print_cube_console import show_cube_console

SEED_MOVES_COUNT = 4

def create_cube():
    """Create cube and apply seed"""
    new_cube = RubicsCube2x2()

    while True:
        seed = new_cube.do_n_random_moves(SEED_MOVES_COUNT)
        
        if not new_cube.is_solved():
            # print seed
            temp_cube = RubicsCube2x2()
            print('seed moves - ', end='')
            for move in seed:
                print(temp_cube.do_move(move), end=' ')
            print('\n')
            # print cube
            show_cube_console(new_cube)

            break
    return new_cube


def solve_cube(cube):
    """solution"""
    # make recursive call with all movements, solve_seed and current depth.
    dynamic_solver(cube, -1, [])

SOLUTIONS = []
DEPTH_LIMIT = SEED_MOVES_COUNT

def dynamic_solver(cube, move, solve_seed):
    if SOLUTIONS:
        minimal_known_depth = len(SOLUTIONS[0])
        if len(solve_seed) >= minimal_known_depth:
            return

    my_cube = deepcopy(cube)
    my_solve_seed = deepcopy(solve_seed)

    if move > -1:
        my_cube.do_move(move)
        my_solve_seed.append(move)
    
    if my_cube.is_solved():
        SOLUTIONS.append(my_solve_seed)
        SOLUTIONS.sort(key=len)
        return

    if len(my_solve_seed) == DEPTH_LIMIT:
        return
    
    # for next_move in range(0, 12):
    next_moves = random.sample(range(12), 12)
    for next_move in next_moves:
        if (move ^ 1) != next_move: # if not back move, then do the next move
            dynamic_solver(my_cube, next_move, my_solve_seed)


CUBE = create_cube()

solve_cube(CUBE)

# SOLUTIONS.sort(key=len)
print('solutions - ', len(SOLUTIONS))

for index in range(3):
    if index >= len(SOLUTIONS):
        continue

    solution = SOLUTIONS[index]
    print("solution #{}. moves - {}".format(index, len(solution)))
    cube = deepcopy(CUBE)
    for move in solution:
        print(cube.do_move(move), end=' ')
    print('')
    print('is solved - ', cube.is_solved())
    print('')

