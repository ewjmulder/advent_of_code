from src.main.base_solution import BaseSolution
from src.util import *


class Solution(BaseSolution):

    def _parse_grid(self):
        return self.parser.to_number_grid(separator="")

    def _do_flash(self, levels, cells):
        all_neighbors = flatten([levels.get_neighbor_cells(cell.coord, include_diagonal=True) for cell in cells])
        for neighbor in all_neighbors:
            if neighbor.value > 0:
                # neighbor.value += 1
                levels[neighbor.coord.row][neighbor.coord.column] += 1
        cells_to_flash = []
        # cells_to_flash = {neighbor for neighbor in all_neighbors if levels.get_value(neighbor.coord) >= 10}
        # for cell in cells:
        #     neighbors = levels.get_neighbor_cells(cell.coord, include_diagonal=True)
        # print("before", len(all_neighbors))
        all_neighbors = set(all_neighbors)
        # print("after", len(all_neighbors))
        # ????
        for cell in cells:
            for neighbor in levels.get_neighbor_cells(cell.coord, include_diagonal=True):
                if neighbor.value >= 10:
                    neighbor.value = 0
                    levels[neighbor.coord.row][neighbor.coord.column] = 0
                    cells_to_flash.append(neighbor)
        if len(cells_to_flash) == 0:
            return levels, len(cells)
        else:
            levels, sub_flashes = self._do_flash(levels, cells_to_flash)
            return levels, len(cells) + sub_flashes

    def _step(self, levels, step, flashes, stop_condition):
        levels = levels.map_values_by_function(lambda x: x + 1 if x < 9 else 0)
        cells_to_flash = levels.find_cells_by_value(0)
        levels, step_flashes = self._do_flash(levels, cells_to_flash)

        if stop_condition(levels, step):
            return step, flashes + step_flashes
        else:
            return self._step(levels, step + 1, flashes + step_flashes, stop_condition)

    def puzzle1(self):
        last_step, flashes = self._step(self._parse_grid(), 1, 0, lambda levels, step: step == 100)
        return flashes

    def puzzle2(self):
        last_step, flashes = self._step(
            self._parse_grid(), 1, 0, lambda levels, step: len(levels.find_cells_by_value(0)) == len(levels.flatten()))
        return last_step


Solution().run(1, SAMPLE)
