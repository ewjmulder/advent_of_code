from src.util.coordinate import Coordinate


def test_from_grid():
    coord = Coordinate.from_grid(row=1, column=2)
    assert coord.row == 1
    assert coord.column == 2
    assert coord.y == 1
    assert coord.x == 2


def test_from_point():
    coord = Coordinate.from_point(x=1, y=2)
    assert coord.row == 2
    assert coord.column == 1
    assert coord.y == 2
    assert coord.x == 1


def test_neighbors():
    coord = Coordinate.from_point(x=2, y=2)

    assert coord.get_neighbor_left().x == 1
    assert coord.get_neighbor_left().y == 2
    assert coord.get_neighbor_right().x == 3
    assert coord.get_neighbor_right().y == 2
    assert coord.get_neighbor_above().x == 2
    assert coord.get_neighbor_above().y == 1
    assert coord.get_neighbor_below().x == 2
    assert coord.get_neighbor_below().y == 3

    assert coord.get_neighbor_left_above().x == 1
    assert coord.get_neighbor_left_above().y == 1
    assert coord.get_neighbor_right_above().x == 3
    assert coord.get_neighbor_right_above().y == 1
    assert coord.get_neighbor_left_below().x == 1
    assert coord.get_neighbor_left_below().y == 3
    assert coord.get_neighbor_right_below().x == 3
    assert coord.get_neighbor_right_below().y == 3

    non_diagonal_neighbors = [coord.get_neighbor_left(), coord.get_neighbor_right(),
                              coord.get_neighbor_above(), coord.get_neighbor_below()]
    assert coord.get_neighbors(include_diagonal=False) == non_diagonal_neighbors
    assert coord.get_neighbors(include_diagonal=True) == non_diagonal_neighbors + [
        coord.get_neighbor_left_above(), coord.get_neighbor_right_above(),
        coord.get_neighbor_left_below(), coord.get_neighbor_right_below()
    ]
