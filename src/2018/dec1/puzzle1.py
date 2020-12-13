import math

input = open("input1", "r")
lines = input.readlines()

level = 0
for line in lines:
    step = int(line)
    level += step

print(level)
