from src.util import *
from src.util.collections import range_incl

instructions = Parser.from_file(INPUT).to_regex_match(f"{WORD} x={NUMBER}..{NUMBER},y={NUMBER}..{NUMBER},z={NUMBER}..{NUMBER}", [str, int, int, int, int, int, int])

print(instructions)

ons = set()

for instruction in instructions:
    if -50 <= instruction[1] <= 50:
        for x in range_incl(instruction[1], instruction[2]):
            if -50 <= x <= 50:
                for y in range_incl(instruction[3], instruction[4]):
                    if -50 <= y <= 50:
                        for z in range_incl(instruction[5], instruction[6]):
                            if -50 <= z <= 50:
                                coord = (x, y, z)
                                if instruction[0] == "on":
                                    ons.add(coord)
                                else:
                                    if coord in ons:
                                        ons.remove(coord)

print(len(ons))
