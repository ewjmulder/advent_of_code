import pytest

from src.util.coordinate import Coordinate
from src.util.grid import Grid, Cell, FrozenGrid


def create_test_grid():
    return Grid.from_values([[1, 2, 3], [4, 5, 6]])


def create_bit_test_grid():
    return Grid.from_values([[1, 1, 1, 1], [0, 1, 0, 0], [1, 1, 0, 0]])


@pytest.fixture
def test_grid():
    return create_test_grid()


@pytest.fixture
def bit_test_grid():
    return create_bit_test_grid()


def test_data_class_features(test_grid: Grid[int]):
    # Grids should be equal if their data is equal
    assert test_grid == create_test_grid()

    # Normal Grid cannot be hashed, since it's mutable
    with pytest.raises(TypeError):
        hash(test_grid)
    # But FrozenGrid can be hashed (still mutable, but at your own risk)
    hash(test_grid.freeze())


def test_cell(test_grid: Grid[int]):
    cell = test_grid[0][2]
    assert cell.row == 0
    assert cell.column == 2
    assert cell.value == 3


def test_validate():
    with pytest.raises(ValueError):
        Grid.from_values([])
    with pytest.raises(ValueError):
        Grid.from_values([[1, 2], [3]])


def test_from_values():
    assert Grid.from_values([[0, 1]]).rows == [[Cell(Coordinate(0, 0), 0), Cell(Coordinate(0, 1), 1)]]


def test_fill_grid():
    grid = Grid.fill_grid(2, 3, 0)
    assert grid.height == 2
    assert grid.width == 3
    assert grid.get_all_values() == [0, 0, 0, 0, 0, 0]


def test_freeze(test_grid: Grid[int]):
    assert isinstance(test_grid.freeze(), FrozenGrid)
    assert type(hash(test_grid.freeze())) == int


def test_get_item(test_grid: Grid[int]):
    assert Grid.from_values([[0, 1]])[0] == [Cell(Coordinate(0, 0), 0), Cell(Coordinate(0, 1), 1)]


def test_get_cell_by_index(test_grid: Grid[int]):
    assert test_grid.get_cell_by_index(1, 2) == Cell(Coordinate(1, 2), 6)


def test_get_cell_by_coord(test_grid: Grid[int]):
    assert test_grid.get_cell_by_coord(Coordinate(0, 1)) == Cell(Coordinate(0, 1), 2)


def test_get_cells_by_coords(test_grid: Grid[int]):
    assert test_grid.get_cells_by_coords([Coordinate(0, 1), Coordinate(1, 2)]) == [
        Cell(Coordinate(0, 1), 2), Cell(Coordinate(1, 2), 6)
    ]


def test_get_value_by_index(test_grid: Grid[int]):
    assert test_grid.get_value_by_index(0, 2) == 3


def test_get_value_by_coord(test_grid: Grid[int]):
    assert test_grid.get_value_by_coord(Coordinate(0, 0)) == 1


def test_get_values_by_coords(test_grid: Grid[int]):
    assert test_grid.get_values_by_coords([Coordinate(1, 1), Coordinate(0, 2)]) == [5, 3]


def test_get_all_cells(test_grid: Grid[int]):
    assert test_grid.get_all_cells() == [
        Cell(Coordinate(0, 0), 1), Cell(Coordinate(0, 1), 2), Cell(Coordinate(0, 2), 3),
        Cell(Coordinate(1, 0), 4), Cell(Coordinate(1, 1), 5), Cell(Coordinate(1, 2), 6)
    ]


def test_get_all_coords(test_grid: Grid[int]):
    assert test_grid.get_all_coords() == [
        Coordinate(0, 0), Coordinate(0, 1), Coordinate(0, 2),
        Coordinate(1, 0), Coordinate(1, 1), Coordinate(1, 2)
    ]


def test_get_all_values(test_grid: Grid[int]):
    assert test_grid.get_all_values() == [1, 2, 3, 4, 5, 6]


def test_count_value(test_grid: Grid[int]):
    grid = Grid.from_values([[1, 1, 0, 1], [1, 0, 1, 0]])
    assert grid.count_value(0) == 3
    assert grid.count_value(1) == 5
    assert grid.count_value(2) == 0


def test_min(test_grid: Grid[int]):
    assert test_grid.min_value() == 1


def test_max(test_grid: Grid[int]):
    assert test_grid.max_value() == 6


