lines = [line.rstrip() for line in open("input")]

leave = int(lines[0])
busses_raw = lines[1].split(",")
busses = []
for b in busses_raw:
    if b != "x":
        busses.append(int(b))

print(leave)
print(busses)

b_leave = {}
for b in busses:
    t = b
    while t < leave:
        t += b
    b_leave[b] = t

print(b_leave)

lowest_t = min(b_leave.values())

the_b = [b for (b, t) in b_leave.items() if t == lowest_t][0]

print(the_b)
print(the_b * (lowest_t - leave))
