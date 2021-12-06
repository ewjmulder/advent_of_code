from typing import Any

from src.main.base_solution import BaseSolution
from src.util import *


class Solution(BaseSolution):

    def solve(self, include_diagonals: bool):
        lines = self.parser.to_regex_match(f"{NUMBER},{NUMBER} \\-\\> {NUMBER},{NUMBER}", int)

        max_size = max(flatten(lines)) + 1
        counts = Grid.fill_grid(max_size, max_size, 0)

        for [from_x, from_y, to_x, to_y] in lines:
            if from_x == to_x:
                xs = (abs(from_y - to_y) + 1) * [from_x]
            else:
                xs = range_incl(from_x, to_x)
            if from_y == to_y:
                ys = (abs(from_x - to_x) + 1) * [from_y]
            else:
                ys = range_incl(from_y, to_y)
            xys = zip(xs, ys)
            for (x, y) in xys:
                if include_diagonals or from_x == to_x or from_y == to_y:
                    counts.rows[y][x] += 1

        highs = counts.find_cells_by_predicate(lambda cell: cell > 1)
        return len(highs)

    def puzzle1(self) -> Any:
        return self.solve(False)

    def puzzle2(self) -> Any:
        return self.solve(True)


Solution().run(1, INPUT)
