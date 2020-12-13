input = open("input1", "r")
lines = input.readlines()

import re

all_claims = set()
doubles_counted = set()
for line in lines:
    line = line.rstrip()
    match = re.match("\#([0-9]+) \@ ([0-9]+),([0-9]+)\: ([0-9]+)x([0-9]+)", line)
    # print(match.groups())
    id = int(match.groups()[0])
    left = int(match.groups()[1])
    top = int(match.groups()[2])
    width = int(match.groups()[3])
    height = int(match.groups()[4])
    claim = set()
    for x in range(left, left + width):
        for y in range(top, top + height):
            if (x, y) in all_claims:
                doubles_counted.add((x, y))
            all_claims.add((x, y))

# print(all_claims)
# print(doubles_counted)

for line in lines:
    line = line.rstrip()
    match = re.match("\#([0-9]+) \@ ([0-9]+),([0-9]+)\: ([0-9]+)x([0-9]+)", line)
    # print(match.groups())
    id = int(match.groups()[0])
    left = int(match.groups()[1])
    top = int(match.groups()[2])
    width = int(match.groups()[3])
    height = int(match.groups()[4])
    free = True
    for x in range(left, left + width):
        for y in range(top, top + height):
            if (x, y) in doubles_counted:
                # print(id, "not free for coord", x, y)
                free = False
    if free:
        print(id)
