from __future__ import annotations

from dataclasses import dataclass
from typing import List

from bitstring import BitStream


@dataclass
class BitString:
    bits: BitStream

    @classmethod
    def from_string(cls, string: str, separator=None):
        if len(string) == 0:
            raise ValueError("Input string must not be empty")
        if separator:
            return BitString(BitStream([int(char.strip()) for char in string.split(separator)]))
        else:
            return BitString(BitStream(bin=string))

    @classmethod
    def from_bit_list(cls, bit_list: List[int]):
        if len(bit_list) == 0:
            raise ValueError("Input bit list must not be empty")
        return BitString(BitStream(bit_list))

    def __getitem__(self, i: int):
        return self.bits[i]

    def to_int(self) -> int:
        return self.bits.uint

    def to_string(self) -> str:
        return self.bits.bin

    def flip_bits(self) -> BitString:
        copy = self.bits.copy()
        copy.invert()
        return BitString(copy)
