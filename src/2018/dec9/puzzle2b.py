#428 players; last marble is worth 70825 points

from collections import deque

players = 428
high = 708250

scores = {}
for p in range(1, players + 1):
    scores[p] = 0
marbles = deque()
marbles.append(0)
curr = 0
p = 1
for m in range(1, high + 1):
    if m % 10000 == 0:
        print(str(m / high * 100) + "%")
    if m % 23 == 0:
        scores[p] += m
        ind = (curr - 7) % len(marbles)
        val = marbles[ind]
        scores[p] += val
        del marbles[ind]
        curr = ind % len(marbles)
    else:
        ind = ((curr + 1) % len(marbles)) + 1
        marbles.insert(ind, m)
        curr = ind
    # print(curr, marbles[curr], marbles)
    p += 1
    if p == players + 1:
        p = 1

print(max([score for _, score in scores.items()]))
