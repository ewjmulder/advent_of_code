from src.util import *
from collections import Counter

sections = Parser.from_file(SAMPLE).to_sections()

string = sections[0].strip()
print(string)
rewrites = {key: value for [key, value] in Parser.from_string(sections[1]).to_regex_match(f"{WORD} -> {WORD}")}
print(rewrites)

for step in range(10):
    i = 0
    inserts = []
    while True:
        chars = string[i:i+2]
        char = rewrites[chars]
        inserts.append(char)
        # print(char)
        i += 1
        if i >= len(string) - 1:
            break
    j = len(string) - 1
    while True:
        string = string[:j] + inserts[-1] + string[j:]
        del inserts[-1]
        j -= 1
        if j == 0:
            break
    print(string)
    c = Counter(string)
    print(c)

c = Counter(string)
print(max(c.values()) - min(c.values()))