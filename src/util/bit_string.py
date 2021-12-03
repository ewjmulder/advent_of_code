from __future__ import annotations
from bitstring import BitStream
from dataclasses import dataclass
from typing import List


@dataclass
class BitString:
    bits: BitStream

    @classmethod
    def from_string(cls, string: str):
        return BitString(BitStream(string))

    @classmethod
    def from_bit_list(cls, bit_list: List[int]):
        return BitString(BitStream(bit_list))

    def __getitem__(self, i: int):
        return self.bits[i]

    def to_int(self) -> int:
        return self.bits.uint

    def flip_bits(self) -> BitString:
        copy = self.bits.copy()
        copy.invert()
        return BitString(copy)
