#!/usr/bin/python3
""" print solution path """

from copy import deepcopy

def print_solution(cube, solution):
    print("solution moves - {}".format(len(solution)))
    copy_cube = deepcopy(cube)
    for move in solution:
        print(copy_cube.do_move(move), end=' ')
    print('\nis solved - ', copy_cube.is_solved(), end='\n\n')

