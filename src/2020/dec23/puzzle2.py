from collections import deque

trial = False
test = True
printing_cups = False
printing = False

input = "389125467"
if not test:
    input = "362981754"
cups = deque([int(char) for char in input])

if printing:
    print(cups)
    print("")
if not test:
    for i in range(10, 1000001):
        cups.append(i)
elif not trial:
    for i in range(10, 1000001):
        cups.append(i)

moves = 10000
if not test:
    moves = 10000000
elif trial:
    moves = 100
amount = len(cups)

current_i = 0
current_val = cups[0]
pct = int(moves / 100)
for m in range(0, moves):
    if m % pct == 0:
        print(f"{int(m/moves*100)}%")
    if printing_cups:
        print(m, cups)
    if printing:
        print("current_i:", current_i)
        print("current_val:", current_val)
    rot_amount = amount - 3 - (current_i + 1)
    cups.rotate(rot_amount - 1)
    current_i = (current_i + rot_amount) % amount
    new_current_val = cups.pop()
    ns = [cups.pop(), cups.pop(), cups.pop()]
    cups.append(new_current_val)
    cups.rotate(1)
    dest = current_val - 1
    while dest in ns or dest < 1:
        if dest < 1:
            dest = amount
        else:
            dest -= 1
    dest_i = cups.index(dest)
    if printing:
        print("dest_i:", dest_i)
        print("dest:", cups[dest_i])
    rot_amount = -1 * (dest_i + 1)
    cups.rotate(rot_amount)
    current_i = (current_i + rot_amount) % amount
    cups.extendleft(ns)
    current_i = (current_i + 4) % amount
    current_val = new_current_val
    # print("")

if printing:
    print("")
    print(cups)
index_1 = cups.index(1)
cups.rotate(-1 * (index_1 + 1))
star2 = cups.popleft()
star1 = cups.popleft()
print(star1, star2)
print(star1 * star2)
