from src.util import *


def parse_packet(string: str) -> int:
    print("")
    if len(string) == 0 or string == len(string) * "0":
        return 0
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
        while more:
            nr = BitString.from_string(bit_string.to_string()[i:i + 1]).to_int()
            print("next:", nr)
            if nr == 0:
                # Last one
                more = False
            number = BitString.from_string(bit_string.to_string()[i + 1:i + 5]).to_int()
            print("number:", number)
            i += 5
        return number
    else:
        # Operator
        print("Operator")
        length_type_id = BitString.from_string(bit_string.to_string()[6:7]).to_int()
        print("length_type_id:", length_type_id)
        if length_type_id == 0:
            length = BitString.from_string(bit_string.to_string()[7:22]).to_int()
            print("length:", length)
            return version + parse_packet(bit_string.to_string()[22:])
        else:
            length = BitString.from_string(bit_string.to_string()[7:18]).to_int()
            print("length:", length)
            return version + parse_packet(bit_string.to_string()[18:])


hex_lines = Parser.from_file(INPUT).to_lines()
total_versions = parse_packet(BitString.from_hex_string(hex_lines[0]).to_string())
print("total:", total_versions)
