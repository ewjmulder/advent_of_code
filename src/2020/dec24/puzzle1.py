from src.util import *

lines = parse_string_list_from_file(INPUT)

steps_list = []
for line in lines:
    steps = []
    steps_list.append(steps)
    i = 0
    while i < len(line):
        if line[i] == "e":
            steps.append((2, 0))
            i += 1
        elif line[i] == "w":
            steps.append((-2, 0))
            i += 1
        elif line[i:i+2] == "ne":
            steps.append((1, 1))
            i += 2
        elif line[i:i+2] == "nw":
            steps.append((-1, 1))
            i += 2
        elif line[i:i+2] == "se":
            steps.append((1, -1))
            i += 2
        elif line[i:i+2] == "sw":
            steps.append((-1, -1))
            i += 2

print(steps_list)

tiles = {}
for steps in steps_list:
    x = 0
    y = 0
    for (step_x, step_y) in steps:
        x += step_x
        y += step_y
    end = (x, y)
    tiles.setdefault(end, True)
    tiles[end] = not tiles[end]

count = sum([1 for color in tiles.values() if not color])
print(count)
