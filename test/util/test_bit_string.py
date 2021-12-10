import pytest

from src.util.bit_string import BitString


def test_from_string():
    assert BitString.from_string("1101").to_string() == "1101"

    assert BitString.from_string("1,1,0,1", separator=",").to_string() == "1101"
    assert BitString.from_string(" 1 |  1  | 0 |  1 ", separator="|").to_string() == "1101"

    with pytest.raises(ValueError):
        BitString.from_string("")


def test_from_bit_list():
    assert BitString.from_bit_list([1]).to_string() == "1"
    assert BitString.from_bit_list([1, 1, 0, 1]).to_string() == "1101"

    with pytest.raises(ValueError):
        BitString.from_bit_list([])


def test_get_item():
    bit_string = BitString.from_string("1101")
    assert bit_string[0] == 1
    assert bit_string[1] == 1
    assert bit_string[2] == 0
    assert bit_string[1] == 1


def test_to_int():
    assert BitString.from_string("0").to_int() == 0
    assert BitString.from_string("1101").to_int() == 13


def test_flip_bits():
    assert BitString.from_string("1101").flip_bits().to_string() == "0010"
