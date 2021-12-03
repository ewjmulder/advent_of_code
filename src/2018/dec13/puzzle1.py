from src.util import *
from enum import Enum
from itertools import combinations


class Direction(Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


class Turn(Enum):
    LEFT = "L"
    STRAIGHT = "S"
    RIGHT = "R"


direction_mapping = {
    Direction.LEFT: Coordinate.neighbor_left,
    Direction.RIGHT: Coordinate.neighbor_right,
    Direction.UP: Coordinate.neighbor_above,
    Direction.DOWN: Coordinate.neighbor_below,
}


@dataclass
class Cart:
    pos: Coordinate
    dir: Direction
    next_turn: Turn = Turn.LEFT

    def step(self):
        self.pos = direction_mapping[self.dir](self.pos)
        track = grid.get_cell(self.pos)
        if track == "/":
            if self.dir == Direction.UP:
                self.dir = Direction.RIGHT
            elif self.dir == Direction.DOWN:
                self.dir = Direction.LEFT
            elif self.dir == Direction.LEFT:
                self.dir = Direction.DOWN
            elif self.dir == Direction.RIGHT:
                self.dir = Direction.UP
        elif track == "\\":
            if self.dir == Direction.UP:
                self.dir = Direction.LEFT
            elif self.dir == Direction.DOWN:
                self.dir = Direction.RIGHT
            elif self.dir == Direction.LEFT:
                self.dir = Direction.UP
            elif self.dir == Direction.RIGHT:
                self.dir = Direction.DOWN
        elif track == "+":
            if self.next_turn == Turn.LEFT:
                if self.dir == Direction.UP:
                    self.dir = Direction.LEFT
                elif self.dir == Direction.DOWN:
                    self.dir = Direction.RIGHT
                elif self.dir == Direction.LEFT:
                    self.dir = Direction.DOWN
                elif self.dir == Direction.RIGHT:
                    self.dir = Direction.UP
            elif self.next_turn == Turn.RIGHT:
                if self.dir == Direction.UP:
                    self.dir = Direction.RIGHT
                elif self.dir == Direction.DOWN:
                    self.dir = Direction.LEFT
                elif self.dir == Direction.LEFT:
                    self.dir = Direction.UP
                elif self.dir == Direction.RIGHT:
                    self.dir = Direction.DOWN
            if self.next_turn == Turn.LEFT:
                self.next_turn = Turn.STRAIGHT
            elif self.next_turn == Turn.STRAIGHT:
                self.next_turn = Turn.RIGHT
            elif self.next_turn == Turn.RIGHT:
                self.next_turn = Turn.LEFT


def to_cart(cart_data: Tuple[str, Coordinate]) -> Cart:
    (icon, coordinate) = cart_data
    return Cart(coordinate, Direction(icon))


grid = parse_character_grid_from_file(INPUT)
carts = list(map(to_cart, grid.find_cells([">", "<", "^", "v"])))
grid = grid.replace_values({">": "-", "<": "-", "^": "|", "v": "|"})


collision: Coordinate = None
while collision is None:
    carts = sorted(carts, key=lambda cart: cart.pos.row * grid.width + cart.pos.column)
    for cart in carts:
        cart.step()
        for (c1, c2) in list(combinations(carts, 2)):
            if c1.pos == c2.pos:
                collision = c1.pos

print(f"{collision.column},{collision.row}")
