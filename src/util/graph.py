from __future__ import annotations
from typing import Iterable, List
from pygraph.classes.graph import graph
from pygraph.algorithms.minmax import shortest_path as shortest_paths, path as shortest_path
from dataclasses import dataclass


@dataclass
class Graph:
    wrapped_graph: graph

    @classmethod
    def from_edges(cls, edges: Iterable[Iterable[str]], accept_duplicate_edges: bool = True) -> Graph:
        g = graph()
        for edge in edges:
            for node in edge:
                if not g.has_node(node):
                    g.add_node(node)
        for (node_from, node_to) in edges:
            if not accept_duplicate_edges or not g.has_edge((node_from, node_to)):
                g.add_edge((node_from, node_to))
        return Graph(g)

    def shortest_path(self, from_node: str, to_node: str) -> List[str]:
            return list(reversed(shortest_path(shortest_paths(self.wrapped_graph, from_node)[0], to_node)))

    def shortest_path_len(self, from_node: str, to_node: str) -> int:
        return len(self.shortest_path(from_node, to_node)) - 1
