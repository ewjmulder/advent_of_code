lines = [line.rstrip() for line in open("input").readlines()]

import re

def print_grid(lights, prev_width):
    min_x = min([x for [x, _, _, _] in lights])
    max_x = max([x for [x, _, _, _] in lights])
    width = max_x - min_x
    if width > prev_width:
        for light in lights:
            light[0] -= light[2]
            light[1] -= light[3]

        min_x = min([x for [x, _, _, _] in lights])
        max_x = max([x for [x, _, _, _] in lights])
        min_y = min([y for [_, y, _, _] in lights])
        max_y = max([y for [_, y, _, _] in lights])
        coords = [(x, y) for [x, y, _, _] in lights]
        for y in range(min_y, max_y + 1):
            line = ""
            for x in range(min_x, max_x + 1):
                exists = (x, y) in coords
                if exists:
                    line += "#"
                else:
                    line += "."
            print(line)

    return width


lights = []
for line in lines:
    match = re.match("position\=\<[ ]*([0-9-]+),[ ]*([0-9-]+)> velocity\=\<[ ]*([0-9-]+),[ ]*([0-9-]+)\>", line)
    x = int(match.group(1))
    y = int(match.group(2))
    dx = int(match.group(3))
    dy = int(match.group(4))
    pos = (x, y)
    speed = (dx, dy)
    lights.append([x, y, dx, dy])

print(lights)

prev_width = 99999999
while (True):
    for light in lights:
        light[0] += light[2]
        light[1] += light[3]
    width = print_grid(lights, prev_width)
    if width > prev_width:
        break
    else:
        prev_width = width



