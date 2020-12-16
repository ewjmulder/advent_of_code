from src.util import *
from pygraph.classes.graph import graph
from pygraph.readwrite import dot
from pygraph.algorithms.minmax import shortest_path

orbit_data = parse_regex_from_file(SAMPLE, f"{WORD}\\){WORD}")
print(orbit_data)

g = graph()
for data in orbit_data:
    if not g.has_node(data[0]):
        g.add_node(data[0])
    if not g.has_node(data[1]):
        g.add_node(data[1])
for data in orbit_data:
    g.add_edge((data[0], data[1]))


print(shortest_path(g, "COM"))

#print(dot.write(g))
# dot -Tpng /tmp/dotty.txt -o /tmp/graph.png

# input = open("input1", "r")
# lines = input.readlines()
# lines = [l.rstrip() for l in lines]
#
# orbs = {}
# orbits = [l.split(")") for l in lines]
# for [a, b] in orbits:
#     if not orbs.get(a):
#         orbs[a] = []
#     orbs[a].append(b)
#
# def count(l, acc):
#     counter = 0
#     if orbs.get(l):
#         for i in orbs[l]:
#             counter += count(i, acc + 1)
#         counter += acc
#         return counter
#     else:
#         return acc
#
#
# print(count("COM", 0))
