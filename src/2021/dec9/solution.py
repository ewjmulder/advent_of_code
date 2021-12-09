from src.main.base_solution import BaseSolution
from src.util import *


class Solution(BaseSolution):

    def _get_heights(self):
        return self.parser.to_number_grid(separator="")

    def _get_low_cells(self):
        heights = self._get_heights()
        return heights.find_cells_by_predicate_on_cell(
            lambda cell: cell.value < min(heights.get_neighbor_values(cell.coord, include_diagonal=False)))

    def puzzle1(self):
        return sum(low_cell.value + 1 for low_cell in self._get_low_cells())

    def puzzle2(self):
        def proceed(from_cell, to_cell): return to_cell.value != 9 and from_cell.value < to_cell.value

        heights = self._get_heights()
        area_sizes = [len(heights.get_local_area_cells(low_cell, proceed, include_diagonal=False))
                      for low_cell in self._get_low_cells()]
        return multiply(sorted(area_sizes)[-3:])


Solution().run(2, INPUT)
