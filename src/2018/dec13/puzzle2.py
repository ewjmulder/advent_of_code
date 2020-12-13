lines = [line.rstrip() for line in open("input").readlines()]

offset = 200
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
totals = []
for g in range(0, 200):
    curr_new = curr
    print(str(g) + ": " + curr)
    for i in range(2, len(curr) - 2):
        pattern = curr[i-2:i+3]
        if rules.get(pattern):
            curr_new = curr_new[0:i] + rules[pattern] + curr_new[i+1:]
        else:
            curr_new = curr_new[0:i] + "." + curr_new[i+1:]
    curr = curr_new

    total = 0
    for i in range(0, len(curr)):
        if curr[i] == "#":
            total += i - offset
    totals.append(total)

print(totals)
totals_diff = []
for i in range(0, len(totals) - 1):
    diff = totals[i + 1] - totals[i]
    totals_diff.append(diff)

print(totals_diff)
totals_d_diff = []
for i in range(0, len(totals_diff) - 1):
    d_diff = totals_diff[i + 1] - totals_diff[i]
    totals_d_diff.append(d_diff)

print(totals_d_diff)

print(totals[19])
print(totals[150])
print(totals[151])
print(totals[152])

print(totals[150] + (50000000000 - 151) * 46)
