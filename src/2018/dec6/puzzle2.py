input = open("input1", "r")
lines = input.readlines()

curr_or = lines[0]
# reacted = True
# while reacted:
#     reacted = False

min_l = 999999999
min_without = ""
for r in "abcdefghijklmnopqrstuvwxyz":
    print("trying without", r)
    curr = curr_or.replace(r, "").replace(r.upper(), "")
    i = 0
    while i < len(curr) - 1:
        # print(curr)
        # print(i)
        c1 = curr[i]
        c2 = curr[i + 1]
        if c1.lower() == c2.lower() and c1 != c2:
            curr = curr[:i] + curr[i + 2:]
            if i > 0:
                i -= 1
        else:
            i += 1
        # print("")
    length = len(curr)
    if length < min_l:
        min_l = length
        min_without = r

print(min_l)
print(min_without)
