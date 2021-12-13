from src.main.base_solution import BaseSolution
from src.util import *


class Solution(BaseSolution):

    def _parse_input(self) -> (Grid[str], [(str, int)]):
        (coord_section, fold_section) = self.parser.to_sections()
        coords = Parser.from_string(coord_section).to_coordinate_list(separator=",")
        folds = Parser.from_string(fold_section).to_regex_match(f"fold along {WORD}={NUMBER}", [str, int])

        height = max(coord.y for coord in coords) + 1
        width = max(coord.x for coord in coords) + 1
        paper = Grid.fill_grid(height, width, ".")
        for coord in coords:
            paper[coord.y][coord.x] = "#"

        return paper, folds

    def _fold(self, paper: Grid[str], fold: (str, int)) -> Grid[str]:
        axis = fold[1]
        if fold[0] == "x":
            part1 = Grid([row[0:axis] for row in paper.get_rows()])
            part2 = Grid([row[axis + 1:] for row in paper.get_rows()]).flip_horizontal()
        else:
            part1 = Grid(paper.get_rows()[0:axis])
            part2 = Grid(paper.get_rows()[axis + 1:]).flip_vertical()

        folded = []
        for y in range(part1.height):
            folded.append([])
            for x in range(part1.width):
                folded[y].append("." if part1[y][x] == "." and part2[y][x] == "." else "#")

        return Grid(folded)

    def puzzle1(self):
        paper, folds = self._parse_input()
        return self._fold(paper, folds[0]).count_value("#")

    def puzzle2(self):
        pass


Solution().run(1, INPUT)
