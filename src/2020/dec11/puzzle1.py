from src.util import *

grid = parse_character_grid_from_file(INPUT)


def update(value: str, coordinate: Coordinate):
    taken = grid.get_neighbors(coordinate).count("#")
    if value == ".":
        return "."
    elif value == "L":
        if taken == 0:
            return "#"
        else:
            return "L"
    elif value == "#":
        if taken >= 4:
            return "L"
        else:
            return "#"


while True:
    new_grid = grid.map_values_and_coordinates(update)
    if grid == new_grid:
        break
    else:
        grid = new_grid


print(grid)
print("")
print(grid.count("#"))
