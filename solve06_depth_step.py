#!/usr/bin/python3
""" depth step by step brute force """

from create_random_cube import create_scrumbled_cube
from solve06_CubeState import CubeState
from print_solution import print_solution


def make_next_layer_for(cube_state) -> list:
    """ we need to go deeper """
    next_layer = []
    for next_move in range(0, 6): # sequentive next move
        previous_move = None if not cube_state.path else cube_state.path[-1]
        if previous_move != (next_move ^ 1): # if next_move is not back move, then continue
            new_cube_state = CubeState(cube_state.cube, cube_state.path, next_move)
            next_layer.append(new_cube_state)
    return next_layer


def solve_cube(cube, limit) -> list:
    """solution"""
    cube_state = CubeState(cube)
    if cube_state.is_solved():
        return cube.path

    this_layer_cubes = [cube_state]
    while True:
        if len(this_layer_cubes[0].path) > limit:
            return []

        next_layer_cubes = []
        for this_cube in this_layer_cubes:
            next_layer = make_next_layer_for(this_cube)
            for next_layer_cube in next_layer:
                if next_layer_cube.is_solved():
                    return next_layer_cube.path
            next_layer_cubes.extend(next_layer)
        this_layer_cubes = next_layer_cubes


def main():
    depth = 7
    seed_moves_count = depth

    cube = create_scrumbled_cube(seed_moves_count * 3)
    solution = solve_cube(cube, depth)
    if solution:
        print_solution(cube, solution)
    else:
        print('No solution found for depth {}.'.format(depth))

if __name__ == '__main__':
    main()
