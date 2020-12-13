# from src.util import *

# input = open("sample")
input = open("input")
lines = input.readlines()
lines = [line.rstrip() for line in lines]

actions = [(line[0:1], line[1:]) for line in lines]

print(actions)

dirs = {}
dirs["E"] = (1, 0)
dirs["N"] = (0, -1)
dirs["S"] = (0, 1)
dirs["W"] = (-1, 0)

turn_r = "ESWN"
turn_l = "ENWS"

cur_wp = (10, -1)

cur_dir = "E"
cur_pos = (0, 0)
for a in actions:
    cur_ds = dirs[cur_dir]
    dir = a[0]
    amount = int(a[1])
    if dir == "E" or dir == "N" or dir == "S" or dir == "W":
        cur_ds = dirs[dir]
        cur_wp = (cur_wp[0] + amount * cur_ds[0], cur_wp[1] + amount * cur_ds[1])
    elif dir == "F":
        cur_pos = (cur_pos[0] + amount * cur_wp[0], cur_pos[1] + amount * cur_wp[1])
    # elif dir == "L":
    #     cur_i = turn_l.index(cur_dir)
    #     turns = int(amount / 90)
    #     cur_dir = turn_l[(cur_i + turns) % 4]
    # elif dir == "R":
    #     cur_i = turn_r.index(cur_dir)
    #     turns = int(amount / 90)
    #     cur_dir = turn_r[(cur_i + turns) % 4]
    elif dir == "L" or dir == "R":
        turns = int(amount / 90)
        if dir == "L":
            turns = -1 * turns
        turns = turns % 4
        # print(turns)
        for t in range(0, turns):
            e = -1 * cur_wp[1]
            n = cur_wp[0]
            cur_wp = (e, n)

    print(a)
    print(cur_wp)
    print(cur_pos)
    print("")


print(abs(cur_pos[0]) + abs(cur_pos[1]))
