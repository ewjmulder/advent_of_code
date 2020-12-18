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

# print(grids)

empty_grids = {}
for i in range(-1 * cycles, cycles + 1):
    empty_grids[i] = empty_grid()

# print("empty_grids:", empty_grids)

fourth_dim = {}
for i in range(-1 * cycles, cycles + 1):
    fourth_dim[i] = {i: empty_grid() for i in range(-1 * cycles, cycles + 1)}
fourth_dim[0] = grids

# print("fourth_dim:", fourth_dim)

curr_z = ValueReference(0)
curr_w = ValueReference(0)


def map_val(val, coord):
    count = 0
    amount = 0
    for w in range(curr_w.value - 1, curr_w.value + 2):
        for z in range(curr_z.value - 1, curr_z.value + 2):
            if -1 * cycles <= z <= cycles and -1 * cycles <= w <= cycles:
                include_self = z != curr_z.value or w != curr_w.value
                neighbors = fourth_dim[w][z].get_neighbors(coord, include_own_cell=include_self)
                amount += len(neighbors)
                count += neighbors.count("#")
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
    print("cycle:", cycle)
    new_fourth_dim = {}
    for w in range(-1 * cycles, cycles + 1):
        curr_w.value = w
        grids = fourth_dim[w]
        new_grids = {}
        for z in range(-1 * cycles, cycles + 1):
            curr_z.value = z
            grid = grids[z]
            new_grid = grid.map_values_and_coordinates(map_val)
            new_grids[z] = new_grid
        new_fourth_dim[w] = new_grids
        # print(new_grids)
        # for z in new_grids.keys():
        #     print("w:", w, "z:", z)
        #     print(new_grids[z])
        #     print("")
    fourth_dim = new_fourth_dim


summed = 0
for w in range(-1 * cycles, cycles + 1):
    summed += sum(grid.count("#") for grid in fourth_dim[w].values())

print(summed)

