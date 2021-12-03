import sys
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


grid = parse_character_grid_from_file(SAMPLE2)
carts = list(map(to_cart, grid.find_cells([">", "<", "^", "v"])))
grid = grid.replace_values({">": "-", "<": "-", "^": "|", "v": "|"})


def print_grid_with_cards(carts, removed_carts):
    lines = grid.to_string_list()
    for active_cart in [cart for cart in carts if cart not in removed_carts]:
        lines[active_cart.pos.row] = lines[active_cart.pos.row][:active_cart.pos.column] + "C" + lines[active_cart.pos.row][active_cart.pos.column + 1:]
    print("\n".join(lines))
    print("")

count = 0
leftover: Cart = None
removed_carts = []
while leftover is None:
    carts = sorted(carts, key=lambda cart: cart.pos.row * grid.width + cart.pos.column)
    count += 1
    # if count % 100 == 0:
    #     print(len(carts), len(removed_carts))
    if count > 100:
        sys.exit(1)
    for cart in carts:
        if cart not in removed_carts:
            print_grid_with_cards(carts, removed_carts)
            cart.step()
            for (c1, c2) in list(combinations([cart for cart in carts if cart not in removed_carts], 2)):
                if c1.pos == c2.pos:
                    # Upon collision, remove those 2 carts
                    removed_carts.append(c1)
                    removed_carts.append(c2)
                    if len(carts) - len(removed_carts) == 1:
                        leftover = [cart for cart in carts if cart not in removed_carts][0]
                        break

print(len(removed_carts))
print_grid_with_cards(carts, removed_carts)
print(f"{leftover.pos.column},{leftover.pos.row}")
