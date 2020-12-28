from src.util import *
from collections import deque

cups = deque([int(char) for char in open(SAMPLE).readlines()[0]])

print(cups)
print("")

moves = 100
amount = len(cups)

current_i = 0
current_val = cups[0]
for m in range(0, moves):
    print(cups)
    print("current_i:", current_i)
    print("current_val:", current_val)
    cups.rotate(amount - 3 - (current_i + 1))
    n3 = cups.pop()
    n2 = cups.pop()
    n1 = cups.pop()
    ns = [n1, n2, n3]
    dest = current_val - 1
    while dest in ns or dest < 1:
        if dest < 1:
            dest = 9
        else:
            dest -= 1
    dest_i = cups.index(dest)
    print("dest_i:", dest_i)
    print("dest:", cups[dest_i])
    cups.insert(dest_i + 1, n3)
    cups.insert(dest_i + 1, n2)
    cups.insert(dest_i + 1, n1)
    current_i = cups.index(current_val) + 1
    if current_i > amount - 1:
        current_i = 0
    current_val = cups[current_i]
    print("")

print("")
print(cups)
print("")
index_1 = cups.index(1)
cups.rotate(-1 * (index_1 + 1))
print(cups)
print("")
cups.pop()
print("".join([str(n) for n in cups]))
