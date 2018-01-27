#!/usr/bin/python3

from copy import deepcopy
from RubicsCube2x2 import RubicsCube2x2

class CubeState(object):
    def __init__(self, cube=None, path=None, move=None):
        self.cube = deepcopy(cube) if cube else RubicsCube2x2()
        self.path = deepcopy(path) if path else []
        if move:
            self.cube.do_move(move)
            self.path.append(move)

    def is_solved(self) -> bool:
        return self.cube.is_solved()
