input = open("input1", "r")
lines = input.readlines()

wire1 = lines[0].split(",")
wire2 = lines[1].split(",")


def coords(wire):
    cs = {(0,0)}
    curr = (0,0)
    for step in wire:
        dir = step[0]
        amount = int(step[1:])
        if dir == "R":
            for d in range(1, amount + 1):
                curr = (curr[0] + 1, curr[1])
                cs.add(curr)
        if dir == "L":
            for d in range(1, amount + 1):
                curr = (curr[0] - 1, curr[1])
                cs.add(curr)
        if dir == "U":
            for d in range(1, amount + 1):
                curr = (curr[0], curr[1] + 1)
                cs.add(curr)
        if dir == "D":
            for d in range(1, amount + 1):
                curr = (curr[0], curr[1] - 1)
                cs.add(curr)
        # print(curr)
    return cs


cs1 = coords(wire1)
cs2 = coords(wire2)
print(cs1)
print(cs2)

min = 99999999
for c in cs1:
    if c in cs2 and c != (0,0):
        dist = abs(c[0]) + abs(c[1])
        if dist < min:
            min = dist

print(min)
