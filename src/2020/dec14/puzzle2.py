from src.util.parser import *
from bitstring import BitArray

data = parse_as_string_list(INPUT)

mem = {}

mask_str = ""
for line in data:
    if line.startswith("mask"):
        mask_str = line[7:]
        # mask_str = mask_str.replace()
        # mask = BitArray("bin={mask_str}")
        # print(mask_str)
    else:
        match = re.match("mem\[([0-9)]+)\] = ([0-9]+)", line)
        addr = int(match.group(1))
        val = int(match.group(2))
        addr_bits = BitArray(f"uint:36={addr}")
        addr_bits_str = addr_bits.bin
        def find_addrs(bit_string, acc, i):
            while True:
                if i >= len(bit_string):
                    return [acc]
                mask_i = bit_string[i]
                addr_i = addr_bits_str[i]
                # print(bit_string, acc, i, mask_i, addr_i)
                if mask_i == "X":
                    # print("X found")
                    return find_addrs(bit_string, acc + "0", i + 1) + find_addrs(bit_string, acc + "1", i + 1)
                elif mask_i == "1":
                    acc += "1"
                else:
                    acc += addr_i
                i += 1
        addrs = find_addrs(mask_str, "", 0)
        for add in addrs:
            add_int = BitArray(f"bin={add}").uint
            # print(f"writing {val} in {add_int}")
            mem[add] = val
        # print(addr)
        # print(val)

print(sum(mem.values()))
