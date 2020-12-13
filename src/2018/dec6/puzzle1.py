input = open("input1", "r")
lines = input.readlines()

curr = lines[0]
# reacted = True
# while reacted:
#     reacted = False

i = 0
while i < len(curr) - 1:
    # print(curr)
    # print(i)
    c1 = curr[i]
    c2 = curr[i + 1]
    if c1.lower() == c2.lower() and c1 != c2:
        print("removing", c1, c2)
        curr = curr[:i] + curr[i + 2:]
        if i > 0:
            i -= 1
    else:
        i += 1
    # print("")

# print(curr)
print(len(curr))
