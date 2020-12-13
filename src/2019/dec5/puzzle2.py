input = open("input1", "r")
lines = input.readlines()

program = [int(n) for n in lines[0].split(",")]

provide = 5

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
        elif op_code == 3 or op_code == 4:
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
        elif op_code == 5 or op_code == 6:
            param_mode = 0
            if len(param_modes) >= 1:
                param_mode = int(param_modes[0])
            if param_mode == 0:
                val = program[program[i + 1]]
            else:
                val = program[i + 1]

            param_mode = 0
            if len(param_modes) >= 2:
                param_mode = int(param_modes[1])
            if param_mode == 0:
                pos = program[program[i + 2]]
            else:
                pos = program[i + 2]

            if (op_code == 5 and val > 0) or (op_code == 6 and val == 0):
                i = pos
            else:
                i += 3
        else:
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

            if (op_code == 7 and n1 < n2) or (op_code == 8 and n1 == n2):
                program[program[i + 3]] = 1
            else:
                program[program[i + 3]] = 0
            i += 4

print("")

print(program)
