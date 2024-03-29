from src.main.base_solution import BaseSolution, Any
from src.util import *

CHECKED = -1


class Solution(BaseSolution):

    def solve(self):
        inputs = self.parser.to_sections()
        numbers = [int(n) for n in inputs[0].split(",")]
        boards = [Parser.from_string(board).to_number_grid() for board in inputs[1:]]

        scores = []
        for n in numbers:
            boards = [board.map_values_by_dict({n: CHECKED}) for board in boards]
            for board in boards:
                for line in board.get_rows_and_columns_values():
                    if line.count(CHECKED) == board.width:
                        scores.append(n * sum(board.map_values_by_dict({CHECKED: 0}).get_all_values()))
                        boards.remove(board)
                        break
        return scores

    def puzzle1(self) -> Any:
        return self.solve()[0]

    def puzzle2(self) -> Any:
        return self.solve()[-1]


Solution().run(2, INPUT)
