from src.util import *

commands = Parser.from_file(INPUT).to_regex_match(f"{WORD} {NUMBER}", [str, int])

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
