input = open("input1", "r")
lines = input.readlines()
lines = [l.rstrip() for l in lines]

orbs = {}
orbits = [l.split(")") for l in lines]
for [a, b] in orbits:
    if not orbs.get(a):
        orbs[a] = []
    orbs[a].append(b)

def count(l, acc):
    counter = 0
    if orbs.get(l):
        for i in orbs[l]:
            counter += count(i, acc + 1)
        counter += acc
        return counter
    else:
        return acc


print(count("COM", 0))
