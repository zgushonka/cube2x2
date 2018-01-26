#!/usr/bin/python3
""" solution test """

# import sys
# print(sys.version)

import random
from copy import deepcopy
from RubicsCube2x2 import RubicsCube2x2
from print_cube_console import show_cube_console

SEED_MOVES_COUNT = 6

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
    # make recursive call with all movements, empsolve_seed.
    dynamic_solver(cube)

SOLUTIONS = []
DEPTH_LIMIT = SEED_MOVES_COUNT

def dynamic_solver(cube, move = -1, solve_seed = []):
    my_cube = deepcopy(cube)
    my_solve_seed = deepcopy(solve_seed)

    # do move if valid
    if move > -1:
        my_cube.do_move(move)
        my_solve_seed.append(move)
    
    # no solution found. stop search
    if my_cube.is_solved():
        SOLUTIONS.append(my_solve_seed)
        SOLUTIONS.sort(key=len)
        return

    # no solution in this branch. stop search
    if len(my_solve_seed) == DEPTH_LIMIT:
        return
    
    # for next_move in range(0, 6): # sequentive next move
    next_moves = random.sample(range(6), 6) # random next move
    for next_move in next_moves:
        if (move ^ 1) != next_move: # if next_move is not back move, then continue

            # stop recursion if shorter solution found
            if SOLUTIONS:
                minimal_known_depth = len(SOLUTIONS[0])
                if len(solve_seed) >= minimal_known_depth:
                    return
            
            dynamic_solver(my_cube, next_move, my_solve_seed)


CUBE = create_cube()

solve_cube(CUBE)

# SOLUTIONS.sort(key=len)
print('solutions - ', len(SOLUTIONS), end='\n\n')

for index in range(2):
    if index >= len(SOLUTIONS):
        continue

    solution = SOLUTIONS[index]
    print("solution #{}. moves - {}".format(index, len(solution)))
    cube = deepcopy(CUBE)
    for move in solution:
        print(cube.do_move(move), end=' ')
    print('\nis solved - ', cube.is_solved(), end='\n\n')

