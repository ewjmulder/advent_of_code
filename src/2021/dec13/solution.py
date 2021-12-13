from src.main.base_solution import BaseSolution
from src.util import *
from src.util.collections import reduce


class Solution(BaseSolution):

    def _parse_input(self) -> (Grid[str], [(str, int)]):
        (coord_section, fold_section) = self.parser.to_sections()
        coords = Parser.from_string(coord_section).to_coordinate_list(separator=",")
        folds = Parser.from_string(fold_section).to_regex_match(f"fold along {WORD}={NUMBER}", [str, int])

        height = max(coord.y for coord in coords) + 1
        width = max(coord.x for coord in coords) + 1
        paper = Grid.fill_grid(height, width, ".")
        for coord in coords:
            paper.get_cell_by_coord(coord).value = "#"

        return paper, folds

    def _fold(self, paper: Grid[str], fold: (str, int)) -> Grid[str]:
        axis = fold[1]
        if fold[0] == "x":
            part1 = Grid.from_values([row[0:axis] for row in paper.get_rows_values()])
            part2 = Grid.from_values([row[axis + 1:] for row in paper.get_rows_values()]).flip_horizontal()
        else:
            part1 = Grid.from_values(paper.get_rows_values()[0:axis])
            part2 = Grid.from_values(paper.get_rows_values()[axis + 1:]).flip_vertical()

        return Grid.from_values([["." if part1[y][x].value == "." and part2[y][x].value == "." else "#"
                                  for x in range(part1.width)]
                                 for y in range(part1.height)
                                 ])

    def puzzle1(self):
        paper, folds = self._parse_input()
        return self._fold(paper, folds[0]).count_value("#")

    def puzzle2(self):
        start_paper, folds = self._parse_input()
        return reduce(lambda paper, fold: self._fold(paper, fold), folds, start_paper).to_string_mapped({
            ".": "⬜", "#": "⬛"
        })


Solution().run(2, INPUT)
