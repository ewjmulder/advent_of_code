from dataclasses import dataclass


@dataclass
class Coordinate:
    x: int
    y: int

    @property
    def row(self):
        return self.y

    @property
    def column(self):
        return self.x


def coord_from_point(x, y):
    return Coordinate(x, y)


def coord_from_grid(row, column):
    return Coordinate(column, row)
