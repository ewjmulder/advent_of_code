import sys

from src.util import *
from collections import defaultdict

lines = Parser.from_file(INPUT).to_lines()

init_p1 = int(lines[0][-1])
init_p2 = int(lines[1][-1])
print(init_p1, init_p2)

scores_per_turn = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
pos_scores = defaultdict(int)
pos_scores[(init_p1, 0, init_p2, 0)] += 1


steps = 0
while True:
    steps += 1
    done = True

    new_pos_scores_p1 = defaultdict(int)
    for (p1, s1, p2, s2), amount in pos_scores.items():
        if s1 < 21 and s2 < 21:
            done = False

            # Turn for p1
            for steps, times in scores_per_turn.items():
                new_p1 = (p1 + steps) % 10
                if new_p1 == 0:
                    new_p1 = 10
                new_s1 = s1 + new_p1
                new_pos_scores_p1[(new_p1, new_s1, p2, s2)] += times * amount
        else:
            new_pos_scores_p1[(p1, s1, p2, s2)] += amount

    new_pos_scores_p2 = defaultdict(int)
    for (p1, s1, p2, s2), amount in new_pos_scores_p1.items():
        if s1 < 21 and s2 < 21:
            done = False

            # Turn for p2
            for steps, times in scores_per_turn.items():
                new_p2 = (p2 + steps) % 10
                if new_p2 == 0:
                    new_p2 = 10
                new_s2 = s2 + new_p2
                new_pos_scores_p2[(p1, s1, new_p2, new_s2)] += times * amount
        else:
            new_pos_scores_p2[(p1, s1, p2, s2)] += amount

    pos_scores = new_pos_scores_p2
    if done:
        print("steps:", steps)
        # print(pos_scores)
        total_p1 = sum(amount for (p1, s1, p2, s2), amount in pos_scores.items() if s1 > s2)
        total_p2 = sum(amount for (p1, s1, p2, s2), amount in pos_scores.items() if s2 > s1)
        print(max(total_p1, total_p2))
        sys.exit(0)
