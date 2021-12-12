from collections import Counter

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
        elif n == n.lower():
            c = Counter(acc)
            ok = True
            # print(acc)
            # print(c)
            low = 0
            if c.get(n) == 2:
                ok = False
            elif c.get(n) == 0:
                ok = True
            elif c.get(n) == 1:
                low = 0
                for i in c.items():
                    if i[0] == i[0].lower():
                        if i[1] == 2:
                            ok = False
                            break
            if low <= 1 and ok:
                count += visit(n, acc + [n])
        elif n != n.lower():
            count += visit(n, acc + [n])
        else:
            count += 0
    return count


print(visit("start", ["start"]))