def test_get_row_cells(test_grid: Grid[int]):
    assert test_grid.get_row_cells(0) == [
        Cell(Coordinate(0, 0), 1), Cell(Coordinate(0, 1), 2), Cell(Coordinate(0, 2), 3)
    ]


def test_get_row_coords(test_grid: Grid[int]):
    assert test_grid.get_row_coords(1) == [
        Coordinate(1, 0), Coordinate(1, 1), Coordinate(1, 2)
    ]


def test_get_row_values(test_grid: Grid[int]):
    assert test_grid.get_row_values(1) == [4, 5, 6]


def test_get_rows_cells(test_grid: Grid[int]):
    assert test_grid.get_rows_cells() == [
        [Cell(Coordinate(0, 0), 1), Cell(Coordinate(0, 1), 2), Cell(Coordinate(0, 2), 3)],
        [Cell(Coordinate(1, 0), 4), Cell(Coordinate(1, 1), 5), Cell(Coordinate(1, 2), 6)]
    ]


def test_get_rows_coords(test_grid: Grid[int]):
    assert test_grid.get_rows_coords() == [
        [Coordinate(0, 0), Coordinate(0, 1), Coordinate(0, 2)],
        [Coordinate(1, 0), Coordinate(1, 1), Coordinate(1, 2)]
    ]


def test_get_rows_values(test_grid: Grid[int]):
    assert test_grid.get_rows_values() == [
        [1, 2, 3],
        [4, 5, 6]
    ]


def test_get_column_cells(test_grid: Grid[int]):
    assert test_grid.get_column_cells(0) == [
        Cell(Coordinate(0, 0), 1), Cell(Coordinate(1, 0), 4)
    ]


def test_get_column_coords(test_grid: Grid[int]):
    assert test_grid.get_column_coords(1) == [
        Coordinate(0, 1), Coordinate(1, 1)
    ]


def test_get_column_values(test_grid: Grid[int]):
    assert test_grid.get_column_values(1) == [2, 5]


def test_get_columns_cells(test_grid: Grid[int]):
    assert test_grid.get_columns_cells() == [
        [Cell(Coordinate(0, 0), 1), Cell(Coordinate(1, 0), 4)],
        [Cell(Coordinate(0, 1), 2), Cell(Coordinate(1, 1), 5)],
        [Cell(Coordinate(0, 2), 3), Cell(Coordinate(1, 2), 6)]
    ]


def test_get_columns_coords(test_grid: Grid[int]):
    assert test_grid.get_columns_coords() == [
        [Coordinate(0, 0), Coordinate(1, 0)],
        [Coordinate(0, 1), Coordinate(1, 1)],
        [Coordinate(0, 2), Coordinate(1, 2)]
    ]


def test_get_columns_values(test_grid: Grid[int]):
    assert test_grid.get_columns_values() == [
        [1, 4],
        [2, 5],
        [3, 6]
    ]


def test_get_rows_and_columns_cells(test_grid: Grid[int]):
    assert test_grid.get_rows_and_columns_cells() == [
        [Cell(Coordinate(0, 0), 1), Cell(Coordinate(0, 1), 2), Cell(Coordinate(0, 2), 3)],
        [Cell(Coordinate(1, 0), 4), Cell(Coordinate(1, 1), 5), Cell(Coordinate(1, 2), 6)],
        [Cell(Coordinate(0, 0), 1), Cell(Coordinate(1, 0), 4)],
        [Cell(Coordinate(0, 1), 2), Cell(Coordinate(1, 1), 5)],
        [Cell(Coordinate(0, 2), 3), Cell(Coordinate(1, 2), 6)]
    ]


def test_get_rows_and_columns_coords(test_grid: Grid[int]):
    assert test_grid.get_rows_and_columns_coords() == [
        [Coordinate(0, 0), Coordinate(0, 1), Coordinate(0, 2)],
        [Coordinate(1, 0), Coordinate(1, 1), Coordinate(1, 2)],
        [Coordinate(0, 0), Coordinate(1, 0)],
        [Coordinate(0, 1), Coordinate(1, 1)],
        [Coordinate(0, 2), Coordinate(1, 2)]
    ]


def test_get_rows_and_columns_values(test_grid: Grid[int]):
    assert test_grid.get_rows_and_columns_values() == [
        [1, 2, 3],
        [4, 5, 6],
        [1, 4],
        [2, 5],
        [3, 6]
    ]


