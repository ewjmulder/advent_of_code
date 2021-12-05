from typing import Any

from src.util import *
from src.main.base_solution import BaseSolution

CHECKED = -1


class Solution(BaseSolution):

    def solve(self):
        inputs = self.parser.to_sections()
        numbers = [int(n) for n in inputs[0].split(",")]
        boards = [Parser.from_string(board).to_number_grid() for board in inputs[1:]]

        scores = []
        for n in numbers:
            boards = [board.replace_values({n: CHECKED}) for board in boards]
            for board in boards:
                for line in board.get_rows_and_columns():
                    if line.count(CHECKED) == board.width:
                        scores.append(n * sum(board.replace_values({CHECKED: 0}).flatten()))
                        boards.remove(board)
                        break
        return scores

    def puzzle1(self) -> Any:
        return self.solve()[0]

    def puzzle2(self) -> Any:
        return self.solve()[-1]


Solution().run(2, INPUT)

