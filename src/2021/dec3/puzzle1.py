from src.util import *

grid = Parser.from_file(INPUT).to_number_grid(separator="")
gamma = BitString.from_bit_list([grid.find_most_common_in_column(i) for i in range(grid.width)])
epsilon = gamma.flip_bits()
print(gamma.to_int() * epsilon.to_int())
