#!/usr/bin/python3
""" depth step by step brute force """

from create_random_cube import create_cube
from solve06_CubeState import CubeState
from print_solution import print_solution


def make_next_layer_for(cube_state) -> list:
    """ we need to go deeper """
    next_layer = []
    for next_move in range(0, 6): # sequentive next move
        previous_move = -1 
        if cube_state.path:
            previous_move = cube_state.path[-1]
        if (previous_move ^ 1) != next_move: # if next_move is not back move, then continue
            next_layer.append( CubeState(cube_state.cube, cube_state.path, next_move) )
    return next_layer


def solve_cube(cube, limit) -> list:
    """solution"""
    cube_state = CubeState(cube)
    if cube_state.is_solved():
        return cube.path

    this_layer_cubes = [cube_state]
    while True:
        next_layer_cubes = []
        for this_cube in this_layer_cubes:
            if len(this_cube.path) > limit:
                return []
            next_layer = make_next_layer_for(this_cube)
            for next_layer_cube in next_layer:
                if next_layer_cube.is_solved():
                    # found solution - exit
                    return next_layer_cube.path
                next_layer_cubes.append(next_layer_cube)
        this_layer_cubes = next_layer_cubes


def main():
    depth = 4
    seed_moves_count = depth

    cube = create_cube(seed_moves_count * 3)
    solution = solve_cube(cube, depth)
    if solution:
        print_solution(cube, solution)
    else:
        print('No solution found for depth {}.'.format(depth))

if __name__ == '__main__':
    main()
