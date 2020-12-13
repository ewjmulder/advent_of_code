from typing import Union, List, Tuple, Type
import re

INPUT = "input"
SAMPLE = "sample"
SAMPLE_2 = "sample2"


def parse_as_string_list(file: str) -> List[str]:
    return _read_lines(file)


def parse_as_character_grid(file: str) -> List[List[str]]:
    return [list(line) for line in _read_lines(file)]


def parse_as_number_list(file: str) -> List[int]:
    return [int(line) for line in _read_lines(file)]


def parse_as_number_grid(file: str, separator: str = " ") -> List[List[int]]:
    return [[int(word) for word in line.split(separator)] for line in _read_lines(file)]


def parse_as_regex(file: str, pattern: str, type_or_types: Union[Type, List[Type]] = None) -> List[List]:
    result = []
    regex = re.compile(pattern)
    for line in _read_lines(file):
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


def _read_lines(file: str) -> List[str]:
    return [line.rstrip() for line in open(file).readlines()]
