from src.main.base_solution import BaseSolution, Any
from src.util import *


class Solution(BaseSolution):

    def solve(self, step_cost_function, cost_function):
        crab_positions = self.parser.to_number_list_single_line(separator=",")
        max_pos = max(crab_positions)
        crab_numbers = [crab_positions.count(pos) for pos in range(0, max_pos + 1)]
        costs = [sum(crab_numbers[pos] * cost_function(0, pos) for pos in range(1, max_pos + 1))]
        for pos in range(1, max_pos + 1):
            costs.append(costs[pos - 1]
                         # Extra costs: all steps of crabs on the left of the new position
                         + sum(crab_numbers[p] * step_cost_function(p, pos) for p in range(0, pos))
                         # Reduced costs: all steps of crabs on the right of the old position
                         - sum(crab_numbers[p] * step_cost_function(p, pos - 1) for p in range(pos, max_pos + 1)))
        return min(costs)

    def puzzle1(self) -> Any:
        return self.solve(lambda pos1, pos2: 0 if pos1 == pos2 else 1, lambda pos1, pos2: abs(pos1 - pos2))

    def puzzle2(self) -> Any:
        return self.solve(lambda pos1, pos2: abs(pos1 - pos2), lambda pos1, pos2: sum(range(1, abs(pos1 - pos2) + 1)))


Solution().run(2, INPUT)
