import sys

from src.util import *
from src.util.coordinate import Coordinate

cuc = Parser.from_file(INPUT).to_character_grid()


def move_to_right(c: Coordinate, g: Grid):
    new_col = c.column + 1
    if new_col >= g.width:
        new_col = 0
    return Coordinate(c.row, new_col)


def move_to_down(c: Coordinate, g: Grid):
    new_row = c.row + 1
    if new_row >= g.height:
        new_row = 0
    return Coordinate(new_row, c.column)


def can_move_right(c: Cell, g: Grid[str]):
    new_coord = move_to_right(c.coord, g)
    return g.get_value_by_coord(new_coord) == "."


def can_move_down(c: Cell, g: Grid[str]):
    new_coord = move_to_down(c.coord, g)
    return g.get_value_by_coord(new_coord) == "."


moved = True
step = 0
while moved:
    moved = False
    step += 1
    print("step:", step)
    # print(cuc.to_string())
    if step == 1000:
        sys.exit(1)
    easts = cuc.find_cells_by_value(">")
    move_easts = []
    for east in easts:
        if can_move_right(east, cuc):
            moved = True
            move_easts.append(east)
    for east in move_easts:
        cuc.get_cell_by_coord(east.coord).value = "."
        cuc.get_cell_by_coord(move_to_right(east.coord, cuc)).value = ">"
    souths = cuc.find_cells_by_value("v")
    move_souths = []
    for south in souths:
        if can_move_down(south, cuc):
            moved = True
            move_souths.append(south)
    for south in move_souths:
        cuc.get_cell_by_coord(south.coord).value = "."
        cuc.get_cell_by_coord(move_to_down(south.coord, cuc)).value = "v"

print(step)
