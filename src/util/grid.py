from __future__ import annotations
from typing import List, Tuple, TypeVar, Generic, Callable, Union, Dict
from dataclasses import dataclass
from collections import Counter

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
        self.hash_value = 1
        for row in self.rows:
            self.hash_value *= sum([hash(cell) for cell in row])

    def __hash__(self):
        return self.hash_value

    def __getitem__(self, row_j: int):
        return self.rows[row_j]

    def get_cell(self, coord: Coordinate) -> T:
        return self[coord.row][coord.column]

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

    # ##### SEARCH FUNCTIONS #####

    def find_cells(self, value_or_values: Union[T, List[T]]) -> List[Tuple[T, Coordinate]]:
        return [(cell, coord_from_grid(row_i, column_i))
                for (row_i, row) in enumerate(self.rows)
                for (column_i, cell) in enumerate(row)
                if (isinstance(value_or_values, List) and cell in value_or_values) or cell == value_or_values]

    def find_most_common_in_row(self, row_i: int, default_for_tie: T = None) -> T:
        return self._find_common_in_list(self.get_row(row_i), True, default_for_tie)

    def find_most_common_in_column(self, column_i: int, default_for_tie: T = None) -> T:
        return self._find_common_in_list(self.get_column(column_i), True, default_for_tie)

    def find_least_common_in_row(self, row_i: int, default_for_tie: T = None) -> T:
        return self._find_common_in_list(self.get_row(row_i), False, default_for_tie)

    def find_least_common_in_column(self, column_i: int, default_for_tie: T = None) -> T:
        return self._find_common_in_list(self.get_column(column_i), False, default_for_tie)

    def _find_common_in_list(self, input_list: List[T], most: bool, default_for_tie: T = None) -> T:
        most_common = Counter(input_list).most_common()
        if not most:
            most_common = list(reversed(most_common))
        if len(most_common) == 1:
            # There is just 1 unique value in the list, so return that.
            return most_common[0][0]
        elif most_common[0][1] == most_common[1][1]:
            # There are 2 (or more) values in the list with the most common count, return default.
            return default_for_tie
        else:
            # There is 1 most common value in the list, return that one.
            return most_common[0][0]

    # ##### SELECTION FUNCTIONS #####

    def get_row(self, row_i: int):
        return self[row_i]

    def get_column(self, column_i: int):
        return [self[row_i][column_i] for row_i in range(0, len(self.rows))]

    def get_neighbors(self, coordinate: Coordinate, include_diagonal: bool = True, include_own_cell: bool = False):
        neighbors = []
        for row_i in range(coordinate.row - 1, coordinate.row + 2):
            for column_i in range(coordinate.column - 1, coordinate.column + 2):
                append = True
                if row_i == coordinate.row and column_i == coordinate.column:
                    if not include_own_cell:
                        append = False
                elif row_i != coordinate.row and column_i != coordinate.column:
                    if not include_diagonal:
                        append = False
                if append and 0 <= row_i < self.height and 0 <= column_i < self.width:
                    neighbors.append(self[row_i][column_i])
        return neighbors

    def get_all_orientations(self, include_flip: bool = True) -> List[Grid[T]]:
        def _append_three_rotations(orientation_list):
            for rotate in range(0, 3):
                orientation_list.append(orientation_list[-1].rotate_right_once())

        orientations = [self.copy()]
        _append_three_rotations(orientations)
        if include_flip:
            orientations.append(self.flip_horizontal())
            _append_three_rotations(orientations)
        return orientations

    # ##### TRANSFORMATION FUNCTIONS #####

    def replace_values(self, replacements: Dict[T, T]) -> Grid[T]:
        return Grid[T]([[replacements[cell] if cell in replacements else cell for cell in row] for row in self.rows])

    def copy(self) -> Grid[T]:
        return Grid[T]([row.copy() for row in self.rows])

    def flatten(self) -> List[T]:
        return [cell for row in self.rows for cell in row]

    def filter_rows(self, filter_function: Callable[[List[T]], bool]) -> Grid[T]:
        return Grid[T]([row for row in self.rows if filter_function(row)])

    def rotate_right(self, steps: int) -> Grid[T]:
        return self.rotate_left(-1 * steps)

    def rotate_right_once(self) -> Grid[T]:
        return self.rotate_right(1)

    def rotate_left(self, steps) -> Grid[T]:
        steps = steps % 4
        new_grid = self.copy()
        for step in range(0, steps):
            new_grid = new_grid.rotate_left_once()
        return new_grid

    def rotate_left_once(self) -> Grid[T]:
        rotated_rows = []
        for i in reversed(range(0, self.width)):
            rotated_rows.append(self.get_column(i))
        return Grid[T](rotated_rows)

    def flip_horizontal(self) -> Grid[T]:
        return Grid[T]([list(reversed(row)) for row in self.rows])

    def flip_vertical(self) -> Grid[T]:
        return self.flip_horizontal().rotate_right(2)

    # ##### HIGHER ORDER FUNCTIONS #####

    def map_values(self, func: Callable[[T], R]) -> Grid[R]:
        return Grid[R]([[func(cell) for cell in row] for row in self.rows])

    def map_values_and_coordinates(self, func: Callable[[T, Coordinate], R]) -> Grid[R]:
        mapped_rows = []
        for row_i in range(0, len(self.rows)):
            mapped_row = []
            for column_i in range(0, len(self[row_i])):
                mapped_row.append(func(self[row_i][column_i], coord_from_grid(row_i, column_i)))
            mapped_rows.append(mapped_row)
        return Grid[R](mapped_rows)

    def __str__(self) -> str:
        return self.to_string()

    def to_string_justified(self) -> str:
        max_width = self.map_values(str).map_values(len).max()
        return self.to_string(max_width, True)

    def to_string(self, cell_width: int = 1, separate_cells: bool = False):
        return "\n".join(self.to_string_list(cell_width, separate_cells))

    def to_string_list(self, cell_width: int = 1, separate_cells: bool = False):
        lines = []
        for row in self.rows:
            line = ""
            for cell in row:
                line += str(cell).rjust(cell_width, " ") + (" " if separate_cells else "")
            lines.append(line)
        return lines
