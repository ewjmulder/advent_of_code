from src.util import *

area = Parser.from_file(INPUT).to_regex_match(f"target area: x={NUMBER}..{NUMBER}, y=-{NUMBER}..-{NUMBER}", int)[0]

# print(area)

min_xx = area[0]
max_xx = area[1]
min_yy = -1 * area[2]
max_yy = -1 * area[3]
# print(min_x, max_x, min_y, max_y)

total_max_y = 0
for idx in range(1, 20):
    for idy in range(1, 1000):
        max_y = 0
        dx = idx
        dy = idy
        x = 0
        y = 0
        step = 0
        hit = False
        missed = False
        while not missed and not hit:
            step += 1
            if step == 10000:
                print("breaking")
                break
            x += dx
            y += dy
            if y > max_y:
                max_y = y
            if min_xx <= x <= max_xx and min_yy <= y <= max_yy:
                # print("hit")
                hit = True
            if y < min_yy:
                # print("miss")
                missed = True
            if dx > 0:
                dx -= 1
            dy -= 1
        if hit:
            if max_y > total_max_y:
                print("new max y:", idx, idy, max_y)
                total_max_y = max_y

print(total_max_y)

