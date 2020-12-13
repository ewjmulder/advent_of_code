import re

input = open("input1", "r")
lines = input.readlines()

graph = {}
all_colors = set()
for line in lines:
    line = line.rstrip()
    # print(line)
    match = re.fullmatch("([a-z ]+) bags? contain [0-9]+ ([a-z ]*) bags?(, [0-9]+ ([a-z ]+) bags?)?(, [0-9]+ ([a-z ]+) bags?)?(, [0-9]+ ([a-z ]+) bags?)?(, [0-9]+ ([a-z ]+) bags?)?(, [0-9]+ ([a-z ]+) bags?)?\." , line)
    # print(match)
    if match:
        first = False
        fc = ""
        to = []
        for group in match.groups():
            if group and group.count(" ") == 1:
                if not first:
                    fc = group
                    all_colors.add(group)
                    first = True
                else:
                    to.append(group)
                    all_colors.add(group)
        graph[fc] = to

print(graph)
print(all_colors)
# print(len(all_colors))

search = "shiny gold"
amount = 0
for color in all_colors:
    # print(color)
    reach = set()
    curr = set()
    curr.add(color)
    if color == search:
        continue
    while len(curr) > 0:
        cop = curr.copy()
        curr = set()
        for c in cop:
            if c in graph:
                for cc in graph[c]:
                    reach.add(cc)
                    curr.add(cc)
    if search in reach:
        # print("YES", color, "=>", reach)
        amount += 1
    # else:
        # print("NO", color, "=>", reach)


print(amount)
