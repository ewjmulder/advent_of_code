from CSP_Solver import CSP

from src.main.base_solution import BaseSolution
from src.util import *


class Solution(BaseSolution):

    def parse(self):
        return [[[word for word in part.strip().split(" ")]
                 for part in line.split("|")]
                for line in self.parser.to_lines()]

    def puzzle1(self):
        return len([word for word in flatten(words[1] for words in self.parse()) if len(word) in [2, 3, 4, 7]])

    def puzzle2(self):
        def calculate_output(digits_in, digits_out):
            digits_in_sorted = sorted(map(frozenset, digits_in), key=len)

            task = CSP(variables=10)
            # Define the domains as tightly as possible (already known or 3 options) (10=0)
            task.separateDomain(1, [digits_in_sorted[0]])
            task.separateDomain(7, [digits_in_sorted[1]])
            task.separateDomain(4, [digits_in_sorted[2]])
            task.separateDomain(8, [digits_in_sorted[9]])
            for var in [2, 3, 5]:
                task.separateDomain(var, digits_in_sorted[3:6])
            for var in [6, 9, 10]:
                task.separateDomain(var, digits_in_sorted[6:9])

            # All digits must be different (value[0] = None, so total length of unique values = 11)
            task.addConstraint('len(set(value)) == 11')

            # Provide checks that uniquely identify 3, 6, 5 and 9. The rest follow automatically.
            task.addConstraint('len(value[3].intersection(value[1])) == 2')
            task.addConstraint('len(value[6].intersection(value[1])) == 1')
            task.addConstraint('len(value[5].intersection(value[6])) == 5')
            task.addConstraint('len(value[9].intersection(value[5])) == 5')

            task.solve_dfs()
            solution = {task.value[i]: i for i in range(11)}
            return int("".join(str(solution[frozenset(digit_out)] % 10) for digit_out in digits_out))

        return sum(calculate_output(digits_in, digits_out) for [digits_in, digits_out] in self.parse())


Solution().run(2, INPUT)
