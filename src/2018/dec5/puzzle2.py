input = open("input1", "r")
lines = input.readlines()

coords = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in lines]

# counts = {}
# for coord in coords:
#     counts[coord] = 0

region = 0
for x in range (0, 400):
    for y in range (0, 400):
        print(x, y)
        dists = {coord: (abs(coord[0] - x) + abs(coord[1] - y)) for coord in coords}
        total_dist = sum([dist for (coord, dist) in dists.items()])
        if total_dist < 10000:
            region += 1

print(region)
