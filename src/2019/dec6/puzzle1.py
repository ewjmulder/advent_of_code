from src.util import *

print(sum(shortest_paths(parse_graph_from_file(INPUT, ")"), "COM")[1].values()))
