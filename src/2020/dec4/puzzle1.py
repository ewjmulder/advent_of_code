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
    while line < len(lines) and lines[line] != "\n":
        for kv in lines[line].split(" "):
            # print(kv)
            k = kv.split(":")[0]
            # print(k)
            all_keys.append(k)
        line += 1
    # print(all_keys)
    all_keys.sort()
    valid = all_keys == all_keys_list
    # print(valid)
    valid = valid or all_keys == but_one
    # print(valid)
    if valid:
        valids += 1
    line += 1

print(valids)
