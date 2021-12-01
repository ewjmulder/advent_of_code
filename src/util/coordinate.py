from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Coordinate:
    row: int
    column: int

    @property
    def x(self):
        return self.column

    @property
    def y(self):
        return self.row

    def neighbor_left(self) -> Coordinate:
        return Coordinate(self.row, self.column - 1)

    def neighbor_right(self) -> Coordinate:
        return Coordinate(self.row, self.column + 1)

    def neighbor_above(self) -> Coordinate:
        return Coordinate(self.row - 1, self.column)

    def neighbor_below(self) -> Coordinate:
        return Coordinate(self.row + 1, self.column)


def coord_from_point(x, y):
    return Coordinate(row=y, column=x)


def coord_from_grid(row, column):
    return Coordinate(row, column)
