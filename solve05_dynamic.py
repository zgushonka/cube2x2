#!/usr/bin/python3
""" solution test """

# import sys
# print(sys.version)

import random
from copy import deepcopy
from create_random_cube import create_scrumbled_cube
from print_solution import print_solution

SEED_MOVES_COUNT = 4

SOLUTIONS = []
DEPTH_LIMIT = SEED_MOVES_COUNT

def solve_cube(cube):
    """solution"""
    # make recursive call with all movements, empsolve_seed.
    dynamic_solver(cube)


def dynamic_solver(cube, move=None, solve_seed=None):
    if SOLUTIONS:
        return # find only one solution

    my_cube = deepcopy(cube)
    my_solve_seed = deepcopy(solve_seed) if solve_seed else []

    # do move if valid
    if move != None:
        my_cube.do_move(move)
        my_solve_seed.append(move)
    
    # no solution found. stop search
    if my_cube.is_solved():
        SOLUTIONS.append(my_solve_seed)
        SOLUTIONS.sort(key=len)
        return

    # no solution in this branch. stop search
    if len(my_solve_seed) >= DEPTH_LIMIT:
        return
    
    
    # for next_move in range(0, 6): # sequentive next move
    next_moves = random.sample(range(6), 6) # random next move
    for next_move in next_moves:
        if move != (next_move ^ 1): # if next_move is not back move, then continue
            if SOLUTIONS:
                return # find only one solution
            dynamic_solver(my_cube, next_move, my_solve_seed)


CUBE = create_scrumbled_cube(SEED_MOVES_COUNT)
solve_cube(CUBE)

solution = SOLUTIONS[0]
print_solution(CUBE, solution)

