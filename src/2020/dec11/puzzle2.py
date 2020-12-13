input = open("input1", "r")
lines = input.readlines()
lines = [line.rstrip() for line in lines]

lines.insert(0, "." * len(lines[0]))
lines.append("." * len(lines[0]))
for i in range(0, len(lines)):
    lines[i] = "." + lines[i] + "."

for y in range(0, len(lines)):
    lines[y] = list(lines[y])

changed = True
while changed:
    new_lines = []
    for line in lines:
        new_lines.append(line.copy())
    # print("")
    # print("")
    # for i in range(0, len(lines)):
    #     s = ""
    #     for c in lines[i]:
    #         s += c
    #     print(s)
    changed = False
    for y in range(1, len(lines) - 1):
        for x in range(1, len(lines[y]) - 1):
            if lines[y][x] != ".":
                around = 0
                dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                for dir in dirs:
                    found = False
                    mul = 1
                    while not found:
                        j = y + mul * dir[1]
                        i = x + mul * dir[0]
                        mul += 1
                        if j < 0 or j >= len(lines) or i < 0 or i >= len(lines[0]):
                            found = True
                        else:
                            if lines[j][i] == ".":
                                found = False
                            elif lines[j][i] == "#":
                                around += 1
                                found = True
                            elif lines[j][i] == "L":
                                found = True
                # print(x, y, around)
                if lines[y][x] == "L" and around == 0:
                    new_lines[y][x] = "#"
                    changed = True
                elif lines[y][x] == "#" and around >= 5:
                    new_lines[y][x] = "L"
                    changed = True
    lines = new_lines

count = 0
for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[y]) - 1):
        if lines[y][x] == "#":
            count += 1

print(count)