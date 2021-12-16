from collections import Counter

from src.main.base_solution import BaseSolution
from src.util import *


class Solution(BaseSolution):

    def _parse_graph(self) -> Graph[str]:
        return self.parser.to_string_graph("-")

    def puzzle1(self):
        return self._parse_graph().get_number_of_paths(
            "start", "end", lambda path, node: node == node.lower() and Counter(path)[node] == 1)

    def puzzle2(self):
        def stop_condition(path, node):
            return node == node.lower() and (path.count(node) == 2 or len(
                [item for item in Counter(path + [node]).items() if item[0] == item[0].lower() and item[1] == 2]) == 2)

        return self._parse_graph().get_number_of_paths("start", "end", stop_condition)


Solution().run(2, SAMPLE)
