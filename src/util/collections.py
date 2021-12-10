from functools import reduce
from operator import mul
from typing import Iterable, List, Set


def flatten(collections: Iterable[Iterable]) -> List:
    return reduce(lambda iter1, iter2: list(iter1) + list(iter2), collections, [])


def union_sets(sets: Iterable[Set]) -> Set:
    return set(reduce(set.union, sets, set()))


def multiply(collection: Iterable[int]):
    list_collection = list(collection)
    if len(list(list_collection)) == 0:
        return 0
    else:
        return reduce(mul, list_collection, 1)


def range_incl(val_from: int, val_to: int) -> List[int]:
    if val_from == val_to:
        raise ValueError("No range possible with same val_from and val_to")
    elif val_to > val_from:
        return list(range(val_from, val_to + 1))
    else:
        return list(range(val_from, val_to - 1, -1))
