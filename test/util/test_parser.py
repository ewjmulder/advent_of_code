import pytest

from src.util.coordinate import Coordinate
from src.util.grid import Grid
from src.util.parser import Parser, WORD, NUMBER, ALFANUM


def test_from_file():
    assert Parser.from_file("test_parser_input").to_lines() == ["123", "456"]


def test_from_string():
    assert Parser.from_string("123\n456").to_lines() == ["123", "456"]


def test_from_lines():
    assert Parser.from_lines(["123", "456"]).to_lines() == ["123", "456"]


def test_to_string():
    assert Parser.from_string("123\n456").to_string() == "123\n456"


def test_to_lines():
    assert Parser.from_string("123\n456").to_lines() == ["123", "456"]


def test_to_sections():
    assert Parser.from_string("123\n\n456").to_sections() == ["123", "456"]


def test_to_word_lists():
    assert Parser.from_lines(["word1 word2", "word3 word4"]).to_word_lists() == \
           [["word1", "word2"], ["word3", "word4"]]
    assert Parser.from_lines(["word1, word2", "word3, word4"]).to_word_lists(separator=",") == \
           [["word1", "word2"], ["word3", "word4"]]


def test_to_number_lists():
    assert Parser.from_lines(["1 2", "3 4"]).to_number_lists() == [[1, 2], [3, 4]]
    assert Parser.from_lines(["1, 2", "3, 4"]).to_number_lists(separator=",") == [[1, 2], [3, 4]]


def test_to_number_list_from_single_line():
    assert Parser.from_lines(["1 2 3 4"]).to_number_list_from_single_line() == [1, 2, 3, 4]
    assert Parser.from_lines(["1, 2, 3, 4"]).to_number_list_from_single_line(separator=",") == [1, 2, 3, 4]


def test_to_number_list_from_multi_line():
    assert Parser.from_lines(["1", "2", "3", "4"]).to_number_list_from_multi_line() == [1, 2, 3, 4]


def test_to_coordinate_list():
    assert Parser.from_lines(["1 2", "3 4"]).to_coordinate_list() == \
           [Coordinate.from_point(1, 2), Coordinate.from_point(3, 4)]
    assert Parser.from_lines(["1, 2", "3, 4"]).to_coordinate_list(separator=",") == \
           [Coordinate.from_point(1, 2), Coordinate.from_point(3, 4)]


def test_to_bitstring_list():
    assert [bit_string.to_int() for bit_string in Parser.from_lines(["10101", "101"]).to_bitstring_list()] == [21, 5]


def test_to_character_grid():
    assert Parser.from_lines(["..#", "#.#"]).to_character_grid() == Grid.from_values([[".", ".", "#"], ["#", ".", "#"]])


def test_to_number_grid():
    assert Parser.from_lines(["123", "456"]).to_number_grid() == \
           Grid.from_values([[1, 2, 3], [4, 5, 6]])
    assert Parser.from_lines(["1 2 3", "4 5 6"]).to_number_grid(separator=None) == \
           Grid.from_values([[1, 2, 3], [4, 5, 6]])
    assert Parser.from_lines(["1, 2, 3", "4, 5, 6"]).to_number_grid(separator=",") == \
           Grid.from_values([[1, 2, 3], [4, 5, 6]])


def test_to_regex_match():
    assert Parser.from_lines(["from here to there", "from anywhere to somewhere"]).to_regex_match(
        f"from {WORD} to {WORD}") == [["here", "there"], ["anywhere", "somewhere"]]
    assert Parser.from_lines(["from here to 99", "from anywhere to 42"]).to_regex_match(
        f"from {WORD} to {NUMBER}", [str, int]) == [["here", 99], ["anywhere", 42]]
    assert Parser.from_lines(["from 1 to 99", "from 0 to 42"]).to_regex_match(
        f"from {NUMBER} to {NUMBER}", int) == [[1, 99], [0, 42]]
    assert Parser.from_lines(["alfanum 4lf4n1m", "alfanum 0a1b2c"]).to_regex_match(
        f"alfanum {ALFANUM}") == [["4lf4n1m"], ["0a1b2c"]]

    with pytest.raises(ValueError):
        Parser.from_lines(["some line"]).to_regex_match("not that line")

    with pytest.raises(ValueError):
        Parser.from_lines(["abc"]).to_regex_match(NUMBER)

# TODO: test if graph is refactored
# def test_to_string_graph():
#     pass
