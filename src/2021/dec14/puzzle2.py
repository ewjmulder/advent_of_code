from src.util import *
from collections import Counter

sections = Parser.from_file(INPUT).to_sections()

string = sections[0].strip()
orig_string = string
# print(string)
rewrites = {key: value for [key, value] in Parser.from_string(sections[1]).to_regex_match(f"{WORD} -> {WORD}")}
# print(rewrites)
pair_rewrites = {key: (key[0] + value, value + key[1]) for [key, value] in Parser.from_string(sections[1]).to_regex_match(f"{WORD} -> {WORD}")}
# print(pair_rewrites)

pairs = {}
for key in rewrites.keys():
    pairs[key] = 0
for i in range(len(string) - 1):
    pairs[string[i:i+2]] += 1
# print(pairs)
for step in range(40):
    new_pairs = {}
    for key in rewrites.keys():
        new_pairs[key] = 0
    for pair, amount in pairs.items():
        new_ps = pair_rewrites[pair]
        for new_p in new_ps:
            new_pairs[new_p] += amount
    pairs = new_pairs
    print(step + 1, pairs)

# print(pairs)
counter = {}
l = list(pairs.items())
for pair, amount in l:
    if pair[0] not in counter:
        counter[pair[0]] = 0
    counter[pair[0]] += amount

counter[orig_string[-1]] += 1

# if l[-1][0][1] not in counter:
#     counter[l[-1][0][1]] = 0
# counter[l[-1][0][1]] += l[-1][1]


print(counter)

max_val = max(counter.values())
print(max_val)
min_val = min(counter.values())
print(min_val)
print(max_val - min_val)

# Template:     NNCB
# After step 1: NCNBCHB
# After step 2: NBCCNBBBCBHCB
# After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
# After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
