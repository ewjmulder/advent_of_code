from src.util import *

commands = parse_regex_from_file(INPUT, f"{WORD} {NUMBER}", [str, int])

forward = sum([amount for (direction, amount) in commands if direction == "forward"])
depth = sum([amount if direction == "down" else -1 * amount for (direction, amount) in commands if direction != "forward"])

print(forward * depth)
