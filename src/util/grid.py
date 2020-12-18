from __future__ import annotations
from typing import List, TypeVar, Generic, Callable
from dataclasses import dataclass

from src.util.coordinate import Coordinate, coord_from_grid

T = TypeVar('T')
R = TypeVar('R')


@dataclass
class Grid(Generic[T]):
    rows: List[List[T]]

    def __post_init__(self):
        if len(self.rows) == 0:
            raise ValueError("Grid must have at least 1 row")
        if len(set([len(row) for row in self.rows])) > 1:
            raise ValueError("All rows in a grid must have the same length")

    def __getitem__(self, row_j: int):
        return self.rows[row_j]

    # ##### AGGREGATION FUNCTIONS #####

    @property
    def height(self):
        return len(self.rows)

    @property
    def width(self):
        return len(self.rows[0])

    def count(self, value: T):
        return sum([row.count(value) for row in self.rows])

    def min(self):
        return min(self.flatten())

    def max(self):
        return max(self.flatten())

    # ##### SELECTION FUNCTIONS #####

    def copy(self):
        Grid[T](row.copy() for row in self.rows)

    def get_row(self, row_j: int):
        return self[row_j]

    def get_column(self, column_i: int):
        return [self[row_j][column_i] for row_j in range(0, len(self.rows))]

    def get_neighbors(self, coordinate: Coordinate, include_diagonal: bool = True, include_own_cell: bool = False):
        neighbors = []
        for row_i in range(coordinate.row - 1, coordinate.row + 2):
            for column_j in range(coordinate.column - 1, coordinate.column + 2):
                append = True
                if row_i == coordinate.row and column_j == coordinate.column:
                    if not include_own_cell:
                        append = False
                elif row_i != coordinate.row and column_j != coordinate.column:
                    if not include_diagonal:
                        append = False
                if append and 0 <= row_i < self.height and 0 <= column_j < self.width:
                    neighbors.append(self[row_i][column_j])
        return neighbors

    def flatten(self):
        return [cell for row in self.rows for cell in row]

    # ##### HIGHER ORDER FUNCTIONS #####

    def map_values(self, func: Callable[[T], R]) -> Grid[R]:
        return Grid[R]([[func(cell) for cell in row] for row in self.rows])

    def map_values_and_coordinates(self, func: Callable[[T, Coordinate], R]) -> Grid[R]:
        mapped_rows = []
        for row_j in range(0, len(self.rows)):
            mapped_row = []
            for column_i in range(0, len(self[row_j])):
                mapped_row.append(func(self[row_j][column_i], coord_from_grid(row_j, column_i)))
            mapped_rows.append(mapped_row)
        return Grid[R](mapped_rows)

    def __str__(self):
        return self.to_string()

    def to_string_separated(self):
        max_width = self.map_values(str).map_values(len).max()
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
