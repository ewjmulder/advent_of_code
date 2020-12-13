input = open("input1", "r")
lines = input.readlines()

coords = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in lines]

counts = {}
for coord in coords:
    counts[coord] = 0

for x in range (-100, 500):
    for y in range (-100, 500):
        # print(x, y)
        dists = {coord: (abs(coord[0] - x) + abs(coord[1] - y)) for coord in coords}
        min_dist = min([dist for (coord, dist) in dists.items()])
        min_coords = [coord for (coord, dist) in dists.items() if dist == min_dist]
        if len(min_coords) == 1:
            counts[min_coords[0]] += 1

counts_a = counts

counts = {}
for coord in coords:
    counts[coord] = 0

for x in range (0, 400):
    for y in range (0, 400):
        # print(x, y)
        dists = {coord: (abs(coord[0] - x) + abs(coord[1] - y)) for coord in coords}
        min_dist = min([dist for (coord, dist) in dists.items()])
        min_coords = [coord for (coord, dist) in dists.items() if dist == min_dist]
        if len(min_coords) == 1:
            counts[min_coords[0]] += 1

counts_b = counts

counts = {}
for coord in coords:
    if counts_a[coord] == counts_b[coord]:
        counts[coord] = counts_a[coord]

print(counts)

max_c = max([cnt for (coord, cnt) in counts.items()])

print(max_c)
