from src.util import *

sections = Parser.from_file(INPUT).to_sections()
enhancer = sections[0]
image = Parser.from_string(sections[1]).to_character_grid()

# print(enhancer)
# print(image.to_string_justified())

rows = []
space = 55
for row_i in range(0, image.width + space * 2):
    if row_i < space or row_i >= image.height + space:
        rows.append(["." for i in range(image.width + space * 2)])
    else:
        rows.append(["." for i in range(space)] + image.get_row_values(row_i - space) + ["." for i in range(space)])

image = Grid.from_values(rows)
# print(image.to_string_justified())


def enhance(img: Grid[str], step: int) -> Grid[str]:
    new_rows = []
    for row in img.rows:
        new_row = []
        for cell in row:
            ns = img.get_neighbor_cells(cell.coord, include_diagonal=True, include_own_cell=True)
            if len(ns) == 9:
                ns_string = [n.value for n in ns]
                if cell.coord.row < space - step or cell.coord.row >= image.width - (space - step) or cell.coord.column < space - step or cell.coord.column >= image.width - (space - step):
                    if step % 2 == 0:
                        new_char = "."
                    else:
                        new_char = "#"
                else:
                    ns_bits = [0 if n == "." else 1 for n in ns_string]
                    index = BitString.from_bit_list(ns_bits).to_int()
                    new_char = enhancer[index]
            else:
                new_char = "."
            new_row.append(new_char)
        new_rows.append(new_row)
    return Grid.from_values(new_rows)


steps = 2
for step in range(1, steps + 1):
    print(step)
    image = enhance(image, step)
    # print(image.to_string_justified())

print(image)
print(image.count_value("#"))
