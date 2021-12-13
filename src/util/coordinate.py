from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Coordinate:
    row: int
    column: int

    def __post_init__(self):
        self.hash_value = (self.row * self.column) + self.column

    def __hash__(self):
        return self.hash_value

    @classmethod
    def from_grid(cls, row: int, column: int) -> Coordinate:
        return Coordinate(row=row, column=column)

    @classmethod
    def from_point(cls, x: int, y: int) -> Coordinate:
        return Coordinate(row=y, column=x)

    @property
    def x(self):
        return self.column

    @property
    def y(self):
        return self.row

    def get_neighbor_left(self) -> Coordinate:
        return Coordinate(self.row, self.column - 1)

    def get_neighbor_right(self) -> Coordinate:
        return Coordinate(self.row, self.column + 1)

    def get_neighbor_above(self) -> Coordinate:
        return Coordinate(self.row - 1, self.column)

    def get_neighbor_below(self) -> Coordinate:
        return Coordinate(self.row + 1, self.column)

    def get_neighbor_left_above(self) -> Coordinate:
        return Coordinate(self.row - 1, self.column - 1)

    def get_neighbor_right_above(self) -> Coordinate:
        return Coordinate(self.row - 1, self.column + 1)

    def get_neighbor_left_below(self) -> Coordinate:
        return Coordinate(self.row + 1, self.column - 1)

    def get_neighbor_right_below(self) -> Coordinate:
        return Coordinate(self.row + 1, self.column + 1)

    def get_neighbors(self, include_diagonal: bool) -> List[Coordinate]:
        neighbors = [self.get_neighbor_left(), self.get_neighbor_right(),
                     self.get_neighbor_above(), self.get_neighbor_below()]
        if include_diagonal:
            neighbors += [self.get_neighbor_left_above(), self.get_neighbor_right_above(),
                          self.get_neighbor_left_below(), self.get_neighbor_right_below()]
        return neighbors
