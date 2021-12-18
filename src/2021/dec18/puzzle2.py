from __future__ import annotations
from typing import Tuple, Optional, List
from src.util import *
from dataclasses import dataclass
import itertools


snail_strings = Parser.from_file(INPUT).to_lines()


def parse_node(input: str) -> Tuple[Node, str]:
    if input[0] == '[':
        (left, input_rest) = parse_node(input[1:])
        if input_rest[0] != ',':
            print("FAILED! No comma separator")
        (right, input_rest) = parse_node(input_rest[1:])
        if input_rest[0] != ']':
            print("FAILED! No matching close bracket")
        parent = Node(left, right, None)
        left.parent = parent
        right.parent = parent
        return parent, input_rest[1:]
    else:
        number = int(input[0])
        return Node(None, None, number), input[1:]


def add_snails(node1: Node, node2: Node) -> Node:
    parent = Node(node1, node2, None)
    node1.parent = parent
    node2.parent = parent
    return parent


@dataclass
class Node:
    left: Optional[Node] = None
    right: Optional[Node] = None
    data: Optional[int] = None
    parent: Optional[Node] = None

    def __str__(self):
        if self.data is not None:
            return str(self.data)
        else:
            return f"[{self.left.__str__()},{self.right.__str__()}]"

    def get_level(self, level: int, cur: int) -> Optional[Node]:
        if cur == level and self.data is None:
            return self
        else:
            if self.left is not None:
                ret = self.left.get_level(level, cur + 1)
                if ret is not None:
                    return ret
            if self.right is not None:
                ret = self.right.get_level(level, cur + 1)
                if ret is not None:
                    return ret
            return None

    def flatten(self) -> List[Node]:
        flatten_left = []
        flatten_right = []
        if self.left is not None:
            flatten_left = self.left.flatten()
        if self.right is not None:
            flatten_right = self.right.flatten()
        return flatten_left + ([] if self.data is None else [self]) + flatten_right

    def remove(self, child: Node):
        if self.left is child:
            self.parent.replace(self, self.right)
        if self.right is child:
            self.parent.replace(self, self.left)

    def replace(self, child_from, child_to):
        if self.left is child_from:
            self.left = child_to
        if self.right is child_from:
            self.right = child_to
        child_to.parent = self

    def mag(self):
        mag_left = 0
        mag_right = 0
        if self.left is not None:
            mag_left = self.left.mag()
        if self.right is not None:
            mag_right = self.right.mag()
        return 3 * mag_left + (0 if self.data is None else self.data) + 2 * mag_right

    def copy(self):
        copy_left = None
        copy_right = None
        if self.left is not None:
            copy_left = self.left.copy()
        if self.right is not None:
            copy_right = self.right.copy()
        copy = Node(copy_left, copy_right, self.data)
        if self.left is not None:
            copy_left.parent = copy
        if self.right is not None:
            copy_right.parent = copy
        return copy

def get_to_split(tree: Node) -> Optional[Node]:
    flat = tree.flatten()
    for i in range(len(flat)):
        if flat[i].data is not None and flat[i].data > 9:
            return flat[i]
    return None


def get_left_neighbor(tree: Node, node: Node) -> Optional[Node]:
    flat = tree.flatten()
    for i in range(len(flat)):
        if flat[i] is node:
            if i == 0:
                return None
            else:
                return flat[i - 1]


def get_right_neighbor(tree: Node, node: Node) -> Optional[Node]:
    flat = tree.flatten()
    for i in range(len(flat)):
        if flat[i] is node:
            if i == len(flat) - 1:
                return None
            else:
                return flat[i + 1]


def reduce(snail: Node) -> Node:
    # print("snail:", snail)
    to_explode = snail.get_level(4, 0)
    # print("to_explode:", to_explode)
    if to_explode is not None:
        left_neighbor = get_left_neighbor(snail, to_explode.left)
        # print("left_neighbor:", left_neighbor)
        if left_neighbor is not None:
            left_neighbor.data += to_explode.left.data
        right_neighbor = get_right_neighbor(snail, to_explode.right)
        # print("right_neighbor:", right_neighbor)
        if right_neighbor is not None:
            right_neighbor.data += to_explode.right.data
        to_explode.parent.replace(to_explode, Node(None, None, 0))
        reduce(snail)
    to_split = get_to_split(snail)
    # print("to_split:", to_split)
    if to_split is not None:
        split = to_split
        # print("split:", split)
        nr = split.data
        split.data = None
        split.left = Node(None, None, int(nr / 2))
        split.left.parent = split
        split.right = Node(None, None, int((nr + 1) / 2))
        split.right.parent = split
        reduce(snail)
    return snail


stack = []
for snail_string in snail_strings:
    # print("snail string to parse:", snail_string)
    snail = parse_node(snail_string)[0]
    # print("snail parsed:", snail)
    stack.append(snail)

largest = 0
for sn1i, sn2i in itertools.combinations(stack, 2):
    sn1 = sn1i.copy()
    sn2 = sn2i.copy()
    added = add_snails(sn1, sn2)
    mag = reduce(added).mag()
    if mag > largest:
        largest = mag

    sn1 = sn1i.copy()
    sn2 = sn2i.copy()
    added = add_snails(sn2, sn1)
    mag = reduce(added).mag()
    if mag > largest:
        largest = mag


print(largest)
