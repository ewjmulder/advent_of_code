input = open("input1", "r")
lines = input.readlines()
lines = [line.rstrip() for line in lines]


def run(program):
    acc = 0
    ptr = 0
    ptrs = set()
    while True:
        if ptr in ptrs:
            print("Loop", acc)
            return -1
        ptrs.add(ptr)
        if ptr == len(program):
            print("Correct", acc)
            return 0
        instr = program[ptr]
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


for i in range(0, len(lines)):
    program = lines.copy()
    if program[i][:3] == "nop":
        program[i] = "jmp " + program[i][3:]
    elif program[i][:3] == "jmp":
        program[i] = "nop " + program[i][3:]
    run(program)
