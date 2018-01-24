#!/usr/bin/python3

#  rubicsCube2x2
"""Cube 2x2x2 Model"""

from enum import Enum
from random import randint

class Color(Enum):
    """Colors for Tile"""
    WHITE = 'W'      # up
    ORANGE = 'O'     # front
    YELLOW = 'Y'     # down
    RED = 'R'        # back
    GREEN = 'G'      # right
    BLUE = 'B'       # left

class Tile(object):
    """One cube tile with some color."""
    def __init__(self, color):
        self.color = color

    def is_equal_to(self, tile): # -> bool:
        """Compare with Tile. Returns bool."""
        return self.color is tile.color


class Side2x2(object):
    """2x2 Cube Side.
    Contains 4 items Array with Color value:
    # 0 1
    # 3 2
    """

    def __init__(self, color):
        self.tiles = [Tile(color)] * 4

    def is_equal_to(self, side): # -> bool:
        """Compare with Side. Returns bool."""
        for index in range(0, 4):
            tile = self.tiles[index]
            other_tile = side.tiles[index]
            if not tile.is_equal_to(other_tile):
                return False
        return True

    def turn_cw(self):
        """Turn Side CW"""
        last = self.tiles[3]
        self.tiles[3] = self.tiles[2]
        self.tiles[2] = self.tiles[1]
        self.tiles[1] = self.tiles[0]
        self.tiles[0] = last
        return self

    def turn_ccw(self):
        """Turn Side CCW"""
        first = self.tiles[0]
        self.tiles[0] = self.tiles[1]
        self.tiles[1] = self.tiles[2]
        self.tiles[2] = self.tiles[3]
        self.tiles[3] = first
        return self

    def get_12(self):
        return self.tiles[1:3]


class SideKey(Enum):
    """String Keys for 2x22 Cube sides Dictionary"""
    UP = 'up'
    FRONT = 'front'
    DOWN = 'down'
    BACK = 'back'
    LEFT = 'left'
    RIGHT = 'right'


