import sys

from pygraph.algorithms.minmax import shortest_path as shortest_paths, path as shortest_path
from pygraph.classes.digraph import digraph

from src.util import *

sys.setrecursionlimit(2000)
risks = Parser.from_file(INPUT).to_number_grid(separator="")

risk_map = {}
cur = risks
for i in range(0, 9):
    risk_map[i] = cur
    cur = cur.map_values_by_function(lambda value: 1 if value == 9 else value + 1)

rows = []
for r in range(5 * risks.height):
    min_r = int(r / risks.height)
    # print(r, min_r)
    rr = r % risks.height
    new_row = []
    for rrr in range(min_r, min_r + 5):
        new_row += [c.value for c in risk_map[rrr].rows[rr]]
    rows.append(new_row)

risks = Grid.from_values(rows)


def val(co: Coordinate):
    global risks
    return co.row * risks.width + co.column


g = digraph()
for c in risks.get_all_coords():
    g.add_node(val(c))

for c in risks.get_all_coords():
    for n in risks.get_neighbor_cells(c, include_diagonal=False):
        # if n.coord.x >= c.x and n.coord.y >= c.y:
        g.add_edge((val(c), val(n.coord)), wt=n.value)

g.add_node(-1)
g.add_edge((-1, 0), wt=risks.get_value_by_index(0, 0))

g.add_node(9999999999)
g.add_edge((val(risks.rows[-1][-1].coord), 9999999999), wt=0)

shortest = list(reversed(shortest_path(shortest_paths(g, -1)[0], 9999999999)))
print(shortest)

cost = 0
for n in shortest[2:-1]:
    c = Coordinate(int(n / risks.width), n % risks.width)
    cost += risks.get_value_by_coord(c)

print(cost)
