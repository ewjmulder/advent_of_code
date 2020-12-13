import re

input = open("input1", "r")
lines = input.readlines()

graph = {}
all_colors = set()
for line in lines:
    line = line.rstrip()
    # print(line)
    match = re.fullmatch("([a-z ]+) bags? contain ([0-9]+) ([a-z ]*) bags?(, ([0-9]+) ([a-z ]+) bags?)?(, ([0-9]+) ([a-z ]+) bags?)?(, ([0-9]+) ([a-z ]+) bags?)?(, ([0-9]+) ([a-z ]+) bags?)?(, ([0-9]+) ([a-z ]+) bags?)?\." , line)
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
                    to.append((group, n))
                    all_colors.add(group)
            elif group and len(group) < 5:
                n = int(group)
        graph[fc] = to

print(graph)
print(all_colors)
# print(len(all_colors))


def calc(color):
    curr = set()
    curr.add(color)
    if color in graph:
        count = 1
        for cc in graph[color]:
            curr.add(cc[0])
            # print(color, " => ", cc[1], " * ", calc(cc[0]))
            count += cc[1] * calc(cc[0])
        return count
    else:
        # print(color, " => 1")
        return 1


search = "shiny gold"
print(calc(search) - 1)
