from typing import Any

from src.main.base_solution import BaseSolution
from src.util import *


class Solution(BaseSolution):

    def solve(self, days: int):
        ages = self.parser.to_number_list_single_line(separator=",")
        fish = {}
        for age in range(0, 9):
            fish[age] = ages.count(age)

        for d in range(days):
            breeds = fish[0]
            for i in range(0, 8):
                fish[i] = fish[i + 1]
            fish[6] += breeds
            fish[8] = breeds

        return sum(fish.values())

    def puzzle1(self) -> Any:
        return self.solve(80)

    def puzzle2(self) -> Any:
        return self.solve(256)


Solution().run(2, INPUT)
