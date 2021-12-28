import pytest

from src.util.graph import Graph


@pytest.fixture
def test_graph():
    return Graph.from_edges([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])


# def test_from_edges():
#     assert Graph.from_edges([("A", "B"), ("B", "C")]).get_nodes() == ["A", "B", "C"]
#     assert Graph.from_edges([(1, 2), (2, 3)]).get_nodes() == [1, 2, 3]
#     assert Graph.from_edges([(1, 2), (2, 3)]).get_edges() == [((1, 2), 1), ((2, 1), 1), ((2, 3), 1), ((3, 2), 1)]
#
#
# def test_from_weighted_edges():
#     assert Graph.from_weighted_edges([((1, 2), 5)]).get_edges() == [((1, 2), 5), ((2, 1), 5)]
#
#
# def test_from_directed_edges():
#     assert Graph.from_directed_edges([(1, 2)]).get_edges() == [((1, 2), 1)]
#
#
# def test_from_directed_weighted_edges():
#     assert Graph.from_directed_weighted_edges([((1, 2), 5)]).get_edges() == [((1, 2), 5)]


def test_get_neighbors(test_graph: Graph[int]):
    assert test_graph.get_neighbors(1) == [2, 5]


def test_calc_shortest_path(test_graph: Graph[int]):
    assert test_graph.calc_shortest_path(1, 5) == [1, 5]
    assert test_graph.calc_shortest_path(2, 4) == [2, 3, 4]


def test_calc_shortest_path_len(test_graph: Graph[int]):
    assert test_graph.calc_shortest_path_len(1, 5) == 1
    assert test_graph.calc_shortest_path_len(2, 4) == 2


def test_get_all_paths_by_stop_condition(test_graph: Graph[int]):
    assert test_graph.get_all_paths_by_stop_condition(2, 5, lambda path, node: path[-1] > node) == [[2, 3, 4, 5]]


def test_get_number_of_paths_by_stop_condition(test_graph: Graph[int]):
    assert test_graph.get_number_of_paths_by_stop_condition(2, 5, lambda path, node: path[-1] > node) == 1
