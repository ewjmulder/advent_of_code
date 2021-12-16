from src.util import *

risks = Parser.from_file(INPUT).to_number_grid(separator="")
risk_graph = risks.to_directed_weighted_graph(include_diagonal=False)
shortest_path = risk_graph.calc_shortest_path(0, (risks.width * risks.height) - 1)

cost = 0
for n in shortest_path[1:]:
    c = Coordinate(int(n / risks.width), n % risks.width)
    cost += risks.get_value_by_coord(c)

print(cost)
