import sys
from src.util import *

CHECKED = -1

inputs = Parser.from_file(INPUT).to_sections()
numbers = [int(n) for n in inputs[0].split(",")]
boards = [Parser.from_string(board).to_number_grid() for board in inputs[1:]]

for n in numbers:
    boards = [board.replace_values({n: CHECKED}) for board in boards]
    for board in boards:
        for line in board.get_rows_and_columns():
            if line.count(CHECKED) == board.width:
                print(n * sum(board.replace_values({CHECKED: 0}).flatten()))
                sys.exit(0)
