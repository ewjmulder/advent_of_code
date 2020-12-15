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
        print(mask_str)
    else:
        match = re.match("mem\[([0-9)]+)\] = ([0-9]+)", line)
        addr = int(match.group(1))
        val = int(match.group(2))
        val_bits = BitArray(f"uint:36={val}")
        val_bits_str = val_bits.bin
        new_val = ""
        for i in range(0, 36):
            mask_i = mask_str[i]
            val_i = val_bits_str[i]
            if mask_i == "X":
                new_val += val_i
            else:
                new_val += mask_i
        mem[addr] = BitArray(f"bin={new_val}").uint
        # print(addr)
        # print(val)

print(sum(mem.values()))
