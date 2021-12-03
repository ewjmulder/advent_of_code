from src.util import *

commands = Parser.from_file(INPUT).to_regex_match(f"{WORD} {NUMBER}", [str, int])

forward = sum([amount for (direction, amount) in commands if direction == "forward"])
depth = sum([amount if direction == "down" else -1 * amount for (direction, amount) in commands if direction != "forward"])

print(forward * depth)
