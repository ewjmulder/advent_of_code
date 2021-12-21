from src.util import *

lines = Parser.from_file(INPUT).to_lines()

p1 = int(lines[0][-1])
p2 = int(lines[1][-1])
print(p1, p2)

curr = 0
total = 0
def roll():
    global curr, total
    curr += 1
    total += 1
    if curr == 101:
        curr = 1
    return curr

s1 = 0
s2 = 0


while True:
    p1 = (p1 + roll() + roll() + roll()) % 10
    if p1 == 0:
        p1 = 10
    s1 += p1
    if s1 >= 1000:
        print(s1, s2, curr, total)
        print(s2 * total)
        break
    p2 = (p2 + roll() + roll() + roll()) % 10
    if p2 == 0:
        p2 = 10
    s2 += p2
    if s2 >= 1000:
        print(s1, s2, curr, total)
        print(s1 * total)
        break