import re

input = open("input1", "r")
lines = input.readlines()

line = 0
valids = 0

all_keys_list = ["ecl", "pid", "eyr", "hcl",
                 "byr", "iyr", "cid", "hgt"]
all_keys_list.sort()
but_one = ["ecl", "pid", "eyr", "hcl",
           "byr", "iyr", "hgt"]
but_one.sort()
while line < len(lines):
    valid = False
    all_keys = []
    all_kvs = {}
    while line < len(lines) and lines[line] != "\n":
        for kv in lines[line].split(" "):
            # print(kv)
            kv_split = kv.split(":")
            all_kvs[kv_split[0]] = kv_split[1].rstrip()
            # print(k)
            all_keys.append(kv_split[0])
        line += 1
    # print(all_keys)
    all_keys.sort()
    valid = all_keys == all_keys_list
    # print(valid)
    valid = valid or all_keys == but_one
    # print(valid)
    # print(all_kvs)
    if valid:
        try:
            byr = int(all_kvs["byr"])
            valid = valid and 1920 <= byr <= 2002

            iyr = int(all_kvs["iyr"])
            valid = valid and 2010 <= iyr <= 2020

            eyr = int(all_kvs["eyr"])
            valid = valid and 2020 <= eyr <= 2030

            hgt = all_kvs["hgt"]
            if hgt.endswith("cm"):
                hgt = int(hgt[:-2])
                valid = valid and 150 <= hgt <= 193
            elif hgt.endswith("in"):
                hgt = int(hgt[:-2])
                valid = valid and 59 <= hgt <= 76
            else:
                valid = False

            hcl = all_kvs["hcl"]
            valid = valid and re.search("#[a-f0-9]{6}", hcl) is not None

            ecl = all_kvs["ecl"]
            valid = valid and ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

            pid = all_kvs["pid"]
            valid = valid and len(pid) == 9 and re.search("[0-9]{9}", pid) is not None

        except Exception as e:
            # print(e)
            valid = False
        if valid:
            valids += 1
        # print(valid)
    line += 1

print(valids)
