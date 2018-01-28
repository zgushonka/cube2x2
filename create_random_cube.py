#!/usr/bin/python3
""" depth step by step brute force """

import random
from RubicsCube2x2 import RubicsCube2x2
from print_cube_console import show_cube_console


def create_scrumbled_cube(moves_count = 1) -> RubicsCube2x2:
    """Create cube and apply seed"""
    new_cube = RubicsCube2x2()

    while True:
        seed = new_cube.do_n_random_moves(moves_count)
        
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
