from src.util import *

tiles_data = open(INPUT).read().split("\n\n")

tiles = {}
for tile_data in tiles_data:
    tile_lines = [line.strip() for line in parse_string_list_from_string(tile_data)]
    tile_number = int(tile_lines[0][5:9])
    tiles[tile_number] = parse_character_grid_from_lines(tile_lines[1:])

# print(tiles)
corners = []
for tile_number, tile in tiles.items():
    first_row = tile.get_row(0)
    last_row = list(reversed(tile.get_row(tile.height - 1)))
    first_column = list(reversed(tile.get_column(0)))
    last_column = tile.get_column(tile.width - 1)
    def match(row):
        for tile_number_b, tile_b in tiles.items():
            if tile_number_b != tile_number:
                tile_b_edges = {"top_row": list(reversed(tile_b.get_row(0))),
                                "top_row_flipped": tile_b.get_row(0),
                                "bottom_row": tile_b.get_row(tile_b.height - 1),
                                "bottom_row_flipped": list(reversed(tile_b.get_row(tile_b.height - 1))),
                                "left_column": tile_b.get_column(0),
                                "left_column_flipped": list(reversed(tile_b.get_column(0))),
                                "right_column": tile_b.get_column(tile_b.width - 1),
                                "right_column_flipped": list(reversed(tile_b.get_column(tile_b.width - 1)))}
                for name, edge in tile_b_edges.items():
                    if row == edge:
                        print(tile_number, "matches", name, "of", tile_number_b)
                        return 1
        return 0
    summed = sum([match(first_row), match(last_row), match(first_column), match(last_column)])
    print(f"{tile_number} has score {summed}")
    if summed == 2:
        corners.append(tile_number)

print(corners)
prod = 1
for corner in corners:
    prod *= corner
print(prod)
