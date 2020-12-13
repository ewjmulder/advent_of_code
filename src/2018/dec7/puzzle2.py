input = open("input1", "r")
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

workers = 5
done_at = {}
queue = list(curr)
for second in range(0, 999999):
    to_dels = []
    for l, sec in done_at.items():
        if sec == second:
            to_dels.append(l)
            for t in graph[l]:
                r_graph[t].remove(l)
                if r_graph[t] == []:
                    queue.append(t)
    for to_del in to_dels:
        del done_at[to_del]
    if len(queue) == 0 and len(done_at) == 0:
        print("done!")
        break
    queue.sort()

    while len(queue) > 0 and len(done_at) < workers:
        select = queue[0]
        time = 60 + ord(select) - 64
        done_at[select] = second + time
        queue.remove(select)

print(second)
