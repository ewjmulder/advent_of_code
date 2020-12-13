amount = 0
for i in range(136818, 685980):
# for i in range(136818, 136819):
    match = False
    same = False
    prev = -1
    all_ok = False
    for ds in str(i):
        # print(ds)
        d = int(ds)
        if prev == d:
            if same:
                match = False
            else:
                match = True
                same = True
        else:
            if match:
                all_ok = True
            same = False
        if prev > d:
            match = False
            all_ok = False
            break
        prev = d
    if match or all_ok:
        amount += 1

print(amount)
