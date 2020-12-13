input = open("input1", "r")
lines = input.readlines()
height = len(lines)
width = len(lines[0])

trees1 = 0
pos = (0, 0)
dx = 3
dy = 1

while pos[1] < height - 1:
    pos = (pos[0] + dx, pos[1] + dy)
    # print(pos)
    # print(lines[pos[1]][pos[0] % width])
    if lines[pos[1]][pos[0] % (width - 1)] == "#":
        trees1 += 1

trees2 = 0
pos = (0, 0)
dx = 1
dy = 1

while pos[1] < height - 1:
    pos = (pos[0] + dx, pos[1] + dy)
    # print(pos)
    # print(lines[pos[1]][pos[0] % width])
    if lines[pos[1]][pos[0] % (width - 1)] == "#":
        trees2 += 1

trees3 = 0
pos = (0, 0)
dx = 5
dy = 1

while pos[1] < height - 1:
    pos = (pos[0] + dx, pos[1] + dy)
    # print(pos)
    # print(lines[pos[1]][pos[0] % width])
    if lines[pos[1]][pos[0] % (width - 1)] == "#":
        trees3 += 1

trees4 = 0
pos = (0, 0)
dx = 7
dy = 1

while pos[1] < height - 1:
    pos = (pos[0] + dx, pos[1] + dy)
    # print(pos)
    # print(lines[pos[1]][pos[0] % width])
    if lines[pos[1]][pos[0] % (width - 1)] == "#":
        trees4 += 1

trees5 = 0
pos = (0, 0)
dx = 1
dy = 2

while pos[1] < height - 1:
    pos = (pos[0] + dx, pos[1] + dy)
    # print(pos)
    # print(lines[pos[1]][pos[0] % width])
    if lines[pos[1]][pos[0] % (width - 1)] == "#":
        trees5 += 1

print(trees1 * trees2 * trees3 * trees4 * trees5)
