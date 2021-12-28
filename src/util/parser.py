from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Union, List, Type, Optional

from src.util.bit_string import BitString
from src.util.coordinate import Coordinate
from src.util.graph import Graph
from src.util.grid import Grid

# A Separator of None means: any whitespace
_DEFAULT_SEPARATOR = None

INPUT = "input"
SAMPLE = "sample"
SAMPLE_2 = "sample2"

WORD = "([a-zA-Z]+)"
NUMBER = "(-?[0-9]+)"
ALFANUM = "([a-zA-Z0-9]+)"


@dataclass
class Parser:
    lines: List[str]

    @classmethod
    def from_file(cls, file: str) -> Parser:
        return Parser.from_string(open(file).read())

    @classmethod
    def from_string(cls, string: str) -> Parser:
        return Parser.from_lines(string.splitlines(keepends=False))

    @classmethod
    def from_lines(cls, lines: List[str]) -> Parser:
        return Parser(lines)

    def to_string(self) -> str:
        return "\n".join(self.lines)

    def to_lines(self) -> List[str]:
        return self.lines

    def to_sections(self) -> List[str]:
        return self.to_string().split("\n\n")

    def to_word_lists(self, separator: str = _DEFAULT_SEPARATOR) -> List[List[str]]:
        return [[word.strip() for word in line.split(separator)] for line in self.lines]

    def to_number_lists(self, separator: str = _DEFAULT_SEPARATOR) -> List[List[int]]:
        return [[int(word.strip()) for word in words] for words in self.to_word_lists(separator)]

    def to_number_list_from_single_line(self, separator: str = _DEFAULT_SEPARATOR) -> List[int]:
        return [int(word.strip()) for word in self.lines[0].split(separator)]

    def to_number_list_from_multi_line(self) -> List[int]:
        return [int(line) for line in self.lines]

    def to_coordinate_list(self, separator: str = _DEFAULT_SEPARATOR) -> List[Coordinate]:
        return [Coordinate.from_point(numbers[0], numbers[1]) for numbers in self.to_number_lists(separator)]

    def to_bitstring_list(self) -> List[BitString]:
        return list(map(BitString.from_string, self.lines))

    def to_character_grid(self) -> Grid[str]:
        return Grid.from_values([[character for character in line] for line in self.lines])

    def to_number_grid(self, separator: Optional[str] = "") -> Grid[int]:
        def split_line(line: str) -> List[str]:
            if separator == "":
                # Empty string means: no separator, take character by character
                return [char for char in line]
            else:
                # None means: default of split, which is any whitespace
                # Any other value means: use this specific separator to split.
                return line.split(separator)

        return Grid.from_values([[int(word.strip()) for word in split_line(line)] for line in self.lines])

    def to_regex_match(self, pattern: str, type_or_types: Union[Type, List[Type]] = None) -> List[List]:
        result = []
        regex = re.compile(pattern)
        for line in self.lines:
            match = regex.match(line)
            if not match:
                raise ValueError(f"Line: '{line}' did not match regex pattern: '{pattern}'")
            groups = [str(group) for group in match.groups()]
            if type_or_types:
                if type(type_or_types) == type:
                    groups = [type_or_types(group) for group in groups]
                elif type(type_or_types) == list:
                    groups = [type_converter(group) for type_converter, group in zip(type_or_types, groups)]
                else:
                    raise ValueError("type_or_types should be a type or a list of types")
            result.append(groups)
        return result

    def to_string_graph(self, separator: str = _DEFAULT_SEPARATOR) -> Graph[str]:
        return Graph.from_edges(self.to_word_lists(separator))

    def to_number_graph(self, separator: str = _DEFAULT_SEPARATOR) -> Graph[int]:
        return Graph.from_edges(self.to_number_lists(separator))
