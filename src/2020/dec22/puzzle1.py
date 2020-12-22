from src.util import *
from collections import deque

players_data = open(INPUT).read().split("\n\n")
print(players_data)
player1 = deque(reversed([int(num) for num in players_data[0].split("\n")[1:]]))
player2 = deque(reversed([int(num) for num in players_data[1].split("\n")[1:]]))

print(player1)
print(player2)

rounds = 0
while len(player1) > 0 and len(player2) > 0:
    rounds += 1
    print("Next round")
    print(player1)
    print(player2)

    draw1 = player1.pop()
    draw2 = player2.pop()
    print("draws", draw1, draw2)
    maxi = max([draw1, draw2])
    mini = min([draw1, draw2])
    winner = player1
    if maxi == draw2:
        winner = player2
    winner.insert(0, maxi)
    winner.insert(0, mini)

print("")
print(rounds)
print(player1)
print(player2)

winner_all = player1
if len(player1) == 0:
    winner_all = player2

score = 0
for i in range(0, len(winner_all)):
    num = winner_all[i]
    score += (i + 1) * num

print(score)