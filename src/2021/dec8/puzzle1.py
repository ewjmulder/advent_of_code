from src.util import *

lines = Parser.from_file(INPUT).to_lines()

outlines = [line.split("|")[1].strip() for line in lines]

print(outlines)

outwords = flatten([line.split(" ") for line in outlines])
print(outwords)

uniq_outwords = [word for word in outwords if len(word) != 5 and len(word) != 6]

print(uniq_outwords)

print(len(uniq_outwords))