class RubicsCube2x2(object):
    """
    RubicksCube 2x2 model. Contains Dictionary<SideKey:Side2x2>

       u        w
     l f r    g o b
       d        y
       b        r
    """

    def __init__(self):
        self._sides = {}
        self._sides[SideKey.UP] = Side2x2(Color.WHITE)
        self._sides[SideKey.FRONT] = Side2x2(Color.ORANGE)
        self._sides[SideKey.DOWN] = Side2x2(Color.YELLOW)
        self._sides[SideKey.BACK] = Side2x2(Color.RED)
        self._sides[SideKey.LEFT] = Side2x2(Color.GREEN)
        self._sides[SideKey.RIGHT] = Side2x2(Color.BLUE)

    def up_side(self):
        return self._sides[SideKey.UP]

    def down_side(self):
        return self._sides[SideKey.DOWN]

    def front_side(self):
        return self._sides[SideKey.FRONT]

    def back_side(self):
        return self._sides[SideKey.BACK]

    def left_side(self):
        return self._sides[SideKey.LEFT]

    def right_side(self):
        return self._sides[SideKey.RIGHT]

    def is_equal_to(self, cube): # -> bool:
        """Compare with cube. Returns bool."""
        for side_key in SideKey:
            if not self._sides[side_key].is_equal_to(cube._sides[side_key]):
                return False
        return True

    def turn_left(self):
        """Turn all Cube Left"""
        self._sides[SideKey.UP] = self._sides[SideKey.UP].turn_cw()
        self._sides[SideKey.DOWN] = self._sides[SideKey.DOWN].turn_ccw()
        front_side = self._sides[SideKey.FRONT]
        self._sides[SideKey.FRONT] = self._sides[SideKey.RIGHT]
        self._sides[SideKey.RIGHT] = self._sides[SideKey.BACK].turn_cw().turn_cw()
        self._sides[SideKey.BACK] = self._sides[SideKey.LEFT].turn_cw().turn_cw()
        self._sides[SideKey.LEFT] = front_side

    def turn_right(self):
        """Turn all Cube Right"""
        self._sides[SideKey.UP] = self._sides[SideKey.UP].turn_ccw()
        self._sides[SideKey.DOWN] = self._sides[SideKey.DOWN].turn_cw()
        front_side = self._sides[SideKey.FRONT]
        self._sides[SideKey.FRONT] = self._sides[SideKey.LEFT]
        self._sides[SideKey.LEFT] = self._sides[SideKey.BACK].turn_cw().turn_cw()
        self._sides[SideKey.BACK] = self._sides[SideKey.RIGHT].turn_cw().turn_cw()
        self._sides[SideKey.RIGHT] = front_side

    def turn_up(self):
        """Turn all Cube Up"""
        self._sides[SideKey.LEFT] = self._sides[SideKey.LEFT].turn_ccw()
        self._sides[SideKey.RIGHT] = self._sides[SideKey.RIGHT].turn_cw()
        front_side = self._sides[SideKey.FRONT]
        self._sides[SideKey.FRONT] = self._sides[SideKey.DOWN]
        self._sides[SideKey.DOWN] = self._sides[SideKey.BACK]
        self._sides[SideKey.BACK] = self._sides[SideKey.UP]
        self._sides[SideKey.UP] = front_side


    def turn_down(self):
        """Turn all Cube Down"""
        self._sides[SideKey.LEFT] = self._sides[SideKey.LEFT].turn_cw()
        self._sides[SideKey.RIGHT] = self._sides[SideKey.RIGHT].turn_ccw()
        front_side = self._sides[SideKey.FRONT]
        self._sides[SideKey.FRONT] = self._sides[SideKey.UP]
        self._sides[SideKey.UP] = self._sides[SideKey.BACK]
        self._sides[SideKey.BACK] = self._sides[SideKey.DOWN]
        self._sides[SideKey.DOWN] = front_side

    def rotate_left(self):
        """Rotate all Cube Left"""
        self._sides[SideKey.FRONT] = self._sides[SideKey.FRONT].turn_ccw()
        self._sides[SideKey.BACK] = self._sides[SideKey.BACK].turn_cw()
        up_side = self._sides[SideKey.UP]
        self._sides[SideKey.UP] = self._sides[SideKey.RIGHT].turn_ccw()
        self._sides[SideKey.RIGHT] = self._sides[SideKey.DOWN].turn_ccw()
        self._sides[SideKey.DOWN] = self._sides[SideKey.LEFT].turn_ccw()
        self._sides[SideKey.LEFT] = up_side.turn_ccw()

    def rotate_right(self):
        """Rotate all Cube Right"""
        self._sides[SideKey.FRONT] = self._sides[SideKey.FRONT].turn_cw()
        self._sides[SideKey.BACK] = self._sides[SideKey.BACK].turn_ccw()
        up_side = self._sides[SideKey.UP]
        self._sides[SideKey.UP] = self._sides[SideKey.LEFT].turn_cw()
        self._sides[SideKey.LEFT] = self._sides[SideKey.DOWN].turn_cw()
        self._sides[SideKey.DOWN] = self._sides[SideKey.RIGHT].turn_cw()
        self._sides[SideKey.RIGHT] = up_side.turn_cw()

    def R(self):
        """Right 1/4 turn rotation up"""
        self._sides[SideKey.RIGHT] = self._sides[SideKey.RIGHT].turn_cw()
        front_side_tiles = self.front_side().get_12()
        self._sides[SideKey.FRONT].tiles[1:3] = self.down_side().get_12()
        self._sides[SideKey.DOWN].tiles[1:3] = self.back_side().get_12()
        self._sides[SideKey.BACK].tiles[1:3] = self.up_side().get_12()
        self._sides[SideKey.UP].tiles[1:3] = front_side_tiles

    def Ri(self):
        """Right 1/4 turn rotation down"""
        self._sides[SideKey.RIGHT] = self._sides[SideKey.RIGHT].turn_ccw()
        front_side_tiles = self.front_side().get_12()
        self._sides[SideKey.FRONT].tiles[1:3] = self._sides[SideKey.UP].get_12()
        self._sides[SideKey.UP].tiles[1:3] = self._sides[SideKey.BACK].get_12()
        self._sides[SideKey.BACK].tiles[1:3] = self._sides[SideKey.DOWN].get_12()
        self._sides[SideKey.DOWN].tiles[1:3] = front_side_tiles

    def L(self):
        """Left 1/4 turn rotation down"""
        self.R()
        self.turn_down()

    def Li(self):
        """Left 1/4 turn rotation up"""
        self.Ri()
        self.turn_up()

    def B(self):
        """Back 1/4 turn rotation CCW"""
        self.turn_left()
        self.R()
        self.turn_right()

    def Bi(self):
        """Back 1/4 turn rotation CW"""
        self.turn_left()
        self.Ri()
        self.turn_right()

    def D(self):
        """Down 1/4 turn rotation right"""
        self.rotate_left()
        self.R()
        self.rotate_right()

    def Di(self):
        """Down 1/4 turn rotation left"""
        self.rotate_left()
        self.Ri()
        self.rotate_right()

    def F(self):
        """Front 1/4 turn rotation CW"""
        self.turn_right()
        self.R()
        self.turn_left()

    def Fi(self):
        """Front 1/4 turn rotation CCW"""
        self.turn_right()
        self.Ri()
        self.turn_left()

    def U(self):
        """Up 1/4 turn rotation right"""
        self.rotate_right()
        self.R()
        self.rotate_left()

    def Ui(self):
        """Up 1/4 turn rotation left"""
        self.rotate_right()
        self.Ri()
        self.rotate_left()

    def do_move(self, i):
        if i == 0:
            self.R()
        if i == 1:
            self.Ri()
        if i == 2:
            self.L()
        if i == 3:
            self.Li()
        if i == 4:
            self.B()
        if i == 5:
            self.Bi()
        if i == 6:
            self.D()
        if i == 7:
            self.Di()
        if i == 8:
            self.F()
        if i == 9:
            self.Fi()
        if i == 10:
            self.U()
        if i == 11:
            self.Ui()

        if i == 12:
            self.turn_left()
        if i == 13:
            self.turn_right()
        if i == 14:
            self.turn_up()
        if i == 15:
            self.turn_down()
        if i == 16:
            self.rotate_left()
        if i == 17:
            self.rotate_right()

    def do_random_move(self):
        i = randint(0, 12)
        self.do_move(i)
        return i

    def do_n_random_moves(self, n):
        seed = []
        for i in range(0, n):
            move = self.do_random_move()
            seed.append(move)
        return seed

    def is_solved(self):
        for key, side in self._sides.items():
            first_tile = side.tiles[0]
            for tile in side.tiles:
                if not tile.is_equal_to(first_tile):
                    return False
        return True
