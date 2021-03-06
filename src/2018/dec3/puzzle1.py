input = open("input1", "r")
lines = input.readlines()

import re

claims = []
all_claims = set()
doubles_counted = set()
amount = 0
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
            claim.add((x, y))
            if (x, y) in all_claims:
                if (x, y) not in doubles_counted:
                    amount += 1
                    doubles_counted.add((x, y))
            else:
                all_claims.add((x, y))
    claims.append(claim)


print(amount)
