input = open("input1", "r")
lines = input.readlines()

wire1 = lines[0].split(",")
wire2 = lines[1].split(",")


def coords(wire):
    curr = (0,0)
    steps = 0
    cs = {curr: steps}
    for step in wire:
        dir = step[0]
        amount = int(step[1:])
        if dir == "R":
            for d in range(1, amount + 1):
                steps += 1
                curr = (curr[0] + 1, curr[1])
                if curr not in cs:
                    cs[curr] = steps
        if dir == "L":
            for d in range(1, amount + 1):
                steps += 1
                curr = (curr[0] - 1, curr[1])
                if curr not in cs:
                    cs[curr] = steps
        if dir == "U":
            for d in range(1, amount + 1):
                steps += 1
                curr = (curr[0], curr[1] + 1)
                if curr not in cs:
                    cs[curr] = steps
        if dir == "D":
            for d in range(1, amount + 1):
                steps += 1
                curr = (curr[0], curr[1] - 1)
                if curr not in cs:
                    cs[curr] = steps
        # print(curr)
    return cs


cs1 = coords(wire1)
cs2 = coords(wire2)
print(cs1)
print(cs2)

min = 99999999
for c in cs1:
    if c in cs2 and c != (0,0):
        dist = cs1[c] + cs2[c]
        if dist < min:
            min = dist

print(min)
