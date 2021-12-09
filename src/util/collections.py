from functools import reduce
from operator import add, mul
from typing import Iterable, List, Set


def flatten(collections: Iterable[Iterable]) -> List:
    return reduce(add, collections, [])


def union_sets(sets: Iterable[Set]) -> Set:
    return set(reduce(set.union, sets, set()))


def multiply(collection: Iterable[int]):
    return reduce(mul, collection, 1)


def range_incl(val_from: int, val_to: int) -> List[int]:
    if val_from == val_to:
        raise ValueError("No range possible with same val_from and val_to")
    elif val_to > val_from:
        return list(range(val_from, val_to + 1))
    else:
        return list(range(val_from, val_to - 1, -1))
