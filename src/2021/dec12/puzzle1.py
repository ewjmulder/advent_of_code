from src.util import *

# edges = Parser.from_file(SAMPLE).to_regex_match(f"{WORD}-{WORD}")
gr = Parser.from_file(INPUT).to_graph("-")


def visit(node, acc):
    ns = gr.wrapped_graph.neighbors(node)
    count = 0
    for n in ns:
        if n == "end":
            print(acc)
            count += 1
        elif n == "start":
            count += 0
        elif n == n.lower() and acc.count(n) == 0:
            count += visit(n, acc + [n])
        elif n != n.lower():
            count += visit(n, acc + [n])
        else:
            count += 0
    return count


print(visit("start", ["start"]))
