from src.util import *

lines = parse_string_list_from_file(INPUT)
rules = {}
row = 0
for row in range(0, len(lines)):
    line = lines[row]
    if line == "":
        break
    [field, f1, t1, f2, t2] = parse_regex_from_lines([line],
                                                     f"([a-z ]+)\\: {NUMBER}\\-{NUMBER} or {NUMBER}\\-{NUMBER}",
                                                     [str, int, int, int, int])[0]
    rules[field] = [(f1, t1), (f2, t2)]

row += 2
mine = parse_number_grid_from_lines([lines[row]], separator=",")[0]

row += 3
nearbys = parse_number_grid_from_lines(lines[row:], separator=",").rows


print(rules)
print(mine)
print(nearbys)

pos_order = {}
for field, [(f1, t1), (f2, t2)] in rules.items():
    pos_order[field] = []
    for i in range(0, len(mine)):
        pos_order[field].append((i + 1))

print(pos_order)

invalid_nearbys = []
for nearby in nearbys:
    for n in nearby:
        invalid = True
        for field, [(f1, t1), (f2, t2)] in rules.items():
            if f1 <= n <= t1 or f2 <= n <= t2:
                invalid = False
        if invalid:
            invalid_nearbys.append(nearby)

for invalid_nearby in invalid_nearbys:
    nearbys.remove(invalid_nearby)

for nearby in nearbys:
    for i in range(0, len(nearby)):
        n = nearby[i]
        for field, [(f1, t1), (f2, t2)] in rules.items():
            if f1 <= n <= t1 or f2 <= n <= t2:
                pass
            else:
                if (i + 1) in pos_order[field]:
                    pos_order[field].remove((i + 1))

print(pos_order)

while max([len(pos) for pos in pos_order.values()]) > 1:
    ones = [pos for pos in pos_order.values() if len(pos) == 1]
    ones = [o for one in ones for o in one]
    for pos in pos_order.values():
        if len(pos) > 1:
            for one in ones:
                if one in pos:
                    pos.remove(one)

print(pos_order)

rev_pos_order = {}
for pos, [num] in pos_order.items():
    rev_pos_order[num] = pos

print(rev_pos_order)

mul = 1
for i in range(0, len(mine)):
    match = rev_pos_order[i + 1]
    if match.startswith("departure"):
        mul *= mine[i]

print(mul)
