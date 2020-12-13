#428 players; last marble is worth 70825 points

players = 428
high = 70825

scores = {}
for p in range(1, players + 1):
    scores[p] = 0
marbles = {0: 0}
curr = 0
p = 1
for m in range(1, high + 1):
    if m % 10000 == 0:
        print(str(m / high * 100) + "%")
    if m % 23 == 0:
        scores[p] += m
        ind = (curr - 7) % len(marbles)
        num = marbles[ind]
        scores[p] += num
        for i in range(ind + 1, len(marbles)):
            marbles[i - 1] = marbles[i]
        del marbles[len(marbles) - 1]
        curr = ind % len(marbles)
    else:
        ind = ((curr + 1) % len(marbles)) + 1
        for i in range(ind, len(marbles) + 1):
            marbles[ind + (len(marbles) - (i))] = marbles[ind + (len(marbles) - (i + 1))]
        marbles[ind] = m
        curr = ind
    # print(curr, marbles[curr], marbles)
    p += 1
    if p == players + 1:
        p = 1

print(max([score for _, score in scores.items()]))
