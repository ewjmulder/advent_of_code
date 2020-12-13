import math

input = open("input1", "r")
lines = input.readlines()

freqs = set()
level = 0
found = False
while not found:
    for line in lines:
        step = int(line)
        level += step
        if level in freqs:
            found = True
            break
        freqs.add(level)

print(level)
