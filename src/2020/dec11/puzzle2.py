from src.util import *

grid = parse_character_grid_from_file(SAMPLE)

directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def update(value: str, coordinate: Coordinate):
    taken = 0
    for direction in directions:
        multiplier = 1
        row_to_check = coordinate.row + multiplier * direction[0]
        column_to_check = coordinate.column + multiplier * direction[1]
        while 0 <= row_to_check < grid.height and 0 <= column_to_check < grid.width:
            if grid[row_to_check][column_to_check] == "#":
                taken += 1
                break
            multiplier += 1
            row_to_check = coordinate.row + multiplier * direction[0]
            column_to_check = coordinate.column + multiplier * direction[1]
    if value == ".":
        return "."
    elif value == "L":
        if taken == 0:
            return "#"
        else:
            return "L"
    elif value == "#":
        if taken >= 5:
            return "L"
        else:
            return "#"


while True:
    print(grid)
    print("")
    new_grid = grid.map_values_and_coordinates(update)
    if grid == new_grid:
        break
    else:
        grid = new_grid


print(grid)
print("")
print(grid.count("#"))
