from dataclasses import dataclass

import pytest

from src.util.graph import Graph


def undirected_unweighted_graph() -> Graph[int]:
    return Graph.from_edges([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])


def directed_unweighted_graph() -> Graph[int]:
    return Graph.from_directed_edges([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])


def undirected_weighted_graph() -> Graph[int]:
    return Graph.from_weighted_edges([((1, 2), 1), ((2, 3), 2), ((3, 4), 3), ((4, 5), 4), ((5, 1), 5)])


def directed_weighted_graph() -> Graph[int]:
    return Graph.from_directed_weighted_edges([((1, 2), 1), ((2, 3), 2), ((3, 4), 3), ((4, 5), 4), ((5, 1), 5)])


@dataclass
class TestGraphs:
    undirected_unweighted: Graph[int]
    directed_unweighted: Graph[int]
    undirected_weighted: Graph[int]
    directed_weighted: Graph[int]


@pytest.fixture
def test_graphs() -> TestGraphs:
    return TestGraphs(undirected_unweighted_graph(), directed_unweighted_graph(),
                      undirected_weighted_graph(), directed_weighted_graph())


def test_from_edges():
    assert Graph.from_edges([("A", "B"), ("B", "C")]).get_nodes() == ["A", "B", "C"]
    assert Graph.from_edges([(1, 2), (2, 3)]).get_nodes() == [1, 2, 3]
    assert Graph.from_edges([(1, 2), (2, 3)]).get_edges() == [((1, 2), 1), ((2, 3), 1)]
    assert not Graph.from_edges([(1, 2), (2, 3)]).is_directed()


def test_from_weighted_edges():
    assert Graph.from_weighted_edges([((1, 2), 5)]).get_edges() == [((1, 2), 5)]
    assert not Graph.from_edges([(1, 2), (2, 3)]).is_directed()


def test_from_directed_edges():
    assert Graph.from_directed_edges([(1, 2)]).get_edges() == [((1, 2), 1)]
    assert Graph.from_directed_edges([(1, 2)]).is_directed()


def test_from_directed_weighted_edges():
    assert Graph.from_directed_weighted_edges([((1, 2), 5)]).get_edges() == [((1, 2), 5)]
    assert Graph.from_directed_weighted_edges([((1, 2), 5)]).is_directed()


# Above test methods also test get_nodes, get_edges and is_directed


def test_get_neighbors(test_graphs: TestGraphs):
    assert test_graphs.undirected_unweighted.get_neighbors(1) == [2, 5]
    assert test_graphs.directed_unweighted.get_neighbors(1) == [2]
    assert test_graphs.undirected_weighted.get_neighbors(1) == [2, 5]
    assert test_graphs.directed_weighted.get_neighbors(1) == [2]


def test_calc_shortest_path(test_graphs: TestGraphs):
    assert test_graphs.undirected_unweighted.calc_shortest_path(1, 5) == [1, 5]
    assert test_graphs.undirected_unweighted.calc_shortest_path(4, 2) == [4, 3, 2]

    assert test_graphs.directed_unweighted.calc_shortest_path(1, 5) == [1, 2, 3, 4, 5]
    assert test_graphs.directed_unweighted.calc_shortest_path(4, 2) == [4, 5, 1, 2]

    assert test_graphs.undirected_weighted.calc_shortest_path(1, 5) == [1, 5]
    assert test_graphs.undirected_weighted.calc_shortest_path(4, 1) == [4, 3, 2, 1]

    assert test_graphs.directed_weighted.calc_shortest_path(1, 5) == [1, 2, 3, 4, 5]
    assert test_graphs.directed_weighted.calc_shortest_path(4, 1) == [4, 5, 1]


def test_calc_shortest_path_len(test_graphs: TestGraphs):
    assert test_graphs.undirected_unweighted.calc_shortest_path_len(1, 5) == 1
    assert test_graphs.directed_unweighted.calc_shortest_path_len(1, 5) == 4


def test_get_all_paths_by_stop_condition(test_graphs: TestGraphs):
    assert test_graphs.undirected_unweighted.get_all_paths_by_stop_condition(
        2, 5, lambda path, node: path[-1] > node) == [[2, 3, 4, 5]]


def test_get_number_of_paths_by_stop_condition(test_graphs: TestGraphs):
    assert test_graphs.undirected_unweighted.get_number_of_paths_by_stop_condition(
        2, 5, lambda path, node: path[-1] > node) == 1
