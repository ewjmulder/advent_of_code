input = open("sample1", "r")
lines = input.readlines()
lines = [line.rstrip() for line in lines]

import re

graph = {}
r_graph = {}
all_f = set()
all_t = set()
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    graph[c] = []
    r_graph[c] = []
for line in lines:
    match = re.match("Step ([A-Z]) must be finished before step ([A-Z]) can begin\.", line)
    f = match.groups()[0]
    t = match.groups()[1]
    graph[f].append(t)
    r_graph[t].append(f)
    all_f.add(f)
    all_t.add(t)

print(graph)


curr = all_f - all_t

curr = list(curr)

order = ""
while len(curr) > 0:
    curr.sort()
    print(curr)
    select = curr[0]
    print(select)
    order += select
    for t in graph[select]:
        r_graph[t].remove(select)
        if r_graph[t] == []:
            curr.append(t)
    curr.remove(select)

print(order)
