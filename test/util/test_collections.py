import pytest

from src.util.collections import *


def test_flatten():
    assert flatten([]) == []
    assert flatten([[]]) == []
    assert flatten([[1], [2, 3], [], [4], [5, 6], []]) == [1, 2, 3, 4, 5, 6]
    assert flatten((range(1, 3), range(3, 5), range(5, 7))) == [1, 2, 3, 4, 5, 6]


def test_union_sets():
    assert union_sets(set()) == set()
    assert union_sets(set(set())) == set()

    assert union_sets([{1, 2}, {2, 3}, set(), {3, 4}, {4, 5}, set(), {5, 6}]) == {1, 2, 3, 4, 5, 6}


def test_multiply():
    assert multiply([]) == 0
    assert multiply([1]) == 1
    assert multiply([99]) == 99
    assert multiply([1, 2, 3, 4]) == 24


def test_range_incl():
    assert range_incl(1, 2) == [1, 2]
    assert range_incl(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert range_incl(5, 0) == [5, 4, 3, 2, 1, 0]
    assert range_incl(2, -2) == [2, 1, 0, -1, -2]

    with pytest.raises(ValueError):
        range_incl(1, 1)
