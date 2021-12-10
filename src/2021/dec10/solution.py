from src.main.base_solution import BaseSolution
from src.util import *

BRACES_PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}
ERROR_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
COMPLETE_SCORE = {")": 1, "]": 2, "}": 3, ">": 4}


def _traverse(line, acc):
    if len(line) == 0:
        return acc
    char = line[0]
    if char in BRACES_PAIRS:
        return _traverse(line[1:], acc + [BRACES_PAIRS[char]])
    else:
        if char == acc[-1]:
            return _traverse(line[1:], acc[:-1])
        else:
            return [char, "*"]


class Solution(BaseSolution):

    def puzzle1(self):
        return sum(ERROR_SCORE[result[0]]
                   for line in self.parser.to_lines()
                   for result in [_traverse(line, [])]
                   if result[-1] == "*")

    def puzzle2(self):
        def complete_score(remaining, acc):
            if len(remaining) == 0:
                return acc
            else:
                return complete_score(remaining[1:], acc * 5 + COMPLETE_SCORE[remaining[0]])

        scores = [complete_score(list(reversed(result)), 0)
                  for line in self.parser.to_lines()
                  for result in [_traverse(line, [])]
                  if result[-1] != "*"]
        return sorted(scores)[int((len(scores) - 1) / 2)]


Solution().run(2, INPUT)
