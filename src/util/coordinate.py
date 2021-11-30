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


def coord_from_point(x, y):
    return Coordinate(row=y, column=x)


def coord_from_grid(row, column):
    return Coordinate(row, column)
