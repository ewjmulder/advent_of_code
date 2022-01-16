from __future__ import annotations

from typing import TypeVar, Generic, List, Callable, Any

from src.util.collections import flatten

T = TypeVar('T')
R = TypeVar('R')


class Tree(Generic[T]):
    def __init__(self, name: str = None, data: T = None, children: List[Tree[T]] = None, parent: Tree[T] = None):
        self.name = name
        self.data = data
        self.children = children or []
        self.parent = parent

    def __hash__(self) -> int:
        return hash((self.name, self.data))

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.data == other.data and self.children == self.children

    def is_root(self) -> bool:
        return self.parent is None

    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def add_child(self, child: Tree[T]):
        self.children.append(child)
        child.parent = self

    def depth(self) -> int:
        return 1 + max(self.recurse(Tree.depth), default=0)

    def find_one_by_name(self, name: str) -> Tree[T]:
        # Assume there is always 1 unique match
        return self.find_all_by_name(name)[0]

    def find_all_by_name(self, name: str) -> List[Tree[T]]:
        return ([self] if self.name == name else []) + self.flat_rec(Tree.find_all_by_name, name=name)

    def get_nodes_at_level(self, level: int) -> List[Tree[T]]:
        return [self] if level == 1 else self.flat_rec(Tree.get_nodes_at_level, level=level - 1)

    def to_list_prefix(self) -> List[Tree[T]]:
        return [self] + self.flat_rec(Tree.to_list_prefix)

    def to_list_postfix(self) -> List[Tree[T]]:
        return self.flat_rec(Tree.to_list_postfix) + [self]

    def flatten(self) -> List[Tree[T]]:
        return self.to_list_prefix()

    def flatten_name(self) -> List[str]:
        return [tree.name for tree in self.to_list_prefix()]

    def flatten_data(self) -> List:
        return [tree.data for tree in self.to_list_prefix()]

    def recurse(self, function: Callable[[Tree[T], Any], R], **kwargs) -> List[R]:
        return [function(child, **kwargs) for child in self.children]

    def flat_rec(self, function: Callable[[Any], List[Tree[T]]], **kwargs) -> List[Tree[T]]:
        return flatten(self.recurse(function, **kwargs))

    def map_data_to_data(self, mapping_function: Callable[[T], R]) -> Tree[R]:
        return self.map_tree_to_tree(lambda tree: Tree(name=tree.name, data=mapping_function(tree.data)))

    def map_tree_to_data(self, mapping_function: Callable[[Tree[T]], R]) -> Tree[R]:
        return self.map_tree_to_tree(lambda tree: Tree(name=tree.name, data=mapping_function(tree)))

    def map_tree_to_name_and_data(self, mapping_function: Callable[[Tree[T]], R]) -> Tree[R]:
        def _name_and_data_to_tree(tree):
            mapped_name, mapped_data = mapping_function(tree)
            return Tree(name=mapped_name, data=mapped_data)

        return self.map_tree_to_tree(_name_and_data_to_tree)

    def map_tree_to_tree(self, mapping_function: Callable[[Tree[T]], Tree[R]]) -> Tree[R]:
        mapped_self = mapping_function(self)
        for mapped_child in self.recurse(Tree.map_tree_to_tree, mapping_function=mapping_function):
            mapped_self.add_child(mapped_child)
        return mapped_self

    def to_string_node(self) -> str:
        string = ""
        if self.name is not None:
            string += self.name
            if self.data is not None:
                string += f"({self.data})"
        elif self.data is not None:
            string += str(self.data)
        else:
            string += "."
        return string

    def to_string_tree(self) -> str:
        return self.to_string_node() + "[" + ", ".join(self.recurse(Tree.to_string_tree)) + "]"

    def __str__(self) -> str:
        return self.to_string_tree()

# TODO: BinTree 'wraps' around Tree and maps left and right to children 0 and 1
# class BinTree(Generic[T]):
#
#     @staticmethod
#     def from_nested_lists(lists: List[List]):
#         pass
#
#     @property
#     def left(self):
#         return self.tree.nodes
#         children(self.tree.)
