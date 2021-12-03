from __future__ import annotations
from typing import Union, List, Type, Optional
from dataclasses import dataclass
import re

from src.util.grid import Grid
from src.util.bit_string import BitString
from src.util.graph import Graph

_DEFAULT_SEPARATOR = " "

INPUT = "input"
SAMPLE = "sample"
SAMPLE2 = "sample2"

WORD = "([a-zA-Z]+)"
NUMBER = "([0-9]+)"
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

    def to_number_list(self) -> List[int]:
        return [int(line) for line in self.lines]

    def to_bitstring_list(self) -> List[BitString]:
        return list(map(BitString.from_string, self.lines))

    def to_character_grid(self) -> Grid[str]:
        return Grid[str]([[character for character in line] for line in self.lines])

    def to_number_grid(self, separator: Optional[str] = _DEFAULT_SEPARATOR) -> Grid[int]:
        def split_line(line: str) -> List[str]:
            if separator:
                return line.split(separator)
            else:
                return [char for char in line]

        return Grid[int]([[int(word.strip()) for word in split_line(line)] for line in self.lines])

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
            result.append(groups)
        return result

    def to_graph(self, separator: str) -> Graph:
        return Graph.from_edges([line.split(separator) for line in self.lines])