def test_get_neighbor_cells(test_grid: Grid[int]):
    assert test_grid.get_neighbor_cells(Coordinate(0, 1), include_diagonal=False) == [
        Cell(Coordinate(0, 0), 1), Cell(Coordinate(0, 2), 3), Cell(Coordinate(1, 1), 5)
    ]
    assert test_grid.get_neighbor_cells(Coordinate(0, 1), include_diagonal=True) == [
        Cell(Coordinate(0, 0), 1), Cell(Coordinate(0, 2), 3),
        Cell(Coordinate(1, 0), 4), Cell(Coordinate(1, 1), 5), Cell(Coordinate(1, 2), 6)
    ]
    assert test_grid.get_neighbor_cells(Coordinate(0, 1), include_diagonal=True, include_own_cell=True) == [
        Cell(Coordinate(0, 0), 1), Cell(Coordinate(0, 1), 2), Cell(Coordinate(0, 2), 3),
        Cell(Coordinate(1, 0), 4), Cell(Coordinate(1, 1), 5), Cell(Coordinate(1, 2), 6)
    ]

    assert test_grid.get_neighbor_cells(Coordinate(1, 1), include_diagonal=False) == [
        Cell(Coordinate(0, 1), 2), Cell(Coordinate(1, 0), 4), Cell(Coordinate(1, 2), 6)
    ]
    assert test_grid.get_neighbor_cells(Coordinate(1, 1), include_diagonal=True) == [
        Cell(Coordinate(0, 0), 1), Cell(Coordinate(0, 1), 2), Cell(Coordinate(0, 2), 3),
        Cell(Coordinate(1, 0), 4), Cell(Coordinate(1, 2), 6)
    ]
    assert test_grid.get_neighbor_cells(Coordinate(1, 1), include_diagonal=True, include_own_cell=True) == [
        Cell(Coordinate(0, 0), 1), Cell(Coordinate(0, 1), 2), Cell(Coordinate(0, 2), 3),
        Cell(Coordinate(1, 0), 4), Cell(Coordinate(1, 1), 5), Cell(Coordinate(1, 2), 6)
    ]

    assert test_grid.get_neighbor_cells(Coordinate(0, 0), include_diagonal=False) == [
        Cell(Coordinate(0, 1), 2), Cell(Coordinate(1, 0), 4)
    ]
    assert test_grid.get_neighbor_cells(Coordinate(0, 2), include_diagonal=False) == [
        Cell(Coordinate(0, 1), 2), Cell(Coordinate(1, 2), 6)
    ]
    assert test_grid.get_neighbor_cells(Coordinate(1, 0), include_diagonal=False) == [
        Cell(Coordinate(0, 0), 1), Cell(Coordinate(1, 1), 5)
    ]
    assert test_grid.get_neighbor_cells(Coordinate(1, 2), include_diagonal=False) == [
        Cell(Coordinate(0, 2), 3), Cell(Coordinate(1, 1), 5)
    ]


def test_get_neighbor_coords(test_grid: Grid[int]):
    assert test_grid.get_neighbor_coords(Coordinate(0, 1), include_diagonal=False) == [
        Coordinate(0, 0), Coordinate(0, 2), Coordinate(1, 1)
    ]


def test_get_neighbor_values(test_grid: Grid[int]):
    assert test_grid.get_neighbor_values(Coordinate(0, 1), include_diagonal=False) == [1, 3, 5]


def test_get_local_area_cells(test_grid: Grid[int]):
    assert test_grid.get_local_area_cells(Coordinate(0, 1),
                                          lambda cell1, cell2: cell1.value < cell2.value,
                                          include_diagonal=False) == [
               Cell(Coordinate(0, 1), 2), Cell(Coordinate(0, 2), 3),
               Cell(Coordinate(1, 1), 5), Cell(Coordinate(1, 2), 6)
           ]
    assert test_grid.get_local_area_cells(Coordinate(1, 1),
                                          lambda cell1, cell2: abs(cell1.value - cell2.value) == 4,
                                          include_diagonal=True) == [
               Cell(Coordinate(0, 0), 1), Cell(Coordinate(1, 1), 5)
           ]


def test_find_cells_by_predicate_on_cell(test_grid: Grid[int]):
    assert test_grid.find_cells_by_predicate_on_cell(lambda cell: cell.value >= 3 and cell.coord.column >= 1) == \
           [Cell(Coordinate(0, 2), 3), Cell(Coordinate(1, 1), 5), Cell(Coordinate(1, 2), 6)]


