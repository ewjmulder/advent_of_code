input = open("input1", "r")
lines = input.readlines()

twice = 0
trice = 0
for line in lines:
    ls = set(line)
    twd = False
    trd = False
    for l in ls:
        count = line.count(l)
        # print(line)
        # print(l)
        # print(count)
        if count == 2 and not twd:
            twice += 1
            twd = True
        if count == 3 and not trd:
            trice += 1
            trd = True

print(twice * trice)
