#!/usr/bin/python3
"""print cube console"""

#     side     color
#      u         w
#    l f r     g o b
#      d         y
#      b         r

def show_cube_console(cube):
    """Print cube in console output"""
    print_side_intended(cube.up_side())

    left = cube.left_side()
    front = cube.front_side()
    right = cube.right_side()

    print(left.tiles[0].color.value + " " + left.tiles[1].color.value + " " \
        + front.tiles[0].color.value + " " + front.tiles[1].color.value + " " \
        + right.tiles[0].color.value + " " + right.tiles[1].color.value)
    print(left.tiles[3].color.value + " " + left.tiles[2].color.value + " " \
        + front.tiles[3].color.value + " " + front.tiles[2].color.value + " " \
        + right.tiles[3].color.value + " " + right.tiles[2].color.value)
    print_side_intended(cube.down_side())
    print_side_intended(cube.back_side())
    print('')

def print_side_intended(side):
    """print intended side"""
    print('    ' + side.tiles[0].color.value + " " + side.tiles[1].color.value)
    print('    ' + side.tiles[3].color.value + " " + side.tiles[2].color.value)
