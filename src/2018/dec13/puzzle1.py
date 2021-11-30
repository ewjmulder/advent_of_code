from src.util import *
from enum import Enum


class Direction(Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


@dataclass
class Cart:
    pos: Coordinate
    dir: Direction


def to_cart(cart_data: Tuple[str, Coordinate]) -> Cart:
    (icon, coordinate) = cart_data
    return Cart(coordinate, Direction(icon))


grid = parse_character_grid_from_file(SAMPLE)
carts = list(map(to_cart, grid.find_cells([">", "<", "^", "v"])))
grid = grid.replace_values({">": "-", "<": "-", "^": "|", "v": "|"})

carts = reversed(carts)
print(sorted(carts, key=lambda cart: cart.pos.row * grid.width + cart.pos.column))

# collision = None
# while collision is None:
#     sorted(carts, key=lambda cart: cart.pos.row * grid.width + cart.pos.column)
#
#
# print(collision)
