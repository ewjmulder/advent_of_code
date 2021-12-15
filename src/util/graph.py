from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, TypeVar, Generic, Callable

from pygraph.algorithms.minmax import shortest_path as shortest_paths, path as shortest_path
from pygraph.classes.graph import graph

from src.util.collections import flatten

T = TypeVar('T')


@dataclass
class Graph(Generic[T]):
    wrapped_graph: graph

    @classmethod
    def from_edges(cls, edges: Iterable[Iterable[T]], accept_duplicate_edges: bool = True) -> Graph:
        g = graph()
        for edge in edges:
            for node in edge:
                if not g.has_node(node):
                    g.add_node(node)
        for (node_from, node_to) in edges:
            if not accept_duplicate_edges or not g.has_edge((node_from, node_to)):
                g.add_edge((node_from, node_to))
        return Graph(g)

    # @classmethod
    # def from_directed_edges(cls):

    def get_neighbors(self, node: T) -> List[T]:
        return self.wrapped_graph.neighbors(node)

    def calc_shortest_path(self, from_node: T, to_node: T) -> List[T]:
        return list(reversed(shortest_path(shortest_paths(self.wrapped_graph, from_node)[0], to_node)))

    def calc_shortest_path_len(self, from_node: T, to_node: T) -> int:
        return len(self.calc_shortest_path(from_node, to_node)) - 1

    def get_paths(self, start_node: T, end_node: T, stop_condition: Callable[[List[T], T], bool]) -> List[List[T]]:
        def visit(node: T, path: List[T]) -> List[List[T]]:
            return flatten([
                [path + [end_node]] if neighbor == end_node else visit(neighbor, path + [neighbor])
                for neighbor in self.wrapped_graph.neighbors(node)
                if neighbor != start_node and not stop_condition(path, neighbor)
            ])

        return visit(start_node, [start_node])

    def get_number_of_paths(self, start_node: T, end_node: T, stop_condition: Callable[[List[T], T], bool]) -> int:
        return len(self.get_paths(start_node, end_node, stop_condition))
