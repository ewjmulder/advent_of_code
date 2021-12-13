from src.util import *

sections = Parser.from_file(INPUT).to_sections()
numbers = Parser.from_string(sections[0]).to_number_lists(separator=",")
folds = Parser.from_string(sections[1]).to_regex_match(f"fold along {WORD}={NUMBER}", [str, int])

coords = [Coordinate.from_point(x=num[0], y=num[1]) for num in numbers]

print(coords)
print(folds)

height = max(coord.y for coord in coords) + 1
width = max(coord.x for coord in coords) + 1
paper = Grid.fill_grid(height, width, ".")
for coord in coords:
    paper[coord.y][coord.x] = "#"

# print(paper.to_string_justified())

for fold in folds:
    if fold[0] == "x":
        axis = fold[1]
        part1r = []
        for row in paper.rows:
            part1r.append(row[0:axis])
        part2r = []
        for row in paper.rows:
            part2r.append(row[axis + 1:])

        p1 = Grid(part1r)
        p2 = Grid(part2r)
        p2 = p2.flip_horizontal()

        # print(p1.to_string_justified())
        # print(p2.to_string_justified())

        folded = []
        for y in range(p1.height):
            folded.append([])
            for x in range(p1.width):
                folded[y].append("." if p1[y][x] == "." and p2[y][x] == "." else "#")

        paper = Grid(folded)
    else:
        axis = fold[1]
        part1r = paper.get_rows()[0:axis]
        part2r = paper.get_rows()[axis + 1:]

        p1 = Grid(part1r)
        p2 = Grid(part2r)
        p2 = p2.flip_vertical()

        # print(p1.to_string_justified())
        # print(p2.to_string_justified())

        folded = []
        for y in range(p1.height):
            folded.append([])
            for x in range(p1.width):
                folded[y].append("." if p1[y][x] == "." and p2[y][x] == "." else "#")

        paper = Grid(folded)

# print(fg.to_string_justified())
# count = fg.count_value("#")
print(paper)
