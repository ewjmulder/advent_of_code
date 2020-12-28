from collections import deque

trial = False
test = False
printing_cups = False
printing = False

input = "389125467"
if not test:
    input = "362981754"
cups = deque([int(char) for char in input])

if printing:
    print(cups)
    print("")

moves = 10000000
if not test:
    moves = 10000000
elif trial:
    moves = 100

current = cups[0]

fill = 1000000
if not test:
    fill = 1000000
elif trial:
    fill = 10
neighbors = {}
for i in range(0, 8):
    neighbors[cups[i]] = cups[i + 1]
neighbors[cups[8]] = cups[0]


if fill > 10:
    neighbors[cups[8]] = 10
    for i in range(10, fill + 1):
        neighbors[i] = i + 1
    neighbors[fill] = cups[0]

amount = len(neighbors)

print(amount)
if printing_cups:
    print(neighbors)

pct = int(moves / 100)
for m in range(0, moves):
    if m % pct == 0:
        print(f"{int(m/moves*100)}%")
    if printing_cups:
        print(neighbors)
    if printing:
        print("current:", current)
    n1 = neighbors[current]
    n2 = neighbors[n1]
    n3 = neighbors[n2]
    if printing:
        print(n1, n2, n3)
    neighbors[current] = neighbors[n3]
    dest = current - 1
    while dest in [n1, n2, n3] or dest < 1:
        if dest == 0:
            dest = amount
        else:
            dest -= 1
    old_neighbor_new_current = neighbors[dest]
    neighbors[dest] = n1
    neighbors[n3] = old_neighbor_new_current
    current = neighbors[current]
    if printing:
        print("new_current:", current)

print("")
star1 = neighbors[1]
star2 = neighbors[star1]
print(star1, star2)
print(star1 * star2)
