input = open("input1", "r")
lines = input.readlines()
lines = [line.rstrip() for line in lines]

acc = 0
ptr = 0
ptrs = set()
while True:
    if ptr in ptrs:
        print(acc)
        break
    ptrs.add(ptr)
    instr = lines[ptr]
    action = instr[:3]
    print(action)
    if action == "nop":
        ptr += 1
    elif action == "acc":
        acc += int(instr[3:])
        ptr += 1
    elif action == "jmp":
        amount = int(instr[3:])
        ptr += amount
