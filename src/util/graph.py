from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, TypeVar, Generic, Tuple, Callable

from igraph import Graph as IGraph

from src.util.collections import flatten

T = TypeVar('T')


@dataclass
class Graph(Generic[T]):
    igraph: IGraph

    @classmethod
    def from_edges(cls, edges: Iterable[Iterable[T]]) -> Graph[T]:
        """Creates an undirected, unweighted graph"""
        return cls._from_edges(False, [(list(edge), 1) for edge in edges])

    @classmethod
    def from_weighted_edges(cls, edges: Iterable[(Iterable[T], int)]) -> Graph[T]:
        """Creates an undirected, weighted graph"""
        return cls._from_edges(False, [(list(edge), weight) for edge, weight in edges])

    @classmethod
    def from_directed_edges(cls, edges: Iterable[Iterable[T]]) -> Graph[T]:
        """Creates an directed, unweighted graph"""
        return cls._from_edges(True, [(list(edge), 1) for edge in edges])

    @classmethod
    def from_directed_weighted_edges(cls, edges: Iterable[(Iterable[T], int)]) -> Graph[T]:
        """Creates an directed, weighted graph"""
        return cls._from_edges(True, [(list(edge), weight) for edge, weight in edges])

    @classmethod
    def _from_edges(cls, directed: bool, edges: List[Tuple[List[T], int]]):
        igraph = IGraph(directed=directed)
        for edge, weight in edges:
            for node in edge:
                if len(igraph.vs) == 0 or node not in igraph.vs["node"]:
                    igraph.add_vertex(str(node), node=node)
        for (node_from, node_to), weight in edges:
            igraph.add_edge(str(node_from), str(node_to), edge=(node_from, node_to), weight=weight)
        return Graph(igraph)

    def _vertex_indices_to_nodes(self, vertex_indices: Iterable[int]) -> List[T]:
        node_values = self.igraph.vs["node"]
        return [node_values[vertex_index] for vertex_index in vertex_indices]

    def get_nodes(self) -> List[T]:
        return self.igraph.vs["node"]

    def get_edges(self) -> List[Tuple[T, T]]:
        return list(zip(self.igraph.es["edge"], self.igraph.es["weight"]))

    def get_neighbors(self, node: T) -> List[T]:
        return self._vertex_indices_to_nodes(self.igraph.neighbors(str(node), mode="out"))

    def is_directed(self) -> bool:
        return self.igraph.is_directed()

    def calc_shortest_path(self, from_node: T, to_node: T) -> List[T]:
        return self._vertex_indices_to_nodes(
            self.igraph.get_shortest_paths(str(from_node), str(to_node), weights=self.igraph.es["weight"])[0])

    def calc_shortest_path_len(self, from_node: T, to_node: T) -> int:
        return len(self.calc_shortest_path(from_node, to_node)) - 1

    def get_all_paths_by_stop_condition(self, start_node: T, end_node: T,
                                        stop_condition: Callable[[List[T], T], bool]) -> List[List[T]]:
        def visit(node: T, path: List[T]) -> List[List[T]]:
            return flatten([
                [path + [end_node]] if neighbor == end_node else visit(neighbor, path + [neighbor])
                for neighbor in self.get_neighbors(node)
                if neighbor != start_node and not stop_condition(path, neighbor)
            ])

        return visit(start_node, [start_node])

    def get_number_of_paths_by_stop_condition(self, start_node: T, end_node: T,
                                              stop_condition: Callable[[List[T], T], bool]) -> int:
        return len(self.get_all_paths_by_stop_condition(start_node, end_node, stop_condition))
