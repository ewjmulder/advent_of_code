lines = [line.rstrip() for line in open("sample2")]

busses_raw = lines[1].split(",")
busses = []
bus_dict = {}
bus_dict_orig = {}

first = None
i = 0
for b in busses_raw:
    if b != "x":
        bb = int(b)
        busses.append(bb)
        bus_dict[bb] = (bb - i) % bb
        bus_dict_orig[bb] = i
        if not first:
            first = bb
    # else:
    #     busses.append(-1)
    i += 1

# overwrite
# bus_dict = {5: 0, 7: 1}
# first = 5

print(bus_dict_orig)
print(bus_dict)

maal = 1
for b in busses:
    maal *= b

# maxi = max(bus_dict.keys())
#
# found = False
# mul = 1
# while not found:
#     i = maxi * mul - bus_dict_orig[maxi]
#     if mul % 1000000 == 0:
#         print(i)
#     all_ok = True
#     for t in bus_dict:
#         all_ok = all_ok and (i % t == bus_dict[t])
#         if not all_ok:
#             break
#     if all_ok:
#         break
#     mul += 1


# found = False
# mul = 1
# maxi = 6545012404362376579539966834
# offset = 26681
# while not found:
#     i = offset + maxi * mul
#     if mul % 1000000 == 0:
#         print(i)
#     all_ok = True
#     for t in bus_dict:
#         all_ok = all_ok and (i % t == bus_dict[t])
#         if not all_ok:
#             # print(t)
#             break
#     if all_ok:
#         break
#     mul += 1

print("")
print("")
print(busses)

found = False
mul = 1
term = busses[0]
offset = 0
done = set()
done.add(term)
for bus in busses[1:]:
    print("finding")
    print("term:", term)
    print("offset:", offset)
    print("bus:", bus)
    print("")
    while not found:
        i = offset + term * mul
        if mul % 1000000 == 0:
            print(i)
        all_ok = True
        # for t in bus_dict:
        #     all_ok = all_ok and (t in done or (i % t == bus_dict[t]))
        #     if not all_ok:
        #         # print(t)
        #         break
        if i % bus == bus_dict[bus]:
            offset = i
            term *= bus
            mul = 1
            done.add(bus)
            print("found:", offset, term)
            break
        mul += 1

print("maal:", maal)
print("mul:", mul)
print("i:", i)
print("perc:", (i % maal))
