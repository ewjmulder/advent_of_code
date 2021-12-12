from src.util import *

octos = Parser.from_file(INPUT).to_number_grid(separator="")

steps = 100

flashes = 0
flashed_step = []


def flash(grid, cells):
    global flashes, flashed_step
    flashes += len(cells)
    for c in cells:
        flashed_step.append(c)
        neighbors = grid.get_neighbor_cells(c.coord, include_diagonal=True)
        for n in neighbors:
            if grid[n.coord.row][n.coord.column] > 0 and n not in flashed_step:
                grid[n.coord.row][n.coord.column] += 1
    fs = []
    for c in cells:
        neighbors = grid.get_neighbor_cells(c.coord, include_diagonal=True)
        for n in neighbors:
            if grid.get_value(n.coord) >= 10:
                grid[n.coord.row][n.coord.column] = 0
                fs.append(n)
    if len(fs) > 0:
        flash(grid, fs)


print(octos.to_string_justified())
print()
for step in range(steps):
    flashed_step = []
    octos = octos.map_values(lambda x: x + 1)
    nines = octos.find_cells_by_value(10)
    octos = octos.map_values(lambda x: 0 if x == 10 else x)
    flash(octos, nines)
    print(octos.to_string_justified())
    print()

print(flashes)
