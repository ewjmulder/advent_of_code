lines = [line.rstrip() for line in open("input").readlines()]

offset = 25
init = "." * offset + lines[0][15:] + "." * offset
rules = {}
for line in lines[2:]:
    pat = line[0:5]
    res = line[9:10]
    rules[pat] = res

print(init)
print(rules)
print("")

curr = init
pp = set()
for g in range(0, 20):
    curr_new = curr
    print(str(g) + ": " + curr)
    for i in range(2, len(curr) - 2):
        pattern = curr[i-2:i+3]
        if rules.get(pattern):
            curr_new = curr_new[0:i] + rules[pattern] + curr_new[i+1:]
            pp.add(i - offset)
        else:
            curr_new = curr_new[0:i] + "." + curr_new[i+1:]
    curr = curr_new

total = 0
for i in range(0, len(curr)):
    if curr[i] == "#":
        print("found:", i - offset)
        total += i - offset

print(total)