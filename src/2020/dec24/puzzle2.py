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

neighbor_diffs = [(2, 0), (-2, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

count = sum([1 for color in tiles.values() if not color])
print(f"0: {count}")

days = 100
for day in range(1, days + 1):
    new_tiles = {}
    min_x = min([x for (x, y) in tiles])
    max_x = max([x for (x, y) in tiles])
    min_y = min([y for (x, y) in tiles])
    max_y = max([y for (x, y) in tiles])
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 2, max_x + 3):
            count_black = 0
            for (diff_x, diff_y) in neighbor_diffs:
                neighbor = (x + diff_x, y + diff_y)
                if tiles.__contains__(neighbor):
                    if not tiles.get(neighbor):
                        count_black += 1
            current_color = True
            if tiles.__contains__((x, y)):
                current_color = tiles[(x, y)]
            if current_color and count_black == 2:
                new_tiles[(x, y)] = False
            elif not current_color and (count_black == 1 or count_black == 2):
                new_tiles[(x, y)] = False

    tiles = new_tiles

    count = sum([1 for color in tiles.values() if not color])
    print(f"{day}: {count}")
