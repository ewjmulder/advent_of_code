def calc(x, y, ser_nr):
    rack_id = x + 10
    s = rack_id * y
    i = s + ser_nr
    m = i * rack_id
    n = int(str(m)[-3])
    return n - 5


ser_nr = 7165
#ser_nr = 42
grid = []
empty_line = []
for x in range(0, 301):
    empty_line.append(-999)
for y in range(0, 301):
    grid.append(empty_line.copy())
for x in range(1, 301):
    for y in range(1, 301):
        grid[y][x] = calc(x, y, ser_nr)

max_total = -999
max_coord = (None, None)
max_size = -1
grids = []
grids.append([])
grids.append(grid)
for size in range(2, 25): # never goes very high, so 301 not needed
    if size % 10 == 0:
        print(str(size / 300 * 100) + "%")
    new_grid = []
    grids.append(new_grid)
    for y in range(0, 301):
        new_grid.append(empty_line.copy())
    for x in range(1, 302 - size):
        for y in range(1, 302 - size):
            total = grids[size - 1][y][x]
            for i in range(0, size):
                total += grid[y + size - 1][x + i]
            for j in range(0, size - 1):
                total += grid[y + j][x + size - 1]
            new_grid[y][x] = total
            if total > max_total:
                max_total = total
                max_coord = (x, y)
                max_size = size

print(max_total)
print(max_coord)
print(max_size)
