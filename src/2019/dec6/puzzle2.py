input = open("input1", "r")
lines = input.readlines()
lines = [l.rstrip() for l in lines]

you = ""
san = ""
orbs = {}
orbits = [l.split(")") for l in lines]
for [a, b] in orbits:
    if b == "YOU":
        you = a
    if b == "SAN":
        san = a
    if not orbs.get(a):
        orbs[a] = []
    orbs[a].append(b)

print(you)
print(san)
print(orbs)

steps = 0
found = {you}
front = {you}
while san not in found:
    steps += 1
    new_front = set()
    for f in front:
        if orbs.get(f):
            for sub in orbs[f]:
                new_front.add(sub)
                found.add(sub)
        for o in orbs:
            if f in orbs[o]:
                new_front.add(o)
                found.add(o)
    front = new_front
print(steps)
