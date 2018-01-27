#!/usr/bin/python3
""" depth step by step brute force """

from RubicsCube2x2 import RubicsCube2x2
from create_random_cube import create_cube
from solve06_CubeState import CubeState
from print_solution import print_solution

from print_cube_console import show_cube_console

def make_next_layer_for_cube(cube_state) -> dict:
    """ we need to go deeper """
    next_layer = {}
    for next_move in range(0, 6): # sequentive next move
        previous_move = -1
        if cube_state.path:
            previous_move = cube_state.path[-1]
        if (previous_move ^ 1) != next_move: # if next_move is not back move, then continue
            next_cube_state = CubeState(cube_state.cube, cube_state.path, next_move)
            next_layer[next_cube_state.cube.hash()] = next_cube_state
    return next_layer


def make_next_layer_for_layer(cube_layer) -> dict:
    next_layer_cubes = {}
    for hash, cube in cube_layer.items():
        next_branch = make_next_layer_for_cube(cube)
        next_layer_cubes.update(next_branch)
    return next_layer_cubes

def check_for_matches(ls_cubes, rs_cubes) -> (CubeState, CubeState):
    """ look for identical cubes """
    for l_cube in ls_cubes:
        if l_cube in rs_cubes:
            return(ls_cubes[l_cube], rs_cubes[l_cube])
    return None

def combine_solution(dcube, icube) -> list:
    print(dcube.path, icube.path)
    dpath = dcube.path
    ipath = icube.path
    path = dpath
    for move in list(reversed(ipath)):
        path.append(move ^ 1)
    return path

def print_solution_cubes(dcube, icube):
    show_cube_console(dcube)
    print()
    show_cube_console(icube)
    print()

def solve_cube(cube, limit) -> list:
    """solution"""
    cube_state = CubeState(cube)
    if cube_state.is_solved():
        return cube.path

    direct_layer_cubes = {cube_state.cube.hash(): cube_state}
    new_cube_state = CubeState(RubicsCube2x2())
    inverse_layer_cube = {new_cube_state.cube.hash(): new_cube_state}
    while True:
        direct_layer_cubes = make_next_layer_for_layer(direct_layer_cubes)
        match = check_for_matches(direct_layer_cubes, inverse_layer_cube)
        if match:
            path = combine_solution(match[0], match[1])
            return path

        inverse_layer_cube = make_next_layer_for_layer(inverse_layer_cube)
        match = check_for_matches(direct_layer_cubes, inverse_layer_cube)
        if match:
            path = combine_solution(match[0], match[1])
            return path

        for hash, cube_state in inverse_layer_cube.items():
            current_depth = len(cube_state.path)
            if current_depth > limit:
                print('current_depth > limit')
                return []


def main():
    depth = 7
    seed_moves_count = depth

    cube = create_cube(seed_moves_count * 4)
    solution = solve_cube(cube, depth)
    if solution:
        print_solution(cube, solution)
    else:
        print('No solution found for depth {}.'.format(depth))

if __name__ == '__main__':
    main()