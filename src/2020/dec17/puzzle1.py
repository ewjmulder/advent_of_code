from src.util import *

init_grid = parse_string_list_from_file(INPUT)
cycles = 6

size = len(init_grid[0])
for c in range(0, cycles):
    init_grid.insert(0, "." * size)
    init_grid.append("." * size)

for c in range(0, len(init_grid)):
    init_grid[c] = ("." * cycles) + init_grid[c] + ("." * cycles)

grid = parse_character_grid_from_lines(init_grid)

print(grid)

height = grid.height
width = grid.width


def empty_grid():
    return parse_character_grid_from_lines(grid.__str__().replace("#", ".").split("\n"))


grids = {}
for i in range(-1 * cycles, cycles + 1):
    grids[i] = empty_grid()
grids[0] = grid

print(grids)

curr_z = ValueReference(0)


def map_val(val, coord):
    count = 0
    # print(f"cur_z {curr_z.value} coord: {coord.x}, {coord.y}")
    for z in range(curr_z.value - 1, curr_z.value + 2):
        if -1 * cycles <= z <= cycles:
            include_self = z != curr_z.value
            count += grids[z].get_neighbors(coord, include_own_cell=include_self).count("#")
    if val == "#":
        if 2 <= count <= 3:
            return "#"
        else:
            return "."
    elif val == ".":
        if count == 3:
            return "#"
        else:
            return "."


for cycle in range(1, cycles + 1):
    new_grids = {}
    for z in range(-1 * cycles, cycles + 1):
        # print(f"cycle {cycle} z {z}")
        curr_z.value = z
        grid = grids[z]
        new_grid = grid.map_values_and_coordinates(map_val)
        new_grids[z] = new_grid
    grids = new_grids
    print(grids)
    # for z in grids.keys():
    #     print("z:", z)
    #     print(grids[z])
    #     print("")


print(sum(grid.count("#") for grid in grids.values()))

