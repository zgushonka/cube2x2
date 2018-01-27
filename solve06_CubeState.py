#!/usr/bin/python3

from copy import deepcopy

class CubeState(object):
    def __init__(self, cube, path = [], move = -1):
        self.cube = deepcopy(cube)
        self.path = deepcopy(path)
        if move > -1:
            self.cube.do_move(move)
            self.path.append(move)

    def is_solved(self) -> bool:
        return self.cube.is_solved()