def test_find_cells_by_predicate_on_coord(test_grid: Grid[int]):
    assert test_grid.find_cells_by_predicate_on_coord(lambda coord: coord.row + coord.column == 2) == \
           [Cell(Coordinate(0, 2), 3), Cell(Coordinate(1, 1), 5)]


def test_find_cells_by_predicate_on_value(test_grid: Grid[int]):
    assert test_grid.find_cells_by_predicate_on_value(lambda value: value % 2 == 0) == \
           [Cell(Coordinate(0, 1), 2), Cell(Coordinate(1, 0), 4), Cell(Coordinate(1, 2), 6)]


def test_find_cells_by_value(test_grid: Grid[int]):
    assert test_grid.find_cells_by_value(1) == [Cell(Coordinate(0, 0), 1)]
    assert test_grid.find_cells_by_value([2, 4]) == [Cell(Coordinate(0, 1), 2), Cell(Coordinate(1, 0), 4)]


def test_find_most_common_value_in_grid(bit_test_grid: Grid[int]):
    assert bit_test_grid.find_most_common_value_in_grid() == 1


def test_find_most_common_value_in_row(bit_test_grid: Grid[int]):
    assert bit_test_grid.find_most_common_value_in_row(0) == 1
    assert bit_test_grid.find_most_common_value_in_row(1) == 0
    assert bit_test_grid.find_most_common_value_in_row(2) is None
    assert bit_test_grid.find_most_common_value_in_row(2, default_for_tie=2) == 2


def test_find_most_common_value_in_column(bit_test_grid: Grid[int]):
    assert bit_test_grid.find_most_common_value_in_column(0) == 1
    assert bit_test_grid.find_most_common_value_in_column(3) == 0


def test_find_least_common_value_in_grid(bit_test_grid: Grid[int]):
    assert bit_test_grid.find_least_common_value_in_grid() == 0


def test_find_least_common_value_in_row(bit_test_grid: Grid[int]):
    assert bit_test_grid.find_least_common_value_in_row(0) == 1
    assert bit_test_grid.find_least_common_value_in_row(1) == 1
    assert bit_test_grid.find_least_common_value_in_row(2) is None
    assert bit_test_grid.find_least_common_value_in_row(2, default_for_tie=2) == 2


def test_find_least_common_value_in_column(bit_test_grid: Grid[int]):
    assert bit_test_grid.find_least_common_value_in_column(0) == 0
    assert bit_test_grid.find_least_common_value_in_column(3) == 1


def test_copy(test_grid: Grid[int]):
    assert test_grid.copy().rows == [
        [Cell(Coordinate(0, 0), 1), Cell(Coordinate(0, 1), 2), Cell(Coordinate(0, 2), 3)],
        [Cell(Coordinate(1, 0), 4), Cell(Coordinate(1, 1), 5), Cell(Coordinate(1, 2), 6)]
    ]
    assert not test_grid.copy() is test_grid
    assert not test_grid.copy() is test_grid.copy()


def test_filter_rows(test_grid: Grid[int]):
    assert test_grid.filter_rows(lambda row: sum(cell.value for cell in row) > 8) == \
           Grid([[Cell(Coordinate(1, 0), 4), Cell(Coordinate(1, 1), 5), Cell(Coordinate(1, 2), 6)]])


def test_rotate_right(test_grid: Grid[int]):
    assert test_grid.rotate_right(1) == Grid([
        [Cell(Coordinate(0, 0), 4), Cell(Coordinate(0, 1), 1)],
        [Cell(Coordinate(1, 0), 5), Cell(Coordinate(1, 1), 2)],
        [Cell(Coordinate(2, 0), 6), Cell(Coordinate(2, 1), 3)]
    ])


def test_rotate_right_once(test_grid: Grid[int]):
    assert test_grid.rotate_right_once() == test_grid.rotate_right(1)


def test_rotate_left(test_grid: Grid[int]):
    assert test_grid.rotate_left(1) == Grid([
        [Cell(Coordinate(0, 0), 3), Cell(Coordinate(0, 1), 6)],
        [Cell(Coordinate(1, 0), 2), Cell(Coordinate(1, 1), 5)],
        [Cell(Coordinate(2, 0), 1), Cell(Coordinate(2, 1), 4)]
    ])


def test_rotate_left_once(test_grid: Grid[int]):
    assert test_grid.rotate_left_once() == test_grid.rotate_left(1)


