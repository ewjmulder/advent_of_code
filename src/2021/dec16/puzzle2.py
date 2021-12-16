from typing import List

from src.util import *
from src.util.collections import multiply


def parse_packet(string: str, stop_mode: str, stop_value: int, bits_parsed: int, acc: List[int]) -> (int, List[int]):
    print("")
    if len(string) == 0 or string == len(string) * "0":
        return bits_parsed, acc
    if stop_mode == "bits" and stop_value == bits_parsed:
        return bits_parsed, acc
    if stop_mode == "amount" and stop_value == len(acc):
        return bits_parsed, acc
    bit_string = BitString.from_string(string)
    print(bit_string.to_string())
    version = BitString.from_string(bit_string.to_string()[0:3]).to_int()
    print("version:", version)
    type_id = BitString.from_string(bit_string.to_string()[3:6]).to_int()
    print("type_id:", type_id)
    if type_id == 4:
        # Literal
        print("Literal")
        more = True
        i = 6
        total_number_bits = ""
        while more:
            nr = BitString.from_string(bit_string.to_string()[i:i + 1]).to_int()
            print("next:", nr)
            if nr == 0:
                # Last one
                more = False
            number_bits = bit_string.to_string()[i + 1:i + 5]
            total_number_bits += number_bits
            # print("number:", BitString.from_string(number_bits).to_int())
            i += 5
        total_number = BitString.from_string(total_number_bits).to_int()
        print("total number:", total_number)
        return parse_packet(bit_string.to_string()[i:], stop_mode, stop_value, bits_parsed + i, acc + [total_number])
    else:
        # Operator
        print("Operator")
        length_type_id = BitString.from_string(bit_string.to_string()[6:7]).to_int()
        print("length_type_id:", length_type_id)
        if length_type_id == 0:
            sub_packets_length = BitString.from_string(bit_string.to_string()[7:22]).to_int()
            print("sub_packets_length:", sub_packets_length)
            bits_parsed_sub, acc_sub = parse_packet(bit_string.to_string()[22:], stop_mode="bits",
                                                    stop_value=sub_packets_length, bits_parsed=0, acc=[])
            result = calc(type_id, acc_sub)
            return parse_packet(bit_string.to_string()[22 + bits_parsed_sub:], stop_mode, stop_value,
                                bits_parsed + bits_parsed_sub + 22, acc + [result])
        else:
            number_of_sub_packets = BitString.from_string(bit_string.to_string()[7:18]).to_int()
            print("number_of_sub_packets:", number_of_sub_packets)
            bits_parsed_sub, acc_sub = parse_packet(bit_string.to_string()[18:], stop_mode="amount",
                                                    stop_value=number_of_sub_packets, bits_parsed=0, acc=[])
            result = calc(type_id, acc_sub)
            return parse_packet(bit_string.to_string()[18 + bits_parsed_sub:], stop_mode, stop_value,
                                bits_parsed + bits_parsed_sub + 18, acc + [result])


def calc(type_id, acc):
    if type_id == 0:
        return sum(acc)
    if type_id == 1:
        return multiply(acc)
    if type_id == 2:
        return min(acc)
    if type_id == 3:
        return max(acc)
    if type_id == 5:
        return 1 if acc[0] > acc[1] else 0
    if type_id == 6:
        return 1 if acc[0] < acc[1] else 0
    if type_id == 7:
        return 1 if acc[0] == acc[1] else 0


hex_lines = Parser.from_file(INPUT).to_lines()
bit_string = BitString.from_hex_string(hex_lines[0]).to_string()
bits_parsed, acc = parse_packet(bit_string, stop_mode="bits",
                                stop_value=len(bit_string), bits_parsed=0, acc=[])

print(acc)
