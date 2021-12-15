from pygraph.algorithms.minmax import shortest_path as shortest_paths, path as shortest_path
from pygraph.classes.digraph import digraph

from src.util import *

# risks = Parser.from_file(SAMPLE).to_number_grid(separator="")
# pos = risks.get_cell_by_coord(Coordinate(0, 0))
# paths = [([pos], pos.value)]
# while True:
#     paths.sort(key=lambda tup: tup[1] + abs(tup[0][-1].coord.x - risks.width) + abs(tup[0][-1].coord.y - risks.height))
#     best_p = paths[0]
#     del paths[0]
#     ns = risks.get_neighbor_cells(best_p[0][-1].coord, include_diagonal=False)
#     for n in ns:
#         if n == risks.rows[-1][-1]:
#             print("paths:", len(paths))
#             print(best_p[1] + n.value)
#             sys.exit(0)
#         elif n not in best_p[0]:
#             paths += [(best_p[0] + [n], best_p[1] + n.value)]
#         else:
#             pass

# def dfs(r: Grid[int], p: Coordinate, path: List[Cell]):
#     ns = r.get_neighbor_cells(p, include_diagonal=False)
#     paths = []
#     for n in ns:
#         if n == r.rows[-1][-1]:
#             paths.append(path + [n])
#         elif n not in path:
#             paths += dfs(r, n.coord, path + [n])
#         else:
#             pass
#     return paths


risks = Parser.from_file(INPUT).to_number_grid(separator="")


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
