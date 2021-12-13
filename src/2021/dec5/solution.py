from typing import List, Tuple

from src.main.base_solution import BaseSolution, Any
from src.util import *


class Solution(BaseSolution):

    def _parse_lines(self) -> List[List[int]]:
        return self.parser.to_regex_match(f"{NUMBER},{NUMBER} \\-\\> {NUMBER},{NUMBER}", int)

    def _get_xys(self, from_x: int, from_y: int, to_x: int, to_y: int) -> List[Tuple[int, int]]:
        if from_x == to_x:
            xs = (abs(from_y - to_y) + 1) * [from_x]
        else:
            xs = range_incl(from_x, to_x)
        if from_y == to_y:
            ys = (abs(from_x - to_x) + 1) * [from_y]
        else:
            ys = range_incl(from_y, to_y)
        return list(zip(xs, ys))

    def _solve(self, include_diagonals: bool):
        return self._solve_with_dict(include_diagonals)

    def _solve_with_dict(self, include_diagonals: bool):
        def increment(dictionary, coord):
            if coord not in counts:
                dictionary[coord] = 1
            else:
                dictionary[coord] += 1

        lines = self._parse_lines()
        counts = {}
        for [from_x, from_y, to_x, to_y] in lines:
            for (x, y) in self._get_xys(from_x, from_y, to_x, to_y):
                if include_diagonals or from_x == to_x or from_y == to_y:
                    increment(counts, Coordinate.from_point(x, y))
        return len(list(filter(lambda count: count >= 2, counts.values())))

    def _solve_with_grid(self, include_diagonals: bool):
        lines = self._parse_lines()

        max_size = max(flatten(lines)) + 1
        counts = Grid.fill_grid(max_size, max_size, 0)

        for [from_x, from_y, to_x, to_y] in lines:
            for (x, y) in self._get_xys(from_x, from_y, to_x, to_y):
                if include_diagonals or from_x == to_x or from_y == to_y:
                    counts.rows[y][x].value += 1

        highs = counts.find_cells_by_predicate_on_value(lambda value: value >= 2)
        return len(highs)

    def puzzle1(self) -> Any:
        return self._solve(False)

    def puzzle2(self) -> Any:
        return self._solve(True)


Solution().run(1, INPUT)
