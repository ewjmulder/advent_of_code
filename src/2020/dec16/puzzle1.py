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

invalids = []
for nearby in nearbys:
    for n in nearby:
        invalid = True
        for field, [(f1, t1), (f2, t2)] in rules.items():
            if f1 <= n <= t1 or f2 <= n <= t2:
                invalid = False
        if invalid:
            invalids.append(n)

print(sum(invalids))

