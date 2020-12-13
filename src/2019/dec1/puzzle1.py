import math

input = open("input1", "r")
lines = input.readlines()

total = 0
for line in lines:
    mass = int(line)
    fuel = math.floor(mass / 3) - 2
    extra_fuel = fuel
    while extra_fuel >= 1:
        extra_fuel = math.floor(extra_fuel / 3) - 2
        if extra_fuel >= 1:
            fuel += extra_fuel
    total += fuel

print(total)
