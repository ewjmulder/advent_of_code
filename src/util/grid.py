from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import List, Set, TypeVar, Generic, Callable, Union, Dict

from src.util.collections import flatten
from src.util.collections import union_sets
from src.util.coordinate import Coordinate

T = TypeVar('T')
R = TypeVar('R')


@dataclass
class Cell(Generic[T]):
    coord: Coordinate
    value: T

    def __post_init__(self):
        self.hash_value = hash(self.coord) * hash(self.value)

    def __hash__(self):
        return self.hash_value

    @property
    def row(self):
        return self.coord.row

    @property
    def column(self):
        return self.coord.column


@dataclass
class Grid(Generic[T]):
    rows: List[List[Cell[T]]]

    @classmethod
    def from_values(cls, values: List[List[T]]) -> Grid[T]:
        Grid.validate(values)
        return Grid([[Cell(Coordinate(row_i, column_i), values[row_i][column_i])
                      for column_i in range(len(values[0]))]
                     for row_i in range(len(values))])

    @classmethod
    def fill_grid(cls, grid_height: int, grid_width: int, value: T) -> Grid[T]:
        rows = []
        for row_i in range(grid_height):
            rows.append(grid_width * [value])
        return Grid.from_values(rows)

    @classmethod
    def validate(cls, rows: List[List]):
        if len(rows) == 0:
            raise ValueError("Grid must have at least 1 row")
        if len(set([len(row) for row in rows])) > 1:
            raise ValueError("All rows in a grid must have the same length")

    def __post_init__(self):
        Grid.validate(self.rows)
        self.hash_value = 1
        for row in self.rows:
            self.hash_value *= sum([hash(cell) for cell in row])

    def __hash__(self):
        return self.hash_value

    def __getitem__(self, row_i: int):
        return self.rows[row_i]

    def get_cell_by_index(self, row_i: int, column_i: int) -> Cell[T]:
        return self[row_i][column_i]

    def get_cell_by_coord(self, coord: Coordinate) -> Cell[T]:
        return self[coord.row][coord.column]

    def get_value_by_index(self, row_i: int, column_i: int) -> T:
        return self[row_i][column_i].value

    def get_value_by_coord(self, coord: Coordinate) -> T:
        return self[coord.row][coord.column].value

    def get_all_cells(self) -> List[Cell[T]]:
        return flatten(self.rows)

    def get_all_coordinates(self) -> List[Coordinate]:
        return [self.rows[row_i][column_i].coord for column_i in range(self.width) for row_i in range(self.height)]

    def get_all_values(self) -> List[T]:
        return [self.rows[row_i][column_i].value for column_i in range(self.width) for row_i in range(self.height)]

    # ##### AGGREGATION FUNCTIONS #####

    @property
    def height(self):
        return len(self.rows)

    @property
    def width(self):
        return len(self.rows[0])

    def count_value(self, value: T):
        return self.get_all_values().count(value)

    def min(self):
        return min(self.get_all_values())

    def max(self):
        return max(self.get_all_values())

    # ##### SELECTION FUNCTIONS #####

    def get_row_cells(self, row_i: int) -> List[Cell[T]]:
        return self[row_i]

    def get_row_values(self, row_i: int) -> List[T]:
        return [cell.value for cell in self.get_row_cells(row_i)]

    def get_rows_cells(self) -> List[List[Cell[T]]]:
        return self.rows

    def get_rows_values(self) -> List[List[T]]:
        return [[cell.value for cell in row] for row in self.get_rows_cells()]

    def get_column_cells(self, column_i: int) -> List[Cell[T]]:
        return [self[row_i][column_i] for row_i in range(0, len(self.rows))]

    def get_column_values(self, column_i: int) -> List[T]:
        return [self[row_i][column_i].value for row_i in range(0, len(self.rows))]

    def get_columns_cells(self) -> List[List[Cell[T]]]:
        return [self.get_column_cells(column_i) for column_i in range(self.width)]

    def get_columns_values(self) -> List[List[T]]:
        return [self.get_column_values(column_i) for column_i in range(self.width)]

    def get_rows_and_columns_cells(self) -> List[List[Cell[T]]]:
        return self.get_rows_cells() + self.get_columns_cells()

    def get_rows_and_columns_values(self) -> List[List[T]]:
        return self.get_rows_values() + self.get_columns_values()

    def get_neighbor_cells(self, coord: Coordinate, include_diagonal: bool = True,
                           include_own_cell: bool = False) -> List[Cell[T]]:
        neighbors = []
        for row_i in range(coord.row - 1, coord.row + 2):
            for column_i in range(coord.column - 1, coord.column + 2):
                # Decision to add: check on own cell, diagonal neighbors and grid range.
                if (row_i != coord.row or column_i != coord.column or include_own_cell) and \
                        (row_i == coord.row or column_i == coord.column or include_diagonal) and \
                        (0 <= row_i < self.height and 0 <= column_i < self.width):
                    neighbors.append(self.get_cell_by_index(row_i, column_i))
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
        return self._find_common_value_in_list(self.get_all_values(), True, default_for_tie)

    def find_most_common_value_in_row(self, row_i: int, default_for_tie: T = None) -> T:
        return self._find_common_value_in_list(self.get_row_values(row_i), True, default_for_tie)

    def find_most_common_value_in_column(self, column_i: int, default_for_tie: T = None) -> T:
        return self._find_common_value_in_list(self.get_column_values(column_i), True, default_for_tie)

    def find_least_common_value_in_grid(self, default_for_tie: T = None) -> T:
        return self._find_common_value_in_list(self.get_all_values(), False, default_for_tie)

    def find_least_common_value_in_row(self, row_i: int, default_for_tie: T = None) -> T:
        return self._find_common_value_in_list(self.get_row_values(row_i), False, default_for_tie)

    def find_least_common_value_in_column(self, column_i: int, default_for_tie: T = None) -> T:
        return self._find_common_value_in_list(self.get_column_values(column_i), False, default_for_tie)

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

    def copy(self) -> Grid[T]:
        return Grid[T]([row.copy() for row in self.rows])

    def filter_rows(self, filter_function: Callable[[List[Cell[T]]], bool]) -> Grid[Cell[T]]:
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
            rotated_rows.append(self.get_column_cells(i))
        return Grid[T](rotated_rows)

    def flip_horizontal(self) -> Grid[T]:
        return Grid[T]([list(reversed(row)) for row in self.rows])

    def flip_vertical(self) -> Grid[T]:
        return self.flip_horizontal().rotate_right(2)

    # ##### HIGHER ORDER FUNCTIONS #####

    def map_values_by_function(self, mapping_function: Callable[[T], R]) -> Grid[R]:
        return self.map_cells(lambda cell: mapping_function(cell.value))

    def map_values_by_dict(self, replacements: Dict[T, T]) -> Grid[T]:
        return self.map_cells(lambda cell: replacements[cell.value] if cell.value in replacements else cell.value)

    def map_cells(self, mapping_function: Callable[[Cell[T]], R]) -> Grid[R]:
        def map_cell(cell: Cell[T]) -> Cell[R]:
            return Cell(cell.coord, mapping_function(cell))

        return Grid[R]([[map_cell(self[row_i][column_i])
                         for column_i in range(self.width)]
                        for row_i in range(self.height)])

    # ##### DISPLAY FUNCTIONS #####

    def __str__(self) -> str:
        return self.to_string()

    def to_string(self, cell_width: int = 1, separate_cells: bool = False) -> str:
        return "\n".join(self.to_string_list(cell_width, separate_cells))

    def to_string_justified(self) -> str:
        max_width = self.map_values_by_function(str).map_values_by_function(len).max()
        return self.to_string(max_width, True)

    def to_string_list(self, cell_width: int = 1, separate_cells: bool = False) -> List[str]:
        lines = []
        for row in self.rows:
            line = ""
            for cell in row:
                line += str(cell.value).rjust(cell_width, " ") + (" " if separate_cells else "")
            lines.append(line)
        return lines + [""]
