from typing import Union, List, Type
from src.util.grid import Grid
import re

_DEFAULT_SEPARATOR = " "

INPUT = "input"
SAMPLE = "sample"
SAMPLE2 = "sample2"

WORD = "([a-zA-Z]+)"
NUMBER = "([0-9]+)"
ALFANUM = "([a-zA-Z0-9]+)"


def parse_string_list_from_file(file: str) -> List[str]:
    return read_file_as_lines(file)


def parse_lines_from_string(string: str) -> List[str]:
    return string.splitlines(keepends=False)


def parse_character_grid_from_file(file: str) -> Grid[str]:
    return parse_character_grid_from_lines(read_file_as_lines(file))


def parse_character_grid_from_string(string: str) -> Grid[str]:
    return parse_character_grid_from_lines(parse_lines_from_string(string))


def parse_character_grid_from_lines(lines: List[str]) -> Grid[str]:
    return Grid[str]([[character for character in line] for line in lines])


def parse_number_list_from_file(file: str) -> List[int]:
    return parse_number_list_from_lines(read_file_as_lines(file))


def parse_number_list_from_string(string: str) -> List[int]:
    return parse_number_list_from_lines(parse_lines_from_string(string))


def parse_number_list_from_lines(lines: List[str]) -> List[int]:
    return [int(line) for line in lines]


def parse_number_grid_from_file(file: str, separator: str = _DEFAULT_SEPARATOR) -> Grid[int]:
    return parse_number_grid_from_lines(read_file_as_lines(file), separator)


def parse_number_grid_from_string(string: str, separator: str = _DEFAULT_SEPARATOR) -> Grid[int]:
    return parse_number_grid_from_lines(parse_lines_from_string(string), separator)


def parse_number_grid_from_lines(lines: List[str], separator: str = _DEFAULT_SEPARATOR) -> Grid[int]:
    return Grid[int]([[int(word.strip()) for word in line.split(separator)] for line in lines])


def parse_regex_from_file(file: str, pattern: str, type_or_types: Union[Type, List[Type]] = None) -> List[List]:
    return parse_regex_from_lines(read_file_as_lines(file), pattern, type_or_types)


def parse_regex_from_string(string: str, pattern: str, type_or_types: Union[Type, List[Type]] = None) -> List[List]:
    return parse_regex_from_lines(parse_lines_from_string(string), pattern, type_or_types)


def parse_regex_from_lines(lines: List[str], pattern: str, type_or_types: Union[Type, List[Type]] = None) -> List[List]:
    result = []
    regex = re.compile(pattern)
    for line in lines:
        match = regex.match(line)
        if not match:
            raise ValueError(f"Line: '{line}' did not match regex pattern: '{pattern}'")
        groups = [str(group) for group in match.groups()]
        if type_or_types:
            if type(type_or_types) == type:
                groups = [type_or_types(group) for group in groups]
            elif type(type_or_types) == list:
                groups = [type_converter(group) for type_converter, group in zip(type_or_types, groups)]
        result.append(groups)
    return result


def read_file_as_lines(file: str) -> List[str]:
    return parse_lines_from_string(read_file_as_string(file))


def read_file_as_string(file: str) -> str:
    return open(file).read()
