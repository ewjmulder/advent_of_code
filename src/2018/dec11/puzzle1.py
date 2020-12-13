def calc(x, y, ser_nr):
    rack_id = x + 10
    s = rack_id * y
    i = s + ser_nr
    m = i * rack_id
    n = int(str(m)[-3])
    return n - 5


#ser_nr = 7165
ser_nr = 42
grid = []
empty_line = []
for x in range(0, 301):
    empty_line.append(-999)
for y in range(0, 301):
    grid.append(empty_line.copy())
for x in range(1, 301):
    for y in range(1, 301):
        grid[x][y] = calc(x, y, ser_nr)

max_total = -999
max_coord = (None, None)
for x in range(1, 299):
    for y in range(1, 299):
        total = 0
        for i in range(0, 3):
            for j in range(0, 3):
                total += grid[x + i][y + j]
        if total > max_total:
            max_total = total
            max_coord = (x, y)

print(max_total)
print(max_coord)
