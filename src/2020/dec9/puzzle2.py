input = open("input1", "r")
lines = input.readlines()
lines = [int(line.rstrip()) for line in lines]

puzlen = 25

prevs = []
for i in range(0, puzlen):
    prevs.append(lines[i])

err = -1
err_pos = -1
for i in range(puzlen, len(lines)):
    next = lines[i]
    found = False
    # print("Testing", next)
    # print("prevs", prevs)
    for x in range(0, puzlen):
        for y in range(0, puzlen):
            if x != y:
                if prevs[x] + prevs[y] == next:
                    found = True
    del prevs[0]
    prevs.append(next)
    if not found:
        err = next
        err_pos = i
        break

print(err)
print(err_pos)
for i in range(0, err_pos):
    for j in range(1, err_pos):
        sub = lines[i:j]
        summed = sum(sub)
        if summed == err:
            print(sub)
            print(min(sub))
            print(max(sub))
            print(min(sub) + max(sub))
