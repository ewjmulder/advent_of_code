from src.util import *


def generator_rating(common_function, bit: int) -> BitString:
    grid = Parser.from_file(INPUT).to_number_grid(separator="")
    for column_i in range(grid.width):
        most_common_or_default = [common_function(grid, i, default_for_tie=bit) for i in range(grid.width)]
        grid = grid.filter_rows(lambda row: row[column_i] == most_common_or_default[column_i])

    return BitString.from_bit_list(grid[0])


print(generator_rating(Grid.find_most_common_in_column, 1).to_int() *
      generator_rating(Grid.find_least_common_in_column, 0).to_int())
