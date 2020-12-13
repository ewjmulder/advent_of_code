input = open("input1", "r")
lines = input.readlines()

program = [int(n) for n in lines[0].split(",")]

provide = 1

i = 0
while i < len(program):
    action = program[i]
    print("action:", action)
    if action == 99:
        break
    else:
        op_code = int(str(action)[-2:])
        param_modes = str(action)[:-2][::-1]
        print("op:", op_code)
        print("modes:", param_modes)
        if op_code == 1 or op_code == 2:
            param_mode = 0
            if len(param_modes) >= 1:
                param_mode = int(param_modes[0])
            if param_mode == 0:
                n1 = program[program[i + 1]]
            else:
                n1 = program[i + 1]

            param_mode = 0
            if len(param_modes) >= 2:
                param_mode = int(param_modes[1])
            if param_mode == 0:
                n2 = program[program[i + 2]]
            else:
                n2 = program[i + 2]
            if op_code == 1:
                print("add:", n1, n2, "store in", program[i + 3])
                program[program[i + 3]] = n1 + n2
            if op_code == 2:
                print("mul:", n1, n2, "store in", program[i + 3])
                program[program[i + 3]] = n1 * n2
            i += 4
        else:
            if op_code == 3:
                print("store:", provide, "in", program[i + 1])
                program[program[i + 1]] = provide
            if op_code == 4:
                param_mode = 0
                if len(param_modes) >= 1:
                    param_mode = int(param_modes[0])
                if param_mode == 0:
                    print("output:", program[program[i + 1]])
                else:
                    print("output:", program[i + 1])
            i += 2
    print("")

print(program)