def test_flip_horizontal(test_grid: Grid[int]):
    assert test_grid.flip_horizontal() == Grid([
        [Cell(Coordinate(0, 0), 3), Cell(Coordinate(0, 1), 2), Cell(Coordinate(0, 2), 1)],
        [Cell(Coordinate(1, 0), 6), Cell(Coordinate(1, 1), 5), Cell(Coordinate(1, 2), 4)]
    ])


def test_flip_vertical(test_grid: Grid[int]):
    assert test_grid.flip_vertical() == Grid([
        [Cell(Coordinate(0, 0), 4), Cell(Coordinate(0, 1), 5), Cell(Coordinate(0, 2), 6)],
        [Cell(Coordinate(1, 0), 1), Cell(Coordinate(1, 1), 2), Cell(Coordinate(1, 2), 3)]
    ])


def test_get_all_orientations(test_grid: Grid[int]):
    rotations_no_flip = [
        test_grid.rotate_right(0), test_grid.rotate_right(1), test_grid.rotate_right(2), test_grid.rotate_right(3)
    ]
    assert test_grid.get_all_orientations(include_flip=False) == rotations_no_flip

    test_grid_flipped = test_grid.flip_horizontal()
    assert test_grid.get_all_orientations(include_flip=True) == rotations_no_flip + [
        test_grid_flipped.rotate_right(0), test_grid_flipped.rotate_right(1),
        test_grid_flipped.rotate_right(2), test_grid_flipped.rotate_right(3)
    ]


# TODO: Re-write when Graph has been refactored
# def test_to_directed_weighted_graph(test_grid: Grid[int]):
#     assert test_grid.to_directed_weighted_graph(include_diagonal=False) ==


def test_map_values_by_function(test_grid: Grid[int]):
    assert test_grid.map_values_by_function(lambda value: value + 1) == Grid([
        [Cell(Coordinate(0, 0), 2), Cell(Coordinate(0, 1), 3), Cell(Coordinate(0, 2), 4)],
        [Cell(Coordinate(1, 0), 5), Cell(Coordinate(1, 1), 6), Cell(Coordinate(1, 2), 7)]
    ])


def test_map_values_by_dict(test_grid: Grid[int]):
    assert test_grid.map_values_by_dict({1: 11, 3: 33, 4: 44}) == Grid([
        [Cell(Coordinate(0, 0), 11), Cell(Coordinate(0, 1), 2), Cell(Coordinate(0, 2), 33)],
        [Cell(Coordinate(1, 0), 44), Cell(Coordinate(1, 1), 5), Cell(Coordinate(1, 2), 6)]
    ])


def test_map_cells_by_function(test_grid: Grid[int]):
    assert test_grid.map_cells_by_function(lambda cell: cell.value + cell.coord.row + cell.coord.column) == Grid([
        [Cell(Coordinate(0, 0), 1), Cell(Coordinate(0, 1), 3), Cell(Coordinate(0, 2), 5)],
        [Cell(Coordinate(1, 0), 5), Cell(Coordinate(1, 1), 7), Cell(Coordinate(1, 2), 9)]
    ])


def test___str___(test_grid: Grid[int]):
    assert test_grid.__str__() == test_grid.to_string()


def test_to_string(test_grid: Grid[int]):
    assert test_grid.to_string() == "123\n456\n"
    assert test_grid.to_string(cell_width=2) == " 1 2 3\n 4 5 6\n"
    assert test_grid.to_string(separate_cells=True) == "1 2 3 \n4 5 6 \n"
    assert test_grid.to_string(cell_width=3, separate_cells=True) == "  1   2   3 \n  4   5   6 \n"


def test_to_string_mapped(test_grid: Grid[int]):
    assert test_grid.to_string_mapped({"1": "a", "2": "b", "5": "e"}) == "ab3\n4e6\n"


def test_to_string_justified(test_grid: Grid[int]):
    assert test_grid.to_string_justified() == "1 2 3 \n4 5 6 \n"
    assert test_grid.map_values_by_dict({1: 111}).to_string_justified() == "111   2   3 \n  4   5   6 \n"


def test_to_string_list(test_grid: Grid[int]):
    assert test_grid.to_string_list() == test_grid.to_string().splitlines() + [""]
    assert test_grid.to_string_list(cell_width=2) == test_grid.to_string(cell_width=2).splitlines() + [""]
    assert test_grid.to_string_list(separate_cells=True) == test_grid.to_string(separate_cells=True).splitlines() + [""]
    assert test_grid.to_string_list(cell_width=3, separate_cells=True) == \
           test_grid.to_string(cell_width=3, separate_cells=True).splitlines() + [""]
