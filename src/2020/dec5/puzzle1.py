input = open("input1", "r")
lines = input.readlines()

highest = 0
for line in lines:
    line = line.rstrip()
    fb = line[0:7]
    fb = fb.replace("F", "0")
    fb = fb.replace("B", "1")
    # print(int(fb, 2))
    lr = line[7:10]
    lr = lr.replace("L", "0")
    lr = lr.replace("R", "1")
    # print(int(lr, 2))
    id = int(fb, 2) * 8 + int(lr, 2)
    # print(id)
    if id > highest:
        highest = id

print(highest)