from __future__ import annotations
from typing import List, TypeVar, Generic, Callable

T = TypeVar('T')
R = TypeVar('R')


class Grid(Generic[T]):
    def __init__(self, rows: List[List[T]]):
        self.rows = rows

    # ##### AGGREGATION FUNCTIONS #####

    def count(self, value):
        return sum([row.count(value) for row in self.rows])

    def min(self):
        return min(self.flatten())

    def max(self):
        return max(self.flatten())

    # ##### HIGHER ORDER FUNCTIONS #####

    def flatten(self):
        return [cell for row in self.rows for cell in row]

    def map_values(self, func: Callable[[T], R]) -> Grid[R]:
        return Grid[R]([[func(cell) for cell in row] for row in self.rows])

    # def map_values_and_coordinates(self, func: Callable[[T, int, int], R]) -> Grid[R]:
    #     return Grid[R]([[func(cell) for cell in row] for row in self.rows])

    def __str__(self):
        return self.to_string()

    def to_string_separated(self):
        max_width = self.map(str).map(len).max()
        return self.to_string(max_width, True)

    def to_string(self, cell_width: int = 1, separate_cells: bool = False):
        lines = []
        for row in self.rows:
            line = ""
            for cell in row:
                line += str(cell).rjust(cell_width, " ") + (" " if separate_cells else "")
            lines.append(line)
        return "\n".join(lines)


def grid_of_characters(strings: List[str]) -> Grid[str]:
    return Grid[str]([[char for char in string] for string in strings])


def grid_of_strings(rows: List[List[str]]) -> Grid[str]:
    return Grid[str](rows)


def grid_of_numbers(rows: List[List[int]]) -> Grid[int]:
    return Grid[int](rows)


grid = grid_of_numbers([[1, 2, 3], [4, 5, 6], [243, 323, 224]])
print(grid.to_string_separated())
print(grid.max())

grid = grid_of_characters(["abc", "def"])
print(grid)
