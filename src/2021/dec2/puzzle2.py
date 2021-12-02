from src.util import *

commands = parse_regex_from_file(INPUT, f"{WORD} {NUMBER}", [str, int])

aim = 0
forward = 0
depth = 0
for (direction, amount) in commands:
    if direction == "forward":
        forward += amount
        depth += amount * aim
    elif direction == "up":
        aim -= amount
    elif direction == "down":
        aim += amount

print(forward * depth)
