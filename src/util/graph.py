# For graph functionality, the python-graph-core library should be used.
# This module contains some extra util functions for convenience

from typing import Iterable, List
from pygraph.classes.graph import graph
from pygraph.algorithms.minmax import shortest_path as shortest_paths, path as shortest_path
from .parser import read_file_as_lines, parse_lines_from_string


def parse_graph_from_file(file: str, separator: str) -> graph:
    return parse_graph_from_lines(read_file_as_lines(file), separator)


def parse_graph_from_string(string: str, separator: str) -> graph:
    return build_graph([line.split(separator) for line in parse_lines_from_string(string)])


def parse_graph_from_lines(lines: List[str], separator: str) -> graph:
    return build_graph([line.split(separator) for line in lines])


def build_graph(edges: Iterable[Iterable[str]], accept_duplicate_edges: bool = True) -> graph:
    g = graph()
    for edge in edges:
        for node in edge:
            if not g.has_node(node):
                g.add_node(node)
    for (node_from, node_to) in edges:
        if not accept_duplicate_edges or not g.has_edge((node_from, node_to)):
            g.add_edge((node_from, node_to))
    return g


def calc_shortest_path(g: graph, from_node: str, to_node: str) -> List[str]:
    return list(reversed(shortest_path(shortest_paths(g, from_node)[0], to_node)))


def calc_shortest_path_len(g: graph, from_node: str, to_node: str) -> int:
    return len(calc_shortest_path(g, from_node, to_node)) - 1
