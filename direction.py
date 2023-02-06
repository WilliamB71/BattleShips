from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @property
    def next(self):
        return Direction((self.value + 1) % 4)


class TextMessages:
    intro1 = 'Place your ships on the board'
    intro2 = 'Move ship = Arrow Keys'
    intro3 = 'Rotate = R'
    intro4 = 'Place Ship = Enter / Space'
