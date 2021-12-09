from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import List, Set, TypeVar, Generic, Callable, Union, Dict

from src.util.collections import union_sets
from src.util.coordinate import Coordinate, coord_from_grid

T = TypeVar('T')
R = TypeVar('R')


@dataclass
class Cell(Generic[T]):
    coord: Coordinate
    value: T

    def __post_init__(self):
        self.hash_value = self.coord.row * self.coord.column * hash(self.value)

    def __hash__(self):
        return self.hash_value


@dataclass
class Grid(Generic[T]):
    rows: List[List[T]]

    @classmethod
    def fill_grid(cls, grid_height: int, grid_width: int, value: T) -> Grid[T]:
        rows = []
        for row_i in range(grid_height):
            rows.append(grid_width * [value])
        return Grid(rows)

    def __post_init__(self):
        if len(self.rows) == 0:
            raise ValueError("Grid must have at least 1 row")
        if len(set([len(row) for row in self.rows])) > 1:
            raise ValueError("All rows in a grid must have the same length")
        self.hash_value = 1
        for row in self.rows:
            self.hash_value *= sum([hash(value) for value in row])

    def __hash__(self):
        return self.hash_value

    def __getitem__(self, row_i: int):
        return self.rows[row_i]

    def get_value(self, coord: Coordinate) -> T:
        return self[coord.row][coord.column]

    def get_cell(self, coord: Coordinate) -> Cell[T]:
        return Cell(coord, self[coord.row][coord.column])

    def get_all_coordinates(self) -> List[Coordinate]:
        return [Coordinate(row_i, column_i) for row_i in range(self.height) for column_i in range(self.width)]

    def get_all_cells(self) -> List[Cell[T]]:
        return [self.get_cell(coord) for coord in self.get_all_coordinates()]

    # ##### AGGREGATION FUNCTIONS #####

    @property
    def height(self):
        return len(self.rows)

    @property
    def width(self):
        return len(self.rows[0])

    def count_value(self, value: T):
        return sum([row.count(value) for row in self.rows])

    def min(self):
        return min(self.flatten())

    def max(self):
        return max(self.flatten())

    # ##### SELECTION FUNCTIONS #####

    def get_row(self, row_i: int) -> List[T]:
        return self[row_i]

    def get_rows(self) -> List[List[T]]:
        return self.rows

    def get_column(self, column_i: int) -> List[T]:
        return [self[row_i][column_i] for row_i in range(0, len(self.rows))]

    def get_columns(self) -> List[List[T]]:
        return [self.get_column(column_i) for column_i in range(self.width)]

    def get_rows_and_columns(self) -> List[List[T]]:
        return self.get_rows() + self.get_columns()

    def get_neighbor_cells(self, coord: Coordinate, include_diagonal: bool = True,
                           include_own_cell: bool = False) -> List[Cell[T]]:
        neighbors = []
        for row_i in range(coord.row - 1, coord.row + 2):
            for column_i in range(coord.column - 1, coord.column + 2):
                # Decision to add: check on own cell, diagonal neighbors and grid range.
                if (row_i != coord.row or column_i != coord.column or include_own_cell) and \
                        (row_i == coord.row or column_i == coord.column or include_diagonal) and \
                        (0 <= row_i < self.height and 0 <= column_i < self.width):
                    neighbors.append(self.get_cell(Coordinate(row_i, column_i)))
        return neighbors

    def get_neighbor_coords(self, coord: Coordinate, include_diagonal: bool = True,
                            include_own_cell: bool = False) -> List[Coordinate]:
        return list(map(lambda cell: cell.coord, self.get_neighbor_cells(coord, include_diagonal, include_own_cell)))

    def get_neighbor_values(self, coord: Coordinate, include_diagonal: bool = True,
                            include_own_cell: bool = False) -> List[T]:
        return list(map(lambda cell: cell.value, self.get_neighbor_cells(coord, include_diagonal, include_own_cell)))

    def get_local_area_cells(self, cell: Cell, spread_function: Callable[[Cell[T], Cell[T]], bool],
                             include_diagonal: bool = True) -> Set[Cell[T]]:
        def recurse_local_area(from_cell: Cell, accumulator: Set[Cell[T]]) -> Set[Cell[T]]:
            new_from_cells = [neighbor_cell for neighbor_cell in
                              self.get_neighbor_cells(from_cell.coord, include_diagonal)
                              if neighbor_cell not in accumulator and spread_function(from_cell, neighbor_cell)]
            accumulator = accumulator.union(new_from_cells)
            return accumulator | union_sets(
                recurse_local_area(new_from_cell, accumulator) for new_from_cell in new_from_cells)

        return recurse_local_area(cell, {cell})

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

    # ##### SEARCH FUNCTIONS #####

    def find_cells_by_predicate_on_cell(self, predicate_function: Callable[[Cell[T]], bool]) -> List[Cell[T]]:
        return list(filter(predicate_function, self.get_all_cells()))

    def find_cells_by_predicate_on_coordinate(self, predicate_function: Callable[[Coordinate], bool]) -> List[Cell[T]]:
        return list(filter(lambda cell: predicate_function(cell.coord), self.get_all_cells()))

    def find_cells_by_predicate_on_value(self, predicate_function: Callable[[T], bool]) -> List[Cell[T]]:
        return list(filter(lambda cell: predicate_function(cell.value), self.get_all_cells()))

    def find_cells_by_value(self, value_or_values: Union[T, List[T]]) -> List[Cell[T]]:
        return self.find_cells_by_predicate_on_value(
            lambda value: value in value_or_values if isinstance(value_or_values, List) else value == value_or_values)

    def find_most_common_value_in_grid(self, default_for_tie: T = None) -> T:
        return self._find_common_value_in_list(self.flatten(), True, default_for_tie)

    def find_most_common_value_in_row(self, row_i: int, default_for_tie: T = None) -> T:
        return self._find_common_value_in_list(self.get_row(row_i), True, default_for_tie)

    def find_most_common_value_in_column(self, column_i: int, default_for_tie: T = None) -> T:
        return self._find_common_value_in_list(self.get_column(column_i), True, default_for_tie)

    def find_least_common_value_in_grid(self, default_for_tie: T = None) -> T:
        return self._find_common_value_in_list(self.flatten(), False, default_for_tie)

    def find_least_common_value_in_row(self, row_i: int, default_for_tie: T = None) -> T:
        return self._find_common_value_in_list(self.get_row(row_i), False, default_for_tie)

    def find_least_common_value_in_column(self, column_i: int, default_for_tie: T = None) -> T:
        return self._find_common_value_in_list(self.get_column(column_i), False, default_for_tie)

    def _find_common_value_in_list(self, input_list: List[T], most: bool, default_for_tie: T) -> T:
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

    # ##### TRANSFORMATION FUNCTIONS #####

    def replace_values(self, replacements: Dict[T, T]) -> Grid[T]:
        return Grid[T]([[replacements[value] if value in replacements else value for value in row]
                        for row in self.rows])

    def copy(self) -> Grid[T]:
        return Grid[T]([row.copy() for row in self.rows])

    def flatten(self) -> List[T]:
        return [value for row in self.rows for value in row]

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

    def map_values(self, mapping_function: Callable[[T], R]) -> Grid[R]:
        return Grid[R]([[mapping_function(value) for value in row] for row in self.rows])

    def map_values_and_coordinates(self, func: Callable[[T, Coordinate], R]) -> Grid[R]:
        mapped_rows = []
        for row_i in range(0, len(self.rows)):
            mapped_row = []
            for column_i in range(0, len(self[row_i])):
                mapped_row.append(func(self[row_i][column_i], coord_from_grid(row_i, column_i)))
            mapped_rows.append(mapped_row)
        return Grid[R](mapped_rows)

    # ##### DISPLAY FUNCTIONS #####

    def __str__(self) -> str:
        return self.to_string()

    def to_string(self, cell_width: int = 1, separate_cells: bool = False):
        return "\n".join(self.to_string_list(cell_width, separate_cells))

    def to_string_justified(self) -> str:
        max_width = self.map_values(str).map_values(len).max()
        return self.to_string(max_width, True)

    def to_string_list(self, cell_width: int = 1, separate_cells: bool = False):
        lines = []
        for row in self.rows:
            line = ""
            for value in row:
                line += str(value).rjust(cell_width, " ") + (" " if separate_cells else "")
            lines.append(line)
        return lines
