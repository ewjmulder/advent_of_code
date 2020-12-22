from src.util import *
from collections import deque

players_data = open(INPUT).read().split("\n\n")
player1 = deque(reversed([int(num) for num in players_data[0].split("\n")[1:]]))
player2 = deque(reversed([int(num) for num in players_data[1].split("\n")[1:]]))

print(player1)
print(player2)



def play_game(player1, player2):
    rounds = set()
    player1 = player1.copy()
    player2 = player2.copy()

    while len(player1) > 0 and len(player2) > 0:
        # print("")
        # print("Next round")
        # print(player1)
        # print(player2)

        if (tuple(player1), tuple(player2)) in rounds:
            print("END LOOP")
            return player1, player1, player2
        else:
            rounds.add((tuple(player1), tuple(player2)))


        draw1 = player1.pop()
        draw2 = player2.pop()
        # print("draws", draw1, draw2)

        if len(player1) >= draw1 and len(player2) >= draw2:
            print("SUB GAME")
            sub_winner, sub_player1, sub_player2 = play_game(deque(list(player1)[-1 * draw1:]), deque(list(player2)[-1 * draw2:]))

            if sub_winner == sub_player1:
                player1.insert(0, draw1)
                player1.insert(0, draw2)
            else:
                player2.insert(0, draw2)
                player2.insert(0, draw1)
        else:
            maxi = max([draw1, draw2])
            mini = min([draw1, draw2])
            winner = player1
            if maxi == draw2:
                winner = player2
            winner.insert(0, maxi)
            winner.insert(0, mini)
    return (player1 if len(player2) == 0 else player2), player1, player2


winner_all, player1, player2 = play_game(player1, player2)
print("")
print(player1)
print(player2)

score = 0
for i in range(0, len(winner_all)):
    num = winner_all[i]
    score += (i + 1) * num

print(score)