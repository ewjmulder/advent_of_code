from .parser import Parser, SAMPLE, SAMPLE_2, INPUT, WORD, NUMBER, ALFANUM
from .value_reference import ValueReference
from .coordinate import Coordinate
from .grid import Grid
from .graph import Graph
from .bit_string import BitString

from typing import List


def flatten(lists: List[List]) -> List:
    return [item for sublist in lists for item in sublist]


def range_incl(val_from: int, val_to: int) -> List[int]:
    if val_from == val_to:
        raise ValueError("No range possible with same val_from and val_to")
    elif val_to > val_from:
        return list(range(val_from, val_to + 1))
    else:
        return list(range(val_from, val_to - 1, -1))
