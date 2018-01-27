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

    def is_equal_to(self, tile) -> bool:
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

    def is_equal_to(self, side) -> bool:
        """Compare with Side. Returns bool."""
        for index in range(0, 4):
            if self.code(index) == side.code():
                return True
        return False

    def code(self, offset = 0) -> str:
        result = []
        for index in range(4):
            result.append(self.tiles[index].color.value)
        for i in range(offset):
            result.insert(0, result.pop())
        return result

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
        self.sides = {}
        self.sides[SideKey.UP] = Side2x2(Color.WHITE)
        self.sides[SideKey.FRONT] = Side2x2(Color.ORANGE)
        self.sides[SideKey.DOWN] = Side2x2(Color.YELLOW)
        self.sides[SideKey.BACK] = Side2x2(Color.RED)
        self.sides[SideKey.LEFT] = Side2x2(Color.BLUE)
        self.sides[SideKey.RIGHT] = Side2x2(Color.GREEN)

    def up_side(self):
        return self.sides[SideKey.UP]

    def down_side(self):
        return self.sides[SideKey.DOWN]

    def front_side(self):
        return self.sides[SideKey.FRONT]

    def back_side(self):
        return self.sides[SideKey.BACK]

    def left_side(self):
        return self.sides[SideKey.LEFT]

    def right_side(self):
        return self.sides[SideKey.RIGHT]

    def is_equal_to(self, cube): # -> bool:
        """Compare with cube. Returns bool."""
        equal_sides = 0
        for key, my_side in self.sides.items():
            for key, other_side in cube.sides.items():
                if my_side.is_equal_to(other_side):
                    equal_sides += 1
                    break
        return equal_sides == 6

    def turn_left(self):
        """Turn all Cube Left"""
        self.sides[SideKey.UP] = self.sides[SideKey.UP].turn_cw()
        self.sides[SideKey.DOWN] = self.sides[SideKey.DOWN].turn_ccw()
        front_side = self.sides[SideKey.FRONT]
        self.sides[SideKey.FRONT] = self.sides[SideKey.RIGHT]
        self.sides[SideKey.RIGHT] = self.sides[SideKey.BACK].turn_cw().turn_cw()
        self.sides[SideKey.BACK] = self.sides[SideKey.LEFT].turn_cw().turn_cw()
        self.sides[SideKey.LEFT] = front_side

    def turn_right(self):
        """Turn all Cube Right"""
        self.sides[SideKey.UP] = self.sides[SideKey.UP].turn_ccw()
        self.sides[SideKey.DOWN] = self.sides[SideKey.DOWN].turn_cw()
        front_side = self.sides[SideKey.FRONT]
        self.sides[SideKey.FRONT] = self.sides[SideKey.LEFT]
        self.sides[SideKey.LEFT] = self.sides[SideKey.BACK].turn_cw().turn_cw()
        self.sides[SideKey.BACK] = self.sides[SideKey.RIGHT].turn_cw().turn_cw()
        self.sides[SideKey.RIGHT] = front_side

    def turn_up(self):
        """Turn all Cube Up"""
        self.sides[SideKey.LEFT] = self.sides[SideKey.LEFT].turn_ccw()
        self.sides[SideKey.RIGHT] = self.sides[SideKey.RIGHT].turn_cw()
        front_side = self.sides[SideKey.FRONT]
        self.sides[SideKey.FRONT] = self.sides[SideKey.DOWN]
        self.sides[SideKey.DOWN] = self.sides[SideKey.BACK]
        self.sides[SideKey.BACK] = self.sides[SideKey.UP]
        self.sides[SideKey.UP] = front_side


    def turn_down(self):
        """Turn all Cube Down"""
        self.sides[SideKey.LEFT] = self.sides[SideKey.LEFT].turn_cw()
        self.sides[SideKey.RIGHT] = self.sides[SideKey.RIGHT].turn_ccw()
        front_side = self.sides[SideKey.FRONT]
        self.sides[SideKey.FRONT] = self.sides[SideKey.UP]
        self.sides[SideKey.UP] = self.sides[SideKey.BACK]
        self.sides[SideKey.BACK] = self.sides[SideKey.DOWN]
        self.sides[SideKey.DOWN] = front_side

    def rotate_left(self):
        """Rotate all Cube Left"""
        self.sides[SideKey.FRONT] = self.sides[SideKey.FRONT].turn_ccw()
        self.sides[SideKey.BACK] = self.sides[SideKey.BACK].turn_cw()
        up_side = self.sides[SideKey.UP]
        self.sides[SideKey.UP] = self.sides[SideKey.RIGHT].turn_ccw()
        self.sides[SideKey.RIGHT] = self.sides[SideKey.DOWN].turn_ccw()
        self.sides[SideKey.DOWN] = self.sides[SideKey.LEFT].turn_ccw()
        self.sides[SideKey.LEFT] = up_side.turn_ccw()

    def rotate_right(self):
        """Rotate all Cube Right"""
        self.sides[SideKey.FRONT] = self.sides[SideKey.FRONT].turn_cw()
        self.sides[SideKey.BACK] = self.sides[SideKey.BACK].turn_ccw()
        up_side = self.sides[SideKey.UP]
        self.sides[SideKey.UP] = self.sides[SideKey.LEFT].turn_cw()
        self.sides[SideKey.LEFT] = self.sides[SideKey.DOWN].turn_cw()
        self.sides[SideKey.DOWN] = self.sides[SideKey.RIGHT].turn_cw()
        self.sides[SideKey.RIGHT] = up_side.turn_cw()

    def R(self):
        """Right 1/4 turn rotation up"""
        self.sides[SideKey.RIGHT] = self.sides[SideKey.RIGHT].turn_cw()
        front_side_tiles = self.front_side().get_12()
        self.sides[SideKey.FRONT].tiles[1:3] = self.down_side().get_12()
        self.sides[SideKey.DOWN].tiles[1:3] = self.back_side().get_12()
        self.sides[SideKey.BACK].tiles[1:3] = self.up_side().get_12()
        self.sides[SideKey.UP].tiles[1:3] = front_side_tiles

    def Ri(self):
        """Right 1/4 turn rotation down"""
        self.sides[SideKey.RIGHT] = self.sides[SideKey.RIGHT].turn_ccw()
        front_side_tiles = self.front_side().get_12()
        self.sides[SideKey.FRONT].tiles[1:3] = self.sides[SideKey.UP].get_12()
        self.sides[SideKey.UP].tiles[1:3] = self.sides[SideKey.BACK].get_12()
        self.sides[SideKey.BACK].tiles[1:3] = self.sides[SideKey.DOWN].get_12()
        self.sides[SideKey.DOWN].tiles[1:3] = front_side_tiles

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
        # unique moves
        if i == 0:
            self.R()
            return "R"
        if i == 1:
            self.Ri()
            return 'Ri'
        if i == 2:
            self.F()
            return 'F'
        if i == 3:
            self.Fi()
            return 'Fi'
        if i == 4:
            self.U()
            return 'U'
        if i == 5:
            self.Ui()
            return 'Ui'

        # other moves
        if i == 6:
            self.L()
            return 'L'
        if i == 7:
            self.Li()
            return 'Li'
        if i == 8:
            self.B()
            return 'B'
        if i == 9:
            self.Bi()
            return 'Bi'
        if i == 10:
            self.D()
            return 'D'
        if i == 11:
            self.Di()
            return 'Di'
        
        # non mutate moves
        if i == 12:
            self.turn_left()
            return 'turn_left'
        if i == 13:
            self.turn_right()
            return 'turn_right'
        if i == 14:
            self.turn_up()
            return 'turn_up'
        if i == 15:
            self.turn_down()
            return 'turn_down'
        if i == 16:
            self.rotate_left()
            return 'rotate_left'
        if i == 17:
            self.rotate_right()
            return 'rotate_right'

    def do_random_move(self, prevoius_move = -1):
        while True:
            next_move = randint(0, 5)
            if (prevoius_move ^ 1) != next_move: #don't do back move
                self.do_move(next_move)
                return next_move

    def do_n_random_moves(self, n):
        seed = []
        for i in range(0, n):
            prevoius_move = -1
            if seed:
                prevoius_move = seed[-1] 
            move = self.do_random_move(prevoius_move)
            seed.append(move)
        return seed

    def is_solved(self) -> bool:
        for key, side in self.sides.items():
            first_tile = side.tiles[0]
            for tile in side.tiles:
                if not tile.is_equal_to(first_tile):
                    return False
        return True
